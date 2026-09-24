# Sesión 17: Testing con unittest y pytest

Bienvenido a la **Sesión 17** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **escribir 6 pruebas (normales, bordes, errores) con `unittest` que pasan en verde, re-ejecutarlas con `pytest` cuando está instalado, ordenar cada prueba en arrange-act-assert, aplicar el ciclo rojo-verde-refactor, y probar validadores Pydantic con `assertRaises(ValidationError)` comparando el modo lax (convierte `"15"` a `15`) contra `strict=True` (rechaza la conversión)**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x) y Pydantic v2 (`python -c "import pydantic; print(pydantic.VERSION)"` debe responder `2.x`).
3. Mantén intacto el lote `validate_events.py` de la Sesión 16 y crea el controlador `review_batch.py` más su suite `test_review.py`.
4. Ejecuta `python review_batch.py` desde la raíz del proyecto y verifica el reporte probado; luego ejecuta `python -m unittest test_review.py -v` (6/6 en verde) y, si está instalado, `pytest test_review.py -v`.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

15 min encuadre y anatomía de la prueba (por qué probar, arrange-act-assert) · 10 min demo en vivo rojo-verde-refactor con `ValidationError` · 25 min práctica con `review_batch.py`, 6 pruebas y ambos corredores · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que entrega eventos probados al tablero del siguiente turno sin que nadie consuma una cifra sin verificar. Recibes **10 dicts** en el lote de revisión, un umbral de 5 y **el lote `validate_events.py` heredado de la Sesión 16**: cuentas aceptados por nivel con `contar_por_nivel`, revisas la config local con `validar_config`, repites la frontera `Evento` con `model_validate` (lax contra `strict=True`), y encierras todo en **6 pruebas** que corren en verde con `unittest` y se re-ejecutan con `pytest`. En la Sesión 16 los datos quedaron validados; hoy además cada cifra queda probada y repetible.

## Secuencia conceptual

Cada lote probado del programa sigue este orden explícito:

1. **Evidencia:** `REVIEW_THRESHOLD = 5`, `sample_events` (10 dicts) y tu identidad.
2. **Conteo probado:** `contar_por_nivel(sample_events)` → `INFO=4, WARNING=3, ERROR=3` (pruebas 1–3: mixto, vacío, niveles ignorados).
3. **Config probada:** `validar_config(18080, "INFO")` → `True`; puerto 0 y `DEBUG` → `False` (prueba 4: normal más bordes).
4. **Frontera repetida:** `Evento.model_validate(...)` acepta `"15"` → `15` en lax y lo rechaza con `strict=True` (prueba 5: aceptación Pydantic).
5. **Rechazo esperado:** el dict sin `level` lanza `ValidationError` capturada con `assertRaises` (prueba 6: rechazo Pydantic).
6. **Reporte probado:** par de errores contra el umbral, nota de corredores y alcance local.

## Cómo se prueba en el límite (en clase, sin evaluar nada más)

El TestCase ordena cada prueba en arrange-act-assert; cada assert lleva mensaje en español; `unittest` es la base garantizada y `pytest` re-ejecuta el mismo archivo con salida más legible:

```python
import unittest
from solution import Evento, contar_por_nivel, sample_events, validar_config
from pydantic import ValidationError


class TestReviewBatch(unittest.TestCase):
    """Six local checks: three for counts and config, three for the boundary."""

    def test_count_mixed_levels(self):
        # Arrange: ten local dicts with 4 INFO, 3 WARNING, 3 ERROR.
        batch = list(sample_events)
        # Act: count the batch by level.
        counts = contar_por_nivel(batch)
        # Assert: exact counts, so a lost row turns the test red.
        self.assertEqual(
            counts,
            {"INFO": 4, "WARNING": 3, "ERROR": 3},
            "Se esperaban 4 INFO, 3 WARNING y 3 ERROR en el lote de 10",
        )
```

```python
# Aceptacion lax: el texto numerico entra convertido.
event = Evento.model_validate({"event_id": "15", ...})
assert event.event_id == 15
# El mismo dict se rechaza cuando strict prohibe la conversion.
Evento.model_validate({"event_id": "15", ...}, strict=True)  # lanza ValidationError
```

```python
# Rechazo esperado: el dict sin level lanza, nunca interrumpe.
with self.assertRaises(ValidationError, msg="El registro sin level debia rechazarse"):
    Evento.model_validate({"event_id": 16, "message": "linea sin nivel", "source": "sensor-a"})
```

Con los 10 dicts de la práctica, `contar_por_nivel` devuelve `INFO=4, WARNING=3, ERROR=3` (3 errores → `"Rutina local"` bajo el umbral 5). Sin clases de dominio nuevas, sin `argparse`, sin red y sin shell: las pruebas solo leen dicts locales y validan la misma frontera de la Sesión 16.

