"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 18 (PyDefSec)
FILE: test_modelo.py (three local checks for the finding model)
PURPOSE: Lock the Finding evolution with three unittest tests
         (normal, error, strict boundary), runnable with unittest as
         the guaranteed runner and with pytest as the optional
         readable runner.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they save this
      file as test_modelo.py next to finding_model.py and run it from
      the project root with unittest first, then with pytest when
      available. Every test follows arrange-act-assert order and every
      assert carries a message in Spanish.
RUNNERS:
      python -m unittest test_modelo.py -v   (guaranteed, always works)
      pytest test_modelo.py -v               (optional, more readable)
==============================================================================

Conceptual sequence: evidence -> modeled task -> auditable report.
Three tests mirror the three proven lines of finding_model.py; red
means a broken model, green means the evolution still holds.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from solution import (
    FINDING_THRESHOLD,
    Finding,
    ManualFinding,
    sample_records,
)
from pydantic import ValidationError


class TestFindingModel(unittest.TestCase):
    """Three local checks: manual anatomy, acceptance, strict rejection."""

    def test_manual_finding_summarizes_and_classifies(self):
        """Manual class exposes anatomy before any BaseModel exists."""
        # Arrange: one local finding built with the manual constructor.
        probe = ManualFinding(1, "INFO", "servicio iniciado en localhost", "sensor-a")
        # Act: ask the object for its summary plus its critical flag.
        summary = probe.summary()
        critical = probe.is_critical()
        # Assert: summary carries the level and INFO is not critical.
        self.assertTrue(
            summary.startswith("[INFO]"),
            "El resumen manual debia empezar con el nivel [INFO]",
        )
        self.assertFalse(
            critical,
            "Un hallazgo INFO no debia marcarse como critico",
        )

    def test_validated_finding_accepts_valid_record(self):
        """Valid record is accepted with every field stored exactly."""
        # Arrange: first local record of the batch (INFO, id 1).
        raw_record = dict(sample_records[0])
        # Act: validate the record at the BaseModel boundary.
        finding = Finding.model_validate(raw_record)
        # Assert: exact fields, so a lost attribute turns the test red.
        self.assertEqual(
            finding.finding_id,
            1,
            "El hallazgo valido debia conservar finding_id igual a 1",
        )
        self.assertEqual(
            (finding.level, finding.message, finding.source),
            ("INFO", "servicio iniciado en localhost", "sensor-a"),
            "El hallazgo valido debia conservar nivel, mensaje y origen",
        )

    def test_validated_finding_rejects_empty_message_and_strict_text_id(self):
        """Empty message is rejected and strict rejects the text id."""
        # Arrange: record 7 arrives with an empty message text.
        bad_record = {
            "finding_id": 7,
            "level": "INFO",
            "message": "",
            "source": "sensor-a",
        }
        # Act plus assert: validation must raise with a motive naming message.
        with self.assertRaises(
            ValidationError,
            msg="El mensaje vacio debia rechazarse con ValidationError",
        ) as raised:
            Finding.model_validate(bad_record)
        self.assertIn(
            "message",
            str(raised.exception),
            "El motivo del rechazo debia nombrar el campo message",
        )
        # Arrange: the same boundary receives the id as text "7".
        lax_record = {
            "finding_id": "7",
            "level": "INFO",
            "message": "inventario local actualizado",
            "source": "sensor-b",
        }
        # Act: validate once in lax mode (default converts the text).
        lax_event = Finding.model_validate(lax_record)
        # Assert: lax converts "7" to 7 at this input boundary.
        self.assertEqual(
            lax_event.finding_id,
            7,
            "El modo lax debia convertir el texto 7 al entero 7",
        )
        # Assert: the same dict is rejected when strict forbids conversion.
        with self.assertRaises(
            ValidationError,
            msg="strict=True debia rechazar el texto 7 sin convertirlo",
        ):
            Finding.model_validate(lax_record, strict=True)


if __name__ == "__main__":
    unittest.main()
