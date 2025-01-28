import reprlib
import array
import math

class Vector:
    typecode = 'd'

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

    @classmethod
    def frombytes(cls, bts):
        typecode = chr(bts[0])
        memv = memoryview(bts[1:]).cast(typecode=typecode)
        return cls(memv)
