# Sesión 04: Decisiones condicionales y clasificación local

Bienvenido a la **Sesión 04** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **clasificar una observación sintética de laboratorio con condicionales: comprobar una regla de volumen con `if/else`, asignar una prioridad de revisión de tres niveles con una cadena breve `if/elif/else` ordenada de la condición más exigente a la menos exigente, y mostrar un resumen simple en consola**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `incident_classifier.py` y escribe el ejercicio.
4. Ejecuta `python incident_classifier.py` y comprueba el resumen con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `incident_classifier.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que prepara observaciones de práctica para revisión humana. El cuaderno de práctica registra **una observación**: 9 intentos fallidos de acceso en la máquina local de entrenamiento. Antes de pasársela a quien revisa el caso, la clasificas en tu propia máquina con dos decisiones encadenadas. Primero compruebas una regla de volumen ya conocida (`>= 5`, de la sesión 02) con un `if/else` simple: la comparación produce un valor booleano y ese booleano, usado directamente como condición, elige un mensaje. Después asignas una prioridad de revisión de tres niveles con una cadena breve `if/elif/else` sobre el mismo conteo: las reglas didácticas del laboratorio (`>= 10` se revisa hoy con un mentor, `>= 5` se agenda esta semana) ordenan la revisión humana. Finalmente muestras un resumen que permite identificar de quién es el trabajo, revisar cada resultado y saber qué rama se ejecutó.

## Secuencia conceptual

Cada decisión del programa sigue este orden explícito:

1. **Evidencia:** el conteo observado (`failed_attempts = 9`).
2. **Expresión booleana:** la comparación `>=` produce `True` o `False`.
3. **Condición:** ese valor decide qué rama se ejecuta.
4. **Rama ejecutada:** Python corre **solo la primera rama verdadera**.
5. **Mensaje/recomendación:** etiquetas y recomendaciones para revisión humana.

## Cómo decide Python con `if` (en clase, sin evaluar nada más)

Una condición elige **una sola rama**:

```python
many_failed_attempts = failed_attempts >= 5

if many_failed_attempts:
    volume_message = "Regla de volumen cumplida: 5 o más intentos"
else:
    volume_message = "Regla de volumen no cumplida: menos de 5 intentos"
```

La comparación `>=` produce el booleano y el `if/else` lo usa directamente como condición: con `True` corre la primera rama, con `False` corre la segunda. Nunca corren las dos.

Con tres niveles, la cadena se lee de arriba a abajo y **se detiene en la primera condición verdadera**:

```python
if failed_attempts >= 10:
    risk_label = "HIGH"
elif failed_attempts >= 5:
    risk_label = "MEDIUM"
else:
    risk_label = "LOW"
```

Por eso el orden va de la condición más exigente (`>= 10`) a la menos exigente (`>= 5`): con 9, la primera condición es falsa y la segunda es verdadera, así que corre `MEDIUM`. Si invirtieras el orden, 12 se detendría en `>= 5` y `HIGH` nunca correría, sin ningún mensaje de error.

Tres precisiones y nada más:

- En esta sesión las condiciones usan la comparación `>=` y un booleano ya calculado. Combinar condiciones con `and`/`or`, buscar con `in`, comparar identidad con `is None` y anidar `if` dentro de otro `if` quedan para sesiones posteriores.
- Los umbrales `>= 10` y `>= 5` son **reglas didácticas de este laboratorio** para practicar condicionales: no son estándares universales y no prueban un ataque.
- En esta sesión trabajamos `str`, `int` y `bool` con `if`/`elif`/`else`. Python posee otros tipos, colecciones y estructuras que se estudiarán después.

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
notepad incident_classifier.py

# 5. Ejecuta tu ejercicio
python incident_classifier.py
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
touch incident_classifier.py

# 5. Ejecuta tu ejercicio
python3 incident_classifier.py
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
touch incident_classifier.py

# 5. Ejecuta tu ejercicio
python3 incident_classifier.py
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

Crea `incident_classifier.py` con código lineal (sin funciones, sin `try/except`, sin colecciones, sin `and`/`or`/`in`/`is None`, sin anidación, sin `imports`) que haga lo siguiente:

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Evidencia | Asigna el conteo observado de la práctica y tu identidad (de qué caso se trata y de quién es el trabajo) | `failed_attempts = 9`, `student_name`, `student_id` |
| 2. Regla de volumen | Comprueba la regla explícita del laboratorio (5 o más intentos) y decide el mensaje con `if/else` (la comparación produce el booleano; el booleano, usado directo, elige la rama) | `many_failed_attempts = failed_attempts >= 5`, `volume_message` con `if/else` |
| 3. Prioridad | Clasifica el mismo conteo en tres niveles con `if/elif/else` de la condición más exigente a la menos exigente (`>= 10` hoy con un mentor, `>= 5` esta semana, lo demás al registro local) | `risk_label`, `review_action` con `if/elif/else` |
| 4. Comunicación | Imprime el encabezado y las siete líneas de datos con `print()` (evidencia legible para revisar qué rama se ejecutó) | Encabezado más siete líneas de datos legibles |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y reglas visibles (léelas antes de programar)

```python
failed_attempts = 9
```

| Regla del laboratorio | Condición | Etiqueta | Recomendación |
|-----------------------|-----------|----------|---------------|
| Revisión de hoy | `failed_attempts >= 10` | `HIGH` | `Revisar hoy con un mentor` |
| Revisión de la semana | `failed_attempts >= 5` | `MEDIUM` | `Agendar revisión esta semana` |
| Registro local | en otro caso | `LOW` | `Conservar en el registro local` |

Regla de volumen: `many_failed_attempts = failed_attempts >= 5` (`True` 5 o más intentos, `False` menos de 5). Los umbrales son reglas didácticas de este laboratorio, no estándares universales.

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
--- Resumen del incidente ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Intentos fallidos: 9
Regla de volumen cumplida: True
Mensaje de volumen: Regla de volumen cumplida: 5 o más intentos
Nivel de riesgo: MEDIUM
Revisión recomendada: Agendar revisión esta semana
```

