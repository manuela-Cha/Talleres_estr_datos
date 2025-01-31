from Laboratorio_no_6.Actividad_1 import HEAP
class PriorityQueue:
    def __init__(self, capacity):
        """
        Inicializa una cola de prioridad vacía usando un MAX-HEAP.
        """
        self.heap = HEAP(capacity)
        
    def heap_maximum(self):
        """
        Retorna el elemento con mayor prioridad sin eliminarlo.
        Lanza una excepción si la cola está vacía.
        """
        if self.heap.size == 0:
            raise ValueError("La cola de prioridad está vacía")
        return self.heap.A[0]
    
    def heap_extract_max(self):
        """
        Elimina y retorna el elemento con mayor prioridad.
        Lanza una excepción si la cola está vacía.
        """
        if self.heap.size == 0:
            raise ValueError("La cola de prioridad está vacía")
            
        max_element = self.heap.A[0]
        self.heap.A[0] = self.heap.A[self.heap.size - 1]
        self.heap.size -= 1
        self.heap.max_heapify(0)
        
        return max_element
    
    def heap_increase_key(self, i, key):
        """
        Aumenta la clave del elemento en la posición i al nuevo valor key.
        Lanza una excepción si la nueva clave es menor que la actual.
        """
        if key < self.heap.A[i]:
            raise ValueError("La nueva clave es menor que la clave actual")
            
        self.heap.A[i] = key
        
        while i > 0 and self.heap.A[self.heap.parent(i)] < self.heap.A[i]:
            self.heap.A[i], self.heap.A[self.heap.parent(i)] = \
                self.heap.A[self.heap.parent(i)], self.heap.A[i]
            i = self.heap.parent(i)
    
    def max_heap_insert(self, key):
        """
        Inserta un nuevo elemento con la clave especificada.
        Lanza una excepción si la cola está llena.
        """
        if self.heap.size >= len(self.heap.A):
            raise ValueError("La cola de prioridad está llena")
            
        self.heap.size += 1
        self.heap.A[self.heap.size - 1] = float('-inf')  # Valor temporal mínimo
        self.heap_increase_key(self.heap.size - 1, key)
    
    def get_size(self):
        """
        Retorna el número actual de elementos en la cola.
        """
        return self.heap.size
    
    def get_elements(self):
        """
        Retorna la lista de elementos actuales en la cola.
        """
        return self.heap.get_array()