from collections.abc import Iterator
from typing import TYPE_CHECKING, reveal_type
import pytest
from top import top

def test_top_tuples() -> None:
    fruit = 'mango pear apple kiwi banana blackberry strawberry'.split()
    series: Iterator[tuple[int, str]] = (
        (len(s), s) for s in fruit
    )
    length = 3 
    expected = [(10, 'strawberry'), (10, 'blackberry'), (6, 'banana')]
    result = top(series=series, length=length) 
    if TYPE_CHECKING:
        reveal_type(series)
        reveal_type(expected)
        reveal_type(result)
    assert result == expected

def test_top_objects_error() -> None:
    series = [object() for _ in range(5)]
    if TYPE_CHECKING:
        reveal_type(series)
    with pytest.raises(TypeError) as excinfo:
        top(series, 3)
    assert "'<' not supported" in str(excinfo.value)
