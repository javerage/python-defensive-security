"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 11 (PyDefSec)
FILE: homework_starter.py (guided skeleton for shift_helpers.py)
PURPOSE: Split a night-shift local checker over 20 synthetic events
         into 3 pure functions with def, return, and a minimal
         docstring: count WARNING entries, decide the shift verdict,
         and format the shift line.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_helpers.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      report. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as shift_helpers.py plus run:
        python shift_helpers.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

BEFORE CODING, ANALYZE (count by hand first, without running):
    - How many WARNING entries are there by hand (expect 7), and what
      does count_warnings(shift_events) return?
    - What verdict does decide_shift(7) return under threshold 5,
      and why is the class rule unchanged?
    - What exact line does format_shift return, and where does the
      single print block go?

DELIVERY: explain aloud the chain list -> count -> decide -> format
for the shift. Local practice data only. The program organizes data
for human review; it opens no ports, touches no disk, and contacts
nothing.
==============================================================================

Conceptual sequence: flat list -> count -> decide -> format ->
shift report.
Homework chain: new shift data plus another level (WARNING) -> same
3-function technique, while the class exercise counts ERROR.
"""

# ==============================================================================
# STEP 1: Evidence (given). Twenty synthetic night-shift events plus
# operator identity.
# ==============================================================================
shift_events = [
    "WARNING", "INFO", "WARNING", "ERROR", "INFO",
    "WARNING", "INFO", "WARNING", "ERROR", "INFO",
    "WARNING", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "ERROR", "INFO",
]

# Identity of whose report this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Eventos del turno: {len(shift_events)}")

# ==============================================================================
# STEP 2: Split (TODO). Three pure helpers with one-line docstrings;
# definitions above, chained calls below. No prints inside.
# ==============================================================================
# TODO 2.1: Define count_warnings(events) with a docstring stating what
# it receives and returns; return events.count("WARNING") (expect 7).
# def count_warnings(events):
#     """Return how many WARNING entries the list holds."""

# TODO 2.2: Define decide_shift(total) with a docstring; return
# "Revisión prioritaria" for 5 or more, else "Rutina local".
# def decide_shift(total):
#     """Return the shift verdict for the given total."""

# TODO 2.3: Define format_shift(total, verdict) with a docstring;
# return the exact line "Avisos: 7 - Revisión prioritaria".
# def format_shift(total, verdict):
#     """Return the shift line for the given total and verdict."""

# TODO 2.4: Call the three in order and keep each return (safe
# defaults so the skeleton runs; replace each one with its call).
warning_total = 0  # TODO: build it with count_warnings(shift_events)
shift_verdict = "PENDING"  # TODO: build it with decide_shift(warning_total)
shift_line = "PENDING"  # TODO: build it with format_shift(warning_total, shift_verdict)

print("PENDING")  # TODO: print f"Avisos contados: {warning_total}"
print("PENDING")  # TODO: print f"Verdicto: {shift_verdict}"
print("PENDING")  # TODO: print f"Reporte: {shift_line}"

# ==============================================================================
# STEP 3: Communication (given). Shift report for whoever receives it.
# ==============================================================================
print("--- Verificador del turno ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print("Funciones: 3 puras con docstring")
