const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const DESIGN_DIR = path.join(__dirname, '..');
const SHEET_PATH = path.join(DESIGN_DIR, 'style-sheet.html');

// Tokens tomados literalmente de visual-style.md (11 valores propuestos).
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
const REVIEW_IDS = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6'];

function sheet() {
  return fs.readFileSync(SHEET_PATH, 'utf8');
}

function sectionBody(html, id) {
  const start = html.indexOf(`id="${id}"`);
  assert.notEqual(start, -1, `falta la sección de revisión ${id}`);
  const end = html.indexOf('</section>', start);
  assert.notEqual(end, -1, `la sección ${id} no cierra`);
  return html.slice(start, end);
}

function cssBlock(html, selector) {
  const start = html.indexOf(`${selector} {`);
  assert.notEqual(start, -1, `falta la regla CSS ${selector}`);
  const open = html.indexOf('{', start);
  const close = html.indexOf('}', open);
  assert.notEqual(close, -1, `la regla ${selector} no cierra`);
  return html.slice(open + 1, close);
}

test('define los 11 tokens de color como custom properties compartidas', () => {
  const html = sheet();
  const declared = [...html.matchAll(/--color-([a-z-]+)\s*:/g)].map(match => match[1]);
  assert.deepEqual(declared.sort(), TOKENS.map(([name]) => name).sort());
  for (const [name, hex] of TOKENS) {
    assert.match(html, new RegExp(`--color-${name}\\s*:\\s*${hex}`, 'i'), `falta --color-${name}: ${hex}`);
  }
});

test('cada muestra de color declara token, hex y uso semántico', () => {
  const body = sectionBody(sheet(), 'V1');
  for (const [name, hex] of TOKENS) {
    assert.match(body, new RegExp(`data-token="${name}"`), `falta la muestra del token ${name}`);
    assert.match(body, new RegExp(hex, 'i'), `falta el hex ${hex}`);
  }
  for (const usage of [/Fondo general/i, /Serpiente/i, /Comida/i, /Acentos/i, /Contorno de foco/i]) {
    assert.match(body, usage);
  }
});

test('incluye especímenes de títulos, cifras, instrucciones acentuadas y «dark angel»', () => {
  const body = sectionBody(sheet(), 'V2');
  assert.match(body, /class="[^"]*\btype-pixel\b/);
  assert.match(body, /class="[^"]*\btype-body\b/);
  assert.match(body, /dark angel/);
  assert.match(body, /\d{3,}/);
  assert.match(body, /[áéíóúñ¿¡…«»]/);
  assert.match(body, /instrucciones/i);
});

test('marca la tipografía pixelada como Silkscreen seleccionada con integración local pendiente', () => {
  const body = sectionBody(sheet(), 'V2');
  const start = body.indexOf('id="V2-fallback-nota"');
  assert.notEqual(start, -1, 'falta la nota de la fuente seleccionada');
  const note = body.slice(start, body.indexOf('</p>', start));
  assert.match(note, /seleccionad/i);
  assert.match(note, /Silkscreen/);
  assert.match(note, /integraci[oó]n local/i);
  assert.match(note, /pendiente/i);
  assert.match(note, /OFL/);
  assert.match(note, /sustituto/i, 'la hoja debe advertir del sustituto si falla la carga remota');
});

test('usa controles nativos: campo de texto etiquetado y botones type=button', () => {
  const body = sectionBody(sheet(), 'V3');
  assert.match(body, /<input[^>]*type="text"/);
  assert.match(body, /<label[^>]*for="nombre-ejemplo"[^>]*>/);
  assert.match(body, /id="nombre-ejemplo"/);
  const buttons = [...body.matchAll(/<button\b[^>]*>/g)].map(match => match[0]);
  assert.ok(buttons.length >= 2, 'se esperaban al menos dos botones de muestra');
  for (const button of buttons) {
    assert.match(button, /type="button"/);
    assert.match(button, /class="btn"/, 'los dos botones usan el mismo tratamiento propuesto');
  }
  assert.doesNotMatch(sheet(), /type="submit"/);
});

