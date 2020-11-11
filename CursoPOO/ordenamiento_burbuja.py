from random import randint


def burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == '__main__':
    tamano_lista = int(input('De que tamanio desea la lista? '))

    lista = [randint(0, 100) for i in range(tamano_lista)]

    print(lista)

    lista_ordenada = burbuja(lista[:])

    print(lista_ordenada)
