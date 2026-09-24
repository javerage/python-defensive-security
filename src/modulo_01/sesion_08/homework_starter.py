"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 08 (PyDefSec)
FILE: homework_starter.py (guided skeleton for shift_groups.py)
PURPOSE: Group one synthetic local night-shift address log with tuple
         plus set: protect the 3-field shift record, deduplicate 20
         observations into 10 unique addresses, verify presence with
         in, and print an ordered report without any loop.
NOTE: Homework after class, outside the 60 minutes. Create
      shift_groups.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; PENDING
      marks unfinished work, and replaced placeholders give the expected
      report. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as shift_groups.py plus run:
        python shift_groups.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting process safely.

BEFORE CODING, PREDICT (read the shift tables first, without running):
    - Predict what len(shift_ips) gives versus len(set(shift_ips)),
      and how many repetitions are removed; verify after running.
    - Which field does shift_record protect, and why does assigning
      to shift_record[0] interrupt the program?
    - What does "127.0.0.1" in shift_unique return versus
      "10.9.9.9" in shift_unique, and why does neither touch
      the network?

DELIVERY: explain aloud the chain list -> tuple -> set -> membership
-> report for the shift, why the list keeps 20 entries while the set
keeps 10 unique ones, and how each result reaches the report. Local
practice data only. The program organizes data for human review; it
opens no ports, touches no disk, and contacts nothing.
==============================================================================

Conceptual sequence: list -> sealed record -> set -> membership ->
ordered report.
Homework chain: new shift data -> same grouping technique -> ordered
report, while the class exercise groups the day list.
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
# STEP 2: Grouping (TODO). One set conversion, one ordering, explicit
# membership checks. No loops, no set comprehensions.
# ==============================================================================
# TODO 2.1: Deduplicate with set(shift_ips).
shift_unique = set()  # TODO: build it with set(shift_ips)

# TODO 2.2: print how many unique addresses the shift holds.
print("PENDING")  # TODO: print f"Direcciones únicas del turno: {len(shift_unique)}"

# TODO 2.3: Order the unique addresses with sorted(shift_unique)
# (given pattern: the set itself has no order).
shift_ordered = []  # TODO: build it with sorted(shift_unique)

# TODO 2.4: Check loopback presence with "127.0.0.1" in shift_unique
# and print it.
shift_seen = False  # TODO: build it with "127.0.0.1" in shift_unique
print("PENDING")  # TODO: print f"Bucle local visto: {shift_seen}"

# TODO 2.5: Check an absent address with "10.9.9.9" in shift_unique
# and print it.
shift_missing = False  # TODO: build it with "10.9.9.9" in shift_unique
print("PENDING")  # TODO: print f"Desconocida vista: {shift_missing}"

# ==============================================================================
# STEP 3: Communication (given). Ordered report for whoever receives
# the shift.
# ==============================================================================
print("--- Parte del turno ---")
print(f"Nombre: {student_name}")
print(f"Total de observaciones: {len(shift_ips)}")
print(f"Únicas: {len(shift_unique)}")
print(f"Lista ordenada: {shift_ordered}")
