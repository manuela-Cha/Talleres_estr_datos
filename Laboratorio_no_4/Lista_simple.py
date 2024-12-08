from Laboratorio_no_4.Nodo_simple import Node

class Lista_Simple:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def setSize(self, new_size):
        self.size = new_size

    def First(self):
        return self.head

    def Last(self):
        return self.tail

    def addFirst(self, data):
        nuevo_nodo = Node(data)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo
        if self.tail is None:
            self.tail = nuevo_nodo
        self.size += 1

    def addLast(self, data):
        nuevo_nodo = Node(data)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            self.tail = nuevo_nodo
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return data
    
    def encontrar_nodo(self, valor):
        temporal = self.head
        while temporal:
            if temporal.data == valor:
                return temporal
            temporal = temporal.next
        return None
    
    def __str__(self):
        temp = self.head
        resultado = ""
        while temp:
            resultado += str(temp.data) + " "
            temp = temp.next
        return resultado.strip()