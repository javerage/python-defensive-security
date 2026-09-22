"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 07 (PyDefSec)
FILE: starter.py (guided skeleton for level_summary.py)
PURPOSE: Count 20 synthetic local observations by level and by origin
         module with dicts: build each count with list.count(), store
         one value per key, read safely with .get(), stage plus retire
         one test key, and print an ordered summary without any loop.
NOTE: The repository is only a backup. Create level_summary.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected summary.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as level_summary.py and run:
        python level_summary.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the counting tables in your student material first: they hold
    the 20 levels, the 20 modules, and the expected totals. No part of
    this skeleton shows the final counts, keys, or lookups.

WHY NO LOOP HERE: loops arrive in Session 09. Until then each count is
    one explicit .count() line so every step stays visible.
==============================================================================

Conceptual sequence: flat list (order plus duplicates) -> count per
value -> dict (one value per key) -> safe lookup -> ordered summary.
A list keeps all 20 entries; a dict keeps one total per key.
"""

# ==============================================================================
# STEP 1: Evidence (given). Twenty synthetic local observations plus
# operator identity. Same positions in both lists.
# ==============================================================================
event_levels = [
    "INFO", "ERROR", "WARNING", "INFO", "INFO",
    "WARNING", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "INFO", "WARNING",
    "ERROR", "INFO", "WARNING", "ERROR", "INFO",
]
event_modules = [
    "auth", "disk", "auth", "backup", "net",
    "auth", "backup", "disk", "auth", "net",
    "backup", "auth", "disk", "backup", "net",
    "auth", "backup", "disk", "auth", "backup",
]

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Observaciones registradas: {len(event_levels)}")

# ==============================================================================
# STEP 2: Counts plus dicts (TODO). One explicit .count() line per value.
# ==============================================================================
# TODO 2.1: Count each level with .count() (expect INFO 9, WARNING 6,
# ERROR 5; the three add up to 20).
info_count = 0  # TODO: build it with event_levels.count("INFO")
warning_count = 0  # TODO: build it with event_levels.count("WARNING")
error_count = 0  # TODO: build it with event_levels.count("ERROR")

# TODO 2.2: Store one value per key in level_counts (given keys with 0
# so the skeleton runs; replace each 0 with its count variable).
level_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}  # TODO: use info_count, warning_count, error_count

# TODO 2.3: print how many distinct keys the dict holds (expect 3).
print("PENDING")  # TODO: print f"Niveles distintos: {len(level_counts)}"

# TODO 2.4: Count each module with .count() (expect auth 7, backup 6,
# disk 4, net 3; the four add up to 20).
auth_count = 0  # TODO: build it with event_modules.count("auth")
backup_count = 0  # TODO: build it with event_modules.count("backup")
disk_count = 0  # TODO: build it with event_modules.count("disk")
net_count = 0  # TODO: build it with event_modules.count("net")

# TODO 2.5: Store one value per key in module_counts (given keys with 0
# so the skeleton runs; replace each 0 with its count variable).
module_counts = {"auth": 0, "backup": 0, "disk": 0, "net": 0}  # TODO: use auth_count, backup_count, disk_count, net_count

# TODO 2.6: print how many distinct keys the dict holds (expect 4).
print("PENDING")  # TODO: print f"Módulos distintos: {len(module_counts)}"

# TODO 2.7: Stage a test key DEBUG with 0, then retire it with
# .pop("DEBUG", 0) and keep the retired value in removed_debug.
removed_debug = 0  # TODO: add the two lines above this print first
print("PENDING")  # TODO: print f"Clave de prueba retirada: {removed_debug}"

# TODO 2.8: Read the retired key safely with .get("DEBUG", 0).
# Direct level_counts["DEBUG"] would raise KeyError; .get() returns 0.
debug_lookup = 0  # TODO: build it with level_counts.get("DEBUG", 0)

# TODO 2.9: print the safe lookup (expect 0).
print("PENDING")  # TODO: print f"Búsqueda segura de DEBUG: {debug_lookup}"

# Ordered keys reuse Session 06 (given): sorted() returns an ordered
# list of keys, and each position is read back with [0], [1], [2].
ordered_levels = sorted(level_counts)
ordered_modules = sorted(module_counts)

# ==============================================================================
# STEP 3: Communication (given). Ordered summary for the reviewer.
# ==============================================================================
print("--- Resumen de niveles y módulos ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total de observaciones: {len(event_levels)}")
print(f"{ordered_levels[0]}: {level_counts[ordered_levels[0]]}")
print(f"{ordered_levels[1]}: {level_counts[ordered_levels[1]]}")
print(f"{ordered_levels[2]}: {level_counts[ordered_levels[2]]}")
print(f"{ordered_modules[0]}: {module_counts[ordered_modules[0]]}")
print(f"{ordered_modules[1]}: {module_counts[ordered_modules[1]]}")
print(f"{ordered_modules[2]}: {module_counts[ordered_modules[2]]}")
print(f"{ordered_modules[3]}: {module_counts[ordered_modules[3]]}")
print(f"Lista completa: {len(event_levels)} entradas, diccionario: {len(level_counts)} claves")
