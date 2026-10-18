'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const dir = path.join(__dirname, '..');
const file = path.join(dir, 'game-over-pilot.html');
const html = fs.existsSync(file) ? fs.readFileSync(file, 'utf8') : '';
const script = html.match(/<script id="game-over-font-status">([\s\S]*?)<\/script>/)?.[1] || '';

test('Game Over is a standalone Spanish reference accepted as a visual reference', () => {
  assert.match(html, /<!DOCTYPE html>/i);
  assert.match(html, /<html lang="es">/);
  assert.match(html, /<h1[^>]*>GAME OVER<\/h1>/);
  assert.match(html, /GAME OVER · Results/);
  assert.match(html, /referencia visual aceptada · sin jugabilidad/);
  assert.doesNotMatch(html, /pendiente de revisión visual/);
});

test('the new reference reuses all eleven existing colors without changing their values', () => {
  const reference = fs.readFileSync(path.join(dir, 'start-pilot.html'), 'utf8');
  const tokens = [...reference.matchAll(/--color-[\w-]+:\s*#[\dA-F]{6};/g)].map(match => match[0]);
  assert.equal(tokens.length, 11);
  for (const token of tokens) assert.ok(html.includes(token), token);
  assert.match(html, /\.game-title\s*\{[^}]*color:\s*var\(--color-food\)/);
});

test('panel and summary preserve the approved wireframe boxes', () => {
  for (const [selector, properties] of [
    ['pilot-screen', ['width: 1024px', 'height: 768px']],
    ['game-panel', ['left: 112px', 'top: 80px', 'width: 800px', 'height: 600px']],
    ['results-card', ['left: 200px', 'top: 238px', 'width: 400px', 'height: 236px']],
  ]) {
    const block = html.match(new RegExp(`\\.${selector}\\s*\\{([^}]+)\\}`))?.[1] || '';
    for (const property of properties) assert.ok(block.includes(property), `${selector}: ${property}`);
  }
});

test('the semantic summary contains the four illustrative wireframe values', () => {
  assert.match(html, /<dl class="results-list">/);
  for (const [label, value] of [['Nombre', 'player_20261016_120000_000'], ['Puntaje', '0'], ['Nivel', '1'], ['Velocidad', '1']]) {
    assert.match(html, new RegExp(`<dt>${label}<\/dt>\\s*<dd[^>]*>${value}<\/dd>`));
  }
  assert.match(html, /Valores ilustrativos — no son resultados reales\./);
  assert.match(html, /agotarse las vidas/);
});

test('the five-second conditional transition is explanatory, never an active action', () => {
  assert.match(html, /Tras 5 segundos: Top 10 si el resultado clasifica; si no clasifica, vuelve al inicio\./);
  assert.match(html, /Sin botones de continuar ni reintentar/);
  assert.match(html, /sin animación ni redirección activa/);
  assert.doesNotMatch(html, /<(?:button|input|form|canvas|iframe)\b|<meta[^>]+http-equiv|\bon(?:click|keydown|submit)=/i);
  assert.equal([...html.matchAll(/<script\b/g)].length, 1);
  assert.ok(script);
  assert.doesNotMatch(script, /location|localStorage|sessionStorage|setInterval|requestAnimationFrame|addEventListener/);
});

test('font roles use only real Silkscreen weights, and explain temporary external loading', () => {
  assert.match(html, /family=Silkscreen:wght@400;700/);
  assert.doesNotMatch(html, /font-weight:\s*(?:800|900)|Pixelify Sans|Press Start 2P/);
  assert.match(html, /--font-body: system-ui/);
  assert.match(html, /\.result-name\s*\{[^}]*font-family:\s*var\(--font-body\)/);
  assert.match(html, /<noscript>/);
  assert.match(html, /integración local sigue pendiente/);
  assert.match(html, /sustituto monoespaciado/);
});

async function runFontCheck(mode) {
  const status = { hidden: false, dataset: {}, textContent: '' };
  const calls = [];
  const timers = new Map();
  const document = { querySelector: () => status };
  if (mode !== 'unavailable') document.fonts = {
    load: (spec, sample) => {
      calls.push({ spec, sample });
      if (mode === 'rejected') return Promise.reject(new Error('offline'));
      if (mode === 'timeout') return new Promise(() => {});
      return Promise.resolve(mode === 'empty' ? [] : [{}]);
    },
  };
  vm.runInNewContext(script, {
    document,
    setTimeout: callback => { timers.set(1, callback); return 1; },
    clearTimeout: id => timers.delete(id),
  });
  if (mode === 'timeout') for (const callback of timers.values()) callback();
  await new Promise(resolve => setImmediate(resolve));
  return { status, calls, timers };
}

test('both font weights must load before the warning is hidden', async () => {
  assert.ok(script);
  const { status, calls, timers } = await runFontCheck('loaded');
  assert.deepEqual(calls.map(call => call.spec), ['400 16px "Silkscreen"', '700 24px "Silkscreen"']);
  assert.ok(calls.every(call => call.sample.includes('GAME OVER')));
  assert.equal(status.dataset.fontState, 'loaded');
  assert.equal(status.hidden, true);
  assert.equal(timers.size, 0);
});

for (const mode of ['rejected', 'empty', 'timeout', 'unavailable']) {
  test(`font failure stays visible and honest: ${mode}`, async () => {
    assert.ok(script);
    const { status } = await runFontCheck(mode);
    assert.equal(status.hidden, false);
    assert.equal(status.dataset.fontState, mode === 'unavailable' ? 'unavailable' : 'failed');
    assert.match(status.textContent, /sustituto/);
  });
}

test('public guides record accepted Game Over within a scoped approval', () => {
  for (const name of ['README.md', 'index.html', 'DESIGN.md', 'visual-style.md', 'screens.md', 'style-sheet.html']) {
    const text = fs.readFileSync(path.join(dir, name), 'utf8');
    assert.match(text, /game-over-pilot\.html/, name);
    assert.match(text, /Game Over[^\n]{0,200}aceptad[ao] como referencia visual/i, name);
    // A later Victoria clause may legitimately be pending on the same line.
    assert.doesNotMatch(text, /Game Over(?:(?!Victoria)[^\n]){0,140}pendiente de revisi[oó]n visual/i, name);
    assert.match(text, /start-pilot\.html/, name);
    assert.match(text, /playing-pilot\.html/, name);
    assert.doesNotMatch(text, /Game Over.{0,80}planificado y todavía no creado/, name);
    assert.doesNotMatch(text, /Game Over[^\n]{0,120}todav[ií]a no creado/i, name);
  }
  const readme = fs.readFileSync(path.join(dir, 'README.md'), 'utf8');
  assert.match(readme, /node --test[^\n]*game-over-pilot\.test\.cjs/);
  assert.match(readme, /game-over-pilot\.browser\.test\.cjs/);
  assert.match(readme, /Victoria[^\n]{0,180}pendiente de revisión visual/i, 'Victoria debe conservar su revisión independiente tras aceptar Game Over');
});
