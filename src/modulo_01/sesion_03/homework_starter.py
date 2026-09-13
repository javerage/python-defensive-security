"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 03 (PyDefSec)
FILE: homework_starter.py (guided skeleton for record_analysis.py)
PURPOSE: Review one synthetic local lab note and extract its basic parts:
         measure it, strip padding, read the first character, slice the
         fixed case code, normalize the note level, mask the practice
         operator alias, and check that the local reference tag
         LAB-LOCAL appears in the text.
NOTE: Homework after class, outside the 60 minutes. Create
      record_analysis.py manually in your Session 01 project. Complete
      each task marked TODO. This skeleton compiles plus runs; replaced
      placeholders give the expected summary. Check homework_solution.py
      only after trying alone.

STUDENT INSTRUCTIONS:
    Work in your Session 01 project folder (curso-python-defensivo),
    with .venv active. Save your work as record_analysis.py plus run:
        python record_analysis.py

    Terminal hygiene:
        - Look before jumping: dir (Windows) or ls (macOS/Linux) first.
        - Tab autocompletes file names. Up arrow recalls commands.
        - Ctrl + C cancels a waiting input prompt safely.

BEFORE CODING, ANALYZE (read the note first, without running code):
    - Which padding surrounds the note, and why would it corrupt a
      fixed-position slice?
    - Which fixed code opens the clean note, and how many characters
      does it use?
    - Which word travels between [ and ], and how is it shown uniformly?
    - Which practice alias must be masked, and which local reference tag
      must be searched?

DELIVERY: explain aloud why you strip before slicing, what each
operation reads, what the != -1 comparison produces, and how each
result reaches the summary. Local text only. No network use.
==============================================================================

Conceptual sequence: dirty text -> clean text -> extract ->
normalize -> report.
"""

# ==============================================================================
# STEP 1: Dirty input (given). One practice lab note with padding to clean.
# ==============================================================================
# The case code answers WHICH case it is; [info] answers with what level
# it was written; LAB-LOCAL-07 is a text reference tag of the local lab.
raw_lab_note = "   LAB-2026-041 [info] nota: revision de inventario local ref=LAB-LOCAL-07 operador=operador_temporal   \n"
raw_note_length = len(raw_lab_note)

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Cleaning (TODO). Padding would corrupt the case code slice.
# ==============================================================================
# TODO 2.1: Remove leading/trailing spaces and the final newline.
cleaned_note = ""  # TODO: replace "" with raw_lab_note.strip()

# TODO 2.2: Measure the clean copy.
cleaned_note_length = 0  # TODO: replace 0 with len(cleaned_note)

# ==============================================================================
# STEP 3: Extraction (TODO). Positions are zero-based; slices exclude the end.
# ==============================================================================
# TODO 3.1: Read the first character (confirms the padding is gone).
first_char = ""  # TODO: replace "" with cleaned_note[0]

# TODO 3.2: Slice the fixed 12-character case code (LAB-YYYY-NNN).
case_id = ""  # TODO: replace "" with cleaned_note[:12]

# TODO 3.3: Locate each bracket with find().
bracket_start = 0  # TODO: replace 0 with cleaned_note.find("[")
bracket_end = 0  # TODO: replace 0 with cleaned_note.find("]")

# TODO 3.4: Slice between the brackets and show the word uniformly.
note_level = ""  # TODO: replace "" with cleaned_note[bracket_start + 1:bracket_end].upper()

# ==============================================================================
# STEP 4: Masking and local reference (TODO). Only text search, no network.
# ==============================================================================
# TODO 4.1: Build a sanitized copy with the practice alias masked.
sanitized_note = ""  # TODO: replace "" with cleaned_note.replace("operador_temporal", "practicante_local")

# TODO 4.2: Locate the local reference tag (position, or -1 when absent).
marker_index = 0  # TODO: replace 0 with cleaned_note.find("LAB-LOCAL")

# TODO 4.3: Check whether the text contains the tag (True or False).
is_local_ref = False  # TODO: replace False with marker_index != -1

# TODO 4.4: Read exactly the 12 characters of "LAB-LOCAL-07" from its position.
reference_code = ""  # TODO: replace "" with cleaned_note[marker_index:marker_index + 12]

# ==============================================================================
# STEP 5: Communication (given). Simple readable console summary.
# ==============================================================================
print("--- Resumen de la nota ---")
print(f"Nombre: {student_name}")
print(f"Identificador: {student_id}")
print(f"Longitud cruda: {raw_note_length}")
print(f"Longitud limpia: {cleaned_note_length}")
print(f"Primer caracter: {first_char}")
print(f"Caso: {case_id}")
print(f"Nivel de nota: {note_level}")
print(f"Contiene referencia local: {is_local_ref}")
print(f"Codigo de referencia: {reference_code}")
print(f"Nota saneada: {sanitized_note}")
