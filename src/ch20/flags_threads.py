from concurrent import futures

from flags import main, save_flag, download_flag


def download_one(flag: str) -> str:
    image = download_flag(flag)
    save_flag(image, f'{flag}.gif')
    print(flag, end=' ', flush=True)
    return flag


def download_many(ccs: list[str]) -> int:
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one, sorted(ccs))
    print('')

    return len(list(res))


if __name__ == "__main__":
    main(download_many)
