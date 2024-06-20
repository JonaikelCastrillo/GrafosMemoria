import heapq

class Grafo:

    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
            return True
        else:
            return False
        
    def buscar_vertice(self, vertice):
        if vertice in self.vertices:
            return True
        else:
            return False
        
    def agregar_arista(self, desde, hacia, costo):
        if desde in self.vertices and hacia in self.vertices:
            self.vertices[desde].append((costo, hacia))
            
    def __str__(self):
        return f"Vuelos: {self.vertices}"
    

