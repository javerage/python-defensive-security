# Sesión 05: Lógica compuesta y validación local

Bienvenido a la **Sesión 05** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **validar una configuración sintética de laboratorio con lógica compuesta: comprobar un rango con `and`, un conjunto permitido con `or`, detectar ausencia con `is None`, producir un mensaje específico por campo y combinar cada resultado parcial en un veredicto final legible en consola**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `config_check.py` y escribe el ejercicio.
4. Ejecuta `python config_check.py` y comprueba el resumen con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `config_check.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Eres parte del equipo que prepara el laboratorio defensivo local antes de cada jornada. Otra persona del equipo te entrega una ficha con la configuración que se usará en la práctica: puerto local `18080`, ruta `configs/lab.conf`, nivel `WARNING` y una casilla para la nota de quien revisa. Recibes esa ficha antes de la práctica; no la inventas tú: tu trabajo es validarla en tu propia máquina con cuatro chequeos encadenados antes de entregársela a quien revisa el caso.

El problema es que cada campo puede impedir una práctica reproducible o dejar una revisión incompleta: un puerto fuera del rango del laboratorio no corresponde a lo esperado, una ruta desconocida impide localizar la configuración prevista, un nivel no permitido desordena la revisión y una nota ausente deja sin contexto a quien revisa. Si el programa aceptara todo con un único mensaje genérico («todo bien»), nadie sabría qué campo debe corregirse.

La consecuencia es humana y operativa, sin dramatismo: la persona que revisa pierde tiempo buscando qué campo falló, la práctica empieza tarde o la revisión queda a medias porque falta información. Por eso cada campo necesita su propio chequeo y su propio mensaje.

La decisión que debes producir es clara: determinar si la configuración queda lista para revisión o requiere correcciones específicas, campo por campo.

Cada dato tiene un significado causal dentro de esta historia. El puerto `18080` es el puerto local observado de esta práctica: debe estar dentro del rango del laboratorio (`1` a `65535`) para considerarse correspondiente. La ruta `configs/lab.conf` es la ruta conocida del laboratorio: solo la coincidencia exacta con esa ruta se considera válida, y la comprobación es simulada (ningún disco se toca). El nivel `WARNING` es el nivel de registro anotado: debe ser uno de los tres niveles permitidos (`INFO`, `WARNING`, `ERROR`) porque esos niveles organizan la revisión humana. La ausencia de nota (`None`) significa que no llegó ninguna nota del revisor: no es un error, pero debe quedar registrado para que la revisión continúe sin comentarios.

Límites honestos: el programa solo valida estos datos sintéticos y recomienda; no abre puertos, no toca archivos, no conecta red ni confirma ataques. `True` solo indica que se cumple la regla correspondiente del laboratorio.

### Mapeo dominio → código (léelo antes de programar)

| Dato del caso | Variable | Pregunta / regla | Booleano y mensaje producido | Contribución al veredicto |
|---------------|----------|------------------|------------------------------|---------------------------|
| Puerto local `18080` | `target_port` | ¿Está dentro del rango `1-65535`? (`target_port >= 1 and target_port <= 65535`) | `port_ok` (`True`/`False`) + `port_message` («Puerto válido» / «Puerto inválido») | Una parte de `config_ready`; si es `False`, la configuración se detiene |
| Ruta `configs/lab.conf` | `config_path` (contra `known_config_path`) | ¿Está vacía? ¿Coincide con la ruta conocida? (`if/elif/else`) | `path_ok` (`True`/`False`) + `path_message` (vacía / desconocida / válida) | Una parte de `config_ready`; si es `False`, la configuración se detiene |
| Nivel `WARNING` | `log_level` | ¿Coincide con alguna de las tres opciones? (`== "INFO" or == "WARNING" or == "ERROR"`) | `level_ok` (`True`/`False`) + `level_message` («Nivel válido» / «Nivel inválido») | Una parte de `config_ready`; si es `False`, la configuración se detiene |
| Ausencia de nota (`None`) | `reviewer_note` | ¿No llegó ninguna nota? (`reviewer_note is None`) | `note_missing` (`True`/`False`) + `note_message` («Sin nota…» / «Nota registrada») | Informa a la revisión humana; no bloquea el veredicto |
| Veredicto combinado | `config_ready`, `needs_fix`, `final_decision` | ¿Cada resultado parcial es `True`? (`port_ok and path_ok and level_ok`) | `config_ready` (`True`/`False`), `needs_fix = not config_ready`, `final_decision` (lista / detenida) | Decisión final y recomendación para quien revisa |

Primero abstrae con la historia y la tabla de mapeo; después codifica siguiendo la secuencia campo → chequeo booleano → mensaje específico → veredicto combinado → recomendación.

## Secuencia conceptual

Cada validación del programa sigue este orden explícito:

1. **Campo:** el valor observado (`target_port = 18080`).
2. **Chequeo booleano:** la expresión con `and`/`or`/`is None` produce `True` o `False`.
3. **Mensaje específico:** cada campo deja su propio mensaje según su regla.
4. **Veredicto combinado:** `and` une cada resultado parcial; basta un `False` para detener la configuración.
5. **Recomendación:** la decisión final organiza la revisión humana.

## Cómo combina Python con `and`, `or` y `not` (en clase, sin evaluar nada más)

Con `and` cada parte debe cumplirse; Python se detiene en el primer `False` (cortocircuito):

```python
port_ok = target_port >= 1 and target_port <= 65535
```

Con `18080`, la primera comparación es verdadera y la segunda también: `port_ok` es `True`. Con `0` o con `99999`, una de las dos es falsa y `port_ok` es `False` sin necesidad de seguir evaluando.

La comparación encadenada equivalente `1 <= target_port <= 65535` es válida, idiomática y compacta en Python y expresa matemáticamente que el valor está entre ambos límites; se enseñará como alternativa una vez comprendidas las dos comparaciones. No es la forma principal de este ejercicio porque oculta el `and` que la sesión pretende practicar. Compromiso: legibilidad matemática y menor repetición frente a visibilidad explícita del operador lógico.

Con `or` basta una sola coincidencia:

```python
level_ok = log_level == "INFO" or log_level == "WARNING" or log_level == "ERROR"
```

Con `WARNING`, la segunda comparación ya es verdadera y `level_ok` es `True`. Con `DEBUG`, las tres son falsas y `level_ok` es `False`.

Con `not` inviertes un veredicto:

```python
needs_fix = not config_ready
```

### Qué es `None` y cómo se detecta (nada más)

`None` representa la ausencia de valor en Python y cumple un propósito similar a `null` en otros lenguajes, pero es el objeto único `None` de Python. La forma idiomática de detectarlo es `value is None`: `is` comprueba identidad con ese objeto único, no una igualdad de contenido, así que `== None` no se enseña como alternativa en esta sesión.

```python
note_missing = reviewer_note is None
```

No confundas `None` con `""`, `0` ni `False`: esos son valores presentes aunque sean falsey (texto vacío, número cero y falso lógico). En el dominio de esta sesión, «no llegó una nota» (`None`) no es igual a «llegó una nota vacía» (`""`): lo primero es ausencia de valor y lo segundo es un valor presente.

**Concepto:** la presencia se pregunta con la forma negativa idiomática `value is not None`, no con `not value is None`. `is`/`is not` preguntan identidad (si es el mismo objeto, como el objeto único `None`); `==`/`!=` preguntan igualdad de valor (si el contenido coincide, como el texto del nivel). Las cadenas se comparan con `==`: Python no usa `.equals()` para esta comparación y no se debe usar `is` con cadenas. `None`, `""`, `0` y `False` pueden ser falsey, pero no significan lo mismo: cada uno es un valor distinto.

```python
reviewer_note = None
reviewer_note is None        # True: ausencia
reviewer_note is not None    # False: no hay presencia
log_level = "WARNING"
log_level == "WARNING"       # True: igualdad de valor
log_level != "INFO"          # True: desigualdad de valor
```

**Predicción 1:** con `reviewer_note = None`, ¿qué vale `reviewer_note is not None`? Resultado: `False`, porque no hay presencia: la ausencia ya se confirma con `is None`. **Predicción 2:** con `log_level = ""`, ¿qué vale la cadena con `or` de esta sesión? Resultado: `False`, porque el texto vacío no coincide con ninguna opción permitida. **Conexión con el ejercicio:** en tu programa, la nota usa identidad con `None` (`is None`) y el nivel usa igualdad de cadenas (`==` con `or`).

| Forma | Qué pregunta | Significado y uso |
|-------|--------------|-------------------|
| `reviewer_note is None` | ¿Es ausencia? | Ausencia: no llegó ninguna nota. Se usa. |
| `reviewer_note is not None` | ¿Hay presencia? | Presencia: sí llegó una nota. Se usa; es la forma negativa idiomática. |
| `log_level == "WARNING"` | ¿El valor coincide? | Igualdad de valor entre cadenas. Se usa. |
| `log_level != "INFO"` | ¿El valor difiere? | Desigualdad de valor entre cadenas. Se usa como ejemplo de la forma. |
| `is` con cadenas | — | No se usa: las cadenas se comparan con `==`. No uses `is` con cadenas. |
| `.equals()` | — | No se usa: Python no usa `.equals()` para esta comparación. |
| `== None` | — | No se usa: la ausencia se detecta con `is None`. |

> **Cuadro: ¿y `student_name is not None and student_name == "Juan"`?** Esa combinación es válida pero redundante si solo se pregunta por el valor: para saber si el nombre es `"Juan"` basta `student_name == "Juan"`. La primera parte (`student_name is not None`) solo tiene sentido como guardia antes de operar con un posible `None`, es decir, comprobar presencia antes de operar con ese valor (por ejemplo, antes de llamar un método sobre él). Por eso NO se añade al programa principal: no es requisito ni TODO. El ejercicio ya distingue presencia de nota (con `is None`) de valor de nivel (con `==`).

Tres precisiones y nada más:

- En esta sesión las condiciones se combinan con `and`/`or` y se niegan con `not`; la ausencia se detecta con `is None`. Existe además una forma compacta de elegir entre dos valores en una sola línea (el operador ternario), pero **solo se menciona: no se usa ni se evalúa en esta sesión**.
- El rango `1-65535`, la ruta conocida `configs/lab.conf` y los niveles `INFO`/`WARNING`/`ERROR` son **reglas didácticas de este laboratorio** para practicar lógica compuesta: no son estándares universales y `True` solo indica que se cumple la regla correspondiente.
- El currículo llama a este paso `validar_config` con retorno anticipado, pero las funciones (`def`/`return`) llegan en la Sesión 11. Hasta entonces cada chequeo corre de arriba a abajo en un guion lineal: cada resultado parcial se guarda en su propia variable booleana y el veredicto final lee esas variables. Mismas decisiones, sin llamada a función todavía.

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
notepad config_check.py

# 5. Ejecuta tu ejercicio
python config_check.py
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
touch config_check.py

# 5. Ejecuta tu ejercicio
python3 config_check.py
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
touch config_check.py

# 5. Ejecuta tu ejercicio
python3 config_check.py
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

## Qué forma de `if` elegir (reactivación breve de la Sesión 04, antes del reto)

En la Sesión 04 una condición elegía una rama; hoy cada mensaje necesita la forma adecuada. Tres formas, de menor a mayor. El **if simple** es una sola acción informativa que solo ocurre a veces: si la condición es `True`, el bloque corre; si es `False`, se omite y el programa continúa. El `else` es opcional y aquí no hace falta, porque no hay respuesta alternativa:

```python
lab_door_open = True

