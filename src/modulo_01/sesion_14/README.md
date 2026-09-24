# Sesión 14: Módulos, paquetes, pip, venv y Pydantic fijado

Bienvenido a la **Sesión 14** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **organizar el conteo y el filtrado heredados en un paquete `kit/` de dos módulos, importarlo de tres formas, instalar `pydantic>=2.0,<3` en tu `venv` y probar la reproducibilidad con `pip freeze` y la versión instalada**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el paquete `kit/` (`kit/__init__.py`, `kit/count_kit.py`, `kit/filter_kit.py`), el archivo `requirements.txt` y el controlador `pack_review.py`.
4. Instala con `pip install -r requirements.txt` y ejecuta `python pack_review.py` desde la raíz del proyecto.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

15 min encuadre y anatomía módulo-paquete-venv · 10 min demo en vivo con error de importación · 25 min práctica con `pack_review.py` y `pip freeze` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que entrega número y letrero juntos sin que nada interrumpa el cambio de turno. Recibes **20 eventos**, un umbral de 5 y **2 funciones heredadas** de las Sesiones 11 a 13 (conteo y filtrado): las mudas a dos módulos del paquete `kit/`, las alcanzas desde `pack_review.py` con **3 formas de importar**, instalas **Pydantic 2.x fijado** en tu `venv` y anuncias `BaseModel` sin modelar todavía (llega en la Sesión 16). En la Sesión 13 el dato imperfecto bastaba; hoy además el entorno entero es reproducible.

## Secuencia conceptual

Cada revisión empaquetada del programa sigue este orden explícito:

1. **Evidencia:** `REVIEW_THRESHOLD = 5`, `event_log` (20 textos) y tu identidad.
2. **Tarea empaquetada:** `count_events(event_log)` → (`6`, prioritaria) para `ERROR`.
3. **Segunda tarea:** `count_events(event_log, "WARNING")` → (`5`, prioritaria).
4. **Filtro empaquetado:** `filter_events(event_log, "ERROR")` → 6 de 20.
5. **Reporte fijado:** paquete, versión de Pydantic con su pin, contexto `__main__` y entorno `venv`.

## Cómo empaqueta Python (en clase, sin evaluar nada más)

Un módulo es un archivo `.py`; un paquete es una carpeta con `__init__.py`; el controlador solo corre su trabajo cuando se ejecuta directo:

```python
# kit/count_kit.py (modulo 1: reutiliza la Sesion 11)
REVIEW_THRESHOLD = 5

def count_events(events, level="ERROR"):
    """Return count and verdict for the given level."""
    total = events.count(level)
    if total >= REVIEW_THRESHOLD:
        verdict = "Revisión prioritaria"
    else:
        verdict = "Rutina local"
    return total, verdict
```

```python
# kit/filter_kit.py (modulo 2: reutiliza la Sesion 12)
def filter_events(events, level="ERROR"):
    """Return the list of events matching the given level."""
    matched = []
    for event in events:
        if event == level:
            matched.append(event)
    return matched
```

```python
# kit/__init__.py (portada del paquete)
"""Local defensive review kit: count plus filter, no network."""
KIT_VERSION = "1.0.0"

from kit.count_kit import REVIEW_THRESHOLD, count_events
from kit.filter_kit import filter_events
```

Las 3 formas de importar, todas en `pack_review.py` desde la raíz del proyecto:

```python
import kit.count_kit            # forma 1: ruta completa al modulo
from kit.count_kit import count_events   # forma 2: funcion directa
from kit import filter_kit      # forma 3: modulo desde el paquete
```

Y la guardia que distingue ejecución directa de importación:

```python
def main():
    """Run the packaged review from the project root."""

if __name__ == "__main__":
    main()
```

Con los 20 eventos de la práctica, `count_events(event_log)` devuelve `(6, "Revisión prioritaria")` por defecto. Con `count_events(event_log, "WARNING")` devuelve `(5, "Revisión prioritaria")`. Con `filter_events(event_log, "ERROR")` devuelve la lista de 6 coincidencias. Pydantic solo se importa y se anuncia: `import pydantic` más `pydantic.VERSION`; ningún modelo se define hasta la Sesión 16.

Tres precisiones y nada más:

- Paquete: la carpeta `kit/` sin `__init__.py` no es paquete y el `import` falla; el controlador siempre se ejecuta desde la raíz para que la ruta al paquete exista.
- `venv`: solo aísla dependencias Python, no es sandbox de seguridad; la protección real siguen siendo loopback, allowlist, límites y limpieza.
- Pin compatible: `requirements.txt` contiene `pydantic>=2.0,<3`; `pip freeze` congela lo instalado (serie 2.x) y la versión impresa lo prueba.

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

# 4. Crea manualmente el paquete y los archivos nuevos
mkdir kit
notepad kit\__init__.py
notepad kit\count_kit.py
notepad kit\filter_kit.py
notepad requirements.txt
notepad pack_review.py

