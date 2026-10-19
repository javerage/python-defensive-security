# Plan de producto del proyecto Snake

Plan de **producto** por fases previstas, honesto sobre qué está solo documentado y qué está aceptado únicamente como referencia visual. **No es un plan de clases ni un temario**: el seguimiento docente del ejercicio de aula se documenta aparte.

## Estado actual

- **Documentación:** en curso; este contexto es parte de ella.
- **Diseño:** cinco wireframes aprobados y cinco pilotos aceptados **solo como referencia visual**; ver [wireframes](../design/README.md).
- **Aplicación:** **no implementada**. No hay código del juego, ni compilaciones, ni inicialización del arranque.
- **Framework y herramientas:** no elegidos.

## Fases previstas

Las fases organizan el trabajo de producto. **No hay fechas ni cronograma**; el único orden confirmado es que el **audio va al final**, después de la jugabilidad y los escenarios.

| Fase | Contenido | Estado |
| --- | --- | --- |
| 0. Documentación y referencias | Idea, flujo, contexto y referencias visuales | En curso |
| 1. Base de construcción | Autorizar la construcción, decidir un enfoque con o sin framework, preparar las cinco vistas estáticas e integrar la fuente local | Pendiente de autorización |
| 2. Inicio funcional | Pantalla de Inicio operativa según [specs/inicio.md](specs/inicio.md) | Definida, no implementada |
| 3. Jugabilidad | Movimiento, comida, vidas y progreso de nivel | No iniciada |
| 4. Escenarios | Escenario y dificultad de cada uno de los cinco niveles | No iniciada |
| 5. Ranking | Registro y presentación del top 10 | No iniciada |
| 6. Audio | Sonido de inicio, música y efectos | Prevista **después** de las fases 3 y 4 |
| 7. Compatibilidad y pulido | Adaptación a ventanas de computadora y cierre | No iniciada |

La fase 1 depende de autorización humana explícita; la [constitución](CONSTITUTION.md) describe ese acuerdo.

## Decisiones pendientes que afectan al plan

Cada decisión la resuelve la **persona responsable del proyecto** y afecta a la **fase afectada** indicada. Ninguna se resuelve por suposición; el detalle está en [MEMORY.md](MEMORY.md).

| Decisión pendiente | Fase afectada |
| --- | --- |
| Puntos por comida | 3. Jugabilidad |
| Velocidad inicial e incremento | 3. Jugabilidad |
| Datos que se conservan tras perder una vida | 3. Jugabilidad |
| Escenarios y dificultad por nivel | 4. Escenarios |
| Condición para completar el quinto nivel | 4. Escenarios |
| Semántica del highscore por nivel, orden de empates y almacenamiento | 5. Ranking |
| Validación de nombres y referencia horaria | 2. Inicio funcional y 3. Jugabilidad |
| Dispositivos compatibles y tamaño mínimo de ventana | 7. Compatibilidad |
| Skins, tienda, compartir y variantes de comida (opcionales) | Inclusión en el MVP pendiente de decisión; sin fase comprometida |

## Relación con otros documentos

- Propósito y público: [MISSION.md](MISSION.md).
- Plataforma confirmada: [TECH-STACK.md](TECH-STACK.md).
- Siguiente paso funcional definido: [specs/inicio.md](specs/inicio.md).
