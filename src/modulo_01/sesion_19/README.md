# Sesión 19: Checkpoint de fundamentos (analizador local con Pi observador)

Bienvenido a la **Sesión 19** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **integrar los fundamentos (M1–M10) en un analizador local `analizar.py` (texto/JSON/CSV + conteos + reporte) que pasa las 8 pruebas del docente, con `Finding` de la Sesión 18 como base de validación**.

> Pi es SOLO observador en esta sesión: predice la salida, revisa el diff propuesto sin aplicarlo, explica cada línea y reflexiona qué aceptaría o rechazaría. Pi no escribe ni ejecuta código aquí. Existe ruta completa sin Pi con ejemplo parcial para todo el grupo.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x) y Pydantic v2 (`python -c "import pydantic; print(pydantic.VERSION)"` debe responder `2.x`).
3. Mantén intacto el lote `finding_model.py` de la Sesión 18 y crea el analizador `analizar.py` más su suite `test_analizar.py`.
4. Ejecuta `python analizar.py` desde la raíz del proyecto y verifica el reporte del checkpoint; luego ejecuta `python -m unittest test_analizar.py -v` (8/8 en verde) y, si está instalado, `pytest test_analizar.py -v`.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos, distribución explícita de checkpoint)

**10 + 12 + 33 + 5 = 60**: 10 min integración de M1–M10 y lectura de especificación con criterios · 12 min demo en vivo de un subproblema con Pi como observador (predecir → revisar diff → explicar → reflexionar) · 33 min desarrollo individual del analizador con lista de criterios · 5 min registro de evidencia y cierre.

## Historia del ejercicio

Eres el analista de turno que convierte el turno completo en un reporte firmable. La flota de sensores produjo **20 eventos** crudos en tres formatos locales (8 líneas de texto, 6 registros JSON, 6 filas CSV); tu trabajo es integrarlos en **17 hallazgos** aceptados más **3 filas** rechazadas con motivo, con umbral de 5: los parsers convierten cada formato en dicts crudos, cada dict cruza la frontera `Finding` de la Sesión 18, solo las filas aceptadas llegan al conteo, y los 6 errores aceptados sobre el umbral dictan `"Revision prioritaria"`. En la Sesión 18 las cifras quedaron probadas con 6 dicts; hoy el mismo modelo sostiene 20 eventos sin cambiar una línea del esquema.

## Secuencia conceptual

Cada turno analizado del programa sigue este orden explícito:

1. **Evidencia:** `FINDING_THRESHOLD = 5`, `TEXT_LOG` (8 líneas: 3 INFO, 2 WARNING, 2 ERROR, 1 malformada), `JSON_PAYLOAD` (6 registros: 2 INFO, 1 WARNING, 2 ERROR, 1 DEBUG inválido), `CSV_PAYLOAD` (6 filas: 2 INFO, 1 WARNING, 2 ERROR, 1 mensaje vacío) y tu identidad.
2. **Parsers:** `parse_text_log(...)` → 7 más 1; `parse_json_payload(...)` → 6 crudos; `parse_csv_payload(...)` → 6 crudos (pruebas 1–3: un parser por formato).
3. **Frontera validada:** `validate_records(...)` → 17 aceptados más 3 rechazados con motivo por posición (pruebas 2–4 y 7: aceptación y rechazo Pydantic).
4. **Conteo y veredicto:** `FindingReport.count_by_level()` → `INFO=7, WARNING=4, ERROR=6`; `verdict()` → `(6, "Revision prioritaria")` sobre el umbral 5 (pruebas 5–6).
5. **Reporte auditable:** `format_report(...)` con operador, sello fijo, alcance local y declaración de confinamiento (prueba 8).

## Cómo se integra en el límite (en clase, sin sintaxis nueva)

Los parsers convierten texto en dicts; el `BaseModel` convierte o rechaza dicts en la frontera; el reporte cuenta solo aceptados. Pydantic no sustituye comprender parsers ni pruebas: solo guarda la frontera donde tú lo pones, igual que en la Sesión 18.

```python
def parse_text_log(raw_text):
    """Split pipe-separated lines into raw finding dicts."""
    # Cada linea "LEVEL | message | source" es un dict crudo;
    # la linea sin separadores es un rechazo de formato con motivo.
```

