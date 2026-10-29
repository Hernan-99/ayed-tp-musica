from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        self._items.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self._items.extraer_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede consultar una cola vacía")
        return self._items.ver_primero()

    def esta_vacia(self):
        return self._items.esta_vacia()

    def __iter__(self):
        return iter(self._items)