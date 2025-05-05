"""
>>> Dog = record_factory("Dog", "name weight owner")
>>> reksio = Dog("Reks", 10.0, "Paweł")
>>> reksio
Dog(name='Reks', weight=10.0, owner='Paweł')
>>> name, weight, _ = reksio
>>> name, weight
('Reks', 10.0)
>>> Dog.__mro__
(<class 'record_factory.Dog'>, <class 'object'>)
"""
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
        attr = dict(zip(self.__slots__, args))
        attr.update(kwargs)
        for att, val in attr.items():
            setattr(self, att, val)


    def __iter__(self) -> Iterator[Any]:
        for att in self.__slots__:
            yield getattr(self, att)


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
