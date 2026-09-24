"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 16 (PyDefSec)
FILE: homework_solution.py (reference for validate_shift.py)
PURPOSE: Validate the night-shift events with the same boundary
         technique as class: the same Evento model plus strict demo
         turn 10 raw shift dicts into accepted rows plus labeled
         rejections, published to a shift CSV with a shift log.
NOTE: Homework after class, outside the 60 minutes. Create
      validate_shift.py plus datos/turno_eventos.json manually in your
      Session 01 project, reusing the validated technique from class.
      Use this file only as backup guidance after attempting the task
      on your own.
PEDAGOGICAL RESTRICTIONS:
    - Same new syntax as class only: json plus csv DictReader /
      DictWriter, logging to file, Evento BaseModel with type hints,
      model_validate, ValidationError, lax versus strict=True.
    - Reused only: def plus return (S11), try/except (S13), pathlib
      anchored routes plus UTF-8 (S15), list plus dict plus for
      (S06-S10).
    - No new domain classes, no argparse, no network, no shell.
    - English PEP 8 identifiers plus comments (style guidance).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> validated task ->
auditable shift report.
Homework chain: new shift data with the same boundary technique,
while the class exercise validates the day batch. Counts prove
nothing by themselves; they order human review of local practice
data. This report opens no ports, touches no network, and contacts
nothing beyond its own console plus local files.
"""

import csv
import json
import logging
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# ANCHORED ROUTES (always resolved from this file, never from the console
# working directory). Run validate_shift.py from the project root.
# ==============================================================================
PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_DIR = PROJECT_ROOT / "datos"
OUTPUT_DIR = PROJECT_ROOT / "salida"
JSON_PATH = INPUT_DIR / "turno_eventos.json"
CSV_PATH = OUTPUT_DIR / "turno_eventos.csv"
LOG_PATH = PROJECT_ROOT / "turno_proceso.log"

# ==============================================================================
# STEP 1: Evidence (given). Shift threshold, ten synthetic night-shift
# event dicts, plus operator identity.
# ==============================================================================
SHIFT_THRESHOLD = 5
EVENT_FIELDS = ("event_id", "level", "message", "source")

shift_events = [
    {"event_id": 21, "level": "INFO", "message": "turno nocturno iniciado", "source": "sensor-a"},
    {"event_id": 22, "level": "WARNING", "message": "ronda local sin novedad", "source": "sensor-b"},
    {"event_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"event_id": 24, "level": "WARNING", "message": "cola de eventos llena", "source": "sensor-b"},
    {"event_id": "25", "level": "INFO", "message": "respaldo local confirmado", "source": "sensor-a"},
    {"event_id": 26, "level": "ERROR", "message": "archivo temporal corrupto", "source": "sensor-b"},
    {"event_id": 27, "level": "INFO", "message": "inventario local actualizado", "source": "sensor-a"},
    {"event_id": 28, "level": "WARNING", "message": "latencia alta en loopback", "source": "sensor-b"},
    {"event_id": 29, "message": "linea sin nivel", "source": "sensor-a"},
    {"event_id": "sin-numero", "level": "INFO", "message": "tipo invalido", "source": "sensor-b"},
]

# Identity of whose report this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Validated tasks. Same boundary technique as class, applied to
# the night-shift data with its own threshold.
# ==============================================================================


class Evento(BaseModel):
    """Validated defensive event at the input boundary."""

    event_id: int
    level: Literal["INFO", "WARNING", "ERROR"]
    message: str = Field(min_length=1)
    source: str = Field(min_length=1)


def setup_logger(log_path):
    """Return a file logger that restarts the shift log."""
    batch_logger = logging.getLogger("validate_shift")
    batch_logger.setLevel(logging.INFO)
    batch_logger.handlers.clear()
    handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    batch_logger.addHandler(handler)
    batch_logger.propagate = False
    return batch_logger


def ensure_fixture_json(json_path, records):
    """Create the shift fixture only when it is still missing."""
    if json_path.exists():
        return False
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return True


def read_raw_records(json_path):
    """Return raw shift dicts, or an empty list when missing."""
    try:
        content = json_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {json_path} (revise la ruta anclada)")
        return []
    data = json.loads(content)
    return [item for item in data if isinstance(item, dict)]


def describe_rejection(error):
    """Return a short Spanish motive for one Pydantic error."""
    field = str(error["loc"][0]) if error.get("loc") else "registro"
    kind = error.get("type", "")
    if kind == "missing":
        return field, "campo faltante"
    if "parsing" in kind or kind in ("string_type", "int_type", "model_type"):
        return field, "tipo invalido"
    return field, "valor no permitido"


def validate_records(raw_records):
    """Split raw shift dicts into accepted events plus rejections."""
    accepted = []
    rejected = []
    for position, raw_item in enumerate(raw_records, start=1):
        try:
            accepted.append(Evento.model_validate(raw_item))
        except ValidationError as exc:
            field, motive = describe_rejection(exc.errors()[0])
            rejected.append(f"registro {position}: {motive} ({field})")
    return accepted, rejected


def write_events_csv(csv_path, accepted):
    """Publish accepted shift events to CSV with headers and UTF-8."""
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open(mode="w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(EVENT_FIELDS))
        writer.writeheader()
        for event in accepted:
            writer.writerow(event.model_dump())


def main():
    """Run the validated shift batch from the project root."""
    batch_logger = setup_logger(LOG_PATH)
    batch_logger.info("Inicio de turno: 10 registros crudos (umbral 5, modo lax)")

    ensure_fixture_json(JSON_PATH, shift_events)
    batch_logger.info("Fixture JSON escrito: datos/turno_eventos.json (10 registros, UTF-8)")

    raw_records = read_raw_records(JSON_PATH)
    accepted, rejected = validate_records(raw_records)
    batch_logger.info(
        f"Validacion Pydantic: {len(accepted)} aceptados, {len(rejected)} rechazados"
    )

    sample = {
        "event_id": "25",
        "level": "INFO",
        "message": "respaldo local confirmado",
        "source": "sensor-a",
    }
    try:
        Evento.model_validate(sample, strict=True)
    except ValidationError:
        batch_logger.info(
            'Demo strict: registro "25" rechazado con strict=True '
            "(lax lo convierte a 25)"
        )

    write_events_csv(CSV_PATH, accepted)

    error_total = sum(1 for event in accepted if event.level == "ERROR")
    if error_total >= SHIFT_THRESHOLD:
        error_verdict = "Revisión prioritaria"
    else:
        error_verdict = "Rutina local"
    batch_logger.info(
        f"CSV publicado: salida/turno_eventos.csv ({len(accepted)} filas); "
        f"errores aceptados: {error_total} - {error_verdict}"
    )

    print(f"Eventos leidos: {len(raw_records)}")
    print(f"Eventos aceptados: {len(accepted)}")
    print(f"Eventos rechazados: {len(rejected)}")
    print(f"Errores (aceptados): {error_total} - {error_verdict}")
    print("Salida: salida/turno_eventos.csv (8 filas) + turno_proceso.log (5 entradas)")
    print(f"Rechazados ({len(rejected)}):")
    for detail in rejected:
        print(f"- {detail}")

    # ==========================================================================
    # STEP 3: Communication. Anchored shift report with the lax/strict
    # note plus the file proof that the next reader consumes.
    # ==========================================================================
    print("--- Revision validada del turno ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print('Modo: lax convierte ("25" -> 25); strict=True rechaza')
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