test('solo ejecuta el aviso de fuentes, sin formulario, atajos globales ni lógica de juego', () => {
  const html = sheet();
  assert.doesNotMatch(html, /<form\b/i);
  const scripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)];
  assert.equal(scripts.length, 1);
  assert.match(scripts[0][1], /id="selected-font-status"/);
  assert.doesNotMatch(scripts[0][1], /\bsrc=/);
  assert.match(scripts[0][2], /document\.fonts\.load/);
  assert.doesNotMatch(html, /addEventListener/);
  assert.doesNotMatch(html, /setInterval|requestAnimationFrame/);
  assert.doesNotMatch(html, /autofocus/i);
  assert.doesNotMatch(html, /contenteditable/i);
  assert.doesNotMatch(html, /localStorage|sessionStorage|fetch\(|XMLHttpRequest/);
  assert.doesNotMatch(html, /keydown|keyup|keypress/i);
});

test('documenta hover, active, focus-visible y deshabilitado con ejemplos rotulados', () => {
  const html = sheet();
  assert.match(html, /:hover/);
  assert.match(html, /:active/);
  assert.match(html, /:focus-visible/);
  assert.match(html, /outline:\s*(?:2px|var\(--border-w\))\s+solid\s+var\(--color-focus\)/);
  const body = sectionBody(html, 'V3');
  for (const cls of ['is-hover', 'is-active', 'is-focus', 'is-disabled']) {
    assert.match(body, new RegExp(cls), `falta el estado estático ${cls}`);
  }
  for (const label of [/hover/i, /pulsad|active/i, /foco|focus/i, /deshabilitad|disabled/i]) {
    assert.match(body, label);
  }
});

test('ilustra un tablero con serpiente, cabeza diferenciada, comida rombo y muros con trama', () => {
  const html = sheet();
  const board = sectionBody(html, 'V4');
  assert.match(board, /class="[^"]*\bv4-board\b/);
  assert.match(board, /class="[^"]*\bsnake-head\b/);
  assert.match(board, /class="[^"]*\bfood\b/);
  assert.match(board, /class="[^"]*\bwall\b/);
  const cells = [...board.matchAll(/data-cell="(\d+),(\d+)"/g)].map(match => `${match[1]},${match[2]}`);
  assert.ok(cells.length >= 6, 'el tablero debe colocar varias piezas');
  assert.equal(new Set(cells).size, cells.length, 'las piezas del tablero no deben solaparse');
  assert.match(html, /\.food\s*\{[^}]*clip-path:\s*polygon/);
  assert.match(html, /repeating-linear-gradient/);
  assert.match(board, /grid-area/);
});

test('muestra un HUD y un fragmento de ranking con datos ficticios', () => {
  const body = sectionBody(sheet(), 'V5');
  for (const label of ['JUGADOR', 'PUNTAJE', 'VIDAS', 'NIVEL', 'VELOCIDAD']) {
    assert.match(body, new RegExp(label, 'i'));
  }
  assert.match(body, /<table/);
  for (const name of ['Ada_88', 'SnakeMaster', 'nori_7']) {
    assert.match(body, new RegExp(name));
  }
  assert.match(body, /ilustrativ|fictici|no son rankings reales/i);
});

test('incluye acentos breves de Game Over y victoria sin acciones nuevas', () => {
  const html = sheet();
  const body = sectionBody(html, 'V6');
  assert.match(body, /result-gameover/);
  assert.match(body, /result-victory/);
  assert.match(body, /GAME OVER/i);
  assert.match(body, /victoria/i);
  assert.doesNotMatch(body, /<button/);
  assert.doesNotMatch(body, /<a\b/);
  assert.match(html, /var\(--color-food\)/);
  assert.match(html, /var\(--color-snake\)/);
});

test('organiza secciones de revisión con ids estables y preguntas de retroalimentación', () => {
  const html = sheet();
  for (const id of REVIEW_IDS) {
    const body = sectionBody(html, id);
    assert.match(body, /class="[^"]*review-prompt/, `la sección ${id} no tiene bloque de preguntas`);
    assert.match(body, /Qu[eé] revisar/i, `la sección ${id} no indica qué revisar`);
    assert.match(body, /propuesta/i, `la sección ${id} no declara la propuesta`);
    assert.match(body, /ajuste/i, `la sección ${id} no pide el ajuste a describir`);
  }
  const ids = [...html.matchAll(/data-review-section="([^"]+)"/g)].map(match => match[1]);
  assert.deepEqual(ids.sort(), [...REVIEW_IDS].sort());
});

