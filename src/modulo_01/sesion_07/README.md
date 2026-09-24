# Sesión 07: Diccionarios: leer y comunicar resúmenes por nivel y módulo

Bienvenido a la **Sesión 07** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **leer resúmenes de diccionario ya calculados por nivel y por módulo: consultar claves conocidas con acceso directo, contar claves con `len()`, agregar y retirar claves con asignación y `pop()`, leer con `.get()` sin provocar `KeyError` y mostrar un resumen ordenado sin ningún bucle**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `level_summary.py` y escribe el ejercicio.
4. Ejecuta `python level_summary.py` y comprueba el resumen con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `level_summary.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que comunica el resumen de la jornada antes de entregarla. Un proceso local previo resumió **20 observaciones sintéticas** en un total por etiqueta: el resumen agrupa por nivel (`INFO`, `WARNING`, `ERROR`) y por módulo de origen (`auth`, `backup`, `disk`, `net`), todo local y sintético. Tu trabajo no es reconstruir esos totales, sino leerlos y comunicarlos: consultas cada total por su etiqueta con acceso directo, cuentas cuántas etiquetas distintas hay con `len()`, manejas la etiqueta ausente con `.get()` (que devuelve un valor por defecto en vez de interrumpir), retiras una clave de prueba con `pop()` y muestras un resumen ordenado con `sorted()`. El diccionario no contó automáticamente: solo organiza totales ya calculados bajo cada etiqueta, y responde "¿cuántos?" por nombre sin recorrer nada. El resumen identifica de quién es el trabajo y muestra cada total en orden.

## De dónde viene el resumen (puente honesto)

Un proceso local previo resumió 20 observaciones sintéticas en un total por etiqueta; esta sesión consume ese resumen. Generar resúmenes automáticamente desde observaciones crudas llegará con los bucles (Sesión 09): hoy practicas inspeccionar, consultar, modificar, validar y comunicar el resumen ya calculado.

## Secuencia conceptual

Cada lectura del programa sigue este orden explícito:

1. **Resumen dado:** cada etiqueta ya tiene su total (`level_counts["INFO"]` es `9`).
2. **Lectura directa:** una línea por cada clave conocida.
3. **Conteo de claves:** `len()` dice cuántas etiquetas distintas hay (`3`, no `20`).
4. **Lectura segura:** `.get()` con valor por defecto en vez de acceso directo.
5. **Resumen ordenado:** `sorted()` ordena las claves y cada posición se lee con `[0]`, `[1]`, `[2]`.

## Cómo se lee un resumen con diccionarios (en clase, sin evaluar nada más)

El resumen ya trae cada total bajo su etiqueta; tu programa lo consulta por nombre:

```python
info_count = level_counts["INFO"]
```

Con el resumen de la práctica, `info_count` es `9`: la clave `"INFO"` responde `9` directamente. El diccionario tiene `3` claves y el resumen representa `20` observaciones.

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

- En esta sesión solo diccionarios sobre un resumen dado: lectura directa de claves conocidas, `len()` sobre claves, acceso seguro con `.get()`, asignación por clave y eliminación con `pop()`, más `sorted()` e índices ya dominados en la Sesión 06. Las tuplas y los sets **quedan fuera: llegan en la Sesión 08**.
- Los niveles y módulos son **etiquetas didácticas de este laboratorio** para practicar diccionarios: no son estándares universales y leer `9` no prueba un ataque.
- Los bucles llegan en la Sesión 09 y automatizarán la generación de resúmenes como este. Hoy cada lectura es una línea explícita para que cada paso quede visible: resumen dado, consulta por etiqueta, misma técnica de lectura que reutilizarás después.

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
| 1. Resumen dado | Asigna los resúmenes ya calculados (totales por nivel y por módulo), el total de observaciones y tu identidad | `level_counts` (3 claves), `module_counts` (4 claves), `total_events` (`20`), `student_name`, `student_id`; imprime el total (`20`) |
| 2. Lecturas y manejo | Lee cada clave conocida con acceso directo, cuenta claves con `len()`, agrega y retira la clave de prueba con `pop()` y lee con `.get()` | `info_count = 9`, `warning_count = 6`, `error_count = 5`, `auth_count = 7`, `backup_count = 6`, `disk_count = 4`, `net_count = 3`, `removed_debug = 0`, `debug_lookup = 0`, `ordered_levels`, `ordered_modules` con `sorted()` |
| 3. Comunicación | Imprime el encabezado y las once líneas de datos con `print()` (cada total en orden) | Encabezado más once líneas de datos legibles |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Resumen dado y tablas de totales (léelos antes de programar)

```python
level_counts = {"INFO": 9, "WARNING": 6, "ERROR": 5}
module_counts = {"auth": 7, "backup": 6, "disk": 4, "net": 3}
total_events = 20
```

| Nivel | Total dado | Lectura directa |
|-------|-----------|-----------------|
| `INFO` | `9` | `level_counts["INFO"]` |
| `WARNING` | `6` | `level_counts["WARNING"]` |
| `ERROR` | `5` | `level_counts["ERROR"]` |

Los tres valores suman `20`, igual que las observaciones que el resumen representa.

| Módulo | Total dado | Lectura directa |
|--------|-----------|-----------------|
| `auth` | `7` | `module_counts["auth"]` |
| `backup` | `6` | `module_counts["backup"]` |
| `disk` | `4` | `module_counts["disk"]` |
| `net` | `3` | `module_counts["net"]` |

Los cuatro valores suman `20`: cada observación del resumen tiene exactamente un módulo.

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
Resumen: 3 claves de nivel, 4 claves de módulo
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: cinco impresiones intermedias más un encabezado y once líneas de datos. Los niveles salen en orden (`ERROR`, `INFO`, `WARNING`) porque `sorted()` ordena las claves; los módulos igual (`auth`, `backup`, `disk`, `net`). La última línea cuenta claves (`3` y `4`), no observaciones.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El resumen **organiza la evidencia para la revisión humana**: totales por nivel y por módulo en orden. No lee archivos, no toca la red y no modifica nada fuera de sus propias estructuras en memoria. Leer `9` solo indica que el resumen trae nueve bajo esa etiqueta.

## Nota precisa sobre errores con diccionarios

Errores que verás en esta sesión:

- `KeyError: 'DEBUG'`: leíste una clave que no existe con acceso directo, por ejemplo `level_counts["DEBUG"]`. El acceso directo exige que la clave exista y se interrumpe si falta. La corrección es leer con valor por defecto: `level_counts.get("DEBUG", 0)`.
- Error silencioso de mayúsculas: si escribes `level_counts.get("info", 0)`, el programa muestra `0` sin ningún mensaje de error y esconde los `9` reales. La causa es que las claves distinguen mayúsculas: `"info"` no es `"INFO"`, así que `.get()` devuelve el valor por defecto como si no hubiera datos. La corrección es usar la clave exacta en mayúsculas.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`level_counts`, `module_counts`, `total_events`, `info_count`, `debug_lookup`, `ordered_levels`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`). El ejemplo usa f-strings como forma cómoda de mostrar variables; su sintaxis no es un objetivo evaluado.

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] De dónde viene el resumen (un proceso previo agrupó 20 observaciones) y qué generará automáticamente la Sesión 09.
- [ ] Qué responde cada lectura directa (`9`, `6`, `5` / `7`, `6`, `4`, `3`) y a cuánto suman los valores de cada resumen.
- [ ] Qué mide `len()` sobre cada diccionario (claves distintas: `3` y `4`) y qué NO mide (totales de observaciones).
- [ ] Qué guarda `level_counts["INFO"]` y cómo responde "¿cuántos?" por nombre.
- [ ] Qué hace `.get("DEBUG", 0)` frente a `level_counts["DEBUG"]` y cuándo usar cada uno.
- [ ] Qué agregan y retiran las dos líneas de `DEBUG` y qué guarda `removed_debug`.
- [ ] Cómo ordena `sorted()` las claves y cómo se lee cada posición con `[0]`, `[1]`, `[2]`.
- [ ] Por qué `.get("info", 0)` muestra `0` en silencio y cómo se corrige.
- [ ] Qué significa cada número del resumen y qué NO hace el programa (no lee archivos, no toca la red, no confirma un incidente).
- [ ] Cómo llega cada resultado al resumen (qué variable muestra cada línea).
- [ ] Tu programa se ejecuta sin errores y muestra las cinco impresiones intermedias más el encabezado y las once líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, agrega un `print(len(level_counts))` y un `print(len(module_counts))` temporales al final, ejecuta con `↑` y di en voz alta por qué el primero muestra `3` y el segundo `4`. Después explica por qué esa diferencia NO dice nada sobre los totales de observaciones: ambos resúmenes representan las mismas `20` observaciones y `len()` solo cuenta etiquetas distintas. Es solo práctica extra dentro de la clase con sintaxis ya explicada: no cambia tu calificación y no usa conceptos nuevos. Esta comparación (cuántas etiquetas agrupa cada resumen) prepara la Sesión 08. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia un poco más compleja para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`shift_summary.py`), distinto del `level_summary.py` de clase y del desafío opcional de arriba.

