class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando Caminando!')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Estoy pedaleando!')