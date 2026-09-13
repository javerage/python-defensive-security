# Sesión 03: Cadenas, índices y limpieza de texto

Bienvenido a la **Sesión 03** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **limpiar una línea de registro sintética local, leer su primer carácter, extraer su marca temporal, normalizar su nivel de alerta, enmascarar su nombre de práctica, comprobar si contiene el marcador local y mostrar un resumen simple en consola**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `log_normalizer.py` y escribe el ejercicio.
4. Ejecuta `python log_normalizer.py` y comprueba el resumen con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `log_normalizer.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que revisa registros de práctica antes de una revisión de seguridad. Recibes una línea de registro local con relleno de espacios y un salto de línea final que estorbaría cualquier lectura. Para dejarla utilizable quitas ese relleno, compruebas que la limpieza funcionó mirando su primer carácter, lees su marca temporal, normalizas su nivel de alerta a mayúsculas, enmascaras su nombre de práctica en una copia saneada y compruebas si el texto contiene el marcador local `127.0.0.1`. Finalmente muestras un resumen que permite identificar de quién es el trabajo, revisar cada resultado y saber si el marcador aparece en la línea.

## Secuencia conceptual

Cada línea del programa sigue este orden explícito:

1. **Texto sucio:** la línea cruda trae relleno que hay que quitar.
2. **Limpieza:** `strip()` produce una copia limpia y `len()` mide ambas versiones.
3. **Extracción:** el índice `[0]` lee el primer carácter y el corte `[:19]` aísla la marca temporal.
4. **Normalización:** `find()` localiza los corchetes, el corte entre ellos aísla la palabra y `upper()` la muestra uniforme; `replace()` enmascara el nombre en una copia saneada.
5. **Marcador local:** `find("127.0.0.1")` localiza el marcador y la comparación `!= -1` produce un valor booleano (`True` o `False`).
6. **Comunicación:** `print()` lleva cada resultado al resumen: un encabezado más diez líneas de datos.

## Cómo se lee una cadena en Python (en clase, sin evaluar)

Una cadena es una secuencia de caracteres donde cada posición se cuenta desde cero:

```python
cleaned_log = "2026-09-10 11:15:32 [warn] ..."
print(cleaned_log[0])   # Muestra: 2
print(cleaned_log[:19]) # Muestra: 2026-09-10 11:15:32
```

El **índice** `0` lee el primer carácter y el **corte** `[:19]` toma los caracteres del `0` al `18` (el `19` queda fuera). Si pides una posición que no existe, el programa se interrumpe con `IndexError`.

Tres precisiones y nada más:

- Las cadenas son **inmutables**: ningún método cambia la cadena original en su lugar; cada método devuelve una cadena nueva.
- `find()` devuelve la **posición** donde aparece el texto buscado, o `-1` si no aparece. Por eso se compara con `!= -1`.
- En esta sesión trabajamos solo `str`, `int` y `bool`. Python posee otros tipos y colecciones que se estudiarán después.

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
notepad log_normalizer.py

# 5. Ejecuta tu ejercicio
python log_normalizer.py
```

> Si PowerShell bloquea la activación, ejecuta primero `Set-ExecutionPolicy -Scope Process Bypass` y vuelve a activar.

### Linux / macOS (Bash / Zsh)

