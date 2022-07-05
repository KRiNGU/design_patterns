from abc import ABC, abstractmethod
import math


class Operators():
    def sum(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def sqrt(self, a):
        return math.sqrt(a)


class ClientInterface(ABC):
    @abstractmethod
    def get_hypotenuse(leg1, leg2):
        pass


class Adapter(ClientInterface):
    operators = Operators()

    def get_hypotenuse(self, leg1, leg2):
        return int(self.operators.sqrt(self.operators.sum(self.operators.mul(leg1, leg1), self.operators.mul(leg2, leg2))))


hypotenuse_calc: ClientInterface = Adapter()
hypotenuse = hypotenuse_calc.get_hypotenuse(3, 4)
print(hypotenuse)
