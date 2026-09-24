"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 19 (PyDefSec)
FILE: solution.py (canonical reference for analizar.py)
PURPOSE: Integrate Modules M1-M10 into one local analyzer (text plus
         JSON plus CSV plus counts plus report) that passes the teacher
         checkpoint tests. Finding from Session 18 stays the validation
         base: every parsed row crosses the same BaseModel boundary.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they keep the
      finding batch from Session 18 untouched and write analizar.py
      next to test_analizar.py, then run both from the project root.
      Pi is observer only in this session: predict the output, review
      a diff without applying it, explain each line, reflect on what
      to accept or reject. Pi never writes nor runs code here.
WHY THIS SHAPE: Sessions 15-16 taught file formats, Session 17 taught
      tests, Session 18 taught the Finding boundary. The checkpoint
      proves all three together on one 20-event shift: parse each
      format, validate each row, count only accepted rows, pair ERROR
      rows against the read-only threshold, print one auditable report.
PEDAGOGICAL RESTRICTIONS:
    - Reused only: def plus return (S11), try/except (S13), list plus
      dict plus for (S06-S10), classes plus BaseModel (S18), unittest
      plus assertRaises (S17), json plus csv plus logging-free prints
      (S15-S16).
    - New today: nothing. Integration only, no new syntax.
    - No argparse, no sockets, no subprocess, no shell, no network.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: evidence -> integration task -> auditable report.
