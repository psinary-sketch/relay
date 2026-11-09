# -*- coding: utf-8 -*-
"""b748_face.py -- THE ACT'S FACE, COMPOSED: b747's sealed face (lines above its lock block) read unedited, the standing paragraphs between b747's blocks carried by the
act shift, the act's own blocks from tools/b748_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b747's own blocks' first and last lines in b747's face, no line number kept.
Writes data/b748_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool, carried from tools/b747_face.py, its MAP, PAT, LOGS and FIXES set by hand,
and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes (data/b748_probe_<part>.txt) and the pre-lock comparison.
### (R358)(7): the (W) row and N5's write clause regenerated from the ruling (no amendment row this act) by tools/standing/amend.py, the regeneration printed into the face's (W) section before the lock.
### The face is written whole to a scratch name beside it and moved over the face only after the write returns (no zero-byte husk on an error).
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
import b748_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b747_registration_2026-11-08.txt'), os.path.join(D, 'b748_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b747_face_blocks.txt'), os.path.join(T, 'b748_face_blocks.txt')
FERRY = os.path.join(D, 'b748_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
MAP = {'b747_registration_2026-11-08': 'b748_registration_%s' % K.DATE, 'b747': 'b748', 'b746': 'b747', '(R357)': '(R358)', 'R357': 'R358', 'v1.27.1': 'v1.28.1', 'v1.27.0': 'v1.28.0'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b747_registration_2026-11-08', '(R357)', 'R357', 'v1.27.1', 'v1.27.0', 'b747', 'b746')))
LOGS = ((ROOT, '7d34b587'), ('D:/MY-DOwnloads/PLACE-papers', 'ea29289'))   # ### b747's closing and its PLACE-papers record: the pre-face commits after them
W_ANCHOR = '### No Zeta23 or vendored byte;'
FIXES = ()   # ### b747's (W) clause was (R357)(7); (R358)'s is (7): the shift carries it, nothing to set
# ### the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ', 'G-DELETES-ONE-BRANCH')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0); its predicate (tools/b649_checks.py :452, carried) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b747 carried it.",
    "### `G-RULE-POSTSEAL-READ` raises TypeError at every reading after the seal: tools/standing/postseal.py wrap() reads the rule arm`s bool as a tuple (b741`s defect (n)), unrepaired at v1.28.1, outside (R358)(3)`s items; the arm cannot pass and is carried, the repair a version`s.",
    "### `G-DELETES-ONE-BRANCH` reads the ferry`s kept clause through tools/standing/allow.py kept_clause, which reads neither of its wordings in (R358)`s \"the kept branches as banked, zq-b730 past v0.38\" (ferry :19); the five step-zero deletes each of one branch, by name, no glob, no variable, nothing chained after; standing frozen at v1.28.1 and the clause`s reader outside (R358)(3)`s items, so the arm cannot pass on this ferry and is carried, the reader a version`s.",
    "### An arm failing at step [7] on real state beyond these is an event, not a letter.",
)
NEWLY = ('G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD', 'G-PP-SCOPE', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL',
         'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS')   # ### G-PP-SCOPE: b748 first touches OPEN_TRAILS at the record (the trail), not before the lock


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
    """the paragraphs of b747's face standing between its blocks: gap[k], the lines after block k up to the next, blank edges cut; the lines found by each block's own last
    and first lines, each read once."""
    gaps = {}
    i = 0
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
    t = t.replace('@@DATE@@', K.DATE)
    t = t.replace('@@DECLARED@@', ' '.join('`%s`' % a for a in DECLARED) + '.' if DECLARED else 'NONE.')
    t = t.replace('@@DECLARED_LINES@@\n', ''.join(l + '\n' for l in DECLARED_LINES))
    t = t.replace('@@NEWLY@@', ' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE')
    for a_, b_ in FIXES:
        if t.count(a_) != 1:
            print('REFUSED: a carried sentence to set found %d times: %s' % (t.count(a_), a_[:80].replace('\n', ' / ')))
            return 2
        t = t.replace(a_, b_)
        print('SET:', b_[:100].replace('\n', ' / '))
    left = [x for x in re.findall(r'@@\w+@@', t) if x != '@@N5_WRITES@@']
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    stale = sorted(set(re.findall(r'b748_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b748')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b748', ferry, t, rows)
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
    tmp = NEW + '.part'
    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        f.write(t)
    os.replace(tmp, NEW)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
