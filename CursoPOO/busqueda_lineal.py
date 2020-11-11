def busqueda_lineal(lista, elemento):
    """
    Busca un elemento en una lista en forma lineal.
    :param lista: lista de entrada.
    :param elemento: elemento a buscar.
    :return: True si encontro el elemento, False en caso contrario.
    """
    for item in lista:
        if item == elemento:
            return True

    return False
