# Lenguaje visual de Snake — fase 1

**Estado:** dirección confirmada; los valores visuales aplicados en las pantallas piloto ya aceptadas quedan como referencia y el resto de tokens y componentes sigue en borrador. Los cinco wireframes están aprobados. En la ronda actual se acordaron refinamientos concretos de componentes (radio, estados de botón, forma de la serpiente y ranking) y se eligió la fuente pixelada **Silkscreen**, con lo que la revisión de tipografía queda cerrada. La **pantalla piloto de Inicio** ([`start-pilot.html`](start-pilot.html)), la **pantalla piloto de Partida** ([`playing-pilot.html`](playing-pilot.html)) y la **pantalla piloto de Game Over** ([`game-over-pilot.html`](game-over-pilot.html)) quedaron **aceptadas como referencia visual**; los valores visuales aplicados en las tres (color, tamaños y estilo) quedan aceptados como referencia, sin que esa aceptación se extienda a los demás mockups ni a la implementación. La Partida reutiliza este lenguaje visual y **no** copia la disposición de Inicio como layout de todas las pantallas. Los códigos hexadecimales y los tamaños quedan aceptados como referencia en esas tres pantallas y su aplicación al resto sigue propuesta; la integración local de la fuente queda pendiente de construcción. Este documento no rediseña los wireframes, no implementa el juego, no extrae componentes y no aprueba el estilo final; el layout de producción, los breakpoints responsive y los mockups del resto de pantallas siguen pendientes.

## Decisiones confirmadas

| Tema | Elección |
| --- | --- |
| Dirección | Arcade 8/16 bits: formas pixeladas y elementos del tablero diferenciados |
| Tipografía | Pixelada en títulos, botones y cifras; sencilla en nombres e instrucciones |
| Paleta | Verde clásico: fondo carbón, serpiente verde, comida coral y acentos cian |

Estas elecciones se confirmaron mediante tres preguntas. La familia pixelada ya está elegida (Silkscreen); los códigos de color y los tamaños quedan aceptados como referencia en las pantallas piloto aceptadas, no como sistema aprobado para el resto de mockups. Los refinamientos listados abajo sí se acordaron en la ronda actual.

## Refinamientos acordados (ronda actual)

Estos ajustes están acordados y se reflejan en la [hoja de revisión visual](style-sheet.html). Se separan de la paleta y la tipografía, cuyos valores aplicados en las pantallas piloto quedan aceptados como referencia.

- **Radio de 8 px:** botones y campo de nombre usan 8 px de redondeo (dentro del rango acordado de 6–8 px). El panel y el tablero conservan su geometría recta.
- **Botones `play` y «Nueva partida»:** estado normal con relleno `snake` y texto `background`; hover con relleno carbón, texto verde y borde verde; pulsado conserva esos colores invertidos y añade una señal interior sin desplazar la caja. Nunca texto carbón sobre relleno carbón.
- **Foco de teclado separado:** contorno exterior `focus` de 2 px, separado del control por 2 px de fondo oscuro reales en las combinaciones normal, hover y pulsado. El foco no se iguala al hover.
- **Serpiente como tubo continuo:** el cuerpo se lee como un tubo, no como bloques sueltos, con cola redondeada y cabeza redondeada y amistosa con ojos. Se permite un **volumen sutil solo para la serpiente**, como excepción documentada a la regla general «sin degradados»; se construye mezclando los tokens existentes (por ejemplo con `color-mix`), sin inventar valores hexadecimales nuevos. Sin animación, sin CRT ni 3D fotorrealista.
- **Ranking sin cuadrícula de celdas:** se conserva la tabla semántica, el caption, los encabezados y las columnas con alineación y espaciado claros; se retiran los bordes de celda y se admite una alternancia discreta con los tokens existentes. Esto se refiere al ranking, no a la cuadrícula decorativa del tablero.
- **Vidas con corazones:** el indicador de vidas usa **tres corazones pixelados** de posiciones fijas —llenos para las vidas disponibles y de contorno para las perdidas—, con la misma geometría en ambos estados y sin depender solo del color. Se dibujan con trazado local (forma escalonada del estilo arcade); no son emoji ni iconos externos. Esta representación no cambia las reglas de vidas y no se implementa aquí: se construirá con el juego.

