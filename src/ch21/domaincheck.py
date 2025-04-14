import argparse
import asyncio
from keyword import kwlist

from domainlib import multi_probe


async def main(tld: str):
    urls = [f'{kw}.{tld}'.lower() for kw in kwlist]
    async for result in multi_probe(urls):
        prefix = '☑' if result.exists else '☐'
        print(f'{prefix} {result.url}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('tld', type=str)
    args = parser.parse_args()

    asyncio.run(main(args.tld))
    
