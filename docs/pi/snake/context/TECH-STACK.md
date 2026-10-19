# Plataforma y lenguaje del proyecto Snake

Registra únicamente lo confirmado sobre la plataforma y el lenguaje. **No fija versiones, frameworks ni herramientas**, porque todavía no se han elegido: las versiones de lenguaje, tiempo de ejecución, navegador o herramientas **no están confirmadas** y no se inventan aquí.

## Confirmado

| Tema | Decisión | Fuente |
| --- | --- | --- |
| Lenguaje | **TypeScript** | [idea](../../idea-proyecto-snake.md) |
| Plataforma | **Navegador web únicamente** | [idea](../../idea-proyecto-snake.md) |
| Versión de terminal | **No habrá** una versión para jugar en la terminal | [idea](../../idea-proyecto-snake.md) |
| Pantallas | Vistas web estáticas y cinco pantallas piloto | [wireframes](../design/README.md) |

## No confirmado

- **Framework o biblioteca de interfaz:** no elegido.
- **Cadena de herramientas, empaquetador o runner:** no elegido.
- **Versiones** de TypeScript, tiempo de ejecución o navegador: no confirmadas.
- **Almacenamiento del highscore:** forma y ubicación pendientes.
- **Tecnología de audio:** pendiente; el audio se desarrolla al final.

## Lenguaje visual confirmado (referencia)

Hechos visuales confirmados en las fuentes de diseño, **como referencia y no como implementación**:

- Dirección arcade de 8/16 bits, con formas pixeladas y elementos del tablero diferenciados.
- Tipografía pixelada en títulos, botones y cifras; fuente sencilla del sistema en nombres e instrucciones.
- Paleta verde clásico: fondo oscuro, serpiente verde, comida coral y acentos cian.
- **Fuente pixelada elegida: Silkscreen**, con integración local **pendiente**.

Los valores concretos de color, tamaños y componentes están aceptados **solo como referencia** en las pantallas piloto y no como sistema aprobado. Ver [visual-style.md](../design/visual-style.md).

## Límites conocidos

- La interfaz se adaptará a distintos tamaños de ventana en computadora; el **tamaño mínimo** y los **dispositivos compatibles** siguen pendientes.
- No se confirma soporte para teléfonos, tabletas ni controles táctiles.
- No se han realizado compilaciones de la aplicación ni una validación del renderizado sin conexión con la fuente real.
