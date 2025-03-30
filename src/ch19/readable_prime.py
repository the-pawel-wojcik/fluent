import math
import time

def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    root = math.isqrt(n)
    for divisor in range(3, root + 1, 2):
        if n % divisor == 0:
            return False
    return True

start = time.time_ns()
print(f'{is_prime(5_000_111_000_222_021)}')
end = time.time_ns()
elapsed = end - start
print(f'It took {elapsed/1.0e9:.3f} s')
