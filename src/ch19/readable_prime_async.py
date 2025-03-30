import asyncio
import time
import math

from spinner_async import spin

async def async_is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    root = math.isqrt(n)
    for divisor in range(3, root + 1, 2):
        if n % divisor == 0:
            return False

        if divisor % 100_000 == 1:
            await asyncio.sleep(0)

    return True


async def supervisor() -> bool:
    tested_number = 5_000_111_000_222_021
    print(f'Checking if {tested_number} is prime.')

    spinner = asyncio.create_task(spin('Checking...'))
    prime_test_result = await async_is_prime(tested_number)
    spinner.cancel()

    return prime_test_result


def main():
    start = time.time_ns()
    prime_test_result = asyncio.run(supervisor())
    if prime_test_result is True:
        print('It\'s a PRIME number.')
    else:
        print('It is NOT a PRIME number.')
    end = time.time_ns()
    elapsed = end - start
    print(f'It took {elapsed/1.0e9:.3f} s.')


if __name__ == "__main__":
    main()
