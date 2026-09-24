"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 07 (PyDefSec)
FILE: solution.py (reference for level_summary.py)
PURPOSE: Inspect, query, modify, and communicate a precomputed dictionary
         summary of 20 synthetic local observations: read known keys
         directly, count keys with len(), stage plus retire one test key
         with pop(), read safely with .get(), and print an ordered
         summary without any loop.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      level_summary.py manually.
WHY NO LOOP HERE: loops arrive in Session 09. Until then every summary
      line is one explicit print so each step stays visible. Automatic
      generation of these summaries from raw observations also arrives
      with loops; today the summary is given and the work is reading it.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no loops, no imports, no tuples, no sets).
    - Only dicts over a given summary: direct access for known keys,
      len() over keys, item assignment, .pop() with default, .get()
      with default, and sorted() over keys.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: given summary (label -> total) -> direct read ->
key count -> safe lookup -> ordered summary.
A prior local process summarized 20 synthetic observations; this script
consumes that summary and communicates it. It does not regenerate the
totals from raw observations: that automation arrives with loops in
Session 09.
"""

# ==============================================================================
# STEP 1: Summary (given). A prior local process summarized 20 synthetic
# local observations into one total per label. Session 07 consumes that
# summary: each key answers "how many?" without scanning anything.
# ==============================================================================
level_counts = {"INFO": 9, "WARNING": 6, "ERROR": 5}
module_counts = {"auth": 7, "backup": 6, "disk": 4, "net": 3}

# Total number of observations the summary represents (given).
total_events = 20

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Observaciones registradas: {total_events}")

# ==============================================================================
# STEP 2: Reads plus handling. Direct access for known keys, key counts
# with len(), one staged plus retired test key, and one safe lookup.
# ==============================================================================
info_count = level_counts["INFO"]
warning_count = level_counts["WARNING"]
error_count = level_counts["ERROR"]

# How many distinct labels the dict holds (keys, not observations).
print(f"Niveles distintos: {len(level_counts)}")

auth_count = module_counts["auth"]
backup_count = module_counts["backup"]
disk_count = module_counts["disk"]
net_count = module_counts["net"]

print(f"Módulos distintos: {len(module_counts)}")

# Staging and removal: add a provisional key, then retire it. pop() with
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
# Totals order human review of local practice data. The program blocks
# nothing, isolates nothing, and contacts nothing.
# ==============================================================================
print("--- Resumen de niveles y módulos ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total de observaciones: {total_events}")
print(f"{ordered_levels[0]}: {level_counts[ordered_levels[0]]}")
print(f"{ordered_levels[1]}: {level_counts[ordered_levels[1]]}")
print(f"{ordered_levels[2]}: {level_counts[ordered_levels[2]]}")
print(f"{ordered_modules[0]}: {module_counts[ordered_modules[0]]}")
print(f"{ordered_modules[1]}: {module_counts[ordered_modules[1]]}")
print(f"{ordered_modules[2]}: {module_counts[ordered_modules[2]]}")
print(f"{ordered_modules[3]}: {module_counts[ordered_modules[3]]}")
print(f"Resumen: {len(level_counts)} claves de nivel, {len(module_counts)} claves de módulo")
