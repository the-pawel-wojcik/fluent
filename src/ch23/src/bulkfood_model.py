"""
>>> banana = LineItem('banana', 1.3, 0.5)
>>> banana.subtotal()
0.65
>>> banana.weight = -1.0
Traceback (most recent call last):
...
ValueError: weight must be positive.
>>> banana.price = 3
>>> no_name = LineItem('  ', 1.0, 4.1)
Traceback (most recent call last):
...
ValueError: description cannot be blank.
"""

import model


class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description: str, weight: float, price: float):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price
