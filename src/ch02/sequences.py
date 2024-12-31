from collections import abc
from collections import deque

assert(issubclass(tuple, abc.Sequence) == True)
assert(issubclass(tuple, abc.MutableSequence) ==  False)

assert(issubclass(list, abc.Sequence) == True)
assert(issubclass(list, abc.MutableSequence) ==  True)

def return_a_list_with_one_field():
    return [['hidden gem']]

# Single element tuples must end with a trailing comma
((unpacked,),) = return_a_list_with_one_field()
print(f"{unpacked=}")

# Run this in an interactive mode
# immutable = ('p', 'w', [10, 90])
# immutable[2] += [-10, 45]
# print("{immutable=}")

print("\nDeque demonstration")
dq = deque(range(10), maxlen=10)
print(f"{dq=}")
dq.rotate(1)
print(f"dq.rotate(1): {dq=}")
dq.rotate(1)
print(f"dq.rotate(1): {dq=}")
dq.appendleft(20)
dq.extendleft([-1, -1])
print(f"{dq=}")

