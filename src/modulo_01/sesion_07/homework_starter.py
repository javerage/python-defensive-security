"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 07 (PyDefSec)
FILE: homework_starter.py (guided skeleton for shift_summary.py)
PURPOSE: Summarize one synthetic local night-shift log with dicts:
         count 20 observations by level and by module with explicit
         .count() lines, read safely with .get(), retire one test key
         with .pop(), model the analyst card as a dict, and print an
         ordered summary without any loop.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_summary.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      summary. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as shift_summary.py plus run:
        python shift_summary.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

BEFORE CODING, ANALYZE (read the shift tables first, without running):
    - Which three .count() lines feed level_counts, and what must the
      three add up to?
    - Which key does .pop("DEBUG", 0) retire, and why does the default
      keep the program running?
    - Which card field is missing, and which default does .get() return
      for it?

DELIVERY: explain aloud the chain flat list -> count per value -> dict
-> safe lookup -> ordered summary for levels and for modules, why the
list keeps 20 entries while the dict keeps one total per key, and how
each result reaches the summary. Local practice data only. The program
organizes data for human review; it blocks nothing, isolates nothing,
and contacts nothing.
==============================================================================

Conceptual sequence: flat list -> count per value -> dict -> safe
lookup -> ordered summary.
Homework chain: new shift data -> same counting technique -> analyst
card -> communication, while the class exercise summarizes the day list.
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
# STEP 2: Counts plus dicts (TODO). One explicit .count() line per value.
# ==============================================================================
# TODO 2.1: Count each level with .count() (expect INFO 8, WARNING 7,
# ERROR 5; the three add up to 20).
info_count = 0  # TODO: build it with shift_levels.count("INFO")
warning_count = 0  # TODO: build it with shift_levels.count("WARNING")
error_count = 0  # TODO: build it with shift_levels.count("ERROR")

# TODO 2.2: Store one value per key (given keys with 0 so the skeleton
# runs; replace each 0 with its count variable).
level_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}  # TODO: use info_count, warning_count, error_count

# TODO 2.3: print how many distinct keys the dict holds (expect 3).
print("PENDING")  # TODO: print f"Niveles distintos: {len(level_counts)}"

# TODO 2.4: Count each module with .count() (expect auth 6, backup 8,
# disk 6; the three add up to 20).
auth_count = 0  # TODO: build it with shift_modules.count("auth")
backup_count = 0  # TODO: build it with shift_modules.count("backup")
disk_count = 0  # TODO: build it with shift_modules.count("disk")

# TODO 2.5: Store one value per key (given keys with 0 so the skeleton
# runs; replace each 0 with its count variable).
module_counts = {"auth": 0, "backup": 0, "disk": 0}  # TODO: use auth_count, backup_count, disk_count

# TODO 2.6: print how many distinct keys the dict holds (expect 3).
print("PENDING")  # TODO: print f"Módulos distintos: {len(module_counts)}"

# TODO 2.7: Retire the test key with .pop("DEBUG", 0). The default keeps
# the program running even though DEBUG was never stored.
removed_debug = 0  # TODO: build it with level_counts.pop("DEBUG", 0)

# TODO 2.8: print the retired value (expect 0).
print("PENDING")  # TODO: print f"Clave de prueba retirada: {removed_debug}"

# TODO 2.9: Read the retired key safely with .get("DEBUG", 0). Direct
# level_counts["DEBUG"] would raise KeyError; .get() returns 0.
debug_lookup = 0  # TODO: build it with level_counts.get("DEBUG", 0)

# TODO 2.10: print the safe lookup (expect 0).
print("PENDING")  # TODO: print f"Búsqueda segura de DEBUG: {debug_lookup}"

# TODO 2.11: Model the analyst card as a dict with the keys name, shift,
# and total_events (given structure, fill it with student_name,
# "noche", and 20).
analyst_card = {}  # TODO: replace {} with the three card pairs

# TODO 2.12: Read the card safely: name defaults to "desconocido",
# zone (never recorded) defaults to "laboratorio local".
card_name = "PENDING"  # TODO: build it with analyst_card.get("name", "desconocido")
card_zone = "PENDING"  # TODO: build it with analyst_card.get("zone", "laboratorio local")

# TODO 2.13: print the card (expect Alex Mendez, laboratorio local).
print("PENDING")  # TODO: print f"Tarjeta del analista: {card_name} ({card_zone})"

# Ordered keys reuse Session 06 (given): sorted() returns an ordered
# list of keys, and each position is read back with [0], [1], [2].
ordered_levels = sorted(level_counts)
ordered_modules = sorted(module_counts)

# ==============================================================================
# STEP 3: Communication (given). Ordered summary for the reviewer.
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
