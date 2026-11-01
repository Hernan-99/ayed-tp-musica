

def busqueda_lineal(coleccion, clave, obtener_clave):
    """Devuelve el ítem cuya clave coincide, o None."""

    # Recorremos la coleccion elemento por elemento
    for item in coleccion:
        if obtener_clave(item) == clave: # obtengo clave de elemento
            return item
    return None # si termina el loop y no encuentra, devuelve None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave."""
    left = 0
    right = len(coleccion_ordenada) - 1

    while left <= right:
        middle = (left + right) // 2
        current_key = obtener_clave(coleccion_ordenada[middle])

        if current_key == clave:
            return coleccion_ordenada[middle]
        elif current_key < clave:
            left = middle + 1
        else:
            right = middle - 1

    return None