from Laboratorio_no_4.Nodo_doble import DoubleNode

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def addFirst(self, data):
        new_node = DoubleNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addLast(self, data):
        new_node = DoubleNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            print("La lista está vacía, no se puede eliminar el primer nodo.")
            return None
        
        data = self.head.data
        if self.head == self.tail:  # Solo queda un nodo
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        print(f"Primer nodo con valor {data} eliminado. Nuevo tamaño: {self.size}")
        return data



    def removeLast(self):
        if self.isEmpty():
            print("La lista está vacía, no se puede eliminar el último nodo.")
            return None
        
        data = self.tail.data
        if self.head == self.tail:  # Solo queda un nodo
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        print(f"Último nodo con valor {data} eliminado. Nuevo tamaño: {self.size}")
        return data


    def remove(self, node):
        """Elimina un nodo específico de la lista doblemente enlazada."""
        if self.isEmpty() or node is None:
            return None

        # Caso 1: El nodo es el primero (head)
        if node == self.head:
            self.head = node.next
            if self.head:  # Si hay un siguiente nodo, desvincula el anterior
                self.head.prev = None
            else:  # Si no hay, la lista queda vacía
                self.tail = None

        # Caso 2: El nodo es el último (tail)
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:  # Si hay un nodo previo, desvincula el siguiente
                self.tail.next = None
            else:  # Si no hay, la lista queda vacía
                self.head = None

        # Caso 3: El nodo está en el medio
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

        # Limpia referencias del nodo eliminado
        node.next = node.prev = None
        self.size -= 1  # Actualiza el tamaño de la lista
        return node.data  # Retorna los datos del nodo eliminado



    def addAfter(self, node, data):
        if node is None:
            return
        new_node = DoubleNode(data)
        if node == self.tail:
            self.addLast(data)
        else:
            new_node.prev = node
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
            self.size += 1

    def addBefore(self, node, data):
        if node is None:
            return
        new_node = DoubleNode(data)
        if node == self.head:
            self.addFirst(data)
        else:
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node
            self.size += 1

    def encontrar_nodo(self, valor):
        temporal = self.head
        while temporal:
            if temporal.data == valor:
                return temporal
            temporal = temporal.next
        return None
    
    def obtener_nodo_en_posicion(self, posicion):
        if posicion < 0 or posicion >= self.size:
            return None

        nodo_actual = self.head
        for _ in range(posicion):
            nodo_actual = nodo_actual.next

        return nodo_actual

    def __str__(self):
        temp = self.head
        resultado = ""
        while temp:
            resultado += str(temp.data)
            temp = temp.next
        return resultado.strip()



