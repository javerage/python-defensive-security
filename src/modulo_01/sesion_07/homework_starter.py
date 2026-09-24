"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 07 (PyDefSec)
FILE: homework_starter.py (guided skeleton for shift_summary.py)
PURPOSE: Inspect, query, modify, and communicate a precomputed dictionary
         summary of one synthetic local night shift: read known keys
         directly, count keys with len(), stage plus retire one test key
         with pop(), read safely with .get(), model the analyst card as
         a dict, and print an ordered summary without any loop.
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
    - Which three direct reads feed on level_counts, and what do the
      three values add up to?
    - Which key does .pop("DEBUG", 0) retire, and why does the default
      keep the program running?
    - Which card field is missing, and which default does .get() return
      for it?

DELIVERY: explain aloud the chain given summary -> direct read -> key
count -> safe lookup -> ordered summary for levels and for modules, how
many keys each dict holds and why, and how each result reaches the
summary. Local practice data only. The program organizes data for human
review; it blocks nothing, isolates nothing, and contacts nothing.
==============================================================================

Conceptual sequence: given summary -> direct read -> key count -> safe
lookup -> ordered summary.
Homework chain: new shift summary -> same reading technique -> analyst
card -> communication, while the class exercise summarizes the day
summary.
"""

# ==============================================================================
# STEP 1: Summary (given). A prior local process summarized 20 synthetic
# night-shift observations into one total per label, plus operator
# identity and the analyst card.
# ==============================================================================
level_counts = {"INFO": 8, "WARNING": 7, "ERROR": 5}
module_counts = {"auth": 6, "backup": 8, "disk": 6}

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# Analyst card (given structure): one dict models whose shift this is.
analyst_card = {"name": student_name, "shift": "noche", "total_events": 20}

print(f"Observaciones del turno: {analyst_card['total_events']}")

# ==============================================================================
# STEP 2: Reads plus handling (TODO). Direct access for known keys, key
# counts with len(), one staged plus retired test key, safe lookups.
# ==============================================================================
# TODO 2.1: Read each known level directly (expect INFO 8, WARNING 7,
# ERROR 5; the three add up to 20).
info_count = 0  # TODO: read it with level_counts["INFO"]
warning_count = 0  # TODO: read it with level_counts["WARNING"]
error_count = 0  # TODO: read it with level_counts["ERROR"]

# TODO 2.2: print how many distinct keys the dict holds (expect 3).
print("PENDING")  # TODO: print f"Niveles distintos: {len(level_counts)}"

# TODO 2.3: Read each known module directly (expect auth 6, backup 8,
# disk 6; the three add up to 20).
auth_count = 0  # TODO: read it with module_counts["auth"]
backup_count = 0  # TODO: read it with module_counts["backup"]
disk_count = 0  # TODO: read it with module_counts["disk"]

# TODO 2.4: print how many distinct keys the dict holds (expect 3).
print("PENDING")  # TODO: print f"Módulos distintos: {len(module_counts)}"

# TODO 2.5: Stage a test key DEBUG with 0, then retire it with
# .pop("DEBUG", 0) and keep the retired value in removed_debug.
removed_debug = 0  # TODO: add the two lines above this print first

# TODO 2.6: print the retired value (expect 0).
print("PENDING")  # TODO: print f"Clave de prueba retirada: {removed_debug}"

# TODO 2.7: Read the retired key safely with .get("DEBUG", 0). Direct
# level_counts["DEBUG"] would raise KeyError; .get() returns 0.
debug_lookup = 0  # TODO: build it with level_counts.get("DEBUG", 0)

# TODO 2.8: print the safe lookup (expect 0).
print("PENDING")  # TODO: print f"Búsqueda segura de DEBUG: {debug_lookup}"

# TODO 2.9: Read the card safely: name defaults to "desconocido",
# zone (never recorded) defaults to "laboratorio local".
card_name = "PENDING"  # TODO: build it with analyst_card.get("name", "desconocido")
card_zone = "PENDING"  # TODO: build it with analyst_card.get("zone", "laboratorio local")

# TODO 2.10: print the card (expect Alex Mendez, laboratorio local).
print("PENDING")  # TODO: print f"Tarjeta del analista: {card_name} ({card_zone})"

# Ordered keys reuse Session 06 (given): sorted() returns an ordered
# list of keys, and each position is read back with [0], [1], [2].
ordered_levels = sorted(level_counts)
ordered_modules = sorted(module_counts)

# ==============================================================================
# STEP 3: Communication (given frame, TODO lines). Ordered summary for
# the reviewer; PENDING marks each line you still have to write.
# ==============================================================================
print("--- Resumen del turno ---")
print(f"Nombre: {card_name}")
print(f"Identificador: {student_id}")
print(f"Total de observaciones: {analyst_card['total_events']}")
print("PENDING")  # TODO: print f"{ordered_levels[0]}: {level_counts[ordered_levels[0]]}"
print("PENDING")  # TODO: print f"{ordered_levels[1]}: {level_counts[ordered_levels[1]]}"
print("PENDING")  # TODO: print f"{ordered_levels[2]}: {level_counts[ordered_levels[2]]}"
print("PENDING")  # TODO: print f"{ordered_modules[0]}: {module_counts[ordered_modules[0]]}"
print("PENDING")  # TODO: print f"{ordered_modules[1]}: {module_counts[ordered_modules[1]]}"
print("PENDING")  # TODO: print f"{ordered_modules[2]}: {module_counts[ordered_modules[2]]}"
print("PENDING")  # TODO: print f"Resumen: {len(level_counts)} claves de nivel, {len(module_counts)} claves de módulo"