if lab_door_open:
    print("Puerta abierta: pasa al puesto de trabajo")

print("El programa continúa aquí")
```

Con `True` ves ambos mensajes; con `False`, solo el último. Cuidado de principiante: si una variable se crea únicamente dentro de un `if` simple y la condición es `False`, esa variable puede no existir después. Por eso en esta sesión cada mensaje nace dentro de su rama completa.

El **if/else** cubre dos caminos mutuamente excluyentes cuando ambos necesitan una respuesta. Reutiliza un booleano ya conocido:

```python
if port_ok:
    port_message = "Puerto válido: dentro del rango 1-65535"
else:
    port_message = "Puerto inválido: fuera del rango 1-65535"
```

El **if/elif/else** ordena tres o más alternativas. Recuerda el ejemplo de la Sesión 04 con `failed_attempts = 9`: `elif` significa «si lo anterior no se cumplió, prueba esta condición»; el `else` no lleva condición y captura el caso restante. Solo se ejecuta la primera rama verdadera: con 9, la primera es falsa y la segunda verdadera, así que corre `MEDIUM`:

```python
if failed_attempts >= 10:
    risk_label = "HIGH"
elif failed_attempts >= 5:
    risk_label = "MEDIUM"
else:
    risk_label = "LOW"
```

Reglas de forma: un bloque siempre empieza con `if`; puede haber cero o más `elif`; tanto `elif` como `else` son opcionales. Después viene el MAPEO hacia tu ruta (no el código final): vacía → inválida; distinta de la conocida → inválida; conocida → válida. Esa es la forma que el TODO 2.3 te pedirá reconocer.

## Ejercicio obligatorio

Crea `config_check.py` con código lineal (sin funciones, sin `try/except`, sin colecciones, sin bucles, sin `imports`, sin `regex`) que haga lo siguiente:

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Configuración | Asigna la configuración observada de la práctica y tu identidad (de qué caso se trata y de quién es el trabajo) | `target_port = 18080`, `config_path`, `known_config_path`, `log_level = "WARNING"`, `reviewer_note = None`, `student_name`, `student_id` |
| 2. Chequeos parciales | Comprueba el rango con `and` y decide el mensaje con `if/else`; decide la ruta con `if/elif/else` (vacía, desconocida, conocida); comprueba el nivel con `or` y decide el mensaje con `if/else`; detecta ausencia con `is None` y decide el mensaje con `if/else` | `port_ok`, `port_message`, `path_ok`, `path_message`, `level_ok`, `level_message`, `note_missing`, `note_message` |
| 3. Veredicto | Combina cada resultado parcial con `and`, niega con `not` y decide la recomendación con `if/else` | `config_ready = port_ok and path_ok and level_ok`, `needs_fix = not config_ready`, `final_decision` con `if/else` |
| 4. Comunicación | Imprime el encabezado y las doce líneas de datos con `print()` (evidencia legible para revisar cada chequeo y el veredicto) | Encabezado más doce líneas de datos legibles |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada sintética y reglas visibles (léelas antes de programar)

```python
target_port = 18080
config_path = "configs/lab.conf"
known_config_path = "configs/lab.conf"
log_level = "WARNING"
reviewer_note = None
```

| Campo | Condición | Válido | Mensaje cuando no se cumple |
|-------|-----------|--------|------------------------------|
| Puerto | `target_port >= 1 and target_port <= 65535` | `18080` → `True` | `Puerto inválido: fuera del rango 1-65535` |
| Ruta | `""` → inválida; distinta de la conocida → inválida; igual → válida | `configs/lab.conf` → válida | `Ruta inválida: está vacía` / `Ruta inválida: no es una ruta conocida del laboratorio` |
| Nivel | `== "INFO" or == "WARNING" or == "ERROR"` | `WARNING` → `True` | `Nivel inválido: usa INFO, WARNING o ERROR` |
| Nota | `reviewer_note is None` → sin nota | `None` → sin nota | (continúa sin comentarios) |
| Veredicto | `port_ok and path_ok and level_ok` | Todo `True` → lista | `Configuración detenida: corrige los campos marcados` |

El rango, la ruta conocida y los niveles son reglas didácticas de este laboratorio, no estándares universales.

## Casos de borde para explorar (cambia el valor y re-ejecuta con `↑`)

| Caso | Valor que pruebas | Resultado esperado |
|------|-------------------|--------------------|
| Puerto bajo | `target_port = 0` | `Puerto inválido`, veredicto detenido |
| Puerto común | `target_port = 80` | `Puerto válido` (sigue dentro del rango) |
| Puerto del laboratorio | `target_port = 18080` | `Puerto válido` (ejemplo canónico) |
| Puerto alto | `target_port = 99999` | `Puerto inválido`, veredicto detenido |
| Ruta vacía | `config_path = ""` | `Ruta inválida: está vacía`, veredicto detenido |

## Salida esperada

Ejecuta tu archivo y compara con este ejemplo (usa tus propios nombre e identificador; los demás valores deben coincidir):

```text
--- Resumen de la configuración ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Puerto local: 18080
Chequeo de puerto: Puerto válido: dentro del rango 1-65535
Ruta de configuración: configs/lab.conf
Chequeo de ruta: Ruta válida: archivo conocido del laboratorio
Nivel de registro: WARNING
Chequeo de nivel: Nivel válido: organiza la revisión humana
Nota del revisor: Sin nota del revisor: se continúa sin comentarios
Configuración lista: True
Requiere corrección: False
Decisión final: Configuración lista para la práctica local
```

Con tus propios datos el nombre y el identificador cambian, pero la forma del resumen es siempre la misma: un encabezado y doce líneas de datos legibles. Con `18080`, ruta conocida y `WARNING`, cada resultado parcial es `True` y el veredicto es configuración lista.

## Nota precisa sobre lo que el programa sí hace y lo que no hace

El resumen **organiza la evidencia para la revisión humana**: mensajes por campo (`Puerto válido`, `Ruta válida`, `Nivel válido`) y una decisión (`Configuración lista para la práctica local` o `Configuración detenida`). No abre puertos, no crea archivos, no toca el disco y no abre conexiones. `True` solo indica que se cumple la regla correspondiente del laboratorio.

## Nota precisa sobre errores con lógica compuesta

Errores que verás en esta sesión:

- `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`: escribiste `if target_port = 18080:` con un solo `=` (asignación) donde Python espera una comparación. La corrección es usar `==` para comparar o, en esta sesión, evaluar el booleano ya calculado (`if port_ok:`).
- Error silencioso con `or`: si escribes `level_ok = log_level == "INFO" or "WARNING"`, el programa dice que `DEBUG` es válido sin ningún mensaje de error. La causa es que `"WARNING"` por sí solo siempre es verdadero (texto no vacío), así que el `or` siempre resulta verdadero. La corrección es comparar cada vez: `log_level == "INFO" or log_level == "WARNING" or log_level == "ERROR"`.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`target_port`, `config_path`, `log_level`, `port_ok`, `level_ok`, `config_ready`, `needs_fix`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`). El ejemplo usa f-strings como forma cómoda de mostrar variables; su sintaxis no es un objetivo evaluado.

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué configuración observaste (`18080`, `configs/lab.conf`, `WARNING`, `None`) y qué significa cada valor.
- [ ] Por qué `and` exige que cada parte sea `True` y qué pasa con `0` y con `99999`.
- [ ] Por qué `or` se conforma con una sola coincidencia y qué pasa con `DEBUG`.
- [ ] Qué detecta `is None` y por qué no es lo mismo que comparar con `==`.
- [ ] Por qué `log_level == "INFO" or "WARNING"` siempre resulta verdadero y cómo se corrige.
- [ ] Cómo se combina el veredicto (`port_ok and path_ok and level_ok`), qué invierte `not` y qué NO hace el programa (no abre puertos, no crea archivos, no contacta nada).
- [ ] Cómo llega cada resultado al resumen (qué variable muestra cada línea).
- [ ] Tu resumen se ejecuta sin errores y muestra el encabezado más las doce líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, cambia `target_port` a `0` y luego a `80`, ejecuta de nuevo con `↑` y di en voz alta qué mensaje de puerto aparece en cada caso y por qué el veredicto cambia solo con `0`. Es solo práctica extra dentro de la clase con valores ya explicados: no cambia tu calificación y no usa sintaxis nueva. No lo confundas con la tarea posterior de abajo, que se hace fuera de clase con un archivo distinto.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia un poco más compleja para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal. Usa un archivo nuevo (`service_config_review.py`), distinto del `config_check.py` de clase y del desafío opcional de arriba.

