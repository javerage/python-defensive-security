# Wireframes de Snake (propuesta de diseño)

Bocetos en escala de grises de las pantallas del juego Snake. Los cinco wireframes son una **propuesta de diseño revisada y aprobada**: su disposición está acordada, y esa aprobación es **independiente de los mockups en color**. El lenguaje visual cuenta con un [borrador de fase 1](visual-style.md); los valores visuales aplicados en las pantallas piloto ya aceptadas quedan como referencia y su aplicación al resto sigue pendiente. En una ronda de revisión se acordaron refinamientos de componentes (radio de 8 px en botones y campo de nombre, estados de botón con inversión de color y foco separado, serpiente como tubo continuo y ranking sin cuadrícula) y se eligió la fuente pixelada **Silkscreen**, que cierra la revisión de tipografía. La **pantalla piloto de Inicio** (`start-pilot.html`) y la **pantalla piloto de Partida** (`playing-pilot.html`) fueron **aceptadas como referencia visual** por la persona responsable: los valores visuales aplicados en ambas (color, tamaños y estilo) quedan aceptados como referencia, sin que esa aceptación se extienda a los demás mockups ni a la implementación. El siguiente paso acordado es el mockup de **Game Over** —planificado y todavía no creado—, antes de Victoria y Top 10. La extensión de esos valores al resto de mockups, la integración local de la fuente y el estilo visual final del conjunto siguen pendientes.

En la ronda actual, la pantalla piloto de Partida se actualizó: las **vidas** se muestran como **tres corazones pixelados** de posiciones fijas —llenos para las vidas disponibles y de contorno para las perdidas—, y se corrigió el aviso al pie (`.scene-note`) para que no desborde el marco inferior del panel. Ambos cambios están construidos en la pantalla piloto, que quedó **aceptada como referencia visual** con ellos incluidos. La comida sigue representada por un **único rombo ilustrativo**; las variantes de comida (formas, colores o efectos) **no están definidas ni se muestran en el mockup** y se registran como posibilidad abierta en la [idea inicial del proyecto](../../idea-proyecto-snake.md).

## Cómo abrir la galería y las pantallas piloto

1. Abre `docs/pi/snake/design/index.html` en un navegador (doble clic o «Abrir con»).
2. Opcional: sírvelo localmente desde la raíz del repositorio con `python3 -m http.server` y visita la ruta del archivo.
3. La **pantalla piloto de Inicio** está en `docs/pi/snake/design/start-pilot.html`: ábrela igual, con doble clic o «Abrir con». Está **aceptada como referencia visual**; sus valores visuales aplicados quedan aceptados como referencia y su aplicación al resto de mockups se revisará después.
4. La **pantalla piloto de Partida** está en `docs/pi/snake/design/playing-pilot.html`: ábrela igual, con doble clic o «Abrir con». Está **aceptada como referencia visual**; el siguiente punto a revisar es el mockup de Game Over, antes de Victoria y Top 10.

La galería de wireframes no requiere dependencias, JavaScript ni recursos externos. La hoja `style-sheet.html` y las pantallas piloto `start-pilot.html` y `playing-pilot.html` sí solicitan temporalmente a Google Fonts la fuente ya elegida, **Silkscreen** (400 y 700): esas muestras requieren conexión y usan un script local solo para avisar de la carga. Si la carga no se confirma, cada página muestra un sustituto monoespaciado y avisa de que no debe juzgarse como la fuente real; el resto del contenido sigue disponible sin conexión. No se guardan archivos de fuentes en el proyecto; la integración local (licencia, `@font-face` y renderizado sin conexión) es una tarea de construcción pendiente.

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
| `start-pilot.html` | Pantalla piloto de Inicio: aplica el borrador visual con los valores propuestos; **aceptada como referencia visual** (sus valores visuales aplicados quedan aceptados como referencia) |
| `playing-pilot.html` | Pantalla piloto de Partida: aplica el borrador visual con datos y escena ilustrativos; vidas como tres corazones pixelados y aviso al pie corregido; **aceptada como referencia visual** (sus valores visuales aplicados quedan aceptados como referencia) |
| `tests/playing-pilot.browser.test.cjs` | Prueba opcional de navegador real (Chrome/CDP): mide el encaje del aviso al pie y los tres corazones; se omite si no hay Chrome instalado |
| `wireframes/start.svg` | Inicio (`AwaitingStart`) |
| `wireframes/playing.svg` | Partida (`Playing`) |
| `wireframes/game-over.svg` | Game Over (`Results`) |
| `wireframes/victory.svg` | Victoria (`Victory`) |
| `wireframes/top10.svg` | Top 10 (`Highscores`) |

