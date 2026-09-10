"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 01 (PyDefSec)
FILE: hola.py
PURPOSE: Baseline environment verification and local telemetry reporting.
SCOPE: Localhost authorized testing environment (127.0.0.1) only.
==============================================================================

INSTRUCTIONS FOR EXECUTION:
    1. Ensure your Python 3.13 virtual environment is created and activated:
       - Linux/macOS (Bash / Zsh):
           source .venv/bin/activate
       - Windows (PowerShell):
           .\\.venv\\Scripts\\Activate.ps1
       - Windows (Command Prompt):
           .\\.venv\\Scripts\\activate.bat
    2. Confirm prompt displays the '(.venv)' prefix.
    3. Run this script using:
           python hola.py
       or:
           python3 hola.py
"""

from datetime import datetime
import sys


def verify_python_version() -> bool:
    """Verify whether the active interpreter strictly satisfies the Python 3.13 baseline.

    Returns:
        bool: True if Python version starts with '3.13', False otherwise.
    """
    version_str: str = sys.version.split()[0]
    return version_str.startswith("3.13")


def main() -> None:
    """Execute local defensive environment verification and display audit telemetry."""
    # --- 1. OPERATOR METADATA ---
    # Replace these placeholders with your authorized student identity details
    student_name: str = "DEFENSIVE STUDENT"
    student_id: str = "DEF-2026-09"
    current_timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --- 2. PYTHON RUNTIME INSPECTION ---
    python_version: str = sys.version.split()[0]
    interpreter_path: str = sys.executable
    expected_version: str = "3.13.x"
    is_valid_version: bool = verify_python_version()

    # --- 3. FORMATTED AUDIT REPORT ---
    print("==================================================")
    print("[STATUS] LOCAL DEFENSIVE ENVIRONMENT INITIALIZATION")
    print("==================================================")
    print(f"Authorized Operator  : {student_name} (ID: {student_id})")
    print(f"Local Timestamp      : {current_timestamp}")
    print(f"Python Interpreter   : {python_version}")
    print(f"Executable Path      : {interpreter_path}")

    # Version approval verification
    if is_valid_version:
        print("Version Compliance   : [APPROVED: Active Python 3.13 standard]")
    else:
        print(f"Version Compliance   : [ALERT: Detected {python_version}, expected {expected_version}]")

    # Ethical confinement and scope declarations
    print("--------------------------------------------------")
    print("[DECLARATION] Exclusive operation on localhost and local fixtures.")
    if ".venv" in interpreter_path:
        print("[DECLARATION] Virtual environment verified and active.")
    else:
        print("[WARNING] Active interpreter does not reside within '.venv'.")
    print("==================================================")


if __name__ == "__main__":
    main()
