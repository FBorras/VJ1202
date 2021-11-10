from unittest import TestCase

from calcular_nota import calcular_nota


class Test(TestCase):
    def test_calcular_notaSb(self):
        actual = calcular_nota(9, 10)
        expected = "SOBRESALIENTE"
        self.assertEqual(expected, actual)

    def test_calcular_notaNt(self):
        actual = calcular_nota(8, 7)
        expected = "NOTABLE"
        self.assertEqual(expected, actual)

    def test_calcular_notaSf(self):
        actual = calcular_nota(5, 6)
        expected = "SUFICIENTE"
        self.assertEqual(expected, actual)

    def test_calcular_notaNSec(self):
        actual = calcular_nota(4, 8)
        expected = "NO SUPERA"
        self.assertEqual(expected, actual)

    def test_calcular_notaNSex(self):
        actual = calcular_nota(8, 4)
        expected = "NO SUPERA"
        self.assertEqual(expected, actual)

    def test_calcular_notaNS(self):
        actual = calcular_nota(4, 3)
        expected = "NO SUPERA"
        self.assertEqual(expected, actual)
