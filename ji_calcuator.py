import ji_add
import test1
import bong_sub


class Calculator:

    def add(self, a, b):
        return ji_add.ji_add(a, b)

    def sub(self, a, b):
        return bong_sub.sub(a, b)

    def mul(self, a, b):
        return test1.multiply(a, b)
    def div(self, a, b):
        return a/b

calc = Calculator()

print(calc.add(10, 5))
print(calc.sub(10, 5))
print(calc.mul(10, 5))
print(calc.div(10, 5))