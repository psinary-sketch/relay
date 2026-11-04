# -*- coding: utf-8 -*-
"""b739_face.py -- THE ACT'S FACE, COMPOSED: b738's sealed face (lines above its lock block) read unedited, the standing paragraphs between b738's blocks carried by the
act shift, the act's own blocks from tools/b739_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b738's own blocks' first and last lines in b738's face, no line number kept.
Writes data/b739_registration_2026-11-04.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool, carried from tools/b738_face.py, its MAP, PAT and LOGS set by hand.
### (R349)(4): the (W) row and N5's write clause regenerated from the ruling plus the amendment rows (data/b739_amendments.json) by
### tools/standing/amend.py, the regeneration printed into the face's (W) section before the lock; faceform.w_row read the ruling's clauses alone.
"""
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
from standing import faceform as FF   # noqa: E402,F401
from standing.faceform import PRE_FACE_TITLE   # noqa: E402
from standing import amend as AM   # noqa: E402
import b739_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b738_registration_2026-11-03.txt'), os.path.join(D, 'b739_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b738_face_blocks.txt'), os.path.join(T, 'b739_face_blocks.txt')
FERRY = os.path.join(D, 'b739_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
MAP = {'b738_registration_2026-11-03': 'b739_registration_%s' % K.DATE, 'b738': 'b739', 'b737': 'b738', '(R348)': '(R349)', 'R348': 'R349', 'v1.18.0': 'v1.19.0'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b738_registration_2026-11-03', '(R348)', 'R348', 'v1.18.0', 'b738', 'b737')))
LOGS = ((ROOT, '3f45857d'), ('D:/MY-DOwnloads/PLACE-papers', '42dba04'))   # ### b738's closing and its PLACE-papers record: the pre-face commits after them
W_ANCHOR = '### No Zeta23 or vendored byte;'
# ### the carried paragraphs read seven suite parts where b738 split them into ten ((R348)(2)(vi)); each sentence set to the ten here, by
# ### an exact pair that must occur once in the composed face, printed, else refused
FIXES = (
    ('`fold.py checks --prerun` IN ITS SEVEN PARTS (R202)(3), each its own',
     '`fold.py checks --prerun` IN ITS TEN PARTS (R202)(3), each its own'),
    ('over b738`s seven\n### committed part banks', 'over b738`s ten\n### committed part banks'),
    ('recomputes the chain at commit in three parts by act with the\n### suite`s own remote reads, its range read from data/act_current.json -- standing-b2a the first quarter, banked, standing-b2b the second,\n### banked, and standing-b3 the second half through b739,',
     'recomputes the chain at commit in five parts by act with the\n### suite`s own remote reads, its range read from data/act_current.json -- standing-b2a to standing-b2d the first half`s four quarters,\n### each banked, and standing-b3 the second half through b739,'),
    ('standing arms run in the suite`s first six parts -- `G-NODISCLOSURE-PUBLIC` and the four figures` arms in standing-c, `G-SHARED-ADDITIVE`\n### in standing-b1, no arm in standing-b2a or standing-b2b, `G-ACTROOT-VERIFY` in standing-b3, every other standing arm and the rule arms in\n### standing-a -- and this act`s arms in the seventh,',
     'standing arms run in the suite`s first nine parts -- `G-NODISCLOSURE-PUBLIC` and the four figures` arms in standing-c, `G-SHARED-ADDITIVE`\n### in standing-b1, no arm in standing-a1 or in standing-b2a to standing-b2d, `G-ACTROOT-VERIFY` in standing-b3, every other standing arm and the rule arms in\n### standing-a2 -- and this act`s arms in the tenth,'))


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
    """the paragraphs of b738's face standing between its blocks: gap[k], the lines after block k up to the next, blank edges cut; the lines found by each block's own last
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
    for a_, b_ in FIXES:
        if t.count(a_) != 1:
            print('REFUSED: a carried sentence to set found %d times: %s' % (t.count(a_), a_[:80].replace('\n', ' / ')))
            return 2
        t = t.replace(a_, b_)
        print('SET (ten parts):', b_[:100].replace('\n', ' / '))
    left = [x for x in re.findall(r'@@\w+@@', t) if x != '@@N5_WRITES@@']   # ### N5's write clause filled after the (W) regeneration below
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    stale = sorted(set(re.findall(r'b739_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b739')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b739', ferry, t, rows)
    t = t.replace(W_ANCHOR, '\n'.join(regen) + '\n' + W_ANCHOR)
    t = t.replace('@@N5_WRITES@@', AM.n5_clause(ferry, rows, t).upper())
    left = re.findall(r'@@\w+@@', t)
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    print('\n'.join(regen))
    print('(W) COVERS THE RULING`S CLAUSE-ORDERED FILES:', AM.writes(ferry, rows), '; THE COMPOSER`S ROW:', row or 'NONE NEEDED', '; MISSING AFTER:', AM.missing(ferry, rows, t))
    if '--dry' in sys.argv:
        print('DRY: nothing written', len(t), 'chars', t.count('\n'), 'lines')
        return 0
    open(NEW, 'w', encoding='utf-8', newline='').write(t)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
