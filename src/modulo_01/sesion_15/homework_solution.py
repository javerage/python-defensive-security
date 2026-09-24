"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 15 (PyDefSec)
FILE: homework_solution.py (reference for normalize_shift.py)
PURPOSE: Normalize the night-shift log with the same anchored technique
         as class: the same anchored routes plus atomic publish pair turn
         20 raw shift lines into clean lines with exact processed plus
         skipped counts.
NOTE: Homework after class, outside the 60 minutes. Create
      normalize_shift.py plus datos/turno.log manually in your Session
      01 project, reusing the anchored technique from class. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Same new syntax as class only: pathlib Path, anchored routes,
      explicit UTF-8, atomic write through temporary plus rename.
    - Reused only: def plus return (S11), try/except (S13), logging
      (S13), list plus dict plus for (S06-S10).
    - No Pydantic modeling until Session 16, no new domain classes, no
      argparse, no network, no shell.
    - English PEP 8 identifiers plus comments (style guidance).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: shift threshold (read-only) -> anchored task ->
atomic shift report.
Homework chain: new shift data with the same anchor technique, while
the class exercise normalizes the day log. Counts prove nothing by
themselves; they order human review of local practice data. This
report opens no ports, touches no network, and contacts nothing
beyond its own console plus local files.
"""

import logging
from pathlib import Path

# Quiet console logger for skipped lines (Session 13 reuse, console only).
logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
logger = logging.getLogger("normalize_shift")

# ==============================================================================
# ANCHORED ROUTES (always resolved from this file, never from the console
# working directory). Run normalize_shift.py from the project root.
# ==============================================================================
PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_PATH = PROJECT_ROOT / "datos" / "turno.log"
OUTPUT_DIR = PROJECT_ROOT / "salida"
OUTPUT_PATH = OUTPUT_DIR / "turno_normalizado.txt"
TEMP_PATH = OUTPUT_DIR / "turno_normalizado.tmp"

# ==============================================================================
# STEP 1: Evidence (given). Shift threshold, twenty synthetic night-shift
# log lines, plus operator identity.
# ==============================================================================
SHIFT_THRESHOLD = 5
ALLOWED_LEVELS = ("INFO", "WARNING", "ERROR")

shift_lines = [
    "WARNING: turno nocturno iniciado",
    "INFO: ronda local sin novedad",
    "ERROR: sensor local sin respuesta",
    "WARNING: reintento de lectura local",
    "INFO: bitacora local verificada",
    "WARNING: cola de eventos llena",
    "INFO: respaldo local confirmado",
    "ERROR: archivo temporal corrupto",
    "WARNING: umbral cercano al limite",
    "INFO: inventario local actualizado",
    "WARNING: latencia alta en loopback",
    "ERROR: registro incompleto detectado",
    "INFO: limpieza de salida completada",
    "WARNING: reintento de conexion local",
    "INFO: auditoria local sin hallazgos",
    "WARNING: segundo reintento local",
    "INFO: cierre parcial registrado",
    "linea rota sin nivel",
    "",
    "ERROR: disco lleno en localhost",
]

# Identity of whose report this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"


# ==============================================================================
# STEP 2: Anchored tasks. Same anchor technique as class, applied to the
# night-shift data with its own threshold.
# ==============================================================================


def ensure_fixture(input_path, lines):
    """Create the shift fixture only when it is still missing."""
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
    """Return raw shift lines, or an empty list when missing."""
    try:
        content = input_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {input_path} (revise la ruta anclada)")
        return []
    return content.splitlines()


def write_atomic(output_path, temp_path, clean_lines):
    """Publish clean shift lines through a temporary file plus rename."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path.write_text("\n".join(clean_lines) + "\n", encoding="utf-8")
    temp_path.replace(output_path)


def main():
    """Run the anchored shift normalization from the project root."""
    ensure_fixture(INPUT_PATH, shift_lines)

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

    # First shift finding uses ERROR: 4 stays below the threshold.
    if error_total >= SHIFT_THRESHOLD:
        error_verdict = "Revisión prioritaria"
    else:
        error_verdict = "Rutina local"

    # Second shift finding uses WARNING: 7 reaches the threshold.
    if warn_total >= SHIFT_THRESHOLD:
        warn_verdict = "Revisión prioritaria"
    else:
        warn_verdict = "Rutina local"

    print(f"Lineas leidas: {len(raw_lines)}")
    print(f"Lineas normalizadas: {len(clean_lines)}")
    print(f"Lineas omitidas: {skipped_total}")
    print(f"Errores: {error_total} - {error_verdict}")
    print(f"Avisos: {warn_total} - {warn_verdict}")
    print("Salida: salida/turno_normalizado.txt (escritura atomica)")

    # ==========================================================================
    # STEP 3: Communication. Anchored shift report with both pairs plus
    # the file proof that the next reader consumes.
    # ==========================================================================
    print("--- Revision normalizada del turno ---")
    print(f"Nombre: {student_name}")
    print(f"Identificador: {student_id}")
    print(f"Umbral: {SHIFT_THRESHOLD} (solo lectura)")
    print("Alcance: localhost (127.0.0.1) y fixtures locales")


if __name__ == "__main__":
    main()
