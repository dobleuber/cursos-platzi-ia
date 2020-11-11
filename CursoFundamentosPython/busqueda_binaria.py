objetivo = int(input('Escoge un entero: '))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2.0

while abs(respuesta**2 - objetivo) >= epsilon:
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2.0

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
