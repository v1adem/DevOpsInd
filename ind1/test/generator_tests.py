import unittest
from ..generator import even_odd_generator

class GeneratorTests(unittest.TestCase):
    def test_even_odd_generator(self):
        generator = even_odd_generator()
        self.assertEqual(next(generator), "Even")
        self.assertEqual(next(generator), "Odd")
        self.assertEqual(next(generator), "Even")
        self.assertEqual(next(generator), "Odd")