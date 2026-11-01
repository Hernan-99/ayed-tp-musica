def ordenar_seleccion(coleccion, clave):
    """Ordenamiento por selección. Devuelve una nueva secuencia, no usa sorted."""

    n = len(coleccion)
    for i in range(n - 1):
        min_index =  i

        # busco el elemento mas chico de la parte no ordenada
        for j in range(i + 1, n):
            if clave(coleccion[j]) < clave(coleccion[min_index]):
                min_index = j

        # coloco el elemento mas chico en su posicion
        coleccion[i], coleccion[min_index] = (
            coleccion[min_index],
            coleccion[i],
        )

    return coleccion


def ordenar_insercion(coleccion, clave):
    """Ordenamiento por inserción. Devuelve una nueva secuencia, no usa sorted."""

    for i in range(1, len(coleccion)):
        current = coleccion[i]
        j = i - 1

        # desplazo los elementos mayores hacia la derecha
        while j >= 0 and clave(coleccion[j]) > clave(current):
            coleccion[j + 1] = coleccion[j]
            j -= 1

        # inserto el elemento en su posicion correspondiente
        coleccion[j + 1] = current

    return coleccion