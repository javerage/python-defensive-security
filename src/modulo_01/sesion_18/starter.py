"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 18 (PyDefSec)
FILE: starter.py (guided skeleton for finding_model.py)
PURPOSE: Model local findings first with minimal manual classes and
         then evolve them to validated Pydantic models, keeping the
         same three checks green and every check local.
NOTE: The repository is only a backup. Create finding_model.py plus
      test_modelo.py manually in your Session 01 project and complete
      each task marked TODO. This skeleton compiles and runs; PENDING
      marks unfinished work, and replaced placeholders give the
      expected modeled report.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Keep the review batch from Session 17
    untouched, then save your work as finding_model.py and run from
    the project root:
        python finding_model.py
        python -m unittest test_modelo.py -v

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the mapping table in your student material first: it holds
    the 6 local dicts, the shared threshold (5), the manual-first
    note, and the lax versus strict note.

    BEFORE COMPLETING EACH TODO, PREDICT FIRST: write on paper the
    value you expect and why; then run the script and compare what you
    got with your prediction and with the expected-output block
    (predict -> execute -> compare).

ORDER: evidence above, modeled tasks in the middle, auditable report
    at the end. No inheritance, no argparse, no network, no shell.
    No Pi in this session.
==============================================================================

Conceptual sequence: evidence -> modeled task -> auditable report.
Manual classes teach object anatomy; BaseModel adds the validated
schema at the same boundary.
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). Shared threshold, six synthetic local
# finding dicts, plus operator identity.
# ==============================================================================
FINDING_THRESHOLD = 5
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

sample_records = [
    {"finding_id": 1, "level": "INFO", "message": "servicio iniciado en localhost", "source": "sensor-a"},
    {"finding_id": 2, "level": "WARNING", "message": "reintento de conexion local", "source": "sensor-a"},
    {"finding_id": 3, "level": "ERROR", "message": "disco lleno en localhost", "source": "sensor-b"},
    {"finding_id": 4, "level": "INFO", "message": "copia de respaldo verificada", "source": "sensor-b"},
    {"finding_id": 5, "level": "ERROR", "message": "puerto local sin respuesta", "source": "sensor-b"},
    {"finding_id": 6, "level": "INFO", "message": "sesion local auditada", "source": "sensor-a"},
]

# Identity of whose model this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Modeled tasks (TODO). Manual classes first, then the same
# shape as validated Pydantic models.
# ==============================================================================
# TODO 2.1: Define class ManualFinding with __init__ storing finding_id,
# level, message, source as public attributes plus _label as private
# by convention; add summary() returning "[LEVEL] message (source)"
# and is_critical() returning True only for ERROR. Check level plus
# non-empty message and source with ValueError; leave numeric-string
# ids and over-long messages unchecked on purpose (the BaseModel
# rejects them later).
# class ManualFinding:
#     """..."""

# TODO 2.2: Define class ManualReport with __init__(threshold) storing
# the threshold plus an empty items list; add add(), count_by_level()
# starting each level at zero, and verdict() pairing ERROR rows
# against the threshold.
# class ManualReport:
#     """..."""

# TODO 2.3: Define class Finding(BaseModel) with type hints for the
# four fields (finding_id as int, level as the three allowed texts,
# message as text between 1 and 140 chars, source as non-empty text).
# Add the same summary() and is_critical() methods. Use the imported
# helpers only.
# class Finding(BaseModel):
#     """..."""

# TODO 2.4: Define build_validated_batch(raw_records) splitting raw
# dicts into accepted findings plus labeled rejections with
# Finding.model_validate inside try/except ValidationError.
# def build_validated_batch(raw_records):
#     """..."""


def main():
    """Run the modeled finding batch from the project root."""
    # TODO 2.5: Wire the batch with the helpers above; validate the six
    # rows, group them in the report, pair ERROR rows against
    # FINDING_THRESHOLD, and replay the lax/strict proof.
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}  # TODO: count it with the helpers
    error_total = 0  # TODO: read it from the counts
    error_verdict = "PENDING"  # TODO: decide it against FINDING_THRESHOLD
    manual_ok = "PENDING"  # TODO: prove it with the manual summary
    validated_ok = "PENDING"  # TODO: prove it with Field plus strict

    print("PENDING")  # TODO: print the "Pruebas del modelo" finding line
    print("PENDING")  # TODO: print the "Conteo por nivel" finding line
    print("PENDING")  # TODO: print the "Errores (aceptados)" finding line
    print("PENDING")  # TODO: print the "Clase manual" finding line
    print("PENDING")  # TODO: print the "Modelo validado" finding line

    # ==========================================================================
    # STEP 3: Communication (given). Modeled report with the evolution
    # note plus the local scope the checkpoint inherits.
    # ==========================================================================
    print("--- Reporte probado ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {FINDING_THRESHOLD} (solo lectura)")
    print("Evolucion: manual (__init__) -> BaseModel (Field + strict)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
