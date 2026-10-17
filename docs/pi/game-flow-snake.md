# Snake Game Flow

## Game

Este documento describe el recorrido de una partida de Snake: cómo comienza, qué sucede mientras se juega, cómo termina por victoria o al agotarse las vidas y cómo se prepara una nueva partida. La tabla y el diagrama representan el mismo flujo. Los nombres de estados y eventos están en inglés; las explicaciones están en español.

**Source:** [Idea inicial: juego de Snake](idea-proyecto-snake.md).

**Template:** [Game Flow Template](game-flow-template.md).

Las referencias de la tabla corresponden a estas secciones de la idea:

- **S1:** «1. Qué quiere construir»: navegador web, TypeScript y modo historia de cinco niveles con dificultad creciente y cambio de escenario.
- **S3:** «3. Qué necesidad o experiencia quiere atender»: presentación del juego y resultados al finalizar.
- **S4:** «4. Qué comportamientos considera indispensables»: inicio, controles, movimiento, comida, progreso, vidas, escenarios, highscore y sonido.
- **S5:** «5. Qué quedará fuera de la primera versión»: sin guardar y retomar partidas ni modo multijugador; se mantiene el highscore.
- **S6:** «6. Qué todavía no sabe decidir»: reglas y funciones que siguen abiertas.

El inicio y el reinicio se rigen por estas reglas de la sección S4:

- **Player name:** se puede indicar un nombre antes de iniciar. Activar `play` o pulsar Enter desde el campo de nombre inicia la partida. Escribir «dark angel», incluidos sus espacios, no la inicia; espacio deja de ser un atajo global de inicio. Si no se ha indicado un nombre, se genera `player_YYYYMMDD_HHmmss_SSS` con la fecha, la hora y tres dígitos de milisegundos del momento de inicio, y la partida comienza sin pedir otra acción. Por ejemplo: `player_20261015_173025_482`. No se usa aleatoriedad ni se garantiza unicidad; es un nombre visible de la partida, no un identificador único. La referencia horaria y la validación detallada de los nombres escritos siguen pendientes.
- **Automatic restart:** si una colisión consume una vida y todavía quedan otras, la partida se reinicia y el movimiento se reanuda automáticamente. No se vuelve a pedir `play` ni Enter. Qué datos se conservan o reinician sigue pendiente.
- **New game:** desde el top 10, «Nueva partida» vuelve al inicio y espera `play` o Enter desde el campo de nombre, sin iniciar el movimiento. El nombre escrito por el jugador queda precargado y editable; se puede conservar, cambiar o borrar. Si la partida anterior usó un nombre automático, no se reutiliza y el campo vuelve vacío; si no se escribe otro nombre, se genera uno al iniciar. La misma política se aplica al regreso automático al inicio por no clasificar. Una nueva partida no arrastra el estado de juego anterior; no es el reinicio automático tras perder una vida con vidas restantes.

**Entry focus:** en cada entrada al inicio (`AwaitingStart`), tanto al abrir el juego como al regresar desde `Highscores` o por no clasificar, se coloca el foco en el campo de nombre. El indicador de foco es visible; recibirlo no cambia el contenido del campo ni inicia la partida. Tab permite pasar a «play» y el foco no se recupera continuamente mientras el jugador navega. Con el campo vacío, Enter inicia con el nombre automático ya definido. Es una regla de entrada al inicio, no del reinicio automático por perder una vida.

Los estados describen situaciones del juego, no pantallas ni diseños de interfaz:

- `AwaitingStart`: se espera la acción de inicio; indicar un nombre es opcional.
- `Playing`: la serpiente se mueve y el jugador puede dirigirla.
- `Results`: la partida terminó por agotarse las vidas y se muestran sus resultados.
- `Victory`: la partida terminó al completar los cinco niveles y se muestran sus resultados.
- `Highscores`: se muestra la pantalla del top 10 tras registrar un resultado que clasifica.

`Results` muestra la animación de «game over» y `Victory` la de victoria. En ambos casos se muestran nombre, puntaje, nivel y velocidad; después de cinco segundos se redirige según la clasificación. Si hay menos de diez entradas, el resultado clasifica incluso con cero puntos. Con diez entradas, solo clasifica un puntaje estrictamente mayor al del último; un empate no lo desplaza. Estas reglas no deciden cómo se organiza el registro por nivel ni cómo se ordenan los empates entre entradas admitidas.

`Pending decision` es una marca de información faltante, no un estado que el juego deba implementar. No implica pausar, terminar o continuar la partida de una forma que todavía no se haya acordado.

## States & Transitions

