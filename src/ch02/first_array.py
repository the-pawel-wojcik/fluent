from array import array
from random import random

floatcnt = 10**6
milion = array('d', (random() for _ in range(floatcnt)))
with open('milion.bin', 'wb') as mfile:
    milion.tofile(mfile)

second_milion = array('d')
with open('milion.bin', 'rb') as mfile:
    second_milion.fromfile(mfile, floatcnt)

print(f"{milion==second_milion=}")

