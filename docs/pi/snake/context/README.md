# Contexto del proyecto Snake

Documentación concreta del proyecto **Snake**: un juego de navegador en TypeScript que se documenta aquí como proyecto propio, separado de las plantillas de enseñanza reutilizables y de las referencias visuales aceptadas. Este conjunto describe acuerdos, propósito, plataforma, plan y memoria del proyecto; **no implementa el juego** y no sustituye a la [idea inicial](../../idea-proyecto-snake.md) ni al [recorrido de una partida](../../game-flow-snake.md), que siguen siendo la fuente funcional.

Estado: **documentado, no implementado**. No existe código de la aplicación, ni compilaciones, ni inicialización del juego. El arranque real de la aplicación **no se ha implementado**.

## Documentos

| Documento | Contenido |
| --- | --- |
| [CONSTITUTION.md](CONSTITUTION.md) | Acuerdos de trabajo estables del proyecto |
| [MISSION.md](MISSION.md) | Propósito, público y alcance del producto |
| [TECH-STACK.md](TECH-STACK.md) | Plataforma y lenguaje confirmados |
| [ROADMAP.md](ROADMAP.md) | Plan de producto por fases |
| [MEMORY.md](MEMORY.md) | Hechos aprobados con su fuente y dudas abiertas |
| [specs/inicio.md](specs/inicio.md) | Primera entrega funcional de Inicio (definida, no implementada) |
| [AGENTS.example.md](AGENTS.example.md) | Ejemplo ilustrativo de navegación (no es configuración activa) |

## Fuentes funcionales

- [Idea inicial: juego de Snake](../../idea-proyecto-snake.md) — propósito, público y comportamientos indispensables.
- [Recorrido de una partida](../../game-flow-snake.md) — estados, transiciones y casos de ranking.
- [Wireframes de Snake](../design/README.md) — propuesta de diseño y estado de las pantallas piloto.

## Estado del diseño y de la aplicación

Los cinco pilotos (`start-pilot.html`, `playing-pilot.html`, `game-over-pilot.html`, `victory-pilot.html` y `top10-pilot.html`) están **aceptados únicamente como referencia visual**. Esa aceptación no implica que exista un juego implementado, ni compatibilidad responsive de producción, ni validación del renderizado sin conexión con la fuente real, ni compilaciones de la aplicación. El framework y la cadena de herramientas **no están elegidos**.

Para el detalle de diseño, ver [visual-style.md](../design/visual-style.md), [screens.md](../design/screens.md) y la [guía de aplicación](../design/DESIGN.md).

## Contexto de aula

Este proyecto se documenta en un contexto de clase confirmado: los estudiantes crean un *starter* en clase; existen cinco vistas estáticas sin jugabilidad; y la primera entrega funcional es la pantalla de Inicio (nombre, foco y `play`/Enter hacia Partida, sin movimiento). El objetivo de tiempo para la actividad es de **30 a 45 minutos**; **no se ha medido ni observado una duración real de aula**. Estos datos describen el ejercicio de clase y **no** el propósito del producto, descrito en [MISSION.md](MISSION.md).
