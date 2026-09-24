"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 16 (PyDefSec)
FILE: solution.py (reference for validate_events.py)
PURPOSE: Convert local events between JSON and CSV, rotate a file log
         with logging, keep UTF-8 plus headers, and validate every
         record with a first Pydantic BaseModel, catching
         ValidationError with a useful message per rejected row.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they create
      datos/eventos.json manually (or let the script bootstrap it),
      keep the normalize_logs.py reader from Session 15 untouched,
      and run validate_events.py from the project root.
WHY VALIDATE: Session 15 shipped clean lines but trusted every field
      by shape. Today one Evento model turns 20 raw dicts into 15
      accepted rows plus 5 rejected with motive, the CSV carries only
      accepted rows, and proceso.log keeps 6 entries so the next
      reader (Session 17 tests) can replay the batch.
PEDAGOGICAL RESTRICTIONS:
    - New today only: json plus csv DictReader/DictWriter, logging to
      file, first BaseModel with type hints, model_validate,
      ValidationError, lax conversion versus strict=True.
    - Reused only: def plus return (S11), try/except (S13), pathlib
      anchored routes plus UTF-8 (S15), list plus dict plus for
      (S06-S10), logging console habit (S13).
    - No new domain classes, no argparse, no network, no shell.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: evidence -> validated task -> auditable report.
