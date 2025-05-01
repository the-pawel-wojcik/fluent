from collections.abc import Iterable, Iterator
from typing import Any


def parse(attributes: str | Iterable[str]) -> tuple[str, ...]:
    if isinstance(attributes, str):
        attributes = attributes.replace(',', ' ').split()

    if not all(att.isidentifier() for att in attributes):
        raise ValueError('All names must be valid isidentifiers')

    return tuple(attributes)



def record_factory(cls_name, attributes: str | Iterable[str] ) -> type[tuple]:

    slots = parse(attributes)

    def __init__(self, *args, **kwargs):
        for att, val in zip(slots, *args):
            self.__dict__[att] = val
        self.__dict__.update(kwargs)


    def __iter__(self) -> Iterator[Any]:
        for att in self.__slots__:
            yield self.getattr(att)


    def __repr__(self) -> str:
        argument = ', '.join(
            [f'{att}={val!r}' for att, val in zip(self.__slots__, self)]
        )
        return f'{self.__class__.__name__}({argument})'

    attr = {
        '__slots__': slots,
        '__init__': __init__,
        '__iter__': __iter__,
        '__repr__': __repr__,
    }

    return type(cls_name, (object,), attr)
