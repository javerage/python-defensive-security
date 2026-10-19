'use strict';

// Encoding contract for the reusable Spanish Markdown templates.
//
// Symptom under test: opening constitucion-template.md / mision-template.md directly
// in a browser showed mojibake such as "secciÃ³n" instead of "sección". The source is
// valid UTF-8, but a plain-text client that receives no charset (a downloaded file, a
// static server that omits the parameter, a legacy default encoding) may decode the
// UTF-8 bytes as windows-1252 and mojibake every accent. A leading UTF-8 BOM makes the
// client detect UTF-8 regardless of the transport default.
//
// The same condition applies to every Markdown file of this repository: any of them
// can be opened directly in a browser. The repo-wide check therefore requires a BOM on
// README.md and every .md under docs/ and src/.
//
// These checks are read-only: they read bytes, they never rewrite the templates. The
// browser test reuses the dependency-free CDP pattern of docs/pi/snake/design/tests/*
// .browser.test.cjs and is skipped when Chrome/Chromium is unavailable.

const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');
const fs = require('node:fs');
const http = require('node:http');
const os = require('node:os');
const path = require('node:path');
const { test, before, after } = require('node:test');

const PI_DIR = path.join(__dirname, '..');
const TEMPLATES = ['constitucion-template.md', 'mision-template.md'];
const UTF8_BOM = Buffer.from([0xef, 0xbb, 0xbf]);
const MOJIBAKE = /[ÃÂ]/;
const REPLACEMENT = '\uFFFD';

const bytesOf = name => fs.readFileSync(path.join(PI_DIR, name));

for (const name of TEMPLATES) {
  test(`${name} starts with a UTF-8 BOM so plain-text clients do not guess a legacy charset`, () => {
    const raw = bytesOf(name);
    assert.ok(raw.subarray(0, 3).equals(UTF8_BOM), `${name}: missing UTF-8 BOM (EF BB BF)`);
    assert.ok(!raw.subarray(3, 6).equals(UTF8_BOM),
      `${name}: BOM must appear exactly once`);
  });

  test(`${name} keeps its Spanish content intact after the BOM`, () => {
    const raw = bytesOf(name);
    assert.ok(raw.subarray(0, 3).equals(UTF8_BOM), `${name}: prerequisite BOM is missing`);
    const body = raw.subarray(3);
    const text = body.toString('utf8');

    assert.ok(!text.includes(REPLACEMENT), `${name}: contains a UTF-8 replacement character`);
    assert.doesNotMatch(text, MOJIBAKE, `${name}: contains mojibake markers`);
    assert.ok(text.startsWith('# '), `${name}: the BOM must not leak into the first heading`);
    for (const phrase of ['sección', 'constitución', 'misión']) {
      assert.ok(text.includes(phrase), `${name}: lost the accented phrase "${phrase}"`);
    }
    assert.ok(Buffer.from(text, 'utf8').equals(body), `${name}: the BOM must not re-encode the body`);
  });

  test(`${name} is genuinely multibyte UTF-8, the condition that mojibakes under windows-1252`, () => {
    const body = bytesOf(name).subarray(3);
    const asLegacy = body.toString('latin1');
    assert.match(asLegacy, MOJIBAKE, `${name}: expected a legacy decode to mojibake`);
    assert.ok(asLegacy.includes('secciÃ³n'), `${name}: legacy decode must reproduce the reported "secciÃ³n"`);
  });
}

// --- Repo-wide invariant -------------------------------------------------------

const REPO_ROOT = path.join(PI_DIR, '..', '..');

function collectMarkdown(dir) {
  const found = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === 'node_modules' || entry.name.startsWith('.')) continue;
    const absolute = path.join(dir, entry.name);
    if (entry.isDirectory()) found.push(...collectMarkdown(absolute));
    else if (entry.name.endsWith('.md')) found.push(absolute);
  }
  return found;
}

const REPO_MARKDOWN = [
  path.join(REPO_ROOT, 'README.md'),
  ...collectMarkdown(path.join(REPO_ROOT, 'docs')),
  ...collectMarkdown(path.join(REPO_ROOT, 'src')),
].sort();

const KNOWN_AT_RISK = [
  'docs/pi/snake/context/CONSTITUTION.md',
  'docs/pi/snake/context/MISSION.md',
  'docs/pi/snake/design/visual-style.md',
  'docs/pi/game-flow-template.md',
  'src/modulo_01/sesion_10/README.md',
];

test('every Markdown file in README.md, docs/ and src/ carries a BOM and valid UTF-8', () => {
  assert.ok(REPO_MARKDOWN.length >= 42,
    `expected at least 42 Markdown files, found ${REPO_MARKDOWN.length}`);

  const relative = REPO_MARKDOWN.map(absolute => path.relative(REPO_ROOT, absolute));
  for (const expected of KNOWN_AT_RISK) {
    assert.ok(relative.includes(expected), `${expected} must be covered by the repo-wide check`);
  }

  const failures = [];
  for (const absolute of REPO_MARKDOWN) {
    const rel = path.relative(REPO_ROOT, absolute);
    const raw = fs.readFileSync(absolute);
    if (!raw.subarray(0, 3).equals(UTF8_BOM)) failures.push(`${rel}: missing UTF-8 BOM`);
    if (raw.subarray(3, 6).equals(UTF8_BOM)) failures.push(`${rel}: duplicate UTF-8 BOM`);
    const body = raw.subarray(3);
    const text = body.toString('utf8');
    if (text.includes(REPLACEMENT)) failures.push(`${rel}: contains a UTF-8 replacement character`);
    if (MOJIBAKE.test(text)) failures.push(`${rel}: contains mojibake markers`);
    if (!Buffer.from(text, 'utf8').equals(body)) failures.push(`${rel}: body is not valid UTF-8`);
    if (text.trim() === '') failures.push(`${rel}: body is empty`);
  }
  assert.deepEqual(failures, []);
});

