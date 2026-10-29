
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError


class Playlist:
    """Coleccion de canciones con capacidad maxima."""

    def __init__(self, capacity: int = 6):
        if capacity <= 0:
            raise ValueError("La capacidad debe ser mayor que cero")

        self._items = ListaEnlazada()
        self._capacity = capacity

    def agregar(self, song):
        if self._items.tamanio() >= self._capacity:
            raise ColeccionLlenaError("La playlist esta llena")

        self._items.insertar_al_final(song)

    def eliminar(self, song):
        return self._items.eliminar(song)

    def tamanio(self):
        return self._items.tamanio()

    def esta_vacia(self):
        return self._items.esta_vacia()

    def esta_llena(self):
        return self.tamanio() >= self._capacity

    def __iter__(self):
        return iter(self._items)
