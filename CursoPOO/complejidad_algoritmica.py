import time
from sys import setrecursionlimit

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)


if __name__ == '__main__':
    n = 8000

    setrecursionlimit(n * 2)

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    print(final - comienzo)
