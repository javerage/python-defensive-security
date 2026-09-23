"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 08 (PyDefSec)
FILE: solution.py (reference for event_groups.py)
PURPOSE: Group 20 synthetic local address observations: protect the
         analyst record in an immutable tuple, deduplicate the list
         into a set of 11 unique addresses, and classify 7 loopback
         versus 4 documentation addresses with membership checks,
         printing an ordered report without any loop.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      event_groups.py manually.
WHY NO LOOP HERE: loops arrive in Session 09. Until then the set is
      built with one set() conversion and each check is one explicit
      line. Same groups a loop would produce, spelled out so every
      step stays visible.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom linear script (no functions, no try/except,
      no loops, no set comprehensions, no imports, no files, no network).
    - Only lists plus new tuples and sets: tuple indexing and len(),
      set() conversion, len(), in, and sorted() for display.
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: list (order plus duplicates) -> tuple (sealed
record) -> set (one copy per value) -> membership -> ordered report.
A list keeps all 20 entries; a set keeps the 11 unique ones.
"""

# ==============================================================================
# STEP 1: Evidence (given). Twenty synthetic local address observations
# plus the sealed analyst record.
# ==============================================================================
event_ips = [
    "127.0.0.1", "127.0.0.2", "127.0.0.1", "192.0.2.10", "127.0.0.53",
    "::1", "127.0.0.2", "192.0.2.20", "127.0.0.1", "127.0.0.3",
    "192.0.2.10", "::1", "127.0.0.53", "192.0.2.30", "127.0.0.4",
    "127.0.0.1", "192.0.2.20", "::1", "127.0.0.5", "192.0.2.40",
]

# Sealed record: three fields, read-only with an index (given,
# replace with your own data). Assigning to analyst_record[0] would
# raise TypeError because the tuple is immutable.
analyst_record = ("Alex Mendez", "DEF-2026-09", 20)

# Identity of whose report this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Observaciones registradas: {len(event_ips)}")

# ==============================================================================
# STEP 2: Grouping. One set conversion removes the 9 repetitions;
# loops arrive in Session 09 and would compress the explicit checks.
# ==============================================================================
# Deduplication: the set keeps one copy per value, with no order.
unique_ips = set(event_ips)
print(f"Direcciones únicas: {len(unique_ips)}")

# Ordering reuse Session 06: sorted() returns an ordered list of the
# unique addresses because the set itself has no order.
ordered_ips = sorted(unique_ips)

# Membership asks presence as text only: in connects to nothing.
loopback_seen = "127.0.0.1" in unique_ips
print(f"Bucle local visto: {loopback_seen}")

# An address never observed answers False without any error.
missing_seen = "10.9.9.9" in unique_ips
print(f"Desconocida vista: {missing_seen}")

# Classification with explicit membership checks: each int(... in ...)
# is 1 when present and 0 when absent; the sum is the group total.
# Loopback group of this lab (teaching rule): 127.0.0.0/8 plus ::1.
local_count = (
    int("127.0.0.1" in unique_ips)
    + int("127.0.0.2" in unique_ips)
    + int("127.0.0.53" in unique_ips)
    + int("::1" in unique_ips)
    + int("127.0.0.3" in unique_ips)
    + int("127.0.0.4" in unique_ips)
    + int("127.0.0.5" in unique_ips)
)
print(f"Locales: {local_count}")

# Documentation group of this lab (teaching rule): TEST-NET-1
# addresses 192.0.2.0/24, classified as text, never contacted.
doc_count = (
    int("192.0.2.10" in unique_ips)
    + int("192.0.2.20" in unique_ips)
    + int("192.0.2.30" in unique_ips)
    + int("192.0.2.40" in unique_ips)
)
print(f"Documentales: {doc_count}")

# ==============================================================================
# STEP 3: Communication (given). Ordered report for the reviewer.
# Counts prove nothing by themselves; they order human review of local
# practice data. The program opens no ports, touches no disk,
# and contacts nothing.
# ==============================================================================
print("--- Parte de direcciones ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total de observaciones: {len(event_ips)}")
print(f"Únicas: {len(unique_ips)}")
print(f"Lista ordenada: {ordered_ips}")
