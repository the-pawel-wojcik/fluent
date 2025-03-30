import time
import itertools
from threading import Event, Thread


def spin(msg: str, done: Event) -> None:
    for wheel in itertools.cycle(r'\|/-'):
        status = f'\r{wheel} {msg}'
        print(status, end='', flush=True)
        blanks = ' ' * len(status)
        if done.wait(.1):
            print(f'\r{blanks}\r', end='', flush=True)
            break
        print(f'\r{blanks}\r', end='', flush=True)


def slow() -> int:
    time.sleep(3)
    return 7


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('spinner', done))
    print(f'{spinner=}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()

    return result


def main():
    result = supervisor()
    print(f'The result is {result}')

if __name__ == '__main__':
    main()
