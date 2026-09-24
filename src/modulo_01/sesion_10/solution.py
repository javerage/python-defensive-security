"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 10 (PyDefSec)
FILE: solution.py (reference for matrix_review.py)
PURPOSE: Review a 3-day local matrix of 6 events per day with nested
         loops: skip 2 malformed UNKNOWN lines with continue, stop
         day 3 early at STOP with break, and show the per-day summary
         with verified totals.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      matrix_review.py manually.
WHY TWO LEVELS: one flat loop from Session 09 cannot separate days.
      The outer for chooses the day and the inner for visits each
      event; a third level is never needed in this lab.
PEDAGOGICAL RESTRICTIONS:
    - Nested loops of two levels only: outer day, inner event, one
      break and one continue, skipped counter.
    - No functions, no loop else, no try/except, no imports, no files,
      no network.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
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
# STEP 2: Nested walk. The outer cycle climbs floors; the inner cycle
# knocks on each door. continue skips ONE door and keeps the floor;
# break closes THE FLOOR at the stop sign.
# ==============================================================================
grand_total = 0
skipped = 0
day_totals = [0, 0, 0]
day_index = 0

for day in day_logs:
    for event in day:
        if event == "UNKNOWN":
            skipped = skipped + 1
            continue
        if event == "STOP":
            break
        if event == "ERROR":
            day_totals[day_index] = day_totals[day_index] + 1
            grand_total = grand_total + 1
    day_index = day_index + 1

print(f"Día 1: {day_totals[0]}")
print(f"Día 2: {day_totals[1]}")
print(f"Día 3: {day_totals[2]}")
print(f"Omitidas: {skipped}")
print(f"Total de errores: {grand_total}")

# Positions of this lab: 3 days of 6, minus the skipped lines.
total_positions = len(day_logs[0]) + len(day_logs[1]) + len(day_logs[2])
valid_positions = total_positions - skipped

# ==============================================================================
# STEP 3: Communication (given). Per-day summary for the reviewer.
# Subtotals prove nothing by themselves; they order human review of
# local practice data. The program opens no ports, touches no disk,
# and contacts nothing.
# ==============================================================================
print("--- Resumen por día ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Días: {len(day_logs)}, posiciones: {total_positions}, válidas: {valid_positions}")
