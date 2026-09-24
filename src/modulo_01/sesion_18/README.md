# Sesión 18: POO mínima y evolución a modelos Pydantic

Bienvenido a la **Sesión 18** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **modelar `Hallazgo` y `Reporte` primero como clases manuales con constructor, atributos y métodos, sin herencia, con 3 pruebas que pasan, y después evolucionarlas a modelos Pydantic (`BaseModel`) con restricciones (`Field`, `Literal`, `strict=True` donde se exige rechazo), manteniendo las pruebas en verde y explicando la diferencia entre clase manual y esquema validado**.

> Última sesión con prohibición total de Pi. Sin asistente de IA en clase ni en la tarea.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x) y Pydantic v2 (`python -c "import pydantic; print(pydantic.VERSION)"` debe responder `2.x`).
3. Mantén intacto el lote `review_batch.py` de la Sesión 17 y crea el modelo `finding_model.py` más su suite `test_modelo.py`.
4. Ejecuta `python finding_model.py` desde la raíz del proyecto y verifica el reporte probado; luego ejecuta `python -m unittest test_modelo.py -v` (3/3 en verde) y, si está instalado, `pytest test_modelo.py -v`.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

15 min encuadre y anatomía del objeto (clase, objeto, `__init__`, atributos/métodos, `_privado`) · 10 min demo en vivo clase manual → `BaseModel` con `ValidationError` · 25 min práctica con `finding_model.py`, 3 pruebas y ambos corredores · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del turno que convierte eventos sueltos en hallazgos firmables. La flota de sensores produjo **20 eventos** crudos; tu trabajo es condensarlos en **6 hallazgos** revisables con umbral de 5: primero los modelas como **clases manuales** (`ManualFinding` con `__init__`, atributos públicos, método `summary()` e `is_critical()`, etiqueta `_label` privada por convención), sin herencia; después los evolucionas al **esquema validado** (`Finding(BaseModel)` con `Field`, `Literal` y `strict=True` donde se exige rechazo). En la Sesión 17 las cifras quedaron probadas con dicts; hoy cada hallazgo es un objeto y cada fila rota se rechaza en la frontera con motivo por campo.

## Secuencia conceptual

Cada lote modelado del programa sigue este orden explícito:

1. **Evidencia:** `FINDING_THRESHOLD = 5`, `sample_records` (6 dicts: 3 INFO, 1 WARNING, 2 ERROR) y tu identidad.
2. **Clase manual:** `ManualFinding(1, "INFO", ...)` → `summary()` empieza con `[INFO]`; `is_critical()` es `False` (prueba 1: anatomía del objeto).
3. **Esquema validado:** `Finding.model_validate(...)` acepta el dict válido con campos exactos (prueba 2: aceptación Pydantic).
4. **Rechazo esperado:** el dict con `message` vacío lanza `ValidationError` que nombra `message`; el id como texto `"7"` se convierte en lax (`7`) y se rechaza con `strict=True` (prueba 3: rechazo + frontera strict).
5. **Reporte modelado:** par de errores contra el umbral, nota de evolución y alcance local.

## Cómo se modela en el límite (en clase, sin evaluar nada más)

La clase manual enseña anatomía; el `BaseModel` agrega esquema con type hints que valida en el límite de entrada. Pydantic no sustituye comprender clases ni pruebas: solo convierte o rechaza datos donde tú lo pones a guardar la frontera.

```python
class ManualFinding:
    """Manual finding with constructor, public attributes and methods."""

    def __init__(self, finding_id, level, message, source):
        if level not in ALLOWED_LEVELS:
            raise ValueError("level must be one of INFO, WARNING, ERROR")
        self.finding_id = finding_id  # public attribute
        self.level = level            # public attribute
        self._label = f"{level}-{finding_id}"  # private by convention

    def summary(self):  # public method
        return f"[{self.level}] {self.message} ({self.source})"

    def is_critical(self):  # public method
        return self.level == "ERROR"
```

```python
class Finding(BaseModel):
    """Validated defensive finding at the input boundary."""

    finding_id: int
    level: Literal["INFO", "WARNING", "ERROR"]
    message: str = Field(min_length=1, max_length=140)
    source: str = Field(min_length=1)
```

