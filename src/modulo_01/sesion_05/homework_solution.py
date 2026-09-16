"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 05 (PyDefSec)
FILE: homework_solution.py (reference for service_config_review.py)
PURPOSE: Review one synthetic local backup-service configuration with
          compound logic: read the port and the level from the keyboard,
          convert the port, check the lab range with and, the allowed
          levels with or, the fixed lab path with ==, absence with
          is None, and combine every partial result into one verdict.
STORY: You are the assistant leaving the local backup-service
       configuration ready before its nightly review (a different
       case from class). Another teammate leaves you the service
       notice: you record whose work it is, ask the local port and
       the level from the keyboard, keep the fixed lab path, and
       check every field for one combined verdict. Each field can
       leave the service without a complete review, and a generic
       message would hide what must be fixed. The night reviewer
       needs one place saying ready or stopped plus which field to
       fix. The program only validates synthetic data and
       recommends: it opens no ports, touches no files, contacts
       no network, and confirms no attack.
DOMAIN -> CODE MAPPING (read before coding):
       case datum | variable | question/rule | bool + message | verdict share
       typed port (8080) | raw_target_port -> target_port (after int) | inside 1-65535? (and) | port_ok + port_message | part of config_ready
       fixed path configs/lab.conf | config_path vs known_config_path | matches known? (if/elif/else) | path_ok + path_message | part of config_ready
       typed level (INFO) | log_level | one of three? (or) | level_ok + level_message | part of config_ready
       note absent (None) | reviewer_note | no note arrived? (is None) | note_missing + note_message | informs the review
       combined | config_ready, needs_fix, final_decision | every partial True? (and/not) | verdict + recommendation | final decision
NOTE ON NONE: None means absence of value (purpose similar to
      null elsewhere, but Python's unique None object). Detect it
      with reviewer_note is None: is checks identity, so == None
      is not taught. None is not "" or 0 or False (present
      values). Here "no note arrived" (None) is not "an empty
      note arrived" ("").
NOTE ON IDENTITY VS EQUALITY: is / is not ask identity (whether
      it is the same object, like the unique None object);
      == / != ask value equality (whether the content matches,
      like the level text). Presence uses the idiomatic negative
      form value is not None, never not value is None. Strings
      compare with ==: Python has no .equals() for this comparison,
      and is with strings is never used. None, "", 0, and False
      can all be falsey, but they do not mean the same thing.
      Quick map (concept -> minimal example -> use):
        reviewer_note is None -> absence ("no note arrived").
        reviewer_note is not None -> presence ("a note arrived").
        log_level == "WARNING" -> value equality between strings.
        log_level != "INFO" -> value inequality between strings.
        is with strings, .equals(), == None -> never used here.
NOTE ON student_name: student_name is not None and
      student_name == "Juan" is valid but redundant when only the
      value is asked: student_name == "Juan" alone is enough. The
      first part only makes sense as a guard before operating on a
      possible None (checking presence before operating on that
      value, e.g. before calling a method on it). It is not added
      to the main program: not a requirement, not a TODO.
PREDICTIONS (read, then check against the rules): with
      reviewer_note = None, reviewer_note is not None is False
      (no presence); with log_level = "", the or chain of this
      session is False (empty text matches no allowed option).
NOTE ON INPUT: input() returns text; pressing Enter with no typing
      gives "", not None. That is why the level uses string
      equality (== with or, != for inequality) while a missing
      note uses identity with None (is None / is not None).
NOTE: Homework after class, outside the 60 minutes. Create
      service_config_review.py manually in your Session 01 project.
      Use this file only as backup guidance after attempting the task
      on your own.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no collections, no loops, no imports, no regex).
    - Only input() plus int() conversion from Session 02, and/or/not
      plus comparisons from Session 05; is None only to detect absence.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
    - If non-numeric text is typed for the port, the program stops with
      ValueError. That interruption is expected behavior; it is not
      caught with try/except in this session.
==============================================================================

