# -*- coding: utf-8 -*-
"""b726_face.py -- THE ACT'S FACE, COMPOSED: b725's sealed face (lines above its lock block) read unedited, the standing paragraphs carried by the
act shift, the act's own blocks from tools/b726_face_blocks.txt. Writes data/b726_registration_2026-10-30.txt alone, and only before the lock:
it refuses when the face already carries a lock block. Written by the Write tool.
"""
import os
import re
import sys

T = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(T), 'data')
OLD, NEW = os.path.join(D, 'b725_registration_2026-10-30.txt'), os.path.join(D, 'b726_registration_2026-10-30.txt')
BLOCKS = os.path.join(T, 'b726_face_blocks.txt')
KEEP = ('keiper-b725', 'c2-b725', 'scratch-b724', 'rebuild-b721')
MAP = {'b725': 'b726', 'b724': 'b725', '(R335)': '(R336)', 'R335': 'R336', 'v1.5.0': 'v1.6.0'}
PLACE = dict(DISPATCHES='EIGHTEEN', R83='3 rows in 2 classes repeating three acts running, printed in the entry for the author beside the next act of (R336)(10)',
             REFUSALS='one command', C2_COMMIT='8b6a6c71',
             PROBE_NOTE=('relay da63319f -- those banks, the act module`s and the worklist`s stage values and this composer; (`fold.py checks --mid`): the act part, 22 of 31 passing, '
                         'no positive control passing, whose G-BRANCHES-BANKED found defect (u); standing-a twice (data/b726_probe_standing-a_standing-a.txt, '
                         'data/b726_probe2_standing-a.txt), whose first run found defect (v), repaired by the Edit tool before this face`s commit; standing-b3 (data/b726_probe3_standing-b3.txt), '
                         'the chain b659-b725 AGREE, its arm reading no first half in a part run alone.'),
             DECLARED=('`G-AXIOM-CLAIM`.\n### `G-AXIOM-CLAIM` reads CONTRADICTED 1 (the probe: 198 claims, CONTRADICTED 1, VERIFIED 54), the row b721`s defect (u), b722`s (w), b723`s (c`), '
                       'b724`s (r) and b725`s carried, tools/axiom_claim.py outside (W), no bank rewritten.\n### `G-ACTROOT-VERIFY` is not declared: with b723`s row carried on its branch the chain '
                       'reads AGREE at the probe. An arm failing at step [7] on real state beyond this is an event, not a letter.'))   # ### set by the Edit tool from the banks before the gate
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('(R335)', 'R335', 'v1.5.0', 'b725', 'b724')))


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
