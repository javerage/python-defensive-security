# Notas por pantalla — wireframes de Snake (propuesta)

Propuesta de diseño **revisada y aprobada**. Cada boceto usa una referencia de ventana de computadora de **1024 × 768**. Los wireframes permanecen en escala de grises y aprobados; el [lenguaje visual](visual-style.md) se documenta aparte como borrador de fase 1 y no modifica estos bocetos. Existen además cinco **pantallas piloto** separadas que aplican el borrador visual: la **[pantalla piloto de Inicio](start-pilot.html)**, la **[pantalla piloto de Partida](playing-pilot.html)**, la **[pantalla piloto de Game Over](game-over-pilot.html)**, la **[pantalla piloto de Victoria](victory-pilot.html)** y la **[pantalla piloto de Top 10](top10-pilot.html)**, las cinco **aceptadas como referencia visual** (los valores visuales aplicados en ellas quedan aceptados como referencia). Las notas de abajo describen los wireframes en escala de grises.

La [pantalla piloto de Top 10](top10-pilot.html) quedó **aceptada como referencia visual** con sus valores visuales aplicados, que no se extienden a la implementación.

> Los nombres de estado (`AwaitingStart`, `Playing`, `Results`, `Victory`, `Highscores`) provienen del [recorrido de una partida](../../game-flow-snake.md). Los bocetos proponen disposición, no reglas nuevas.

## Inicio — `AwaitingStart`
- **Propósito:** permitir indicar un nombre (opcional) y esperar la acción de inicio.
- **Elementos visibles:** título del juego; campo de nombre editable (vacío por defecto); botón con la etiqueta exacta `play`; nota de que sin nombre se genera `player_YYYYMMDD_HHmmss_SSS`.
- **Acciones:** escribir un nombre; activar `play` o pulsar Enter desde el campo de nombre. Los espacios permiten escribir «dark angel» sin iniciar; espacio no es un atajo global de inicio.
- **Foco al entrar:** el campo de nombre recibe el foco al abrir el juego y en cada regreso al inicio, desde el top 10 o por no clasificar. Se muestra un indicador visible, sin cambiar el contenido ni iniciar la partida. Tab permite pasar a `play`; el foco no se recupera continuamente durante la navegación. Enter con el campo vacío inicia con nombre automático.
- **Transiciones:** a `Playing` al activar `play` o pulsar Enter desde el campo de nombre. Escribir el nombre no inicia la partida; sin nombre se mantiene la generación automática al iniciar.
- **Referencia:** 1024 × 768.
- **Notas de reglas pendientes:** validación detallada del nombre y referencia horaria del automático. El campo no precarga el nombre automático anterior.

## Partida — `Playing`
- **Artefacto:** [pantalla piloto de Partida](playing-pilot.html) (aceptada como referencia visual).
- **Propósito:** mostrar el estado de la partida y el tablero mientras la serpiente se mueve.
- **Elementos visibles:** jugador, puntaje, vidas, nivel y velocidad; las vidas se muestran como tres corazones pixelados (llenos para las disponibles, de contorno para las perdidas); tablero central con serpiente, comida, muros y obstáculos.
- **Acciones:** dirigir la serpiente con las flechas del teclado. No hay pausa, ajustes, reinicio manual ni registro desde esta pantalla.
- **Transiciones:** dentro de `Playing` al comer, avanzar de nivel o perder una vida (reinicio automático); a `Results` al perder la última vida; a `Victory` al completar el quinto nivel.
- **Referencia:** 1024 × 768 (tablero y HUD dentro del panel central).
- **Notas de reglas pendientes:** puntos por comida, velocidad inicial e incremento, datos conservados tras perder una vida, escenarios por nivel y condición para completar el quinto. Escenario, serpiente y comida usan valores ilustrativos. La comida se mantiene como un único rombo ilustrativo: las variantes de comida (formas, colores o efectos) no están definidas ni se presentan en el mockup y se registran como posibilidad abierta en la [idea inicial del proyecto](../../idea-proyecto-snake.md). La presentación de vidas con corazones pixelados es de referencia y no implementa la pérdida de vidas.

## Game Over — `Results`
- **Artefacto:** [pantalla piloto de Game Over](game-over-pilot.html), aceptada como referencia visual. Referencia estática: sin animación, temporizador, registro ni redirección activa; el texto describe el flujo futuro, no lo ejecuta.
- **Propósito:** mostrar los resultados cuando se agotan las vidas.
- **Elementos visibles:** animación de «game over»; nombre, puntaje, nivel y velocidad; nota de redirección a los 5 segundos.
- **Acciones:** ninguna acción del jugador; la redirección es automática. Sin botón de continuar ni de reintentar.
- **Transiciones:** tras 5 segundos, a `Highscores` si el resultado clasifica; a `AwaitingStart` si no clasifica.
- **Referencia:** 1024 × 768.
- **Notas de reglas pendientes:** valores mostrados son ilustrativos. La admisión al top 10 ya está definida en el flujo; siguen pendientes la interpretación del registro por nivel, el orden de empates admitidos y el almacenamiento.

## Victoria — `Victory`
- **Artefacto:** [pantalla piloto de Victoria](victory-pilot.html), aceptada como referencia visual. Es una referencia estática con acento verde `snake`, nivel y velocidad ilustrativos de 5; no ejecuta animación, registro, temporizador ni redirección. La condición para completar el quinto nivel sigue pendiente.
- **Propósito:** mostrar los resultados tras completar los cinco niveles.
- **Elementos visibles:** animación de victoria; nombre, puntaje, nivel y velocidad; nota de redirección a los 5 segundos; nota de que la condición de finalización sigue pendiente.
- **Acciones:** ninguna acción del jugador; la redirección es automática. Sin botón de continuar ni de reintentar.
- **Transiciones:** tras 5 segundos, a `Highscores` si el resultado clasifica; a `AwaitingStart` si no clasifica.
- **Referencia:** 1024 × 768.
- **Notas de reglas pendientes:** condición concreta para completar el quinto nivel.

## Top 10 — `Highscores`
- **Artefacto:** [pantalla piloto de Top 10](top10-pilot.html), aceptada como referencia visual. Conserva las diez filas ilustrativas del wireframe y el botón «Nueva partida» como muestra de estados visuales; no navega, guarda resultados ni inicia partidas. La aceptación es de los valores visuales aplicados y no se extiende a la implementación.
- **Propósito:** mostrar hasta diez resultados registrados y ofrecer una nueva partida.
- **Elementos visibles:** tabla con hasta diez entradas (posición, nombre, puntaje, nivel) con datos ilustrativos; una única acción con la etiqueta exacta «Nueva partida».
- **Acciones:** pulsar «Nueva partida».
- **Transiciones:** a `AwaitingStart` al pulsar «Nueva partida»: vuelve al inicio sin iniciar movimiento, conserva precargado y editable solo el nombre escrito por el jugador y espera `play` o Enter desde el campo de nombre.
- **Foco de destino:** al entrar al inicio, el campo de nombre recibe el foco sin alterar su contenido ni iniciar movimiento.
- **Referencia:** 1024 × 768.
- **Notas de reglas pendientes:** interpretación del registro por nivel, orden entre empates iguales, almacenamiento y duración. Los datos de la tabla son ilustrativos, no rankings reales.
