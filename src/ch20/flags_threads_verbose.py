from concurrent import futures

from flags_threads import main, download_one


def download_many(ccs: list[str]) -> int:
    idx = 0  # if everything fails
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        todo: list[futures.Future] = list()
        for cc in sorted(ccs):
            future = executor.submit(download_one, cc)
            todo.append(future)
            print(f'Scheduled {future!r}')

        for idx, future  in enumerate(futures.as_completed(todo), 1):
            res: str = future.result()
            print(f'{idx}: {res} produced by {future!r}')

    return idx


if __name__ == "__main__":
    main(download_many)
