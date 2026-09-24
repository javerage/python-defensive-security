"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 12 (PyDefSec)
FILE: starter.py (guided skeleton for scope_review.py)
PURPOSE: Review 20 synthetic local events with a default parameter
         plus a double return: count plus verdict travel together in
         one call, the global threshold is read-only, and both calls
         (default ERROR plus explicit WARNING) are unpacked.
NOTE: The repository is only a backup. Create scope_review.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected review.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as scope_review.py and run:
        python scope_review.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the mapping table in your student material first: it holds
    the 20 events, the global threshold (5), and the expected pairs.
    Predict each pair on paper before completing the TODOs below;
    then run and compare with the expected output.

ORDER: read-only global above, definition with default in the middle,
    unpacking plus print at the end. Never reassign the global and
    never declare global: data travels by parameter.
==============================================================================

Conceptual sequence: global threshold (read-only) -> default call ->
explicit call -> unpacked pairs -> review summary.
One trip delivers the tray with both seats: count plus verdict.
"""

# ==============================================================================
# STEP 1: Evidence (given). Shared threshold, twenty synthetic local
# events, plus operator identity.
# ==============================================================================
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
# STEP 2: Review (TODO). One definition with a default, two unpacked
# calls. The local total lives only inside; the global is only read.
# ==============================================================================
# TODO 2.1: Define review_events(events, level="ERROR") with a
# docstring stating what it receives and returns; count the given
# level, decide against REVIEW_THRESHOLD (5 or more is prioritaria),
# and return total, verdict together.
# def review_events(events, level="ERROR"):
#     """Return count and verdict for the given level."""

# TODO 2.2: Unpack the default call review_events(event_log) into
# error_total plus error_verdict and print the Errores line.
error_total = 0  # TODO: unpack it with error_total, error_verdict = review_events(event_log)
error_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print f"Errores: {error_total} - {error_verdict}"

# TODO 2.3: Unpack the explicit call
# review_events(event_log, "WARNING") into warn_total plus
# warn_verdict and print the Avisos line.
warn_total = 0  # TODO: unpack it with warn_total, warn_verdict = review_events(event_log, "WARNING")
warn_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print f"Avisos: {warn_total} - {warn_verdict}"

# ==============================================================================
# STEP 3: Communication (given). Review summary with both pairs.
# ==============================================================================
print("--- Revisión con ámbitos ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Umbral global: {REVIEW_THRESHOLD} (solo lectura)")
