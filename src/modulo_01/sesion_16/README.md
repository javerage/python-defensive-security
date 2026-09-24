# Sesión 16: JSON, CSV, registros y primer BaseModel

Bienvenido a la **Sesión 16** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **convertir eventos entre JSON y CSV con UTF-8 y encabezados, rotar un registro de lote con `logging` a archivo, validar cada registro con un primer modelo Pydantic `Evento(BaseModel)` usando `model_validate`, capturar `ValidationError` con un mensaje útil por fila, y explicar la diferencia entre modo lax (convierte `"15"` a `15`) y `strict=True` (rechaza la conversión)**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x) y Pydantic v2 (`python -c "import pydantic; print(pydantic.VERSION)"` debe responder `2.x`).
3. Crea manualmente el fixture `datos/eventos.json` (o deja que el arranque lo genere) y el controlador `validate_events.py`.
4. Ejecuta `python validate_events.py` desde la raíz del proyecto y verifica `salida/eventos.csv` (15 filas) más `proceso.log` (6 entradas).

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

15 min encuadre y anatomía del modelo en el límite de entrada · 10 min demo en vivo con JSON→CSV y `ValidationError` · 25 min práctica con `validate_events.py`, modo lax contra `strict=True` y registro a archivo · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que entrega eventos validados al tablero del siguiente turno sin que nadie consuma una fila rota. Recibes **20 dicts** en `eventos.json`, un umbral de 5 y **el lector `normalize_logs.py` heredado de la Sesión 15**: conviertes JSON a dicts, validas cada dict con el modelo `Evento` usando `model_validate`, cuentas aceptados y rechazados con motivo, publicas solo aceptados en `salida/eventos.csv` con encabezados, y rotas cada etapa en `proceso.log`. En la Sesión 15 las líneas quedaron limpias; hoy además cada campo queda validado en el límite de entrada.

## Secuencia conceptual

Cada lote validado del programa sigue este orden explícito:

1. **Evidencia:** `REVIEW_THRESHOLD = 5`, `raw_events` (20 dicts) y tu identidad.
2. **Arranque JSON:** `ensure_fixture_json(JSON_PATH, raw_events)` → `datos/eventos.json` con indentación 2 y UTF-8.
3. **Validación Pydantic:** `validate_records(...)` → 15 aceptados más 5 rechazados con motivo (`model_validate` + `try/except ValidationError`).
4. **Demostración strict:** `check_strict_sample(...)` → el registro `"15"` se convierte en lax y se rechaza con `strict=True`.
5. **Publicación CSV:** `write_events_csv(CSV_PATH, accepted)` → `salida/eventos.csv` con 15 filas más encabezados.
6. **Prueba CSV→dict:** `DictReader` entrega dicts de cadenas; la fila 1 reingresa por el mismo límite y lax convierte `"1"` a `1`.
7. **Reporte validado:** pares de errores contra el umbral, detalle de rechazados y alcance local.

## Cómo valida Pydantic en el límite (en clase, sin evaluar nada más)

El modelo declara el esquema con type hints; `model_validate` valida dicts; `ValidationError` agrupa los errores por campo; el modo lax convierte y `strict=True` rechaza:

```python
from typing import Literal
from pydantic import BaseModel, Field, ValidationError

class Evento(BaseModel):
    """Validated defensive event at the input boundary."""

    event_id: int
    level: Literal["INFO", "WARNING", "ERROR"]
    message: str = Field(min_length=1)
    source: str = Field(min_length=1)
```

```python
try:
    event = Evento.model_validate(raw_item)
except ValidationError as exc:
    field, motive = describe_rejection(exc.errors()[0])
    rejected.append(f"registro {position}: {motive} ({field})")
```

```python
# Lax convierte el texto numerico; strict rechaza la conversion.
Evento.model_validate({"event_id": "15", ...})  # acepta, event_id == 15
Evento.model_validate({"event_id": "15", ...}, strict=True)  # rechaza con ValidationError
```

