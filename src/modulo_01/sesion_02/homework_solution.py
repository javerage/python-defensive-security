"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 02 (PyDefSec)
FILE: homework_solution.py (reference for access_analysis.py)
PURPOSE: Act as the analyst responsible for organizing initial
         observations for human review. Starting from a local practice
         alert, prepare a triage summary for the person reviewing the case.
         Local data only. No network use.
NOTE: Homework after class, outside the 60 minutes. Create access_analysis.py
      manually in your Session 01 project. Use this file only as backup
      guidance after attempting the task on your own.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom sequential script (no functions, no try/except,
      no collections, no conditionals, no extra operators).
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: text input -> conversion -> calculation ->
decisions -> communication.

IMPORTANT: Thresholds >= 5 and >= 2.0 are independent teaching rules
chosen for practicing counting, division, and comparisons. They are not
universal standards, and they prove no attack. This report organizes
initial observations so the reviewer can decide whether to gather more
information or continue a human investigation. It blocks no account.
"""

# STEP 1: Text input. input() ALWAYS returns str, even for digits.
# account_id identifies the case account; failed_attempts counts events;
# observation_minutes bounds the time window under review.
account_id = input("Escribe el identificador de la cuenta: ")
raw_failed_attempts = input("Escribe la cantidad de intentos fallidos: ")
raw_observation_minutes = input("Escribe los minutos observados: ")

# STEP 2: Conversion. Text that already holds a number becomes a number.
failed_attempts = int(raw_failed_attempts)
observation_minutes = float(raw_observation_minutes)

# STEP 3: Calculation. Division gives frequency (attempts per minute).
# Frequency matters: 12 attempts in 3 minutes is not the same pace as
# 12 attempts spread across a much larger window.
attempts_per_minute = failed_attempts / observation_minutes

# STEP 4: Decisions. Each comparison checks one teaching rule and
# produces a bool (True or False). many_failed_attempts reflects volume;
# rapid_attempts reflects pace. True only means its rule was met.
many_failed_attempts = failed_attempts >= 5
rapid_attempts = attempts_per_minute >= 2.0

# STEP 5: Communication. Readable summary for the reviewer: account,
# data, frequency, plus both signals in one place.
print("--- Resumen de triage ---")
print(f"Cuenta: {account_id}")
print(f"Intentos fallidos: {failed_attempts}")
print(f"Minutos observados: {observation_minutes}")
print(f"Intentos por minuto: {attempts_per_minute}")
print(f"Muchos intentos fallidos: {many_failed_attempts}")
print(f"Intentos rapidos: {rapid_attempts}")
