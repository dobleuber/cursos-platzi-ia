import unittest


class CajaNegraTest(unittest.TestCase):
    """Caja negra tests"""
    def test_suma_dos_positivos(self):
        """
        Prueba Suma dos enteros positivos
        """
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        """
        Prueba que suma dos numeros negativos
        """
        num_1 = -10
        num_2 = -5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 5)


def suma(num_1, num_2):
    """Suma dos numeros enteros"""
    return abs(num_1) + num_2


if __name__ == '__main__':
    unittest.main()
