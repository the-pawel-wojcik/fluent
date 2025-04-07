import asyncio
import socket
from keyword import kwlist

MAX_KEYWORD_LEN = 10


async def probe(domain: str) -> tuple[str, bool]:
    loop = asyncio.get_running_loop()

    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return domain, False

    return domain, True


async def main() -> None:
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f'{kw}.dev'.lower() for kw in names)
    corous = [probe(domain) for domain in domains]
    for coro in asyncio.as_completed(corous):
        domain, found = await coro
        label = '+' if found is True else ' '
        print(f'{label} {domain}')


if __name__ == "__main__":
    asyncio.run(main())
