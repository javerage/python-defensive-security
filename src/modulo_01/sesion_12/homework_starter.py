"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 12 (PyDefSec)
FILE: homework_starter.py (guided skeleton for shift_scope.py)
PURPOSE: Review 20 synthetic night-shift events with a default
         parameter plus a double return: unpack the default WARNING
         pair and the explicit ERROR pair against the shift threshold.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_scope.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      report. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as shift_scope.py plus run:
        python shift_scope.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

BEFORE CODING, ANALYZE (without running any code):
    - Which pair does the default call return (expect 7 plus
      prioritaria), and why is the default "WARNING"?
    - Which pair does the call with "ERROR" return (expect 4 plus
      rutina), and which verdict fits it?
    - Where does each total live, and why is it never read outside
      review_shift?

DELIVERY: explain aloud the chain default -> double return ->
unpacking -> local versus global. Local practice data only. The
program organizes data for human review; it opens no ports, touches
no disk, and contacts nothing.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> default call ->
explicit call -> unpacked pairs -> shift report.
Homework chain: new shift data with another default ("WARNING") ->
same double-return technique, while the class exercise defaults to
"ERROR".
"""

# ==============================================================================
# STEP 1: Evidence (given). Shift threshold, twenty synthetic
# night-shift events, plus operator identity.
# ==============================================================================
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
# STEP 2: Review (TODO). One definition with a default, two unpacked
# calls. The local total lives only inside; the global is only read.
# ==============================================================================
# TODO 2.1: Define review_shift(events, level="WARNING") with a
# docstring stating what it receives and returns; count the given
# level, decide against SHIFT_THRESHOLD (5 or more is prioritaria),
# and return total, verdict together.
# def review_shift(events, level="WARNING"):
#     """Return count and verdict for the given shift level."""

# TODO 2.2: Unpack the default call review_shift(shift_events) into
# warn_total plus warn_verdict (expect 7 plus prioritaria) and print
# "Avisos: 7 - Revisión prioritaria".
warn_total = 0  # TODO: unpack it with warn_total, warn_verdict = review_shift(shift_events)
warn_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print f"Avisos: {warn_total} - {warn_verdict}"

# TODO 2.3: Unpack the explicit call
# review_shift(shift_events, "ERROR") into error_total plus
# error_verdict (expect 4 plus rutina) and print
# "Errores: 4 - Rutina local".
error_total = 0  # TODO: unpack it with error_total, error_verdict = review_shift(shift_events, "ERROR")
error_verdict = "PENDING"  # TODO: same unpacking as above
print("PENDING")  # TODO: print f"Errores: {error_total} - {error_verdict}"

# ==============================================================================
# STEP 3: Communication (given). Shift report with both pairs.
# ==============================================================================
print("--- Revisión del turno ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Umbral global: {SHIFT_THRESHOLD} (solo lectura)")
