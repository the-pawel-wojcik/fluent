import asyncio
from collections.abc import Sequence
from typing import Counter
from pathlib import Path
import sys

import httpx
from httpx import AsyncClient, HTTPError
from http import HTTPStatus
from tqdm import tqdm

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

from ch20.flags2_common import DownloadStatus, main, save_flag
from flags2_asyncio import download_flag, download_many

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


async def download_country(
    client: AsyncClient,
    base_url: str,
    cc: str,
) -> str:
    url = f'{base_url}/{cc}/metadata.json'.lower()
    response = await client.get(url=url, follow_redirects=False, timeout=10)
    response.raise_for_status()
    meta = response.json()
    return meta['country']


async def get_one(
    client: AsyncClient,
    base_url: str,
    cc: str,
    semaphore: asyncio.Semaphore,
    verbose: bool,
) -> DownloadStatus:
    try:
        async with semaphore:
            image = await download_flag(client, base_url, cc)
        async with semaphore:
            country = await download_country(client, base_url, cc)
    except httpx.HTTPStatusError as exc:
        response = exc.response
        if response.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'Not found {response.url}'
        else:
            raise
    else:
        filename = country.replace(' ', '_')
        await asyncio.to_thread(save_flag, image, f'{cc}_{filename}.gif')
        status = DownloadStatus.OK
        msg = 'ok'

    if verbose:
        print(f'{cc} {msg}')

    return status


def download_many(
    ccs: Sequence[str],
    base_url: str,
    verbose: bool,
    max_concur_req: int,
) -> Counter[DownloadStatus]:
    coro = async_download_many(ccs, base_url, verbose, max_concur_req)
    counts = asyncio.run(coro)
    return counts


async def async_download_many(
    ccs: Sequence[str],
    base_url: str,
    verbose: bool,
    concur_req: int,
) -> Counter[DownloadStatus]:
    """aka supervisor"""

    counter: Counter[DownloadStatus] = Counter()
    semaphore = asyncio.Semaphore(concur_req)

    # spawn coroutines
    async with AsyncClient() as client:
        tasks = [
            get_one(client, base_url, cc, semaphore, verbose) 
            for cc in sorted(ccs)
        ]

        tasks_iter = asyncio.as_completed(tasks)
        if not verbose:
            tasks_iter = tqdm(tasks_iter, total=len(ccs))

        error: HTTPError | None = None
        err_msg = ''
        for done_task in tasks_iter:
            try:
                status: DownloadStatus = await done_task
            except httpx.HTTPStatusError as exc:
                res = exc.response
                status = DownloadStatus.ERROR
                err_msg = f'HTTP error {res.status_code} - {res.reason_phrase}'
                error = exc
            except httpx.RequestError as exc:
                status = DownloadStatus.ERROR
                err_msg = f'{exc} {type(exc)}'.strip()
                error = exc
            except KeyboardInterrupt:
                break
            except:
                raise

            counter[status] += 1

            if error:
                status = DownloadStatus.ERROR
                if verbose:
                    url = str(error.request.url)
                    cc = Path(url).stem.upper()
                    print(f'{cc} error: {err_msg}')

    return counter


if __name__ == "__main__":
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
