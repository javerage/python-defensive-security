"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 06 (PyDefSec)
FILE: homework_starter.py (guided skeleton for alert_queue.py)
PURPOSE: Review one synthetic in-memory queue of local lab alerts with
         the same linear six-operation pipeline: append, count, index,
         remove, sort, and slice, with intermediate prints after every
         mutation.
NOTE: Homework after class, outside the 60 minutes. Create
      alert_queue.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      summary. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as alert_queue.py plus run:
        python alert_queue.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

BEFORE CODING, ANALYZE (read the queue plus the pipeline first):
    - Which queued text does count() look for, and does count remove it?
    - Which position does index() return for the sensor error, and why
      does it start at 0?
    - Which item does remove() delete, and how does the size change from
      6 back to 5?

DELIVERY: explain aloud the chain ordered collection -> operation ->
visible state -> final sample for all six operations, what each print
proves, and how the final summary is built. Also explain what changes
in the domain (night shift, alert queue) and what technique stays
(same six operations, same evidence chain). Local practice data only.
The program organizes data for human review; it blocks nothing,
isolates nothing, and contacts nothing.
==============================================================================

Conceptual sequence: ordered collection -> operation -> visible state ->
final sample.
Homework chain: new queue -> same six operations -> communication,
while the class exercise processes the service event list.

# Night-shift story (your case, not a literal clone of class): you are
# the night assistant leaving the local alert queue usable before
# handover. You receive five pending alerts, add the archived note with
# append, count the sensor errors, locate their position, remove the
# archived check, sort the same queue, and copy the priority sample.
# Same six decisions as class; new domain (night shift, alert queue).
# Delivery must explain what changes in the domain and what technique
# stays: need -> question -> operation -> variable -> printed evidence.
#
# Collections map (reference only, no exercises beyond list):
# - list: ordered, allows duplicates; the only collection built here.
# - tuple: fixed order without changes; arrives in S08 (mentioned only).
# - set: unique items without order; arrives in S08 (mentioned only).
# - dict: key-value pairs; arrives in S07 (mentioned only).
# - range: number sequences used with loops; arrives in S09 (mentioned only).
#
# Common list queries (reference only; the six TODO calls stay unchanged):
# - The membership operator `in` (an operator, not a method) answers
#   "does this alert exist?" with True/False, False when missing.
# - list.count(value) answers "how many match?" with 0 when missing.
# - list.index(value) answers "where is the first match?" and raises
#   ValueError when missing (no try/except in this session).
# - Contrast with S03 text.find(value): missing text returns -1,
#   while list.index(value) raises ValueError.
# Question "does this alert exist?" asked safely first (commented out,
# not an evaluated step, no summary line, no output change):
#   target_alert = "ERROR: sensor local sin respuesta"
#   print(target_alert in alert_queue)  # True
#   print("ERROR: inexistente" in alert_queue)  # False
# The pipeline uses index() only on a known fixture value.
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
# STEP 2: Six-operation pipeline (TODO). One question, one decision, one evidence.
# ==============================================================================
# TODO 2.1 (operation 1 of 6): add the archived note at the end with append.
# Case question: which night-shift note is archived and missing from the queue?
# Call: alert_queue.append("INFO: nota local archivada")
# Decide to use append because the need is adding one note at the end.
# Evidence check only: size moves 5 -> 6.

# TODO 2.2: print the new size with len() to prove the note was added.
# Case question: what does the new size prove after the append?
# Call: print with f"Alertas tras agregar: {len(alert_queue)}" using len.
# Decide to use len because the need is showing the size as evidence.
# Evidence check only: 6.
print("PENDING")  # TODO: leave evidence with f"Alertas tras agregar: {len(alert_queue)}"

