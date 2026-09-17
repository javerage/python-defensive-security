# Sesión 06: Listas y pipeline de eventos locales

Bienvenido a la **Sesión 06** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **procesar una lista sintética de eventos en memoria con un pipeline lineal de seis operaciones: agregar con `append`, contar con `count`, localizar con `index`, eliminar con `remove`, ordenar con `sort` y copiar una muestra con slicing, mostrando el estado tras cada operación**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `event_pipeline.py` y escribe el ejercicio.
4. Ejecuta `python event_pipeline.py` y comprueba el resumen con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `event_pipeline.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

**Rol:** formas parte del equipo que ordena los apuntes de la jornada antes de archivarlos. **Evidencia recibida:** el cuaderno trae **cinco eventos en memoria**: arranque del servicio, memoria alta, respaldo completo, disco lleno y registro de un usuario, todos locales y sintéticos. **Problema:** los apuntes llegan desordenados y sin conteo, así que nadie puede verificar qué pasó antes de archivarlos. **Consecuencia si no se procesan:** el caso se archiva a ciegas, sin total, sin conteo y sin muestra verificable para quien revisa. **Seis decisiones en orden:** primero agregas un sexto evento al final con `append` y muestras el nuevo tamaño; después cuentas cuántas veces aparece el error de disco lleno con `count` (contar no elimina nada) y localizas su posición con `index` (las posiciones empiezan en `0`); después eliminas por valor el evento ya archivado con `remove` y muestras el nuevo tamaño; después ordenas la misma lista con `sort` y copias una muestra de tres con slicing `[0:3]` sin tocar el original. **Resultado verificable:** cada operación deja una impresión intermedia y el resumen identifica de quién es el trabajo y muestra el total final (`5`), el conteo (`1`), la posición (`3`) y la muestra de tres. Nada avanza a ciegas.

## Secuencia conceptual

Cada paso del programa sigue este orden explícito:

1. **Colección ordenada:** la lista con sus cinco eventos iniciales.
2. **Operación:** un solo método o rebanado sobre la lista.
3. **Estado visible:** una impresión inmediata prueba qué cambió.
4. **Muestra final:** el resumen reúne total, conteo, posición y rebanado.

## Cómo procesa Python una lista (en clase, sin evaluar nada más)

### Mapa breve de colecciones (solo orientación, sin ejercicios nuevos)

| Colección | Idea en una línea | Alcance en el curso |
|-----------|-------------------|---------------------|
| `list` | Orden guarda, duplicados permite; se lee por posición desde `0` | **Hoy en profundidad:** la única colección que se construye y evalúa |
| `tuple` | Orden fijo sin cambios | Llega en la S08 (solo se menciona hoy) |
| `set` | Elementos únicos sin orden | Llega en la S08 (solo se menciona hoy) |
| `dict` | Pares clave-valor | Llega en la S07 (solo se menciona hoy) |
| `range` | Secuencias de números para repetir con bucles | Llega en la S09 con bucles (solo se menciona hoy) |

Las demás colecciones solo se nombran para ubicarte: no tienen ejercicios, métodos ni evaluación en esta sesión.

Una lista guarda orden y permite duplicados. Cada operación devuelve algo distinto:

```python
event_log.append("WARNING: reintento local programado")
error_count = event_log.count("ERROR: disco lleno en el laboratorio")
error_position = event_log.index("ERROR: disco lleno en el laboratorio")
```

`append` agrega al final y no devuelve nada útil; `count` devuelve cuántos coinciden (aquí `1`) sin borrar; `index` devuelve la posición del primer coincidente (aquí `3`).

```python
event_log.remove("INFO: respaldo local completo")
event_log.sort()
recent_events = event_log[0:3]
```

`remove` borra por valor el primer coincidente; `sort` ordena la misma lista y devuelve `None` (por eso se llama solo, nunca se asigna); el rebanado `[0:3]` copia las posiciones `0`, `1` y `2` en una lista nueva sin tocar el original.

Tres precisiones y nada más:

- En esta sesión solo creación, índices, slicing, `len()` y los métodos `append`, `count`, `index`, `remove` y `sort`. El desempaquetado y las matrices (listas anidadas) **solo se mencionan: no se usan ni se evalúan en esta sesión**.
- Los textos `INFO`, `WARNING` y `ERROR` son **etiquetas didácticas de este laboratorio** para practicar listas: no son estándares universales y contar `1` no prueba un ataque.
- En esta sesión trabajamos listas de texto en memoria con impresiones intermedias. Los diccionarios llegan en la Sesión 07 y los bucles en la Sesión 09.

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
notepad event_pipeline.py

# 5. Ejecuta tu ejercicio
python event_pipeline.py
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
touch event_pipeline.py

# 5. Ejecuta tu ejercicio
python3 event_pipeline.py
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
touch event_pipeline.py

# 5. Ejecuta tu ejercicio
python3 event_pipeline.py
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

Crea `event_pipeline.py` con código lineal (sin funciones, sin `try/except`, sin bucles, sin `imports`, sin diccionarios, sin tuplas, sin sets, sin escribir matrices anidadas) que haga lo siguiente:

| Paso | Qué hace | Variables y operaciones |
|------|----------|-------------------------|
| 1. Evidencia | Asigna la lista inicial de cinco eventos y tu identidad (de qué caso se trata y de quién es el trabajo) | `event_log` con cinco textos, `student_name`, `student_id`; imprime el tamaño inicial (`5`) |
| 2. Pipeline | Aplica seis operaciones en orden, con impresión intermedia tras cada mutación: agregar, contar, localizar, eliminar, ordenar, rebanar | `append` → imprime `6`; `count` → `error_count = 1`; `index` → `error_position = 3`; `remove` → imprime `5`; `sort` (solo, sin asignar); `[0:3]` → `recent_events` |
| 3. Comunicación | Imprime el encabezado y las seis líneas de datos con `print()` (evidencia legible para revisar cada resultado) | Encabezado más seis líneas de datos legibles |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y pipeline visible (léelos antes de programar)

```python
event_log = [
    "INFO: servicio local iniciado",
    "WARNING: memoria alta en el laboratorio",
    "INFO: respaldo local completo",
    "ERROR: disco lleno en el laboratorio",
    "INFO: usuario local registrado",
]
```

| Operación | Llamada | Efecto y resultado |
|-----------|---------|--------------------|
| 1. Agregar | `event_log.append("WARNING: reintento local programado")` | La lista pasa de `5` a `6` eventos |
| 2. Contar | `event_log.count("ERROR: disco lleno en el laboratorio")` | `error_count = 1` (contar no elimina) |
| 3. Localizar | `event_log.index("ERROR: disco lleno en el laboratorio")` | `error_position = 3` (las posiciones empiezan en `0`) |
| 4. Eliminar | `event_log.remove("INFO: respaldo local completo")` | Borra por valor el primer coincidente; la lista vuelve a `5` |
| 5. Ordenar | `event_log.sort()` | Ordena la misma lista (devuelve `None`: se llama solo, nunca se asigna) |
| 6. Rebanar | `event_log[0:3]` | `recent_events` copia las posiciones `0`, `1` y `2` sin tocar el original |

Las etiquetas son didácticas del laboratorio, no estándares universales.

### Lectura abstracta (pregunta → operación → evidencia)

Lee cada paso como una decisión, no como una llamada para copiar:

| Pregunta del caso | Operación | Variable/llamada | Evidencia impresa |
|-------------------|-----------|------------------|-------------------|
| ¿Qué evento nuevo falta al final? | Agregar | `event_log.append("WARNING: reintento local programado")` | `Eventos tras agregar: 6` |
| ¿Cuántas veces aparece el error de disco lleno? | Contar | `error_count = event_log.count("ERROR: disco lleno en el laboratorio")` | `Errores de disco lleno: 1` |
| ¿En qué posición está ese error? | Localizar | `error_position = event_log.index("ERROR: disco lleno en el laboratorio")` | `Posición del error: 3` |
| ¿Qué evento ya archivado debe salir? | Eliminar | `event_log.remove("INFO: respaldo local completo")` | `Eventos tras eliminar: 5` |
| ¿Cómo queda la misma lista en orden? | Ordenar | `event_log.sort()` (solo, sin asignar) | `Eventos ordenados: [...]` |
| ¿Qué tres eventos muestro sin tocar el original? | Rebanar | `recent_events = event_log[0:3]` | `Muestra ordenada: [...]` |

### Consultas comunes de listas (preguntar antes de romper)

| Consulta | Qué responde | Si falta el valor |
|----------|--------------|-------------------|
| `target_event in event_log` | ¿Existe este evento? (`True`/`False`) | `False` |
| `event_log.count(target_event)` | ¿Cuántos coinciden? | `0` |
| `event_log.index(target_event)` | ¿Dónde está el primero? | `ValueError` (sin `try/except` en esta sesión) |
| `text.find(value)` (texto, S03) | ¿Dónde aparece en la cadena? | `-1` |

`in` es un **operador de pertenencia**, no un método: no lleva paréntesis propios y no modifica la lista. Contraste clave: `str.find()` ante un valor ausente devuelve `-1`, mientras `list.index()` ante un valor ausente interrumpe con `ValueError`. Por eso primero se pregunta sin romper y el pipeline usa `index()` solo sobre un valor conocido del fixture.

Ejemplo conectado a la pregunta “¿existe este evento?” (lectura previa, no es un paso del pipeline):

```python
target_event = "ERROR: disco lleno en el laboratorio"
print(target_event in event_log)  # True
print("ERROR: inexistente" in event_log)  # False
```

`in` **no** se convierte en séptimo paso evaluado: no añade línea al resumen ni cambia las salidas. Solo permite preguntar primero sin romper; el pipeline evaluado sigue siendo de seis operaciones con `index()` sobre el valor conocido del fixture.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Eventos iniciales: 5
Eventos tras agregar: 6
Errores de disco lleno: 1
Posición del error: 3
Eventos tras eliminar: 5
Eventos ordenados: ['ERROR: disco lleno en el laboratorio', 'INFO: servicio local iniciado', 'INFO: usuario local registrado', 'WARNING: memoria alta en el laboratorio', 'WARNING: reintento local programado']
Muestra ordenada: ['ERROR: disco lleno en el laboratorio', 'INFO: servicio local iniciado', 'INFO: usuario local registrado']
--- Resumen de eventos ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Total final: 5
Errores de disco lleno: 1
Posición del error: 3
Muestra ordenada: ['ERROR: disco lleno en el laboratorio', 'INFO: servicio local iniciado', 'INFO: usuario local registrado']
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: siete impresiones previas al resumen más un encabezado y seis líneas de datos. Tras ordenar, `ERROR` queda primero y la muestra `[0:3]` copia exactamente esas tres posiciones.

El paso 3 imprime el informe con el resultado final: lo que se entrega a quien revisa el caso. Las impresiones intermedias son la bitácora del proceso: prueban cada operación mientras se trabaja. El resumen es el único lugar con la identidad del trabajo (`Nombre`, `Identificador`) y con el estado cerrado (`Total final`); algunos valores ya aparecieron en la bitácora con otro sentido (estado transitorio frente a resultado final). No es una repetición inútil: la bitácora sirve a quien ejecuta y el informe a quien revisa, como en S04/S05.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El resumen **organiza la evidencia para la revisión humana**: totales, conteos, posiciones y una muestra ordenada. No lee archivos, no toca la red y no modifica nada fuera de su propia lista en memoria. Contar `1` solo indica que un texto aparece una vez en la lista.

## Nota precisa sobre errores con listas

Errores que verás en esta sesión:

- `IndexError: list index out of range`: pediste una posición que no existe, por ejemplo `event_log[6]` cuando la lista tiene `5` elementos (posiciones `0` a `4`). Python numera desde `0`: la última posición válida es siempre el tamaño menos uno. La corrección es pedir una posición dentro del rango o comprobar el tamaño con `len()` antes.
- Error silencioso con `sort`: si escribes `ordered_log = event_log.sort()`, después `ordered_log` vale `None` y tus impresiones muestran `None` sin ningún mensaje de error. La causa es que `sort` ordena la misma lista y devuelve `None` a propósito. La corrección es llamar `event_log.sort()` solo en su línea y seguir usando `event_log`.

Nota documentada (no es un tercer error provocado ni se evalúa con `try/except`): si `index()` o `remove()` reciben un texto que no está letra por letra en la lista, Python interrumpe con `ValueError: '...' is not in list`. La corrección es copiar el texto exacto de los materiales. Este caso se documenta en la clínica y la matriz; en clase solo se provocan los dos errores de arriba.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`event_log`, `error_count`, `error_position`, `recent_events`, `total_events`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`). El ejemplo usa f-strings como forma cómoda de mostrar variables; su sintaxis no es un objetivo evaluado.

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué cinco eventos trae la lista inicial y por qué las posiciones empiezan en `0`.
- [ ] Qué cambia `append` (tamaño `5` → `6`) y qué muestra la impresión intermedia.
- [ ] Qué devuelve `count` (`1`) y por qué contar no elimina nada.
- [ ] Qué devuelve `index` (`3`) y qué significa esa posición.
- [ ] Qué borra `remove` (por valor, el primer coincidente) y cómo vuelve el tamaño a `5`.
- [ ] Por qué `sort` se llama solo sin asignar y qué pasa si asignas su resultado (`None` silencioso).
- [ ] Qué copia `[0:3]` (posiciones `0`, `1`, `2`) y por qué el original no cambia.
- [ ] Qué significa cada número del resumen y qué NO hace el programa (no lee archivos, no toca la red, no modifica nada fuera de su lista).
- [ ] Cómo llega cada resultado al resumen (qué variable muestra cada línea).
- [ ] Tu programa se ejecuta sin errores y muestra las siete impresiones previas al resumen más el encabezado y las seis líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, predice en voz alta qué tres eventos contiene `event_log[1:4]` después de ordenar y compruébalo agregando un `print(event_log[1:4])` temporal al final. Es solo práctica extra dentro de la clase con sintaxis ya explicada: no cambia tu calificación y no usa conceptos nuevos. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia un poco más compleja para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`alert_queue.py`), distinto del `event_pipeline.py` de clase y del desafío opcional de arriba.