```python
def validate_records(raw_records, first_position):
    """Split raw dicts into accepted findings plus labeled rejections."""
    # Cada dict cruza Finding.model_validate: el aceptado viaja al
    # reporte, el roto se etiqueta con su posicion y su motivo.
```

```python
# Aceptacion: 17 dicts cruzan la frontera intactos.
# Rechazo: DEBUG inventado, mensaje vacio y linea malformada mueren
# en la frontera con motivo (nunca llegan al conteo).
# Veredicto: 6 errores aceptados sobre el umbral 5 en solo lectura.
```

Con los 20 eventos del turno, el reporte agrupa `INFO=7, WARNING=4, ERROR=6` (6 errores → `"Revision prioritaria"` sobre el umbral 5). Sin `argparse`, sin sockets, sin `subprocess`, sin red y sin shell: el analizador solo lee cadenas locales, valida dicts y cuenta aceptados.

Tres precisiones y nada más:

- Crudo contra aceptado: crudo es todo lo que entró (20); aceptado es lo que cruzó la frontera (17); rechazado es lo que murió con motivo (3). El conteo por nivel solo suma aceptados: si cuentas rechazados, el veredicto miente.
- Parser contra frontera: el parser entiende formatos (texto, JSON, CSV); la frontera entiende validez (`Finding`). Una fila bien formateada pero con nivel `DEBUG` pasa el parser y muere en la frontera: dos muertes distintas, dos motivos distintos.
- Pi observador: Pi puede mostrarte un diff o explicarte una línea, pero nunca escribe ni ejecuta en esta sesión. El flujo obligatorio es predecir → revisar el diff sin aplicarlo → explicar cada línea → reflexionar qué aceptas o rechazas. La ruta sin Pi usa el mismo ejemplo parcial de texto y la revisión docente equivalente.

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

# 4. Crea manualmente los archivos nuevos (el lote S18 queda intacto)
notepad analizar.py
notepad test_analizar.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python analizar.py
python -m unittest test_analizar.py -v
pytest test_analizar.py -v
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

# 4. Crea manualmente los archivos nuevos (el lote S18 queda intacto)
touch analizar.py test_analizar.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python3 analizar.py
python3 -m unittest test_analizar.py -v
pytest test_analizar.py -v
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

# 4. Crea manualmente los archivos nuevos (el lote S18 queda intacto)
touch analizar.py test_analizar.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python3 analizar.py
python3 -m unittest test_analizar.py -v
pytest test_analizar.py -v
```

> Desarrollo local en macOS con `python3`. La validación final del laboratorio se realiza en Windows con `python`. El último comando (`pytest`) es opcional: si responde `no se reconoce el comando`, tu nota queda completa con `unittest` en verde.

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
pip install pytest
```

### Linux (Bash)

```bash
mkdir -p ~/curso-python-defensivo
cd ~/curso-python-defensivo
python3.13 -m venv .venv
source .venv/bin/activate
python3 --version
pip install "pydantic>=2.0,<3"
pip install pytest
```

### macOS (Zsh)

```bash
mkdir -p ~/curso-python-defensivo
cd ~/curso-python-defensivo
python3.13 -m venv .venv
source .venv/bin/activate
python3 --version
pip install "pydantic>=2.0,<3"
pip install pytest
```

Debes ver el prefijo `(.venv)` en el prompt, la versión Python 3.13.x y Pydantic 2.x. (`pytest` es opcional: suma legibilidad, nunca es requisito para aprobar.) Después crea `analizar.py` con los 20 eventos de la tabla de abajo y `test_analizar.py` con las 8 pruebas.

## Ejercicio obligatorio

