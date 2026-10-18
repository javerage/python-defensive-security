'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');
const dir = path.join(__dirname, '..');
const file = path.join(dir, 'top10-pilot.html');
const html = fs.existsSync(file) ? fs.readFileSync(file, 'utf8') : '';
const script = html.match(/<script id="top10-font-status">([\s\S]*?)<\/script>/)?.[1] || '';

test('Top 10 is a Spanish standalone pilot accepted as a visual reference', () => {
  assert.match(html, /<html lang="es">/);
  assert.match(html, /<h1[^>]*>Top 10<\/h1>/);
  assert.match(html, /referencia visual aceptada · sin jugabilidad/);
  const title = html.match(/<title>([^<]*)<\/title>/);
  assert.ok(title, 'falta el título del piloto');
  assert.match(title[1], /referencia visual aceptada/i, 'la aceptación de Top 10 ya no deja el piloto marcado como pendiente');
  assert.match(html, /aria-label="Top 10 \(Highscores\) — referencia visual aceptada, referencia 1024 × 768"/);
  assert.doesNotMatch(html, /pendiente de revisión visual/, 'Top 10 ya no debe declararse pendiente de revisión visual');
  // La aceptación es visual y acotada: las reglas abiertas se conservan.
  assert.match(html, /El registro por nivel y el orden entre empates iguales siguen pendientes/);
  assert.match(html, /La integración local sigue pendiente/);
});

test('Top 10 preserves the approved frame, table and button boxes', () => {
  for (const [selector, properties] of [
    ['pilot-screen', ['width: 1024px', 'height: 768px']],
    ['game-panel', ['left: 112px', 'top: 80px', 'width: 800px', 'height: 600px']],
    ['ranking', ['left: 100px', 'top: 116px', 'width: 600px']],
    ['btn', ['left: 300px', 'top: 500px', 'width: 200px', 'height: 52px']],
  ]) {
    const block = html.match(new RegExp(`\\.${selector}\\s*\\{([^}]+)\\}`))?.[1] || '';
    for (const property of properties) assert.ok(block.includes(property), `${selector}: ${property}`);
  }
});

test('the semantic table reproduces all ten illustrative wireframe entries', () => {
  assert.match(html, /<table[^>]*aria-describedby="ranking-note"/);
  assert.equal([...html.matchAll(/<th scope="col">/g)].length, 4);
  const rows = [...html.matchAll(/<tr><th scope="row">(\d+)<\/th><td>([^<]+)<\/td><td>(\d+)<\/td><td>(\d+)<\/td><\/tr>/g)]
    .map(match => match.slice(1));
  const svg = fs.readFileSync(path.join(dir, 'wireframes', 'top10.svg'), 'utf8');
  const values = [...svg.matchAll(/<text x="(?:226|306|546|686)" y="(?:251|283|315|347|379|411|443|475|507|539)"[^>]*>([^<]+)<\/text>/g)].map(match => match[1]);
  assert.equal(rows.length, 10);
  assert.deepEqual(rows.flat(), values);
  assert.match(html, /Datos ilustrativos — no son rankings reales/);
  assert.match(html, /El registro por nivel y el orden entre empates iguales siguen pendientes/);
});

test('the only action is a visual Nueva partida button with no game or persistence logic', () => {
  assert.equal([...html.matchAll(/<button\b/g)].length, 1);
  assert.match(html, /<button type="button" class="btn" aria-describedby="return-note">Nueva partida<\/button>/);
  assert.match(html, /Referencia estática: el botón solo muestra estados visuales; no navega ni inicia partidas/);
  assert.match(html, /espera «play» o Enter desde el campo de nombre/);
  assert.equal([...html.matchAll(/<script\b/g)].length, 1);
  assert.ok(script);
  assert.doesNotMatch(html, /<(?:form|input|canvas|iframe)\b|\bon(?:click|keydown|submit)=|http-equiv|@keyframes|animation:/i);
  assert.doesNotMatch(script, /location|localStorage|sessionStorage|setInterval|addEventListener/);
});

