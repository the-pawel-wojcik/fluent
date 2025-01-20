import time

def clockit(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        call_sig = ', '.join(f'{arg=}' for arg in args)
        print(f'[{elapsed*10e6:10.1f} us] {name}({call_sig}) = {result}')
        return result
    return clocked

@clockit
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

factorial(10)

print(f'{factorial=}')
print(f'{factorial.__name__=}')