Crea `analizar.py` con evidencia arriba, tareas de integración en medio y reporte auditable al final (sin `argparse`, sin sockets, sin `subprocess`, sin red, sin shell; Pi solo observa) que haga lo siguiente:

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 3 payloads y tu identidad; ancla el contrato local | `FINDING_THRESHOLD = 5`, `TEXT_LOG` (8 líneas), `JSON_PAYLOAD` (6 registros), `CSV_PAYLOAD` (6 filas), `student_name`, `student_id`, `AUDIT_STAMP` |
| 2. Integración | Parsea cada formato, valida en la frontera y agrupa en el reporte | `parse_text_log(...)` → 7 más 1; `parse_json_payload(...)` + `validate_records(..., 9)` → 5 más 1; `parse_csv_payload(...)` + `validate_records(..., 15)` → 5 más 1; `analyze_shift()` → 20, 17, 3; conteos `7, 4, 6`; veredicto sobre el umbral |
| 3. Comunicación | Imprime las 4 líneas de prueba, el par de errores contra el umbral y el reporte de ancho fijo | `print()` línea por línea; `format_report(...)` |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py` (ejemplo parcial de texto que ya ejecuta: 8 crudos → 7 aceptados + 1 rechazado). La suite de referencia está en `test_analizar.py` (8 pruebas `unittest`, compatible con `pytest`).

## Entrada sintética y tablas de revisión (léelas antes de programar)

```python
FINDING_THRESHOLD = 5
# TEXT_LOG: 8 lineas (3 INFO, 2 WARNING, 2 ERROR, 1 malformada).
# JSON_PAYLOAD: 6 registros (2 INFO, 1 WARNING, 2 ERROR, 1 DEBUG).
# CSV_PAYLOAD: 6 filas (2 INFO, 1 WARNING, 2 ERROR, 1 mensaje vacio).
# Totales: 20 crudos -> 17 aceptados + 3 rechazados; 6 errores prioritarios.
```

| Revisión integrada | Prueba que la encierra | Par |
|---------|-------|-----|
| Parser de texto (7 más 1) | `test_text_parser_accepts_seven_and_rejects_malformed` (normal) | (`7`, `1`) |
| JSON acepta 5 y rechaza DEBUG | `test_json_parser_rejects_debug_level_at_boundary` (aceptación + rechazo) | (`5`, `1`) |
| CSV acepta 5 y rechaza vacío | `test_csv_parser_rejects_empty_message_at_boundary` (aceptación + rechazo) | (`5`, `1`) |
| Totales del turno | `test_shift_totals_raw_accepted_rejected` (integración) | (`20`, `17`, `3`) |
| Conteos por nivel | `test_shift_counts_by_level` (integración) | (`7`, `4`, `6`) |
| Veredicto sobre umbral | `test_shift_verdict_priority_above_threshold` (integración) | (`6`, prioritaria) |
| Frontera strict + longitud | `test_boundary_rejects_long_message_and_strict_text_id` (rechazo + strict) | (`ValidationError` que nombra `message`; `"31"` → `31`; `strict=True` lanza) |
| Reporte local con operador | `test_report_confined_to_localhost_with_operator` (alcance) | (operador, `127.0.0.1`, sin sockets) |

Totales esperados: `8` pruebas, `8` en verde, `0` errores de suite; `6` errores aceptados con `"Revision prioritaria"`. Checkpoint 1 (fundamentos), parte del 30%.

### Tabla de pruebas (contrato de la suite)

| # | Prueba | Tipo | Qué encierra |
|---|--------|------|--------------|
| 1 | `test_text_parser_accepts_seven_and_rejects_malformed` | normal | El texto produce 7 registros más 1 rechazo de formato |
| 2 | `test_json_parser_rejects_debug_level_at_boundary` | aceptación + rechazo | El JSON acepta 5 y rechaza el nivel DEBUG |
| 3 | `test_csv_parser_rejects_empty_message_at_boundary` | aceptación + rechazo | El CSV acepta 5 y rechaza el mensaje vacío |
| 4 | `test_shift_totals_raw_accepted_rejected` | integración | El turno lee 20: 17 aceptados + 3 rechazados |
| 5 | `test_shift_counts_by_level` | integración | Los conteos son INFO=7 WARNING=4 ERROR=6 |
| 6 | `test_shift_verdict_priority_above_threshold` | integración | 6 errores sobre el umbral 5 dan Revision prioritaria |
| 7 | `test_boundary_rejects_long_message_and_strict_text_id` | rechazo + strict | 141 caracteres se rechaza; `"31"` → `31` en lax y lanza con `strict=True` |
| 8 | `test_report_confined_to_localhost_with_operator` | alcance | El reporte lleva operador, `127.0.0.1` y cero red |

> Nota de fidelidad del respaldo: la suite conserva 3 pruebas de parser más 3 de integración (totales, conteos, veredicto) más 1 de frontera strict y 1 de alcance para reproducir el reporte esperado oficial, que es el contrato que la referencia debe cumplir. Cada prueba sigue arrange-act-assert y cada assert lleva mensaje.

## Salida esperada

Ejecuta tu archivo desde la raíz del proyecto y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Pruebas del docente: 8/8 en verde (unittest)
Conteo por nivel: INFO=7 WARNING=4 ERROR=6
Eventos: 20 crudos -> 17 aceptados + 3 rechazados
Errores (aceptados): 6 - Revision prioritaria
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

Y la suite debe responder así (el tiempo exacto varía por equipo; lo que debe coincidir es `8 tests` y `OK`):

```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

