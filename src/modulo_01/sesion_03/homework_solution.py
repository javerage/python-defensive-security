"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 03 (PyDefSec)
FILE: homework_solution.py (reference for analisis_registro.py)
PURPOSE: Review one synthetic local lab note and extract its basic parts:
         measure it, strip padding, read the first character, slice the
         fixed case code, normalize the note level, mask the practice
         operator alias, and check that the local reference tag
         LAB-LOCAL appears in the text.
NOTE: Homework after class, outside the 60 minutes. Create
      analisis_registro.py manually in your Session 01 project. Use this
      file only as backup guidance after attempting the task on your own.
PEDAGOGICAL RESTRICTIONS:
    - Strictly top-to-bottom sequential script (no functions, no try/except,
      no collections, no type hints, no main(), no conditionals).
    - English PEP 8 identifiers plus comments (style guidance, not graded).
    - Interaction texts in Spanish for the local user.
==============================================================================

Conceptual sequence: dirty text -> clean text -> extract ->
normalize -> report.
"""

# ==============================================================================
# STEP 1: Dirty input (given). One practice lab note with padding to clean.
# ==============================================================================
# The note describes a local inventory review. The case code answers WHICH
# case it is; [info] answers with what level it was written; LAB-LOCAL-07
# is a text reference tag of the local lab; operador_temporal is a practice
# operator alias.
raw_lab_note = "   LAB-2026-041 [info] nota: revision de inventario local ref=LAB-LOCAL-07 operador=operador_temporal   \n"
raw_note_length = len(raw_lab_note)

# Identity of whose summary this is (given, replace with your own data).
student_name = "Alex Mendez"
student_id = "DEF-2026-09"

# ==============================================================================
# STEP 2: Cleaning (each line answers one question about the same note).
# ==============================================================================
# Padding spaces and the final newline would corrupt the case code slice,
# so strip() produces a new clean copy (the original string is immutable).
cleaned_note = raw_lab_note.strip()
cleaned_note_length = len(cleaned_note)

# ==============================================================================
# STEP 3: Extraction. Positions are zero-based; slices exclude the end.
# ==============================================================================
# First character confirms the padding is gone (a space would mean dirty).
first_char = cleaned_note[0]

# The case code always opens the clean note with a fixed 12-character
# shape (LAB-YYYY-NNN), so [:12] isolates WHICH case the note belongs to.
case_id = cleaned_note[:12]

# The note level travels between [ and ]; find() locates each bracket and
# the slice between them isolates the word. upper() shows it uniformly.
bracket_start = cleaned_note.find("[")
bracket_end = cleaned_note.find("]")
note_level = cleaned_note[bracket_start + 1:bracket_end].upper()

# ==============================================================================
# STEP 4: Masking and local reference (no network use, only text search).
# ==============================================================================
# replace() builds a sanitized copy with the practice operator alias masked.
# The original cleaned_note is preserved; strings cannot change in place.
sanitized_note = cleaned_note.replace("operador_temporal", "practicante_local")

# find() returns the position of the reference tag, or -1 when absent.
# The comparison produces a bool: whether the text contains the tag.
# True only means the characters appear in this note; the program opens
# no connections and proves nothing about the network by itself.
marker_index = cleaned_note.find("LAB-LOCAL")
is_local_ref = marker_index != -1

# "LAB-LOCAL-07" is 12 characters long, so this slice reads exactly the tag.
reference_code = cleaned_note[marker_index:marker_index + 12]

# ==============================================================================
# STEP 5: Communication. Simple readable console summary.
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