# 5. Instala dependencias fijadas y ejecuta desde la raíz
pip install -r requirements.txt
python pack_review.py

# 6. Congela lo instalado como prueba de reproducibilidad
pip freeze
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

# 4. Crea manualmente el paquete y los archivos nuevos
mkdir -p kit
touch kit/__init__.py kit/count_kit.py kit/filter_kit.py requirements.txt pack_review.py

# 5. Instala dependencias fijadas y ejecuta desde la raíz
pip install -r requirements.txt
python3 pack_review.py

# 6. Congela lo instalado como prueba de reproducibilidad
pip freeze
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

# 4. Crea manualmente el paquete y los archivos nuevos
mkdir -p kit
touch kit/__init__.py kit/count_kit.py kit/filter_kit.py requirements.txt pack_review.py

# 5. Instala dependencias fijadas y ejecuta desde la raíz
pip install -r requirements.txt
python3 pack_review.py

# 6. Congela lo instalado como prueba de reproducibilidad
pip freeze
```

> Desarrollo local en macOS con `python3`. La validación final del laboratorio se realiza en Windows con `python`.

Contenido exacto de `requirements.txt` (una sola línea fijada):

```text
pydantic>=2.0,<3
```

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

Debes ver el prefijo `(.venv)` en el prompt y la versión Python 3.13.x. Después instala con `pip install -r requirements.txt` una vez creado el archivo.

## Ejercicio obligatorio

Crea `pack_review.py` más el paquete `kit/` con evidencia arriba, tareas empaquetadas en medio, llamadas desempaquetadas bajo la guardia `__main__` y reporte fijado al final (sin modelar con Pydantic, sin clases de dominio, sin red, sin shell) que haga lo siguiente:

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, la lista de 20 y tu identidad; imprime el total (`20`) | `REVIEW_THRESHOLD = 5`, `event_log` (20 textos: 6 `ERROR`, 5 `WARNING`), `student_name`, `student_id` |
| 2. Empaquetado | Define `count_events` (módulo conteo), `filter_events` (módulo filtro) y `main()` bajo `if __name__ == "__main__"`; usa las 3 formas de importar; desempaqueta los dos pares | `count_events(event_log)` → par; `count_events(event_log, "WARNING")` → par; `filter_events(event_log, "ERROR")` → lista de 6 |
| 3. Comunicación | Imprime el encabezado con los dos pares, el filtro, el paquete, Pydantic con su pin, el contexto y el entorno | Encabezado más pares, paquete `kit`, versión instalada, `__main__` y `venv` declarados |

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

| Llamada empaquetada | Importación que la alcanza | Par |
|---------|-------|-----|
| `count_events(event_log)` | `from kit.count_kit import count_events` | (`6`, prioritaria) |
| `count_events(event_log, "WARNING")` | `import kit.count_kit` + ruta completa | (`5`, prioritaria) |
| `filter_events(event_log, "ERROR")` | `from kit import filter_kit` | lista de 6 (6 de 20) |

Totales esperados: `6` con `"Revisión prioritaria"` para errores; `5` con `"Revisión prioritaria"` para avisos; filtro con 6 coincidencias de 20. Con 4 o menos el veredicto sería `"Rutina local"`.

> Nota de fidelidad del respaldo: la lista de 20 posiciones conserva 6 `ERROR` y 5 `WARNING` para reproducir la salida esperada oficial, que es el contrato que la referencia debe cumplir. `solution.py` modela la misma lógica de forma autocontenida; en tu proyecto esa lógica vive en los dos módulos de `kit/`.

## Salida esperada

Ejecuta tu archivo desde la raíz del proyecto y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Eventos registrados: 20
Errores: 6 - Revisión prioritaria
Avisos: 5 - Revisión prioritaria
Filtrados ERROR: 6 de 20
Paquete: kit (count_kit + filter_kit, 3 importaciones)
Pydantic: 2.13.4 (pin pydantic>=2.0,<3)
Contexto: __main__ (ejecucion directa)
--- Revisión empaquetada ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Entorno: venv (.venv) con requirements fijados
Modelos: BaseModel llega en S16 (hoy solo instalacion)
```

> Tu número de parche de Pydantic puede variar dentro de la serie 2.x (por ejemplo 2.10.x); lo obligatorio es que empiece con `2.` y que `pip freeze` lo congele. Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: dos hallazgos empaquetados, un filtro, tres pruebas de entorno más un encabezado y cinco líneas de datos.

Y `pip freeze` debe congelar la serie fijada (extracto; el resto de tu `freeze` depende de tu máquina):

```text
annotated-types==0.7.0
pydantic==2.13.4
pydantic_core==2.46.4
typing_extensions==4.15.0
```

Convención de predicción previa: antes de completar cada TODO, el estudiante escribe su predicción (valor esperado y motivo); solo después de ejecutar el script compara el resultado obtenido con su predicción y con la salida esperada (predecir → ejecutar → comparar).

## Nota precisa sobre lo que el programa sí hace y lo que no hace

