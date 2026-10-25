# -*- coding: utf-8 -*-
"""b712_locate.py -- A NAMED LOCATOR (standing clauses v2 row (15): "a reading made by a named tool"; row (53): "locator and read tools write
nothing"). Carried from tools/b710_locate.py by the Write tool with one repair: it writes no bank (row (53), the later row the version's reading).

### `python -I -X utf8 tools/b712_locate.py <path> <regex> [<path> <regex> ...]`: the line numbers of each <path> whose text matches <regex>, with
### the first 100 characters of each line, printed; the seat reads the spans it names by the Read tool, by offset and a limit of at most two
### hundred. Writes nothing.
"""
import io
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main(argv):
    if len(argv) < 2 or len(argv) % 2:
        print('usage: b712_locate.py <path> <regex> [<path> <regex> ...]')
        return 2
    for k in range(0, len(argv), 2):
        path, pat = argv[k], argv[k + 1]
        p = path if os.path.isabs(path) else os.path.join(ROOT, path)
        text = io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''
        rx = re.compile(pat)
        hits = [(i, l) for i, l in enumerate(text.split(NL), 1) if rx.search(l)]
        print('### %s ; %s ; /%s/ ; hits %d%s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), path, pat, len(hits), '' if os.path.exists(p) else ' (NO SUCH FILE)'))
        for i, l in hits:
            print('  :%d %s' % (i, l.strip()[:100]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
