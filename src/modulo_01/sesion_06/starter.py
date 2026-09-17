"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 06 (PyDefSec)
FILE: starter.py (guided skeleton for event_pipeline.py)
PURPOSE: Process ONE synthetic in-memory list of local lab events with
         a linear six-operation pipeline: append, count, index, remove,
         sort, and slice, with intermediate prints after every mutation.
NOTE: The repository is only a backup. Create event_pipeline.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected summary.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as event_pipeline.py and run:
        python event_pipeline.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the pipeline table in your student material first: it holds
    the six operations in the order you must apply them. No part of
    this skeleton shows the final calls, counts, or positions.
==============================================================================

Conceptual sequence: ordered collection -> operation -> visible state ->
final sample.
A list keeps duplicates and order; every operation shows its effect
with a print before moving on.

# Collections map (reference only, no exercises beyond list):
# - list: ordered, allows duplicates; the only collection built here.
# - tuple: fixed order without changes; arrives in S08 (mentioned only).
# - set: unique items without order; arrives in S08 (mentioned only).
# - dict: key-value pairs; arrives in S07 (mentioned only).
# - range: number sequences used with loops; arrives in S09 (mentioned only).
#
# Abstraction to apply (need -> question -> operation -> variable ->
# printed evidence): read each TODO as one case question, decide which
# single operation answers it, then leave one printed line as evidence.
#
# Common list queries (reference only; the six TODO calls stay unchanged):
# - The membership operator `in` (an operator, not a method) answers
#   "does this event exist?" with True/False, False when missing.
# - list.count(value) answers "how many match?" with 0 when missing.
# - list.index(value) answers "where is the first match?" and raises
#   ValueError when missing (no try/except in this session).
# - Contrast with S03 text.find(value): missing text returns -1,
#   while list.index(value) raises ValueError.
# Question "does this event exist?" asked safely first (commented out,
# not an evaluated step, no summary line, no output change):
#   target_event = "ERROR: disco lleno en el laboratorio"
#   print(target_event in event_log)  # True
#   print("ERROR: inexistente" in event_log)  # False
# The pipeline uses index() only on a known fixture value.
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
# STEP 2: Six-operation pipeline (TODO). One question, one decision, one evidence.
# =============================================================================
# TODO 2.1 (operation 1 of 6): add the late event at the end with append.
# Case question: which event arrived late and is missing from the list?
# Call: event_log.append("WARNING: reintento local programado")
# Decide to use append because the need is adding one item at the end.
# Evidence check only: size moves 5 -> 6.

# TODO 2.2: print the new size with len() to prove the event was added.
# Case question: what does the new size prove after the append?
# Call: print with f"Eventos tras agregar: {len(event_log)}" using len.
# Decide to use len because the need is showing the size as evidence.
# Evidence check only: 6.
print("PENDING")  # TODO: leave evidence with f"Eventos tras agregar: {len(event_log)}"

# TODO 2.3 (operation 2 of 6): count the disk-full matches with count, without removing.
# Case question: how many times does the disk-full error appear in the list?
# Call: event_log.count("ERROR: disco lleno en el laboratorio") stored in error_count.
# Decide to use count because the need is how-many matches without removing.
# Evidence check only: 1.
error_count = 0  # TODO: decide the query from the mapping table

# TODO 2.4: print the count result to prove how many disk-full errors exist.
# Case question: what does the count prove about the disk-full error?
# Call: print with f"Errores de disco lleno: {error_count}" showing the count result.
# Decide to print the count variable because the need is leaving the count as evidence.
# Evidence check only: 1.
print("PENDING")  # TODO: leave evidence with f"Errores de disco lleno: {error_count}"

# TODO 2.5 (operation 3 of 6): locate the first match position with index, counting from 0.
# Case question: where does the first disk-full error sit in the list?
# Call: event_log.index("ERROR: disco lleno en el laboratorio") stored in error_position.
# Decide to use index because the need is the position of the first match from 0.
# Evidence check only: 3.
error_position = 0  # TODO: decide the query from the mapping table

# TODO 2.6: print the position result to prove where the first match sits.
# Case question: what does the position prove about the disk-full error?
# Call: print with f"Posición del error: {error_position}" showing the index result.
# Decide to print the index variable because the need is leaving the position as evidence.
# Evidence check only: 3.
print("PENDING")  # TODO: leave evidence with f"Posición del error: {error_position}"

# TODO 2.7 (operation 4 of 6): take out the archived item by value with remove.
# Case question: which event must be taken out once it is archived?
# Call: event_log.remove("INFO: respaldo local completo")
# Decide to use remove because the need is deleting one item by value.
# Evidence check only: size moves 6 -> 5.

# TODO 2.8: print the new size with len() to prove the event was removed.
# Case question: what does the new size prove after the remove?
# Call: print with f"Eventos tras eliminar: {len(event_log)}" using len.
# Decide to use len because the need is showing the size as evidence of remove.
# Evidence check only: 5.
print("PENDING")  # TODO: leave evidence with f"Eventos tras eliminar: {len(event_log)}"

# TODO 2.9 (operation 5 of 6): order the same list in place with sort, used alone and never assigned.
# Case question: how should the same list look in order without creating a new list?
# Call: event_log.sort() alone; decide to use sort because the need is ordering in place.
# Do not store the result because sort returns None.

# TODO 2.10: print the ordered list to prove the sort result.
# Case question: what does the ordered state prove after sort?
# Call: print with f"Eventos ordenados: {event_log}" showing the sort result.
# Decide to print the same list because the need is leaving the ordered state as evidence.
print("PENDING")  # TODO: leave evidence with f"Eventos ordenados: {event_log}"

# TODO 2.11 (operation 6 of 6): copy a three-item sample with slicing [0:3] without touching the original.
# Case question: which three-item sample shows the head of the ordered list?
# Call: event_log[0:3] stored in recent_events, keeping positions 0, 1, and 2.
# Decide to use slicing [0:3] because the need is copying a range without touching the original.
# Evidence check only: positions 0, 1, and 2.
recent_events = []  # TODO: decide the slice from the mapping table

# TODO 2.12: print the sample to prove what the [0:3] slice copied.
# Case question: what does the three-item sample prove about the ordered list?
# Call: print with f"Muestra ordenada: {recent_events}" showing the [0:3] result.
# Decide to print the slice variable because the need is leaving the sample as evidence.
print("PENDING")  # TODO: leave evidence with f"Muestra ordenada: {recent_events}"

# ==============================================================================
# STEP 3: Communication (given). Readable console summary for the reviewer.
# ==============================================================================
print("--- Resumen de eventos ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total final: {len(event_log)}")
print(f"Errores de disco lleno: {error_count}")
print(f"Posición del error: {error_position}")
print(f"Muestra ordenada: {recent_events}")
