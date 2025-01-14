import unicodedata, functools

nfc = functools.partial(unicodedata.normalize, 'NFD')
s1 = 'Z\u0301le'
s2 = 'Źle'
print(f"{s1=}")
print(f"{s2=}")
print(f"{s1 == s2=}")
print(f"{nfc(s1) == nfc(s2)=}")
