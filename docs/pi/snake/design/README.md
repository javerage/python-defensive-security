# Wireframes de Snake (propuesta de diseño)

Bocetos en escala de grises de las pantallas del juego Snake. Los cinco wireframes son una **propuesta de diseño revisada y aprobada**: su disposición está acordada, y esa aprobación es **independiente de los mockups en color**. El lenguaje visual cuenta con un [borrador de fase 1](visual-style.md). La **pantalla piloto de Inicio** (`start-pilot.html`) y la **pantalla piloto de Partida** (`playing-pilot.html`) fueron **aceptadas como referencia visual**: los valores visuales aplicados en ambas (color, tamaños y estilo) quedan aceptados como referencia, sin extender esa aceptación a los demás mockups ni a la implementación. Los refinamientos de componentes y la fuente pixelada **Silkscreen** están acordados; su integración local y el estilo final del conjunto siguen pendientes.

La pantalla piloto de **Game Over** ([`game-over-pilot.html`](game-over-pilot.html)) quedó **aceptada como referencia visual**: conserva el wireframe aprobado y aplica el acento coral del sistema, sin animación, temporizador, clasificación ni redirección. Sus valores visuales aplicados quedan aceptados como referencia, sin extender esa aceptación a la implementación. Por decisión de la persona responsable, el push queda aplazado hasta finalizar y autorizar todos los diseños; no se publica esta ronda.

La pantalla piloto de **Victoria** ([`victory-pilot.html`](victory-pilot.html)) quedó **aceptada como referencia visual**: conserva el panel y la tarjeta aprobados, con acento verde `snake`, nivel y velocidad ilustrativos de 5. No ejecuta animación, clasificación, temporizador ni redirección. Sus valores visuales aplicados quedan aceptados como referencia, sin extender esa aceptación a la implementación. La condición para completar el quinto nivel sigue pendiente.

La pantalla piloto de **Top 10** ([`top10-pilot.html`](top10-pilot.html)) quedó **aceptada como referencia visual**: conserva las diez filas ilustrativas y la geometría del wireframe aprobado; ranking sin cuadrícula de celdas y un único botón «Nueva partida», con estados visuales pero sin navegación, almacenamiento ni inicio de partidas. Sus valores visuales aplicados quedan aceptados como referencia, sin extender esa aceptación a la implementación. El registro por nivel y el orden entre empates iguales siguen pendientes.

En la ronda actual, la pantalla piloto de Partida se actualizó: las **vidas** se muestran como **tres corazones pixelados** de posiciones fijas —llenos para las vidas disponibles y de contorno para las perdidas—, y se corrigió el aviso al pie (`.scene-note`) para que no desborde el marco inferior del panel. Ambos cambios están construidos en la pantalla piloto, que quedó **aceptada como referencia visual** con ellos incluidos. La comida sigue representada por un **único rombo ilustrativo**; las variantes de comida (formas, colores o efectos) **no están definidas ni se muestran en el mockup** y se registran como posibilidad abierta en la [idea inicial del proyecto](../../idea-proyecto-snake.md).

## Cómo abrir la galería y las pantallas piloto

1. Abre `docs/pi/snake/design/index.html` en un navegador (doble clic o «Abrir con»).
2. Opcional: sírvelo localmente desde la raíz del repositorio con `python3 -m http.server` y visita la ruta del archivo.
3. La **pantalla piloto de Inicio** está en `docs/pi/snake/design/start-pilot.html`: ábrela igual, con doble clic o «Abrir con». Está **aceptada como referencia visual**; sus valores visuales aplicados quedan aceptados como referencia y su aplicación al resto de mockups se revisará después.
4. La **pantalla piloto de Partida** está en `docs/pi/snake/design/playing-pilot.html`: ábrela igual, con doble clic o «Abrir con». Está **aceptada como referencia visual**; sus valores visuales aplicados quedan aceptados como referencia.
5. La **pantalla piloto de Game Over** está en `docs/pi/snake/design/game-over-pilot.html`: ábrela igual. Está **aceptada como referencia visual**; no se redirige al esperar cinco segundos.
6. La **pantalla piloto de Victoria** está en `docs/pi/snake/design/victory-pilot.html`: ábrela igual. Está **aceptada como referencia visual**; permanece estática incluso después de cinco segundos.

7. La **pantalla piloto de Top 10** está en `docs/pi/snake/design/top10-pilot.html`: ábrela igual. Está **aceptada como referencia visual**; el botón no navega ni inicia partidas.

