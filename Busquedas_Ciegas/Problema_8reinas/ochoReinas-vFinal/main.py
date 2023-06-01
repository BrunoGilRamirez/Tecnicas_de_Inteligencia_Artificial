"""
Problema de las 8 reinas

El problema de las 8 reinas consiste en colocar 8 reinas en un tablero de ajedrez
sin que se amenacen entre ellas.

La función principal es problema_reinas, la cual se puede llamar de dos formas:
    - problema_reinas() -> Se generará un vector vacío
    - problema_reinas(vector_prometedor) -> Se utilizará el vector dado
"""


def func_objetivo(vector: list[int]) -> bool:
    """
    Revisa que el vector tenga 8 reinas, lo que significa que llego al objetivo

    :param vector: Vector a revisar
    :type vector: list[int]
    :return: True si el vector tiene 8 reinas, False si no
    """

    return len(vector) == 8


def func_sucesora(vector: list[int]) -> list[list[int]]:
    """
    Función que genera los sucesores del vector dado

    :param vector: Vector a revisar
    :type vector: list[int]
    :return: Lista resultante de sucesores del vector dado
    """

    hijos = []

    # for i in range(8, 0, -1):
    for i in range(1, 9):
        skip = False
        copia_vector = vector.copy()

        # Asegura que no haya una reina en la misma columna
        if i in vector:
            continue

        # Asegura que no haya reina posicionada en diagonal
        for indice, v in enumerate(vector):
            if (indice + 1) - v == (len(vector) + 1) - i:
                skip = True
            if (indice + 1) + v == (len(vector) + 1) + i:
                skip = True
        if skip:
            continue

        copia_vector.append(i)
        hijos.append(copia_vector)

    return hijos


def problema_reinas(vector_prometedor: list[int] = None) -> bool:
    """
    Función que coloca ocho reinas en el tablero de ajedrez sin que se amenacen

    Las 8 reinas se representan con un vector, en donde el índice corresponde a
    la fila, y el número corresponde a la columna

    Ejemplo: [1, 5, 8, 6, 3, 7, 2, 4]
    Significa que:
        - Primera fila: reina en columna 1
        - Segunda fila: reina en columna 5
        - Tercera fila: reina en columna 8
        - etc.

    :param vector_prometedor: Vector Prometedor
    :type vector_prometedor: list[int]
    :return: True si existe solución, False si no existe solución

    """
    vector_prometedor = vector_prometedor or []

    # frontera se utilizara como stack
    frontera = [vector_prometedor]

    while frontera:
        vector = frontera.pop()
        # print(vector, end=' ->\n')

        if func_objetivo(vector):
            print(vector)
            return True

        hijos = func_sucesora(vector)

        # Se agrega a la frontera los hijos del vector
        frontera.extend(hijos)

    return False


if __name__ == '__main__':
    if problema_reinas([5]):
        print('Encontrado')
    else:
        print('No se encontró')

