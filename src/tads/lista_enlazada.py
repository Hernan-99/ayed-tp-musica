import re

from src.tads.nodo import Nodo

class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self):
        self._cabeza = None # indica que inicialmente la lista no tiene nodo
        self._tamanio = 0 # establece que inicialmente tenemos cero elementos

    def esta_vacia(self):
        return self._cabeza is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        new_node = Nodo(dato, self._cabeza)
        self._cabeza = new_node
        self._tamanio += 1

    def insertar_al_final(self, dato):
      new_node = Nodo(dato)
      if self.esta_vacia():
          self._cabeza = new_node
      else:
          current = self._cabeza
          while current.siguiente is not None:
              current = current.siguiente
          current.siguiente = new_node
      self._tamanio += 1

    def insertar_ordenado(self, dato, clave):
        new_node = Nodo(dato)
        if self.esta_vacia() or clave(dato) < clave(self._cabeza.dato):
            new_node.siguiente = self._cabeza
            self._cabeza = new_node
        else:
            current = self._cabeza
            while (
                current.siguiente is not None
                and clave(current.siguiente.dato) <= clave(dato)
            ):
                current = current.siguiente
            new_node.siguiente = current.siguiente
            current.siguiente = new_node

        self._tamanio += 1

    def eliminar(self, dato):
        prev = None
        current = self._cabeza

        while current is not None:
            if current.dato == dato:
                if prev is None:
                    self._cabeza = current.siguiente
                else:
                    prev.siguiente = current.siguiente

                self._tamanio -= 1
                return True

            prev = current
            current = current.siguiente

        return False

    def buscar(self, dato):
        for current in self:
            if current == dato:
                return current
        return None

    def __iter__(self):
        current = self._cabeza

        while current is not None:
            yield current.dato
            current = current.siguiente

    ## ----- METODOS EXTRA -----
    # método para extraer el dato del primer nodo, mover la cabeza al siguiente nodo y reducir el tamaño.
    def extraer_primero(self):
        if self.esta_vacia():
            raise IndexError("La lista esta vacia")

        data = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1

        return data

    # metodo para ver el primer elemento sin eliminarlo
    def ver_primero(self):
        if self.esta_vacia():
            raise IndexError("La lista esta vacia")

        return self._cabeza.dato