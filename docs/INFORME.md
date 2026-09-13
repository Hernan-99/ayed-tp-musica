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
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

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
