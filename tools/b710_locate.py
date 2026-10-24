# -*- coding: utf-8 -*-
"""b710_locate.py -- A NAMED LOCATOR WITH ITS BANK ((R320) standing paragraph: "a reading made by a named tool with its bank or by the Read tool").

### `python -X utf8 tools/b710_locate.py <path> <regex>`: the line numbers of <path> whose text matches <regex>, with the first 100 characters of
### each line, printed and appended to data/b710_locate.txt with the call's time; the seat reads the spans it names by the Read tool, by offset and
### a limit of at most two hundred. Writes nothing else. Written by the Write tool at b710, Component 5.
"""
import io
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
BANK = os.path.join(ROOT, 'data', 'b710_locate.txt')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main(argv):
    if len(argv) < 2:
        print('usage: b710_locate.py <path> <regex>')
        return 2
    path, pat = argv[0], argv[1]
    p = path if os.path.isabs(path) else os.path.join(ROOT, path)
    text = io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    rx = re.compile(pat)
    hits = [(i, l) for i, l in enumerate(text.split(NL), 1) if rx.search(l)]
    L = ['### %s ; %s ; /%s/ ; hits %d' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), path, pat, len(hits))]
    L += ['  :%d %s' % (i, l.strip()[:100]) for i, l in hits]
    prev = io.open(BANK, encoding='utf-8').read() if os.path.exists(BANK) else (
        'b710 -- THE LOCATOR`S BANK: every call of tools/b710_locate.py, its pattern and its hits by line' + NL + NL)
    with open(BANK + '.tmp', 'wb') as fh:
        fh.write((prev + NL.join(L) + NL).encode('utf-8'))
    os.replace(BANK + '.tmp', BANK)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