```python
# Aceptacion lax: el texto numerico entra convertido.
event = Finding.model_validate({"finding_id": "7", ...})
assert event.finding_id == 7
# El mismo dict se rechaza cuando strict prohibe la conversion.
Finding.model_validate({"finding_id": "7", ...}, strict=True)  # lanza ValidationError
```

Con los 6 dicts de la práctica, el reporte agrupa `INFO=3, WARNING=1, ERROR=2` (2 errores → `"Rutina local"` bajo el umbral 5). Sin herencia, sin `argparse`, sin red y sin shell: los objetos solo leen dicts locales y validan la misma frontera que la Sesión 16 enseñó.

Tres precisiones y nada más:

- Clase contra objeto: la clase es el molde (`ManualFinding`, `Finding`); el objeto es cada hallazgo construido (`ManualFinding(1, ...)`, `Finding.model_validate(...)`). `__init__` recibe los datos y `self` los guarda como atributos; los métodos leen `self` para resumir o clasificar.
- Manual contra validado: la clase manual acepta lo que su `__init__` revisa a mano (y deja pasar el id `"7"` y el mensaje de 200 caracteres); el `BaseModel` rechaza ambos en la frontera con `ValidationError` por campo. Por eso la migración mantiene las 3 pruebas en verde: el caso válido sigue aceptado y el inválido ahora trae motivo.
- Corredores: `unittest` viene en la biblioteca estándar y siempre funciona (base garantizada para la nota); `pytest` (opcional, `pip install pytest`) ejecuta el mismo `test_modelo.py` con salida más legible. Si `pytest` no está instalado, `unittest` en verde vale el 100%.

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

# 4. Crea manualmente los archivos nuevos (el lote S17 queda intacto)
notepad finding_model.py
notepad test_modelo.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python finding_model.py
python -m unittest test_modelo.py -v
pytest test_modelo.py -v
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

# 4. Crea manualmente los archivos nuevos (el lote S17 queda intacto)
touch finding_model.py test_modelo.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python3 finding_model.py
python3 -m unittest test_modelo.py -v
pytest test_modelo.py -v
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

# 4. Crea manualmente los archivos nuevos (el lote S17 queda intacto)
touch finding_model.py test_modelo.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python3 finding_model.py
python3 -m unittest test_modelo.py -v
pytest test_modelo.py -v
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

Debes ver el prefijo `(.venv)` en el prompt, la versión Python 3.13.x y Pydantic 2.x. (`pytest` es opcional: suma legibilidad, nunca es requisito para aprobar.) Después crea `finding_model.py` con los 6 dicts de la tabla de abajo y `test_modelo.py` con las 3 pruebas.

## Ejercicio obligatorio

