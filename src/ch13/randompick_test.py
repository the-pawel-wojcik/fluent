import random
from typing import Any, Iterable, TYPE_CHECKING

from randompick import RandomPicker


class SimplePicker:
    def __init__(self, items: Iterable) -> None:
        self._data = list(items)
        random.shuffle(self._data)

    def pick(self) -> Any:
        return self._data.pop()

def test_isinstance() -> None:
    """
    SimplePicker is not a subclass of RandomPicker but checks out as one. This
    is possible thanks to the decorator runtime_checkable placed on
    RandomPicker.
    """
    popper: RandomPicker = SimplePicker([1])
    assert isinstance(popper, RandomPicker)

def test_item_type() -> None:
    items = [1, 2]
    popper = SimplePicker(items)
    item = popper.pick()
    assert item in items
    if TYPE_CHECKING:
        reveal_type(item)
    assert isinstance(item, int)
