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

def shop_quantity(attr_name):

    def getter(instance):
        return instance.__dict__[attr_name]

    def setter(instance, value):
        if value > 0:
            instance.__dict__[attr_name] = value
        else:
            raise ValueError(f'{attr_name} must be positive.')

    return property(getter, setter)



class LineItem:
    weight = shop_quantity('weight')
    price = shop_quantity('price')

    def __init__(self, description: str, weight: float, price: float):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price
