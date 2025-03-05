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

# Cargar el grafo desde el archivo CSV
grafo, nodos = cargar_grafo('Datos vias.csv')
distancia_fw, siguiente_fw = floyd_warshall(grafo, nodos, 'distancia')
tiempo_fw, siguiente_fw_tiempo = floyd_warshall(grafo, nodos, 'tiempo')

def main():
    print("Ingrese las ciudades de inicio y fin:")
    ciudad_inicio = input("Ciudad de inicio: ")
    ciudad_fin = input("Ciudad de fin: ")
    
    if ciudad_inicio in nodos and ciudad_fin in nodos:
        camino_distancia = reconstruir_camino(siguiente_fw, ciudad_inicio, ciudad_fin)
        camino_tiempo = reconstruir_camino(siguiente_fw_tiempo, ciudad_inicio, ciudad_fin)
        
        print(f"Camino más corto por distancia: {camino_distancia}, Distancia: {distancia_fw[ciudad_inicio][ciudad_fin]}")
        print(f"Camino más corto por tiempo: {camino_tiempo}, Minutos: {tiempo_fw[ciudad_inicio][ciudad_fin]}")
    else:
        print("Una o ambas ciudades no se encuentran en el grafo.")

if __name__ == "__main__":
    main()
