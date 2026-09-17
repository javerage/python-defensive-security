"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 06 (PyDefSec)
FILE: homework_solution.py (reference for alert_queue.py)
PURPOSE: Review one synthetic in-memory queue of local lab alerts with
         the same linear six-operation pipeline: append, count, index,
         remove, sort, and slice, with intermediate prints after every
         mutation.
NOTE: Homework after class, outside the 60 minutes. Create
      alert_queue.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no loops, no imports, no dicts, no tuples, no sets).
    - Only list creation, indexing, slicing, len(), and the basic
      methods append, count, index, remove, sort.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: ordered collection -> operation -> visible state ->
final sample.
Homework chain: new queue -> same six operations -> communication,
while the class exercise processes the service event list. The queue
holds local practice alerts only; True counts and positions prove no
attack. This summary organizes data for human review. It blocks
nothing, isolates nothing, and contacts nothing.

# Night-shift story (reference only): the night assistant receives five
# pending local alerts before handover, must leave the queue usable for
# the reviewer, applies the same six decisions in order, and proves each
# step with one printed line. Domain changes (alert queue, night shift);
# technique stays (same six operations, same evidence chain).
#
# Collections map (reference only, no exercises beyond list):
# - list: ordered, allows duplicates; the only collection built here.
# - tuple: fixed order without changes; arrives in S08 (mentioned only).
# - set: unique items without order; arrives in S08 (mentioned only).
# - dict: key-value pairs; arrives in S07 (mentioned only).
# - range: number sequences used with loops; arrives in S09 (mentioned only).
#
# Abstraction applied below (need -> question -> operation -> variable
# -> printed evidence): each step answers one shift question with one
# operation and one printed line as evidence.
#
# Common list queries (reference only; only the six pipeline calls run):
# - The membership operator `in` (an operator, not a method) answers
#   "does this alert exist?" with True/False, False when missing.
# - list.count(value) answers "how many match?" with 0 when missing.
# - list.index(value) answers "where is the first match?" and raises
#   ValueError when missing (no try/except in this session).
# - Contrast with S03 text.find(value): missing text returns -1,
#   while list.index(value) raises ValueError.
# Question "does this alert exist?" asked safely first (commented out,
# not part of the six evaluated steps, no summary line, no output change):
#   target_alert = "ERROR: sensor local sin respuesta"
#   print(target_alert in alert_queue)  # True
#   print("ERROR: inexistente" in alert_queue)  # False
# The pipeline below uses index() only on a known fixture value.
"""

# ==============================================================================
# STEP 1: Evidence (given). One synthetic in-memory alert queue plus
# operator identity. Positions start at 0.
# ==============================================================================
alert_queue = [
    "WARNING: reintento local pendiente",
    "INFO: verificación local completa",
    "ERROR: sensor local sin respuesta",
    "INFO: turno de revisión registrado",
    "WARNING: espacio bajo en el laboratorio",
]

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Alertas iniciales: {len(alert_queue)}")

# ==============================================================================
# STEP 2: Six-operation pipeline. One operation, one visible state.
# ==============================================================================
# Operation 1 of 6: append adds one item at the end (5 -> 6).
alert_queue.append("INFO: nota local archivada")
print(f"Alertas tras agregar: {len(alert_queue)}")

# Operation 2 of 6: count scans and returns matches (no removal).
sensor_errors = alert_queue.count("ERROR: sensor local sin respuesta")
print(f"Errores del sensor: {sensor_errors}")

# Operation 3 of 6: index returns the position of the first match.
sensor_position = alert_queue.index("ERROR: sensor local sin respuesta")
print(f"Posición del error: {sensor_position}")

# Operation 4 of 6: remove deletes the first matching item by value (6 -> 5).
alert_queue.remove("INFO: verificación local completa")
print(f"Alertas tras eliminar: {len(alert_queue)}")

# Operation 5 of 6: sort orders the same list in place (never assigned).
alert_queue.sort()
print(f"Alertas ordenadas: {alert_queue}")

# Operation 6 of 6: slicing copies [start:end] without touching the original.
priority_sample = alert_queue[0:3]
print(f"Muestra prioritaria: {priority_sample}")

# ==============================================================================
# STEP 3: Communication. Readable summary for the reviewer.
# ==============================================================================
print("--- Resumen de la cola ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total final: {len(alert_queue)}")
print(f"Errores del sensor: {sensor_errors}")
print(f"Posición del error: {sensor_position}")
print(f"Muestra prioritaria: {priority_sample}")
