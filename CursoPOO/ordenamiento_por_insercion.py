from random import randint


def insercion(lista):
    iterations = 0

    n = len(lista)

    for i in range(1, n):
        valor_actual = lista[i]
        posicion_actual = i

        while 0 < posicion_actual and valor_actual < lista[posicion_actual - 1]:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            iterations += 1

        lista[posicion_actual] = valor_actual

    print(iterations)

    return lista


if __name__ == '__main__':
    tamano_lista = int(input('De que tamanio desea la lista? '))

    lista = [randint(0, 100) for i in range(tamano_lista)]

    print(lista)

    print('-------')

    lista_ordenada = insercion(lista[:])

    print('-------')

    print(lista_ordenada)
