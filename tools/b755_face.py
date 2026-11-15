# -*- coding: utf-8 -*-
"""b755_face.py -- THE ACT'S FACE, COMPOSED: b754's sealed face (lines above its lock block) read unedited, the standing paragraphs between b754's blocks carried by the
act shift, the act's own blocks from tools/b755_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b754's own blocks' first and last lines in b754's face, no line number kept.
Writes data/b755_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool from tools/b754_face.py, its MAP, PAT, LOGS and FIXES set by hand,
and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes (data/b755_probe_<part>.txt) and the pre-lock comparison.
### (R365)(8): the (W) row and N5's write clause regenerated from the ruling and the two amendment rows (data/b755_amendments.json) by tools/standing/amend.py, the regeneration printed into the face's (W) section before the lock.
### The face is written whole to a scratch name beside it and moved over the face only after the write returns (no zero-byte husk on an error).
### Composed after the act's last commit before the gate and before the gate's add (tools/standing/fold/checks.tpl nothing_ahead_ok :1306 reads every commit to
### the lock declared on the face by hash but the gate's step commits; b754's face, written before its commit 6f50851e, left that one out: data/b755_carried_faults.txt (10)).
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
import b755_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b754_registration_2026-11-12.txt'), os.path.join(D, 'b755_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b754_face_blocks.txt'), os.path.join(T, 'b755_face_blocks.txt')
FERRY = os.path.join(D, 'b755_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
MAP = {'b754_registration_2026-11-12': 'b755_registration_%s' % K.DATE, 'b754': 'b755', 'b753': 'b754', '(R364)': '(R365)', 'R364': 'R365', 'v1.34.5': 'v1.34.6'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b754_registration_2026-11-12', '(R364)', 'R364', 'v1.34.5', 'b754', 'b753')))
LOGS = ((ROOT, '28255aea'), (K.PP, '0545f368'))   # ### b754's closing step row and its PLACE-papers record: the pre-face commits after them
W_ANCHOR = '### No Zeta23 or vendored byte;'
FIXES = (   # ### b755: the lock gate is the act's own, (R365)(2)(i), where b754's face carried b378's name in the gate order
    ('`b378_lockgate.py b755', '`tools/b755_lockgate.py b755'),
)
# ### the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ', 'G-DELETE-FREE', 'G-DELETES-ONE-BRANCH')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :22); its predicate (tools/b649_checks.py :452, carried) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b754 carried it.",
    "### `G-RULE-POSTSEAL-READ` raises TypeError at every reading (the probe of standing-a2 :124: \"'bool' object is not subscriptable\"): tools/standing/postseal.py wrap() reads the rule arm`s bool as a tuple (b741`s defect (n)), unrepaired at v1.34.6, outside (R365)(2)`s three repairs; the arm cannot pass and is carried, the repair a version`s.",
    "### `G-DELETE-FREE` reads the act`s tools` code, prose stripped, for a delete (tools/standing/fold/checks.tpl :1813; the probe of standing-a2 :78): tools/b755_lockgate.py :64 carries `shutil.rmtree` over the gate`s own temporary folder, carried from tools/b754_lockgate.py :61 by (R365)(2)(i); b754 failed the arm from its pre-run on and after its push (data/b755_carried_faults.txt (9)), its probe passing it only before its lock gate existed; (R365)(2) orders no other repair, so the arm is declared and carried.",
    "### `G-DELETES-ONE-BRANCH` fails on one clause of its seven (the probe of the act part :25; tools/standing/fold/checks.tpl :833, read clause by clause): the ruling's kept clause, read by tools/standing/allow.py kept_clause in its three forms (:124-:126), none of which (R365) carries; its delete clause (data/b755_ferry.txt :30) names the push-b754-* branches and no kept branch, and its (9) (:32) keeps every kernel branch in words the reader does not read. The five deletes read each one branch, no glob, no variable, nothing chained after, each allowed, port-b707 not among them; widening the reader's forms is a version's change, outside (R365)(2)'s three repairs, so the arm is declared and carried.",
    "### An arm failing at step [7] on real state beyond these is an event, not a letter.",
)
NEWLY = ('G-CLOSING-DRY-STEP', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-LOCKGATE-EIGHT', 'G-ROOTDRY-READY', 'G-SEAL-VERIFIES',
         'G-SEALED-AFTER-COMPONENTS')
# ### FINAL: tools/standing/prelock.py print b755 at 03:45:40Z (30 failing, 7 newly), after the record routes, the ten prev-mode dry
# ### parts and the probes of standing-a1, standing-a2 and the act part at one HEAD (0b5ab44e); at 03:28:06Z, every part's probe taken
# ### before the record routes (the act part's at 02:06:23Z), it read 34 failing and 11 newly


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
    """the paragraphs of b754's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    stale = sorted(set(re.findall(r'b755_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b755')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b755', ferry, t, rows)
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
