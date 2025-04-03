import sys
from concurrent import futures
from time import perf_counter
from typing import NamedTuple

from prime import NUMBERS, is_prime


class PrimeResult(NamedTuple):
    number: int
    prime: bool
    elapsed: float


def check(tested_number: int) -> PrimeResult:
    start = perf_counter()
    prime_test_result = is_prime(tested_number)
    end = perf_counter()
    elapsed = end-start
    return PrimeResult(tested_number, prime_test_result, elapsed)
    

def main() -> None:
    if len(sys.argv) < 2:
        workers = None
    else:
        workers = int(sys.argv[1])

    executor = futures.ProcessPoolExecutor(max_workers=workers)
    actual_workers = executor._max_workers  # typing: ignore
    print(f'Checking {len(NUMBERS)} numbers with {actual_workers} processes.')

    start = perf_counter()

    numbers = sorted(NUMBERS)
    with executor:
        for result in executor.map(check, numbers):
            label = 'P' if result.prime else ' '
            print(f'{result.number:16} {label} {result.elapsed:9.6f} s')

    end = perf_counter()
    elapsed = end-start
    print(f'Total time {elapsed:.2f} s.')

if __name__ == "__main__":
    main()
