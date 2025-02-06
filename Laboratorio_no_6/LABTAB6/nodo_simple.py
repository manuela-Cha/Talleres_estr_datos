class NodoSimple:
    def __init__(self, dato=None):
        self.dato = dato  
        self.siguiente = None  
        
class ListaSimple:
    def __init__(self):
        self.cabeza = None  

    def agregar(self, dato):
        nuevo_nodo = NodoSimple(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo  
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo  
            
    def eliminar(self, dato):
        if not self.cabeza:
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return

        nodo_actual = self.cabeza
        while nodo_actual.siguiente and nodo_actual.siguiente.dato != dato:
            nodo_actual = nodo_actual.siguiente
        
        if nodo_actual.siguiente:
            nodo_actual.siguiente = nodo_actual.siguiente.siguiente  

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def agregar_al_inicio(self, dato):
        nuevo_nodo = NodoSimple(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar_del_inicio(self):
        if self.cabeza is None:
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        return dato

# Crear la lista simple
lista_simple = ListaSimple()

# Agregar números pares del 1 al 20
for num in range(2, 21, 2):
    lista_simple.agregar(num)

# Eliminar los números 1, 10 y 20
lista_simple.eliminar(1)
lista_simple.eliminar(10)
lista_simple.eliminar(20)
