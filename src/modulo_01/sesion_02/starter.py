"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 02 (PyDefSec)
FILE: starter.py (guided skeleton for operator_profile.py)
PURPOSE: Review practical experience before an incident simulation:
         register name, introductory labs plus average hours, estimate total
         practice hours, check the 10-hour program rule, show a summary.
NOTE: The repository is only a backup. Create operator_profile.py manually
      in your Session 01 project and complete each task marked TODO.
      This skeleton compiles and runs; replaced placeholders give the
      expected summary.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as operator_profile.py and run:
        python operator_profile.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels an input prompt safely.
==============================================================================

Conceptual sequence: text input -> conversion -> calculation ->
decision -> communication.
"""

# ==============================================================================
# STEP 1: Text input (given). input() ALWAYS returns str, even for digits.
# ==============================================================================
# Before an incident simulation, the team reviews practical experience.
# The name identifies whose progress this is; labs plus hours describe it.
operator_name = input("Escribe el nombre del operador: ")
raw_completed_labs = input("Escribe cuantos laboratorios completo: ")
raw_hours_per_lab = input("Escribe el promedio de horas por laboratorio: ")

# ==============================================================================
# STEP 2: Conversion (TODO). Text that already holds a number becomes a number.
# ==============================================================================
# TODO 2.1: Convert raw_completed_labs to int (whole laboratories).
completed_labs = 0  # TODO: replace 0 with int(raw_completed_labs)

# TODO 2.2: Convert raw_hours_per_lab to float (hours can have decimals).
hours_per_lab = 0.0  # TODO: replace 0.0 with float(raw_hours_per_lab)

# ==============================================================================
# STEP 3: Calculation (TODO). Multiplying estimates accumulated practice.
# ==============================================================================
# TODO 3: Multiply laboratories by average hours per laboratory.
total_practice_hours = 0.0  # TODO: replace 0.0 with completed_labs * hours_per_lab

# ==============================================================================
# STEP 4: Decision (TODO). The comparison produces a bool (True or False).
# ==============================================================================
# TODO 4: Check the explicit program rule (10.0-hour minimum). The result
# reports whether the requirement was met; it authorizes nothing by itself.
ready_for_next = False  # TODO: replace False with total_practice_hours >= 10.0

# ==============================================================================
# STEP 5: Communication (given). Simple readable console summary.
# ==============================================================================
print("--- Resumen del operador ---")
print(f"Nombre: {operator_name}")
print(f"Laboratorios completados: {completed_labs}")
print(f"Horas por laboratorio: {hours_per_lab}")
print(f"Horas totales de practica: {total_practice_hours}")
print(f"Listo para la siguiente practica: {ready_for_next}")
