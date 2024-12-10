from Laboratorio_no_4.Lista_simple import Lista_Simple
import random

class OrdenarLista:
    def __init__(self):
        self.lista = Lista_Simple()
        pass

    def inicializar(self, n):
        for i in range(n):
            self.lista.addLast(random.randint(0, 100))  

    def ordenar(self):
        if self.lista.size == 0:
            return

        nodo_externo = self.lista.First()
        while nodo_externo:
            min_nodo = nodo_externo
            nodo_interno = nodo_externo.next

            while nodo_interno:
                if nodo_interno.data < min_nodo.data:
                    min_nodo = nodo_interno
                nodo_interno = nodo_interno.next

            nodo_externo.data, min_nodo.data = min_nodo.data, nodo_externo.data
            nodo_externo = nodo_externo.next

    def mostrar(self):
        print(self.lista)  
