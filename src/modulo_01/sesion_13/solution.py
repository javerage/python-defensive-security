"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 13 (PyDefSec)
FILE: solution.py (reference for harden_review.py)
PURPOSE: Harden the Session 12 review with try/except/else/finally,
         a custom validation exception, and file logging so no missing
         local source interrupts the shift handoff with a raw traceback.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      harden_review.py manually.
WHY HARDEN: Session 12 counted well when data was perfect. Today each
      of the 3 inherited reviews runs inside its own guarded block:
      a missing source or an unknown level is captured, logged, and
      reported in Spanish instead of crashing the handoff.
PEDAGOGICAL RESTRICTIONS:
    - New today only: try/except/else/finally, raise, one custom
      exception subclass (ReviewLevelError), logging to a local file.
    - No Pydantic, no new domain classes, no argparse, no sockets,
      no subprocess, no network, no shell.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
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
# STEP 2: Hardening. One custom exception, two small validators, one
# inherited counter, and one guard that wraps all three reviews.
# ==============================================================================


class ReviewLevelError(Exception):
    """Raised when a review level is unknown to the local lab."""


def load_source(source_name):
    """Return events for a known local source; raise when missing."""
    known_sources = {"local_events": event_log}
    if source_name not in known_sources:
        raise FileNotFoundError(f"missing local source: {source_name}")
    return known_sources[source_name]


def validate_level(level):
    """Return the level when known; raise ReviewLevelError otherwise."""
    known_levels = ("ERROR", "WARNING", "INFO")
    if level not in known_levels:
        raise ReviewLevelError(f"unknown review level: {level}")
    return level


def review_events(events, level="ERROR"):
    """Return count and verdict for the given level."""
    total = events.count(level)
    if total >= REVIEW_THRESHOLD:
        verdict = "Revisión prioritaria"
    else:
        verdict = "Rutina local"
    return total, verdict


def safe_review(source_name, level):
    """Guard one inherited review; never leak a raw traceback."""
    try:
        events = load_source(source_name)
        clean_level = validate_level(level)
        total, verdict = review_events(events, level=clean_level)
    except FileNotFoundError as exc:
        logging.warning(f"captured missing source: {exc}")
        total, verdict = 0, "Rutina local"
    except ReviewLevelError as exc:
        logging.warning(f"captured invalid level: {exc}")
        total, verdict = 0, "Rutina local"
    else:
        logging.info(f"reviewed {source_name} level {clean_level}: {total}")
    finally:
        logging.info(f"finished task for {source_name} level {level}")
    return total, verdict


# First hardened review uses "ERROR": 6 reaches the threshold.
error_total, error_verdict = safe_review("local_events", "ERROR")
print(f"Errores: {error_total} - {error_verdict}")

# Second hardened review uses "WARNING": 5 also reaches it.
warn_total, warn_verdict = safe_review("local_events", "WARNING")
print(f"Avisos: {warn_total} - {warn_verdict}")

# Third hardened review names a missing source: captured, not crashed.
bad_total, bad_verdict = safe_review("missing_source", "CRITICAL")
print(f"Fuente no válida: missing_source - {bad_verdict}")

# ==============================================================================
# STEP 3: Communication (given). Hardened report with both pairs plus
# the captured source and the local log that proves the capture.
# Pairs prove nothing by themselves; they order human review of local
# practice data. The program opens no ports, touches no network,
# and contacts nothing beyond its own log file.
# ==============================================================================
print("--- Revisión endurecida ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Umbral: {REVIEW_THRESHOLD} (solo lectura)")
print(f"Registro: {LOG_PATH} (3 tareas, 1 error capturado)")
