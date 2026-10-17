const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

function loadViewer() {
  const html = fs.readFileSync(path.join(__dirname, '..', 'game-flow-snake.html'), 'utf8');
  const elements = new Map();
  function element() {
    return {
      children: [], style: {}, attributes: {}, listeners: {}, textContent: '',
      classList: { add() {}, remove() {} },
      set innerHTML(value) { this.content = value; this.children = []; },
      get innerHTML() { return this.content || ''; },
      appendChild(child) { this.children.push(child); },
      removeChild(child) { this.children.splice(this.children.indexOf(child), 1); },
      get lastChild() { return this.children.at(-1); },
      setAttribute(key, value) { this.attributes[key] = value; },
      addEventListener(event, callback) { this.listeners[event] = callback; },
    };
  }
  for (const [, id] of html.matchAll(/\bid="([^"]+)"/g)) elements.set(id, element());
  const context = vm.createContext({
    document: {
      getElementById: id => elements.get(id) || null,
      createElement: element,
    },
    setTimeout() {},
  });
  // Real browsers reserve window.history; never let a stub hide that collision.
  Object.defineProperty(context, 'history', { value: Object.freeze({}), writable: false });
  vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context);
  function click(event, destination) {
    const index = context.TRANSITIONS.filter(t => t.from === context.current)
      .findIndex(t => t.event === event && (!destination || t.to === destination));
    assert.notEqual(index, -1, `Missing ${event} -> ${destination} from ${context.current}`);
    elements.get('event-list').children[index].children[0].listeners.click();
  }
  return { context, elements, click };
}

test('both endings lead to the correct animation and preserve the result summary', () => {
  for (const [event, destination, animation] of [
    ['Collision', 'Results', /game over/i],
    ['FinalLevelCompleted', 'Victory', /victoria/i],
  ]) {
    const { context, elements, click } = loadViewer();
    click('StartRequested', 'Playing');
    click(event, destination);
    assert.equal(context.current, destination);
    for (const text of [animation, /nombre/i, /puntaje/i, /nivel/i, /velocidad/i]) {
      assert.match(elements.get('last-response').innerHTML, text);
    }
  }
});

test('each ending explains all three ranking cases and the five-second wait', () => {
  for (const ending of ['Results', 'Victory']) {
    const { context } = loadViewer();
    const routes = context.TRANSITIONS.filter(t => t.from === ending);
    assert.equal(routes.length, 3);
    for (const route of routes) assert.match(route.condition, /5 segundos/);
    const freeSlot = routes.find(t => /menos de diez/.test(t.condition));
    assert.ok(freeSlot);
    assert.equal(freeSlot.to, 'Highscores');
    assert.match(freeSlot.response, /cero/);
    const better = routes.find(t => /estrictamente mayor/.test(t.condition));
    assert.ok(better);
    assert.equal(better.to, 'Highscores');
    assert.match(better.response, /diez/);
    const rejected = routes.find(t => /menor o igual/.test(t.condition));
    assert.ok(rejected);
    assert.equal(rejected.to, 'AwaitingStart');
    assert.match(rejected.response, /no se registra/i);
  }
});

test('ranking routes work through buttons, diagram, back and restart', () => {
  for (const ending of ['Results', 'Victory']) {
    for (const destination of ['Highscores', 'AwaitingStart']) {
      const { context, elements, click } = loadViewer();
      click('StartRequested', 'Playing');
      click(ending === 'Victory' ? 'FinalLevelCompleted' : 'Collision', ending);
      click('AnimationFinished', destination);
      assert.equal(context.current, destination);
      assert.equal(elements.get(`n-${destination}`).attributes.fill, '#1d4ed8');
      elements.get('back-btn').listeners.click();
      assert.equal(context.current, ending);
      elements.get('restart-btn').listeners.click();
      assert.equal(context.current, 'AwaitingStart');
      assert.equal(elements.get('path-log').children.length, 0);
    }
  }
});

test('existing name, play and in-game events retain their navigation', () => {
  const { context, elements, click } = loadViewer();
  click('NameProvided', 'AwaitingStart');
  click('StartRequested', 'Playing');
  for (const event of ['MovementContinues', 'DirectionRequested', 'FoodConsumed', 'LevelAdvance', 'Collision']) {
    click(event, 'Playing');
    assert.equal(context.current, 'Playing');
  }
  assert.match(elements.get('last-response').innerHTML, /automáticamente/);
  assert.equal(elements.get('flow-table').children.length, context.TRANSITIONS.length);
  for (const transition of context.TRANSITIONS) {
    assert.ok(context.STATES[transition.from]);
    assert.ok(context.STATES[transition.to]);
    assert.ok(elements.has(`n-${transition.to}`));
    assert.ok(elements.has(transition.edge));
  }
});

test('Nueva partida returns from either ending through top 10 and waits for play', () => {
  for (const ending of ['Results', 'Victory']) {
    const { context, elements, click } = loadViewer();
    click('NameProvided', 'AwaitingStart');
    click('StartRequested', 'Playing');
    click(ending === 'Victory' ? 'FinalLevelCompleted' : 'Collision', ending);
    click('AnimationFinished', 'Highscores');
    const buttons = elements.get('event-list').children;
    assert.equal(buttons.length, 1);
    assert.match(buttons[0].children[0].innerHTML, /<strong>Nueva partida<\/strong>/);
    click('NewGameRequested', 'AwaitingStart');
    assert.equal(context.current, 'AwaitingStart');
    const response = elements.get('last-response').innerHTML;
    for (const rule of [/nombre escrito/i, /precargado y editable/i, /no se reutiliza/i,
      /play.*espacio/i, /no se arrastra/i]) assert.match(response, rule);
    assert.equal(elements.get('n-AwaitingStart').attributes.fill, '#1d4ed8');
    assert.equal(elements.get('e-new-game').style.opacity, '1');
    elements.get('back-btn').listeners.click();
    assert.equal(context.current, 'Highscores');
    click('NewGameRequested', 'AwaitingStart');
    click('NameProvided', 'AwaitingStart');
    click('StartRequested', 'Playing');
    assert.equal(context.current, 'Playing');
  }
});

test('all returns explain typed-name retention and never reuse generated names', () => {
  const { context, elements, click } = loadViewer();
  const returns = context.TRANSITIONS.filter(t => t.to === 'AwaitingStart' && t.from !== 'AwaitingStart');
  assert.equal(returns.length, 3);
  for (const route of returns) {
    for (const rule of [/nombre escrito/i, /precargado y editable/i, /no se reutiliza/i,
      /play.*espacio/i, /no se arrastra/i]) assert.match(route.response, rule);
  }
  click('StartRequested', 'Playing');
  assert.match(elements.get('last-response').innerHTML, /player_YYYYMMDD_HHmmss_SSS/);
  click('Collision', 'Results');
  click('AnimationFinished', 'AwaitingStart');
  assert.equal(context.current, 'AwaitingStart');
  click('StartRequested', 'Playing');
  assert.match(elements.get('last-response').innerHTML, /Se genera player_YYYYMMDD_HHmmss_SSS/);
});
