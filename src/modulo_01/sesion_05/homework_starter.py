"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 05 (PyDefSec)
FILE: homework_starter.py (guided skeleton for service_config_review.py)
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
      Complete each task marked TODO. This skeleton compiles plus runs;
      PENDING marks unfinished work, and replaced placeholders give the
      expected summary. Check homework_solution.py only after trying
      alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as service_config_review.py
    plus run:
        python service_config_review.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

BEFORE CODING, ANALYZE (read the rules first, without running code):
    - Which keyboard value feeds the range check after int(), and which
      two comparisons must both hold for port_ok?
    - Which typed text feeds the or chain, and why is one single match
      enough for level_ok?
    - Which combined verdict runs for 8080 plus INFO, and what does its
      recommendation ask a human to do (and not do)?

LIMIT: typing non-numeric text for the port stops the program with
ValueError. That interruption is expected; do not catch it with
try/except here. The homework integrates input -> conversion ->
decision -> communication, while the class exercise isolates
decision -> communication.

DELIVERY: explain aloud the chain field -> bool check -> specific
message -> combined verdict -> recommendation for every field, why and
needs every part True while or needs a single match, and how each
result reaches the summary. Local practice data only. The program
recommends; it blocks nothing, isolates nothing, and contacts nothing.

IMPORTANT: The range 1-65535, the known path configs/lab.conf, and the
levels INFO/WARNING/ERROR are teaching rules of this lab for practicing
compound logic. They are not universal standards, and True only means
that the matching lab rule holds.
==============================================================================

Conceptual sequence: field -> bool check -> specific message ->
combined verdict -> recommendation.
Homework chain: input -> conversion -> decision -> communication,
while the class exercise isolates decision -> communication.
"""

# ==============================================================================
# STEP 1: Evidence via keyboard (TODO). Session 02 input plus conversion.
# ==============================================================================
# The evidence is typed at runtime. Typing 8080 and INFO reproduces the
# verified example. If non-numeric text is typed for the port, the
# program stops with ValueError (expected behavior; not caught with
# try/except here).
# TODO 1.1: replace "PENDING" with input("Puerto local: ")
raw_target_port = "PENDING"
# TODO 1.2: replace 0 with int(raw_target_port)
target_port = 0
# TODO 1.3: replace "PENDING" with input("Nivel de registro: ")
log_level = "PENDING"

# Fixed lab path for this review (given, no disk is touched).
config_path = "configs/lab.conf"
known_config_path = "configs/lab.conf"
reviewer_note = None

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Partial checks (TODO). One bool plus one message per field.
# ==============================================================================
# TODO 2.1: Check the lab port range joining both comparisons with and.
# NOTE: the equivalent chained form 1 <= target_port <= 65535 is valid,
# idiomatic, compact Python for a value between both bounds, taught later
# as an alternative; it is not the main form here because it hides the
# and this session practices (math readability and less repetition versus
# explicit visibility of the logical operator).
port_ok = False  # TODO: replace False with target_port >= 1 and target_port <= 65535

# TODO 2.2: Decide with an if/else whose condition is port_ok itself.
port_message = "PENDING"  # TODO: set it with if/else (see the rules)

# TODO 2.3: Decide the fixed path with if/elif/else (empty is invalid,
# different from known_config_path is invalid, matching it is valid).
# Branch shape: one if, zero or more elif, optional else; only the
# first true branch runs (see the S04 HIGH/MEDIUM/LOW recall).
path_message = "PENDING"  # TODO: set it with if/elif/else
path_ok = False  # TODO: set it inside the same branches

# TODO 2.4: Check the allowed lab levels joining the three == with or.
level_ok = False  # TODO: replace False with the or chain (see the rules)

# TODO 2.5: Decide with an if/else whose condition is level_ok itself.
level_message = "PENDING"  # TODO: set it with if/else (see the rules)

# TODO 2.6: Detect absence with is None.
note_missing = False  # TODO: replace False with reviewer_note is None

# TODO 2.7: Decide with an if/else whose condition is note_missing itself.
note_message = "PENDING"  # TODO: set it with if/else (see the rules)

# ==============================================================================
# STEP 3: Combined verdict (TODO). and stops at the first False.
# ==============================================================================
# TODO 3.1: Combine every partial result with and.
config_ready = False  # TODO: replace False with port_ok and path_ok and level_ok

# TODO 3.2: Negate the verdict with not.
needs_fix = False  # TODO: replace False with not config_ready

# TODO 3.3: Decide with an if/else whose condition is config_ready itself.
final_decision = "PENDING"  # TODO: set it with if/else (see the rules)

# ==============================================================================
# STEP 4: Communication (given). Readable summary for the reviewer.
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
