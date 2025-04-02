import time
from pathlib import Path
from typing import Callable

import httpx

POP20 = 'CN IN US ID PK BR NG BD RU JP MX ET PH VN EG DE IR TR TH FR'.split()
BASE_URL = 'https://www.fluentpython.com/data/flags/'
DEST_DIR = Path('flags')


def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)


def download_flag(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    response = httpx.get(
        url=url,
        timeout=6.1,
        follow_redirects=True,
    )
    response.raise_for_status()
    return response.content


def download_many(ccs: list[str]) -> int:
    for cc in sorted(ccs):
        image = download_flag(cc)
        fname = f'{cc}.gif'
        save_flag(image, fname)
        print(cc, end=' ', flush=True)
    return len(ccs)


def main(downloader: Callable[[list[str]], int ]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    start = time.perf_counter()
    cnt = downloader(POP20)  # typing: ignore
    end = time.perf_counter()
    elapsed = end - start
    print(f'Downloaded {cnt} flags in {elapsed:.2f} s.')


if __name__ == '__main__':
    main(download_many)
