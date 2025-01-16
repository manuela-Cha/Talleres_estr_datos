from Laboratorio_no_4.Lista_simple import Lista_Simple
import random

class Ordenador:
    def __init__(self, capacity):
        self.A = Lista_Simple()  
        self.limit = capacity    

    def inicializar(self):
        for i in range(self.limit):
            self.A.addLast(random.randint(0,100))

    def mostrar(self):
        print(self.A)

    def ordenar_burbuja(self):
        if self.A.isEmpty():
            return
        for _ in range(self.A.size):
            nodo_actual = self.A.First()
            while nodo_actual and nodo_actual.next:
                if nodo_actual.data > nodo_actual.next.data:
                    nodo_actual.data, nodo_actual.next.data = nodo_actual.next.data, nodo_actual.data
                nodo_actual = nodo_actual.next

    def ordenar_seleccion(self):
        if self.A.isEmpty():
            return

        nodo_externo = self.A.First()
        while nodo_externo:
            min_nodo = nodo_externo
            nodo_interno = nodo_externo.next

            while nodo_interno:
                if nodo_interno.data < min_nodo.data:
                    min_nodo = nodo_interno
                nodo_interno = nodo_interno.next

            nodo_externo.data, min_nodo.data = min_nodo.data, nodo_externo.data
            nodo_externo = nodo_externo.next

    def insertar_en_orden(self, lista_ordenada, nodo):
        if lista_ordenada.isEmpty() or nodo.data < lista_ordenada.First().data:
            nodo.next = lista_ordenada.First()
            lista_ordenada.head = nodo
            if lista_ordenada.tail is None:
                lista_ordenada.tail = nodo
        else:
            nodo_actual = lista_ordenada.First()
            while nodo_actual.next and nodo_actual.next.data < nodo.data:
                nodo_actual = nodo_actual.next

            nodo.next = nodo_actual.next
            nodo_actual.next = nodo
            if nodo.next is None:
                lista_ordenada.tail = nodo

        lista_ordenada.size += 1

    def ordenar_insercion(self):
        if self.A.isEmpty() or self.A.size == 1:
            return  

        lista_ordenada = Lista_Simple()
        nodo_actual = self.A.First()
        while nodo_actual:
            siguiente_nodo = nodo_actual.next
            self.insertar_en_orden(lista_ordenada, nodo_actual)

            nodo_actual = siguiente_nodo

        self.A.head = lista_ordenada.head
        self.A.tail = lista_ordenada.tail
        self.A.size = lista_ordenada.size



    def ordenar_mergeSort(self):
        if self.A.size <= 1:
            return

        self.A.head = self.merge_sort(self.A.First())

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        medio = self.encontrar_nodo_medio(head)
        siguiente_medio = medio.next
        medio.next = None

        izquierda = self.merge_sort(head)
        derecha = self.merge_sort(siguiente_medio)

        return self.merge(izquierda, derecha)

    def merge(self, izquierda, derecha):
        if not izquierda:
            return derecha
        if not derecha:
            return izquierda

        if izquierda.data < derecha.data:
            resultado = izquierda
            resultado.next = self.merge(izquierda.next, derecha)
        else:
            resultado = derecha
            resultado.next = self.merge(izquierda, derecha.next)

        return resultado

    def encontrar_nodo_medio(self, head):
        if not head:
            return head

        lento = rapido = head
        while rapido.next and rapido.next.next:
            lento = lento.next
            rapido = rapido.next.next

        return lento

    def busqueda_binaria(self, valor):
        izquierda = 0
        derecha = self.A.size - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            nodo_medio = self.obtener_nodo_en_posicion(medio)

            if nodo_medio.data == valor:
                return medio  
            elif nodo_medio.data < valor:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return -1 

    def obtener_nodo_en_posicion(self, posicion):
        if posicion < 0 or posicion >= self.A.size:
            return None

        nodo_actual = self.A.First()
        for _ in range(posicion):
            nodo_actual = nodo_actual.next

        return nodo_actual
    
    def limpiar_ordenador(self):
        self.A = Lista_Simple()
