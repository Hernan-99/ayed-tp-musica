# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical
- Por qué lo eligieron (5–8 líneas): Considere elegir el tema de "Biblioteca Musical" porque creo que es un es un buen proyecto para aplicar los temas vistos en clase hasta el momento. El dominio resulta fácil de comprender y permite representar canciones mediante datos simples inicialmente, como titulo, artista, album, genero, año y duracion.
Considero que es un tema claro para posteriormente ir incorporando los demas apartados.


## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: `show_version(id)`. Recibe el ID de una cancion, busca la cancion en el catalogo y muestra los datos junto con sus versiones derivadas 
- Caso base: ocurre cuando la cancion no tiene versiones derivadas. En ese caso, `version_derivada` es una lista vacia, por ende no entra al bucle `for` y la funcion termina
- Caso recursivo: si la cancion tiene versiones derivadas, se recorren los IDs y se vuelve a llamar a `show_version(version_id)` para cada una
- Traza de un ejemplo real del dataset:
    ```text
    show_version(1)
        Busca ID 1
        Muestra "De Musica Ligera"
        version_derivada = [62]

        show_version(62)
            Busca ID 62
            Muestra "De Musica Ligera (Unplugged)"
            version_derivada = []
            Fin
    ```

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | insertar_al_inicio, insertar_al_final, insertar_ordenado, buscar, eliminar, tamanio, esta_vacia, iterador (__iter__) | Cada nodo apunta al siguiente y el último apunta a None. El tamaño registrado coincide con la cantidad de nodos. |
| Pila | apilar, desapilar, ver_tope, esta_vacia | El último elemento agregado es el primero en salir (LIFO). Los elementos se agregan y retiran por el inicio de la lista enlazada. |
| Cola | encolar, desencolar, ver_frente, esta_vacia | El primer elemento agregado es el primero en salir (FIFO). Los elementos se agregan al final y se retiran por el inicio de la lista enlazada. |

Dónde se usa cada uno en el dominio.
- **ListaEnlazada**: almacena los elementos de las estructuras sin utilizar una lista de Python como almacenamiento interno.
- **Pila**: representa el historial de reproducción de canciones. Permite consultar la última canción registrada y retirarla siguiendo el comportamiento LIFO.
- **Cola**: representa las canciones pendientes de reproducción. Permite consultar y reproducir la siguiente canción siguiendo el comportamiento FIFO.
- **Playlist**: representa la colección principal de canciones, implementada sobre ListaEnlazada, con una capacidad máxima de seis elementos. Si se intenta agregar una canción cuando está llena, se lanza ColeccionLlenaError.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
