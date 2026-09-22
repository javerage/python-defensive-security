"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 07 (PyDefSec)
FILE: solution.py (reference for level_summary.py)
PURPOSE: Count 20 synthetic local observations by level and by origin
         module with dicts: build each count with list.count(), store
         one value per key, read safely with .get(), stage plus retire
         one test key, and print an ordered summary without any loop.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      level_summary.py manually.
WHY NO LOOP HERE: loops arrive in Session 09. Until then the 20
      values stay written out and each count is one explicit .count()
      line. Same results a loop would produce, spelled out so every
      step stays visible.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no loops, no imports, no tuples, no sets).
    - Only Session 06 lists (creation, len, count, sorted, indexing)
      plus new dicts: key/value storage, .get() with default, item
      assignment, and .pop() with default.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: flat list (order plus duplicates) -> count per
value -> dict (one value per key) -> safe lookup -> ordered summary.
A list keeps all 20 entries; a dict keeps one total per key.
"""

# ==============================================================================
# STEP 1: Evidence (given). Twenty synthetic local observations plus
# operator identity. Same positions in both lists: position 0 of one
# list describes the same observation as position 0 of the other.
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
# STEP 2: Counts plus dicts. One explicit .count() line per value;
# loops arrive in Session 09 and would compress these lines later.
# ==============================================================================
info_count = event_levels.count("INFO")
warning_count = event_levels.count("WARNING")
error_count = event_levels.count("ERROR")

# One value per key: the dict answers "how many?" without scanning.
level_counts = {"INFO": info_count, "WARNING": warning_count, "ERROR": error_count}
print(f"Niveles distintos: {len(level_counts)}")

auth_count = event_modules.count("auth")
backup_count = event_modules.count("backup")
disk_count = event_modules.count("disk")
net_count = event_modules.count("net")

module_counts = {
    "auth": auth_count,
    "backup": backup_count,
    "disk": disk_count,
    "net": net_count,
}
print(f"Módulos distintos: {len(module_counts)}")

# Aggregation and removal: stage a test key, then retire it. pop() with
# a default retires the key without raising when it is missing.
level_counts["DEBUG"] = 0
removed_debug = level_counts.pop("DEBUG", 0)
print(f"Clave de prueba retirada: {removed_debug}")

# Safe lookup: .get() with a default returns 0 for the retired key
# instead of raising KeyError like level_counts["DEBUG"] would.
debug_lookup = level_counts.get("DEBUG", 0)
print(f"Búsqueda segura de DEBUG: {debug_lookup}")

# Ordered keys reuse Session 06: sorted() returns an ordered list of
# keys, and each position is read back with [0], [1], [2].
ordered_levels = sorted(level_counts)
ordered_modules = sorted(module_counts)

# ==============================================================================
# STEP 3: Communication (given). Ordered summary for the reviewer.
# Counts prove nothing by themselves; they order human review of local
# practice data. The program blocks nothing, isolates nothing,
# and contacts nothing.
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
