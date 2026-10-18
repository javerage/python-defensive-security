'use strict';

// Local Chrome/CDP checks with web fonts blocked: these measure fallback layout,
// not visual approval or a certification of Silkscreen, accessibility or responsiveness.
const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { test, before, after } = require('node:test');

const chromePath = [
  process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable',
  '/usr/bin/chromium', '/usr/bin/chromium-browser',
].filter(Boolean).find(candidate => {
  try { return fs.statSync(candidate).isFile(); } catch { return false; }
});
const skip = !chromePath ? 'Chrome/Chromium unavailable: browser check not performed.'
  : typeof WebSocket !== 'function' || typeof fetch !== 'function'
    ? 'Global fetch/WebSocket unavailable: Node 22+ required.' : false;
const url = pathToFileURL(path.join(__dirname, '..', 'game-over-pilot.html')).href;
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
let chrome;
let profile;
let socket;
let sequence = 0;
const pending = new Map();

function send(method, params = {}) {
  const id = ++sequence;
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      pending.delete(id);
      reject(new Error(`CDP timeout: ${method}`));
    }, 10000);
    pending.set(id, { resolve, reject, timer });
    socket.send(JSON.stringify({ id, method, params }));
  });
}

async function evaluate(expression) {
  const response = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  assert.ok(!response.exceptionDetails, JSON.stringify(response.exceptionDetails));
  return response.result.value;
}

before(async () => {
  if (skip) return;
  profile = fs.mkdtempSync(path.join(os.tmpdir(), 'snake-game-over-browser-'));
  chrome = spawn(chromePath, [
    '--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`,
    '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--disable-gpu', 'about:blank',
  ], { stdio: 'ignore' });
  let launchError;
  chrome.on('error', error => { launchError = error; });
  const portFile = path.join(profile, 'DevToolsActivePort');
  const deadline = Date.now() + 20000;
  while (!fs.existsSync(portFile) && Date.now() < deadline && !launchError) await sleep(50);
  if (launchError) throw launchError;
  assert.ok(fs.existsSync(portFile), 'Chrome did not expose its debugging port');
  const port = Number(fs.readFileSync(portFile, 'utf8').split('\n')[0]);
  const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`, { signal: AbortSignal.timeout(10000) })).json();
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
  await send('Network.enable');
  await send('Network.setBlockedURLs', { urls: ['*fonts.googleapis.com*', '*fonts.gstatic.com*'] });
  await send('Emulation.setDeviceMetricsOverride', { width: 1024, height: 768, deviceScaleFactor: 1, mobile: false });
  await send('Page.navigate', { url });
  let ready = false;
  for (let attempt = 0; attempt < 100; attempt += 1) {
    ready = await evaluate(`location.href === ${JSON.stringify(url)} && document.readyState === 'complete' && !!document.querySelector('.results-card')`);
    if (ready) break;
    await sleep(50);
  }
  assert.equal(ready, true, 'The Game Over reference did not load');
});

after(async () => {
  for (const request of pending.values()) {
    clearTimeout(request.timer);
    request.reject(new Error('Browser check closed'));
  }
  pending.clear();
  socket?.close();
  if (chrome && chrome.exitCode === null) {
    const exited = new Promise(resolve => chrome.once('exit', resolve));
    chrome.kill('SIGKILL');
    await Promise.race([exited, sleep(3000)]);
  }
  if (profile) fs.rmSync(profile, { recursive: true, force: true, maxRetries: 10, retryDelay: 200 });
});

test('Game Over preserves the reference frame, central panel and result-card geometry', { skip, timeout: 30000 }, async () => {
  const boxes = await evaluate(`['.pilot-screen', '.game-panel', '.results-card'].map(selector => {
    const r = document.querySelector(selector).getBoundingClientRect();
    return [r.x, r.y, r.width, r.height];
  })`);
  assert.deepEqual(boxes, [[0, 0, 1024, 768], [112, 80, 800, 600], [312, 318, 400, 236]]);
});

test('summary, header and explanatory text fit without clipping or overlap', { skip, timeout: 30000 }, async () => {
  const metrics = await evaluate(`(() => {
    const card = document.querySelector('.results-card').getBoundingClientRect();
    const panel = document.querySelector('.game-panel').getBoundingClientRect();
    const textBox = element => {
      const range = document.createRange();
      range.selectNodeContents(element);
      const r = range.getBoundingClientRect();
      return { left: r.left, top: r.top, right: r.right, bottom: r.bottom };
    };
    const rows = [...document.querySelectorAll('.result-row')].map(row => ({
      label: textBox(row.querySelector('dt')), value: textBox(row.querySelector('dd')),
    }));
    return {
      card: { left: card.left, right: card.right, top: card.top, bottom: card.bottom },
      panel: { left: panel.left, right: panel.right, bottom: panel.bottom }, rows,
      title: textBox(document.querySelector('.game-title')),
      subtitle: textBox(document.querySelector('.game-subtitle')),
      scene: textBox(document.querySelector('.scene-note')),
      redirect: textBox(document.querySelector('.redirect-note')),
      scope: textBox(document.querySelector('.scope-note')),
      headerTitle: textBox(document.querySelector('.panel-title')),
      headerNote: textBox(document.querySelector('.panel-note')),
    };
  })()`);
  assert.equal(metrics.rows.length, 4);
  for (const row of metrics.rows) {
    assert.ok(row.label.right + 8 <= row.value.left, 'Label and value must be separated');
    for (const box of [row.label, row.value]) {
      assert.ok(box.left >= metrics.card.left + 2 && box.right <= metrics.card.right - 2);
      assert.ok(box.top >= metrics.card.top + 2 && box.bottom <= metrics.card.bottom - 2);
    }
  }
  assert.ok(metrics.headerTitle.right + 8 <= metrics.headerNote.left);
  assert.ok(metrics.title.bottom < metrics.subtitle.top);
  assert.ok(metrics.subtitle.bottom < metrics.card.top);
  assert.ok(metrics.rows.at(-1).value.bottom < metrics.scene.top);
  assert.ok(metrics.scene.bottom < metrics.card.bottom - 4);
  assert.ok(metrics.card.bottom < metrics.redirect.top);
  assert.ok(metrics.redirect.bottom < metrics.scope.top);
  assert.ok(metrics.scope.bottom <= metrics.panel.bottom - 4);
  for (const box of [metrics.title, metrics.subtitle, metrics.redirect, metrics.scope, metrics.headerNote]) {
    assert.ok(box.left >= metrics.panel.left + 2 && box.right <= metrics.panel.right - 2);
  }
});

test('the static reference stays on Game Over after five seconds without adding controls', { skip, timeout: 30000 }, async () => {
  const snapshot = () => evaluate(`({ url: location.href, results: document.querySelector('.results-card')?.textContent,
    controls: document.querySelectorAll('button, input, form, a').length })`);
  const initial = await snapshot();
  await sleep(5500);
  assert.deepEqual(await snapshot(), initial);
  assert.equal(initial.url, url);
  assert.equal(initial.controls, 0);
});
