# -*- coding: utf-8 -*-
"""b758_face.py -- THE ACT'S FACE, COMPOSED: b757's sealed face (lines above its lock block) read unedited, the standing paragraphs between b757's blocks carried by the
act shift, the act's own blocks from tools/b758_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b757's own blocks' first and last lines in b757's face, no line number kept.
Writes data/b758_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool from tools/b757_face.py, its MAP, PAT, LOGS and FIXES set by hand,
and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes (data/b758_probe_<part>.txt) and the pre-lock comparison.
### (R368)(10): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py, no amendment row banked (data/b758_amendments.json absent), the regeneration printed into the face's (W) section before the lock.
### The face is written whole to a scratch name beside it and moved over the face only after the write returns (no zero-byte husk on an error).
### Composed after the act's last commit before the gate and before the gate's add (tools/standing/fold/checks.tpl nothing_ahead_ok reads every commit to
### the lock declared on the face by hash but the gate's step commits).
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
import b758_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b757_registration_2026-11-16.txt'), os.path.join(D, 'b758_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b757_face_blocks.txt'), os.path.join(T, 'b758_face_blocks.txt')
FERRY = os.path.join(D, 'b758_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
MAP = {'b757_registration_2026-11-16': 'b758_registration_%s' % K.DATE, 'b757': 'b758', 'b756': 'b757', '(R367)': '(R368)', 'R367': 'R368', 'v1.35.5': 'v1.36.2'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b757_registration_2026-11-16', '(R367)', 'R367', 'v1.35.5', 'b757', 'b756')))
LOGS = ((ROOT, 'ff65ccdb'), (K.PP, 'b8c0bd73'))   # ### b758: b757's last relay commit (its record's step row) and its PLACE-papers record (data/b758_ferry.txt :3): the pre-face commits after them
W_ANCHOR = '### No Zeta23 or vendored byte;'
FIXES = (   # ### b758: the (W) list is (R368)(10)'s, as b757's was (R367)(10)'s, the shift carrying it right; (G1)'s order set to b758's components
    # ### (G1)'s order, carried from b757's face where b757 set it to its components: b758 ran the ferry's Components 0 to 4 and Component 5's
    # ### banks before this face (data/b758_ferry.txt :39-:44)
    ('-> COMPONENTS 0-5 AND COMPONENT 6`S BANKS (the listings before any clause;', '-> COMPONENTS 0-4 AND COMPONENT 5`S BANKS (the listings before any clause;'),
)
# ### the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes
DECLARED = ('G-AXIOM-CLAIM', 'G-RESEARCH-REPRODUCES', 'G-LISTINGS-BEFORE-CLAUSES', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :21); its predicate (tools/b649_checks.py :452, carried) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b757 carried it.",
    "### `G-RESEARCH-REPRODUCES` reads tools/research/reproduce.py`s full run banked at the act (data/b758_reproduce.txt and .json), which stand absent: the run calls rows that compute at a field (the Epstein control`s I-54, I-80, I-81, I-82 and I-85, and the class groups of I-106), which (R368)(10) bars, \"nothing computed at any field, the builds apart\" (data/b758_ferry.txt :29); neither the run nor a part of it was run, a part being no run the arm reads, so the arm fails on the absent bank (the probe of standing-a2 :56), as at b757.",
    "### `G-LISTINGS-BEFORE-CLAUSES` takes the time of the first captured shell command that carries `branch ... --merged` (tools/acts/b758.py :452, the needle carried from b754`s module) and reads none: step zero`s listing was printed at 05:02:27Z, before the first delete (05:15:35Z), by a scratch reader that called the git listing within itself (data/b758_stepzero.txt :63-:65); a listing run now would follow the deletes, and the needle is not widened to read a scratch file the capture does not hold (data/b758_defects.txt (f); the probe of the act part :27).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b758 banked (R368)(8)(i)`s check, the answers bank read cut before the root`s appended section, as data/b758_cut.txt, re-cut no paper and banked no search, so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :36, :124), where b757`s suite passed it; (R368) orders its repairs under (3) and (8) and names neither the rule`s pattern nor the bank`s name, so neither is changed (data/b758_defects.txt (q)).",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal (tools/no_sorry_main.py :184) and reads 23 kernels, pairs unequal 1, sorry in code 0 (the probe of standing-a1 :18, :20): the one pair SIDE-dirichlet-mod-24, its clone at push-b758-mod24 with HEAD equal to its remote`s main e5ebdd15 and its local main at 597b0869. The gated push`s default mode moved the remote`s main and no local main (tools/push_gated.sh :207, :229, :232); the local fast-forward is carried by neither the one-call tool nor the gated push, so by (R368)(3)`s last sentence the seat stops at that write and prints the route it lacks (data/b758_events.txt (38)); no plain git sent. SIDE-explicit-formula`s clone was returned to main by the one-call tool`s switch before the probe (HEAD = main = origin/main = 8fbab45d).",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and carried to the next corrigendum, not a letter (the ferry`s Component 6, data/b758_ferry.txt :49).",
)
NEWLY = ('G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-LOCKGATE-EIGHT', 'G-NO-SORRY-MAIN', 'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY',
         'G-RULE-RECUT-QUOTE', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS')
# ### FINAL: tools/standing/prelock.py print b758 at 16:06:56Z (31 failing, 9 newly against b757`s pre-run 23), after the record routes, the
# ### ten prev-mode dry parts (the last, the act part, at 15:48:02Z) and the probes of standing-a1 (15:51:59Z), standing-a2 (15:55:58Z) and
# ### the act part (16:03:06Z) at one HEAD (ef7c36db); of the nine, G-NO-SORRY-MAIN and G-RULE-RECUT-QUOTE fail on real state and are declared
# ### above, the other seven each read an object not yet written (the gate, the lock, the seal, the root dry, the closing dry), as b757`s
# ### seven of the same names did at its comparison (tools/b757_face.py :47-:48); at 15:51:42Z, the probes taken before the record routes,
# ### it read 36 failing and 13 newly; G-DELETES-ONE-BRANCH passes on the command bank (16:03:06Z)


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
    """the paragraphs of b757's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    t = t.replace('@@NEWLY@@', 'PENDING (tools/standing/prelock.py print b758 not yet run)' if NEWLY is None else (' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE'))
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
    stale = sorted(set(re.findall(r'b758_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b758')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b758', ferry, t, rows)
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
