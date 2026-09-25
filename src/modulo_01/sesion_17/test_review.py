"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 17 (PyDefSec)
FILE: test_review.py (six local checks for the review batch)
PURPOSE: Lock contar_por_nivel plus validar_config and replay the
         Evento boundary with six unittest tests (normal, edge,
         error), runnable with unittest as the guaranteed runner and
         with pytest as the optional readable runner.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they save this
      file as test_review.py next to review_batch.py and run it from
      the project root with unittest first, then with pytest when
      available. Every test follows arrange-act-assert order and every
      assert carries a message in Spanish.
RUNNERS:
      python -m unittest test_review.py -v   (guaranteed, always works)
      pytest test_review.py -v               (optional, more readable)
==============================================================================

Conceptual sequence: evidence -> proven task -> auditable report.
Six tests mirror the six proof lines of review_batch.py; red means a
broken batch, green means the batch still holds.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from solution import (
    REVIEW_THRESHOLD,
    Evento,
    contar_por_nivel,
    sample_events,
    validar_config,
)
from pydantic import ValidationError


class TestReviewBatch(unittest.TestCase):
    """Six local checks: four for counts and config, two for the boundary."""

    def test_count_mixed_levels(self):
        """Mixed batch counts each allowed level exactly once per row."""
        # Arrange: ten local dicts with 4 INFO, 3 WARNING, 3 ERROR.
        batch = list(sample_events)
        # Act: count the batch by level.
        counts = contar_por_nivel(batch)
        # Assert: exact counts, so a lost row turns the test red.
        self.assertEqual(
            counts,
            {"INFO": 4, "WARNING": 3, "ERROR": 3},
            "Se esperaban 4 INFO, 3 WARNING y 3 ERROR en el lote de 10",
        )

    def test_count_empty_batch(self):
        """Empty batch is the lower edge: every counter stays at zero."""
        # Arrange: no rows at all (night without events).
        batch = []
        # Act: count the empty batch by level.
        counts = contar_por_nivel(batch)
        # Assert: zeros everywhere, never a missing key.
        self.assertEqual(
            counts,
            {"INFO": 0, "WARNING": 0, "ERROR": 0},
            "El lote vacio debia contar 0 en los tres niveles",
        )

    def test_count_ignores_unknown_level(self):
        """Unknown or missing levels never inflate the proven counts."""
        # Arrange: one invented level plus one row without level.
        batch = [
            {"event_id": 18, "level": "DEBUG", "message": "nivel inventado", "source": "sensor-a"},
            {"event_id": 19, "message": "fila sin nivel", "source": "sensor-b"},
            {"event_id": 1, "level": "INFO", "message": "servicio iniciado en localhost", "source": "sensor-a"},
        ]
        # Act: count the batch by level.
        counts = contar_por_nivel(batch)
        # Assert: only the INFO row counts; the other two are ignored.
        self.assertEqual(
            counts,
            {"INFO": 1, "WARNING": 0, "ERROR": 0},
            "DEBUG y filas sin nivel no debian contarse en ningun nivel",
        )

    def test_config_allows_local_review(self):
        """Local review config accepts the lab port and rejects edges."""
        # Arrange: lab port 18080 with an allowed level.
        # Act: check the valid config plus two rejected edges.
        valid_config = validar_config(18080, "INFO")
        bad_port = validar_config(0, "INFO")
        bad_level = validar_config(18080, "DEBUG")
        # Assert: valid passes, port 0 and DEBUG stay out.
        self.assertTrue(valid_config, "La config (18080, INFO) debia aceptarse")
        self.assertFalse(bad_port, "El puerto 0 debia rechazarse por fuera de rango")
        self.assertFalse(bad_level, "El nivel DEBUG debia rechazarse por no permitido")

    def test_evento_accepts_lax_numeric_string(self):
        """Lax mode converts the numeric string while strict rejects it."""
        # Arrange: record 15 arrives with event_id as text.
        raw_record = {
            "event_id": "15",
            "level": "INFO",
            "message": "inventario local actualizado",
            "source": "sensor-b",
        }
        # Act: validate once in lax mode (default).
        event = Evento.model_validate(raw_record)
        # Assert: lax converts "15" to 15 at this input boundary.
        self.assertEqual(
            event.event_id,
            15,
            "El modo lax debia convertir el texto 15 al entero 15",
        )
        # Assert: the same dict is rejected when strict forbids conversion.
        with self.assertRaises(
            ValidationError,
            msg="strict=True debia rechazar el texto 15 sin convertirlo",
        ):
            Evento.model_validate(raw_record, strict=True)

    def test_evento_rejects_missing_level(self):
        """Record without level is rejected with a field motive, never a crash."""
        # Arrange: record 16 arrives without its level key.
        raw_record = {"event_id": 16, "message": "linea sin nivel", "source": "sensor-a"}
        # Act plus assert: validation must raise, and the motive names level.
        with self.assertRaises(
            ValidationError,
            msg="El registro sin level debia rechazarse con ValidationError",
        ) as raised:
            Evento.model_validate(raw_record)
        self.assertIn(
            "level",
            str(raised.exception),
            "El motivo del rechazo debia nombrar el campo level",
        )


if __name__ == "__main__":
    unittest.main()
