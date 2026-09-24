"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 11 (PyDefSec)
FILE: solution.py (reference for check_helpers.py)
PURPOSE: Split a monolithic local checker over 20 synthetic events
         into 3 pure functions with def, return, and a minimal
         docstring: count levels, decide the verdict, and format the
         final line with the same summary as the single-block version.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      check_helpers.py manually.
WHY THREE PIECES: one block mixes three jobs and hides each contract.
      Counting returns a number, deciding returns a verdict, and
      formatting returns the line ready to print.
PEDAGOGICAL RESTRICTIONS:
    - def plus return only: positional parameters, minimal one-line
      docstrings, pure functions (same arguments, same result, no
      print inside).
    - No scopes beyond local, no *args, no default values (they arrive
      in Session 12), no imports, no files, no network.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
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
# STEP 2: Split. Definitions above, chained calls below, every print
# at the end. The parameter is the declared slot (events); the
# argument is the delivered value (event_log).
# ==============================================================================
def count_errors(events):
    """Return how many ERROR entries the list holds."""
    total = events.count("ERROR")
    return total


def decide_status(total):
    """Return the verdict for the given total."""
    if total >= 5:
        return "Revisión prioritaria"
    return "Rutina local"


def format_report(total, verdict):
    """Return the final line for the given total and verdict."""
    return f"Errores: {total} - {verdict}"


# Chain by returns: each call keeps what the previous one delivered.
error_total = count_errors(event_log)
verdict = decide_status(error_total)
report_line = format_report(error_total, verdict)

print(f"Errores contados: {error_total}")
print(f"Verdicto: {verdict}")
print(f"Reporte: {report_line}")

# ==============================================================================
# STEP 3: Communication (given). Verified summary for the reviewer.
# The split changes nothing in the output; it only makes each contract
# readable. The program opens no ports, touches no disk,
# and contacts nothing.
# ==============================================================================
print("--- Verificador por funciones ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print("Funciones: 3 puras con docstring")
