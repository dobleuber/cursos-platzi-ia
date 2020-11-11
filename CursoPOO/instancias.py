class Coordenada:
    """Define una coordenada con X e Y"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        """
        Encuentra la distancia entre dos coordenadas
        :param otra_coordenada:
        :return: la distancia entre los dos puntos
        """
        x_diff = (self.x - otra_coordenada.x) ** 2
        y_diff = (self.y - otra_coordenada.y) ** 2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 40)
    coord_2 = Coordenada(20, 5)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))