## Pruebas

Las pruebas de regresión documental se ejecutan con Node.js (sin dependencias externas):

```bash
node --test docs/pi/snake/design/tests/style-sheet.test.cjs
node --test docs/pi/snake/design/tests/start-pilot.test.cjs
node --test docs/pi/snake/design/tests/playing-pilot.test.cjs
```

Regresión completa (cinco archivos):

```bash
node --test docs/pi/tests/game-flow-snake.test.cjs docs/pi/snake/design/tests/style-sheet.test.cjs docs/pi/snake/design/tests/start-pilot.test.cjs docs/pi/snake/design/tests/playing-pilot.test.cjs docs/pi/snake/design/tests/playing-pilot.browser.test.cjs
```

### Prueba opcional de navegador

`docs/pi/snake/design/tests/playing-pilot.browser.test.cjs` comprueba el layout real —el encaje del aviso al pie y los tres corazones de las vidas— con Chrome o Chromium headless vía CDP; eso no se puede afirmar con expresiones regulares sobre el HTML.

- **Requisitos:** Node.js con `fetch` y `WebSocket` globales (Node 22 o superior recomendado; esta ronda se ejecutó con Node 26) y Google Chrome o Chromium instalado.
- **Ruta de Chrome:** se detecta en las ubicaciones habituales; también se puede indicar con la variable de entorno `CHROME_PATH`.
- **Sin Chrome:** la comprobación **se omite** (`skip`) y no se marca como aprobada; no se finge un resultado.
- **Sin dependencias nuevas:** usa solo módulos de Node y el navegador ya instalado; no añade paquetes npm.

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

La **pantalla piloto de Inicio** (`start-pilot.html`) y la **pantalla piloto de Partida** (`playing-pilot.html`) quedaron **aceptadas como referencia visual**. El siguiente paso acordado es el mockup de **Game Over** —planificado y todavía no creado—, antes de Victoria y Top 10. La Partida usa los tokens y tamaños de [visual-style.md](visual-style.md) y su [guía de aplicación](DESIGN.md); los valores visuales aplicados en Inicio y Partida quedan aceptados como referencia, su escena y sus datos son ilustrativos, no reglas reales del juego, y su aplicación a los demás mockups y a la implementación se revisará en esas fases. El encaje del HUD y de las cifras con **Silkscreen** ya se comprobó a 1024 × 768 en Chrome. El encaje responsive, cross-browser y de producción queda para fases posteriores, fuera de esta revisión del piloto. El estilo se extenderá al resto de mockups en los siguientes pasos de diseño.

La revisión de la tipografía está cerrada con **Silkscreen** y esta documentación muestra solo esa familia. Su integración local queda pendiente de construcción: adquirir Silkscreen con su licencia OFL, configurar un `@font-face` local y retirar la dependencia de Google al preparar la base de la aplicación. La división de las pantallas en componentes es trabajo de la fase de construcción, no de este paso: por ahora los mockups son archivos HTML estáticos y no se han extraído componentes. El paquete de diseño ya incluye las pantallas piloto de Inicio y Partida además de los wireframes y la hoja de revisión; la colección completa de mockups del resto de pantallas, los archivos de fuentes y los recursos del juego siguen pendientes.
