class MisPelotas:
    def __init__(self):
        self._pelotas = None

    @property
    def pelotas(self):
        return self._pelotas

    @property.setter
    def set_pelotas(self, pelotas):
        if pelotas <= 2:
            self._pelotas = pelotas
        else:
            raise ValueError('Tienes demasiadas pelotas')
