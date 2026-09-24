"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 20 (PyDefSec)
FILE: solution.py (canonical instructor reference solution)
PURPOSE: Defend the Session 19 checkpoint analyzer in a 3-minute brief:
         explain two design decisions, correct the assigned edge live,
         and close Checkpoint 1 with a signed defense record (Block A).
SCOPE: Localhost authorized testing environment (127.0.0.1 / ::1) only.
==============================================================================
DESIGN DECISIONS (the two defended choices):
1. Boundary-first validation: every raw dict crosses the Session 18
   Finding model before any count, so parsers never decide validity.
2. Rejection with position: each refused row becomes a labeled string
   with its record number, so the 20 -> 17 + 3 split stays auditable.
ASSIGNED EDGE (corrected live): the night id arrives as text "31".
   Lax mode converts it silently; the fix normalizes it to int first
   and then validates with strict=True, keeping the report honest.
PEDAGOGICAL RESTRICTIONS:
    - Reused only: def plus return (S11), try/except (S13), list plus
      dict plus for (S06-S10), classes plus BaseModel (S18), unittest
      plus assertRaises (S17), json plus csv plus prints (S15-S16).
    - New today: nothing. Defense plus one bounded edge fix, no syntax.
    - No argparse, no sockets, no subprocess, no shell, no network.
    - 100% English PEP 8 identifiers and comments. User lines in
      Spanish for the local reader.
==============================================================================

Conceptual sequence: evidence -> defense -> auditable record.
Re-run the shift, name two decisions, fix the edge, sign the record.
"""

import csv
import io
import json
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). The defended Session 19 shift: one 20-event
# batch in three local formats, one shared read-only threshold, plus
# operator identity. No network, no files: local synthetic evidence.
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

# Assigned edge (given): the night id arrives as text, not as int.
EDGE_RECORD = {
    "finding_id": "31",
    "level": "INFO",
    "message": "inventario nocturno actualizado",
    "source": "sensor-b",
}


# ==============================================================================
# Finding base (inherited thread from Session 18). Same schema, same
# limits: the defense reuses the proven boundary unchanged.
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
# STEP 2: Defense tasks. Same three parsers, same shared validator,
# same counter as Session 19, plus the one assigned edge correction.
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


def normalize_edge_record(raw_record):
    """Fix the assigned edge: text id becomes int before strict check."""
    fixed = dict(raw_record)
    fixed["finding_id"] = int(str(fixed["finding_id"]).strip())
    fixed["level"] = str(fixed["level"]).strip()
    fixed["message"] = str(fixed["message"]).strip()
    fixed["source"] = str(fixed["source"]).strip()
    return Finding.model_validate(fixed, strict=True)


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
# STEP 3: Communication (given). Three-minute defense lines, the live
# edge correction, and the signed record that closes Checkpoint 1.
# ==============================================================================
def main():
    """Defend the analyzer, fix the edge live, sign the record."""
    figures, report = analyze_shift()
    assert figures["raw_total"] == 20, "La defensa debia leer 20 eventos crudos"
    assert figures["accepted_total"] == 17, "La defensa debia aceptar 17 hallazgos"
    assert figures["rejected_total"] == 3, "La defensa debia rechazar 3 filas"
    assert figures["counts"] == {"INFO": 7, "WARNING": 4, "ERROR": 6}, "Conteos fuera de contrato"
    assert figures["error_total"] == 6, "La defensa debia contar 6 errores aceptados"
    assert figures["error_verdict"] == "Revision prioritaria", "6 errores sobre umbral 5 es prioritario"
    fixed_edge = normalize_edge_record(EDGE_RECORD)
    assert fixed_edge.finding_id == 31, "El borde debia corregirse al entero 31"
    assert fixed_edge.level == "INFO", "El borde corregido debia conservar INFO"

    print("Defensa Checkpoint 1 — Bloque A (20/20)")
    print(f"Operador: {student_name} ({student_id})")
    print("Decision 1: frontera primero (todo dict cruza Finding antes de contar)")
    print("Decision 2: rechazo con posicion (cada fila rota viaja con su motivo)")
    print(f"Conteo por nivel: INFO={figures['counts']['INFO']} WARNING={figures['counts']['WARNING']} ERROR={figures['counts']['ERROR']}")
    print(f"Eventos: {figures['raw_total']} crudos -> {figures['accepted_total']} aceptados + {figures['rejected_total']} rechazados")
    print(f"Errores (aceptados): {figures['error_total']} - {figures['error_verdict']}")
    print('Borde asignado: texto "31" -> 31 (strict en verde)')
    print("Acta de defensa: APROBADA — Checkpoint 1 cerrado, Bloque A 20/20")
    print("--- Reporte del checkpoint ---")
    for line in format_report(figures):
        print(line)


if __name__ == "__main__":
    main()
