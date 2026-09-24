"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 13 (PyDefSec)
FILE: homework_solution.py (reference for harden_shift.py)
PURPOSE: Harden the night-shift review with the same guarded technique
         as class: each of the 3 shift reviews runs inside
         try/except/else/finally, captures travel to shift.log, and no
         missing source interrupts the handoff with a raw traceback.
NOTE: Homework after class, outside the 60 minutes. Create
      harden_shift.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Same new syntax as class only: try/except/else/finally, raise,
      one custom exception subclass (ShiftLevelError), logging.
    - No Pydantic, no new domain classes, no argparse, no sockets,
      no subprocess, no network, no shell.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> guarded task ->
logged shift report.
Homework chain: new shift data with the same guard technique, while
the class exercise hardens the day review. Captures prove nothing by
themselves; they order human review of local practice data. This
report opens no ports, touches no network, and contacts nothing
beyond its own log file.
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
# STEP 2: Hardening. Same guard technique as class, applied to the
# night-shift data with its own threshold and log.
# ==============================================================================


class ShiftLevelError(Exception):
    """Raised when a shift review level is unknown to the local lab."""


def load_shift_source(source_name):
    """Return shift events for a known source; raise when missing."""
    known_sources = {"local_events": shift_events}
    if source_name not in known_sources:
        raise FileNotFoundError(f"missing local source: {source_name}")
    return known_sources[source_name]


def validate_shift_level(level):
    """Return the shift level when known; raise ShiftLevelError."""
    known_levels = ("ERROR", "WARNING", "INFO")
    if level not in known_levels:
        raise ShiftLevelError(f"unknown shift level: {level}")
    return level


def review_shift(events, level="WARNING"):
    """Return count and verdict for the given shift level."""
    total = events.count(level)
    if total >= SHIFT_THRESHOLD:
        verdict = "Revisión prioritaria"
    else:
        verdict = "Rutina local"
    return total, verdict


def safe_shift_review(source_name, level):
    """Guard one shift review; never leak a raw traceback."""
    try:
        events = load_shift_source(source_name)
        clean_level = validate_shift_level(level)
        total, verdict = review_shift(events, level=clean_level)
    except FileNotFoundError as exc:
        logging.warning(f"captured missing source: {exc}")
        total, verdict = 0, "Rutina local"
    except ShiftLevelError as exc:
        logging.warning(f"captured invalid level: {exc}")
        total, verdict = 0, "Rutina local"
    else:
        logging.info(f"reviewed {source_name} level {clean_level}: {total}")
    finally:
        logging.info(f"finished task for {source_name} level {level}")
    return total, verdict


# First hardened shift review uses "WARNING": 7 reaches the threshold.
warn_total, warn_verdict = safe_shift_review("local_events", "WARNING")
print(f"Avisos: {warn_total} - {warn_verdict}")

# Second hardened shift review uses "ERROR": 4 stays routine.
error_total, error_verdict = safe_shift_review("local_events", "ERROR")
print(f"Errores: {error_total} - {error_verdict}")

# Third hardened shift review names a missing source: captured, not crashed.
bad_total, bad_verdict = safe_shift_review("missing_source", "DEBUG")
print(f"Fuente no válida: missing_source - {bad_verdict}")

# ==============================================================================
# STEP 3: Communication. Hardened shift report with both pairs plus
# the captured source and the local log that proves the capture.
# ==============================================================================
print("--- Revisión endurecida del turno ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
print(f"Registro: {LOG_PATH} (3 tareas, 1 error capturado)")
