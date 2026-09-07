# -*- coding: utf-8 -*-
"""b349_checks.py -- THE GATE SUITE FOR THE ROOM, RELATIVE BEFORE EXTENDED.

### ### **THIS SUITE IMPORTS `quote_norm` -- THE SORTIE'S OWN STEP-ZERO BUILD -- FOR EVERY QUOTATION COMPARISON, AND
### ### IS THE FIRST SUITE TO DO SO.** ### That is the whole point of building it: the emitter and its checker use
### one normaliser, so a comparison is about the content and not about the normalisation.
### ### **AND EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE**, which is b348's minted rule applied here.
### ### **THE ARMS (registration section (G)):** `G-NORM`, `G-CITE`, `G-RATIO`, `G-ROWS`, `G-READ`, `G-COND`,
### `G-ROW`, `G-KEY` / `G-NOTEXPLAINED`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`, `G-PAPERS`, `G-NUMBERS`,
### `G-TOOLNUM`, `G-ONCE`, the sweeps, `G-SHARED`, the hedge audit, the must-fail fixtures; re-run after the push.
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
import quote_norm        # noqa: E402  ### THE SORTIE'S SHARED NORMALISER -- both sides of every comparison
import noise_floor as NF  # noqa: E402

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


BANK = d('b349_the_room_relative.txt')
REG = d('b349_registration_2026-09-07.txt')
FERRY = d('b349_ferry_2026-09-07.txt')
EXTRACT = d('b349_extract_notes.txt')
ARUN, AJ = d('b349_relative_run.txt'), d('b349_relative.json')
BRUN, BJ = d('b349_extend_run.txt'), d('b349_extend.json')
CORR, IDX = d('b349_corr_run.txt'), d('b349_index_run.txt')
SCAN, TERMSCAN, GATE = d('b349_ferry_scan.txt'), d('b349_reg_termscan.txt'), d('b349_reg_gate.txt')
CENSUS, FCEN = d('b349_census.txt'), d('b349_faces_census.txt')
REGSPEC, SATIS = d('b349_regspec_run.txt'), d('audit_b349_reg_satisfiable.txt')
PINS, INDEXQ = d('b349_pins_stepzero.txt'), d('audit_b349_index_query.txt')
SEAL = 'e850113882a668fb68f1daaeea3ee3d6802ea8ca8aa4e136ccf9c6112b8192ab'
ROWNUM = '197'

OWNED = [BANK, REG, FERRY, ARUN, AJ, BRUN, BJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         TERMSCAN, EXTRACT, d('b349_satisfiable.json'),
         t('b349_extract.py'), t('b349_regspec.py'), t('b349_relative.py'), t('b349_extend.py'),
         t('b349_correspondence.py'), t('b349_index_append.py'), t('quote_norm.py')]

CARRIERS = [
    (t('b349_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]
NEW_THIS_ACT = {'tools/b349_extract.py', 'tools/b349_regspec.py', 'tools/b349_relative.py', 'tools/b349_extend.py',
                'tools/b349_correspondence.py', 'tools/b349_index_append.py', 'tools/b349_checks.py',
                'tools/quote_norm.py'}

TOOLNUM = [
    ('the relative measure, the minima and the flatness', 'tools/b349_relative.py'),
    ('the seed checks and the extended grid', 'tools/b349_extend.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ('the seed builder and the quantities, IMPORTED', 'tools/b334_aimmap.py'),
    ('lawfulness and the transform, IMPORTED', 'tools/b328_family.py'),
    ('the gate on every sign', 'tools/noise_floor.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 197', 'tools/b349_correspondence.py'),
    ('the key', 'tools/b349_index_append.py'),
    ('30 clauses', 'tools/b349_regspec.py'),
    ('18895 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('b298 -- the comparison that normalised the difference away', d('b298_the_boundary_terminal.txt'),
     '### the BOM), and the comparison against `git HEAD` was ### LINE-CONTENT ### , which normalises'),
    ('b309 -- a CRLF working file against an LF blob', d('b309_the_scaling_trace.txt'),
     '###   ### **(ii) IT COMPARED A CRLF WORKING FILE AGAINST AN LF BLOB.** ### `core.autocrlf` rewrites'),
    ('b309 -- both sides through one IMPORTED normaliser', d('b309_the_scaling_trace.txt'),
     '###     TO WRITE.** ### Both sides are now normalised through `b302_kernel.normalise`, IMPORTED and'),
    ('b348 -- the quotation half, the gate that refused', d('b348_the_fold.txt'),
     '### ### **AND THE GATE REFUSED ONCE BEFORE IT PASSED**'),
    ("b343 -- a minimum at the interval's edge", d('b343_the_maps_next_reach.txt'),
     "### **AND ONE OF THE TWO MINIMA SITS AT THE INTERVAL'S EDGE:** at `a = 40` it is interior (`gamma = 2.0`"),
    ('b344 -- a finer chart and not a trend', d('b344_the_floor_priced.txt'),
     'A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND'),
    ("b348 -- the located point of maximum tension", d('b348_the_fold.txt'),
     '### **THE LOCATED POINT OF MAXIMUM TENSION.**'),
    ('the order -- step zero, the shared normaliser', FERRY,
     'STEP ZERO, this sortie only: one shared normaliser, imported by'),
    ('the order -- leg 1', FERRY, 'LEG 1 (b349) \u2014 THE ROOM, RELATIVE BEFORE EXTENDED.'),
    ('the order -- a degenerate seed is reported, not charted', FERRY,
     'degenerate seed is reported as degenerate, not charted.'),
]

SELF_NEEDLES = [
    ('the bank states the survival first', BANK,
     '### ### ### **THE MINIMUM SURVIVES THE RELATIVE MEASURE, AT BOTH REACHING WIDTHS.**'),
    ('### not an artifact of absolute measurement', BANK,
     '### ### MEASUREMENT**, and the sentence this act was registered to be able to write instead is not written.'),
    ('### the relative measure is flatter', BANK, '### ### ### **AND THE RELATIVE MEASURE IS FLATTER, AT BOTH WIDTHS.**'),
    ('### the halves point opposite ways', BANK, '### ### ### WAYS:** the relative room ### IS ### flatter, as expected -- and the low-height minimum does'),
    ('### weaker than either being right', BANK, '### ### EITHER BEING RIGHT**, and the registration said so before the figures existed.'),
    ('### the normaliser is not retroactive', BANK, '### its own act\'s normalisation and ### **NOTHING IS RE-VERDICTED BY IT.**'),
    ('### nothing was manufactured', BANK, '### ### INCIDENT THIS SEAT COULD LOCATE, AND NONE WAS MANUFACTURED.**'),
    ('### the floor rule fired on nothing', BANK, '### ### **THE FLOOR RULE FIRED ON NOTHING:**'),
    ('### no seed degenerate, and the seat was wrong', BANK,
     '### ### SEAT EXPECTED AT LEAST ONE DEGENERATE SEED AND WAS WRONG.**'),
    ('### a local feature, not a descent', BANK, '### **THAT IS A LOCAL FEATURE AT ONE HEIGHT, NOT A DESCENT**, and'),
    ('### (E1) a run that left no record', BANK, '### ### **(E1) A RUN HAPPENED AND LEFT NO RECORD, AND WAS RE-RUN IN FULL.**'),
    ('### (E2) the order\'s citation', BANK, '### ### **(E2) THE ORDER\'S CITATION OF THE SPECIES DID NOT MATCH THE RECORD, AND THE ACT SAYS SO RATHER'),
    ('### the hook and mirror are not owed', BANK, '### ### **NOTHING IN THE PAPERS REPO. ### NO LEDGER ROW MOVED, SO THE HOOK AND THE MIRROR ARE NOT OWED.**'),
    ('### the shadow', BANK, '### ### **EXPECTED: NOTHING.** ### A second measure of the same figures is a second measure.'),
]

MUST_FAIL = [
    ('the bank never says the room closes', BANK, '### THE ROOM CLOSES.'),
    ('the bank never claims a crossing', BANK, '### A CROSSING IS CLAIMED.'),
    ('the bank never says the construction never degenerates', BANK, '### THE CONSTRUCTION NEVER DEGENERATES.'),
    ('the bank never calls the relative measure the right one', BANK, '### THE RELATIVE MEASURE IS THE RIGHT ONE.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def strip_prose(path):
    """### THE SOURCE WITH COMMENTS AND STRING LITERALS REMOVED -- b348's minted rule, applied here."""
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
    print('b349 -- GATE SUITE (A SECOND MEASURE, THREE NEW HEIGHTS, AND ONE SHARED NORMALISER)')
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = quote_norm.contains(extract, anchor)   # ### THROUGH THE SHARED NORMALISER
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
    A = json.load(io.open(AJ, encoding='utf-8'))
    B = json.load(io.open(BJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    arun = io.open(ARUN, encoding='utf-8').read()
    brun = io.open(BRUN, encoding='utf-8').read()

    print(chr(10) + '  G-NORM (the shared normaliser exists, is IMPORTED by both sides, its fixtures hold, its reach stated):')
    n1 = quote_norm.self_test(verbose=False)
    own = strip_prose(t('b349_checks.py'))
    n2 = 'quote_norm' in own and 'quote_norm.contains' in io.open(t('b349_checks.py'), encoding='utf-8').read()
    qsrc = io.open(t('quote_norm.py'), encoding='utf-8').read()
    n3 = ('IT DOES NOT MAKE A QUOTATION TRUE' in qsrc and 'NOT RETROACTIVE' in qsrc
          and 'NOTHING IS RE-VERDICTED BY THIS FILE' in qsrc)
    n4 = 'def contains(' in qsrc and 'norm(needle) in norm(haystack)' in qsrc
    gn = n1 and n2 and n3 and n4
    print('    its fixtures hold, negative arms included : %s ; this suite imports it and uses it : %s' % (n1, n2))
    print('    its reach stated in its own header : %s ; `contains` normalises BOTH sides : %s' % (n3, n4))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORM')

    print(chr(10) + "  G-CITE (the order's citation checked against the record, not accepted):")
    c1 = 'b305' in bf and 'NONE WAS MANUFACTURED' in bf
    c2 = quote_norm.contains(extract, '### the BOM), and the comparison against `git HEAD` was ### LINE-CONTENT ### , which normalises')
    c3 = quote_norm.contains(extract, 'Both sides are now normalised through `b302_kernel.normalise`, IMPORTED and')
    c4 = 'b298' in bank and 'b309' in bank and 'b348' in bank
    gc = c1 and c2 and c3 and c4
    print('    the bank names b305 and says nothing was manufactured : %s' % c1)
    print('    b298 and b309 located in the extract : %s / %s ; all three named in the bank : %s' % (c2, c3, c4))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CITE')

    print(chr(10) + '  G-RATIO (the sealed denominator, the same everywhere; the floor stated; non-RESOLVED rows excluded):')
    bad = []
    for r in A['table']:
        den = max(abs(r['arch_z']), abs(r['prime_z']))
        if abs(r['den_z'] - den) > 1e-12 * max(1.0, den):
            bad.append((r['a'], r['gamma']))
        if abs(r['rel_z'] * r['den_z'] - r['places_z']) > 1e-9 * max(1.0, r['places_z']):
            bad.append((r['a'], r['gamma'], 'ratio'))
    r1 = not bad
    r2 = len(A['excluded']) == 0 and all(x['ok_z'] for x in A['table'])
    r3 = abs(A['floor'] - NF.DEFAULT_FLOOR) < 1e-300 and ('%.16e' % NF.DEFAULT_FLOOR) in reg
    r4 = 'max(|arch|, |prime|)' in reg
    gr = r1 and r2 and r3 and r4
    print('    the denominator recomputed at every row and the ratio consistent : %s (bad %s)' % (r1, bad or 'none'))
    print('    every row gate-RESOLVED so none excluded : %s ; the floor is the imported one and stated in the seal : %s' % (r2, r3))
    print('    the sealed denominator appears in the sealed file : %s' % r4)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RATIO')

    print(chr(10) + '  G-ROWS (exactly the aims already charted; no new seed in part (a); duplicates counted once):')
    srcs = set(x['src'] for x in A['table'])
    w1 = srcs <= {'b334_leg_reaching_40.json', 'b334_leg_reaching_81.json', 'b343_fine_40.json',
                  'b343_fine_81.json', 'b344_edge.json'}
    w2 = A['duplicates'] > 0 and 'DUPLICATE' in arun
    code = strip_prose(t('b349_relative.py'))
    w3 = 'seed_aimed' not in code and 'quantities' not in code
    keys = [(x['a'], x['gamma']) for x in A['table']]
    w4 = len(keys) == len(set(keys))
    gw = w1 and w2 and w3 and w4
    print('    rows only from the five named records : %s (%s)' % (w1, sorted(srcs)))
    print('    duplicates reported and counted once : %s ; every (width, height) unique : %s' % (w2, w4))
    print("    part (a)'s CODE builds no seed and computes no quantity : %s" % w3)
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-ROWS')

    print(chr(10) + "  G-READ (the reading by (D)'s rule; the artifact sentence present iff the minimum moved; flatness reported either way):")
    moved = not all(v['same'] for v in A['verdicts'].values())
    d1 = (A['survives'] is True) == A['verdicts'][str(A['desk_width'])]['same']
    d2 = ('AN ARTIFACT OF ABSOLUTE MEASUREMENT' in bf) and (('NOT AN ARTIFACT' in bf) != moved)
    d3 = all(('%.2f' % v['absolute']) in bank and ('%.2f' % v['relative']) in bank for v in A['flatness'].values())
    d4 = all(v['relative_flatter'] for v in A['flatness'].values()) == ('THE RELATIVE MEASURE IS FLATTER' in bf.upper())
    gd = d1 and d2 and d3 and d4
    print("    the survival flag follows (D)'s rule : %s ; the artifact sentence used correctly : %s" % (d1, d2))
    print('    the flatness figures in the bank : %s ; the flatness claim matches the measurement : %s' % (d3, d4))
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-READ')

    print(chr(10) + '  G-COND (part (b) ran iff (a) left the minimum standing; the sealed heights; both seed conditions; degenerates not charted):')
    e1 = (A['survives'] is True) and os.path.exists(BJ)
    e2 = B['extension'] == [0.75, 0.5, 0.25] and B['width'] == 81.0
    e3 = B['window'] == [45.0, 135.0]
    e4 = all(('def31' in s and 'in_window' in s) for s in B['seeds'])
    e5 = set(B['charted']) == {s['gamma'] for s in B['seeds'] if s['charted']} and not (set(B['degenerate']) & set(B['charted']))
    e6 = len(B['rows']) == len(B['charted'])
    # ### THIS ARM ASSERTS A PRESENCE, SO IT READS THE RAW SOURCE. ### b348's rule governs ABSENCE claims; an
    # ### arm that greps STRIPPED code for a string KEY removes the very thing it is looking for, which is what
    # ### this arm did on its first run.
    bsrc = io.open(t('b349_extend.py'), encoding='utf-8').read()
    e7 = ("if not R.get('survives')" in bsrc) and ("b349_relative.json" in bsrc)
    ge = e1 and e2 and e3 and e4 and e5 and e6 and e7
    print('    it ran and (a) said it may : %s ; the sealed heights and width : %s ; the sealed WINDOW : %s' % (e1, e2, e3))
    print('    every seed carries both conditions : %s ; charted and degenerate disjoint : %s ; only charted seeds have rows : %s' % (e4, e5, e6))
    print("    the tool's CODE consults (a)'s record before running : %s" % e7)
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-COND')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'A SECOND MEASURE OF THE SAME FIGURES IS A SECOND MEASURE' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTEXPLAINED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : room-relative returns 1 row(s)' in irun
    k2 = all(('%-40s NO KEY after  : True  PASS' % q) in irun for q in
             ('the room closes', 'a crossing is near', 'the construction never degenerates',
              'the relative measure is the right one'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s' % (k1, k2, k3))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOTEXPLAINED')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
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

    print(chr(10) + '  G-NOEDIT / G-PAPERS (no owner instrument; nothing in the papers repo, so the hook and mirror are NOT OWED):')
    owner = ['tools/b334_aimmap.py', 'tools/b328_family.py', 'tools/noise_floor.py', 'tools/reg_seal.py',
             'tools/b302_kernel.py', 'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    tcstat = [x for x in git(TC, 'status', '--porcelain').splitlines() if x.strip()]
    nohook = not os.path.exists(d('b349_hooks.txt')) and not os.path.exists(d('b349_mirror.txt'))
    gne = not touched and not ppstat and not tcstat and nohook and 'THE HOOK AND THE MIRROR ARE NOT OWED' in bf
    print('    owner instruments modified : %s ; papers dirty : %s ; TECHNE dirty : %s' % (touched or 'none', ppstat or 'none', tcstat or 'none'))
    print('    no hook or mirror record, and the bank says they are not owed : %s' % (nohook and 'THE HOOK AND THE MIRROR ARE NOT OWED' in bf))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT/G-PAPERS')

    print(chr(10) + '  G-ORDER (the seal verifies through its owning tool; the ordering read from two clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and A['run_clock'] > stampm.group(1) and B['run_clock'] > A['run_clock']
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; it carries its clock (%s) : %s' % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    the ordering from three clocks: seal %s < part (a) %s < part (b) %s : %s'
          % (stampm.group(1) if stampm else '?', A['run_clock'], B['run_clock'], o3))
    print('    the audit reads JOINTLY SATISFIABLE : %s' % o4)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    v40, v81 = A['verdicts']['40.0'], A['verdicts']['81.0']
    f40, f81 = A['flatness']['40.0'], A['flatness']['81.0']
    checks = [
        ('the row count %d and duplicates %d' % (len(A['table']), A['duplicates']),
         ('`%d`' % len(A['table'])) in bank and ('`%d`' % A['duplicates']) in bank),
        ('the two minima', ('%e' % v40['abs_val']).replace('e-05', 'e-05') and
         ('%.6e' % v40['abs_val']) in bank and ('%.6e' % v81['abs_val']) in bank
         and ('%.6e' % v40['rel_val']) in bank and ('%.6e' % v81['rel_val']) in bank),
        ('the four flatness figures', all(('%.2f' % x) in bank for x in
                                          (f40['absolute'], f40['relative'], f81['absolute'], f81['relative']))),
        ('the two spreads', ('%.3e' % A['spread_arch']) in bank and ('%.3e' % A['spread_places']) in bank),
        ('the gate floor', ('%.16e' % A['floor']) in bank),
        ('the three phases', all(('%.3f' % s['phase_deg']) in bank for s in B['seeds'])),
        ('the extended grid rows', all(('%+.9f' % r['room_z']) in bank for r in B['rows'])),
        ('the two clocks', A['run_clock'] is not None and B['run_clock'] is not None),
        ('the seal hash', SEAL in bank),
        ('the seal stamp', (stampm.group(1) if stampm else 'x') in bank),
    ]
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    checks.append(('%s clauses' % cl, ('%s clauses' % cl) in bank))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path):')
    once = (all(os.path.exists(p) for p in [ARUN, BRUN, CORR, IDX])
            and not os.path.exists(d('b349_relative_run2.txt'))
            and not os.path.exists(d('b349_extend_run2.txt')))
    print('    %s' % once)
    if not once:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):' % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
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

    ib2 = idx[idx.index('# ### THE ROOM, RELATIVE BEFORE EXTENDED (b349).'):idx.index('# ### THE PRICED-AND-RESOLVED ARC')] if '# ### THE ROOM, RELATIVE BEFORE EXTENDED (b349).' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the index row, swept):' % ROWNUM)
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
    tmpdir = tempfile.mkdtemp(prefix='b349_hedge_')
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
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
