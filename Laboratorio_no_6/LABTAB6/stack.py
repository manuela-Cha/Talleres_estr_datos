from nodo_simple import NodoSimple, ListaSimple

class SilentListaSimple(ListaSimple):
    def imprimir(self):
        pass

class Stack:
    def __init__(self):
        self.lista = SilentListaSimple()
        self._size = 0

    def push(self, dato):
        self.lista.agregar_al_inicio(dato)
        self._size += 1

    def pop(self):
        dato = self.lista.eliminar_del_inicio()
        if dato is not None:
            self._size -= 1
        return dato

    def is_empty(self):
        return self.lista.cabeza is None

    def size(self):
        return self._size

    def top(self):
        if self.lista.cabeza is None:
            return None
        return self.lista.cabeza.dato

    def print_stack(self):
        current = self.lista.cabeza
        while current is not None:
            print(current.dato, end=" <- ")
            current = current.siguiente
        print("None")

# Crear la pila y agregar los valores 2, 4, 6, 8, 10
stack = Stack()
for valor in [2, 4, 6, 8, 10]:
    stack.push(valor)

# Imprimir la pila original
print("Pila original:")
stack.print_stack()

# Desapilar paso a paso e imprimir el estado de la pila
print("\npaso a paso:")
while not stack.is_empty():
    stack.pop()
    stack.print_stack()
