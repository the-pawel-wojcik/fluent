"""
Slicing::

    >>> cafe = bytes('café', "utf8")
    >>> cafe
    b'caf\xc3\xa9'
    >>> cafe[0]
    99
    >>> cafe[:1]
    b'c'

"""
name = "Paweł Wójcik"
print(f"Unicode: {name}")
print(f"Bytes: {name.encode("utf-8")}")
