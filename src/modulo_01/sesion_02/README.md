# Sesión 02: Tipos de datos, entrada y conversiones

Bienvenido a la **Sesión 02** del currículo *Python for Defensive Security: Fundamentals and Local Lab Tooling* (`PyDefSec`).

Al terminar la sesión podrás **revisar la experiencia práctica de un operador, convertir su entrada de texto a números, estimar sus horas totales de práctica, verificar si alcanzó el requisito y mostrar un resumen simple en consola**.

## Ruta rápida

1. Abre tu proyecto de la sesión 01 (`curso-python-defensivo`) y activa `.venv`.
2. Verifica el intérprete (`python --version` debe responder Python 3.13.x).
3. Crea manualmente el archivo `operator_profile.py` y escribe el ejercicio.
4. Ejecuta `python operator_profile.py` y comprueba el resumen con el ejemplo de abajo.

> El repositorio es solamente respaldo. No necesitas clonarlo ni navegar su estructura para completar la sesión.

## Duración (60 minutos)

10 min reencuentro con tu proyecto y verificación · 15 min secuencia y demo · 25 min práctica con `operator_profile.py` · 10 min verificación de comprensión y cierre.

## Historia del ejercicio

Formas parte del equipo que coordina el entrenamiento de nuevos operadores de seguridad. Antes de permitir que un operador participe en una simulación de incidentes, debes revisar su experiencia práctica. Para ello registras su nombre, cuántos laboratorios introductorios completó y el promedio de horas que dedicó a cada uno. Al multiplicar los laboratorios completados por el promedio de horas, obtienes una estimación de sus horas totales de práctica. El programa de entrenamiento establece un mínimo de 10 horas antes de avanzar a la siguiente simulación. Finalmente, muestras un resumen que permite identificar al operador, revisar su progreso y saber si alcanzó ese requisito.

## Secuencia conceptual

Cada línea del programa sigue este orden explícito:

1. **Entrada de texto:** `input()` siempre devuelve texto (`str`), incluso si escribes dígitos.
2. **Conversión:** `int()` y `float()` transforman ese texto en números cuando el texto ya es numérico.
3. **Cálculo:** el operador `*` combina los números en la métrica total.
4. **Decisión:** la comparación `>=` produce un valor booleano (`True` o `False`).
5. **Comunicación:** `print()` lleva cada resultado al resumen: un encabezado más cinco líneas de datos.

## Cómo nace una variable en Python (en clase, sin evaluar)

En Python asignas un valor **sin declarar antes el tipo**:

```python
failed_attempts = 5
```

El **nombre** referencia un valor y el **valor** tiene el tipo. Puedes mirarlo con `type()` (una linterna para observar, no un tema evaluado):

```python
print(type(failed_attempts))  # <class 'int'>
```

| Lenguaje | Cómo se escribe | Qué significa |
|----------|-----------------|---------------|
| Python | `failed_attempts = 5` | Asignas sin declarar el tipo. |
| C / Java | `int failed_attempts = 5;` | Declaras el tipo antes de asignar. |
| JavaScript | `let failed_attempts = 5;` | `let` declara el enlace, pero no escribe el tipo del valor. |

Tres precisiones y nada más:

- Python es **dinámico pero fuerte**: no declaras tipos, pero tampoco mezcla automáticamente texto y números en operaciones incompatibles (por eso existe el `TypeError` de arriba).
- Python 3 usa un **solo `int` de precisión arbitraria**: no hay `byte`, `short`, `int` y `long` de distinto rango como en otros lenguajes (esos nombres, y `TINYINT` o `SMALLINT`, los verás en bases de datos). No es memoria infinita: el límite práctico es la memoria disponible.
- En esta sesión trabajamos `str`, `int`, `float` y `bool`. Python posee otros tipos incorporados y colecciones que se estudiarán después; estos cuatro no son los únicos.

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
notepad operator_profile.py

# 5. Ejecuta tu ejercicio
python operator_profile.py
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
touch operator_profile.py

# 5. Ejecuta tu ejercicio
python3 operator_profile.py
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

Crea `operator_profile.py` con código lineal (sin funciones, sin `try/except`, sin colecciones) que haga lo siguiente:

| Paso | Qué hace | Variables |
|------|----------|-----------|
| 1. Entrada | Pide nombre, laboratorios introductorios y promedio de horas con `input()` (de quién es el progreso y sus prácticas terminadas) | `operator_name`, `raw_completed_labs`, `raw_hours_per_lab` |
| 2. Conversión | Convierte el texto a número | `completed_labs = int(...)`, `hours_per_lab = float(...)` |
| 3. Cálculo | Estima la práctica acumulada al multiplicar | `total_practice_hours = completed_labs * hours_per_lab` |
| 4. Decisión | Verifica la regla explícita del programa (mínimo 10.0 horas) | `ready_for_next = total_practice_hours >= 10.0` |
| 5. Comunicación | Imprime el encabezado y las cinco líneas de datos con `print()` (evidencia legible para revisar si alcanzó el requisito) | Encabezado más cinco líneas de datos legibles |

La solución de referencia está en `solution.py` y la plantilla guiada en `starter.py`.

## Entrada de ejemplo y salida esperada

Entrada (escribe estos valores cuando el programa los pida):

```text
Escribe el nombre del operador: Alex Rivera
Escribe cuantos laboratorios completo: 4
Escribe el promedio de horas por laboratorio: 2.5
```

Salida esperada:

```text
--- Resumen del operador ---
Nombre: Alex Rivera
Laboratorios completados: 4
Horas por laboratorio: 2.5
Horas totales de practica: 10.0
Listo para la siguiente practica: True
```

Los números cambian con tus datos, pero la forma del resumen es siempre la misma: un encabezado y cinco líneas de datos legibles.

