"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 19 (PyDefSec)
FILE: homework_starter.py (guided skeleton for analizar_borde.py)
PURPOSE: Transfer the checkpoint technique to the night-shift edge
         batch: 8 raw records with boundary cases, verified with five
         message-carrying checks. Attempt the task on your own first;
         this skeleton only scaffolds the attempt.
NOTE: The repository is only a backup. Create analizar_borde.py
      manually in your Session 01 project. This skeleton compiles and
      runs; PENDING marks unfinished work. Run from the project root:
          python analizar_borde.py

    BEFORE COMPLETING EACH TODO, PREDICT FIRST: write on paper the
    value you expect and why; then run the script and compare what you
    got with your prediction and with the expected-output block
    (predict -> execute -> compare). TODO comments never hold answers.

ORDER: evidence above, edge tasks in the middle, auditable report
    at the end. No argparse, no sockets, no subprocess, no network.
==============================================================================

Conceptual sequence: evidence -> edge task -> auditable report.
Five checks lock totals, counts, lax conversion, strict rejection,
and the length boundary.
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). Night-shift threshold, 8 edge dicts, plus
# operator identity. Records 4-8 probe the boundary on purpose.
# ==============================================================================
SHIFT_THRESHOLD = 3
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

shift_records = [
    {"finding_id": 21, "level": "INFO", "message": "ronda nocturna iniciada en localhost", "source": "sensor-a"},
    {"finding_id": 22, "level": "WARNING", "message": "latencia nocturna alta en loopback", "source": "sensor-b"},
    {"finding_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"finding_id": 24, "level": "INFO", "message": "x" * 140, "source": "sensor-b"},
    {"finding_id": 25, "level": "INFO", "message": "x" * 141, "source": "sensor-a"},
    {"finding_id": "31", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"},
    {"finding_id": 27, "level": "ERROR", "message": "sonda local sin origen", "source": ""},
    {"finding_id": 28, "level": "DEBUG", "message": "nivel nocturno inventado", "source": "sensor-b"},
]

# Identity of whose analyzer this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# Finding base (given, reused from Session 18 unchanged).
# ==============================================================================
class Finding(BaseModel):
    """Validated defensive finding at the input boundary."""

    finding_id: int
    level: Literal["INFO", "WARNING", "ERROR"]
    message: str = Field(min_length=1, max_length=140)
    source: str = Field(min_length=1)

    def summary(self):
        """Return the one-line human review of this finding."""
        return f"[{self.level}] {self.message} ({self.source})"

    def is_critical(self):
        """Return True only for ERROR findings."""
        return self.level == "ERROR"


# ==============================================================================
# STEP 2: Edge tasks (TODO). Predict each value on paper before you run.
# ==============================================================================
# TODO 2.1: Split the night dicts into accepted findings plus labeled
# rejections. Validate each raw dict at the Finding boundary, append
# each accepted finding, and label each rejected dict with its
# position starting at 21.
def validate_shift_records(raw_records):
    """Split night dicts into accepted findings plus labeled rejections."""
    accepted = []
    rejected = []
    # TODO: replace this PENDING stub with the boundary loop.
    return accepted, rejected


# TODO 2.2: Count the accepted findings by level. Start each of the
# three levels at zero and add one per finding whose level matches.
def count_by_level(findings):
    """Count grouped findings by level, starting each at zero."""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    # TODO: replace this PENDING stub with the counting loop.
    return counts


# TODO 2.3: Pair the accepted ERROR rows against the night threshold.
# Return the pair (total, verdict): priority review at or above the
# threshold, local routine below it.
def shift_verdict(error_total, threshold):
    """Pair accepted ERROR rows against the night threshold."""
    # TODO: replace this PENDING stub with the threshold pair.
    return error_total, "PENDING"


# ==============================================================================
# STEP 3: Communication (given). Partial night lines; the full report
# replaces PENDING values only.
# ==============================================================================
def main():
    """Run the night-shift edge batch from the project root."""
    accepted, rejected = validate_shift_records(shift_records)
    counts = count_by_level(accepted)
    error_total, error_verdict = shift_verdict(counts["ERROR"], SHIFT_THRESHOLD)
    print("Turno leido: 8")
    print(f"Turno aceptado: {len(accepted)} (PENDING)")
    print(f"Turno rechazado: {len(rejected)} (PENDING)")
    print(f"Conteo por nivel: INFO={counts['INFO']} WARNING={counts['WARNING']} ERROR={counts['ERROR']}")
    print(f"Errores (aceptados): {error_total} - {error_verdict}")
    print("--- Reporte probado (turno, PARCIAL) ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print("Evolucion: Finding (S18) -> analizar.py (S19)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