# TODO 2.3 (operation 2 of 6): count the sensor-error matches with count, without removing.
# Case question: how many times does the sensor error appear in the queue?
# Call: alert_queue.count("ERROR: sensor local sin respuesta") stored in sensor_errors.
# Decide to use count because the need is how-many matches without removing.
# Evidence check only: 1.
sensor_errors = 0  # TODO: decide the query from the mapping table

# TODO 2.4: print the count result to prove how many sensor errors exist.
# Case question: what does the count prove about the sensor error?
# Call: print with f"Errores del sensor: {sensor_errors}" showing the count result.
# Decide to print the count variable because the need is leaving the count as evidence.
# Evidence check only: 1.
print("PENDING")  # TODO: leave evidence with f"Errores del sensor: {sensor_errors}"

# TODO 2.5 (operation 3 of 6): locate the first match position with index, counting from 0.
# Case question: where does the first sensor error sit in the queue?
# Call: alert_queue.index("ERROR: sensor local sin respuesta") stored in sensor_position.
# Decide to use index because the need is the position of the first match from 0.
# Evidence check only: 2.
sensor_position = 0  # TODO: decide the query from the mapping table

# TODO 2.6: print the position result to prove where the first match sits.
# Case question: what does the position prove about the sensor error?
# Call: print with f"Posición del error: {sensor_position}" showing the index result.
# Decide to print the index variable because the need is leaving the position as evidence.
# Evidence check only: 2.
print("PENDING")  # TODO: leave evidence with f"Posición del error: {sensor_position}"

# TODO 2.7 (operation 4 of 6): take out the archived check by value with remove.
# Case question: which alert must be taken out once it is archived?
# Call: alert_queue.remove("INFO: verificación local completa")
# Decide to use remove because the need is deleting one item by value.
# Evidence check only: size moves 6 -> 5.

# TODO 2.8: print the new size with len() to prove the alert was removed.
# Case question: what does the new size prove after the remove?
# Call: print with f"Alertas tras eliminar: {len(alert_queue)}" using len.
# Decide to use len because the need is showing the size as evidence of remove.
# Evidence check only: 5.
print("PENDING")  # TODO: leave evidence with f"Alertas tras eliminar: {len(alert_queue)}"

# TODO 2.9 (operation 5 of 6): order the same queue in place with sort, used alone and never assigned.
# Case question: how should the same queue look in order without creating a new queue?
# Call: alert_queue.sort() alone; decide to use sort because the need is ordering in place.
# Do not store the result because sort returns None.

# TODO 2.10: print the ordered queue to prove the sort result.
# Case question: what does the ordered state prove after sort?
# Call: print with f"Alertas ordenadas: {alert_queue}" showing the sort result.
# Decide to print the same queue because the need is leaving the ordered state as evidence.
print("PENDING")  # TODO: leave evidence with f"Alertas ordenadas: {alert_queue}"

# TODO 2.11 (operation 6 of 6): copy a three-item sample with slicing [0:3] without touching the original.
# Case question: which three-item priority sample shows the head of the ordered queue?
# Call: alert_queue[0:3] stored in priority_sample, keeping positions 0, 1, and 2.
# Decide to use slicing [0:3] because the need is copying a range without touching the original.
# Evidence check only: positions 0, 1, and 2.
priority_sample = []  # TODO: decide the slice from the mapping table

# TODO 2.12: print the sample to prove what the [0:3] slice copied.
# Case question: what does the three-item priority sample prove about the ordered queue?
# Call: print with f"Muestra prioritaria: {priority_sample}" showing the [0:3] result.
# Decide to print the slice variable because the need is leaving the sample as evidence.
print("PENDING")  # TODO: leave evidence with f"Muestra prioritaria: {priority_sample}"

# ==============================================================================
# STEP 3: Communication (given). Readable summary for the reviewer.
# ==============================================================================
print("--- Resumen de la cola ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total final: {len(alert_queue)}")
print(f"Errores del sensor: {sensor_errors}")
print(f"Posición del error: {sensor_position}")
print(f"Muestra prioritaria: {priority_sample}")
