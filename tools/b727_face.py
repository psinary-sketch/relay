# -*- coding: utf-8 -*-
"""b727_face.py -- THE ACT'S FACE, COMPOSED: b725's sealed face (lines above its lock block) read unedited, the standing paragraphs carried by the
act shift as b726's composer read them, the act's own blocks from tools/b727_face_blocks.txt. Writes data/b727_registration_2026-10-31.txt alone, and only before the lock:
it refuses when the face already carries a lock block. Written by the Write tool.
"""
import os
import re
import sys

T = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(T), 'data')
OLD, NEW = os.path.join(D, 'b725_registration_2026-10-30.txt'), os.path.join(D, 'b727_registration_2026-10-31.txt')
BLOCKS = os.path.join(T, 'b727_face_blocks.txt')
KEEP = ('keiper-b725', 'c2-b725', 'scratch-b724', 'rebuild-b721')
MAP = {'b725': 'b727', 'b724': 'b726', '(R335)': '(R337)', 'R335': 'R337', 'v1.5.0': 'v1.7.0', '2026-10-30': '2026-10-31'}
PLACE = dict(R83='1 row in 1 class repeating three acts running, printed in the entry for the author beside the next act of (R337)(7)',
             REFUSALS='one command',
             DECLARED=('`G-AXIOM-CLAIM`.\n### `G-AXIOM-CLAIM` reads CONTRADICTED 1, the row b721`s defect (u) and each act since carried, tools/axiom_claim.py outside (W), no bank rewritten. '
                       'An arm failing at step [7] on real state beyond this is an event, not a letter.'))   # ### set by the Edit tool from the banks before the gate
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('(R335)', 'R335', 'v1.5.0', 'b725', 'b724', '2026-10-30')))


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


def main():
    if os.path.exists(NEW) and 'THE REGISTRATION LOCK' in open(NEW, encoding='utf-8').read():
        print('REFUSED: the face carries its lock block')
        return 2
    o = open(OLD, encoding='utf-8', newline='').read().split('\n')
    L = lambda a, b: shift('\n'.join(o[a - 1:b]))
    B = blocks()
    parts = [B['HEAD'], '', '', B['ZERO'], '', '', B['A'], '', '', L(193, 199), B['B_TOOLS'], B['B_STANDING'], B['B_RUN'],
             L(216, 216), B['B_LAST'], '', '', B['C'], '', '', B['D'], '', '', L(253, 258), '', '', L(260, 270), B['NEEDLES'], '', '',
             L(275, 303), B['G2'], L(324, 348), '', '', B['W'], '', '', B['Z'], '']
    t = '\n'.join(parts)
    for k, v in PLACE.items():
        t = t.replace('@@%s@@' % k, v)
    left = re.findall(r'@@\w+@@', t)
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    open(NEW, 'w', encoding='utf-8', newline='').write(t)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
