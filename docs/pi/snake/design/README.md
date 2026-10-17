# Wireframes de Snake (propuesta de diseño)

Bocetos en escala de grises de las pantallas del juego Snake. Son una **propuesta pendiente de revisión humana**: no son un diseño visual final ni una implementación del juego. El color, la tipografía y el estilo visual están aplazados.

## Cómo abrir la galería

1. Abre `docs/pi/snake/design/index.html` en un navegador (doble clic o «Abrir con»).
2. Opcional: sírvelo localmente desde la raíz del repositorio con `python3 -m http.server` y visita la ruta del archivo.

No requiere instalar dependencias, ni JavaScript, ni recursos externos.

El inicio acordado es activar «play» o pulsar Enter desde el campo de nombre. Se pueden escribir nombres como «dark angel» sin que sus espacios inicien la partida. Los bocetos describen esta regla, no capturan teclas ni implementan un formulario.

El campo de nombre recibe el foco en cada entrada al inicio (acceso inicial, «Nueva partida» o regreso por no clasificar), sin modificar su contenido ni iniciar la partida. El indicador de foco es visible y Tab permite pasar a «play», sin retener el foco mientras se navega. El doble contorno del campo en el boceto representa ese foco; no lo implementa en la galería.

## Qué contiene

| Archivo | Contenido |
| --- | --- |
| `index.html` | Galería local que muestra y enlaza los cinco bocetos |
| `screens.md` | Notas por pantalla: propósito, elementos, acciones, transiciones y reglas pendientes |
| `wireframes/start.svg` | Inicio (`AwaitingStart`) |
| `wireframes/playing.svg` | Partida (`Playing`) |
| `wireframes/game-over.svg` | Game Over (`Results`) |
| `wireframes/victory.svg` | Victoria (`Victory`) |
| `wireframes/top10.svg` | Top 10 (`Highscores`) |

## Fuentes del juego

La idea y el flujo son la fuente del significado del juego; los bocetos no añaden reglas nuevas.

- [Idea inicial: juego de Snake](../../idea-proyecto-snake.md)
- [Recorrido de una partida (flujo)](../../game-flow-snake.md)

## Dimensiones y alcance

- Referencia de cada boceto: ventana de computadora de 1024 × 768.
- Escala de grises; sin color, tipografía ni estilo visual finales (aplazados).
- 1024 × 768 es una referencia de diseño, no una prueba de compatibilidad de navegadores.
- No incluye jugabilidad, recursos, sonido ni soporte táctil.
- No se duplican ni se mueven la idea ni el flujo: se enlazan desde aquí.

## Siguiente paso

Revisión humana de estos bocetos. Después de la revisión se decidirá si se aplica el estilo visual. Este paquete no introduce el estilo visual, los mockups ni sus recursos.