**Historia:** actúas como el auxiliar responsable de dejar listo el resumen del turno de noche antes de entregarlo, distinto del resumen del día de clase. Para dejarlo utilizable registras de quién es el trabajo (`student_name`, `student_id`), partes del resumen ya calculado del turno (`level_counts` con `INFO 8`, `WARNING 7`, `ERROR 5`; `module_counts` con `auth 6`, `backup 8`, `disk 6`), lees cada clave con acceso directo, cuentas claves con `len()`, retiras la clave de prueba con `pop("DEBUG", 0)` (`removed_debug = 0`), lees con `.get()` (`debug_lookup = 0`), modelas tu tarjeta como diccionario (`analyst_card` con `name`, `shift` y `total_events`; `card_name` con `.get("name", "desconocido")`, `card_zone` con `.get("zone", "laboratorio local")` porque el turno nunca registró la zona) y muestras el resumen ordenado con `sorted()`. Los totales solo indican cuántas observaciones agrupa cada etiqueta; las etiquetas son reglas didácticas, no estándares universales, y no prueban un ataque. El resumen le sirve a la persona responsable de recibir el turno para ver niveles, módulos y tarjeta en un solo lugar. La tarea aplica la misma técnica de lectura sobre un resumen nuevo más la tarjeta del analista, mientras el ejercicio principal comunica el resumen del día.

