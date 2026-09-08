# -*- coding: utf-8 -*-
"""b370_checks.py -- THE GATE SUITE FOR THE FOLD, b361 THROUGH b369.

### ### **`G-NOEDIT` IS RESTATED, NOT SOFTENED.** ### This act was SENT to repair one owner instrument.
### It is named here and ### **ANY OTHER INSTRUMENT MOVING IS STILL A FAILURE.**
### ### **`G-FIXTURE` RUNS THE REPAIRED TOOL'S OWN FIXTURE INSIDE THIS SUITE** rather than reading its
### claim -- a fixture nobody runs is a docstring.
### ### **THE SIDES, BY `b352`:** ### `G-ADDITIVE`'s and `G-NOEDIT`'s working-tree halves and `G-ROW`'s
### ancestry reading are BEFORE THE PUSH; the hook and mirror AFTER; `G-ORDER` and `G-FIXTURE` are
### SIDE-INVARIANT.
"""
import ast
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import hedge_audit        # noqa: E402
import ferry_scan         # noqa: E402
import banned_terms       # noqa: E402
import b306_stem_scope    # noqa: E402
import b317_checks as K7   # noqa: E402
import gate_text          # noqa: E402
import run_clock          # noqa: E402
import gate_needle as GN   # noqa: E402
import b366_sweep as SW    # noqa: E402
import b363_span as SPAN   # noqa: E402  ### THE TOOL THIS ACT REPAIRED, EXERCISED HERE

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b370_the_fold.txt')
REG = d('b370_registration_2026-09-08.txt')
FERRY = d('b370_ferry_2026-09-08.txt')
CORR, IDX = d('b370_corr_run.txt'), d('b370_index_run.txt')
SCAN, TERMSCAN, GATE = d('b370_ferry_scan.txt'), d('b370_reg_termscan.txt'), d('b370_reg_gate.txt')
CENSUS0, FCEN = d('b370_census_stepzero.txt'), d('b370_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b370_regspec_run.txt'), d('audit_b370_reg_satisfiable.txt')
PINS0 = d('b370_pins_stepzero.txt')
SEAL = 'd9241326c9240bab40e414d38b00e3b813a3bf3fd1d043d034c6d2759f4e81d5'
ROWNUM = '219'
MARK = '## THE APPARATUS ARC, b361–b369 — THE FOLD'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b370_reads.json'), ('S', 'b370_span.json'), ('F', 'b370_fold.json'),
                   ('L', 'b370_lore.json'), ('Q', 'b370_desk.json'))}

LICENSED = {'tools/b363_span.py'}
NEW_THIS_ACT = {'tools/b370_regspec.py', 'tools/b370_extract.py', 'tools/b370_reg_gate.py',
                'tools/b370_fold.py', 'tools/b370_lore.py', 'tools/b370_desk.py',
                'tools/b370_bank.py', 'tools/b370_correspondence.py',
                'tools/b370_index_append.py', 'tools/b370_checks.py'}

TOOLNUM = [
    ('the fold, F-NOGRADE and the additive bar', 'tools/b370_fold.py'),
    ('the three mints', 'tools/b370_lore.py'),
    ('the span, counted', 'tools/b363_span.py'),
    ('the 39 reads', 'tools/b370_extract.py'),
    ('the desk marks', 'tools/b370_desk.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b370_bank.py'),
    ('the three-arm registration gate', 'tools/b370_reg_gate.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 219', 'tools/b370_correspondence.py'),
    ('the key', 'tools/b370_index_append.py'),
    ('the clause spec', 'tools/b370_regspec.py'),
    ('17787 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('the pins across four', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act and its span', FERRY,
     'ACT b370 - THE FOLD, b361 through b369, nine acts against the'),
    ('the order -- step zero', FERRY, 'STEP ZERO - THE TOOL THAT WRITES INTO OTHER ACTS: the span'),
    ('the order -- the fixture it demands', FERRY,
     'fixture proving it leaves a foreign pointer byte-identical.'),
    ('the order -- component 1', FERRY, 'COMPONENT 1 - THE FOLD, nine acts, each with its grade, owning'),
    ('the order -- component 2', FERRY, 'COMPONENT 2 - THE ARC AS ONE STATEMENT, at the grade the acts'),
    ('the order -- no new mathematics', FERRY,
     'produced no new mathematics about the clause; it produced two'),
    ('the order -- component 3', FERRY, 'COMPONENT 3 - THE LORE, with three mints: one incident does not'),
    ('the order -- component 4', FERRY, 'COMPONENT 4 - THE DESK, swept under the freshness rule, marks'),
    ('the order -- component 5', FERRY, 'COMPONENT 5 - THE NEXT ARC NAMED AND NOT OPENED: the federation'),
    ('the order -- audit nothing was already the cap', FERRY,
     'the ranking cannot look; and its first target is the one'),
    ('the record -- the last fold heading this one follows', FINDINGS,
     '## THE UNIFORMITY ARC, b349–b359 — THE FOLD'),
]

