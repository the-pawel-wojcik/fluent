import itertools
from multiprocessing import Process, Event
from multiprocessing import synchronize
from spinner_thread import slow, main


def spin(msg: str, done: synchronize.Event) -> None:
    for wheel in itertools.cycle(r'\|/-'):
        status = f'\r{wheel} {msg}'
        print(status, end='', flush=True)
        blanks = ' ' * len(status)
        if done.wait(.1):
            print(f'\r{blanks}\r', end='', flush=True)
            break
        print(f'\r{blanks}\r', end='', flush=True)


def supervisor() -> int:
    done = Event()
    spinner = Process(
        target=spin,
        args=('thinking', done),
    )
    print(f'{spinner=}')
    spinner.start()
    print(f'{spinner=}')
    result = slow()
    done.set()
    spinner.join()
    print(f'{spinner=}')

    return result


def main():
    result = supervisor()
    print(f'The result is {result}')

if __name__ == '__main__':
    main()

    

