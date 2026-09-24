"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 07 (PyDefSec)
FILE: homework_solution.py (reference for shift_summary.py)
PURPOSE: Inspect, query, modify, and communicate a precomputed dictionary
         summary of one synthetic local night shift: read known keys
         directly, count keys with len(), stage plus retire one test key
         with pop(), read safely with .get(), model the analyst card as
         a dict, and print an ordered summary without any loop.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_summary.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no loops, no imports, no tuples, no sets).
    - Only dicts over given summaries: direct access for known keys,
      len() over keys, item assignment, .pop() with default, .get()
      with default, and sorted() over keys.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: given summary (label -> total) -> direct read ->
key count -> safe lookup -> ordered summary.
A prior local process summarized 20 synthetic night-shift observations;
this script consumes that summary and communicates it. It does not
regenerate the totals from raw observations: that automation arrives
with loops in Session 09.
Homework chain: new shift summary -> same reading technique -> analyst
card -> communication, while the class exercise summarizes the day
summary. Summaries order human review of local practice data; this one
blocks nothing, isolates nothing, and contacts nothing.
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
# STEP 2: Reads plus handling. Direct access for known keys, key counts
# with len(), one staged plus retired test key, and safe lookups.
# ==============================================================================
info_count = level_counts["INFO"]
warning_count = level_counts["WARNING"]
error_count = level_counts["ERROR"]

print(f"Niveles distintos: {len(level_counts)}")

auth_count = module_counts["auth"]
backup_count = module_counts["backup"]
disk_count = module_counts["disk"]

print(f"Módulos distintos: {len(module_counts)}")

# Staging and removal: add a provisional key, then retire it. pop() with
# a default retires the key without raising when it is missing.
level_counts["DEBUG"] = 0
removed_debug = level_counts.pop("DEBUG", 0)
print(f"Clave de prueba retirada: {removed_debug}")

# Safe lookups with defaults: 0 for the retired key, and the local lab
# for the card field this shift never recorded.
debug_lookup = level_counts.get("DEBUG", 0)
print(f"Búsqueda segura de DEBUG: {debug_lookup}")

# .get() with a default covers the field the shift never recorded.
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
print(f"Total de observaciones: {analyst_card['total_events']}")
print(f"{ordered_levels[0]}: {level_counts[ordered_levels[0]]}")
print(f"{ordered_levels[1]}: {level_counts[ordered_levels[1]]}")
print(f"{ordered_levels[2]}: {level_counts[ordered_levels[2]]}")
print(f"{ordered_modules[0]}: {module_counts[ordered_modules[0]]}")
print(f"{ordered_modules[1]}: {module_counts[ordered_modules[1]]}")
print(f"{ordered_modules[2]}: {module_counts[ordered_modules[2]]}")
print(f"Resumen: {len(level_counts)} claves de nivel, {len(module_counts)} claves de módulo")
