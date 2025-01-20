import time
import functools

def better_clockit(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        call_sig = ', '.join(repr(arg) for arg in args)
        call_sig += ', '.join(f'{key}={val!r}' for key, val in kwargs.items())
        print(f'[{elapsed*10e6:10.1f} us] {name}({call_sig}) = {result!r}')
        return result
    return clocked

@better_clockit
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(8)

print(f'{fibonacci=}')
print(f'{fibonacci.__name__=}')
