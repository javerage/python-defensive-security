"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 11 (PyDefSec)
FILE: starter.py (guided skeleton for check_helpers.py)
PURPOSE: Split a monolithic local checker over 20 synthetic events
         into 3 pure functions with def, return, and a minimal
         docstring: count levels, decide the verdict, and format the
         final line with the same summary as the single-block version.
NOTE: The repository is only a backup. Create check_helpers.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected verification.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as check_helpers.py and run:
        python check_helpers.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the mapping table in your student material first: it holds
    the 20 events, the threshold (5), and the expected line
    ("Errores: 6 - Revisión prioritaria").

DEFINITIONS UP, CALLS DOWN: define the 3 functions first, call them
    in order below, and keep every print at the end. No function
    prints inside: each one returns its result.
==============================================================================

Conceptual sequence: flat list (20 events) -> count -> decide ->
format -> verified summary.
Each station receives, returns, and never does another station's job.
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
# STEP 2: Split (TODO). Three pure helpers with one-line docstrings;
# definitions above, chained calls below. No prints inside.
# ==============================================================================
# TODO 2.1: Define count_errors(events) with a docstring stating what
# it receives and returns; return events.count("ERROR") (expect 6).
# def count_errors(events):
#     """Return how many ERROR entries the list holds."""

# TODO 2.2: Define decide_status(total) with a docstring; return
# "Revisión prioritaria" for 5 or more, else "Rutina local".
# def decide_status(total):
#     """Return the verdict for the given total."""

# TODO 2.3: Define format_report(total, verdict) with a docstring;
# return the exact line "Errores: 6 - Revisión prioritaria".
# def format_report(total, verdict):
#     """Return the final line for the given total and verdict."""

# TODO 2.4: Call the three in order and keep each return (safe
# defaults so the skeleton runs; replace each one with its call).
error_total = 0  # TODO: build it with count_errors(event_log)
verdict = "PENDING"  # TODO: build it with decide_status(error_total)
report_line = "PENDING"  # TODO: build it with format_report(error_total, verdict)

print("PENDING")  # TODO: print f"Errores contados: {error_total}"
print("PENDING")  # TODO: print f"Verdicto: {verdict}"
print("PENDING")  # TODO: print f"Reporte: {report_line}"

# ==============================================================================
# STEP 3: Communication (given). Verified summary for the reviewer.
# ==============================================================================
print("--- Verificador por funciones ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print("Funciones: 3 puras con docstring")