Crea `finding_model.py` con evidencia arriba, tareas modeladas en medio y reporte modelado al final (sin herencia, sin `argparse`, sin red, sin shell, sin Pi) que haga lo siguiente:

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 6 dicts y tu identidad; ancla el contrato local | `FINDING_THRESHOLD = 5`, `sample_records` (6 dicts: 3 INFO, 1 WARNING, 2 ERROR), `student_name`, `student_id`, `ALLOWED_LEVELS` |
| 2. Modelado | Construye la clase manual, evoluciona al `BaseModel` y agrupa en el reporte | `ManualFinding(...)` → `summary()`/`is_critical()`; `Finding.model_validate(...)` → acepta válido; `build_validated_batch(...)` → 6 más 0; lax `"7"` → `7`; `strict=True` rechaza |
| 3. Comunicación | Imprime las 5 líneas modeladas, el par de errores contra el umbral, la nota de evolución y el alcance | `print()` línea por línea |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`. La suite de referencia está en `test_modelo.py` (3 pruebas `unittest`, compatible con `pytest`).

## Entrada sintética y tablas de revisión (léelas antes de programar)

```python
FINDING_THRESHOLD = 5
sample_records = [
    # 1, 4, 6: INFO (3 en total).
    # 2: WARNING (1 en total).
    # 3, 5: ERROR (2 en total, bajo el umbral: Rutina local).
]
```

| Revisión modelada | Prueba que la encierra | Par |
|---------|-------|-----|
| Anatomía manual (resumen + crítica) | `test_manual_finding_summarizes_and_classifies` (normal) | (`[INFO]...`, `False`) |
| Registro válido aceptado exacto | `test_validated_finding_accepts_valid_record` (aceptación Pydantic) | (`1`, campos exactos) |
| Mensaje vacío rechazado con motivo + id texto | `test_validated_finding_rejects_empty_message_and_strict_text_id` (rechazo + strict) | (`ValidationError` que nombra `message`; `"7"` → `7`; `strict=True` lanza) |

Totales esperados: `3` pruebas, `3` en verde, `0` errores de suite; `2` errores aceptados con `"Rutina local"`. Con 5 o más el veredicto sería `"Revisión prioritaria"`.

### Tabla de pruebas (contrato de la suite)

| # | Prueba | Tipo | Qué encierra |
|---|--------|------|--------------|
| 1 | `test_manual_finding_summarizes_and_classifies` | normal | `ManualFinding(1, ...)` resume `[INFO]` y no es crítico |
| 2 | `test_validated_finding_accepts_valid_record` | aceptación Pydantic | `Finding.model_validate` conserva `1` y campos exactos |
| 3 | `test_validated_finding_rejects_empty_message_and_strict_text_id` | rechazo + strict | `message` vacío lanza `ValidationError`; `"7"` → `7` en lax y lanza con `strict=True` |

> Nota de fidelidad del respaldo: la suite conserva 1 prueba manual más 1 de aceptación y 1 de rechazo Pydantic (con frontera strict incluida) para reproducir el reporte esperado oficial, que es el contrato que la referencia debe cumplir. Cada prueba sigue arrange-act-assert y cada assert lleva mensaje.

## Salida esperada

Ejecuta tu archivo desde la raíz del proyecto y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Pruebas del modelo: 3/3 en verde (unittest)
Conteo por nivel: INFO=3 WARNING=1 ERROR=2
Errores (aceptados): 2 - Rutina local
Clase manual: resumen() e is_critical() en verde
Modelo validado: Field (1..140) y strict en verde
--- Reporte probado ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Evolucion: manual (__init__) -> BaseModel (Field + strict)
Alcance: localhost (127.0.0.1) y fixtures locales
```

Y la suite debe responder así (el tiempo exacto varía por equipo; lo que debe coincidir es `3 tests` y `OK`):

```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

Con `pytest` instalado, la misma suite responde con 3 nodos en verde (`3 passed`); sin `pytest`, el bloque `unittest` de arriba vale el 100% de la nota.

Convención de predicción previa: antes de completar cada TODO, el estudiante escribe su predicción (valor esperado y motivo); solo después de ejecutar el script compara el resultado obtenido con su predicción y con la salida esperada (predecir → ejecutar → comparar).

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El lote modelado **convierte eventos sueltos en hallazgos firmables sin ejecutar nada fuera de la máquina**: 6 dicts validados, conteo por nivel, par contra el umbral y una evolución documentada de clase manual a esquema validado. No abre puertos, no toca red y no confirma un incidente. Los objetos encierran el comportamiento de hoy; no certifican cambios futuros ni sustituyen leer el código, revisar el alcance ni repetir la suite tras cada edición. Pydantic valida en la frontera donde lo colocas; no garantiza los tipos del resto del programa.

## Nota precisa sobre errores con clases y modelos

Errores que verás en esta sesión:

- `AttributeError: 'Finding' object has no attribute 'mesage'`: escribiste `finding.mesage` en vez de `finding.message` y el objeto no inventa atributos. La causa es un nombre mal escrito, no un hallazgo roto. La corrección es completar con `Tab` (`finding.me` + `Tab`), re-ejecutar con `↑` y leer la sugerencia (`Did you mean: 'message'?`).
- `ValidationError` que la clase manual dejó pasar: construiste `ManualFinding(9, "INFO", "x"*200, ...)` sin protesta, pero `Finding.model_validate` del mismo dict lanza `String should have at most 140 characters`. La causa es una validación manual débil (sin tope de longitud), no un dato correcto. La corrección es acotar el mensaje antes de validar, re-ejecutar con `↑` y comparar ambos mensajes de error.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, clases nuevas, rutas y comentarios) se escribe en inglés (`sample_records`, `ManualFinding`, `Finding`, `summary`, `is_critical`, `FINDING_THRESHOLD`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario y los mensajes de cada assert se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`; las constantes usan `UPPER_CASE`; las clases usan `PascalCase`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué guarda `__init__` en `self` y qué leen `summary()` e `is_critical()` desde `self`.
- [ ] Qué atributo es público (`finding.message`) y cuál es privado por convención (`_label`) y por qué no se lee desde fuera.
- [ ] Qué deja pasar la clase manual (id `"7"`, mensaje de 200 caracteres) y qué rechaza el `BaseModel` con `ValidationError` por campo.
- [ ] Qué convierte el modo lax (`"7"` → `7`), qué rechaza `strict=True` sobre el mismo dict y cómo lo espera cada prueba (`assertEqual` contra `assertRaises`).
- [ ] Por qué la migración mantiene las 3 pruebas en verde (el válido sigue aceptado; el inválido ahora trae motivo).
- [ ] Qué corredor garantiza tu nota (`unittest`, biblioteca estándar) y qué aporta el opcional (`pytest`, legibilidad).
- [ ] Qué NO garantizan las 3 pruebas ni Pydantic (no certifican cambios futuros; tras cada edición se repite la suite).
- [ ] Tu programa se ejecuta desde la raíz sin errores y muestra reporte modelado, suite 3/3 y alcance.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, sin sintaxis nueva: agrega un método `short_label()` a `ManualFinding` que devuelva `"INFO-1"` para el hallazgo 1 y predice en papel el valor antes de ejecutar con `↑`. Después valida el dict con `message` de exactamente 140 caracteres (debe aceptarse) y con 141 (debe rechazarse con `ValidationError` que nombra `message`). Es solo práctica extra: no cambia tu calificación. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`finding_shift.py`), distinto del `finding_model.py` de clase y del desafío opcional de arriba.

