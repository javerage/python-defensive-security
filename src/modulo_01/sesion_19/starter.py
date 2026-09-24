"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 19 (PyDefSec)
FILE: starter.py (guided skeleton for analizar.py)
PURPOSE: Integrate Modules M1-M10 into one local analyzer (text plus
         JSON plus CSV plus counts plus report) that passes the teacher
         checkpoint tests. The text parser below is the worked partial
         example for the no-Pi route: every student can run and study
         it with no account. Pi is observer only in this session.
NOTE: The repository is only a backup. Create analizar.py manually
      in your Session 01 project and complete each task marked TODO.
      This skeleton compiles and runs; PENDING marks unfinished work,
      and replaced placeholders give the expected checkpoint report.
      Run from the project root:
          python analizar.py
          python -m unittest test_analizar.py -v

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Keep the finding batch from Session 18
    untouched, then save your work as analizar.py and run from the
    project root.

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the mapping table in your student material first: it holds
    the 20 local events, the shared threshold (5), and the parse plus
    validate plus count note.

    BEFORE COMPLETING EACH TODO, PREDICT FIRST: write on paper the
    value you expect and why; then run the script and compare what you
    got with your prediction and with the expected-output block
    (predict -> execute -> compare). TODO comments never hold answers.

ORDER: evidence above, integration tasks in the middle, auditable
    report at the end. No argparse, no sockets, no subprocess, no
    shell, no network. Pi observes only: it never writes nor runs.
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
# shared read-only threshold, plus operator identity.
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
# Finding base (given, inherited from Session 18). Do not modify: the
# checkpoint reuses this proven boundary unchanged.
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
# STEP 2: Integration tasks (TODO). Worked text example is given; the
# JSON plus CSV plus validate plus count tasks are yours. Predict each
# value on paper before you run.
# ==============================================================================
def parse_text_log(raw_text):
    """Split pipe-separated lines into raw finding dicts (worked example)."""
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


# TODO 2.1: Parse the JSON array into raw finding dicts. Load the text
# with the JSON reader, keep each dict item as one raw record, and turn
# each non-dict item into one labeled boundary rejection.
def parse_json_payload(raw_text):
    """Load the JSON array into raw finding dicts."""
    records = []
    errors = []
    # TODO: replace this PENDING stub with the JSON reader logic.
    return records, errors


# TODO 2.2: Parse the CSV rows into raw finding dicts. Read the header
# plus rows with the CSV reader, keep the four columns of each row as
# one raw record, and turn each row with missing columns into one
# labeled boundary rejection.
def parse_csv_payload(raw_text):
    """Read the CSV rows into raw finding dicts."""
    records = []
    errors = []
    # TODO: replace this PENDING stub with the CSV reader logic.
    return records, errors


# TODO 2.3: Split raw dicts into accepted findings plus labeled
# rejections. Validate each raw dict at the Finding boundary, append
# each accepted finding, and label each rejected dict with its
# position so no broken row travels silently.
def validate_records(raw_records, first_position):
    """Split raw dicts into accepted findings plus labeled rejections."""
    accepted = []
    rejected = []
    # TODO: replace this PENDING stub with the boundary loop.
    return accepted, rejected


# TODO 2.4: Run the full shift in analyze_shift. Parse the three
# payloads, validate each batch at its own first position, group the
# accepted findings in FindingReport, and return the figures dict plus
# the report. Count accepted rows only; rejected rows never reach the
# counter.
def analyze_shift():
    """Run the full shift: parse, validate, count, pair with threshold."""
    # TODO: replace this PENDING partial run with the full pipeline.
    # Partial no-Pi route: text only, so the script already runs.
    # The text batch crosses the real boundary inline; the JSON plus
    # CSV batches wait for validate_records in TODO 2.3.
    text_records, text_errors = parse_text_log(TEXT_LOG)
    accepted = []
    text_rejected = []
    for offset, raw_item in enumerate(text_records):
        try:
            accepted.append(Finding.model_validate(raw_item))
        except ValidationError:
            text_rejected.append(f"registro {1 + offset}: rechazado en la frontera")
    rejected = text_rejected + text_errors
    report = FindingReport(threshold=FINDING_THRESHOLD)
    for finding in accepted:
        report.add(finding)
    counts = report.count_by_level()
    error_total, error_verdict = report.verdict()
    figures = {
        "raw_total": len(text_records) + len(text_errors),
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
        "| DEFENSIVE AUDIT REPORT — SESSION 19 (PARCIAL: solo texto)                   |",
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
# STEP 3: Communication (given). Partial proof lines plus the partial
# report. The full checkpoint report replaces PENDING values only.
# ==============================================================================
def main():
    """Run the shift analyzer from the project root."""
    figures, report = analyze_shift()
    print("Ruta sin Pi: ejemplo parcial (texto) en ejecucion")
    print(f"Conteo por nivel: INFO={figures['counts']['INFO']} WARNING={figures['counts']['WARNING']} ERROR={figures['counts']['ERROR']}")
    print(f"Eventos: {figures['raw_total']} crudos -> {figures['accepted_total']} aceptados + {figures['rejected_total']} rechazados")
    print(f"Errores (aceptados): {figures['error_total']} - {figures['error_verdict']}")
    print("--- Reporte del checkpoint (PARCIAL) ---")
    for line in format_report(figures):
        print(line)


if __name__ == "__main__":
    main()
