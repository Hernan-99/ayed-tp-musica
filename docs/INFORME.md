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

Se implementó la persistencia del catálogo de la Biblioteca Musical mediante archivos de texto y archivos binarios. El objetivo es permitir almacenar, recuperar y modificar las canciones sin depender exclusivamente de los datos mantenidos en memoria durante la ejecución.

### 6.1. Persistencia en archivos de texto

Se implementaron las funciones `cargar_texto()` y `guardar_texto()` en el módulo `src/persistencia/texto.py`.

El archivo `data/canciones.txt` contiene el catálogo inicial. Cada fila representa una canción y utiliza los siguientes campos:

| Campo | Descripción |
| --- | --- |
| `id` | Identificador único de la canción. |
| `titulo` | Título de la canción. |
| `artista` | Nombre del artista o grupo. |
| `album` | Álbum al que pertenece. |
| `genero` | Género musical. |
| `anio` | Año de publicación. |
| `duracion_seg` | Duración expresada en segundos. |

La función `cargar_texto()` lee los registros y permite construir el catálogo inicial mediante `create_catalog_from_txt()`. La función `guardar_texto()` permite exportar el catálogo actualizado a `data/canciones_guardadas.txt`.

Se realizan validaciones sobre la estructura de los datos y se utiliza `ArchivoInvalidoError` para informar errores de formato.

### 6.2. Formato del archivo binario

El catálogo se almacena en `data/canciones.bin` mediante registros de longitud fija, utilizando el módulo `struct` de Python.

**Cabecera del archivo:**

| Campo | Formato `struct` | Tamaño |
| --- | --- | --- |
| Identificador mágico | `4s` | 4 bytes |
| Identificador de tema | `1s` | 1 byte |
| Cantidad de registros | `I` | 4 bytes |
| **Total** | **`<4s1sI`** | **9 bytes** |

- Identificador mágico: `AYED`.
- Identificador de tema: `M`, correspondiente a Biblioteca Musical.
- Cantidad de registros: número de canciones almacenadas.
- El símbolo `<` indica orden de bytes *little-endian* y tamaños estándar sin relleno automático.

**Layout de cada registro:**

| Campo | Formato `struct` | Tamaño |
| --- | --- | --- |
| `id` | `I` | 4 bytes |
| `titulo` | `30s` | 30 bytes |
| `artista` | `60s` | 60 bytes |
| `album` | `30s` | 30 bytes |
| `genero` | `12s` | 12 bytes |
| `anio` | `H` | 2 bytes |
| `duracion_seg` | `H` | 2 bytes |
| **Total** | **`<I30s60s30s12s2H`** | **140 bytes** |

Los campos de texto se codifican en UTF-8 y se completan con bytes nulos (`\x00`) hasta alcanzar su longitud fija. El campo `genero` almacena el nombre del género musical en 12 bytes, aunque dentro del programa se representa mediante un identificador numérico del 1 al 6. Durante la lectura, el nombre se convierte nuevamente a su identificador correspondiente.

Los campos numéricos se almacenan mediante enteros sin signo.

El tamaño total del archivo se calcula mediante:

`Tamaño total = 9 + (140 × cantidad de registros)`

Para un catálogo de 67 canciones, el tamaño esperado es:

`9 + (140 × 67) = 9389 bytes`

### 6.3. Operaciones de persistencia binaria

Se implementaron las siguientes funciones en `src/persistencia/binario.py`:

| Función | Descripción |
| --- | --- |
| `guardar_binario()` | Escribe la cabecera y todos los registros del catálogo. |
| `cargar_binario()` | Lee y valida el archivo binario para reconstruir el catálogo. |
| `actualizar_registro()` | Modifica un registro específico mediante acceso directo. |
| `alta_binario()` | Incorpora una canción al archivo binario. |
| `baja_binario()` | Elimina una canción del archivo binario. |

Las operaciones están disponibles desde la opción 9 del menú principal, que permite guardar, cargar, agregar, eliminar y modificar canciones.

### 6.4. Actualización de un registro por posición

La modificación de una canción se realiza mediante acceso directo al archivo binario, sin necesidad de reescribir todos sus registros.

Como los registros tienen longitud fija, la posición de un registro se calcula mediante:

`Desplazamiento = tamaño_cabecera + (posición × tamaño_registro)`

En este proyecto:

`Desplazamiento = 9 + (posición × 140)`

La posición comienza en cero. Por ejemplo, el tercer registro se encuentra en el desplazamiento:

`9 + (2 × 140) = 289 bytes`

La función `actualizar_registro()` utiliza `seek()` para posicionarse en el desplazamiento calculado y sobrescribir únicamente el registro correspondiente.

Antes de realizar la modificación, se valida la cabecera, se comprueba que la posición solicitada esté dentro del rango permitido y se verifica que el tamaño del archivo coincida con la cantidad de registros declarada.

Esta operación mantiene constante el tamaño del archivo y evita reescribir el catálogo completo.

### 6.5. Alta y baja de canciones

**Alta:** la función `alta_binario()` valida la cabecera y el tamaño del archivo, verifica que no exista otra canción con el mismo identificador y agrega el nuevo registro al final. Posteriormente, actualiza la cantidad de registros almacenada en la cabecera.

**Baja:** la función `baja_binario()` carga el catálogo desde el archivo binario, recorre las canciones y construye una nueva colección excluyendo aquella cuyo identificador coincide con el solicitado. Si el ID no existe, se informa mediante `ArchivoInvalidoError`. Si existe, se reescribe el archivo completo mediante `guardar_binario()`, actualizando automáticamente la cantidad de registros de la cabecera.

A diferencia de la modificación, que utiliza acceso directo mediante `seek()`, la baja requiere reescribir el archivo para conservar la estructura de registros consecutivos.

Después de las operaciones de alta, baja y modificación, el programa sincroniza el catálogo en memoria y actualiza la exportación de texto mediante `save_catalog_text()`.

### 6.6. Validación de archivos

Durante la lectura se comprueba que el archivo binario tenga una estructura válida. Entre las situaciones contempladas se encuentran:

- Cabecera incompleta o con identificador mágico incorrecto.
- Identificador de tema distinto de `M`.
- Archivo binario truncado o con registros incompletos.
- Género musical no reconocido.
- Presencia de bytes adicionales después del último registro declarado en la cabecera.
- Archivo de texto con una estructura inválida.

Ante estas situaciones, se utiliza la excepción `ArchivoInvalidoError` para informar el problema y evitar trabajar con registros inconsistentes.

### 6.7. Integración con el catálogo

Al iniciar el programa, se comprueba si existe `data/canciones.bin`. Si está disponible, se carga el catálogo desde ese archivo; de lo contrario, se utiliza `data/canciones.txt`.

Las relaciones entre canciones originales y versiones derivadas se recuperan desde `data/versiones.txt` y se vinculan con las canciones existentes mediante `restore_song_versions()`.

De esta manera, el programa conserva la funcionalidad desarrollada en entregas anteriores y permite recuperar los datos persistidos entre ejecuciones.

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
