# Sesión 10: Ciclos anidados y control de la matriz local

Bienvenido a la **Sesión 10** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **recorrer 3 días con ciclos anidados, saltar 2 líneas malformadas con `continue`, detener un día con `break` y mostrar el resumen por día con totales verificados**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `matrix_review.py` y escribe el ejercicio.
4. Ejecuta `python matrix_review.py` y comprueba el resumen con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `matrix_review.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que resume la matriz local antes de entregarla. Recibes **3 días con 6 posiciones cada uno**: cuenta los `ERROR` por día con ciclos anidados, salta 2 `UNKNOWN` con `continue` y detén el tercer día en `STOP` con `break`. En la Sesión 09 recorriste una sola lista; hoy recorres 3 días con 6 eventos cada uno y 2 marcas malformadas que se cuentan como omitidas.

## Secuencia conceptual

Cada revisión del programa sigue este orden explícito:

1. **Matriz:** 3 días con 6 posiciones cada uno (18 visitas).
2. **Recorrido anidado:** exterior día, interior evento.
3. **Control:** `continue` en `UNKNOWN` (+1 omitida), `break` en `STOP` (detiene solo ese día).
4. **Subtotales:** un total por día (`2`, `2`, `1`).
5. **Total verificado:** la suma por día coincide con el general (`5`).

## Cómo controla Python los ciclos anidados (en clase, sin evaluar nada más)

El exterior elige el día y el interior visita cada evento:

```python
day_total = 0
for day in day_logs:
    for event in day:
        if event == "ERROR":
            day_total = day_total + 1
```

Con 3 días de 6 eventos, el interior corre 18 veces en total. Cada día deja su subtotal y la suma de los tres es el total general.

El `continue` salta lo malformado y el `break` cierra el día:

```python
if event == "UNKNOWN":
    continue
if event == "STOP":
    break
