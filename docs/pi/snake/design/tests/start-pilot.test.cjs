const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const DESIGN_DIR = path.join(__dirname, '..');
const PILOT_PATH = path.join(DESIGN_DIR, 'start-pilot.html');

// Tokens tomados literalmente de visual-style.md (11 valores propuestos, sin aprobar).
const TOKENS = [
  ['background', '#0D1117'],
  ['surface', '#161B22'],
  ['board', '#0B1014'],
  ['text', '#F0F6FC'],
  ['text-muted', '#A9B4C0'],
  ['border', '#8B949E'],
  ['grid', '#22303A'],
  ['snake', '#7EE787'],
  ['food', '#FF7B72'],
  ['accent', '#79C0FF'],
  ['focus', '#F2CC60'],
];

function pilot() {
  return fs.readFileSync(PILOT_PATH, 'utf8');
}

function cssBlock(html, selector) {
  const start = html.indexOf(`${selector} {`);
  assert.notEqual(start, -1, `falta la regla CSS ${selector}`);
  const open = html.indexOf('{', start);
  const close = html.indexOf('}', open);
  assert.notEqual(close, -1, `la regla ${selector} no cierra`);
  return html.slice(open + 1, close);
}

test('define los 11 tokens semánticos exactos de visual-style.md', () => {
  const html = pilot();
  const declared = [...html.matchAll(/--color-([a-z-]+)\s*:/g)].map(match => match[1]);
  assert.deepEqual(declared.sort(), TOKENS.map(([name]) => name).sort());
  for (const [name, hex] of TOKENS) {
    assert.match(html, new RegExp(`--color-${name}\\s*:\\s*${hex}`, 'i'), `falta --color-${name}: ${hex}`);
  }
});

test('reproduce la referencia 1024 × 768 con el panel central aprobado', () => {
  const html = pilot();
  const screen = cssBlock(html, '.pilot-screen');
  assert.match(screen, /width:\s*1024px/);
  assert.match(screen, /height:\s*768px/);

  const panel = cssBlock(html, '.game-panel');
  assert.match(panel, /position:\s*absolute/);
  assert.match(panel, /left:\s*112px/);
  assert.match(panel, /top:\s*80px/);
  assert.match(panel, /width:\s*800px/);
  assert.match(panel, /height:\s*600px/);
  assert.match(panel, /background:\s*var\(--color-surface\)/, 'el panel es carbón (surface)');

  // Cajas aprobadas del wireframe: campo 360 × 48 y botón 200 × 56.
  const field = cssBlock(html, '.name-field');
  assert.match(field, /width:\s*360px/);
  assert.match(field, /height:\s*48px/);
  const button = cssBlock(html, '.btn');
  assert.match(button, /width:\s*200px/);
  assert.match(button, /height:\s*56px/);

  assert.match(html, /<meta name="viewport"/, 'la vista puede desplazarse en ventanas pequeñas');
  assert.doesNotMatch(cssBlock(html, 'body'), /overflow:\s*hidden/, 'el body no recorta la pantalla de referencia');
});