La revisión empaquetada **organiza el conteo local para el cambio de turno con dependencias reproducibles**: dos pares empaquetados, un filtro y tres pruebas de entorno (`kit`, Pydantic fijado, `__main__`). No abre puertos, no toca red y no confirma un incidente. Pydantic queda instalado y anunciado; ningún modelo se define hasta la Sesión 16.

## Nota precisa sobre errores con paquetes y venv

Errores que verás en esta sesión:

- `ModuleNotFoundError: No module named 'kit'`: importaste el paquete fuera de la raíz del proyecto o `kit/` no tiene `__init__.py`; Python señala el nombre que no encontró en la ruta. La corrección es verificar con `dir` o `ls` que `kit/__init__.py` existe, volver a la raíz con `cd` y re-ejecutar con `↑`.
- `pip freeze` sin Pydantic (o con serie 1.x): congelaste el Python global porque olvidaste activar `.venv`, o instalaste sin el pin compatible. La corrección es activar el entorno (el prompt debe mostrar `(.venv)`), ejecutar `pip install -r requirements.txt` con el pin `pydantic>=2.0,<3` y repetir `pip freeze` hasta ver la serie 2.x.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, funciones, módulos y comentarios) se escribe en inglés (`event_log`, `count_events`, `filter_kit`, `REVIEW_THRESHOLD`, `error_total`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`; los módulos usan nombres cortos en minúsculas).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué contiene cada módulo de `kit/` y qué reutiliza de las Sesiones 11 a 13.
- [ ] Qué par devuelve cada llamada empaquetada y qué veredicto le toca.
- [ ] Las 3 formas de importar y cuándo conviene cada una.
- [ ] Qué imprime la guardia `__main__` y qué pasaría al importar el controlador como módulo.
- [ ] Qué congela `pip freeze` y por qué el pin es `pydantic>=2.0,<3`.
- [ ] Por qué el `venv` no es un sandbox de seguridad.
- [ ] Qué NO hace el programa (no modela con Pydantic aún, no abre puertos, no toca red, no confirma un incidente).
- [ ] Tu programa se ejecuta desde la raíz sin errores y muestra los dos hallazgos, el filtro y las tres pruebas de entorno.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, sin sintaxis nueva: cuenta el tercer nivel con `count_events(event_log, "INFO")` y predice en papel el par antes de ejecutar con `↑` (pista: hay 9 `INFO`, así que también alcanza el umbral). Después ejecuta `python pack_review.py` desde una subcarpeta y predice qué `ModuleNotFoundError` obtendrás y por qué. Es solo práctica extra: no cambia tu calificación. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`pack_shift.py`), distinto del `pack_review.py` de clase y del desafío opcional de arriba.

**Historia:** dejas lista la revisión empaquetada del turno antes de entregarla, distinta de la revisión del día de clase. Partes de 20 eventos nuevos del turno, reutilizas el mismo paquete `kit/` con umbral propio, desempaquetas los dos pares bajo la guardia `__main__` y muestras el reporte con el mismo `requirements.txt` fijado.

Crea manualmente `pack_shift.py` en tu proyecto personal, reutilizando `kit/` con umbral arriba, tareas en medio y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 20 del turno y tu identidad; imprime el total (`20`) | `SHIFT_THRESHOLD = 5`, `shift_events` (20 textos: 7 `WARNING`, 4 `ERROR`), `student_name`, `student_id` |
| 2. Empaquetado | Reutiliza `count_shift` y `filter_shift` bajo `main()` con la guardia; desempaqueta los dos pares | `count_shift(shift_events, "WARNING")` → par; `count_shift(shift_events, "ERROR")` → par; `filter_shift(shift_events, "WARNING")` → lista de 7 |
| 3. Comunicación | Reporte empaquetado del turno con los dos pares, el filtro y el entorno fijado | `print()` línea por línea |

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
Filtrados WARNING: 7 de 20
Paquete: kit (count_kit + filter_kit, 3 importaciones)
Pydantic: 2.13.4 (pin pydantic>=2.0,<3)
Contexto: __main__ (ejecucion directa)
--- Revisión empaquetada del turno ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Entorno: venv (.venv) con requirements fijados
Modelos: BaseModel llega en S16 (hoy solo instalacion)
```

> Notas de respaldo: el bloque de resumen replica la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los pares deben coincidir.

**Antes de programar, analiza:** qué llamada empaquetada revisa el nivel de avisos y qué veredicto le toca sobre el umbral; qué par devuelve la llamada de errores y por qué queda en rutina; qué filtro cuenta las 7 coincidencias y dónde viaja la versión de Pydantic en vez de un modelo.

**Propósito real:** la revisión organiza el conteo local para el cambio de turno con dependencias reproducibles: no abre puertos, no toca red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena módulo → importación → venv → freeze. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos. `pip install` solo descarga el paquete fijado desde el índice oficial; ningún script de la sesión abre sockets ni envía tráfico.
