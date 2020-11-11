class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.altura * self.base


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
