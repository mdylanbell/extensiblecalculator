import unittest
from Calculator import Calculator

c = Calculator()

class CalculatorTests(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(
            [5],
            c.calculate('2 + 3')
        )

    def test_simple_subtraction(self):
        self.assertEqual(
            [3],
            c.calculate('5 - 2')
        )

    def test_simple_multiplication(self):
        self.assertEqual(
            [30],
            c.calculate('10 * 3')
        )

    def test_simple_division(self):
        self.assertEqual(
            [4],
            c.calculate('8 / 2')
        )

    def test_multipart_expression(self):
        self.assertEqual(
            [12],
            c.calculate('5 * 2 + 4 - 2')
        )

    def test_order_of_operations(self):
        self.assertEqual(
            [52],
            c.calculate('2 + 5 * 10')
        )

    def test_multiple_expressions(self):
        self.assertEqual(
            [10, 20],
            c.calculate('2 * 6 - 2, 5 * 5 - 10 / 2')
        )

if __name__ == '__main__':
    unittest.main()
