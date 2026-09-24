"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 14 (PyDefSec)
FILE: starter.py (guided skeleton for pack_review.py)
PURPOSE: Pack the Session 11-13 count plus filter logic as the kit package
         workflow: two documented modules, three import forms, one venv
         with pinned requirements, and Pydantic installed plus announced.
NOTE: The repository is only a backup. Create pack_review.py plus the
      kit/ package manually in your Session 01 project and complete
      each task marked TODO. This skeleton compiles and runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      packaged report.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Create kit/__init__.py, kit/count_kit.py,
    kit/filter_kit.py, and requirements.txt manually, then save your
    work as pack_review.py and run from the project root:
        python pack_review.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the mapping table in your student material first: it holds
    the 20 events, the shared threshold (5), the kit layout, the three
    import forms, and the pinned requirement (pydantic>=2.0,<3).

    BEFORE COMPLETING EACH TODO, PREDICT FIRST: write on paper the
    value you expect and why; then run the script and compare what you
    got with your prediction and with the expected-output block
    (predict -> execute -> compare).

ORDER: evidence above, packaged tasks in the middle, pinned report at
    the end. Modules hold the logic; imports reach it; the venv plus
    freeze prove it.
==============================================================================

Conceptual sequence: evidence -> packaged task -> pinned report.
Two documented modules hold the inherited logic; three import forms
reach it; the venv plus freeze prove reproducibility while the console
keeps every verdict.
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
# STEP 2: Packaged tasks (TODO). Reference copies of the two kit modules
# plus the driver that unpacks both reviews through the guard.
# ==============================================================================
# TODO 2.1: Define count_events(events, level="ERROR") with a docstring
# stating what it receives and returns; count the given level, decide
# against REVIEW_THRESHOLD, and return total, verdict together.
# def count_events(events, level="ERROR"):
#     """..."""

# TODO 2.2: Define filter_events(events, level="ERROR") with a docstring
# stating what it receives and returns; collect matching events with an
# explicit for loop and return the matched list.
# def filter_events(events, level="ERROR"):
#     """..."""

# TODO 2.3: Define main() that prints the registered total, unpacks the
# ERROR review plus the WARNING review, prints the ERROR filter count,
# and prints the package plus pinned dependency proof lines.
# def main():
#     """Run the packaged review from the project root."""

def main():
    """Run the packaged review from the project root."""
    print(f"Eventos registrados: {len(event_log)}")

    # TODO 2.4: Unpack the first packaged review count_events with the
    # default level into error_total plus error_verdict and print the
    # "Errores" finding line.
    error_total = 0  # TODO: unpack it with error_total, error_verdict = count_events(...)
    error_verdict = "PENDING"  # TODO: same unpacking as above
    print("PENDING")  # TODO: print the "Errores" finding line

    # TODO 2.5: Unpack the second packaged review count_events with the
    # warning level into warn_total plus warn_verdict and print the
    # "Avisos" finding line.
    warn_total = 0  # TODO: unpack it with warn_total, warn_verdict = count_events(...)
    warn_verdict = "PENDING"  # TODO: same unpacking as above
    print("PENDING")  # TODO: print the "Avisos" finding line

    # TODO 2.6: Call filter_events with the ERROR level into
    # error_matches and print the "Filtrados ERROR" count line.
    error_matches = []  # TODO: call it with error_matches = filter_events(...)
    print("PENDING")  # TODO: print the "Filtrados ERROR" count line

    # Package proof plus pinned dependency proof (given lines).
    print("Paquete: kit (count_kit + filter_kit, 3 importaciones)")
    print(f"Pydantic: {pydantic.VERSION} (pin pydantic>=2.0,<3)")
    print(f"Contexto: {__name__} (ejecucion directa)")

    # ==========================================================================
    # STEP 3: Communication (given). Packaged report with both pairs plus
    # the pinned environment that proves reproducibility.
    # ==========================================================================
    print("--- Revisión empaquetada ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {REVIEW_THRESHOLD} (solo lectura)")
    print("Entorno: venv (.venv) con requirements fijados")
    print("Modelos: BaseModel llega en S16 (hoy solo instalacion)")


if __name__ == "__main__":
    main()