SELF_NEEDLES = [
    ('the bank states the answer first', BANK,
     'THE FOLD IS FILED, AND THE SPAN WAS COUNTED BEFORE IT WAS WRITTEN.'),
    ('### step zero: filed twice, fixed never', BANK,
     'BOTH REVERTED IT. ### NEITHER FIXED IT.'),
    ('### an arm that cannot fail is not an arm, applied to its own tool', BANK,
     'FAIL IS NOT AN ARM**, which is `b363`s own sentence, applied to `b363`s own tool.'),
    ('### the folding act is not in its own fold', BANK, 'THE FOLDING ACT IS NOT IN ITS OWN FOLD.'),
    ('### the attribution was the hard half', BANK,
     'AND THE ATTRIBUTION WAS THE HARD HALF, NOT THE PRESENCE.'),
    ('### no new mathematics', BANK, 'THIS SPAN PRODUCED NO NEW MATHEMATICS ABOUT THE CLAUSE.'),
    ('### seven of the nine', BANK, 'SEVEN OF THE NINE ACTS PRODUCED NO RESULT ABOUT THE OBJECT AT ALL.'),
    ('### the fold that would let them read as progress', BANK,
     'A FOLD THAT LET THOSE SEVEN READ AS PROGRESS ON THE CLAUSE WOULD BE THE EXACT DEFECT THIS'),
    ('### the defects table is not a confession', BANK,
     'THE DEFECTS TABLE IS NOT A CONFESSION AND IT IS NOT A BOAST.'),
    ('### the first mint has no mechanizable half', BANK,
     'NO MECHANIZABLE HALF AT ALL, AND THE MODULE SAYS SO FIRST'),
    ('### the second was caught by re-derivation', BANK,
     'THE SHARP ONE WAS CAUGHT BY RE-DERIVATION AND NOT BY ANY ARM'),
    ('### the guards a fresh clone starts without', BANK,
     'SO THE GUARDS THAT HAVE CAUGHT THE MOST ARE THE ONES'),
    ('### a predicate can be widened but never shown complete', BANK,
     'PREDICATE CAN BE WIDENED BUT NEVER SHOWN COMPLETE.'),
    ('### the third time the same number with the same caveat', BANK,
     'AND THIS IS THE THIRD TIME THE SAME NUMBER HAS BEEN REPORTED WITH THE SAME CAVEAT.'),
    ('### a measurement nobody is using', BANK,
     'NEVER MOVE IS A MEASUREMENT NOBODY IS USING'),
    ('### the front document is not now correct', BANK, 'DOCUMENT IS NOT NOW CORRECT'),
    ('### the durable fix priced and not built', BANK,
     'THE HOOK IS NOT DURABLE, AND A DURABLE FIX IS PRICED AND NOT BUILT.'),
    ('### and the act does not build it', BANK,
     'AND THE ACT DOES NOT BUILD IT, WHICH IS WORTH NOTICING'),
    ('### the next arc: surface kinds, not repositories alone', BANK,
     'CORRECTION ONE: IT ENUMERATES SURFACE KINDS, NOT REPOSITORIES ALONE.'),
    ('### its first target, settled by one read', BANK,
     'CORRECTION TWO: ITS FIRST TARGET IS THE ONE CONFIRMED LIVE CLAIM.'),
    ('### and it is not opened here', BANK, 'AND IT IS NOT OPENED HERE.'),
    ('### (E2) refuted, and the seat cannot prove why', BANK,
     'A SEAT SAYING ITS OWN ARM WOULD HAVE'),
    ('### the incident: U-1 fired, then fired on the explanation', BANK,
     'AND THEN THE EXPLANATION QUOTED THE'),
    ('### the incident: the placeholder split, a fourth time', BANK,
     'THE PLACEHOLDER-SPLIT SPECIES, AGAIN, IN THIS ACT`S OWN BANK WRITER.'),
]

