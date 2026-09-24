"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 19 (PyDefSec)
FILE: test_analizar.py (eight teacher checks for the checkpoint analyzer)
PURPOSE: Lock the Checkpoint 1 analyzer with eight unittest tests
         (parsers, totals, counts, verdict, strict boundary, local
         scope), runnable with unittest as the guaranteed runner and
         with pytest as the optional readable runner.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they save this
      file as test_analizar.py next to analizar.py and run it from
      the project root with unittest first, then with pytest when
      available. Every test follows arrange-act-assert order and every
      assert carries a message in Spanish. Checkpoint 1, part of 30%.
RUNNERS:
      python -m unittest test_analizar.py -v   (guaranteed, always works)
      pytest test_analizar.py -v               (optional, more readable)
==============================================================================

Conceptual sequence: evidence -> integration task -> auditable report.
Eight tests mirror the eight proven lines of analizar.py; red means
a broken integration, green means the checkpoint still holds.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from solution import (
    CSV_PAYLOAD,
    FINDING_THRESHOLD,
    JSON_PAYLOAD,
    TEXT_LOG,
    Finding,
    analyze_shift,
    format_report,
    parse_csv_payload,
    parse_json_payload,
    parse_text_log,
    validate_records,
)
from pydantic import ValidationError


class TestCheckpointAnalyzer(unittest.TestCase):
    """Eight teacher checks: parsers, totals, verdict, boundary, scope."""

    def test_text_parser_accepts_seven_and_rejects_malformed(self):
        """Text log yields seven records plus one format rejection."""
        # Arrange: the eight local text lines of the shift.
        raw_text = TEXT_LOG
        # Act: split the lines into records plus errors.
        records, errors = parse_text_log(raw_text)
        # Assert: seven records travel on, one malformed line is labeled.
        self.assertEqual(
            len(records),
            7,
            "El texto debia producir 7 registros crudos",
        )
        self.assertEqual(
            len(errors),
            1,
            "El texto debia producir 1 rechazo de formato",
        )

    def test_json_parser_rejects_debug_level_at_boundary(self):
        """JSON batch parses six rows; DEBUG dies at the Finding boundary."""
        # Arrange: the six local JSON rows of the shift.
        json_records, _json_errors = parse_json_payload(JSON_PAYLOAD)
        # Act: validate the batch starting at position 9.
        accepted, rejected = validate_records(json_records, 9)
        # Assert: five accepted, one rejected (the invented DEBUG level).
        self.assertEqual(
            len(accepted),
            5,
            "El JSON debia aceptar 5 hallazgos",
        )
        self.assertEqual(
            len(rejected),
            1,
            "El JSON debia rechazar 1 fila (nivel DEBUG)",
        )

    def test_csv_parser_rejects_empty_message_at_boundary(self):
        """CSV batch parses six rows; the empty message dies at the boundary."""
        # Arrange: the six local CSV rows of the shift.
        csv_records, _csv_errors = parse_csv_payload(CSV_PAYLOAD)
        # Act: validate the batch starting at position 15.
        accepted, rejected = validate_records(csv_records, 15)
        # Assert: five accepted, one rejected (the empty message).
        self.assertEqual(
            len(accepted),
            5,
            "El CSV debia aceptar 5 hallazgos",
        )
        self.assertEqual(
            len(rejected),
            1,
            "El CSV debia rechazar 1 fila (mensaje vacio)",
        )

    def test_shift_totals_raw_accepted_rejected(self):
        """Whole shift reads 20 raw events: 17 accepted plus 3 rejected."""
        # Arrange: the three payloads analyzed as one shift.
        # Act: run the full shift pipeline.
        figures, _report = analyze_shift()
        # Assert: totals match the checkpoint contract exactly.
        self.assertEqual(
            (figures["raw_total"], figures["accepted_total"], figures["rejected_total"]),
            (20, 17, 3),
            "El turno debia leer 20 crudos: 17 aceptados + 3 rechazados",
        )

    def test_shift_counts_by_level(self):
        """Accepted findings group as INFO 7, WARNING 4, ERROR 6."""
        # Arrange: the analyzed shift figures.
        # Act: read the counts from the figures dict.
        figures, _report = analyze_shift()
        # Assert: counts match the checkpoint contract exactly.
        self.assertEqual(
            figures["counts"],
            {"INFO": 7, "WARNING": 4, "ERROR": 6},
            "Los conteos debian ser INFO=7 WARNING=4 ERROR=6",
        )

    def test_shift_verdict_priority_above_threshold(self):
        """Six accepted ERROR rows on threshold 5 mean priority review."""
        # Arrange: the shared read-only threshold of the checkpoint.
        # Act: run the shift and read its verdict pair.
        figures, _report = analyze_shift()
        # Assert: threshold stands at 5 and the verdict is priority.
        self.assertEqual(
            FINDING_THRESHOLD,
            5,
            "El umbral del checkpoint debia ser 5",
        )
        self.assertEqual(
            (figures["error_total"], figures["error_verdict"]),
            (6, "Revision prioritaria"),
            "6 errores sobre el umbral 5 debian dar Revision prioritaria",
        )

    def test_boundary_rejects_long_message_and_strict_text_id(self):
        """The 141-char message dies; lax converts 31 but strict rejects it."""
        # Arrange: a message one char over the 140 limit.
        long_record = {
            "finding_id": 30,
            "level": "INFO",
            "message": "x" * 141,
            "source": "sensor-a",
        }
        # Act plus assert: validation must raise naming message.
        with self.assertRaises(
            ValidationError,
            msg="El mensaje de 141 caracteres debia rechazarse",
        ) as raised:
            Finding.model_validate(long_record)
        self.assertIn(
            "message",
            str(raised.exception),
            "El motivo del rechazo debia nombrar el campo message",
        )
        # Arrange: the same boundary receives the id as text "31".
        lax_record = {
            "finding_id": "31",
            "level": "INFO",
            "message": "inventario nocturno actualizado",
            "source": "sensor-b",
        }
        # Act: validate once in lax mode (default converts the text).
        lax_event = Finding.model_validate(lax_record)
        # Assert: lax converts "31" to 31 at this input boundary.
        self.assertEqual(
            lax_event.finding_id,
            31,
            "El modo lax debia convertir el texto 31 al entero 31",
        )
        # Assert: the same dict is rejected when strict forbids conversion.
        with self.assertRaises(
            ValidationError,
            msg="strict=True debia rechazar el texto 31 sin convertirlo",
        ):
            Finding.model_validate(lax_record, strict=True)

    def test_report_confined_to_localhost_with_operator(self):
        """Report carries the operator, the counts, and the local scope."""
        # Arrange: the analyzed shift figures.
        # Act: build the fixed-width report lines.
        figures, _report = analyze_shift()
        lines = format_report(figures)
        text = "\n".join(lines)
        # Assert: operator plus scope plus figures are all visible.
        self.assertIn(
            "Alex Mendez",
            text,
            "El reporte debia llevar el nombre del operador",
        )
        self.assertIn(
            "DEF-2026-09",
            text,
            "El reporte debia llevar el identificador del operador",
        )
        self.assertIn(
            "127.0.0.1",
            text,
            "El reporte debia declarar el alcance localhost",
        )
        self.assertNotIn(
            "socket",
            text.lower(),
            "El reporte no debia mencionar sockets ni red",
        )


if __name__ == "__main__":
    unittest.main()
