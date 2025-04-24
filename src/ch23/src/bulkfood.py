"""
>>> banana = LineItem('banana', 1.3, 0.5)
>>> banana.subtotal()
0.65
>>> banana.weight = -1.0
Traceback (most recent call last):
...
ValueError: weight must be positive.
>>> banana.price = 3
"""

class Quantity:
    def __init__(self, name: str):
        self.__name: str = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.__name] = value
        else:
            raise ValueError(f'{self.__name} must be positive.')


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description: str, weight: float, price: float):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price
