def f(x):
    respuesta = 0

    for i in range(1000):  # 1000 operaciones
        respuesta += 1

    for i in range(x):  # x operaciones
        respuesta += 1

    for i in range(x):  # 2 * (x**2) operaciones
        for j in range(x):
            respuesta += 1
            respuesta += 1

    return respuesta


if __name__ == '__main__':
    x = 2
    print(f(x))