Tres precisiones y nada más:

- Arrange-act-assert: cada prueba prepara datos (arrange), ejecuta una sola acción (act) y comprueba un solo veredicto (assert). Una prueba con dos acciones esconde dos veredictos; se divide en dos pruebas.
- Rojo-verde-refactor: primero se escribe la prueba y se ve fallar (rojo), después se corrige el código hasta verla pasar (verde), y al final se limpia sin romper el verde (refactor). El demo de clase lo muestra con el conteo vacío.
- Corredores: `unittest` viene en la biblioteca estándar y siempre funciona (base garantizada para la nota); `pytest` (opcional, `pip install pytest`) ejecuta el mismo `test_review.py` con salida más legible. Si `pytest` no está instalado, `unittest` en verde vale el 100%.

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

# 4. Crea manualmente los archivos nuevos (el lote S16 queda intacto)
notepad review_batch.py
notepad test_review.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python review_batch.py
python -m unittest test_review.py -v
pytest test_review.py -v
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

# 4. Crea manualmente los archivos nuevos (el lote S16 queda intacto)
touch review_batch.py test_review.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python3 review_batch.py
python3 -m unittest test_review.py -v
pytest test_review.py -v
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

# 4. Crea manualmente los archivos nuevos (el lote S16 queda intacto)
touch review_batch.py test_review.py

# 5. Ejecuta desde la raíz y verifica el reporte más la suite
python3 review_batch.py
python3 -m unittest test_review.py -v
pytest test_review.py -v
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

Debes ver el prefijo `(.venv)` en el prompt, la versión Python 3.13.x y Pydantic 2.x. (`pytest` es opcional: suma legibilidad, nunca es requisito para aprobar.) Después crea `review_batch.py` con los 10 dicts de la tabla de abajo y `test_review.py` con las 6 pruebas.

## Ejercicio obligatorio

Crea `review_batch.py` con evidencia arriba, tareas probadas en medio y reporte probado al final (sin clases de dominio, sin `argparse`, sin red, sin shell) que haga lo siguiente:

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 10 dicts y tu identidad; ancla el contrato local | `REVIEW_THRESHOLD = 5`, `sample_events` (10 dicts: 4 INFO, 3 WARNING, 3 ERROR), `student_name`, `student_id`, `ALLOWED_LEVELS` |
| 2. Probado | Cuenta por nivel, revisa la config, repite lax contra strict y publica el veredicto | `contar_por_nivel(...)` → 4/3/3; `validar_config(...)` → `True`/`False`; `describe_batch(...)` → conteos, par, pruebas lax/strict |
| 3. Comunicación | Imprime las 6 líneas probadas, el par de errores contra el umbral, la nota de corredores y el alcance | `print()` línea por línea |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`. La suite de referencia está en `test_review.py` (6 pruebas `unittest`, compatible con `pytest`).

## Entrada sintética y tablas de revisión (léelas antes de programar)

```python
REVIEW_THRESHOLD = 5
sample_events = [
    # 1, 4, 7, 10: INFO (4 en total).
    # 2, 6, 8: WARNING (3 en total).
    # 3, 5, 9: ERROR (3 en total, bajo el umbral: Rutina local).
]
```

| Revisión probada | Prueba que la encierra | Par |
|---------|-------|-----|
| Conteo mixto del lote | `test_count_mixed_levels` (normal) | (`4, 3, 3`, exactos) |
| Lote vacío como borde inferior | `test_count_empty_batch` (borde) | (`0, 0, 0`, sin claves faltantes) |
| Niveles desconocidos ignorados | `test_count_ignores_unknown_level` (borde) | (`DEBUG` y sin nivel no cuentan) |
| Config local aceptada y bordes fuera | `test_config_allows_local_review` (normal + bordes) | (`18080/INFO` sí; puerto 0 y `DEBUG` no) |
| Frontera aceptada en lax, rechazada en strict | `test_evento_accepts_lax_numeric_string` (aceptación Pydantic) | (`"15"` → `15`; `strict=True` lanza) |
| Registro sin nivel rechazado con motivo | `test_evento_rejects_missing_level` (rechazo Pydantic) | (`ValidationError` que nombra `level`) |

Totales esperados: `6` pruebas, `6` en verde, `0` errores de suite; `3` errores aceptados con `"Rutina local"`. Con 5 o más el veredicto sería `"Revisión prioritaria"`.

### Tabla de pruebas (contrato de la suite)

| # | Prueba | Tipo | Qué encierra |
|---|--------|------|--------------|
| 1 | `test_count_mixed_levels` | normal | `contar_por_nivel` sobre 10 dicts → `4, 3, 3` exactos |
| 2 | `test_count_empty_batch` | borde | `contar_por_nivel([])` → `0, 0, 0` sin claves faltantes |
| 3 | `test_count_ignores_unknown_level` | borde | `DEBUG` y fila sin nivel no inflan ningún contador |
| 4 | `test_config_allows_local_review` | normal + bordes | `(18080, INFO)` sí; puerto `0` y `DEBUG` no |
| 5 | `test_evento_accepts_lax_numeric_string` | aceptación Pydantic | lax convierte `"15"` → `15`; `strict=True` lanza `ValidationError` |
| 6 | `test_evento_rejects_missing_level` | rechazo Pydantic | dict sin `level` lanza `ValidationError` que nombra `level` |

> Nota de fidelidad del respaldo: la suite conserva 3 pruebas de conteo/config más 1 de aceptación y 1 de rechazo Pydantic (más la prueba 4 mixta) para reproducir el reporte esperado oficial, que es el contrato que la referencia debe cumplir. Cada prueba sigue arrange-act-assert y cada assert lleva mensaje.

## Salida esperada

Ejecuta tu archivo desde la raíz del proyecto y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Pruebas del lote: 6/6 en verde (unittest)
Conteo por nivel: INFO=4 WARNING=3 ERROR=3
Errores (aceptados): 3 - Rutina local
Config valida (18080, INFO): True
Evento aceptado (lax "15" -> 15): True
Evento rechazado (strict=True): True
--- Revision probada ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Corredores: unittest (base) + pytest (legible, opcional)
Alcance: localhost (127.0.0.1) y fixtures locales
```

