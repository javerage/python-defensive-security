"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 12 (PyDefSec)
FILE: solution.py (reference for scope_review.py)
PURPOSE: Review 20 synthetic local events with a default parameter
         plus a double return: count plus verdict travel together in
         one call, the global threshold is read-only, and both calls
         (default ERROR plus explicit WARNING) are unpacked.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      scope_review.py manually.
WHY DOUBLE RETURN: Session 11 needed two stations for number plus
      sign. Today one trip delivers the tray with both seats, and the
      usual level ("ERROR") travels as the default.
PEDAGOGICAL RESTRICTIONS:
    - Default parameter plus multiple return only: level="ERROR",
      return total, verdict, two-variable unpacking, read-only global.
    - No global reassignment, no *args, no classes, no decorators,
      no imports, no files, no network.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
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

# Fixture fidelity note: the last row keeps 6 ERROR and 5 WARNING so
# the code reproduces the expected pairs (6 plus 5). The student guide
# table lists the same 20 positions with one WARNING more; that extra
# WARNING was written here as INFO to honor the expected-output box,
# which is the contract the reference must satisfy.
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
# STEP 2: Review. The default proposes "ERROR" when nobody says
# otherwise; the global is only read, never reassigned, so no global
# statement is needed. The local total is born and dies inside.
# ==============================================================================
def review_events(events, level="ERROR"):
    """Return count and verdict for the given level."""
    total = events.count(level)
    if total >= REVIEW_THRESHOLD:
        verdict = "Revisión prioritaria"
    else:
        verdict = "Rutina local"
    return total, verdict


# Default call uses "ERROR": 6 reaches the threshold.
error_total, error_verdict = review_events(event_log)
print(f"Errores: {error_total} - {error_verdict}")

# Explicit call replaces the default with "WARNING": 5 also reaches it.
warn_total, warn_verdict = review_events(event_log, "WARNING")
print(f"Avisos: {warn_total} - {warn_verdict}")

# ==============================================================================
# STEP 3: Communication (given). Review summary with both pairs.
# Pairs prove nothing by themselves; they order human review of local
# practice data. The program opens no ports, touches no disk,
# and contacts nothing.
# ==============================================================================
print("--- Revisión con ámbitos ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Umbral global: {REVIEW_THRESHOLD} (solo lectura)")
