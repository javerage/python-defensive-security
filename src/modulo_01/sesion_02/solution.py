"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 02 (PyDefSec)
FILE: solution.py (reference for perfil_operador.py)
PURPOSE: Review practical experience before an incident simulation:
         register name, introductory labs plus average hours, estimate total
         practice hours, check the 10-hour program rule, show a summary.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 and create perfil_operador.py manually.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom sequential script (no functions, no try/except,
      no collections, no type hints, no main()).
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: text input -> conversion -> calculation ->
decision -> communication.
"""

# STEP 1: Text input. input() ALWAYS returns str, even for digits.
# The name identifies whose progress this is; labs plus hours describe it.
operator_name = input("Escribe el nombre del operador: ")
raw_completed_labs = input("Escribe cuantos laboratorios completo: ")
raw_hours_per_lab = input("Escribe el promedio de horas por laboratorio: ")

# STEP 2: Conversion. Text that already holds a number becomes a number.
completed_labs = int(raw_completed_labs)
hours_per_lab = float(raw_hours_per_lab)

# STEP 3: Calculation. Multiplying estimates accumulated practice.
total_practice_hours = completed_labs * hours_per_lab

# STEP 4: Decision. The comparison checks the explicit program rule
# (10.0 hours) plus produces a bool: whether the requirement was met.
ready_for_next = total_practice_hours >= 10.0

# STEP 5: Communication. Readable evidence for reviewing the decision.
print("--- Resumen del operador ---")
print(f"Nombre: {operator_name}")
print(f"Laboratorios completados: {completed_labs}")
print(f"Horas por laboratorio: {hours_per_lab}")
print(f"Horas totales de practica: {total_practice_hours}")
print(f"Listo para la siguiente practica: {ready_for_next}")
