from collections import Counter
from http import HTTPStatus
from collections.abc import Sequence

import httpx
import tqdm

from flags2_common import main, save_flag, DownloadStatus

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1


def get_flag(base_url: str, cc: str) -> bytes:
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    response = httpx.get(url=url, follow_redirects=False, timeout=10)
    response.raise_for_status()
    return response.content


def get_one(base_url: str, cc: str, verbose: bool) -> DownloadStatus:
    try:
        image = get_flag(base_url, cc)
    except httpx.HTTPStatusError as exc:
        response = exc.response
        if response.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'Not found {response.url}'
        else:
            raise
    else:
        save_flag(image, f'{cc}.gif')
        status = DownloadStatus.OK
        msg = 'ok'

    if verbose:
        print(f'{cc} {msg}')

    return status


def download_many(
    ccs: Sequence[str],
    base_url: str,
    verbose: bool,
    _: int,
) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()

    cc_iter = sorted(ccs)
    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter)

    for cc in cc_iter:
        try:
            status = get_one(base_url=base_url, cc=cc, verbose=verbose)
        except httpx.HTTPStatusError as exc:
            status = DownloadStatus.ERROR
            res = exc.response
            error_msg = f'HTTP error {res.status_code} - {res.reason_phrase}'
        except httpx.RequestError as exc:
            status = DownloadStatus.ERROR
            error_msg = f'{exc} {type(exc)}'.strip()
        except KeyboardInterrupt:
            break
        else:
            error_msg = ''
            
        counter[status] += 1
        if verbose:
            print(cc, error_msg)

    return counter


if __name__ == "__main__":
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
