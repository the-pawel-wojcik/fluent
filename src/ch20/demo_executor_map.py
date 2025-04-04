from time import sleep, strftime
from concurrent import futures


def time_stamp(*args):
    print(strftime('[%H:%M:%S]'), end=' ', flush=True)
    print(*args)


def loiter(n: int) -> int:
    indent = ' ' * n
    time_stamp(f'{indent}loiter({n}): doing nothing for {n}s...')
    sleep(n)
    time_stamp(f'{indent}loiter({n}): done')
    return 6 * n


def main():
    time_stamp('Script started.')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    print('results: ', results)
    # print(f'{results=}')
    print('Waiting for individual results:')
    for idx, res in enumerate(results):
        print(f'result {idx}: {res}')
    

if __name__ == "__main__":
    main()
