# Plantilla de constitución del proyecto

Usa esta estructura para preparar `CONSTITUTION.md` en la carpeta de contexto que acuerdes, relativa a la raíz de tu proyecto abierto. Puedes completarla manualmente o pedir a un asistente de IA que te guíe con una entrevista, sección por sección, antes de proponer un borrador. La constitución registra los principios, las responsabilidades humanas y del asistente, las autorizaciones y las reglas para gestionar datos, verificar resultados y aprobar cambios. El propósito, las personas destinatarias, el alcance y las señales de éxito se documentan por separado en la misión del proyecto. No es un plan técnico ni un mecanismo de seguridad ejecutable. Adapta esta estructura a las necesidades y los acuerdos de tu proyecto.

**Uso manual:** sustituye cada texto entre corchetes. **Uso asistido:** entrega esta plantilla a un asistente de IA desde su ubicación real y pídele que lea únicamente los documentos de contexto que tú indiques; incluye la misión aplicable solo si ya existe y autorizas su lectura. La misión no es un requisito previo para crear la constitución: su referencia puede quedar pendiente. El asistente debe hacer una entrevista con una pregunta por turno, explicar la sección y esperar tu respuesta antes de continuar; no vuelve a preguntar lo ya confirmado en los documentos que leyó y pregunta únicamente lo que falte o sea ambiguo. Después presenta el borrador completo y espera tu aprobación explícita antes de guardar. Puede trabajar con un archivo temporal descargado o con la plantilla abierta en su ubicación original: no es obligatorio copiarla a la carpeta del proyecto. Si `CONSTITUTION.md` ya existe, el asistente debe mostrar los cambios propuestos y esperar autorización explícita para actualizarlo; sin autorización, conserva el original. Tras el guardado aprobado, la comprobación final es una lectura de solo lectura que cita secciones reales del archivo. Los ejemplos son ilustrativos. Lo desconocido queda como «Pendiente de decisión» e indica quién debe decidirlo; no inventes datos. No incluyas secretos ni datos personales sensibles.

### Rutas, destino y fuentes (uso asistido)

La carpeta del proyecto abierto es la raíz de trabajo: las rutas se expresan relativas a ella. Si el asistente no puede determinar el proyecto abierto o su raíz, debe preguntar antes de continuar.

Tú confirmas la subcarpeta de contexto y el nombre del archivo una sola vez, como parte de la aprobación del contenido, antes de guardar. Si el documento ya existe, indícale su ruta exacta para que lo lea; el asistente no busca archivos por su cuenta. El nombre de esa subcarpeta es un ejemplo ilustrativo y no una carpeta obligatoria (por ejemplo, `docs/contexto/CONSTITUTION.md`).

La plantilla puede permanecer fuera del proyecto, en una ubicación accesible que autorices; no es obligatorio copiarla ni conceder acceso externo general. La plantilla es la fuente estructural; la constitución es el documento real y adaptado de tu proyecto, que puede no existir todavía.

Puedes autorizar fuentes existentes opcionales, como la idea del proyecto, requisitos acordados o decisiones confirmadas; «Ninguno» se refiere solo a esas fuentes opcionales, no a la plantilla que el asistente debe leer. La entrevista no exige una hoja de ruta, un stack ni especificaciones futuras.

Durante la entrevista no se crean ni modifican archivos ni carpetas y no se ejecuta código; si hace falta crear la carpeta, se confirma por separado como parte del guardado autorizado. Muestra la ruta prevista y confirma la ruta exacta (carpeta y nombre de archivo) antes de guardar.

## 1. Identificación

**Qué escribir:** nombre corto, responsable y fecha de revisión. No incluyas datos personales innecesarios.

**Ejemplo según el proyecto:** una herramienta local, un sitio web informativo o un informe basado en datos sintéticos.

- Proyecto: [nombre]
- Responsable de las decisiones: [persona o equipo]
- Última revisión: [AAAA-MM-DD]

## 2. Propósito y alcance de referencia

**Qué escribir:** identifica el proyecto en una línea y enlaza el documento donde se detallan el propósito, las personas destinatarias, el alcance, las exclusiones y las señales de éxito: la misión del proyecto. Esta constitución gobierna reglas, responsabilidades y autorizaciones; no repitas aquí el propósito ni el alcance detallados.

- Proyecto: [nombre y una línea de propósito]
- Misión aplicable: [mision-template.md](mision-template.md) o la ruta real de `MISSION.md`; si aún no existe, «Pendiente de decisión: se prepara en la etapa de misión»

## 3. Principios de trabajo

**Qué escribir:** de tres a cinco reglas que guían decisiones cuando haya dudas. Incluye honestidad sobre evidencia y prioridad de revisión humana.

**Ejemplos:** «No presentar estimaciones como mediciones»; «Preferir cambios pequeños y revisables»; «Explicar las limitaciones conocidas».

- [Principio y conducta observable]
- [Principio y conducta observable]
- [Principio y conducta observable]

## 4. Personas, responsabilidades y autorización

**Qué escribir:** quién decide el alcance, quién revisa resultados y qué puede proponer o hacer un asistente de IA. Distingue sugerir de ejecutar y exige aprobación humana explícita para acciones no autorizadas.

