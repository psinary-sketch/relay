# -*- coding: utf-8 -*-
"""b733_face.py -- THE ACT'S FACE, COMPOSED: b732's sealed face (lines above its lock block) read unedited, the standing paragraphs between b731's blocks carried by the
act shift, the act's own blocks from tools/b733_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b732's own blocks' first and last lines in b732's face, no line number kept.
Writes data/b733_registration_2026-11-02.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool.
"""
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
from standing import faceform as FF   # noqa: E402
from standing.faceform import PRE_FACE_TITLE   # noqa: E402
OLD, NEW = os.path.join(D, 'b732_registration_2026-11-01.txt'), os.path.join(D, 'b733_registration_2026-11-02.txt')
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b732_face_blocks.txt'), os.path.join(T, 'b733_face_blocks.txt')
FERRY = os.path.join(D, 'b733_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721')
MAP = {'b732': 'b733', 'b731': 'b732', 'b733': 'b734', '(R342)(7)': '(R343)(4)', '(R342)': '(R343)', 'R342': 'R343', 'v1.12.0': 'v1.13.0'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('(R342)(7)', '(R342)', 'R342', 'v1.12.0', 'b733', 'b732', 'b731')))
LOGS = ((ROOT, 'a8a702dd'), ('D:/MY-DOwnloads/PLACE-papers', '998dc4a'), ('D:/SIDE-explicit-formula', '1b34964a..zq-b730'))
W_ANCHOR = '### No Zeta23 or vendored byte;'


def shift(s):
    return PAT.sub(lambda m: MAP.get(m.group(0), m.group(0)), s)


def blocks(path):
    out, cur = {}, None
    for l in open(path, encoding='utf-8').read().split('\n'):
        m = re.match(r'^@@@ (\S+)$', l)
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur:
            out[cur].append(l)
    return {k: '\n'.join(v).rstrip('\n') for k, v in out.items()}


def carried(o, old):
    """the paragraphs of b730's face standing between its blocks: gap[k], the lines after block k up to the next, blank edges cut; the lines found by each block's own last
    and first lines, each read once."""
    gaps = {}
    i = 0   # ### a gap kept line for line, its blank lines the face's own
    for n, k in enumerate(ORDER):
        ls = old[k].split('\n')
        first = next(l for l in ls if l and '@@' not in l)
        last = ls[-1]
        a = o.index(first, i)
        b = o.index(last, a)
        if n:
            gaps[ORDER[n - 1]] = o[i:a]
        i = b + 1
    return gaps


def pre_face():
    hs = []
    for repo, r in LOGS:
        rng = r if '..' in r else r + '..HEAD'
        hs += subprocess.run(['git', '-C', repo, 'rev-list', '--reverse', rng], capture_output=True, text=True).stdout.split()
    return ' '.join(h[:8] for h in hs)


def main():
    if os.path.exists(NEW) and 'THE REGISTRATION LOCK' in open(NEW, encoding='utf-8').read():
        print('REFUSED: the face carries its lock block')
        return 2
    o = open(OLD, encoding='utf-8', newline='').read().split('\n')
    o = o[:o.index(next(l for l in o if l.startswith('### THE REGISTRATION LOCK'))) - 1]
    G = carried(o, blocks(OLD_BLOCKS))
    B = blocks(BLOCKS)
    parts = []
    for k in ORDER:
        parts += [B[k]] + [shift(l) for l in G.get(k, [])]
    t = '\n'.join(parts) + '\n'
    t = t.replace('@@PREFACE@@', PRE_FACE_TITLE + ' ' + pre_face())
    t = t.replace('b733_registration_2026-11-01', 'b733_registration_2026-11-02')
    left = re.findall(r'@@\w+@@', t)
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    stale = sorted(set(re.findall(r'b733_registration_(?!2026-11-02)[\d-]+', t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry =open(FERRY, encoding='utf-8', newline='').read()
    row = FF.w_row(ferry, t)
    if row:
        if t.count(W_ANCHOR) != 1:
            print('REFUSED: the (W) anchor')
            return 2
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    print('(W) COVERS THE RULING`S CLAUSE-ORDERED FILES:', FF.clause_writes(ferry), '; THE COMPOSER`S ROW:', row or 'NONE NEEDED', '; MISSING AFTER:', FF.w_missing(ferry, t))
    open(NEW, 'w', encoding='utf-8', newline='').write(t)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
