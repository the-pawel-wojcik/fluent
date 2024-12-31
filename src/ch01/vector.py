```
vector.py: a class representing real 2D vectors.

Advanced bussines, for experts only. A mature library.

Addition::

>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2 
Vector(4, 5)

Absolute value::

>>> v = Vector(5, 12)
>>> abs(v)
13.0

Multiplication::

>>> v * 2
Vector(10, 24)
>>> abs(v * 2)
26.0

```

class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Vector({self._x!r}, {self._y!r})'

    def __abs__(self):
        return pow(self._x**2 + self._y**2, 0.5)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self._x * scalar, self._y * scalar)


