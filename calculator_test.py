import unittest
from Calculator import Calculator
from MoreFunctionalCalculator import MoreFunctionalCalculator

c = Calculator()
mfc = MoreFunctionalCalculator()

class CalculatorTests(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(
            5,
            c.calculate('2 + 3')
        )

    def test_simple_subtraction(self):
        self.assertEqual(
            3,
            c.calculate('5 - 2')
        )

    def test_simple_multiplication(self):
        self.assertEqual(
            30,
            c.calculate('10 * 3')
        )

    def test_simple_division(self):
        self.assertEqual(
            4,
            c.calculate('8 / 2')
        )

    def test_multipart_expression(self):
        self.assertEqual(
            12,
            c.calculate('5 * 2 + 4 - 2')
        )

    def test_order_of_operations(self):
        self.assertEqual(
            52,
            c.calculate('2 + 5 * 10')
        )

    def test_order_of_operations_complex(self):
        self.assertEqual(
            8,
            c.calculate('6 - 2 + 4')
        )

    # Test MoreFunctionalCalculator

    def test_mfc_modulus_0(self):
        self.assertEqual(
            0,
            mfc.calculate('4 % 2')
        )

    def test_mfc_modulus_1(self):
        self.assertEqual(
            1,
            mfc.calculate('4 % 3')
        )

    def test_mfc_exponent(self):
        self.assertEqual(
            32,
            mfc.calculate('2 ^ 5')
        )

    def test_mfc_extended_parent(self):
        self.assertEqual(
            12,
            mfc.calculate('5 * 2 + 4 - 2')
        )

if __name__ == '__main__':
    unittest.main()
