from collections.abc import Iterator

def tree_names_generator(
    aclass: type,
    level: int = 0
) -> Iterator[tuple[str, int]]:
    yield aclass.__name__, level
    for subclass in aclass.__subclasses__():
        yield from tree_names_generator(subclass, level+1)


def display(aclass):
    for name, level in tree_names_generator(aclass=aclass, level=0):
        indent =  ' ' * 3 * level
        print(f'{indent}{name}')
    

display(BaseException)
