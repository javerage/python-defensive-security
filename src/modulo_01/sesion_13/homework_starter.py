"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 13 (PyDefSec)
FILE: homework_starter.py (guided skeleton for harden_shift.py)
PURPOSE: Harden the night-shift review with the same guarded technique
         as class: each of the 3 shift reviews runs inside
         try/except/else/finally, captures travel to shift.log, and no
         missing source interrupts the handoff with a raw traceback.
NOTE: Homework after class, outside the 60 minutes. Create
      harden_shift.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      report. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as harden_shift.py plus run:
        python harden_shift.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    BEFORE CODING, ANALYZE (without running any code):
        - Which guarded call reviews the warning level on the known
          source, and which branch (try, except, else, finally) records
          its success?
        - Which guarded call reviews the error level, and which verdict
          fits a count below the shift threshold?
        - Which guarded call names the missing source, and where does
          its capture travel instead of the console?

DELIVERY: explain aloud the chain guard -> capture -> log -> verdict.
Local practice data only. The program organizes data for human review;
it opens no ports, touches no network, and contacts nothing beyond its
own log file.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> guarded task ->
logged shift report.
Homework chain: new shift data with the same guard technique, while
the class exercise hardens the day review.
"""

import logging

# ==============================================================================
# STEP 1: Evidence (given). Shift threshold, twenty synthetic
# night-shift events, operator identity, plus the local shift log.
# ==============================================================================
LOG_PATH = "shift.log"
logging.basicConfig(
    filename=LOG_PATH,
    filemode="w",
    level=logging.INFO,
    format="%(levelname)s %(message)s",
)

SHIFT_THRESHOLD = 5

shift_events = [
    "WARNING", "INFO", "ERROR", "WARNING", "INFO",
    "WARNING", "INFO", "ERROR", "WARNING", "INFO",
    "WARNING", "ERROR", "INFO", "WARNING", "INFO",
    "INFO", "WARNING", "INFO", "ERROR", "INFO",
]

# Identity of whose report this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Eventos del turno: {len(shift_events)}")

# ==============================================================================
# STEP 2: Hardening (TODO). Same guard technique as class, applied to
# the night-shift data with its own threshold and log.
# ==============================================================================
# TODO 2.1: Define ShiftLevelError as a subclass of Exception with a
# docstring stating when it is raised.
# class ShiftLevelError(Exception):
#     """..."""

# TODO 2.2: Define load_shift_source(source_name) that returns the shift
# events for the known local source and raises FileNotFoundError
# otherwise.
# def load_shift_source(source_name):
#     """..."""

# TODO 2.3: Define validate_shift_level(level) that returns the level
# when it belongs to the known set and raises ShiftLevelError otherwise.
# def validate_shift_level(level):
#     """..."""

# TODO 2.4: Define review_shift(events, level="WARNING") with a docstring
# stating what it receives and returns; count the given level, decide
# against SHIFT_THRESHOLD, and return total, verdict together.
# def review_shift(events, level="WARNING"):
#     """..."""

# TODO 2.5: Define safe_shift_review(source_name, level) with a guarded
# block (try/except/else/finally) that captures a missing source and an
# unknown level, logs every path, and returns total, verdict together.
# def safe_shift_review(source_name, level):
#     """Guard one shift review."""

# TODO 2.6: Unpack the first hardened shift review safe_shift_review
# with the known source and the warning level into warn_total plus
# warn_verdict and print the "Avisos" finding line.
warn_total = 0  # TODO: unpack it with warn_total, warn_verdict = safe_shift_review(...)
warn_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print the "Avisos" finding line

# TODO 2.7: Unpack the second hardened shift review safe_shift_review
# with the known source and the error level into error_total plus
# error_verdict and print the "Errores" finding line.
error_total = 0  # TODO: unpack it with error_total, error_verdict = safe_shift_review(...)
error_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print the "Errores" finding line

# TODO 2.8: Unpack the third hardened shift review safe_shift_review
# with the missing source into bad_total plus bad_verdict and print the
# finding line for the invalid source.
bad_total = 0  # TODO: unpack it with bad_total, bad_verdict = safe_shift_review(...)
bad_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print the finding line for the invalid source

# ==============================================================================
# STEP 3: Communication (given). Hardened shift report with both pairs
# plus the captured source and the local log that proves the capture.
# ==============================================================================
print("--- Revisión endurecida del turno ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
print(f"Registro: {LOG_PATH} (3 tareas, 1 error capturado)")
