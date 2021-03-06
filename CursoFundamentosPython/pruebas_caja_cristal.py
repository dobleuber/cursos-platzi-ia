import unittest


def es_mayor_de_edad(edad):
    """Dice si la edad es para un mayor de edad"""
    if edad > 18:
        return True
    else:
        return False


class CajaDeCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)

        self.assertTrue(resultado)

    def test_es_menor_de_edad(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)

        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
