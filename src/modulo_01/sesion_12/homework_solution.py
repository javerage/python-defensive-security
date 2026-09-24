"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 12 (PyDefSec)
FILE: homework_solution.py (reference for shift_scope.py)
PURPOSE: Review 20 synthetic night-shift events with a default
         parameter plus a double return: unpack the default WARNING
         pair and the explicit ERROR pair against the shift threshold.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_scope.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Default parameter plus multiple return only: level="WARNING",
      return total, verdict, two-variable unpacking, read-only global.
    - No global reassignment, no *args, no classes, no decorators,
      no imports, no files, no network.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> default call ->
explicit call -> unpacked pairs -> shift report.
Homework chain: new shift data with another default ("WARNING") ->
same double-return technique, while the class exercise defaults to
"ERROR". Pairs prove nothing by themselves; they order human review
of local practice data. This report opens no ports, touches no disk,
and contacts nothing.
"""

# ==============================================================================
# STEP 1: Evidence (given). Shift threshold, twenty synthetic
# night-shift events, plus operator identity.
# ==============================================================================
SHIFT_THRESHOLD = 5

# Fixture note: these 20 positions match the student guide table
# (7 WARNING and 4 ERROR) and reproduce the expected pairs.
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
# STEP 2: Review. The default proposes "WARNING" when nobody says
# otherwise; the global is only read, never reassigned. Each local
# total lives only inside its own call.
# ==============================================================================
def review_shift(events, level="WARNING"):
    """Return count and verdict for the given shift level."""
    total = events.count(level)
    if total >= SHIFT_THRESHOLD:
        verdict = "Revisión prioritaria"
    else:
        verdict = "Rutina local"
    return total, verdict


# Default call uses "WARNING": 7 reaches the threshold.
warn_total, warn_verdict = review_shift(shift_events)
print(f"Avisos: {warn_total} - {warn_verdict}")

# Explicit call replaces the default with "ERROR": 4 stays routine.
error_total, error_verdict = review_shift(shift_events, "ERROR")
print(f"Errores: {error_total} - {error_verdict}")

# ==============================================================================
# STEP 3: Communication. Shift report with both pairs.
# ==============================================================================
print("--- Revisión del turno ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Umbral global: {SHIFT_THRESHOLD} (solo lectura)")
