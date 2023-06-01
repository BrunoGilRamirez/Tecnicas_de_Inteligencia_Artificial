import heapq

# Función para calcular la distancia Euclidiana entre dos puntos
def distancia(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# Implementación del algoritmo A*
def a_star(mapa, inicio, objetivo):
    # Dimensiones del mapa
    filas, columnas = len(mapa), len(mapa[0])

    # Lista de nodos abiertos y cerrados
    abiertos = []
    cerrados = set()

    # Creamos el nodo de inicio con valor f = g + h = 0 + distancia(inicio, objetivo)
    nodo_actual = (0, inicio, None)
    heapq.heappush(abiertos, nodo_actual)

    # Bucle principal
    while abiertos:
        # Sacamos el nodo con menor valor f de la lista de abiertos
        nodo_actual = heapq.heappop(abiertos)

        # Si hemos llegado al objetivo, devolvemos la ruta
        if nodo_actual[1] == objetivo:
            ruta = []
            while nodo_actual[2] is not None:
                ruta.append(nodo_actual[1])
                nodo_actual = nodo_actual[2]
            ruta.append(inicio)
            return ruta[::-1]

        # Añadimos el nodo actual a la lista de cerrados
        cerrados.add(nodo_actual[1])

        # Generamos los sucesores del nodo actual
        for sucesor in [(nodo_actual[1][0] + 1, nodo_actual[1][1]),
                        (nodo_actual[1][0] - 1, nodo_actual[1][1]),
                        (nodo_actual[1][0], nodo_actual[1][1] + 1),
                        (nodo_actual[1][0], nodo_actual[1][1] - 1)]:
            # Si el sucesor está fuera del mapa, lo ignoramos
            if sucesor[0] < 0 or sucesor[0] >= filas or sucesor[1] < 0 or sucesor[1] >= columnas:
                continue
            # Si el sucesor es un obstáculo o ya está en la lista de cerrados, lo ignoramos
            if mapa[sucesor[0]][sucesor[1]] == 1 or sucesor in cerrados:
                continue
            # Calculamos el valor g del sucesor
            g = nodo_actual[0] + 1
            # Calculamos el valor h del sucesor
            h = distancia(sucesor, objetivo)
            # Calculamos el valor f del sucesor
            f = g + h
            # Añadimos el sucesor a la lista de abiertos
            heapq.heappush(abiertos, (f, sucesor, nodo_actual))

    # Si no se ha encontrado una ruta, devolvemos None
    return None

# Ejemplo de uso del algoritmo A*
mapa = [[0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]]

inicio = (0, 0)
objetivo = (4, 5)

ruta = a_star(mapa, inicio, objetivo)

if ruta is None:
    print("No se ha encontrado una ruta")
else:
    print("Ruta encontrada:", ruta)
