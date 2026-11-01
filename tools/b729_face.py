# -*- coding: utf-8 -*-
"""b729_face.py -- THE ACT'S FACE, COMPOSED: b728's sealed face (lines above its lock block) read unedited, the standing paragraphs carried by the
act shift, the act's own blocks from tools/b729_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)). Writes
data/b729_registration_2026-10-31.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool.
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
OLD, NEW = os.path.join(D, 'b728_registration_2026-10-31.txt'), os.path.join(D, 'b729_registration_2026-10-31.txt')
BLOCKS = os.path.join(T, 'b729_face_blocks.txt')
KEEP = ('keiper-b725', 'c2-b725', 'scratch-b724', 'rebuild-b721')
MAP = {'b728': 'b729', 'b727': 'b728', '(R338)': '(R339)', 'R338': 'R339', 'v1.8.0': 'v1.9.0'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('(R338)', 'R338', 'v1.8.0', 'b728', 'b727')))
LOGS = ((ROOT, '0650a188'), ('D:/MY-DOwnloads/PLACE-papers', '26fb938'), ('D:/SIDE-explicit-formula', 'b91bf5af..c2-b725'),
        ('D:/SIDE-explicit-formula', '2cb3936c..keiper-b725'), ('D:/SIDE-explicit-formula', 'main..detect-b729'))


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
    parts = [B['HEAD'], '', '', B['ZERO'], '', '', B['A'], '', '', L(132, 133), B['B_TOOLS'], L(144, 150), B['B_LAST'], '', '', B['C'], '', '', B['D'], '', '', L(182, 189),
             L(190, 200), B['NEEDLES'], '', '', L(205, 233), B['G2'], L(239, 245), B['G2_RUN'], L(252, 276), '', '', B['W'], '', '', B['Z'], '']
    t = '\n'.join(parts).replace('@@PREFACE@@', PRE_FACE_TITLE + ' ' + pre_face())
    t = t.replace('(R339)(8)`s (W) list', '(R339)(9)`s (W) list').replace('read (R339)(8) and the rules banks', 'read (R339)(9) and the rules banks')   # ### b728's (W) clause, this act's (9)
    t = t.replace('`tools/b729_*.py` and `tools/b728_*.py` run unedited', '`tools/b728_*.py` run unedited')
    left = re.findall(r'@@\w+@@', t)
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    open(NEW, 'w', encoding='utf-8', newline='').write(t)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