```python
import logging

batch_logger = logging.getLogger("validate_events")
handler = logging.FileHandler(LOG_PATH, mode="w", encoding="utf-8")
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
batch_logger.addHandler(handler)
batch_logger.info("Validacion Pydantic: 15 aceptados, 5 rechazados")
```

Con los 20 dicts de la práctica, `validate_records` devuelve 15 eventos aceptados (el registro 15 entra por conversión lax de `"15"` a `15`) y 5 rechazados con motivo. `write_events_csv` deja `salida/eventos.csv` con encabezados más 15 filas. Sin clases de dominio nuevas, sin `argparse`, sin red y sin shell: Pydantic valida en este límite de entrada y no garantiza los tipos del resto del programa.

Tres precisiones y nada más:

- CSV→dict: `csv.DictReader` entrega cada fila como dict de cadenas; el dict (no la lista cruda) es lo que entra a `model_validate`. Validar una lista produce `ValidationError` de tipo `model_type`.
- Lax contra strict: el modo lax convierte valores compatibles (`"15"` → `15`); `strict=True` (o `ConfigDict(strict=True)`) rechaza cualquier conversión inesperada. La demostración del lote usa el mismo registro para probar ambos modos.
- Registro a archivo: `FileHandler` en modo `"w"` con UTF-8 reinicia `proceso.log` por lote; la consola imprime el reporte y el archivo guarda la traza del lote (6 entradas). El mensaje útil al usuario va en español; la traza cruda nunca se imprime.

## Ruta principal: reutiliza tu proyecto de la sesión 01

### Windows (PowerShell)

```powershell
# 1. Localiza y abre tu proyecto de la sesión 01
cd curso-python-defensivo
dir

# 2. Activa el entorno virtual
.\.venv\Scripts\Activate.ps1

# 3. Verifica el intérprete y Pydantic (debe mostrar Python 3.13.x y Pydantic 2.x)
python --version
python -c "import pydantic; print(pydantic.VERSION)"

# 4. Crea manualmente el fixture y el archivo nuevo
mkdir datos
notepad datos\eventos.json
notepad validate_events.py

# 5. Ejecuta desde la raíz y verifica las salidas
python validate_events.py
dir salida
type proceso.log
```

> Si PowerShell bloquea la activación, ejecuta primero `Set-ExecutionPolicy -Scope Process Bypass` y vuelve a activar.

### Linux (Bash)

```bash
# 1. Localiza y abre tu proyecto de la sesión 01
cd ~/curso-python-defensivo
ls

# 2. Activa el entorno virtual
source .venv/bin/activate

# 3. Verifica el intérprete y Pydantic (debe mostrar Python 3.13.x y Pydantic 2.x)
python3 --version
python3 -c "import pydantic; print(pydantic.VERSION)"

# 4. Crea manualmente el fixture y el archivo nuevo
mkdir -p datos
touch datos/eventos.json validate_events.py

# 5. Ejecuta desde la raíz y verifica las salidas
python3 validate_events.py
ls salida
cat proceso.log
```

### macOS (Zsh)

```bash
# 1. Localiza y abre tu proyecto de la sesión 01
cd ~/curso-python-defensivo
ls

# 2. Activa el entorno virtual
source .venv/bin/activate

# 3. Verifica el intérprete y Pydantic (debe mostrar Python 3.13.x y Pydantic 2.x)
python3 --version
python3 -c "import pydantic; print(pydantic.VERSION)"

# 4. Crea manualmente el fixture y el archivo nuevo
mkdir -p datos
touch datos/eventos.json validate_events.py

# 5. Ejecuta desde la raíz y verifica las salidas
python3 validate_events.py
ls salida
cat proceso.log
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
pip install "pydantic>=2.0,<3"
```

### Linux (Bash)

