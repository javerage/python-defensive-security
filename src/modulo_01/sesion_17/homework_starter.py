"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 17 (PyDefSec)
FILE: homework_starter.py (guided skeleton for review_shift.py)
PURPOSE: Prove the night-shift batch with the same tested technique
         as class: the same Evento model plus counting and config
         checks turn raw shift dicts into accepted rows plus labeled
         rejections, verified by six inline asserts with messages.
NOTE: Homework after class, outside the 60 minutes. Create
      review_shift.py manually in your Session 01 project, reusing
      the tested technique from class. Complete each task marked
      TODO. This skeleton compiles plus runs; PENDING marks
      unfinished work, and replaced placeholders give the expected
      report. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as review_shift.py plus run
    from the project root:
        python review_shift.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    BEFORE CODING, ANALYZE (without running any code):
        - Which split call keeps every shift row proven, and which
          verdict fits an error count below the shift threshold?
        - Which boundary call converts the numeric string in lax mode,
          and which call rejects it with strict=True?
        - Which counting call ignores unknown levels, and where does
          each rejected motive travel instead of a raw trace?

DELIVERY: explain aloud the chain shift data -> proven checks ->
report. Local practice data only. The program organizes data for
human review; it opens no ports, touches no network, and contacts
nothing beyond its own console plus local files.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> proven task ->
auditable shift report.
Homework chain: new shift data with the same tested technique, while
the class exercise proves the day batch.
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). Shift threshold, ten synthetic night-shift
# dicts, plus operator identity.
# ==============================================================================
SHIFT_THRESHOLD = 3
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

shift_events = [
    {"event_id": 21, "level": "INFO", "message": "ronda nocturna iniciada en localhost", "source": "sensor-a"},
    {"event_id": 22, "level": "WARNING", "message": "reintento nocturno local", "source": "sensor-b"},
    {"event_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"event_id": 24, "level": "INFO", "message": "bitacora nocturna verificada", "source": "sensor-b"},
    {"event_id": 25, "level": "ERROR", "message": "cola nocturna llena", "source": "sensor-a"},
    {"event_id": 26, "level": "WARNING", "message": "latencia nocturna alta", "source": "sensor-b"},
    {"event_id": 27, "level": "INFO", "message": "respaldo nocturno completado", "source": "sensor-a"},
    {"event_id": "28", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"},
    {"event_id": 29, "message": "linea nocturna sin nivel", "source": "sensor-a"},
    {"event_id": 30, "level": "DEBUG", "message": "nivel nocturno inventado", "source": "sensor-b"},
]

# Identity of whose review this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Proven tasks (TODO). Same boundary model and same pure
# functions as class, applied to the night-shift data.
# ==============================================================================
# TODO 2.1: Define class Evento(BaseModel) with type hints for the four
# fields (event_id as int, level as the three allowed texts, message
# plus source as non-empty texts). Use the imported helpers only.
# class Evento(BaseModel):
#     """..."""

# TODO 2.2: Define contar_por_nivel(events) with a docstring stating
# what it receives and returns; count only levels inside the allowed
# contract and ignore unknown or missing levels.
# def contar_por_nivel(events):
#     """..."""

# TODO 2.3: Define validar_config(port, level) with a docstring stating
# what it receives and returns; reject ports outside 1-65535 first,
# then accept only levels inside the allowed contract.
# def validar_config(port, level):
#     """..."""

# TODO 2.4: Define validate_shift_records(raw_records) with a docstring
# stating what it receives and returns; validate each dict with
# Evento.model_validate inside try/except ValidationError, appending
# accepted events plus labeled rejections.
# def validate_shift_records(raw_records):
#     """..."""


def main():
    """Run the proven night-shift batch from the project root."""
    # TODO 2.5: Wire the six shift checks with the helpers above
    # (split, lax proof, strict proof, counts, config, verdict).
    accepted_total = 0  # TODO: count it with the split helper
    rejected_total = 0  # TODO: count it with the split helper
    error_total = 0  # TODO: read it from the accepted counts
    error_verdict = "PENDING"  # TODO: decide it against SHIFT_THRESHOLD

    print("PENDING")  # TODO: print the "Turno leido" finding line
    print("PENDING")  # TODO: print the "Turno aceptado" finding line
    print("PENDING")  # TODO: print the "Turno rechazado" finding line
    print("PENDING")  # TODO: print the "Errores (aceptados)" finding line
    print("PENDING")  # TODO: print the "Chequeos del turno" finding line

    # ==========================================================================
    # STEP 3: Communication (given). Proven shift report the teacher
    # consumes next session.
    # ==========================================================================
    print("--- Revision probada (turno) ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print("Corredores: unittest (base) + pytest (legible, opcional)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
