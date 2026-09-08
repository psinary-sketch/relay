# -*- coding: utf-8 -*-
"""b362_checks.py -- THE GATE SUITE FOR THE APPROXIMATION REGISTER, READ UNDER A CAP.

### ### **THIS SUITE USES `gate_text.flat` AND DEFINES NO FLATTENER OF ITS OWN**, and every `G-NO*`-shaped
### arm reads STRIPPED CODE or a marked region rather than raw prose -- `b348`'s rule.
### ### **THE ARMS (locked registration section (H)):** ### `G-QUOTE`, `G-PIN`, `G-HINT`, `G-STRUCTURAL`,
### `G-CIRCULAR`, `G-RHYME`, `G-PRICE`, `G-ROW`, `G-KEY` with `G-NOTADOPTED`, `G-NOEDIT`, `G-ORDER`,
### `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, `G-NOCOMPUTE`, the struck-clause and stem sweeps, `G-SHARED`, the
### hedge audit, the must-fail fixtures. ### Re-run after the push.
### ### **THE SIDES, DECLARED BY `b352`'s RULE:** ### `G-NOEDIT`'s working-tree half and `G-ROW`'s ancestry
### reading are read BEFORE THE PUSH; `G-HOOK` and `G-MIRROR` AFTER THE PUSH; `G-ORDER` SIDE-INVARIANT.
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
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import gate_text         # noqa: E402
import run_clock         # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b362_the_approximation_register.txt')
REG = d('b362_registration_2026-09-07.txt')
FERRY = d('b361_ferry_2026-09-07.txt')
S1 = d('b362_source_baezduarte0202141.txt')
S2 = d('b362_source_baezduarte_abs0202141.txt')
S3 = d('b362_source_burnol0103058.txt')
S5 = d('b362_source_baezduarte0205003.txt')
B321 = d('b321_the_window_opened.txt')
REG358 = d('b358_registration_2026-09-07.txt')
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
CORR, IDX = d('b362_corr_run.txt'), d('b362_index_run.txt')
SCAN, TERMSCAN, GATE = d('b362_ferry_scan.txt'), d('b362_reg_termscan.txt'), d('b362_reg_gate.txt')
CENSUS, FCEN = d('b361_census_stepzero.txt'), d('b361_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b362_regspec_run.txt'), d('audit_b362_reg_satisfiable.txt')
PINS = d('b361_pins_stepzero.txt')
SEAL = '3622fa87ce23fa4b6ead59deac84d86dcf7c61504f8ed96758a92e1018f9173d'
ROWNUM = '211'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('R', 'b362_read.json'), ('E', 'b362_reads.json'), ('F', 'b362_faces_row.json'),
                   ('L', 'b362_locate.json'))}

NEW_THIS_ACT = {'tools/b362_regspec.py', 'tools/b362_locate.py', 'tools/b362_extract.py',
                'tools/b362_read.py', 'tools/b362_faces_row.py', 'tools/b362_correspondence.py',
                'tools/b362_index_append.py', 'tools/b362_checks.py'}

TOOLNUM = [
    ('the five branches, the circularity table and the verdict', 'tools/b362_read.py'),
    ('the 37 reads and the 7 differing anchors', 'tools/b362_extract.py'),
    ('the five fetches and every sha256', 'tools/b362_locate.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the N1 row', 'tools/b362_faces_row.py'),
    ('the ledger writer it imports', 'tools/b327_faces_row.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 211', 'tools/b362_correspondence.py'),
    ('the key', 'tools/b362_index_append.py'),
    ('51 clauses', 'tools/b362_regspec.py'),
    ('18068 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNED = [BANK, REG, FERRY, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, GATE, TERMSCAN,
         d('b362_satisfiable.json'), d(_J['E']['run_file']), d(_J['R']['run_file']),
         d(_J['F']['run_file']), d(_J['L']['run_file']),
         t('b362_regspec.py'), t('b362_locate.py'), t('b362_extract.py'), t('b362_read.py'),
         t('b362_faces_row.py'), t('b362_correspondence.py'), t('b362_index_append.py')]

CARRIERS = [
    (t('b362_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (d(_J['E']['run_file']), "the extract file carries the sources' own words"),
    (S1, 'A PINNED SOURCE -- its words are its own'),
    (S3, 'A PINNED SOURCE -- its words are its own'),
    (S5, 'A PINNED SOURCE -- its words are its own'),
]

OWNER_NEEDLES = [
    ('the order -- leg 2', FERRY, 'LEG 2 (b362) \u2014 THE APPROXIMATION REGISTER, READ UNDER A CAP.'),
    ('the order -- the CAP', FERRY, 'CAP, quoted in the registration: ONE act; reads and a pricing'),
    ('the order -- the hint is recall and NOT a file', FERRY,
     'from recall and NOT from any file, that the hypothesis has a'),
    ('the order -- the hint itself', FERRY, 'Nyman\u2013Beurling criterion, that a fixed function lies in the'),
    ('the order -- the shortfall comparison it demands', FERRY,
     'the shortfall the window act found in the positivity register,'),
    ('the order -- the floor-versus-edge question', FERRY,
     'two fresh incidents of exactly this \u2014 how a floor would be told'),
    ('S3 -- the classical criterion', S3,
     'Theorem 1.1 (Nyman [14], Beurling [3]) The Riemann Hypothesis holds if and only if'),
    ('S3 -- the family and its parameter range', S3,
     'of K consisting of the \ufb01nite linear combinations of the function s t'),
    ('S3 -- the lower bound, attributed', S3,
     'Theorem 1.2 (B\u00b4 aez-Duarte, Balazard, Landreau and Saias [2]) Let us write D(\u03bb) for'),
    ('S3 -- and what it is if the hypothesis FAILS', S3,
     'If the Riemann Hypothesis fails this result is true but trivi al as the left-hand side then take'),
    ('S3 -- the numerical explorations, NAMED and not fetched', S3,
     '5.5 to give the exact order of decrease of the quantity D(\u03bb) and the numerical explorations'),
    ('S1 -- the variant', S1, 'Theorem 1.1. The Riemann hypothesis is equivalent to the statement that'),
    ('S1 -- the family restricted to the naturals', S1,
     'The much smaller subspace Bnat of natural Beurling functions is generated'),
    ('S1 -- AND THE CAVEAT: the original formulation is a different space', S1,
     'modi\ufb01ed form [4] (the original formulation is related to L2(0, 1)), that the'),
    ('S5 -- the upper bound, UNDER the hypothesis', S5,
     'second version di\ufb00ers from the \ufb01rst in showing that under the Riemann'),
    ('b321 -- the shortfall the window act found', B321,
     '### ### OWN DISTANCE FROM THE ANSWER**, and reporting this control as having settled the exponent'),
    ("b358 -- circularity question (i), carried by reference", REG358,
     "**(i)** Does the statement's own hypothesis list contain the hypothesis under study, by name?"),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK,
     '### ### ### **LOCATED BUT NOT WORTH OPENING** -- at the reach the record can afford, and the reason is'),
    ('### the hint, confirmed with one correction', BANK,
     '### ### **(i) THE HINT IS CONFIRMED, WITH ONE CORRECTION.**'),
    ('### the finite instance is unconditional', BANK,
     '### ### ### **(ii) A FINITE INSTANCE IN THIS REGISTER IS AN UNCONDITIONAL UPPER BOUND**, and the reason is'),
    ('### and it does NOT carry the window act\u2019s shortfall', BANK,
     '### ### ### **SO THIS REGISTER DOES NOT CARRY THE SHORTFALL THE WINDOW ACT FOUND IN THE POSITIVITY'),
    ('### and the shortfall it carries instead', BANK,
     '### ### ### **AND THE SHORTFALL IT CARRIES INSTEAD, SAID EXACTLY: THE CRITERION IS A STATEMENT ABOUT A'),
    ('### the asymmetry, stated once', BANK,
     "### ### ### **(iii) AND THE REGISTER'S ASYMMETRY, WHICH IS THE FINDING: WHAT IS UNCONDITIONAL HERE IS THE"),
    ('### the hint was a search string and never a source', BANK,
     "### ### **AND THE ORDER'S OWN RULE OVER IT, OBEYED:**"),
    ('### no bridge typed, in either direction', BANK,
     '### ### ### **AND NO BRIDGE IS TYPED, IN EITHER DIRECTION.**'),
    ('### the pricing priced', BANK,
     '### ### ### **AND SO THE PRICING IN ACTS CANNOT BE GIVEN FROM WHAT IS LOCATED, AND THE PRICING IS PRICED'),
    ('### the welcome verdict shown unreachable', BANK,
     '### ### **(NO USABLE STATEMENT LOCATED) -- UNREACHABLE.**'),
    ('### the heredoc species, declared', BANK,
     '### ### **(E1) THE HEREDOC-BACKSLASH SPECIES BIT FOR THE THIRD TIME IN THIS SESSION, AND THIS TIME IT'),
    ('### the term scan firing on the seat\u2019s own prose, declared', BANK,
     "### ### **(E4) THE TERM SCAN FIRED ON THIS ACT'S OWN BANK, AND THE SEAT'S SENTENCE WAS REWRITTEN.**"),
    ('### the shadow', BANK, '### ### **EXPECTED: EITHER A DOOR OR A WALL.**'),
    ('### and what a famous equivalence is', BANK,
     '### ### **A FAMOUS EQUIVALENCE IS STILL AN EQUIVALENCE.**'),
]

MUST_FAIL = [
    ('the bank never says the register is adopted', BANK, '### THE REGISTER IS ADOPTED.'),
    ('the bank never says a face is promoted', BANK, '### A FACE IS PROMOTED.'),
    ('the bank never says the distance is evaluated', BANK, '### THE DISTANCE IS EVALUATED.'),
    ('the bank never says the hint is the source', BANK, '### THE HINT IS THE SOURCE.'),
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
    print('b362 -- GATE SUITE (THE HELD ITEM, DECIDED)')
    print('=' * 100)
    extract = io.open(d(_J['E']['run_file']), encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE RELIED-ON EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    R, E, F = _J['R'], _J['E'], _J['F']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    faces = io.open(FACES, encoding='utf-8').read()
    read = io.open(d(R['run_file']), encoding='utf-8', errors='replace').read()

    print(chr(10) + '  G-QUOTE (the extract located every read; no statement quoted from a hint):')
    q1 = E['without_anchor'] == 0 and E['reads'] > 0
    q2 = '### WITHOUT AN ANCHOR : 0' in extract
    q3 = 'A HINT IS SOMETHING TO SEARCH ON AND NEVER SOMETHING TO CITE' in gate_text.flat(reg)
    gq = q1 and q2 and q3
    print('    %d of %d reads located, 0 without an anchor : %s ; the run file says so : %s'
          % (E['reads'] - E['without_anchor'], E['reads'], q1, q2))
    print('    and the LOCKED registration fixed the rule over the hint : %s' % q3)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTE')

    print(chr(10) + '  G-PIN (every source fetched and hashed; the rendering seam named):')
    L = _J['L']
    p1 = L['attempted'] == L['fetched'] and L['fetched'] > 0
    p2 = all(s2.get('sha256') for s2 in L['sources'])
    p3 = all(s2.get('text_sha256') for s2 in L['sources'])
    p4 = 'A HASH ON A PDF DOES NOT CERTIFY' in gate_text.flat(reg)
    p5 = 'A HASH FIXES THE BYTES' in io.open(d(L['run_file']), encoding='utf-8', errors='replace').read()
    gp = p1 and p2 and p3 and p4 and p5
    print('    %d attempted, %d fetched : %s ; every source hashed : %s ; every rendering hashed : %s'
          % (L['attempted'], L['fetched'], p1, p2, p3))
    print('    the seam named on the locked face : %s ; and in the fetch record : %s' % (p4, p5))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PIN')

    print(chr(10) + '  G-HINT (the hint reported CONFIRMED / CORRECTED / NOT LOCATED, and quoted first):')
    h1 = R['hint_status'] in ('CONFIRMED', 'CORRECTED', 'NOT LOCATED', 'CONFIRMED, WITH ONE CORRECTION')
    h2 = 'THE HINT: %s' % R['hint_status'] in read
    h3 = 'THE CORRECTION, QUOTED AND NOT PARAPHRASED' in read
    h4 = 'the original formulation is related to L2(0, 1)' in bank
    gh2 = h1 and h2 and h3 and h4
    print('    the status is one of the three fixed forms : %s (%r)' % (h1, R['hint_status']))
    print('    the reading says so : %s ; the correction is quoted : %s ; and it is in the bank : %s'
          % (h2, h3, h4))
    print('    %s' % ('PASS' if gh2 else '### FAIL ###'))
    if not gh2:
        fails.append('G-HINT')

    print(chr(10) + '  G-STRUCTURAL (the finite instance decided; BOTH halves of the shortfall comparison):')
    t1 = R['finite_instance_unconditional'] is True
    t2 = R['carries_window_shortfall'] is False
    t3 = 'DOES NOT CARRY THAT SHORTFALL' in read
    t4 = 'AND THE SHORTFALL IT CARRIES INSTEAD' in read and R['shortfall_carried'].strip() != ''
    t5 = 'A REGISTER WITHOUT THE SHORTFALL YOU KNOW IS NOT A REGISTER WITHOUT A SHORTFALL' in read
    gt = t1 and t2 and t3 and t4 and t5
    print('    unconditional : %s ; does not carry the window shortfall : %s' % (t1, t2))
    print('    the reading says so : %s ; and says WHICH it carries instead : %s' % (t3, t4))
    print('    and refuses the half-report : %s' % t5)
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-STRUCTURAL')

    print(chr(10) + "  G-CIRCULAR (b358's three questions run; conditional and unconditional KEPT APART):")
    c1 = len(R['circularity']) == 3
    c2 = any('CIRCULAR AT (i)' in x['verdict'] for x in R['circularity'])
    c3 = sum(1 for x in R['circularity'] if x['verdict'] == 'NOT CIRCULAR') == 2
    c4 = 'If the Riemann Hypothesis fails this result is true but trivi al' in read
    c5 = 'under the Riemann' in read and 'MARKED AT FULL PROMINENCE' in read
    gc2 = c1 and c2 and c3 and c4 and c5
    print('    three statements classified : %s ; one CIRCULAR at (i) : %s ; two NOT CIRCULAR : %s'
          % (c1, c2, c3))
    print('    the unconditional side quoted with its own case split : %s' % c4)
    print('    the conditional side marked at full prominence : %s' % c5)
    print('    %s' % ('PASS' if gc2 else '### FAIL ###'))
    if not gc2:
        fails.append('G-CIRCULAR')

    print(chr(10) + '  G-RHYME (the uniformity obstruction placed; NO BRIDGE TYPED; the refusal quoted):')
    y1 = R['uniformity'] == 'REAPPEARS, AS A RATE'
    y2 = R['bridge_typed'] is False
    y3 = 'AND NO BRIDGE IS TYPED' in read
    # ### **THE PHRASE WRAPS ACROSS THE READING'S OWN LINES, SO THE ARM READS THE FLATTENED
    # ### READING.** ### Its first version searched the raw text and fired on a reading that carries
    # ### the refusal across two lines -- the needle-wrapping species, cured with the flattener and
    # ### never with a shorter needle.
    y4 = 'not** compiling the cross-register equivalences' in gate_text.flat(read)
    y5 = ('THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS' in read
          and 'a fourth that rhymes is a' in read)
    gy = y1 and y2 and y3 and y4 and y5
    print('    the obstruction placed as a RATE : %s ; no bridge typed : %s / %s' % (y1, y2, y3))
    print("    the deposit's own refusal quoted : %s ; three are three : %s" % (y4, y5))
    print('    %s' % ('PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-RHYME')

    print(chr(10) + '  G-PRICE (the pricing NOT attempted, and then priced; the control is a control):')
    r1 = 'THE RECORD HOLDS NOTHING IN THIS REGISTER TO REPRODUCE' in read
    r2 = 'AN ABSENCE OF READING, NOT AN ABSENCE OF' in read
    r3 = 'THE ANSWER IS A CONTROL AND NOT A HOPE' in read
    r4 = 'THE PRICING IS' in read and 'PRICED' in read
    r5 = 'THAT IS A GUESS ABOUT NUMERICS AND THIS ACT MEASURED NOTHING' in read
    gpr = r1 and r2 and r3 and r4 and r5
    print('    no control in the record to reproduce : %s ; the named-not-fetched reference : %s' % (r1, r2))
    print('    the floor-versus-edge answer is a control : %s ; the pricing is priced : %s' % (r3, r4))
    print('    and what the act does NOT establish is said : %s' % r5)
    print('    %s' % ('PASS' if gpr else '### FAIL ###'))
    if not gpr:
        fails.append('G-PRICE')

    print(chr(10) + '  G-LEDGER (ONE NEW ROW, through the writer; graded; NOT adopted) ### the ancestry '
          'reading READ BEFORE THE PUSH:')
    fb = blob_of(PP, 'FACES_LEDGER.md')
    F = _J['F']
    l1 = F['status'] in ('WRITTEN', 'DUPLICATE') and F['form'].startswith('NEW ROW')
    l2 = faces.count(chr(124) + ' N1 ' + chr(124)) == 1
    if fb is None:
        l3 = True
    else:
        _old, _new = norm(fb).split(chr(10)), norm(faces).split(chr(10))
        _i = 0
        for _ln in _new:
            if _i < len(_old) and _ln == _old[_i]:
                _i += 1
        l3 = (_i == len(_old))
    l4 = 'IMPORTED (TRUSTED-AT-CITE)' in F['grade'] and 'NAMED-ONLY' in F['grade']
    l5 = R['register_adopted'] is False and R['face_promoted'] is False
    gl = l1 and l2 and l3 and l4 and l5
    print('    written through the writer as a NEW row : %s ; the row appears once : %s' % (l1, l2))
    print('    every line of the ledger blob still present, IN ORDER : %s ; the grade is SPLIT : %s'
          % (l3, l4))
    print('    ### **A NEW ROW IS SPLICED INTO THE TABLE, WHICH SITS ABOVE THE CASCADES, SO THE FILE IS')
    print('    ### NOT A PURE APPEND AND A TRUE-PREFIX TEST CANNOT PASS ON A CORRECT WRITE.**')
    print('    the register is NOT adopted and no face promoted : %s' % l5)
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LEDGER')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason) ### READ BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'A REGISTER READ IS NOT A REGISTER ENTERED' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTADOPTED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : approximation-register returns 1 row(s)' in irun
    k2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
             ('the register is adopted', 'a face is promoted',
              'the distance is evaluated', 'the criterion is proved'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the run passed : %s'
          % (k1, k2, k3))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOTADOPTED')

    print(chr(10) + "  G-NOEDIT (no owner instrument; only this act's papers path touched) ### the working-tree "
          "half READ BEFORE THE PUSH; the blob half SIDE-INVARIANT:")
    owner = ['tools/e16/b264_eps_decay.py', 'tools/noise_floor.py', 'tools/reg_seal.py',
             'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py',
             'tools/anchor_from_file.py', 'tools/quote_norm.py', 'tools/ferry_scan.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'FACES_LEDGER.md']
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    tech = not git(TC, 'status', '--porcelain').strip() if os.path.isdir(TC) else True
    gne = not touched and not ppbad and hand and dep and fnd and tech
    print('    owner instruments modified : %s ; papers paths beyond FACES_LEDGER.md : %s'
          % (touched or 'none', ppbad or 'none'))
    print('    HANDOFF clean : %s ; the deposited monograph clean : %s ; FINDINGS clean : %s ; TECHNE clean : %s'
          % (hand, dep, fnd, tech))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the lock verifies; EVERY relied-on run is AFTER the lock; nothing before it) '
          '### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, R, F))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY READ, ANY SEARCH AND ANY FETCH' in gate_text.flat(reg)
    go = o1 and o2 and o3 and o4 and o5
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('        lock    %s' % (stampm.group(1) if stampm else '?'))
    print('        extract %s   read %s   ledger %s' % (E['run_clock'], R['run_clock'], F['run_clock']))
    print('    the audit reads JOINTLY SATISFIABLE : %s ; the face says LOCKED BEFORE ANY READ : %s' % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### READ AFTER THE PUSH:')
    hookp, mirrorp = d('b362_hooks.txt'), d('b362_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        # ### **THE ROSTER SLOT b360 ADDED, EXERCISED:** ### this is the first faces update to reach the
        # ### archive at all, and the arm checks the ledger is IN the rebuilt archive rather than assuming it.
        r_ok = 'FACES_LEDGER.md IS IN THE REBUILT ARCHIVE : True' in mt
        gh = h_ok and m_ok and r_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror clean on all three : %s'
              % (h_ok, m_ok))
        print('    ### **THE ROSTER SLOT EXERCISED: the faces ledger is IN the rebuilt archive** : %s' % r_ok)
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    cl = re.search(r'clauses\s*:\s*(\d+)', sat)
    sm = re.search(r'### bytes locked : (\d+)', reg)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [
        ('reads %d' % E['reads'], ('`%d`' % E['reads']) in bank),
        ('without an anchor %d' % E['without_anchor'], ('`%d`' % E['without_anchor']) in bank),
        ('anchors differing %d' % E['anchors_differing'], ('`%d`' % E['anchors_differing']) in bank),
        ('sources attempted/fetched %d/%d' % (_J['L']['attempted'], _J['L']['fetched']),
         all(str(x) in bank for x in (_J['L']['attempted'], _J['L']['fetched']))),
        ('every source sha256 prefix in the bank',
         all(s2['sha256'][:16] in bank for s2 in _J['L']['sources'])),
        ('every source byte count in the bank',
         all(str(s2['bytes']) in bank for s2 in _J['L']['sources'])),
        ('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'), ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'), ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on read run file', R['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files resolved by their own recorded clocks, never by name):')
    once = True
    for lbl, jf in (('extract', E), ('read', R), ('ledger', _J['F']), ('locate', _J['L'])):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-8s %-26s clock on disk %s == the JSON's %s : %s" % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed but one square of zero, RE-MEASURED ON STRIPPED CODE):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    for p in [t(x) for x in ('b362_regspec.py', 'b362_locate.py', 'b362_extract.py',
                             'b362_read.py', 'b362_faces_row.py', 'b362_correspondence.py',
                             'b362_index_append.py', 'b362_checks.py')]:
        src2 = strip_prose(p)
        for b in banned:
            if b in src2:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in ('b362_read.py', 'b362_extract.py', 'b362_locate.py'))]
    gnc = not hits and not imports
    print("    numerical calls in this act's STRIPPED sources : %d %s" % (len(hits), hits or ''))
    print('    numerical libraries imported : %s' % (imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned = 0, 0, 0
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
            for hh in (ch + sh)[:6]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE APPROXIMATION REGISTER, READ UNDER A CAP (b362).'
    nxt = '# ### THE UNIFORMITY ARC, b349-b359 -- THE FOLD (b360).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    blk = ([ln for ln in faces.split(chr(10)) if ln.startswith('| N1 |')] or [''])[0]
    print(chr(10) + '  G-STEM-APPENDED (row %s, the ledger block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the ledger block', blk),
                      ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-20s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
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
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the ledger block and the index row):')
    tmpdir = tempfile.mkdtemp(prefix='b362_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the ledger block', blk),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
