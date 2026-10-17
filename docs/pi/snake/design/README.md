# Wireframes de Snake (propuesta de diseño)

Bocetos en escala de grises de las pantallas del juego Snake. Son una **propuesta de diseño revisada y aprobada**: la disposición está acordada, pero no son un diseño visual final ni una implementación del juego. El lenguaje visual cuenta ahora con un [borrador de fase 1](visual-style.md); sus tokens no están aprobados todavía. En una ronda de revisión se acordaron refinamientos de componentes (radio de 8 px en botones y campo de nombre, estados de botón con inversión de color y foco separado, serpiente como tubo continuo y ranking sin cuadrícula) y se eligió la fuente pixelada **Silkscreen**, que cierra la revisión de tipografía. El siguiente paso acordado es la **pantalla piloto de Inicio**, todavía no creada; la paleta, los tamaños, la integración local de la fuente y el estilo visual final siguen pendientes.

## Cómo abrir la galería

1. Abre `docs/pi/snake/design/index.html` en un navegador (doble clic o «Abrir con»).
2. Opcional: sírvelo localmente desde la raíz del repositorio con `python3 -m http.server` y visita la ruta del archivo.

La galería de wireframes no requiere dependencias, JavaScript ni recursos externos. La hoja `style-sheet.html` sí solicita temporalmente a Google Fonts la fuente ya elegida, **Silkscreen** (400 y 700), para mostrarla en V2: esa muestra requiere conexión y usa un script local solo para avisar de la carga; el resto de la hoja sigue disponible sin conexión. No se guardan archivos de fuentes en el proyecto; la integración local (licencia, `@font-face` y renderizado sin conexión) es una tarea de construcción pendiente.

El inicio acordado es activar «play» o pulsar Enter desde el campo de nombre. Se pueden escribir nombres como «dark angel» sin que sus espacios inicien la partida. Los bocetos describen esta regla, no capturan teclas ni implementan un formulario.

El campo de nombre recibe el foco en cada entrada al inicio (acceso inicial, «Nueva partida» o regreso por no clasificar), sin modificar su contenido ni iniciar la partida. El indicador de foco es visible y Tab permite pasar a «play», sin retener el foco mientras se navega. El doble contorno del campo en el boceto representa ese foco; no lo implementa en la galería.

## Qué contiene

| Archivo | Contenido |
| --- | --- |
| `index.html` | Galería local que muestra y enlaza los cinco bocetos |
| `screens.md` | Notas por pantalla: propósito, elementos, acciones, transiciones y reglas pendientes |
| `visual-style.md` | Dirección confirmada y propuesta de tokens, tipografía y componentes |
| `style-sheet.html` | Hoja local de revisión visual: muestras de tokens, tipografía (Silkscreen elegida, integración local pendiente), controles, tablero, HUD y ranking (borrador, sin aprobar; incluye los refinamientos acordados) |
| `DESIGN.md` | Guía de aplicación que referencia el lenguaje visual sin duplicar tokens |
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

Aplicar el sistema acordado a una **pantalla piloto: Inicio** y revisarla antes de extender el estilo al resto de pantallas (Partida, Game Over, Victoria y Top 10). La pantalla piloto aún no existe y usará los tokens y tamaños propuestos de [visual-style.md](visual-style.md) y su [guía de aplicación](DESIGN.md); usarlos no los aprueba. El primer punto a comprobar es el encaje del texto más largo de los botones con **Silkscreen** a tamaño real, junto con la paleta y el espaciado.

La revisión de la tipografía está cerrada con **Silkscreen** y esta documentación muestra solo esa familia. Su integración local queda pendiente de construcción: adquirir Silkscreen con su licencia OFL, configurar un `@font-face` local y retirar la dependencia de Google al preparar la base de la aplicación. La fase 1 todavía no contiene mockups, archivos de fuentes ni recursos del juego.
