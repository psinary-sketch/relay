# -*- coding: utf-8 -*-
"""b764_face.py -- THE ACT'S FACE, COMPOSED: b763's sealed face (lines above its lock block) read unedited, the standing paragraphs between b763's blocks carried by the
act shift, the act's own blocks from tools/b764_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b763's own blocks' first and last lines in b763's face, no line number kept.
Writes data/b764_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Carried from tools/b763_face.py by tools/b764_carry.py (data/b764_carry_face.txt),
its OLD, MAP, PAT, the LOGS comment, FIXES and the summaries reader set by hand (data/b764_events.txt (52)), and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes
(data/b764_probe_<part>.txt) and the pre-lock comparison.
### (R374)(13): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py, no amendment row at b764 (data/b764_amendments.json absent, the author's word since the delivery none), the regeneration printed into the face's (W) section before the lock.
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
import b764_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b763_registration_2026-11-19.txt'), os.path.join(D, 'b764_registration_%s.txt' % K.DATE)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b763_face_blocks.txt'), os.path.join(T, 'b764_face_blocks.txt')
FERRY = os.path.join(D, 'b764_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
# ### b764: the shift of b763's face by one act (b763 -> b764, b762 -> b763, R373 -> R374); tools/standing/ moved by (R374)(5) and (7),
# ### v1.37.2 to v1.38.18 (data/b764_repairs.txt), which b764's own blocks say; a name two acts back, push-b759-weil and data/b759_outcomes.txt
# ### among them, stands unshifted (the carry had left b763's pair b761 -> b762 carried to b761 -> b763)
MAP = {'b763_registration_2026-11-19': 'b764_registration_%s' % K.DATE, 'b763': 'b764', 'b762': 'b763', '(R373)': '(R374)', 'R373': 'R374'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b763_registration_2026-11-19', '(R373)', 'R373', 'b763', 'b762')))
# ### b764: b763's closing commits as (R374)'s SCOPE READ gives them, relay 0f9b1df2 and PLACE-papers 7db9a66c (data/b764_ferry.txt :3), the
# ### worklist's PRE_RELAY and PRE_PP: the pre-face commits after them (the carry had left b762's 3fe5b17c and 87cab4f2 in this comment)
LOGS = ((ROOT, K.PRE_RELAY), (K.PP, K.PRE_PP))
W_ANCHOR = '### No Zeta23 or vendored byte;'
# ### b764: four sentences of b763's face carried between its blocks read against b764 and set (scratch gaps764.py, read-only, 02:57Z).
# ### (G1)'s order at b763's :199 names "COMPONENTS 0-5 AND COMPONENT 6`S BANKS", b763's ferry's components; b764's ferry has Components 0
# ### to 5 (data/b764_ferry.txt :150-:155), and before this face b764 ran 0 to 4 and Component 5's banks. The freeze paragraph (:241) and
# ### the arms' paragraph (:276) name "(R374)(13)`s (W) list" and "(R374)(13)`s (W) row", the shift of b763's (R373)(13); b764's (W) list is
# ### (R374)(14)'s (:44). The arms' paragraph (:249) reads G-DELETES-ONE-BRANCH's allowance "through tools/standing/allow.py at v1.37.1",
# ### the standing VERSION each face since b750 names there (b759 v1.36.7, b760 to b763 v1.37.1); b764's is v1.38.18. b763's rules sentence
# ### (:276), "(R374) ordering no rules row and no data/b764_rules.txt written" after the shift, is true of b764 (C1_RULES LEFT EMPTY BY
# ### (R374)(12)) and stands.
FIXES = (
    ('COMPONENTS 0-5 AND COMPONENT 6`S BANKS', 'COMPONENTS 0-4 AND COMPONENT 5`S BANKS'),
    ('(outside (R374)(13)`s (W) list)', '(outside (R374)(14)`s (W) list)'),
    ('read (R374)(13)`s (W) row and the rules banks', 'read (R374)(14)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.37.1', 'tools/standing/allow.py at v1.38.18'),
)
# ### the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b763 carried it (data/b763_events.txt (85)).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b763`s pre-run. b764 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b764_*cut.txt in the tree), so it adds to neither count, and the searches read fail NONE (:38). (R374) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates (commit c9add92) carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b763. The axioms print of run 44670834879, the run that built v0.43`s tree at main 819e4a83, reads each C2Walk.cert_m<n> with no axiom (its artifact`s axioms.txt :136-:153, as b763 read it, data/b763_events.txt (85)), so no fallback branch was taken and sorryAx stands nowhere in its print; the counter counts the text. b764 writes no Lean byte: its one kernel write is the workflow`s file on push-b764-runner, and the kernel`s clone stood at main when standing-a1 ran (data/b764_events.txt (57)); (R374) removes no kernel branch ((4)), and the M<n> files stand as landed.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/fold/checks.tpl :1814, tools/standing/deletefree.py :1-:12); it fails on five lines of tools/b764_repair_controls.py, the controls` cleanups in their finally blocks at :874-:876, :957-:959, :1047-:1049, :1137-:1139 and :1237-:1239, each `shutil.rmtree(t_, ignore_errors=True)` in a loop over the block`s own tempfile.mkdtemp folders, the path read absolute and its name by the control`s own prefix before the call, a loop variable the reader does not follow (the probe of standing-a2 :80; data/b764_defects.txt (i)). Each removes a folder its own block made under the system`s temporary folder, and nothing of the record is deleted. The tool ran and banked in that form (data/b764_repair_controls.txt) and is not edited, as b762 kept its own for b762 (j); that the reader does not follow a loop variable is a fault of tools/standing/, which (R374)(12) moves under (5) and (7) alone, carried to the next act of the record`s upkeep.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b764_ferry.txt :155; (R374)(5) [K10]).",
)
NEWLY = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETE-FREE', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD',
         'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b764: DECLARED and DECLARED_LINES set by hand from b764's probes (standing-a1 :20, :22, :23 at 01:16:37Z; standing-a2 :38, :80, :127
# ### at 01:21:42Z, and again at 02:30:37Z with the same 25 failing by name): b763's three, each line read against b764's own state, and
# ### G-DELETE-FREE for defect (i) (data/b764_events.txt (62), (64)). NEWLY the thirteen of `tools/standing/prelock.py print b764` at
# ### 02:38:52Z (read 116, failing 35, at b763's pre-run 22, banks absent NONE): b763's twelve (data/b763_prelock.txt :3-:15), each an
# ### object of the record, the lock or the seal not yet written, and G-DELETE-FREE. Set again from the last comparison before the gate
# ### where it differs.


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
    """the paragraphs of b763's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    """### b764, from the bank (no count kept by hand): the hook's refusals before this lock counted by kind, against b763's bank, and the kinds
    above b763's count, each one event by [U3] (data/b754_rules.txt (12)). Returns (n, kinds, sentence)."""
    own, prev = _refusal_rows('b764'), _refusal_rows('b763')
    ko, kp = _kinds(own), _kinds(prev)
    kinds = ', '.join('%s %d' % (k, ko[k]) for k in sorted(ko)) or 'NONE'
    pk = ', '.join('%s %d' % (k, kp[k]) for k in sorted(kp)) or 'none'
    if not own:
        return '0', 'NONE', ('The hook refused nothing before this lock (data/b764_hook_refusals.txt absent), so by [U3] no kind stands above '
                             'b763`s count (data/b763_hook_refusals.txt: %s).' % pk)
    rows = '; '.join('%s :%d %s' % (kind, n, t[11:]) for n, t, kind in own)
    above = ', '.join('%s %d against %d' % (k, ko[k], kp.get(k, 0)) for k in sorted(ko) if ko[k] > kp.get(k, 0))
    s = ('The hook refused %d call%s before this lock, each before it ran (data/b764_hook_refusals.txt: %s), counted by kind %s against b763`s '
         'bank`s %s; by [U3] each kind above b763`s count is one event of data/b764_events.txt and takes no letter: %s.'
         % (len(own), '' if len(own) == 1 else 's', rows, kinds, pk, above or 'none above it'))
    return str(len(own)), kinds, s


