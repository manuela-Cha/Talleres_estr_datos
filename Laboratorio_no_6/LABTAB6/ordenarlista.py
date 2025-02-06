import random

class Nodo:
    """Clase que representa un nodo de la lista simple"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    """Clase que representa una lista simple"""
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        """Agrega un nodo al final de la lista"""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        """Muestra todos los valores de la lista"""
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def convertir_a_lista(self):
        """Convierte la lista simple en una lista de Python"""
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente
        return lista

    def actualizar_desde_lista(self, lista):
        """Actualiza los valores de la lista simple desde una lista de Python"""
        self.cabeza = None
        for dato in lista:
            self.agregar(dato)

class ORDENADOR_LISTA:
    def __init__(self):
        """Constructor que inicializa una lista simple"""
        self.L = ListaSimple()

    def inicializar(self, n):
        """Llena la lista con valores aleatorios"""
        for _ in range(n):
            self.L.agregar(random.randint(1, 100))

    def ordenar(self):
        """Ordena la lista simple usando el método de burbuja"""
        lista = self.L.convertir_a_lista()
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        self.L.actualizar_desde_lista(lista)

    def mostrar(self):
        """Muestra los valores de la lista simple"""
        self.L.mostrar()

# Ejemplo de uso de la clase ORDENADOR_LISTA
if __name__ == "__main__":
    # Paso 1: Crear un objeto ORDENADOR_LISTA
    O = ORDENADOR_LISTA()

    # Paso 2: Inicializar la lista con 12 valores aleatorios
    O.inicializar(12)

    # Paso 3: Mostrar la lista original
    print("Lista original:")
    O.mostrar()

    # Paso 4: Ordenar la lista
    O.ordenar()

    # Paso 5: Mostrar la lista ordenada
    print("\nLista ordenada:")
    O.mostrar()