test('usa controles nativos: nombre etiquetado y vacío, y botón type=button con la etiqueta exacta play', () => {
  const html = pilot();
  assert.doesNotMatch(html, /<form\b/i);
  assert.doesNotMatch(html, /type="submit"/);

  assert.match(
    html,
    /<label[^>]*class="field-label"[^>]*for="player-name"[^>]*>Nombre del jugador \(opcional\)<\/label>/,
  );
  assert.match(html, /<input[^>]*class="name-field"[^>]*type="text"[^>]*id="player-name"/);

  const input = html.match(/<input[^>]*id="player-name"[^>]*>/)[0];
  assert.doesNotMatch(input, /\bvalue="/, 'el campo de nombre empieza vacío');
  assert.doesNotMatch(input, /\breadonly\b/);
  assert.doesNotMatch(input, /\bdisabled\b/);

  const buttons = [...html.matchAll(/<button\b[^>]*>([\s\S]*?)<\/button>/g)];
  assert.equal(buttons.length, 1, 'solo se permite el botón play');
  const button = html.match(/<button\b[^>]*id="play-button"[^>]*>/)[0];
  assert.match(button, /type="button"/);
  assert.equal(buttons[0][1].trim(), 'play', 'la etiqueta visible del botón es exactamente «play»');
});

test('no añade lógica de juego, atajos, generación de nombres ni navegación', () => {
  const html = pilot();
  assert.doesNotMatch(html, /addEventListener/);
  assert.doesNotMatch(html, /keydown|keyup|keypress/i);
  assert.doesNotMatch(html, /setInterval|requestAnimationFrame/);
  assert.doesNotMatch(html, /localStorage|sessionStorage|fetch\(|XMLHttpRequest/);
  assert.doesNotMatch(html, /window\.location|location\.href|location\.assign|location\.replace/);
  assert.doesNotMatch(html, /\.value\s*=/, 'ningún script escribe en el campo: el texto se conserva');
  assert.doesNotMatch(html, /onclick|onkeydown|onsubmit/i);

  const script = html.match(/<script id="pilot-font-status">([\s\S]*?)<\/script>/)[1];
  assert.doesNotMatch(script, /player_/, 'el script no genera nombres; la instrucción es solo texto');
  assert.match(html, /player_YYYYMMDD_HHmmss_SSS/, 'la instrucción de generación sigue presente como texto');
});

test('aplica los roles tipográficos: Silkscreen en título y botón, sistema en nombre e instrucciones', () => {
  const html = pilot();
  assert.match(cssBlock(html, '.game-title'), /font-family:\s*var\(--font-pixel\)/);
  assert.match(cssBlock(html, '.game-title'), /font-size:\s*24px/);
  assert.match(cssBlock(html, '.btn'), /font-family:\s*var\(--font-pixel\)/);
  assert.match(cssBlock(html, '.btn'), /font-size:\s*16px/);
  assert.match(cssBlock(html, '.name-field'), /font-family:\s*var\(--font-body\)/);
  assert.match(cssBlock(html, '.field-label'), /font-family:\s*var\(--font-body\)/);
  assert.match(cssBlock(html, 'body'), /font-family:\s*var\(--font-body\)/, 'nombre e instrucciones usan la fuente del sistema');
});

test('usa los estados acordados de botón con inversión y foco exterior separado', () => {
  const html = pilot();

  const base = cssBlock(html, '.btn');
  assert.match(base, /background:\s*var\(--color-snake\)/);
  assert.match(base, /color:\s*var\(--color-background\)/);
  assert.match(base, /border-radius:\s*var\(--radius\)/);

  const hover = cssBlock(html, '.btn:hover');
  assert.match(hover, /background:\s*var\(--color-background\)/);
  assert.match(hover, /color:\s*var\(--color-snake\)/);
  assert.match(hover, /border-color:\s*var\(--color-snake\)/);
  assert.doesNotMatch(hover, /color:\s*var\(--color-background\)/, 'nunca texto carbón sobre relleno carbón');

  const active = cssBlock(html, '.btn:active');
  assert.match(active, /background:\s*var\(--color-background\)/);
  assert.match(active, /color:\s*var\(--color-snake\)/);
  assert.match(active, /box-shadow:\s*inset/);
  assert.doesNotMatch(active, /(?:transform|translate|margin|padding|top|left):/, 'la pulsación no desplaza la caja');

  const focus = cssBlock(html, '.btn:focus-visible');
  assert.match(focus, /outline:\s*var\(--border-w\)\s+solid\s+var\(--color-focus\)/);
  assert.match(focus, /outline-offset:\s*2px/);
  assert.match(focus, /box-shadow:\s*0 0 0 2px var\(--color-background\)/);

  const both = cssBlock(html, '.btn:active:focus-visible');
  assert.match(both, /inset/);
  assert.match(both, /0 0 0 2px var\(--color-background\)/);
});

test('campo y botón usan radio de 8 px y foco dorado con hueco real de 2 px', () => {
  const html = pilot();
  assert.match(cssBlock(html, ':root'), /--radius:\s*8px/);
  assert.match(cssBlock(html, '.name-field'), /border-radius:\s*var\(--radius\)/);
  assert.match(cssBlock(html, '.name-field'), /background:\s*var\(--color-surface\)/);
  assert.match(cssBlock(html, '.name-field'), /border:\s*var\(--border-w\)\s+solid\s+var\(--color-border\)/);

  const focus = cssBlock(html, '.name-field:focus-visible');
  assert.match(focus, /outline:\s*var\(--border-w\)\s+solid\s+var\(--color-focus\)/);
  assert.match(focus, /outline-offset:\s*2px/);
  assert.match(focus, /box-shadow:\s*0 0 0 2px var\(--color-background\)/, 'el hueco de 2 px es fondo real');

  assert.doesNotMatch(cssBlock(html, '.game-panel'), /border-radius/, 'el panel conserva su geometría recta');
});

test('recibe el foco de entrada sin retenerlo y permite salir con Tab', () => {
  const html = pilot();
  const input = html.match(/<input[^>]*id="player-name"[^>]*>/)[0];
  assert.match(input, /autofocus\b/, 'el foco de entrada se modela con autofocus nativo');
  assert.doesNotMatch(input, /tabindex="-[0-9]/);

  assert.doesNotMatch(html, /addEventListener/);
  assert.doesNotMatch(html, /\.focus\(\)/, 'ningún script atrapa el foco');
  assert.match(html, /Tab permite pasar a «play»/);
  assert.match(html, /<button\b[^>]*id="play-button"[^>]*>/);
});

test('limita las referencias externas a la familia seleccionada de Google Fonts', () => {
  const html = pilot();
  const resources = [...html.matchAll(/(?:href|src)="([^"]+)"/g)].map(match => match[1]);
  const remote = resources.filter(value => /^https?:/.test(value));
  assert.equal(remote.length, 1, 'solo se permite la hoja de Google Fonts');

  const url = new URL(remote[0].replaceAll('&amp;', '&'));
  assert.equal(url.origin, 'https://fonts.googleapis.com');
  assert.equal(url.pathname, '/css2');
  assert.deepEqual(url.searchParams.getAll('family'), ['Silkscreen:wght@400;700']);
  assert.equal(url.searchParams.get('display'), 'swap');

  assert.match(html, /referrerpolicy="no-referrer"/);
  assert.doesNotMatch(html, /fonts\.gstatic\.com/);
  assert.doesNotMatch(html, /Pixelify Sans|Press Start 2P/);
});

test('solo ejecuta la comprobación de carga con FontFaceSet, sin src ni otra lógica', () => {
  const html = pilot();
  const scripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)];
  assert.equal(scripts.length, 1);
  assert.match(scripts[0][1], /id="pilot-font-status"/);
  assert.doesNotMatch(scripts[0][1], /\bsrc=/);
  assert.match(scripts[0][2], /document\.fonts\.load/);
  assert.doesNotMatch(html, /addEventListener/);
});

async function fontStatusHarness({ outcome = 'loaded', api = true } = {}) {
  const script = pilot().match(/<script id="pilot-font-status">([\s\S]*?)<\/script>/);
  assert.ok(script, 'falta la comprobación de carga real');
  const requests = [];
  const timers = new Map();
  const status = { hidden: false, dataset: {}, textContent: 'Sin comprobar' };
  const fonts = api ? {
    load(font, text) {
      requests.push({ font, text });
      if (outcome === 'rejected') return Promise.reject(new Error('blocked'));
      if (outcome === 'timeout') return new Promise(() => {});
      if (outcome === 'empty') return Promise.resolve([]);
      if (outcome === 'partial') {
        const isFirstWeight = requests.length === 1;
        return Promise.resolve(isFirstWeight ? [{}] : []);
      }
      return Promise.resolve([{}]);
    },
  } : undefined;

  vm.runInNewContext(script[1], {
    document: {
      fonts,
      querySelector(selector) {
        assert.equal(selector, '[data-font-status]');
        return status;
      },
    },
    setTimeout(callback, delay) {
      assert.equal(delay, 10000);
      const id = timers.size + 1;
      timers.set(id, callback);
      return id;
    },
    clearTimeout(id) { timers.delete(id); },
  });

  if (api) assert.equal(status.dataset.fontState, 'loading');
  if (outcome === 'timeout') for (const callback of [...timers.values()]) callback();
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(timers.size, 0, 'la comprobación no deja temporizadores pendientes');
  return { status, requests };
}

test('comprueba ambos pesos reales y solo marca cargada con caras no vacías, ocultando el aviso', async () => {
  const { status, requests } = await fontStatusHarness();
  assert.deepEqual(requests.map(request => request.font), ['400 16px "Silkscreen"', '700 24px "Silkscreen"']);
  for (const { text } of requests) assert.match(text, /á é í ó ú ñ ü ¿ ¡/);
  assert.equal(status.dataset.fontState, 'loaded');
  assert.equal(status.hidden, true, 'el aviso de éxito se oculta para conservar «solo pantalla»');
  assert.match(status.textContent, /cargada/);
});

for (const outcome of ['rejected', 'empty', 'timeout', 'partial']) {
  test(`advierte del sustituto cuando la carga falla: ${outcome}`, async () => {
    const { status } = await fontStatusHarness({ outcome });
    assert.equal(status.dataset.fontState, 'failed');
    assert.equal(status.hidden, false, 'el aviso de fallo permanece visible');
    assert.match(status.textContent, /sustituto/i);
    assert.match(status.textContent, /no lo juzgues/i);
  });
}

test('sin API de fuentes no presenta el sustituto como la fuente real', async () => {
  const { status, requests } = await fontStatusHarness({ api: false });
  assert.equal(requests.length, 0);
  assert.equal(status.dataset.fontState, 'unavailable');
  assert.match(status.textContent, /No se puede comprobar/i);
});

test('explica el comportamiento solo con el texto aprobado del wireframe', () => {
  const html = pilot();
  for (const text of [
    'INICIO · AwaitingStart',
    'SNAKE',
    'Pantalla de inicio · el jugador aún no inicia el movimiento',
    'Nombre del jugador (opcional)',
    'Si se deja vacío, al iniciar se genera player_YYYYMMDD_HHmmss_SSS.',
    'Activa «play» o pulsa Enter desde el campo de nombre para iniciar.',
    'Puedes escribir «dark angel»: sus espacios no inician la partida.',
    'Foco en el nombre en cada entrada al inicio; Tab permite pasar a «play».',
  ]) {
    assert.ok(html.includes(text), `falta el texto aprobado: ${text}`);
  }
  assert.match(html, /[áéíóúñü¿¡«»…]/, 'conserva los caracteres españoles');
});

test('se presenta como referencia visual aceptada y no añade pantallas ni galería de componentes', () => {
  const html = pilot();
  assert.match(html, /piloto/i);
  assert.match(html, /referencia visual aceptada/i);
  assert.match(html, /sin jugabilidad/i);
  const title = html.match(/<title>([^<]*)<\/title>/)[1];
  assert.match(title, /referencia visual aceptada/i, 'la aceptación de Inicio ya no deja el piloto marcado como sin aprobar');
  assert.doesNotMatch(title, /sin aprobar/i);
  assert.match(html, /<noscript>/);
  assert.doesNotMatch(html, /<table/);
  assert.doesNotMatch(html, /class="[^"]*\bboard\b/);
});

