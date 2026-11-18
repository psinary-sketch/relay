# -*- coding: utf-8 -*-
"""b759_face.py -- THE ACT'S FACE, COMPOSED: b758's sealed face (lines above its lock block) read unedited, the standing paragraphs between b758's blocks carried by the
act shift, the act's own blocks from tools/b759_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b758's own blocks' first and last lines in b758's face, no line number kept.
Writes data/b759_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Written by the Write tool from tools/b758_face.py, its MAP, PAT, LOGS and FIXES set by hand,
and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes (data/b759_probe_<part>.txt) and the pre-lock comparison.
### (R369)(11): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py, no amendment row at b759 (data/b759_amendments.json absent, the author's word since the delivery none), the regeneration printed into the face's (W) section before the lock.
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
import b759_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b758_registration_2026-11-16.txt'), os.path.join(D, 'b759_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b758_face_blocks.txt'), os.path.join(T, 'b759_face_blocks.txt')
FERRY = os.path.join(D, 'b759_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
MAP = {'b758_registration_2026-11-16': 'b759_registration_%s' % K.DATE, 'b758': 'b759', 'b757': 'b758', '(R368)': '(R369)', 'R368': 'R369', 'v1.36.2': 'v1.36.7'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b758_registration_2026-11-16', '(R368)', 'R368', 'v1.36.2', 'b758', 'b757')))
# ### b759: b758's closing commits as (R369)'s SCOPE READ gives them, relay e43f1369 and PLACE-papers 4ea41948 (data/b759_ferry.txt :3), the
# ### worklist's PRE_RELAY and PRE_PP: the pre-face commits after them (the carry had left b757's ff65ccdb and b8c0bd73)
LOGS = ((ROOT, K.PRE_RELAY), (K.PP, K.PRE_PP))
W_ANCHOR = '### No Zeta23 or vendored byte;'
FIXES = (   # ### b759: the (W) list is (R369)(11)'s, as b758's was (R368)(10)'s, the shift carrying it right; (G1)'s order set to b759's components
    # ### (G1)'s order, carried from b758's face where b758 set it to its components: b759 ran the ferry's Components 0 to 5 and Component 6's
    # ### banks before this face (data/b759_ferry.txt :45-:51)
    ('-> COMPONENTS 0-4 AND COMPONENT 5`S BANKS (the listings before any clause;', '-> COMPONENTS 0-5 AND COMPONENT 6`S BANKS (the listings before any clause;'),
)
# ### the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452, carried) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b758 carried it.",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :126), as at b758`s pre-run. b759 re-cut fourteen paper lines under (R369)(9) and banked them as data/b759_corpus.txt, a name the pattern does not take, so the arm`s reading of b759 is VACUOUS: (R369)(9) orders each OLD read once at its line and no quotation search, and names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean at :10 or :11, b726`s certificates (commit c9add92) carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b758. The axioms print of run 44162171267, the run that built v0.41`s tree, reads each of the fifteen C2Walk.cert_m<n> with no axiom (its axioms.txt :136-:150), so no fallback branch was taken and sorryAx stands nowhere in its print; the counter counts the text (data/b759_events.txt (56)). (R369) orders no write of those files, so they stand as landed.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and carried to the next corrigendum, not a letter (the ferry`s Component 6, data/b759_ferry.txt :51).",
)
NEWLY = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-CLOSING-SENTENCE', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD',
         'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b759, AT THE COMPARISON AFTER THE TEN PROBES: tools/standing/prelock.py print b759 at 00:4xZ (116 read, 35 failing, 13 newly against
# ### b758`s pre-run 24, banks absent NONE), the probes 23:32:31Z to 00:41:09Z at 81ebf3a9 (data/b759_events.txt (55), (56)). Twelve of the
# ### thirteen read an object not yet written when the probes ran (the face and its (W) row, the gate`s dry step and the closing dry, the
# ### guard`s dry, the root dry, the command bank, the lock gate, the seal, the declared arms, the score route`s calls, "score-route calls 0" at
# ### standing-a2 :25); G-CLOSING-SENTENCE read the act module`s carried list of the closing`s headings, defect (i), repaired at 0ccfa075 and
# ### each conjunct read true. G-AXIOM-CLAIM, G-RULE-RECUT-QUOTE and G-NO-SORRY-MAIN failed at b758`s pre-run too and fail here, declared
# ### above; G-PUSHOUT-COMMITTED and G-RESEARCH-REPRODUCES, declared at b758, pass at b759 (standing-a2 :51, :58) and are not declared.
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
    """the paragraphs of b758's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    """### b759, from the bank (no count kept by hand): the hook's refusals before this lock counted by kind, against b758's bank, and the kinds
    above b758's count, each one event by [U3] (data/b754_rules.txt (12)). Returns (n, kinds, sentence)."""
    own, prev = _refusal_rows('b759'), _refusal_rows('b758')
    ko, kp = _kinds(own), _kinds(prev)
    kinds = ', '.join('%s %d' % (k, ko[k]) for k in sorted(ko)) or 'NONE'
    pk = ', '.join('%s %d' % (k, kp[k]) for k in sorted(kp)) or 'none'
    if not own:
        return '0', 'NONE', ('The hook refused nothing before this lock (data/b759_hook_refusals.txt absent), so by [U3] no kind stands above '
                             'b758`s count (data/b758_hook_refusals.txt: %s).' % pk)
    rows = '; '.join('%s :%d %s' % (kind, n, t[11:]) for n, t, kind in own)
    above = ', '.join('%s %d against %d' % (k, ko[k], kp.get(k, 0)) for k in sorted(ko) if ko[k] > kp.get(k, 0))
    s = ('The hook refused %d call%s before this lock, each before it ran (data/b759_hook_refusals.txt: %s), counted by kind %s against b758`s '
         'bank`s %s; by [U3] each kind above b758`s count is one event of data/b759_events.txt and takes no letter: %s.'
         % (len(own), '' if len(own) == 1 else 's', rows, kinds, pk, above or 'none above it'))
    return str(len(own)), kinds, s


def summaries():
    """### b759, from the events bank: the act's summaries of the session, the host's rows whose head line names a SUMMARY (b759's rows read
    "A SECOND SUMMARY", "AN EIGHTH SUMMARY, AND ...", "...; A NINTH SUMMARY; ...", not b758's "SUMMARY OF THE SESSION"), the summary before the
    delivery (events (2), "... BEFORE THE DELIVERY") and any row headed "... AFTER b758'S LOCK" left out. Returns the phrase "<n words>
    summaries within it (events (a), ..., (z))"."""
    t = open(os.path.join(D, 'b759_events.txt'), encoding='utf-8').read()
    ns = [m.group(1) for m in re.finditer(r"(?m)^    \((\d+)\) THE HOST'S \[[^\]]*\]: ([^\n]*)", t)
          if re.search(r'\bSUMMARY\b', m.group(2)) and 'BEFORE THE DELIVERY' not in m.group(2) and "AFTER b758'S LOCK" not in m.group(2)]
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
    t = t.replace('@@NEWLY@@', 'PENDING (tools/standing/prelock.py print b759 not yet run)' if NEWLY is None else (' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE'))
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
    stale = sorted(set(re.findall(r'b759_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b759')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b759', ferry, t, rows)
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
