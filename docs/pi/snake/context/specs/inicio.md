# Especificación: Inicio (primera entrega funcional)

Define la **primera entrega funcional**: la pantalla de Inicio operativa. Está **definida, no implementada**. No se afirma que exista código, compilación ni arranque real de la aplicación.

Esta especificación describe **comportamiento observable** de la pantalla de Inicio. Las reglas del juego completo viven en la [idea](../../../idea-proyecto-snake.md) y el [flujo](../../../game-flow-snake.md); aquí no se duplican.

## Alcance de la entrega

- Mostrar la pantalla de **Inicio** con el título del juego, un campo de nombre editable y un botón `play`.
- Colocar el **foco** en el campo de nombre al entrar.
- Iniciar la partida al activar `play` o pulsar **Enter** desde el campo de nombre.
- Navegar a la pantalla de **Partida**.

Las vistas estáticas del ejercicio de aula (las cinco pantallas sin jugabilidad) son una **base previa**, no parte de esta entrega funcional.

## Comportamiento observable

| Caso | Entrada | Resultado esperado |
| --- | --- | --- |
| Entrada inicial | Abrir la pantalla de Inicio | El campo de nombre recibe el foco con un indicador visible, sin cambiar su contenido ni iniciar la partida |
| Sin nombre | Activar `play` con el campo vacío | Se genera `player_YYYYMMDD_HHmmss_SSS` y se inicia la transición a Partida |
| Con nombre | Escribir un nombre y activar `play` | Se usa el nombre escrito y se inicia la transición a Partida |
| Enter desde el campo | Pulsar Enter con el campo de nombre enfocado | Inicia igual que `play` |
| Espacios | Escribir «dark angel» | No inicia la partida; los espacios no son un atajo de inicio |
| Teclado | Pulsar Tab desde el campo de nombre | Mueve el foco al botón `play` |

## Fuera de esta entrega

- **Movimiento de la serpiente:** en esta entrega la navegación llega a Partida, pero la serpiente **no se mueve todavía**.
- Puntaje, vidas, niveles, comida, escenarios, ranking y audio.
- Almacenamiento de cualquier tipo y publicación.

El [flujo](../../../game-flow-snake.md) define que, en el juego completo, el inicio conduce a `Playing` con movimiento automático. Esta entrega intermedia **no cambia** ese flujo: es un paso previo y acotado.

## Pendientes que afectan a esta entrega

- **Validación detallada de nombres** y **referencia horaria** del nombre automático. Las decide la persona responsable del proyecto; la fase afectada está en [ROADMAP.md](../ROADMAP.md).

## Referencias

- [Idea inicial](../../../idea-proyecto-snake.md)
- [Recorrido de una partida](../../../game-flow-snake.md)
- [Notas por pantalla](../../design/screens.md)
- [Contexto del proyecto](../README.md)
