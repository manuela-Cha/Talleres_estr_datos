from nodo_simple import NodoSimple, ListaSimple

class Queue:
    def __init__(self):
        self.lista = ListaSimple()
        self._size = 0

    def enqueue(self, dato):
        self.lista.agregar(dato)
        self._size += 1

    def dequeue(self):
        dato = self.lista.eliminar_del_inicio()
        if dato is not None:
            self._size -= 1
        return dato

    def is_empty(self):
        return self.lista.cabeza is None

    def size(self):
        return self._size

    def front(self):
        if self.lista.cabeza is None:
            return None
        return self.lista.cabeza.dato

    def print_queue(self):
        current = self.lista.cabeza
        print("Frente -> ", end="")
        while current is not None:
            print(current.dato, end=" -> ")
            current = current.siguiente
        print("None")

# Crear la cola y agregar los valores 2, 4, 6, 8, 10
queue = Queue()
for valor in [2, 4, 6, 8, 10]:
    queue.enqueue(valor)

# Imprimir la cola original
print("Cola original:")
queue.print_queue()

# Desencolar paso a paso e imprimir el estado de la cola
print("\nDesencolando paso a paso:")
while not queue.is_empty():
    queue.dequeue()
    queue.print_queue()
