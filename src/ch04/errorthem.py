"""
Unicode handing error::

    >>> paweł = "Paweł"
    >>> paweł.encode('utf8')
    b'Pawe\xc5\x82'
    >>> paweł.encode('latin1', errors="ignore")
    b'Pawe'
    >>> paweł.encode('latin1', errors="replace")
    b'Pawe?'
    >>> paweł.encode('latin1', errors="xmlcharrefreplace")
    b'Pawe&#322;'
    >>> paweł.encode('latin1', errors="backslashreplace")
    b'Pawe\\\\u0142'
"""
