# Sesión 12: Funciones II y ámbitos del revisor local

Bienvenido a la **Sesión 12** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **devolver conteo y veredicto juntos con retorno múltiple, usar un parámetro por defecto y distinguir la variable local de la global sin abusar de `global`**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `scope_review.py` y escribe el ejercicio.
4. Ejecuta `python scope_review.py` y comprueba la revisión con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `scope_review.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que entrega número y letrero juntos. Recibes **20 eventos** y un umbral global de 5: implementas `review_events` con defecto `"ERROR"`, devuelves conteo y veredicto juntos y desempaquetas ambas llamadas (defecto y explícita). En la Sesión 11 cada función devolvía un solo valor; hoy una función devuelve dos y el umbral viaja como global de solo lectura.

## Secuencia conceptual

Cada revisión del programa sigue este orden explícito:

1. **Umbral global:** `REVIEW_THRESHOLD = 5`, solo lectura dentro.
2. **Llamada por defecto:** `review_events(event_log)` usa `"ERROR"` → (`6`, prioritaria).
3. **Llamada explícita:** `review_events(event_log, "WARNING")` reemplaza el defecto → (`5`, prioritaria).
4. **Desempaquetado:** cada par cae en sus dos variables.
5. **Resumen con ámbitos:** encabezado con los dos pares y el umbral declarado.

## Cómo devuelve y recuerda Python (en clase, sin evaluar nada más)

El retorno múltiple empaqueta dos valores en una tupla:

```python
def review_events(events, level="ERROR"):
    """Return count and verdict for the given level."""
    total = events.count(level)
    if total >= 5:
        verdict = "Revisión prioritaria"
    else:
        verdict = "Rutina local"
    return total, verdict
