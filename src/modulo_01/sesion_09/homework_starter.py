"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 09 (PyDefSec)
FILE: homework_starter.py (guided skeleton for shift_loop.py)
PURPOSE: Count 7 WARNING entries in 20 synthetic night-shift events
         twice, once with for and once with while under guaranteed
         termination, then verify both counts match.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_loop.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      verification. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as shift_loop.py plus run:
        python shift_loop.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting while that never ends.

BEFORE CODING, PREDICT (count by hand first, without running):
    - How many WARNING entries are there by hand, and in
      which positions are the first two? Write your count first.
    - Which three lines guarantee the while terminates (start,
      condition with len(), progress of one)?
    - What will shift_match hold when both versions agree, and what
      does that mean for whoever receives the shift?

DELIVERY: explain aloud the chain list -> for -> while with progress
-> comparison for the shift. Local practice data only. The program
organizes data for human review; it opens no ports, touches no disk,
and contacts nothing.
==============================================================================

Conceptual sequence: flat list -> for count -> while count ->
comparison -> verified summary.
Homework chain: new shift data plus another level (WARNING) -> same
double-count technique, while the class exercise counts ERROR.
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
# STEP 2: Counts (TODO). One single-level loop per version; the while
# advances its index on every turn so it always terminates.
# PREDICT FIRST: before completing each TODO, write your prediction
# (which value you expect and why); run the script; then compare
# with the expected output in the student material.
# ==============================================================================
# TODO 2.1: Count with for. Start shift_for at 0, visit
# each event with for event in shift_log, add 1 when WARNING.
shift_for = 0  # TODO: build it with the for loop described above

# TODO 2.2: print the for count.
print("PENDING")  # TODO: print f"Conteo con for: {shift_for}"

# TODO 2.3: Count with while. Start shift_while at 0 and
# shift_index at 0; repeat while shift_index < len(shift_log), add 1
# on WARNING, and advance shift_index = shift_index + 1 every turn.
shift_while = 0  # TODO: build it with the while loop described above
shift_index = 0  # TODO: the while loop must advance shift_index every turn

# TODO 2.4: print the while count.
print("PENDING")  # TODO: print f"Conteo con while: {shift_while}"

# TODO 2.5: Compare both counts and print the result.
shift_match = False  # TODO: build it with shift_for == shift_while
print("PENDING")  # TODO: print f"Conteos iguales: {shift_match}"

# ==============================================================================
# STEP 3: Communication (given). Verified summary for whoever receives
# the shift.
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
