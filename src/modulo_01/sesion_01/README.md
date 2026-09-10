# Session 01: Reproducible Environment & Baseline Telemetry

Welcome to **Session 01** of the *Python for Defensive Security: Fundamentals and Local Lab Tooling* curriculum.

This directory contains the baseline source code and practical challenge template for establishing a verified, isolated, reproducible Python 3.13 defensive workstation environment.

---

## Purpose of this Session's Code

1. **`hola.py` (Baseline Verification)**:
   - Verifies the local Python 3.13 runtime.
   - Captures operator metadata and local timestamp.
   - Inspects the active executable path (`sys.executable`) to verify virtual environment isolation.
   - Formalizes the defensive ethics declaration: operation is strictly confined to `localhost` (`127.0.0.1`) and local fixtures.

2. **`auditoria_local.py` (Autonomous Challenge Starter Template)**:
   - Serves as the starter skeleton for the student's hands-on challenge.
   - Demonstrates local operating system telemetry acquisition using `sys`, `platform`, and `datetime`.
   - Contains guided `# TODO:` tasks requiring the student to capture OS details, perform strict boolean version validation (`sys.version_info`), inspect the `.venv` boundary, and print an aligned tabular report using f-strings.
   - Includes safe default fallbacks so the script is runnable immediately out-of-the-box while clearly instructing the student on what to implement.

---

## Prerequisites

Before executing any script, ensure the following requirements are met:

- **Python 3.13.x** installed on the host machine (`python3.13 --version`).
- A dedicated virtual environment named `.venv` created inside your workspace root.
- The virtual environment must be **active** in your current shell session (indicated by the `(.venv)` prefix in your terminal prompt).

---

## Step-by-Step Setup & Execution Commands

### Step 1: Initialize and Activate the Virtual Environment

Navigate to the project directory and activate the virtual environment:

#### macOS / Linux (Bash / Zsh)
```bash
# If .venv does not exist yet:
python3.13 -m venv .venv

# Activate the virtual environment:
source .venv/bin/activate

# Verify Python version:
python --version
# Expected: Python 3.13.x
```

#### Windows (PowerShell)
```powershell
# If .venv does not exist yet:
py -3.13 -m venv .venv

# Activate the virtual environment:
.\.venv\Scripts\Activate.ps1

# Verify Python version:
python --version
# Expected: Python 3.13.x
```

#### Windows (Command Prompt - cmd.exe)
```cmd
:: If .venv does not exist yet:
py -3.13 -m venv .venv

:: Activate the virtual environment:
.\.venv\Scripts\activate.bat

:: Verify Python version:
python --version
```

---

### Step 2: Run the Baseline Script (`hola.py`)

Run the script from within the virtual environment:

```bash
python src/modulo_01/sesion_01/hola.py
```
*(Alternatively, navigate to `src/modulo_01/sesion_01/` and run `python hola.py`)*.

#### Expected Terminal Output:
```text
==================================================
[ESTADO] INICIALIZACIÓN DE ENTORNO DEFENSIVO LOCAL
==================================================
Operador Autorizado : ESTUDIANTE DEFENSIVO (ID: DEF-2026-09)
Timestamp Local     : 2026-09-10 10:15:32
Intérprete Python   : 3.13.0
Ruta del Ejecutable : /Users/analista/python_to_ethical_hacking/.venv/bin/python
Conformidad Versión : [APROBADO: Estándar Python 3.13 activo]
--------------------------------------------------
[DECLARACIÓN] Operación exclusiva en localhost y fixtures.
[DECLARACIÓN] El entorno virtual está verificado y activo.
==================================================
```

---

### Step 3: Complete and Run the Challenge Script (`auditoria_local.py`)

Open `auditoria_local.py` in your code editor. Locate each section marked with `# TODO:`:
1. Replace operator metadata (`estudiante`, `matricula_id`, `rol_defensivo`).
2. Confirm the host OS telemetry calls (`platform.system()`, `platform.release()`, `platform.machine()`).
3. Complete the boolean version condition (`sys.version_info.major == 3 and sys.version_info.minor == 13`).
4. Validate the venv isolation logic (`".venv" in sys.executable`).
5. Execute the script:

```bash
python src/modulo_01/sesion_01/auditoria_local.py
```

#### Expected Terminal Output:
```text
+-----------------------------------------------------------------------------+
| REPORTE DE TELEMETRÍA Y AUDITORÍA DE ENTORNO LOCAL DEFENSIVO                |
+-----------------------------------------------------------------------------+
| Analista Responsable    : CARLOS MENDOZA                                  |
| Credencial / ID         : DEF-2026-09                                     |
| Rol Técnico             : Auditor Defensivo Nivel 1                       |
| Timestamp de Auditoría  : 2026-09-10 10:20:15                             |
| Sistema Operativo       : Linux (x86_64)                                  |
| Versión Kernel          : 6.8.0-45-generic                                |
| Versión de Python       : 3.13.0                                          |
| Estado de Conformidad   : [APROBADO: Estándar Python 3.13 activo]         |
| Estado de Aislamiento   : Aislado (.venv activo)                          |
| Ruta del Ejecutable     : /home/analista/curso-python-defensivo/.venv/bin/python |
+-----------------------------------------------------------------------------+
| DECLARACIÓN: Operación confinada a localhost (127.0.0.1). Sin red externa.  |
+-----------------------------------------------------------------------------+
```

---

## Troubleshooting Common Issues

### Issue 1: Windows PowerShell Execution Policy Error
**Symptom**:
```text
.\.venv\Scripts\Activate.ps1 : File cannot be loaded because running scripts is disabled on this system.
```
**Remedy**:
Open PowerShell for your user account and update the execution policy to allow local scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then retry activating the virtual environment:
```powershell
.\.venv\Scripts\Activate.ps1
```

---

### Issue 2: Script Reports `[ADVERTENCIA] El intérprete activo no reside dentro de '.venv'`
**Symptom**:
The script executes, but reports that the active Python executable is the global or system interpreter rather than `.venv`.
**Remedy**:
1. Check your terminal prompt. If it does not start with `(.venv)`, your virtual environment is not active.
2. Run the activation script for your OS:
   - Linux/macOS: `source .venv/bin/activate`
   - Windows: `.\.venv\Scripts\Activate.ps1`
3. Verify the path with `which python` (Linux/macOS) or `Get-Command python` (PowerShell).

---

### Issue 3: `[FALLO: Versión no autorizada]` / Wrong Python Version
**Symptom**:
The audit reports a version other than Python 3.13 (e.g., Python 3.11, 3.12, or 3.14).
**Remedy**:
1. Check available Python installations:
   - Windows: `py --list`
   - Linux/macOS: `which python3.13`
2. If Python 3.13 is installed, recreate your virtual environment specifying the Python 3.13 binary:
   - Linux/macOS:
     ```bash
     rm -rf .venv
     python3.13 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows:
     ```powershell
     Remove-Item -Recurse -Force .venv
     py -3.13 -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

---

## Security & Ethics Baseline

In accordance with defensive cybersecurity lab standards:
- **No external network operations**: These scripts strictly query local host metadata (`platform`, `sys`) and standard system clocks.
- **Localhost scope**: All networking in subsequent modules will strictly bind to `127.0.0.1`.
- **Reproducibility**: Standard library modules ensure identical operational behavior across Windows, macOS, and Linux without third-party dependencies.
