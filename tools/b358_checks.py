# -*- coding: utf-8 -*-
"""b358_checks.py -- THE GATE SUITE FOR THE LI ASYMPTOTICS, READ UNDER A CAP.

### ### **EVERY `G-NO*` ARM READS STRIPPED CODE** (b348), ### **EVERY PRESENCE ARM READS RAW SOURCE** (b349),
### every quotation goes through `quote_norm`, and ### **EVERY ARM THAT READS A REPOSITORY STATE DECLARES ITS
### SIDE OF THE PUSH** (b352): `G-ROW`/`G-ANCESTOR` and `G-APPENDONLY` are read BEFORE THE PUSH and again
### after, and the pre-push reading is the one that carries; `G-NOEDIT` is `SIDE-INVARIANT`; ### **THIS ACT
### ### WRITES TO THE PAPERS REPO** -- the faces ledger's update block and the errata filing -- ### **SO THE
### ### HOOK AND THE MIRROR ARE OWED AND THIS SUITE CHECKS THEM.**
### ### ### **AND THE ARM THIS ACT ADDED BECAUSE b357 EARNED IT:** ### `G-ONCE` compares the run file this
### suite READS against the clock the relied-on JSON RECORDS. ### `run_clock` numbers repeats, and both the
### extract and the reading ran more than once here.
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
import reg_seal          # noqa: E402
import anchor_from_file as AF   # noqa: E402
import b358_extract as EX       # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
ERRATA = os.path.join(PP, 'ERRATA.md')
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b358_the_li_asymptotics.txt')
REG = d('b358_registration_2026-09-07.txt')
FERRY = d('b358_ferry_2026-09-07.txt')
EXTRACT = d('b358_extract_notes2.txt')          # ### **THE RELIED-ON EXTRACT.**
RUN, RJ = d('b358_read_run3.txt'), d('b358_read.json')   # ### **THE RELIED-ON READING.**
LOC, LJ = d('b358_locate_run.txt'), d('b358_locate.json')
EJ = d('b358_reads.json')
CORR = d('b358_corr_run.txt')
ERUN, FRUN = d('b358_errata_run.txt'), d('b358_faces_row_run.txt')
TERMSCAN, GATE = d('b358_reg_termscan.txt'), d('b358_reg_gate.txt')
CENSUS, FCEN = d('b358_census.txt'), d('b358_faces_census.txt')
REGSPEC, SATIS = d('b358_regspec_run.txt'), d('audit_b358_reg_satisfiable.txt')
PINS, HOOKS = d('b358_pins_stepzero.txt'), d('b358_hooks.txt')
LOCK = '8419da7b98fbb9259085dd24b5d7515d2d3ad725cf2e0b40de5ad24047ee38f7'
ROWNUM, ROWR1 = '206', '207'
EID = 'E-2026-09-07-1'
SRCTXT = ['b358_source_voros0506326.txt', 'b358_source_lagarias0404394.txt',
          'b358_source_coffey0505052.txt', 'b358_source_voros_abs0506326.txt']

OWNED = [BANK, REG, FERRY, RUN, d('b358_read_run.txt'), d('b358_read_run2.txt'), RJ, LOC, LJ, EJ,
         CORR, d('b358_index_run.txt'), d('b358_index_run2.txt'),
         ERUN, FRUN, CENSUS, FCEN, REGSPEC, SATIS, PINS, HOOKS, GATE, TERMSCAN,
         EXTRACT, d('b358_extract_notes.txt'), d('b358_satisfiable.json'), d('b358_ferry_scan.txt'),
         d('b358_faces_row.json'),
         t('b358_locate.py'), t('b358_extract.py'), t('b358_regspec.py'), t('b358_read.py'),
         t('b358_correspondence.py'), t('b358_index_check.py'), t('b358_errata.py'),
         t('b358_faces_row.py')]

NEW_THIS_ACT = {'tools/b358_locate.py', 'tools/b358_extract.py', 'tools/b358_regspec.py',
                'tools/b358_read.py', 'tools/b358_correspondence.py', 'tools/b358_index_check.py',
                'tools/b358_errata.py', 'tools/b358_faces_row.py', 'tools/b358_checks.py'}

TOOLNUM = [
    ('the reading, the grades and the verdict', 'tools/b358_read.py'),
    ('the fetch and the hashes', 'tools/b358_locate.py'),
    ('the thirty-three reads', 'tools/b358_extract.py'),
    ('the anchors, built by reading', 'tools/anchor_from_file.py'),
    ('the needle puller', 'tools/needle_pull.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('the gate flattener', 'tools/gate_text.py'),
    ('rows 206 and 207', 'tools/b358_correspondence.py'),
    ('the key, read back', 'tools/b358_index_check.py'),
    ('the errata filing (R2)', 'tools/b358_errata.py'),
    ("row U1's update block", 'tools/b358_faces_row.py'),
    ("the faces ledger's writer, IMPORTED", 'tools/b327_faces_row.py'),
    ('the registration clauses', 'tools/b358_regspec.py'),
    ('15930 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans, and the DEPRECATED arm', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('the hooks', 'tools/b304_hooks.py'),
]

SELF_HINTS = [
    ('the bank states the verdict first', 'THE ANSWER, FIRST.'),
    ('### exists but circular', 'EXISTS BUT CIRCULAR.'),
    ('### one shape, and it does not survive', 'A SHAPE EXISTS AND IT DOES NOT SURVIVE COMPONENT 3.'),
    ("### the source's own abstract", 'if (and only if) the Hypothesis is true'),
    ('### the derivation opens the same way', 'all the zeros'),
    ('### closed only under the thing being proved', 'SO THE TAIL IS CLOSED ONLY UNDER THE THING BEING PROVED'),
    ('### the split is exact', 'THE SPLIT IS EXACT.'),
    ('### the archimedean half is unconditional', 'THE ARCHIMEDEAN HALF IS UNCONDITIONAL'),
    ('### the zero half has no unconditional bound', 'THE ZERO HALF HAS NO UNCONDITIONAL BOUND AT ALL'),
    ('### what is missing is not an asymptotic', 'IS NOT AN ASYMPTOTIC. ### IT IS AN'),
    ('### the finite range, and where it stops', 'AND IT STOPS THERE'),
    ("### the deposit's attribution held", "THE DEPOSIT'S ATTRIBUTION IS CORRECT AND IS NOW PINNED"),
    ('### the two axes never merged', 'NO HYPOTHESIS CARRIES A MERGED GRADE.'),
    ('### the five undecidable on axis 2', 'THE FIVE THAT ARE `UNDECIDABLE-FROM-THE-RECORD`'),
    ('### H-NGEK, undecidable only by this cap', 'DETERMINED IS NOT COMPUTED'),
    ("### the coincidence that is the act's result", 'THAT COINCIDENCE IS THE ACT'),
    ('### the one unconditional error term', 'AND THE ONE UNCONDITIONAL ERROR TERM IN THE READING IS WORTH NAMING'),
    ("### the converse, locked in (D)", 'NOT THEREBY A CLOSURE OF THE TAIL.'),
    ('### the pricing has no index, and that is the finding', 'THE INDEX BEYOND WHICH THE LOCATED SHAPE WOULD ACT'),
    ("### b327's pin re-verified", 'RE-VERIFIED BYTE FOR BYTE'),
    ('### the source that did not fetch', 'AND ONE NOT FETCHED'),
    ('### an absence of reading, not of literature', 'NOT ### ### ### AN ABSENCE OF LITERATURE'),
    ('### the lock chain on the audit exit code', "LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK"),
    ('### ruling R1 discharged', 'THE MIS-ATTRIBUTING ROW IS CORRECTED BY AN APPEND-ONLY CORRECTION ROW.'),
    ('### ruling R2 discharged', 'THE ROUTED ERRATA ENTRY IS FILED'),
    ('### ruling R3, prospective only', 'THE VOCABULARY, PROSPECTIVE ONLY.'),
    ('### ruling R4, the lane parked', 'THE INSTRUMENT LANE IS PARKED.'),
    ('### this seat scored against itself', 'WRONG ABOUT WHERE THE CIRCULARITY'),
    ('### the shadow', 'EXPECTED: A LIBRARY SEARCH THAT WOULD EITHER FIND THE TOOL'),
]

MUST_FAIL = [
    ('the bank never says the tail is closed', BANK, '### THE TAIL IS CLOSED.'),
    ('the bank never says the hypothesis is proved', BANK, '### THE HYPOTHESIS IS PROVED.'),
    ('the bank never says the partition is decided', BANK, '### THE PARTITION IS DECIDED.'),
    ('the bank never says the literature has nothing', BANK, '### THE LITERATURE HAS NOTHING.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


# ### ### **THE NUMBERED-REPEAT CURE, GENERALISED (b356 notes2/notes3, b357 run/run2, and TWICE MORE IN
# ### ### THIS ACT).** ### `run_clock` numbers a repeat rather than overwriting, so a suite that NAMES a
# ### run file reads whichever run happened first. ### **THIS RESOLVES THE FILE BY ITS OWN RECORDED CLOCK
# ### ### AND PRINTS WHICH IT CHOSE AND WHY**, so the choice is evidence rather than a habit.
def latest_run(prefix):
    cands = []
    for f in sorted(os.listdir(D)):
        if f.startswith(prefix) and f.endswith('.txt'):
            head = io.open(d(f), encoding='utf-8', errors='replace').readline()
            m = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)', head)
            if m:
                cands.append((m.group(1), f))
    if not cands:
        return None, None, []
    cands.sort()
    return d(cands[-1][1]), cands[-1][0], cands


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
    print('b358 -- GATE SUITE (THE LI ASYMPTOTICS, READ UNDER A CAP)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    rgf = gate_text.flat(reg)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    C = json.load(io.open(RJ, encoding='utf-8'))
    E = json.load(io.open(EJ, encoding='utf-8'))
    L = json.load(io.open(LJ, encoding='utf-8'))
    S = {s['tag']: s for s in L['sources']}
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    faces = io.open(FACES, encoding='utf-8').read()
    errata = io.open(ERRATA, encoding='utf-8').read()

    print(chr(10) + '  G-CAP (STRIPPED code: the act computed nothing):')
    forbidden = ('numpy', 'scipy', 'mpmath', 'b316_instrument', 'b317_smear', 'b318_square',
                 'b319_stable', 'b322_ladder', 'b352_fit', 'quad', 'integrate')
    bad2 = []
    for tool in ('b358_read.py', 'b358_extract.py', 'b358_locate.py'):
        code = strip_prose(t(tool))
        for f in forbidden:
            if f in code:
                bad2.append((tool, f))
    c1 = not bad2
    c2 = 'THIS ACT COMPUTED NOTHING' in bf
    c3 = 'the only arithmetic is section (6)' in bank.lower() or 'THE ONLY ARITHMETIC' in bf
    gcap = c1 and c2 and c3
    print('    forbidden imports/calls in stripped code : %s' % (bad2 or 'none'))
    print('    the bank says it computed nothing : %s ; the one arithmetic labelled : %s  %s'
          % (c2, c3, 'PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + '  G-PINNED (every source quoted carries a sha-256; every one not fetched is named):')
    quoted = {'S1', 'S2'}
    p1 = all(S[k].get('sha256') and S[k]['sha256'] in bank for k in quoted)
    p2 = all(S[k].get('fetched') for k in quoted)
    notf = [k for k in S if not S[k].get('fetched')]
    p3 = all(('NOT FETCHED' in bf) for _ in notf) if notf else True
    p4 = all(S[k]['name'].split('0')[0][:6].lower() in bank.lower() for k in notf) if notf else True
    p5 = S['S2']['sha256'].startswith('86f3d3c4')     # ### the record's own b327 pin
    p6 = 'RE-VERIFIED BYTE FOR BYTE' in bf
    gp = p1 and p2 and p3 and p4 and p5 and p6
    print('    quoted sources hashed and the hash in the bank : %s ; fetched : %s' % (p1, p2))
    print('    not fetched : %s ; named in the bank with its reason : %s' % (notf or 'none', p3 and p4))
    print("    ### b327's pin re-verified (86f3d3c4...) : %s ; and the bank says so : %s  %s"
          % (p5, p6, 'PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PINNED')

    print(chr(10) + '  G-ANCHORS (every anchor built by the tool; its fixtures run; the count printed):')
    a1 = AF.self_test(False)
    a2 = E['without_anchor'] == 0 and E['anchors_differing'] > 0
    a3 = str(E['anchors_differing']) in bank and str(E['reads']) in bank
    a4 = 'AMBIGUOUS ACROSS FOUR LINES' in bf      # ### the refusals, reported because they happened
    ga = a1 and a2 and a3 and a4
    print('    fixtures hold : %s ; without a match : %d ; differing from their hint : %d of %d'
          % (a1, E['without_anchor'], E['anchors_differing'], E['reads']))
    print("    the tool's refusals during writing are reported : %s  %s"
          % (a4, 'PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ANCHORS')

    print(chr(10) + "  G-FINITERANGE (the deposit's range stated FROM THE DEPOSIT'S OWN WORDS, with where it stops):")
    try:
        n, line = AF.find(DEPOSIT, 'certifies λ_n ≥ 0 for n up to Voros')
        needle_pull.pull(DEPOSIT, line)
        f1 = True
    except (AF.AnchorError, LookupError):
        f1, n = False, 0
    f2 = 'N₀(T) ≈ 2T²' in bank or 'N_0(T) ≈ 2T²' in bank
    f3 = 'and no further' in bank and 'it is not RH' in bank
    f4 = 'AND IT STOPS THERE' in bf
    gf = f1 and f2 and f3 and f4
    print('    located at the deposited file : %s (line %d) ; the threshold in the bank : %s' % (f1, n, f2))
    print('    the deposit\'s own limiting words quoted : %s ; and where it stops, said : %s  %s'
          % (f3, f4, 'PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FINITERANGE')

    print(chr(10) + '  G-TWOAXES (every hypothesis graded TWICE; no merged grade):')
    H = C['hypotheses']
    x1 = all(('axis1' in v and 'axis2' in v) for v in H.values())
    x2 = all(v['axis1'] in C['grades'] and v['axis2'] in C['grades'] for v in H.values())
    x3 = 'NO HYPOTHESIS CARRIES A MERGED GRADE' in bf
    n_met2 = sum(1 for v in H.values() if v['axis2'] == 'MET')
    x4 = str(C['n_undecidable_axis2']) in bank and str(n_met2) in bank
    x5 = C['n_undecidable_axis2'] + n_met2 == len(H)
    gx = x1 and x2 and x3 and x4 and x5
    print('    %d hypotheses, each with two grades : %s ; every grade one of the locked three : %s'
          % (len(H), x1, x2))
    print('    the bank says none is merged : %s ; the axis-2 counts (%d MET, %d UNDECIDABLE) present : %s  %s'
          % (x3, n_met2, C['n_undecidable_axis2'], x4, 'PASS' if gx else '### FAIL ###'))
    if not gx:
        fails.append('G-TWOAXES')

    print(chr(10) + '  G-CIRCULARITY (the three questions asked of EVERY located statement, before the verdict):')
    run = io.open(RUN, encoding='utf-8').read()
    rf = gate_text.flat(run)
    st = C['statements']
    y1 = len(st) == 7 and all('circular' in s for s in st)
    y2 = all(('(D)(%-3s)' % k) in run for k in ('i', 'ii', 'iii'))
    y3 = run.index('COMPONENT 3') < run.index('COMPONENT 4')
    y4 = len(C['circular']) + len(C['clean']) == len(st)
    y5 = 'NOT THEREBY A CLOSURE OF THE TAIL' in bf
    y6 = str(len(C['circular'])) in bank and str(len(C['clean'])) in bank
    gy = y1 and y2 and y3 and y4 and y5 and y6
    print('    %d statements, each carrying its three answers : %s ; all three asked : %s' % (len(st), y1, y2))
    print('    Component 3 precedes Component 4 in the run : %s ; the split adds up : %s' % (y3, y4))
    print("    the locked converse is stated : %s ; the counts in the bank : %s  %s"
          % (y5, y6, 'PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-CIRCULARITY')

    print(chr(10) + "  G-BRANCH (the branch by (F)'s locked rule, the others shown unreachable):")
    b1 = C['verdict'] == 'EXISTS BUT CIRCULAR' and 'EXISTS BUT CIRCULAR' in bf
    b2 = '(NO USABLE ASYMPTOTICS LOCATED) -- UNREACHABLE, AND SHOWN SO' in rf
    b3 = '(A SHAPE EXISTS) -- UNREACHABLE, AND SHOWN SO' in rf
    b4 = len(C['shapes']) > 0 and len(C['clean_shapes']) == 0
    b5 = 'THE MIXTURE RULE, LOCKED BEFORE THE READING' in rf
    gb = b1 and b2 and b3 and b4 and b5
    print('    verdict agrees : %s ; both others unreachable : %s / %s' % (b1, b2, b3))
    print('    the branch conditions recompute (shapes %d, surviving %d) : %s ; mixture rule named : %s  %s'
          % (len(C['shapes']), len(C['clean_shapes']), b4, b5, 'PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BRANCH')

    print(chr(10) + '  G-NOCLOSE (no coordinate closed, no partition decided, no equivalence compiled):')
    z1 = 'NO COORDINATE IS CLOSED' in bf and 'THE PARTITION STAYS UNDECIDED' in bf
    z2 = "THE TWO FACES' EQUIVALENCE IS NOT COMPILED" in bf
    z3 = 'THE CLAUSE HAS NOT MOVED' in bf and 'NO CLASS IS DISCHARGED' in bf
    z4 = 'A STATEMENT LOCATED IS NOT A STATEMENT APPLIED' in bf
    z5 = 'NAMED-ONLY' in faces.split('## UPDATE — filed 2026-09-07 (b358)')[-1]
    gz = z1 and z2 and z3 and z4 and z5
    print('    no coordinate closed, partition undecided : %s ; no equivalence compiled : %s' % (z1, z2))
    print('    clause unmoved, no class discharged : %s ; located is not applied : %s' % (z3, z4))
    print("    and the faces block's grade is still NAMED-ONLY : %s  %s"
          % (z5, 'PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-NOCLOSE')

    print(chr(10) + "  G-LOCKCHAIN (LOCKED, on the audit's own exit code, and the block is a LOCK block):")
    k1 = "LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK" in bf
    k2 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    k3 = reg_seal.LOCKMARK in reg and reg_seal.MARK not in reg
    k4 = 'LOCKED BEFORE ANY READ' in rgf
    k5 = reg_seal.selftest(False)
    olds = ['b341', 'b345', 'b354', 'b356', 'b357']
    k6 = True
    for a in olds:
        f = [p for p in os.listdir(D) if p.startswith(a + '_registration_') and p.endswith('.txt')
             and 'SEALED_AGAINST' not in p]
        for p in f:
            txt2 = io.open(d(p), encoding='utf-8').read()
            body, banked = reg_seal.split_body(txt2)
            k6 = k6 and (banked is not None) and (reg_seal.digest(body) == banked)
    gk = k1 and k2 and k3 and k4 and k5 and k6
    print('    the bank says it : %s ; the audit is satisfiable : %s ; a LOCK block and not a seal : %s'
          % (k1, k2, k3))
    print('    locked BEFORE any read : %s ; the tool self-tests on both marks : %s' % (k4, k5))
    print('    ### **EVERY REGISTRATION SEALED BEFORE b358 STILL VERIFIES (%s) : %s**  %s'
          % (', '.join(olds), k6, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-LOCKCHAIN')

    print(chr(10) + "  G-RULINGS (R1, R2, R3, R4 -- each CHECKED, not asserted):")
    r1rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWR1)]
    row204 = [ln for ln in tbl.splitlines() if ln.startswith('| 204 |')]
    b204 = blob_of(SIDE, 'CORRESPONDENCE.md')
    r1a = len(r1rows) == 1 and 'A CORRECTION ROW, BY THE AUTHOR' in r1rows[0]
    r1b = len(row204) == 1 and (b204 is None or norm(row204[0]) in norm(b204))
    r1c = 'IT SHOULD READ b354' in r1rows[0] and 'data/b356_the_boundary.txt' in r1rows[0] \
        and 'object-or-boundary' in r1rows[0]
    R1 = r1a and r1b and r1c
    eb = blob_of(PP, 'ERRATA.md')
    r2a = errata.count(EID) == 1 and errata.count('<!-- b358 -->') == 1
    r2b = (eb is None) or norm(errata).startswith(norm(eb).rstrip(chr(10)))
    r2c = 'INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED' in errata.split('<!-- b358 -->')[-1]
    part = '## THE PARTITION'
    r2d = (eb is None) or (norm(eb).split(part)[1].split('<!-- ')[0]
                           == norm(errata).split(part)[1].split('<!-- ')[0])
    R2 = r2a and r2b and r2c and r2d
    r3a = ferry_scan.deprecated_self_test(False)
    r3b = len(ferry_scan.deprecated_scan('the registration was sealed')) == 1
    r3c = len(ferry_scan.deprecated_scan('emitted by tools/reg_seal.py; do not retype')) == 0
    scan = io.open(d('b358_ferry_scan.txt'), encoding='utf-8').read()
    r3d = 'DEPRECATED-WORDING HITS' in scan and 'NOT A HIT IN THE VERDICT' in scan
    R3 = r3a and r3b and r3c and r3d
    codes = chr(10).join(strip_prose(t(f)) for f in
                         ('b358_read.py', 'b358_extract.py', 'b358_locate.py'))
    r4a = 'Frame(' not in codes and 'both_subspaces' not in codes and 'square_trace' not in codes
    r4b = not [p for p in os.listdir(D) if p.startswith('b358_') and
               ('raised' in p or 'sixth' in p or 'frame' in p)]
    r4c = 'THE INSTRUMENT LANE IS PARKED' in bf and 'UNSCHEDULED AND NOT BUILT' in bf
    r4d = not os.path.exists(t('arm_anchor.py'))
    R4 = r4a and r4b and r4c and r4d
    gr = R1 and R2 and R3 and R4
    print('    R1 : correction row present once %s ; ROW 204 BYTE-IDENTICAL TO ITS BLOB %s ; cites bank+key %s'
          % (r1a, r1b, r1c))
    print('    R2 : %s filed once %s ; ERRATA append-only %s ; placed by its own words %s ; PARTITION BLOCK UNCHANGED %s'
          % (EID, r2a, r2b, r2c, r2d))
    print('    R3 : deprecated fixtures %s ; fires on the retired use %s ; quiet on the tool name %s ; reported and excluded %s'
          % (r3a, r3b, r3c, r3d))
    print('    R4 : NO FRAME RECOMPUTED -- no instrument import %s, no frame artefact %s, said parked %s, helper not built %s'
          % (r4a, r4b, r4c, r4d))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RULINGS')

    print(chr(10) + "  SELF NEEDLES (each hint resolved to the bank's own line by the step-zero tool):")
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
    nb2 = 0
    for label, tag, path, hint in EX.READS:
        try:
            _n, line = AF.find(path, hint)
            needle_pull.pull(path, line)
            if not quote_norm.contains(extract, line.rstrip()[:200]):
                nb2 += 1
                print('    ### FAIL (NOT IN THE EXTRACT)  %s' % label)
        except (AF.AnchorError, LookupError):
            nb2 += 1
            print('    ### FAIL (NO ANCHOR)  %s' % label)
    cited = len(re.findall(r'^ +\S+ : line \d+ ', extract, re.M))
    print('    reads %d ; all located and in the extract : %s ; cited lines : %d'
          % (len(EX.READS), nb2 == 0, cited))
    if nb2:
        fails.append('G-EXTRACT')

    print(chr(10) + '  G-ROW / G-ANCESTOR (rows %s and %s). ### **PRE-PUSH READING CARRIES.**' % (ROWNUM, ROWR1))
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    anc = (b204 is not None) and norm(tbl).startswith(norm(b204).rstrip(chr(10)))
    grow = (len(rows) == 1 and len(r1rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'CIRCULAR IN ITS OWN SOURCE' in rows[0] and anc)
    print('    both rows present once : %s ; true prefix of its blob : %s ; %s'
          % (len(rows) == 1 and len(r1rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTCLOSED (the index):')
    IDX, iclock, icands = latest_run('b358_index_run')
    print('    ### the index run is RESOLVED BY ITS OWN CLOCK, not named : %s of %s'
          % (os.path.basename(IDX) if IDX else 'none', [c[1] for c in icands]))
    irun = io.open(IDX, encoding='utf-8').read()
    k_1 = 'READ BACK : li-asymptotics-circular returns 1 row(s), 1 required  PASS' in irun
    k_2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
              ('the tail is closed', 'the asymptotic is unconditional', 'RH is proved',
               'the coordinate is closed'))
    k_3 = '  ### PASS' in irun
    gkey = k_1 and k_2 and k_3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s ; %s'
          % (k_1, k_2, k_3, 'PASS' if gkey else '### FAIL ###'))
    if not gkey:
        fails.append('G-KEY')

    print(chr(10) + '  G-APPENDONLY (banked_index.py, FACES_LEDGER.md, ERRATA.md). ### **READ BEFORE THE PUSH.**')
    ap = True
    for repo, rel, cur in ((ROOT, 'tools/banked_index.py', idx), (PP, 'FACES_LEDGER.md', faces),
                           (PP, 'ERRATA.md', errata)):
        b = blob_of(repo, rel)
        one = True
        if b is not None:
            old, new = norm(b).split(chr(10)), norm(cur).split(chr(10))
            i = 0
            for ln in new:
                if i < len(old) and ln == old[i]:
                    i += 1
            one = (i == len(old))
        print('    %-28s every committed line still present, in order : %s' % (rel, one))
        ap = ap and one
    if not ap:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (no owner instrument edited beyond the ruling\'s additive modes). ### SIDE-INVARIANT.')
    owner = ['tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py',
             'tools/b319_stable.py', 'tools/b320_run.py', 'tools/b352_fit.py', 'tools/quote_norm.py',
             'tools/run_clock.py', 'tools/gate_text.py', 'tools/registration_gate.py',
             'tools/anchor_from_file.py', 'tools/needle_pull.py', 'tools/b327_faces_row.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    additive = ['tools/reg_seal.py', 'tools/ferry_scan.py']
    changed_add = [p for p in additive if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    tcstat = [x for x in git(TC, 'status', '--porcelain').splitlines() if x.strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip()
              and 'BLOB_SENSITIVITY' not in x]
    ppexp = sorted(x.split()[-1] for x in ppstat)
    gne = (not touched) and (not tcstat) and ppexp == ['ERRATA.md', 'FACES_LEDGER.md']
    print('    owner instruments modified : %s ; TECHNE dirty : %s' % (touched or 'none', tcstat or 'none'))
    print('    ### the two ADDITIVE tools under R3 : %s' % (changed_add or 'none'))
    print('    papers dirty, and ONLY the two files this act writes : %s  %s'
          % (ppexp, 'PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so BOTH ARE OWED):')
    hookp, mirrorp = HOOKS, d('b358_mirror.txt')
    gh = os.path.exists(hookp)
    if gh:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        print('    hook: 0 repos failing, all three byte-identical : %s' % h_ok)
        gh = h_ok
    else:
        print('    ### the hook record is NOT YET WRITTEN.')
    if os.path.exists(mirrorp):
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        print('    mirror: clean on all three clauses : %s' % m_ok)
        gh = gh and m_ok
    else:
        print('    ### the mirror record is NOT YET WRITTEN (it is written AFTER the push).')
        gh = False
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed)')

    print(chr(10) + '  G-ORDER (the lock verifies; the ordering read from clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (LOCK in reg)
    body, banked = reg_seal.split_body(reg)
    o1 = o1 and (reg_seal.digest(body) == LOCK == banked)
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and stampm.group(1) < L['run_clock'] < E['run_clock'] < C['run_clock']
    o4 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    go = o1 and o2 and o3 and o4
    print('    the lock recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    ### **LOCK %s < fetch %s < extract %s < reading %s** : %s'
          % (stampm.group(1) if stampm else '?', L['run_clock'], E['run_clock'], C['run_clock'], o3))
    print('    JOINTLY SATISFIABLE : %s  %s' % (o4, 'PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS:')
    sm = re.search(r'### bytes locked : (\d+)', reg).group(1)
    clc = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks = [('the lock hash', LOCK in bank),
              ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
              ('%s bytes locked' % sm, ('%s bytes' % sm) in bank),
              ('%s clauses' % clc, ('%s clauses' % clc) in bank),
              ('rows %s and %s' % (ROWNUM, ROWR1), bool(rows) and bool(r1rows)),
              ('the four clocks', all(x in bank for x in
                                      (stampm.group(1) if stampm else 'x', L['run_clock'],
                                       E['run_clock'], C['run_clock']))),
              ('the reads and the differing anchors',
               str(E['reads']) in bank and str(E['anchors_differing']) in bank),
              ('the statement counts', str(len(C['statements'])) in bank
               and str(len(C['circular'])) in bank and str(len(C['clean'])) in bank),
              ('the axis-2 counts', str(C['n_undecidable_axis2']) in bank and str(n_met2) in bank),
              ('the pricing ratio', ('%.2e' % C['price_ratio']) in bank),
              ("the pricing's two banked counts",
               str(C['price']['computed_to']) in bank and '1e+18' in bank)]
    for k in ('S1', 'S2', 'S3'):
        checks.append(('%s hash and bytes' % S[k]['name'],
                       (S[k]['sha256'] in bank or S[k]['sha256'][:16] in bank)))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the RELIED-ON run files identified by their own clocks):')
    q1 = C['run_clock'] in io.open(RUN, encoding='utf-8').readline()
    q2 = E['run_clock'] in io.open(EXTRACT, encoding='utf-8').readline()
    q3 = os.path.basename(RUN) in bank and os.path.basename(EXTRACT) in bank
    q4 = os.path.exists(d('b358_read_run.txt')) and os.path.exists(d('b358_read_run2.txt'))
    q5 = 'SUPERSEDED AND KEPT UNEDITED' in bf
    q6 = (IDX is not None) and iclock == max(c[0] for c in icands)
    once = q1 and q2 and q3 and q4 and q5 and q6
    print('    the reading file carries the relied-on JSON clock %s : %s' % (C['run_clock'], q1))
    print('    the extract file carries its JSON clock %s : %s' % (E['run_clock'], q2))
    print('    both named in the bank : %s ; the repeats kept : %s ; the superseded one declared : %s'
          % (q3, q4, q5))
    print('    ### the index run resolved to the newest of %d by clock : %s  %s'
          % (len(icands), q6, 'PASS' if once else '### FAIL ###'))
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

    marker = '# ### THE LI ASYMPTOTICS, READ UNDER A CAP (b358).'
    nxt = '# ### WHAT THE LEDGERS SAY THE CHECKS CERTIFY (b357).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if marker in idx and nxt in idx else ''
    fb2 = faces.split('## UPDATE — filed 2026-09-07 (b358)')[-1] if '(b358)' in faces else ''
    eb2 = errata.split('<!-- b358 -->')[-1] if '<!-- b358 -->' in errata else ''
    print(chr(10) + '  G-STEM-APPENDED:')
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''),
                      ('row %s (R1)' % ROWR1, r1rows[0] if r1rows else ''),
                      ('the index row', ib2), ('the faces block', fb2), ('the errata entry', eb2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
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
    tmpdir = tempfile.mkdtemp(prefix='b358_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''),
                      ('row %s (R1)' % ROWR1, r1rows[0] if r1rows else ''),
                      ('the index row', ib2), ('the faces block', fb2), ('the errata entry', eb2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_').replace('(', '').replace(')', '') + '.txt')
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
