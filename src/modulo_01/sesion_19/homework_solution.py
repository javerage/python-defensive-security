"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 19 (PyDefSec)
FILE: homework_solution.py (canonical reference for analizar_borde.py)
PURPOSE: Transfer the checkpoint technique to the night-shift edge
         batch: 8 raw records with boundary cases (140-char message,
         141-char rejection, lax text id, empty source, invented
         level), verified with five message-carrying checks.
NOTE: The repository is only a backup. Create analizar_borde.py
      manually in your Session 01 project after attempting the task
      on your own. This reference runs from the project root:
          python analizar_borde.py
WHY THIS BATCH: the class shift proved the pipeline on clean rows.
      The night shift proves the boundary on hostile rows: what the
      limit accepts, what it rejects, and which motive each rejection
      carries. No argparse, no sockets, no subprocess, no network.
      100% English PEP 8 identifiers and comments; Spanish user texts.
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
# STEP 2: Edge tasks. Same boundary technique as analizar.py, applied
# to the hostile night batch.
# ==============================================================================
def validate_shift_records(raw_records):
    """Split night dicts into accepted findings plus labeled rejections."""
    accepted = []
    rejected = []
    for position, raw_item in enumerate(raw_records, start=21):
        try:
            accepted.append(Finding.model_validate(raw_item))
        except ValidationError:
            rejected.append(f"registro {position}: rechazado en la frontera")
    return accepted, rejected


def count_by_level(findings):
    """Count grouped findings by level, starting each at zero."""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for finding in findings:
        if finding.level in counts:
            counts[finding.level] += 1
    return counts


def shift_verdict(error_total, threshold):
    """Pair accepted ERROR rows against the night threshold."""
    if error_total >= threshold:
        return error_total, "Revision prioritaria"
    return error_total, "Rutina local"


# ==============================================================================
# STEP 3: Communication (given). Five checks plus the night report.
# ==============================================================================
def main():
    """Run the night-shift edge batch from the project root."""
    accepted, rejected = validate_shift_records(shift_records)
    counts = count_by_level(accepted)
    error_total, error_verdict = shift_verdict(counts["ERROR"], SHIFT_THRESHOLD)

    assert len(shift_records) == 8, "El turno debia leer 8 registros"
    assert len(accepted) == 5, "El turno debia aceptar 5 hallazgos"
    assert len(rejected) == 3, "El turno debia rechazar 3 registros"
    assert counts == {"INFO": 3, "WARNING": 1, "ERROR": 1}, "Conteos del turno fuera de contrato"
    assert (error_total, error_verdict) == (1, "Rutina local"), "1 error bajo el umbral 3 es rutina"

    lax_probe = Finding.model_validate(
        {"finding_id": "31", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"}
    )
    assert lax_probe.finding_id == 31, "El modo lax debia convertir el texto 31 al entero 31"
    try:
        Finding.model_validate(
            {"finding_id": "31", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"},
            strict=True,
        )
        strict_rejected = False
    except ValidationError:
        strict_rejected = True
    assert strict_rejected, "strict=True debia rechazar el texto 31 sin convertirlo"

    print("Turno leido: 8")
    print("Turno aceptado: 5")
    print("Turno rechazado: 3")
    print(f"Conteo por nivel: INFO={counts['INFO']} WARNING={counts['WARNING']} ERROR={counts['ERROR']}")
    print(f"Errores (aceptados): {error_total} - {error_verdict}")
    print("Chequeos del turno: 5/5 en verde (asserts con mensaje)")
    print("--- Reporte probado (turno) ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print("Evolucion: Finding (S18) -> analizar.py (S19)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
