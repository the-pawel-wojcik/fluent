import asyncio
from collections.abc import Sequence
import sys
from pathlib import Path

from httpx import AsyncClient

"""
Explicit relative imports are allowed only inside a package. 
The naive import like this i.e.
```python
from ..ch20 import flags  # illegal
```
would fail.

Here is a hack described in
https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
"""
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

from ch20.flags import BASE_URL, save_flag, main


async def download_one(client: AsyncClient, cc: str):
    image = await get_flag(client, cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


async def get_flag(client: AsyncClient, cc:str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.66, follow_redirects=True)
    return resp.read()


def download_many(ccs: Sequence[str]) -> int:
    return asyncio.run(supervisor(ccs))


async def supervisor(ccs: Sequence[str]) -> int:
    async with AsyncClient() as client:
        to_do = [download_one(client, cc) for cc in sorted(ccs)]
        res = await asyncio.gather(*to_do)

    return len(res)


if __name__ == "__main__":
    main(download_many)
