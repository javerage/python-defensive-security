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
    estudiante: str = "ESTUDIANTE DEFENSIVO"
    matricula_id: str = "DEF-2026-09"
    marca_tiempo: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --- 2. PYTHON RUNTIME INSPECTION ---
    python_version: str = sys.version.split()[0]
    executable_path: str = sys.executable
    is_version_approved: bool = verify_python_version()

    # --- 3. FORMATTED AUDIT REPORT ---
    print("==================================================")
    print("[ESTADO] INICIALIZACIÓN DE ENTORNO DEFENSIVO LOCAL")
    print("==================================================")
    print(f"Operador Autorizado : {estudiante} (ID: {matricula_id})")
    print(f"Timestamp Local     : {marca_tiempo}")
    print(f"Intérprete Python   : {python_version}")
    print(f"Ruta del Ejecutable : {executable_path}")

    # Version approval verification
    if is_version_approved:
        print("Conformidad Versión : [APROBADO: Estándar Python 3.13 activo]")
    else:
        print(f"Conformidad Versión : [ALERTA: Se detectó {python_version}, se requiere 3.13.x]")

    # Ethical confinement and scope declarations
    print("--------------------------------------------------")
    print("[DECLARACIÓN] Operación exclusiva en localhost y fixtures.")
    if ".venv" in executable_path:
        print("[DECLARACIÓN] El entorno virtual está verificado y activo.")
    else:
        print("[ADVERTENCIA] El intérprete activo no reside dentro de '.venv'.")
    print("==================================================")


if __name__ == "__main__":
    main()
