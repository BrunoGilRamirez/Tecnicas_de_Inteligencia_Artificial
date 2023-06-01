"""
Las Torres de Hanoi es un juego de origen frances que consiste en mover una serie de discos de un poste a otro,
respetando las siguientes reglas:

    - Solo se puede mover un disco a la vez.
    - Un disco se puede mover si está en la parte superior de un poste.
    - Un disco no puede ser colocado sobre un disco más pequeño.

El objetivo del juego es mover todos los discos de un poste a otro, respetando las reglas anteriores.
"""


def func_objetivo(estado: list[list[int]], objetivo: list[list[int]]) -> bool:
    """
    Revisa que el estado sea el objetivo

    :param estado: Estado a revisar
    :param objetivo: Estado objetivo
    :return: True si el estado es el objetivo, False si no lo es
    """

    return estado == objetivo


def func_sucesora(estado: list[list[int]]) -> list[list[list[int]]]:
    """
    Función que genera los sucesores del estado dado

    :param estado: Estado a revisar
    :return: Lista resultante de sucesores del estado dado
    """

    hijos = []

    for indice, torre in enumerate(estado):
        if torre:
            disco = torre.pop()
            for indice2, torre2 in enumerate(estado):
                if indice != indice2:  # No se puede mover a la misma torre
                    copia_estado = [i.copy() for i in estado]  # Se crea una copia del estado
                    if torre2 and torre2[-1] < disco:  # No se puede colocar un disco más grande sobre uno más pequeño
                        continue
                    copia_estado[indice2].append(disco)
                    hijos.append(copia_estado)
            torre.append(disco)

    return hijos


def func_heuristica(estado: list[list[int]], objetivo: list[list[int]]) -> int:
    """
    Función heurística que calcula el número de discos que no están en su posición correcta

    :param estado: Estado a revisar
    :param objetivo: Estado objetivo
    :return: Número de discos que no están en su posición correcta
    """

    h = 0
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if j >= len(objetivo[i]) or estado[i][j] != objetivo[i][j]:  # Si el disco no está en su posición correcta
                h += 1
    return h


def torres_hanoi(estado_inicial: list[list[int]], estado_final: list[list[int]]) -> (bool, list[list[int]]):
    """
    Función principal del problema de las torres de hanoi

    :param estado_inicial: Estado inicial del problema
    :param estado_final: Estado final del problema
    :return: True si se encontró una solución, False si no se encontró
    """

    frontera = [(estado_inicial, 0, None)]  # Lista de tuples (estado, costo, padre)
    visitados = {}

    while frontera:
        estado, costo, padre = frontera.pop(0)

        if str(estado) in visitados:
            continue
        visitados[str(estado)] = padre

        if func_objetivo(estado, estado_final):
            camino = [estado]
            while padre is not None:
                camino.append(padre)
                padre = visitados[str(padre)]
            camino.reverse()
            return True, camino

        sucesores = func_sucesora(estado)
        for sucesor in sucesores:
            costo_sucesor = costo + 1

            # Si el sucesor no está en la frontera ni en visitados
            if sucesor not in frontera and str(sucesor) not in visitados:
                frontera.append((sucesor, costo_sucesor, estado))

        frontera.sort(key=lambda x: x[1] + func_heuristica(x[0], estado_final))

    return False, []


if __name__ == '__main__':
    from GUI import HanoiApp
    app = HanoiApp()
    app.algorithm = torres_hanoi
    app.run()
