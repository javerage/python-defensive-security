# Crea una skill local para generar logs sintéticos de auditoría informática

Vas a crear una skill **local** de Pi que genera entradas sintéticas de un log de eventos de auditoría informática para practicar en clase. Al terminar, entenderás la diferencia entre una **skill** (un procedimiento reutilizable con perfil propio) y una **plantilla de prompt** (una instrucción repetitiva), y tendrás un generador que responde a una frase natural en español.

- **Tiempo estimado:** 20–25 minutos.
- **Actividad independiente:** esta guía **no** forma parte de la evaluación de la Sesión 09 ni la modifica. No tienes que cambiar nada de la S09 ni de sus archivos para completarla.
- **Lo que obtienes:** una skill local llamada `faker-data-custom` que, ante un pedido natural, devuelve N entradas sintéticas en formato `LEVEL | message`.

## Ruta rápida

1. Abre la raíz de tu proyecto y verifica dónde estás.
2. Crea solo la carpeta `.pi/skills/faker-data-custom/`.
3. Crea el archivo `SKILL.md` copiando el contrato de esta guía.
4. Abre Pi en la raíz, ejecuta `/reload` y prueba con una frase natural.

## Concepto: qué es una skill y en qué se diferencia de una plantilla

Una skill reúne **instrucciones especializadas reutilizables**: en este ejemplo define un dominio, etiquetas, formato y criterios de verificación. Pi puede cargarla cuando la petición coincide con su descripción; no se garantiza que el modelo la seleccione ni que cumpla siempre sus reglas. Un prompt-template también puede contener reglas y formatos, pero se expande al invocar su comando con argumentos. La diferencia es la organización y forma de carga, no que uno permita reglas y el otro no.

| Aspecto | Skill | Plantilla de prompt |
|---|---|---|
| Propósito | Instrucciones especializadas y recursos opcionales | Instrucción reutilizable con argumentos |
| Archivos | Carpeta propia con `SKILL.md` | Archivo Markdown en la carpeta de prompts |
| Ruta local (Pi) | `.pi/skills/<nombre>/SKILL.md` en la raíz del proyecto | `.pi/prompts/<nombre>.md` (comando manual) |
| Invocación | Automática cuando el pedido coincide, o explícita con `/skill:<nombre>` | Solo manual con `/<nombre>` |
| Cuándo conviene | Procedimiento de dominio, referencias o criterios reutilizables | Petición repetitiva que cabe en una plantilla, incluso con reglas |
| Descubrimiento automático | Sí, por `name` + `description` (no garantizado; existe alternativa explícita) | No; siempre la invocas tú |
| Distribución | Se comparte con el proyecto (carpeta local) o contigo (global) | Igual, pero sin activación automática |
| Recursos adicionales | No requeridos para esta guía | No requeridos |
| Límites | Las reglas son instrucciones al modelo, no un sandbox | Las reglas son instrucciones al modelo, no un sandbox |

**Cuándo usar una skill:** cuando hay reglas del dominio (etiquetas permitidas, formato exacto, contenido permitido y prohibido) y quieres verificación antes de entregar. **Cuándo basta una plantilla:** cuando la instrucción es simple y repetitiva. Extender esta skill a otros dominios no es necesario para esta guía.

## Dónde vive cada cosa (local primero)

Trabaja siempre en **local**. La ubicación global existe, pero **no la toques** en esta actividad.

| Ámbito | Ruta exacta | Cuándo usarla |
|---|---|---|
| Local (recomendada) | `<raíz-del-proyecto>/.pi/skills/faker-data-custom/SKILL.md` | Esta guía. Vale solo para el proyecto abierto. |
| Global (opcional, no usar aquí) | `~/.pi/agent/skills/<nombre>/SKILL.md` | Solo si quieres la skill en todos tus proyectos. |
| Descubrimiento alternativo | `.agents/skills/<nombre>/SKILL.md` (por ancestría) | Pi también la descubre; no la necesitas aquí. |

En esta guía el proyecto se muestra como `tu-proyecto/` (un marcador genérico: usa tu propia carpeta, no crees una con ese nombre).

No confundas estas carpetas:

| Ruta | Contenido |
|---|---|
| `.pi/skills/` | Skills (activación automática o `/skill:<nombre>`). Es donde trabaja esta guía. |
| `.pi/prompts/` | Comandos manuales (`/<nombre>`). **No** pongas aquí la skill. |
| `prds/` | Documentos de funcionalidades del curso. Nada que ver con Pi. |
| `.venv/` | Entorno virtual de Python. Nada que ver con Pi. |

