# -*- coding: utf-8 -*-
"""b355_checks.py -- THE GATE SUITE FOR WHAT THE ARRAYS ARE.

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
import b355_extract as EX       # noqa: E402

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


BANK = d('b355_what_the_arrays_are.txt')
REG = d('b355_registration_2026-09-07.txt')
FERRY = d('b355_ferry_2026-09-07.txt')
EXTRACT = d('b355_extract_notes3.txt')
RUN, RJ = d('b355_read_run2.txt'), d('b355_read.json')
FJ = d('b355_reads.json')
CORR, IDX = d('b355_corr_run.txt'), d('b355_index_run.txt')
TERMSCAN, GATE = d('b355_reg_termscan.txt'), d('b355_reg_gate.txt')
CENSUS, FCEN = d('b355_census.txt'), d('b355_faces_census.txt')
REGSPEC, SATIS = d('b355_regspec_run.txt'), d('audit_b355_reg_satisfiable.txt')
PINS = d('b355_pins_stepzero.txt')
SEAL = '582934274b47bae1ac72dced2abd448a5065c24aaafca88b9585db562abf49c2'
ROWNUM = '203'
TERMS = ('USED THE SCAN', 'USED THE EQUIVALENCE', 'USED BOTH', 'USED NEITHER')

OWNED = [BANK, REG, FERRY, RUN, RJ, FJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, GATE, TERMSCAN,
         EXTRACT, d('b355_extract_notes.txt'), d('b355_extract_notes2.txt'), d('b355_read_run.txt'),
         d('b355_satisfiable.json'), d('b355_ferry_scan.txt'),
         t('b355_extract.py'), t('b355_regspec.py'), t('b355_read.py'),
         t('b355_correspondence.py'), t('b355_index_append.py')]

NEW_THIS_ACT = {'tools/b355_extract.py', 'tools/b355_regspec.py', 'tools/b355_read.py',
                'tools/b355_correspondence.py', 'tools/b355_index_append.py', 'tools/b355_checks.py'}

TOOLNUM = [
    ('the three layers, the checks and the verdict', 'tools/b355_read.py'),
    ('the anchors, built by reading', 'tools/anchor_from_file.py'),
    ('the reads', 'tools/b355_extract.py'),
    ('the generating formula, READ', 'tools/e16/carto_atlas.py'),
    ('the object integrated, READ', 'tools/b317_smear.py'),
    ('the scan and its stated reach, READ', 'tools/b318_square.py'),
    ('the aliasing consequence, READ', 'tools/b326_closure.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 203', 'tools/b355_correspondence.py'),
    ('the key', 'tools/b355_index_append.py'),
    ('35 clauses', 'tools/b355_regspec.py'),
    ('14242 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

SELF_HINTS = [
    ('the bank states the verdict first', 'THE RECORD STATES IT, AND `b353` DID NOT LOOK AT THE LINE'),
    ('### the one-sentence answer', 'THE CORPUS INTEGRATES A PIECEWISE-LINEAR INTERPOLANT OF A SAMPLED SMOOTH BUMP'),
    ('### layer 1, the smooth formula', 'THE TEXTBOOK `Cc^infty` BUMP'),
    ('### layer 2, the trapezoid normalisation', 'SO THE NORMALISING CONSTANT IS THE PIECEWISE-LINEAR INTEGRAL'),
    ('### layer 3, and the reason', 'THE CHOICE WAS MADE FOR INTERNAL CONSISTENCY WITH BANKED NUMBERS'),
    ('### H1 answered on its own', 'SO THE OBJECT INTEGRATED IS NOT IN THE CLASS THE EQUIVALENCE QUANTIFIES OVER'),
    ('### and what does not follow', 'NOTHING HERE SAYS THE TWO GIVE'),
    ('### H3 is a different question', "AND HERE IS WHY THE ORDER WAS RIGHT TO SEPARATE THE TWO:"),
    ('### the automatic positivity', 'positivity is ### **AUTOMATIC.**'),
    ('### the scan is not an independent class test', 'NOT AN INDEPENDENT TEST OF CLASS'),
    ('### the control that keeps it from being vacuous', 'AND THE CONTROL THAT KEEPS IT FROM BEING VACUOUS'),
    ('### no act tested membership independently', 'NO ACT IN THIS FAMILY EVER TESTED CLASS MEMBERSHIP'),
    ('### the branch, and the fourth outcome', 'AND THIS IS THE FOURTH OUTCOME THE REGISTRATION ANTICIPATED'),
    ('### a relabelling and not a demotion', 'A RELABELLING AND NOT A DEMOTION.** ### **EVERY BANKED NUMBER STANDS'),
    ('### the two readings, old and new', 'THE SECOND IS NARROWER AND IT IS TRUE. ### THE FIRST WAS NEVER MEASURED'),
    ('### no errata drafted, and why', 'NO ERRATA ENTRY IS DRAFTED'),
    ('### confirm and not strengthen', "CONFIRMS b353'S SENTENCE AND DOES NOT STRENGTHEN IT"),
    ('### the dropped-possessive species', 'A DROPPED POSSESSIVE IS A CHANGED WORD'),
    ('### the thing no seat wrote down', 'THE SCAN AND THE CONSTRUCTION WERE NEVER INDEPENDENT'),
    ('### the shadow', 'EXPECTED: A SMALL BOOKKEEPING ANSWER'),
]

MUST_FAIL = [
    ('the bank never says the arrays are in the class', BANK, '### THE ARRAYS ARE IN THE CLASS.'),
    ('the bank never says the arrays are not in the class', BANK, '### THE ARRAYS ARE NOT IN THE CLASS.'),
    ('the bank never says a measurement is wrong', BANK, '### A MEASUREMENT IS WRONG.'),
    ('the bank never says the width coordinate is closed', BANK, '### THE WIDTH COORDINATE IS CLOSED.'),
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
    print('b355 -- GATE SUITE (A READ THAT MOVES NOTHING)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    P = json.load(io.open(RJ, encoding='utf-8'))
    F = json.load(io.open(FJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()

    print(chr(10) + '  G-ANCHORS (the step-zero tool built every anchor, its fixtures hold, the refusals reported):')
    a1 = AF.self_test(False)
    a2 = F['without_anchor'] == 0 and F['anchors_differing'] > 0
    a3 = str(F['anchors_differing']) in bank and str(F['reads']) in bank
    a4 = 'EVERY ONE WAS A DROPPED POSSESSIVE' in bf
    ga = a1 and a2 and a3 and a4
    print('    fixtures hold : %s ; anchors without a match : %d ; differing from their hint : %d of %d'
          % (a1, F['without_anchor'], F['anchors_differing'], F['reads']))
    print('    the counts in the bank : %s ; the refusal species named : %s  %s'
          % (a3, a4, 'PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ANCHORS')

    print(chr(10) + '  G-SEPARATE (H1 and H3 in their own sections, neither stated in terms of the other):')
    e1 = '### (2) `H1`, ANSWERED ON ITS OWN' in bank
    e2 = '### (3) `H3`, ANSWERED ON ITS OWN' in bank
    e3 = 'AN ANSWER TO' in bf and 'EITHER SETTLES NOTHING ABOUT THE OTHER' in bf
    e4 = ('H1` fails because of WHAT' in bf and 'H3` is undecided because of HOW FAR THE LOOKING WENT' in bf)
    ge = e1 and e2 and e3 and e4
    print('    H1 has its own section : %s ; H3 has its own : %s' % (e1, e2))
    print('    the reason for keeping them apart present : %s / %s  %s' % (e3, e4, 'PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-SEPARATE')

    print(chr(10) + '  G-LAYERS (three layers named, each located at an emitting line):')
    layers = P['layers']
    l1 = len(layers) == 3
    l2 = all(x.upper().split()[-1] in bf for x in ('the generating formula', 'the sampled array', 'the object integrated'))
    l3 = ('carto_atlas.py:49' in bank and 'b317_smear.py:136' in bank)
    l4 = 'THESE THREE CAN DIFFER' in gate_text.flat(reg)
    gl = l1 and l2 and l3 and l4
    print('    three layers recorded : %s ; each named in the bank : %s' % (l1, l2))
    print('    emitting lines cited : %s ; the separation sealed in the registration : %s  %s'
          % (l3, l4, 'PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LAYERS')

    print(chr(10) + '  G-EACHCHECK (every check classified by the sealed vocabulary and by no other):')
    checks = P['checks']
    c1 = len(checks) >= 5
    bad_terms = [c for c in checks if c['used'] not in TERMS]
    c2 = not bad_terms
    c3 = all(c['certifies'].strip() for c in checks)
    c4 = all(term in reg for term in TERMS)
    for c in checks:
        print('      %-28s %-22s %s' % (c['act'][:28], c['used'], c['what'][:44]))
    gce = c1 and c2 and c3 and c4
    print('    checks classified : %d ; off-vocabulary : %s ; each says what it certifies : %s  %s'
          % (len(checks), bad_terms or 'none', c3, 'PASS' if gce else '### FAIL ###'))
    if not gce:
        fails.append('G-EACHCHECK')

    print(chr(10) + '  G-RELABEL (a relabelling is not a demotion, in the act\'s own words):')
    r1 = 'A RELABELLING AND NOT A DEMOTION' in bf
    r2 = 'EVERY BANKED NUMBER STANDS' in bf and 'EVERY CHECK THAT PASSED STILL PASSED' in bf
    r3 = 'A CHECK THAT CERTIFIES SOMETHING NARROWER' in gate_text.flat(reg)
    r4 = 'THE FIRST WAS NEVER MEASURED' in bf
    gr = r1 and r2 and r3 and r4
    print('    stated in the bank : %s ; numbers and checks stand : %s' % (r1, r2))
    print('    sealed in the registration : %s ; the two readings given : %s  %s'
          % (r3, r4, 'PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RELABEL')

    print(chr(10) + '  G-NOMOVE (the act moves no verdict, and says so):')
    m1 = 'NO VERDICT IS MOVED BY THIS ACT' in bf
    m2 = 'THAT IS A READING AND THE' in bf and 'AUTHOR MOVES ROWS' in bf
    m3 = P['errata'].startswith('NOT DRAFTED')
    m4 = 'NO ERRATA ENTRY IS DRAFTED' in bf
    gm = m1 and m2 and m3 and m4
    print('    says no verdict is moved : %s ; routes rather than applies : %s' % (m1, m2))
    print('    no errata drafted, recorded and stated : %s / %s  %s' % (m3, m4, 'PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-NOMOVE')

    print(chr(10) + '  G-CONFIRMNOTSTRENGTHEN (where it confirms b353, it says it does not strengthen):')
    n1 = 'CONFIRMS b353' in bf and 'DOES NOT STRENGTHEN IT' in bf
    n2 = 'confirmed and not' in bf and 'strengthened' in bf
    n3 = "STAYS `UNDECIDED`" in bank or 'STAYS UNDECIDED' in bf
    gcn = n1 and n2 and n3
    print('    said in the act : %s / %s ; the partition still UNDECIDED : %s  %s'
          % (n1, n2, n3, 'PASS' if gcn else '### FAIL ###'))
    if not gcn:
        fails.append('G-CONFIRMNOTSTRENGTHEN')

    print(chr(10) + '  G-NOCOMPUTE (STRIPPED code: the read tool imports nothing that could compute):')
    code = strip_prose(t('b355_read.py'))
    forbidden = ('numpy', 'scipy', 'b316_instrument', 'b317_smear', 'b318_square', 'b319_stable',
                 'b326_windows', 'b328_family', 'b334_aimmap', 'b352_fit', 'carto_atlas')
    hit = [x for x in forbidden if x in code]
    imports = sorted(set(re.findall(r'^import (\w+)', code, re.M)))
    gnc = (not hit) and set(imports) <= {'io', 'json', 'os', 'sys', 'needle_pull', 'quote_norm',
                                        'run_clock', 'anchor_from_file'}
    print('    forbidden imports in the CODE : %s ; what it does import : %s  %s'
          % (hit or 'none', imports, 'PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + "  G-BRANCH (the branch by (C)'s rule; the branches not taken shown unreachable):")
    v1 = P['verdict'] == 'THE RECORD STATES IT' and 'THE RECORD STATES IT' in bf
    v2 = '(THE RECORD DOES NOT STATE IT) -- UNREACHABLE' in bf
    v3 = '(THE RECORD CONTRADICTS ITSELF) -- UNREACHABLE' in bf
    v4 = 'THE FOURTH OUTCOME THE REGISTRATION ANTICIPATED' in bf
    gv = v1 and v2 and v3 and v4
    print('    verdict agrees : %s ; both others unreachable : %s / %s ; the fourth outcome named : %s  %s'
          % (v1, v2, v3, v4, 'PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-BRANCH')

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
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'RELABELLING' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s ; %s'
          % (ROWNUM, len(rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTDEMOTED (the index):')
    irun = io.open(IDX, encoding='utf-8').read()
    k_1 = 'READ BACK : what-the-arrays-are returns 1 row(s)' in irun
    k_2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
              ('a measurement is wrong', 'the arrays are in the class', 'the corpus chose badly', 'the verdicts are withdrawn'))
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
    o3 = (stampm is not None) and F['run_clock'] < stampm.group(1) < P['run_clock']
    o4 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    extract %s < seal < read %s : %s ; JOINTLY SATISFIABLE : %s'
          % (F['run_clock'], P['run_clock'], o3, o4))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS:')
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    clc = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    nchecks = [('the seal hash', SEAL in bank),
               ('the seal stamp', (stampm.group(1) if stampm else 'x') in bank),
               ('%s bytes sealed' % sm, ('%s bytes' % sm) in bank),
               ('%s clauses' % clc, ('%s clauses' % clc) in bank),
               ('row %s' % rn, rn == ROWNUM),
               ('the extract and read clocks', F['run_clock'] in bank and P['run_clock'] in bank),
               ('the anchors differing', str(F['anchors_differing']) in bank),
               ('the reads attempted', str(F['reads']) in bank)]
    checks = nchecks
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the numbered repeats on disk AND declared):')
    once = (os.path.exists(d('b355_extract_notes.txt')) and os.path.exists(EXTRACT)
            and os.path.exists(d('b355_read_run.txt')) and os.path.exists(RUN)
            and 'THE EXTRACT RAN THREE TIMES AND ALL THREE RUN FILES ARE ON DISK' in bf
            and 'THE READ RAN TWICE' in bf)
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

    ib2 = idx[idx.index('# ### WHAT THE ARRAYS ARE (b355).'):idx.index('# ### THE SIXTH FRAME (b354).')] \
        if '# ### WHAT THE ARRAYS ARE (b355).' in idx else ''
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
    tmpdir = tempfile.mkdtemp(prefix='b355_hedge_')
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
