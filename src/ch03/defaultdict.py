import re
import collections

WORD_RE = re.compile(r'\w+')

default_idx = collections.defaultdict(list)
index = dict()
with open('the-zen-of-python.txt', 'r') as zen_file:
    for line_no, line in enumerate(zen_file, 1):
        match_iter = WORD_RE.finditer(line)
        for matched in match_iter:
            column_no = matched.span()[0] + 1
            word = matched.group()
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)
            default_idx[word].append(location)

print("Dict used with setdefault.")
for word in sorted(index, key=lambda x: len(index[x]), reverse=True):
    print(f"{len(index[word]):>3d} {word:20}: {index[word][:3]}" )