```

Con los 20 eventos de la práctica, `review_events(event_log)` devuelve `(6, "Revisión prioritaria")` porque el defecto es `"ERROR"`. Con `review_events(event_log, "WARNING")` el defecto se reemplaza y devuelve `(5, "Revisión prioritaria")`.

El desempaquetado recoge cada valor en su variable:

```python
error_total, error_verdict = review_events(event_log)
```

`error_total` es `6` y `error_verdict` es `"Revisión prioritaria"`. La global `REVIEW_THRESHOLD = 5` solo se lee dentro: no se reasigna ni se declara `global`.

Tres precisiones y nada más:

- Doble retorno: `return total, verdict` empaqueta una tupla de 2; el desempaquetado exige 2 variables. Si pides una sola, recibes la tupla completa sin ningún error.
- Ámbitos de hoy, nada más: local frente a global de solo lectura y defecto `"ERROR"`. Sin `global` para reasignar, sin `*args`, sin clases ni decoradores.
- Alcance de hoy: 20 datos sintéticos con 6 `ERROR` y 5 `WARNING`. Las etiquetas son didácticas del laboratorio, no estándares universales.

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
notepad scope_review.py

# 5. Ejecuta tu ejercicio
python scope_review.py
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
touch scope_review.py

# 5. Ejecuta tu ejercicio
python3 scope_review.py
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
touch scope_review.py

# 5. Ejecuta tu ejercicio
python3 scope_review.py
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

Crea `scope_review.py` con global de lectura arriba, definición con defecto en medio, desempaquetado y `print` al final (sin `global`, sin `*args`, sin clases, sin decoradores, sin `imports`) que haga lo siguiente:

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, la lista de 20 y tu identidad; imprime el total (`20`) | `REVIEW_THRESHOLD = 5`, `event_log` (20 textos: 6 `ERROR`, 5 `WARNING`), `student_name`, `student_id` |
| 2. Revisión | Define `review_events` con defecto, retorno doble y lectura global; desempaqueta ambas llamadas | `review_events(events, level="ERROR")` → pares; `error_total = 6`, `error_verdict`, `warn_total = 5`, `warn_verdict` |
| 3. Comunicación | Imprime el encabezado con los dos pares | Encabezado más pares y umbral declarado |

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

| Llamada | Regla | Par |
|---------|-------|-----|
| `review_events(event_log)` | Usa `"ERROR"` | (`6`, prioritaria) |
| `review_events(event_log, "WARNING")` | Reemplaza defecto | (`5`, prioritaria) |

Totales esperados: defecto `6` con `"Revisión prioritaria"`; explícito `5` con `"Revisión prioritaria"`. Con 4 o menos el veredicto sería `"Rutina local"`.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Eventos registrados: 20
Errores: 6 - Revisión prioritaria
Avisos: 5 - Revisión prioritaria
--- Revisión con ámbitos ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral global: 5 (solo lectura)
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: tres impresiones intermedias más un encabezado y tres líneas de datos.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

La revisión **organiza el conteo local para el cambio de turno**: dos pares desempaquetados más el umbral declarado. No abre puertos, no toca disco ni red y no confirma un incidente.

## Nota precisa sobre errores con ámbitos

Errores que verás en esta sesión:

- `NameError: name 'total' is not defined`: leíste `total` fuera de `review_events`, pero `total` es local: nace dentro de la función y no existe en el módulo; Python señala el nombre. La corrección es usar las variables desempaquetadas (`error_total`) que sí viven en el módulo.
- Desempaquetado incompleto, en silencio (sin traza): con `single = review_events(event_log)`, una sola variable recibe la tupla completa `(6, 'Revisión prioritaria')` y el par viaja junto sin quedar separado. La corrección es desempaquetar con `error_total, error_verdict = review_events(event_log)`.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, funciones y comentarios) se escribe en inglés (`event_log`, `review_events`, `REVIEW_THRESHOLD`, `error_total`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué par devuelve la llamada por defecto y por qué el defecto es `"ERROR"`.
- [ ] Qué par devuelve la llamada con `"WARNING"` y qué veredicto le toca.
- [ ] Dónde vive cada `total` y por qué no se lee fuera de `review_events`.
- [ ] Qué distingue la variable local de la global y por qué no se abusa de `global`.
- [ ] Qué pasa si desempaquetas en una sola variable (recibes la tupla completa).
- [ ] Qué NO hace el programa (no abre puertos, no toca disco/red, no confirma un incidente).
- [ ] Tu programa se ejecuta sin errores y muestra las tres impresiones intermedias más el encabezado y las tres líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, tapa las salidas, llama sin nivel y con `"WARNING"`, escribe en papel los dos pares y ejecuta con `↑` para comprobar. Es solo práctica extra: no cambia tu calificación y no usa sintaxis nueva. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`shift_scope.py`), distinto del `scope_review.py` de clase y del desafío opcional de arriba.

**Historia:** dejas lista la revisión del turno antes de entregarla, distinta de la revisión del día de clase. Partes de 20 eventos nuevos del turno, aplicas la misma técnica de retorno doble con defecto `"WARNING"`, desempaquetas ambos pares y muestras el reporte.

Crea manualmente `shift_scope.py` en tu proyecto personal, con umbral arriba, definición con defecto en medio y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, los 20 del turno y tu identidad; imprime el total (`20`) | `SHIFT_THRESHOLD = 5`, `shift_events` (20 textos: 7 `WARNING`, 4 `ERROR`), `student_name`, `student_id` |
| 2. Revisión | Define `review_shift` con defecto y retorno doble; desempaqueta ambos pares | `review_shift(events, level="WARNING")` → pares; `warn_total = 7`, `error_total = 4` |
| 3. Comunicación | Reporte del turno con los dos pares | `print()` línea por línea |

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
--- Revisión del turno ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral global: 5 (solo lectura)
```

Con tus propios datos el nombre y el identificador cambian, pero los pares deben coincidir.

**Antes de programar, analiza:** qué par devuelve la llamada por defecto (espera `7` + prioritaria) y por qué el defecto es `"WARNING"`; qué par devuelve la llamada con `"ERROR"` (espera `4` + rutina) y qué veredicto le toca; dónde vive cada `total` y por qué no se lee fuera de `review_shift`.

**Propósito real:** la revisión organiza el conteo local para el cambio de turno: no abre puertos, no toca disco/red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena defecto → retorno doble → desempaquetado → local frente a global. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
