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
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f'{self.name} must be positive.')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description: str, weight: float, price: float):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price
