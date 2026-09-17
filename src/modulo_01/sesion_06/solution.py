"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 06 (PyDefSec)
FILE: solution.py (reference for event_pipeline.py)
PURPOSE: Process ONE synthetic in-memory list of local lab events with
         a linear six-operation pipeline: append, count, index, remove,
         sort, and slice, with intermediate prints after every mutation.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      event_pipeline.py manually.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no loops, no imports, no dicts, no tuples, no sets).
    - Only list creation, indexing, slicing, len(), and the basic
      methods append, count, index, remove, sort.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: ordered collection -> operation -> visible state ->
final sample.
A list keeps duplicates and order; every operation below shows its
effect with a print before moving on. Unpacking and nested matrices
are not used in this session.

# Collections map (reference only, no exercises beyond list):
# - list: ordered, allows duplicates; the only collection built here.
# - tuple: fixed order without changes; arrives in S08 (mentioned only).
# - set: unique items without order; arrives in S08 (mentioned only).
# - dict: key-value pairs; arrives in S07 (mentioned only).
# - range: number sequences used with loops; arrives in S09 (mentioned only).
#
# Abstraction applied below (need -> question -> operation -> variable
# -> printed evidence): each pipeline step answers one case question,
# applies one operation, stores or shows one variable/call, and leaves
# one printed line as evidence before moving on.
#
# Common list queries (reference only; only the six pipeline calls run):
# - The membership operator `in` (an operator, not a method) answers
#   "does this event exist?" with True/False, False when missing.
# - list.count(value) answers "how many match?" with 0 when missing.
# - list.index(value) answers "where is the first match?" and raises
#   ValueError when missing (no try/except in this session).
# - Contrast with S03 text.find(value): missing text returns -1,
#   while list.index(value) raises ValueError. No new behavior is
#   evaluated here.
# Question "does this event exist?" asked safely first (commented out,
# not part of the six evaluated steps, no summary line, no output change):
#   target_event = "ERROR: disco lleno en el laboratorio"
#   print(target_event in event_log)  # True
#   print("ERROR: inexistente" in event_log)  # False
# The pipeline below uses index() only on a known fixture value, after
# the safe question above was already answered in the materials.
"""

# ==============================================================================
# STEP 1: Evidence (given). One synthetic in-memory event list plus
# operator identity. Positions start at 0: the first item lives at [0].
# ==============================================================================
event_log = [
    "INFO: servicio local iniciado",
    "WARNING: memoria alta en el laboratorio",
    "INFO: respaldo local completo",
    "ERROR: disco lleno en el laboratorio",
    "INFO: usuario local registrado",
]

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Eventos iniciales: {len(event_log)}")

# ==============================================================================
# STEP 2: Six-operation pipeline. One operation, one visible state.
# ==============================================================================
# Operation 1 of 6: append adds one item at the end (5 -> 6).
event_log.append("WARNING: reintento local programado")
print(f"Eventos tras agregar: {len(event_log)}")

# Operation 2 of 6: count scans the list and returns matches (no removal).
error_count = event_log.count("ERROR: disco lleno en el laboratorio")
print(f"Errores de disco lleno: {error_count}")

# Operation 3 of 6: index returns the position of the first match.
error_position = event_log.index("ERROR: disco lleno en el laboratorio")
print(f"Posición del error: {error_position}")

# Operation 4 of 6: remove deletes the first matching item by value (6 -> 5).
event_log.remove("INFO: respaldo local completo")
print(f"Eventos tras eliminar: {len(event_log)}")

# Operation 5 of 6: sort orders the same list in place (returns None,
# so it is never assigned). Smallest first: ERROR, then INFO, then WARNING.
event_log.sort()
print(f"Eventos ordenados: {event_log}")

# Operation 6 of 6: slicing copies a range [start:end] without touching
# the original. [0:3] keeps positions 0, 1, and 2.
recent_events = event_log[0:3]
print(f"Muestra ordenada: {recent_events}")

# ==============================================================================
# STEP 3: Communication (given). Readable console summary for the reviewer.
# The program organizes local practice data; it blocks nothing, isolates
# nothing, and contacts nothing.
# ==============================================================================
print("--- Resumen de eventos ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total final: {len(event_log)}")
print(f"Errores de disco lleno: {error_count}")
print(f"Posición del error: {error_position}")
print(f"Muestra ordenada: {recent_events}")