test('mantiene navegación local y limita las referencias externas a Google Fonts', () => {
  const html = sheet();
  const resources = [...html.matchAll(/(?:href|src)="([^"]+)"/g)].map(match => match[1]);
  const remote = resources.filter(value => /^https?:/.test(value));
  assert.equal(remote.length, 1, 'solo se permite la hoja de Google Fonts');
  const url = new URL(remote[0].replaceAll('&amp;', '&'));
  assert.equal(url.origin, 'https://fonts.googleapis.com');
  assert.equal(url.pathname, '/css2');
  assert.deepEqual(url.searchParams.getAll('family'), ['Silkscreen:wght@400;700']);
  assert.equal(url.searchParams.get('display'), 'swap');
  for (const value of resources) {
    if (remote.includes(value)) continue;
    assert.match(value, /^(?:#[\w-]*|\.{0,2}\/?[\w./-]+)$/, `recurso no local: ${value}`);
  }
  for (const target of ['README.md', 'index.html', 'visual-style.md']) {
    assert.ok(resources.includes(target), `falta el enlace a ${target}`);
  }
  for (const id of REVIEW_IDS) {
    assert.ok(resources.includes(`#${id}`), `falta el ancla #${id}`);
  }
});

test('muestra la fuente seleccionada con textos y tamaños equivalentes y avisos de conexión', () => {
  const html = sheet();
  const body = sectionBody(html, 'V2');
  const selected = [...body.matchAll(/<article\b[^>]*data-font-selected="([^"]+)"[^>]*>([\s\S]*?)<\/article>/g)];
  assert.deepEqual(selected.map(match => match[1]), ['Silkscreen']);
  const content = selected[0][2];
  assert.match(content, /data-font-status[^>]*role="status"/);
  assert.match(content, /Sin comprobar/);
  const sample = content.match(/<div class="font-examples">([\s\S]*?)<\/div>/);
  assert.ok(sample);
  for (const text of ['SNAKE', 'Nueva partida', '0123456789', 'dark angel', 'á é í ó ú ñ ü ¿ ¡']) assert.ok(sample[1].includes(text));
  assert.match(cssBlock(html, '.font-examples'), /font-synthesis:\s*none/);
  assert.match(cssBlock(html, '.font-title'), /font-size:\s*24px/);
  assert.match(cssBlock(html, '.font-examples .btn'), /font-family:\s*inherit/);
  assert.match(body, /conexi[oó]n/i);
  assert.match(body, /solicitudes a Google/i);
  assert.match(body, /integraci[oó]n local/i);
  assert.doesNotMatch(html, /Pixelify Sans|Press Start 2P/, 'las candidatas descartadas no deben aparecer en la hoja');
  assert.match(body, /<noscript>/);
  assert.match(html, /referrerpolicy="no-referrer"/);
  assert.doesNotMatch(html, /Sin recursos externos|sin formulario ni JavaScript|no pide red/i);
});

async function fontStatusHarness({ outcome = 'loaded', api = true } = {}) {
  const script = sheet().match(/<script id="selected-font-status">([\s\S]*?)<\/script>/);
  assert.ok(script, 'falta la comprobación de carga real');
  const requests = [];
  const timers = new Map();
  const cards = ['Silkscreen'].map(family => ({
    dataset: { fontSelected: family },
    status: { textContent: 'Sin comprobar' },
    querySelector(selector) { assert.equal(selector, '[data-font-status]'); return this.status; },
  }));
  const fonts = api ? { load(font, text) {
    requests.push({ font, text });
    if (outcome === 'rejected') return Promise.reject(new Error('blocked'));
    if (outcome === 'timeout') return new Promise(() => {});
    return Promise.resolve(outcome === 'empty' ? [] : [{}]);
  } } : undefined;
  vm.runInNewContext(script[1], {
    document: { fonts, querySelectorAll(selector) { assert.equal(selector, '[data-font-selected]'); return cards; } },
    setTimeout(callback, delay) { assert.equal(delay, 10000); const id = timers.size + 1; timers.set(id, callback); return id; },
    clearTimeout(id) { timers.delete(id); },
  });
  if (api) for (const card of cards) assert.equal(card.dataset.fontState, 'loading');
  if (outcome === 'timeout') for (const callback of [...timers.values()]) callback();
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(timers.size, 0, 'las comprobaciones no dejan temporizadores pendientes');
  return { cards, requests };
}

test('solo marca cargada la fuente seleccionada cuando FontFaceSet devuelve caras reales', async () => {
  const { cards, requests } = await fontStatusHarness();
  assert.deepEqual(requests.map(request => request.font), [
    `400 16px "${cards[0].dataset.fontSelected}"`,
    `700 24px "${cards[0].dataset.fontSelected}"`,
  ]);
  for (const { text } of requests) assert.match(text, /á é í ó ú ñ ü ¿ ¡/);
  for (const card of cards) {
    assert.equal(card.dataset.fontState, 'loaded');
    assert.match(card.status.textContent, /cargada/);
  }
});

for (const outcome of ['rejected', 'empty', 'timeout']) {
  test(`advierte del sustituto si la carga falla: ${outcome}`, async () => {
    const { cards } = await fontStatusHarness({ outcome });
    for (const card of cards) {
      assert.equal(card.dataset.fontState, 'failed');
      assert.match(card.status.textContent, /sustituto/i);
      assert.match(card.status.textContent, /no conf[ií]es/i);
    }
  });
}

test('un navegador sin API de fuentes no presenta el sustituto como fuente cargada', async () => {
  const { cards, requests } = await fontStatusHarness({ api: false });
  assert.equal(requests.length, 0);
  for (const card of cards) {
    assert.equal(card.dataset.fontState, 'unavailable');
    assert.match(card.status.textContent, /no se puede comprobar/i);
  }
});

test('declara alcance: confirmado frente a propuesto y qué no se aprueba', () => {
  const html = sheet();
  assert.match(html, /sin aprobar/i);
  assert.match(html, /borrador/i);
  assert.match(html, /wireframe/i);
  assert.match(html, /disposici[óo]n/i);
  assert.match(html, /jugabilidad/i);
  assert.match(html, /compatibilidad/i);
  assert.match(html, /no es el (layout|dise[ñn]o) final|no demuestra/i);
});

test('explica cómo abrir y usar la hoja sin robar el foco', () => {
  const html = sheet();
  assert.match(html, /Shift\+Tab/);
  assert.match(html, /hover/i);
  assert.match(html, /focus-visible/i);
  assert.match(html, /mantener/i);
  assert.match(html, /cambiar/i);
  assert.match(html, /pendiente/i);
});

// Refinamiento 1: botones con inversión de relleno/texto y foco separado (nativo).
test('los botones invierten relleno y texto en hover y pulsado, con foco exterior separado', () => {
  const html = sheet();

  const base = cssBlock(html, '.btn');
  assert.match(base, /background:\s*var\(--color-snake\)/);
  assert.match(base, /color:\s*var\(--color-background\)/);
  assert.match(base, /border-radius:\s*var\(--radius\)/);

  const hover = cssBlock(html, '.btn:hover');
  assert.match(hover, /background:\s*var\(--color-background\)/, 'el hover rellena con el carbón');
  assert.match(hover, /color:\s*var\(--color-snake\)/, 'el hover usa texto verde');
  assert.match(hover, /border-color:\s*var\(--color-snake\)/, 'el hover usa borde verde');
  assert.doesNotMatch(hover, /--color-accent/, 'el hover ya no es solo un borde cian');
  assert.doesNotMatch(hover, /color:\s*var\(--color-background\)/, 'nunca texto carbón sobre relleno carbón');

  const active = cssBlock(html, '.btn:active');
  assert.match(active, /background:\s*var\(--color-background\)/);
  assert.match(active, /color:\s*var\(--color-snake\)/);
  assert.match(active, /box-shadow:\s*inset/, 'la pulsación añade una señal interior');
  assert.doesNotMatch(active, /(?:transform|translate|margin|padding|top|left):/, 'la pulsación no desplaza la caja');

  const focus = cssBlock(html, '.btn:focus-visible');
  assert.match(focus, /outline:\s*(?:2px|var\(--border-w\))\s+solid\s+var\(--color-focus\)/);
  assert.match(focus, /outline-offset:\s*2px/);
  assert.match(focus, /box-shadow:\s*0 0 0 2px var\(--color-background\)/, 'separación real de 2 px con el fondo');

  const both = cssBlock(html, '.btn:active:focus-visible');
  assert.match(both, /inset/);
  assert.match(both, /0 0 0 2px var\(--color-background\)/, 'la separación sigue siendo real sobre el estado pulsado');
});

test('las muestras estáticas replican la inversión y el foco separado de los controles nativos', () => {
  const html = sheet();

  const base = cssBlock(html, '.state-sample');
  assert.match(base, /background:\s*var\(--color-snake\)/);
  assert.match(base, /color:\s*var\(--color-background\)/);
  assert.match(base, /border-radius:\s*var\(--radius\)/);

  const hover = cssBlock(html, '.state-sample.is-hover');
  assert.match(hover, /background:\s*var\(--color-background\)/);
  assert.match(hover, /color:\s*var\(--color-snake\)/);
  assert.match(hover, /border-color:\s*var\(--color-snake\)/);
  assert.doesNotMatch(hover, /--color-accent/);

  const active = cssBlock(html, '.state-sample.is-active');
  assert.match(active, /background:\s*var\(--color-background\)/);
  assert.match(active, /color:\s*var\(--color-snake\)/);
  assert.match(active, /box-shadow:\s*inset/);

  const focus = cssBlock(html, '.state-sample.is-focus');
  assert.match(focus, /outline:\s*(?:2px|var\(--border-w\))\s+solid\s+var\(--color-focus\)/);
  assert.match(focus, /outline-offset:\s*2px/);
  assert.match(focus, /box-shadow:\s*0 0 0 2px var\(--color-background\)/);
});

// Refinamiento 2: radio de 8 px en botones y campo de nombre, documentado.
test('botones y campo de nombre usan un radio de 8 px documentado', () => {
  const html = sheet();
  assert.match(cssBlock(html, ':root'), /--radius:\s*8px/);
  assert.match(cssBlock(html, '.btn'), /border-radius:\s*var\(--radius\)/);
  assert.match(cssBlock(html, '.field input'), /border-radius:\s*var\(--radius\)/);
  assert.doesNotMatch(cssBlock(html, '.v4-board'), /border-radius/, 'el tablero conserva su geometría');
  const spec = fs.readFileSync(path.join(DESIGN_DIR, 'visual-style.md'), 'utf8');
  assert.match(spec, /8\s*px/, 'el radio concreto debe quedar documentado');
  assert.match(spec, /redonde|radio|esquina/i);
});

// Refinamiento 3: serpiente como tubo continuo con cabeza redondeada y ojos.
test('la serpiente se lee como tubo continuo con cola y cabeza redondeadas y ojos', () => {
  const html = sheet();
  const body = sectionBody(html, 'V4');
  assert.match(cssBlock(html, '.snake'), /linear-gradient/, 'volumen sutil como excepción documentada');
  assert.doesNotMatch(cssBlock(html, '.snake'), /border-radius/, 'sin radio por celda: evita separaciones en el cuerpo');
  assert.match(cssBlock(html, '.snake-tail'), /border-radius/);
  assert.match(cssBlock(html, '.snake-head'), /border-radius/);
  assert.match(cssBlock(html, '.snake-head::before'), /border-radius/);
  assert.match(cssBlock(html, '.snake-head::after'), /border-radius/);
  assert.match(body, /class="cell snake snake-tail"[^>]*data-cell="6,3"/, 'la cola se marca en la primera celda del cuerpo');
  assert.match(body, /class="cell snake snake-head"[^>]*data-cell="6,6"/, 'la cabeza conserva su posición');
  assert.match(body, /class="cell food"/, 'la comida sigue diferenciada');
  assert.match(body, /class="cell wall"/, 'los muros siguen diferenciados');
  const spec = fs.readFileSync(path.join(DESIGN_DIR, 'visual-style.md'), 'utf8');
  assert.match(spec, /excepci[oó]n/i, 'la excepción de degradado de la serpiente debe quedar documentada');
});

// Refinamiento 4: ranking sin cuadrícula de celdas pero semántico.
test('el ranking elimina la cuadrícula de celdas y conserva la tabla semántica', () => {
  const html = sheet();
  const cells = cssBlock(html, '.ranking th, .ranking td');
  assert.doesNotMatch(cells, /border:\s*1px/, 'las celdas ya no llevan borde de cuadrícula');
  assert.match(cells, /border:\s*(?:none|0)\b/);
  const body = sectionBody(html, 'V5');
  assert.match(body, /<table/);
  assert.match(body, /<caption/);
  assert.match(body, /<thead/);
  assert.match(body, /<th scope="col"/);
  assert.match(html, /tbody tr:nth-child\((?:even|odd)\)/, 'alternancia discreta con los tokens existentes');
});

// Sincronización de documentación: retirar afirmaciones obsoletas y separar confirmado de propuesto.
test('sincroniza los acuerdos y retira las afirmaciones obsoletas en la documentación', () => {
  const spec = fs.readFileSync(path.join(DESIGN_DIR, 'visual-style.md'), 'utf8');
  assert.doesNotMatch(spec, /esquinas rectas/i, 'ya no se afirma geometría solo recta');
  assert.doesNotMatch(spec, /segmentos cuadrados/i, 'ya no se describe la serpiente como bloques cuadrados');
  assert.doesNotMatch(spec, /hover a[ñn]ade borde `accent`/i, 'ya no se describe el hover como solo borde cian');
  assert.match(spec, /sin cuadr[ií]cula de celdas/i, 'el ranking ya no se describe con cuadrícula');
  assert.match(spec, /Refinamientos acordados/i, 'separar lo acordado de lo propuesto');
  assert.match(spec, /8\s*px/);
  assert.doesNotMatch(spec, /Pixelify Sans|Press Start 2P/, 'solo Silkscreen debe figurar en la guía pública');
  assert.match(spec, /Silkscreen/, 'la familia seleccionada debe quedar documentada');
  assert.match(spec, /integraci[oó]n local|@font-face/i, 'la integración local pendiente debe quedar documentada');
  assert.match(spec, /fallback|sustituto/i);

  const guide = fs.readFileSync(path.join(DESIGN_DIR, 'DESIGN.md'), 'utf8');
  assert.match(guide, /acordad|confirmad/i);
  assert.match(guide, /excepci[oó]n/i);
  assert.doesNotMatch(guide, /Pixelify Sans|Press Start 2P/, 'solo Silkscreen debe figurar en la guía pública');
  assert.match(guide, /Silkscreen/);
  assert.match(guide, /integraci[oó]n local|@font-face/i);

  const readme = fs.readFileSync(path.join(DESIGN_DIR, 'README.md'), 'utf8');
  assert.doesNotMatch(readme, /Pixelify Sans|Press Start 2P/, 'solo Silkscreen debe figurar en el README público');
  assert.match(readme, /Silkscreen/);
  assert.match(readme, /integraci[oó]n local|pendiente/i);

  const html = sheet();
  assert.match(html, /Refinamientos acordados/i);
  assert.match(html, /Silkscreen/);
});

// Punto actual: la revisión de la tipografía está cerrada y sigue la pantalla piloto.
test('actualiza el punto actual: tipografía cerrada y pantalla piloto como siguiente paso', () => {
  const docs = {
    'README.md': fs.readFileSync(path.join(DESIGN_DIR, 'README.md'), 'utf8'),
    'visual-style.md': fs.readFileSync(path.join(DESIGN_DIR, 'visual-style.md'), 'utf8'),
    'DESIGN.md': fs.readFileSync(path.join(DESIGN_DIR, 'DESIGN.md'), 'utf8'),
    'index.html': fs.readFileSync(path.join(DESIGN_DIR, 'index.html'), 'utf8'),
    'style-sheet.html': sheet(),
  };
  for (const [name, text] of Object.entries(docs)) {
    assert.match(text, /pantalla piloto/i, `${name} debe indicar la pantalla piloto como siguiente paso`);
  }
  assert.match(docs['visual-style.md'], /Inicio/, 'la pantalla piloto acordada es Inicio');
  assert.match(docs['README.md'], /Silkscreen/);
  assert.doesNotMatch(docs['README.md'], /falta elegir|sin elegir la fuente|fuente sin decidir/i, 'la tipografía ya no está abierta');
});