Y la suite debe responder así (el tiempo exacto varía por equipo; lo que debe coincidir es `6 tests` y `OK`):

```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Con `pytest` instalado, la misma suite responde con 6 nodos en verde (`6 passed`); sin `pytest`, el bloque `unittest` de arriba vale el 100% de la nota.

Convención de predicción previa: antes de completar cada TODO, el estudiante escribe su predicción (valor esperado y motivo); solo después de ejecutar el script compara el resultado obtenido con su predicción y con la salida esperada (predecir → ejecutar → comparar).

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El lote probado **convierte cifras de turno en cifras verificadas sin ejecutar nada fuera de la máquina**: 10 dicts contados, config local revisada, frontera lax/strict repetida, 6 pruebas en verde y un par contra el umbral que el tablero puede citar. No abre puertos, no toca red y no confirma un incidente. Las pruebas encierran el comportamiento de hoy; no certifican cambios futuros ni sustituyen leer el código, revisar el alcance ni repetir la suite tras cada edición.

## Nota precisa sobre errores con pruebas y modelos

Errores que verás en esta sesión:

- `AssertionError` sin mensaje: escribiste `assertEqual(counts, {...})` sin el tercer argumento y la consola solo dice qué difiere, no qué esperabas. La causa es un assert mudo, no un fallo del lote. La corrección es agregar siempre el mensaje (`"Se esperaban 4 INFO..."`), re-ejecutar con `↑` y leer el motivo antes que el diff.
- `FAILED` que en realidad pasa por coincidencia: escribiste `assertIn("INFO", str(counts))` y pasa aunque los números estén mal, porque solo mira la palabra, no la cifra. La causa es una comprobación débil, no un lote correcto. La corrección es comparar el dict exacto con `assertEqual(counts, {"INFO": 4, ...})`, re-ejecutar con `↑` y confirmar que un conteo roto vuelve la prueba roja.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, funciones nuevas, rutas y comentarios) se escribe en inglés (`sample_events`, `TestReviewBatch`, `test_count_mixed_levels`, `error_total`, `ALLOWED_LEVELS`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Dos nombres se conservan por contrato del hilo curricular: la entidad `Evento` (mandato S16, esperada por las Sesiones 17–18) y las funciones `contar_por_nivel` y `validar_config` (hilo S05/S07/S11 que esta sesión prueba sin renombrar). Los mensajes para el usuario y los mensajes de cada assert se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`; las constantes usan `UPPER_CASE`; las clases de prueba usan `PascalCase`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué ordena cada prueba (arrange-act-assert) y qué pasa si una prueba ejecuta dos acciones en vez de una.
- [ ] Qué encierra cada prueba (conteo mixto, vacío, niveles ignorados, config, aceptación lax, rechazo) y qué tipo le toca (normal, borde, error).
- [ ] Qué convierte el modo lax (`"15"` → `15`), qué rechaza `strict=True` sobre el mismo dict y cómo lo espera cada prueba (`assertEqual` contra `assertRaises`).
- [ ] Por qué cada assert lleva mensaje y qué pierdes cuando el `AssertionError` llega mudo.
- [ ] Por qué `assertIn("INFO", str(counts))` pasa por coincidencia y qué comparación exacta lo reemplaza.
- [ ] Qué corredor garantiza tu nota (`unittest`, biblioteca estándar) y qué aporta el opcional (`pytest`, legibilidad).
- [ ] Qué NO garantizan las 6 pruebas (no certifican cambios futuros; tras cada edición se repite la suite).
- [ ] Tu programa se ejecuta desde la raíz sin errores y muestra reporte probado, suite 6/6 y alcance.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, sin sintaxis nueva: agrega una séptima prueba de borde que cuente el lote completo de la Sesión 16 (15 aceptados: 7 INFO, 5 WARNING, 3 ERROR) con `contar_por_nivel` y predice en papel el dict exacto antes de ejecutar con `↑`. Después agrega una prueba que confirme `validar_config(65535, "ERROR")` como borde superior permitido y `validar_config(65536, "ERROR")` como primer puerto rechazado. Es solo práctica extra: no cambia tu calificación. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`review_shift.py`), distinto del `review_batch.py` de clase y del desafío opcional de arriba.

