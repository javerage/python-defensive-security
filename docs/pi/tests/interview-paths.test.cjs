'use strict';

// Static contracts for the guided interview path guidance in the public
// constitution/mission teaching materials (S9).
//
// Scope and limits: these checks pin wording invariants about the working root,
// relative paths, the agreed context subfolder, the optional existing sources and
// the no-write interview, across the two reusable templates and the two public HTML
// guides. They read strings from files; they cannot prove that a conversational
// agent follows the guidance, creates no directory, or that a client loads a
// document. No runtime agent RED can be derived from string matching, so the
// published documents remain the only subject under test.
//
// The tests read only public files, so they run without the ignored private teacher
// guides.

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { test } = require('node:test');

const PI_DIR = path.join(__dirname, '..');
const read = name => fs.readFileSync(path.join(PI_DIR, name), 'utf8');

const CONSTITUTION_DOCS = ['constitucion-template.md', 'constitucion-proyecto.html'];
const MISSION_DOCS = ['mision-template.md', 'mision-proyecto.html'];
const INTERVIEW_DOCS = [...CONSTITUTION_DOCS, ...MISSION_DOCS];
const HTML_DOCS = ['constitucion-proyecto.html', 'mision-proyecto.html'];

const occurrences = (text, token) => text.split(token).length - 1;

// The copyable prompts are the operative interface: what a student pastes to Pi.
// Prose may illustrate with an example folder; the prompt blocks must not hardcode it.
function preBlocks(name) {
  const doc = read(name);
  const blocks = [...doc.matchAll(/<pre><code>([\s\S]*?)<\/code><\/pre>/g)].map(match => match[1]);
  assert.ok(blocks.length > 0, `${name}: expected at least one copyable prompt block`);
  return blocks;
}

test('every interview guide treats the open project folder as the working root for relative paths', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /raíz de trabajo/i, `${name}: must name the working root`);
    assert.match(doc, /rutas?[^.]*relativ/i, `${name}: must explain relative paths`);
  }
});

test('the context subfolder is confirmed once as the destination, not negotiated repeatedly', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /subcarpeta de contexto/i, `${name}: must name the context subfolder`);
    assert.match(doc, /una sola vez/i, `${name}: the destination is confirmed once`);
    assert.match(doc, /antes de guardar/i, `${name}: confirmation happens before saving`);
    assert.match(doc, /ejemplo ilustrativo/i, `${name}: the example folder is illustrative`);
    assert.match(doc, /no una carpeta obligatoria/i, `${name}: the example folder is not mandatory`);
  }
});

test('the interview creates no files, folders or code, and folder creation is confirmed separately', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /no se crean ni modifican archivos ni carpetas/i, `${name}: no writes during interview`);
    assert.match(doc, /no se ejecuta c[oó]digo/i, `${name}: no code execution during interview`);
    assert.match(doc, /crear la carpeta[^.]*confirm/i, `${name}: folder creation is confirmed separately`);
    assert.match(doc, /guardado autorizado/i, `${name}: folder creation belongs to the authorized save`);
  }
});

test('the exact destination path is shown and confirmed before saving', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /ruta prevista/i, `${name}: must show the intended path`);
    assert.match(doc, /ruta exacta/i, `${name}: must confirm the exact destination`);
    assert.match(doc, /antes de guardar/i, `${name}: confirmation happens before saving`);
  }
});

test('optional existing sources stay optional and «ninguno» only covers them', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /fuentes existentes opcionales/i, `${name}: existing sources are optional`);
    assert.match(doc, /«Ninguno» se refiere solo a esas fuentes opcionales/i,
      `${name}: «ninguno» must not cover the required template or constitution`);
  }
});

test('optional sources are authorized by enumeration, never by a self-referential conditional', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.equal(/si\s+(?:los|las)\s+autoriz[oa]s?/i.test(doc), false,
      `${name}: must not ask the agent to evaluate “si los autorizo/autorizas”`);
  }
  for (const name of HTML_DOCS) {
    const prompts = preBlocks(name).join('\n');
    assert.match(prompts, /fuentes existentes de esta lista/i,
      `${name}: the enumerated list itself must express the authorization scope`);
  }
});

test('the interview does not require future SDD artifacts', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /no exige[^.]*hoja de ruta/i, `${name}: roadmap is not a prerequisite`);
    assert.match(doc, /especificaciones futuras/i, `${name}: future specs are not a prerequisite`);
  }
});

test('the template can stay outside the project at an authorized location without copying', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /no es obligatorio copiarla/i, `${name}: copying the template is not required`);
    assert.match(doc, /acceso externo/i, `${name}: no blanket external access`);
  }
});

test('operative prompts use the current open project as the relative base and ask when it is ambiguous', () => {
  for (const name of HTML_DOCS) {
    const doc = read(name);
    const prompts = preBlocks(name).join('\n');
    assert.equal(occurrences(prompts, '[RUTA REAL DEL PROYECTO]'), 0,
      `${name}: the operative prompt must not ask unconditionally for the project root`);
    assert.equal(occurrences(doc, '[RUTA REAL]'), 0,
      `${name}: must not reuse a bare absolute-root placeholder`);
    assert.match(prompts, /proyecto abierto/i, `${name}: must default to the open project`);
    assert.match(prompts, /relativ/i, `${name}: must express paths relative to it`);
    assert.match(prompts, /no puedes determinar[^.]*preg[úu]ntame|preg[úu]ntame[^.]*(?:ambigu|raíz)/i,
      `${name}: must ask when the open project or root is unknown`);
  }
});

