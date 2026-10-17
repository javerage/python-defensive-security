'use strict';
// Comprobación de navegador real (Chrome headless vía CDP) para la pantalla piloto de Partida.
//
// Motivo: dos defectos solo se observan al medir el layout real. El aviso de escena
// desbordaba el marco inferior del panel (la última línea se solapaba con el borde) y las
// vidas debían pasar de una cifra a tres corazones con posiciones estables. Ninguno de los
// dos se puede afirmar con expresiones regulares sobre el HTML.
//
// Alcance honesto: usa Chrome si está instalado; en otros equipos se omite sin fingir que
// se comprobó. No certifica accesibilidad completa, otros navegadores ni comportamiento
// responsive, ni depende de la carga de fuentes en red (el texto del aviso usa la fuente
// del sistema; se bloquean las peticiones a Google Fonts para que la medición sea estable).

const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { test, before, after } = require('node:test');

const DESIGN_DIR = path.join(__dirname, '..');
const PILOT_URL = 'file://' + path.join(DESIGN_DIR, 'playing-pilot.html');
const VIEW = { width: 1024, height: 768 };

const CHROME_CANDIDATES = [
  process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome',
  '/usr/bin/google-chrome-stable',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
].filter(Boolean);

function findChrome() {
  return CHROME_CANDIDATES.find(candidate => {
    try { return fs.statSync(candidate).isFile(); } catch { return false; }
  });
}

const CHROME = findChrome();
const skip = CHROME ? false : 'Google Chrome/Chromium no está instalado: la comprobación de navegador se omite honestamente.';

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

async function waitForDevToolsPort(profileDir, timeoutMs) {
  const file = path.join(profileDir, 'DevToolsActivePort');
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    if (fs.existsSync(file)) {
      const [port] = fs.readFileSync(file, 'utf8').split('\n');
      if (port) return Number(port);
    }
    await sleep(50);
  }
  throw new Error('Chrome no publicó DevToolsActivePort a tiempo');
}

class CDP {
  constructor(url) {
    this.id = 0;
    this.pending = new Map();
    this.waiters = new Map();
    this.ws = new WebSocket(url);
  }
  connect() {
    return new Promise((resolve, reject) => {
      this.ws.addEventListener('open', () => resolve(), { once: true });
      this.ws.addEventListener('error', event => reject(new Error(`error de WebSocket: ${event.message || 'desconocido'}`)), { once: true });
      this.ws.addEventListener('message', event => {
        const message = JSON.parse(event.data);
        if (message.id && this.pending.has(message.id)) {
          const { resolve: res, reject: rej } = this.pending.get(message.id);
          this.pending.delete(message.id);
          if (message.error) rej(new Error(`${message.error.message}`));
          else res(message.result);
        } else if (message.method && this.waiters.has(message.method)) {
          for (const handler of this.waiters.get(message.method)) handler(message.params);
        }
      });
    });
  }
  send(method, params = {}) {
    const id = this.id += 1;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }
  waitFor(method, timeoutMs) {
    return new Promise((resolve, reject) => {
      const handlers = this.waiters.get(method) || [];
      const timer = setTimeout(() => reject(new Error(`tiempo de espera agotado: ${method}`)), timeoutMs);
      handlers.push(params => { clearTimeout(timer); resolve(params); });
      this.waiters.set(method, handlers);
    });
  }
  close() {
    try { this.ws.close(); } catch { /* ya cerrado */ }
  }
}

let chrome;
let cdp;
let profileDir;

async function evaluate(expression) {
  const result = await cdp.send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  if (result.exceptionDetails) throw new Error(`evaluate falló: ${JSON.stringify(result.exceptionDetails)}`);
  return result.result.value;
}

