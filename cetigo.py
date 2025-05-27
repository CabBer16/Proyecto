import heapq

grafo = {
    "Plaza Patria": {"Glorieta Minerva": 12},
    "Tonalá – Plaza Cihualpilli": {"Paradero Tlaquepaque": 20},
    "Paradero Tlaquepaque": {"Glorieta Minerva": 18},
    "Glorieta Minerva": {"Plaza del Sol": 10},
    "Plaza del Sol": {"Zapopan Norte": 15},
    "Zapopan Norte": {"CETI Colomos": 20},
}

grafoss = {
    "Plaza Patria": {"Glorieta Minerva": 12},
    "Tonalá": {"Paradero Tlaquepaque": 20},
    "Paradero Tlaquepaque": {"Glorieta Minerva": 18},
    "Glorieta Minerva": {"Plaza del Sol": 10},
    "Plaza del Sol": {"Zapopan Norte": 15},
    "Zapopan Norte": {"CETI Colomos": 20},
}

horarios_salida = [
    "06:30 AM",
    "07:50 AM",
    "08:40 AM",
    "9:30 AM"
]

def dijkstra(inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        (dist_actual, actual) = heapq.heappop(cola)

        for vecino, peso in grafo.get(actual, {}).items():
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias.get(vecino, float('inf')):
                distancias[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))

    return distancias.get(destino, float('inf'))

def mostrar_horarios():
    print("\nHorarios de salida del camión al CETI:")
    for h in horarios_salida:
        print(f"- {h}")

def mostrar_ruta():
    print("\nRuta fija del camión:")
    ruta = [
        "Tonalá",
        "Paradero Tlaquepaque",
        "Plaza del Sol",
        "Glorieta Minerva",
        "Zapopan Centro",
        "Plaza Patria",
        "CETI Colomos"
    ]
    for i, parada in enumerate(ruta):
        print(f"{i+1}. {parada}")

def calcular_tiempo_llegada():
    print("\nParadas disponibles:")
    for i, parada in enumerate(grafo.keys()):
        print(f"{i + 1}. {parada}")
    origen = input("Ingresa el nombre exacto de tu parada: ")

    if origen not in grafo:
        print("Parada no válida.")
        return

    tiempo_estimado = dijkstra(origen, "CETI Colomos")
    if tiempo_estimado == float('inf'):
        print("No hay ruta disponible desde esa parada.")
    else:
        print(f"Tiempo estimado de llegada al CETI desde {origen}: {tiempo_estimado} minutos")

def menu():
    while True:
        print("\nCETI GO")
        print("1. Ver horarios de salida")
        print("2. Ver ruta del camión")
        print("3. Ver tiempo estimado de llegada al CETI")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_horarios()
        elif opcion == "2":
            mostrar_ruta()
        elif opcion == "3":
            calcular_tiempo_llegada()
        elif opcion == "4":
            print("¡Gracias por usar CETI GO!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()
