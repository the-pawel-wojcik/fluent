"""
Coroutine::
    >>> coroutine = average()
    >>> next(coroutine)
    0.0
    >>> coroutine.send(1.0)
    1.0
    >>> coroutine.send(3.0)
    2.0
    >>> coroutine.send(5.0)
    3.0
    >>> coroutine.close()
"""

from typing import Generator


def average() -> Generator[float, float, None]:
    count = 0
    total = 0.0
    average = 0.0
    while True:
        total += yield average
        count += 1
        average = total/count
