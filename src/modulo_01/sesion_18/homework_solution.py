"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 18 (PyDefSec)
FILE: homework_solution.py (reference for finding_shift.py)
PURPOSE: Prove the night-shift findings with the same modeled
         technique as class: the same Finding model plus counting
         turns raw shift dicts into accepted rows plus labeled
         rejections, checked by four inline asserts with messages
         before the shift report is printed.
NOTE: Homework after class, outside the 60 minutes. Create
      finding_shift.py manually in your Session 01 project, reusing
      the modeled technique from class. Check this reference only
      after trying alone.
WHY MODEL: The night shift reuses the class technique on new data: 6
      raw dicts (3 exact, 1 lax numeric string, 2 invalid) become 4
      accepted plus 2 rejected, and four inline checks prove the
      figures before anyone consumes the shift report.
PEDAGOGICAL RESTRICTIONS:
    - Reused only: ManualFinding plus Finding plus lax versus
      strict (S18 class), plain assert statements with messages
      (same proving idea, no new syntax).
    - No inheritance, no argparse, no network, no shell.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
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
# dicts, plus operator identity. Records 1-3 are exact, record 4 uses
# a numeric string so lax mode proves its conversion, records 5-6
# are intentionally broken.
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
# STEP 2: Modeled tasks. Same boundary model as class, applied to the
# night-shift data.
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


def validate_shift_records(raw_records):
    """Split raw shift dicts into accepted findings plus labeled rejections."""
    accepted = []
    rejected = []
    for position, raw_item in enumerate(raw_records, start=1):
        try:
            accepted.append(Finding.model_validate(raw_item))
        except ValidationError:
            rejected.append(f"registro {position}: rechazado en la frontera")
    return accepted, rejected


def count_by_level(findings):
    """Count validated findings by level, starting each at zero."""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for finding in findings:
        if finding.level in counts:
            counts[finding.level] += 1
    return counts


def main():
    """Run the modeled night-shift batch from the project root."""
    # Check 1-2 (arrange-act-assert): shift split keeps every row proven.
    accepted, rejected = validate_shift_records(shift_records)
    assert len(accepted) == 4, "El turno debia aceptar 4 hallazgos"
    assert len(rejected) == 2, "El turno debia rechazar 2 hallazgos"

    # Check 3 (edge): lax converts the numeric string of record 4.
    lax_event = Finding.model_validate(shift_records[3])
    assert lax_event.finding_id == 24, "El modo lax debia convertir el texto 24 al entero 24"

    # Check 4 (edge): accepted counts ignore the two rejected rows.
    counts = count_by_level(accepted)
    assert counts == {"INFO": 2, "WARNING": 1, "ERROR": 1}, "Se esperaban 2 INFO, 1 WARNING y 1 ERROR aceptados"

    error_total = counts["ERROR"]
    if error_total >= SHIFT_THRESHOLD:
        error_verdict = "Revisión prioritaria"
    else:
        error_verdict = "Rutina local"

    print(f"Turno leido: {len(shift_records)}")
    print(f"Turno aceptado: {len(accepted)}")
    print(f"Turno rechazado: {len(rejected)}")
    print(f"Errores (aceptados): {error_total} - {error_verdict}")
    print("Chequeos del turno: 4/4 en verde (asserts con mensaje)")

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