**Historia (turno de noche, caso propio):** eres el auxiliar del turno de noche y debes dejar lista la cola de alertas locales antes del relevo. **Evidencia recibida:** cinco alertas pendientes (reintento pendiente, verificación completa, sensor sin respuesta, turno registrado y espacio bajo). **Problema:** la cola llega sin nota de cierre, sin conteo del error del sensor y sin muestra prioritaria para quien revisa el turno. **Consecuencia si no se procesa:** el relevo recibe una cola sin verificar, sin posición del error y sin resumen utilizable. **Seis decisiones en orden:** agregas la nota archivada con `append` (`6` alertas), cuentas los errores del sensor con `count` (`sensor_errors = 1`, contar no elimina), localizas su posición con `index` (`sensor_position = 2`), eliminas la verificación ya archivada con `remove` (vuelve a `5`), ordenas con `sort` (solo, sin asignar) y copias la muestra prioritaria con `[0:3]` (`priority_sample`). **Resultado verificable:** siete impresiones previas al resumen más encabezado y seis líneas con total `5`, errores `1`, posición `2` y muestra de tres empezando en `ERROR`. Los conteos solo indican cuántas veces aparece un texto en la lista; las etiquetas son reglas didácticas, no estándares universales, y no prueban un ataque. El resumen le sirve a la persona responsable de revisar el turno para ver totales, conteos y muestra en un solo lugar. La tarea aplica el mismo pipeline de seis operaciones sobre una cola nueva, mientras el ejercicio principal procesa la lista del servicio.

