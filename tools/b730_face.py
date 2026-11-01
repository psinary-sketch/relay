# -*- coding: utf-8 -*-
"""b730_face.py -- THE ACT'S FACE, COMPOSED: b729's sealed face (lines above its lock block) read unedited, the standing paragraphs between b729's blocks carried by the
act shift, the act's own blocks from tools/b730_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)). The carried paragraphs are found by b729's own
blocks' first and last lines in b729's face, no line number kept. Writes data/b730_registration_2026-11-01.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool.
"""
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
from standing.faceform import PRE_FACE_TITLE   # noqa: E402
OLD, NEW = os.path.join(D, 'b729_registration_2026-10-31.txt'), os.path.join(D, 'b730_registration_2026-11-01.txt')
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b729_face_blocks.txt'), os.path.join(T, 'b730_face_blocks.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'scratch-b724', 'rebuild-b721')
MAP = {'b729': 'b730', 'b728': 'b729', '(R339)': '(R340)', 'R339': 'R340', 'v1.9.0': 'v1.10.0'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('(R339)', 'R339', 'v1.9.0', 'b729', 'b728')))
LOGS = ((ROOT, 'ee4ba59a'), ('D:/MY-DOwnloads/PLACE-papers', 'ea2ba4e'), ('D:/SIDE-explicit-formula', 'main..zq-b730'))


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
    """the paragraphs of b729's face standing between its blocks: gap[k], the lines after block k up to the next, blank edges cut; the lines found by each block's own last
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
        parts += [B[k]] + [shift(l).replace('(R340)(9)`s (W) list', '(R340)(6)`s (W) list').replace('read (R340)(9) and the rules banks', 'read (R340)(6) and the rules banks') for l in G.get(k, [])]
    t = '\n'.join(parts) + '\n'
    t = t.replace('@@PREFACE@@', PRE_FACE_TITLE + ' ' + pre_face())
    t = t.replace('`tools/b730_*.py` and `tools/b729_*.py` run unedited', '`tools/b729_*.py` run unedited')
    left = re.findall(r'@@\w+@@', t)
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    open(NEW, 'w', encoding='utf-8', newline='').write(t)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
