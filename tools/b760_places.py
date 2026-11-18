# -*- coding: utf-8 -*-
"""tools/b760_places.py -- (R370)(5)(ii): THE PLACES OF ACTS WHOSE FERRIES CARRY NONE, banked as data/b760_places.txt from BLOCK P of the
text block (data/b760_text.txt), its words read from the bank and not retyped.

The ruling's words (relay data/b760_ferry.txt :17): "(ii) THE PLACE OF AN ACT WHOSE FERRY CARRIES NONE: handoff.py reads it from
data/b760_places.txt, banked from BLOCK P, where the ferry has no such line." The text bank is read only where its sha256 equals the figure
of (R370) PATHS (data/b760_ferry.txt :7); BLOCK P is the part from its heading line ("@@ BLOCK P") to the next block's heading; each entry is
a marker line "@@ P b<n>", then "NEW>>", one line, "<<NEW". Wanted: the entries b758 and b759, in that order, each one line opening
"THE ACT'S PLACE. "; anything else exits, nothing written. Each row of the bank is "b<n> | <that line, unedited>"; the bank's head names
its source by path, line and digest. The rows are read by tools/standing/handoff.py from v1.36.9.

  python -X utf8 -u tools/b760_places.py dry      the rows and the yields printed; nothing written
  python -X utf8 -u tools/b760_places.py write    data/b760_places.txt written whole, its lines and sha256 printed
"""
import hashlib
import os
import re
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
TEXT = 'b760_text.txt'
TEXT_SHA = '7c8fe2f89718604a4cc13b61b6f5b94b0dcd2582044694557f2741d233ef3472'   # ### (R370) PATHS, data/b760_ferry.txt :7
OUT = 'b760_places.txt'
WANT = ('b758', 'b759')
PLACE = "THE ACT'S PLACE. "
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rows():
    """([(act, the bank's line of the text, the place line)], the block's first and last lines); exits on any other shape."""
    b = open(os.path.join(D, TEXT), 'rb').read()
    sha = hashlib.sha256(b).hexdigest()
    if sha != TEXT_SHA:
        sys.exit('### data/%s sha256 %s, not the figure of (R370) PATHS %s -- NOTHING WRITTEN' % (TEXT, sha[:16], TEXT_SHA[:16]))
    L = b.decode('utf-8').split(NL)
    heads = [k for k, l in enumerate(L, 1) if l.startswith('@@ BLOCK P')]
    if len(heads) != 1:
        sys.exit('### BLOCK P`s heading read %d times, one wanted -- NOTHING WRITTEN' % len(heads))
    h = heads[0]
    end = next((k for k in range(h + 1, len(L) + 1) if L[k - 1].startswith('@@ BLOCK ')), len(L))
    out = []
    for k in range(h + 1, end):
        m = re.match(r'^@@ P (b\d+)$', L[k - 1])
        if not m:
            continue
        if L[k] != 'NEW>>' or L[k + 2] != '<<NEW':
            sys.exit('### the entry %s at :%d is not one line between NEW>> and <<NEW -- NOTHING WRITTEN' % (m.group(1), k))
        out.append((m.group(1), k + 2, L[k + 1]))
    if tuple(a for a, _k, _t in out) != WANT:
        sys.exit('### BLOCK P`s entries %s, not %s -- NOTHING WRITTEN' % ([a for a, _k, _t in out], list(WANT)))
    bad = [a for a, _k, t in out if not t.startswith(PLACE) or '\r' in t or t != t.strip()]
    if bad:
        sys.exit('### entries not one clean line opening "%s": %s -- NOTHING WRITTEN' % (PLACE.strip(), bad))
    return out, (h, end - 1)


def bank(out, span):
    return ['b760 -- THE PLACES OF ACTS WHOSE FERRIES CARRY NONE, (R370)(5)(ii): BANKED FROM BLOCK P OF THE TEXT BLOCK (%s)' % time.strftime('%Y-%m-%d', time.gmtime()),
            '',
            '### rows: <act> | <the place, BLOCK P`s line unedited>. Source: relay data/%s :%d-:%d (BLOCK P), the text bank`s sha256 %s..., equal to'
            % (TEXT, span[0], span[1], TEXT_SHA[:16]),
            '### (R370) PATHS (data/b760_ferry.txt :7); each row`s line of the text bank: %s. Written by tools/b760_places.py; read by'
            % ', '.join('%s :%d' % (a, k) for a, k, _t in out),
            '### tools/standing/handoff.py (v1.36.9) where an act`s ferry carries no THE ACT`S PLACE line.',
            ''] + ['%s | %s' % (a, t) for a, _k, t in out]


def main(argv):
    if not argv or argv[0] not in ('dry', 'write'):
        sys.exit(__doc__)
    out, span = rows()
    B = bank(out, span)
    print('### BLOCK P at data/%s :%d-:%d ; entries %d %s ; each one line opening "%s"' % (
        TEXT, span[0], span[1], len(out), ['%s :%d' % (a, k) for a, k, _t in out], PLACE.strip()))
    for a, k, t in out:
        print('  %s :%d, %d characters, sha256 %s' % (a, k, len(t), hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]))
    if argv[0] == 'dry':
        print(NL.join(B))
        return
    b = (NL.join(B) + NL).encode('utf-8')
    p = os.path.join(D, OUT)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    print('written data/%s: %d lines, %d bytes, sha256 %s' % (OUT, len(B), len(b), hashlib.sha256(b).hexdigest()[:16]))


if __name__ == '__main__':
    main(sys.argv[1:])
