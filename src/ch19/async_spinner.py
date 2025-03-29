import itertools
import asyncio


async def spin(msg: str) -> None:
    status = ''
    for state in itertools.cycle(r'\|/-'):
        status = f'\r{state} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='', flush=True)


async def slow() -> int:
    await asyncio.sleep(3)
    return 4


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('Thinking'))
    print(f'{spinner=}')
    result = await slow()
    spinner.cancel()
    return result


def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer = {result}')


if __name__ == "__main__":
    main()
