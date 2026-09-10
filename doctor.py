#!/usr/bin/env python3
"""
Python for Defensive Security (PyDefSec) - Environment Doctor
Diagnostic tool to verify local lab prerequisites in 1-click.
No external dependencies required (Standard Library only).
"""

import os
import platform
import subprocess
import sys


class Colors:
    """ANSI color codes with safe Windows terminal fallback."""

    if sys.platform == "win32":
        # Enable ANSI support in modern Windows Terminal / PowerShell
        os.system("")

    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def check_python_version() -> tuple[bool, str, str]:
    """Verify that Python is 3.12 or newer, noting 3.13 certification."""
    major, minor, micro = sys.version_info[:3]
    version_str = f"{major}.{minor}.{micro}"

    if major == 3 and minor == 13:
        return (
            True,
            f"Python {version_str} (Certificado oficial para el curso)",
            f"{Colors.GREEN}[OK]{Colors.RESET}",
        )
    elif major == 3 and minor >= 12:
        return (
            True,
            f"Python {version_str} (Compatible con el curso; la versión recomendada es 3.13)",
            f"{Colors.YELLOW}[COMPATIBLE]{Colors.RESET}",
        )
    else:
        return (
            False,
            f"Python {version_str} (No soportado; se requiere Python 3.12 o 3.13)",
            f"{Colors.RED}[ACCION REQUERIDA]{Colors.RESET}",
        )


def check_virtual_environment() -> tuple[bool, str, str, str]:
    """Check if the active interpreter is running inside a virtual environment (.venv)."""
    is_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    exec_path = sys.executable

    if is_venv:
        return (
            True,
            f"Entorno virtual activo (.venv)",
            f"{Colors.GREEN}[OK]{Colors.RESET}",
            exec_path,
        )
    else:
        # Determine activation command based on OS
        if sys.platform == "win32":
            hint = ".venv\\Scripts\\Activate.ps1"
        else:
            hint = "source .venv/bin/activate"

        return (
            False,
            f"Ejecutando en Python global del sistema (NO estás dentro del venv)",
            f"{Colors.RED}[ACCION REQUERIDA]{Colors.RESET}",
            f"Ejecuta en tu terminal: {Colors.CYAN}{hint}{Colors.RESET}",
        )


def check_operating_environment() -> tuple[str, str, bool]:
    """Detect operating system and whether it is running inside WSL (Windows Subsystem for Linux)."""
    os_system = platform.system()
    os_release = platform.release()
    is_wsl = False

    if os_system == "Linux":
        if "microsoft" in os_release.lower() or "wsl" in os_release.lower():
            is_wsl = True
        elif os.path.exists("/proc/version"):
            try:
                with open("/proc/version", "r", encoding="utf-8") as f:
                    if "microsoft" in f.read().lower():
                        is_wsl = True
            except Exception:
                pass

    if is_wsl:
        desc = (
            f"Linux bajo WSL (Subsistema de Windows para Linux)\n"
            f"  {Colors.YELLOW}Nota:{Colors.RESET} Si deseabas usar Windows PowerShell nativo, asegúrate de no haber pulsado 'Abrir en WSL' en VS Code."
        )
        tag = f"{Colors.YELLOW}[AVISO WSL]{Colors.RESET}"
    elif os_system == "Windows":
        desc = f"Windows nativo ({os_release}) - Entorno ideal con PowerShell"
        tag = f"{Colors.GREEN}[OK]{Colors.RESET}"
    elif os_system == "Darwin":
        desc = f"macOS ({platform.mac_ver()[0]}) - Entorno Unix nativo (zsh)"
        tag = f"{Colors.GREEN}[OK]{Colors.RESET}"
    else:
        desc = f"Linux nativo ({os_release}) - Entorno Bash/Zsh"
        tag = f"{Colors.GREEN}[OK]{Colors.RESET}"

    return desc, tag, is_wsl


def check_powershell_execution_policy() -> tuple[bool | None, str, str]:
    """Check PowerShell execution policy on Windows hosts."""
    if sys.platform != "win32":
        return None, "No aplica (Sistema Unix / Linux / macOS)", "[N/A]"

    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", "Get-ExecutionPolicy"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        policy = proc.stdout.strip()
        if policy in ("RemoteSigned", "Unrestricted", "Bypass"):
            return (
                True,
                f"Política de ejecución: {policy} (Permite activar venv sin bloqueos)",
                f"{Colors.GREEN}[OK]{Colors.RESET}",
            )
        else:
            return (
                False,
                f"Política de ejecución: {policy} (Bloqueará la activación de scripts .ps1)",
                f"{Colors.RED}[ACCION REQUERIDA]{Colors.RESET}",
            )
    except Exception as e:
        return (
            None,
            f"No fue posible consultar ExecutionPolicy: {e}",
            f"{Colors.YELLOW}[ADVERTENCIA]{Colors.RESET}",
        )


def main() -> int:
    border = "=" * 70
    print(f"\n{Colors.BOLD}{border}{Colors.RESET}")
    print(
        f"{Colors.BOLD}{Colors.CYAN}  PyDefSec Doctor - Diagnóstico de Entorno de Laboratorio{Colors.RESET}"
    )
    print(f"{Colors.BOLD}{border}{Colors.RESET}\n")

    issues_count = 0

    # 1. OS & Environment
    os_desc, os_tag, is_wsl = check_operating_environment()
    print(f"1. Sistema Operativo     : {os_tag} {os_desc}")

    # 2. Python Version
    py_ok, py_desc, py_tag = check_python_version()
    print(f"2. Versión de Python     : {py_tag} {py_desc}")
    if not py_ok:
        issues_count += 1

    # 3. Virtual Environment
    venv_ok, venv_desc, venv_tag, venv_extra = check_virtual_environment()
    print(f"3. Entorno Virtual (venv): {venv_tag} {venv_desc}")
    if not venv_ok:
        issues_count += 1
        print(f"   -> Instrucción: {venv_extra}")
    else:
        print(f"   -> Ruta activa: {venv_extra}")

    # 4. Windows Execution Policy (if applicable)
    if sys.platform == "win32":
        ps_ok, ps_desc, ps_tag = check_powershell_execution_policy()
        print(f"4. Permisos PowerShell   : {ps_tag} {ps_desc}")
        if ps_ok is False:
            issues_count += 1
            print(
                f"   -> Para desbloquear, ejecuta en PowerShell:\n"
                f"      {Colors.CYAN}Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass{Colors.RESET}"
            )

    print(f"\n{border}")

    # Summary
    if issues_count == 0:
        print(
            f"{Colors.BOLD}{Colors.GREEN}  ¡EXCELENTE! Tu máquina cumple con todos los requisitos del curso.{Colors.RESET}"
        )
        print(
            f"  Puedes ejecutar tus scripts con tranquilidad: {Colors.CYAN}python src/modulo_01/sesion_01/hola.py{Colors.RESET}"
        )
        print(f"{border}\n")
        return 0
    else:
        print(
            f"{Colors.BOLD}{Colors.YELLOW}  Se detectaron {issues_count} observación(es) para resolver antes de la clase.{Colors.RESET}"
        )
        print(
            f"  Sigue las instrucciones marcadas arriba con {Colors.RED}[ACCION REQUERIDA]{Colors.RESET}."
        )
        print(f"{border}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
