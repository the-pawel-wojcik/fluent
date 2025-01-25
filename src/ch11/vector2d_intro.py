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
    __match_args__ = ('x', 'y')  # support for positional pattern matching
    __slots__ = ('__x', '__y')
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

    def __truediv__(self, denominator: float):
        if not isinstance(denominator, float):
            raise ValueError(f'{denominator} needs to be a float')
        # Keeping the type in runtime helps with inheritance
        return type(self)(self.x/denominator, self.y/denominator)



def keyword_pattern_demo(v: Vector2d) -> None:
    """
    >>> keyword_pattern_demo(Vector2d(3, 0))
    Vector2d(3.0, 0.0) points along the x axis.
    >>> keyword_pattern_demo(Vector2d(3, 5))
    Vector2d(3.0, 5.0) points along (0.51, 0.86).
    """
    match v:
        case Vector2d(x=0, y=0):
            print(f'{v!r} is null.')
        case Vector2d(x=0):
            print(f'{v!r} points along the y axis.')
        case Vector2d(y=0):
            print(f'{v!r} points along the x axis.')
        case Vector2d(x=x, y=y) if x==y:
            print(f'{v!r} points along the (1,1) axis.')
        case _:
            print(f'{v!r} points along {v/abs(v):.2f}.')


class shortVector2d(Vector2d):
    """
    >>> len(bytes(Vector2d(1, 1)))
    17
    >>> len(bytes(shortVector2d(1, 1)))
    9
    """
    typecode = 'f'


