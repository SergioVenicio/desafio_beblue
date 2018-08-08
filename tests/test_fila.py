from fila import Fila
from unittest import TestCase



class TestFila(TestCase):
    def setUp(self):
        self.fila = Fila([0, 1, 2, 3, 4, 5])

    def test_pop(self):
        self.assertEqual(self.fila.pop(), 0)

    def test_pop_all(self):
        with self.assertRaises(IndexError):
            while self.fila:
                self.fila.pop()

    def test_intert(self):
        self.fila.insert(10)
        self.assertIn(10, self.fila.numeros)

    def test_min(self):
        menor = self.fila.min()
        self.assertEqual(menor, 0)

    def test_max(self):
        maior = self.fila.max()
        self.assertEqual(maior, 5)