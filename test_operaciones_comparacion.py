# test_operaciones_comparacion.py

import unittest
from operaciones_comparacion import (
    es_mayor_que,
    es_menor_que,
    es_mayor_o_igual_que,
    es_menor_o_igual_que,
    son_iguales
)

class TestOperacionesComparacion(unittest.TestCase):

    def test_es_mayor_que(self):
        # Casos positivos
        self.assertTrue(es_mayor_que(10, 5))
        self.assertGreater(8, 5)
        
        # Casos negativos
        self.assertFalse(es_mayor_que(2, 5))
        self.assertFalse(es_mayor_que(5, 5))  # iguales, no debería ser mayor

    def test_es_menor_que(self):
        self.assertTrue(es_menor_que(1, 2))
        self.assertLess(3, 5)

        self.assertFalse(es_menor_que(7, 3))
        self.assertFalse(es_menor_que(4, 4))

    def test_es_mayor_o_igual_que(self):
        self.assertTrue(es_mayor_o_igual_que(6, 4))  # mayor
        self.assertTrue(es_mayor_o_igual_que(7, 7))  # igual
        self.assertGreaterEqual(9, 9)

        self.assertFalse(es_mayor_o_igual_que(3, 10))  # menor

    def test_es_menor_o_igual_que(self):
        self.assertTrue(es_menor_o_igual_que(3, 9))  # menor
        self.assertTrue(es_menor_o_igual_que(5, 5))  # igual
        self.assertLessEqual(1, 1)

        self.assertFalse(es_menor_o_igual_que(10, 2))  # mayor

    def test_son_iguales(self):
        self.assertTrue(son_iguales(4, 4))
        self.assertEqual(son_iguales(100, 100), True)

        self.assertFalse(son_iguales(3, 4))
        self.assertEqual(son_iguales(0, 1), False)

# Esto se asegura que las pruebas se ejecuten si corres el archivo directamente
if __name__ == '__main__':
    unittest.main()
