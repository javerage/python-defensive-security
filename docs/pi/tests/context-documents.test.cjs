// Static document contracts for the public constitution/mission teaching materials.
//
// Scope and limits: these checks pin wording invariants across the reusable templates,
// the public HTML guides and the concrete Snake examples. They are read-only string/links
// contracts; they cannot prove that a conversational agent behaves as described, that a
// client loads a document, or that any permission is enforced at runtime. No runtime
// game or agent RED can be derived from string matching, so the documents themselves
// remain the only subject under test here.

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { test } = require('node:test');

const PI_DIR = path.join(__dirname, '..');
const read = name => fs.readFileSync(path.join(PI_DIR, name), 'utf8');

const PUBLIC_DOCS = [
  'constitucion-template.md',
  'mision-template.md',
  'snake/context/CONSTITUTION.md',
  'snake/context/MISSION.md',
  'constitucion-proyecto.html',
  'mision-proyecto.html',
  'index.html',
];

const INTERVIEW_DOCS = [
  'constitucion-template.md',
  'mision-template.md',
  'constitucion-proyecto.html',
  'mision-proyecto.html',
];

// Return the body under a markdown heading up to the next level-2 heading.
function section(text, headingPrefix) {
  const start = text.indexOf(headingPrefix);
  assert.notEqual(start, -1, `missing section ${headingPrefix}`);
  const rest = text.slice(start + headingPrefix.length);
  const next = rest.search(/^## /m);
  return next === -1 ? rest : rest.slice(0, next);
}

test('constitution governs rules and delegates purpose/scope to the mission', () => {
  const doc = read('constitucion-template.md');

  const purpose = section(doc, '## 2.');
  assert.match(purpose, /referencia/i, 'section 2 must be a reference, not a duplicated purpose');
  assert.match(purpose, /misi[oó]n/i, 'section 2 must point to the mission');
  assert.match(purpose, /mision-template\.md/, 'section 2 must link the mission template');
  assert.doesNotMatch(purpose, /Personas destinatarias\s*:/i, 'audience belongs to the mission');
  assert.doesNotMatch(purpose, /Resultado esperado\s*:/i, 'outcome belongs to the mission');

  const scope = section(doc, '## 5.');
  assert.match(scope, /misi[oó]n/i, 'product scope must be referenced from the mission');
  assert.match(scope, /excluid|fuera|no autoriza/i, 'authorized action exclusions must stay');

  for (const role of [/principios/i, /responsabilidad/i, /autorizaci[oó]n/i, /datos/i, /evidencia/i, /cambios/i]) {
    assert.match(doc, role, `constitution must keep its governance responsibility: ${role}`);
  }
});

test('mission keeps purpose, audience, scope and success without redefining rules', () => {
  const doc = read('mision-template.md');
  for (const part of [
    /[Pp]roblema u oportunidad/,
    /[Pp]ersonas destinatarias/,
    /[Mm]isi[oó]n en una frase/,
    /[Rr]esultado deseado/,
    /[Aa]lcance y exclusiones/,
  ]) {
    assert.match(doc, part, `mission must keep: ${part}`);
  }
  assert.match(doc, /constituci[oó]n/i, 'mission must reference the constitution');
  assert.match(doc, /no (?:reemplaza|modifica|cambia|concede)/i, 'mission must not redefine the constitution rules');
  assert.doesNotMatch(doc, /sandbox/i, 'mission is not a sandbox clause');
});

test('public templates reference each other', () => {
  assert.match(read('constitucion-template.md'), /mision-template\.md/);
  assert.match(read('mision-template.md'), /constitucion-template\.md/);
});

test('public HTML guides link their counterpart', () => {
  assert.match(read('constitucion-proyecto.html'), /href="mision-proyecto\.html"/);
  assert.match(read('mision-proyecto.html'), /href="constitucion-proyecto\.html"/);
});

test('guides and portal use the concrete Snake documents as their examples', () => {
  for (const [guide, example] of [
    ['constitucion-proyecto.html', 'CONSTITUTION.md'],
    ['mision-proyecto.html', 'MISSION.md'],
  ]) {
    const href = `href="snake/context/${example}"`;
    assert.ok(read(guide).includes(href), `${guide}: must link its concrete Snake example`);
    assert.ok(read('index.html').includes(href), `portal: must link ${example}`);
    assert.match(read(guide), /ejemplo concreto.*Snake/i);
  }
  assert.match(read('snake/context/CONSTITUTION.md'), /MISSION\.md/);
  assert.match(read('snake/context/MISSION.md'), /CONSTITUTION\.md/);
});

test('interview contracts never re-ask confirmed context', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /[Nn]o vuelv[ae]s? a preguntar lo ya confirmado/, `${name}: must not re-ask confirmed facts`);
    assert.match(doc, /[uú]nicamente lo que falte o sea ambiguo/, `${name}: must ask only missing or ambiguous decisions`);
  }
});

test('interview, draft, explicit approval, limited save and read-only check are preserved', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /entrevista/i, `${name}: interview`);
    assert.match(doc, /borrador/i, `${name}: draft`);
    assert.match(doc, /aprobaci[oó]n expl[ií]cita|autorizaci[oó]n expl[ií]cita/i, `${name}: explicit approval`);
    assert.match(doc, /solo lectura/i, `${name}: read-only verification`);
    assert.match(doc, /no cambia|conserva el original|no sobrescrib|sin cambios/i, `${name}: cancel/reject leaves files unchanged`);
  }
});

test('honesty safeguards are preserved: pending unknowns, explicit approval, no invented facts', () => {
  for (const name of INTERVIEW_DOCS) {
    const doc = read(name);
    assert.match(doc, /Pendiente de decisi[oó]n/i, `${name}: unknowns stay pending`);
    assert.match(doc, /invent/i, `${name}: no invented facts`);
  }
});

test('retired Session 10 examples are absent from disk and live public guidance', () => {
  for (const retired of ['constitucion-sesion-10.md', 'mision-sesion-10.md']) {
    assert.equal(fs.existsSync(path.join(PI_DIR, retired)), false, `${retired}: must be retired`);
    for (const name of PUBLIC_DOCS) {
      assert.equal(read(name).includes(retired), false, `${name}: must not reference ${retired}`);
    }
  }
  for (const name of ['constitucion-proyecto.html', 'mision-proyecto.html', 'index.html']) {
    assert.doesNotMatch(read(name), /S10|Sesi[oó]n 10|matrix_review\.py/i,
      `${name}: must not present the retired teaching example`);
  }
});

test('local links in the public context documents resolve to real files', () => {
  for (const name of PUBLIC_DOCS) {
    const filePath = path.join(PI_DIR, name);
    const doc = fs.readFileSync(filePath, 'utf8');
    const targets = [
      ...[...doc.matchAll(/\]\(([^)\s]+)\)/g)].map(match => match[1]),
      ...[...doc.matchAll(/href="([^"]+)"/g)].map(match => match[1]),
    ];
    assert.ok(targets.length > 0, `${name}: expected at least one local link`);
    for (const target of targets) {
      if (/^(?:https?:|mailto:|#)/.test(target)) continue;
      const resolved = path.resolve(path.dirname(filePath), target.split('#')[0]);
      assert.ok(fs.existsSync(resolved), `${name}: broken local link -> ${target}`);
    }
  }
});

test('public context documents never link private teacher material', () => {
  for (const name of PUBLIC_DOCS) {
    assert.doesNotMatch(read(name), /data\/private|guia_docente/i, `${name}: must not expose private material`);
  }
});
