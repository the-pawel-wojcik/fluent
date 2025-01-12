from functools import reduce

def factorial(n: int) -> int:
    if isinstance(n, int) is False:
        raise ValueError("Factorial requires int")
    if n < 1:
        return 1
    return reduce(lambda a, b: a*b, range(1, n+1)) 

func = factorial
out = list(map(func, range(10)))
print(out)
