# Sesión 11: Funciones I para el verificador local

Bienvenido a la **Sesión 11** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **dividir el verificador en 3 funciones puras con `def`, `return` y docstring mínima, contar niveles sobre 20 eventos y mostrar el mismo resumen que la versión monolítica**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `check_helpers.py` y escribe el ejercicio.
4. Ejecuta `python check_helpers.py` y comprueba la verificación con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `check_helpers.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que volvió legible el verificador. Recibes un verificador monolítico de **20 eventos**: lo divides en `count_errors`, `decide_status` y `format_report`, cada una pura con su docstring, y verificas que la salida no cambia tras la división. En la Sesión 10 acumulaste con ciclos sueltos; hoy esas mismas líneas viven dentro de 3 funciones puras que se llaman en orden sobre los mismos 20 eventos.

## Secuencia conceptual

Cada verificación del programa sigue este orden explícito:

1. **Lista plana:** los 20 eventos con 6 `ERROR`.
2. **Contar:** `count_errors(event_log)` devuelve `6`.
3. **Decidir:** `decide_status(6)` devuelve `"Revisión prioritaria"`.
4. **Formatear:** `format_report(6, veredicto)` devuelve la línea final.
5. **Resumen verificado:** encabezado, conteo, veredicto y línea final.

## Cómo define Python sus funciones (en clase, sin evaluar nada más)

Cada función declara, documenta y devuelve:

```python
def count_errors(events):
    """Return how many ERROR entries the list holds."""
    total = events.count("ERROR")
    return total
```

Con los 20 eventos de la práctica, `count_errors(event_log)` devuelve `6`. La llamada entrega el argumento; el `return` devuelve el resultado.

Las tres funciones se encadenan por sus retornos:

```python
error_total = count_errors(event_log)
verdict = decide_status(error_total)
report_line = format_report(error_total, verdict)
```

Con `6` errores, `verdict` es `"Revisión prioritaria"` y `report_line` es `"Errores: 6 - Revisión prioritaria"`. Ninguna función imprime dentro: solo devuelven.

Tres precisiones y nada más:

- Parámetro frente a argumento: el parámetro es el hueco (`events`); el argumento es el valor (`event_log`). Si llamas sin el argumento, Python se interrumpe por falta de dato.
- Funciones de hoy, nada más: `def`, `return`, parámetros posicionales y docstring mínima. Sin ámbitos más allá de lo local, sin `*args`, sin valores por defecto (llegan en la Sesión 12).
- Alcance de hoy: 20 datos sintéticos con 6 `ERROR`. Las etiquetas son didácticas del laboratorio, no estándares universales. Funciones puras: mismo argumento, mismo retorno.

## Ruta principal: reutiliza tu proyecto de la sesión 01

### Windows (PowerShell)

```powershell
# 1. Localiza y abre tu proyecto de la sesión 01
cd curso-python-defensivo
dir

# 2. Activa el entorno virtual
.\.venv\Scripts\Activate.ps1

# 3. Verifica el intérprete (debe mostrar Python 3.13.x)
python --version

# 4. Crea manualmente el archivo nuevo para esta sesión
notepad check_helpers.py

# 5. Ejecuta tu ejercicio
python check_helpers.py
```

> Si PowerShell bloquea la activación, ejecuta primero `Set-ExecutionPolicy -Scope Process Bypass` y vuelve a activar.

### Linux (Bash)

```bash
# 1. Localiza y abre tu proyecto de la sesión 01
cd ~/curso-python-defensivo
ls

# 2. Activa el entorno virtual
source .venv/bin/activate

# 3. Verifica el intérprete (debe mostrar Python 3.13.x)
python3 --version

# 4. Crea manualmente el archivo nuevo para esta sesión
touch check_helpers.py

# 5. Ejecuta tu ejercicio
python3 check_helpers.py
```

### macOS (Zsh)

```bash
# 1. Localiza y abre tu proyecto de la sesión 01
cd ~/curso-python-defensivo
ls

# 2. Activa el entorno virtual
source .venv/bin/activate

# 3. Verifica el intérprete (debe mostrar Python 3.13.x)
python3 --version

# 4. Crea manualmente el archivo nuevo para esta sesión
touch check_helpers.py

# 5. Ejecuta tu ejercicio
python3 check_helpers.py
```

> Desarrollo local en macOS con `python3`. La validación final del laboratorio se realiza en Windows con `python`.

## Ruta breve de recuperación (si perdiste tu proyecto)

Si no tienes la carpeta de la sesión 01, reconstrúyela antes de empezar:

### Windows (PowerShell)

```powershell
mkdir curso-python-defensivo
cd curso-python-defensivo
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

### Linux (Bash)

```bash
mkdir -p ~/curso-python-defensivo
cd ~/curso-python-defensivo
python3.13 -m venv .venv
source .venv/bin/activate
python3 --version
```

### macOS (Zsh)

```bash
mkdir -p ~/curso-python-defensivo
cd ~/curso-python-defensivo
python3.13 -m venv .venv
source .venv/bin/activate
python3 --version
```

Debes ver el prefijo `(.venv)` en el prompt y la versión Python 3.13.x.

## Ejercicio obligatorio

Crea `check_helpers.py` con definiciones arriba, llamadas abajo e impresión solo al final (sin variables globales, sin `*args`, sin `imports`) que haga lo siguiente:

