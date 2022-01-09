import unittest
from calculatorlibrary.calculator import Math  # add, subtract


class MathTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Math.add(3, 4), 6)
