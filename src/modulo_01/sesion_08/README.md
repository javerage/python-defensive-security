# Sesión 08: Tuplas y sets para agrupar direcciones locales

Bienvenido a la **Sesión 08** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **agrupar 20 observaciones sintéticas con tuplas y sets: proteger la ficha del analista en una tupla inmutable, deduplicar la lista en un set de 11 direcciones únicas, clasificar 7 locales frente a 4 documentales con pertenencia (`in`) y mostrar un parte ordenado con `sorted()` sin ningún bucle**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `event_groups.py` y escribe el ejercicio.
4. Ejecuta `python event_groups.py` y comprueba el parte con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `event_groups.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que deja listo el parte de direcciones del laboratorio antes de entregarlo. El cuaderno trae **20 observaciones** de direcciones locales con repeticiones: proteges la ficha del analista en una tupla de 3 campos, deduplicas con un set de **11 únicas** y clasificas cada única como local o documental solo leyendo texto, sin abrir puertos ni tocar la red. La lista conserva las 20 entradas con su orden y sus duplicados; la tupla protege 3 campos sellados; el set conserva 11 únicas para responder "¿cuántas únicas hay?". El parte identifica de quién es el trabajo y muestra cada grupo en orden.

## Secuencia conceptual

Cada agrupación del programa sigue este orden explícito:

1. **Lista plana:** las 20 entradas con orden y duplicados.
2. **Tupla sellada:** 3 campos de la ficha, solo lectura con índice.
3. **Set:** una copia por valor (`set(event_ips)` deja 11 únicas).
4. **Pertenencia:** `in` pregunta presencia como texto, sin conectar nada.
5. **Parte ordenado:** `sorted()` ordena las únicas y cada total llega a su línea.

## Cómo agrupa Python con tuplas y sets (en clase, sin evaluar nada más)

La tupla protege la ficha con paréntesis y no admite cambios:

```python
analyst_record = ("Alex Mendez", "DEF-2026-09", 20)
```

Con índices lees cada campo: `analyst_record[0]` es `"Alex Mendez"` y `len(analyst_record)` es `3`. Intentar `analyst_record[0] = "Otro"` se interrumpe: la tupla es inmutable.

El set elimina duplicados al convertir la lista:

```python
unique_ips = set(event_ips)
ordered_ips = sorted(unique_ips)
```

Con las 20 observaciones de la práctica, `len(event_ips)` es `20` y `len(unique_ips)` es `11`: se retiraron 9 repeticiones. El set no tiene orden, por eso se muestra con `sorted()`.

La pertenencia con `in` clasifica sin conectar nada:

```python
loopback_seen = "127.0.0.1" in unique_ips
missing_seen = "10.9.9.9" in unique_ips
```

`loopback_seen` es `True` porque esa dirección sí está en el set. `missing_seen` es `False` porque `10.9.9.9` nunca se observó: `in` pregunta presencia, no conecta nada.

Tres precisiones y nada más:

- Tupla frente a lista: la tupla no cambia (3 campos sellados); la lista sí cambia y conserva duplicados (20 entradas). Si necesitas corregir la ficha, creas otra tupla: no la editas.
- Sets de hoy, nada más: creación con `set()`, unicidad automática, `len()`, `in` y `sorted()` para mostrar. No hay bucles, no hay comprensión de conjuntos, no hay métodos de diccionario más allá de lo conocido.
- Alcance de hoy: 20 datos sintéticos del laboratorio: 7 únicos locales y 4 únicos documentales (`192.0.2.0/24`). Las etiquetas son didácticas del laboratorio, no estándares universales. Los bucles llegan en la Sesión 09.

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
notepad event_groups.py

# 5. Ejecuta tu ejercicio
python event_groups.py
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
touch event_groups.py

# 5. Ejecuta tu ejercicio
python3 event_groups.py
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
touch event_groups.py

# 5. Ejecuta tu ejercicio
python3 event_groups.py
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

Crea `event_groups.py` con código lineal (sin funciones, sin `try/except`, sin bucles, sin comprensión de conjuntos, sin `imports`) que haga lo siguiente:

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna las 20 observaciones y la tupla sellada más tu identidad | `event_ips` (20 textos), `analyst_record` (3 campos), `student_name`, `student_id`; imprime el total (`20`) |
| 2. Agrupación | Deduplica con `set()`, ordena con `sorted()`, verifica presencia con `in` y clasifica con conteos explícitos | `unique_ips` (deduplicadas con `set`), `ordered_ips` (ordenadas con `sorted`), `loopback_seen`, `missing_seen` (verificación con `in`), `local_count`, `doc_count` (conteos con `int(... in ...)`) |
| 3. Comunicación | Imprime el encabezado y las líneas del parte con conteos y los valores de la lista ordenada | Encabezado más líneas de datos legibles |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

Antes de completar cada paso, predice el valor que esperas y por qué; ejecuta tu archivo y compara con la salida esperada solo después de ejecutar.

## Entrada sintética y tablas de agrupación (léelas antes de programar)

```python
event_ips = [
    "127.0.0.1", "127.0.0.2", "127.0.0.1", "192.0.2.10", "127.0.0.53",
    "::1", "127.0.0.2", "192.0.2.20", "127.0.0.1", "127.0.0.3",
    "192.0.2.10", "::1", "127.0.0.53", "192.0.2.30", "127.0.0.4",
    "127.0.0.1", "192.0.2.20", "::1", "127.0.0.5", "192.0.2.40",
]
analyst_record = ("Alex Mendez", "DEF-2026-09", 20)
```

| Grupo | Regla | Total |
|-------|-------|-------|
| Registradas | `len(event_ips)` | `20` |
| Únicas | `len(set(event_ips))` | `11` (9 repeticiones retiradas) |
| Locales | `in` sobre `127.0.0.0/8` y `::1` | `7` |
| Documentales | `in` sobre `192.0.2.0/24` | `4` |

Los dos grupos suman `11`, igual que el set: cada única pertenece a exactamente un grupo. Las `192.0.2.x` son direcciones documentales de ejemplo (TEST-NET-1): solo se clasifican como texto, nunca se contactan.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Observaciones registradas: 20
Direcciones únicas: 11
Bucle local visto: True
Desconocida vista: False
Locales: 7
Documentales: 4
--- Parte de direcciones ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Total de observaciones: 20
Únicas: 11
Lista ordenada: ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4', '127.0.0.5', '127.0.0.53', '192.0.2.10', '192.0.2.20', '192.0.2.30', '192.0.2.40', '::1']
```

