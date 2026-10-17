const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const DESIGN_DIR = path.join(__dirname, '..');
const PILOT_PATH = path.join(DESIGN_DIR, 'playing-pilot.html');

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
const TOKEN_HEX = TOKENS.map(([, hex]) => hex.toUpperCase());

// Reglas ilustrativas del wireframe: NO son reglas de juego reales.
const SCORE = '0';
const LIVES = '3';
const LEVEL = '1';
const SPEED = '1';
const PLAYER = 'player_20261016_120000_000';

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

function px(block, prop) {
  const match = block.match(new RegExp(`${prop}\\s*:\\s*(-?\\d+)px`));
  assert.ok(match, `falta ${prop} en px`);
  return Number(match[1]);
}

// Contraste WCAG a partir de los tokens existentes; no se inventan colores nuevos.
function srgbToLinear(channel) {
  const value = channel / 255;
  return value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
}
function luminance(hex) {
  const raw = hex.replace('#', '');
  const r = parseInt(raw.slice(0, 2), 16);
  const g = parseInt(raw.slice(2, 4), 16);
  const b = parseInt(raw.slice(4, 6), 16);
  return 0.2126 * srgbToLinear(r) + 0.7152 * srgbToLinear(g) + 0.0722 * srgbToLinear(b);
}
function contrast(a, b) {
  const hi = Math.max(luminance(a), luminance(b));
  const lo = Math.min(luminance(a), luminance(b));
  return (hi + 0.05) / (lo + 0.05);
}
const token = name => TOKENS.find(([tokenName]) => tokenName === name)[1];

function gridArea(html, selector) {
  const raw = cssBlock(html, selector).match(/grid-area\s*:\s*([\d\s/]+)/);
  assert.ok(raw, `falta grid-area en ${selector}`);
  return raw[1].split('/').map(part => Number(part.trim()));
}

test('define los 11 tokens semánticos exactos de visual-style.md', () => {
  const html = pilot();
  const declared = [...html.matchAll(/--color-([a-z-]+)\s*:/g)].map(match => match[1]);
  assert.deepEqual(declared.sort(), TOKENS.map(([name]) => name).sort());
  for (const [name, hex] of TOKENS) {
    assert.match(html, new RegExp(`--color-${name}\\s*:\\s*${hex}`, 'i'), `falta --color-${name}: ${hex}`);
  }
});

