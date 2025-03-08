"""
LookingGlass::
    >>> from mirror import LookingGlass
    >>> manager = LookingGlass()
    >>> manager # doctest: +ELLIPSIS
    <mirror.LookingGlass object at 0x...>
    >>> monster = manager.__enter__()
    >>> monster == 'Jabberwocky'
    eurT
    >>> monster
    'ykcowrebbaJ'
    >>> manager # doctest: +ELLIPSIS
    >...x0 ta tcejbo ssalGgnikooL.rorrim<
    >>> manager.__exit__(None, None, None)
    >>> monster
    'Jabberwocky'
"""
