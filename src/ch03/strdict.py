""" Class that converts key to str on lookup

Tests for item retrieval using `d[key]` notation::

    >>> d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    >>> d['2']
    'two'
    >>> d[4]
    'four'
    >>> d[1]
    Traceback (most recent call last):
      ...
    KeyError: '1'

Tests for item retrieval using `d.get(key)` notation::

    >>> d.get('2')
    'two'
    >>> d.get(4)
    'four'
    >>> d.get(1, 'N/A')
    'N/A'


Tests for the `in` operator::

    >>> 2 in d
    True
    >>> 1 in d
    False

"""


class StrKeyDict0(dict):
    """ Dictionary that accepts keys either as str or int on retrieval. """

    def __missing__(self, key):
        """ `dict` supports this dunder – this is really all that's needed. """
        if isinstance(key, str):
            raise KeyError(key)
        else:
            return self[str(key)]

    # Apparently __itemget__ knows how to use __missing__ but get does not
    def get(self, key, default=None):
        try:
            return self[key]  # __missing__ handles checks for str as well
        except KeyError:
            return default

    def __contains__(self, key, /) -> bool:
        return key in self.keys() or str(key) in self.keys()