Estos refinamientos son acuerdos de componentes; no implican que el estilo visual completo esté aprobado. La fuente ya está elegida (Silkscreen); su integración local y la revisión final de estilo siguen pendientes.

## Tokens de color propuestos

| Token | Valor | Uso |
| --- | --- | --- |
| `background` | `#0D1117` | Fondo general y texto sobre botones verdes |
| `surface` | `#161B22` | Panel, campo de nombre y filas del ranking |
| `board` | `#0B1014` | Fondo del tablero |
| `text` | `#F0F6FC` | Texto principal sobre fondos oscuros |
| `text-muted` | `#A9B4C0` | Instrucciones y etiquetas secundarias |
| `border` | `#8B949E` | Límites de campos, muros y obstáculos |
| `grid` | `#22303A` | Cuadrícula decorativa, nunca un obstáculo |
| `snake` | `#7EE787` | Serpiente y relleno de botones de acción |
| `food` | `#FF7B72` | Comida; acento del resultado Game Over |
| `accent` | `#79C0FF` | Acentos de interfaz y etiquetas destacadas |
| `focus` | `#F2CC60` | Contorno de foco del campo y botones |

Usar `text` o `text-muted` solo sobre `background`, `surface` o `board`. En botones con relleno `snake`, usar texto `background`, no blanco. Los acentos `snake`, `food` y `accent` se usan sobre fondos oscuros, no como fondos de texto claro.

## Tipografía y geometría propuestas

- Títulos: fuente pixelada, 24 px; 32 px solo si cabe en la caja aprobada. Botones y cifras: 16 px. No comprimir texto para simular píxeles.
- Nombres, instrucciones, etiquetas y texto del ranking: fuente sencilla del sistema, 16 px e interlineado 1,5. Las cifras del ranking usan el rol pixelado; los nombres no.
- **Fuente pixelada elegida: Silkscreen.** La persona responsable eligió **Silkscreen** para títulos, botones y cifras, con pesos reales 400 y 700 (títulos a 24 px, botones y cifras a 16 px), sin estilos sintéticos. Nombres, instrucciones y texto del ranking conservan la fuente sencilla del sistema. La hoja de referencia carga solo Silkscreen desde Google Fonts de forma temporal: requiere conexión y hace solicitudes a Google; cada muestra informa si la carga pudo confirmarse y, si falla, avisa de que se muestra un sustituto monoespaciado y no debe juzgarse como la fuente real. El navegador descarga temporalmente la fuente y puede conservarla en caché, pero no se guardan sus archivos en el proyecto. La elección no implica alojamiento local. Un script local comprueba únicamente la carga de la muestra, sin lógica de juego, almacenamiento ni envío de los textos introducidos.
- **Integración local pendiente de construcción.** Antes de entregar la aplicación con estilo hay que adquirir Silkscreen desde su fuente oficial, conservar su licencia OFL, configurar un `@font-face` local para los pesos y roles requeridos, retirar la dependencia de Google en tiempo de ejecución y verificar el renderizado sin conexión, los caracteres españoles y el encaje del texto. Nada de esto se ha realizado todavía.
- Base de espaciado: 4 px; usar 4, 8, 12, 16, 24 y 32 px cuando sean compatibles con el espacio existente. No ajustar la disposición aprobada para imponer esta escala.
- Bordes sólidos de 2 px; radio de 8 px solo en botones y campo de nombre (panel y tablero rectos). Sin degradados ni desenfoque generales, con la única excepción documentada del volumen sutil de la serpiente.
- Se conservan panel central, HUD, tablero, tablas y cajas de los [wireframes](README.md). Si un texto no cabe, revisar el token antes de proponer un cambio de disposición.

## Componentes y estados propuestos

