# Sesión 07: Diccionarios y conteo por nivel y módulo

Bienvenido a la **Sesión 07** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **contar 20 observaciones sintéticas por nivel y por módulo usando diccionarios: construir cada total con `count()`, guardar un valor por clave, leer con `.get()` sin provocar `KeyError`, retirar una clave con `pop()` y mostrar un resumen ordenado sin ningún bucle**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `level_summary.py` y escribe el ejercicio.
4. Ejecuta `python level_summary.py` y comprueba el resumen con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `level_summary.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que resume la jornada antes de entregarla. El cuaderno trae **20 observaciones** con su nivel (`INFO`, `WARNING`, `ERROR`) y su módulo de origen (`auth`, `backup`, `disk`, `net`), todas locales y sintéticas. Recorrerlas a mano una por una tardaría demasiado, así que las cuentas por valor: cada total se construye con una línea explícita de `count()` y se guarda en un diccionario, una clave por cada valor distinto. Después lees con `.get()` (que devuelve un valor por defecto en vez de interrumpir), retiras una clave de prueba con `pop()` y muestras un resumen ordenado con `sorted()`. La lista conserva las 20 entradas con su orden y sus duplicados; el diccionario conserva un total por clave para responder "¿cuántos?" sin recorrer nada. El resumen identifica de quién es el trabajo y muestra cada total en orden.

## Secuencia conceptual

Cada conteo del programa sigue este orden explícito:

1. **Lista plana:** las 20 entradas con orden y duplicados.
2. **Conteo por valor:** una línea de `count()` por cada valor distinto.
3. **Diccionario:** una clave guarda un total (`level_counts["INFO"]` es `9`).
4. **Lectura segura:** `.get()` con valor por defecto en vez de acceso directo.
5. **Resumen ordenado:** `sorted()` ordena las claves y cada posición se lee con `[0]`, `[1]`, `[2]`.

## Cómo cuenta Python con diccionarios (en clase, sin evaluar nada más)

La lista guarda todo; el diccionario resume por clave:

```python
info_count = event_levels.count("INFO")
level_counts = {"INFO": info_count, "WARNING": warning_count, "ERROR": error_count}
```

Con las 20 observaciones de la práctica, `info_count` es `9` y `level_counts["INFO"]` responde `9` sin recorrer la lista. La lista tiene `20` entradas; el diccionario tiene `3` claves.

La lectura segura evita la interrupción del acceso directo:

```python
debug_lookup = level_counts.get("DEBUG", 0)
```

`.get("DEBUG", 0)` devuelve `0` porque esa clave no existe. En cambio `level_counts["DEBUG"]` se interrumpe con `KeyError`: esa es la diferencia que practicas hoy.

Agregar y retirar claves es explícito:

```python
level_counts["DEBUG"] = 0
removed_debug = level_counts.pop("DEBUG", 0)
```

La primera línea agrega la clave de prueba; la segunda la retira y guarda `0`. El `0` por defecto de `pop()` evita la interrupción si la clave ya falta.

Tres precisiones y nada más:

- En esta sesión solo listas de la Sesión 06 (`count`, `len`, `sorted`, índices) más diccionarios nuevos: claves y valores, acceso seguro con `.get()`, asignación por clave y eliminación con `pop()`. Las tuplas y los sets **quedan fuera: llegan en la Sesión 08**.
- Los niveles y módulos son **etiquetas didácticas de este laboratorio** para practicar diccionarios: no son estándares universales y contar `9` no prueba un ataque.
- Los bucles llegan en la Sesión 09 y comprimirán estas líneas repetidas en tres líneas. Hoy cada conteo es una línea explícita para que cada paso quede visible: 20 datos, conteo manual razonable, misma técnica que automatizarás después.

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
notepad level_summary.py

# 5. Ejecuta tu ejercicio
python level_summary.py
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
touch level_summary.py

# 5. Ejecuta tu ejercicio
python3 level_summary.py
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
touch level_summary.py

# 5. Ejecuta tu ejercicio
python3 level_summary.py
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

Crea `level_summary.py` con código lineal (sin funciones, sin `try/except`, sin bucles, sin `imports`, sin tuplas, sin sets) que haga lo siguiente:

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna las 20 observaciones (niveles y módulos en las mismas posiciones) y tu identidad | `event_levels` (20 textos), `event_modules` (20 textos), `student_name`, `student_id`; imprime el total (`20`) |
| 2. Conteos y diccionarios | Cuenta cada valor con `count()`, guarda un total por clave, retira la clave de prueba con `pop()` y lee con `.get()` | `info_count = 9`, `warning_count = 6`, `error_count = 5`, `level_counts` (3 claves), `auth_count = 7`, `backup_count = 6`, `disk_count = 4`, `net_count = 3`, `module_counts` (4 claves), `removed_debug = 0`, `debug_lookup = 0`, `ordered_levels`, `ordered_modules` con `sorted()` |
| 3. Comunicación | Imprime el encabezado y las once líneas de datos con `print()` (cada total en orden) | Encabezado más once líneas de datos legibles |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y tablas de conteo (léelas antes de programar)

```python
event_levels = [
    "INFO", "ERROR", "WARNING", "INFO", "INFO",
    "WARNING", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "INFO", "WARNING",
    "ERROR", "INFO", "WARNING", "ERROR", "INFO",
]
event_modules = [
    "auth", "disk", "auth", "backup", "net",
    "auth", "backup", "disk", "auth", "net",
    "backup", "auth", "disk", "backup", "net",
    "auth", "backup", "disk", "auth", "backup",
]
```

| Nivel | `count()` | Total |
|-------|-----------|-------|
| `INFO` | `event_levels.count("INFO")` | `9` |
| `WARNING` | `event_levels.count("WARNING")` | `6` |
| `ERROR` | `event_levels.count("ERROR")` | `5` |

Los tres suman `20`, igual que la lista: no se perdió ninguna observación.

| Módulo | `count()` | Total |
|--------|-----------|-------|
| `auth` | `event_modules.count("auth")` | `7` |
| `backup` | `event_modules.count("backup")` | `6` |
| `disk` | `event_modules.count("disk")` | `4` |
| `net` | `event_modules.count("net")` | `3` |

Los cuatro suman `20`: cada observación tiene exactamente un módulo.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Observaciones registradas: 20
Niveles distintos: 3
Módulos distintos: 4
Clave de prueba retirada: 0
Búsqueda segura de DEBUG: 0
--- Resumen de niveles y módulos ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Total de observaciones: 20
ERROR: 5
INFO: 9
WARNING: 6
auth: 7
backup: 6
disk: 4
net: 3
Lista completa: 20 entradas, diccionario: 3 claves
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: cinco impresiones intermedias más un encabezado y once líneas de datos. Los niveles salen en orden (`ERROR`, `INFO`, `WARNING`) porque `sorted()` ordena las claves; los módulos igual (`auth`, `backup`, `disk`, `net`).

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El resumen **organiza la evidencia para la revisión humana**: totales por nivel y por módulo en orden. No lee archivos, no toca la red y no modifica nada fuera de sus propias estructuras en memoria. Contar `9` solo indica que un texto aparece nueve veces en la lista.

## Nota precisa sobre errores con diccionarios

Errores que verás en esta sesión:

- `KeyError: 'DEBUG'`: leíste una clave que no existe con acceso directo, por ejemplo `level_counts["DEBUG"]`. El acceso directo exige que la clave exista y se interrumpe si falta. La corrección es leer con valor por defecto: `level_counts.get("DEBUG", 0)`.
- Error silencioso de mayúsculas: si escribes `level_counts.get("info", 0)`, el programa muestra `0` sin ningún mensaje de error y esconde los `9` reales. La causa es que las claves distinguen mayúsculas: `"info"` no es `"INFO"`, así que `.get()` devuelve el valor por defecto como si no hubiera datos. La corrección es usar la clave exacta en mayúsculas.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`event_levels`, `event_modules`, `level_counts`, `module_counts`, `info_count`, `debug_lookup`, `ordered_levels`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`). El ejemplo usa f-strings como forma cómoda de mostrar variables; su sintaxis no es un objetivo evaluado.

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué 20 observaciones trae cada lista y por qué ambas comparten las mismas posiciones.
- [ ] Qué devuelve cada `count()` (`9`, `6`, `5` / `7`, `6`, `4`, `3`) y por qué los totales suman `20`.
- [ ] Por qué la lista conserva `20` entradas mientras el diccionario conserva `3` claves (orden y duplicados frente a un total por clave).
- [ ] Qué guarda `level_counts["INFO"]` y cómo responde "¿cuántos?" sin recorrer la lista.
- [ ] Qué hace `.get("DEBUG", 0)` frente a `level_counts["DEBUG"]` y cuándo usar cada uno.
- [ ] Qué agregan y retiran las dos líneas de `DEBUG` y qué guarda `removed_debug`.
- [ ] Cómo ordena `sorted()` las claves y cómo se lee cada posición con `[0]`, `[1]`, `[2]`.
- [ ] Por qué `.get("info", 0)` muestra `0` en silencio y cómo se corrige.
- [ ] Qué significa cada número del resumen y qué NO hace el programa (no lee archivos, no toca la red, no confirma un incidente).
- [ ] Cómo llega cada resultado al resumen (qué variable muestra cada línea).
- [ ] Tu programa se ejecuta sin errores y muestra las cinco impresiones intermedias más el encabezado y las once líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, agrega un `print(len(event_levels))` y un `print(len(level_counts))` temporales al final, ejecuta con `↑` y di en voz alta por qué el primero muestra `20` y el segundo `3`. Es solo práctica extra dentro de la clase con sintaxis ya explicada: no cambia tu calificación y no usa conceptos nuevos. Esta comparación (lista ordenada y mutable frente a diccionario por clave) prepara la Sesión 08. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia un poco más compleja para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`shift_summary.py`), distinto del `level_summary.py` de clase y del desafío opcional de arriba.

