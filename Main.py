from Dijkstra import Dijkstra
from Grafo import Grafo


grafo = Grafo()
opcion = 0

while opcion != 5:
    opcion = int(input("Digite la opción que requiera:\n"
                       "1. Agragar ciudad \n" 
                       "2. Agregar ruta\n"
                       "3. Ver vuelos\n"
                       "4. Ver vuelo más corto\n" 
                       "5. Salir: \n"))
    
    match opcion:
        case 1:
            ciudad = input("Ingrese el nombre de la ciudad: ")
            if grafo.agregar_vertice(ciudad):
                print("Ciudad agregada correctamente.")
            else:
                print("La ciudad ya se encuentra registrada.")
        case 2:
            ciudad_inicio = input("Ingrese la ciudad de partida: ")
            if grafo.buscar_vertice(ciudad_inicio):
                ciudad_destino = input("Ingrese la ciudad de destino: ")
                if grafo.buscar_vertice(ciudad_destino):
                    try:
                        costo = int(input("Ingrese el costo de la ruta: "))
                        grafo.agregar_arista(ciudad_inicio, ciudad_destino, costo)
                    except:
                        print("El costo debe ser un entero.")
                else:
                    print("La ciudad no se encuentra registrada.")
            else:
                print("La ciudad no se encuentra registrada.")
        case 3:
            print(grafo)
        case 4:
            ciudad_inicio = input("Ingrese la ciudad de partida: ")
            if grafo.buscar_vertice(ciudad_inicio):
                ciudad_destino = input("Ingrese la ciudad de destino: ")
                if grafo.buscar_vertice(ciudad_destino):
                    dijikstra = Dijkstra(grafo, ciudad_inicio)
                    costo = dijikstra.ruta_mas_corta(ciudad_destino)
                    print(f"El vuelo más barato desde {ciudad_inicio} hasta {ciudad_destino} cuesta  ${costo}")
                else:
                    print("La ciudad no se encuentra registrada.")
            else:
                print("La ciudad no se encuentra registrada.")
        case 5:
            print("Saliendo...")
                    
            
            
                
            