```bash
mkdir -p ~/curso-python-defensivo
cd ~/curso-python-defensivo
python3.13 -m venv .venv
source .venv/bin/activate
python3 --version
pip install "pydantic>=2.0,<3"
```

### macOS (Zsh)

```bash
mkdir -p ~/curso-python-defensivo
cd ~/curso-python-defensivo
python3.13 -m venv .venv
source .venv/bin/activate
python3 --version
pip install "pydantic>=2.0,<3"
```

Debes ver el prefijo `(.venv)` en el prompt, la versión Python 3.13.x y Pydantic 2.x. Después crea `datos/eventos.json` con los 20 dicts de la tabla de abajo.

## Ejercicio obligatorio

Crea `validate_events.py` con evidencia arriba, tareas validadas en medio, demostración strict y reporte validado al final (sin clases de dominio, sin `argparse`, sin red, sin shell) que haga lo siguiente:

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 20 dicts y tu identidad; ancla las rutas al archivo | `REVIEW_THRESHOLD = 5`, `raw_events` (20 dicts), `student_name`, `student_id`, `JSON_PATH`, `CSV_PATH`, `LOG_PATH` |
| 2. Validado | Arranca el fixture JSON, valida cada dict con `model_validate`, demuestra strict y publica aceptados en CSV | `ensure_fixture_json(...)`, `read_raw_records(JSON_PATH)` → 20; `validate_records(...)` → 15 más 5 con motivo; `check_strict_sample(...)`; `write_events_csv(...)` → `salida/eventos.csv` |
| 3. Comunicación | Imprime conteos del lote, el par de errores contra el umbral, el detalle de rechazados y el alcance | `print()` línea por línea |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y tablas de revisión (léelas antes de programar)

```python
REVIEW_THRESHOLD = 5
raw_events = [
    # 1-14: registros correctos (tipos exactos, niveles permitidos).
    # 15: {"event_id": "15", ...} texto numerico (lax lo convierte).
    # 16: sin "level" (campo faltante).
    # 17: {"event_id": "sin-numero", ...} (tipo invalido).
    # 18: {"level": "DEBUG", ...} (valor no permitido).
    # 19: sin "event_id" (campo faltante).
    # 20: {"message": "", ...} (valor no permitido).
]
```

| Revisión validada | Llamada que la produce | Par |
|---------|-------|-----|
| Errores aceptados contra el umbral | conteo de `ERROR` en eventos aceptados | (`3`, rutina: 3 < 5) |
| Archivo publicado | `write_events_csv` con encabezados | 15 filas en `salida/eventos.csv` |
| Traza del lote | `FileHandler` en modo `"w"` | 6 entradas en `proceso.log` |

Totales esperados: `20` leídos, `15` aceptados, `5` rechazados con motivo; `3` errores con `"Rutina local"`. Con 5 o más el veredicto sería `"Revisión prioritaria"`.

### Tabla de aceptados y rechazados

| # | event_id | level | Motivo / estado |
|---|----------|-------|-----------------|
| 1–14 | 1–14 | INFO / WARNING / ERROR | Aceptado (tipos exactos) |
| 15 | `"15"` → `15` | INFO | Aceptado por conversión lax |
| 16 | 16 | — | Rechazado: campo faltante (`level`) |
| 17 | `"sin-numero"` | ERROR | Rechazado: tipo inválido (`event_id`) |
| 18 | 18 | `DEBUG` | Rechazado: valor no permitido (`level`) |
| 19 | — | INFO | Rechazado: campo faltante (`event_id`) |
| 20 | 20 | INFO | Rechazado: valor no permitido (`message`) |

> Nota de fidelidad del respaldo: la lista de 20 posiciones conserva 14 aceptados exactos, 1 aceptado por conversión lax y 5 rechazados con motivo para reproducir la salida esperada oficial, que es el contrato que la referencia debe cumplir.

## Salida esperada

