"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 15 (PyDefSec)
FILE: solution.py (reference for normalize_logs.py)
PURPOSE: Read a synthetic local log with pathlib, normalize each line to a
         single LEVEL plus message form with UTF-8, handle missing files
         with try/except, and publish the result with an atomic write
         (temporary file plus rename), so the shift handoff reads one
         clean file with exact processed plus skipped counts.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo): they create
      datos/app.log manually (or let the script bootstrap it), keep the
      kit/ reader from Session 14 untouched, and run normalize_logs.py
      from the project root.
WHY NORMALIZE: Session 14 packed counts well but every reader parsed raw
      text on the fly. Today one anchored reader turns 20 raw lines into
      18 clean lines plus 2 skipped, and the atomic rename guarantees no
      half-written file ever reaches the next reader.
PEDAGOGICAL RESTRICTIONS:
    - New today only: pathlib Path, anchored relative routes, explicit
      UTF-8, atomic write through temporary plus rename.
    - Reused only: def plus return (S11), try/except (S13), logging (S13),
      list plus dict plus for (S06-S10).
    - No Pydantic modeling until Session 16, no new domain classes, no
      argparse, no network, no shell.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: evidence -> anchored task -> atomic report.
One anchored reader holds the fixture logic; try/except keeps missing
files from crashing the console; the temporary plus rename pair proves
no half-written file ever ships while the console keeps every count.
"""

import logging
from pathlib import Path

# Quiet console logger for skipped lines (Session 13 reuse, console only).
logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
logger = logging.getLogger("normalize_logs")

# ==============================================================================
# ANCHORED ROUTES (always resolved from this file, never from the console
# working directory). Run normalize_logs.py from the project root.
# ==============================================================================
PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_PATH = PROJECT_ROOT / "datos" / "app.log"
OUTPUT_DIR = PROJECT_ROOT / "salida"
OUTPUT_PATH = OUTPUT_DIR / "normalizado.txt"
TEMP_PATH = OUTPUT_DIR / "normalizado.tmp"

# ==============================================================================
# STEP 1: Evidence (given). Shared threshold, twenty synthetic local log
# lines, plus operator identity. The bootstrap writes the fixture only
# when datos/app.log is still missing, so copies stay reproducible.
# ==============================================================================
REVIEW_THRESHOLD = 5
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

fixture_lines = [
    "INFO: servicio iniciado en localhost",
    "ERROR: disco lleno en localhost",
    "WARNING: reintento de conexion local",
    "INFO: revision de turno completada",
    "ERROR: puerto local sin respuesta",
    "WARNING: latencia alta en loopback",
    "ERROR: archivo temporal corrupto",
    "INFO: copia de respaldo verificada",
    "WARNING: umbral cercano al limite",
    "ERROR: registro incompleto detectado",
    "INFO: sesion local iniciada",
    "WARNING: cola de eventos llena",
    "INFO: limpieza de salida completada",
    "INFO: verificacion final aprobada",
    "INFO: auditoria local sin hallazgos",
    "WARNING: reintento de lectura local",
    "INFO: inventario local actualizado",
    "linea rota sin nivel",
    "",
    "INFO: cierre de turno registrado",
]

# Identity of whose review this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Anchored tasks. Bootstrap plus normalize plus atomic publish.
# ==============================================================================


def ensure_fixture(input_path, lines):
    """Create the fixture file only when it is still missing."""
    if input_path.exists():
        return False
    input_path.parent.mkdir(parents=True, exist_ok=True)
    input_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def normalize_line(raw_line):
    """Return the clean level plus message pair, or None when skipped."""
    text = raw_line.strip()
    if not text:
        return None
    if ":" not in text:
        return None
    level, _, message = text.partition(":")
    level = level.strip().upper()
    message = message.strip()
    if level not in ALLOWED_LEVELS or not message:
        return None
    return level, f"{level}: {message}"


def read_input_lines(input_path):
    """Return raw lines, or an empty list when the fixture is missing."""
    try:
        content = input_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {input_path} (revise la ruta anclada)")
        return []
    return content.splitlines()


def write_atomic(output_path, temp_path, clean_lines):
    """Publish clean lines through a temporary file plus rename."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path.write_text("\n".join(clean_lines) + "\n", encoding="utf-8")
    temp_path.replace(output_path)


def main():
    """Run the anchored normalization from the project root."""
    ensure_fixture(INPUT_PATH, fixture_lines)

    raw_lines = read_input_lines(INPUT_PATH)
    clean_lines = []
    error_total = 0
    warn_total = 0
    skipped_total = 0
    for raw_line in raw_lines:
        parsed = normalize_line(raw_line)
        if parsed is None:
            skipped_total += 1
            logger.warning("Linea omitida: %r", raw_line.strip())
            continue
        level, clean_line = parsed
        clean_lines.append(clean_line)
        if level == "ERROR":
            error_total += 1
        elif level == "WARNING":
            warn_total += 1

    # Atomic publish: readers only ever see the finished file.
    if raw_lines:
        write_atomic(OUTPUT_PATH, TEMP_PATH, clean_lines)

    # First anchored finding uses ERROR: 4 stays below the threshold.
    if error_total >= REVIEW_THRESHOLD:
        error_verdict = "Revisión prioritaria"
    else:
        error_verdict = "Rutina local"

    # Second anchored finding uses WARNING: 5 reaches the threshold.
    if warn_total >= REVIEW_THRESHOLD:
        warn_verdict = "Revisión prioritaria"
    else:
        warn_verdict = "Rutina local"

    print(f"Lineas leidas: {len(raw_lines)}")
    print(f"Lineas normalizadas: {len(clean_lines)}")
    print(f"Lineas omitidas: {skipped_total}")
    print(f"Errores: {error_total} - {error_verdict}")
    print(f"Avisos: {warn_total} - {warn_verdict}")
    print("Salida: salida/normalizado.txt (escritura atomica)")

    # ==========================================================================
    # STEP 3: Communication (given). Anchored report with both pairs plus
    # the file proof that the next reader consumes.
    # Pairs prove nothing by themselves; they order human review of local
    # practice data. The program opens no ports, touches no network,
    # and contacts nothing beyond its own console plus local files.
    # ==========================================================================
    print("--- Revision normalizada ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {REVIEW_THRESHOLD} (solo lectura)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
