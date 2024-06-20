import heapq
class Dijkstra:
    def __init__(self, grafo, inicio):
        self.grafo = grafo
        self.inicio = inicio
        
    def ruta_mas_corta(self, destino):
        
        costos = {vertice: float('infinity') for vertice in self.grafo.vertices}
        costos[self.inicio] = 0
        prioridad_cola = [(0, self.inicio)]
        
        heapq.heapify(prioridad_cola)

        while prioridad_cola:
            costo_actual, vertice_actual = heapq.heappop(prioridad_cola)
            if costo_actual > costos[vertice_actual]:
                continue
            for costo, vecino in self.grafo.vertices[vertice_actual]:
                costo_total = costo_actual + costo
                if costo_total < costos[vecino]:
                    costos[vecino] = costo_total
                    heapq.heappush(prioridad_cola, (costo_total, vecino))

        return costos[destino]
    

        