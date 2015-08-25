""" Extensible calculator
"""

import re


class Calculator(object):
    """ Calculator class to perform calculations on expressions
    """

    operators = []
    order_of_operations = []

    def calculate(self, expression):
        """ Perform calculation (not worrying about parentheses) on expression
            of arbitrary length, respecting order of operations
        """

        for operators in self.order_of_operations:
            # Look for 2 numbers sepearated by our operator,
            # capture the numbers (operands) before and after
            # operator
            regex = r'(\d+)\s*([' + re.escape(operators) + r'])\s*(\d+)'

            match = re.search(regex, expression)

            while match:

                operand_a = int(match.group(1))
                operand_b = int(match.group(3))
                operator = match.group(2)

                value = self._operate(operator, operand_a, operand_b)

                # Replace the single operation we just performed with the
                # result value, reducing expression

                expression = re.sub(regex, str(value), expression, 1)

                match = re.search(regex, expression)

        return int(expression)

    def add(self, a, b):
        """ Returns result of simple addition (a + b)
        """
        return a + b

    def subtract(self, a, b):
        """ Returns result of simple subtraction (a - b)
        """
        return a - b

    def multiply(self, a, b):
        """ Returns result of simple multiplication (a * b)
        """
        return a * b

    def divide(self, a, b):
        """ Returns result of simple division (a / b)
        """
        return a / b

    def __init__(self):
        operators = [
            {
                'symbol': '*',
                'method': self.multiply
            },
            {
                'symbol': '/',
                'method': self.divide
            },
            {
                'symbol': '+',
                'method': self.add
            },
            {
                'symbol': '-',
                'method': self.subtract
            }
        ]

        for operator in operators:
            self._add_operator(operator['symbol'], operator['method'])

        self.order_of_operations = ['*/', '+-']

    def _operate(self, symbol, operand_a, operand_b):
        """ Perform single calculation based on an operator, and 2 operands
        """
        operator = self._get_operator_by_symbol(symbol)
        method = operator['method']

        return method(operand_a, operand_b)

    def _get_operator_by_symbol(self, symbol):
        """ Internal-use / private method to return an operator entry based on
            symbol
        """
        for operator in self.operators:
            if operator['symbol'] == symbol:
                return operator

        return None

    def _add_operator(self, symbol, method):
        """ Add operator to operator list.  Operators are defined by a symbol
            (e.g. '*', '/'), and a corresponding handler function.

            Each symbol can only be used once, so this method will overwrite
            earlier operator definitions using the same symbol.
        """
        existing_operator = self._get_operator_by_symbol(symbol)

        if existing_operator:
            existing_operator['method'] = method
            return

        self.operators.append({'symbol': symbol, 'method': method})

    def _remove_operator(self, symbol):
        """ Remove an operator from operator list based on symbol
        """
        operator = self._get_operator_by_symbol(symbol)

        if operator:
            self.operators.remove(operator)

    def _set_order_of_operations(self, order):
        """ Set order of operations
            Takes: list of symbols that represents order of operations
        """
        if sorted(''.join(order)) != \
           sorted(''.join([x['symbol'] for x in self.operators])):
            raise ValueError('symbol mismatch between provided order and '
                             + 'existing list')

        self.order_of_operations = order
