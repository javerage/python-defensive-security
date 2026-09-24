"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 09 (PyDefSec)
FILE: starter.py (guided skeleton for event_loop.py)
PURPOSE: Count 6 ERROR entries in 20 synthetic local events twice:
         once with for and once with while under guaranteed
         termination, then verify both counts match.
NOTE: The repository is only a backup. Create event_loop.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected verification.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as event_loop.py and run:
        python event_loop.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely (use it if a
          while without progress never ends).

    Count two ERROR entries in the first row by hand before coding:
    both versions must reach 6 over the same 20 events.

WHY ONE LEVEL ONLY: nested loops arrive in Session 10. Until then
    each version visits the flat list of 20 exactly once.
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
# STEP 2: Counts (TODO). One single-level loop per version; the while
# advances its index on every turn so it always terminates.
# ==============================================================================
# TODO 2.1: Count with for (expect 6). Start for_count at 0, visit
# each event with for event in event_log, add 1 when event == "ERROR".
for_count = 0  # TODO: build it with the for loop described above

# TODO 2.2: print the for count (expect 6).
print("PENDING")  # TODO: print f"Conteo con for: {for_count}"

# TODO 2.3: Count with while (expect 6). Start while_count at 0 and
# index at 0; repeat while index < len(event_log), add 1 on ERROR,
# and advance index = index + 1 every turn.
while_count = 0  # TODO: build it with the while loop described above
index = 0  # TODO: the while loop must leave index at 20

# TODO 2.4: print the while count (expect 6).
print("PENDING")  # TODO: print f"Conteo con while: {while_count}"

# TODO 2.5: Compare both counts (expect True) and print the result.
both_match = False  # TODO: build it with for_count == while_count
print("PENDING")  # TODO: print f"Conteos iguales: {both_match}"

# ==============================================================================
# STEP 3: Communication (given). Verified summary for the reviewer.
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
