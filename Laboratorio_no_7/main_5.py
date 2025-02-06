from Laboratorio_no_6.Actividad_1 import HEAP
from Laboratorio_no_6.Actividad_2 import PriorityQueue
import random
import time

def print_separator():
    print("\n" + "="*50 + "\n")

random.seed(42)  
data = [random.randint(1, 100) for _ in range(20)]

print_separator()

print("Datos aleatorios generados:")
print(f"Arreglo original: {data}")
print(f"Cantidad de elementos: {len(data)}")
print_separator()

print("1. PRUEBAS DE LA CLASE HEAP")
print("-" * 30)

heap = HEAP(30)

print("1.1 Prueba de build_max_heap")
heap.build_max_heap(data)
print(f"Heap después de build_max_heap: {heap.get_array()}")

def is_max_heap(arr, size, i=0):
    left = 2 * i + 1
    right = 2 * i + 2
    is_heap = True
    
    if left < size:
        if arr[i] < arr[left]:
            return False
        is_heap = is_max_heap(arr, size, left)
    
    if right < size:
        if arr[i] < arr[right]:
            return False
        is_heap &= is_max_heap(arr, size, right)
    
    return is_heap

print(f"¿Es un max heap válido? {'Sí' if is_max_heap(heap.A, heap.size) else 'No'}")
print_separator()

print("1.2 Prueba de heap_sort")
print(f"Arreglo antes de heap_sort: {heap.get_array()}")
heap.heap_sort()
print(f"Arreglo después de heap_sort: {heap.get_array()}")
print(f"¿Está ordenado correctamente? {'Sí' if heap.get_array() == sorted(data) else 'No'}")
print_separator()

print("2. PRUEBAS DE LA CLASE PRIORITY QUEUE")
print("-" * 30)

pq = PriorityQueue(30)

print("2.1 Prueba de max_heap_insert")
print("Insertando elementos uno por uno...")
for num in data:
    pq.max_heap_insert(num)
    print(f"Insertado {num}, cola actual: {pq.get_elements()}")
print_separator()

print("2.2 Prueba de heap_maximum")
max_value = pq.heap_maximum()
print(f"Elemento máximo (sin extraer): {max_value}")
print(f"Cola después de heap_maximum: {pq.get_elements()}")
print_separator()

print("2.3 Prueba de heap_extract_max")
print("Extrayendo los 5 elementos máximos...")
extracted = []
for _ in range(5):
    max_value = pq.heap_extract_max()
    extracted.append(max_value)
    print(f"Extraído {max_value}, cola actual: {pq.get_elements()}")
print(f"Elementos extraídos en orden: {extracted}")
print_separator()

print("2.4 Prueba de heap_increase_key")
print(f"Cola antes de increase_key: {pq.get_elements()}")
index_to_increase = 2 
old_value = pq.heap.A[index_to_increase]
new_value = old_value + 50
print(f"Aumentando valor en posición {index_to_increase} de {old_value} a {new_value}")
pq.heap_increase_key(index_to_increase, new_value)
print(f"Cola después de increase_key: {pq.get_elements()}")
print_separator()

print("2.5 Prueba de manejo de errores")
print("Intentando extraer de una cola vacía...")
try:
    empty_pq = PriorityQueue(5)
    empty_pq.heap_extract_max()
except ValueError as e:
    print(f"Error capturado correctamente: {e}")

print("\nIntentando insertar en una cola llena...")
try:
    small_pq = PriorityQueue(2)
    small_pq.max_heap_insert(1)
    small_pq.max_heap_insert(2)
    small_pq.max_heap_insert(3)  # Debería lanzar error
except ValueError as e:
    print(f"Error capturado correctamente: {e}")

print("\nIntentando disminuir una clave...")
try:
    pq.heap_increase_key(0, 1) 
except ValueError as e:
    print(f"Error capturado correctamente: {e}")