```bash
# 1. Localiza y abre tu proyecto de la sesión 01
cd ~/curso-python-defensivo
ls

# 2. Activa el entorno virtual
source .venv/bin/activate

# 3. Verifica el intérprete (debe mostrar Python 3.13.x)
python3 --version

# 4. Crea manualmente el archivo nuevo para esta sesión
touch log_normalizer.py

# 5. Ejecuta tu ejercicio
python3 log_normalizer.py
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

### Linux / macOS (Bash / Zsh)

```bash
mkdir -p ~/curso-python-defensivo
cd ~/curso-python-defensivo
python3.13 -m venv .venv
source .venv/bin/activate
python3 --version
```

Debes ver el prefijo `(.venv)` en el prompt y la versión Python 3.13.x.

## Ejercicio obligatorio

Crea `log_normalizer.py` con código lineal (sin funciones, sin `try/except`, sin colecciones, sin `if`) que haga lo siguiente:

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Entrada sucia | Asigna la línea cruda de práctica y mide su longitud (de cuándo es el evento y con qué relleno llegó) | `raw_log_entry`, `raw_length = len(...)`, `student_name`, `student_id` |
| 2. Limpieza | Quita el relleno y mide la copia limpia | `cleaned_log = raw_log_entry.strip()`, `cleaned_length = len(...)` |
| 3. Extracción | Lee el primer carácter, aísla la marca temporal y normaliza la alerta | `first_char = cleaned_log[0]`, `timestamp_str = cleaned_log[:19]`, `bracket_start`, `bracket_end`, `alert_level = ... .upper()` |
| 4. Máscara y marcador | Enmascara el nombre de práctica, localiza el marcador local y lee la IP | `sanitized_log = ... .replace(...)`, `loopback_index = ... .find(...)`, `is_localhost = loopback_index != -1`, `target_ip = ...` |
| 5. Comunicación | Imprime el encabezado y las diez líneas de datos con `print()` (evidencia legible para revisar cada resultado) | Encabezado más diez líneas de datos legibles |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
--- Resumen del registro ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Longitud cruda: 94
Longitud limpia: 87
Primer caracter: 2
Marca temporal: 2026-09-10 11:15:32
Nivel de alerta: WARN
Contiene marcador local: True
IP local: 127.0.0.1
Registro saneado: 2026-09-10 11:15:32 [warn] AuthFailure ip=127.0.0.1 port=8080 user=analyst_sandbox status=401
```

Con tus propios datos el nombre y el identificador cambian, pero la forma del resumen es siempre la misma: un encabezado y diez líneas de datos legibles. Las palabras `AuthFailure` y `port=8080` viajan en la copia saneada como contexto; hoy no se extraen por separado.

## Nota precisa sobre el marcador local

`find("127.0.0.1")` solo busca esos caracteres dentro del texto. `True` significa que el marcador aparece en esta línea; no abre conexiones, no revisa la red y no prueba nada sobre otros equipos. Decidir automáticamente a partir de este valor con `if` lo aprenderás en la sesión 04; hoy basta con observarlo y mostrarlo.

## Nota precisa sobre errores de cadenas

Errores que verás en esta sesión:

