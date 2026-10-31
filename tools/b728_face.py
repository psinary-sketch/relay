# -*- coding: utf-8 -*-
"""b728_face.py -- THE ACT'S FACE, COMPOSED: b727's sealed face (lines above its lock block) read unedited, the standing paragraphs carried by the
act shift, the act's own blocks from tools/b728_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)). Writes
data/b728_registration_2026-10-31.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool.
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
OLD, NEW = os.path.join(D, 'b727_registration_2026-10-31.txt'), os.path.join(D, 'b728_registration_2026-10-31.txt')
BLOCKS = os.path.join(T, 'b728_face_blocks.txt')
KEEP = ('keiper-b725', 'c2-b725', 'scratch-b724', 'rebuild-b721')
MAP = {'b727': 'b728', 'b726': 'b727', '(R337)': '(R338)', 'R337': 'R338', 'v1.7.0': 'v1.8.0'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('(R337)', 'R337', 'v1.7.0', 'b727', 'b726')))
LOGS = ((ROOT, '1bf8a57c'), ('D:/MY-DOwnloads/PLACE-papers', '3742f12'), ('D:/SIDE-rcurve', 'f093005'), ('D:/SIDE-archimedean', '0e3336f'), ('D:/SIDE-spinor', '5c34c72'),
        ('D:/SIDE-explicit-formula', 'ea95a8d..c2-b725'), ('D:/SIDE-explicit-formula', 'f52e188..keiper-b725'))


def shift(s):
    return PAT.sub(lambda m: MAP.get(m.group(0), m.group(0)), s)


def blocks():
    out, cur = {}, None
    for l in open(BLOCKS, encoding='utf-8').read().split('\n'):
        m = re.match(r'^@@@ (\S+)$', l)
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur:
            out[cur].append(l)
    return {k: '\n'.join(v).rstrip('\n') for k, v in out.items()}


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
    L = lambda a, b: shift('\n'.join(o[a - 1:b]))
    B = blocks()
    parts = [B['HEAD'], '', '', B['ZERO'], '', '', B['A'], '', '', L(135, 136), B['B_TOOLS'], L(147, 153), B['B_LAST'], '', '', B['C'], '', '', B['D'], '', '', L(185, 192),
             L(193, 203), B['NEEDLES'], '', '', L(208, 236), B['G2'], L(242, 248), B['G2_RUN'], L(255, 279), '', '', B['W'], '', '', B['Z'], '']
    t = '\n'.join(parts).replace('@@PREFACE@@', PRE_FACE_TITLE + ' ' + pre_face())
    left = re.findall(r'@@\w+@@', t)
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    open(NEW, 'w', encoding='utf-8', newline='').write(t)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
