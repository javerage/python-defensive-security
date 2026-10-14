# Idea inicial: juego de Snake

Juego de Snake para navegador web desarrollado con TypeScript. La serpiente se desplaza por escenarios de bloques geométricos, come bloques de comida para sumar puntos y crecer, avanza por 5 niveles con dificultad progresiva y cambio de escenario, y el jugador evita chocar con los muros o consigo misma.

## 1. Qué quiere construir

Quiere construir un juego de Snake que se juega únicamente en un navegador web; queda descartado usar la terminal como medio de juego. Se desarrollará con TypeScript. La serpiente se desplaza por escenarios formados por bloques geométricos; el jugador intenta comer bloques de comida, sumar puntos y avanzar por niveles mientras evita chocar con los muros o consigo misma.

El modo historia consiste en una progresión por 5 niveles, con dificultad creciente y cambio de escenario al avanzar de nivel.

## 2. Para quién

- **Personas que pueden jugar:** cualquier persona que pueda acceder a la página web, sin restringir el juego al rango de edad del público objetivo. Por ahora no se definen adaptaciones específicas para otras edades.
- **Público objetivo de diseño:** adolescentes de 14 a 18 años. Sus preferencias orientarán los colores, los escenarios y las mecánicas del juego, conservando las reglas ya confirmadas y dejando los detalles abiertos para definirlos después.
- **Objetivo por validar:** se busca que el diseño resulte atractivo para ese público; todavía no se ha comprobado ni se ha definido cómo validarlo. Esta intención no añade actividades de evaluación ni recopilación de datos.

## 3. Qué necesidad o experiencia quiere atender

La experiencia buscada es una partida accesible y entretenida, con progreso que se pueda observar mediante puntos, niveles y velocidad. Los escenarios de bloques geométricos de colores deben ayudar a distinguir el espacio de juego, los muros, los obstáculos y la comida. El estilo visual propuesto usa un fondo oscuro, texto blanco y una serpiente de color llamativo.

La partida debería comunicar con claridad el resultado alcanzado: al terminar, mostrar el nombre del jugador, el puntaje, el nivel y la velocidad alcanzados.

## 4. Qué comportamientos considera indispensables

- Antes de jugar, solicitar el nombre del jugador. El inicio de la partida debe poder activarse con un botón cuya etiqueta sea «play» o con la tecla de espacio; las flechas del teclado sirven para mover la serpiente.
- La serpiente comienza con un tamaño de tres bloques y avanza automáticamente en línea recta horizontal. Al comer bloques de comida, obtiene puntos y crece en 1 bloque por cada bloque consumido; el contador de puntaje aumenta según la comida consumida.
- La partida muestra contadores de puntaje, vidas y velocidad. Cada 15 puntos, el jugador sube un nivel y la velocidad aumenta. El ejercicio considera 5 niveles; el modo historia consiste en ese incremento paulatino y en el cambio de escenario por cada nivel que se avance.
- El jugador comienza con tres vidas. Una colisión con un muro o con la propia serpiente consume una vida y reinicia el juego, salvo cuando era la última vida, caso en el que la partida termina. Al finalizar, se muestra el puntaje, el nivel y la velocidad alcanzados junto con el nombre del jugador.
- Los escenarios de cada nivel están compuestos por bloques de distintos colores que representan muros y obstáculos; las formas son geométricas y simples.
- El juego contempla guardar un «highscore» por nivel alcanzado mostrando únicamente el top 10: nunca se muestran más de 10 resultados y los puntajes se van eliminando a medida que son superados.
- La interfaz se adapta a distintos tamaños de ventana en computadora. Quedan por definir el tamaño mínimo y los dispositivos compatibles; esta adaptación no confirma soporte para teléfonos, tabletas ni controles táctiles.
- La propuesta de sonido contempla un sonido de inicio, música suave que se repite en bucle durante la partida, un sonido «coin» al comer comida, «explosion» al perder una vida y «game over» al morir la serpiente. Estos elementos se dejan para el final del desarrollo, después de contar con jugabilidad y escenarios.

## 5. Qué quedará fuera de la primera versión

Quedan fuera de la primera versión:

- **Guardar y retomar partidas:** no se conserva una partida en curso para continuarla después. Esto no excluye guardar el «highscore» top 10, que se mantiene como requisito.
- **Modo multijugador:** no se incluye jugar con otras personas.

Estas son decisiones de alcance del MVP, no imposibilidades técnicas de un juego web ni exclusiones permanentes de versiones futuras. La compatibilidad con teléfonos, tabletas y controles táctiles sigue pendiente: no se confirma ni se descarta. La adaptación a distintos tamaños de ventana en computadora sí está incluida.

El modo historia, los 5 niveles y el «highscore» top 10 se mantienen. El sonido se implementará al final, después de la jugabilidad y los escenarios; esa prioridad no lo elimina del objetivo del juego.

## 6. Qué todavía no sabe decidir

Las siguientes decisiones sobre el juego permanecen abiertas. Se distinguen los detalles necesarios para concretar su funcionamiento de las funciones cuya inclusión todavía no se ha decidido.

**Reglas y experiencia de juego**

- Cuántos puntos da cada bloque de comida.
- Cuánto aumenta la velocidad al subir de nivel y cuál es la velocidad inicial.
- Qué se conserva o reinicia —incluidos puntaje, nivel y velocidad— después de perder una vida y reiniciar la partida.
- Cómo se determina la dificultad y el diseño de los escenarios de cada uno de los 5 niveles.

**Compatibilidad y presentación**

- Qué dispositivos serán compatibles, incluido el posible soporte de teléfonos y tabletas, y qué controles serían necesarios para ellos.
- Cuál será el tamaño mínimo de ventana admitido y cómo comprobar la adaptación de la interfaz en computadora.

**Funciones y alcance por decidir**

- Si el juego tendrá skins para personalizar la serpiente.
- Si el juego tendrá una tienda para adquirir ítems.
- Si se podrán compartir los resultados en redes sociales.
- Qué otros límites del MVP necesitan definirse, además de las exclusiones ya confirmadas de guardar y retomar partidas y del modo multijugador.

Las skins, la tienda y la opción de compartir resultados son posibilidades pendientes de decisión: no son requisitos aprobados del MVP ni compromisos para una versión futura.
