"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 10 (PyDefSec)
FILE: homework_starter.py (guided skeleton for night_review.py)
PURPOSE: Review a 2-night local matrix of 6 events per night with
         nested loops: skip 1 malformed UNKNOWN line with continue
         and show the per-night summary with verified totals.
NOTE: Homework after class, outside the 60 minutes. Create
      night_review.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      summary. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as night_review.py plus run:
        python night_review.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

BEFORE CODING, PREDICT (count by hand first, without running):
    - How many ERROR entries are there per night by hand, and in
      which position is the single UNKNOWN? Write your count first.
    - Which line adds to night_skipped, and why does that position
      never add to the total?
    - What will the general total hold when both nights accumulate,
      and what does that mean for whoever receives the shift?

DELIVERY: explain aloud the chain matrix -> night -> event ->
skipped -> subtotal -> total. Local practice data only. The program
organizes data for human review; it opens no ports, touches no disk,
and contacts nothing.
==============================================================================

Conceptual sequence: matrix -> nested walk -> skipped line ->
subtotals -> verified total.
Homework chain: new shorter data (2 nights) -> same nested technique,
while the class exercise reviews 3 days with an early stop.
"""

# ==============================================================================
# STEP 1: Evidence (given). Two synthetic local nights of 6 positions
# each plus operator identity.
# ==============================================================================
night_logs = [
    ["INFO", "WARNING", "ERROR", "INFO", "ERROR", "INFO"],
    ["ERROR", "UNKNOWN", "INFO", "WARNING", "ERROR", "INFO"],
]

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Noches registradas: {len(night_logs)}")

# ==============================================================================
# STEP 2: Nested walk (TODO). Outer night, inner event; continue skips
# the malformed line. No functions, no third level.
# PREDICT FIRST: before completing each TODO, write your prediction
# (which value you expect and why); run the script; then compare
# with the expected output in the student material.
# ==============================================================================
# TODO 2.1: Start night_grand at 0, night_skipped at 0, night_totals
# with two zeros, and night_index at 0.
night_grand = 0  # TODO: keep it, the nested walk adds each ERROR here
night_skipped = 0  # TODO: keep it, the continue adds 1 here
night_totals = [0, 0]  # TODO: keep it, position night_index holds its night
night_index = 0  # TODO: keep it, it points at the current night

# TODO 2.2: Walk night by night. For each night, visit each event:
# on "UNKNOWN" add 1 to night_skipped and continue; on "ERROR" add 1
# to night_totals[night_index] and to night_grand. After each night,
# advance night_index = night_index + 1.

# TODO 2.3: print each night subtotal.
print("PENDING")  # TODO: print f"Noche 1: {night_totals[0]}"
print("PENDING")  # TODO: print f"Noche 2: {night_totals[1]}"

# TODO 2.4: print the skipped lines.
print("PENDING")  # TODO: print f"Omitidas: {night_skipped}"

# TODO 2.5: print the general total.
print("PENDING")  # TODO: print f"Total de errores: {night_grand}"

# Positions of this lab: 2 nights of 6 (given expressions, they stay).
night_positions = len(night_logs[0]) + len(night_logs[1])
night_valid = night_positions - night_skipped

# ==============================================================================
# STEP 3: Communication (given). Per-night summary for whoever receives
# the shift.
# ==============================================================================
print("--- Resumen por noche ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Noches: {len(night_logs)}, posiciones: {night_positions}, válidas: {night_valid}")
