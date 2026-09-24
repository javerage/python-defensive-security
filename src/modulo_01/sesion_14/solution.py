"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 14 (PyDefSec)
FILE: solution.py (reference for pack_review.py)
PURPOSE: Pack the Session 11-13 count plus filter logic as the kit package
         workflow: two documented modules, three import forms, one venv
         with pinned requirements, and Pydantic installed plus announced
         (no modeling yet), so the shift handoff runs from the project
         root with reproducible dependencies.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they create kit/
      (kit/__init__.py, kit/count_kit.py, kit/filter_kit.py) plus
      requirements.txt manually, install into .venv, and run
      pack_review.py from the project root.
WHY PACK: Sessions 11 to 13 counted well but scripts lay loose. Today
      the same two functions live in two documented modules, the driver
      reaches them through three import forms, and pip freeze proves the
      venv holds Pydantic 2.x under its compatible pin.
PEDAGOGICAL RESTRICTIONS:
    - New today only: modules, packages, __name__ == "__main__" guard,
      pip plus venv workflow, pinned requirements, pydantic import plus
      version announcement (no BaseModel modeling until Session 16).
    - No pathlib, no new domain classes, no argparse, no sockets,
      no subprocess, no network, no shell.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: evidence -> packaged task -> pinned report.
Two documented modules hold the inherited logic; three import forms
reach it; the venv plus freeze prove reproducibility while the console
keeps every verdict. Pydantic is installed and announced only.
"""

import pydantic

# ==============================================================================
# KIT LAYOUT (created manually in curso-python-defensivo, never in repo):
#   kit/__init__.py    -> KIT_VERSION plus re-exports
#   kit/count_kit.py   -> REVIEW_THRESHOLD plus count_events (S11 reuse)
#   kit/filter_kit.py  -> filter_events (S12 reuse)
#   pack_review.py     -> this driver, always run from the project root
#   requirements.txt   -> one pinned line: pydantic>=2.0,<3
# THREE IMPORT FORMS (typed in pack_review.py once kit/ exists):
#   import kit.count_kit
#   from kit.count_kit import count_events
#   from kit import filter_kit
# ==============================================================================

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


# ==============================================================================
# STEP 2: Packaged tasks. Reference copies of the two kit modules: the
# counter from kit.count_kit (Session 11 reuse) and the filter from
# kit/filter_kit (Session 12 reuse). In the student project these live
# in their own files and arrive through the three import forms above.
# ==============================================================================


def count_events(events, level="ERROR"):
    """Return count and verdict for the given level."""
    total = events.count(level)
    if total >= REVIEW_THRESHOLD:
        verdict = "Revisión prioritaria"
    else:
        verdict = "Rutina local"
    return total, verdict


def filter_events(events, level="ERROR"):
    """Return the list of events matching the given level."""
    matched = []
    for event in events:
        if event == level:
            matched.append(event)
    return matched


def main():
    """Run the packaged review from the project root."""
    print(f"Eventos registrados: {len(event_log)}")

    # First packaged review uses "ERROR": 6 reaches the threshold.
    error_total, error_verdict = count_events(event_log)
    print(f"Errores: {error_total} - {error_verdict}")

    # Second packaged review uses "WARNING": 5 also reaches it.
    warn_total, warn_verdict = count_events(event_log, "WARNING")
    print(f"Avisos: {warn_total} - {warn_verdict}")

    # Packaged filter reuses the Session 12 logic: 6 of 20 match ERROR.
    error_matches = filter_events(event_log, "ERROR")
    print(f"Filtrados ERROR: {len(error_matches)} de {len(event_log)}")

    # Package proof plus pinned dependency proof (given lines).
    print("Paquete: kit (count_kit + filter_kit, 3 importaciones)")
    print(f"Pydantic: {pydantic.VERSION} (pin pydantic>=2.0,<3)")
    print(f"Contexto: {__name__} (ejecucion directa)")

    # ==========================================================================
    # STEP 3: Communication (given). Packaged report with both pairs plus
    # the pinned environment that proves reproducibility.
    # Pairs prove nothing by themselves; they order human review of local
    # practice data. The program opens no ports, touches no network,
    # and contacts nothing beyond its own console.
    # ==========================================================================
    print("--- Revisión empaquetada ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {REVIEW_THRESHOLD} (solo lectura)")
    print("Entorno: venv (.venv) con requirements fijados")
    print("Modelos: BaseModel llega en S16 (hoy solo instalacion)")


if __name__ == "__main__":
    main()