Ejecuta tu archivo desde la raíz del proyecto y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Eventos leidos: 20
Eventos aceptados: 15
Eventos rechazados: 5
Errores (aceptados): 3 - Rutina local
Salida: salida/eventos.csv (15 filas) + proceso.log (6 entradas)
Rechazados (5):
- registro 16: campo faltante (level)
- registro 17: tipo invalido (event_id)
- registro 18: valor no permitido (level)
- registro 19: campo faltante (event_id)
- registro 20: valor no permitido (message)
--- Revision validada ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Modo: lax convierte ("15" -> 15); strict=True rechaza
Alcance: localhost (127.0.0.1) y fixtures locales
```

Además `salida/eventos.csv` debe contener encabezados `event_id,level,message,source` más exactamente 15 filas (solo aceptados), `datos/eventos.json` debe conservar los 20 dicts con indentación 2, y `proceso.log` debe contener exactamente 6 entradas `INFO:` (inicio, fixture, validación, demo strict, CSV publicado, prueba CSV→dict). Los 5 rechazados viajan a consola con motivo en español, no como traza cruda.

Convención de predicción previa: antes de completar cada TODO, el estudiante escribe su predicción (valor esperado y motivo); solo después de ejecutar el script compara el resultado obtenido con su predicción y con la salida esperada (predecir → ejecutar → comparar).

## Nota precisa sobre lo que el programa sí hace y lo que no hace

La validación en el límite **prepara eventos confiables para el tablero local sin consumir filas rotas**: 20 dicts leídos, 15 publicados con esquema garantizado, 5 rechazados con motivo, un par contra el umbral y una traza de 6 entradas que los tests de la Sesión 17 pueden reproducir. No abre puertos, no toca red y no confirma un incidente. Pydantic valida en este límite de entrada con type hints; no garantiza los tipos del resto del programa y no sustituye la comprensión de tipos, las pruebas ni el análisis estático.

## Nota precisa sobre errores con JSON, CSV y modelos

Errores que verás en esta sesión:

- `ValidationError: 1 validation error for Evento — level — Field required`: validaste un dict sin la clave `level` (registro 16). La causa es un campo faltante, no un fallo del modelo. La corrección es capturar `ValidationError` con `try/except`, extraer `exc.errors()[0]` para el motivo en español, y re-ejecutar con `↑`.
- `ValidationError: Input should be a valid dictionary`: pasaste una lista (fila CSV cruda) directo a `model_validate` en vez de un dict. La corrección es pasar siempre por `csv.DictReader` (cada fila ya es dict) antes de validar, verificar con `dir` o `ls` que `salida/eventos.csv` existe, y re-ejecutar con `↑`.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, funciones, rutas y comentarios) se escribe en inglés (`raw_events`, `validate_records`, `write_events_csv`, `JSON_PATH`, `error_total`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. La entidad validada se llama `Evento` por mandato del currículo (contrato con las Sesiones 17–18). Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`; las constantes usan `UPPER_CASE`; la clase usa `PascalCase`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué declara cada campo de `Evento` (`event_id`, `level`, `message`, `source`) y qué type hint lo sostiene.
- [ ] Qué valida cada llamada (`model_validate` por dict) y qué motivo le toca a cada rechazado.
- [ ] Qué convierte el modo lax (`"15"` → `15`) y qué rechaza `strict=True` sobre el mismo registro.
- [ ] Por qué el CSV llega a dict (`DictReader`) antes de validar y qué error produce validar una lista.
- [ ] Qué registra cada una de las 6 entradas de `proceso.log` y dónde viaja el motivo de cada rechazado.
- [ ] Qué captura el `try/except ValidationError` y qué imprime en vez de una traza cruda.
- [ ] Qué NO garantiza Pydantic (no certifica el resto del programa, ni sustituye pruebas ni análisis estático).
- [ ] Tu programa se ejecuta desde la raíz sin errores y muestra conteos, pares, detalle de rechazados y alcance.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, sin sintaxis nueva: cuenta el tercer nivel sobre los eventos ya aceptados (`INFO` suma 7, así que también alcanza el umbral) y predice en papel el par antes de ejecutar con `↑`. Después valida el registro `"15"` con `strict=True` en el intérprete y predice qué error devuelve y por qué. Es solo práctica extra: no cambia tu calificación. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`validate_shift.py`), distinto del `validate_events.py` de clase y del desafío opcional de arriba.

