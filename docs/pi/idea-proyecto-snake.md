# Idea inicial: juego de Snake

El proyecto consiste en crear un juego de Snake para navegador web utilizando TypeScript. El jugador guiará a la serpiente para recoger comida, sumar puntos y hacerla crecer, evitando que choque con los muros o con su propio cuerpo. La partida recorrerá cinco niveles, cada uno con un escenario diferente y una dificultad mayor que el anterior.

## 1. Qué quiere construir

El juego se desarrollará con TypeScript y se jugará únicamente desde un navegador web; no tendrá una versión para jugar en la terminal.

Su modo historia consistirá en avanzar por cinco niveles con escenarios de bloques geométricos y dificultad creciente. Completar el quinto nivel terminará la partida con una animación de victoria; la condición concreta para completarlo sigue pendiente.

## 2. Para quién

Cualquier persona que pueda acceder a la página web podrá jugar, sin restricciones de edad. Sin embargo, el diseño estará dirigido principalmente a adolescentes de 14 a 18 años: sus preferencias orientarán la elección de colores, los escenarios y las mecánicas, sin cambiar las reglas ya acordadas. Por ahora no se prevén adaptaciones específicas para otras edades.

Se busca que el juego resulte atractivo para ese público, pero todavía no se ha comprobado ni se ha definido cómo validarlo. Este objetivo no supone añadir actividades de evaluación ni recopilar datos.

## 3. Qué necesidad o experiencia quiere atender

La intención es ofrecer partidas accesibles y entretenidas, en las que el jugador pueda seguir su progreso mediante los puntos, el nivel y la velocidad. El diseño visual tendrá un fondo oscuro, texto blanco y una serpiente de color llamativo. Los escenarios usarán formas geométricas simples y bloques de colores para distinguir el espacio de juego, los muros, los obstáculos y la comida.

Al terminar la partida, se mostrarán el nombre del jugador y los resultados alcanzados: puntaje, nivel y velocidad.

## 4. Qué comportamientos considera indispensables

- Antes de jugar, se ofrecerá indicar un nombre. La partida comenzará al activar un botón con la etiqueta exacta «play» o pulsar Enter desde el campo de nombre. Escribir el nombre no iniciará la partida: los espacios permiten nombres como «dark angel» y no actúan como un atajo global de inicio. Si no se ha indicado un nombre, se generará uno con el formato `player_YYYYMMDD_HHmmss_SSS`, usando la fecha, la hora y tres dígitos de milisegundos del momento de inicio; por ejemplo, `player_20261015_173025_482`. No se añadirá un componente aleatorio. El nombre será una etiqueta visible de la partida que busca reducir coincidencias, sin garantizar unicidad. Las flechas del teclado servirán para dirigir la serpiente.
- La serpiente empezará con tres bloques y avanzará automáticamente en línea recta horizontal. Cada bloque de comida consumido sumará puntos y hará crecer la serpiente en un bloque.
- Durante la partida se mostrarán el puntaje, las vidas y la velocidad. Cada 15 puntos se subirá un nivel y aumentará la velocidad. La progresión prevista es de cinco niveles, con dificultad creciente y un cambio de escenario en cada nivel.
- En cada entrada a la pantalla de inicio, el campo de nombre recibirá el foco: tanto al abrir el juego como al regresar mediante «Nueva partida» o por no clasificar. El foco tendrá un indicador visible y no cambiará el contenido del campo ni iniciará la partida. Se podrá escribir directamente o pulsar Enter con el campo vacío para iniciar con un nombre automático; Tab permitirá pasar al botón «play». El foco se establecerá al entrar, no se recuperará continuamente mientras el jugador navegue.
- El jugador comenzará con tres vidas. Chocar contra un muro o contra la propia serpiente consumirá una vida. Si todavía quedan vidas, se reiniciará la partida y el movimiento se reanudará automáticamente, sin volver a activar «play» ni pulsar Enter; al perder la última, el juego terminará. Las vidas se mostrarán como tres corazones pixelados de posiciones fijas —trazados con la forma escalonada del estilo arcade, no emoji ni iconos externos—; el corazón lleno indicará una vida disponible y el de contorno, una vida perdida. Ambos estados compartirán la misma geometría y el color no será la única señal. Esta forma de mostrar las vidas es solo una representación: no cambia el arranque con tres vidas, la pérdida de vida ni los demás comportamientos ya descritos.
- Los escenarios tendrán muros y obstáculos representados con bloques de distintos colores y formas geométricas simples.
- Se guardará un «highscore» por nivel alcanzado y se mostrarán hasta diez resultados, correspondientes a los mejores puntajes, nunca más de diez. Las reglas del registro por nivel y del orden entre entradas admitidas con igual puntaje, así como la forma y el tiempo de almacenamiento, siguen pendientes.
- Al perder todas las vidas se mostrará una animación de «game over»; al completar los cinco niveles, una animación de victoria. En ambos finales se mostrarán el nombre, el puntaje, el nivel y la velocidad alcanzados. Tras cinco segundos se redirigirá a la pantalla del top 10 si el resultado clasifica, o al menú de inicio si no clasifica.
- Si hay menos de diez resultados registrados, el resultado ingresará al top 10, incluso con cero puntos. Si ya hay diez, solo ingresará si su puntaje es estrictamente mayor que el del último: desplazará ese resultado y la lista conservará un máximo de diez entradas. Un empate con el último no lo desplazará. No se registrará un resultado que no clasifique.
- La pantalla del top 10 ofrecerá un botón con la etiqueta exacta «Nueva partida». Volverá al inicio, sin iniciar el movimiento ni exigir salir automáticamente del top 10. Tanto por este botón como al regresar por no clasificar, el nombre escrito por el jugador quedará precargado y editable: podrá conservarlo, cambiarlo o borrarlo. Se esperará nuevamente la activación de «play» o Enter desde el campo de nombre. El nombre automático de la partida anterior no se reutilizará: si no hay un nombre escrito, el campo estará vacío y se generará otro al iniciar, con la regla ya definida. Una nueva partida no arrastrará el estado de juego anterior; esto no equivale al reinicio automático por perder una vida mientras quedan otras.
- La interfaz se adaptará a distintos tamaños de ventana en computadora. El tamaño mínimo y los dispositivos compatibles siguen pendientes; no se confirma soporte para teléfonos, tabletas ni controles táctiles.
- El juego incluirá un sonido de inicio y música suave en bucle durante la partida; al comer, sonará «coin»; al perder una vida, «explosion»; y al morir la serpiente, «game over». El audio se abordará al final del desarrollo, después de la jugabilidad y los escenarios.

