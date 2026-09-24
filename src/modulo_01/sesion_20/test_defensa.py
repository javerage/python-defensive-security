"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 20 (PyDefSec)
FILE: test_defensa.py (defense checks for Checkpoint 1)
PURPOSE: Lock the brief defense with unittest tests (analyzer rerun,
         counts, verdict, corrected edge, strict boundary, local scope),
         runnable with unittest as the guaranteed runner.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they save this
      file as test_defensa.py next to defensa.py and run it from the
      project root with unittest. Every test follows arrange-act-assert
      order and every assert carries a message in Spanish. Checkpoint 1,
      part of 30%. Closes Block A (20/20).
RUNNERS:
      python -m unittest test_defensa.py -v   (guaranteed, always works)
==============================================================================

Conceptual sequence: evidence -> defense -> auditable record.
Green means the defense still holds and the record can be signed.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from solution import (
    EDGE_RECORD,
    FINDING_THRESHOLD,
    Finding,
    analyze_shift,
    format_report,
    normalize_edge_record,
)
from pydantic import ValidationError


class TestBriefDefense(unittest.TestCase):
    """Teacher checks: defended analyzer plus corrected edge."""

    def test_defended_shift_totals_raw_accepted_rejected(self):
        """Defended shift reads 20 raw events: 17 accepted plus 3 rejected."""
        # Arrange: the defended Session 19 shift payloads.
        # Act: re-run the full shift pipeline.
        figures, _report = analyze_shift()
        # Assert: totals match the checkpoint contract exactly.
        self.assertEqual(
            (figures["raw_total"], figures["accepted_total"], figures["rejected_total"]),
            (20, 17, 3),
            "La defensa debia leer 20 crudos: 17 aceptados + 3 rechazados",
        )

    def test_defended_counts_by_level(self):
        """Defended findings group as INFO 7, WARNING 4, ERROR 6."""
        # Arrange: the analyzed shift figures.
        # Act: read the counts from the figures dict.
        figures, _report = analyze_shift()
        # Assert: counts match the checkpoint contract exactly.
        self.assertEqual(
            figures["counts"],
            {"INFO": 7, "WARNING": 4, "ERROR": 6},
            "Los conteos debian ser INFO=7 WARNING=4 ERROR=6",
        )

    def test_defended_verdict_priority_above_threshold(self):
        """Six accepted ERROR rows on threshold 5 mean priority review."""
        # Arrange: the shared read-only threshold of the checkpoint.
        # Act: re-run the shift and read its verdict pair.
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

    def test_assigned_edge_corrected_to_int_and_strict_passes(self):
        """Assigned edge text "31" is fixed to 31 and passes strict."""
        # Arrange: the night id that arrives as text.
        raw_edge = dict(EDGE_RECORD)
        # Act: apply the live correction.
        fixed_edge = normalize_edge_record(raw_edge)
        # Assert: the corrected id is the integer 31 with INFO kept.
        self.assertEqual(
            (fixed_edge.finding_id, fixed_edge.level),
            (31, "INFO"),
            "El borde debia corregirse al entero 31 conservando INFO",
        )

    def test_assigned_edge_rejected_without_correction_in_strict(self):
        """The same edge dict without correction fails the strict check."""
        # Arrange: the uncorrected night id as text.
        raw_edge = dict(EDGE_RECORD)
        # Act plus assert: strict validation must raise.
        with self.assertRaises(
            ValidationError,
            msg="strict=True debia rechazar el texto 31 sin corregirlo",
        ):
            Finding.model_validate(raw_edge, strict=True)

    def test_defense_record_confined_to_localhost_with_operator(self):
        """Defense record carries the operator, the counts, and local scope."""
        # Arrange: the analyzed shift figures.
        # Act: build the fixed-width checkpoint report lines.
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
