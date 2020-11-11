from random import sample
from collections import Counter
from functools import reduce

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']


def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas


def obtener_mano(barajas, tamano_mano):
    mano = sample(barajas, tamano_mano)

    return mano


def es_escalera(valores):
    data = sorted([int(v) for v in valores])
    data = [data[i + 1] - data[i] == 1 for i in range(len(valores) - 1)]
    return reduce(lambda a, b: a and b, data)


def main(tamano_mano, intentos):
    baraja = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(baraja, tamano_mano)
        manos.append(mano)

    escaleras = 0
    escalera_reales = 0
    for mano in manos:
        valores = []
        palos = []
        for carta in mano:
            palos.append(carta[0])      # el palo esta en la posicion 0 del set
            valores.append(carta[1])    # el valor esta en la posicion 1 del set

        counter = Counter(palos)
        if es_escalera(valores):
            escaleras += 1
            if tamano_mano in counter.values():
                escalera_reales += 1

    probabilidad_escalera = escaleras / intentos
    probabilidad_escalera_real = escalera_reales / intentos
    print(f'La probabilidad de obtener una escalera en una mano de tamanio: {tamano_mano} es: {probabilidad_escalera}')
    print(f'La probabilidad de obtener una escalera real en una mano de tamanio: {tamano_mano} es: {probabilidad_escalera_real}')


if __name__ == '__main__':
    tamano_mano = int(input('Cuantas cartas tiene la mano? '))
    intentos = int(input('Cuantos intentos vamos a probar? '))

    main(tamano_mano, intentos)
