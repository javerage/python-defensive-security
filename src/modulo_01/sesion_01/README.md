# Sesión 01: Entorno Reproducible y Telemetría Base

Bienvenido a la **Sesión 01** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Este directorio contiene el código fuente base y la plantilla del reto práctico para establecer y certificar una estación de trabajo defensiva verificada, aislada y reproducible en Python 3.13.

---

## Propósito del Código de esta Sesión

1. **`hola.py` (Verificación de Línea Base del Entorno)**:
   - Verifica que el intérprete activo cumpla estrictamente con la versión Python 3.13 (`verify_python_version()`).
   - Registra metadatos de identidad del operador (`student_name`, `student_id`, `current_timestamp`).
   - Inspecciona la ruta activa del ejecutable (`interpreter_path = sys.executable`) para confirmar el aislamiento en el entorno virtual (`.venv`).
   - Formaliza la declaración de ética defensiva: operaciones confinadas a `localhost` (`127.0.0.1`) y fixtures locales de prueba.

2. **`auditoria_local.py` (Plantilla del Reto Autónomo de Auditoría Local)**:
   - Estructura lineal y secuencial en 4 pasos (sin `def`, optimizada para aprendizaje incremental y fundamentos sólidos).
   - Recolecta telemetría del sistema operativo anfitrión (`os_name`, `os_release`, `os_architecture`, `system_info`) mediante los módulos de la biblioteca estándar `platform` y `datetime`.
   - Evalúa la versión de Python mediante expresiones booleanas estrictas (`is_valid_version`) y asigna el estado de conformidad (`compliance_status`).
   - Inspecciona la frontera de aislamiento del entorno virtual (`is_venv_isolated`, `isolation_status`).
   - Presenta un reporte tabular limpio y alineado en consola utilizando f-strings y formato ASCII (`horizontal_border`).

---

## Requisitos Previos

Antes de ejecutar cualquier script, asegúrese de cumplir con los siguientes requisitos:

- **Python 3.13.x** instalado en la máquina anfitriona (`python3.13 --version`).
- Un entorno virtual dedicado denominado `.venv` en la raíz del repositorio.
- El entorno virtual debe estar **activo** en la terminal actual (identificable por el prefijo `(.venv)` en el prompt).

---

## Guía Práctica: Cómo Ejecutar un Script de Python en la Vida Real

En ciberseguridad defensiva y desarrollo profesional, ejecutar scripts desde la terminal es una habilidad operativa diaria. El flujo de trabajo estándar en la línea de comandos consta de cuatro pasos esenciales:

### 1. Navegar entre directorios con `cd` (*Change Directory*)
Para ejecutar un archivo, la terminal debe saber en qué directorio se encuentra ubicado o usted debe navegar hacia él:
- **Verificar directorio actual**:
  - Linux / macOS: `pwd` (*Print Working Directory*)
  - Windows PowerShell: `Get-Location` (o simplemente `pwd`)
- **Moverse a la carpeta del script**:
  ```bash
  cd src/modulo_01/sesion_01
  ```
- **Retroceder un nivel hacia la carpeta superior**:
  ```bash
  cd ..
  ```
- **Volver a la raíz del proyecto**:
  ```bash
  cd ../../..
  ```

### 2. Verificar la presencia del archivo con `ls` o `dir`
Antes de invocar Python, compruebe visualmente que el archivo `.py` que desea ejecutar existe en el directorio de trabajo:
- **macOS / Linux**:
  ```bash
  ls -la
  ```
- **Windows (PowerShell / CMD)**:
  ```powershell
  dir
  ```
Debe observar archivos como `hola.py` y `auditoria_local.py` en la lista.

### 3. Invocar el intérprete de Python
Ejecute el script pasando el nombre del archivo al ejecutable de Python de su entorno virtual activo:
- **Estando dentro de `src/modulo_01/sesion_01/`**:
  ```bash
  python hola.py
  python auditoria_local.py
  ```
- **Estando en la raíz del repositorio (`python_to_ethical_hacking/`)**:
  ```bash
  python src/modulo_01/sesion_01/hola.py
  python src/modulo_01/sesion_01/auditoria_local.py
  ```

### 4. Atajos de productividad indispensables en la terminal
- **Autocompletado con la tecla `Tab`**:
  No escriba nombres largos manualmente. Escriba `python au` y presione la tecla `Tab`. La terminal autocompletará instantáneamente a `python auditoria_local.py`. Esto previene errores de dedo (*typos*) y acelera su flujo de trabajo.
- **Historial con teclas `Flecha Arriba` (↑) y `Flecha Abajo` (↓)**:
  Al modificar su código en el editor, no necesita volver a escribir el comando de ejecución. Presione la tecla `↑` para recuperar el último comando ejecutado y presione `Enter` para correrlo nuevamente.

---

## Inicialización del Entorno Virtual (.venv)

### macOS / Linux (Bash / Zsh)
```bash
# Crear el entorno virtual con Python 3.13 (si no existe):
python3.13 -m venv .venv

# Activar el entorno virtual:
source .venv/bin/activate

# Verificar versión activa:
python --version
# Salida esperada: Python 3.13.x
```

### Windows (PowerShell)
```powershell
# Crear el entorno virtual con Python 3.13 (si no existe):
py -3.13 -m venv .venv

# Activar el entorno virtual:
.\.venv\Scripts\Activate.ps1

# Verificar versión activa:
python --version
# Salida esperada: Python 3.13.x
```