Reglas de nombre de archivo y carpeta:

- El archivo debe llamarse exactamente `SKILL.md`, en mayúsculas y con extensión `.md` (nunca `.txt`).
- La carpeta usa minúsculas con guiones (kebab-case): `faker-data-custom`.
- La carpeta y el campo `name` del frontmatter deben coincidir para que la skill sea portable.

## Paso 1 — Ubícate en la raíz de tu proyecto

Abre una terminal en la raíz del proyecto que tú elijas (tu propia ruta, la que ya usas en clase) y confirma dónde estás:

```bash
pwd
ls
```

En PowerShell:

```powershell
Get-Location
Get-ChildItem
```

Debes ver la raíz de tu proyecto (sus archivos y carpetas habituales). Todo lo que sigue se ejecuta desde ahí.

## Paso 2 — Crea solo la carpeta nueva

Primero verifica si la skill ya existe. Si el archivo `SKILL.md` ya está, **detente y no lo sobrescribas**: revísalo con el Paso 4 en lugar de reemplazarlo.

En macOS o Linux:

```bash
ls .pi/skills/faker-data-custom/SKILL.md
mkdir -p .pi/skills/faker-data-custom
```

En Windows (PowerShell):

```powershell
Test-Path .pi/skills/faker-data-custom/SKILL.md
New-Item -ItemType Directory -Force .pi/skills/faker-data-custom
```

Crea **solo** directorios nuevos. No borres ni modifiques nada existente.

## Paso 3 — Crea el contrato de la skill

Crea manualmente el archivo `.pi/skills/faker-data-custom/SKILL.md` con tu editor, guárdalo en UTF-8 y copia el bloque completo siguiente. Mantén las instrucciones concisas; Pi no exige un número de palabras.

Sobre el frontmatter (la parte entre `---`): los campos usan los nombres que reconoce Pi. En esta guía escribimos `description` en **una sola línea entre comillas** para facilitar la copia y mantener YAML válido; no es la única sintaxis YAML posible. Incluye el disparador en español (`eventos sintéticos`) junto con los términos en inglés del dominio. Para este ejemplo basta con `name` y `description`; campos como `license` y `metadata` son opcionales y se omiten.

La skill no usa scripts, ni TypeScript, ni integración con Faker: se activa con un pedido en lenguaje natural y devuelve datos de ejemplo.

Copia desde aquí:

````markdown
---
name: faker-data-custom
description: "Trigger: eventos sintéticos, synthetic audit log events, synthetic log entries. Generate synthetic IT audit log entries in TEXT format for classroom practice."
---

# Faker Data Custom — Synthetic Audit Log

Generate N synthetic IT audit log entries as pure classroom data. Default N is 20 when the request states no number.

## Default output format

Unless the user explicitly requests another format, output plain TEXT, one entry per line, with this exact shape:

LEVEL | message

Do not output a Python list or code by default. Another format is allowed only when the user explicitly requests it. Output pure data in the conversation only. Never present data as a Python processing solution.

## Audit profile (fixed)

Use only these labels. They are synthetic educational labels, not a universal severity standard and not verified findings:

- INFO: normal confirmation of a simulated routine action.
- WARNING: reviewable discrepancy in a simulated routine action.
- ERROR: the simulated task could not complete. It is not a verified vulnerability or an actual audited finding.

Accept only INFO, WARNING, and ERROR.

## Allowed content

Write each message in Spanish. Describe only inert simulated actions such as a permissions check on a test directory, an integrity check producing a synthetic record, or a mock configuration review. Never include real secrets, real personal data, real URLs, real IPs, network actions, or malware actions.

Vary the entries. Repeated levels are allowed. Do not force random uniqueness, uniform distribution of levels, deterministic randomness, seeds, or any fixed external count table.

## Limits

Ask a clarifying question only when the request is materially unclear or contains a meaningful contradiction. Never perform a real audit, read the filesystem, execute code, or use the network. Never create files and never write outside the conversation without explicit authorization. Before delivering, self-check quantity, allowed labels, the `|` separator, Spanish message text, and audit context. If the request is outside this audit domain, decline briefly and explain this skill covers only synthetic audit logs; quantity, format, and context may vary within the audit domain. For very large N, propose delivering in batches instead of generating an unbounded output.
````

Hasta aquí la copia. Verifica que el archivo guardado empiece con `---`, que `name` sea `faker-data-custom` (minúsculas, 17 caracteres, dentro del máximo de 64) y que `description` sea una sola línea entre comillas (dentro del máximo de 1024).

