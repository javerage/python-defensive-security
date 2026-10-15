# Snake Game Flow

## Game

Este documento describe el recorrido de una partida de Snake: cómo comienza, qué sucede mientras se juega y cómo termina cuando se agotan las vidas. La tabla y el diagrama representan el mismo flujo. Los nombres de estados y eventos están en inglés; las explicaciones están en español.

**Source:** [Idea inicial: juego de Snake](idea-proyecto-snake.md).

**Template:** [Game Flow Template](game-flow-template.md).

Las referencias de la tabla corresponden a estas secciones de la idea:

- **S1:** «1. Qué quiere construir»: navegador web, TypeScript y modo historia de cinco niveles con dificultad creciente y cambio de escenario.
- **S3:** «3. Qué necesidad o experiencia quiere atender»: presentación del juego y resultados al finalizar.
- **S4:** «4. Qué comportamientos considera indispensables»: inicio, controles, movimiento, comida, progreso, vidas, escenarios, highscore y sonido.
- **S5:** «5. Qué quedará fuera de la primera versión»: sin guardar y retomar partidas ni modo multijugador; se mantiene el highscore.
- **S6:** «6. Qué todavía no sabe decidir»: reglas y funciones que siguen abiertas.

El inicio y el reinicio se rigen por estas reglas de la sección S4:

- **Player name:** se puede indicar un nombre antes de iniciar. Si se pulsa `play` o la tecla de espacio sin haberlo indicado, se genera `player_YYYYMMDD_HHmmss_SSS` con la fecha, la hora y tres dígitos de milisegundos del momento de inicio, y la partida comienza sin pedir otra acción. Por ejemplo: `player_20261015_173025_482`. No se usa aleatoriedad ni se garantiza unicidad; es un nombre visible de la partida, no un identificador único. La referencia horaria y la validación detallada de los nombres escritos siguen pendientes.
- **Automatic restart:** si una colisión consume una vida y todavía quedan otras, la partida se reinicia y el movimiento se reanuda automáticamente. No se vuelve a pedir `play` ni la tecla de espacio. Qué datos se conservan o reinician sigue pendiente.

Los estados describen situaciones del juego, no pantallas ni diseños de interfaz:

- `AwaitingStart`: se espera la acción de inicio; indicar un nombre es opcional.
- `Playing`: la serpiente se mueve y el jugador puede dirigirla.
- `Results`: la partida terminó por agotarse las vidas y se muestran sus resultados.

`Pending decision` es una marca de información faltante, no un estado que el juego deba implementar. No implica pausar, terminar o continuar la partida de una forma que todavía no se haya acordado.

## States & Transitions

| Current state | Action or event | Condition | Game response | Next state | Source or open question |
| --- | --- | --- | --- | --- | --- |
| `AwaitingStart` | `NameProvided` — indicar el nombre | Todavía no se ha solicitado el inicio | Conservar el nombre escrito y esperar `play` o espacio | `AwaitingStart` | S4. Validación detallada: S6 |
| `AwaitingStart` | `StartRequested` — pulsar `play` o espacio | No se ha indicado un nombre | Generar `player_YYYYMMDD_HHmmss_SSS` e iniciar con tres vidas y una serpiente de tres bloques que avanza automáticamente en horizontal; mostrar puntaje, vidas y velocidad; reproducir el sonido de inicio y la música suave en bucle | `Playing` | S4. Referencia horaria y velocidad inicial: S6 |
| `AwaitingStart` | `StartRequested` — pulsar `play` o espacio | Hay un nombre indicado | Usar el nombre escrito e iniciar con tres vidas y una serpiente de tres bloques que avanza automáticamente en horizontal; mostrar puntaje, vidas y velocidad; reproducir el sonido de inicio y la música suave en bucle | `Playing` | S4. Velocidad inicial: S6 |
| `Playing` | `MovementContinues` — transcurre el movimiento | No ocurre una colisión ni otro evento de cambio | Continuar el desplazamiento automático | `Playing` | S4 |
| `Playing` | `DirectionRequested` — pulsar una flecha | La partida está en curso | Dirigir la serpiente con las flechas del teclado | `Playing` | S4. No se añaden reglas de giro que no estén definidas |
| `Playing` | `FoodConsumed` — comer un bloque | La serpiente consume comida | Sumar puntos, crecer un bloque, actualizar el puntaje y reproducir `coin`; comprobar si corresponde subir de nivel | `Playing` | S4. Puntos por comida: S6 |
| `Playing` | `LevelAdvance` — corresponde subir de nivel | Se cumple el umbral de 15 puntos y queda un nivel siguiente entre los cinco previstos | Subir de nivel, aumentar la velocidad y cambiar el escenario con mayor dificultad | `Playing` | S1; S4. Incremento de velocidad y escenarios concretos: S6 |
| `Playing` | `Collision` — chocar con un muro o con el propio cuerpo | Tras descontar una vida todavía quedan otras | Actualizar las vidas, reproducir `explosion`, reiniciar la partida y reanudar el movimiento automáticamente | `Playing` | S4. Puntaje, nivel, velocidad y demás datos tras el reinicio: S6 |
| `Playing` | `Collision` — chocar con un muro o con el propio cuerpo | Se pierde la última vida | Terminar la partida y mostrar nombre, puntaje, nivel y velocidad alcanzados; se aplican los sonidos de pérdida de vida y `game over`, sin fijar su orden | `Results` | S3; S4 |
| `Playing` | `FinalLevelCompleted` — completar el quinto nivel | La condición de finalización todavía no está definida | No se decide una victoria, un sexto nivel ni otra continuación | `Pending decision` | S1; S6. Es un límite del conocimiento del flujo, no un comportamiento aprobado |
| `Pending decision` | `HighscoreRecording` — registrar y consultar resultados | El momento y el punto de acceso todavía no están definidos | Requisito confirmado: guardar highscore por nivel alcanzado y mostrar como máximo los diez mejores resultados, retirando los superados. No se fija todavía su conexión con el resto del recorrido | `Pending decision` | S4; S6. Registro por nivel, empates, almacenamiento y duración: pendientes |