Con tus propios datos el nombre y el identificador cambian, pero la forma de la salida es siempre la misma: seis impresiones intermedias más un encabezado y cinco líneas de datos.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El parte **organiza direcciones locales para la revisión humana**: únicas, grupos y los valores de la lista ordenada. No abre puertos, no toca disco ni red y no confirma un incidente. Que una dirección esté en el set solo indica que apareció en la lista.

## Nota precisa sobre errores con tuplas y sets

Errores que verás en esta sesión:

- `TypeError: 'tuple' object does not support item assignment`: intentaste editar la ficha con `analyst_record[0] = "Otro nombre"`. La tupla es inmutable: Python señala los corchetes porque ese puesto no admite asignación. La corrección es leer con `analyst_record[0]`; si cambia la ficha, crea una tupla nueva completa.
- Orden falso sin traza: si muestras el set con `list(unique_ips)[0]`, hoy ves una dirección y mañana otra, porque el set no tiene orden y el puesto `[0]` no significa "la primera registrada". La corrección es mostrar con `sorted(unique_ips)` y contar con `len(unique_ips)`.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`event_ips`, `unique_ips`, `ordered_ips`, `analyst_record`, `loopback_seen`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué 20 observaciones trae la lista y por qué conserva repeticiones.
- [ ] Qué campo protege `analyst_record` y por qué asignar a `analyst_record[0]` se interrumpe.
- [ ] Qué da `len(event_ips)` frente a `len(set(event_ips))` y cuántas repeticiones se retiran (`20` frente a `11`).
- [ ] Qué devuelve `"127.0.0.1" in unique_ips` frente a `"10.9.9.9" in unique_ips` y por qué ninguno toca la red.
- [ ] Cómo llega cada grupo al parte (qué variable muestra cada línea).
- [ ] Qué NO hace el programa (no abre puertos, no toca disco/red, no confirma un incidente).
- [ ] Tu programa se ejecuta sin errores y muestra las seis impresiones intermedias más el encabezado y las cinco líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, agrega un `print(len(event_ips))` y un `print(len(unique_ips))` temporales al final, ejecuta con `↑` y di en voz alta por qué el primero muestra `20` y el segundo `11`. Es solo práctica extra dentro de la clase con sintaxis ya explicada: no cambia tu calificación y no usa conceptos nuevos. Esta comparación (lista con duplicados frente a set único) prepara la Sesión 09. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`shift_groups.py`), distinto del `event_groups.py` de clase y del desafío opcional de arriba.

