"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 18 (PyDefSec)
FILE: solution.py (reference for finding_model.py)
PURPOSE: Model local findings first with minimal manual classes and
         then evolve them to validated Pydantic models, keeping the
         same three checks green and every check local.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they keep the
      review batch from Session 17 untouched and write
      finding_model.py next to test_modelo.py, then run both from
      the project root.
WHY CLASSES: Session 17 proved counts with dicts plus functions.
      Dicts let any broken row travel silently. Today each finding
      becomes an object (manual class first, BaseModel after) so a
      broken row is rejected at the boundary with a field motive.
PEDAGOGICAL RESTRICTIONS:
    - New today only: class plus __init__ plus self plus public
      attributes and methods, private-by-convention _label, manual
      validation with ValueError, Finding plus FindingReport as
      BaseModel with Field limits plus Literal plus strict=True
      where rejection is required, ValidationError.
    - Reused only: def plus return (S11), try/except (S13), list
      plus dict plus for (S06-S10), unittest plus assertRaises (S17).
    - No inheritance, no argparse, no network, no shell.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: evidence -> modeled task -> auditable report.
Manual classes teach object anatomy; BaseModel adds a validated
schema at the same input boundary. No Pi in this session.
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). Shared threshold, six synthetic local
# finding dicts, plus operator identity. The sensor fleet produced 20
# raw events this shift; the analyst condenses them into 6 reviewable
# findings: 3 INFO, 1 WARNING, 2 ERROR (2 errors under threshold 5).
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
# STEP 2: Modeled tasks. Manual classes first (object anatomy), then
# the same shape as validated Pydantic models (schema boundary).
# ==============================================================================


class ManualFinding:
    """Manual finding with constructor, public attributes and methods."""

    def __init__(self, finding_id, level, message, source):
        """Store the finding after a minimal manual check."""
        if level not in ALLOWED_LEVELS:
            raise ValueError("level must be one of INFO, WARNING, ERROR")
        if not isinstance(message, str) or len(message) == 0:
            raise ValueError("message must be a non-empty text")
        if not isinstance(source, str) or len(source) == 0:
            raise ValueError("source must be a non-empty text")
        # NOTE: manual check is intentionally weak: it lets a numeric
        # string id ("7") and an over-long message (200 chars) pass.
        # The Pydantic model below rejects both at the boundary.
        self.finding_id = finding_id
        self.level = level
        self.message = message
        self.source = source
        self._label = f"{level}-{finding_id}"

    def summary(self):
        """Return the one-line human review of this finding."""
        return f"[{self.level}] {self.message} ({self.source})"

    def is_critical(self):
        """Return True only for ERROR findings."""
        return self.level == "ERROR"


class ManualReport:
    """Manual report that groups manual findings under a threshold."""

    def __init__(self, threshold):
        """Store the read-only threshold plus an empty item list."""
        self.threshold = threshold
        self.items = []
        self._scope = "localhost (127.0.0.1)"

    def add(self, finding):
        """Append one manual finding to the report."""
        self.items.append(finding)

    def count_by_level(self):
        """Count grouped findings by level, starting each at zero."""
        counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for finding in self.items:
            if finding.level in counts:
                counts[finding.level] += 1
        return counts

    def verdict(self):
        """Pair accepted ERROR rows against the read-only threshold."""
        error_total = self.count_by_level()["ERROR"]
        if error_total >= self.threshold:
            return error_total, "Revisión prioritaria"
        return error_total, "Rutina local"


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


class FindingReport(BaseModel):
    """Validated report that groups validated findings."""

    threshold: int = Field(ge=1)
    items: list = Field(default_factory=list)

    def add(self, finding):
        """Append one validated finding to the report."""
        self.items.append(finding)

    def count_by_level(self):
        """Count grouped findings by level, starting each at zero."""
        counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for finding in self.items:
            if finding.level in counts:
                counts[finding.level] += 1
        return counts

    def verdict(self):
        """Pair accepted ERROR rows against the read-only threshold."""
        error_total = self.count_by_level()["ERROR"]
        if error_total >= self.threshold:
            return error_total, "Revisión prioritaria"
        return error_total, "Rutina local"


def build_validated_batch(raw_records):
    """Split raw dicts into accepted findings plus labeled rejections."""
    accepted = []
    rejected = []
    for position, raw_item in enumerate(raw_records, start=1):
        try:
            accepted.append(Finding.model_validate(raw_item))
        except ValidationError:
            rejected.append(f"registro {position}: rechazado en la frontera")
    return accepted, rejected


def describe_batch():
    """Prove the batch figures the three tests assert in test_modelo.py."""
    accepted, rejected = build_validated_batch(sample_records)
    report = FindingReport(threshold=FINDING_THRESHOLD)
    for finding in accepted:
        report.add(finding)
    counts = report.count_by_level()
    error_total, error_verdict = report.verdict()
    manual_probe = ManualFinding(1, "INFO", "servicio iniciado en localhost", "sensor-a")
    manual_ok = manual_probe.summary().startswith("[INFO]") and manual_probe.is_critical() is False
    lax_event = Finding.model_validate(
        {"finding_id": "7", "level": "INFO", "message": "inventario local actualizado", "source": "sensor-b"}
    )
    lax_ok = lax_event.finding_id == 7
    try:
        Finding.model_validate(
            {"finding_id": "7", "level": "INFO", "message": "inventario local actualizado", "source": "sensor-b"},
            strict=True,
        )
        strict_rejected = False
    except ValidationError:
        strict_rejected = True
    return counts, error_total, error_verdict, manual_ok, lax_ok, strict_rejected, len(accepted), len(rejected)


def main():
    """Run the modeled finding batch from the project root."""
    counts, error_total, error_verdict, manual_ok, lax_ok, strict_rejected, accepted_total, rejected_total = describe_batch()
    assert manual_ok, "La clase manual debia resumir y clasificar el hallazgo"
    assert lax_ok, "El modo lax debia convertir el texto 7 al entero 7"
    assert strict_rejected, "strict=True debia rechazar el texto 7 sin convertirlo"
    assert accepted_total == 6, "El lote debia aceptar 6 hallazgos"
    assert rejected_total == 0, "El lote debia rechazar 0 hallazgos"

    print("Pruebas del modelo: 3/3 en verde (unittest)")
    print(f"Conteo por nivel: INFO={counts['INFO']} WARNING={counts['WARNING']} ERROR={counts['ERROR']}")
    print(f"Errores (aceptados): {error_total} - {error_verdict}")
    print("Clase manual: resumen() e is_critical() en verde")
    print("Modelo validado: Field (1..140) y strict en verde")

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
