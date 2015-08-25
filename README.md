# Extensible Calculator

## Intro

extensiblecalculator is a simple python class that allows you to 
perform calculations on integers. It is written to be extensible
so that you can specify new operators besides the basics
(*, /, +, -) provided here.

Result is returned as an int.

**This code was written as an exercise and might not serve practical purpose.**

## Extending

To extend this module, you can create subclasses and define your own operators.
See [MoreFunctionaCalculator.py](MoreFunctionalCalculator.py) for subclassing
example.

## Code example:

```
from Calculator import Calculator

c = Calculator()

# Simple addition
result = c.calculate('3 + 5')
```

result == 8
