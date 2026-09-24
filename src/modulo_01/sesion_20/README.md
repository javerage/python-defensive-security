# Sesión 20: Checkpoint 1 y defensa breve (cierra Bloque A)
### Course: *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`)

Este directorio contiene los archivos fuente base y la plantilla del reto práctico para la **Sesión 20** del currículo PyDefSec.

Al terminar la sesión podrás **defender en 3 minutos tu analizador de la Sesión 19, explicar dos decisiones de diseño y corregir en vivo el borde asignado, cerrando el Checkpoint 1 con acta firmada y el Bloque A 20/20**.

> Pi es SOLO revisor breve en esta sesión (máximo 10 minutos): predice primero, revisa cada sugerencia del diff, explica si la aceptas o no y reflexiona por escrito. Existe ruta completa sin Pi con revisión docente equivalente.

## Estructura de Archivos en esta Sesión

| Archivo | Propósito Operativo | Perfil de Uso |
| :--- | :--- | :--- |
| **`starter.py`** | Plantilla guiada con comentarios `# TODO` en 4 pasos para la defensa breve (cifras, 2 decisiones, borde). | Estudiante |
| **`solution.py`** | Solución de referencia canónica con identificadores 100% en inglés bajo PEP 8. | Docente / Autoevaluación |
| **`test_defensa.py`** | Suite de 6 pruebas `unittest` que verifica la defensa: analizador + borde corregido. | Estudiante / Docente |
| **`homework_starter.py`** | Plantilla de la tarea: lectura del compromiso ético S21 + verificación del laboratorio. | Estudiante |
| **`homework_solution.py`** | Referencia de la tarea: chequeo de alistamiento S21 (solo lectura local, sin red). | Docente / Autoevaluación |
| **`fixtures/`** *(opcional)* | Archivos sintéticos locales de prueba (logs, JSON, CSV) de solo lectura. | Estudiante / Docente |

---

## Requisitos Previos de Ejecución

Antes de ejecutar cualquier script, asegúrese de cumplir las siguientes condiciones operativas en su estación de trabajo:

1. **Python 3.13 instalado localmente:**
   - Comprobar versión: `python --version` (debe retornar `Python 3.13.x`).
2. **Entorno virtual (`.venv`) activado:**
   - El prompt de la terminal debe mostrar el prefijo `(.venv)`.
3. **Ubicación en el directorio del proyecto:**
   - Estar posicionado en la carpeta de trabajo `curso-python-defensivo/`.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

---

## Higiene Operativa de Terminal ("Mirar antes de saltar")

En la práctica profesional de ciberseguridad, los analistas ejecutan sus herramientas directamente desde la interfaz de línea de comandos (CLI). Adopte estos cuatro hábitos fundamentales:

1. **Verificar la presencia de archivos antes de ejecutar:**
   - En Windows: ejecute `dir`.
   - En macOS / Linux: ejecute `ls -la`.
   - Confirme que el archivo que desea ejecutar aparece físicamente en la lista de la pantalla.

2. **Autocompletar nombres con la tecla `Tab`:**
   - Escriba `python st` y presione la tecla **`Tab`**. La terminal autocompletará a `python starter.py`.
   - Si al presionar `Tab` no se completa nada, verifique si está en la carpeta correcta o si cometió un error tipográfico.

3. **Recuperar comandos previos con la Flecha Arriba (`↑`):**
   - No vuelva a tipear el comando desde cero tras guardar cambios en su editor. Presione **`↑`** para recuperar la última instrucción y pulse `Enter`.

4. **Abortar procesos colgados con `Ctrl + C`:**
   - Si su script entra en un bucle imprevisto o espera una entrada que no llega, presione **`Ctrl + C`** para forzar la detención inmediata del proceso.

---

## Guía de Ejecución Multiplataforma

### 1. Windows (PowerShell)

