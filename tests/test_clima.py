import unittest
from src.api import obter_clima


class TestClima(unittest.TestCase):

    def test_clima_valido(self):
        self.assertIn(obter_clima("Aracaju"), ["ruim", "bom", "normal"])
