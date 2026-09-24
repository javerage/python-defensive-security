"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 17 (PyDefSec)
FILE: starter.py (guided skeleton for review_batch.py)
PURPOSE: Prove the local review batch with tests: count accepted
         events by level, check the review config, and replay the
         Evento boundary (lax acceptance plus strict rejection),
         keeping every check local with unittest first and pytest
         as the optional readable runner.
NOTE: The repository is only a backup. Create review_batch.py plus
      test_review.py manually in your Session 01 project and complete
      each task marked TODO. This skeleton compiles and runs; PENDING
      marks unfinished work, and replaced placeholders give the
      expected proven report.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Keep the validate_events.py batch from Session
    16 untouched, then save your work as review_batch.py and run from
    the project root:
        python review_batch.py
        python -m unittest test_review.py -v
        pytest test_review.py -v   (optional, when installed)

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the mapping table in your student material first: it holds
    the 10 local dicts, the shared threshold (5), the lax versus
    strict note, and the arrange-act-assert order.

    BEFORE COMPLETING EACH TODO, PREDICT FIRST: write on paper the
    value you expect and why; then run the script and compare what you
    got with your prediction and with the expected-output block
    (predict -> execute -> compare).

ORDER: evidence above, proven tasks in the middle, auditable report
    at the end. Tests never touch the network; unittest runs
    everywhere, pytest only re-runs the same file.
==============================================================================

Conceptual sequence: evidence -> proven task -> auditable report.
Two small pure functions hold the batch logic; six tests replay them;
the Evento model keeps guarding the input boundary only.
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). Shared threshold, ten synthetic local event
# dicts, plus operator identity.
# ==============================================================================
REVIEW_THRESHOLD = 5
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

sample_events = [
    {"event_id": 1, "level": "INFO", "message": "servicio iniciado en localhost", "source": "sensor-a"},
    {"event_id": 2, "level": "WARNING", "message": "reintento de conexion local", "source": "sensor-a"},
    {"event_id": 3, "level": "ERROR", "message": "disco lleno en localhost", "source": "sensor-b"},
    {"event_id": 4, "level": "INFO", "message": "revision de turno completada", "source": "sensor-a"},
    {"event_id": 5, "level": "ERROR", "message": "puerto local sin respuesta", "source": "sensor-b"},
    {"event_id": 6, "level": "WARNING", "message": "latencia alta en loopback", "source": "sensor-a"},
    {"event_id": 7, "level": "INFO", "message": "copia de respaldo verificada", "source": "sensor-b"},
    {"event_id": 8, "level": "WARNING", "message": "umbral cercano al limite", "source": "sensor-a"},
    {"event_id": 9, "level": "ERROR", "message": "registro incompleto detectado", "source": "sensor-b"},
    {"event_id": 10, "level": "INFO", "message": "sesion local iniciada", "source": "sensor-a"},
]

# Identity of whose review this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Proven tasks (TODO). Reused boundary model plus two small pure
# functions the six tests lock in place.
# ==============================================================================
# TODO 2.1: Define class Evento(BaseModel) with type hints for the four
# fields (event_id as int, level as the three allowed texts, message
# plus source as non-empty texts). Use the imported helpers only.
# class Evento(BaseModel):
#     """..."""

# TODO 2.2: Define contar_por_nivel(events) with a docstring stating
# what it receives and returns; start every allowed level at zero,
# walk the rows with for, read each level safely, and count only the
# levels inside the contract (ignore unknown or missing levels).
# def contar_por_nivel(events):
#     """..."""

# TODO 2.3: Define validar_config(port, level) with a docstring stating
# what it receives and returns; reject ports outside 1-65535 first,
# then accept only levels inside the allowed contract.
# def validar_config(port, level):
#     """..."""

# TODO 2.4: Define describe_batch() with a docstring stating what it
# receives and returns; count the sample by level, pair ERROR rows
# against REVIEW_THRESHOLD, check the lab config, prove lax converts
# the numeric string, and prove strict=True rejects the same dict.
# def describe_batch():
#     """..."""


def main():
    """Run the proven review batch from the project root."""
    # TODO 2.5: Wire the batch with the helpers above; count rows by
    # level against REVIEW_THRESHOLD and replay the lax/strict proof.
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}  # TODO: count it with the helpers
    error_total = 0  # TODO: read it from the counts
    error_verdict = "PENDING"  # TODO: decide it against REVIEW_THRESHOLD
    config_ok = "PENDING"  # TODO: check it with the lab port and level
    lax_ok = "PENDING"  # TODO: prove it with the numeric-string record
    strict_rejected = "PENDING"  # TODO: prove it with strict=True

    print("PENDING")  # TODO: print the "Pruebas del lote" finding line
    print("PENDING")  # TODO: print the "Conteo por nivel" finding line
    print("PENDING")  # TODO: print the "Errores (aceptados)" finding line
    print("PENDING")  # TODO: print the "Config valida" finding line
    print("PENDING")  # TODO: print the "Evento aceptado" finding line
    print("PENDING")  # TODO: print the "Evento rechazado" finding line

    # ==========================================================================
    # STEP 3: Communication (given). Proven report with the runner note
    # plus the local scope the next reader inherits.
    # ==========================================================================
    print("--- Revision probada ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {REVIEW_THRESHOLD} (solo lectura)")
    print("Corredores: unittest (base) + pytest (legible, opcional)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