| Current state | Action or event | Condition | Game response | Next state | Source or open question |
| --- | --- | --- | --- | --- | --- |
| `AwaitingStart` | `NameProvided` — indicar el nombre | Todavía no se ha solicitado el inicio | Conservar el nombre escrito, incluidos sus espacios, y esperar `play` o Enter desde el campo de nombre | `AwaitingStart` | S4. Validación detallada: S6 |
| `AwaitingStart` | `StartRequested` — activar `play` o pulsar Enter desde el campo de nombre | No se ha indicado un nombre | Generar `player_YYYYMMDD_HHmmss_SSS` e iniciar con tres vidas y una serpiente de tres bloques que avanza automáticamente en horizontal; mostrar puntaje, vidas y velocidad; reproducir el sonido de inicio y la música suave en bucle | `Playing` | S4. Referencia horaria y velocidad inicial: S6 |
| `AwaitingStart` | `StartRequested` — activar `play` o pulsar Enter desde el campo de nombre | Hay un nombre indicado | Usar el nombre escrito e iniciar con tres vidas y una serpiente de tres bloques que avanza automáticamente en horizontal; mostrar puntaje, vidas y velocidad; reproducir el sonido de inicio y la música suave en bucle | `Playing` | S4. Velocidad inicial: S6 |
| `Playing` | `MovementContinues` — transcurre el movimiento | No ocurre una colisión ni otro evento de cambio | Continuar el desplazamiento automático | `Playing` | S4 |
| `Playing` | `DirectionRequested` — pulsar una flecha | La partida está en curso | Dirigir la serpiente con las flechas del teclado | `Playing` | S4. No se añaden reglas de giro que no estén definidas |
| `Playing` | `FoodConsumed` — comer un bloque | La serpiente consume comida | Sumar puntos, crecer un bloque, actualizar el puntaje y reproducir `coin`; comprobar si corresponde subir de nivel | `Playing` | S4. Puntos por comida: S6 |
| `Playing` | `LevelAdvance` — corresponde subir de nivel | Se cumple el umbral de 15 puntos y queda un nivel siguiente entre los cinco previstos | Subir de nivel, aumentar la velocidad y cambiar el escenario con mayor dificultad | `Playing` | S1; S4. Incremento de velocidad y escenarios concretos: S6 |
| `Playing` | `Collision` — chocar con un muro o con el propio cuerpo | Tras descontar una vida todavía quedan otras | Actualizar las vidas, reproducir `explosion`, reiniciar la partida y reanudar el movimiento automáticamente | `Playing` | S4. Puntaje, nivel, velocidad y demás datos tras el reinicio: S6 |
| `Playing` | `Collision` — chocar con un muro o con el propio cuerpo | Se pierde la última vida | Terminar la partida, mostrar nombre, puntaje, nivel y velocidad, e iniciar la animación de «game over»; los sonidos de pérdida de vida y `game over` no tienen un orden fijado | `Results` | S3; S4 |
| `Playing` | `FinalLevelCompleted` — completar el quinto nivel | Se completa el quinto nivel; la condición concreta sigue pendiente | Terminar la partida, mostrar nombre, puntaje, nivel y velocidad, e iniciar la animación de victoria | `Victory` | S1; S3; S4. Condición de finalización: S6 |
| `Results` | `AnimationFinished` — finalizar la animación | Han transcurrido 5 segundos y hay menos de diez entradas | Registrar el resultado, incluso con cero puntos, y mostrar el top 10 | `Highscores` | S4 |
| `Results` | `AnimationFinished` — finalizar la animación | Han transcurrido 5 segundos, hay diez entradas y el puntaje es estrictamente mayor al del último | Registrar el resultado, retirar el desplazado y mostrar como máximo diez entradas | `Highscores` | S4 |
| `Results` | `AnimationFinished` — finalizar la animación | Han transcurrido 5 segundos, hay diez entradas y el puntaje es menor o igual al del último | No registrar el resultado y volver al menú de inicio | `AwaitingStart` | S4 |
| `Victory` | `AnimationFinished` — finalizar la animación | Han transcurrido 5 segundos y hay menos de diez entradas | Registrar el resultado, incluso con cero puntos, y mostrar el top 10 | `Highscores` | S4 |
| `Victory` | `AnimationFinished` — finalizar la animación | Han transcurrido 5 segundos, hay diez entradas y el puntaje es estrictamente mayor al del último | Registrar el resultado, retirar el desplazado y mostrar como máximo diez entradas | `Highscores` | S4 |
| `Victory` | `AnimationFinished` — finalizar la animación | Han transcurrido 5 segundos, hay diez entradas y el puntaje es menor o igual al del último | No registrar el resultado y volver al menú de inicio | `AwaitingStart` | S4 |
| `Highscores` | `NewGameRequested` — pulsar «Nueva partida» | El jugador solicita una nueva partida desde el top 10 | Volver al inicio sin iniciar el movimiento; dejar el nombre escrito precargado y editable, sin reutilizar el automático; esperar `play` o Enter desde el campo de nombre y no arrastrar el estado de juego anterior | `AwaitingStart` | S4 |

