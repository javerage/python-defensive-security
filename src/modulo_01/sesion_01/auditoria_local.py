"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 01 (PyDefSec)
FILE: auditoria_local.py
PURPOSE: Starter template for the Autonomous Local Audit Challenge.
SCOPE: Localhost authorized testing environment (127.0.0.1) only.
==============================================================================

STUDENT INSTRUCTIONS:
    In this challenge, you will construct your first autonomous defensive audit tool.
    This script executes linearly (top-to-bottom).
    It does not require defining complex functions; the entire flow is processed step by step.

    Complete each section marked with '# TODO:' by updating test values
    with your authorized data or validating the acquired system telemetry.

    To execute this script inside your active virtual environment (.venv):
        python auditoria_local.py
    or from the repository root:
        python src/modulo_01/sesion_01/auditoria_local.py

    Verify that the terminal displays the formatted tabular report with the
    analyst identity, host telemetry, Python 3.13 compliance, and the
    localhost ethical confinement declaration.
"""

# ==============================================================================
# STANDARD LIBRARY MODULE IMPORTS
# ==============================================================================
# In Python, modules are reusable standard library packages.
#
# 'import sys' and 'import platform':
# Import the full module namespace. Access functions with dot notation
# (e.g., sys.version_info or platform.system()).
#
# 'from datetime import datetime':
# Imports only the 'datetime' class from the 'datetime' module. This allows
# direct access to datetime.now() rather than datetime.datetime.now().

import platform
import sys
from datetime import datetime

# ==============================================================================
# --- STEP 1: Responsible Analyst Identity ---
# ==============================================================================
# Assign string literals (type str) to variables documenting the authorized
# defensive security operator running this audit.
#
# TODO 1.1: Replace the text with your full name.
# TODO 1.2: Enter your student ID or institutional credential.
# TODO 1.3: Customize your defensive operational security role if desired.

student_name = "TRAINEE ANALYST"                  # TODO: Replace with your name
student_id = "DEF-2026-09"                       # TODO: Replace with your credential or ID
analyst_role = "Defensive Security Auditor L1"    # TODO: Adjust your assigned role

# ==============================================================================
# --- STEP 2: Host Machine Telemetry ---
# ==============================================================================
# In defensive cybersecurity, telemetry is the automated collection of system
# state and hardware/kernel attributes from the host machine.
#
# TODO 2.1: platform.system() returns the OS family (Linux, Darwin for macOS, Windows).
# TODO 2.2: platform.release() returns the specific OS kernel release version.
# TODO 2.3: platform.machine() returns the CPU architecture (x86_64, arm64, etc.).
# TODO 2.4: datetime.now().strftime(...) formats the active system clock timestamp.

os_name = platform.system()
os_release = platform.release()
os_architecture = platform.machine()
audit_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Combine operating system and CPU architecture into a single formatted string
system_info = f"{os_name} ({os_architecture})"

# ==============================================================================
# --- STEP 3: Python 3.13 Validation & Environment Isolation ---
# ==============================================================================
# A professional defensive workstation must certify interpreter baseline version
# and dependency isolation to guarantee reproducibility and prevent host OS drift.
#
# sys.version_info provides structured interpreter version metadata:
# - sys.version_info.major: Major version (must be 3)
# - sys.version_info.minor: Minor version (must be 13)
# - sys.version_info.micro: Patch release number (e.g., 0)

current_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
interpreter_path = sys.executable

# TODO 3.1: Evaluate whether the active interpreter satisfies Python 3.13.
#           The 'and' boolean operator requires both expressions to evaluate to True.
is_valid_version = sys.version_info.major == 3 and sys.version_info.minor == 13

# TODO 3.2: Evaluate version compliance status using conditional branching (if / else).
if is_valid_version:
    compliance_status = "[APPROVED: Active Python 3.13 standard]"
else:
    compliance_status = f"[FAIL: Unauthorized version ({current_version})]"

# TODO 3.3: Verify virtual environment isolation boundary.
#           Evaluate whether the '.venv' substring exists within the interpreter executable path.
is_venv_isolated = ".venv" in interpreter_path
if is_venv_isolated:
    isolation_status = "Isolated (.venv active)"
else:
    isolation_status = "WARNING: Outside .venv"

# ==============================================================================
# --- STEP 4: Formatted Terminal Report with f-strings ---
# ==============================================================================
# Display audit telemetry within a structured ASCII border.
# Python f-strings allow direct expression embedding.
# The format specifier {:<49} left-aligns text to a fixed width of 49 characters,
# maintaining vertical column alignment across standard terminals.
#
# TODO 4.1: Review the print() statements and execute the script to verify
#           that the tabular output prints cleanly with the localhost ethical scope.

horizontal_border = "+-----------------------------------------------------------------------------+"

print(horizontal_border)
print("| LOCAL DEFENSIVE ENVIRONMENT TELEMETRY & AUDIT REPORT                        |")
print(horizontal_border)
print(f"| Responsible Analyst     : {student_name:<49} |")
print(f"| Credential / Student ID : {student_id:<49} |")
print(f"| Technical Role          : {analyst_role:<49} |")
print(f"| Audit Timestamp         : {audit_timestamp:<49} |")
print(f"| Operating System        : {system_info:<49} |")
print(f"| Kernel Release          : {os_release:<49} |")
print(f"| Python Version          : {current_version:<49} |")
print(f"| Compliance Status       : {compliance_status:<49} |")
print(f"| Isolation Status        : {isolation_status:<49} |")
print(f"| Interpreter Path        : {interpreter_path:<49} |")
print(horizontal_border)
print("| DECLARATION: Operation confined to localhost (127.0.0.1). No external net.  |")
print(horizontal_border)
