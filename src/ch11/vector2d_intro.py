"""
Test vector::

    >>> v1 = Vector2d(3, 4)
    >>> print(v1.x, v1.y)
    3.0 4.0
    >>> x, y = v1
    >>> x, y
    (3.0, 4.0)
    >>> v1
    Vector2d(3.0, 4.0)
    >>> v1_clone = eval(repr(v1))
    >>> v1 == v1_clone
    True
    >>> print(v1)
    (3.0, 4.0)
    >>> {Vector2d(1, 0), Vector2d(0, 1)} # hash supported
    {Vector2d(1.0, 0.0), Vector2d(0.0, 1.0)}
"""
from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        """
        >>> bytes(Vector2d(3.0, 4.0))
        b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
        """
        return (
            bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))
        )

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        """
        >>> abs(Vector2d(3, 4))
        5.0
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        >>> bool(Vector2d(-1, 10))
        True
        >>> bool(Vector2d(0, 0))
        False
        """
        return bool(abs(self))

    def __format__(self, format_spec: str, /) -> str:
        """
        >>> format(Vector2d(1, 1), '.2f')
        '(1.00, 1.00)'
        >>> format(Vector2d(1, 1), '.2fp')
        '<r=1.41, φ=0.79>'
        """
        if format_spec.endswith('p'):
            fmt = format_spec[:-1]
            coords = (abs(self), math.atan2(self.y, self.x))
            out_fmt = "<r={}, φ={}>"
        else:
            fmt = format_spec
            coords = tuple(self)
            out_fmt = "({}, {})"
        components = (format(val, fmt) for val in coords)
        return out_fmt.format(*components)
    
    def __hash__(self) -> int:
        """
        >>> hash(Vector2d(0, 1))
        -1950498447580522560
        """
        return hash((self.x, self.y))

    def __complex__(self) -> complex:
        """
        >>> complex(Vector2d(1, 1))
        (1+1j)
        """
        return self.x + self.y * 1j
