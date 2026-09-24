"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 09 (PyDefSec)
FILE: solution.py (reference for event_loop.py)
PURPOSE: Count 6 ERROR entries in 20 synthetic local events twice:
         once with for and once with while under guaranteed
         termination, then verify both counts match.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      event_loop.py manually.
WHY ONE LEVEL ONLY: nested loops arrive in Session 10. Until then
      each version visits the flat list of 20 exactly once, with no
      break/continue required and no functions.
PEDAGOGICAL RESTRICTIONS:
    - Single-level loops only: for over the list, while with counter,
      len() as the bound, comparison of both totals.
    - No nested loops, no functions, no try/except, no imports,
      no files, no network.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: flat list (20 events) -> for count -> while
count with progress -> comparison -> verified summary.
"""

# ==============================================================================
# STEP 1: Evidence (given). Twenty synthetic local events plus operator
# identity.
# ==============================================================================
event_log = [
    "INFO", "ERROR", "WARNING", "INFO", "ERROR",
    "INFO", "WARNING", "ERROR", "INFO", "WARNING",
    "INFO", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "ERROR", "INFO",
]

# Identity of whose verification this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Eventos registrados: {len(event_log)}")

# ==============================================================================
# STEP 2: Counts. The for visits each event and stops by itself; the
# while repeats while its condition holds and must progress each turn.
# ==============================================================================
# First verdict: for needs no manual index, so it cannot hang.
for_count = 0
for event in event_log:
    if event == "ERROR":
        for_count = for_count + 1
print(f"Conteo con for: {for_count}")

# Second verdict: start, condition against len(), and progress of one
# per turn. Without index = index + 1 the same position repeats
# forever; cancel such a hang with Ctrl + C and restore the progress.
while_count = 0
index = 0
while index < len(event_log):
    if event_log[index] == "ERROR":
        while_count = while_count + 1
    index = index + 1
print(f"Conteo con while: {while_count}")

# Equivalence check: both versions walked the same 20 events.
both_match = for_count == while_count
print(f"Conteos iguales: {both_match}")

# ==============================================================================
# STEP 3: Communication (given). Verified summary for the reviewer.
# Counts prove nothing by themselves; they order human review of local
# practice data. The program opens no ports, touches no disk,
# and contacts nothing.
# ==============================================================================
print("--- Verificación del registro ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total de eventos: {len(event_log)}")
print(f"Errores (for): {for_count}")
print(f"Errores (while): {while_count}")

if both_match:
    verification_message = "conteos iguales"
else:
    verification_message = "conteos distintos"
print(f"Verificación: {verification_message}")