test('operative prompts read only explicit paths and never open a separate folder negotiation', () => {
  for (const name of HTML_DOCS) {
    const prompts = preBlocks(name).join('\n');
    assert.equal(prompts.includes('docs/contexto/'), false,
      `${name}: the operative prompt must not hardcode the example folder`);
    assert.equal(/prop[oó]n o pregunta la subcarpeta|reutil[ií]zala una vez acordada/i.test(prompts), false,
      `${name}: the prompt must not negotiate a subfolder before the interview`);
    assert.match(prompts, /no busques archivos por tu cuenta/i,
      `${name}: must read only the paths the human provides`);
    assert.match(read(name), /docs\/contexto\//, `${name}: the illustrative example stays in prose`);
  }
});

test('constitution prompt reads an existing CONSTITUTION.md only from an explicit path', () => {
  const prompts = preBlocks('constitucion-proyecto.html').join('\n');
  assert.equal(prompts.includes('en esa subcarpeta confirmada'), false,
    'constitution: must not check a negotiated subfolder for an existing file');
  assert.match(prompts, /no busques archivos por tu cuenta/i,
    'constitution: must read only the paths the human provides');
  assert.equal(prompts.includes('docs/contexto/'), false,
    'constitution: the operative prompt must not hardcode the example folder');
});

test('mission interview prompt keeps distinct required-source placeholders', () => {
  const prompts = preBlocks('mision-proyecto.html').join('\n');
  assert.match(prompts, /\[RUTA REAL DE LA PLANTILLA\]/, 'mission: template placeholder');
  assert.match(prompts, /\[RUTA REAL DE LA CONSTITUCIÓN\]/, 'mission: real constitution placeholder');
  assert.match(prompts, /\[RUTAS REALES O “NINGUNO”\]/, 'mission: optional-sources placeholder');
  assert.match(prompts, /fuentes existentes de esta lista/i, 'mission: authorized sources are enumerated');
});

test('mission final-read prompt uses the real saved mission and the concrete constitution path', () => {
  const prompts = preBlocks('mision-proyecto.html').join('\n');
  assert.match(prompts, /\[RUTA REAL DE MISSION\.md\]/, 'mission: actual saved mission path');
  assert.match(prompts, /\[RUTA REAL DE LA CONSTITUCIÓN\]/, 'mission: concrete constitution path');
  assert.match(prompts, /proyecto abierto|relativ/i, 'mission: relative base');
  assert.equal(prompts.includes('docs/contexto/'), false,
    'mission: final-read prompt must not hardcode the example folder');
  assert.equal(prompts.includes('[RUTA REAL DE LOS DOCUMENTOS GUARDADOS]'), false,
    'mission: the merged placeholder must be gone');
});

test('the illustrative relative example path stays in the guidance', () => {
  for (const name of INTERVIEW_DOCS) {
    assert.match(read(name), /docs\/contexto\//, `${name}: must keep an illustrative relative example`);
  }
});

test('constitution preparation does not require an existing constitution', () => {
  for (const name of CONSTITUTION_DOCS) {
    const doc = read(name);
    assert.match(doc, /puede no existir todavía/i, `${name}: the constitution need not exist yet`);
    assert.match(doc, /fuente estructural/i, `${name}: the template is the structural source`);
    assert.match(doc, /documento real/i, `${name}: the constitution is the project's real document`);
  }
});

test('mission guidance separates the structural constitution template from the real project constitution', () => {
  const doc = read('mision-template.md');
  assert.match(doc, /plantilla estructural de constituci[oó]n/i,
    'mission template: must name the structural constitution template');
  assert.match(doc, /no la constituci[oó]n del proyecto/i,
    'mission template: must not equate the structural template with the real constitution');
  assert.match(doc, /constituci[oó]n aplicable real/i,
    'mission template: must still require the real constitution');
});

test('mission preparation requires the real constitution and stops instead of inventing', () => {
  for (const name of MISSION_DOCS) {
    const doc = read(name);
    assert.match(doc, /requiere leer la constitución aplicable/i, `${name}: must require the real constitution`);
    assert.match(doc, /detente y pregunta/i, `${name}: must stop and ask when a required source is missing`);
    assert.match(doc, /plantilla de misión y de la constitución aplicable/i,
      `${name}: must name the mission template plus the applicable constitution`);
    assert.match(doc, /misi[oó]n no puede cambiar la constituci[oó]n/i, `${name}: mission cannot change the constitution`);
  }
});

test('interview, draft, explicit approval, limited save and read-only check remain intact', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /entrevista/i, `${name}: interview`);
    assert.match(doc, /borrador/i, `${name}: draft`);
    assert.match(doc, /aprobaci[oó]n expl[ií]cita|autorizaci[oó]n expl[ií]cita/i, `${name}: explicit approval`);
    assert.match(doc, /solo lectura/i, `${name}: read-only verification`);
  }
});