**Historia:** actúas como el auxiliar responsable de dejar listo el resumen del turno de noche antes de entregarlo, distinto de la lista del día de clase. Para dejarlo utilizable registras de quién es el trabajo (`student_name`, `student_id`), partes de 20 observaciones nuevas del turno (`shift_levels` con `INFO 8`, `WARNING 7`, `ERROR 5`; `shift_modules` con `auth 6`, `backup 8`, `disk 6`), cuentas cada valor con `count()` y guardas un total por clave (`level_counts` con 3 claves, `module_counts` con 3 claves), retiras la clave de prueba con `pop("DEBUG", 0)` (`removed_debug = 0`), lees con `.get()` (`debug_lookup = 0`), modelas tu tarjeta como diccionario (`analyst_card` con `name`, `shift` y `total_events`; `card_name` con `.get("name", "desconocido")`, `card_zone` con `.get("zone", "laboratorio local")` porque el turno nunca registró la zona) y muestras el resumen ordenado con `sorted()`. Los conteos solo indican cuántas veces aparece cada texto; las etiquetas son reglas didácticas, no estándares universales, y no prueban un ataque. El resumen le sirve a la persona responsable de recibir el turno para ver niveles, módulos y tarjeta en un solo lugar. La tarea aplica la misma técnica de conteo sobre datos nuevos más la tarjeta del analista, mientras el ejercicio principal resume la lista del día.