**Historia:** actúas como el auxiliar responsable de dejar lista la configuración del servicio local de respaldo antes de su revisión nocturna, distinta de la configuración de práctica de clase. Otra persona del equipo te deja el aviso del servicio: debes registrar de quién es el trabajo (`student_name`, `student_id`), pedir por teclado el puerto local y el nivel y convertir el puerto (`raw_target_port = input("Puerto local: ")`, `target_port = int(raw_target_port)`, `log_level = input("Nivel de registro: ")`; reactiva la sesión 02 sin manejo de errores), y mantener la ruta fija del laboratorio (`config_path = "configs/lab.conf"`, `known_config_path = "configs/lab.conf"`, `reviewer_note = None`).

El problema es el mismo que en clase: cada campo puede dejar el servicio sin una revisión completa (puerto fuera de rango, ruta desconocida, nivel no permitido o nota sin registrar), y un mensaje genérico ocultaría qué debe corregirse. La consecuencia es operativa: quien revisa de noche necesita saber en un solo lugar si el servicio queda listo o detenido y qué campo debe corregirse, sin tener que adivinar. La decisión que produces es esa: servicio listo o detenido, con mensajes específicos por campo.

Cada dato conserva su significado causal: el puerto escrito por teclado (por ejemplo `8080`) alimenta el chequeo de rango tras `int()` y solo es válido dentro de `1-65535`; el texto del nivel (por ejemplo `INFO`) alimenta la cadena con `or` y basta una sola coincidencia para ser válido; la ruta fija solo es válida porque coincide con la ruta conocida (existencia simulada, sin tocar el disco); `None` significa que no llegó ninguna nota del revisor, distinto de una nota vacía. Límites: el programa solo valida estos datos sintéticos y recomienda; no abre puertos, no crea archivos, no conecta red ni confirma ataques. `True` solo indica que se cumple la regla correspondiente; el rango, la ruta conocida y los niveles son reglas didácticas, no estándares universales, y no prueban un ataque. El resumen le sirve a la persona responsable de revisar el caso para decidir si el servicio queda listo o detenido en un solo lugar. La tarea integra entrada → conversión → decisión → comunicación, mientras el ejercicio principal aísla decisión → comunicación.