## 5. Qué quedará fuera de la primera versión

Quedan fuera de la primera versión:

- **Guardar y retomar partidas:** no se podrá guardar una partida en curso para continuarla después. Esta exclusión no afecta al guardado del «highscore» top 10.
- **Modo multijugador:** no se podrá jugar con otras personas en una misma partida.

Estas exclusiones delimitan el MVP; no representan imposibilidades técnicas para un juego web ni descartes permanentes de versiones futuras. La compatibilidad con teléfonos, tabletas y controles táctiles sigue pendiente: no se confirma ni se descarta. La adaptación a distintos tamaños de ventana en computadora sí forma parte del alcance.

El modo historia, los cinco niveles y el «highscore» top 10 seguirán formando parte del juego. El sonido también estará incluido, aunque se desarrollará después de la jugabilidad y los escenarios.

## 6. Qué todavía no sabe decidir

Siguen pendientes decisiones necesarias para concretar las reglas y la presentación, así como la inclusión de algunas funciones. Que una función aparezca aquí no significa que esté aprobada para el MVP ni comprometida para una versión futura.

**Reglas y experiencia de juego**

- Cuántos puntos otorga cada bloque de comida.
- Cuál será la velocidad inicial y cuánto aumentará al subir de nivel.
- Qué se conserva o reinicia —incluidos puntaje, nivel y velocidad— tras perder una vida.
- Cómo se definirán la dificultad y los escenarios de cada uno de los cinco niveles.
- Qué condición permitirá completar el quinto nivel. El desenlace de victoria y la redirección posterior ya están definidos; no se añade un sexto nivel.
- Cómo se interpretará el «highscore» por nivel, cómo se ordenarán las entradas admitidas con puntajes iguales, dónde se conservarán los resultados y durante cuánto tiempo. El empate con el último de una lista llena no permite ingresar.
- Qué referencia horaria se usará para generar los nombres y cuáles serán las reglas detalladas de validación de los nombres escritos por el jugador.

**Compatibilidad y presentación**

- Qué dispositivos serán compatibles, incluido el posible soporte para teléfonos y tabletas, y qué controles se necesitarían.
- Cuál será el tamaño mínimo de ventana y cómo se comprobará la adaptación de la interfaz en computadora.

**Funciones y alcance por decidir**

- Si se incluirán «skins» para personalizar la serpiente.
- Si habrá una tienda para adquirir ítems.
- Si se podrán compartir resultados en redes sociales.
- Si la comida tendrá distintas formas o colores —y si la forma o el color cambiarían el comportamiento del juego—. Es una posibilidad abierta: no está aprobada para el MVP ni comprometida para una versión futura, y no modifica la regla actual de que cada bloque de comida suma puntos y hace crecer la serpiente en un bloque.
- Qué otros límites del MVP necesitan definirse, además de las exclusiones ya confirmadas de guardar y retomar partidas y del modo multijugador.

Las skins, la tienda, la opción de compartir resultados y la variedad de comida son posibilidades pendientes de decisión: no son requisitos aprobados del MVP ni compromisos para una versión futura.
