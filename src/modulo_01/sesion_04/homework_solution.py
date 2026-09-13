"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 04 (PyDefSec)
FILE: homework_solution.py (reference for evaluacion_alerta.py)
PURPOSE: Review one synthetic local practice alert with conditionals:
         check a volume rule with if/else, then assign a three-level
         review priority with an if/elif/else chain on the average
         response time, ordered from the most demanding threshold to
         the least demanding one.
NOTE: Homework after class, outside the 60 minutes. Create
      evaluacion_alerta.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your own.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom sequential script (no functions, no try/except,
      no collections, no type hints, no main(), no loops, no imports).
    - Only input() plus int()/float() conversion from Session 02, one
      if/else plus one short if/elif/else chain; only the >=
      comparison, plus a bool variable used directly as a condition.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
    - If non-numeric text is typed, the program stops with ValueError.
      That interruption is expected behavior; it is not caught with
      try/except in this session.
==============================================================================

Conceptual sequence: evidence -> boolean expression -> condition ->
executed branch -> message/recommendation.
Homework chain: input -> conversion -> decision -> communication,
while the class exercise isolates decision -> communication.

IMPORTANT: Thresholds >= 10 and >= 1000.0 / >= 500.0 are teaching rules
of this lab for practicing conditionals. They are not universal
standards, and they prove no attack. This summary organizes local
practice evidence so the reviewer can prioritize human review. It blocks
nothing, isolates nothing, and contacts nothing.
"""

# ==============================================================================
# STEP 1: Evidence via keyboard (input plus conversion, Session 02).
# ==============================================================================
# The evidence is typed at runtime: error lines as int and average
# response as float. Typing 14 and 850.0 reproduces the verified
# example. Non-numeric text stops the program with ValueError
# (expected; not caught with try/except in this session).
raw_error_lines = input("Líneas de error: ")
error_lines = int(raw_error_lines)
raw_avg_response_ms = input("Respuesta promedio en ms: ")
avg_response_ms = float(raw_avg_response_ms)

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Boolean expression plus simple decision (if/else on one bool).
# ==============================================================================
# The comparison checks the explicit lab volume rule (10 or more error
# lines) and produces a bool: whether the rule was met. The bool itself
# is the condition of the if/else below.
many_errors = error_lines >= 10

if many_errors:
    volume_message = "Regla de volumen cumplida: 10 o más líneas de error"
else:
    volume_message = "Regla de volumen no cumplida: menos de 10 líneas de error"

# ==============================================================================
# STEP 3: Three-level priority (if/elif/else chain on one number).
# ==============================================================================
# Teaching thresholds for the average response time: 1000.0 separates the
# few cases the team reviews today, and 500.0 separates the ones queued
# for review this week. Python runs ONLY the first branch whose condition
# is True, so the most demanding condition (>= 1000.0) comes first.
if avg_response_ms >= 1000.0:
    risk_label = "HIGH"
    review_action = "Revisar hoy con un mentor"
elif avg_response_ms >= 500.0:
    risk_label = "MEDIUM"
    review_action = "Agendar revisión esta semana"
else:
    risk_label = "LOW"
    review_action = "Conservar en el registro local"

# ==============================================================================
# STEP 4: Communication. Simple readable summary for the reviewer.
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
