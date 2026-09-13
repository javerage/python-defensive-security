"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 04 (PyDefSec)
FILE: solution.py (reference for incident_classifier.py)
PURPOSE: Classify ONE synthetic local lab observation with conditionals:
         check a volume rule with if/else, then assign a three-level
         review priority with an if/elif/else chain ordered from the
         most demanding condition to the least demanding one.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      incident_classifier.py manually.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom sequential script (no functions, no try/except,
      no collections, no type hints, no main(), no loops, no imports).
    - Only one if/else plus one short if/elif/else chain; only the >=
      comparison, plus a bool variable used directly as a condition.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: evidence -> boolean expression -> condition ->
executed branch -> message/recommendation.
"""

# ==============================================================================
# STEP 1: Evidence (given). One synthetic local lab observation.
# ==============================================================================
# The practice notebook records 9 failed access attempts on the local
# training machine. The count is the evidence; nothing is decided yet.
failed_attempts = 9

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Boolean expression plus simple decision (if/else on one bool).
# ==============================================================================
# The comparison checks the explicit lab volume rule (5 or more attempts)
# and produces a bool: whether the rule was met. The bool itself is the
# condition of the if/else below: True runs the first branch, False runs
# the second one. Only one branch ever runs.
many_failed_attempts = failed_attempts >= 5

if many_failed_attempts:
    volume_message = "Regla de volumen cumplida: 5 o más intentos"
else:
    volume_message = "Regla de volumen no cumplida: menos de 5 intentos"

# ==============================================================================
# STEP 3: Three-level priority (if/elif/else chain on one number).
# ==============================================================================
# Training thresholds of this lab (teaching rules, not universal
# standards): 10 separates the few cases the team reviews today, and 5
# separates the ones queued for review this week. They prove no attack;
# they only order human review of local practice data.
# Python runs ONLY the first branch whose condition is True, so the chain
# goes from the most demanding condition (>= 10) to the least demanding
# one (>= 5). Reversed order would trap 12 at MEDIUM and HIGH would never
# run (see the silent error in the student material).
if failed_attempts >= 10:
    risk_label = "HIGH"
    review_action = "Revisar hoy con un mentor"
elif failed_attempts >= 5:
    risk_label = "MEDIUM"
    review_action = "Agendar revisión esta semana"
else:
    risk_label = "LOW"
    review_action = "Conservar en el registro local"

# ==============================================================================
# STEP 4: Communication (given). Simple readable console summary.
# ==============================================================================
# Labels plus recommendations for human review. The program recommends;
# it blocks nothing, isolates nothing, and contacts nothing.
print("--- Resumen del incidente ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Intentos fallidos: {failed_attempts}")
print(f"Regla de volumen cumplida: {many_failed_attempts}")
print(f"Mensaje de volumen: {volume_message}")
print(f"Nivel de riesgo: {risk_label}")
print(f"Revisión recomendada: {review_action}")
