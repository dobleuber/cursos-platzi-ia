def enumeracion(objetivo):
    respuesta = 0

    while respuesta ** 2 < objetivo:
        respuesta += 1

    if respuesta ** 2 == objetivo:
        return respuesta
    else:
        return -1


def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0.0

    while (abs(respuesta ** 2 - objetivo)) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        return -1
    else:
        return respuesta


def busqueda_binaria(objetivo):
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2.0

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2.0

    return respuesta

metodos = {
    '1': 'Enumeracion',
    '2': 'Aproximacion',
    '3': 'Busqueda binaria'
}


entrada = int(input('Por favor ingrese un numero: '))

for i, m in metodos.items():
    print(i, m)

selected_method = int(input('Que metodo desea usar para encontrar la raiz cuadrada?'))
respuesta = -1

if selected_method == 1:
    respuesta = enumeracion(entrada)
elif selected_method == 2:
    respuesta = aproximacion(entrada)
else:
    respuesta = busqueda_binaria(entrada)

if respuesta != -1:
    print(f'La raiz cuadrada de {entrada} es: {respuesta}.')
else:
    print('Lo siento no encontramos la raiz cuadrada.')