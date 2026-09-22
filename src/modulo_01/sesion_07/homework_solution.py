"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 07 (PyDefSec)
FILE: homework_solution.py (reference for shift_summary.py)
PURPOSE: Summarize one synthetic local night-shift log with dicts:
         count 20 observations by level and by module with explicit
         .count() lines, read safely with .get(), retire one test key
         with .pop(), model the analyst card as a dict, and print an
         ordered summary without any loop.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_summary.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no loops, no imports, no tuples, no sets).
    - Only Session 06 lists plus dicts: key/value storage, .get() with
      default, item assignment, and .pop() with default.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: flat list -> count per value -> dict -> safe
lookup -> ordered summary.
Homework chain: new shift data -> same counting technique -> analyst
card -> communication, while the class exercise summarizes the day
list. Counts prove nothing by themselves; they order human review of
local practice data. This summary blocks nothing, isolates nothing,
and contacts nothing.
"""

# ==============================================================================
# STEP 1: Evidence (given). Twenty synthetic night-shift observations
# plus operator identity. Same positions in both lists.
# ==============================================================================
shift_levels = [
    "INFO", "WARNING", "ERROR", "INFO", "WARNING",
    "INFO", "ERROR", "WARNING", "INFO", "WARNING",
    "ERROR", "INFO", "WARNING", "INFO", "ERROR",
    "WARNING", "INFO", "ERROR", "WARNING", "INFO",
]
shift_modules = [
    "auth", "backup", "disk", "auth", "backup",
    "backup", "disk", "auth", "backup", "disk",
    "auth", "backup", "backup", "disk", "auth",
    "backup", "disk", "auth", "backup", "disk",
]

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Observaciones del turno: {len(shift_levels)}")

# ==============================================================================
# STEP 2: Counts plus dicts. One explicit .count() line per value.
# ==============================================================================
info_count = shift_levels.count("INFO")
warning_count = shift_levels.count("WARNING")
error_count = shift_levels.count("ERROR")

level_counts = {"INFO": info_count, "WARNING": warning_count, "ERROR": error_count}
print(f"Niveles distintos: {len(level_counts)}")

auth_count = shift_modules.count("auth")
backup_count = shift_modules.count("backup")
disk_count = shift_modules.count("disk")

module_counts = {"auth": auth_count, "backup": backup_count, "disk": disk_count}
print(f"Módulos distintos: {len(module_counts)}")

# Retire the test key the day list staged: pop() with a default retires
# it without raising when it is already missing.
removed_debug = level_counts.pop("DEBUG", 0)
print(f"Clave de prueba retirada: {removed_debug}")

# Safe lookups with defaults: 0 for the retired key, and the local lab
# for the card field this shift never recorded.
debug_lookup = level_counts.get("DEBUG", 0)
print(f"Búsqueda segura de DEBUG: {debug_lookup}")

# Analyst card (given structure): one dict models whose shift this is.
# .get() with a default covers the field the shift never recorded.
analyst_card = {"name": student_name, "shift": "noche", "total_events": 20}
card_name = analyst_card.get("name", "desconocido")
card_zone = analyst_card.get("zone", "laboratorio local")
print(f"Tarjeta del analista: {card_name} ({card_zone})")

ordered_levels = sorted(level_counts)
ordered_modules = sorted(module_counts)

# ==============================================================================
# STEP 3: Communication. Ordered summary for the reviewer.
# ==============================================================================
print("--- Resumen del turno ---")
print(f"Nombre: {card_name}")
print(f"Identificador: {student_id}")
print(f"Total de observaciones: {len(shift_levels)}")
print(f"{ordered_levels[0]}: {level_counts[ordered_levels[0]]}")
print(f"{ordered_levels[1]}: {level_counts[ordered_levels[1]]}")
print(f"{ordered_levels[2]}: {level_counts[ordered_levels[2]]}")
print(f"{ordered_modules[0]}: {module_counts[ordered_modules[0]]}")
print(f"{ordered_modules[1]}: {module_counts[ordered_modules[1]]}")
print(f"{ordered_modules[2]}: {module_counts[ordered_modules[2]]}")
print(f"Lista completa: {len(shift_levels)} entradas, diccionario: {len(level_counts)} claves")