Con `pytest` instalado, la misma suite responde con 8 nodos en verde (`8 passed`); sin `pytest`, el bloque `unittest` de arriba vale el 100% de la nota.

Convención de predicción previa: antes de completar cada TODO, el estudiante escribe su predicción (valor esperado y motivo); solo después de ejecutar el script compara el resultado obtenido con su predicción y con la salida esperada (predecir → ejecutar → comparar).

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El turno analizado **convierte 20 eventos sueltos en 17 hallazgos firmables sin ejecutar nada fuera de la máquina**: 3 parsers locales, una frontera validada, conteo de aceptados, par contra el umbral y un reporte de ancho fijo. No abre puertos, no toca red y no confirma un incidente. Los parsers encierran los formatos de hoy; no certifican cambios futuros ni sustituyen leer el código, revisar el alcance ni repetir la suite tras cada edición. Pydantic valida en la frontera donde lo colocas; no garantiza los tipos del resto del programa.

## Nota precisa sobre errores de integración

Errores que verás en esta sesión:

- `FileNotFoundError: [Errno 2] No such file or directory: 'datos/eventos.json'`: intentaste abrir un archivo de datos que no existe porque el turno vive en cadenas dentro del script, no en archivos. La causa es una ruta inventada, no un turno roto. La corrección es mirar antes de saltar (`dir` o `ls`), confirmar que trabajas desde la raíz del proyecto y leer `TEXT_LOG`/`JSON_PAYLOAD`/`CSV_PAYLOAD` en memoria con `↑` para re-ejecutar.
- `AssertionError: El turno debia aceptar 17 hallazgos`: contaste filas rechazadas como aceptadas (por ejemplo sumaste los 20 crudos al reporte) y el veredicto mintió. La causa es mezclar crudos con aceptados, no un parser roto. La corrección es contar solo lo que cruzó `Finding.model_validate`, mantener `rejected` fuera del reporte y re-ejecutar con `↑` hasta ver `17 aceptados + 3 rechazados`.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, funciones nuevas, rutas y comentarios) se escribe en inglés (`parse_text_log`, `validate_records`, `analyze_shift`, `FINDING_THRESHOLD`, `Finding`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario y los mensajes de cada assert se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`; las constantes usan `UPPER_CASE`; las clases usan `PascalCase`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué convierte cada parser (texto, JSON, CSV) en dicts crudos y qué fila muere en cada formato con qué motivo.
- [ ] Qué acepta la frontera `Finding` y qué rechaza (DEBUG inventado, mensaje vacío, línea malformada) con motivo por posición.
- [ ] Por qué el conteo suma solo aceptados (17) y qué mentiría si sumaras crudos (20) o aceptaras rechazados.
- [ ] Qué par produce 6 errores sobre el umbral 5 (`Revision prioritaria`) y qué producirían 2 (`Rutina local`, como en la S18).
- [ ] Qué convierte el modo lax (`"31"` → `31`), qué rechaza `strict=True` sobre el mismo dict y cómo lo espera cada prueba (`assertEqual` contra `assertRaises`).
- [ ] Qué puede y qué no puede hacer Pi en esta sesión (observar, mostrar diff, explicar; nunca escribir ni ejecutar) y cuál es el flujo obligatorio.
- [ ] Qué corredor garantiza tu nota (`unittest`, biblioteca estándar) y qué aporta el opcional (`pytest`, legibilidad).
- [ ] Qué NO garantizan las 8 pruebas ni Pydantic (no certifican cambios futuros; tras cada edición se repite la suite).
- [ ] Tu programa se ejecuta desde la raíz sin errores y muestra reporte del checkpoint, suite 8/8 y alcance.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, sin sintaxis nueva: agrega a tu analizador un contador de rechazados por motivo (`formato`, `frontera`) usando solo dicts y `.get()`, y predice en papel el valor (`formato=1`, `frontera=2`) antes de ejecutar con `↑`. Después valida el dict con `message` de exactamente 140 caracteres (debe aceptarse) y con 141 (debe rechazarse con `ValidationError` que nombra `message`). Es solo práctica extra: no cambia tu calificación. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`analizar_borde.py`), distinto del `analizar.py` de clase y del desafío opcional de arriba.

**Historia:** dejas analizado el turno nocturno antes de entregarlo, distinto del turno del día de clase. Partes de 8 dicts del turno con casos borde, reutilizas la misma frontera `Finding` con umbral propio, verificas con cinco chequeos con mensaje y muestras el reporte con el mismo alcance local.

Crea manualmente `analizar_borde.py` en tu proyecto personal, reutilizando evidencia arriba, tareas de borde en medio y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 8 del turno y tu identidad; imprime el total (`8`) | `SHIFT_THRESHOLD = 3`, `shift_records` (8 dicts: 3 exactos, 1 de 140, 1 de 141, 1 lax `"31"`, 2 inválidos), `student_name`, `student_id` |
| 2. Borde | Reutiliza `Finding`, `validate_shift_records` y `count_by_level` bajo `main()` con cinco asserts con mensaje | `validate_shift_records(...)` → 5 más 3; lax `"31"` → `31`; conteos `3, 1, 1`; veredicto bajo el umbral; `strict=True` rechaza |
| 3. Comunicación | Reporte del turno con el par, los conteos y los chequeos | `print()` línea por línea |

Los 8 dicts del turno (escríbelos tal cual; el registro 4 usa 140 caracteres, el 5 usa 141, el 6 usa texto numérico `"31"` y los registros 7–8 son inválidos):

```python
SHIFT_THRESHOLD = 3
shift_records = [
    {"finding_id": 21, "level": "INFO", "message": "ronda nocturna iniciada en localhost", "source": "sensor-a"},
    {"finding_id": 22, "level": "WARNING", "message": "latencia nocturna alta en loopback", "source": "sensor-b"},
    {"finding_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"finding_id": 24, "level": "INFO", "message": "x" * 140, "source": "sensor-b"},
    {"finding_id": 25, "level": "INFO", "message": "x" * 141, "source": "sensor-a"},
    {"finding_id": "31", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"},
    {"finding_id": 27, "level": "ERROR", "message": "sonda local sin origen", "source": ""},
    {"finding_id": 28, "level": "DEBUG", "message": "nivel nocturno inventado", "source": "sensor-b"},
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Turno leido: 8
Turno aceptado: 5
Turno rechazado: 3
Conteo por nivel: INFO=3 WARNING=1 ERROR=1
Errores (aceptados): 1 - Rutina local
Chequeos del turno: 5/5 en verde (asserts con mensaje)
--- Reporte probado (turno) ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 3 (solo lectura)
Evolucion: Finding (S18) -> analizar.py (S19)
Alcance: localhost (127.0.0.1) y fixtures locales
```

> Notas de respaldo: el bloque de resumen replica la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los pares deben coincidir (5 aceptados con `3, 1, 1`; 1 error bajo el umbral 3).

**Antes de programar, analiza:** qué llamada separa aceptados de rechazados y qué veredicto le toca a 1 error bajo el umbral; qué llamada convierte el texto numérico en modo lax y dónde viaja cada motivo en vez de una traza.

**Propósito real:** el borde convierte filas hostiles del turno en hallazgos citables para el tablero local: no abre puertos, no toca red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena datos del turno → chequeos de borde → reporte. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos. Ningún script de la sesión abre sockets ni envía tráfico: solo parsea cadenas locales, valida dicts e imprime el reporte en tu consola. Pi solo observa en esta sesión: cada línea la escribes, la predices y la explicas tú.