**Historia:** dejas listo el parte del turno de noche antes de entregarlo, distinto de la lista del día de clase. Partes de 20 observaciones nuevas del turno, aplicas la misma técnica de tupla + set, proteges tu ficha y muestras el parte ordenado.

Crea manualmente `shift_groups.py` en tu proyecto personal, con código lineal y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna las 20 del turno más la tupla e imprime el total (`20`) | `shift_ips` (20 textos), `shift_record` (3 campos), `student_name`, `student_id` |
| 2. Agrupación | Deduplica, ordena y verifica presencia con `in` | `shift_unique` (deduplicadas con `set`), `shift_ordered` (ordenadas con `sorted`), `shift_seen`, `shift_missing` (verificación con `in`) |
| 3. Comunicación | Parte ordenado para quien recibe el turno | `print()` línea por línea |

Las 20 observaciones del turno (escríbelas tal cual):

```python
shift_ips = [
    "127.0.0.1", "127.0.0.10", "127.0.0.1", "192.0.2.50", "127.0.0.10",
    "::1", "127.0.0.11", "192.0.2.51", "127.0.0.1", "127.0.0.11",
    "192.0.2.50", "::1", "127.0.0.12", "192.0.2.52", "127.0.0.12",
    "127.0.0.1", "192.0.2.51", "::1", "127.0.0.13", "192.0.2.53",
]
shift_record = ("Alex Mendez", "DEF-2026-09", 20)
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Observaciones del turno: 20
Direcciones únicas del turno: 10
Bucle local visto: True
Desconocida vista: False
--- Parte del turno ---
Nombre: Alex Mendez
Total de observaciones: 20
Únicas: 10
Lista ordenada: ['127.0.0.1', '127.0.0.10', '127.0.0.11', '127.0.0.12', '127.0.0.13', '192.0.2.50', '192.0.2.51', '192.0.2.52', '192.0.2.53', '::1']
```

Con tus propios datos el nombre cambia, pero la forma de la salida es siempre la misma.

**Antes de programar, predice:** qué valor da `len(shift_ips)` frente a `len(set(shift_ips))` y cuántas repeticiones se retiran (verifica después de ejecutar); qué campo protege `shift_record` y por qué asignar a `shift_record[0]` se interrumpe; qué devuelve `"127.0.0.1" in shift_unique` frente a `"10.9.9.9" in shift_unique` y por qué ninguno toca la red.

**Propósito real:** el parte organiza direcciones locales para la revisión: no abre puertos, no toca disco/red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena lista → tupla → set → pertenencia → parte para el turno. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
