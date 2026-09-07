# -*- coding: utf-8 -*-
"""b356_checks.py -- THE GATE SUITE FOR THE OBJECT OR THE BOUNDARY.

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
import b356_extract as EX       # noqa: E402

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


BANK = d('b356_the_boundary.txt')
REG = d('b356_registration_2026-09-07.txt')
FERRY = d('b356_ferry_2026-09-07.txt')
EXTRACT = d('b356_extract_notes3.txt')
RUN, RJ = d('b356_raised_run2.txt'), d('b356_raised.json')
FJ = d('b356_axis.json')
CORR, IDX = d('b356_corr_run.txt'), d('b356_index_run.txt')
TERMSCAN, GATE = d('b356_reg_termscan.txt'), d('b356_reg_gate.txt')
CENSUS, FCEN = d('b356_census.txt'), d('b356_faces_census.txt')
REGSPEC, SATIS = d('b356_regspec_run.txt'), d('audit_b356_reg_satisfiable.txt')
PINS = d('b356_pins_stepzero.txt')
SEAL = 'b645c6c0faac2fc4b6cdde6ceb857322fdd107e6d12765a259f7ec064ecc915b'
ROWNUM = '204'

OWNED = [BANK, REG, FERRY, RUN, RJ, FJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, GATE, TERMSCAN,
         EXTRACT, d('b356_extract_notes.txt'), d('b356_extract_notes2.txt'), d('b356_raised_run.txt'),
         d('b356_satisfiable.json'), d('b356_ferry_scan.txt'),
         t('b356_extract.py'), t('b356_regspec.py'), t('b356_raised.py'),
         t('b356_correspondence.py'), t('b356_index_append.py')]

NEW_THIS_ACT = {'tools/b356_extract.py', 'tools/b356_regspec.py', 'tools/b356_raised.py',
                'tools/b356_correspondence.py', 'tools/b356_index_append.py', 'tools/b356_checks.py'}

TOOLNUM = [
    ('the raised frame, the control and the verdict', 'tools/b356_raised.py'),
    ("b344's quadrature ladder, READ for the bar's floor", 'tools/b356_extract.py'),
    ('the anchors, built by reading', 'tools/anchor_from_file.py'),
    ('the frame itself, IMPORTED', 'tools/b316_instrument.py'),
    ('the stable cut, IMPORTED', 'tools/b319_stable.py'),
    ('the square trace, IMPORTED', 'tools/b318_square.py'),
    ('the seed, IMPORTED', 'tools/b317_smear.py'),
    ("b354's sixth rung, READ", 'tools/b354_sixth.py'),
    ("b344's NY ladder, READ", 'tools/b344_ny.py'),
    ("b320's banked table, READ", 'tools/b320_run.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 204', 'tools/b356_correspondence.py'),
    ('the key', 'tools/b356_index_append.py'),
    ('38 clauses', 'tools/b356_regspec.py'),
    ('16874 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

SELF_HINTS = [
    ('the bank states the verdict first', 'THE ANSWER, FIRST.'),
    ('### the residual returns positive', 'THE RESIDUAL RETURNS POSITIVE AT EVERY COVERED CELL ONCE THE QUADRATURE BOUND IS LIFTED'),
    ('### the rank is clear of the bound', 'AND THE RANK IS NO LONGER AT ITS BOUND'),
    ('### the edge located', "SO b354's SIXTH RUNG WAS THE INSTRUMENT'S EDGE"),
    ('### the extrapolation was accurate', 'within two of the extrapolation'),
    ('### the control held', 'THE CONTROL HELD**, which is what licensed any of this'),
    ("### the bar's floor earned its keep", "AND THE BAR'S FLOOR EARNED ITS KEEP"),
    ('### the one comparison licensed', 'THE ONE COMPARISON THIS ACT LICENSES, AND IT LICENSES NO OTHER'),
    ('### the comparison refused by name', 'AND THE COMPARISON A READER WILL REACH FOR, REFUSED HERE'),
    ('### the bequest, not a conclusion', 'A BEQUEST, NOT A CONCLUSION'),
    ('### two points are not a convergence', 'TWO POINTS ARE NOT A CONVERGENCE'),
    ('### a sign returning once is not safe', 'THAT RETURNS UNDER ONE RAISE IS NOT A SIGN THAT IS SAFE'),
    ('### b354 not re-verdicted, and why', 'AN ACT THAT NAMED ITS OWN AMBIGUITY IS NOT WRONG'),
    ("### b339's side-reading back where b339 left it", "SO b339's SIDE-READING"),
    ('### six dimensions decided the sign', 'SIX DIMENSIONS DECIDED THE SIGN'),
    ('### the practical consequence, named not ordered', 'NONE OF THE THREE CHECKED THE BOUND, AND THE CHECK WAS ALWAYS AVAILABLE'),
    ('### the seal on the audit exit code', "THE SEAL WAS TAKEN ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK"),
    ('### the shadow', 'EXPECTED: ONE PARAMETER MOVED AND A SIGN READ OFF IT'),
]

MUST_FAIL = [
    ("the bank never says the sign is the object's", BANK, "### THE SIGN IS THE OBJECT'S."),
    ('the bank never says b354 is re-verdicted', BANK, '### b354 IS RE-VERDICTED.'),
    ('the bank never says the floor is an artifact', BANK, '### THE FLOOR IS AN ARTIFACT.'),
    ('the bank never says the ceiling was read', BANK, '### THE CEILING WAS READ.'),
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
    print('b356 -- GATE SUITE (ONE PARAMETER MOVED, AND WHAT IT SEPARATED)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    S = json.load(io.open(RJ, encoding='utf-8'))
    F = json.load(io.open(FJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    cells = S['cells']

    print(chr(10) + '  G-ANCHORS (every anchor built by the tool; its fixtures run; refusals and count reported):')
    a1 = AF.self_test(False)
    a2 = F['without_anchor'] == 0 and F['anchors_differing'] > 0
    a3 = str(F['anchors_differing']) in bank and str(F['reads']) in bank
    ga = a1 and a2 and a3
    print('    fixtures hold : %s ; without a match : %d ; differing from their hint : %d of %d  %s'
          % (a1, F['without_anchor'], F['anchors_differing'], F['reads'], 'PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ANCHORS')

    print(chr(10) + '  G-RAISED (the axis raised to exactly the sealed value; everything else identical to b354):')
    B354 = json.load(io.open(d('b354_sixth.json'), encoding='utf-8'))
    r1 = S['raised'] == 1024 and S['sixth'][2] == 1024
    r2 = S['sixth'][0] == B354['sixth'][0] and S['sixth'][1] == B354['sixth'][1]
    r3 = S['frame6']['free'] == B354['frame6']['free']
    r4 = '1024' in bank and 'IT WAS RE-TUNED, ONCE' in bank
    gra = r1 and r2 and r3 and r4
    print('    raised to %d : %s ; N and X identical to b354 : %s ; free identical : %s'
          % (S['raised'], r1, r2, r3))
    print('    and the act says it is RE-TUNING : %s  %s' % (r4, 'PASS' if gra else '### FAIL ###'))
    if not gra:
        fails.append('G-RAISED')

    print(chr(10) + '  G-CONTROL (bars 1 and 2 at the fifth rung, printed with their floors):')
    c1 = S['rank_ok'] and S['rank5'] == 262
    c2 = S['trace_ok'] and S['worst_control_rel'] <= S['bar_trace']
    c3 = S['worst_control_rel'] > S['bar_trace_floor']
    c4 = ('%.3e' % S['bar_trace_floor']) in bank and ('%.3e' % S['worst_control_rel']) in bank
    c5 = S['control_ok']
    gc = c1 and c2 and c3 and c4 and c5
    print('    bar 1, the rank equality : %s (rank %d) ; bar 2, the trace : %s (worst %.3e vs bar %.0e)'
          % (c1, S['rank5'], c2, S['worst_control_rel'], S['bar_trace']))
    print("    the observed move is ABOVE the floor %.3e (so the bar discriminates) : %s ; both in the bank : %s  %s"
          % (S['bar_trace_floor'], c3, c4, 'PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CONTROL')

    print(chr(10) + '  G-IDENTITY (bar 3 at both frames):')
    i1 = S['identity5'] <= 1e-9 and S['identity6'] <= 1e-9
    gi = i1
    print('    fifth %.3e ; raised sixth %.3e ; bar 1e-9  %s'
          % (S['identity5'], S['identity6'], 'PASS' if gi else '### FAIL ###'))
    if not gi:
        fails.append('G-IDENTITY')

    print(chr(10) + '  G-COMPARABLE (one comparison licensed, and the other named as refused):')
    p1 = set(S['signs'].keys()) == set(S['cells'])
    p2 = 'THE ONE COMPARISON THIS ACT LICENSES, AND IT LICENSES NO OTHER' in bf
    p3 = 'AND THE COMPARISON A READER WILL REACH FOR, REFUSED HERE' in bf
    p4 = 'IT MOVES TWO PARAMETERS AT ONCE' in bf
    gp = p1 and p2 and p3 and p4
    print('    the licensed comparison present at every cell : %s ; declared as the only one : %s' % (p1, p2))
    print('    the tempting one named and refused : %s / %s  %s' % (p3, p4, 'PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-COMPARABLE')

    print(chr(10) + '  G-CEILING (CHOSEN in those words, its basis stated, the unpriceable part named):')
    e1 = 'CHOSEN, NOT READ' in gate_text.flat(reg)
    e2 = 'A CHOSEN CEILING IS NOT A READ ONE' in gate_text.flat(reg)
    e3 = ('%.0f' % S['wall_ceiling']) in bank and ('%.1f' % S['wall']) in bank
    e4 = S['wall'] < S['wall_ceiling'] and not S['overran']
    e5 = 'THIS ACT CANNOT PRICE ITS OWN FRAME' in gate_text.flat(reg)
    gce = e1 and e2 and e3 and e4 and e5
    print('    chosen in those words : %s ; the sentence : %s ; cannot price its own frame : %s' % (e1, e2, e5))
    print('    ceiling %.0f and wall %.1f in the bank : %s ; did not overrun : %s  %s'
          % (S['wall_ceiling'], S['wall'], e3, e4, 'PASS' if gce else '### FAIL ###'))
    if not gce:
        fails.append('G-CEILING')

    print(chr(10) + '  G-RANKREPORTED (the observed rank at the raised axis printed, not inferred):')
    k1 = str(S['rank6']) in bank and str(S['raised']) in bank
    k2 = S['cleared'] == (S['rank6'] < S['raised'])
    k3 = '518' in bank and '516' in bank
    gk = k1 and k2 and k3
    print('    rank %d against bound %d, both in the bank : %s ; cleared flag consistent : %s' % (S['rank6'], S['raised'], k1, k2))
    print('    the observed and the extrapolated both printed : %s  %s' % (k3, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-RANKREPORTED')

    print(chr(10) + "  G-VERDICT (the branch by (F)'s rule; the two conditions of the first branch checked as two):")
    v1 = S['verdict'] == 'THE BOUNDARY' and 'THE BOUNDARY' in bf
    v2 = '(THE OBJECT) -- UNREACHABLE, AND SHOWN SO' in bf
    v3 = '(STILL CONFOUNDED) -- UNREACHABLE, AND SHOWN SO' in bf
    v4 = (not S['all_neg']) and S['all_pos'] and S['cleared']
    v5 = 'It demands TWO conditions together' in bank
    gv = v1 and v2 and v3 and v4 and v5
    print('    verdict agrees : %s ; both others unreachable : %s / %s' % (v1, v2, v3))
    print('    the branch conditions recompute : %s ; the two-condition demand stated : %s  %s'
          % (v4, v5, 'PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-VERDICT')

    print(chr(10) + '  G-NOLIMIT (the act nowhere says one raise settles the limit):')
    n1 = 'TWO POINTS ARE NOT A CONVERGENCE' in bf
    n2 = 'NOT A SIGN THAT SURVIVES THE LIMIT' in bf
    n3 = 'NOT A SIGN THAT IS SAFE' in bf
    gnl = n1 and n2 and n3
    print('    two points not a convergence : %s ; not the limit : %s ; and the symmetric refusal : %s  %s'
          % (n1, n2, n3, 'PASS' if gnl else '### FAIL ###'))
    if not gnl:
        fails.append('G-NOLIMIT')

    print(chr(10) + "  G-CRITERION (b352's criterion not replaced; no score reported):")
    q1 = 'stays and is not replaced' in bank
    q2 = 'no fit was ordered' in bank or 'ordered no fit and reported no score' in bank
    code = strip_prose(t('b356_raised.py'))
    q3 = 'b352_fit' not in code and 'aicc' not in code.lower()
    gq = q1 and q2 and q3
    print("    the criterion stays : %s ; no score reported : %s ; the tool imports no fitter : %s  %s"
          % (q1, q2, q3, 'PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-CRITERION')

    print(chr(10) + '  G-STANDS (b354 not re-verdicted; the side-reading not withdrawn):')
    t1 = 'b354 IS NOT RE-VERDICTED' in bf
    t2 = 'AN ACT THAT NAMED ITS OWN AMBIGUITY IS NOT WRONG' in bf
    t3 = 'IS NOT WITHDRAWN' in bf
    t4 = 'b352' in bank and 'UNTOUCHED' in bf
    gst = t1 and t2 and t3 and t4
    print('    b354 stands : %s / %s ; the side-reading kept : %s ; b352 untouched : %s  %s'
          % (t1, t2, t3, t4, 'PASS' if gst else '### FAIL ###'))
    if not gst:
        fails.append('G-STANDS')

    print(chr(10) + "  G-SEALCHAIN (the seal taken only after the audit's own exit code):")
    z1 = "SEALED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK" in bf
    z2 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    z3 = "SEALED ONLY ON THE AUDIT'S OWN EXIT CODE" in gate_text.flat(reg)
    gz = z1 and z2 and z3
    print('    stated in the bank : %s ; the audit is satisfiable : %s ; sealed on it in the registration : %s  %s'
          % (z1, z2, z3, 'PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-SEALCHAIN')

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
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and "INSTRUMENT'S EDGE" in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s ; %s'
          % (ROWNUM, len(rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTCONVERGED (the index):')
    irun = io.open(IDX, encoding='utf-8').read()
    k_1 = 'READ BACK : object-or-boundary returns 1 row(s)' in irun
    k_2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
              ('the residual is positive', 'the floor is confirmed', 'b354 was wrong', 'the ladder continues'))
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
              ('the raised rank and its bound', str(S['rank6']) in bank and str(S['raised']) in bank),
              ("the control's worst relative move", ('%.3e' % S['worst_control_rel']) in bank),
              ("the bar's floor", ('%.3e' % S['bar_trace_floor']) in bank)]
    for k in S['cells']:
        checks.append(('a=%s the two residuals' % k,
                       ('%+.9e' % S['signs'][k]['old']) in bank and ('%+.9e' % S['signs'][k]['new']) in bank))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the numbered repeats on disk AND declared):')
    once = (os.path.exists(d('b356_extract_notes.txt')) and os.path.exists(EXTRACT)
            and os.path.exists(d('b356_raised_run.txt')) and os.path.exists(RUN)
            and 'THE EXTRACT RAN TWICE AND BOTH RUN FILES ARE ON DISK' in bf
            and 'THE RUN RAN TWICE' in bf)
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

    ib2 = idx[idx.index('# ### THE OBJECT OR THE BOUNDARY (b356).'):idx.index('# ### WHAT THE ARRAYS ARE (b355).')] \
        if '# ### THE OBJECT OR THE BOUNDARY (b356).' in idx else ''
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
    tmpdir = tempfile.mkdtemp(prefix='b356_hedge_')
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