```powershell
# 1. Navegar a la carpeta del curso
cd curso-python-defensivo

# 2. Habilitar ejecución en la sesión actual (si PowerShell bloquea scripts)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 3. Activar el entorno virtual
.\.venv\Scripts\Activate.ps1

# 4. Verificar que el prompt muestre (.venv) y comprobar archivos
dir

# 5. Ejecutar la defensa y su suite
python defensa.py
python -m unittest test_defensa.py -v
```

### 2. macOS (Zsh / Terminal)

```bash
# 1. Navegar a la carpeta del curso
cd ~/curso-python-defensivo

# 2. Activar el entorno virtual
source .venv/bin/activate

# 3. Verificar que el prompt muestre (.venv) y comprobar archivos
ls -la

# 4. Ejecutar la defensa y su suite
python3 defensa.py
python3 -m unittest test_defensa.py -v
```

### 3. Linux (Bash / Ubuntu / Debian)

```bash
# 1. Navegar a la carpeta del curso
cd ~/curso-python-defensivo

# 2. Activar el entorno virtual
source .venv/bin/activate

# 3. Verificar que el prompt muestre (.venv) y comprobar archivos
ls -la

# 4. Ejecutar la defensa y su suite
python3 defensa.py
python3 -m unittest test_defensa.py -v
```

> En el respaldo del repositorio los archivos se llaman `solution.py` (defensa de referencia) y `starter.py` (plantilla). En tu proyecto de la Sesión 01 guarda tu defensa como `defensa.py` junto a `test_defensa.py` y ejecútalos desde la raíz.

---

## Salida Esperada en Consola (Verificación de Éxito)

Al ejecutar correctamente la defensa (`python defensa.py` o `python solution.py`), la consola debe generar exactamente estas líneas (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Defensa Checkpoint 1 — Bloque A (20/20)
Operador: Alex Mendez (DEF-2026-09)
Decision 1: frontera primero (todo dict cruza Finding antes de contar)
Decision 2: rechazo con posicion (cada fila rota viaja con su motivo)
Conteo por nivel: INFO=7 WARNING=4 ERROR=6
Eventos: 20 crudos -> 17 aceptados + 3 rechazados
Errores (aceptados): 6 - Revision prioritaria
Borde asignado: texto "31" -> 31 (strict en verde)
Acta de defensa: APROBADA — Checkpoint 1 cerrado, Bloque A 20/20
--- Reporte del checkpoint ---
+-----------------------------------------------------------------------------+
| DEFENSIVE AUDIT REPORT — SESSION 19                                         |
+-----------------------------------------------------------------------------+
| Operator Name           : Alex Mendez                                       |
| Operator ID             : DEF-2026-09                                       |
| Audit Stamp             : 2026-09-24 10:00:00                               |
| Target Scope            : 127.0.0.1 (localhost loopback)                    |
+-----------------------------------------------------------------------------+
| Raw Events              : 20                                                |
| Accepted Findings       : 17                                                |
| Rejected Rows           : 3                                                 |
| Count INFO              : 7                                                 |
| Count WARNING           : 4                                                 |
| Count ERROR             : 6                                                 |
| Threshold (ERROR)       : 5                                                 |
| Verdict                 : Revision prioritaria                              |
+-----------------------------------------------------------------------------+
| STATEMENT: Operation confined to localhost (127.0.0.1). Zero external net.  |
+-----------------------------------------------------------------------------+
```

Y la suite debe responder así (el tiempo exacto varía por equipo; lo que debe coincidir es `6 tests` y `OK`):

```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Convención de predicción previa: antes de completar cada TODO, el estudiante escribe su predicción (valor esperado y motivo); solo después de ejecutar el script compara el resultado obtenido con su predicción y con la salida esperada (predecir → ejecutar → comparar).

---

## Declaración de Confinamiento Ético

> **REGLA DE ORO DEFENSIVA:**
> Toda la lógica implementada en este directorio opera de forma **estrictamente local** contra `localhost` (`127.0.0.1` / `::1`) o sobre archivos sintéticos provistos como fixtures. Queda absolutamente prohibido realizar peticiones, escaneos o envíos de paquetes hacia redes externas, puertas de enlace o equipos ajenos.
