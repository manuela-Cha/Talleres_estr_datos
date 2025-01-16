from Laboratorio_no_4.Lista_doble import DoubleList
from Laboratorio_no_2.Usuario import Usuario

class Ordenador_agenda:
    def __init__(self):
        self.L = DoubleList()

    def agregar_Usuario(self, u):
        self.L.addLast(u)

    def ordenar(self):
        if self.L.isEmpty() or self.L.size == 1:
            return  
        for i in range(self.L.size):
            nodo_actual = self.L.first()
            while nodo_actual and nodo_actual.next:
                if int(nodo_actual.data.getId()) > int(nodo_actual.next.data.getId()):
                    nodo_actual.data, nodo_actual.next.data = nodo_actual.next.data, nodo_actual.data
                nodo_actual = nodo_actual.next

    def mostrar(self):
        print(self.L)
