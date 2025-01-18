from collections.abc import Iterable
from typing import TypeAlias, TypeVar
from protocol import HasLessThan

LT = TypeVar('LT', bound=HasLessThan)

def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]
