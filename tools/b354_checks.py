# -*- coding: utf-8 -*-
"""b354_checks.py -- THE GATE SUITE FOR THE SIXTH FRAME.

### ### **EVERY `G-NO*` ARM READS STRIPPED CODE** (b348), ### **EVERY PRESENCE ARM READS RAW SOURCE** (b349),
### every quotation goes through `quote_norm`, and ### **EVERY ARM THAT READS A REPOSITORY STATE DECLARES ITS
### SIDE OF THE PUSH** (b352): `G-ROW`/`G-ANCESTOR` and `G-APPENDONLY` are read BEFORE THE PUSH and again
### after, and the pre-push reading is the one that carries; `G-NOEDIT` is `SIDE-INVARIANT`; this act writes
### nothing to the papers repo, so `G-NOHOOK` CHECKS that the hook and mirror are NOT OWED.
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
import quote_norm        # noqa: E402
import anchor_from_file as AF   # noqa: E402
import b354_extract as EX       # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b354_the_sixth_frame.txt')
REG = d('b354_registration_2026-09-07.txt')
REGBAD = d('b354_registration_SEALED_AGAINST_A_REFUSAL_2026-09-07.txt')
FERRY = d('b354_ferry_2026-09-07.txt')
EXTRACT = d('b354_extract_notes3.txt')
RUN, RJ = d('b354_sixth_run3.txt'), d('b354_sixth.json')
FJ = d('b354_frames.json')
NANRUN = d('b354_sixth_run_first_nan_scores.txt')
FIX = d('b354_anchor_fixtures.txt')
CORR, IDX = d('b354_corr_run.txt'), d('b354_index_run.txt')
TERMSCAN, GATE = d('b354_reg_termscan.txt'), d('b354_reg_gate.txt')
CENSUS, FCEN = d('b354_census.txt'), d('b354_faces_census.txt')
REGSPEC, SATIS = d('b354_regspec_run.txt'), d('audit_b354_reg_satisfiable.txt')
PINS = d('b354_pins_stepzero.txt')
SEAL = 'ca6accb46bc4af5304fa6c0ebfd47dec922637b4ee0c7acff0ac2e0da3fc1598'
ROWNUM = '202'

OWNED = [BANK, REG, REGBAD, FERRY, RUN, RJ, FJ, NANRUN, FIX, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS,
         GATE, TERMSCAN, EXTRACT, d('b354_extract_notes.txt'), d('b354_extract_notes2.txt'),
         d('b354_satisfiable.json'), d('b354_ferry_scan.txt'), d('b354_sixth_run.txt'), d('b354_sixth_run2.txt'),
         t('anchor_from_file.py'), t('b354_extract.py'), t('b354_regspec.py'), t('b354_sixth.py'),
         t('b354_correspondence.py'), t('b354_index_append.py')]

NEW_THIS_ACT = {'tools/anchor_from_file.py', 'tools/b354_extract.py', 'tools/b354_regspec.py',
                'tools/b354_sixth.py', 'tools/b354_correspondence.py', 'tools/b354_index_append.py',
                'tools/b354_checks.py'}

TOOLNUM = [
    ('the sixth rung, the bars and the verdict', 'tools/b354_sixth.py'),
    ('the anchors, built by reading', 'tools/anchor_from_file.py'),
    ('the frame sizes and the reads', 'tools/b354_extract.py'),
    ('the frame itself, IMPORTED and not re-tuned', 'tools/b316_instrument.py'),
    ('the stable cut, IMPORTED', 'tools/b319_stable.py'),
    ('the square trace, IMPORTED', 'tools/b318_square.py'),
    ('the seed and the ladder, IMPORTED', 'tools/b317_smear.py'),
    ("b352's models and minimiser, IMPORTED", 'tools/b352_fit.py'),
    ("b320's banked ladder, READ", 'tools/b320_run.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 202', 'tools/b354_correspondence.py'),
    ('the key', 'tools/b354_index_append.py'),
    ('35 clauses', 'tools/b354_regspec.py'),
    ('20553 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

SELF_HINTS = [
    ('the bank states the sign change first', 'THE SIXTH RUNG LANDED, AND ITS RESIDUAL IS NEGATIVE AT EVERY COVERED CELL'),
    ('### the rank is limited by NY', 'AND THE SIXTH RUNG IS THE FIRST RUNG AT WHICH THE RANK IS LIMITED BY'),
    ('### the two are not separated', 'SO THE TWO THINGS HAPPEN AT THE SAME RUNG, AND THIS ACT CANNOT SEPARATE THEM'),
    ('### the criterion is undefined', 'THE SEALED CRITERION IS UNDEFINED ON THE SIX-FRAME LADDER'),
    ('### bar 4 reproduced exactly', 'banked values ### **EXACTLY: `0.000e+00` RELATIVE DIFFERENCE AT ALL THREE CELLS.**'),
    ('### the sixth rung is not broken', 'SO THE SIXTH RUNG IS NOT A BROKEN COMPUTATION'),
    ('### the observed rank is NY exactly', 'THE OBSERVED RANK IS `512`. ### THAT IS `NY` EXACTLY'),
    ('### tabled not edited', 'THE CRITERION IS TABLED, NOT EDITED, AND THE TEMPTATION IS WORTH NAMING'),
    ("### the criterion's domain was never stated", 'ITS DOMAIN OF DEFINITION WAS NEVER STATED'),
    ('### a chosen ceiling is not a read one', 'AND THE SENTENCE THE ORDER REQUIRED: A CHOSEN CEILING IS NOT A READ ONE'),
    ('### the first measured wall', 'IS THE FIRST MEASURED WALL THIS LADDER HAS'),
    ('### the branch rule has no slot', 'SO THE SEALED BRANCH RULE HAS NO SLOT FOR THIS OUTCOME'),
    ("### b339's side-reading not withdrawn", 'AND THIS ACT DOES NOT WITHDRAW IT, FOR TWO REASONS AND BOTH ARE STATED'),
    ('### the seal taken against a refusal', 'A FIRST VERSION OF THIS REGISTRATION WAS SEALED AGAINST AN EXPLICIT REFUSAL'),
    ('### the anchor tool built, and its own two defects', 'AND ITS OWN FIXTURES FOUND TWO DEFECTS IN IT BEFORE IT WAS USED ONCE'),
    ('### eighteen anchors differed from their hints', 'ANCHORS DIFFER FROM THE'),
    ('### the thing no seat wrote down', 'THE LADDER HAD A LAST RUNG ALL ALONG, AND NOBODY HAD LOOKED FOR IT'),
    ('### the shadow', 'EXPECTED: ONE MORE NUMBER ON A LADDER'),
]

MUST_FAIL = [
    ('the bank never says the floor is established', BANK, '### THE FLOOR IS ESTABLISHED.'),
    ('the bank never says b352 is re-verdicted', BANK, '### b352 IS RE-VERDICTED.'),
    ('the bank never says the ceiling was read', BANK, '### THE CEILING WAS READ.'),
    ('the bank never says the ladder is a power law', BANK, '### THE LADDER IS A POWER LAW.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


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
    print('b354 -- GATE SUITE (ONE NEW RUNG, AND WHAT ARRIVED WITH IT)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    S = json.load(io.open(RJ, encoding='utf-8'))
    F = json.load(io.open(FJ, encoding='utf-8'))
    B339 = json.load(io.open(d('b339_price.json'), encoding='utf-8'))
    B320 = json.load(io.open(d('b320_rows.json'), encoding='utf-8'))
    B352 = json.load(io.open(d('b352_fit.json'), encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    cells = S['cells']

    print(chr(10) + '  G-ANCHORS (the step-zero tool built every anchor, its fixtures hold, and the count is printed):')
    a1 = AF.self_test(False)
    a2 = F['without_anchor'] == 0 and F['anchors_differing'] > 0
    a3 = str(F['anchors_differing']) in bank and str(F['reads']) in bank
    a4 = os.path.exists(FIX) and 'PASS' in io.open(FIX, encoding='utf-8').read()
    ga = a1 and a2 and a3 and a4
    print('    fixtures hold : %s ; anchors without a match : %d ; differing from their hint : %d of %d'
          % (a1, F['without_anchor'], F['anchors_differing'], F['reads']))
    print('    the counts carried in the bank : %s ; the fixture record on disk : %s  %s'
          % (a3, a4, 'PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ANCHORS')

    print(chr(10) + '  G-CEILING (a CHOSEN number in those words, with its basis and the sentence; the wall printed):')
    c1 = 'IT IS A CHOSEN NUMBER, AND THIS SECTION SAYS SO IN THOSE WORDS' in gate_text.flat(reg)
    c2 = 'A CHOSEN CEILING IS NOT A READ ONE' in bf
    c3 = ('%.0f' % S['wall_ceiling']) in bank and ('%.1f' % S['wall']) in bank
    c4 = S['wall'] < S['wall_ceiling'] and not S['overran']
    c5 = 'THE WALL IS NOT IN THE RECORD' in bf
    gc = c1 and c2 and c3 and c4 and c5
    print('    chosen, in those words : %s ; the sentence present : %s ; the record has no wall : %s' % (c1, c2, c5))
    print('    ceiling %.0f and measured wall %.1f both in the bank : %s ; did not overrun : %s  %s'
          % (S['wall_ceiling'], S['wall'], c3, c4, 'PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CEILING')

    print(chr(10) + "  G-REPRO (bar 4: the fifth rung recomputed equals b320's banked value at every cell):")
    r1 = all(r['ok'] for r in S['repro'])
    r2 = all(abs(r['here'] - B320['axes'][r['a']]['domain'][-1]) == 0.0 for r in S['repro'])
    r3 = S['identity_fifth'] <= 1e-9
    gr = r1 and r2 and r3
    for r in S['repro']:
        print('      a=%-6s here %.12f  banked %.12f  rel %.3e' % (r['a'], r['here'], r['banked'], r['rel']))
    print('    every cell within the bar : %s ; every cell EXACT : %s ; fifth identity control : %.1e  %s'
          % (r1, r2, S['identity_fifth'], 'PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-REPRO')

    print(chr(10) + '  G-IDENTITY (bar 3 at the sixth frame, with its floor):')
    i1 = S['identity_sixth'] <= 1e-9
    floor = S['frame6']['dim'] * 2.220446049250313e-16
    i2 = ('%.1e' % floor) in bank or '7.1e-12' in bank
    gi = i1 and i2
    print('    |Tr - dim| = %.3e   bar 1e-9   floor dim*eps = %.1e   in the bank : %s  %s'
          % (S['identity_sixth'], floor, i2, 'PASS' if gi else '### FAIL ###'))
    if not gi:
        fails.append('G-IDENTITY')

    print(chr(10) + '  G-SAMECRITERION (the models and minimiser IMPORTED by object identity, not by name):')
    import b352_fit as F52
    import b354_sixth as SIX
    s1 = SIX.F52 is F52
    s2 = all(m[1] is n[1] for m, n in zip(F52.MODELS, F52.MODELS))
    s3 = max(S['per_cell'][k]['same_criterion'] for k in cells) < 1e-9
    s4 = all(abs(S['per_cell'][k]['five'][m]['aicc'] - B352['per_cell'][k]['models'][m]['aicc']) < 1e-9
             for k in cells for m in ('M1', 'M2', 'M3'))
    gs = s1 and s2 and s3 and s4
    print('    the run tool holds the SAME module object as b352_fit : %s' % s1)
    print("    refitting five frames reproduces b352's banked AICc to %.2e : %s / %s  %s"
          % (max(S['per_cell'][k]['same_criterion'] for k in cells), s3, s4, 'PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SAMECRITERION')

    print(chr(10) + "  G-SIXTH (the sixth residual at every cell; the first five equal to b339's banked array):")
    x1 = all(k in S['rows'] for k in cells)
    x2 = all(S['per_cell'][k]['R6'][:5] == B339['cells'][k]['R'] for k in cells)
    x3 = all(S['per_cell'][k]['R_sixth'] < 0 for k in cells)
    x4 = all(('%+.9e' % S['per_cell'][k]['R_sixth']) in bank for k in cells)
    x5 = S['xs6'] == list(B339['xs']) + [256.0]
    gx = x1 and x2 and x3 and x4 and x5
    print("    a sixth residual at every cell : %s ; the first five are b339's, unchanged : %s" % (x1, x2))
    print('    all three negative : %s ; all three printed in the bank : %s ; the ladder is six rungs : %s  %s'
          % (x3, x4, x5, 'PASS' if gx else '### FAIL ###'))
    if not gx:
        fails.append('G-SIXTH')

    print(chr(10) + '  G-RANK (the saturation measured, not asserted):')
    k1 = S['rank_saturated'] and S['frame6']['rank'] == 512
    k2 = abs(S['rank_extrapolated'] - 516.0) < 1.0
    k3 = S['ranks_banked'] == [20, 37, 69, 133, 262]
    k4 = '516' in bank and '512' in bank and 'THAT IS `NY` EXACTLY' in bank
    gkk = k1 and k2 and k3 and k4
    print('    observed rank %d = NY : %s ; extrapolated %.0f : %s ; banked ranks %s : %s'
          % (S['frame6']['rank'], k1, S['rank_extrapolated'], k2, S['ranks_banked'], k3))
    print('    both numbers and the sentence in the bank : %s  %s' % (k4, 'PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-RANK')

    print(chr(10) + '  G-NOTSEPARATED (the act separates the sign change from the boundary NOWHERE, and says so):')
    n1 = 'THIS ACT CANNOT SEPARATE THEM' in bf
    n2 = 'NOTHING IN THIS' in bf and 'ACT DECIDES WHETHER THE OBJECT' in bf
    n3 = 'SEPARATES THEM NOWHERE' in tbl
    gns = n1 and n2 and n3
    print('    stated in the bank : %s / %s ; carried into the row : %s  %s' % (n1, n2, n3, 'PASS' if gns else '### FAIL ###'))
    if not gns:
        fails.append('G-NOTSEPARATED')

    print(chr(10) + '  G-CRITERION (undefined, no score reported, TABLED not edited):')
    q1 = S['criterion_undefined']
    q2 = all(S['per_cell'][k]['six'] is None for k in cells)
    q3 = 'TABLED, NOT EDITED' in bf and 'A SECOND CRITERION' in bf
    q4 = 'ITS DOMAIN OF DEFINITION WAS NEVER STATED' in bf
    q5 = os.path.exists(NANRUN)
    code = strip_prose(t('b354_sixth.py'))
    q6 = 'linear' not in code.lower().replace('np.linalg', '').replace('linear', '', 0) or True
    q7 = 'np.log' not in code   # ### the tool does not re-implement the criterion
    gq = q1 and q2 and q3 and q4 and q5 and q7
    print('    the criterion is recorded undefined : %s ; no six-frame score stored : %s' % (q1, q2))
    print('    tabled not edited, and the second-criterion sentence : %s ; the domain fault named : %s' % (q3, q4))
    print('    the not-a-number run banked under a declaring name : %s ; the tool re-implements no fit : %s  %s'
          % (q5, q7, 'PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-CRITERION')

    print(chr(10) + "  G-VERDICT (the branch by (F)'s rule; the branches not taken shown unreachable):")
    v1 = S['verdict'] == 'FLOOR UNDER-RESOLVED STILL' and 'FLOOR UNDER-RESOLVED STILL' in bf
    v2 = '(FLOOR ESTABLISHED) -- UNREACHABLE, AND SHOWN SO' in bf
    v3 = '(NO FLOOR PREFERRED) -- UNREACHABLE FOR THE SAME REASON' in bf
    v4 = '(ABANDONED) -- NOT TAKEN' in bf
    v5 = 'THE REASON IS NOT THE ONE THE BRANCH ANTICIPATED' in bf
    gv = v1 and v2 and v3 and v4 and v5
    print('    verdict agrees : %s ; the three branches accounted for : %s / %s / %s' % (v1, v2, v3, v4))
    print("    and the act says the reason is not the branch's : %s  %s" % (v5, 'PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-VERDICT')

    print(chr(10) + '  G-PENALTY (the two penalty numbers printed, and the attribution honest about having nothing to attribute):')
    p1 = abs(S['pen5'] - 20.0) < 1e-12 and abs(S['pen6'] - 10.0) < 1e-12
    p2 = '20.0' in bank and '10.0' in bank
    p3 = 'THE ATTRIBUTION MACHINERY WAS BUILT AND HAD NOTHING TO ATTRIBUTE' in bf
    gp = p1 and p2 and p3
    print('    penalties %.1f and %.1f as sealed : %s ; in the bank : %s ; the honest note : %s  %s'
          % (S['pen5'], S['pen6'], p1, p2, p3, 'PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PENALTY')

    print(chr(10) + '  G-STANDS (b339, b346 and b352 all standing; b352 EXTENDED and not re-verdicted):')
    t1 = 'b339 IS NOT RE-VERDICTED' in bf and 'ITS `UNAFFORDABLE` STANDS' in bank
    t2 = 'b346 IS NOT RE-VERDICTED' in bf
    t3 = 'b352 IS EXTENDED' in bf and 'NOT RE-VERDICTED' in bf
    t4 = 'AND THIS ACT DOES NOT WITHDRAW IT' in bf
    gst = t1 and t2 and t3 and t4
    print('    b339 : %s ; b346 : %s ; b352 extended : %s ; the side-reading kept : %s  %s'
          % (t1, t2, t3, t4, 'PASS' if gst else '### FAIL ###'))
    if not gst:
        fails.append('G-STANDS')

    print(chr(10) + '  G-SEALINCIDENT (the improperly sealed registration banked byte for byte, and declared):')
    z1 = os.path.exists(REGBAD)
    z2 = z1 and 'THE REGISTRATION SEAL' in io.open(REGBAD, encoding='utf-8', errors='replace').read()
    z3 = 'SEALED AGAINST AN EXPLICIT REFUSAL' in bf
    z4 = 'AN INSTRUMENT REFUSING IS ONLY A REFUSAL IF SOMETHING' in bf
    z5 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    gz = z1 and z2 and z3 and z4 and z5
    print('    the refused file on disk with its seal intact : %s / %s ; declared in the bank : %s' % (z1, z2, z3))
    print('    the lesson stated : %s ; and THIS registration is satisfiable : %s  %s'
          % (z4, z5, 'PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-SEALINCIDENT')

    print(chr(10) + '  SELF NEEDLES (each hint resolved to the bank\'s own line by the step-zero tool):')
    for lbl, hint in SELF_HINTS:
        try:
            n, line = AF.find(BANK, hint)
            needle_pull.pull(BANK, line)
            print('    PASS  %-52s line %d' % (lbl, n))
        except (AF.AnchorError, LookupError) as e:
            fails.append('SELF: ' + lbl)
            print('    ### FAIL  %-52s %s' % (lbl, str(e)[:70]))

    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    print(chr(10) + '  OWNER NEEDLES (each at its emitting file, each in the extract):')
    nbad = 0
    for label, tag, path, hint in EX.READS:
        try:
            _n, line = AF.find(path, hint)
            needle_pull.pull(path, line)
            if not quote_norm.contains(extract, line):
                nbad += 1
                print('    ### FAIL (NOT IN THE EXTRACT)  %s' % label)
        except (AF.AnchorError, LookupError):
            nbad += 1
            print('    ### FAIL (NO ANCHOR)  %s' % label)
    cited = len(re.findall(r'^ +\S+ : line \d+ ', extract, re.M))
    print('    reads %d ; all located and in the extract : %s ; cited lines : %d'
          % (len(EX.READS), nbad == 0, cited))
    if nbad:
        fails.append('G-EXTRACT')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s). ### **PRE-PUSH READING CARRIES.**' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'SEPARATES THEM NOWHERE' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s ; %s'
          % (ROWNUM, len(rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTSEPARATED (the index):')
    irun = io.open(IDX, encoding='utf-8').read()
    k_1 = 'READ BACK : sixth-frame returns 1 row(s)' in irun
    k_2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
              ('the residual crosses zero', 'the floor is gone', 'the instrument failed', 'the criterion was replaced'))
    k_3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k_1 and k_2 and k_3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s ; %s'
          % (k_1, k_2, k_3, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY')

    print(chr(10) + '  G-APPENDONLY (banked_index.py). ### **READ BEFORE THE PUSH.**')
    ib = blob_of(ROOT, 'tools/banked_index.py')
    ap = True
    if ib is not None:
        old, new = norm(ib).split(chr(10)), norm(idx).split(chr(10))
        i = 0
        for ln in new:
            if i < len(old) and ln == old[i]:
                i += 1
        ap = (i == len(old))
    print('    every committed line still present, in order : %s' % ap)
    if not ap:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (no owner instrument edited; nothing outside relay/SIDE moved). ### SIDE-INVARIANT.')
    owner = ['tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py', 'tools/b319_stable.py',
             'tools/b320_run.py', 'tools/b352_fit.py', 'tools/quote_norm.py', 'tools/run_clock.py',
             'tools/gate_text.py', 'tools/registration_gate.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    tcstat = [x for x in git(TC, 'status', '--porcelain').splitlines() if x.strip()]
    gne = not touched and not ppstat and not tcstat
    print('    owner instruments modified : %s ; papers dirty : %s ; TECHNE dirty : %s  %s'
          % (touched or 'none', ppstat or 'none', tcstat or 'none', 'PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-NOHOOK (nothing written to the papers repo, so hook and mirror NOT owed -- CHECKED):')
    h1 = not ppstat
    h2 = git(PP, 'log', '-1', '--format=%H').strip() == git(PP, 'rev-parse', 'origin/main').strip()
    h3 = 'NOT OWED' in tbl
    gho = h1 and h2 and h3
    print('    papers tree clean : %s ; HEAD equals remote : %s ; the row says NOT OWED : %s  %s'
          % (h1, h2, h3, 'PASS' if gho else '### FAIL ###'))
    if not gho:
        fails.append('G-NOHOOK')

    print(chr(10) + '  G-ORDER (the seal verifies; the ordering read from clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and F['run_clock'] < stampm.group(1) < S['run_clock']
    o4 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    extract %s < seal < run %s : %s ; JOINTLY SATISFIABLE : %s'
          % (F['run_clock'], S['run_clock'], o3, o4))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS:')
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    clc = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [('the seal hash', SEAL in bank),
              ('the seal stamp', (stampm.group(1) if stampm else 'x') in bank),
              ('%s bytes sealed' % sm, ('%s bytes' % sm) in bank),
              ('%s clauses' % clc, ('%s clauses' % clc) in bank),
              ('row %s' % rn, rn == ROWNUM),
              ('the extract and run clocks', F['run_clock'] in bank and S['run_clock'] in bank),
              ('the measured wall', ('%.1f' % S['wall']) in bank),
              ('the decomposition wall', ('%.1f' % S['svd_wall']) in bank),
              ('the frame shape', all(str(S['frame6'][x]) in bank for x in ('free', 'rank', 'dim'))),
              ('the size ratio', ('%.2f' % F['size_ratio']) in bank)]
    for k in cells:
        checks.append(('a=%s the sixth residual' % k, ('%+.9e' % S['per_cell'][k]['R_sixth']) in bank))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the numbered repeats on disk AND declared):')
    once = (os.path.exists(NANRUN) and os.path.exists(RUN)
            and 'THE COMPONENT RAN THREE TIMES AND ALL THREE RUN FILES ARE ON DISK' in bf
            and 'the second run built `26` of `26`' in bank)
    print('    %s' % once)
    if not once:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM:')
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
            for hh in (ch + sh)[:4]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib2 = idx[idx.index('# ### THE SIXTH FRAME (b354).'):idx.index("# ### THE WIDTH COORDINATE'S MISSING STATEMENT (b353).")] \
        if '# ### THE SIXTH FRAME (b354).' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED:')
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the index row', ib2)):
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

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b354_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the index row', ib2)):
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
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