Con tus propios datos el nombre y el identificador cambian, pero la forma del resumen es siempre la misma: un encabezado y siete líneas de datos legibles. Con 9, la primera condición (`>= 10`) es falsa y la segunda (`>= 5`) es verdadera: corre `MEDIUM`.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El resumen **organiza la evidencia para la revisión humana**: etiquetas (`HIGH`, `MEDIUM`, `LOW`) y recomendaciones (`Revisar hoy con un mentor`, `Agendar revisión esta semana`, `Conservar en el registro local`). No bloquea tráfico, no aísla equipos, no termina procesos y no abre conexiones. `True` solo indica que se cumple la regla correspondiente.

## Nota precisa sobre errores con condicionales

Errores que verás en esta sesión:

- `IndentationError: expected an indented block after 'if' statement on line 47`: escribiste la rama sin sangría (sin los 4 espacios). Python exige indentar el cuerpo de cada rama.
- Error silencioso de orden: si pruebas `>= 5` antes que `>= 10`, un valor como 12 se detiene en `MEDIUM` y `HIGH` nunca corre, sin ningún mensaje de error. La corrección es ordenar de la condición más exigente a la menos exigente, porque solo se ejecuta la primera rama verdadera.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`failed_attempts`, `many_failed_attempts`, `risk_label`, `review_action`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`). El ejemplo usa f-strings como forma cómoda de mostrar variables; su sintaxis no es un objetivo evaluado.

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué evidencia observaste (`failed_attempts = 9`) y qué regla comprueba `>= 5`.
- [ ] Qué produce la comparación (`True` o `False`) y cómo ese booleano, usado directo como condición, elige una rama del `if/else`.
- [ ] Por qué la cadena `if/elif/else` va de la condición más exigente a la menos exigente y qué rama corre con 9.
- [ ] Qué pasaría con 12 si invirtieras el orden, y por qué Python no mostraría ningún error.
- [ ] Qué significa cada etiqueta y recomendación, y qué NO hace el programa (no bloquea, no aísla, no contacta nada).
- [ ] Cómo llega cada resultado al resumen (qué variable muestra cada línea).
- [ ] Tu resumen se ejecuta sin errores y muestra el encabezado más las siete líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, cambia `failed_attempts` a `3` y luego a `12`, ejecuta de nuevo con `↑` y di en voz alta qué rama se ejecuta en cada caso y por qué. Es solo práctica extra dentro de la clase con valores ya explicados: no cambia tu calificación y no usa sintaxis nueva. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia un poco más compleja para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`evaluacion_alerta.py`), distinto del `incident_classifier.py` de clase y del desafío opcional de arriba.

**Historia:** actúas como el auxiliar responsable de dejar lista una alerta local de práctica para su revisión. El punto de partida es la revisión nocturna del servicio local de práctica, distinta de la observación de intentos de acceso de clase. Para dejarla utilizable registras de quién es el trabajo (`student_name`, `student_id`), pides por teclado las líneas de error de su registro sintético y la respuesta promedio y las conviertes (`raw_error_lines = input("Líneas de error: ")`, `error_lines = int(raw_error_lines)`, `raw_avg_response_ms = input("Respuesta promedio en ms: ")`, `avg_response_ms = float(raw_avg_response_ms)`; reactiva la sesión 02 sin manejo de errores), compruebas la regla de volumen del laboratorio con `if/else` (`many_errors = error_lines >= 10`) y clasificas el tiempo de respuesta en tres niveles con `if/elif/else` (`>= 1000.0` se revisa hoy con un mentor, `>= 500.0` se agenda esta semana, lo demás queda en el registro local). `True` solo indica que se cumple la regla correspondiente; los umbrales son reglas didácticas, no estándares universales, y no prueban un ataque. El resumen le sirve a la persona responsable de revisar el caso para priorizar la revisión humana en un solo lugar. La tarea integra entrada → conversión → decisión → comunicación, mientras el ejercicio principal aísla decisión → comunicación.

Crea manualmente `evaluacion_alerta.py` en tu proyecto personal, con código lineal y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables y fórmula |
|------|----------|---------------------|
| 1. Evidencia | Pide la alerta por teclado y conviértela (reactiva la sesión 02), más tu identidad | `raw_error_lines = input("Líneas de error: ")`, `error_lines = int(raw_error_lines)`, `raw_avg_response_ms = input("Respuesta promedio en ms: ")`, `avg_response_ms = float(raw_avg_response_ms)`, `student_name`, `student_id` |
| 2. Regla de volumen | Comprueba la regla explícita del laboratorio (10 o más líneas de error) y decide el mensaje con `if/else` | `many_errors = error_lines >= 10`, `volume_message` con `if/else` |
| 3. Prioridad | Clasifica el tiempo de respuesta en tres niveles, de la condición más exigente a la menos exigente | `if avg_response_ms >= 1000.0` → `HIGH`, `elif >= 500.0` → `MEDIUM`, `else` → `LOW`; `risk_label`, `review_action` |
| 4. Comunicación | Resumen legible para quien revisa el caso | `print()` línea por línea |

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
--- Resumen de la alerta ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Líneas de error: 14
Regla de volumen cumplida: True
Mensaje de volumen: Regla de volumen cumplida: 10 o más líneas de error
Respuesta promedio: 850.0 ms
Nivel de riesgo: MEDIUM
Revisión recomendada: Agendar revisión esta semana
```

