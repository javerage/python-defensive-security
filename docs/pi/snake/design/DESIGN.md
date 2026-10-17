# Snake — referencia para aplicar el lenguaje visual

**Estado:** guía de aplicación en borrador. Dirección confirmada: arcade 8/16 bits, paleta verde clásica y tipografía pixelada en títulos, botones y cifras. En la ronda actual se acordaron refinamientos de componentes y se eligió la fuente pixelada **Silkscreen**; la paleta y los tamaños siguen propuestos, la integración local de la fuente queda pendiente y el estilo visual final aún no está aprobado. El siguiente paso acordado es la **pantalla piloto de Inicio**, todavía no creada, que aplica el sistema con los valores propuestos sin aprobarlos.

La fuente única de tokens, estados y límites es [visual-style.md](visual-style.md). No duplicar sus valores en esta guía ni tratar sus propuestas como aprobadas.

## Acuerdos y propuestas

- **Acordado en la ronda actual:** radio de 8 px en botones y campo de nombre; botones que invierten relleno y texto en hover y pulsado con foco exterior separado; serpiente como tubo continuo con cola redondeada y cabeza redondeada con ojos; ranking sin cuadrícula de celdas.
- **Todavía propuesto:** los 11 códigos hexadecimales y los tamaños exactos. La familia pixelada ya está elegida (Silkscreen); su descarga y configuración local siguen pendientes de construcción.
- **Excepción documentada:** el volumen sutil de la serpiente permite un degradado construido con los tokens existentes; es la única excepción a la regla general «sin degradados». No inventar valores hexadecimales nuevos.

## Reglas para diseñar las pantallas

1. Consultar el wireframe correspondiente y sus [notas](screens.md). Preservar las cajas y acciones aprobadas en la referencia de 1024 × 768.
2. Aplicar los tokens semánticos de `visual-style.md`; no inventar una paleta por pantalla.
3. Mantener nombres e instrucciones en fuente sencilla; reservar el rol pixelado —**Silkscreen**, ya elegida— para títulos, botones y cifras, con sus pesos reales 400 y 700. La hoja de referencia usa una muestra web temporal a Google Fonts; la conexión es necesaria para esa muestra y no se debe evaluar el sustituto si la carga no se confirma. Antes de entregar la aplicación hay que adquirir Silkscreen con su licencia OFL, configurar un `@font-face` local y retirar la dependencia de Google.
4. Mostrar foco visible, conservar el contenido del nombre y respetar Enter desde ese campo. No convertir el espacio en un atajo global.
5. Diferenciar serpiente, comida y obstáculos por forma además de color. La serpiente se dibuja como tubo continuo, no como bloques cuadrados. No añadir filtros CRT, elementos, estados de juego o reglas nuevas.
6. Verificar contraste, legibilidad, caracteres españoles y encaje con la fuente real antes de aprobar mockups. Esta fase contiene la muestra web de Silkscreen y un aviso local de carga, no mockups, archivos de fuentes ni implementación del juego. La integración local de Silkscreen es una tarea de construcción pendiente; hasta entonces la referencia sigue dependiendo de la web.

La aprobación de los wireframes no implica aprobación de estos tokens ni del futuro diseño visual. No generar pantallas fuera de la fase autorizada.
