from concurrent import futures
from typing import Counter
import sys

import httpx
from tqdm import tqdm

from flags2_common import CCListType, DownloadStatus, main
from flags2_sequential import get_one

DEFAULT_CONCUR_REQ = 30
MAX_CONCUR_REQ = 1000


def download_many(
    ccs: CCListType,
    base_url: str,
    verbose: bool,
    max_concur_req: int,
) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()

    with futures.ThreadPoolExecutor(max_workers=max_concur_req) as executor:
        job_to_flag_map = dict()
        for cc in ccs:
            future = executor.submit(get_one, base_url, cc, verbose)
            job_to_flag_map[future] = cc
        
        jobs_iter = futures.as_completed(job_to_flag_map)
        if not verbose:
            jobs_iter = tqdm(jobs_iter, total=len(ccs))

        for done_job in jobs_iter:
            try:
                status: DownloadStatus = done_job.result(timeout=5.5)
            except httpx.HTTPStatusError as exc:
                res = exc.response
                status = DownloadStatus.ERROR
                err_msg = f'HTTP error {res.status_code} - {res.reason_phrase}'
            except httpx.RequestError as exc:
                status = DownloadStatus.ERROR
                err_msg = f'{exc} {type(exc)}'.strip()
            except KeyboardInterrupt:
                break
            except:
                raise
            else:
                err_msg = ''

            counter[status] += 1

            if verbose and err_msg :
                cc = job_to_flag_map[done_job]
                print(err_msg, file=sys.stderr)

    return counter


if __name__ == "__main__":
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
