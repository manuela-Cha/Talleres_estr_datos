import csv

def cargar_grafo(archivo):
    grafo = {}
    nodos = set()
    with open(archivo, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)  # Omitir encabezado si lo hay
        for fila in reader:
            if len(fila) < 4:
                continue
            ciudad1, ciudad2, distancia, tiempo = fila
            distancia, tiempo = float(distancia), float(tiempo)
            nodos.update([ciudad1, ciudad2])
            
            if ciudad1 not in grafo:
                grafo[ciudad1] = {}
            if ciudad2 not in grafo:
                grafo[ciudad2] = {}
            
            grafo[ciudad1][ciudad2] = {'distancia': distancia, 'tiempo': tiempo}
            grafo[ciudad2][ciudad1] = {'distancia': distancia, 'tiempo': tiempo}
    return grafo, list(nodos)

def floyd_warshall(grafo, nodos, criterio):
    dist = {i: {j: float('inf') for j in nodos} for i in nodos}
    next_node = {i: {j: None for j in nodos} for i in nodos}
    
    for i in nodos:
        dist[i][i] = 0
    
    for i in grafo:
        for j in grafo[i]:
            dist[i][j] = grafo[i][j][criterio]
            next_node[i][j] = j
    
    for k in nodos:
        for i in nodos:
            for j in nodos:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
    
    return dist, next_node

def reconstruir_camino(next_node, inicio, fin):
    if next_node[inicio][fin] is None:
        return None
    camino = [inicio]
    while inicio != fin:
        inicio = next_node[inicio][fin]
        camino.append(inicio)
    return camino

def estan_conectadas_directamente(grafo, ciudad_a, ciudad_b):
    if ciudad_a not in grafo or ciudad_b not in grafo:
        return False, None
    
    if ciudad_b in grafo[ciudad_a]:
        return True, grafo[ciudad_a][ciudad_b]
    
    return False, None

# Cargar el grafo desde el archivo CSV
grafo, nodos = cargar_grafo('Practica_2/Datos_vias.csv')
distancia_fw, siguiente_fw = floyd_warshall(grafo, nodos, 'distancia')
tiempo_fw, siguiente_fw_tiempo = floyd_warshall(grafo, nodos, 'tiempo')

def main():
    while True:
        print("\nMenu de Opciones:")
        print("1. Buscar camino mas corto")
        print("2. Verificar conexion directa entre ciudades")
        print("3. Salir")
        
        opcion = input("Seleccione una opcion (1-3): ")
        
        if opcion == '1':
            print("\nIngrese las ciudades de inicio y fin:")
            ciudad_inicio = input("Ciudad de inicio: ")
            ciudad_fin = input("Ciudad de fin: ")
            
            if ciudad_inicio in nodos and ciudad_fin in nodos:
                camino_distancia = reconstruir_camino(siguiente_fw, ciudad_inicio, ciudad_fin)
                camino_tiempo = reconstruir_camino(siguiente_fw_tiempo, ciudad_inicio, ciudad_fin)
                
                print(f"Camino más corto por distancia: {camino_distancia}, Distancia: {distancia_fw[ciudad_inicio][ciudad_fin]}")
                print(f"Camino más corto por tiempo: {camino_tiempo}, Minutos: {tiempo_fw[ciudad_inicio][ciudad_fin]}")
            else:
                print("Una o ambas ciudades no se encuentran en el grafo.")
        
        elif opcion == '2':
            print("\nVerificar conexión directa entre ciudades:")
            ciudad_a = input("Ingrese la primera ciudad: ")
            ciudad_b = input("Ingrese la segunda ciudad: ")
            
            conectadas, info_carretera = estan_conectadas_directamente(grafo, ciudad_a, ciudad_b)
            
            if conectadas:
                print(f"\n{ciudad_a} y {ciudad_b} están conectadas directamente.")
                print(f"Información de la carretera:")
                print(f"Distancia: {info_carretera['distancia']} km")
                print(f"Tiempo de viaje: {info_carretera['tiempo']} minutos")
            else:
                print(f"\n{ciudad_a} y {ciudad_b} NO están conectadas directamente.")
        
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()