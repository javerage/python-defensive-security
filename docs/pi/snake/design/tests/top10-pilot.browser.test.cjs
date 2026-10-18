'use strict';

// Same dependency-free CDP protocol as the accepted pilots. Web fonts are blocked:
// these checks prove fallback geometry, not approval with the real Silkscreen font.
const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { test, before, after } = require('node:test');
const chromePath = [process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser',
].filter(Boolean).find(candidate => { try { return fs.statSync(candidate).isFile(); } catch { return false; } });
const skip = !chromePath ? 'Chrome/Chromium unavailable: browser check not performed.'
  : typeof WebSocket !== 'function' || typeof fetch !== 'function' ? 'Global fetch/WebSocket unavailable: Node 22+ required.' : false;
const url = pathToFileURL(path.join(__dirname, '..', 'top10-pilot.html')).href;
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
let chrome;
let profile;
let socket;
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
async function evaluate(expression) {
  const response = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  assert.ok(!response.exceptionDetails, JSON.stringify(response.exceptionDetails));
  return response.result.value;
}

before(async () => {
  if (skip) return;
  profile = fs.mkdtempSync(path.join(os.tmpdir(), 'snake-top10-browser-'));
  chrome = spawn(chromePath, ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`,
    '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--disable-gpu', 'about:blank'], { stdio: 'ignore' });
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
    ready = await evaluate(`location.href === ${JSON.stringify(url)} && document.readyState === 'complete' && document.querySelectorAll('tbody tr').length === 10`);
    if (ready) break;
    await sleep(50);
  }
  assert.equal(ready, true, 'The Top 10 reference did not load');
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
});

test('Top 10 keeps the approved panel, table, ten row heights and button geometry', { skip }, async () => {
  const boxes = await evaluate(`['.pilot-screen', '.game-panel', '.ranking', '.btn'].map(selector => {
    const r = document.querySelector(selector).getBoundingClientRect(); return [r.x,r.y,r.width,r.height];
  })`);
  assert.deepEqual(boxes, [[0, 0, 1024, 768], [112, 80, 800, 600], [212, 196, 600, 354], [412, 580, 200, 52]]);
  assert.deepEqual(await evaluate(`[...document.querySelectorAll('tbody tr')].map(row => row.getBoundingClientRect().height)`), Array(10).fill(32));
});

test('all ranking text, long names and footer notes fit without overlapping', { skip }, async () => {
  const metrics = await evaluate(`(() => {
    const box = element => { const r = element.getBoundingClientRect(); return {left:r.left,top:r.top,right:r.right,bottom:r.bottom}; };
    const text = element => { const r = document.createRange(); r.selectNodeContents(element); return box(r); };
    return { cells: [...document.querySelectorAll('th,td')].map(cell => ({cell:box(cell),text:text(cell)})),
      heading: text(document.querySelector('.game-title')), subtitle:text(document.querySelector('.game-subtitle')),
      table:box(document.querySelector('.ranking')), button:box(document.querySelector('.btn')), label:text(document.querySelector('.btn')),
      returnNote:text(document.querySelector('.return-note')), scope:text(document.querySelector('.scope-note')),
      panel:box(document.querySelector('.game-panel')), header:[...document.querySelectorAll('.game-panel-head span')].map(text) };
  })()`);
  assert.equal(metrics.cells.length, 44);
  for (const { cell, text } of metrics.cells) {
    assert.ok(text.left >= cell.left && text.right <= cell.right, 'Cell text must fit its column');
    assert.ok(text.top >= cell.top && text.bottom <= cell.bottom, 'Cell text must fit its row');
  }
  assert.ok(metrics.header[0].right + 8 < metrics.header[1].left);
  assert.ok(metrics.heading.bottom <= metrics.subtitle.top && metrics.subtitle.bottom < metrics.table.top);
  assert.ok(metrics.table.bottom < metrics.button.top && metrics.button.bottom < metrics.returnNote.top);
  assert.ok(metrics.returnNote.bottom < metrics.scope.top && metrics.scope.bottom <= metrics.panel.bottom - 2);
  assert.ok(metrics.label.left > metrics.button.left && metrics.label.right < metrics.button.right);
});

test('Nueva partida shows inverted hover/pressed and separate keyboard focus without navigation or writes', { skip }, async () => {
  const snapshot = () => evaluate(`({url:location.href, table:document.querySelector('.ranking').textContent,
    local:JSON.stringify(localStorage), session:JSON.stringify(sessionStorage), buttons:document.querySelectorAll('button').length})`);
  const initial = await snapshot();
  const style = () => evaluate(`(() => { const b=document.querySelector('.btn'),s=getComputedStyle(b),r=b.getBoundingClientRect();
    return {background:s.backgroundColor,color:s.color,radius:s.borderRadius,outline:s.outlineColor,outlineWidth:s.outlineWidth,offset:s.outlineOffset,shadow:s.boxShadow,box:[r.x,r.y,r.width,r.height]}; })()`);
  await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: 0, y: 0 });
  const normal = await style();
  assert.equal(normal.background, 'rgb(126, 231, 135)');
  assert.equal(normal.color, 'rgb(13, 17, 23)');
  assert.equal(normal.radius, '8px');
  await send('Input.dispatchKeyEvent', { type: 'keyDown', key: 'Tab', code: 'Tab', windowsVirtualKeyCode: 9 });
  await send('Input.dispatchKeyEvent', { type: 'keyUp', key: 'Tab', code: 'Tab', windowsVirtualKeyCode: 9 });
  assert.equal(await evaluate(`document.activeElement === document.querySelector('.btn')`), true);
  const focused = await style();
  assert.equal(focused.outline, 'rgb(242, 204, 96)');
  assert.equal(focused.outlineWidth, '2px');
  assert.equal(focused.offset, '2px');
  await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: 512, y: 606 });
  const hovered = await style();
  assert.equal(hovered.background, normal.color);
  assert.equal(hovered.color, normal.background);
  await send('Input.dispatchMouseEvent', { type: 'mousePressed', button: 'left', clickCount: 1, x: 512, y: 606 });
  const pressed = await style();
  assert.equal(pressed.background, hovered.background);
  assert.equal(pressed.color, hovered.color);
  assert.match(pressed.shadow, /inset/);
  assert.deepEqual(pressed.box, normal.box);
  await send('Input.dispatchMouseEvent', { type: 'mouseReleased', button: 'left', clickCount: 1, x: 512, y: 606 });
  await evaluate(`document.querySelector('.btn').focus()`);
  await send('Input.dispatchKeyEvent', { type: 'keyDown', key: 'Enter', code: 'Enter', windowsVirtualKeyCode: 13 });
  await send('Input.dispatchKeyEvent', { type: 'keyUp', key: 'Enter', code: 'Enter', windowsVirtualKeyCode: 13 });
  assert.deepEqual(await snapshot(), initial);
  assert.equal(initial.buttons, 1);
});
