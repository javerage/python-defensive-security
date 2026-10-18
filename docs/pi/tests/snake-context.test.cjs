'use strict';

// Structural regression tests for the documented Snake project context.
// These tests read Markdown files as data only: they never execute Markdown,
// the game, an agent or any command, and they make no behavioral claims.

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { test } = require('node:test');

const CONTEXT_DIR = path.join(__dirname, '..', 'snake', 'context');

const REQUIRED_FILES = [
  'README.md',
  'CONSTITUTION.md',
  'MISSION.md',
  'TECH-STACK.md',
  'ROADMAP.md',
  'MEMORY.md',
  'specs/inicio.md',
  'AGENTS.example.md',
];

function readContextFile(relative) {
  return fs.readFileSync(path.join(CONTEXT_DIR, relative), 'utf8');
}

function markdownLinkTargets(content) {
  const targets = [];
  const linkPattern = /\[[^\]]*\]\(([^)]+)\)/g;
  let match;
  while ((match = linkPattern.exec(content)) !== null) {
    targets.push(match[1].trim());
  }
  return targets;
}

function isExternal(target) {
  return /^(?:https?:|mailto:|tel:|#)/i.test(target);
}

test('all documented context files exist as non-empty Markdown with an H1', () => {
  for (const relative of REQUIRED_FILES) {
    const absolute = path.join(CONTEXT_DIR, relative);
    assert.ok(fs.existsSync(absolute), `Missing context file: ${relative}`);
    const content = fs.readFileSync(absolute, 'utf8').trim();
    assert.ok(content.length > 0, `Empty context file: ${relative}`);
    assert.match(content, /^#\s+\S/, `Missing H1 title in ${relative}`);
  }
});

test('no active AGENTS.md is created next to the illustrative example', () => {
  assert.equal(fs.existsSync(path.join(CONTEXT_DIR, 'AGENTS.md')), false);
});

test('every relative link inside the context docs resolves on disk', () => {
  let checked = 0;
  for (const relative of REQUIRED_FILES) {
    const filePath = path.join(CONTEXT_DIR, relative);
    for (const rawTarget of markdownLinkTargets(fs.readFileSync(filePath, 'utf8'))) {
      if (isExternal(rawTarget)) continue;
      const withoutAnchor = rawTarget.split('#')[0].split('?')[0];
      if (!withoutAnchor) continue;
      const resolved = path.resolve(path.dirname(filePath), decodeURI(withoutAnchor));
      assert.ok(fs.existsSync(resolved), `Broken link in ${relative}: ${rawTarget}`);
      checked += 1;
    }
  }
  assert.ok(checked > 0, 'Expected at least one relative link to be verified');
});

test('context marks the application as documented but not implemented', () => {
  const readme = readContextFile('README.md');
  const inicio = readContextFile('specs/inicio.md');
  const roadmap = readContextFile('ROADMAP.md');
  assert.match(readme, /no implementad/i);
  assert.match(inicio, /no implementad/i);
  assert.match(roadmap, /no implementad/i);
  for (const [name, content] of [['README.md', readme], ['specs/inicio.md', inicio], ['ROADMAP.md', roadmap]]) {
    assert.doesNotMatch(content, /el juego funciona/i, `${name} must not claim the game works`);
    assert.doesNotMatch(content, /ya se puede jugar/i, `${name} must not claim playability`);
    assert.doesNotMatch(content, /(?:MVP|implementaci[oó]n) (?:completad|terminad)/i, `${name} must not claim completion`);
  }
});

test('public context avoids private paths and commit hashes', () => {
  for (const relative of REQUIRED_FILES) {
    const content = readContextFile(relative);
    assert.doesNotMatch(content, /data\/private/i, `Private path in ${relative}`);
    assert.doesNotMatch(content, /\b[0-9a-f]{7,40}\b/, `Possible public commit hash in ${relative}`);
  }
});

test('tech stack records TypeScript and browser without inventing a framework or versions', () => {
  const tech = readContextFile('TECH-STACK.md');
  assert.match(tech, /TypeScript/);
  assert.match(tech, /navegador/i);
  assert.match(tech, /no elegid/i);
  assert.match(tech, /no confirmad/i);
  assert.doesNotMatch(tech, /\b(?:React|Vue|Angular|Svelte|Vite|webpack|Rollup|Parcel)\b/i);
  assert.doesNotMatch(tech, /\b\d+\.\d+\.\d+\b/, 'Version number invented in tech stack');
});

test('roadmap is a product plan and never claims to be a lesson plan', () => {
  const roadmap = readContextFile('ROADMAP.md');
  assert.match(roadmap, /plan de producto/i);
  assert.match(roadmap, /no (?:es|constituye) un plan de clases/i);
  assert.doesNotMatch(roadmap, /plan de lecci[oó]n|curr[ií]culum/i);
});

test('accepted pilots are recorded as visual reference only', () => {
  const combined = `${readContextFile('README.md')}\n${readContextFile('MEMORY.md')}`;
  assert.match(combined, /referencia visual/i);
  assert.match(combined, /no implementad|sin juego implementado/i);
  assert.match(combined, /responsive/i);
  assert.match(combined, /compilaci/i);
});

test('open decisions stay pending with a named decision owner', () => {
  const memory = readContextFile('MEMORY.md');
  const roadmap = readContextFile('ROADMAP.md');
  assert.match(memory, /dudas abiertas/i);
  assert.match(memory, /persona responsable/i);
  for (const pending of [/puntos por comida/i, /velocidad inicial/i, /perder una vida/i,
    /empates/i, /almacenamiento/i, /validaci[oó]n/i, /tama[ñn]o m[ií]nimo/i, /skins/i]) {
    assert.match(memory, pending, `MEMORY.md must list pending decision ${pending}`);
  }
  assert.match(roadmap, /persona responsable/i);
  assert.match(roadmap, /fase afectada/i);
});

test('confirmed game facts are recorded without changing them', () => {
  const memory = readContextFile('MEMORY.md');
  assert.match(memory, /cinco niveles/i);
  assert.match(memory, /15 puntos/i);
  assert.match(memory, /hace crecer/i);
  assert.match(memory, /estrictamente mayor/i);
  assert.match(memory, /empate/i);
  assert.match(memory, /despu[eé]s de la jugabilidad/i);
});

test('agents example is illustrative navigation and invents no commands', () => {
  const agents = readContextFile('AGENTS.example.md');
  assert.match(agents, /ejemplo ilustrativo/i);
  assert.match(agents, /no es una instrucci[oó]n activa/i);
  assert.doesNotMatch(agents, /npm run|npx |yarn |pnpm |bun run|node --test|docker build|make build/i);
  assert.doesNotMatch(agents, /```(?:bash|sh|shell|console|zsh)/i);
});

test('classroom context is present and distinguished from the product mission', () => {
  for (const relative of ['README.md', 'MEMORY.md']) {
    const content = readContextFile(relative);
    assert.match(content, /contexto de aula|ejercicio de clase/i, `${relative} must name the classroom context`);
    assert.match(content, /30 a 45/i, `${relative} must state the activity time target`);
    assert.match(content, /no se ha (?:medido|observado)/i, `${relative} must deny an observed duration`);
  }
  assert.match(readContextFile('MISSION.md'), /experiencia de quien juega/i);
});
