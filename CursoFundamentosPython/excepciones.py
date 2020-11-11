def divide_elementos_en_lista(lista, divisor):
    """Divide los elementos en la lista entre divisor"""
    try:
        return [i /divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))

divisor = 0

print(divide_elementos_en_lista(lista, divisor))
