"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 18 (PyDefSec)
FILE: homework_starter.py (guided skeleton for finding_shift.py)
PURPOSE: Prove the night-shift findings with the same modeled
         technique as class: the same Finding model plus counting
         turns raw shift dicts into accepted rows plus labeled
         rejections, verified by four inline asserts with messages.
NOTE: Homework after class, outside the 60 minutes. Create
      finding_shift.py manually in your Session 01 project, reusing
      the modeled technique from class. Complete each task marked
      TODO. This skeleton compiles plus runs; PENDING marks
      unfinished work, and replaced placeholders give the expected
      report. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as finding_shift.py plus run
    from the project root:
        python finding_shift.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    BEFORE CODING, ANALYZE (without running any code):
        - Which split call keeps every shift row proven, and which
          verdict fits an error count below the shift threshold?
        - Which boundary call converts the numeric string in lax mode,
          and where does each rejected motive travel instead of a raw
          trace?

DELIVERY: explain aloud the chain shift data -> modeled checks ->
report. Local practice data only. The program organizes data for
human review; it opens no ports, touches no network, and contacts
nothing beyond its own console plus local files.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> modeled task ->
auditable shift report.
Homework chain: new shift data with the same modeled technique, while
the class exercise models the day batch.
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). Shift threshold, six synthetic night-shift
# dicts, plus operator identity.
# ==============================================================================
SHIFT_THRESHOLD = 3
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

shift_records = [
    {"finding_id": 21, "level": "INFO", "message": "ronda nocturna iniciada en localhost", "source": "sensor-a"},
    {"finding_id": 22, "level": "WARNING", "message": "latencia nocturna alta en loopback", "source": "sensor-b"},
    {"finding_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"finding_id": "24", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"},
    {"finding_id": 25, "level": "INFO", "message": "", "source": "sensor-a"},
    {"finding_id": 26, "level": "DEBUG", "message": "nivel nocturno inventado", "source": "sensor-b"},
]

# Identity of whose review this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Modeled tasks (TODO). Same boundary model as class, applied
# to the night-shift data.
# ==============================================================================
# TODO 2.1: Define class Finding(BaseModel) with type hints for the
# four fields (finding_id as int, level as the three allowed texts,
# message as text between 1 and 140 chars, source as non-empty text).
# Add the same summary() and is_critical() methods.
# class Finding(BaseModel):
#     """..."""

# TODO 2.2: Define validate_shift_records(raw_records) with a docstring
# stating what it receives and returns; validate each dict with
# Finding.model_validate inside try/except ValidationError, appending
# accepted findings plus labeled rejections.
# def validate_shift_records(raw_records):
#     """..."""

# TODO 2.3: Define count_by_level(findings) with a docstring stating
# what it receives and returns; count only levels inside the allowed
# contract starting each at zero.
# def count_by_level(findings):
#     """..."""


def main():
    """Run the modeled night-shift batch from the project root."""
    # TODO 2.4: Wire the four shift checks with the helpers above
    # (split, lax proof, counts, verdict).
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
    # STEP 3: Communication (given). Modeled shift report the teacher
    # consumes next session.
    # ==========================================================================
    print("--- Reporte probado (turno) ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print("Evolucion: manual (__init__) -> BaseModel (Field + strict)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
