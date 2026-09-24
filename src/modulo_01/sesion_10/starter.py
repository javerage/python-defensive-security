"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 10 (PyDefSec)
FILE: starter.py (guided skeleton for matrix_review.py)
PURPOSE: Review a 3-day local matrix of 6 events per day with nested
         loops: skip 2 malformed UNKNOWN lines with continue, stop
         day 3 early at STOP with break, and show the per-day summary
         with verified totals.
NOTE: The repository is only a backup. Create matrix_review.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected summary.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as matrix_review.py and run:
        python matrix_review.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the 3-day matrix in your student material first and count
    the ERROR entries of day 1 by hand before coding: each day must
    leave its own subtotal and the skipped lines stay declared.
    No part of this skeleton shows the final counts.

NESTING SHAPE: the outer for chooses the day, the inner for visits
    each event. Indent one level (4 spaces) per cycle, never mixed.
==============================================================================

Conceptual sequence: matrix (days -> events) -> nested walk ->
skipped lines plus early stop -> subtotals -> verified total.
3 days of 6 positions hold 18 visits; 2 skipped leave 16 valid.
"""

# ==============================================================================
# STEP 1: Evidence (given). Three synthetic local days of 6 positions
# each plus operator identity.
# ==============================================================================
day_logs = [
    ["INFO", "ERROR", "UNKNOWN", "INFO", "ERROR", "INFO"],
    ["WARNING", "ERROR", "INFO", "UNKNOWN", "INFO", "ERROR"],
    ["INFO", "ERROR", "STOP", "ERROR", "INFO", "WARNING"],
]

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Días registrados: {len(day_logs)}")

# ==============================================================================
# STEP 2: Nested walk (TODO). Outer day, inner event; continue skips
# one line, break stops only its own day. No functions, no third level.
# PREDICT FIRST: before completing each TODO, write your prediction
# (which value you expect and why); run the script; then compare
# with the expected output in the student material.
# ==============================================================================
# TODO 2.1: Start grand_total at 0, skipped at 0, day_totals with
# three zeros, and day_index at 0.
grand_total = 0  # TODO: keep it, the nested walk adds each ERROR here
skipped = 0  # TODO: keep it, each continue adds 1 here
day_totals = [0, 0, 0]  # TODO: keep it, position day_index holds its day
day_index = 0  # TODO: keep it, it points at the current day

# TODO 2.2: Walk day by day. For each day, visit each event: on
# "UNKNOWN" add 1 to skipped and continue; on "STOP" break the day;
# on "ERROR" add 1 to day_totals[day_index] and to grand_total.
# After each day, advance day_index = day_index + 1.

# TODO 2.3: print each day subtotal.
print("PENDING")  # TODO: print f"Día 1: {day_totals[0]}"
print("PENDING")  # TODO: print f"Día 2: {day_totals[1]}"
print("PENDING")  # TODO: print f"Día 3: {day_totals[2]}"

# TODO 2.4: print the skipped lines.
print("PENDING")  # TODO: print f"Omitidas: {skipped}"

# TODO 2.5: print the general total.
print("PENDING")  # TODO: print f"Total de errores: {grand_total}"

# Positions of this lab: 3 days of 6 (given expressions, they stay).
total_positions = len(day_logs[0]) + len(day_logs[1]) + len(day_logs[2])
valid_positions = total_positions - skipped

# ==============================================================================
# STEP 3: Communication (given). Per-day summary for the reviewer.
# ==============================================================================
print("--- Resumen por día ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Días: {len(day_logs)}, posiciones: {total_positions}, válidas: {valid_positions}")
