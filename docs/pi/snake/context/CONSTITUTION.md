# Constitución del proyecto Snake

Acuerdos de trabajo de este proyecto. **No es un plan técnico ni un mecanismo de seguridad ejecutable.** No sustituye a la misión, al stack ni a las especificaciones funcionales. Tampoco amplía permisos generales de otros proyectos o herramientas.

## 1. Identificación

- **Proyecto:** Snake.
- **Responsable de las decisiones:** equipo de desarrollo.
- **Última revisión:** 2026-10-21.

## 2. Propósito y alcance de referencia

- **Proyecto:** juego de Snake para navegador web.
- **Misión de referencia:** [MISSION.md](MISSION.md).
- **Fuente funcional consultada:** [idea del proyecto](../../idea-proyecto-snake.md).

El propósito, el público, el alcance del producto, sus exclusiones y las señales de éxito corresponden a la misión y a las especificaciones aplicables; no se reproducen aquí.

La referencia a la misión procede de la constitución anterior. Su contenido y la resolución de ese enlace no se comprobaron durante la entrevista que produjo esta revisión.

## 3. Principios de trabajo

- **Honestidad sobre evidencia:** no se presenta como hecho lo que no se observó. Lo que no está implementado o verificado se declara como pendiente.
- **Cambios pequeños y revisables:** cada cambio se limita a lo autorizado y se puede revisar.
- **Aprobación humana explícita:** actuar únicamente dentro de la autorización concedida. Las acciones que requieren aprobación, definidas en la sección de responsabilidades, deben esperar la aprobación explícita del equipo de desarrollo. Ante ambigüedad, detenerse y preguntar.
- **Distinguir referencias de resultados:** una referencia visual aceptada orienta el diseño, pero no demuestra que lo representado esté implementado ni verificado.

## 4. Personas, responsabilidades y autorización

- **Decisiones reservadas al equipo de desarrollo:** alcance, reglas pendientes, compatibilidad, tratamiento de datos, publicación, permisos del asistente y cambios de esta constitución.
- **Ayuda permitida al asistente:** leer las fuentes indicadas, explicarlas y proponer borradores o alternativas.
- **Modificaciones solicitadas por el equipo:** una instrucción explícita autoriza al asistente a modificar el archivo dentro del alcance indicado, sin solicitar una aprobación adicional para ese mismo cambio.
- **Modificaciones propuestas por el asistente:** requieren aprobación antes de ejecutarse. La solicitud debe explicar qué se propone cambiar, por qué y qué consecuencias tendría, para orientar la decisión del equipo.
- **Otras acciones:** una autorización para modificar archivos no autoriza por sí misma instalaciones, commits, publicación u otras operaciones no incluidas en la instrucción.
- **Ante ambigüedad:** detener la acción afectada y preguntar al equipo de desarrollo.

## 5. Alcance autorizado y exclusiones de acción

- **Etapa actual:** planeación y documentación del proyecto.
- **Objetivo de desarrollo confirmado:** completar el juego antes del taller, conforme al alcance aprobado. La implementación no queda excluida permanentemente.
- La planeación no constituye por sí sola una autorización para ejecutar la implementación.
- Las funciones y decisiones que las fuentes mantienen pendientes no se consideran aprobadas por aparecer en ellas.
- El alcance del producto y sus exclusiones se documentan en la misión y las especificaciones; no se redefinen aquí.
- Las acciones que excedan una instrucción explícita esperan la autorización del equipo de desarrollo.

## 6. Datos, privacidad y seguridad

- **Datos permitidos:** contenido del proyecto, material sintético o autorizado y alias y resultados necesarios para el juego y su top 10.
- **Datos excluidos:** credenciales, contraseñas, tokens, datos personales sensibles, material privado del docente y otros datos personales no autorizados.
- Se orientará a los jugadores a utilizar alias y a no introducir nombres reales ni datos personales. Las restricciones de longitud y el aviso no garantizan que nadie los introduzca.
- **Conservación persistente:** solo se conservarán los alias y resultados que integren el top 10. Los registros desplazados se eliminarán.
- **Resultados que no clasifican:** podrán manejarse temporalmente durante la partida y su cierre para mostrarlos y determinar su clasificación, pero no se persistirán ni se conservarán en registros auxiliares.
- **Duración de conservación:** depende de la permanencia del registro en el top 10; no se ha establecido un plazo fijo.
- **Ubicación concreta del almacenamiento:** Pendiente de decisión — equipo de desarrollo. La tecnología elegida se documentará en el stack.
- No se incluirán rutas privadas ni identificadores internos en documentos públicos.
- **Procedimiento ante datos personales introducidos pese al aviso u otros datos sensibles no previstos:** Pendiente de decisión — equipo de desarrollo.

