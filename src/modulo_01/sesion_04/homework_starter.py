"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 04 (PyDefSec)
FILE: homework_starter.py (guided skeleton for alert_evaluation.py)
PURPOSE: Review one synthetic local practice alert with conditionals:
         check a volume rule with if/else, then assign a three-level
         review priority with an if/elif/else chain on the average
         response time, ordered from the most demanding threshold to
         the least demanding one.
NOTE: Homework after class, outside the 60 minutes. Create
      alert_evaluation.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      summary. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as alert_evaluation.py plus run:
        python alert_evaluation.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

BEFORE CODING, ANALYZE (read the rules first, without running code):
    - Which keyboard value feeds the volume bool after int(), and which
      rule does >= 10 check?
    - Which converted float feeds the three-level chain, and why must
      >= 1000.0 be tested before >= 500.0?
    - Which branch runs for 850.0 milliseconds, and what does its
      recommendation ask a human to do (and not do)?

LIMIT: typing non-numeric text stops the program with ValueError.
That interruption is expected; do not catch it with try/except here.
The homework integrates input -> conversion -> decision ->
communication, while the class exercise isolates decision ->
communication.

DELIVERY: explain aloud the chain evidence -> boolean expression ->
condition -> executed branch -> message/recommendation for both
decisions, why the chain order matters, and how each result reaches
the summary. Local practice data only. The program recommends; it
blocks nothing, isolates nothing, and contacts nothing.

IMPORTANT: Thresholds >= 10 and >= 1000.0 / >= 500.0 are teaching rules
of this lab for practicing conditionals. They are not universal
standards, and they prove no attack.
==============================================================================

Conceptual sequence: evidence -> boolean expression -> condition ->
executed branch -> message/recommendation.
Homework chain: input -> conversion -> decision -> communication,
while the class exercise isolates decision -> communication.
"""

# ==============================================================================
# STEP 1: Evidence via keyboard (TODO). Session 02 input plus conversion.
# ==============================================================================
# The evidence is typed at runtime. Typing 14 and 850.0 reproduces the
# verified example. If non-numeric text is typed, the program stops
# with ValueError (expected behavior; not caught with try/except here).
# TODO 1.1: replace "PENDING" with input("Líneas de error: ")
raw_error_lines = "PENDING"
# TODO 1.2: replace 0 with int(raw_error_lines)
error_lines = 0
# TODO 1.3: replace "PENDING" with input("Respuesta promedio en ms: ")
raw_avg_response_ms = "PENDING"
# TODO 1.4: replace 0.0 with float(raw_avg_response_ms)
avg_response_ms = 0.0

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Boolean expression plus simple decision (TODO).
# ==============================================================================
# TODO 2.1: Check the explicit lab volume rule (10 or more error lines).
many_errors = False  # TODO: replace False with error_lines >= 10

# TODO 2.2: Decide with an if/else whose condition is many_errors itself.
volume_message = "PENDING"  # TODO: set it with if/else (see the rules)

# ==============================================================================
# STEP 3: Three-level priority (TODO). Most demanding threshold first.
# ==============================================================================
# TODO 3: Classify avg_response_ms with an if/elif/else chain testing
# >= 1000.0 before >= 500.0, and set risk_label plus review_action to the
# values of the matching branch. Python runs ONLY the first True branch.
risk_label = "PENDING"  # TODO: replace "PENDING" with the chain result
review_action = "PENDING"  # TODO: replace "PENDING" with the chain result

# ==============================================================================
# STEP 4: Communication (given). Simple readable summary for the reviewer.
# ==============================================================================
print("--- Resumen de la alerta ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Líneas de error: {error_lines}")
print(f"Regla de volumen cumplida: {many_errors}")
print(f"Mensaje de volumen: {volume_message}")
print(f"Respuesta promedio: {avg_response_ms} ms")
print(f"Nivel de riesgo: {risk_label}")
print(f"Revisión recomendada: {review_action}")