// --- Real-browser reproduction ------------------------------------------------
// A legacy client is simulated with `Content-Type: text/markdown; charset=windows-1252`.
// The BOM must win over that declaration (WHATWG encoding sniffing), so the same bytes
// render as UTF-8. Without the BOM the browser honors windows-1252 and mojibakes.

const chromePath = [process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser',
].filter(Boolean).find(candidate => { try { return fs.statSync(candidate).isFile(); } catch { return false; } });
const skip = !chromePath ? 'Chrome/Chromium unavailable: browser check not performed.'
  : typeof WebSocket !== 'function' || typeof fetch !== 'function' ? 'Global fetch/WebSocket unavailable: Node 22+ required.' : false;

const fixedBytes = bytesOf(TEMPLATES[0]);
const legacyBytes = fixedBytes.subarray(0, 3).equals(UTF8_BOM) ? fixedBytes.subarray(3) : fixedBytes;
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
let chrome;
let profile;
let socket;
let server;
let port;
let sequence = 0;
const pending = new Map();

function send(method, params = {}) {
  const id = ++sequence;
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`CDP timeout: ${method}`)); }, 10000);
    pending.set(id, { resolve, reject, timer });
    socket.send(JSON.stringify({ id, method, params }));
  });
}

before(async () => {
  if (skip) return;
  server = http.createServer((request, response) => {
    const body = request.url === '/fixed' ? fixedBytes : legacyBytes;
    response.writeHead(200, { 'Content-Type': 'text/markdown; charset=windows-1252' });
    response.end(body);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  port = server.address().port;

  profile = fs.mkdtempSync(path.join(os.tmpdir(), 'markdown-encoding-browser-'));
  chrome = spawn(chromePath, ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`,
    '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--disable-gpu', 'about:blank'], { stdio: 'ignore' });
  let launchError;
  chrome.on('error', error => { launchError = error; });
  const portFile = path.join(profile, 'DevToolsActivePort');
  const deadline = Date.now() + 20000;
  while (!fs.existsSync(portFile) && Date.now() < deadline && !launchError) await sleep(50);
  if (launchError) throw launchError;
  assert.ok(fs.existsSync(portFile), 'Chrome did not expose its debugging port');
  const debugPort = Number(fs.readFileSync(portFile, 'utf8').split('\n')[0]);
  const targets = await (await fetch(`http://127.0.0.1:${debugPort}/json/list`, { signal: AbortSignal.timeout(10000) })).json();
  const page = targets.find(target => target.type === 'page');
  assert.ok(page?.webSocketDebuggerUrl);
  socket = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('CDP connection timed out')), 10000);
    socket.addEventListener('open', () => { clearTimeout(timer); resolve(); }, { once: true });
    socket.addEventListener('error', () => { clearTimeout(timer); reject(new Error('CDP connection failed')); }, { once: true });
  });
  socket.addEventListener('message', event => {
    const response = JSON.parse(event.data);
    const request = pending.get(response.id);
    if (!request) return;
    pending.delete(response.id);
    clearTimeout(request.timer);
    if (response.error) request.reject(new Error(response.error.message));
    else request.resolve(response.result);
  });
  await send('Page.enable');
});

after(async () => {
  for (const request of pending.values()) { clearTimeout(request.timer); request.reject(new Error('Browser check closed')); }
  pending.clear();
  socket?.close();
  if (chrome && chrome.exitCode === null) {
    const exited = new Promise(resolve => chrome.once('exit', resolve));
    chrome.kill('SIGKILL');
    await Promise.race([exited, sleep(3000)]);
  }
  if (profile) fs.rmSync(profile, { recursive: true, force: true, maxRetries: 10, retryDelay: 200 });
  if (server) await new Promise(resolve => server.close(resolve));
});

async function render(route) {
  await send('Page.navigate', { url: `http://127.0.0.1:${port}${route}` });
  for (let attempt = 0; attempt < 60; attempt += 1) {
    const ready = await send('Runtime.evaluate', {
      expression: `location.href.endsWith(${JSON.stringify(route)}) && document.readyState === 'complete' && document.body && document.body.innerText.length > 0`,
      returnByValue: true,
    });
    if (ready.result.value) break;
    await sleep(50);
  }
  const result = await send('Runtime.evaluate', {
    expression: `({ charset: document.characterSet, text: document.body.innerText.slice(0, 2000) })`,
    returnByValue: true,
  });
  assert.ok(!result.exceptionDetails, JSON.stringify(result.exceptionDetails));
  return result.result.value;
}

test('the BOM makes a legacy-default browser render the template as UTF-8 instead of mojibake', { skip }, async () => {
  const legacy = await render('/legacy');
  assert.equal(legacy.charset, 'windows-1252', 'the control must exercise the legacy path');
  assert.ok(legacy.text.includes('secciÃ³n'), 'the control must reproduce the reported mojibake');

  const fixed = await render('/fixed');
  assert.equal(fixed.charset, 'UTF-8', 'the UTF-8 BOM must force UTF-8 detection');
  assert.doesNotMatch(fixed.text, MOJIBAKE, 'the BOM render must not contain mojibake');
  assert.ok(fixed.text.includes('sección'), 'the BOM render must keep the accented phrase');
  assert.ok(fixed.text.includes('constitución'), 'the BOM render must keep the accented phrase');
});