**Ejemplos:** la persona responsable aprueba los cambios que afectan el alcance, los datos o la publicación; el equipo propone alternativas y pide explicaciones antes de decidir; las acciones no autorizadas esperan aprobación explícita.

- Decisiones reservadas a una persona: [alcance, publicación, datos, cambios sensibles]
- Ayuda permitida al asistente: [por ejemplo, explicar archivos leídos o proponer opciones]
- Acciones que requieren aprobación antes de ejecutarse: [enumerar]
- Si la instrucción o autorización no está clara: [detenerse y preguntar a quién]

## 5. Alcance autorizado y exclusiones de acción

**Qué escribir:** el alcance del producto y sus exclusiones se documentan en la misión; aquí registra solo qué acciones, usos y datos quedan autorizados en esta etapa y qué queda expresamente fuera. Evita prometer capacidades no comprobadas.

**Ejemplos:** una herramienta local puede procesar un conjunto de demostración sin conectarse a servicios; un sitio puede mostrar páginas informativas sin recopilar cuentas; un informe puede resumir datos facilitados sin inferir identidades.

- Alcance del producto y exclusiones: documentados en la misión; no se repiten aquí
- Acciones y usos autorizados en esta etapa: [resultados y actividades incluidas]
- Acciones y usos excluidos: [funciones, públicos o usos excluidos]
- Supuestos pendientes de confirmar: [supuesto y persona que lo confirmará]

## 6. Datos, privacidad y seguridad

**Qué escribir:** qué datos se usarán, de dónde proceden, si son sintéticos o autorizados, dónde se guardan y qué no debe incorporarse. No pegues secretos, contraseñas, tokens ni datos personales sensibles en este documento ni en solicitudes al asistente.

**Ejemplos:** «solo registros ficticios creados para la práctica»; «contenido público aprobado por el responsable»; «archivo agregado sin identificadores personales, entregado por el equipo».

- Datos permitidos y procedencia: [descripción verificable]
- Datos excluidos: [por ejemplo, credenciales o datos personales no autorizados]
- Ubicación y conservación: [dónde se guardan y cuándo se eliminan, si aplica]
- Límites de seguridad aplicables: [límites aprobados para este proyecto]
- Si aparece un dato no previsto o sensible: [detener el uso y avisar a]

## 7. Entorno y herramientas autorizadas

**Qué escribir:** las decisiones de plataformas, herramientas y versiones se documentan en el stack del proyecto; aquí registra solo el entorno ya confirmado que los límites de seguridad necesitan y las acciones permitidas al asistente. Define acciones permitidas a partir de la autorización real del proyecto; este texto no instala ni concede permisos.

**Ejemplos:** «editor de texto en Windows, macOS o Linux»; «navegador actual para revisar páginas»; «hoja de cálculo disponible en el equipo». No adoptes un ejemplo si no corresponde.

- Entorno y plataformas confirmadas para esta etapa: [sistemas/dispositivos y versiones comprobadas o “por decidir”]
- Decisiones de stack y herramientas: documentadas en el stack del proyecto o «Pendiente de decisión»; no se repiten aquí
- Acciones permitidas al asistente: [solo lo autorizado; separar lectura, propuesta y escritura]
- Acciones que no se autorizan: [por ejemplo, publicar o modificar datos originales]
- Límites técnicos conocidos: [compatibilidad, acceso, almacenamiento u otros]

## 8. Calidad, verificación y evidencia

**Qué escribir:** cómo una persona comprobará que el resultado sirve y qué evidencia se conservará. Distingue pruebas planificadas de pruebas realmente ejecutadas.

**Ejemplos:** comprobar manualmente una suma con datos de prueba; recorrer enlaces de un sitio antes de publicarlo; contrastar un gráfico con los registros de origen.

- Criterios de aceptación: [condiciones observables]
- Verificación prevista: [pasos y responsable]
- Evidencia a registrar: [salida, revisión, fuente o resultado; nunca afirmarla antes de observarla]
- Limitaciones conocidas: [qué no demuestra la verificación]

## 9. Cambios, aprobación y revisión

**Qué escribir:** quién puede cambiar esta constitución, cómo se aprueban modificaciones del proyecto y cuándo se revisará el documento. La constitución puede cambiar mediante decisión humana explícita.

**Ejemplos:** «Revisar al cambiar el público objetivo»; «La persona responsable aprueba antes de publicar»; «Registrar fecha y motivo cuando cambie el tratamiento de datos».

- Aprobación de cambios: [persona o proceso]
- Cambios que requieren revisión previa: [alcance, datos, publicación, permisos]
- Próxima revisión o condición que la activa: [fecha o condición]
- Historial breve de decisiones: [fecha — decisión — responsable]

## Revisión antes de adoptar

- [ ] El propósito y los límites describen el proyecto real.
- [ ] El propósito y el alcance detallados viven en la misión y aquí solo se referencian.
- [ ] Las autorizaciones son específicas y fueron confirmadas por una persona.
- [ ] Los datos y riesgos están descritos sin incluir información sensible.
- [ ] Las verificaciones no afirman resultados que aún no se observaron.
- [ ] Se eliminaron todos los marcadores entre corchetes y ejemplos que no aplican.
- [ ] La persona responsable revisó y aprobó el documento.
