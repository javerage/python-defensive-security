# Sesión 09: Ciclos for y while sobre el registro local

Bienvenido a la **Sesión 09** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **recorrer 20 eventos sintéticos con `for` y con `while`, contar 6 `ERROR` en ambas versiones con terminación garantizada y verificar que los dos conteos coinciden**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `event_loop.py` y escribe el ejercicio.
4. Ejecuta `python event_loop.py` y comprueba la verificación con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `event_loop.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que verifica el registro local antes de entregarlo. Recibes un registro de **20 eventos**: cuenta los `ERROR` con `for` y repite el conteo con `while` con avance garantizado. Si ambos dan **6**, el conteo queda verificado; si difieren, hay un error de recorrido. En la Sesión 08 agrupaste 20 direcciones con sets sin bucles; hoy recorres 20 eventos de registro con dos ciclos, una vez con cada uno, y ambos deben dar 6.

## Secuencia conceptual

Cada conteo del programa sigue este orden explícito:

1. **Lista plana:** los 20 eventos con 6 `ERROR`.
2. **Conteo con `for`:** visita cada evento, suma si es `ERROR`.
3. **Conteo con `while`:** inicio + condición + avance en cada vuelta.
4. **Comparación:** `for_count == while_count` da `True`.
5. **Resumen verificado:** encabezado, ambos conteos y la coincidencia.

## Cómo recorre Python con for y while (en clase, sin evaluar nada más)

El `for` visita cada elemento sin índices:

```python
for_count = 0
for event in event_log:
    if event == "ERROR":
        for_count = for_count + 1
```

Con los 20 eventos de la práctica, `for_count` termina en `6`. El ciclo se detiene solo: no hay condición que olvidar.

El `while` necesita inicio, condición y avance visibles:

```python
while_count = 0
index = 0
while index < len(event_log):
    if event_log[index] == "ERROR":
        while_count = while_count + 1
    index = index + 1
