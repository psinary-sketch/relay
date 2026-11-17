# -*- coding: utf-8 -*-
"""b758_face.py -- THE ACT'S FACE, COMPOSED: b757's sealed face (lines above its lock block) read unedited, the standing paragraphs between b757's blocks carried by the
act shift, the act's own blocks from tools/b758_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b757's own blocks' first and last lines in b757's face, no line number kept.
Writes data/b758_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool from tools/b757_face.py, its MAP, PAT, LOGS and FIXES set by hand,
and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes (data/b758_probe_<part>.txt) and the pre-lock comparison.
### (R368)(10): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py and its one amendment row (data/b758_amendments.json row 1, amending (1), widening nothing), the regeneration printed into the face's (W) section before the lock.
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
DECLARED = ('G-AXIOM-CLAIM', 'G-RESEARCH-REPRODUCES', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-PUSHOUT-COMMITTED')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452, carried) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b757 carried it.",
    "### `G-RESEARCH-REPRODUCES` reads tools/research/reproduce.py`s full run banked at the act (data/b758_reproduce.txt and .json), which stand absent: the run calls rows that compute at a field (the Epstein control`s I-54, I-80, I-81, I-82 and I-85, and the class groups of I-106), which (R368)(10) bars, \"nothing computed at any field\" (data/b758_ferry.txt :27); neither the run nor a part of it was run, a part being no run the arm reads, so the arm fails on the absent bank (the probe of standing-a2 :58), as at b757.",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :126), as at b757`s pre-run; b758 banks no cut bank, and (R368) names neither the rule`s pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean at :10 or :11, b726`s certificates (commit c9add92) carried onto main by (4)`s landing with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`. The axioms print of run 44007490629, the run that built v0.40`s tree, reads each of the fifteen C2Walk.cert_m<n> with no axiom, so no fallback branch was taken and sorryAx stands in neither run`s print; the counter counts the text (data/b758_events.txt (58)). (R368) orders no write of those files, so they stand as landed; b757`s one unequal pair, SIDE-dirichlet-mod-24, was mended by (6)(i)`s route (events (38)).",
    "### `G-PUSHOUT-COMMITTED` wants the step-zero commit`s files to be the previous act`s closing push capture alone (data/b757_relay_push-b757-closing_push_out.txt, tools/standing/fold/checks.tpl :1673); b757 stopped at [22] on the author`s word, its closing push never ran and no such capture exists; its close, [22] to [25], ran at b758 under (R368)(1) and was committed under component 1 at 401d3bda with no push-b757-closing branch and no push, the commit reaching the remote with b758`s first relay push (data/b758_events.txt (20), (58); the probe of standing-a2 :51); (R368)(2) lists b757`s uncommitted files and names no closing capture.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and carried to the next corrigendum, not a letter (the ferry`s Component 5, data/b758_ferry.txt :44).",
)
NEWLY = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-HOOK-WIRED',
         'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD', 'G-PUSHOUT-COMMITTED', 'G-ROOTDRY-READY', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b758, AT THE FIRST COMPARISON: tools/standing/prelock.py print b758 at 07:11Z and again at 07:3xZ (36 failing, 13 newly against b757`s
# ### pre-run 24), the act part`s probe at 06:59:39Z and standing-a2`s at 07:04:27Z, at a483ffa0; of the thirteen, G-PUSHOUT-COMMITTED fails on
# ### real state and is declared above; G-HOOK-WIRED read this act`s refusals bank absent at the probes and reads it present since the hook`s
# ### first refusal (07:26:13Z, data/b758_events.txt (63)), every clause true at a read-only evaluation (07:3xZ), so it is not declared; the
# ### eleven others each read an object not yet written (the face, the gate and its records, the seal, the root dry, the guard`s dry, the
# ### command bank). G-AXIOM-CLAIM, G-RESEARCH-REPRODUCES, G-RULE-RECUT-QUOTE and G-NO-SORRY-MAIN failed at b757`s pre-run too and fail here.
# ### Set again from the last comparison before the gate.


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


WORDS = ('no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four')


def _refusal_rows(act):
    """the hook's refusals bank of an act, one row a line ("<time> | <KIND> | <tool> | ..."), as (line number, time, kind); () where absent."""
    p = os.path.join(D, '%s_hook_refusals.txt' % act)
    if not os.path.exists(p):
        return ()
    out = []
    for n, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
        f = [x.strip() for x in l.split(' | ')]
        if len(f) >= 2 and re.match(r'^\d{4}-\d\d-\d\dT[\d:]+Z$', f[0]) and re.match(r'^[A-Z]+$', f[1]):
            out.append((n, f[0], f[1]))
    return tuple(out)


def _kinds(rows):
    k = {}
    for _n, _t, kind in rows:
        k[kind] = k.get(kind, 0) + 1
    return k


def refusals():
    """### b758, from the bank (no count kept by hand): the hook's refusals before this lock counted by kind, against b757's bank, and the kinds
    above b757's count, each one event by [U3] (data/b754_rules.txt (12)). Returns (n, kinds, sentence)."""
    own, prev = _refusal_rows('b758'), _refusal_rows('b757')
    ko, kp = _kinds(own), _kinds(prev)
    kinds = ', '.join('%s %d' % (k, ko[k]) for k in sorted(ko)) or 'NONE'
    pk = ', '.join('%s %d' % (k, kp[k]) for k in sorted(kp)) or 'none'
    if not own:
        return '0', 'NONE', ('The hook refused nothing before this lock (data/b758_hook_refusals.txt absent), so by [U3] no kind stands above '
                             'b757`s count (data/b757_hook_refusals.txt: %s).' % pk)
    rows = '; '.join('%s :%d %s' % (kind, n, t[11:]) for n, t, kind in own)
    above = ', '.join('%s %d against %d' % (k, ko[k], kp.get(k, 0)) for k in sorted(ko) if ko[k] > kp.get(k, 0))
    s = ('The hook refused %d call%s before this lock, each before it ran (data/b758_hook_refusals.txt: %s), counted by kind %s against b757`s '
         'bank`s %s; by [U3] each kind above b757`s count is one event of data/b758_events.txt and takes no letter: %s.'
         % (len(own), '' if len(own) == 1 else 's', rows, kinds, pk, above or 'none above it'))
    return str(len(own)), kinds, s


def summaries():
    """### b758, from the events bank: the act's summaries of the session, its rows headed "A ... SUMMARY OF THE SESSION" (b757's after its lock,
    rows headed "... AFTER b757'S LOCK", left out). Returns the phrase "<n words> summaries within it (events (a), ..., (z))"."""
    t = open(os.path.join(D, 'b758_events.txt'), encoding='utf-8').read()
    ns = [m.group(1) for m in re.finditer(r"(?m)^    \((\d+)\) THE HOST'S \[[^\]]*\]: ([^\n]*)", t)
          if 'SUMMARY OF THE SESSION' in m.group(2) and "AFTER b757'S LOCK" not in m.group(2)]
    lst = ', '.join('(%s)' % n for n in ns[:-1]) + (' and (%s)' % ns[-1] if len(ns) > 1 else '(%s)' % ns[-1] if ns else '')
    return '%s summar%s within it (events %s)' % (WORDS[len(ns)] if len(ns) < len(WORDS) else len(ns), 'y' if len(ns) == 1 else 'ies', lst)


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
    rn, rk, rs = refusals()
    t = t.replace('@@REFUSED_N@@', rn).replace('@@REFUSED_KINDS@@', rk).replace('@@REFUSALS_ZERO@@', rs)
    t = t.replace('@@SUMMARIES@@', summaries())
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