## Ejemplo de salida (ilustrativo, no es una ejecución real)

Así se ven 3 entradas de ejemplo con el formato de la skill. Es solo una ilustración del formato, **no** son 20 entradas generadas ni el resultado de haber ejecutado nada:

```text
INFO | Revisión de permisos completada en el directorio de prueba.
WARNING | Registro de integridad sintético con discrepancia pendiente de revisión.
ERROR | No se pudo completar la revisión simulada de configuración.
```

Observa: cada línea usa una etiqueta permitida, el separador exacto ` | ` y el mensaje en español. En tu prueba real pedirás 20 y contarás las líneas fuera de cualquier comentario.

## Paso 4 — Confía, recarga y prueba en Pi

1. **Lee y revisa** el contenido de tu `SKILL.md` antes de confiar en el proyecto.
2. Abre Pi **en la raíz de tu proyecto** y confía en el proyecto cuando Pi lo pida (esto permite cargar recursos protegidos como tu skill local).
3. Ejecuta `/reload` para que Pi lea la skill nueva o editada.
4. Revisa el diagnóstico de inicio y la disponibilidad de comandos. Si tu skill no aparece en ningún menú de skills, no significa que esté rota: ese menú no está garantizado (y menos si los comandos de skills están desactivados). La prueba real es el pedido en lenguaje natural.
5. Prueba principal, con esta frase exacta:

   ```text
   Genera 20 entradas sintéticas de un log de eventos de auditoría informática.
   ```

6. Verifica el resultado: si la interfaz de Pi muestra que leyó tu `SKILL.md`, úsalo como evidencia; si no lo muestra, usa la alternativa explícita sin asumir activación automática:

   ```text
   /skill:faker-data-custom Genera 20 entradas sintéticas de un log de eventos de auditoría informática.
   ```

7. Haz estas comprobaciones sin resolver ningún ejercicio:
   - Pide 5 y luego 20; cuenta las líneas manualmente y confirma etiquetas, separador y mensajes sintéticos en español, sin código ni archivos.
   - Prueba un pedido no relacionado (por ejemplo, pedir un resumen de otro tema) y confirma que la skill **no** se activa.
   - No afirmes que probaste nada que no ejecutaste realmente.

No desactives la invocación por el modelo (una opción como `disable-model-invocation` en `true` impediría el descubrimiento automático; déjala en su valor por defecto).

## Alternativa sin Pi (misma exigencia)

Si no tienes Pi a mano, no necesitas cuentas ni instalaciones externas. Lee el contrato del Paso 3 y escribe a mano 3 entradas que cumplan los mismos criterios: cantidad exacta, solo etiquetas `INFO`, `WARNING`, `ERROR`, separador ` | `, mensajes sintéticos en español e inertes, sin código, sin archivos y sin datos reales. Luego autoevalúalas con la lista de verificación siguiente.

## Solución de problemas

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| Pi no encuentra la skill | La guardaste en `.pi/agent/skills/` dentro del proyecto (esa ruta es global, con `~`) | Muévela a `.pi/skills/faker-data-custom/SKILL.md` en la raíz |
| El comando `/faker-data-custom` no existe | Confundiste `.pi/prompts` (comandos) con `.pi/skills` (skills) | Las skills se invocan con frase natural o `/skill:faker-data-custom`, no con `/<nombre>` |
| Pi ignora el archivo | Se llama `skill.md` o `SKILL.txt` | Renómbralo a `SKILL.md` exacto, en mayúsculas y con `.md` |
| Error al cargar | Frontmatter YAML mal formado o falta de `description` | Compara con el bloque copiable; usa su descripción entrecomillada para evitar errores |
| Cambios que no aparecen | Falta confiar el proyecto o ejecutar `/reload` | Confía el proyecto, guarda el archivo y ejecuta `/reload` |
| Dos skills con el mismo nombre | Colisión: la primera encontrada gana, sin reemplazo silencioso | Renombra tu carpeta y tu `name` para que coincidan y sean únicos |
| Resultados distintos cada vez | El modelo no es determinista; la carga de la skill tampoco | Es normal: verifica formato y reglas, no igualdad byte a byte |
| "Aleatoriedad con semilla" que no se repite | La aleatoriedad determinista con semilla no está garantizada | No pidas ni prometas semillas; pide entradas variadas y verifícalas a mano |

## Lista de verificación y firma del docente

Marca cada punto cuando lo hayas comprobado. Esta lista verifica que seguiste la guía; **no** es la evaluación de la S09.

