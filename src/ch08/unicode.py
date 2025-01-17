import re
import sys
import unicodedata
from collections.abc import Iterator

WORD_RE = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1


def tokenize(text: str) -> Iterator[str]:
    for match in WORD_RE.finditer(text):
        yield match.group().upper()


def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index

if __name__ == "__main__":
    index = name_index(32, 100)
    for keyword, characters in index.items():
        print(keyword + ':', end='')
        for char in characters:
            print(' ' + char, end='')
        print('')
