"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 04 (PyDefSec)
FILE: starter.py (guided skeleton for incident_classifier.py)
PURPOSE: Classify ONE synthetic local lab observation with conditionals:
         check a volume rule with if/else, then assign a three-level
         review priority with an if/elif/else chain ordered from the
         most demanding condition to the least demanding one.
NOTE: The repository is only a backup. Create incident_classifier.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected summary.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as incident_classifier.py and run:
        python incident_classifier.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the rules table in your student material first: it holds the
    evidence value, the volume rule, and both training thresholds in the
    order you must test them. No part of this skeleton shows the final
    expressions, branches, or results.
==============================================================================

Conceptual sequence: evidence -> boolean expression -> condition ->
executed branch -> message/recommendation.
"""

# ==============================================================================
# STEP 1: Evidence (given). One synthetic local lab observation.
# ==============================================================================
# The practice notebook records the failed access attempts of one local
# training case. The count is the evidence; nothing is decided yet.
failed_attempts = 9

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Boolean expression plus simple decision (TODO).
# ==============================================================================
# TODO 2.1: Build a bool from the evidence with the volume rule from the
# materials (one comparison, no extra operators).
many_failed_attempts = False  # TODO: build the bool from failed_attempts

# TODO 2.2: Write an if/else whose condition is that bool (used directly,
# without comparing it again). Each branch sets volume_message to the
# message stated in the materials for its case.
volume_message = "PENDING"  # TODO: decide it with if/else

# ==============================================================================
# STEP 3: Three-level priority (TODO). One number, most demanding first.
# ==============================================================================
# TODO 3: Write an if/elif/else chain that tests the same count against
# both training thresholds from the rules table, from the most demanding
# threshold to the least demanding one, and sets risk_label plus
# review_action to the values stated there for the matching branch.
# Python runs ONLY the first branch whose condition is True.
risk_label = "PENDING"  # TODO: classify it with if/elif/else
review_action = "PENDING"  # TODO: recommend review with the same chain

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
