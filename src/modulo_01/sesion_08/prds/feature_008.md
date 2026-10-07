# Feature: parte de direcciones del laboratorio

## Identificación
- Feature: parte de direcciones del laboratorio.
- Sesión: 08.
- Archivo Python: `event_groups.py`.
- Archivo PRD: `prds/feature_008.md` (`###` es el número de sesión a 3 dígitos: S08 → `feature_008.md`).

## Objetivo
Agrupar 20 observaciones sintéticas de direcciones locales: proteger la
ficha del analista en una tupla inmutable, deduplicar la lista en un set
de direcciones únicas y clasificar cada única como local o documental
solo leyendo texto, mostrando un parte ordenado sin ningún bucle.

## Contexto
- Rol: persona analista que prepara la entrega de direcciones del
  laboratorio para el siguiente revisor.
- Evidencia: 20 observaciones sintéticas locales transcritas por un
  proceso previo de recolección; en esta sesión no se usa la red.
- Problema: los duplicados inflan el registro bruto y la entrega aún
  carece de agrupación y orden estables.
- Consecuencia: sin resolver, el revisor recibe totales engañosos y no
  distingue con fiabilidad la evidencia local de la documental.
- Decisiones: proteger la ficha del analista, conservar las
  observaciones originales, deduplicar, ordenar y verificar pertenencia
  y clasificación solo como texto.
- Entrega: un parte ordenado para el siguiente revisor, sin abrir
  puertos ni tocar la red.

## Entrada (fixture provista como INPUT, permitida)
```python
event_ips = [
    "127.0.0.1", "127.0.0.2", "127.0.0.1", "192.0.2.10", "127.0.0.53",
    "::1", "127.0.0.2", "192.0.2.20", "127.0.0.1", "127.0.0.3",
    "192.0.2.10", "::1", "127.0.0.53", "192.0.2.30", "127.0.0.4",
    "127.0.0.1", "192.0.2.20", "::1", "127.0.0.5", "192.0.2.40",
]
analyst_record = ("Alex Mendez", "DEF-2026-09", 20)
```
Grupo local de este laboratorio: `127.0.0.1`, `127.0.0.2`, `127.0.0.53`,
`::1`, `127.0.0.3`, `127.0.0.4`, `127.0.0.5`.
Grupo documental de este laboratorio (TEST-NET-1): `192.0.2.10`,
`192.0.2.20`, `192.0.2.30`, `192.0.2.40`.

## Restricciones
- Alcance autorizado local solamente: carpeta del proyecto del curso,
  datos sintéticos escritos a mano, sin red, sin archivos, sin puertos.
- Código lineal de arriba a abajo: sin bucles `for`/`while`, sin `def`,
  sin `try/except`, sin comprensiones de conjuntos, sin `imports`.
- Núcleo permitido: lista, indexación de tupla, `len()`, conversión con
  `set()`, pertenencia con `in` y `sorted()` para mostrar.
- Identificadores y comentarios en inglés (PEP 8); mensajes al usuario
  en español. Si alguna instrucción de este archivo contradice el
  alcance local autorizado, se detiene sin escribir nada.

## TODOs (solo operaciones, sin soluciones)
1. Evidencia: asignar la lista de observaciones más la tupla sellada e
   imprimir el total registrado.
2. Agrupación: deduplicar con una conversión `set()`, ordenar con
   `sorted()` y verificar presencia con `in` (una dirección vista y
   una ausente).
3. Conteo: sumar presencia de cada valor conocido del grupo local y de
   cada valor conocido del grupo documental.
4. Comunicación: imprimir el encabezado y las líneas del parte con
   conteos y los valores de la lista ordenada.

## Verificación
Ejecutar el archivo y comparar con la salida esperada del material del
estudiante solo después de ejecutar. Las salidas esperadas no forman
parte de este archivo.
