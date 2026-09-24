"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 09 (PyDefSec)
FILE: homework_solution.py (reference for shift_loop.py)
PURPOSE: Count 7 WARNING entries in 20 synthetic night-shift events
         twice, once with for and once with while under guaranteed
         termination, then verify both counts match.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_loop.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Single-level loops only: for over the list, while with counter,
      len() as the bound, comparison of both totals.
    - No nested loops, no functions, no try/except, no imports,
      no files, no network.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: flat list -> for count -> while count ->
comparison -> verified summary.
Homework chain: new shift data plus another level (WARNING) -> same
double-count technique, while the class exercise counts ERROR. Counts
prove nothing by themselves; they order human review of local practice
data. This verification opens no ports, touches no disk, and contacts
nothing.
"""

# ==============================================================================
# STEP 1: Evidence (given). Twenty synthetic night-shift events plus
# operator identity.
# ==============================================================================
shift_log = [
    "WARNING", "INFO", "WARNING", "ERROR", "INFO",
    "WARNING", "INFO", "WARNING", "ERROR", "INFO",
    "WARNING", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "ERROR", "INFO",
]

# Identity of whose verification this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Eventos del turno: {len(shift_log)}")

# ==============================================================================
# STEP 2: Counts. The for visits each event and stops by itself; the
# while repeats while its condition holds and must progress each turn.
# ==============================================================================
shift_for = 0
for event in shift_log:
    if event == "WARNING":
        shift_for = shift_for + 1
print(f"Conteo con for: {shift_for}")

shift_while = 0
shift_index = 0
while shift_index < len(shift_log):
    if shift_log[shift_index] == "WARNING":
        shift_while = shift_while + 1
    shift_index = shift_index + 1
print(f"Conteo con while: {shift_while}")

shift_match = shift_for == shift_while
print(f"Conteos iguales: {shift_match}")

# ==============================================================================
# STEP 3: Communication. Verified summary for whoever receives the shift.
# ==============================================================================
print("--- Verificación del turno ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total de eventos: {len(shift_log)}")
print(f"Avisos (for): {shift_for}")
print(f"Avisos (while): {shift_while}")

if shift_match:
    shift_message = "conteos iguales"
else:
    shift_message = "conteos distintos"
print(f"Verificación: {shift_message}")
