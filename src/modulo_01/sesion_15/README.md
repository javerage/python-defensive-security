# Sesión 15: pathlib y archivos de texto

Bienvenido a la **Sesión 15** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **leer un registro local con `pathlib`, anclar rutas relativas a la raíz del proyecto, declarar UTF-8 explícito, manejar archivos faltantes con `try/except` y publicar el resultado con escritura atómica (temporal más renombrar)**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el fixture `datos/app.log` (o deja que el arranque lo genere) y el controlador `normalize_logs.py`.
4. Ejecuta `python normalize_logs.py` desde la raíz del proyecto y verifica `salida/normalizado.txt`.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

15 min encuadre y anatomía ruta-ancla-archivo · 10 min demo en vivo con ruta mal resuelta · 25 min práctica con `normalize_logs.py` y escritura atómica · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que entrega un registro limpio al siguiente turno sin que nadie lea un archivo a medias. Recibes **20 líneas** de `app.log`, un umbral de 5 y **el lector `kit/` heredado de la Sesión 14**: anclas la entrada a la raíz con `pathlib`, normalizas cada línea a la forma `NIVEL: mensaje` con UTF-8, cuentas procesadas y omitidas con `try/except` de la Sesión 13 y publicas con **escritura atómica** (temporal más renombrar). En la Sesión 14 el entorno quedó reproducible; hoy además ningún lector ve jamás un archivo a medio escribir.

## Secuencia conceptual

Cada normalización anclada del programa sigue este orden explícito:

1. **Evidencia:** `REVIEW_THRESHOLD = 5`, `fixture_lines` (20 textos) y tu identidad.
2. **Tarea anclada:** `read_input_lines(INPUT_PATH)` → 20 líneas crudas desde la ruta anclada.
3. **Normalización:** `normalize_line(raw_line)` → 18 limpias más 2 omitidas.
4. **Publicación atómica:** `write_atomic(OUTPUT_PATH, TEMP_PATH, clean_lines)` → `salida/normalizado.txt` solo cuando está terminado.
5. **Reporte anclado:** pares ERROR y WARNING contra el umbral, conteos de archivo y alcance local.

## Cómo lee Python con pathlib (en clase, sin evaluar nada más)

Una ruta anclada nace del archivo, no de la consola; la codificación se declara siempre; el temporal más el renombrar publican solo archivos terminados:

```python
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_PATH = PROJECT_ROOT / "datos" / "app.log"
OUTPUT_PATH = PROJECT_ROOT / "salida" / "normalizado.txt"
TEMP_PATH = PROJECT_ROOT / "salida" / "normalizado.tmp"
```

```python
def normalize_line(raw_line):
    """Return the clean level plus message pair, or None when skipped."""
    text = raw_line.strip()
    if not text:
        return None
    if ":" not in text:
        return None
    level, _, message = text.partition(":")
    level = level.strip().upper()
    message = message.strip()
    if level not in ALLOWED_LEVELS or not message:
        return None
    return level, f"{level}: {message}"
```

```python
def read_input_lines(input_path):
    """Return raw lines, or an empty list when the fixture is missing."""
    try:
        content = input_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {input_path} (revise la ruta anclada)")
        return []
    return content.splitlines()
```

```python
def write_atomic(output_path, temp_path, clean_lines):
    """Publish clean lines through a temporary file plus rename."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path.write_text("\n".join(clean_lines) + "\n", encoding="utf-8")
    temp_path.replace(output_path)
```

Con las 20 líneas de la práctica, `normalize_line` devuelve 18 pares limpios y `None` 2 veces (la línea sin dos puntos y la línea vacía). `read_input_lines` devuelve las 20 crudas. `write_atomic` deja `salida/normalizado.txt` con 18 líneas y ningún `normalizado.tmp` residual. Sin modelado con Pydantic todavía: eso llega en la Sesión 16.

Tres precisiones y nada más:

- Ancla: `Path(__file__).resolve().parent` apunta a la raíz aunque ejecutes desde otra carpeta; la ruta relativa suelta `"datos/app.log"` depende del directorio de la consola y se rompe al moverte.
- UTF-8: `encoding="utf-8"` se declara en cada lectura y escritura; sin ella, Windows y Linux pueden interpretar distinto los mismos bytes.
- Atómica: el lector del siguiente turno solo ve `normalizado.txt` terminado porque el renombrar sustituye el archivo de una vez; escribir directo sobre el final expone mitades si el programa se interrumpe.

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

# 4. Crea manualmente el fixture y el archivo nuevo
mkdir datos
notepad datos\app.log
notepad normalize_logs.py

# 5. Ejecuta desde la raíz y verifica la salida
python normalize_logs.py
dir salida
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

# 4. Crea manualmente el fixture y el archivo nuevo
mkdir -p datos
touch datos/app.log normalize_logs.py

# 5. Ejecuta desde la raíz y verifica la salida
python3 normalize_logs.py
ls salida
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

# 4. Crea manualmente el fixture y el archivo nuevo
mkdir -p datos
touch datos/app.log normalize_logs.py

# 5. Ejecuta desde la raíz y verifica la salida
python3 normalize_logs.py
ls salida
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

Debes ver el prefijo `(.venv)` en el prompt y la versión Python 3.13.x. Después crea `datos/app.log` con las 20 líneas de la tabla de abajo.

## Ejercicio obligatorio

Crea `normalize_logs.py` con evidencia arriba, tareas ancladas en medio, publicación atómica y reporte anclado al final (sin modelar con Pydantic, sin clases de dominio, sin red, sin shell) que haga lo siguiente:

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, las 20 líneas y tu identidad; ancla las rutas al archivo | `REVIEW_THRESHOLD = 5`, `fixture_lines` (20 textos), `student_name`, `student_id`, `PROJECT_ROOT`, `INPUT_PATH`, `OUTPUT_PATH`, `TEMP_PATH` |
| 2. Anclado | Arranca el fixture, lee con `try/except`, normaliza línea por línea y publica con el par atómico | `ensure_fixture(...)`, `read_input_lines(INPUT_PATH)` → 20; `normalize_line(...)` → 18 más 2 omitidas; `write_atomic(...)` → `salida/normalizado.txt` |
| 3. Comunicación | Imprime conteos de archivo, los dos pares contra el umbral, la ruta publicada y el alcance | `print()` línea por línea |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y tablas de revisión (léelas antes de programar)

```python
REVIEW_THRESHOLD = 5
fixture_lines = [
    "INFO: servicio iniciado en localhost",
    "ERROR: disco lleno en localhost",
    "WARNING: reintento de conexion local",
    "INFO: revision de turno completada",
    "ERROR: puerto local sin respuesta",
    "WARNING: latencia alta en loopback",
    "ERROR: archivo temporal corrupto",
    "INFO: copia de respaldo verificada",
    "WARNING: umbral cercano al limite",
    "ERROR: registro incompleto detectado",
    "INFO: sesion local iniciada",
    "WARNING: cola de eventos llena",
    "INFO: limpieza de salida completada",
    "INFO: verificacion final aprobada",
    "INFO: auditoria local sin hallazgos",
    "WARNING: reintento de lectura local",
    "INFO: inventario local actualizado",
    "linea rota sin nivel",
    "",
    "INFO: cierre de turno registrado",
]
```

| Revisión anclada | Llamada que la produce | Par |
|---------|-------|-----|
| Errores contra el umbral | conteo de `ERROR` en líneas limpias | (`4`, rutina: 4 < 5) |
| Avisos contra el umbral | conteo de `WARNING` en líneas limpias | (`5`, prioritaria: 5 >= 5) |
| Archivo publicado | `write_atomic` temporal más renombrar | 18 líneas en `salida/normalizado.txt` |