```

Con las marcas de la práctica, `continue` salta 2 `UNKNOWN` (se cuentan como omitidas) y `break` detiene el tercer día en `STOP`: lo que viene después de `STOP` ese día no se cuenta. No hay `else` en ciclos en esta sesión.

Tres precisiones y nada más:

- `break` frente a `continue`: `continue` salta UNA línea y sigue el día; `break` abandona EL DÍA completo. Si pones `break` donde va `continue`, pierdes eventos válidos sin ningún error.
- Control de hoy, nada más: anidación de dos niveles, un `break` y un `continue`, conteo de omitidas. Sin `else` en ciclos, sin funciones, sin tercer nivel.
- Alcance de hoy: 3 días sintéticos del laboratorio (18 posiciones, 2 omitidas, 16 válidas). Las etiquetas son didácticas del laboratorio, no estándares universales.

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
notepad matrix_review.py

# 5. Ejecuta tu ejercicio
python matrix_review.py
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
touch matrix_review.py

# 5. Ejecuta tu ejercicio
python3 matrix_review.py
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
touch matrix_review.py

# 5. Ejecuta tu ejercicio
python3 matrix_review.py
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

Crea `matrix_review.py` con ciclos anidados de dos niveles (sin funciones, sin `else` en ciclos, sin `imports`) que haga lo siguiente:

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna la matriz de 3 días más tu identidad e imprime los días (`3`) | `day_logs` (3 listas de 6), `student_name`, `student_id` |
| 2. Recorrido | Anida los ciclos, salta `UNKNOWN` con `continue` y detén con `break` en `STOP`; acumula por día | `grand_total = 5`, `skipped = 2`, `day_totals` (`2`, `2`, `1`), `day_index` |
| 3. Comunicación | Imprime el encabezado, un subtotal por día y el total con omitidas | Encabezado más subtotales, omitidas y total |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y tablas de conteo (léelas antes de programar)

```python
day_logs = [
    ["INFO", "ERROR", "UNKNOWN", "INFO", "ERROR", "INFO"],
    ["WARNING", "ERROR", "INFO", "UNKNOWN", "INFO", "ERROR"],
    ["INFO", "ERROR", "STOP", "ERROR", "INFO", "WARNING"],
]
```

| Día | Regla | Subtotal |
|-----|-------|----------|
| Día 1 | 2 `ERROR`, 1 `UNKNOWN` omitida | `2` |
| Día 2 | 2 `ERROR`, 1 `UNKNOWN` omitida | `2` |
| Día 3 | Se detiene en `STOP` (lo posterior no se cuenta) | `1` |
| Omitidas | Un `continue` por `UNKNOWN` | `2` |
| Total | Suma por día | `5` |

Lo posterior a `STOP` el día 3 no se cuenta.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Días registrados: 3
Día 1: 2
Día 2: 2
Día 3: 1
Omitidas: 2
Total de errores: 5
--- Resumen por día ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Días: 3, posiciones: 18, válidas: 16
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: seis impresiones intermedias más un encabezado y tres líneas de datos.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El resumen **organiza la matriz local para la revisión**: subtotales por día, omitidas declaradas y total verificado. No abre puertos, no toca disco ni red y no confirma un incidente.

## Nota precisa sobre errores con ciclos anidados

Errores que verás en esta sesión:

- `IndentationError: expected an indented block after 'for' statement`: el `for` interior quedó al mismo nivel que el exterior y Python esperaba el cuerpo indentado del día. La corrección es indentar el interior un nivel más que el exterior (4 espacios por nivel, sin mezclar).
- `break` donde va `continue`, en silencio (sin traza): con `break` en `UNKNOWN` abandonas el día completo, así que los `ERROR` posteriores a `UNKNOWN` nunca se cuentan y el total sale bajo sin ningún error. La corrección es usar `continue` para `UNKNOWN` y reservar `break` solo para `STOP`.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`day_logs`, `day_total`, `grand_total`, `skipped`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Cómo se reparten exterior (día) e interior (evento) y por qué el interior corre 18 veces.
- [ ] Qué salta `continue` (una línea) frente a qué abandona `break` (el día completo).
- [ ] Por qué el día 3 da `1` y qué posiciones deja de contar tras `STOP`.
- [ ] De dónde sale cada omitida y por qué el resumen las declara (`2`).
- [ ] Cómo se verifica el total sumando los días (`2 + 2 + 1 = 5`).
- [ ] Qué NO hace el programa (no abre puertos, no toca disco/red, no confirma un incidente).
- [ ] Tu programa se ejecuta sin errores y muestra las seis impresiones intermedias más el encabezado y las tres líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, tapa el total, suma `2 + 2 + 1` en voz alta y di por qué da `5` aunque la matriz tiene `18` posiciones. Es solo práctica extra: no cambia tu calificación y no usa sintaxis nueva. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`night_review.py`), distinto del `matrix_review.py` de clase y del desafío opcional de arriba.

**Historia:** dejas listo el resumen de 2 noches antes de entregarlo, distinto de la matriz de 3 días de clase. Partes de 2 noches nuevas con 6 posiciones cada una, aplicas la misma técnica anidada, saltas 1 malformada y muestras el resumen por noche.

Crea manualmente `night_review.py` en tu proyecto personal, con ciclos anidados de dos niveles y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna las 2 noches más tu identidad e imprime las noches (`2`) | `night_logs` (2 listas de 6), `student_name`, `student_id` |
| 2. Recorrido | Anida, salta `UNKNOWN` y acumula por noche | `night_totals` (`2`, `2`), `night_skipped = 1`, `night_grand = 4`, `night_index` |
| 3. Comunicación | Resumen por noche con omitida y total | `print()` línea por línea |

La matriz de 2 noches (escríbela tal cual):

```python
night_logs = [
    ["INFO", "WARNING", "ERROR", "INFO", "ERROR", "INFO"],
    ["ERROR", "UNKNOWN", "INFO", "WARNING", "ERROR", "INFO"],
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Noches registradas: 2
Noche 1: 2
Noche 2: 2
Omitidas: 1
Total de errores: 4
--- Resumen por noche ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Noches: 2, posiciones: 12, válidas: 11
```

> Nota de respaldo: la guía del estudiante muestra explícitamente las cinco primeras líneas del ejemplo; el bloque de resumen replica la estructura del ejercicio de clase para las noches. Con tus propios datos el nombre y el identificador cambian, pero los conteos deben coincidir.

**Antes de programar, predice:** cuántos `ERROR` hay por noche a mano y en qué posición está el único `UNKNOWN` (escribe tu conteo primero y verifica después de ejecutar); qué línea suma a `night_skipped` y por qué esa posición no suma al total; qué valdrá el total general cuando ambas noches se acumulen y qué significa para quien recibe el turno.

**Propósito real:** el resumen organiza la matriz local para la revisión: no abre puertos, no toca disco/red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena matriz → día → evento → omitida → subtotal → total. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
