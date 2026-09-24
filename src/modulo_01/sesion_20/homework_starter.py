"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
CURRICULUM REPOSITORY: python-defensive-security | PyDefSec (PDS-40)
SESSION: 20 — Checkpoint 1 and Brief Defense (Closing Block A)
FILE: homework_starter.py (Take-home starter: Session 21 readiness)
PURPOSE: Guided template to prepare Session 21: read the ethical
         commitment and verify the local lab (venv plus mock ports).
SCOPE: Localhost authorized testing environment (127.0.0.1 / ::1) only.
==============================================================================
INSTRUCTIONS:
1. Complete each numbered STEP in sequential order (top-to-bottom).
2. Identifiers, variables, constants, and comments MUST be in English.
3. Keep all execution confined to localhost or local fixtures.
4. Test your script in terminal using: python homework_starter.py
5. Predict first: write your prediction (expected value + why) before
   completing each TODO, then run and compare (predict -> execute ->
   compare). TODO comments never contain answers. No argparse, no
   sockets, no subprocess, no shell, no network.
==============================================================================
"""

import os
import sys
from datetime import datetime

student_name = "Alex Mendez"  # Replace with your full name
student_id = "DEF-2026-09"    # Replace with your student ID
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# TODO: Step 1.1 - Confirm the ethical commitment reading for Session 21.
# Write which commitment text was read and on which date, in your words.
COMMITMENT_STATUS = "PENDING"

# TODO: Step 2.1 - Verify the local lab without touching the network.
# Report the Python version, whether the venv prefix is active, and the
# working folder name. Predict each value before running.
LAB_STATUS = "PENDING"

border = "+-----------------------------------------------------------------------------+"
print(border)
print("| SESSION 21 READINESS CHECK (STARTER)                                     |")
print(border)
print(f"| Operator Name           : {student_name:<49} |")
print(f"| Operator ID             : {student_id:<49} |")
print(f"| Timestamp               : {current_timestamp:<49} |")
print(f"| Target Scope            : {'127.0.0.1 (localhost loopback)':<49} |")
print(border)

# TODO: Step 3.1 - Print the readiness lines with aligned f-strings.
print(f"| Commitment Reading      : {COMMITMENT_STATUS:<49} |")
print(f"| Local Lab               : {LAB_STATUS:<49} |")

print(border)
print("| STATEMENT: Operation confined to localhost (127.0.0.1). Zero external network. |")
print(border)