Con tus propios datos el nombre y el identificador cambian, pero la forma del resumen es siempre la misma: un encabezado y siete líneas de datos legibles. Con 850.0, la primera condición (`>= 1000.0`) es falsa y la segunda (`>= 500.0`) es verdadera: corre `MEDIUM`.

### Punto de partida: la entrada por teclado (escríbela tal cual)

```python
raw_error_lines = input("Líneas de error: ")
error_lines = int(raw_error_lines)
raw_avg_response_ms = input("Respuesta promedio en ms: ")
avg_response_ms = float(raw_avg_response_ms)
```

Escribe ambas peticiones exactas con esos prompts y esas conversiones: el programa debe pedir y convertir antes de decidir. Para comprobar, escribe `14` y `850.0`; el resumen debe coincidir con el ejemplo único de abajo. Si se escribe texto no numérico, el programa se interrumpe con `ValueError`: es el comportamiento esperado y no se captura con `try/except` en esta sesión. Sin validación, reintentos, bucles, funciones, `try/except`, `imports` ni conceptos futuros. No necesitas abrir el repositorio ni consultar la solución para completar la tarea.

**Antes de programar, analiza:** qué valor de teclado alimenta el booleano de volumen tras `int()` y qué regla comprueba `>= 10`; qué número convertido alimenta la cadena de tres niveles y por qué `>= 1000.0` debe probarse antes que `>= 500.0`; qué rama corre con 850.0 y qué le pide a un humano hacer (y qué no hace por sí sola).

**Propósito real:** el resumen organiza la evidencia local para la revisión humana. No confirma un incidente, no bloquea nada, no aísla equipos y no sustituye la investigación.

**Entrega:** explica en voz alta la cadena evidencia → expresión booleana → condición → rama ejecutada → mensaje/recomendación para ambas decisiones, por qué importa el orden de la cadena y cómo llega cada resultado al resumen. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
