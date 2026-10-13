# Ejemplo didáctico: idea inicial de un juego de Snake

Este ejemplo convierte el ejercicio de Snake en una descripción inicial para que el estudiantado pueda practicar cómo expresar una idea antes de construirla. Mantiene visibles las decisiones que todavía no están confirmadas; no es una especificación técnica ni afirma que el juego ya exista.

## 1. Qué quiere construir

Quiere construir un juego de Snake que pueda jugarse en una página web. La serpiente se desplaza por escenarios formados por bloques geométricos; el jugador intenta comer bloques de comida, sumar puntos y avanzar por niveles mientras evita chocar con los muros o consigo misma.

La idea general contempla un modo historia en el que la serpiente crece según los puntos obtenidos y niveles cuya dificultad aumenta con el progreso. El ejercicio de clase se plantea de manera gradual: primero se prepara un escenario inicial con lo mínimo necesario para comenzar el trabajo; después se incorporan progresivamente prompt-templates de PI, skills y el proceso SDD —especificación, planificación, implementación y validación—, y finalmente se considera automatizar el proceso con agentes y subagentes. Cada estudiante construye su MVP individualmente en clase. Esta secuencia describe la práctica de desarrollo, no pasos que deba realizar quien juega.

## 2. Para quién

Quienes jugarían son adolescentes de 14 a 18 años, para quienes se propone una presentación llamativa. Quienes construyen el MVP son estudiantes que realizan el ejercicio individualmente en clase; no se debe confundir a esos estudiantes con los personajes o usuarios del juego.

## 3. Qué necesidad o experiencia quiere atender

La experiencia buscada es una partida accesible y entretenida, con progreso que se pueda observar mediante puntos, niveles y velocidad. Los escenarios de bloques geométricos de colores deben ayudar a distinguir el espacio de juego, los muros, los obstáculos y la comida. El estilo visual propuesto usa un fondo oscuro, texto blanco y una serpiente de color llamativo.

La partida debería comunicar con claridad el resultado alcanzado: al terminar, mostrar el nombre del jugador, el puntaje, el nivel y la velocidad alcanzados. El ejercicio también busca que el estudiantado desarrolle el juego por etapas, empezando por la jugabilidad y los escenarios antes de abordar el sonido.

## 4. Qué comportamientos considera indispensables

- Antes de jugar, solicitar el nombre del jugador. El inicio de la partida debe poder activarse con un botón cuya etiqueta sea «play» o con la tecla de espacio; las flechas del teclado sirven para mover la serpiente.
- La serpiente comienza con un tamaño de tres bloques y avanza automáticamente en línea recta horizontal. Al comer bloques de comida, obtiene puntos y crece; el contador de puntaje aumenta según la comida consumida.
- La partida muestra contadores de puntaje, vidas y velocidad. Cada 15 puntos, el jugador sube un nivel y la velocidad aumenta. El formato de niveles aumenta la dificultad de acuerdo con el progreso.
- El jugador comienza con tres vidas. Una colisión con un muro o con la propia serpiente consume una vida y reinicia el juego, salvo cuando era la última vida, caso en el que la partida termina. Al finalizar, se muestra el puntaje, el nivel y la velocidad alcanzados junto con el nombre del jugador.
- Los escenarios de cada nivel están compuestos por bloques de distintos colores que representan muros y obstáculos; las formas son geométricas y simples.
- El juego contempla guardar un «highscore» por nivel alcanzado.
- La propuesta de sonido contempla un sonido de inicio, música suave que se repite en bucle durante la partida, un sonido «coin» al comer comida, «explosion» al perder una vida y «game over» al morir la serpiente. Estos elementos se dejan para el final del desarrollo, después de contar con jugabilidad y escenarios.

## 5. Qué quedará fuera de la primera versión

Las exclusiones de la primera versión todavía no están confirmadas. El ejercicio propone construir un MVP de manera gradual, empezando por un escenario inicial mínimo para comenzar el trabajo, pero no define qué características concretas se excluyen de ese MVP. Los elementos descritos en las secciones anteriores siguen siendo parte del objetivo general del ejercicio; el orden gradual no los convierte en exclusiones permanentes.

El sonido está diferido hasta el final de la secuencia de desarrollo; no se elimina del objetivo. No se han acordado otras exclusiones, por lo que no se presupone que funciones como el modo historia, los niveles o el guardado de «highscore» queden descartadas.

## 6. Qué todavía no sabe decidir

Este documento es un ejemplo didáctico basado en el ejercicio, no una descripción final entrevistada con estudiantes ni aprobada por una persona responsable. Las decisiones pendientes deben ser tomadas por el estudiante responsable del proyecto, con la orientación que corresponda; no se completan mediante suposiciones en este ejemplo.

Siguen pendientes, entre otras, estas decisiones:

- Si «utilizar la terminal CLI» describe una herramienta para desarrollar el juego o el medio en que se jugará. La solicitud también dice que se jugará en una página web; esa relación no está aclarada.
- Si se utilizará JavaScript o TypeScript. La solicitud menciona ambas posibilidades sin elegir una.
- Qué significa exactamente el modo historia: no se describen argumento, personajes ni eventos narrativos.
- Cuántos puntos da cada bloque de comida y cuánto crece la serpiente por cada bloque.
- Cuánto aumenta la velocidad al subir de nivel y cuál es la velocidad inicial.
- Qué se conserva o reinicia —incluidos puntaje, nivel y velocidad— después de perder una vida y reiniciar la partida.
- Cuántos niveles hay y cómo se determina su dificultad y el diseño de sus escenarios.
- Qué significa guardar un «highscore» por nivel: por ejemplo, qué puntaje se registra y durante cuánto tiempo se conserva.
- Qué funciones concretas integrarán el MVP inicial, más allá de empezar con un escenario mínimo y priorizar jugabilidad y escenarios antes del sonido.