Mapeo abstracto de la tarea (pregunta → operación → evidencia):

| Pregunta del turno | Operación | Variable/llamada | Evidencia impresa |
|--------------------|-----------|------------------|-------------------|
| ¿Qué nota falta al final de la cola? | Agregar | `alert_queue.append("INFO: nota local archivada")` | `Alertas tras agregar: 6` |
| ¿Cuántos errores del sensor hay? | Contar | `sensor_errors = alert_queue.count("ERROR: sensor local sin respuesta")` | `Errores del sensor: 1` |
| ¿En qué posición está ese error? | Localizar | `sensor_position = alert_queue.index("ERROR: sensor local sin respuesta")` | `Posición del error: 2` |
| ¿Qué verificación ya archivada debe salir? | Eliminar | `alert_queue.remove("INFO: verificación local completa")` | `Alertas tras eliminar: 5` |
| ¿Cómo queda la misma cola en orden? | Ordenar | `alert_queue.sort()` (solo, sin asignar) | `Alertas ordenadas: [...]` |
| ¿Qué tres alertas prioritarias muestro? | Rebanar | `priority_sample = alert_queue[0:3]` | `Muestra prioritaria: [...]` |

Crea manualmente `alert_queue.py` en tu proyecto personal, con código lineal y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables y operaciones |
|------|----------|-------------------------|
| 1. Evidencia | Asigna la cola inicial de cinco alertas y tu identidad | `alert_queue` con cinco textos, `student_name`, `student_id`; imprime el tamaño inicial (`5`) |
| 2. Pipeline | Aplica las seis operaciones en orden, con impresión intermedia tras cada mutación | `append` → imprime `6`; `count` → `sensor_errors = 1`; `index` → `sensor_position = 2`; `remove` → imprime `5`; `sort` (solo, sin asignar); `[0:3]` → `priority_sample` |
| 3. Comunicación | Resumen legible para quien revisa el turno | `print()` línea por línea |

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Alertas iniciales: 5
Alertas tras agregar: 6
Errores del sensor: 1
Posición del error: 2
Alertas tras eliminar: 5
Alertas ordenadas: ['ERROR: sensor local sin respuesta', 'INFO: nota local archivada', 'INFO: turno de revisión registrado', 'WARNING: espacio bajo en el laboratorio', 'WARNING: reintento local pendiente']
Muestra prioritaria: ['ERROR: sensor local sin respuesta', 'INFO: nota local archivada', 'INFO: turno de revisión registrado']
--- Resumen de la cola ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Total final: 5
Errores del sensor: 1
Posición del error: 2
Muestra prioritaria: ['ERROR: sensor local sin respuesta', 'INFO: nota local archivada', 'INFO: turno de revisión registrado']
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: siete impresiones previas al resumen más un encabezado y seis líneas de datos.

**Antes de programar, analiza:** qué texto busca `count()` y si contar lo elimina; qué posición devuelve `index()` para el error del sensor y por qué empieza en `0`; qué elemento borra `remove()` y cómo pasa el tamaño de `6` a `5`; por qué `sort()` se llama sin asignar y qué tres posiciones copia `[0:3]`.

**Propósito real:** el resumen organiza la evidencia local para la revisión humana. No lee archivos, no toca la red y no sustituye la investigación.

**Entrega:** explica en voz alta la cadena colección ordenada → operación → estado visible → muestra final para las seis operaciones, qué prueba cada impresión intermedia y cómo llega cada resultado al resumen. Además explica qué cambia en el dominio (turno de noche, cola de alertas) y qué técnica se conserva (mismo pipeline de seis operaciones, misma cadena de evidencia). El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
