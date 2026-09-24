# Sesión 13: Errores, excepciones y depuración del revisor local

Bienvenido a la **Sesión 13** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **envolver cada revisión en `try/except/else/finally`, crear una excepción propia de validación y registrar cada captura en un archivo de bitácora sin filtrar trazas crudas al usuario**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `harden_review.py` y escribe el ejercicio.
4. Ejecuta `python harden_review.py` y comprueba la revisión endurecida con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

15 min encuadre y guardia `try/except/else/finally` · 10 min demo en vivo con bitácora · 25 min práctica con `harden_review.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que entrega número y letrero juntos sin que nada interrumpa el cambio de turno. Recibes **20 eventos**, un umbral de 5 y **3 revisiones heredadas** de la Sesión 12: envuelves cada una en su propio bloque vigilado, capturas la fuente faltante y el nivel desconocido, y cada captura viaja a `defense.log` mientras cada veredicto viaja a la consola. En la Sesión 12 el dato perfecto bastaba; hoy el dato imperfecto también entrega reporte.

## Secuencia conceptual

Cada revisión endurecida del programa sigue este orden explícito:

1. **Evidencia:** `REVIEW_THRESHOLD = 5`, `event_log` (20 textos) y bitácora `defense.log`.
2. **Guardia por tarea:** `safe_review(source, level)` con `try/except/else/finally` → (`6`, prioritaria) para `ERROR`.
3. **Segunda guardia:** misma técnica con `"WARNING"` → (`5`, prioritaria).
4. **Tercera guardia:** fuente `missing_source` capturada como `FileNotFoundError` → (`0`, rutina).
5. **Reporte con bitácora:** pares en consola y capturas en `defense.log`.

## Cómo vigila Python (en clase, sin evaluar nada más)

El bloque vigilado separa el intento del remedio:

```python
def safe_review(source_name, level):
    """Guard one inherited review."""
    try:
        events = load_source(source_name)
        clean_level = validate_level(level)
        total, verdict = review_events(events, level=clean_level)
    except FileNotFoundError as exc:
        logging.warning(f"captured missing source: {exc}")
        total, verdict = 0, "Rutina local"
    except ReviewLevelError as exc:
        logging.warning(f"captured invalid level: {exc}")
        total, verdict = 0, "Rutina local"
    else:
        logging.info(f"reviewed {source_name} level {clean_level}: {total}")
    finally:
        logging.info(f"finished task for {source_name} level {level}")
    return total, verdict
```

Con los 20 eventos de la práctica, `safe_review("local_events", "ERROR")` devuelve `(6, "Revisión prioritaria")` por la rama `else`. Con `safe_review("local_events", "WARNING")` devuelve `(5, "Revisión prioritaria")`. Con `safe_review("missing_source", "CRITICAL")` la carga falla primero y el `except FileNotFoundError` devuelve `(0, "Rutina local")` sin traza cruda.

La excepción propia nace de una sola subclase permitida:

```python
class ReviewLevelError(Exception):
    """Raised when a review level is unknown to the local lab."""
