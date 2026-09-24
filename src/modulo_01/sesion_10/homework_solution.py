"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 10 (PyDefSec)
FILE: homework_solution.py (reference for night_review.py)
PURPOSE: Review a 2-night local matrix of 6 events per night with
         nested loops: skip 1 malformed UNKNOWN line with continue
         and show the per-night summary with verified totals.
NOTE: Homework after class, outside the 60 minutes. Create
      night_review.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Nested loops of two levels only: outer night, inner event, one
      continue, skipped counter.
    - No functions, no loop else, no try/except, no imports, no files,
      no network.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: matrix -> nested walk -> skipped line ->
subtotals -> verified total.
Homework chain: new shorter data (2 nights) -> same nested technique,
while the class exercise reviews 3 days with an early stop. Subtotals
prove nothing by themselves; they order human review of local practice
data. This summary opens no ports, touches no disk, and contacts
nothing.
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
# STEP 2: Nested walk. The outer cycle chooses the night; the inner
# cycle visits each event; continue skips the malformed line only.
# ==============================================================================
night_grand = 0
night_skipped = 0
night_totals = [0, 0]
night_index = 0

for night in night_logs:
    for event in night:
        if event == "UNKNOWN":
            night_skipped = night_skipped + 1
            continue
        if event == "ERROR":
            night_totals[night_index] = night_totals[night_index] + 1
            night_grand = night_grand + 1
    night_index = night_index + 1

print(f"Noche 1: {night_totals[0]}")
print(f"Noche 2: {night_totals[1]}")
print(f"Omitidas: {night_skipped}")
print(f"Total de errores: {night_grand}")

# Positions of this lab: 2 nights of 6, minus the skipped line.
night_positions = len(night_logs[0]) + len(night_logs[1])
night_valid = night_positions - night_skipped

# ==============================================================================
# STEP 3: Communication. Per-night summary for whoever receives the shift.
# ==============================================================================
print("--- Resumen por noche ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Noches: {len(night_logs)}, posiciones: {night_positions}, válidas: {night_valid}")