Totales esperados: `20` leídas, `18` normalizadas, `2` omitidas (la línea sin dos puntos y la línea vacía); `4` errores con `"Rutina local"`; `5` avisos con `"Revisión prioritaria"`. Con 5 o más el veredicto sería `"Revisión prioritaria"`.

> Nota de fidelidad del respaldo: la lista de 20 posiciones conserva 9 `INFO`, 4 `ERROR`, 5 `WARNING` y 2 malformadas para reproducir la salida esperada oficial, que es el contrato que la referencia debe cumplir.

## Salida esperada

Ejecuta tu archivo desde la raíz del proyecto y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
Lineas leidas: 20
Lineas normalizadas: 18
Lineas omitidas: 2
Errores: 4 - Rutina local
Avisos: 5 - Revisión prioritaria
Salida: salida/normalizado.txt (escritura atomica)
--- Revision normalizada ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Alcance: localhost (127.0.0.1) y fixtures locales
```

Además `salida/normalizado.txt` debe contener exactamente 18 líneas, cada una con la forma `NIVEL: mensaje`, y no debe quedar ningún archivo `salida/normalizado.tmp` residual. Las 2 omitidas viajan al registro de consola como advertencias (`WARNING: Linea omitida: ...`), no como traza cruda.

Convención de predicción previa: antes de completar cada TODO, el estudiante escribe su predicción (valor esperado y motivo); solo después de ejecutar el script compara el resultado obtenido con su predicción y con la salida esperada (predecir → ejecutar → comparar).

## Nota precisa sobre lo que el programa sí hace y lo que no hace

La normalización anclada **prepara el registro local para el cambio de turno sin exponer mitades**: 20 líneas leídas, 18 publicadas con forma única, 2 omitidas con motivo, dos pares contra el umbral y un archivo terminado que el lector `kit/` de la Sesión 14 puede consumir. No abre puertos, no toca red y no confirma un incidente. Pydantic sigue solo instalado y anunciado; ningún modelo se define hasta la Sesión 16.

## Nota precisa sobre errores con rutas y archivos

Errores que verás en esta sesión:

- `FileNotFoundError: [Errno 2] No such file or directory: 'datos/app.log'`: leíste una ruta relativa suelta desde un directorio distinto a la raíz; Python resolvió la ruta contra la consola, no contra el proyecto. La corrección es anclar con `Path(__file__).resolve().parent`, verificar con `dir` o `ls` que `datos/app.log` existe, volver a la raíz con `cd` y re-ejecutar con `↑`.
- `FileNotFoundError` al publicar en `salida/`: intentaste escribir el temporal sin crear la carpeta de salida; la escritura atómica exige la carpeta antes del temporal. La corrección es `output_path.parent.mkdir(parents=True, exist_ok=True)` antes de escribir, y comprobar después que solo queda `normalizado.txt` sin `.tmp` residual.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables, funciones, rutas y comentarios) se escribe en inglés (`fixture_lines`, `normalize_line`, `write_atomic`, `INPUT_PATH`, `error_total`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`; las constantes usan `UPPER_CASE`).

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué ancla cada ruta (`PROJECT_ROOT`, `INPUT_PATH`, `OUTPUT_PATH`, `TEMP_PATH`) y por qué nace de `__file__`.
- [ ] Qué devuelve cada llamada anclada y qué veredicto le toca a cada par.
- [ ] Qué líneas omite `normalize_line` y a dónde viaja el motivo de cada omitida.
- [ ] Qué garantiza el par temporal más renombrar y qué pasaría si escribieras directo sobre el final.
- [ ] Dónde viaja la declaración `encoding="utf-8"` y por qué se repite en lectura y escritura.
- [ ] Qué captura el `try/except FileNotFoundError` y qué imprime en vez de una traza cruda.
- [ ] Qué NO hace el programa (no modela con Pydantic aún, no abre puertos, no toca red, no confirma un incidente).
- [ ] Tu programa se ejecuta desde la raíz sin errores y muestra conteos, pares, ruta publicada y alcance.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, sin sintaxis nueva: cuenta el tercer nivel con las líneas limpias (`INFO` suma 9, así que también alcanza el umbral) y predice en papel el par antes de ejecutar con `↑`. Después ejecuta `python normalize_logs.py` desde una subcarpeta y predice qué ruta anclada sigue funcionando y por qué. Es solo práctica extra: no cambia tu calificación. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`normalize_shift.py`), distinto del `normalize_logs.py` de clase y del desafío opcional de arriba.

