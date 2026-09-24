"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 11 (PyDefSec)
FILE: homework_solution.py (reference for shift_helpers.py)
PURPOSE: Split a night-shift local checker over 20 synthetic events
         into 3 pure functions with def, return, and a minimal
         docstring: count WARNING entries, decide the shift verdict,
         and format the shift line.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_helpers.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - def plus return only: positional parameters, minimal one-line
      docstrings, pure functions (same arguments, same result, no
      print inside).
    - No scopes beyond local, no *args, no default values, no imports,
      no files, no network.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: flat list -> count -> decide -> format ->
shift report.
Homework chain: new shift data plus another level (WARNING) -> same
3-function technique, while the class exercise counts ERROR. The split
changes nothing in the output; it only makes each contract readable.
This report opens no ports, touches no disk, and contacts nothing.
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
# STEP 2: Split. Definitions above, chained calls below, every print
# at the end.
# ==============================================================================
def count_warnings(events):
    """Return how many WARNING entries the list holds."""
    total = events.count("WARNING")
    return total


def decide_shift(total):
    """Return the shift verdict for the given total."""
    if total >= 5:
        return "Revisión prioritaria"
    return "Rutina local"


def format_shift(total, verdict):
    """Return the shift line for the given total and verdict."""
    return f"Avisos: {total} - {verdict}"


# Chain by returns: each call keeps what the previous one delivered.
warning_total = count_warnings(shift_events)
shift_verdict = decide_shift(warning_total)
shift_line = format_shift(warning_total, shift_verdict)

print(f"Avisos contados: {warning_total}")
print(f"Verdicto: {shift_verdict}")
print(f"Reporte: {shift_line}")

# ==============================================================================
# STEP 3: Communication. Shift report for whoever receives it.
# ==============================================================================
print("--- Verificador del turno ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print("Funciones: 3 puras con docstring")