### Windows (Símbolo del Sistema - cmd.exe)
```cmd
:: Crear el entorno virtual con Python 3.13 (si no existe):
py -3.13 -m venv .venv

:: Activar el entorno virtual:
.\.venv\Scripts\activate.bat

:: Verificar versión activa:
python --version
```

---

## Ejecución del Script de Verificación (`hola.py`)

Ejecute el script desde la raíz del proyecto:

```bash
python src/modulo_01/sesion_01/hola.py
```

### Salida esperada en terminal:
```text
==================================================
[STATUS] LOCAL DEFENSIVE ENVIRONMENT INITIALIZATION
==================================================
Authorized Operator  : DEFENSIVE STUDENT (ID: DEF-2026-09)
Local Timestamp      : 2026-09-10 10:46:41
Python Interpreter   : 3.13.15
Executable Path      : /Users/analista/python_to_ethical_hacking/.venv/bin/python
Version Compliance   : [APPROVED: Active Python 3.13 standard]
--------------------------------------------------
[DECLARATION] Exclusive operation on localhost and local fixtures.
[DECLARATION] Virtual environment verified and active.
==================================================
```

---

## Reto Autónomo: Auditoría Local (`auditoria_local.py`)

Abra `auditoria_local.py` en su editor de código. El archivo está estructurado de forma secuencial en 4 pasos lineales:

```python
# STEP 1: Responsible Analyst Identity
student_name = "TRAINEE ANALYST"
student_id = "DEF-2026-09"
analyst_role = "Defensive Security Auditor L1"

# STEP 2: Host Machine Telemetry
os_name = platform.system()
os_release = platform.release()
os_architecture = platform.machine()
audit_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
system_info = f"{os_name} ({os_architecture})"

# STEP 3: Python 3.13 Validation & Environment Isolation
current_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
interpreter_path = sys.executable

is_valid_version = sys.version_info.major == 3 and sys.version_info.minor == 13
if is_valid_version:
    compliance_status = "[APPROVED: Active Python 3.13 standard]"
else:
    compliance_status = f"[FAIL: Unauthorized version ({current_version})]"

is_venv_isolated = ".venv" in interpreter_path
if is_venv_isolated:
    isolation_status = "Isolated (.venv active)"
else:
    isolation_status = "WARNING: Outside .venv"

# STEP 4: Formatted Terminal Report with f-strings
horizontal_border = "+-----------------------------------------------------------------------------+"
```

### Ejecutar el reto:
```bash
python src/modulo_01/sesion_01/auditoria_local.py
```

### Salida esperada en terminal:
```text
+-----------------------------------------------------------------------------+
| LOCAL DEFENSIVE ENVIRONMENT TELEMETRY & AUDIT REPORT                        |
+-----------------------------------------------------------------------------+
| Responsible Analyst     : TRAINEE ANALYST                                   |
| Credential / Student ID : DEF-2026-09                                       |
| Technical Role          : Defensive Security Auditor L1                     |
| Audit Timestamp         : 2026-09-10 10:46:42                               |
| Operating System        : Darwin (arm64)                                    |
| Kernel Release          : 25.5.0                                            |
| Python Version          : 3.13.15                                           |
| Compliance Status       : [APPROVED: Active Python 3.13 standard]           |
| Isolation Status        : Isolated (.venv active)                           |
| Interpreter Path        : /Users/analista/python_to_ethical_hacking/.venv/bin/python |
+-----------------------------------------------------------------------------+
| DECLARATION: Operation confined to localhost (127.0.0.1). No external net.  |
+-----------------------------------------------------------------------------+
```

---

## Solución de Problemas Comunes (Troubleshooting)

### 1. Error de Directiva de Ejecución en Windows PowerShell
**Síntoma**:
```text
.\.venv\Scripts\Activate.ps1 : File cannot be loaded because running scripts is disabled on this system.
```
**Solución**:
Abra PowerShell y habilite la ejecución de scripts locales para su usuario:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Luego vuelva a activar el entorno virtual:
```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 2. Advertencia `WARNING: Outside .venv`
**Síntoma**:
El script corre, pero reporta que el intérprete activo es el intérprete global del sistema operativo y no el de `.venv`.
**Solución**:
1. Revise el prompt de su terminal. Si no muestra el prefijo `(.venv)`, active el entorno virtual.
2. Ejecute el comando de activación según su sistema operativo:
   - Linux / macOS: `source .venv/bin/activate`
   - Windows: `.\.venv\Scripts\Activate.ps1`
3. Verifique la ruta del binario activo con `which python` (macOS/Linux) o `Get-Command python` (PowerShell).

---

### 3. Falla `[FAIL: Unauthorized version]`
**Síntoma**:
El reporte indica una versión diferente a Python 3.13 (ej. Python 3.11, 3.12 o 3.14).
**Solución**:
1. Verifique las versiones de Python instaladas:
   - Linux / macOS: `which python3.13`
   - Windows: `py --list`
2. Si Python 3.13 está instalado, recree el entorno virtual apuntando explícitamente a dicho ejecutable:
   - Linux / macOS:
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

## Marco Ético y Alcance de Seguridad Defensiva

Conforme a las reglas de compromiso ético del laboratorio:
- **Cero operaciones en redes externas**: Los scripts consultan únicamente metadatos locales del sistema (`platform`, `sys`) y el reloj del sistema (`datetime`).
- **Alcance estricto en localhost**: Toda comunicación por sockets o peticiones en módulos posteriores operará exclusivamente en la dirección de bucle local (`127.0.0.1`).
- **Reproducibilidad y portabilidad**: El uso exclusivo de la biblioteca estándar de Python garantiza un comportamiento homogéneo en Windows, macOS y distribuciones de Linux sin dependencias externas.