const HEARTS_EXPR = `(() => {
  const group = document.querySelector('[data-lives-hearts]');
  if (!group) return { found: false };
  const hearts = [...group.querySelectorAll('svg.life-heart')];
  const box = element => {
    const rect = element.getBoundingClientRect();
    return { left: rect.left, top: rect.top, right: rect.right, bottom: rect.bottom, width: rect.width, height: rect.height };
  };
  const cells = [...document.querySelectorAll('.hud-cell')];
  const livesCell = cells[2].getBoundingClientRect();
  const bboxes = hearts.map(box);
  return {
    found: true,
    label: group.getAttribute('aria-label'),
    role: group.getAttribute('role'),
    count: hearts.length,
    full: hearts.filter(h => h.classList.contains('is-full')).length,
    empty: hearts.filter(h => h.classList.contains('is-empty')).length,
    hidden: hearts.map(h => h.getAttribute('aria-hidden')),
    bboxes,
    cellContainsAll: bboxes.every(b => b.left >= livesCell.left - 0.5 && b.right <= livesCell.right + 0.5 && b.top >= livesCell.top - 0.5 && b.bottom <= livesCell.bottom + 0.5),
  };
})()`;

const LAYOUT_EXPR = `(() => {
  const panel = document.querySelector('.game-panel');
  const panelRect = panel.getBoundingClientRect();
  const panelInnerBottom = panelRect.bottom - 2;
  const help = document.querySelector('.board-help').getBoundingClientRect();
  const paragraphs = [...document.querySelectorAll('.board-help p')];
  const last = paragraphs[paragraphs.length - 1];
  const range = document.createRange();
  range.selectNodeContents(last);
  const lines = [...range.getClientRects()]
    .map(rect => ({ top: rect.top, bottom: rect.bottom, left: rect.left, right: rect.right }))
    .sort((a, b) => a.top - b.top || a.left - b.left);
  const lastLine = lines[lines.length - 1];
  return {
    panelBottom: panelRect.bottom,
    panelInnerBottom,
    help: { top: help.top, bottom: help.bottom },
    lastLine,
    lastLineCount: lines.length,
    lastLineBottomToPanelInnerBottom: panelInnerBottom - lastLine.bottom,
    helpBottomToPanelInnerBottom: panelInnerBottom - help.bottom,
  };
})()`;

before(async () => {
  if (!CHROME) return;
  profileDir = fs.mkdtempSync(path.join(os.tmpdir(), 'snake-playing-browser-'));
  chrome = spawn(CHROME, [
    '--headless=new',
    '--remote-debugging-port=0',
    `--user-data-dir=${profileDir}`,
    '--no-first-run',
    '--no-default-browser-check',
    '--disable-gpu',
    '--hide-scrollbars',
    '--disable-extensions',
    'about:blank',
  ], { stdio: ['ignore', 'ignore', 'ignore'] });

  const port = await waitForDevToolsPort(profileDir, 20000);
  const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
  const page = targets.find(target => target.type === 'page');
  assert.ok(page && page.webSocketDebuggerUrl, 'Chrome no expuso una pestaña depurable');

  cdp = new CDP(page.webSocketDebuggerUrl);
  await cdp.connect();
  await cdp.send('Page.enable');
  await cdp.send('Runtime.enable');
  await cdp.send('Network.enable');
  await cdp.send('Network.setBlockedURLs', { urls: ['*fonts.googleapis.com*', '*fonts.gstatic.com*'] });
  await cdp.send('Emulation.setDeviceMetricsOverride', { width: VIEW.width, height: VIEW.height, deviceScaleFactor: 1, mobile: false });
  const loaded = cdp.waitFor('Page.loadEventFired', 20000);
  await cdp.send('Page.navigate', { url: PILOT_URL });
  await loaded;
  await sleep(300);
});

after(async () => {
  if (cdp) cdp.close();
  if (chrome) {
    const exited = new Promise(resolve => chrome.once('exit', resolve));
    chrome.kill('SIGKILL');
    await Promise.race([exited, sleep(3000)]);
  }
  if (profileDir) {
    // Chrome puede tardar en soltar el perfil recién eliminado; se reintenta sin dejar restos.
    for (let attempt = 0; attempt < 10; attempt += 1) {
      try {
        fs.rmSync(profileDir, { recursive: true, force: true, maxRetries: 2, retryDelay: 50 });
        return;
      } catch {
        await sleep(200);
      }
    }
  }
});