## 7. Entorno y herramientas autorizadas

- **Sistemas operativos confirmados para el trabajo:** principalmente Windows, también macOS y, en menor medida, Linux.
- **Navegador oficial:** Chrome.
- **Versiones concretas:** Pendiente de decisión — equipo de desarrollo.
- **Stack de referencia:** [TECH-STACK.md](TECH-STACK.md). Las decisiones técnicas se documentan allí, sin duplicarlas en esta constitución.
- Se prevé utilizar Chrome DevTools con agentes de código para comprobaciones automatizadas. Esta intención no demuestra que la integración esté configurada ni funcionando.
- El asistente distingue lectura, propuesta, escritura y ejecución, y actúa únicamente dentro de la autorización correspondiente.
- Durante una entrevista guiada de documentación no se ejecuta código ni se crean o modifican archivos, salvo una autorización explícita que habilite una acción concreta.
- **Integración concreta de automatización y límites técnicos pendientes:** los definirá el equipo de desarrollo en la documentación técnica.

La referencia al stack no implica que su contenido ni sus enlaces se hayan comprobado en esta revisión.

## 8. Calidad, verificación y evidencia

- **Documentación:** debe ser coherente con los acuerdos aprobados y las fuentes aplicables. La existencia de archivos y la resolución de sus enlaces requieren comprobación; no se presuponen.
- **Juego:** los criterios funcionales detallados corresponden a las especificaciones. Los criterios todavía no definidos quedan como Pendiente de decisión — equipo de desarrollo.
- **Verificación prevista:** comprobaciones documentales y, durante el desarrollo autorizado, comprobaciones manuales o automatizadas que correspondan.
- **Participación de los agentes:** podrán ejecutar comprobaciones dentro de lo autorizado y aportar la evidencia observada.
- **Aceptación:** el equipo de desarrollo revisará la evidencia y decidirá si acepta el resultado.
- **Evidencia:** registrar qué se comprobó, en qué entorno, cuál fue el resultado observado y qué limitaciones quedaron.
- Distinguir siempre las pruebas previstas de las realmente ejecutadas. Una prueba fallida, no ejecutada o bloqueada no se presenta como superada.
- Una comprobación estructural de documentos no demuestra que el juego funcione, y una referencia visual no demuestra una implementación funcional.

## 9. Cambios, aprobación y revisión

- **Aprobación de cambios:** equipo de desarrollo.
- **Motivos de revisión:** cambios en el alcance, resolución o modificación de reglas pendientes, tratamiento de datos, publicación, permisos del asistente o responsabilidades del equipo.
- **Periodicidad:** no se fija una fecha periódica por ahora; la revisión se activa por los motivos anteriores.
- **Flujo para adoptar una revisión:** entrevista → borrador completo y diferencias → aprobación explícita del contenido y la ruta → guardado limitado → verificación de solo lectura.
- El cumplimiento de esta constitución depende de revisión humana; el documento no se carga ni se aplica automáticamente como mecanismo técnico.
- **Historial:** 2026-10-21 — el equipo de desarrollo aprobó esta revisión tras la entrevista guiada.

## Revisión de adopción

- [x] El documento representa los acuerdos del equipo.
- [x] El propósito y el alcance detallados se mantienen en sus documentos de referencia.
- [x] Las autorizaciones distinguen instrucciones explícitas de propuestas del asistente.
- [x] Los datos y sus reglas de conservación están descritos sin incluir información sensible.
- [x] Los asuntos desconocidos identifican al equipo de desarrollo como responsable de decidir.
- [x] El equipo aprobó el contenido completo y la ruta exacta de guardado.
