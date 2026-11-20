# -*- coding: utf-8 -*-
"""b763_face.py -- THE ACT'S FACE, COMPOSED: b762's sealed face (lines above its lock block) read unedited, the standing paragraphs between b762's blocks carried by the
act shift, the act's own blocks from tools/b763_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b762's own blocks' first and last lines in b762's face, no line number kept.
Writes data/b763_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Carried from tools/b762_face.py by tools/b763_carry.py (data/b763_carry_face.txt),
its OLD, MAP, PAT, the LOGS comment, FIXES and the summaries reader set by hand (data/b763_events.txt (67)), and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes
(data/b763_probe_<part>.txt) and the pre-lock comparison.
### (R373)(13): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py, no amendment row at b763 (data/b763_amendments.json absent, the author's word since the delivery none), the regeneration printed into the face's (W) section before the lock.
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
import b763_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b762_registration_2026-11-19.txt'), os.path.join(D, 'b763_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b762_face_blocks.txt'), os.path.join(T, 'b763_face_blocks.txt')
FERRY = os.path.join(D, 'b763_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
# ### b763: the shift of b762's face by one act (b762 -> b763, b761 -> b762, R372 -> R373); tools/standing/ moved by (R373)(5) alone, v1.37.1
# ### to v1.37.2 (data/b763_standing_v1372.txt), which b763's own blocks say; a name two acts back, push-b759-weil and data/b759_outcomes.txt
# ### among them, stands unshifted (the carry had left b762's pair b760 -> b761 carried to b760 -> b762 and its OLD at b761's date)
MAP = {'b762_registration_2026-11-19': 'b763_registration_%s' % K.DATE, 'b762': 'b763', 'b761': 'b762', '(R372)': '(R373)', 'R372': 'R373'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b762_registration_2026-11-19', '(R372)', 'R372', 'b762', 'b761')))
# ### b763: b762's closing commits as (R373)'s SCOPE READ gives them, relay 3fe5b17c and PLACE-papers 87cab4f2 (data/b763_ferry.txt :3), the
# ### worklist's PRE_RELAY and PRE_PP: the pre-face commits after them (the carry had left b761's fb9fbaef and da82a9d5 in this comment)
LOGS = ((ROOT, K.PRE_RELAY), (K.PP, K.PRE_PP))
W_ANCHOR = '### No Zeta23 or vendored byte;'
# ### b763: (G1)'s order as b762's face carries it between its blocks, "-> COMPONENTS 0-5 AND COMPONENT 6`S BANKS (the listings before any
# ### clause;" (data/b762_registration_2026-11-19.txt :200), is b763's own: b763 ran the ferry's Components 0 to 5 and Component 6's banks
# ### before this face (data/b763_ferry.txt :137-:143), so nothing is set. The (W) list is (R373)(13)'s, as (R372)'s was its (13), the shift
# ### carrying b762's "(R372)(13)`s (W) list" (:242) to it with nothing set. b762's face already carries its rules sentence as set at b762,
# ### "(R372) ordering no rules row and no data/b762_rules.txt written" (:277), which the shift carries to (R373) and data/b763_rules.txt:
# ### (R373) orders no rules row and none is written (the act module's G-RULES-ROW-ENTERED reads so), so FIXES is empty and nothing is set.
FIXES = ()
# ### the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b762 carried it (data/b762_events.txt (50)).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :126), as at b762`s pre-run. b763 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b763_*cut.txt in the tree; its re-cut inputs bank, data/b763_recut_inputs.txt, does not end in cut.txt), so it adds to neither count, and the searches read fail NONE (:38). (R373) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean at :10 or :11, b726`s certificates (commit c9add92) carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b762. The axioms print of run 44670834879, the run that built v0.43`s tree at main 819e4a83, reads each C2Walk.cert_m<n> with no axiom (its artifact`s axioms.txt :136-:153), so no fallback branch was taken and sorryAx stands nowhere in its print; the counter counts the text (data/b762_events.txt (50)). The one pair the first standing-a1 probe read unequal, the kernel`s clone checked out at push-b763-keiper, was returned to main by the one-call tool`s switch before the probe these cites read (data/b763_events.txt (84)); (R373) removes no kernel branch ((4)), and the M<n> files stand as landed.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and carried to the next corrigendum, not a letter (the ferry`s Component 6, data/b763_ferry.txt :143).",
)
NEWLY = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT',
         'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS', 'G-WRITELIST-MIRROR-STATE')
# ### b763: DECLARED and DECLARED_LINES set by hand from b763's probes (standing-a1 :20, :22, :23 at 07:06:06Z; standing-a2 :38, :126 at
# ### 07:10:43Z): three of the four arms b762 declared, each line read against b763's own state (data/b763_events.txt (84), (85)): b763 banks
# ### no cut bank and no search, and no kernel branch is removed; G-DELETE-FREE passing (b763 has no page tool, the probe of standing-a2
# ### :79), so not declared. NEWLY the twelve of `tools/standing/prelock.py print b763` at 08:08:13Z (read 116, failing 34, at b762's
# ### pre-run 23, banks absent NONE): b762's thirteen less G-DELETE-FREE, each an object of the record, the lock or the seal not yet
# ### written, G-DELETES-ONE-BRANCH reading the command bank data/b763_commands.txt, written at the record. Set again from the last
# ### comparison before the gate where it differs.


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
    """the paragraphs of b762's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    """### b763, from the bank (no count kept by hand): the hook's refusals before this lock counted by kind, against b762's bank, and the kinds
    above b762's count, each one event by [U3] (data/b754_rules.txt (12)). Returns (n, kinds, sentence)."""
    own, prev = _refusal_rows('b763'), _refusal_rows('b762')
    ko, kp = _kinds(own), _kinds(prev)
    kinds = ', '.join('%s %d' % (k, ko[k]) for k in sorted(ko)) or 'NONE'
    pk = ', '.join('%s %d' % (k, kp[k]) for k in sorted(kp)) or 'none'
    if not own:
        return '0', 'NONE', ('The hook refused nothing before this lock (data/b763_hook_refusals.txt absent), so by [U3] no kind stands above '
                             'b762`s count (data/b762_hook_refusals.txt: %s).' % pk)
    rows = '; '.join('%s :%d %s' % (kind, n, t[11:]) for n, t, kind in own)
    above = ', '.join('%s %d against %d' % (k, ko[k], kp.get(k, 0)) for k in sorted(ko) if ko[k] > kp.get(k, 0))
    s = ('The hook refused %d call%s before this lock, each before it ran (data/b763_hook_refusals.txt: %s), counted by kind %s against b762`s '
         'bank`s %s; by [U3] each kind above b762`s count is one event of data/b763_events.txt and takes no letter: %s.'
         % (len(own), '' if len(own) == 1 else 's', rows, kinds, pk, above or 'none above it'))
    return str(len(own)), kinds, s