Conceptual sequence: field -> bool check -> specific message ->
combined verdict -> recommendation.
Homework chain: input -> conversion -> decision -> communication,
while the class exercise isolates decision -> communication.

IMPORTANT: The range 1-65535, the known path configs/lab.conf, and the
levels INFO/WARNING/ERROR are teaching rules of this lab for practicing
compound logic. They are not universal standards, and True only means
that the matching lab rule holds. This summary organizes local practice
evidence so the reviewer can prioritize human review. It blocks nothing,
isolates nothing, and contacts nothing.
"""

# ==============================================================================
# STEP 1: Evidence via keyboard (input plus conversion, Session 02).
# ==============================================================================
# The evidence is typed at runtime: the local port as int and the log
# level as text. Typing 8080 and INFO reproduces the verified example.
# Non-numeric text for the port stops the program with ValueError
# (expected; not caught with try/except in this session).
raw_target_port = input("Puerto local: ")
target_port = int(raw_target_port)
log_level = input("Nivel de registro: ")

# Fixed lab path for this review (given): the backup job always reads
# the same known configuration file. No disk is touched in this session.
config_path = "configs/lab.conf"
known_config_path = "configs/lab.conf"
reviewer_note = None

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Partial checks. One bool plus one message per field.
# ==============================================================================
# Both range comparisons must hold, so they join with and.
# Equivalent chained form 1 <= target_port <= 65535 is valid, idiomatic,
# compact Python expressing the value is between both bounds; it is taught
# later as an alternative once both comparisons are understood. It is not
# the main form here because it hides the and this session practices.
# Tradeoff: mathematical readability and less repetition versus explicit
# visibility of the logical operator.
port_ok = target_port >= 1 and target_port <= 65535

if port_ok:
    port_message = "Puerto válido: dentro del rango 1-65535"
else:
    port_message = "Puerto inválido: fuera del rango 1-65535"

# Fixed path: valid only because it matches the known lab path.
# Branch shape: one if, zero or more elif, optional else; only the
# first true branch runs (same shape as the S04 HIGH/MEDIUM/LOW recall).
if config_path == "":
    path_message = "Ruta inválida: está vacía"
    path_ok = False
elif config_path != known_config_path:
    path_message = "Ruta inválida: no es una ruta conocida del laboratorio"
    path_ok = False
else:
    path_message = "Ruta válida: archivo conocido del laboratorio"
    path_ok = True

# One single match is enough, so the three comparisons join with or.
level_ok = log_level == "INFO" or log_level == "WARNING" or log_level == "ERROR"

if level_ok:
    level_message = "Nivel válido: organiza la revisión humana"
else:
    level_message = "Nivel inválido: usa INFO, WARNING o ERROR"

# Absence of value ("no note arrived"): purpose similar to null
# elsewhere, but Python's unique None object. is None checks
# identity; "" or 0 or False are present values instead.
note_missing = reviewer_note is None

if note_missing:
    note_message = "Sin nota del revisor: se continúa sin comentarios"
else:
    note_message = "Nota del revisor registrada"

# ==============================================================================
# STEP 3: Combined verdict. and stops at the first False (short-circuit).
# ==============================================================================
config_ready = port_ok and path_ok and level_ok
needs_fix = not config_ready

if config_ready:
    final_decision = "Configuración lista para la práctica local"
else:
    final_decision = "Configuración detenida: corrige los campos marcados"

# ==============================================================================
# STEP 4: Communication. Readable summary for the reviewer.
# ==============================================================================
print("--- Resumen del servicio ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Puerto local: {target_port}")
print(f"Chequeo de puerto: {port_message}")
print(f"Ruta de configuración: {config_path}")
print(f"Chequeo de ruta: {path_message}")
print(f"Nivel de registro: {log_level}")
print(f"Chequeo de nivel: {level_message}")
print(f"Nota del revisor: {note_message}")
print(f"Configuración lista: {config_ready}")
print(f"Requiere corrección: {needs_fix}")
print(f"Decisión final: {final_decision}")
