"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 14 (PyDefSec)
FILE: homework_starter.py (guided skeleton for pack_shift.py)
PURPOSE: Pack the night-shift review with the same kit technique as
         class: the same two documented modules hold the shift logic
         and the driver runs from the project root with Pydantic 2.x
         pinned.
NOTE: Homework after class, outside the 60 minutes. Create
      pack_shift.py manually in your Session 01 project, reusing the
      kit/ package from class. Complete each task marked TODO. This
      skeleton compiles plus runs; PENDING marks unfinished work, and
      replaced placeholders give the expected report. Check
      homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as pack_shift.py plus run from
    the project root:
        python pack_shift.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    BEFORE CODING, ANALYZE (without running any code):
        - Which packaged call reviews the warning level on the shift
          data, and which verdict fits a count above the threshold?
        - Which packaged call reviews the error level, and which verdict
          fits a count below the shift threshold?
        - Which filter call counts the WARNING matches, and where does
          the Pydantic version travel in the report?

DELIVERY: explain aloud the chain module -> import -> venv -> freeze.
Local practice data only. The program organizes data for human review;
it opens no ports, touches no network, and contacts nothing beyond its
own console.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> packaged task ->
pinned shift report.
Homework chain: new shift data with the same pack technique, while
the class exercise packs the day review.
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
# STEP 2: Packaged tasks (TODO). Same pack technique as class, applied to
# the night-shift data with its own threshold.
# ==============================================================================
# TODO 2.1: Define count_shift(events, level="WARNING") with a docstring
# stating what it receives and returns; count the given level, decide
# against SHIFT_THRESHOLD, and return total, verdict together.
# def count_shift(events, level="WARNING"):
#     """..."""

# TODO 2.2: Define filter_shift(events, level="WARNING") with a docstring
# stating what it receives and returns; collect matching events with an
# explicit for loop and return the matched list.
# def filter_shift(events, level="WARNING"):
#     """..."""

# TODO 2.3: Define main() that prints the shift total, unpacks the
# WARNING review plus the ERROR review, prints the WARNING filter
# count, and prints the package plus pinned dependency proof lines.
# def main():
#     """Run the packaged shift review from the project root."""

def main():
    """Run the packaged shift review from the project root."""
    print(f"Eventos del turno: {len(shift_events)}")

    # TODO 2.4: Unpack the first packaged shift review count_shift with
    # the warning level into warn_total plus warn_verdict and print the
    # "Avisos" finding line.
    warn_total = 0  # TODO: unpack it with warn_total, warn_verdict = count_shift(...)
    warn_verdict = "PENDING"  # TODO: same unpacking as above
    print("PENDING")  # TODO: print the "Avisos" finding line

    # TODO 2.5: Unpack the second packaged shift review count_shift with
    # the error level into error_total plus error_verdict and print the
    # "Errores" finding line.
    error_total = 0  # TODO: unpack it with error_total, error_verdict = count_shift(...)
    error_verdict = "PENDING"  # TODO: same unpacking as above
    print("PENDING")  # TODO: print the "Errores" finding line

    # TODO 2.6: Call filter_shift with the WARNING level into
    # warn_matches and print the "Filtrados WARNING" count line.
    warn_matches = []  # TODO: call it with warn_matches = filter_shift(...)
    print("PENDING")  # TODO: print the "Filtrados WARNING" count line

    # Package proof plus pinned dependency proof (given lines).
    print("Paquete: kit (count_kit + filter_kit, 3 importaciones)")
    print(f"Pydantic: {pydantic.VERSION} (pin pydantic>=2.0,<3)")
    print(f"Contexto: {__name__} (ejecucion directa)")

    # ==========================================================================
    # STEP 3: Communication (given). Packaged shift report with both pairs
    # plus the pinned environment that proves reproducibility.
    # ==========================================================================
    print("--- Revisión empaquetada del turno ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print("Entorno: venv (.venv) con requirements fijados")
    print("Modelos: BaseModel llega en S16 (hoy solo instalacion)")


if __name__ == "__main__":
    main()
