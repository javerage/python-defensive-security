"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 08 (PyDefSec)
FILE: starter.py (guided skeleton for event_groups.py)
PURPOSE: Group 20 synthetic local address observations: protect the
         analyst record in an immutable tuple, deduplicate the list
         into a set of 11 unique addresses, and classify 7 loopback
         versus 4 documentation addresses with membership checks,
         printing an ordered report without any loop.
NOTE: The repository is only a backup. Create event_groups.py
      manually in your Session 01 project and complete each task marked
      TODO. This skeleton compiles and runs; PENDING marks unfinished
      work, and replaced placeholders give the expected report.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as event_groups.py and run:
        python event_groups.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

    Read the address tables in your student material first: they hold
    the 20 observations and the expected totals (11 unique, 7 local,
    4 documentation). No part of this skeleton shows the final counts.

WHY NO LOOP HERE: loops arrive in Session 09. Until then the set is
    built with one set() conversion and each check is one explicit
    line so every step stays visible.
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
# replace with your own data).
analyst_record = ("Alex Mendez", "DEF-2026-09", 20)

# Identity of whose report this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

print(f"Observaciones registradas: {len(event_ips)}")

# ==============================================================================
# STEP 2: Grouping (TODO). One set conversion, one ordering, explicit
# membership checks. No loops, no set comprehensions.
# ==============================================================================
# TODO 2.1: Deduplicate with set(event_ips) (expect 11 unique).
unique_ips = set()  # TODO: build it with set(event_ips)

# TODO 2.2: print how many unique addresses the set holds (expect 11).
print("PENDING")  # TODO: print f"Direcciones únicas: {len(unique_ips)}"

# TODO 2.3: Order the unique addresses with sorted(unique_ips)
# (given pattern: the set itself has no order).
ordered_ips = []  # TODO: build it with sorted(unique_ips)

# TODO 2.4: Check loopback presence with "127.0.0.1" in unique_ips
# (expect True) and print it.
loopback_seen = False  # TODO: build it with "127.0.0.1" in unique_ips
print("PENDING")  # TODO: print f"Bucle local visto: {loopback_seen}"

# TODO 2.5: Check an absent address with "10.9.9.9" in unique_ips
# (expect False) and print it.
missing_seen = False  # TODO: build it with "10.9.9.9" in unique_ips
print("PENDING")  # TODO: print f"Desconocida vista: {missing_seen}"

# TODO 2.6: Count the 7 loopback addresses with explicit membership
# checks (127.0.0.1, 127.0.0.2, 127.0.0.53, ::1, 127.0.0.3,
# 127.0.0.4, 127.0.0.5) and print the total (expect 7).
local_count = 0  # TODO: add one int(... in unique_ips) per address
print("PENDING")  # TODO: print f"Locales: {local_count}"

# TODO 2.7: Count the 4 documentation addresses with explicit
# membership checks (192.0.2.10, 192.0.2.20, 192.0.2.30,
# 192.0.2.40) and print the total (expect 4).
doc_count = 0  # TODO: add one int(... in unique_ips) per address
print("PENDING")  # TODO: print f"Documentales: {doc_count}"

# ==============================================================================
# STEP 3: Communication (given). Ordered report for the reviewer.
# ==============================================================================
print("--- Parte de direcciones ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Total de observaciones: {len(event_ips)}")
print(f"Únicas: {len(unique_ips)}")
print(f"Lista ordenada: {ordered_ips}")
