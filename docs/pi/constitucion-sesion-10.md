# Constitución de proyecto — Ejemplo de la Sesión 10

Este documento completo es un ejemplo educativo para el ejercicio `matrix_review.py` de la Sesión 10. No contiene la solución del programa y no sustituye el cuaderno del estudiante. La sesión trabaja con una matriz sintética escrita por el estudiante en su propio equipo; el objetivo aquí es dejar claros el contexto y los límites antes de programar.

## 1. Identificación

- Proyecto: resumen didáctico de una matriz local por día.
- Responsable de las decisiones: estudiante que realiza el ejercicio; la persona docente orienta la práctica.
- Última revisión: ejemplo preparado para acompañar la Sesión 10; no se registra una fecha de aprobación del estudiante.

## 2. Propósito y resultado esperado

- Necesidad: practicar ciclos anidados de dos niveles y comunicar un resumen por día de una matriz local de eventos sintéticos.
- Personas destinatarias: estudiante y persona que revisa su explicación del ejercicio.
- Resultado esperado: un resumen que separa los subtotales por día, declara las entradas `UNKNOWN` omitidas y presenta el total de errores contados, con las limitaciones del recorrido explicadas.

## 3. Principios de trabajo

- La persona estudiante escribe y comprende su propio código; este documento no proporciona las operaciones que debe completar.
- Se informa qué datos se procesaron y qué datos quedaron fuera del conteo.
- No se afirma que un resumen didáctico confirme un incidente real.
- Las decisiones y autorizaciones no descritas se consultan con la persona responsable antes de actuar.

## 4. Personas, responsabilidades y autorización

- Decisiones reservadas a una persona: el estudiante elige y escribe su solución; la persona docente define el marco y revisa la comprensión conforme al material de clase.
- Ayuda permitida al agente: si la persona estudiante lo solicita y las reglas de su curso lo permiten, puede pedir que Pi lea este archivo y resuma sus límites; este ejemplo no concede autorización para resolver el ejercicio.
- Acciones que requieren aprobación antes de ejecutarse: cualquier cambio de alcance, uso de datos distintos de la matriz sintética o acción no indicada por el material autorizado.
- Si la instrucción o autorización no está clara: detenerse y consultar a la persona docente. La declaración de esta constitución no reemplaza las reglas de la sesión sobre asistencia de IA.

## 5. Alcance y exclusiones

- Incluye: ejercicio local `matrix_review.py`; tres listas de seis posiciones como entrada didáctica; ciclo exterior para día e interior para evento; `continue` en `UNKNOWN`; `break` en `STOP`, que termina solo el ciclo del día actual; subtotales por día y total de errores contados.
- No incluye: lectura de archivos, acceso a red, apertura de puertos, conexión con sistemas, análisis de registros reales, confirmación de incidentes ni implementación automática de la solución.
- Supuestos: la matriz es sintética y está transcrita en el cuaderno de trabajo de la Sesión 10; las etiquetas son propias de la práctica, no estándares universales.

## 6. Datos, privacidad y seguridad

- Datos permitidos y procedencia: valores didácticos (`INFO`, `ERROR`, `UNKNOWN`, `WARNING`, `STOP`) de la matriz publicada en el cuaderno del estudiante de la Sesión 10; el estudiante escribe la matriz localmente.
- Datos excluidos: registros reales, credenciales, información personal y datos de terceros.
- Ubicación y conservación: matriz escrita en el archivo local del ejercicio; no se define retención adicional en el material de la sesión.
- Límites de seguridad aplicables: el ejercicio descrito opera sobre datos sintéticos locales y no usa red, archivos de entrada ni puertos.
- Si aparece un dato no previsto o sensible: no incorporarlo; detenerse y consultar a la persona docente.

## 7. Entorno, plataformas y herramientas

- Plataformas objetivo: el material de la Sesión 10 describe Windows, Linux y macOS; no fija aquí versiones instaladas distintas de las indicadas por el material oficial de esa sesión.
- Herramientas permitidas: editor de texto y Python local según la ruta de plataforma del cuaderno; las acciones exactas se rigen por las instrucciones de la sesión.
- Acciones permitidas al agente: esta constitución por sí sola no autoriza lectura, escritura, ejecución ni cambios; cualquier uso de Pi depende de las reglas vigentes del curso y de la instrucción explícita de la persona estudiante.
- Acciones que no se autorizan: completar los TODO del ejercicio, inventar resultados de ejecución, acceder a sistemas externos o ampliar el conjunto de datos.
- Límites técnicos conocidos: la sesión enseña anidación de dos niveles, `continue` y `break`; no introduce funciones, `else` en ciclos ni un tercer nivel.

## 8. Calidad, verificación y evidencia

- Criterios de aceptación: el estudiante puede explicar ciclo exterior e interior, diferenciar `continue` de `break`, explicar los subtotales por día y declarar lo que el programa no hace.
- Verificación prevista: ejecutar el archivo escrito por el estudiante en su entorno y comparar su salida con el cuaderno después de ejecutarlo.
- Evidencia a registrar: salida realmente observada y explicación del estudiante; este documento no afirma que el programa haya sido creado ni ejecutado.
- Limitaciones conocidas: tres días por seis posiciones representan 18 posiciones de entrada, pero no garantizan 18 visitas del ciclo interior: `break` deja de recorrer las posiciones restantes de ese día. Las posiciones posteriores a `STOP` no se cuentan.

## 9. Cambios, aprobación y revisión

- Aprobación de cambios: el estudiante consulta a la persona docente antes de cambiar datos, propósito o límites establecidos por la sesión.
- Cambios que requieren revisión previa: incorporar datos reales, añadir acceso a archivos o red, o solicitar a un agente que complete el ejercicio.
- Próxima revisión o condición que la activa: revisar si cambia el cuaderno oficial o el alcance de la sesión.
- Historial breve de decisiones: ejemplo de constitución preparado como material de apoyo; no registra una aprobación individual ni modifica el ejercicio.

## Referencia

Consulta el [cuaderno de trabajo del estudiante de la Sesión 10](../modulo_01/sesion_10/material_estudiante_sesion_10.html) para la matriz, instrucciones y criterios oficiales del ejercicio. El código del estudiante y los TODO permanecen fuera de este documento.