```

Con los mismos 20 eventos, `while_count` también termina en `6` e `index` termina en `20`. Si falta `index = index + 1`, el ciclo nunca avanza y nunca termina.

La coincidencia se verifica con una comparación directa:

```python
both_match = for_count == while_count
```

`both_match` es `True` porque ambos cuentan `6`. Esa es la prueba de que las dos versiones recorrieron los mismos 20.

Tres precisiones y nada más:

- `for` frente a `while`: `for` termina solo al agotar la lista (20 visitas); `while` termina cuando `index < 20` deja de cumplirse. Si el avance falta, el `while` repite la misma posición sin fin.
- Ciclos de hoy, nada más: `for` sobre lista, `while` con contador, `len()`, `range()` solo como lectura y comparación de totales. Los ciclos anidados llegan en la Sesión 10; hoy un solo nivel.
- Alcance de hoy: 20 datos sintéticos del laboratorio con 6 `ERROR`. Las etiquetas son didácticas del laboratorio, no estándares universales. Sin funciones, sin archivos, sin red.

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
notepad event_loop.py

# 5. Ejecuta tu ejercicio
python event_loop.py
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
touch event_loop.py

# 5. Ejecuta tu ejercicio
python3 event_loop.py
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
touch event_loop.py

# 5. Ejecuta tu ejercicio
python3 event_loop.py
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

Crea `event_loop.py` con ciclos de un solo nivel (sin ciclos anidados, sin `break`/`continue` obligatorios, sin funciones, sin `imports`) que haga lo siguiente:

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna la lista de 20 más tu identidad e imprime el total (`20`) | `event_log` (20 textos, 6 `ERROR`), `student_name`, `student_id` |
| 2. Conteos | Cuenta con `for` y repite con `while` con avance en cada vuelta; compara | `for_count = 6`, `while_count = 6`, `index` (termina en `20`), `both_match = True` |
| 3. Comunicación | Imprime el encabezado, ambos conteos y la coincidencia | Encabezado más líneas de conteos y verificación |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y tablas de conteo (léelas antes de programar)

```python
event_log = [
    "INFO", "ERROR", "WARNING", "INFO", "ERROR",
    "INFO", "WARNING", "ERROR", "INFO", "WARNING",
    "INFO", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "ERROR", "INFO",
]
```

| Versión | Regla | Total |
|---------|-------|-------|
| `for` | Visita cada evento, suma si es `ERROR` | `6` |
| `while` | Condición `index < 20` + avance `+= 1` | `6` |
| Verificación | `for_count == while_count` | `True` |

Cuenta a mano dos `ERROR` en la primera fila antes de programar.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Eventos registrados: 20
Conteo con for: 6
Conteo con while: 6
Conteos iguales: True
--- Verificación del registro ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Total de eventos: 20
Errores (for): 6
Errores (while): 6
Verificación: conteos iguales
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: cuatro impresiones intermedias más un encabezado y seis líneas de datos.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El conteo **organiza el registro local para la revisión**: dos versiones del mismo conteo más su coincidencia. No abre puertos, no toca disco ni red y no confirma un incidente. Contar `6` solo indica que un texto aparece seis veces en la lista.

## Nota precisa sobre errores con ciclos

Errores que verás en esta sesión:

- `IndexError: list index out of range`: la condición permite `index == 20` y la lista llega hasta `19`; Python señala los corchetes de `event_log[index]`. La corrección es mantener `while index < len(event_log)` con avance de uno por vuelta.
- `while` sin avance que se cuelga en silencio (sin traza): sin `index = index + 1`, la condición siempre es verdadera y el programa repite la misma posición sin mostrar error. La corrección es agregar el avance al final del cuerpo y cancelar el cuelgue con `Ctrl + C`.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`event_log`, `for_count`, `while_count`, `index`, `both_match`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué 20 eventos trae la lista y dónde están los 6 `ERROR`.
- [ ] Cómo visita el `for` cada evento hasta 20 y por qué termina solo.
- [ ] Qué tres líneas garantizan que el `while` termina (inicio, condición con `len()`, avance de uno).
- [ ] Por qué un `while` sin avance nunca termina y cómo lo cancelas (`Ctrl + C`).
- [ ] Qué vale `both_match` y qué significa para quien recibe el registro.
- [ ] Qué NO hace el programa (no abre puertos, no toca disco/red, no confirma un incidente).
- [ ] Tu programa se ejecuta sin errores y muestra las cuatro impresiones intermedias más el encabezado y las seis líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, tapa la salida, cambia el último `INFO` por `ERROR`, escribe en papel qué darán `for_count`, `while_count` y `both_match`, y ejecuta con `↑` para comprobar. Es solo práctica extra: no cambia tu calificación y no usa sintaxis nueva. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`shift_loop.py`), distinto del `event_loop.py` de clase y del desafío opcional de arriba.

**Historia:** dejas listo el conteo del turno de noche antes de entregarlo, distinto del registro del día de clase. Partes de 20 eventos nuevos del turno, aplicas la misma técnica de `for` más `while`, cuentas los `WARNING` en ambas versiones y verificas la coincidencia.

Crea manualmente `shift_loop.py` en tu proyecto personal, con ciclos de un solo nivel y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna los 20 del turno más tu identidad e imprime el total (`20`) | `shift_log` (20 textos, 7 `WARNING`), `student_name`, `student_id` |
| 2. Conteos | Cuenta `WARNING` con `for` y repite con `while` | `shift_for = 7`, `shift_while = 7`, `shift_index` (termina en `20`), `shift_match = True` |
| 3. Comunicación | Resumen con ambos conteos y la coincidencia | `print()` línea por línea |

Los 20 eventos del turno (escríbelos tal cual):

```python
shift_log = [
    "WARNING", "INFO", "WARNING", "ERROR", "INFO",
    "WARNING", "INFO", "WARNING", "ERROR", "INFO",
    "WARNING", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "ERROR", "INFO",
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Eventos del turno: 20
Conteo con for: 7
Conteo con while: 7
Conteos iguales: True
--- Verificación del turno ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Total de eventos: 20
Avisos (for): 7
Avisos (while): 7
Verificación: conteos iguales
```

> Nota de respaldo: la guía del estudiante muestra explícitamente las cuatro primeras líneas del ejemplo; el bloque de resumen replica la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los conteos deben coincidir.

**Antes de programar, analiza:** cuántos `WARNING` hay a mano (espera `7`) y en qué posiciones están los dos primeros; qué tres líneas garantizan que el `while` termina (inicio, condición con `len()`, avance de uno); qué vale `shift_match` si ambos cuentan `7` y qué significa para quien recibe el turno.

**Propósito real:** el conteo organiza el registro local para la revisión: no abre puertos, no toca disco/red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena lista → `for` → `while` con avance → comparación para el turno. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