- [ ] La skill está en `.pi/skills/faker-data-custom/SKILL.md` (ruta local, archivo `SKILL.md` exacto).
- [ ] El frontmatter tiene `name` y una `description` entrecomillada en una sola línea; carpeta y `name` coinciden.
- [ ] El perfil de auditoría usa solo `INFO`, `WARNING` y `ERROR` con su significado sintético y educativo.
- [ ] El pedido de 20 entradas devuelve 20 líneas con el formato `LEVEL | message`, mensajes sintéticos en español, sin código ni archivos.
- [ ] Hay evidencia de que seguiste las instrucciones (captura o nota de `/reload`, del pedido y del conteo manual).

**Firma del docente:** ______________________________ **Fecha:** ______________

## Anexo — Prepara feature_009.md y úsalo con /nuevo-py

Esta es una demostración separada de preparación: con `/nuevo-py` se genera SOLO el encabezado y los TODOs en inglés. No cambia la S09, no resuelve su ejercicio y no autoriza por sí sola el uso evaluado; ese uso lo autoriza el docente según la política vigente. Para esta demo no leas, escribas ni modifiques archivos reales de la S09 ni su material original.

Son dos actividades distintas. La skill de esta guía produce líneas de conversación con forma `LEVEL | message` para practicar la lectura de datos sintéticos. El PRD de la S09 usa una lista Python con etiquetas desnudas `INFO`, `WARNING` y `ERROR`. No hay compatibilidad directa: una comparación del tipo `event == ERROR` sobre la línea completa con mensaje no aplica. No sustituyas la fixture canónica por líneas generadas, no cambies sus valores y no añadas partición de texto como concepto nuevo.

Pasos desde la raíz del proyecto (tu propia carpeta; aquí se muestra la forma, no una ruta fija):

1. Inspecciona primero y crea la carpeta `prds` solo si falta. En macOS o Linux:

   ```bash
   ls
   # Si no ves prds, créala con:
   mkdir -p prds
   ```

   En Windows (PowerShell):

   ```powershell
   Test-Path prds
   # Si dice False, créala con:
   New-Item -ItemType Directory -Force -Path prds
   ```

2. Crea el archivo a mano con tu editor copiando el bloque canónico completo de abajo en `prds/feature_009.md`. Si el archivo ya existe, detente y avisa al docente; no lo sobrescribas. El repositorio trae respaldo en `src/modulo_01/sesion_09/prds/feature_009.md`; el archivo de trabajo es el tuyo.
3. `/reload` solo si el comando o prompt es nuevo o cambió. Tras crear o editar solo el PRD no hace falta recargar para leerlo, pues se lee en la invocación.
4. Lanza Pi desde la raíz y, solo si el destino no existe y el docente lo autoriza, ejecuta:

   ```text
   /nuevo-py event_loop.py 09 prds/feature_009.md
   ```

5. Inspecciona el resultado: encabezado completo con COURSE/REPOSITORY/SESSION/FILE/PURPOSE/SCOPE y después solo comentarios TODO en inglés, sin lógica ni conteos resueltos. Confirma que no se sobrescribió nada existente. El comando está protegido: si el destino ya existe, se detiene sin escribir. Si `event_loop.py` ya existe, detente ahí. Solo como variante opcional separada, para no tocar la práctica real, habría que copiar el PRD a una demo aparte y ajustar su Archivo Python al destino demo; no muta lo canónico. Se deja una sola llamada principal para no confundir.

Por qué conviene unir ambas piezas: la skill entrena la lectura de datos sintéticos independientes; el PRD deja fijo el requisito exacto e inmutable de la S09 y el comando solo lo documenta como encabezado y TODOs. No alimentes el comando con líneas emitidas por la skill para afirmar resultados originales. Un PRD guiado por un log generado sería una variante nueva, no la pedida aquí. Detalle en la guía del comando: [Crea tu comando /nuevo-py](nuevo-py.html).

Copia canónica para `prds/feature_009.md` (pega tal cual):

````markdown
# Feature: doble conteo del registro local con for y while

## Identificación
- Feature: doble conteo del registro local con for y while.
- Sesión: 09.
- Archivo Python: `event_loop.py`.
- Archivo PRD: `prds/feature_009.md` (`###` es el número de sesión a 3 dígitos: S09 → `feature_009.md`).

## Objetivo
Recorrer la lista local de eventos con un ciclo `for` de un solo nivel para contar entradas `ERROR`.
Repetir el mismo recorrido con un ciclo `while` con inicio, condición y avance en cada vuelta.
Comparar ambos conteos y dejar un resumen verificado para revisión humana posterior.

