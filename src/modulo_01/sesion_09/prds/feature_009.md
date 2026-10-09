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
