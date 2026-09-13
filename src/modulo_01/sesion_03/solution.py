"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 03 (PyDefSec)
FILE: solution.py (reference for log_normalizer.py)
PURPOSE: Clean one synthetic local log line and extract its basic parts:
         measure it, strip padding, read the first character, slice the
         timestamp, normalize the alert word, mask the practice username,
         and check that the local marker 127.0.0.1 appears in the text.
NOTE: The repository is only a backup. Students work in the project
      created in Session 01 (curso-python-defensivo) and create
      log_normalizer.py manually.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom sequential script (no functions, no try/except,
      no collections, no type hints, no main(), no conditionals).
    - 100% English PEP 8 identifiers and comments (consistency and
      collaboration standard, see README).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: dirty text -> clean text -> extract ->
normalize -> report.
"""

# ==============================================================================
# STEP 1: Dirty input (given). One practice log line with padding to clean.
# ==============================================================================
# The line describes a local practice event. The timestamp answers WHEN it
# happened; [warn] answers with what severity it was written; 127.0.0.1 is
# a text marker of the local machine; sec_admin is a practice username.
raw_log_entry = "   2026-09-10 11:15:32 [warn] AuthFailure ip=127.0.0.1 port=8080 user=sec_admin status=401   \n"
raw_length = len(raw_log_entry)

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Cleaning (each line answers one question about the same log).
# ==============================================================================
# Padding spaces and the final newline would corrupt the timestamp slice,
# so strip() produces a new clean copy (the original string is immutable).
cleaned_log = raw_log_entry.strip()
cleaned_length = len(cleaned_log)

# ==============================================================================
# STEP 3: Extraction. Positions are zero-based; slices exclude the end.
# ==============================================================================
# First character confirms the padding is gone (a space would mean dirty).
first_char = cleaned_log[0]

# The timestamp always opens the clean line with a fixed 19-character
# shape (YYYY-MM-DD HH:MM:SS), so [:19] isolates WHEN the event happened.
timestamp_str = cleaned_log[:19]

# The alert word travels between [ and ]; find() locates each bracket and
# the slice between them isolates the word. upper() shows it uniformly.
bracket_start = cleaned_log.find("[")
bracket_end = cleaned_log.find("]")
alert_level = cleaned_log[bracket_start + 1:bracket_end].upper()

# ==============================================================================
# STEP 4: Masking and local marker (no network use, only text search).
# ==============================================================================
# replace() builds a sanitized copy with the practice username masked.
# The original cleaned_log is preserved; strings cannot change in place.
sanitized_log = cleaned_log.replace("sec_admin", "analyst_sandbox")

# find() returns the position of the marker, or -1 when it is absent.
# The comparison produces a bool: whether the text contains the marker.
# True only means the characters appear in this line; the program opens
# no connections and proves nothing about the network by itself.
loopback_index = cleaned_log.find("127.0.0.1")
is_localhost = loopback_index != -1

# "127.0.0.1" is 9 characters long, so this slice reads exactly the marker.
target_ip = cleaned_log[loopback_index:loopback_index + 9]

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