En los tres regresos a `AwaitingStart` se aplican las políticas **New game** y **Entry focus**: conservar solo el nombre escrito por el jugador, permitir editarlo o borrarlo, no reutilizar el automático y esperar `play` o Enter desde el campo de nombre. El campo queda vacío si no hay un nombre escrito y recibe el foco sin cambiar su contenido. Volver al inicio no arranca la nueva partida.

Los eventos de comida y avance de nivel pueden relacionarse: la tabla no establece una prioridad de procesamiento ni inventa cuántos puntos da cada comida. Del mismo modo, la transición de colisión confirma el reinicio automático, pero no supone que se conserven o se pierdan datos todavía no decididos.

El audio forma parte del comportamiento previsto, aunque se desarrollará después de la jugabilidad y los escenarios. Sus referencias en la tabla no afirman que esté implementado. No se define aquí una secuencia nueva de sonidos al reiniciar o terminar.

## Flow Diagram

```text
[AwaitingStart]
  Entry: focus the name field without changing its content or starting the game.
  -- NameProvided --------------------------------> [AwaitingStart]
       Keep the supplied name, including spaces; wait for play or Enter in the name field.
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
       Show player name, score, level and speed; start Game Over animation.
  -- FinalLevelCompleted -------------------------> [Victory]
       Show player name, score, level and speed; start victory animation.
       The condition for completing level five remains open.

[Results] or [Victory]
  -- AnimationFinished [after 5 seconds; fewer than 10 entries]
       Record the result, even zero points. ------------> [Highscores]
  -- AnimationFinished [after 5 seconds; 10 entries; score > last score]
       Replace the last entry, retaining at most 10. ---> [Highscores]
  -- AnimationFinished [after 5 seconds; 10 entries; score <= last score]
       Do not record the result. ----------------------> [AwaitingStart]

[Highscores]
  -- NewGameRequested [button "Nueva partida"] ----> [AwaitingStart]
       Prefill only the user-supplied name; allow edits or clearing.
       Do not reuse the generated name or carry prior gameplay state.
       Wait for play or Enter in the name field; generate a name at start if none is supplied.

All returns to AwaitingStart use the same name policy.
```

Las condiciones `remaining lives > 0` y `remaining lives = 0` se evalúan después de descontar la vida por la colisión. Las redirecciones tras cinco segundos son automáticas; no requieren un botón de continuar. «Nueva partida» sale de `Highscores` solo cuando el jugador lo pulsa, después de cualquiera de los dos finales. No se añade una acción para volver a jugar directamente desde los resultados ni un acceso al top 10 desde el menú.

## Open Questions & Proposals

**Game rules**

- Cuántos puntos otorga cada comida.
- Velocidad inicial e incremento al avanzar de nivel.
- Qué datos se conservan o reinician tras perder una vida. La reanudación automática está definida en S4.
- Dificultad y escenario de cada nivel y condición para completar el quinto. Su desenlace de victoria ya está definido.
- Reglas detalladas para validar un nombre escrito y referencia horaria del nombre automático. El formato `player_YYYYMMDD_HHmmss_SSS` ya está definido y no promete unicidad.

**Highscore flow**

- Cómo se interpreta el registro por nivel, cómo se ordenan empates entre resultados admitidos, dónde se guarda y durante cuánto tiempo. El empate con el último de una lista llena no permite ingresar.

**Compatibility**

- Dispositivos compatibles y posible soporte de teléfonos, tabletas y controles táctiles.
- Tamaño mínimo de ventana y cómo comprobar su adaptación en computadora.

**Unapproved features**

- Skins, tienda de ítems y compartir resultados siguen siendo posibilidades por decidir, no transiciones confirmadas ni compromisos para otra versión.
- Guardar y retomar partidas y el modo multijugador están fuera del MVP según S5; por eso no aparecen como ramas del flujo.

Estas preguntas pueden permanecer abiertas y evolucionar con decisiones explícitas o evidencia del proyecto. El documento no autoriza resolverlas por suposición ni modificar la idea original.
