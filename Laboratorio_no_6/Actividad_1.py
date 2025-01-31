class HEAP:
    def __init__(self, capacity):
        """
        Inicializa un heap vacío con una capacidad máxima.
        """
        self.A = [None] * capacity  
        self.size = 0               
    
    def parent(self, i):
        """
        Retorna la posición del padre del nodo i.
        """
        return (i - 1) // 2
    
    def left(self, i):
        """
        Retorna la posición del hijo izquierdo del nodo i.
        """
        return 2 * i + 1
    
    def right(self, i):
        """
        Retorna la posición del hijo derecho del nodo i.
        """
        return 2 * i + 2
    
    def max_heapify(self, i):
        """
        Mantiene la propiedad del heap dado una posición i.
        """
        largest = i
        left = self.left(i)
        right = self.right(i)
        
        if left < self.size and self.A[left] > self.A[largest]:
            largest = left
            
        if right < self.size and self.A[right] > self.A[largest]:
            largest = right
            
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)
    
    def build_max_heap(self, B):
        """
        Construye un heap a partir de un arreglo no ordenado.
        """
        if len(B) > len(self.A):
            raise ValueError("El arreglo es demasiado grande para la capacidad del heap")
        
        for i in range(len(B)):
            self.A[i] = B[i]
        self.size = len(B)
        
        for i in range(self.size // 2 - 1, -1, -1):
            self.max_heapify(i)
    
    def heap_sort(self):
        """
        Implementa el algoritmo de ordenamiento heapsort.
        """
        original_size = self.size
        
        for i in range(self.size - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            
            self.size -= 1
            self.max_heapify(0)
            
        self.size = original_size

    def get_array(self):
        """
        Retorna el arreglo interno.
        """
        return self.A[:self.size]