test('Top 10 reuses the eleven tokens, font roles and agreed button states without a cell grid', () => {
  const reference = fs.readFileSync(path.join(dir, 'victory-pilot.html'), 'utf8');
  const tokens = text => [...text.matchAll(/--color-[\w-]+:\s*#[\dA-F]{6};/g)].map(match => match[0]);
  assert.equal(tokens(html).length, 11);
  assert.deepEqual(tokens(html), tokens(reference));
  assert.deepEqual([...new Set(html.match(/#[\dA-Fa-f]{6}\b/g))].sort(), [...new Set(reference.match(/#[\dA-Fa-f]{6}\b/g))].sort());
  assert.match(html, /family=Silkscreen:wght@400;700/);
  assert.match(html, /td:nth-child\(2\)\s*\{[^}]*font-family: var\(--font-body\)/);
  assert.match(html, /th, td\s*\{[^}]*border: 0/);
  for (const state of [':hover', ':active', ':focus-visible', ':active:focus-visible']) assert.ok(html.includes(`.btn${state}`));
  assert.match(html, /border-radius: 8px/);
  assert.match(html, /integración local sigue pendiente/);
  assert.match(html, /<noscript>/);
});

for (const mode of ['loaded', 'rejected', 'empty', 'timeout', 'unavailable']) {
  test(`Top 10 font notice remains honest: ${mode}`, async () => {
    assert.ok(script);
    const status = { hidden: false, dataset: {}, textContent: '' };
    const timers = new Map();
    const calls = [];
    const document = { querySelector: () => status };
    if (mode !== 'unavailable') document.fonts = { load: spec => {
      calls.push(spec);
      if (mode === 'rejected') return Promise.reject(new Error('offline'));
      if (mode === 'timeout') return new Promise(() => {});
      return Promise.resolve(mode === 'empty' ? [] : [{}]);
    } };
    vm.runInNewContext(script, { document, setTimeout: callback => { timers.set(1, callback); return 1; }, clearTimeout: id => timers.delete(id) });
    if (mode === 'timeout') for (const callback of timers.values()) callback();
    await new Promise(resolve => setImmediate(resolve));
    assert.equal(status.hidden, mode === 'loaded');
    assert.equal(status.dataset.fontState, mode === 'loaded' ? 'loaded' : mode === 'unavailable' ? 'unavailable' : 'failed');
    if (mode !== 'unavailable') assert.deepEqual(calls, ['400 16px "Silkscreen"', '700 24px "Silkscreen"']);
    if (mode !== 'loaded') assert.match(status.textContent, /sustituto/);
    assert.equal(timers.size, 0);
  });
}

test('all six guides link Top 10 as accepted, preserve previous acceptance and describe the next step', () => {
  for (const name of ['README.md', 'index.html', 'DESIGN.md', 'visual-style.md', 'screens.md', 'style-sheet.html']) {
    const text = fs.readFileSync(path.join(dir, name), 'utf8');
    assert.match(text, /top10-pilot\.html/, name);
    assert.match(text, /Top 10[^\n]{0,180}aceptad[ao] como referencia visual/i, name);
    for (const pilot of ['start', 'playing', 'game-over', 'victory']) assert.ok(text.includes(`${pilot}-pilot.html`), name);
    assert.doesNotMatch(text, /(?:crear (?:el )?mockup de (?:\*\*)?Top 10|Top 10[^\n]{0,60}pendiente de creaci[oó]n)/i, name);
    assert.doesNotMatch(text, /Top 10[^\n]{0,120}pendiente de revisi[oó]n visual/i, name);
  }
  const readme = fs.readFileSync(path.join(dir, 'README.md'), 'utf8');
  assert.match(readme, /node --test[^\n]*top10-pilot\.test\.cjs/);
  assert.match(readme, /top10-pilot\.browser\.test\.cjs/);
});