- `IndexError: string index out of range`: pediste una posición que no existe (por ejemplo `cleaned_log[150]` en una línea de 87 caracteres, con índices válidos de 0 a 86).
- `TypeError: 'str' object does not support item assignment`: intentaste cambiar un carácter en su lugar (por ejemplo `cleaned_log[0] = "#"`). Las cadenas son inmutables: se construye una copia nueva con `replace()` o con cortes.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`raw_log_entry`, `cleaned_log`, `timestamp_str`, `alert_level`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`). El ejemplo usa f-strings como forma cómoda de mostrar variables; su sintaxis no es un objetivo evaluado.

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Por qué limpias con `strip()` antes de leer la marca temporal.
- [ ] Qué lee `cleaned_log[0]` y qué aísla `cleaned_log[:19]`.
- [ ] Cómo localizas los corchetes con `find()` y qué hace `upper()`.
- [ ] Por qué `replace()` crea una copia nueva en vez de cambiar la original.
- [ ] Qué devuelve `find()` cuando el marcador no aparece y qué produce la comparación `!= -1`: si el texto contiene el marcador local (el programa solo presenta la evidencia, no revisa la red).
- [ ] Cómo llega cada resultado al resumen (qué variable muestra cada línea).
- [ ] Tu resumen se ejecuta sin errores y muestra el encabezado más las diez líneas de datos.

## Desafío opcional para avance rápido (sin impacto en la evaluación)

Si terminas antes, extrae el nombre de práctica de forma dinámica (sin adivinar su posición): localiza `"user="` con `find()`, suma su longitud para hallar el inicio, localiza el siguiente espacio con `find(" ", inicio)` y corta entre ambos. Es solo práctica extra dentro de la clase con operaciones ya explicadas: no cambia tu calificación y no usa `if`, funciones ni expresiones regulares. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia un poco más compleja para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal.

**Historia:** actúas como el auxiliar responsable de dejar lista una nota local de laboratorio para su revisión. El punto de partida es una nota de práctica sobre una revisión de inventario, distinta del registro de autenticación de clase. Para dejarla utilizable registras de quién es el trabajo (`student_name`, `student_id`), quitas el relleno que corrompería cualquier lectura por posición (`cleaned_note`), compruebas la limpieza con su primer carácter (`first_char`), lees de qué caso se trata con su código fijo de 12 caracteres (`case_id`), normalizas su nivel de nota a mayúsculas (`note_level`), enmascaras el alias de práctica en una copia saneada (`sanitized_note`) y compruebas si el texto contiene la etiqueta local de referencia (`is_local_ref`). `True` solo indica que esos caracteres aparecen en esta nota; no es un estándar universal, no revisa la red ni prueba nada sobre otros equipos. El resumen le sirve a la persona responsable de revisar el caso para verificar cada resultado en un solo lugar.

Crea manualmente `record_analysis.py` en tu proyecto personal, con código lineal y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables y fórmula |
|------|----------|---------------------|
| 1. Entrada sucia | Asigna la nota cruda de práctica y mide su longitud (de qué caso se trata y con qué relleno llegó) | `raw_lab_note`, `raw_note_length = len(...)`, `student_name`, `student_id` |
| 2. Limpieza | Quita el relleno y mide la copia limpia | `cleaned_note = raw_lab_note.strip()`, `cleaned_note_length = len(...)` |
| 3. Extracción | Lee el primer carácter, aísla el código del caso y normaliza el nivel | `first_char = cleaned_note[0]`, `case_id = cleaned_note[:12]`, `bracket_start`, `bracket_end`, `note_level = ... .upper()` |
| 4. Máscara y referencia | Enmascara el alias de práctica, localiza la etiqueta local y lee el código | `sanitized_note = ... .replace("operador_temporal", "practicante_local")`, `marker_index = ... .find("LAB-LOCAL")`, `is_local_ref = marker_index != -1`, `reference_code = ...` |
| 5. Comunicación | Resumen legible para quien revisa el caso | `print()` línea por línea |

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
--- Resumen de la nota ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Longitud cruda: 105
Longitud limpia: 98
Primer caracter: L
Caso: LAB-2026-041
Nivel de nota: INFO
Contiene referencia local: True
Codigo de referencia: LAB-LOCAL-07
Nota saneada: LAB-2026-041 [info] nota: revision de inventario local ref=LAB-LOCAL-07 operador=practicante_local
```

Con tus propios datos el nombre y el identificador cambian, pero la forma del resumen es siempre la misma: un encabezado y diez líneas de datos legibles.

### Punto de partida: la nota cruda (cópiala tal cual)

```python
raw_lab_note = "   LAB-2026-041 [info] nota: revision de inventario local ref=LAB-LOCAL-07 operador=operador_temporal   \n"
```

Los tres espacios iniciales, los tres espacios finales y el `\n` final son suciedad deliberada para practicar `strip()`. Cópiala exacta y no los borres del literal: el programa debe quitarlos con `raw_lab_note.strip()`. No necesitas abrir el repositorio ni consultar la solución para completar la tarea.

**Antes de programar, analiza:** qué relleno rodea la nota y por qué corrompería un corte de posición fija; qué código fijo abre la nota limpia y cuántos caracteres usa; qué palabra viaja entre `[` y `]` y cómo se muestra uniforme; qué alias de práctica debe enmascararse y qué etiqueta local debe buscarse.

**Propósito real:** el resumen organiza los resultados de la nota para la revisión humana. No confirma un incidente, no revisa la red y no sustituye la investigación.

**Entrega:** explica en voz alta por qué limpias con `strip()` antes de cortar, qué lee cada operación (`[0]`, `[:12]`, `find()`, `upper()`, `replace()`), qué devuelve `find()` cuando la etiqueta no aparece y qué produce la comparación `!= -1`. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con una línea de texto sintética escrita en tu propia máquina. No hay conexiones de red ni destinos externos.
