# -*- coding: utf-8 -*-
"""b351_checks.py -- THE GATE SUITE FOR THE PARTITION QUESTION.

### ### **EVERY `G-NO*` ARM READS STRIPPED CODE** (b348's rule), and ### **EVERY PRESENCE ARM READS RAW SOURCE**
### (b349's correction to it: the rule governs ABSENCE claims, not PRESENCE ones).
### ### **EVERY QUOTATION COMPARISON GOES THROUGH `quote_norm`**, the sortie's shared normaliser.
### ### **THE ARMS (registration section (F)):** `G-CEILING`, `G-NOCOMPUTE`, `G-FOURCOORD`, `G-STATE`,
### `G-INSTRUMENT`, `G-QUOTE`, `G-VERDICT`, `G-PRICE`, `G-NOSILENCE`, `G-NOGRADE`, `G-NOEDIT`, `G-ORDER`,
### `G-ROW`, `G-KEY`/`G-NOTSHAPED`, `G-APPENDONLY`, `G-NOHOOK` (the papers repo does NOT move, checked and not
### assumed), `G-STRUCK`, `G-STEM`, `G-SHARED`, `G-TOOLNUM`, `G-NUMBERS`, `G-ONCE`, the hedge audit, `G-AFTER`.
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
import b351_extract as EX  # noqa: E402

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


BANK = d('b351_the_partition_question.txt')
REG = d('b351_registration_2026-09-07.txt')
FERRY = d('b351_ferry_2026-09-07.txt')
ORDER = d('b350_ferry_2026-09-07.txt')
EXTRACT, EXTRACT1 = d('b351_extract_notes2.txt'), d('b351_extract_notes.txt')
RRUN, RJ = d('b351_read_run.txt'), d('b351_read.json')
CORR, IDX = d('b351_corr_run.txt'), d('b351_index_run.txt')
SCAN, TERMSCAN, GATE = d('b351_ferry_scan.txt'), d('b351_reg_termscan.txt'), d('b351_reg_gate.txt')
CENSUS, FCEN = d('b351_census.txt'), d('b351_faces_census.txt')
REGSPEC, SATIS = d('b351_regspec_run.txt'), d('audit_b351_reg_satisfiable.txt')
PINS, INDEXQ = d('b351_pins_stepzero.txt'), d('audit_b351_index_query.txt')
SEAL = '379a358b83148b02e0039490d17e4bf7248d5a9d2689f0facf6e07271a1950c1'
ROWNUM = '199'

OWNED = [BANK, REG, FERRY, RRUN, RJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         TERMSCAN, EXTRACT, EXTRACT1, d('b351_satisfiable.json'),
         t('b351_extract.py'), t('b351_regspec.py'), t('b351_read.py'),
         t('b351_correspondence.py'), t('b351_index_append.py')]

NEW_THIS_ACT = {'tools/b351_extract.py', 'tools/b351_regspec.py', 'tools/b351_read.py',
                'tools/b351_correspondence.py', 'tools/b351_index_append.py', 'tools/b351_checks.py'}

TOOLNUM = [
    ('the four coordinates, the states and the verdict', 'tools/b351_read.py'),
    ('every quotation at its emitting line', 'tools/b351_extract.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ("b326's census figures, READ and not recomputed", 'tools/b326_offline.py'),
    ("b334's charted sets, READ and not recomputed", 'tools/b334_aimmap.py'),
    ("b328's phase identity, READ and not recomputed", 'tools/b328_family.py'),
    ('row 199', 'tools/b351_correspondence.py'),
    ('the key', 'tools/b351_index_append.py'),
    ('40 clauses', 'tools/b351_regspec.py'),
    ('14215 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

CEILING = [
    ('the ceiling -- reads and a pricing only', ORDER, 'and a pricing only; NO partition constructed, NO class proved'),
    ('the ceiling -- UNAFFORDABLE is a full verdict', ORDER, 'banked; UNAFFORDABLE is a full and welcome verdict. Ask: do'),
    ('the question -- the coordinates', ORDER, "the aim plane's own coordinates"),
    ('the method -- bound it, or prove a class silent', ORDER, 'whether the record can bound it, and where a class would have'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK, '### ### ### **UNDECIDED.**'),
    ('### the sealed distinction', BANK, '### **A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE.**'),
    ('### the abscissa is closed as an object', BANK, '### ### **THIS CLOSES THE COORDINATE FOR ZEROS NOBODY HAS FOUND.**'),
    ('### the height bound is the looking', BANK, '### ### **THE NUMBER `150` IS WHERE THE CENSUS STOPPED. ### IT IS NOT A PROPERTY OF THE OBJECT.**'),
    ('### instances are not a class', BANK, '### ### HIGHER BUYS MORE INSTANCES, AND A CLASS IS NOT MADE OF INSTANCES.**'),
    ('### the price is for the wrong object', BANK, '### ### OBJECT.** ### Sixty boxes buy the zeros between `150` and `300`.'),
    ('### the phase is finitely cut', BANK, '### ### ALGEBRAIC RATHER THAN MEASURED**'),
    ('### the one class the algebra cannot see', BANK, "### ### **AND EXACTLY ONE CLASS SURVIVES THE ALGEBRA: `|G| = 0`.**"),
    ('### the width has no method', BANK, '### **THE WIDTH HAS NO METHOD.**'),
    ('### both branches shown unreachable', BANK, '### ### **(A SHAPE EXISTS) -- UNREACHABLE, AND SHOWN SO.**'),
    ('### an absence is not an obstruction', BANK, '### ### **(NO FINITE PARTITION) -- UNREACHABLE, AND FOR A REASON THE REGISTRATION FIXED BEFORE THE'),
    ('### what UNDECIDED is', BANK, '### ### **AND WHAT `UNDECIDED` IS: A STATEMENT ABOUT THE RECORD, NOT ABOUT THE OBJECT.**'),
    ('### the thing no seat wrote down', BANK, '### ### ### **THE ABSCISSA WAS ALREADY CLOSED, AND HAS BEEN SINCE b326.**'),
    ('### the hook and mirror are NOT owed, checked', BANK, '### ### **NO PLACE-PAPERS FILE MOVES AND NOTHING IS FILED**'),
    ('### the shadow', BANK, '### ### **EXPECTED: NOTHING.** ### An act that reads the record and reports what the record does not hold'),
]

MUST_FAIL = [
    ('the bank never says the partition exists', BANK, '### THE PARTITION EXISTS.'),
    ('the bank never says a class is silent', BANK, '### THE CLASS IS SILENT.'),
    ('the bank never says the height is bounded', BANK, '### THE HEIGHT IS BOUNDED.'),
    ('the bank never says no finite partition exists', BANK, '### NO FINITE PARTITION EXISTS.'),
]

STATES = ('BOUNDED BY AN ARGUMENT', 'BOUNDED BY A MEASUREMENT', 'NOT BOUNDED')
COORDS = ('beta', 'gamma', 'phi', 'a')


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
    print('b351 -- GATE SUITE (A READ THAT COMPUTES NOTHING AND MOVES NOTHING)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    P = json.load(io.open(RJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()

    print(chr(10) + "  G-CEILING (the order's clauses located verbatim in the banked ferry; the act's refusals present):")
    cl = []
    for lbl, path, anchor in CEILING:
        try:
            needle_pull.pull(path, anchor)
            ok = quote_norm.contains(reg, anchor) or quote_norm.contains(bank, anchor)
            cl.append(True)
            print('    PASS  %-46s (located; carried in the act : %s)' % (lbl, ok))
        except LookupError:
            cl.append(False)
            fails.append('G-CEILING: ' + lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)
    r1 = 'NO PARTITION IS CONSTRUCTED' in bf and 'NO CLASS IS PROVED SILENT' in bf and 'NO INSTRUMENT IS WRITTEN' in bf
    r2 = 'no computation beyond the banked' in bank or 'nothing computed beyond' in bank
    gc = all(cl) and r1 and r2
    print('    the act carries all four refusals in its own words : %s / %s  %s' % (r1, r2, 'PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CEILING')

    print(chr(10) + '  G-NOCOMPUTE (STRIPPED code: the reading tool imports nothing that evaluates anything):')
    code = strip_prose(t('b351_read.py'))
    forbidden = ('b316_instrument', 'b317_smear', 'b318_square', 'b319_stable', 'b321_window', 'b326_windows',
                 'b328_family', 'b334_aimmap', 'b313f_qeps_layer', 'carto_atlas', 'noise_floor', 'numpy', 'mpmath')
    hit = [x for x in forbidden if x in code]
    imports = sorted(set(re.findall(r'^import (\w+)', code, re.M)))
    n1 = not hit
    n2 = set(imports) <= {'io', 'json', 'math', 'os', 'sys', 'needle_pull', 'quote_norm', 'run_clock'}
    gn = n1 and n2
    print('    forbidden instrument imports in the CODE : %s' % (hit or 'none'))
    print('    what it does import : %s' % imports)
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-FOURCOORD (each coordinate reported, with its range, its state and its class):')
    miss = [c for c in COORDS if c not in P['coordinates']]
    per = {c: P['coordinates'][c] for c in COORDS if c in P['coordinates']}
    f1 = not miss and len(per) == len(COORDS)
    f2 = all(('COORDINATE' in bf) for _ in [0]) and all(k in bf for k in ('THE ABSCISSA', 'THE HEIGHT', 'THE SEED'))
    f3 = all(('silent_class' in v and 'missing' in v and 'price' in v) for v in per.values())
    gf = f1 and f2 and f3
    print('    every coordinate present in the record : %s (missing %s)' % (f1, miss or 'none'))
    print('    each carries its class, its missing statement and its price slot : %s' % f3)
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FOURCOORD')

    print(chr(10) + '  G-STATE (every state is exactly one of the sealed three, spelled as sealed):')
    bad = [(c, v['state']) for c, v in per.items() if v['state'] not in STATES]
    inreg = all(s in reg for s in STATES)
    inbank = all(s in bf for s in STATES)
    gs = not bad and inreg and inbank
    for c in COORDS:
        print('      %-6s %s' % (c, per[c]['state']))
    print('    off-list states : %s ; all three sealed in the registration : %s ; all three in the bank : %s  %s'
          % (bad or 'none', inreg, inbank, 'PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-STATE')

    print(chr(10) + '  G-INSTRUMENT (the sealed distinction present, and every instrument-ceiling said to be one):')
    i1 = 'A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE' in gate_text.flat(reg)
    i2 = 'A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE' in bf
    i3 = 'THE NUMBER `150` IS WHERE THE CENSUS STOPPED' in bf and 'IT IS NOT A PROPERTY OF THE OBJECT' in bf
    i4 = 'WHICH IS TO SAY THE LOOKING IS BOUNDED AND' in bf
    gi = i1 and i2 and i3 and i4
    print('    fixed in the registration : %s ; carried in the bank : %s' % (i1, i2))
    print("    the height's bound named as the looking : %s / %s  %s" % (i3, i4, 'PASS' if gi else '### FAIL ###'))
    if not gi:
        fails.append('G-INSTRUMENT')

    print(chr(10) + '  G-QUOTE (every read located through the shared normaliser at the line the extract names):')
    n_ok, n_bad = 0, []
    for label, _coord, path, anchor in EX.READS:
        try:
            needle_pull.pull(path, anchor)
            rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
            if quote_norm.contains(extract, anchor) or (rel in extract and quote_norm.contains(extract, anchor[:60])):
                n_ok += 1
            else:
                n_bad.append(label)
        except LookupError:
            n_bad.append(label + ' (UNPULLABLE)')
    # ### THE FORMAT IS THE EXTRACT'S OWN, READ OFF THE FILE AND NOT ASSUMED: `      <path> : line <n>`.
    counted = len(re.findall(r'^ +\S+ : line \d+$', extract, re.M))
    gq = not n_bad and n_ok == len(EX.READS) and counted == len(EX.READS)
    print('    reads located at their emitting files : %d of %d ; cited lines in the extract file : %d'
          % (n_ok, len(EX.READS), counted))
    print('    %s %s' % ('PASS' if gq else '### FAIL ###', n_bad if n_bad else ''))
    if not gq:
        fails.append('G-QUOTE')

    print(chr(10) + "  G-VERDICT (the branch by (D)'s rule; both others shown unreachable, not merely unclaimed):")
    v1 = P['verdict'] == 'UNDECIDED' and 'UNDECIDED' in bf
    v2 = '(A SHAPE EXISTS) -- UNREACHABLE, AND SHOWN SO' in bf
    v3 = '(NO FINITE PARTITION) -- UNREACHABLE' in bf and 'an absence of a bound is NOT an' in bank
    v4 = sorted(P['argued']) == ['beta', 'phi'] and sorted(P['open_coords']) == ['a', 'gamma']
    gv = v1 and v2 and v3 and v4
    print('    the verdict and the bank agree : %s' % v1)
    print('    (A SHAPE EXISTS) shown unreachable : %s ; (NO FINITE PARTITION) shown unreachable : %s' % (v2, v3))
    print('    the split is exactly the two argued and the two open : %s  %s' % (v4, 'PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-VERDICT')

    print(chr(10) + "  G-PRICE (a price in the record's own printed unit; where a wall could not be had, the act says so):")
    p1 = abs(P['boxes_per_unit'] - P['boxes'] / (P['t_hi'] - P['t_lo'])) < 1e-12
    p2 = P['coordinates']['gamma']['price']['unit'] == 'boxes' and P['coordinates']['gamma']['price']['wall'] == 'NOT PRINTED BY THE RECORD'
    p3 = 'PRINTED NO WALL TIME FOR THE CENSUS' in bf.upper()
    p4 = 'UNPRICEABLE FROM BANKED FIGURES' in bf and P['coordinates']['a']['price']['unit'] is None
    p5 = '89.35' in bank and 'is not transplanted here' in bank
    gp = p1 and p2 and p3 and p4 and p5
    print('    the boxes-per-unit recomputes from the banked box grid : %s' % p1)
    print('    the unit is boxes and the wall is recorded as NOT PRINTED : %s / %s' % (p2, p3))
    print("    the width's price is UNPRICEABLE and no unit is claimed : %s" % p4)
    print("    b344's wall is named and explicitly NOT transplanted : %s  %s" % (p5, 'PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PRICE')

    print(chr(10) + '  G-NOSILENCE (the act nowhere asserts a class IS silent):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)
    s1 = 'WOULD HAVE TO BE PROVED SILENT' in bf
    s2 = 'NO CLASS IS DISCHARGED' in bf
    print('    every class named is named as one that WOULD HAVE TO BE proved silent : %s ; no class discharged : %s' % (s1, s2))
    if not (s1 and s2):
        fails.append('G-NOSILENCE')

    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        ok = quote_norm.contains(bank, anchor)
        print('    %s  %s' % ('PASS' if ok else '### FAIL (NOT FOUND)', lbl))
        if not ok:
            fails.append('SELF: ' + lbl)

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s):' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'NOT ABOUT THE OBJECT' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s ; %s' % (ROWNUM, len(rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTSHAPED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : aim-plane-coordinates returns 1 row(s)' in irun
    k2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
             ('the plane has a shape', 'no finite partition exists', 'the height is bounded', 'the classes are named'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s ; %s'
          % (k1, k2, k3, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOTSHAPED')

    print(chr(10) + '  G-APPENDONLY (banked_index.py):')
    ib = blob_of(ROOT, 'tools/banked_index.py')
    ap = True
    if ib is not None:
        old, new = norm(ib).split(chr(10)), norm(idx).split(chr(10))
        i = 0
        for ln in new:
            if i < len(old) and ln == old[i]:
                i += 1
        ap = (i == len(old))
    print('    %s' % ap)
    if not ap:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (no owner instrument; the papers repo untouched; TECHNE clean):')
    owner = ['tools/b326_offline.py', 'tools/b328_family.py', 'tools/b334_aimmap.py', 'tools/b344_ny.py',
             'tools/quote_norm.py', 'tools/run_clock.py', 'tools/gate_text.py', 'tools/needle_pull.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    tcstat = [x for x in git(TC, 'status', '--porcelain').splitlines() if x.strip()]
    gne = not touched and not ppstat and not tcstat
    print('    owner instruments modified : %s ; papers paths changed : %s ; TECHNE dirty : %s ; %s'
          % (touched or 'none', ppstat or 'none', tcstat or 'none', 'PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-NOHOOK (the papers repo does NOT move, so the hook and mirror are NOT owed -- CHECKED, not assumed):')
    h1 = not ppstat
    h2 = git(PP, 'log', '-1', '--format=%H').strip() == git(PP, 'rev-parse', 'origin/main').strip()
    h3 = 'NOT' in bf and 'OWED' in bf and 'NO PLACE-PAPERS FILE MOVES AND NOTHING IS FILED' in bf
    gh = h1 and h2 and h3
    print('    the papers working tree is clean : %s ; its HEAD equals its remote : %s' % (h1, h2))
    print('    and the bank says so in its own words : %s  %s' % (h3, 'PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-NOHOOK')

    print(chr(10) + '  G-ORDER (the seal verifies; the ordering read from clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and P['run_clock'] > stampm.group(1)
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; clock %s : %s' % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    seal < read %s : %s ; the audit JOINTLY SATISFIABLE : %s' % (P['run_clock'], o3, o4))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS:')
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    clc = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [
        ('the boxes-per-unit %.5f' % P['boxes_per_unit'], ('%.5f' % P['boxes_per_unit']) in bank),
        ('the further boxes to T = 300', str(P['boxes_to_T300']) in bank),
        # ### THE HEIGHTS ARE FLOATS IN THE RECORD AND INTEGERS IN THE PROSE; THE ARM COMPARES THE PROSE'S SHAPE.
        ('the census box grid', all(str(int(x)) in bank for x in (P['boxes'], P['t_hi']))
         and ('%.1f' % P['box_h']) in bank),
        ('the seal hash', SEAL in bank),
        ('the seal stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes sealed' % sm, ('%s bytes' % sm) in bank),
        ('%s clauses' % clc, ('%s clauses' % clc) in bank),
        ('row %s' % rn, rn == ROWNUM),
        ('the reads count', ('%d' % len(EX.READS)) in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = (all(os.path.exists(p) for p in [RRUN, CORR, IDX, EXTRACT, EXTRACT1])
            and not os.path.exists(d('b351_read_run2.txt')))
    print('    the reading ran once ; the extract ran twice and BOTH are on disk and declared : %s' % once)
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
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib2 = idx[idx.index('# ### THE PARTITION QUESTION (b351).'):idx.index("# ### THE FLOOR'S TWO HELD AXES, PRICED (b350).")] \
        if '# ### THE PARTITION QUESTION (b351).' in idx else ''
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
    tmpdir = tempfile.mkdtemp(prefix='b351_hedge_')
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
