# Memoria del proyecto Snake

Registro conciso de **hechos aprobados con su fuente** y de las **dudas abiertas**. No es una transcripción de conversaciones ni un historial de cambios.

## Hechos aprobados

| Hecho | Fuente |
| --- | --- |
| Juego de Snake para navegador, en TypeScript, sin versión de terminal | [idea](../../idea-proyecto-snake.md) |
| Modo historia de **cinco niveles** con dificultad creciente y cambio de escenario | [idea](../../idea-proyecto-snake.md) |
| Comida: cada bloque **suma puntos** y **hace crecer un bloque** la serpiente | [idea](../../idea-proyecto-snake.md), [flujo](../../game-flow-snake.md) |
| Progreso: cada **15 puntos** se sube un nivel y aumenta la velocidad | [idea](../../idea-proyecto-snake.md), [flujo](../../game-flow-snake.md) |
| Inicio: nombre opcional; `play` o Enter desde el campo de nombre inician; escribir el nombre no inicia | [idea](../../idea-proyecto-snake.md), [flujo](../../game-flow-snake.md) |
| Nombre automático `player_YYYYMMDD_HHmmss_SSS`, sin aleatoriedad ni unicidad garantizada | [idea](../../idea-proyecto-snake.md) |
| Tres vidas; perder una reinicia y reanuda el movimiento; perder la última termina la partida | [idea](../../idea-proyecto-snake.md), [flujo](../../game-flow-snake.md) |
| Highscore top 10: entra si hay menos de diez; con diez, solo con puntaje **estrictamente mayor** al último; un empate **no desplaza** | [idea](../../idea-proyecto-snake.md), [flujo](../../game-flow-snake.md) |
| El sonido está **incluido** y se desarrolla **después de la jugabilidad y los escenarios** | [idea](../../idea-proyecto-snake.md) |
| Cinco pilotos aceptados **solo como referencia visual**, sin juego implementado | [wireframes](../design/README.md) |

## Contexto de aula (confirmado)

- Los estudiantes crean un *starter* en clase y existen cinco vistas estáticas sin jugabilidad.
- La primera entrega funcional es la pantalla de Inicio (nombre, foco y `play`/Enter hacia Partida, sin movimiento), definida en [specs/inicio.md](specs/inicio.md).
- El objetivo de tiempo de la actividad es de **30 a 45 minutos**; **no se ha observado una duración real**.
- Estos datos describen el ejercicio de clase, **no** el propósito del producto.

## Dudas abiertas

Ninguna de estas dudas está resuelta; no se inventan respuestas. Las decide la **persona responsable del proyecto**, y la fase afectada está en [ROADMAP.md](ROADMAP.md).

- Puntos por comida; velocidad inicial e incremento por nivel.
- Datos que se conservan o reinician tras perder una vida.
- Escenarios y dificultad de cada nivel; condición para completar el quinto.
- Semántica del highscore por nivel, orden de empates iguales y almacenamiento (forma y duración).
- Validación detallada de nombres y referencia horaria del nombre automático.
- Dispositivos compatibles, tamaño mínimo de ventana y posible soporte táctil.
- Funciones opcionales por decidir: skins, tienda, compartir resultados y variantes de comida.

## Límites

Las referencias visuales **no** demuestran responsive de producción, ni validación de fuente sin conexión, ni compilaciones. El framework **no** está elegido y el arranque de la aplicación **no** se ha implementado.