### Mapeo dominio → código de la tarea (léelo antes de programar)

| Dato del caso | Variable | Pregunta / regla | Booleano y mensaje producido | Contribución al veredicto |
|---------------|----------|------------------|------------------------------|---------------------------|
| Puerto escrito por teclado (`8080`) | `raw_target_port` → `target_port` (tras `int()`) | ¿Está dentro del rango `1-65535`? (`target_port >= 1 and target_port <= 65535`) | `port_ok` + `port_message` | Parte de `config_ready`; si es `False`, el servicio se detiene |
| Ruta fija `configs/lab.conf` | `config_path` (contra `known_config_path`) | ¿Coincide con la ruta conocida? (`if/elif/else`) | `path_ok` + `path_message` | Parte de `config_ready`; si es `False`, el servicio se detiene |
| Nivel escrito por teclado (`INFO`) | `log_level` | ¿Coincide con alguna de las tres opciones? (`or`) | `level_ok` + `level_message` | Parte de `config_ready`; si es `False`, el servicio se detiene |
| Ausencia de nota (`None`) | `reviewer_note` | ¿No llegó ninguna nota? (`is None`) | `note_missing` + `note_message` | Informa a la revisión; no bloquea el veredicto |
| Veredicto combinado | `config_ready`, `needs_fix`, `final_decision` | ¿Cada resultado parcial es `True`? (`and`) | `config_ready`, `needs_fix`, `final_decision` | Decisión final para quien revisa |

