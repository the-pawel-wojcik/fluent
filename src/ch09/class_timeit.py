import time
import functools

class Clock:
    DEFAULT_FMT = '[{elapsed:0.10f} s] {name}({call_sig}) = {result!r}'

    def __init__(self, fmt=None):
        if fmt is None:
            self.fmt = self.DEFAULT_FMT
        else:
            self.fmt = fmt

    def __call__(self, func):

        @functools.wraps(func)
        def decorate(*args):
            start_time = time.perf_counter()
            result = func(*args)
            elapsed = time.perf_counter() - start_time
            name = func.__name__
            call_sig = ', '.join(repr(arg) for arg in args)
            print(self.fmt.format(**locals()))
            return result

        return decorate


@Clock()
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


print(factorial.__name__)
print(f'{factorial(10)=}')