**Historia:** dejas modelado el turno nocturno antes de entregarlo, distinto del lote del día de clase. Partes de 6 dicts nuevos del turno, reutilizas la misma técnica modelada con umbral propio, verificas con cuatro chequeos con mensaje y muestras el reporte con el mismo alcance local.

Crea manualmente `finding_shift.py` en tu proyecto personal, reutilizando evidencia arriba, tareas modeladas en medio y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 6 del turno y tu identidad; imprime el total (`6`) | `SHIFT_THRESHOLD = 3`, `shift_records` (6 dicts: 3 exactos, 1 lax `"24"`, 2 inválidos), `student_name`, `student_id` |
| 2. Modelado | Reutiliza `Finding`, `validate_shift_records` y `count_by_level` bajo `main()` con cuatro asserts con mensaje | `validate_shift_records(...)` → 4 más 2; lax `"24"` → `24`; conteos `2, 1, 1`; veredicto bajo el umbral |
| 3. Comunicación | Reporte modelado del turno con el par, los conteos y los chequeos | `print()` línea por línea |

Los 6 dicts del turno (escríbelos tal cual; el registro 4 usa texto numérico `"24"` y los registros 5–6 son inválidos):

```python
SHIFT_THRESHOLD = 3
shift_records = [
    {"finding_id": 21, "level": "INFO", "message": "ronda nocturna iniciada en localhost", "source": "sensor-a"},
    {"finding_id": 22, "level": "WARNING", "message": "latencia nocturna alta en loopback", "source": "sensor-b"},
    {"finding_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"finding_id": "24", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"},
    {"finding_id": 25, "level": "INFO", "message": "", "source": "sensor-a"},
    {"finding_id": 26, "level": "DEBUG", "message": "nivel nocturno inventado", "source": "sensor-b"},
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Turno leido: 6
Turno aceptado: 4
Turno rechazado: 2
Errores (aceptados): 1 - Rutina local
Chequeos del turno: 4/4 en verde (asserts con mensaje)
--- Reporte probado (turno) ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 3 (solo lectura)
Evolucion: manual (__init__) -> BaseModel (Field + strict)
Alcance: localhost (127.0.0.1) y fixtures locales
```

> Notas de respaldo: el bloque de resumen replica la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los pares deben coincidir (4 aceptados con `2, 1, 1`; 1 error bajo el umbral 3).

**Antes de programar, analiza:** qué llamada modelada separa aceptados de rechazados y qué veredicto le toca a 1 error bajo el umbral; qué llamada convierte el texto numérico en modo lax y dónde viaja cada motivo en vez de una traza.

**Propósito real:** el modelo convierte filas del turno en hallazgos citables para el tablero local: no abre puertos, no toca red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena datos del turno → chequeos modelados → reporte. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos. Ningún script de la sesión abre sockets ni envía tráfico: solo define clases, valida dicts locales e imprime el reporte en tu consola. Sin Pi en esta sesión: cada línea la escribes, la predices y la explicas tú.