## Contexto
- Rol: persona analista que verifica el registro local antes de entregarlo al revisor siguiente.
- Evidencia: lista sintética local de eventos transcrita en clase, trabajada en memoria en la máquina propia; en esta sesión no se usa la red.
- Problema: un solo recorrido puede ocultar un fallo de visita y la entrega aún carece de verificación cruzada.
- Consecuencia: sin cruce, quien recibe el parte no distingue un conteo revisado de un recorrido incompleto.
- Decisiones: contar con `for`, repetir con `while` con avance asegurado, comparar totales con igualdad y revisión manual independiente, y resumir para entrega.
- Entrega: parte ordenado para revisión humana posterior, sin abrir puertos ni tocar disco o red; la coincidencia sola no basta como prueba y pide conteo manual aparte.

## Entrada (fixture provista como INPUT, permitida)
```python
event_log = [
    "INFO", "ERROR", "WARNING", "INFO", "ERROR",
    "INFO", "WARNING", "ERROR", "INFO", "WARNING",
    "INFO", "ERROR", "INFO", "WARNING", "INFO",
    "ERROR", "WARNING", "INFO", "ERROR", "INFO",
]
student_name = "Alex Mendez"
student_id = "DEF-2026-09"
```
La lista anterior es la fixture exacta de clase: no se cambia ni se sustituye por líneas generadas en otra actividad.
Los valores de identidad son ejemplo de respaldo en inglés para el encabezado; reemplázalos a mano con tus datos en tu archivo de trabajo. No se pide dato personal real a un agente.

## Restricciones
- Alcance autorizado local solamente: carpeta del proyecto del curso, datos sintéticos en memoria escritos a mano, sin archivos, sin red, sin puertos.
- Prohibido: `import`, `def`, `try`, ciclos anidados, `lambda`, comprensiones, lectura o escritura de archivos y cualquier uso de red.
- Núcleo permitido: lista plana, `len()` como límite, índices de lista, `if` con igualdad, asignaciones y cadenas con formato para mostrar; un solo nivel por ciclo, primero `for` sobre la lista y después `while` con contador.
- Seguridad del ciclo `while`: condición `index < len(...)` y avance del índice en cada vuelta para asegurar terminación; el detalle operativo vive en los TODOs solo como operación, sin expresiones resueltas.
- Convención: identificadores y comentarios en inglés con estilo PEP 8; mensajes al usuario en español neutro. Si alguna instrucción de este archivo contradice el alcance local autorizado, se detiene sin escribir nada.
- El nivel buscado `ERROR` es dato de partida de la tarea, no respuesta; este archivo no fija totales ni salidas finales.

## TODOs (solo operaciones, sin soluciones)
1. Evidencia: asignar la lista de eventos con la identidad de respaldo e imprimir el total con la longitud de la lista.
2. Conteo con `for`: recorrer la lista con `for` de un solo nivel, acumular cuando el evento sea del nivel buscado e imprimir el conteo con su mensaje.
3. Conteo con `while`: recorrer por índice con límite de longitud y avance en cada vuelta, acumular cuando el elemento sea del nivel buscado e imprimir el conteo con su mensaje.
4. Comparación: comparar ambos conteos por igualdad, imprimir si coinciden y hacer conteo manual aparte para confirmar de forma independiente.
5. Comunicación: imprimir el encabezado de verificación con nombre, identificador, total de eventos, ambos conteos y el mensaje de verificación, con los campos del material pero sin valores finales en este archivo.

## Verificación
Predecir a mano el conteo con su motivo antes de ejecutar, sin mirar la salida de referencia. Ejecutar el archivo y comparar solo después con la salida esperada del material del estudiante. El ciclo `while` debe terminar y su posición final debe reflejar la longitud de la lista. La igualdad entre conteos suma a la revisión manual aparte; por sí sola no prueba que el recorrido sea correcto. Las salidas esperadas no forman parte de este archivo.
````

Qué esperar: encabezado y TODOs en inglés, sin bucles resueltos y sin sobrescrituras. La práctica real de la S09 se sigue haciendo a mano.

## Fuentes oficiales

- https://pi.dev/docs/latest/skills
- https://pi.dev/docs/latest/configuration
- https://pi.dev/docs/latest/security

Consulta esas páginas si quieres confirmar cómo Pi descubre, confía y recarga las skills locales.

[Volver al portal del curso](../index.html)