test('los corazones de vidas se renderizan dentro de la columna VIDAS', { skip, timeout: 30000 }, async () => {
  const m = await evaluate(HEARTS_EXPR);
  assert.equal(m.found, true, 'el grupo de vidas existe en el DOM');
  assert.equal(m.role, 'img', 'el grupo se expone como imagen accesible');
  assert.equal(m.label, '3 de 3 vidas disponibles', 'etiqueta accesible del grupo');
  assert.equal(m.count, 3, 'tres iconos de corazón');
  assert.equal(m.full, 3, 'inicialmente tres corazones llenos');
  assert.equal(m.empty, 0, 'sin corazones vacíos en el estado inicial');
  assert.deepEqual(m.hidden, ['true', 'true', 'true'], 'cada icono es decorativo');
  assert.equal(new Set(m.bboxes.map(b => `${b.width}x${b.height}`)).size, 1, 'tamaño consistente entre iconos');
  assert.equal(m.cellContainsAll, true, 'los tres iconos caben en la columna de vidas');
  for (let i = 1; i < m.bboxes.length; i += 1) {
    assert.ok(m.bboxes[i].left > m.bboxes[i - 1].left, 'los corazones se alinean de izquierda a derecha');
  }
});

test('el estado vacío conserva las tres posiciones y se distingue por contorno', { skip, timeout: 30000 }, async () => {
  const beforeState = await evaluate(HEARTS_EXPR);
  const simulated = await evaluate(`(() => {
    const group = document.querySelector('[data-lives-hearts]');
    const hearts = [...group.querySelectorAll('svg.life-heart')];
    hearts[0].classList.remove('is-full');
    hearts[0].classList.add('is-empty');
    const box = element => {
      const rect = element.getBoundingClientRect();
      return { left: rect.left, top: rect.top, right: rect.right, bottom: rect.bottom, width: rect.width, height: rect.height };
    };
    const after = hearts.map(box);
    const style = getComputedStyle(hearts[0].querySelector('path'));
    const result = { after, fill: style.fill, stroke: style.stroke, strokeWidth: style.strokeWidth };
    // Restauración: la simulación no deja ningún estado de demostración en el documento.
    hearts[0].classList.remove('is-empty');
    hearts[0].classList.add('is-full');
    return result;
  })()`);
  assert.deepEqual(simulated.after, beforeState.bboxes, 'las tres posiciones no cambian al vaciar un corazón');
  assert.ok(simulated.fill === 'none' || /rgba\(0,\s*0,\s*0,\s*0\)/.test(simulated.fill), 'el corazón vacío no está relleno');
  assert.notEqual(simulated.stroke, 'none', 'el corazón vacío dibuja contorno');
  assert.ok(Number.parseFloat(simulated.strokeWidth) > 0, 'el contorno tiene grosor visible');
});

test('la última línea del aviso queda dentro del panel con holgura positiva', { skip, timeout: 30000 }, async () => {
  const m = await evaluate(LAYOUT_EXPR);
  assert.equal(m.lastLineCount, 1, 'el aviso de escena ocupa una sola línea');
  assert.ok(m.lastLine.bottom <= m.panelInnerBottom, `la última línea se solapa con el marco inferior (${m.lastLine.bottom} > ${m.panelInnerBottom})`);
  assert.ok(m.lastLineBottomToPanelInnerBottom >= 4, `holgura insuficiente bajo la última línea: ${m.lastLineBottomToPanelInnerBottom}px`);
  assert.ok(m.help.bottom <= m.panelInnerBottom + 0.5, `la caja de ayuda rebasa el panel (${m.help.bottom} > ${m.panelInnerBottom})`);
});

test('la pantalla de referencia 1024 × 768 encaja en la ventana', { skip, timeout: 30000 }, async () => {
  const m = await evaluate(`(() => {
    const rect = document.querySelector('.pilot-screen').getBoundingClientRect();
    return { left: rect.left, top: rect.top, width: rect.width, height: rect.height, vw: window.innerWidth, vh: window.innerHeight };
  })()`);
  assert.equal(m.width, 1024, 'ancho de referencia');
  assert.equal(m.height, 768, 'alto de referencia');
  assert.ok(m.left >= 0 && m.top >= 0, 'el marco no sale por arriba ni por la izquierda');
  assert.ok(m.left + m.width <= m.vw + 0.5, 'el marco no se recorta por la derecha');
  assert.ok(m.top + m.height <= m.vh + 0.5, 'el marco no se recorta por abajo');
});
