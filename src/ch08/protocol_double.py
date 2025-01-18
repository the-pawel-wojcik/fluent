from typing import Protocol, TypeVar

T = TypeVar('T')

class HasMulInt(Protocol):
    def __mul__(self: T, other: int) -> T: ...

MI = TypeVar('MI', bound=HasMulInt)

def double(x: MI) -> MI:
    return x * 2