test('no introduce hexadecimales fuera de los 11 tokens aprobados', () => {
  const html = pilot();
  const literals = [...html.matchAll(/#[0-9a-fA-F]{6}\b/g)].map(match => match[0].toUpperCase());
  for (const literal of literals) {
    assert.ok(TOKEN_HEX.includes(literal), `hex fuera de los tokens aprobados: ${literal}`);
  }
});

test('reproduce la referencia 1024 × 768 con el panel, HUD y tablero aprobados', () => {
  const html = pilot();
  const screen = cssBlock(html, '.pilot-screen');
  assert.match(screen, /width:\s*1024px/);
  assert.match(screen, /height:\s*768px/);

  const panel = cssBlock(html, '.game-panel');
  assert.match(panel, /position:\s*absolute/);
  assert.match(panel, /background:\s*var\(--color-surface\)/, 'el panel es carbón (surface)');
  assert.equal(px(panel, 'left'), 112);
  assert.equal(px(panel, 'top'), 80);
  assert.equal(px(panel, 'width'), 800);
  assert.equal(px(panel, 'height'), 600);
  assert.equal(px(cssBlock(html, '.game-panel-head'), 'height'), 46);

  const panelLeft = px(panel, 'left');
  const panelTop = px(panel, 'top');

  const hud = cssBlock(html, '.hud');
  assert.match(hud, /position:\s*absolute/);
  // Coordenadas de pantalla aprobadas: HUD (124, 140), 776 × 52.
  assert.equal(panelLeft + px(hud, 'left'), 124);
  assert.equal(panelTop + px(hud, 'top'), 140);
  assert.equal(px(hud, 'width'), 776);
  assert.equal(px(hud, 'height'), 52);

  const board = cssBlock(html, '.board');
  assert.match(board, /position:\s*absolute/);
  // Coordenadas de pantalla aprobadas: tablero (252, 212), 520 × 400.
  assert.equal(panelLeft + px(board, 'left'), 252);
  assert.equal(panelTop + px(board, 'top'), 212);
  assert.equal(px(board, 'width'), 520);
  assert.equal(px(board, 'height'), 400);
  assert.match(board, /grid-template-columns:\s*repeat\(13,\s*40px\)/, 'rejilla ilustrativa de 40 px (13 columnas)');
  assert.match(board, /grid-template-rows:\s*repeat\(10,\s*40px\)/, 'rejilla ilustrativa de 40 px (10 filas)');
  assert.match(board, /background-color:\s*var\(--color-board\)/);
});

test('mantiene todas las cajas dentro del panel central', () => {
  const html = pilot();
  const panel = cssBlock(html, '.game-panel');
  const left = px(panel, 'left');
  const top = px(panel, 'top');
  const right = left + px(panel, 'width');
  const bottom = top + px(panel, 'height');

  for (const selector of ['.hud', '.board']) {
    const block = cssBlock(html, selector);
    const boxLeft = left + px(block, 'left');
    const boxTop = top + px(block, 'top');
    assert.ok(boxLeft >= left, `${selector} no sale por la izquierda`);
    assert.ok(boxTop >= top, `${selector} no sale por arriba`);
    assert.ok(boxLeft + px(block, 'width') <= right, `${selector} no sale por la derecha (${boxLeft + px(block, 'width')} > ${right})`);
    assert.ok(boxTop + px(block, 'height') <= bottom, `${selector} no sale por abajo (${boxTop + px(block, 'height')} > ${bottom})`);
  }
});

test('divide el HUD en las cinco columnas aprobadas con sus límites exactos', () => {
  const html = pilot();
  const hud = cssBlock(html, '.hud');
  const template = hud.match(/grid-template-columns\s*:\s*([^;]+);/);
  assert.ok(template, 'el HUD declara columnas');
  const widths = [...template[1].matchAll(/(\d+)px/g)].map(match => Number(match[1]));
  assert.equal(widths.length, 5, 'el HUD tiene cinco columnas');

  // Límites de pantalla aprobados: 384, 513, 642, 771 (HUD en x=124).
  const boundaries = [384, 513, 642, 771];
  let accumulated = 124;
  for (let index = 0; index < widths.length - 1; index += 1) {
    accumulated += widths[index];
    assert.equal(accumulated, boundaries[index], `límite ${index + 1} del HUD`);
  }
  assert.equal(widths.reduce((sum, value) => sum + value, 0), 776, 'las columnas suman el ancho del HUD');
});

test('aplica los roles tipográficos: Silkscreen en título y cifras, sistema en nombre e instrucciones', () => {
  const html = pilot();
  assert.match(cssBlock(html, '.panel-title'), /font-family:\s*var\(--font-pixel\)/);
  assert.match(cssBlock(html, '.hud-value'), /font-family:\s*var\(--font-pixel\)/);
  assert.match(cssBlock(html, '.hud-value'), /font-size:\s*16px/);
  assert.match(cssBlock(html, '.panel-title'), /font-size:\s*16px/);
  assert.match(cssBlock(html, '.hud-player'), /font-family:\s*var\(--font-body\)/);
  assert.match(cssBlock(html, '.hud-label'), /font-family:\s*var\(--font-body\)/);
  assert.match(cssBlock(html, '.board-help'), /font-family:\s*var\(--font-body\)/);
  assert.doesNotMatch(html, /font-size:\s*52px/, 'no copia el marcador de posición de 52 px como tipo aprobado');
});

test('dibuja la serpiente como tubo continuo con cola y cabeza reconocibles y sin huecos', () => {
  const html = pilot();
  const tube = cssBlock(html, '.tube');
  assert.match(tube, /linear-gradient\(180deg/);
  assert.match(tube, /color-mix\(in srgb, var\(--color-snake\)/);
  assert.doesNotMatch(tube, /border-radius/, 'el cuerpo no redondea por celda: es continuo');

  assert.match(cssBlock(html, '.tube-tail'), /border-radius:\s*50%\s*0\s*0\s*50%/, 'cola redondeada en el extremo expuesto');
  const head = cssBlock(html, '.tube-head');
  assert.match(head, /border-radius:\s*0\s*50%\s*50%\s*0/, 'cabeza redondeada hacia el frente');
  assert.match(html, /\.tube-head::before/, 'la cabeza amistosa tiene ojos');
  assert.match(html, /\.tube-head::after/);

  const board = cssBlock(html, '.board');
  assert.doesNotMatch(board, /gap:\s*[1-9]/, 'sin separación entre celdas: el tubo queda continuo');

  const tail = gridArea(html, '.tube-tail');
  const body = gridArea(html, '.tube-body');
  const headArea = gridArea(html, '.tube-head');
  assert.deepEqual(tail, [7, 5, 8, 6], 'cola en la celda (412, 452)');
  assert.deepEqual(body, [7, 6, 8, 7], 'cuerpo en la celda (452, 452)');
  assert.deepEqual(headArea, [7, 7, 8, 8], 'cabeza en la celda (492, 452)');
  assert.equal(html.match(/class="tube\b/g).length, 3, 'la serpiente ilustrativa ocupa tres celdas');
});

// Corrección: la cabeza no puede llevar un anillo interior de color tablero que la separe del cuerpo.
test('la cabeza no dibuja un contorno interior de color tablero en la unión con el cuerpo', () => {
  const html = pilot();
  const head = cssBlock(html, '.tube-head');
  assert.doesNotMatch(head, /box-shadow\s*:\s*inset[^;]*var\(--color-board\)/, 'sin anillo interior de color tablero');
  assert.doesNotMatch(head, /border\s*:\s*[^;]*var\(--color-board\)/, 'sin borde de color tablero en todas las aristas');
  assert.doesNotMatch(head, /outline\s*:[^;]*var\(--color-board\)/, 'sin contorno de color tablero');

  // La cabeza conserva su forma frontal redondeada, sus ojos y su posición.
  assert.match(head, /border-radius:\s*0\s*50%\s*50%\s*0/);
  assert.match(html, /\.tube-head::before/);
  assert.match(html, /\.tube-head::after/);
  assert.deepEqual(gridArea(html, '.tube-head'), [7, 7, 8, 8]);
});

test('distingue comida y obstáculos por forma, no solo por color', () => {
  const html = pilot();
  const food = cssBlock(html, '.food');
  assert.match(food, /background:\s*var\(--color-food\)/);
  assert.match(food, /clip-path:\s*polygon\(/, 'la comida es un rombo, no un círculo');
  assert.deepEqual(gridArea(html, '.food'), [5, 10, 6, 11], 'la comida conserva la celda ilustrativa (632, 392)');

  const wall = cssBlock(html, '.wall');
  assert.match(wall, /repeating-linear-gradient\(45deg/, 'los obstáculos llevan trama interior');

  const obstacles = [
    ['1', [1, 3, 2, 6]],
    ['2', [1, 10, 2, 13]],
    ['3', [10, 2, 11, 5]],
    ['4', [10, 11, 11, 14]],
    ['5', [4, 6, 6, 7]],
    ['6', [7, 9, 8, 11]],
  ];
  for (const [index, area] of obstacles) {
    assert.deepEqual(gridArea(html, `.obstacle-${index}`), area, `huella del obstáculo ${index}`);
  }
  assert.equal(html.match(/class="wall\b/g).length, 6, 'se conservan seis huellas de obstáculo');
});

test('usa el volumen sutil solo en la serpiente y la cuadrícula solo como decorado', () => {
  const html = pilot();
  const gradients = [...html.matchAll(/[^-]linear-gradient\(/g)];
  assert.ok(gradients.length > 0, 'la serpiente usa su degradado documentado');
  // Cada uso no repetido de linear-gradient vive en una regla de la serpiente.
  for (const match of gradients) {
    const contextStart = html.lastIndexOf('}', match.index);
    const context = html.slice(contextStart, match.index);
    assert.match(context, /\.tube/, 'solo la serpiente usa degradados de volumen');
  }
  const boardBg = cssBlock(html, '.board').match(/background-image\s*:\s*([\s\S]*?);/);
  assert.ok(boardBg, 'el tablero declara su cuadrícula decorativa');
  assert.match(boardBg[1], /var\(--color-grid\)/, 'la cuadrícula decorativa usa --color-grid');
  assert.doesNotMatch(boardBg[1], /var\(--color-border\)/, 'la cuadrícula no se dibuja como obstáculo');
});

// Devuelve el contenido interno de la celda VIDAS del HUD.
function livesCell(html) {
  const cell = html.match(/<div class="hud-cell">\s*<span class="hud-label">VIDAS<\/span>([\s\S]*?)<\/div>/);
  assert.ok(cell, 'falta la celda VIDAS del HUD');
  return cell[1];
}

test('presenta cifras ilustrativas de HUD y una serpiente de tres celdas, sin afirmar reglas reales', () => {
  const html = pilot();
  for (const label of ['JUGADOR', 'PUNTAJE', 'VIDAS', 'NIVEL', 'VELOCIDAD']) {
    assert.ok(html.includes(label), `falta la etiqueta del HUD: ${label}`);
  }
  // Las vidas ya no son una cifra: se representan con iconos de corazón.
  for (const value of [SCORE, LEVEL, SPEED]) {
    assert.ok(html.includes(`>${value}<`), `falta el valor ilustrativo del HUD: ${value}`);
  }
  assert.ok(html.includes(PLAYER), 'el nombre ilustrativo se muestra completo');
  assert.match(html, /ilustrativ/i, 'declara los datos y la escena como ilustrativos');
  assert.match(html, /referencia visual aceptada/i, 'declara la referencia visual aceptada');
  assert.doesNotMatch(html, /propuesta\s*[—-]\s*aprobada/i, 'no hereda la anotación del wireframe aprobado');
  assert.doesNotMatch(html, /revisada y aprobada/i);
});

// Corrección pedida: las vidas se muestran como corazones, no como la cifra 3.
test('representa las vidas con tres iconos de corazón y no con la cifra 3', () => {
  const html = pilot();
  const cell = livesCell(html);
  assert.doesNotMatch(cell, /hud-value">\s*3\s*</, 'la cifra 3 no es el valor visible de vidas');
  assert.match(cell, /data-lives-hearts/, 'las vidas usan un grupo de iconos');
  assert.equal((cell.match(/class="life-heart is-full"/g) || []).length, 3, 'hay tres corazones llenos');
  assert.equal((cell.match(/class="life-heart is-empty"/g) || []).length, 0, 'el estado inicial muestra las tres vidas llenas');
  assert.equal((cell.match(/<svg class="life-heart[^>]*>/g) || []).length, 3, 'se mantienen exactamente tres posiciones de vida');
});

test('expone el grupo de vidas como «3 de 3 vidas disponibles» con iconos decorativos', () => {
  const html = pilot();
  assert.match(html, /data-lives-hearts[^>]*role="img"/, 'el grupo es una imagen accesible');
  assert.equal((html.match(/aria-label="3 de 3 vidas disponibles"/g) || []).length, 1, 'la etiqueta accesible no se repite por icono');
  const svgs = [...html.matchAll(/<svg class="life-heart[^>]*>/g)].map(match => match[0]);
  assert.equal(svgs.length, 3, 'tres iconos de corazón');
  for (const svg of svgs) {
    assert.match(svg, /aria-hidden="true"/, 'cada icono es decorativo para no repetir la etiqueta tres veces');
  }
});

test('los estados lleno y vacío comparten la misma geometría de corazón pixelado', () => {
  const html = pilot();
  const paths = [...html.matchAll(/<svg class="life-heart[^>]*><path d="([^"]+)"/g)].map(match => match[1]);
  assert.equal(paths.length, 3, 'los tres iconos declaran su trazado');
  assert.equal(new Set(paths).size, 1, 'los corazones usan el mismo trazado');
  const d = paths[0];
  assert.match(d, /^M[\d\sHVZ]+Z$/, 'el trazado es un polígono escalonado de segmentos rectos');
  assert.doesNotMatch(d, /[CSAQAcsqa]/, 'sin curvas: iconos pixelados, no redondeados ni emoji');
  assert.doesNotMatch(html, /[❤♥]/, 'sin emoji ni glifos de corazón');

  const full = cssBlock(html, '.life-heart.is-full path');
  assert.match(full, /fill:\s*var\(--color-food\)/, 'el corazón lleno usa un token existente de la paleta');
  const empty = cssBlock(html, '.life-heart.is-empty path');
  assert.match(empty, /fill:\s*none/, 'el corazón vacío es contorno, no relleno');
  assert.match(empty, /stroke:\s*var\(--color-food\)/, 'el contorno comparte token, sin hexadecimales nuevos');
  const strokeW = empty.match(/stroke-width:\s*([\d.]+)/);
  assert.ok(strokeW && Number(strokeW[1]) > 0, 'el contorno tiene grosor visible sobre el HUD');
});

test('los corazones caben en la columna VIDAS sin alterar el HUD', () => {
  const html = pilot();
  const width = Number(html.match(/<svg class="life-heart[^>]*width="(\d+)"/)[1]);
  const gap = Number(cssBlock(html, '.hud-lives').match(/gap:\s*(\d+)px/)[1]);
  // Columna de 129 px con 12 px de relleno por lado => 105 px útiles.
  assert.ok(width * 3 + gap * 2 <= 105, `los tres corazones deben caber en la columna: ${width * 3 + gap * 2} > 105`);
});

// Corrección pedida: el aviso de escena no puede solaparse con el marco inferior.
test('el aviso de escena termina en «reglas ni valores reales.» y se mantiene conciso', () => {
  const html = pilot();
  const note = html.match(/<p class="scene-note">([^<]*)<\/p>/);
  assert.ok(note, 'falta el aviso de escena');
  const text = note[1].trim();
  assert.match(text, /no son reglas ni valores reales\.$/, 'el aviso termina con la frase exigida');
  assert.match(text, /ilustrativ/i, 'declara la escena y los datos como ilustrativos');
  assert.match(html, /referencia visual aceptada/i, 'la pantalla se declara referencia visual aceptada');
  assert.ok(text.length <= 140, 'el aviso se acorta para caber en una línea (comprobado en navegador)');
});

test('el aviso de escena recupera su tamaño 11 px frente a la regla genérica de párrafos', () => {
  const html = pilot();
  // La regla genérica .board-help p (0,1,1) fijaba 12 px y anulaba .scene-note (0,1,0).
  assert.match(cssBlock(html, '.board-help'), /font-family:\s*var\(--font-body\)/);
  assert.match(cssBlock(html, '.board-help .scene-note'), /font-size:\s*11px/, 'el aviso usa su tamaño diseñado de 11 px');
});

test('no añade acciones, botones, juego, atajos ni bucle de render', () => {
  const html = pilot();
  assert.doesNotMatch(html, /<form\b/i);
  assert.doesNotMatch(html, /<button\b/i);
  assert.doesNotMatch(html, /<input\b/i);
  assert.doesNotMatch(html, /<a\b/i, 'sin navegación');
  assert.doesNotMatch(html, /<canvas\b/i);
  assert.doesNotMatch(html, /addEventListener/);
  assert.doesNotMatch(html, /onclick|onkeydown|onsubmit|onload=/i);
  assert.doesNotMatch(html, /keydown|keyup|keypress/i);
  assert.doesNotMatch(html, /setInterval|requestAnimationFrame/);
  assert.doesNotMatch(html, /localStorage|sessionStorage|fetch\(|XMLHttpRequest/);
  assert.doesNotMatch(html, /window\.location|location\.href|location\.assign|location\.replace/);
  assert.doesNotMatch(html, /@keyframes/i);
  assert.doesNotMatch(html, /animation\s*:/i);
  assert.doesNotMatch(html, /transition\s*:/i);
  assert.doesNotMatch(html, /<table\b/i);
  assert.doesNotMatch(html, /<img\b/i);
});

test('reproduce las instrucciones aprobadas del wireframe sin pausa ni ajustes', () => {
  const html = pilot();
  assert.ok(html.includes('Flechas del teclado (← ↑ → ↓): dirigir la serpiente.'), 'falta la guía de flechas');
  assert.ok(
    html.includes('Sin pausa, ajustes, reinicio manual ni registro de puntaje desde esta pantalla.'),
    'falta la nota de que no hay pausa ni ajustes',
  );
  assert.match(html, /[←↑→↓áéíóúñ¿¡«»]/, 'conserva los caracteres españoles');
});

test('se marca como referencia visual aceptada y sin jugabilidad en el encabezado y el título', () => {
  const html = pilot();
  const note = html.match(/<span class="panel-note">([^<]*)<\/span>/);
  assert.ok(note, 'falta la nota del panel');
  assert.match(note[1], /referencia visual aceptada/i);
  assert.match(note[1], /sin jugabilidad/i);
  assert.match(html.match(/<title>([^<]*)<\/title>/)[1], /referencia visual aceptada/i);
  assert.match(html, /PARTIDA · Playing/);
  assert.match(html, /<noscript>/);
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
});

test('solo ejecuta la comprobación de carga con FontFaceSet, sin src ni otra lógica', () => {
  const html = pilot();
  const scripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)];
  assert.equal(scripts.length, 1);
  assert.match(scripts[0][1], /id="playing-font-status"/);
  assert.doesNotMatch(scripts[0][1], /\bsrc=/);
  assert.match(scripts[0][2], /document\.fonts\.load/);
  assert.doesNotMatch(html, /addEventListener/);
});

async function fontStatusHarness({ outcome = 'loaded', api = true } = {}) {
  const script = pilot().match(/<script id="playing-font-status">([\s\S]*?)<\/script>/);
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
  assert.deepEqual(requests.map(request => request.font), ['400 16px "Silkscreen"', '700 16px "Silkscreen"']);
  for (const { text } of requests) assert.match(text, /á é í ó ú ñ ü ¿ ¡/);
  assert.equal(status.dataset.fontState, 'loaded');
  assert.equal(status.hidden, true, 'el aviso de éxito se oculta');
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

test('la envoltura del aviso no deja espacio vertical con el aviso oculto', () => {
  const html = pilot();
  const wrapper = cssBlock(html, '.page-note');
  assert.match(wrapper, /padding:\s*0 24px/, 'la envoltura solo aporta relleno horizontal');
  assert.doesNotMatch(wrapper, /padding-(top|bottom)/);
  assert.doesNotMatch(wrapper, /padding:\s*[1-9]\d*px/);
  assert.match(cssBlock(html, '.font-status'), /margin:\s*[^;]*[1-9]/, 'el espaciado pasa al aviso visible');
  assert.match(cssBlock(html, '.font-status[hidden]'), /display:\s*none/);
});

test('los contrastes esenciales se sostienen con los tokens existentes', () => {
  assert.ok(contrast(token('text'), token('background')) >= 4.5, 'texto sobre fondo');
  assert.ok(contrast(token('text'), token('surface')) >= 4.5, 'texto sobre panel');
  assert.ok(contrast(token('text'), token('board')) >= 4.5, 'texto sobre tablero');
  assert.ok(contrast(token('text-muted'), token('background')) >= 4.5, 'texto atenuado sobre fondo');
  assert.ok(contrast(token('text-muted'), token('surface')) >= 4.5, 'texto atenuado sobre panel');
  assert.ok(contrast(token('border'), token('board')) >= 3, 'límites de obstáculos sobre tablero');
  assert.ok(contrast(token('border'), token('surface')) >= 3, 'límites del HUD y panel');
  assert.ok(contrast(token('snake'), token('board')) >= 3, 'serpiente sobre tablero');
  assert.ok(contrast(token('food'), token('board')) >= 3, 'comida sobre tablero');
});

test('la vista no recorta la pantalla de referencia', () => {
  const html = pilot();
  assert.match(html, /<meta name="viewport"/);
  assert.doesNotMatch(cssBlock(html, 'body'), /overflow:\s*hidden/, 'el body no recorta la pantalla de referencia');
});