def summaries():
    """### b764, from the events bank: the act's summaries of the session, the host's rows whose head line names a SUMMARY or SUMMARIES (b764's
    rows read "TWO SUMMARIES WITHIN STEP ZERO" (7), "A THIRD AND A FOURTH SUMMARY" (30), "A FIFTH SUMMARY" (32), ...), each row counted for each
    summary it names (two for "TWO SUMMARIES"; otherwise one, and one more for each " AND A "), the summary before the delivery and any row
    headed "... AFTER b763'S LOCK" left out, and b763's own rows after its lock (b764 events (13) to (24), (18) among them) left out by their
    section, from its head "b763'S TWELVE FINDINGS AFTER ITS LOCK" to the next, "THE NAVIGATOR'S OWN" (b764 events :78 and :135). Returns the
    phrase "<n words> summaries within it (events (a), ..., (z))"."""
    t = open(os.path.join(D, 'b764_events.txt'), encoding='utf-8').read()
    a_, b_ = "\nb763'S TWELVE FINDINGS AFTER ITS LOCK", "\nTHE NAVIGATOR'S OWN, FROM (R374)(1)"
    if t.count(a_) != 1 or t.count(b_) != 1 or t.index(a_) > t.index(b_):
        raise SystemExit("REFUSED: the events bank's section of b763's findings after its lock not found once, before the navigator's own")
    t = t[:t.index(a_)] + t[t.index(b_):]
    hits = [(m.group(1), 2 if 'TWO SUMMARIES' in m.group(2) else 1 + m.group(2).split('SUMMARY')[0].count(' AND A '))
            for m in re.finditer(r"(?m)^    \((\d+)\) THE HOST'S \[[^\]]*\]: ([^\n]*)", t)
            if re.search(r'\bSUMMAR(?:Y|IES)\b', m.group(2)) and 'BEFORE THE DELIVERY' not in m.group(2) and "AFTER b763'S LOCK" not in m.group(2)]
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
    t = t.replace('@@NEWLY@@', 'PENDING (tools/standing/prelock.py print b764 not yet run)' if NEWLY is None else (' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE'))
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
    stale = sorted(set(re.findall(r'b764_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b764')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b764', ferry, t, rows)
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
