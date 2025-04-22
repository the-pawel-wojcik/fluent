"""
>>> banana = LineItem('banana', 1.3, 0.5)
>>> banana.subtotal()
0.65
>>> banana.weight = -1.0
Traceback (most recent call last):
...
ValueError: Weight can not be negative.
"""

class LineItem:

    def __init__(self, description: str, weight: float, price: float):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight


    @weight.setter
    def weight(self, value):
        if value >= 0.0:
            self.__weight = value
        else:
            raise ValueError("Weight can not be negative.")