def summaries():
    """### b763, from the events bank: the act's summaries of the session, the host's rows whose head line names a SUMMARY (b763's rows read
    "A SUMMARY WITHIN STEP ZERO", "A SECOND AND A THIRD SUMMARY", "A FOURTH SUMMARY", ...), each row counted for each summary it names (one,
    and one more for each " AND A "), the summary before the delivery and any row headed "... AFTER b762'S LOCK" left out, and b762's own
    summary after its lock (b763 events (24)) left out by its section, from its head "b762'S FINDINGS AFTER ITS LOCK" to the next, "THE
    NAVIGATOR'S OWN" (b763 events (67)). Returns the phrase "<n words> summaries within it (events (a), ..., (z))"."""
    t = open(os.path.join(D, 'b763_events.txt'), encoding='utf-8').read()
    a_, b_ = "\nb762'S FINDINGS AFTER ITS LOCK", "\nTHE NAVIGATOR'S OWN, FROM (R373)(1)"
    if t.count(a_) != 1 or t.count(b_) != 1 or t.index(a_) > t.index(b_):
        raise SystemExit("REFUSED: the events bank's section of b762's findings after its lock not found once, before the navigator's own")
    t = t[:t.index(a_)] + t[t.index(b_):]
    hits = [(m.group(1), 1 + m.group(2).split('SUMMARY')[0].count(' AND A ')) for m in re.finditer(r"(?m)^    \((\d+)\) THE HOST'S \[[^\]]*\]: ([^\n]*)", t)
            if re.search(r'\bSUMMARY\b', m.group(2)) and 'BEFORE THE DELIVERY' not in m.group(2) and "AFTER b762'S LOCK" not in m.group(2)]
    ns, n_ = [h_[0] for h_ in hits], sum(h_[1] for h_ in hits)
    lst = ', '.join('(%s)' % n for n in ns[:-1]) + (' and (%s)' % ns[-1] if len(ns) > 1 else '(%s)' % ns[-1] if ns else '')
    return '%s summar%s within it (events %s)' % (WORDS[n_] if n_ < len(WORDS) else n_, 'y' if n_ == 1 else 'ies', lst)


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
    t = t.replace('@@NEWLY@@', 'PENDING (tools/standing/prelock.py print b763 not yet run)' if NEWLY is None else (' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE'))
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
    stale = sorted(set(re.findall(r'b763_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b763')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b763', ferry, t, rows)
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