Los eventos de comida y avance de nivel pueden relacionarse: la tabla no establece una prioridad de procesamiento ni inventa cuántos puntos da cada comida. Del mismo modo, la transición de colisión confirma el reinicio automático, pero no supone que se conserven o se pierdan datos todavía no decididos.

El audio forma parte del comportamiento previsto, aunque se desarrollará después de la jugabilidad y los escenarios. Sus referencias en la tabla no afirman que esté implementado. No se define aquí una secuencia nueva de sonidos al reiniciar o terminar.

## Flow Diagram

```text
[AwaitingStart]
  -- NameProvided --------------------------------> [AwaitingStart]
       Keep the supplied name and wait for play or Space.
  -- StartRequested [no name] ---------------------> [Playing]
       Generate player_YYYYMMDD_HHmmss_SSS and start immediately.
  -- StartRequested [name provided] --------------> [Playing]
       Use the supplied name and start.

[Playing]
  -- MovementContinues [no state-changing event] -> [Playing]
  -- DirectionRequested --------------------------> [Playing]
  -- FoodConsumed --------------------------------> [Playing]
       Add points, grow one block and check level progress.
  -- LevelAdvance [threshold reached; next level] -> [Playing]
       Advance within the five levels; increase speed and change scenery.
  -- Collision [remaining lives > 0] -------------> [Playing]
       Lose one life; restart and resume automatically.
  -- Collision [remaining lives = 0] -------------> [Results]
       Show player name, score, level and speed.
  -- FinalLevelCompleted -------------------------> [Pending decision]
       Completion condition and outcome are not defined.

HighscoreRecording:
  Origin, destination and access point: Pending decision.
  Confirmed constraint: record the highscore by level and show the top 10.
```

Las condiciones `remaining lives > 0` y `remaining lives = 0` se evalúan después de descontar la vida por la colisión. La rama de highscore no supone que el registro ocurra antes o después de `Results`: esa conexión permanece abierta. Tampoco se añade una acción para volver a jugar desde los resultados.

## Open Questions & Proposals

**Game rules**

- Cuántos puntos otorga cada comida.
- Velocidad inicial e incremento al avanzar de nivel.
- Qué datos se conservan o reinician tras perder una vida. La reanudación automática está definida en S4.
- Dificultad y escenario de cada nivel, condición para completar el quinto y qué sucede después.
- Reglas detalladas para validar un nombre escrito y referencia horaria del nombre automático. El formato `player_YYYYMMDD_HHmmss_SSS` ya está definido y no promete unicidad.

**Highscore flow**

- En qué momento se registra un resultado y desde dónde se consulta el top 10.
- Cómo se interpreta el registro por nivel, cómo se resuelven los empates, dónde se guarda y durante cuánto tiempo.

**Compatibility**

- Dispositivos compatibles y posible soporte de teléfonos, tabletas y controles táctiles.
- Tamaño mínimo de ventana y cómo comprobar su adaptación en computadora.

**Unapproved features**

- Skins, tienda de ítems y compartir resultados siguen siendo posibilidades por decidir, no transiciones confirmadas ni compromisos para otra versión.
- Guardar y retomar partidas y el modo multijugador están fuera del MVP según S5; por eso no aparecen como ramas del flujo.

Estas preguntas pueden permanecer abiertas y evolucionar con decisiones explícitas o evidencia del proyecto. El documento no autoriza resolverlas por suposición ni modificar la idea original.
