from typing import NamedTuple
import time

from prime import NUMBERS, is_prime


class Result(NamedTuple):
    is_prime: bool
    elapsed_s: float


def check(tested_number: int) -> Result:
    start = time.perf_counter()
    prime_test_result = is_prime(tested_number)
    elapsed_s = time.perf_counter() - start
    return Result(is_prime=prime_test_result, elapsed_s=elapsed_s)


def main():
    start = time.perf_counter()
    for tested_number in NUMBERS:
        res = check(tested_number)
        label = 'P' if res.is_prime else ' ' 
        print(f'{tested_number:>16d} {label} {res.elapsed_s:>6.3f} s')
    end = time.perf_counter()
    print(f'Total took: {end-start:.3f} s')


if __name__ == "__main__":
    main()

