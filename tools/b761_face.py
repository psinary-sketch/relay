# -*- coding: utf-8 -*-
"""b761_face.py -- THE ACT'S FACE, COMPOSED: b760's sealed face (lines above its lock block) read unedited, the standing paragraphs between b760's blocks carried by the
act shift, the act's own blocks from tools/b761_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b760's own blocks' first and last lines in b760's face, no line number kept.
Writes data/b761_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Carried from tools/b760_face.py by tools/b761_carry.py (data/b761_carry_face.txt),
its OLD, MAP, PAT, the LOGS comment, FIXES and the summaries reader set by hand (data/b761_events.txt (65)), and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes
(data/b761_probe_<part>.txt) and the pre-lock comparison.
### (R371)(13): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py, no amendment row at b761 (data/b761_amendments.json absent, the author's word since the delivery none), the regeneration printed into the face's (W) section before the lock.
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
import b761_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b760_registration_2026-11-18.txt'), os.path.join(D, 'b761_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b760_face_blocks.txt'), os.path.join(T, 'b761_face_blocks.txt')
FERRY = os.path.join(D, 'b761_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
# ### b761: the shift of b760's face by one act (b760 -> b761, b759 -> b760, R370 -> R371); no version pair, tools/standing/ unmoved at
# ### v1.37.1 from b760's close ((R371)(11)), so b760's "v1.37.1" stands as b761's (the carry had left b760's pairs, b758 -> b760 and
# ### v1.36.7 -> v1.37.1, which shift b759's face, not b760's)
MAP = {'b760_registration_2026-11-18': 'b761_registration_%s' % K.DATE, 'b760': 'b761', 'b759': 'b760', '(R370)': '(R371)', 'R370': 'R371'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b760_registration_2026-11-18', '(R370)', 'R370', 'b760', 'b759')))
# ### b761: b760's closing commits as (R371)'s SCOPE READ gives them, relay 622ea434 and PLACE-papers 91b69bf1 (data/b761_ferry.txt :3), the
# ### worklist's PRE_RELAY and PRE_PP: the pre-face commits after them (the carry had left b759's 15f762dd and d711a5d6 in this comment)
LOGS = ((ROOT, K.PRE_RELAY), (K.PP, K.PRE_PP))
W_ANCHOR = '### No Zeta23 or vendored byte;'
# ### b761: (G1)'s order as b760's face carries it between its blocks, "-> COMPONENTS 0-5 AND COMPONENT 6`S BANKS (the listings before any
# ### clause;" (data/b760_registration_2026-11-18.txt :198), is b761's own: b761 ran the ferry's Components 0 to 5 and Component 6's banks
# ### before this face (data/b761_ferry.txt :85-:91), so nothing is set. The (W) list is (R371)(13)'s, as (R370)'s was its (13), the shift
# ### carrying b760's "(R370)(13)`s (W) list" (:240) to it with nothing set. One carried sentence names b760's rules row, "(5)(i)`s row (a)
# ### among them" (:275), (R370)(5)(i)'s; (R371) orders no rules row and no data/b761_rules.txt is written (the act module's
# ### G-RULES-ROW-ENTERED reads so), so that clause is set to say it.
FIXES = (("`G-WRITELIST-MIRROR-STATE` and `G-RULES-ROW-ENTERED` read (R371)(13)`s (W) row and the rules banks, (5)(i)`s row (a) among them",
          "`G-WRITELIST-MIRROR-STATE` and `G-RULES-ROW-ENTERED` read (R371)(13)`s (W) row and the rules banks, (R371) ordering no rules row and no data/b761_rules.txt written"),)
# ### the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b760 carried it (data/b760_events.txt (56)).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :126), as at b760`s pre-run. b761`s own reading is not vacuous and passes: its search data/b761_quote.json, the edition`s, timed at 10:25:09Z before PLACE-papers af9a0f9f, stands beside the one cut bank of b761 the pattern takes, data/b761_wsc_cut.txt, and the searches read fail NONE (:38). (R371) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean at :10 or :11, b726`s certificates (commit c9add92) carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b760. The axioms print of run 44162171267, the run that built v0.41`s tree, reads each of the fifteen C2Walk.cert_m<n> with no axiom (its axioms.txt :136-:150), so no fallback branch was taken and sorryAx stands nowhere in its print; the counter counts the text (data/b760_events.txt (56)). (R371) orders no kernel write beyond the removal of (4), so they stand as landed.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and carried to the next corrigendum, not a letter (the ferry`s Component 6, data/b761_ferry.txt :51).",
)
NEWLY = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD',
         'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS', 'G-WRITELIST-MIRROR-STATE')
# ### b761: DECLARED and DECLARED_LINES set by hand from b761's probes (standing-a1 :20, :22, :23; standing-a2 :38, :126, :133), the same
# ### three arms b760 declared, each line read against b761's own state (data/b761_events.txt (85)); NEWLY the eleven of
# ### `tools/standing/prelock.py print b761` at 13:55:46Z (read 116, failing 34, at b760's pre-run 23, banks absent NONE), each an object of
# ### the record, the lock or the seal not yet written. Set again from the last comparison before the gate where it differs.


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
    """the paragraphs of b760's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    """### b761, from the bank (no count kept by hand): the hook's refusals before this lock counted by kind, against b760's bank, and the kinds
    above b760's count, each one event by [U3] (data/b754_rules.txt (12)). Returns (n, kinds, sentence)."""
    own, prev = _refusal_rows('b761'), _refusal_rows('b760')
    ko, kp = _kinds(own), _kinds(prev)
    kinds = ', '.join('%s %d' % (k, ko[k]) for k in sorted(ko)) or 'NONE'
    pk = ', '.join('%s %d' % (k, kp[k]) for k in sorted(kp)) or 'none'
    if not own:
        return '0', 'NONE', ('The hook refused nothing before this lock (data/b761_hook_refusals.txt absent), so by [U3] no kind stands above '
                             'b760`s count (data/b760_hook_refusals.txt: %s).' % pk)
    rows = '; '.join('%s :%d %s' % (kind, n, t[11:]) for n, t, kind in own)
    above = ', '.join('%s %d against %d' % (k, ko[k], kp.get(k, 0)) for k in sorted(ko) if ko[k] > kp.get(k, 0))
    s = ('The hook refused %d call%s before this lock, each before it ran (data/b761_hook_refusals.txt: %s), counted by kind %s against b760`s '
         'bank`s %s; by [U3] each kind above b760`s count is one event of data/b761_events.txt and takes no letter: %s.'
         % (len(own), '' if len(own) == 1 else 's', rows, kinds, pk, above or 'none above it'))
    return str(len(own)), kinds, s


