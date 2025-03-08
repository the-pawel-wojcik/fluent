"""
Decorated contex manager::

    >>> with mirror_gen() as what:
    ...     print("Alice in Wonderlands")
    ...     print(what)
    sdnalrednoW ni ecilA
    YKCOWREBBAJ
    >>> what
    'JABBERWOCKY'
    >>> with mirror_gen():
    ...     1/0
    Please do not divide by zero
    >>> @mirror_gen()
    ... def MrAlienGnorts():
    ...     print("Neil Armstrong")
    >>> MrAlienGnorts()
    gnortsmrA lieN
"""
import sys
from contextlib import contextmanager


@contextmanager
def mirror_gen():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please do not divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)