## Nota precisa sobre errores de conversión

`int()` y `float()` **no validan ni corrigen**: solo transforman un texto que ya es numérico. Si escribes algo que no es un número (por ejemplo `cuatro`, `2,5` con coma o dejas la entrada vacía), el programa se interrumpe con `ValueError`. Eso es normal y esperado. Aprender a controlar ese caso con `try/except` queda para una sesión posterior; hoy basta con ingresar números y leer el mensaje de error.

Errores que verás en esta sesión:

- `TypeError: can't multiply sequence by non-int of type 'float'`: intentaste multiplicar el texto de `input()` por un decimal sin convertirlo antes (por ejemplo `raw_completed_labs * hours_per_lab`).
- `ValueError: invalid literal for int() with base 10`: el texto no era un número válido.

## Convención de nombres en inglés (orientación, no se califica)

El código (variables y comentarios) se escribe en inglés (`operator_name`, `completed_labs`, `total_practice_hours`) por **consistencia y colaboración**: los equipos internacionales comparten herramientas, ejemplos y revisiones en inglés, y así cualquiera puede leer tu código. Los mensajes para el usuario se escriben en español porque los lee una persona local. Todo el programa sigue PEP 8 (`snake_case`). El ejemplo usa f-strings como forma cómoda de mostrar variables; su sintaxis no es un objetivo evaluado.

## Lista de verificación (comprensión)

Antes de pedir la firma del docente, comprueba que puedes explicar en voz alta:

- [ ] Qué devuelve `input()` y por qué siempre es texto.
- [ ] Por qué conviertes con `int()` y `float()` antes de calcular.
- [ ] Qué hace el operador `*` en tu cálculo.
- [ ] Qué produce la comparación `>=` y qué significa `True` o `False`: si alcanzó el requisito definido de 10 horas (el programa presenta la evidencia, no autoriza por sí solo).
- [ ] Cómo llega cada resultado al resumen (qué variable muestra cada línea).
- [ ] Tu resumen se ejecuta sin errores y muestra el encabezado más las cinco líneas de datos.

## Desafío opcional (sin impacto en la evaluación)

Si terminas antes, decora tu resumen con líneas separadoras o un título con marcos ASCII. Es solo presentación: no cambia tu calificación.

## Tarea posterior a la clase (fuera de los 60 minutos)

Esta tarea es una transferencia un poco más compleja para hacer fuera de clase. No forma parte del cronograma ni expande el ejercicio principal.

**Historia:** actúas como el analista responsable de organizar observaciones iniciales para una revisión humana. El punto de partida es una alerta local de práctica sobre intentos fallidos de acceso. Para preparar el resumen registras el identificador de la cuenta del caso (`account_id`), cuantos eventos ocurrieron (`failed_attempts`) y la ventana temporal observada (`observation_minutes`). Calcular la frecuencia importa porque 12 intentos en 3 minutos no representan el mismo ritmo que 12 intentos durante una ventana mucho mayor. Dos reglas didácticas independientes —`>= 5` para practicar conteo y `>= 2.0` para practicar división y comparación— generan dos señales: volumen (`many_failed_attempts`) y ritmo (`rapid_attempts`). `True` solo indica que se cumple la regla correspondiente; no son estándares universales ni prueban un ataque. El resumen le sirve a la persona responsable de revisar el caso para decidir si necesita recopilar más información o continuar una investigación humana.

Crea manualmente `access_analysis.py` en tu proyecto personal, con código lineal y nombres técnicos en inglés (mensajes en español):

| Paso | Qué hace | Variables y fórmula |
|------|----------|---------------------|
| 1. Entrada | Pide cuenta del caso, eventos y ventana temporal con `input()` | `account_id`, `raw_failed_attempts`, `raw_observation_minutes` |
| 2. Conversión | Convierte el texto a número | `failed_attempts = int(...)`, `observation_minutes = float(...)` |
| 3. Cálculo | Divide para obtener el ritmo (frecuencia) | `attempts_per_minute = failed_attempts / observation_minutes` |
| 4. Decisiones | Dos reglas didácticas con operadores ya explicados (volumen y ritmo) | `many_failed_attempts = failed_attempts >= 5`, `rapid_attempts = attempts_per_minute >= 2.0` |
| 5. Comunicación | Resumen legible para quien revisa el caso | `print()` línea por línea |

Ejemplo único (úsalo para comprobar): cuenta `admin-local`, `12` intentos, `3` minutos.

```text
Escribe el identificador de la cuenta: admin-local
Escribe la cantidad de intentos fallidos: 12
Escribe los minutos observados: 3
--- Resumen de triage ---
Cuenta: admin-local
Intentos fallidos: 12
Minutos observados: 3.0
Intentos por minuto: 4.0
Muchos intentos fallidos: True
Intentos rapidos: True
```

**Propósito real:** el reporte organiza observaciones iniciales para la revisión humana. No confirma un ataque, no bloquea cuentas y no sustituye la investigación.

**Datos de prueba:** usa minutos mayores que cero (como el `3` del ejemplo). Si `observation_minutes` vale `0` o `0.0`, la división produce `ZeroDivisionError`. Controlar ese error y otras entradas inválidas queda para la sesión de manejo de errores posterior.

**Entrega:** explica en voz alta por qué conviertes cada entrada, qué hace la división `/` y qué produce cada comparación `>=`. El repositorio contiene `homework_starter.py` (plantilla) y `homework_solution.py` (referencia) solo como respaldo: úsalos como contingencia o guía **después** de intentar la tarea por tu cuenta.

## Declaración de alcance

Todo el código de esta sesión opera con datos locales escritos por ti en tu propia máquina. No hay conexiones de red ni destinos externos.
