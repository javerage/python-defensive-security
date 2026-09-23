"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 08 (PyDefSec)
FILE: homework_solution.py (reference for shift_groups.py)
PURPOSE: Group one synthetic local night-shift address log with tuple
         plus set: protect the 3-field shift record, deduplicate 20
         observations into 10 unique addresses, verify presence with
         in, and print an ordered report without any loop.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_groups.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your
      own.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no loops, no set comprehensions, no imports, no files, no network).
    - Only lists plus tuples and sets: tuple indexing and len(),
      set() conversion, len(), in, and sorted() for display.
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: list -> sealed record -> set -> membership ->
ordered report.
Homework chain: new shift data -> same grouping technique -> ordered
report, while the class exercise groups the day list. Groupings prove
nothing by themselves; they order human review of local practice
data. This report opens no ports, touches no disk, and contacts
nothing.
"""

# ==============================================================================
# STEP 1: Evidence (given). Twenty synthetic night-shift observations
# plus the sealed shift record.
# ==============================================================================
shift_ips = [
    "127.0.0.1", "127.0.0.10", "127.0.0.1", "192.0.2.50", "127.0.0.10",
    "::1", "127.0.0.11", "192.0.2.51", "127.0.0.1", "127.0.0.11",
    "192.0.2.50", "::1", "127.0.0.12", "192.0.2.52", "127.0.0.12",
    "127.0.0.1", "192.0.2.51", "::1", "127.0.0.13", "192.0.2.53",
]

# Sealed record of the shift (given, replace with your own data).
shift_record = ("Alex Mendez", "DEF-2026-09", 20)

# Identity of whose report this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Observaciones del turno: {len(shift_ips)}")

# ==============================================================================
# STEP 2: Grouping. One set conversion removes the 10 repetitions.
# ==============================================================================
# Deduplication: the set keeps one copy per value, with no order.
shift_unique = set(shift_ips)
print(f"Direcciones únicas del turno: {len(shift_unique)}")

# Ordering reuse Session 06: sorted() returns an ordered list of the
# unique addresses because the set itself has no order.
shift_ordered = sorted(shift_unique)

# Membership asks presence as text only: in connects to nothing.
shift_seen = "127.0.0.1" in shift_unique
print(f"Bucle local visto: {shift_seen}")

# An address never observed answers False without any error.
shift_missing = "10.9.9.9" in shift_unique
print(f"Desconocida vista: {shift_missing}")

# ==============================================================================
# STEP 3: Communication. Ordered report for whoever receives the shift.
# ==============================================================================
print("--- Parte del turno ---")
print(f"Nombre: {student_name}")
print(f"Total de observaciones: {len(shift_ips)}")
print(f"Únicas: {len(shift_unique)}")
print(f"Lista ordenada: {shift_ordered}")
