"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 14 (PyDefSec)
FILE: homework_solution.py (reference for pack_shift.py)
PURPOSE: Pack the night-shift review with the same kit technique as
         class: the same two documented modules hold the shift logic,
         the driver reaches them from the project root, and pip freeze
         proves the venv holds Pydantic 2.x under its compatible pin.
NOTE: Homework after class, outside the 60 minutes. Create
      pack_shift.py manually in your Session 01 project, reusing the
      kit/ package from class. Use this file only as backup guidance
      after attempting the task on your own.
PEDAGOGICAL RESTRICTIONS:
    - Same new syntax as class only: modules, packages,
      __name__ == "__main__" guard, pip plus venv workflow, pinned
      requirements, pydantic import plus version (no modeling yet).
    - No pathlib, no new domain classes, no argparse, no sockets,
      no subprocess, no network, no shell.
    - English PEP 8 identifiers plus comments (style guidance).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> packaged task ->
pinned shift report.
Homework chain: new shift data with the same pack technique, while
the class exercise packs the day review. Pairs prove nothing by
themselves; they order human review of local practice data. This
report opens no ports, touches no network, and contacts nothing
beyond its own console.
"""

import pydantic

# ==============================================================================
# KIT LAYOUT (tecnica de clase reutilizada; respaldo autocontenido aqui):
#   kit/__init__.py    -> KIT_VERSION plus re-exports (clase: REVIEW_THRESHOLD,
#                         count_events y filter_events sin cambios)
#   kit/count_kit.py   -> REVIEW_THRESHOLD plus count_events (S11 reuse)
#   kit/filter_kit.py  -> filter_events (S12 reuse)
#   pack_shift.py      -> this driver con SHIFT_THRESHOLD propio y variantes
#                         shift autocontenidas (count_shift, filter_shift),
#                         siempre corrido desde la raiz del proyecto
#   requirements.txt   -> one pinned line: pydantic>=2.0,<3
# THREE IMPORT FORMS (typed in pack_shift.py once kit/ exists;
# technique reuse: same kit/ names as class, shift variants live
# autocontenidas in this driver backup):
#   import kit.count_kit
#   from kit.count_kit import count_events
#   from kit import filter_kit
# ==============================================================================

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


# ==============================================================================
# STEP 2: Packaged tasks. Reference copies of the two kit modules applied
# to the night-shift data with its own threshold.
# ==============================================================================


def count_shift(events, level="WARNING"):
    """Return count and verdict for the given shift level."""
    total = events.count(level)
    if total >= SHIFT_THRESHOLD:
        verdict = "Revisión prioritaria"
    else:
        verdict = "Rutina local"
    return total, verdict


def filter_shift(events, level="WARNING"):
    """Return the list of shift events matching the given level."""
    matched = []
    for event in events:
        if event == level:
            matched.append(event)
    return matched


def main():
    """Run the packaged shift review from the project root."""
    print(f"Eventos del turno: {len(shift_events)}")

    # First packaged shift review uses "WARNING": 7 reaches the threshold.
    warn_total, warn_verdict = count_shift(shift_events, "WARNING")
    print(f"Avisos: {warn_total} - {warn_verdict}")

    # Second packaged shift review uses "ERROR": 4 stays routine.
    error_total, error_verdict = count_shift(shift_events, "ERROR")
    print(f"Errores: {error_total} - {error_verdict}")

    # Packaged shift filter: 7 of 20 match WARNING.
    warn_matches = filter_shift(shift_events, "WARNING")
    print(f"Filtrados WARNING: {len(warn_matches)} de {len(shift_events)}")

    # Package proof plus pinned dependency proof (given lines).
    print("Paquete: kit (count_kit + filter_kit, 3 importaciones)")
    print(f"Pydantic: {pydantic.VERSION} (pin pydantic>=2.0,<3)")
    print(f"Contexto: {__name__} (ejecucion directa)")

    # ==========================================================================
    # STEP 3: Communication. Packaged shift report with both pairs plus
    # the pinned environment that proves reproducibility.
    # ==========================================================================
    print("--- Revisión empaquetada del turno ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print("Entorno: venv (.venv) con requirements fijados")
    print("Modelos: BaseModel llega en S16 (hoy solo instalacion)")


if __name__ == "__main__":
    main()