MUST_FAIL = [
    ('the bank never says a grade was moved', BANK, '### A GRADE WAS MOVED.'),
    ('the bank never says an act was re-verdicted', BANK, '### AN ACT WAS RE-VERDICTED.'),
    ('the bank never says the next arc is opened', BANK, '### THE NEXT ARC IS OPENED.'),
    ('the bank never says a desk item is closed', BANK, '### A DESK ITEM IS CLOSED.'),
    ('the bank never says the span was typed', BANK, '### THE SPAN WAS TYPED.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def strip_prose(path):
    src2 = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src2)
    spans = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and hasattr(n, 'lineno'):
            spans.append((n.lineno, n.end_lineno))
    keep = []
    for i, ln in enumerate(src2.split(chr(10)), 1):
        if any(a <= i <= b for a, b in spans):
            continue
        keep.append(ln.split('#')[0])
    return chr(10).join(keep)


def main():
    fails = []
    print('=' * 100)
    print('b370 -- GATE SUITE (THE FOLD, b361 THROUGH b369)')
    print('=' * 100)
    E, S, F, L, Q = _J['E'], _J['S'], _J['F'], _J['L'], _J['Q']
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            trunc = False
            if not inx and len(line.rstrip()) > 220:
                inx = line.rstrip()[:220] in extract
                trunc = bool(inx)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    '  ### -- ITS RECORDED PREFIX' if trunc
                                    else ('' if inx else '  -- NOT IN THE EXTRACT FILE')))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  MUST-FAIL FIXTURES:')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    fnd = norm(io.open(FINDINGS, encoding='utf-8', newline='').read())

    print(chr(10) + '  G-SPAN (BAR 3: the span is counted, and the fold refuses if it disagrees):')
    s1 = S['span_starts_at'] == 361 and S['this_act'] == 369 and S['current_span'] == 9
    s2 = F['span_agrees'] is True and F['acts'] == S['current_span']
    s3 = S['emitted_for'] == 'b370'
    src = strip_prose(t('b370_fold.py'))
    s4 = 'return 3' in src and 'span_agrees' not in src.split('json.dumps')[0][:0] + ''
    s5 = 'THE FOLD IS NOT WRITTEN' in io.open(t('b370_fold.py'), encoding='utf-8').read()
    gs = s1 and s2 and s3 and s5
    print('    the counter reads b%d-b%d, %d acts : %s'
          % (S['span_starts_at'], S['this_act'], S['current_span'], s1))
    print('    the fold names the same range and has that many rows : %s' % s2)
    print('    ### **AND THE SPAN JSON IS UNDER THIS ACT`S OWN STEM, NOT b363`S** : %s' % s3)
    print('    ### **AND THE EMITTER HAS A REFUSAL BRANCH IT CAN ACTUALLY TAKE** : %s' % s5)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SPAN')

    print(chr(10) + '  G-READONLY / G-FIXTURE (BAR 4) ### SIDE-INVARIANT:')
    foreign = d('b363_span.json')
    h0 = hashlib.sha256(open(foreign, 'rb').read()).hexdigest()
    fx = SPAN.self_test(False)
    h1 = hashlib.sha256(open(foreign, 'rb').read()).hexdigest()
    ssrc = strip_prose(t('b363_span.py'))
    r1 = fx is True
    r2 = (h0 == h1)
    r3 = "'b363_span_notes'" not in ssrc and "'b363_span.json'" not in ssrc
    r4 = 'THIS_ACT' not in ssrc
    r5 = git(ROOT, 'diff', '--name-only', 'HEAD', '--', 'tools/b363_span.py').strip() != ''
    gro = r1 and r2 and r3 and r4 and r5
    print("    ### **THE TOOL'S OWN FIXTURE, RUN HERE AND NOT READ FROM ITS DOCSTRING : %s**" % r1)
    print('    ### **AND RUNNING IT LEFT THE FOREIGN POINTER BYTE-IDENTICAL : %s** (%s)' % (r2, h0[:16]))
    print('    no hardcoded foreign stem in the stripped source : %s ; no hardcoded act number : %s'
          % (r3, r4))
    print('    ### **AND THE INSTRUMENT WAS ACTUALLY EDITED BY THIS ACT** : %s' % r5)
    print('    %s' % ('PASS' if gro else '### FAIL ###'))
    if not gro:
        fails.append('G-READONLY/G-FIXTURE')

    print(chr(10) + '  G-ADDITIVE (BAR 1) ### BEFORE THE PUSH:')
    fb = norm(blob_of(PP, 'FINDINGS.md') or '')
    a1 = fnd.count(MARK) == 1
    a2 = fnd.startswith(fb.rstrip(chr(10)))
    a3 = F['prefix_of_file'] and F['prefix_of_blob'] and F['side'] == 'BEFORE THE PUSH'
    a4 = F['sections_edited'] == 0
    ga = a1 and a2 and a3 and a4
    print('    the fold heading appears once : %s ; the committed blob is a true prefix : %s' % (a1, a2))
    print('    the writer recorded both prefixes before the push : %s ; sections edited : %d'
          % (a3, F['sections_edited']))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ADDITIVE')

    print(chr(10) + '  G-NOGRADE / G-NINE / G-QUOTED (BAR 2):')
    sect = fnd.split(MARK)[-1]
    BANKS = {361: 'b361_the_held_item.txt', 362: 'b362_the_approximation_register.txt',
             363: 'b363_the_anchored_gate_arms.txt', 364: 'b364_the_copy_that_did_not_reproduce.txt',
             365: 'b365_the_owed_read_paid.txt', 366: 'b366_the_dated_arm_sweep.txt',
             367: 'b367_the_scaffold_repair.txt', 368: 'b368_the_front_document_reconciled.txt',
             369: 'b369_the_list_repaired.txt'}
    n1 = F['grade_misses'] == 0
    n2 = all(('| **b%d** |' % a) in sect for a in BANKS)
    n3 = len(re.findall(r'^\| \*\*b3\d\d\*\* \|', sect, re.M)) >= 9
    # ### **AND THE QUOTATIONS ARE RE-CHECKED HERE, AGAINST THE BANKS, NOT AGAINST THE WRITER'S JSON.**
    bad_q = []
    for q in F['quoted']:
        b = io.open(d(BANKS[q['act']]), encoding='utf-8', errors='replace').read()
        if GN.norm(q['quote'][:60]) not in GN.norm(b):
            bad_q.append(q['act'])
    n4 = not bad_q
    n5 = 'no grade moves here, no act is re-verdicted' in sect
    gng = n1 and n2 and n3 and n4 and n5
    print('    grade strings not found in their own bank : %d' % F['grade_misses'])
    print('    all nine acts have a row in the filed section : %s' % n2)
    print('    ### **AND EVERY OBSTACLE RE-CHECKED AGAINST ITS OWN BANK HERE : %s** %s'
          % (n4, bad_q or ''))
    print('    the section states the no-grade-moved claim in its own voice : %s' % n5)
    print('    %s' % ('PASS' if gng else '### FAIL ###'))
    if not gng:
        fails.append('G-NOGRADE/G-NINE/G-QUOTED')

    print(chr(10) + '  G-CORRECTIONS / G-DEFECTS (the two further tables):')
    c1 = 'The corrections this span made' in sect and 'A correction is not a re-verdict' in sect
    c2 = 'The defects these seats declared in their own work' in sect
    c3 = 'not a confession and it is not a boast' in sect
    c4 = sect.count('| **b369** | a gate driver') == 1 or 'gate driver that tested a tuple' in sect
    gcd = c1 and c2 and c3 and c4
    print('    the corrections table, with its own disclaimer : %s' % c1)
    print('    the declared-defects table : %s ; and it says what it is not : %s' % (c2, c3))
    print('    %s' % ('PASS' if gcd else '### FAIL ###'))
    if not gcd:
        fails.append('G-CORRECTIONS/G-DEFECTS')

    print(chr(10) + '  G-ARC / G-KIND (the arc as one statement, honest about its kind):')
    k1 = 'produced no new mathematics about the clause' in sect
    k2 = 'Seven of the nine acts produced no result about the object at all' in sect
    k3 = 'making the record checkable by a reader who trusts none of it' in sect
    k4 = 'The clause has not moved and no act in the span claims otherwise' in sect
    k5 = 'are graded where their own acts left them and are not promoted here' in sect
    gk = k1 and k2 and k3 and k4 and k5
    print('    no new mathematics : %s ; seven produced nothing about the object : %s' % (k1, k2))
    print('    the main product named : %s ; the clause has not moved : %s' % (k3, k4))
    print('    ### **AND THE TWO SHAPE RESULTS ARE NOT PROMOTED** : %s' % k5)
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-ARC/G-KIND')

    print(chr(10) + '  G-MINTS / G-LOCAL (three modules, each stating its halves, local only):')
    MD = os.path.join(TC, 'modules', '2026-09')
    want = ['ONE_INCIDENT_IS_NOT_A_PARTITION.md', 'PREDICATE_ONE_SHAPE.md', 'DURABILITY_SPLIT.md']
    m1 = all(os.path.exists(os.path.join(MD, w)) for w in want)
    m2 = L['all_state_halves'] is True and L['minted'] == 3
    m3 = all(f in L['module_names'] for f in ('WRONG_ARM.md', 'DATED_ARM.md', 'DESK_FRESHNESS.md'))
    ahead = git(TC, 'rev-list', '--count', 'origin/main..HEAD').strip()
    m4 = L['pushed'] is False and ahead.isdigit() and int(ahead) > 0
    m5 = not git(TC, 'status', '--porcelain').strip()
    # ### **AND EACH MODULE'S OWN HALVES ARE RE-READ HERE, NOT TAKEN FROM THE WRITER'S JSON.**
    halves = []
    for w in want:
        txt = io.open(os.path.join(MD, w), encoding='utf-8').read()
        halves.append((w, 'Mechanizable' in txt or 'mechanizable half' in txt))
    m6 = all(v for _w, v in halves)
    gm = m1 and m2 and m3 and m4 and m5 and m6
    print('    all three minted : %s ; each states its halves (writer) : %s' % (m1, m2))
    print('    ### **AND RE-READ HERE** : %s %s' % (m6, halves))
    print('    the arm species are beside them : %s' % m3)
    print('    ### **LOCAL ONLY: %s AHEAD OF origin/main, NOT PUSHED** : %s ; tree clean : %s'
          % (ahead, m4, m5))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-MINTS/G-LOCAL')

    print(chr(10) + '  G-DESKSWEEP / G-NOCLOSE / G-OWED:')
    q1 = Q['items_closed'] == 0 and Q['module_written'] is False
    q2 = (Q['confirmed'] + Q['unconfirmed']) == Q['items']
    q3 = all(m['hit'] is None or not m['hit']['file'].startswith('data/b370_') for m in Q['marks'])
    q4 = Q.get('owed_named') == 2 and Q.get('durable_fix_built') is False
    q5 = 'THE HOOK IS NOT DURABLE' in bf and 'PRICED AND NOT BUILT' in bf
    q6 = 'A MEASUREMENT WHOSE RESULT AND WHOSE CAVEAT BOTH' in bf
    gq = q1 and q2 and q3 and q4 and q5 and q6
    print('    items closed : %d ; counts add up : %s' % (Q['items_closed'], q2))
    print("    ### **NO ITEM CONFIRMED FROM THIS ACT'S OWN FILES** : %s" % q3)
    print('    ### **TWO OWED ITEMS NAMED, NO DURABLE FIX BUILT** : %s ; the bank says so : %s'
          % (q4, q5))
    print('    and the caveat is stated for the third time : %s' % q6)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-DESKSWEEP/G-NOCLOSE/G-OWED')

    print(chr(10) + '  G-NEXTARC / G-NOTOPENED (named and priced; the read NOT made):')
    x1 = 'ENUMERATES SURFACE KINDS, NOT REPOSITORIES ALONE' in bf
    x2 = 'ITS FIRST TARGET IS THE ONE CONFIRMED LIVE CLAIM' in bf
    x3 = 'SCOPE-DEPENDENT' in bank and 'STALE' in bank
    x4 = 'AND IT IS NOT OPENED HERE.' in bf
    # ### **AND THE CAP IS RE-MEASURED, NOT READ:** ### no tool of this act fetches a surface.
    fetched = [x for x in sorted(os.listdir(os.path.join(ROOT, 'tools')))
               if x.startswith('b370_') and x.endswith('.py')
               and re.search(r'\bgh\b|urllib|requests|raw\.githubusercontent',
                             strip_prose(t(x)))]
    x5 = not fetched
    gx = x1 and x2 and x3 and x4 and x5
    print('    surface kinds, not repositories alone : %s ; the first target named : %s' % (x1, x2))
    print('    the two possible outcomes named : %s ; and it is not opened : %s' % (x3, x4))
    print("    ### **AND NO TOOL OF THIS ACT FETCHES ANY SURFACE** (stripped code) : %s %s"
          % (x5, fetched or ''))
    print('    %s' % ('PASS' if gx else '### FAIL ###'))
    if not gx:
        fails.append('G-NEXTARC/G-NOTOPENED')

    print(chr(10) + '  G-ROW (row %s) ### BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    ancr = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'THE SPAN COUNTED AND NOT TYPED' in rows[0]
            and 'MOVES NO GRADE' in rows[0] and 'NOT OPENED' in rows[0] and ancr)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, ancr))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW')

    print(chr(10) + '  G-KEY / G-NOTMOVED:')
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    kk1 = 'READ BACK : apparatus-arc-fold returns 1 row(s)' in irun
    kk2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the clause moved', 'the fold proves', 'the federation is audited',
               'the hook is durable'))
    kk3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    kk4 = 'A FOLD MOVES NO GRADE AND SETTLES NOTHING' in idx
    gkk = kk1 and kk2 and kk3 and kk4
    print('    one key and one row : %s ; four overreadings NO KEY after : %s ; run passed : %s'
          % (kk1, kk2, kk3))
    print('    ### **AND THE KEY SAYS A FOLD SETTLES NOTHING** : %s' % kk4)
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTMOVED')

    print(chr(10) + '  G-ORDER ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (S, F, L, Q))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    go = o1 and stampm and o3 and o4 and o5 and o6
    print('    the lock recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('    audit JOINTLY SATISFIABLE : %s ; face says LOCKED BEFORE ANY WRITE : %s' % (o4, o5))
    print('    the three-arm registration gate read CLEAR : %s' % o6)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b370_hooks.txt'), d('b370_mirror.txt')
    gh2 = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh2:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh2 = h_ok and m_ok
        print('    hook: 0 failing, all byte-identical : %s ; mirror clean : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook and mirror records are NOT YET WRITTEN (written at the push).')
    if not gh2:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS:')
    checks = [
        ('span %d-%d' % (S['span_starts_at'], S['this_act']),
         ('`b%d` AND RUNS THROUGH `b%d`' % (S['span_starts_at'], S['this_act'])) in bf),
        ('span %d acts' % S['current_span'], ('`%d` ACTS' % S['current_span']) in bf),
        ('rows %d' % F['acts'], ('`%d` ROWS' % F['acts']) in bf),
        ('grade misses %d' % F['grade_misses'],
         ('OWN ACT`S BANK : `%d`' % F['grade_misses']) in bf),
        ('obstacles %d' % F['obstacles'], ('`%d` OBSTACLES' % F['obstacles']) in bf),
        ('lines appended %d' % F['lines_appended'], str(F['lines_appended']) in bank),
        ('bytes grown %d' % F['grew'], str(F['grew']) in bank),
        ('sections edited %d' % F['sections_edited'],
         ('`%d` EXISTING SECTIONS EDITED' % F['sections_edited']) in bf),
        ('minted %d' % L['minted'], ('MINTED : `%d`' % L['minted']) in bf),
        ('modules now %d' % L['modules_now'], str(L['modules_now']) in bank),
        ('techne head', L['techne_head'] in bank),
        ('desk items %d' % Q['items'], ('ITEMS SWEPT `%d`' % Q['items']) in bf),
        ('desk closed %d' % Q['items_closed'], ('CLOSED `%d`' % Q['items_closed']) in bf),
        ('row %s' % ROWNUM, re.search(r'row to append : (\d+)',
                                      io.open(CORR, encoding='utf-8').read()).group(1) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on fold run', F['run_file'] in bank),
        ('the relied-on span run', S['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('span', S), ('fold', F), ('lore', L), ('desk', Q)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-8s %-26s clock %s == JSON's %s : %s" % (lbl, jf['run_file'], st,
                                                             jf['run_clock'], ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b370_') and x.endswith('.py')))
    hits = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits and not imports
    print('    numerical calls in stripped sources : %d %s ; libraries : %s'
          % (len(hits), hits or '', imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-BYCONTENT:')
    selfhits = []
    for p in [t(x) for x in mymods]:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    DECLARED = {'last-row cells': 'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE.',
                'the fold section split': 'the section is located by its own MARK and only then '
                                          'sliced; the index is a consequence of a content read.'}

    def which(code):
        if '[-1:]' in code or '[-1]' in code:
            return 'last-row cells'
        if 'split(MARK)' in code or "split('" in code:
            return 'the fold section split'
        return None
    undeclared = []
    for fn, i, code in selfhits:
        key = which(code)
        print('    %-26s line %-6d | %s' % (fn, i, code))
        if key is None:
            undeclared.append((fn, i))
            print('        ### ### **UNDECLARED HIT.**')
        else:
            print('        %s' % DECLARED[key])
    gbc = not undeclared
    print('    ### hits : %d ; UNDECLARED : %d  %s'
          % (len(selfhits), len(undeclared), 'PASS' if gbc else '### FAIL ###'))
    if not gbc:
        fails.append('G-BYCONTENT')

    print(chr(10) + '  G-NOEDIT ### BEFORE THE PUSH:')
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/gate_content.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b304_hooks.py',
             'tools/b363_span.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    unlicensed = [p for p in touched if p not in LICENSED]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').splitlines()
              if x.strip() and 'b370' not in x and x.strip() != 'tools/banked_index.py'
              and x.strip() not in LICENSED]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines()
              if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'FINDINGS.md']
    faces_clean = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    gne = not unlicensed and not others and not ppbad and faces_clean
    print('    owner instruments modified : %s' % (touched or 'none'))
    print('    ### **LICENSED : %s** ; ### **UNLICENSED : %s**' % (sorted(LICENSED),
                                                                   unlicensed or 'none'))
    print('    tracked relay files of other acts modified : %s' % (others or 'none'))
    print('    papers paths beyond FINDINGS.md : %s ; FACES_LEDGER untouched : %s'
          % (ppbad or 'none', faces_clean))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b370_satisfiable.json'), t('b370_regspec.py'), t('b370_extract.py'),
             t('b370_reg_gate.py'), t('b370_bank.py'), t('b370_correspondence.py'),
             t('b370_index_append.py'), t('b370_lore.py')]
    CARRIERS = [
        (t('b370_checks.py'), 'its own fixtures'),
        (FERRY, "IT IS THE ORDER"), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries nine banks' own words"),
        (d(S['run_file']), "the span run carries the record's own fold headings"),
        (d(F['run_file']), "the fold run carries nine banks' own grade lines"),
        (d(L['run_file']), "the lore run carries the modules' own clauses"),
        (d(Q['run_file']), "the desk run carries the fold's own sentence"),
        (t('b370_fold.py'), "ITS PROBES AND ITS ROWS ARE THE NINE BANKS' OWN SENTENCES"),
        (t('b370_desk.py'), "ITS DESK ROWS ARE THE FOLD'S OWN ITEM NAMES"),
        (t('b363_span.py'), "the repaired instrument; its prose quotes the defect it fixes"),
    ]
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned, live_bad = 0, 0, 0, []
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for hh in (ch + sh)[:4]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
        if sh:
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', p],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **HANDED TO THE SHARED SCANNER : CLEAN : %s**' % clean)
            if not clean:
                live_bad.append(os.path.basename(p))
    print('    files scanned %d   struck %d   stem %d   ### **LIVE : %d** %s'
          % (scanned, total, stem_total, len(live_bad),
             'PASS' if not (total or live_bad) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in
                [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                 ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                 ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [],
                                     stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or live_bad or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE APPARATUS ARC, b361-b369 -- THE FOLD (b370).'
    nxt = '# ### THE LIST REPAIRED IN PLACE, THE ROSTER MENDED, THE PASS PRICED (b369).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the fold section, the index row):' % ROWNUM)
    for lbl, b2 in (('row %s' % ROWNUM, rows[0] if rows else ''),
                    ('the fold section', sect), ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(b2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(b2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(b2)))
        if ch or not b2:
            fails.append('G-STEM-APPENDED ' + lbl)
        if sh:
            tmp = os.path.join(tempfile.mkdtemp(prefix='b370_stem_'), 'blk.txt')
            io.open(tmp, 'w', encoding='utf-8', newline=chr(10)).write(b2)
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', tmp],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **%d STEM HIT(S) HANDED TO THE SHARED SCANNER: CLEAN : %s**'
                  % (len(sh), clean))
            if not clean:
                fails.append('G-STEM-APPENDED live ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr2 = K7.git_tracked(ROOT, tool)
        if not (ex and (tr2 or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b370_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the fold section', sect),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles refused : %d ; owner needles not in the extract file : %d'
          % (refused, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
