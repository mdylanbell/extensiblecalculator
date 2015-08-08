extensiblecalculator is a simple python class that allows you to 
perform calculations on integers. It is written to be extensible
so that you can specify new operators besides the basics
(*, /, +, -) provided here.

Result is returned as an int.

To extend this module, you can create subclasses and define your own operators.
See [MoreFunctionaCalculator.py](MoreFunctionalCalculator.py) for subclass example.

Code example:

from Calculator import Calculator

c = Calculator()

# Simple addition
c.calculate('3 + 5')

8