Crea manualmente `shift_summary.py` en tu proyecto personal, con código lineal y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Resumen dado | Asigna los resúmenes del turno, la tarjeta del analista y tu identidad | `level_counts` (3 claves), `module_counts` (3 claves), `analyst_card` (`name`, `shift`, `total_events`), `student_name`, `student_id`; imprime el total (`20`) |
| 2. Lecturas y manejo | Lee cada clave, cuenta claves, retira la clave de prueba, lee con `.get()`, modela la tarjeta | `info_count = 8`, `warning_count = 7`, `error_count = 5`, `auth_count = 6`, `backup_count = 8`, `disk_count = 6`, `removed_debug = 0`, `debug_lookup = 0`, `card_name`, `card_zone`, `ordered_levels`, `ordered_modules` |
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
Resumen: 3 claves de nivel, 3 claves de módulo
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: seis impresiones intermedias más un encabezado y diez líneas de datos.

**Antes de programar, analiza:** qué tres lecturas directas consultan `level_counts` y a cuánto deben sumar sus valores; qué clave retira `.pop("DEBUG", 0)` y por qué el valor por defecto mantiene el programa corriendo; qué campo de la tarjeta falta y qué valor por defecto devuelve `.get()` para él.

**Propósito real:** el resumen organiza la evidencia local para el cambio de turno. No confirma un incidente y no sustituye la investigación.

**Entrega:** explica en voz alta la cadena resumen dado → lectura directa → conteo de claves → lectura segura → resumen ordenado para niveles y para módulos, cuántas claves agrupa cada diccionario y por qué, y cómo llega cada resultado al resumen. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
