"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 13 (PyDefSec)
FILE: starter.py (guided skeleton for harden_review.py)
PURPOSE: Harden the Session 12 review with try/except/else/finally,
         a custom validation exception, and file logging so no missing
         local source interrupts the shift handoff with a raw traceback.
NOTE: The repository is only a backup. Create harden_review.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected hardened report.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as harden_review.py and run:
        python harden_review.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the mapping table in your student material first: it holds
    the 20 events, the shared threshold (5), the known sources, and
    the known levels.

    BEFORE COMPLETING EACH TODO, PREDICT FIRST: write on paper the
    value you expect and why; then run the script and compare what you
    got with your prediction and with the expected-output block
    (predict -> execute -> compare).

ORDER: evidence above, guards in the middle, unpacked calls plus
    hardened report at the end. Captures travel to the log file;
    verdicts travel to the console.
==============================================================================

Conceptual sequence: evidence -> guarded task -> logged report.
Three guarded tasks harden three inherited reviews; the log keeps
every capture while the console keeps every verdict.
"""

import logging

# ==============================================================================
# STEP 1: Evidence (given). Shared threshold, twenty synthetic local
# events, operator identity, plus the local log that keeps captures.
# ==============================================================================
LOG_PATH = "defense.log"
logging.basicConfig(
    filename=LOG_PATH,
    filemode="w",
    level=logging.INFO,
    format="%(levelname)s %(message)s",
)

REVIEW_THRESHOLD = 5

event_log = [
    "INFO", "ERROR", "WARNING", "INFO", "ERROR",
    "WARNING", "ERROR", "INFO", "WARNING", "ERROR",
    "INFO", "WARNING", "INFO", "ERROR", "WARNING",
    "INFO", "ERROR", "INFO", "INFO", "INFO",
]

# Identity of whose review this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Eventos registrados: {len(event_log)}")

# ==============================================================================
# STEP 2: Hardening (TODO). One custom exception, two small validators,
# one inherited counter, and one guard that wraps all three reviews.
# ==============================================================================
# TODO 2.1: Define ReviewLevelError as a subclass of Exception with a
# docstring stating when it is raised.
# class ReviewLevelError(Exception):
#     """..."""

# TODO 2.2: Define load_source(source_name) that returns the events for
# the known local source and raises FileNotFoundError otherwise.
# def load_source(source_name):
#     """..."""

# TODO 2.3: Define validate_level(level) that returns the level when it
# belongs to the known set and raises ReviewLevelError otherwise.
# def validate_level(level):
#     """..."""

# TODO 2.4: Define review_events(events, level="ERROR") with a docstring
# stating what it receives and returns; count the given level, decide
# against REVIEW_THRESHOLD, and return total, verdict together.
# def review_events(events, level="ERROR"):
#     """..."""

# TODO 2.5: Define safe_review(source_name, level) with a guarded block
# (try/except/else/finally) that captures a missing source and an
# unknown level, logs every path, and returns total, verdict together.
# def safe_review(source_name, level):
#     """Guard one inherited review."""

# TODO 2.6: Unpack the first hardened review safe_review with the known
# source and the default level into error_total plus error_verdict and
# print the "Errores" finding line.
error_total = 0  # TODO: unpack it with error_total, error_verdict = safe_review(...)
error_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print the "Errores" finding line

# TODO 2.7: Unpack the second hardened review safe_review with the known
# source and the warning level into warn_total plus warn_verdict and
# print the "Avisos" finding line.
warn_total = 0  # TODO: unpack it with warn_total, warn_verdict = safe_review(...)
warn_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print the "Avisos" finding line

# TODO 2.8: Unpack the third hardened review safe_review with the missing
# source into bad_total plus bad_verdict and print the finding line for
# the invalid source.
bad_total = 0  # TODO: unpack it with bad_total, bad_verdict = safe_review(...)
bad_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print the finding line for the invalid source

# ==============================================================================
# STEP 3: Communication (given). Hardened report with both pairs plus
# the captured source and the local log that proves the capture.
# ==============================================================================
print("--- Revisión endurecida ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Umbral: {REVIEW_THRESHOLD} (solo lectura)")
print(f"Registro: {LOG_PATH} (3 tareas, 1 error capturado)")