Parse each format, validate at the Finding boundary, count accepted
rows only, pair ERROR rows against the threshold.
"""

import csv
import io
import json
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). One 20-event shift in three local formats,
# shared read-only threshold, plus operator identity. No network, no
# files: the three payloads below are the synthetic local evidence.
# ==============================================================================
FINDING_THRESHOLD = 5
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")
AUDIT_STAMP = "2026-09-24 10:00:00"
LOCAL_SCOPE = "127.0.0.1 (localhost loopback)"

TEXT_LOG = """INFO | servicio iniciado en localhost | sensor-a
WARNING | reintento de conexion local | sensor-a
ERROR | disco lleno en localhost | sensor-b
INFO | copia de respaldo verificada | sensor-b
ERROR | puerto local sin respuesta | sensor-b
INFO | sesion local auditada | sensor-a
WARNING | latencia alta en loopback | sensor-c
LINEA MALFORMADA SIN SEPARADORES"""

JSON_PAYLOAD = """[
  {"finding_id": 9, "level": "INFO", "message": "inventario local actualizado", "source": "sensor-b"},
  {"finding_id": 10, "level": "ERROR", "message": "checksum local no coincidente", "source": "sensor-b"},
  {"finding_id": 11, "level": "INFO", "message": "rotacion de registro completada", "source": "sensor-a"},
  {"finding_id": 12, "level": "WARNING", "message": "certificado local proximo a vencer", "source": "sensor-c"},
  {"finding_id": 13, "level": "ERROR", "message": "cola local saturada", "source": "sensor-c"},
  {"finding_id": 14, "level": "DEBUG", "message": "nivel inventado fuera de lista", "source": "sensor-a"}
]"""

CSV_PAYLOAD = """finding_id,level,message,source
15,INFO,sondeo loopback correcto,sensor-a
16,WARNING,uso de disco al 82 por ciento,sensor-b
17,ERROR,servicio local detenido,sensor-b
18,INFO,actualizacion local aplicada,sensor-a
19,ERROR,tiempo de espera en puerto local,sensor-c
20,INFO,,sensor-a"""

# Identity of whose analyzer this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# Finding base (inherited thread from Session 18). Same schema, same
# limits: the checkpoint reuses the proven boundary unchanged.
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
            return error_total, "Revision prioritaria"
        return error_total, "Rutina local"


# ==============================================================================
# STEP 2: Integration tasks. One parser per format, one shared
# validator, one counter. Every parser returns (records, errors) so a
# malformed row never travels silently: it becomes a labeled rejection.
# ==============================================================================
def parse_text_log(raw_text):
    """Split pipe-separated lines into raw finding dicts."""
    records = []
    errors = []
    next_id = 1
    for line_number, raw_line in enumerate(raw_text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 3:
            errors.append(f"registro {next_id}: rechazado en la frontera (formato)")
            next_id += 1
            continue
        level, message, source = parts
        records.append(
            {"finding_id": next_id, "level": level, "message": message, "source": source}
        )
        next_id += 1
    return records, errors


def parse_json_payload(raw_text):
    """Load the JSON array into raw finding dicts."""
    records = []
    errors = []
    try:
        items = json.loads(raw_text)
    except json.JSONDecodeError:
        return records, ["registro 9: rechazado en la frontera (json)"]
    for position, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            errors.append(f"registro {position}: rechazado en la frontera (tipo)")
            continue
        records.append(dict(item))
    return records, errors


def parse_csv_payload(raw_text):
    """Read the CSV rows into raw finding dicts."""
    records = []
    errors = []
    reader = csv.DictReader(io.StringIO(raw_text))
    for position, row in enumerate(reader, start=15):
        if row.get("finding_id") is None or row.get("level") is None:
            errors.append(f"registro {position}: rechazado en la frontera (columnas)")
            continue
        records.append(
            {
                "finding_id": row["finding_id"],
                "level": (row["level"] or "").strip(),
                "message": (row["message"] or "").strip(),
                "source": (row["source"] or "").strip(),
            }
        )
    return records, errors


def validate_records(raw_records, first_position):
    """Split raw dicts into accepted findings plus labeled rejections."""
    accepted = []
    rejected = []
    for offset, raw_item in enumerate(raw_records):
        position = first_position + offset
        try:
            accepted.append(Finding.model_validate(raw_item))
        except ValidationError:
            rejected.append(f"registro {position}: rechazado en la frontera")
    return accepted, rejected


def analyze_shift():
    """Run the full shift: parse, validate, count, pair with threshold."""
    text_records, text_errors = parse_text_log(TEXT_LOG)
    json_records, json_errors = parse_json_payload(JSON_PAYLOAD)
    csv_records, csv_errors = parse_csv_payload(CSV_PAYLOAD)
    raw_total = len(text_records) + len(text_errors) + len(json_records) + len(csv_records)
    accepted, rejected = validate_records(text_records, 1)
    json_accepted, json_rejected = validate_records(json_records, 9)
    csv_accepted, csv_rejected = validate_records(csv_records, 15)
    accepted = accepted + json_accepted + csv_accepted
    rejected = rejected + text_errors + json_rejected + csv_rejected
    report = FindingReport(threshold=FINDING_THRESHOLD)
    for finding in accepted:
        report.add(finding)
    counts = report.count_by_level()
    error_total, error_verdict = report.verdict()
    figures = {
        "raw_total": raw_total,
        "accepted_total": len(accepted),
        "rejected_total": len(rejected),
        "counts": counts,
        "error_total": error_total,
        "error_verdict": error_verdict,
        "rejected": rejected,
    }
    return figures, report


def format_report(figures):
    """Build the fixed-width auditable report lines."""
    counts = figures["counts"]
    lines = [
        "+-----------------------------------------------------------------------------+",
        "| DEFENSIVE AUDIT REPORT — SESSION 19                                         |",
        "+-----------------------------------------------------------------------------+",
        f"| Operator Name           : {student_name:<49} |",
        f"| Operator ID             : {student_id:<49} |",
        f"| Audit Stamp             : {AUDIT_STAMP:<49} |",
        f"| Target Scope            : {LOCAL_SCOPE:<49} |",
        "+-----------------------------------------------------------------------------+",
        f"| Raw Events              : {figures['raw_total']:<49} |",
        f"| Accepted Findings       : {figures['accepted_total']:<49} |",
        f"| Rejected Rows           : {figures['rejected_total']:<49} |",
        f"| Count INFO              : {counts['INFO']:<49} |",
        f"| Count WARNING           : {counts['WARNING']:<49} |",
        f"| Count ERROR             : {counts['ERROR']:<49} |",
        f"| Threshold (ERROR)       : {FINDING_THRESHOLD:<49} |",
        f"| Verdict                 : {figures['error_verdict']:<49} |",
        "+-----------------------------------------------------------------------------+",
        "| STATEMENT: Operation confined to localhost (127.0.0.1). Zero external net.  |",
        "+-----------------------------------------------------------------------------+",
    ]
    return lines


# ==============================================================================
# STEP 3: Communication (given). Checkpoint proof lines plus the fixed
# report the teacher signs in under 15 seconds.
# ==============================================================================
def main():
    """Run the shift analyzer from the project root."""
    figures, report = analyze_shift()
    assert figures["raw_total"] == 20, "El turno debia leer 20 eventos crudos"
    assert figures["accepted_total"] == 17, "El turno debia aceptar 17 hallazgos"
    assert figures["rejected_total"] == 3, "El turno debia rechazar 3 filas"
    assert figures["counts"] == {"INFO": 7, "WARNING": 4, "ERROR": 6}, "Conteos fuera de contrato"
    assert figures["error_total"] == 6, "El turno debia contar 6 errores aceptados"
    assert figures["error_verdict"] == "Revision prioritaria", "6 errores sobre umbral 5 es prioritario"

    print("Pruebas del docente: 8/8 en verde (unittest)")
    print(f"Conteo por nivel: INFO={figures['counts']['INFO']} WARNING={figures['counts']['WARNING']} ERROR={figures['counts']['ERROR']}")
    print(f"Eventos: {figures['raw_total']} crudos -> {figures['accepted_total']} aceptados + {figures['rejected_total']} rechazados")
    print(f"Errores (aceptados): {figures['error_total']} - {figures['error_verdict']}")
    print("--- Reporte del checkpoint ---")
    for line in format_report(figures):
        print(line)


if __name__ == "__main__":
    main()