| Paso | Qué hace | Variables / funciones |
|------|----------|----------------------|
| 1. Evidencia | Asigna la lista de 20 más tu identidad e imprime el total (`20`) | `event_log` (20 textos, 6 `ERROR`), `student_name`, `student_id` |
| 2. División | Define las 3 funciones puras con su docstring y encadena sus retornos | `count_errors(events)` → `6`, `decide_status(total)` → veredicto, `format_report(total, verdict)` → línea; `error_total`, `verdict`, `report_line` |
| 3. Comunicación | Imprime el encabezado, el conteo, el veredicto y la línea final | Encabezado más conteo, veredicto y reporte |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y tablas de verificación (léelas antes de programar)

```python
event_log = [
    "INFO", "ERROR", "WARNING", "INFO", "ERROR",
    "INFO", "WARNING", "ERROR", "INFO", "WARNING",
    "INFO", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "ERROR", "INFO",
]
```

| Pieza | Recibe / devuelve | Aporte |
|-------|-------------------|--------|
| `count_errors(events)` | Recibe lista, devuelve `6` | Conteo verificado |
| `decide_status(total)` | Recibe número, devuelve veredicto (umbral 5) | Decisión en español |
| `format_report(total, verdict)` | Recibe dos datos, devuelve la línea | Comunicación lista |

Totales esperados: `6` errores, veredicto `"Revisión prioritaria"` (5 o más) y línea `"Errores: 6 - Revisión prioritaria"`. Con 4 o menos el veredicto sería `"Rutina local"`.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Eventos registrados: 20
Errores contados: 6
Verdicto: Revisión prioritaria
Reporte: Errores: 6 - Revisión prioritaria
--- Verificador por funciones ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Funciones: 3 puras con docstring
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: cuatro impresiones intermedias más un encabezado y tres líneas de datos.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El verificador **organiza el conteo local para la revisión**: conteo, veredicto y línea final con la misma salida que la versión monolítica. No abre puertos, no toca disco ni red y no confirma un incidente.

## Nota precisa sobre errores con funciones

Errores que verás en esta sesión:

- `TypeError: count_errors() missing 1 required positional argument: 'events'`: la llamada no entregó la lista y Python señala la llamada. Cada parámetro exige su argumento. La corrección es llamar con `count_errors(event_log)`: un argumento por cada parámetro.
- Imprimir en vez de devolver, en silencio (sin traza): con `print(events.count("ERROR"))` dentro, la función muestra `6` pero devuelve `None`, y la cadena se rompe porque el siguiente paso recibe `None`. La corrección es usar `return` dentro y dejar el único `print` para el final.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, funciones y comentarios) se escribe en inglés (`event_log`, `count_errors`, `decide_status`, `format_report`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué hace cada una de las 3 funciones (contar → `6`, decidir → veredicto, formatear → línea).
- [ ] Qué recibe y qué devuelve cada función sin mirar el cuerpo (lee sus docstrings).
- [ ] Qué distingue un parámetro (hueco `events`) de un argumento (valor `event_log`).
- [ ] Por qué cada función es pura (mismos argumentos, mismo resultado, sin imprimir dentro).
- [ ] Qué rompe imprimir en vez de devolver (`None` en el siguiente paso).
- [ ] Qué NO hace el programa (no abre puertos, no toca disco/red, no confirma un incidente).
- [ ] Tu programa se ejecuta sin errores y muestra las cuatro impresiones intermedias más el encabezado y las tres líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, lee cada docstring en voz alta y di qué recibe y qué devuelve cada función sin mirar el cuerpo. Es solo práctica extra: no cambia tu calificación y no usa sintaxis nueva. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`shift_helpers.py`), distinto del `check_helpers.py` de clase y del desafío opcional de arriba.

**Historia:** dejas listo el verificador del turno antes de entregarlo, distinto del verificador del día de clase. Partes de 20 eventos nuevos del turno, aplicas la misma técnica de 3 funciones puras, cuentas `WARNING` y muestras el reporte.

Crea manualmente `shift_helpers.py` en tu proyecto personal, con definiciones arriba, llamadas abajo y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / funciones |
|------|----------|----------------------|
| 1. Evidencia | Asigna los 20 del turno más tu identidad e imprime el total (`20`) | `shift_events` (20 textos, 7 `WARNING`), `student_name`, `student_id` |
| 2. División | Define las 3 funciones del turno con docstring y encadena retornos | `count_warnings(events)` → `7`, `decide_shift(total)` → veredicto, `format_shift(total, verdict)` → línea |
| 3. Comunicación | Reporte del turno para quien lo recibe | `print()` línea por línea |

Los 20 eventos del turno (escríbelos tal cual):

```python
shift_events = [
    "WARNING", "INFO", "WARNING", "ERROR", "INFO",
    "WARNING", "INFO", "WARNING", "ERROR", "INFO",
    "WARNING", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "ERROR", "INFO",
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Eventos del turno: 20
Avisos contados: 7
Verdicto: Revisión prioritaria
Reporte: Avisos: 7 - Revisión prioritaria
--- Verificador del turno ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Funciones: 3 puras con docstring
```

> Nota de respaldo: la guía del estudiante muestra explícitamente las tres primeras líneas del ejemplo; la línea de reporte y el bloque de resumen replican la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los conteos deben coincidir.

**Antes de programar, analiza:** cuántos `WARNING` hay a mano (espera `7`) y qué devuelve `count_warnings(shift_events)`; qué veredicto devuelve `decide_shift(7)` con el umbral 5 y por qué no cambia la regla de clase; qué línea exacta devuelve `format_shift` y dónde va el único bloque de `print`.

**Propósito real:** el verificador organiza el conteo local para la revisión: no abre puertos, no toca disco/red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena lista → contar → decidir → formatear para el turno. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