La galería de wireframes no requiere dependencias, JavaScript ni recursos externos. La hoja `style-sheet.html` y los cinco pilotos (`start-pilot.html`, `playing-pilot.html`, `game-over-pilot.html`, `victory-pilot.html` y `top10-pilot.html`) sí solicitan temporalmente a Google Fonts la fuente ya elegida, **Silkscreen** (400 y 700): esas muestras requieren conexión y usan un script local solo para avisar de la carga. Si la carga no se confirma, cada página muestra un sustituto monoespaciado y avisa de que no debe juzgarse como la fuente real; el resto del contenido sigue disponible sin conexión. No se guardan archivos de fuentes en el proyecto; la integración local (licencia, `@font-face` y renderizado sin conexión) es una tarea de construcción pendiente.

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
| `game-over-pilot.html` | Game Over (`Results`), aceptada como referencia visual: resumen ilustrativo, sin botones, animación ni redirección activa |
| `tests/game-over-pilot.test.cjs` | Contrato estático, estados de carga de la fuente y sincronización documental de Game Over |
| `tests/game-over-pilot.browser.test.cjs` | Chrome/CDP: geometría, texto sin solapamientos y permanencia de la referencia después de cinco segundos |
| `victory-pilot.html` | Victoria (`Victory`), aceptada como referencia visual: resumen con acento verde, nivel y velocidad ilustrativos de 5; sin botones, animación ni redirección activa |
| `tests/victory-pilot.test.cjs` | Contrato estático de Victoria, carga de fuente y sincronización documental |
| `tests/victory-pilot.browser.test.cjs` | Chrome/CDP: geometría, acento verde, textos y nota de condición pendiente sin solapamiento; permanencia después de cinco segundos |
| `wireframes/start.svg` | Inicio (`AwaitingStart`) |
| `wireframes/playing.svg` | Partida (`Playing`) |
| `wireframes/game-over.svg` | Game Over (`Results`) |
| `wireframes/victory.svg` | Victoria (`Victory`) |
| `wireframes/top10.svg` | Top 10 (`Highscores`) |
| `top10-pilot.html` | Top 10 (`Highscores`), **aceptada como referencia visual**: diez resultados ilustrativos, tabla sin cuadrícula y botón de muestra «Nueva partida» |
| `tests/top10-pilot.test.cjs` | Contrato de Top 10, diez filas del wireframe, fuente y sincronización de guías |
| `tests/top10-pilot.browser.test.cjs` | Chrome/CDP: geometría, textos sin solapamiento, estados del botón y ausencia de navegación o escritura |

## Pruebas

Las pruebas de regresión documental se ejecutan con Node.js (sin dependencias externas):

```bash
node --test docs/pi/snake/design/tests/style-sheet.test.cjs
node --test docs/pi/snake/design/tests/start-pilot.test.cjs
node --test docs/pi/snake/design/tests/playing-pilot.test.cjs
node --test docs/pi/snake/design/tests/game-over-pilot.test.cjs
node --test docs/pi/snake/design/tests/victory-pilot.test.cjs
node --test docs/pi/snake/design/tests/top10-pilot.test.cjs
```

Regresión completa (once archivos):

```bash
node --test docs/pi/tests/game-flow-snake.test.cjs docs/pi/snake/design/tests/style-sheet.test.cjs docs/pi/snake/design/tests/start-pilot.test.cjs docs/pi/snake/design/tests/playing-pilot.test.cjs docs/pi/snake/design/tests/playing-pilot.browser.test.cjs docs/pi/snake/design/tests/game-over-pilot.test.cjs docs/pi/snake/design/tests/game-over-pilot.browser.test.cjs docs/pi/snake/design/tests/victory-pilot.test.cjs docs/pi/snake/design/tests/victory-pilot.browser.test.cjs docs/pi/snake/design/tests/top10-pilot.test.cjs docs/pi/snake/design/tests/top10-pilot.browser.test.cjs
```

### Prueba opcional de navegador

`docs/pi/snake/design/tests/top10-pilot.browser.test.cjs` comprueba las cajas de la tabla y el botón, las diez filas, el encaje de nombres largos y los estados normal, hover, pulsado y foco de teclado. También confirma que pulsar «Nueva partida» con ratón o Enter no navega ni escribe en el almacenamiento del navegador. Es una muestra visual, no una integración del flujo del juego.

`docs/pi/snake/design/tests/playing-pilot.browser.test.cjs` comprueba el layout real —el encaje del aviso al pie y los tres corazones de las vidas— con Chrome o Chromium headless vía CDP; eso no se puede afirmar con expresiones regulares sobre el HTML.

`docs/pi/snake/design/tests/game-over-pilot.browser.test.cjs` comprueba las cajas del panel y del resumen, la separación de los textos y que la referencia no navegue después de cinco segundos. `docs/pi/snake/design/tests/victory-pilot.browser.test.cjs` comprueba lo mismo en Victoria, además del acento verde y de la nota sobre la condición pendiente. Las pruebas de navegador bloquean Google Fonts para medir sin red con el sustituto; no certifican el encaje con Silkscreen real ni sustituyen la revisión visual de la persona responsable.

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

La **pantalla piloto de Inicio** (`start-pilot.html`) y la **pantalla piloto de Partida** (`playing-pilot.html`) quedaron **aceptadas como referencia visual**, la **pantalla piloto de Game Over** ([`game-over-pilot.html`](game-over-pilot.html)) también quedó **aceptada como referencia visual**, la **pantalla piloto de Victoria** ([`victory-pilot.html`](victory-pilot.html)) quedó **aceptada como referencia visual** y la **pantalla piloto de Top 10** ([`top10-pilot.html`](top10-pilot.html)) también quedó **aceptada como referencia visual** con sus valores visuales aplicados. Con los cinco pilotos aceptados como referencia visual, el siguiente paso es que la persona responsable autorice la construcción del juego. Los valores visuales aplicados en las cinco pantallas aceptadas quedan aceptados como referencia y no se extienden a la implementación, según [visual-style.md](visual-style.md) y la [guía de aplicación](DESIGN.md). La escena y los datos son ilustrativos, no reglas ni resultados reales del juego. El encaje del HUD y de las cifras de Partida con **Silkscreen** ya se comprobó a 1024 × 768 en Chrome. El encaje responsive, cross-browser y de producción queda para fases posteriores.

La revisión de la tipografía está cerrada con **Silkscreen** y esta documentación muestra solo esa familia. Su integración local queda pendiente de construcción: adquirir Silkscreen con su licencia OFL, configurar un `@font-face` local y retirar la dependencia de Google al preparar la base de la aplicación. La división de las pantallas en componentes es trabajo de la fase de construcción, no de este paso: por ahora los mockups son archivos HTML estáticos y no se han extraído componentes. El paquete ya incluye los cinco pilotos: Inicio, Partida, Game Over, Victoria y Top 10 están aceptados como referencia visual. Los archivos de fuentes y los recursos del juego siguen pendientes de creación.
