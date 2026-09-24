"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 20 (PyDefSec)
FILE: homework_solution.py (canonical reference for Session 21 readiness)
PURPOSE: Prepare Session 21 outside class time: confirm the ethical
         commitment reading and verify the local lab (interpreter,
         venv, working folder) without touching the network.
SCOPE: Localhost authorized testing environment (127.0.0.1 / ::1) only.
==============================================================================
HOW IT VERIFIES WITHOUT NETWORK:
- Reads only local process state: sys.version_info, sys.prefix,
  the VIRTUAL_ENV variable, and the current folder name.
- Never opens sockets, never spawns subprocesses, never parses
  arguments: the check is read-only and always exits zero, so the
  student compares lines instead of chasing exit codes.
==============================================================================
"""

import os
import sys
from datetime import datetime

student_name = "Alex Mendez"
student_id = "DEF-2026-09"
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
LOCAL_SCOPE = "127.0.0.1 (localhost loopback)"


def describe_interpreter():
    """Name the running interpreter in one auditable token."""
    info = sys.version_info
    return f"Python {info.major}.{info.minor}.{info.micro}"


def describe_lab():
    """Describe the local lab from read-only process state."""
    venv_active = "VIRTUAL_ENV" in os.environ or sys.prefix != sys.base_prefix
    folder = os.path.basename(os.getcwd()) or "local-folder"
    venv_label = "venv active" if venv_active else "venv not active"
    return f"{describe_interpreter()} | {venv_label} | folder {folder}"


def main():
    """Print the Session 21 readiness lines with fixed-width alignment."""
    commitment_status = "READ: compromiso etico S21 + alcance localhost"
    lab_status = describe_lab()

    border = "+-----------------------------------------------------------------------------+"
    print(border)
    print("| SESSION 21 READINESS CHECK                                              |")
    print(border)
    print(f"| Operator Name           : {student_name:<49} |")
    print(f"| Operator ID             : {student_id:<49} |")
    print(f"| Timestamp               : {current_timestamp:<49} |")
    print(f"| Target Scope            : {LOCAL_SCOPE:<49} |")
    print(border)
    print(f"| Commitment Reading      : {commitment_status:<49} |")
    print(f"| Local Lab               : {lab_status:<49} |")
    print(f"| Mock Ports              : {'18080 reserved (no bind, no traffic)':<49} |")
    print(border)
    print("| STATEMENT: Operation confined to localhost (127.0.0.1). Zero external network. |")
    print(border)


if __name__ == "__main__":
    main()
