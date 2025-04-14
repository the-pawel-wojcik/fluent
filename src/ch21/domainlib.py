import asyncio
import socket
from collections.abc import Iterable, AsyncIterator
from typing import NamedTuple


class Result(NamedTuple):
    url: str
    exists: bool


OptLoop = asyncio.AbstractEventLoop | None


async def probe(domain: str, loop: OptLoop = None) -> Result:
    if loop is None:
        loop = asyncio.get_running_loop()

    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return Result(domain, False)
    return Result(domain, True)


async def multi_probe(domains: Iterable[str]) -> AsyncIterator[Result]:
    loop = asyncio.get_running_loop()
    coros = [probe(domain, loop) for domain in domains]
    for coro in asyncio.as_completed(coros):
        result = await coro
        yield result
    