// Corrección 1: el encabezado visible no puede heredar la anotación de wireframe aprobado.
test('el encabezado visible marca la referencia visual aceptada y sin jugabilidad', () => {
  const html = pilot();
  const note = html.match(/<span class="panel-note">([^<]*)<\/span>/);
  assert.ok(note, 'falta la nota del panel');
  assert.match(note[1], /referencia visual aceptada/i);
  assert.match(note[1], /sin jugabilidad/i);
  assert.doesNotMatch(html, /propuesta — aprobada/, 'no debe heredar la anotación exacta del wireframe aprobado');
});

// Corrección 2: la envoltura del aviso no deja espacio vertical cuando la carga se confirma.
test('la envoltura del aviso no deja espacio vertical con el aviso oculto', () => {
  const html = pilot();
  const wrapper = cssBlock(html, '.page-note');
  assert.match(wrapper, /padding:\s*0 24px/, 'la envoltura solo aporta relleno horizontal');
  assert.doesNotMatch(wrapper, /padding-(top|bottom)/, 'sin relleno vertical residual');
  assert.doesNotMatch(wrapper, /padding:\s*[1-9]\d*px/, 'sin relleno vertical residual');
  assert.match(cssBlock(html, '.font-status'), /margin:\s*[^;]*[1-9]/, 'el espaciado pasa al aviso visible');
  assert.match(cssBlock(html, '.font-status[hidden]'), /display:\s*none/);
});