```

Tres precisiones y nada más:

- Cuatro ramas: `try` intenta, cada `except` captura un tipo, `else` corre solo si nada falló, `finally` siempre deja constancia en la bitácora.
- Excepción propia: `ReviewLevelError` marca niveles desconocidos (`"CRITICAL"`); se lanza con `raise` y se captura por su tipo, nunca con un `except` desnudo.
- Alcance de hoy: 20 datos sintéticos con 6 `ERROR` y 5 `WARNING`, 3 tareas vigiladas y 1 error capturado en `defense.log`. Las etiquetas son didácticas del laboratorio, no estándares universales.

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
notepad harden_review.py

# 5. Ejecuta tu ejercicio
python harden_review.py
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
touch harden_review.py

# 5. Ejecuta tu ejercicio
python3 harden_review.py
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
touch harden_review.py

# 5. Ejecuta tu ejercicio
python3 harden_review.py
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

Crea `harden_review.py` con evidencia arriba, guardias en medio, llamadas desempaquetadas y reporte con bitácora al final (sin Pydantic, sin clases nuevas salvo la excepción propia, sin red, sin shell) que haga lo siguiente:

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, la lista de 20, tu identidad y la bitácora; imprime el total (`20`) | `REVIEW_THRESHOLD = 5`, `event_log` (20 textos: 6 `ERROR`, 5 `WARNING`), `student_name`, `student_id`, `LOG_PATH = "defense.log"` |
| 2. Endurecimiento | Define la excepción propia, `load_source`, `validate_level`, `review_events` y `safe_review` con `try/except/else/finally`; desempaqueta las tres llamadas | `ReviewLevelError`, `safe_review("local_events", "ERROR")` → par; `safe_review("local_events", "WARNING")` → par; `safe_review("missing_source", "CRITICAL")` → par de rutina |
| 3. Comunicación | Imprime el encabezado con los dos pares, la fuente capturada y la bitácora | Encabezado más pares, fuente no válida y registro declarado |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y tablas de revisión (léelas antes de programar)

```python
REVIEW_THRESHOLD = 5
event_log = [
    "INFO", "ERROR", "WARNING", "INFO", "ERROR",
    "WARNING", "ERROR", "INFO", "WARNING", "ERROR",
    "INFO", "WARNING", "INFO", "ERROR", "WARNING",
    "INFO", "ERROR", "INFO", "INFO", "INFO",
]
```

| Llamada vigilada | Rama que responde | Par |
|---------|-------|-----|
| `safe_review("local_events", "ERROR")` | `else` (todo salió bien) | (`6`, prioritaria) |
| `safe_review("local_events", "WARNING")` | `else` (todo salió bien) | (`5`, prioritaria) |
| `safe_review("missing_source", "CRITICAL")` | `except FileNotFoundError` (fuente faltante) | (`0`, rutina) |

Totales esperados: `6` con `"Revisión prioritaria"` para errores; `5` con `"Revisión prioritaria"` para avisos; fuente no válida con `"Rutina local"`. Con 4 o menos el veredicto sería `"Rutina local"`.

> Nota de fidelidad del respaldo: la lista de 20 posiciones conserva 6 `ERROR` y 5 `WARNING` para reproducir la salida esperada oficial, que es el contrato que la referencia debe cumplir. La bitácora `defense.log` guarda 3 tareas trazadas y 1 error capturado.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Eventos registrados: 20
Errores: 6 - Revisión prioritaria
Avisos: 5 - Revisión prioritaria
Fuente no válida: missing_source - Rutina local
--- Revisión endurecida ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Registro: defense.log (3 tareas, 1 error capturado)
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: tres hallazgos vigilados más un encabezado y cuatro líneas de datos. La bitácora `defense.log` queda así:

```text
INFO reviewed local_events level ERROR: 6
INFO finished task for local_events level ERROR
INFO reviewed local_events level WARNING: 5
INFO finished task for local_events level WARNING
WARNING captured missing source: missing local source: missing_source
INFO finished task for missing_source level CRITICAL
```

## Nota precisa sobre lo que el programa sí hace y lo que no hace

La revisión endurecida **organiza el conteo local para el cambio de turno sin interrumpirse**: tres pares vigilados más la bitácora que prueba cada captura. No abre puertos, no toca red y no confirma un incidente.

## Nota precisa sobre errores con guardias

Errores que verás en esta sesión:

- `FileNotFoundError: [Errno 2] No such file or directory: 'daily.log'`: pediste una fuente local que no existe y nada la capturó; Python señala el nombre faltante. La corrección es envolver la carga en `try` y capturar `FileNotFoundError` con reporte y bitácora, sin traza cruda.
- `ReviewLevelError: unknown review level: 'CRITICAL'`: el nivel no pertenece al conjunto conocido y tu `except` estrecho (solo `FileNotFoundError`) lo dejó escapar. La corrección es agregar `except ReviewLevelError` antes del remedio general y registrar la captura con `logging.warning`.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, funciones y comentarios) se escribe en inglés (`event_log`, `safe_review`, `REVIEW_THRESHOLD`, `error_total`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué rama responde en cada llamada (`else` para las dos conocidas, `except` para la fuente faltante).
- [ ] Qué par devuelve cada tarea vigilada y qué veredicto le toca.
- [ ] Cuándo se lanza `ReviewLevelError` y cómo se captura por su tipo.
- [ ] Qué registra `defense.log` y por qué la consola nunca muestra trazas crudas.
- [ ] Qué pasa si capturas con un `except` desnudo (ocultas la causa real).
- [ ] Qué NO hace el programa (no abre puertos, no toca red, no confirma un incidente).
- [ ] Tu programa se ejecuta sin errores y muestra los tres hallazgos más el encabezado y las cuatro líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, provoca la segunda captura sin sintaxis nueva: llama `safe_review("local_events", "DEBUG")` y predice en papel qué `except` responde antes de ejecutar con `↑`. Es solo práctica extra: no cambia tu calificación. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`harden_shift.py`), distinto del `harden_review.py` de clase y del desafío opcional de arriba.

**Historia:** dejas lista la revisión endurecida del turno antes de entregarla, distinta de la revisión del día de clase. Partes de 20 eventos nuevos del turno, aplicas la misma técnica de guardia con defecto `"WARNING"`, desempaquetas los tres pares vigilados y muestras el reporte con `shift.log`.

Crea manualmente `harden_shift.py` en tu proyecto personal, con umbral arriba, guardias en medio y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 20 del turno, tu identidad y la bitácora; imprime el total (`20`) | `SHIFT_THRESHOLD = 5`, `shift_events` (20 textos: 7 `WARNING`, 4 `ERROR`), `student_name`, `student_id`, `LOG_PATH = "shift.log"` |
| 2. Endurecimiento | Define `ShiftLevelError`, `load_shift_source`, `validate_shift_level`, `review_shift` y `safe_shift_review`; desempaqueta los tres pares | `safe_shift_review("local_events", "WARNING")` → par; `safe_shift_review("local_events", "ERROR")` → par; `safe_shift_review("missing_source", "DEBUG")` → par de rutina |
| 3. Comunicación | Reporte endurecido del turno con los dos pares y la fuente capturada | `print()` línea por línea |

Los 20 eventos del turno (escríbelos tal cual):

```python
SHIFT_THRESHOLD = 5
shift_events = [
    "WARNING", "INFO", "ERROR", "WARNING", "INFO",
    "WARNING", "INFO", "ERROR", "WARNING", "INFO",
    "WARNING", "ERROR", "INFO", "WARNING", "INFO",
    "INFO", "WARNING", "INFO", "ERROR", "INFO",
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Eventos del turno: 20
Avisos: 7 - Revisión prioritaria
Errores: 4 - Rutina local
Fuente no válida: missing_source - Rutina local
--- Revisión endurecida del turno ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Registro: shift.log (3 tareas, 1 error capturado)
```

> Notas de respaldo: el bloque de resumen replica la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los pares deben coincidir.

**Antes de programar, analiza:** qué rama responde en la llamada de avisos y por qué llega a `else`; qué par devuelve la llamada de errores y qué veredicto le toca bajo el umbral; qué llamada nombra la fuente faltante y dónde viaja su captura en vez de la consola.

**Propósito real:** la revisión organiza el conteo local para el cambio de turno sin interrumpirse: no abre puertos, no toca red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena guardia → captura → bitácora → veredicto. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
