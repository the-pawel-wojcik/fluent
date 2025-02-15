from typing import Any, Callable, Iterable, Protocol, overload, TypeVar
MISSING = object()
empty_msg = 'max args is an empty list'


class SupportsLessThan(Protocol):
    def __lessthan__(self, other: Any) -> bool: ...

T = TypeVar('T')
LT = TypeVar('LT', bound=SupportsLessThan)
R = TypeVar('R')

# No key, no default
@overload
def max(__arg1: Iterable[LT]) -> LT:
    ...

@overload
def max(__arg1: LT, *_args: Iterable[LT]) -> LT:
    ...

# With key, no default
@overload
def max(__arg1: Iterable[T], *, key: Callable[[T], LT]) -> T:
    ...

@overload
def max(__arg1: T, *_args: Iterable[T], key: Callable[[T], LT]) -> T:
    ...

# No key, With default
@overload
def max(__iterable: Iterable[LT], *, default: R) -> LT | R:
    ...

# with key, with default
@overload
def max(
    __iterable: Iterable[T],
    *,
    key: Callable[[T], LT],
    default: R
) -> T | R:
    ...


def max(first, *args, key = None, default = MISSING):
    """ Return the largest item in the iterable or the largest of two or more
    arguments. """
    if args:
        series = iter(args)
        candidate = first
    else:
        series = iter(first)
        try:
            candidate = next(series)
        except StopIteration:
            if default is not MISSING:
                return default
            raise ValueError(empty_msg) from None

    if key is None:
        for element in series:
            if element > candidate:
                candidate = element
    else:
        candidate_key = key(candidate)
        for element in series:
            element_key = key(element)
            if element_key > candidate_key:
                candidate = element
                candidate_key = element_key
    return candidate
