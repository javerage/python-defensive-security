"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 02 (PyDefSec)
FILE: homework_starter.py (guided skeleton for access_analysis.py)
PURPOSE: Act as the analyst responsible for organizing initial
         observations for human review. Starting from a local practice
         alert, prepare a triage summary for the person reviewing the case.
         Local data only. No network use.
NOTE: Homework after class, outside the 60 minutes. Create access_analysis.py
      manually in your Session 01 project. Complete each task marked TODO.
      This skeleton compiles plus runs; replaced placeholders give the
      expected summary. Check homework_solution.py only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as access_analysis.py plus run:
        python access_analysis.py

    Test data: admin-local, 12, 3 (minutes above zero).
    Controlling zero plus other invalid entries belongs to a later session
    on error handling.

IMPORTANT: Thresholds >= 5 and >= 2.0 are independent teaching rules
chosen for practicing counting, division, and comparisons. They are not
universal standards, and they prove no attack. This report organizes
initial observations so the reviewer can decide whether to gather more
information or continue a human investigation. It blocks no account.
==============================================================================

Conceptual sequence: text input -> conversion -> calculation ->
decisions -> communication.
"""

# ==============================================================================
# STEP 1: Text input (given). input() ALWAYS returns str, even for digits.
# ==============================================================================
# An analyst organizes initial observations for human review, starting
# from a local practice alert, without connecting to systems.
# account_id identifies the case account; failed_attempts counts events;
# observation_minutes bounds the time window under review.
account_id = input("Escribe el identificador de la cuenta: ")
raw_failed_attempts = input("Escribe la cantidad de intentos fallidos: ")
raw_observation_minutes = input("Escribe los minutos observados: ")

# ==============================================================================
# STEP 2: Conversion (TODO). Text that already holds a number becomes a number.
# ==============================================================================
# TODO 2.1: Convert raw_failed_attempts to int (whole attempts).
failed_attempts = 0  # TODO: replace 0 with int(raw_failed_attempts)

# TODO 2.2: Convert raw_observation_minutes to float (minutes allow decimals).
observation_minutes = 1.0  # TODO: replace 1.0 with float(raw_observation_minutes)

# ==============================================================================
# STEP 3: Calculation (TODO). Division gives frequency (attempts per minute).
# Frequency matters: 12 attempts in 3 minutes is not the same pace as
# 12 attempts spread across a much larger window.
# ==============================================================================
# TODO 3: Divide attempts by minutes.
attempts_per_minute = 0.0  # TODO: replace 0.0 with failed_attempts / observation_minutes

# ==============================================================================
# STEP 4: Decisions (TODO). Each comparison checks one teaching rule and
# produces a bool (True or False). many_failed_attempts reflects volume;
# rapid_attempts reflects pace. True only means its rule was met.
# ==============================================================================
# TODO 4.1: Flag five or more failed attempts.
many_failed_attempts = False  # TODO: replace False with failed_attempts >= 5

# TODO 4.2: Flag frequency at or above 2.0 attempts per minute.
rapid_attempts = False  # TODO: replace False with attempts_per_minute >= 2.0

# ==============================================================================
# STEP 5: Communication (given). Simple readable triage summary.
# ==============================================================================
print("--- Resumen de triage ---")
print(f"Cuenta: {account_id}")
print(f"Intentos fallidos: {failed_attempts}")
print(f"Minutos observados: {observation_minutes}")
print(f"Intentos por minuto: {attempts_per_minute}")
print(f"Muchos intentos fallidos: {many_failed_attempts}")
print(f"Intentos rapidos: {rapid_attempts}")