**Historia:** dejas probado el turno nocturno antes de entregarlo, distinto del lote del día de clase. Partes de 10 dicts nuevos del turno, reutilizas la misma técnica probada con umbral propio, verificas con seis chequeos con mensaje y muestras el reporte con el mismo alcance local.

Crea manualmente `review_shift.py` en tu proyecto personal, reutilizando evidencia arriba, tareas probadas en medio y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 10 del turno y tu identidad; imprime el total (`10`) | `SHIFT_THRESHOLD = 3`, `shift_events` (10 dicts: 7 exactos, 1 lax `"28"`, 2 inválidos), `student_name`, `student_id` |
| 2. Probado | Reutiliza `Evento`, `validate_shift_records`, `contar_por_nivel` y `validar_config` bajo `main()` con seis asserts con mensaje | `validate_shift_records(...)` → 8 más 2; lax `"28"` → `28`; `strict=True` rechaza; conteos `4, 2, 2`; config `(18080, INFO)` |
| 3. Comunicación | Reporte probado del turno con el par, los conteos y los chequeos | `print()` línea por línea |

Los 10 dicts del turno (escríbelos tal cual; el registro 8 usa texto numérico `"28"` y los registros 9–10 son inválidos):

```python
SHIFT_THRESHOLD = 3
shift_events = [
    {"event_id": 21, "level": "INFO", "message": "ronda nocturna iniciada en localhost", "source": "sensor-a"},
    {"event_id": 22, "level": "WARNING", "message": "reintento nocturno local", "source": "sensor-b"},
    {"event_id": 23, "level": "ERROR", "message": "sensor local sin respuesta", "source": "sensor-a"},
    {"event_id": 24, "level": "INFO", "message": "bitacora nocturna verificada", "source": "sensor-b"},
    {"event_id": 25, "level": "ERROR", "message": "cola nocturna llena", "source": "sensor-a"},
    {"event_id": 26, "level": "WARNING", "message": "latencia nocturna alta", "source": "sensor-b"},
    {"event_id": 27, "level": "INFO", "message": "respaldo nocturno completado", "source": "sensor-a"},
    {"event_id": "28", "level": "INFO", "message": "inventario nocturno actualizado", "source": "sensor-b"},
    {"event_id": 29, "message": "linea nocturna sin nivel", "source": "sensor-a"},
    {"event_id": 30, "level": "DEBUG", "message": "nivel nocturno inventado", "source": "sensor-b"},
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Turno leido: 10
Turno aceptado: 8
Turno rechazado: 2
Errores (aceptados): 2 - Rutina local
Chequeos del turno: 6/6 en verde (asserts con mensaje)
--- Revision probada (turno) ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 3 (solo lectura)
Corredores: unittest (base) + pytest (legible, opcional)
Alcance: localhost (127.0.0.1) y fixtures locales
```

> Notas de respaldo: el bloque de resumen replica la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los pares deben coincidir (8 aceptados con `4, 2, 2`; 2 errores bajo el umbral 3).

**Antes de programar, analiza:** qué llamada probada separa aceptados de rechazados y qué veredicto le toca a 2 errores bajo el umbral; qué llamada convierte el texto numérico en modo lax y cuál la rechaza con `strict=True`; qué llamada de conteo ignora niveles inventados y dónde viaja cada motivo en vez de una traza.

**Propósito real:** la suite convierte cifras de turno en cifras citables para el tablero local: no abre puertos, no toca red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena datos del turno → chequeos probados → reporte. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos. Ningún script de la sesión abre sockets ni envía tráfico: solo define funciones, valida dicts locales e imprime el reporte en tu consola.
