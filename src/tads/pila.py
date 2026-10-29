
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()
        
    def apilar(self, dato):
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self._items.extraer_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede consultar una pila vacia")
        return self._items.ver_primero()

    def esta_vacia(self):
        return self._items.esta_vacia()