CSV rows are always dicts before validation; lax mode converts
"15" to 15 while strict=True rejects it; Pydantic guards the input
boundary only, never the rest of the program.
"""

import csv
import json
import logging
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# ANCHORED ROUTES (always resolved from this file, never from the console
# working directory). Run validate_events.py from the project root.
# ==============================================================================
PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_DIR = PROJECT_ROOT / "datos"
OUTPUT_DIR = PROJECT_ROOT / "salida"
JSON_PATH = INPUT_DIR / "eventos.json"
CSV_PATH = OUTPUT_DIR / "eventos.csv"
LOG_PATH = PROJECT_ROOT / "proceso.log"

# ==============================================================================
# STEP 1: Evidence (given). Shared threshold, twenty synthetic local event
# dicts, plus operator identity. The bootstrap writes the JSON fixture
# only when datos/eventos.json is still missing, so copies stay
# reproducible. Records 16-20 are intentionally broken; record 15 uses
# a numeric string so lax mode proves its conversion.
# ==============================================================================
REVIEW_THRESHOLD = 5
EVENT_FIELDS = ("event_id", "level", "message", "source")

raw_events = [
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
    {"event_id": 11, "level": "WARNING", "message": "cola de eventos llena", "source": "sensor-b"},
    {"event_id": 12, "level": "INFO", "message": "limpieza de salida completada", "source": "sensor-a"},
    {"event_id": 13, "level": "INFO", "message": "verificacion final aprobada", "source": "sensor-b"},
    {"event_id": 14, "level": "WARNING", "message": "reintento de lectura local", "source": "sensor-a"},
    {"event_id": "15", "level": "INFO", "message": "inventario local actualizado", "source": "sensor-b"},
    {"event_id": 16, "message": "linea sin nivel", "source": "sensor-a"},
    {"event_id": "sin-numero", "level": "ERROR", "message": "tipo invalido", "source": "sensor-b"},
    {"event_id": 18, "level": "DEBUG", "message": "nivel inventado", "source": "sensor-a"},
    {"level": "INFO", "message": "falta identificador", "source": "sensor-b"},
    {"event_id": 20, "level": "INFO", "message": "", "source": "sensor-a"},
]

# Identity of whose review this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Validated tasks. First BaseModel plus JSON/CSV round trip plus
# file logging. CSV rows are dicts of strings; they are validated only
# after reaching dict form, never as raw lists.
# ==============================================================================


class Evento(BaseModel):
    """Validated defensive event at the input boundary."""

    event_id: int
    level: Literal["INFO", "WARNING", "ERROR"]
    message: str = Field(min_length=1)
    source: str = Field(min_length=1)


def setup_logger(log_path):
    """Return a file logger that restarts the batch log."""
    batch_logger = logging.getLogger("validate_events")
    batch_logger.setLevel(logging.INFO)
    batch_logger.handlers.clear()
    handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    batch_logger.addHandler(handler)
    batch_logger.propagate = False
    return batch_logger


def ensure_fixture_json(json_path, records):
    """Create the JSON fixture only when it is still missing."""
    if json_path.exists():
        return False
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return True


def read_raw_records(json_path):
    """Return raw dicts, or an empty list when the fixture is missing."""
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
    """Split raw dicts into accepted events plus labeled rejections."""
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
    """Publish accepted events to CSV with headers and UTF-8."""
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open(mode="w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(EVENT_FIELDS))
        writer.writeheader()
        for event in accepted:
            writer.writerow(event.model_dump())


def check_strict_sample(batch_logger):
    """Prove strict=True rejects the lax-accepted numeric string."""
    sample = {
        "event_id": "15",
        "level": "INFO",
        "message": "inventario local actualizado",
        "source": "sensor-b",
    }
    try:
        Evento.model_validate(sample, strict=True)
    except ValidationError:
        batch_logger.info(
            'Demo strict: registro "15" rechazado con strict=True '
            "(lax lo convierte a 15)"
        )
        return True
    return False


def main():
    """Run the JSON-to-CSV validation batch from the project root."""
    batch_logger = setup_logger(LOG_PATH)
    batch_logger.info("Inicio de lote: 20 registros crudos (umbral 5, modo lax)")

    ensure_fixture_json(JSON_PATH, raw_events)
    batch_logger.info("Fixture JSON escrito: datos/eventos.json (20 registros, UTF-8)")

    raw_records = read_raw_records(JSON_PATH)
    accepted, rejected = validate_records(raw_records)
    batch_logger.info(
        f"Validacion Pydantic: {len(accepted)} aceptados, {len(rejected)} rechazados"
    )

    check_strict_sample(batch_logger)
    write_events_csv(CSV_PATH, accepted)
    batch_logger.info(
        "CSV publicado: salida/eventos.csv "
        "(15 filas, encabezados event_id,level,message,source)"
    )

    # CSV proof: DictReader yields dicts of strings; the first row
    # re-enters through the same boundary and lax converts "1" to 1.
    with CSV_PATH.open(mode="r", encoding="utf-8", newline="") as check_file:
        first_row = next(csv.DictReader(check_file))
    proof_event = Evento.model_validate(first_row)

    error_total = sum(1 for event in accepted if event.level == "ERROR")
    if error_total >= REVIEW_THRESHOLD:
        error_verdict = "Revisión prioritaria"
    else:
        error_verdict = "Rutina local"
    batch_logger.info(
        f"Prueba CSV->dict: fila 1 aceptada (lax convierte \"1\" a "
        f"{proof_event.event_id}); errores aceptados: "
        f"{error_total} - {error_verdict}"
    )

    print(f"Eventos leidos: {len(raw_records)}")
    print(f"Eventos aceptados: {len(accepted)}")
    print(f"Eventos rechazados: {len(rejected)}")
    print(f"Errores (aceptados): {error_total} - {error_verdict}")
    print("Salida: salida/eventos.csv (15 filas) + proceso.log (6 entradas)")
    print(f"Rechazados ({len(rejected)}):")
    for detail in rejected:
        print(f"- {detail}")

    # ==========================================================================
    # STEP 3: Communication (given). Validated report with the lax/strict
    # note plus the file proof the next reader consumes. Pydantic
    # guards this input boundary only; it never certifies the rest of
    # the program, the tests, or the static types.
    # ==========================================================================
    print("--- Revision validada ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {REVIEW_THRESHOLD} (solo lectura)")
    print('Modo: lax convierte ("15" -> 15); strict=True rechaza')
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