**Historia:** dejas lista la normalización del turno nocturno antes de entregarla, distinta del registro del día de clase. Partes de 20 líneas nuevas del turno, reutilizas la misma técnica anclada con umbral propio, publicas con el mismo par atómico y muestras el reporte con el mismo alcance local.

Crea manualmente `normalize_shift.py` en tu proyecto personal, reutilizando rutas ancladas con umbral arriba, tareas en medio y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables / llamadas |
|------|----------|---------------------|
| 1. Evidencia | Asigna el umbral, las 20 del turno y tu identidad; imprime el total (`20`) | `SHIFT_THRESHOLD = 5`, `shift_lines` (20 textos: 7 `WARNING`, 4 `ERROR`), `student_name`, `student_id` |
| 2. Anclado | Reutiliza `normalize_line`, `read_input_lines` y `write_atomic` bajo `main()` con la guardia; publica el turno | `read_input_lines(...)` → 20; `normalize_line(...)` → 18 más 2 omitidas; `write_atomic(...)` → `salida/turno_normalizado.txt` |
| 3. Comunicación | Reporte anclado del turno con los dos pares, los conteos y la ruta publicada | `print()` línea por línea |

Las 20 líneas del turno (escríbelas tal cual):

```python
SHIFT_THRESHOLD = 5
shift_lines = [
    "WARNING: turno nocturno iniciado",
    "INFO: ronda local sin novedad",
    "ERROR: sensor local sin respuesta",
    "WARNING: reintento de lectura local",
    "INFO: bitacora local verificada",
    "WARNING: cola de eventos llena",
    "INFO: respaldo local confirmado",
    "ERROR: archivo temporal corrupto",
    "WARNING: umbral cercano al limite",
    "INFO: inventario local actualizado",
    "WARNING: latencia alta en loopback",
    "ERROR: registro incompleto detectado",
    "INFO: limpieza de salida completada",
    "WARNING: reintento de conexion local",
    "INFO: auditoria local sin hallazgos",
    "WARNING: segundo reintento local",
    "INFO: cierre parcial registrado",
    "linea rota sin nivel",
    "",
    "ERROR: disco lleno en localhost",
]
```

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
Lineas leidas: 20
Lineas normalizadas: 18
Lineas omitidas: 2
Errores: 4 - Rutina local
Avisos: 7 - Revisión prioritaria
Salida: salida/turno_normalizado.txt (escritura atomica)
--- Revision normalizada del turno ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Umbral: 5 (solo lectura)
Alcance: localhost (127.0.0.1) y fixtures locales
```

> Notas de respaldo: el bloque de resumen replica la estructura del ejercicio de clase para el turno. Con tus propios datos el nombre y el identificador cambian, pero los pares deben coincidir.

**Antes de programar, analiza:** qué conteo anclado revisa el nivel de errores y qué veredicto le toca bajo el umbral; qué conteo revisa el nivel de avisos y por qué alcanza revisión prioritaria; qué llamada de publicación garantiza que no queden mitades y dónde viaja la declaración UTF-8 en vez de un modelo.

**Propósito real:** la normalización prepara el registro local para el cambio de turno sin exponer mitades: no abre puertos, no toca red y no confirma un incidente.

**Entrega:** explica en voz alta la cadena ancla → normaliza → escritura atómica. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos. Ningún script de la sesión abre sockets ni envía tráfico: solo lee y escribe archivos dentro de tu carpeta del curso.
