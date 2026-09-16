"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 05 (PyDefSec)
FILE: starter.py (guided skeleton for config_check.py)
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
       which field must be fixed. Your program decides whether the
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
       Abstract first with the story plus the mapping, then code
       following field -> bool check -> specific message ->
       combined verdict -> recommendation.
NOTE ON NONE: None means absence of value. It serves a purpose
      similar to null in other languages, but it is Python's
      unique None object. Detect it with reviewer_note is None:
      is checks identity with that unique object, so == None is
      not taught as an alternative. None is not "" or 0 or False:
      those are present values. Here "no note arrived" (None) is
      not "an empty note arrived" ("").
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
NOTE: The repository is only a backup. Create config_check.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected summary.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as config_check.py and run:
        python config_check.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the rules table in your student material first: it holds the
    port range, the known lab path, and the allowed levels in the order
    you must check them. No part of this skeleton shows the final
    expressions, messages, or verdict.

WHY NO FUNCTION HERE: the curriculum names this step validar_config,
    but functions (def/return) arrive in Session 11. Until then every
    check runs top-to-bottom in one linear script. Same decisions,
    no function call yet.
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
# STEP 2: Partial checks (TODO). One bool plus one message per field.
# ==============================================================================
# TODO 2.1: Check the lab port range (1 to 65535) joining both
# comparisons with and. With 18080 the result is True.
# NOTE: the equivalent chained form 1 <= target_port <= 65535 is valid,
# idiomatic, compact Python for a value between both bounds, taught later
# as an alternative; it is not the main form here because it hides the
# and this session practices (math readability and less repetition versus
# explicit visibility of the logical operator).
port_ok = False  # TODO: build it with target_port >= 1 and target_port <= 65535

# TODO 2.2: Decide port_message with if/else over port_ok itself.
port_message = "PENDING"  # TODO: decide it with if/else (see the rules)

# TODO 2.3: Decide the path with if/elif/else: empty ("") is invalid,
# different from known_config_path is invalid, matching it is valid.
# Set path_message plus path_ok in each branch.
# Branch shape: one if, zero or more elif, optional else; only the
# first true branch runs (see the S04 HIGH/MEDIUM/LOW recall).
path_message = "PENDING"  # TODO: decide it with if/elif/else
path_ok = False  # TODO: set it inside the same branches

# TODO 2.4: Check the allowed lab levels joining the three == with or.
# With WARNING the result is True.
level_ok = False  # TODO: build it with or (see the rules)

# TODO 2.5: Decide level_message with if/else over level_ok itself.
level_message = "PENDING"  # TODO: decide it with if/else (see the rules)

# TODO 2.6: Detect absence with is None (None means absence of value:
# "no note arrived", not "an empty note"; None is not "" or 0 or False).
note_missing = False  # TODO: build it with reviewer_note is None

# TODO 2.7: Decide note_message with if/else over note_missing itself.
note_message = "PENDING"  # TODO: decide it with if/else (see the rules)

# ==============================================================================
# STEP 3: Combined verdict (TODO). and stops at the first False.
# ==============================================================================
# TODO 3.1: Combine every partial result with and.
config_ready = False  # TODO: build it with port_ok and path_ok and level_ok

# TODO 3.2: Negate the verdict with not.
needs_fix = False  # TODO: build it with not config_ready

# TODO 3.3: Decide final_decision with if/else over config_ready itself.
final_decision = "PENDING"  # TODO: decide it with if/else (see the rules)

# ==============================================================================
# STEP 4: Communication (given). Readable console summary for the reviewer.
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
