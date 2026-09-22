"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 05 (PyDefSec)
FILE: solution.py (reference for config_check.py)
PURPOSE: Validate ONE synthetic local lab configuration with compound
          logic: a range check with and, an allowed-set check with or,
          an emptiness check with !=, an absence check with is None,
          and a final verdict combining every partial result.
STORY: You are part of the team preparing the local defensive lab
       before each practice day. Another teammate hands you a setup
       sheet with one configuration: local port 18080, path
       configs/lab.conf, level WARNING, and a reviewer-note slot.
       Each field can block a reproducible practice or leave the
       review incomplete, and a single generic message would hide
       which field must be fixed. This program decides whether the
       configuration is ready for review or needs specific fixes,
       one message per field plus a combined verdict. It only
       validates synthetic data and recommends: it opens no ports,
       touches no files, contacts no network, and confirms no attack.
DOMAIN -> CODE MAPPING (read before coding):
       case datum | variable | question/rule | bool + message | verdict share
       port 18080 | target_port | inside 1-65535? (and) | port_ok + port_message | part of config_ready
       path configs/lab.conf | config_path vs known_config_path | empty? known? (if/elif/else) | path_ok + path_message | part of config_ready
       level WARNING | log_level | one of three? (or) | level_ok + level_message | part of config_ready
       note absent (None) | reviewer_note | no note arrived? (is None) | note_missing + note_message | informs the review
       combined | config_ready, needs_fix, final_decision | every partial True? (and/not) | verdict + recommendation | final decision
NOTE ON NONE: None means absence of value. It serves a purpose
      similar to null in other languages, but it is Python's
      unique None object. The idiom is reviewer_note is None:
      is checks identity with that unique object, so == None is
      not taught as an alternative. None is not "" or 0 or False:
      those are present values even when falsey. Here "no note
      arrived" (None) is not "an empty note arrived" ("").
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
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      config_check.py manually.
WHY NO FUNCTION HERE: the curriculum names this step validar_config
      with early returns, but functions (def/return) arrive in
      Session 11. Until then every check runs top-to-bottom in one
      linear script: each partial result is stored in its own bool
      variable, and the final verdict reads those variables. Same
      decisions, no function call yet.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no collections, no loops, no imports, no regex).
    - Only and/or/not plus comparisons; is None only to detect absence.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: field -> bool check -> specific message ->
combined verdict -> recommendation.
"""

# ==============================================================================
# STEP 1: Configuration under review (given) plus operator identity.
# ==============================================================================
# One synthetic local practice configuration. Nothing is decided yet.
target_port = 18080
config_path = "configs/lab.conf"
known_config_path = "configs/lab.conf"
log_level = "WARNING"
reviewer_note = None

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Partial checks. Each check stores one bool plus one message.
# ==============================================================================
# Port range of this lab (teaching rule, not a universal standard):
# from 1 to 65535. Both comparisons must hold, so they join with and.
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

# Simulated known path: a non-empty value is not enough, it must also
# match the lab path recorded above. No disk is touched in this session.
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

# Allowed levels of this lab (teaching set): one single match is enough,
# so the three comparisons join with or.
level_ok = log_level == "INFO" or log_level == "WARNING" or log_level == "ERROR"

if level_ok:
    level_message = "Nivel válido: organiza la revisión humana"
else:
    level_message = "Nivel inválido: debe ser INFO, WARNING o ERROR"

# Absence check: None means absence of value ("no note arrived"),
# similar in purpose to null elsewhere but Python's unique None
# object. is None checks identity; "" or 0 or False are present
# values instead, so "no note arrived" is not "an empty note".
note_missing = reviewer_note is None

if note_missing:
    note_message = "Sin nota del revisor: se continúa sin comentarios"
else:
    note_message = "Nota del revisor registrada"

# ==============================================================================
# STEP 3: Combined verdict. and stops at the first False (short-circuit);
# with 18080, a known path, and WARNING, every partial result is True.
# ==============================================================================
config_ready = port_ok and path_ok and level_ok
needs_fix = not config_ready

if config_ready:
    final_decision = "Configuración lista para la práctica local"
else:
    final_decision = "Configuración detenida: corrige los campos marcados"

# ==============================================================================
# STEP 4: Communication (given). Readable console summary for the reviewer.
# The program recommends; it blocks nothing, isolates nothing,
# and contacts nothing.
# ==============================================================================
print("--- Resumen de la configuración ---")
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