Crea manualmente `shift_summary.py` en tu proyecto personal, con código lineal y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna las 20 observaciones del turno y tu identidad | `shift_levels` (20 textos), `shift_modules` (20 textos), `student_name`, `student_id`; imprime el total (`20`) |
| 2. Conteos y diccionarios | Cuenta cada valor, guarda un total por clave, retira la clave de prueba, lee con `.get()`, modela la tarjeta | `info_count = 8`, `warning_count = 7`, `error_count = 5`, `level_counts`, `auth_count = 6`, `backup_count = 8`, `disk_count = 6`, `module_counts`, `removed_debug = 0`, `debug_lookup = 0`, `analyst_card`, `card_name`, `card_zone`, `ordered_levels`, `ordered_modules` |
| 3. Comunicación | Resumen ordenado para quien recibe el turno | `print()` línea por línea |

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Observaciones del turno: 20
Niveles distintos: 3
Módulos distintos: 3
Clave de prueba retirada: 0
Búsqueda segura de DEBUG: 0
Tarjeta del analista: Alex Mendez (laboratorio local)
--- Resumen del turno ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Total de observaciones: 20
ERROR: 5
INFO: 8
WARNING: 7
auth: 6
backup: 8
disk: 6
Lista completa: 20 entradas, diccionario: 3 claves
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: seis impresiones intermedias más un encabezado y diez líneas de datos.

**Antes de programar, analiza:** qué tres líneas de `count()` alimentan `level_counts` y a cuánto deben sumar; qué clave retira `.pop("DEBUG", 0)` y por qué el valor por defecto mantiene el programa corriendo; qué campo de la tarjeta falta y qué valor por defecto devuelve `.get()` para él.

**Propósito real:** el resumen organiza la evidencia local para el cambio de turno. No confirma un incidente y no sustituye la investigación.

**Entrega:** explica en voz alta la cadena lista plana → conteo por valor → diccionario → lectura segura → resumen ordenado para niveles y para módulos, por qué la lista conserva 20 entradas mientras el diccionario conserva un total por clave, y cómo llega cada resultado al resumen. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
