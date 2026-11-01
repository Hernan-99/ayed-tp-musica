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
| Búsqueda lineal | O(n) | O(1) | Recorre los elementos uno por uno hasta encontrar la coincidencia o llegar al final de la colección. |
| Búsqueda binaria | O(log n) | O(1) | En cada iteración divide a la mitad el intervalo de búsqueda. Requiere que la colección esté ordenada previamente. |
| Ordenamiento por selección | O(n²) | O(1) | Utiliza dos ciclos anidados para encontrar el menor elemento de la parte no ordenada. |
| Ordenamiento por inserción | O(n²) | O(1) | En el peor caso debe desplazar los elementos anteriores para insertar cada elemento en su posición. |
| ListaEnlazada: insertar_al_inicio | O(1) | O(1) | Crea un nodo y actualiza la referencia a la cabeza. |
| ListaEnlazada: insertar_al_final | O(n) | O(1) | Recorre la lista hasta encontrar el último nodo. |
| ListaEnlazada: buscar / eliminar | O(n) | O(1) | Puede ser necesario recorrer todos los nodos para encontrar el elemento. |
| ListaEnlazada: insertar_ordenado | O(n) | O(1) | Recorre los nodos hasta encontrar la posición correspondiente. |
| ListaEnlazada: tamanio / esta_vacia | O(1) | O(1) | Consulta atributos almacenados directamente en la estructura. |
| Pila: apilar / desapilar / ver_tope | O(1) | O(1) | Las operaciones trabajan directamente sobre el primer nodo de la lista enlazada. |
| Cola: encolar | O(n) | O(1) | Inserta al final utilizando `insertar_al_final`, que recorre la lista. |
| Cola: desencolar / ver_frente | O(1) | O(1) | Accede directamente al primer nodo de la lista enlazada. |
| Playlist: agregar / eliminar | O(n) | O(1) | Agregar recorre la lista para insertar al final y eliminar puede recorrerla para encontrar la canción. |

*Nota: el espacio indicado corresponde al espacio auxiliar de cada operación, sin contar la estructura de datos ni la colección recibida. En el menú, los ordenamientos y la búsqueda binaria trabajan sobre una copia del catálogo, que requiere O(n) espacio adicional.*


Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| Búsqueda lineal | 67 | 0.00000934 |
| Búsqueda lineal | 670 | 0.00015726 |
| Búsqueda binaria | 67 | 0.00000247 |
| Búsqueda binaria | 670 | 0.00000407 |
| Ordenamiento por selección | 67 | 0.00063408 |
| Ordenamiento por selección | 670 | 0.07144154 |
| Ordenamiento por inserción | 67 | 0.00043978 |
| Ordenamiento por inserción | 670 | 0.07626102 |

Las mediciones muestran que la búsqueda binaria presenta un crecimiento reducido al aumentar el tamaño de la colección, mientras que la búsqueda lineal y los ordenamientos presentan incrementos mayores.

La búsqueda binaria se midió sobre una colección previamente ordenada, sin incluir el tiempo necesario para prepararla. En el menú, esa preparación se realiza mediante ordenamiento por inserción, por lo que la operación completa tiene una complejidad O(n²).



## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
