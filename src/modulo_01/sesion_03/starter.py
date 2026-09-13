"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 03 (PyDefSec)
FILE: starter.py (guided skeleton for log_normalizer.py)
PURPOSE: Clean one synthetic local log line and extract its basic parts:
         measure it, strip padding, read the first character, slice the
         timestamp, normalize the alert word, mask the practice username,
         and check that the local marker 127.0.0.1 appears in the text.
NOTE: The repository is only a backup. Create log_normalizer.py manually
      in your Session 01 project and complete each task marked TODO.
      This skeleton compiles and runs; replaced placeholders give the
      expected summary.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as log_normalizer.py and run:
        python log_normalizer.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting input prompt safely.
==============================================================================

Conceptual sequence: dirty text -> clean text -> extract ->
normalize -> report.
"""

# ==============================================================================
# STEP 1: Dirty input (given). One practice log line with padding to clean.
# ==============================================================================
# The timestamp answers WHEN it happened; [warn] answers with what severity
# it was written; 127.0.0.1 is a text marker of the local machine.
raw_log_entry = "   2026-09-10 11:15:32 [warn] AuthFailure ip=127.0.0.1 port=8080 user=sec_admin status=401   \n"
raw_length = len(raw_log_entry)

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Cleaning (TODO). Padding would corrupt the timestamp slice.
# ==============================================================================
# TODO 2.1: Remove leading/trailing spaces and the final newline.
cleaned_log = ""  # TODO: replace "" with raw_log_entry.strip()

# TODO 2.2: Measure the clean copy.
cleaned_length = 0  # TODO: replace 0 with len(cleaned_log)

# ==============================================================================
# STEP 3: Extraction (TODO). Positions are zero-based; slices exclude the end.
# ==============================================================================
# TODO 3.1: Read the first character (confirms the padding is gone).
first_char = ""  # TODO: replace "" with cleaned_log[0]

# TODO 3.2: Slice the fixed 19-character timestamp (YYYY-MM-DD HH:MM:SS).
timestamp_str = ""  # TODO: replace "" with cleaned_log[:19]

# TODO 3.3: Locate each bracket with find().
bracket_start = 0  # TODO: replace 0 with cleaned_log.find("[")
bracket_end = 0  # TODO: replace 0 with cleaned_log.find("]")

# TODO 3.4: Slice between the brackets and show the word uniformly.
alert_level = ""  # TODO: replace "" with cleaned_log[bracket_start + 1:bracket_end].upper()

# ==============================================================================
# STEP 4: Masking and local marker (TODO). Only text search, no network use.
# ==============================================================================
# TODO 4.1: Build a sanitized copy with the practice username masked.
sanitized_log = ""  # TODO: replace "" with cleaned_log.replace("sec_admin", "analyst_sandbox")

# TODO 4.2: Locate the local marker (position, or -1 when absent).
loopback_index = 0  # TODO: replace 0 with cleaned_log.find("127.0.0.1")

# TODO 4.3: Check whether the text contains the marker (True or False).
is_localhost = False  # TODO: replace False with loopback_index != -1

# TODO 4.4: Read exactly the 9 characters of "127.0.0.1" from its position.
target_ip = ""  # TODO: replace "" with cleaned_log[loopback_index:loopback_index + 9]

# ==============================================================================
# STEP 5: Communication (given). Simple readable console summary.
# ==============================================================================
print("--- Resumen del registro ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Longitud cruda: {raw_length}")
print(f"Longitud limpia: {cleaned_length}")
print(f"Primer caracter: {first_char}")
print(f"Marca temporal: {timestamp_str}")
print(f"Nivel de alerta: {alert_level}")
print(f"Contiene marcador local: {is_localhost}")
print(f"IP local: {target_ip}")
print(f"Registro saneado: {sanitized_log}")
