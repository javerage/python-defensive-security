"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 17 (PyDefSec)
FILE: homework_solution.py (reference for review_shift.py)
PURPOSE: Prove the night-shift batch with the same tested technique
         as class: the same Evento model plus contar_por_nivel and
         validar_config turn raw shift dicts into accepted rows plus
         labeled rejections, checked by six inline asserts with
         messages before the shift report is printed.
NOTE: Homework after class, outside the 60 minutes. Create
      review_shift.py manually in your Session 01 project, reusing
      the tested technique from class. Check this reference only
      after trying alone.
WHY TEST: The night shift reuses the day technique on new data: 10
      raw dicts (7 exact, 1 lax numeric string, 2 invalid) become 8
      accepted plus 2 rejected, and six inline checks prove the
      figures before anyone consumes the shift report.
PEDAGOGICAL RESTRICTIONS:
    - Reused only: unittest asserts are replaced here by plain
      assert statements with messages (same proving idea, no new
      syntax), Evento plus lax versus strict (S16), contar_por_nivel
      plus validar_config plus arrange-act-assert (S17 class).
    - No new domain classes, no argparse, no network, no shell.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> proven task ->
auditable shift report.
Homework chain: new shift data with the same tested technique, while
the class exercise proves the day batch.
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# STEP 1: Evidence (given). Shift threshold, ten synthetic night-shift
# dicts, plus operator identity. Records 1-7 are exact, record 8 uses
# a numeric string so lax mode proves its conversion, records 9-10
# are intentionally broken.
# ==============================================================================
SHIFT_THRESHOLD = 3
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

shift_events = [
    {"event_id": 21, "level": "INFO", "message": "ronda nocturna iniciada en localhost", "source": "sensor-a"},
    {"event_id": 22, "level": "WARNING", "message": "reintento nocturno local", "source": "sensor-b"},
    {"event_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"event_id": 24, "level": "INFO", "message": "bitacora nocturna verificada", "source": "sensor-b"},
    {"event_id": 25, "level": "ERROR", "message": "cola nocturna llena", "source": "sensor-a"},
    {"event_id": 26, "level": "WARNING", "message": "latencia nocturna alta", "source": "sensor-b"},
    {"event_id": 27, "level": "INFO", "message": "respaldo nocturno completado", "source": "sensor-a"},
    {"event_id": "28", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"},
    {"event_id": 29, "message": "linea nocturna sin nivel", "source": "sensor-a"},
    {"event_id": 30, "level": "DEBUG", "message": "nivel nocturno inventado", "source": "sensor-b"},
]

# Identity of whose review this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Proven tasks. Same boundary model and same pure functions as
# class, applied to the night-shift data.
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


def validate_shift_records(raw_records):
    """Split raw shift dicts into accepted events plus labeled rejections."""
    accepted = []
    rejected = []
    for position, raw_item in enumerate(raw_records, start=1):
        try:
            accepted.append(Evento.model_validate(raw_item))
        except ValidationError:
            rejected.append(f"registro {position}: rechazado en la frontera")
    return accepted, rejected


def main():
    """Run the proven night-shift batch from the project root."""
    # Check 1-2 (arrange-act-assert): shift split keeps every row proven.
    accepted, rejected = validate_shift_records(shift_events)
    assert len(accepted) == 8, "El turno debia aceptar 8 registros"
    assert len(rejected) == 2, "El turno debia rechazar 2 registros"

    # Check 3 (edge): lax converts the numeric string of record 8.
    lax_event = Evento.model_validate(shift_events[7])
    assert lax_event.event_id == 28, "El modo lax debia convertir el texto 28 al entero 28"

    # Check 4 (error): strict rejects the same numeric string.
    try:
        Evento.model_validate(shift_events[7], strict=True)
        strict_rejected = False
    except ValidationError:
        strict_rejected = True
    assert strict_rejected, "strict=True debia rechazar el texto 28 sin convertirlo"

    # Check 5 (edge): unknown levels never inflate the accepted counts.
    counts = contar_por_nivel([event.model_dump() for event in accepted])
    assert counts == {"INFO": 4, "WARNING": 2, "ERROR": 2}, "Se esperaban 4 INFO, 2 WARNING y 2 ERROR aceptados"

    # Check 6 (normal): shift config stays inside the local contract.
    assert validar_config(18080, "INFO"), "La config (18080, INFO) debia aceptarse"

    error_total = counts["ERROR"]
    if error_total >= SHIFT_THRESHOLD:
        error_verdict = "Revisión prioritaria"
    else:
        error_verdict = "Rutina local"

    print(f"Turno leido: {len(shift_events)}")
    print(f"Turno aceptado: {len(accepted)}")
    print(f"Turno rechazado: {len(rejected)}")
    print(f"Errores (aceptados): {error_total} - {error_verdict}")
    print("Chequeos del turno: 6/6 en verde (asserts con mensaje)")

    # ==========================================================================
    # STEP 3: Communication (given). Proven shift report the teacher
    # consumes next session.
    # ==========================================================================
    print("--- Revision probada (turno) ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print("Corredores: unittest (base) + pytest (legible, opcional)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
