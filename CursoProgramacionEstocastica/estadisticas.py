from random import randint


def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)
    return sum([(x - mu)**2 for x in X]) / len(X)


def desviacion_estandar(X):
    return varianza(X)**(1/2)


if __name__ == '__main__':
    X = [randint(1, 21) for _ in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'array X: {X}')
    print(f'Media: {mu}')
    print(f'Var: {Var}')
    print(f'sigma: {sigma}')