| Componente | Tratamiento visual | Límite funcional |
| --- | --- | --- |
| Campo de nombre | Fondo `surface`, texto `text`, borde `border`, radio de 8 px; etiqueta e instrucciones siempre legibles | Mantener el foco de entrada sin cambiar el contenido; no añadir validaciones |
| Botones `play` y «Nueva partida» | Radio de 8 px; normal con relleno `snake` y texto `background`; hover con relleno `background`, texto `snake` y borde `snake`; pulsado mantiene la inversión y añade una señal interior sin desplazar la caja | Mantener sus acciones existentes; no crear botones nuevos |
| Foco de teclado | Contorno exterior `focus` de 2 px, separado por 2 px de fondo oscuro, distinto de hover en normal, hover y pulsado | Tab permite salir del campo hacia `play`; no retener el foco |
| HUD | Etiquetas sencillas y cifras pixeladas; jugador en fuente sencilla; vidas como tres corazones pixelados de posiciones fijas (llenos para disponibles, de contorno para perdidas); texto `text` y acentos `accent` | No añadir indicadores ni alterar su orden; la forma y el contorno distinguen los estados, no solo el color |
| Tablero | Serpiente verde como tubo continuo con cola redondeada y cabeza redondeada con ojos; comida coral con forma de rombo (única forma ilustrativa: las variantes de comida no están definidas); muros y obstáculos sólidos con trama interior. Volumen sutil solo en la serpiente, sin nuevos valores de paleta | Formas y colores ilustrativos; no definir niveles ni reglas de colisión. La cuadrícula decorativa no es jugabilidad; las variantes de comida no se presentan aquí |
| Resultados | Game Over con acento `food`; victoria con acento `snake`; resumen legible en ambas variantes | Mantener cinco segundos y el enrutado ya definido; no añadir acciones |
| Top 10 | Nombres legibles y cifras pixeladas, sin cuadrícula de celdas, con alineación y espaciado claros y alternancia discreta | No inferir orden de empates ni almacenamiento |

## Legibilidad y efectos

- La identificación no depende solo del color: conservar formas, etiquetas y contornos diferenciados. No poner cuadrícula decorativa al mismo nivel visual que obstáculos.
- Objetivo de contraste: al menos 4,5:1 para texto y 3:1 para límites necesarios de controles y foco contra su fondo adyacente. Comprobar las combinaciones reales de los mockups, no solo estos tokens. Para botones, elegir pares que no dependan de un borde fino sobre el relleno verde.
- Evitar scanlines sobre contenido, brillo que borre contornos, parpadeos y filtros CRT. No se necesita animación decorativa para representar esta dirección.
- Las animaciones de victoria y Game Over siguen siendo requisitos del flujo; su aspecto se diseñará después. Este documento no las elimina ni cambia su duración.

## Revisión y siguiente paso

**Punto actual:** la [pantalla piloto de Game Over](game-over-pilot.html) quedó **aceptada como referencia visual**. La [pantalla piloto de Victoria](victory-pilot.html) está creada y **pendiente de revisión visual**: resumen estático con acento `snake`, nivel y velocidad ilustrativos de 5, sin botones, animación ni redirección activa. La condición para completar el quinto nivel sigue pendiente. Revisar Victoria antes de crear Top 10; la aceptación de Inicio, Partida y Game Over no se amplía automáticamente. El push queda aplazado hasta finalizar y autorizar todos los diseños.

La revisión de la tipografía está cerrada con **Silkscreen** y los refinamientos de componentes están acordados. Los valores visuales aplicados en Inicio, Partida y Game Over quedan aceptados como referencia; su aplicación a los demás mockups y a la implementación necesita su propia revisión. La **pantalla piloto de Inicio** ([`start-pilot.html`](start-pilot.html)), la **pantalla piloto de Partida** ([`playing-pilot.html`](playing-pilot.html)) y la **pantalla piloto de Game Over** ([`game-over-pilot.html`](game-over-pilot.html)) quedaron **aceptadas como referencia visual**; puedes consultar también la [hoja de revisión visual](style-sheet.html) (V1–V6). La Partida incluye las vidas como **tres corazones pixelados** (llenos/contorno) y el aviso al pie corregido. El siguiente paso es revisar **Victoria**, ya creada, antes de Top 10. La comida sigue como un **único rombo ilustrativo**: las variantes de comida (formas, colores o efectos) **no están definidas** ni se presentan en los mockups, y permanecen como posibilidad abierta en la [idea de Snake](../../idea-proyecto-snake.md). La integración local de la fuente y la extensión del estilo al resto siguen pendientes. El encaje del HUD y de las cifras de Partida con **Silkscreen** ya se comprobó a 1024 × 768 en Chrome; el encaje responsive, cross-browser y de producción queda para fases posteriores. No afirmar accesibilidad completa ni comportamiento de teclado a partir de esta especificación.

Fuentes funcionales: [idea de Snake](../../idea-proyecto-snake.md), [flujo](../../game-flow-snake.md) y [notas por pantalla](screens.md). Las reglas del juego aún abiertas siguen abiertas.
