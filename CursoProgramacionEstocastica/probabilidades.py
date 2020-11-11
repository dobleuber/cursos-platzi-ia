from random import choice


def tirar_dado(num_tiros):
    secuencia_de_tiros = []

    for _ in range(num_tiros):
        tiro_1 = choice([1, 2, 3, 4, 5, 6])
        tiro_2 = choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro_1 + tiro_2)

    return secuencia_de_tiros


def main(num_tiros, num_de_intentos):
    tiros = []
    for _ in range(num_de_intentos):
        secuencia_de_tiros = tirar_dado(num_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_12 = 0
    for tiro in tiros:
        if 12 in tiro:
            tiros_con_12 += 1

    probabilidad_tiros_con_1 = tiros_con_12 / num_de_intentos
    print(f'Probabilidad de par de 6 en tiros: {probabilidad_tiros_con_1}')


if __name__ == '__main__':
    num_tiros = int(input('Cuantas veces quieres tirar el dado: '))
    numeros_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(num_tiros, numeros_de_intentos)
