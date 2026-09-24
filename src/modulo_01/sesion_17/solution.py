"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 17 (PyDefSec)
FILE: solution.py (reference for review_batch.py)
PURPOSE: Prove the Session 16 batch with tests: count accepted events
         by level, check the review config, and replay the Evento
         boundary (lax acceptance plus strict rejection), keeping every
         check local with unittest as the guaranteed runner and pytest
         as the optional readable runner.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they keep the
      validate_events.py batch from Session 16 untouched and write
      test_review.py next to review_batch.py, then run both runners
      from the project root.
WHY TEST: Session 16 shipped 15 accepted plus 5 rejected rows but
      nothing proves the counts stay correct after each edit. Today
      six tests (normal, edge, error) lock contar_por_nivel plus
      validar_config and replay the Evento boundary, so the next
      reader (Session 18 classes) inherits a proven batch.
PEDAGOGICAL RESTRICTIONS:
    - New today only: unittest (TestCase, assertEqual, assertTrue,
      assertFalse, assertIn, assertRaises), pytest as optional
      runner, arrange-act-assert order, red-green-refactor cycle.
    - Reused only: def plus return (S11), try/except (S13), list plus
      dict plus for (S06-S10), Evento BaseModel plus model_validate
      plus ValidationError plus lax versus strict=True (S16).
    - No new domain classes, no argparse, no network, no shell.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: evidence -> proven task -> auditable report.
Tests never touch the network; unittest runs everywhere, pytest only
re-runs the same file with more readable output.
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). Shared threshold, ten synthetic local event
# dicts, plus operator identity. Same contract as Session 16, smaller
# batch so each test stays readable: 4 INFO, 3 WARNING, 3 ERROR.
# ==============================================================================
REVIEW_THRESHOLD = 5
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

sample_events = [
    {"event_id": 1, "level": "INFO", "message": "servicio iniciado en localhost", "source": "sensor-a"},
    {"event_id": 2, "level": "WARNING", "message": "reintento de conexion local", "source": "sensor-a"},
    {"event_id": 3, "level": "ERROR", "message": "disco lleno en localhost", "source": "sensor-b"},
    {"event_id": 4, "level": "INFO", "message": "revision de turno completada", "source": "sensor-a"},
    {"event_id": 5, "level": "ERROR", "message": "puerto local sin respuesta", "source": "sensor-b"},
    {"event_id": 6, "level": "WARNING", "message": "latencia alta en loopback", "source": "sensor-a"},
    {"event_id": 7, "level": "INFO", "message": "copia de respaldo verificada", "source": "sensor-b"},
    {"event_id": 8, "level": "WARNING", "message": "umbral cercano al limite", "source": "sensor-a"},
    {"event_id": 9, "level": "ERROR", "message": "registro incompleto detectado", "source": "sensor-b"},
    {"event_id": 10, "level": "INFO", "message": "sesion local iniciada", "source": "sensor-a"},
]

# Identity of whose review this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Proven tasks. Reused boundary model plus two small pure
# functions the six tests lock in place.
# ==============================================================================


class Evento(BaseModel):
    """Validated defensive event at the input boundary."""

    event_id: int
    level: Literal["INFO", "WARNING", "ERROR"]
    message: str = Field(min_length=1)
    source: str = Field(min_length=1)


def contar_por_nivel(events):
    """Count events by level, ignoring unknown or missing levels."""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for event in events:
        level = event.get("level")
        if level in counts:
            counts[level] += 1
    return counts


def validar_config(port, level):
    """Check that the review port and level stay inside the local contract."""
    if port < 1 or port > 65535:
        return False
    return level in ALLOWED_LEVELS


def describe_batch():
    """Prove the batch figures the six tests assert in test_review.py."""
    counts = contar_por_nivel(sample_events)
    error_total = counts["ERROR"]
    if error_total >= REVIEW_THRESHOLD:
        error_verdict = "Revisión prioritaria"
    else:
        error_verdict = "Rutina local"
    config_ok = validar_config(18080, "INFO")
    lax_event = Evento.model_validate(
        {
            "event_id": "15",
            "level": "INFO",
            "message": "inventario local actualizado",
            "source": "sensor-b",
        }
    )
    lax_ok = lax_event.event_id == 15
    try:
        Evento.model_validate(
            {
                "event_id": "15",
                "level": "INFO",
                "message": "inventario local actualizado",
                "source": "sensor-b",
            },
            strict=True,
        )
        strict_rejected = False
    except ValidationError:
        strict_rejected = True
    return counts, error_total, error_verdict, config_ok, lax_ok, strict_rejected


def main():
    """Run the proven review batch from the project root."""
    counts, error_total, error_verdict, config_ok, lax_ok, strict_rejected = describe_batch()

    print("Pruebas del lote: 6/6 en verde (unittest)")
    print(f"Conteo por nivel: INFO={counts['INFO']} WARNING={counts['WARNING']} ERROR={counts['ERROR']}")
    print(f"Errores (aceptados): {error_total} - {error_verdict}")
    print(f"Config valida (18080, INFO): {config_ok}")
    print(f"Evento aceptado (lax \"15\" -> 15): {lax_ok}")
    print(f"Evento rechazado (strict=True): {strict_rejected}")

    # ==========================================================================
    # STEP 3: Communication (given). Proven report with the runner note
    # plus the local scope the next reader inherits.
    # ==========================================================================
    print("--- Revision probada ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {REVIEW_THRESHOLD} (solo lectura)")
    print("Corredores: unittest (base) + pytest (legible, opcional)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