def summaries():
    """### b761, from the events bank: the act's summaries of the session, the host's rows whose head line names a SUMMARY (b761's rows read
    "A SUMMARY", "A SECOND SUMMARY", ..., "A TENTH SUMMARY" at the carry), the summary before the delivery and any row headed "... AFTER
    b760'S LOCK" left out, and b760's own summaries after its lock (events (27) and (34), "THE NINETEENTH SUMMARY" and "THE TWENTIETH
    SUMMARY") left out by their section, from its head "b760'S FINDINGS AFTER ITS LOCK" to the next, "THE NAVIGATOR'S OWN" (b761 events (65);
    the section's heads read as b761's bank writes them). Returns the phrase "<n words> summaries within it (events (a), ..., (z))"."""
    t = open(os.path.join(D, 'b761_events.txt'), encoding='utf-8').read()
    a_, b_ = "\nb760'S FINDINGS AFTER ITS LOCK", "\nTHE NAVIGATOR'S OWN, FROM (R371)(1)"
    if t.count(a_) != 1 or t.count(b_) != 1 or t.index(a_) > t.index(b_):
        raise SystemExit("REFUSED: the events bank's section of b760's findings after its lock not found once, before the navigator's own")
    t = t[:t.index(a_)] + t[t.index(b_):]
    ns = [m.group(1) for m in re.finditer(r"(?m)^    \((\d+)\) THE HOST'S \[[^\]]*\]: ([^\n]*)", t)
          if re.search(r'\bSUMMARY\b', m.group(2)) and 'BEFORE THE DELIVERY' not in m.group(2) and "AFTER b760'S LOCK" not in m.group(2)]
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
    t = t.replace('@@NEWLY@@', 'PENDING (tools/standing/prelock.py print b761 not yet run)' if NEWLY is None else (' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE'))
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
    stale = sorted(set(re.findall(r'b761_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b761')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b761', ferry, t, rows)
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
