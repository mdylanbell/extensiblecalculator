""" Use Calculator class to make a slightly more advanced Calculator
    that supports modulus (%) and exponent(^) operators
"""

from Calculator import Calculator


class MoreFunctionalCalculator(Calculator):

    def __init__(self):
        # Add some more operators
        operators = [
            {
                'symbol': '%',
                'method': self.modulus
            },
            {
                'symbol': '^',
                'method': self.exponent
            }
        ]

        for operator in operators:
            self._add_operator(operator['symbol'], operator['method'])

        self._set_order_of_operations(['^', '*', '/', '%', '+', '-'])

    def modulus(self, a, b):
        """ Calculates simple modulus result (a % b)
        """
        return a % b

    def exponent(self, a, b):
        """ Calculate exponent (a ** b)
        """
        return a ** b
