from random import randint


def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        # Iteradores para recorrer las sublistas
        i = 0
        j = 0

        # Iterador lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 20)

    return lista


if __name__ == '__main__':
    tamano_lista = int(input('De que tamanio desea la lista? '))

    lista = [randint(0, 100) for i in range(tamano_lista)]

    print(lista)

    print('-------')

    lista_ordenada = merge_sort(lista[:])

    print('-------')

    print(lista_ordenada)
