# -*- coding: utf-8 -*-
"""b753_face.py -- THE ACT'S FACE, COMPOSED: b752's sealed face (lines above its lock block) read unedited, the standing paragraphs between b752's blocks carried by the
act shift, the act's own blocks from tools/b753_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b752's own blocks' first and last lines in b752's face, no line number kept.
Writes data/b753_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool, carried from tools/b752_face.py, its MAP, PAT, LOGS and FIXES set by hand,
and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes (data/b753_probe_<part>.txt) and the pre-lock comparison.
### (R363)(9): the (W) row and N5's write clause regenerated from the ruling and the amendment rows (data/b753_amendments.json) by tools/standing/amend.py, the regeneration printed into the face's (W) section before the lock.
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
import b753_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b752_registration_2026-11-10.txt'), os.path.join(D, 'b753_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b752_face_blocks.txt'), os.path.join(T, 'b753_face_blocks.txt')
FERRY = os.path.join(D, 'b753_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
MAP = {'b752_registration_2026-11-10': 'b753_registration_%s' % K.DATE, 'b752': 'b753', 'b751': 'b752', '(R362)': '(R363)', 'R362': 'R363', 'v1.32.0': 'v1.33.0'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b752_registration_2026-11-10', '(R362)', 'R362', 'v1.32.0', 'b752', 'b751')))
LOGS = ((ROOT, '0e855242'), ('D:/MY-DOwnloads/PLACE-papers', '4db2fc1c'))   # ### b752's closing step row and its PLACE-papers record: the pre-face commits after them
W_ANCHOR = '### No Zeta23 or vendored byte;'
FIXES = (   # ### b753, defect (y')'s class: two carried sentences cite the write list as clause (5), which (R363)(9) is; (R363)(5) is the reads
    ('(outside (R363)(5)`s (W) list)', '(outside (R363)(9)`s (W) list)'),
    ('`G-RULES-ROW-ENTERED` read (R363)(5) and the rules banks', '`G-RULES-ROW-ENTERED` read (R363)(9) and the rules banks'),
)
# ### the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ', 'G-DELETES-ONE-BRANCH', 'G-BRANCHES-BANKED', 'G-LISTINGS-BEFORE-CLAUSES')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0); its predicate (tools/b649_checks.py :452, carried) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b752 carried it.",
    "### `G-RULE-POSTSEAL-READ` raises TypeError at every reading (the probe of standing-a2 :124: \"'bool' object is not subscriptable\"): tools/standing/postseal.py wrap() reads the rule arm`s bool as a tuple (b741`s defect (n)), unrepaired at v1.33.0, outside (R363)(7)`s items; the arm cannot pass and is carried, the repair a version`s.",
    "### `G-DELETES-ONE-BRANCH`, `G-BRANCHES-BANKED` and `G-LISTINGS-BEFORE-CLAUSES` fail on one reader: the record tool`s delete_shape (tools/standing/delread.py) reads no branch in the five step-zero deletes, each sent in PowerShell`s form with the interpreter`s quoted path before the one-call tool`s delete route (`commit.py <repo> delete <branch>`, one branch by name, no glob, no variable, nothing chained after), where it reads the bare interpreter`s form (data/b753_defects.txt (u')); with no delete read the capture has no first delete, which the branch row`s arm and the listings arm each ask, and the command bank counts \"BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER 0 OF 0\". The five deletes and their --merged listing stand in the step-zero bank (data/b753_stepzero.txt :90-:95); the reader`s repair a version`s.",
    "### An arm failing at step [7] on real state beyond these is an event, not a letter.",
)
NEWLY = ('G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL',
         'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS')   # ### set from tools/standing/prelock.py print b753 (2026-11-11, after the prev-mode dry): 11 newly failing, 2 of them declared above


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
    """the paragraphs of b752's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    stale = sorted(set(re.findall(r'b753_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b753')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b753', ferry, t, rows)
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
        if '--show' in sys.argv:
            print(t)
        return 0
    tmp = NEW + '.part'
    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        f.write(t)
    os.replace(tmp, NEW)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
