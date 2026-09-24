"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 07 (PyDefSec)
FILE: starter.py (guided skeleton for level_summary.py)
PURPOSE: Inspect, query, modify, and communicate a precomputed dictionary
         summary of 20 synthetic local observations: read known keys
         directly, count keys with len(), stage plus retire one test key
         with pop(), read safely with .get(), and print an ordered
         summary without any loop.
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

    Read the summary tables in your student material first: they hold
    the given totals per level and per module. No part of this
    skeleton shows the final reads, key counts, or lookups.

WHY NO LOOP HERE: loops arrive in Session 09. Until then every summary
    line is one explicit print so each step stays visible. Automatic
    generation of these summaries from raw observations also arrives
    with loops; today the summary is given and the work is reading it.
==============================================================================

Conceptual sequence: given summary (label -> total) -> direct read ->
key count -> safe lookup -> ordered summary.
A prior local process summarized 20 synthetic observations; this script
consumes that summary and communicates it.
"""

# ==============================================================================
# STEP 1: Summary (given). A prior local process summarized 20 synthetic
# local observations into one total per label, plus operator identity.
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
# STEP 2: Reads plus handling (TODO). Direct access for known keys, key
# counts with len(), one staged plus retired test key, one safe lookup.
# ==============================================================================
# TODO 2.1: Read each known level directly (expect INFO 9, WARNING 6,
# ERROR 5).
info_count = 0  # TODO: read it with level_counts["INFO"]
warning_count = 0  # TODO: read it with level_counts["WARNING"]
error_count = 0  # TODO: read it with level_counts["ERROR"]

# TODO 2.2: print how many distinct keys the dict holds (expect 3).
print("PENDING")  # TODO: print f"Niveles distintos: {len(level_counts)}"

# TODO 2.3: Read each known module directly (expect auth 7, backup 6,
# disk 4, net 3).
auth_count = 0  # TODO: read it with module_counts["auth"]
backup_count = 0  # TODO: read it with module_counts["backup"]
disk_count = 0  # TODO: read it with module_counts["disk"]
net_count = 0  # TODO: read it with module_counts["net"]

# TODO 2.4: print how many distinct keys the dict holds (expect 4).
print("PENDING")  # TODO: print f"Módulos distintos: {len(module_counts)}"

# TODO 2.5: Stage a test key DEBUG with 0, then retire it with
# .pop("DEBUG", 0) and keep the retired value in removed_debug.
removed_debug = 0  # TODO: add the two lines above this print first
print("PENDING")  # TODO: print f"Clave de prueba retirada: {removed_debug}"

# TODO 2.6: Read the retired key safely with .get("DEBUG", 0).
# Direct level_counts["DEBUG"] would raise KeyError; .get() returns 0.
debug_lookup = 0  # TODO: build it with level_counts.get("DEBUG", 0)

# TODO 2.7: print the safe lookup (expect 0).
print("PENDING")  # TODO: print f"Búsqueda segura de DEBUG: {debug_lookup}"

# Ordered keys reuse Session 06 (given): sorted() returns an ordered
# list of keys, and each position is read back with [0], [1], [2].
ordered_levels = sorted(level_counts)
ordered_modules = sorted(module_counts)

# ==============================================================================
# STEP 3: Communication (given frame, TODO lines). Ordered summary for
# the reviewer; PENDING marks each line you still have to write.
# ==============================================================================
print("--- Resumen de niveles y módulos ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total de observaciones: {total_events}")
print("PENDING")  # TODO: print f"{ordered_levels[0]}: {level_counts[ordered_levels[0]]}"
print("PENDING")  # TODO: print f"{ordered_levels[1]}: {level_counts[ordered_levels[1]]}"
print("PENDING")  # TODO: print f"{ordered_levels[2]}: {level_counts[ordered_levels[2]]}"
print("PENDING")  # TODO: print f"{ordered_modules[0]}: {module_counts[ordered_modules[0]]}"
print("PENDING")  # TODO: print f"{ordered_modules[1]}: {module_counts[ordered_modules[1]]}"
print("PENDING")  # TODO: print f"{ordered_modules[2]}: {module_counts[ordered_modules[2]]}"
print("PENDING")  # TODO: print f"{ordered_modules[3]}: {module_counts[ordered_modules[3]]}"
print("PENDING")  # TODO: print f"Resumen: {len(level_counts)} claves de nivel, {len(module_counts)} claves de módulo"