**Historia:** dejas lista la validación del turno nocturno antes de entregarla, distinta del lote del día de clase. Partes de 10 dicts nuevos del turno, reutilizas la misma técnica validada con umbral propio, publicas con el mismo `DictWriter` y muestras el reporte con el mismo alcance local.

Crea manualmente `validate_shift.py` en tu proyecto personal, reutilizando evidencia arriba, tareas validadas en medio y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 10 del turno y tu identidad; imprime el total (`10`) | `SHIFT_THRESHOLD = 5`, `shift_events` (10 dicts: 7 exactos, 1 lax `"25"`, 2 inválidos), `student_name`, `student_id` |
| 2. Validado | Reutiliza `Evento`, `validate_records` y `write_events_csv` bajo `main()` con la guardia; publica el turno | `read_raw_records(...)` → 10; `validate_records(...)` → 8 más 2 con motivo; `write_events_csv(...)` → `salida/turno_eventos.csv` |
| 3. Comunicación | Reporte validado del turno con el par, los conteos y la ruta publicada | `print()` línea por línea |

Los 10 dicts del turno (escríbelos tal cual; el registro 5 usa texto numérico `"25"` y los registros 9–10 son inválidos):

```python
SHIFT_THRESHOLD = 5
shift_events = [
    {"event_id": 21, "level": "INFO", "message": "turno nocturno iniciado", "source": "sensor-a"},
    {"event_id": 22, "level": "WARNING", "message": "ronda local sin novedad", "source": "sensor-b"},
    {"event_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"event_id": 24, "level": "WARNING", "message": "cola de eventos llena", "source": "sensor-b"},
    {"event_id": "25", "level": "INFO", "message": "respaldo local confirmado", "source": "sensor-a"},
    {"event_id": 26, "level": "ERROR", "message": "archivo temporal corrupto", "source": "sensor-b"},
    {"event_id": 27, "level": "INFO", "message": "inventario local actualizado", "source": "sensor-a"},
    {"event_id": 28, "level": "WARNING", "message": "latencia alta en loopback", "source": "sensor-b"},
    {"event_id": 29, "message": "linea sin nivel", "source": "sensor-a"},
    {"event_id": "sin-numero", "level": "INFO", "message": "tipo invalido", "source": "sensor-b"},
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Eventos leidos: 10
Eventos aceptados: 8
Eventos rechazados: 2
Errores (aceptados): 2 - Rutina local
Salida: salida/turno_eventos.csv (8 filas) + turno_proceso.log (5 entradas)
Rechazados (2):
- registro 9: campo faltante (level)
- registro 10: tipo invalido (event_id)
--- Revision validada del turno ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Modo: lax convierte ("25" -> 25); strict=True rechaza
Alcance: localhost (127.0.0.1) y fixtures locales
```

> Notas de respaldo: el bloque de resumen replica la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los pares deben coincidir.

**Antes de programar, analiza:** qué conteo validado revisa el nivel de errores y qué veredicto le toca bajo el umbral; qué llamada convierte el texto numérico en modo lax y cuál la rechaza con `strict=True`; qué llamada de publicación garantiza encabezados más UTF-8 y dónde viaja cada motivo en vez de una traza.

**Propósito real:** la validación prepara eventos confiables para el tablero local sin consumir filas rotas: no abre puertos, no toca red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena JSON → validación → CSV más registro. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos. Ningún script de la sesión abre sockets ni envía tráfico: solo lee y escribe archivos dentro de tu carpeta del curso.
