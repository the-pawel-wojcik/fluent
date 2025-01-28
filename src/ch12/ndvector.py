import reprlib
import array
import math
import operator
from typing import Any

class Vector:
    typecode = 'd'
    __match_attr__ = ('x', 'y', 'z', 't')

    def __init__(self, elements):
        """
        >>> Vector([])
        Vector()
        >>> Vector([0])
        Vector([0.0])
        >>> Vector([3, 4])
        Vector([3.0, 4.0])
        """
        self._content = array.array(self.typecode, elements)

    def __repr__(self):
        content = reprlib.repr(self._content)
        content = content[content.find('['):-1]  # -1 trimms ')' from '])'
        return 'Vector(' + content + ')'

    def __iter__(self):
        return iter(self._content)

    def __bytes__(self):
         return bytes([ord(self.typecode)]) + bytes(self._content)

    def __eq__(self, other):
        """
        >>> Vector([3, 3]) == Vector([1, 1])
        False
        >>> Vector([1, 2]) == Vector([1, 2, 3])
        False
        >>> Vector([1, 2, 3]) == Vector([1, 2, 3])
        True
        """
        return tuple(self) == tuple(other)

    def __abs__(self):
        """
        >>> abs(Vector([5, 12]))
        13.0
        """
        return math.hypot(*self)

    def __bool__(self):
        """
        >>> bool(Vector([5, 12]))
        True
        >>> bool(Vector([0, 0, 0, 0]))
        False
        """
        return bool(abs(self))

    def __len__(self):
        return len(self._content)

    def __getitem__(self, key):
        """
        >>> v1 = Vector(range(10))
        >>> v1[5]
        5.0
        >>> v1[:5:2]
        Vector([0.0, 2.0, 4.0])
        >>> v1[-1:]
        Vector([9.0])
        """
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._content[key])
        idx = operator.index(key)
        return self._content[idx]

    def __getattr__(self, key):
        """
        >>> v = Vector([0, 1, 3])
        >>> v.x
        0.0
        >>> v.t
        Traceback (most recent call last):
        ...
        AttributeError: 'Vector' object has no attribute 't'
        >>> v.ł
        Traceback (most recent call last):
        ...
        AttributeError: 'Vector' object has no attribute 'ł'
        """
        cls = type(self)
        try:
            pos = self.__match_attr__.index(key)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._content):
            return self._content[pos]

        msg = f'{cls.__name__!r} object has no attribute {key!r}'
        raise AttributeError(msg)

    def __setattr__(self, name: str, value: Any, /) -> None:
        """
        >>> v1 = Vector([1])
        >>> v1.x = 5
        Traceback (most recent call last):
        ...
        AttributeError: Read-only attribute 'x'
        >>> v1.g = 5
        Traceback (most recent call last):
        ...
        AttributeError: Can't set attributes 'a'-'z' in 'Vector'
        >>> v1.Ł = 5
        """
        cls = self.__class__
        if len(name) == 1:
            if name in self.__match_attr__:
                msg = f'Read-only attribute {name!r}'
            elif name.islower():
                msg = f"Can't set attributes 'a'-'z' in {cls.__name__!r}"
            else:
                msg = ''
            if msg:
                raise AttributeError(msg)

        super().__setattr__(name, value)
        
        
        

    @classmethod
    def frombytes(cls, bts):
        typecode = chr(bts[0])
        memv = memoryview(bts[1:]).cast(typecode=typecode)
        return cls(memv)
