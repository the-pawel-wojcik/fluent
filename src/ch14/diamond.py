"""
What does python do with multiple inheritance::

>>> rt = Root()
>>> rt.ping()
<Root>.ping() from Root
>>> def print_mro(cls):
...     print(', '.join(c.__name__ for c in cls.__mro__))
...
>>> print_mro(LeafAB)
LeafAB, A, B, Root, object
>>> print_mro(LeafBA)
LeafBA, B, A, Root, object
"""
class Root:
    def ping(self):
        print(f"{self}.ping() from Root")

    def pong(self):
        print(f"{self}.pong() from Root")

    def __repr__(self):
        return f'<{type(self).__name__}>'

class A(Root):
    def ping(self):
        print(f"{self}.ping() from A")
        super().ping()

    def pong(self):
        print(f"{self}.pong() from A")
        super().pong()


class B(Root):
    def ping(self):
        print(f"{self}.ping() from B")
        super().ping()

    def pong(self):
        print(f"{self}.pong() from B")

class LeafAB(A, B):
    """
    >>> lab = LeafAB()
    >>> lab.ping()
    <LeafAB>.ping() from LeafAB
    <LeafAB>.ping() from A
    <LeafAB>.ping() from B
    <LeafAB>.ping() from Root
    >>> lab.pong()
    <LeafAB>.pong() from LeafAB
    <LeafAB>.pong() from A
    <LeafAB>.pong() from B
    """
    def ping(self):
        print(f"{self}.ping() from LeafAB")
        super().ping()

    def pong(self):
        print(f"{self}.pong() from LeafAB")
        super().pong()

class LeafBA(B, A):
    """
    >>> lba = LeafBA()
    >>> lba.ping()
    <LeafBA>.ping() from LeafBA
    <LeafBA>.ping() from B
    <LeafBA>.ping() from A
    <LeafBA>.ping() from Root
    >>> lba.pong()
    <LeafBA>.pong() from LeafBA
    <LeafBA>.pong() from B
    """
    def ping(self):
        print(f"{self}.ping() from LeafBA")
        super().ping()

    def pong(self):
        print(f"{self}.pong() from LeafBA")
        super().pong()