Primero abstrae con la historia y el mapeo; después codifica. Compruebas el rango con `and` (`target_port >= 1 and target_port <= 65535`), la ruta con `if/elif/else` y el nivel con `or` (`== "INFO" or == "WARNING" or == "ERROR"`), y combinas cada resultado parcial con `and` (`config_ready = port_ok and path_ok and level_ok`, `needs_fix = not config_ready`). La comparación encadenada equivalente `1 <= target_port <= 65535` es válida, idiomática y compacta en Python y expresa matemáticamente que el valor está entre ambos límites; se enseñará como alternativa una vez comprendidas las dos comparaciones. No es la forma principal de este ejercicio porque oculta el `and` que la sesión pretende practicar. Compromiso: legibilidad matemática y menor repetición frente a visibilidad explícita del operador lógico.

Crea manualmente `service_config_review.py` en tu proyecto personal, con código lineal y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables y fórmula |
|------|----------|---------------------|
| 1. Evidencia | Pide la configuración por teclado y convierte el puerto (reactiva la sesión 02), más tu identidad y la ruta fija | `raw_target_port = input("Puerto local: ")`, `target_port = int(raw_target_port)`, `log_level = input("Nivel de registro: ")`, `config_path`, `known_config_path`, `reviewer_note = None`, `student_name`, `student_id` |
| 2. Chequeos parciales | Comprueba el rango con `and`, la ruta fija con `if/elif/else`, el nivel con `or` y la ausencia con `is None` | `port_ok`, `port_message`, `path_ok`, `path_message`, `level_ok`, `level_message`, `note_missing`, `note_message` |
| 3. Veredicto | Combina cada resultado parcial con `and`, niega con `not` y decide la recomendación con `if/else` | `config_ready = port_ok and path_ok and level_ok`, `needs_fix = not config_ready`, `final_decision` |
| 4. Comunicación | Resumen legible para quien revisa el caso | `print()` línea por línea |

