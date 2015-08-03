""" Extensible calculator
"""

import re
import sys


class Calculator(object):
    """ Calculator class to perform calculations on expressions
    """

    def calculate(self, input):
        """ Perform calculation (not worrying about parentheses) on expression
            of arbitrary length, respecting order of operations
        """

        expressions = re.split(',', input)
        results = []

        for expression in expressions:

            for operator in self.order_of_operations:
                regex = r'(\d+)\s*' + re.escape(operator) + r'\s*(\d+)'

                m = re.search(regex, expression)

                while m:

                    a = int(m.group(1))
                    b = int(m.group(2))

                    value = self.operations_dict[operator](a, b)
                    expression = re.sub(regex, str(value), expression, 1)

                    m = re.search(regex, expression)

            results.append(int(expression))

        return results

    @classmethod
    def add(self, a, b):
        return a + b

    @classmethod
    def subtract(self, a, b):
        return a - b

    @classmethod
    def multiply(self, a, b):
        return a * b

    @classmethod
    def divide(self, a, b):
        return a / b

    def __init__(self):
        self.operations_dict = {
            '*': self.multiply,
            '/': self.divide,
            '+': self.add,
            '-': self.subtract
        }

        self.order_of_operations = ['*', '/', '+', '-']