Ejemplo único (úsalo para comprobar; usa tus propios nombre e identificador):

```text
--- Resumen del servicio ---
Nombre: Alex Mendez
Identificador: DEF-2026-09
Puerto local: 8080
Chequeo de puerto: Puerto válido: dentro del rango 1-65535
Ruta de configuración: configs/lab.conf
Chequeo de ruta: Ruta válida: archivo conocido del laboratorio
Nivel de registro: INFO
Chequeo de nivel: Nivel válido: organiza la revisión humana
Nota del revisor: Sin nota del revisor: se continúa sin comentarios
Configuración lista: True
Requiere corrección: False
Decisión final: Configuración lista para la práctica local
```

Con tus propios datos el nombre y el identificador cambian, pero la forma del resumen es siempre la misma: un encabezado y doce líneas de datos legibles. Con `8080` y `INFO`, cada resultado parcial es `True` y el veredicto es configuración lista.

### Punto de partida: la entrada por teclado (escríbela tal cual)

```python
raw_target_port = input("Puerto local: ")
target_port = int(raw_target_port)
log_level = input("Nivel de registro: ")
```

Escribe ambas peticiones exactas con esos prompts y esa conversión: el programa debe pedir y convertir antes de decidir. Para comprobar, escribe `8080` e `INFO`; el resumen debe coincidir con el ejemplo único de abajo. Ten en cuenta que `input()` devuelve texto: si pulsas Enter sin escribir nada, obtienes `""`, no `None`. Por eso el nivel usa igualdad de cadenas (`==` con `or`, y su contraparte `!=` para la desigualdad), mientras la ausencia de nota usa identidad con `None` (`is None` para la ausencia y `is not None` para la presencia). Si se escribe texto no numérico para el puerto, el programa se interrumpe con `ValueError`: es el comportamiento esperado y no se captura con `try/except` en esta sesión. Sin validación, reintentos, bucles, funciones, `try/except`, `imports`, colecciones ni conceptos futuros. No necesitas abrir el repositorio ni consultar la solución para completar la tarea.

**Antes de programar, analiza:** qué valor de teclado alimenta el chequeo de rango tras `int()` y qué dos comparaciones deben cumplirse para `port_ok`; qué texto alimenta la cadena con `or` y por qué basta una sola coincidencia para `level_ok`; qué veredicto corre con `8080` más `INFO` y qué le pide a un humano hacer (y qué no hace por sí solo).

**Propósito real:** el resumen organiza la evidencia local para la revisión humana. No abre puertos, no crea archivos, no confirma un incidente y no sustituye la investigación.

**Entrega:** explica en voz alta la cadena campo → chequeo booleano → mensaje específico → veredicto combinado → recomendación para cada campo, por qué `and` exige cada parte mientras `or` se conforma con una, y cómo llega cada resultado al resumen. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos sintéticos escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
