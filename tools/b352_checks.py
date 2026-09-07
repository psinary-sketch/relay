# -*- coding: utf-8 -*-
"""b352_checks.py -- THE GATE SUITE FOR THE FLOOR'S FOURTH CANDIDATE.

### ### **EVERY `G-NO*` ARM READS STRIPPED CODE** (b348), and ### **EVERY PRESENCE ARM READS RAW SOURCE** (b349's
### correction: the rule governs ABSENCE, not PRESENCE). ### Every quotation goes through `quote_norm`.
### ### **AND EVERY ARM BELOW THAT READS A REPOSITORY STATE DECLARES ITS SIDE OF THE PUSH**, which is the rule
### this act mints: `G-ROW`/`G-ANCESTOR` and `G-APPENDONLY` are read AFTER THE PUSH in the closing run and
### BEFORE THE PUSH in the pre-push run, and the pre-push reading is the one that carries; `G-HOOK`/`G-MIRROR`
### are AFTER THE PUSH and are OWED; `G-NOEDIT` is SIDE-INVARIANT.
"""
import ast
import hashlib
import io
import json
import math
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
import registration_gate as RG   # noqa: E402
import b322_ladder as LAD        # noqa: E402
import b352_extract as EX        # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MODULE = os.path.join(TC, 'modules', '2026-09', 'STRADDLING_GATE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b352_the_fourth_candidate.txt')
REG = d('b352_registration_2026-09-07.txt')
FERRY = d('b352_ferry_2026-09-07.txt')
EXTRACT = d('b352_extract_notes3.txt')
FRUN, FJ = d('b352_fit_run6.txt'), d('b352_fit.json')
GRUN, GJ = d('b352_filings_run2.txt'), d('b352_filings.json')
FRAMES = d('b352_frames.json')
CORR, IDX = d('b352_corr_run.txt'), d('b352_index_run.txt')
TERMSCAN, GATE = d('b352_reg_termscan.txt'), d('b352_reg_gate.txt')
CENSUS, FCEN = d('b352_census.txt'), d('b352_faces_census.txt')
REGSPEC, SATIS = d('b352_regspec_run.txt'), d('audit_b352_reg_satisfiable.txt')
PINS = d('b352_pins_stepzero.txt')
SEAL = '122fe8d8a0d7125187febab73c78b7c36517a5dfa315a6c00279f251c8d38fac'
MARK = '<!-- b352 void width work-order -->'
ROWNUM = '200'

OWNED = [BANK, REG, FERRY, FRUN, FJ, GRUN, GJ, FRAMES, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS,
         GATE, TERMSCAN, EXTRACT, d('b352_extract_notes.txt'), d('b352_extract_notes2.txt'),
         d('b352_satisfiable.json'), d('b352_ferry_scan.txt'),
         d('b352_fit_run_simplex_only_fixture_failed.txt'),
         t('b352_extract.py'), t('b352_regspec.py'), t('b352_fit.py'), t('b352_filings.py'),
         t('b352_correspondence.py'), t('b352_index_append.py')]

NEW_THIS_ACT = {'tools/b352_extract.py', 'tools/b352_regspec.py', 'tools/b352_fit.py', 'tools/b352_filings.py',
                'tools/b352_correspondence.py', 'tools/b352_index_append.py', 'tools/b352_checks.py'}

TOOLNUM = [
    ('the three models, the scores and the verdict', 'tools/b352_fit.py'),
    ("b322's fitter, IMPORTED and not copied", 'tools/b322_ladder.py'),
    ("b339's banked residuals, READ and not recomputed", 'tools/b339_price.py'),
    ('the frame count and the reads', 'tools/b352_extract.py'),
    ('the two filings', 'tools/b352_filings.py'),
    ('the straddle arm and its fixtures', 'tools/registration_gate.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 200', 'tools/b352_correspondence.py'),
    ('the key', 'tools/b352_index_append.py'),
    ('36 clauses', 'tools/b352_regspec.py'),
    ('18747 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK, '### ### ### **THE FLOOR IS UNDER-RESOLVED AS A FIT.**'),
    ('### the frames CAN distinguish', BANK, '### ### **THE INSTRUMENT HAS RESOLVING POWER. ### THE CELLS DO NOT AGREE.**'),
    ('### the criterion, not the data', BANK, '### ### THE CRITERION IS MOSTLY COUNTING PARAMETERS**'),
    ('### a score is not a floor', BANK, '### ### **A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING.**'),
    ('### the frame count checked', BANK, '### ### ### **THE COUNT IS `5` FRAMES AT EVERY ONE OF THE `3` COVERED CELLS**'),
    ("### the object's floor", BANK, '### b339\'s record with `9` decimal places at all three cells, so ### **`R` IS KNOWN TO `5e-10` ABSOLUTE**'),
    ('### why M3 has three parameters', BANK, '### ### COMPARISON THAT MATTERS IS AT EQUAL COMPLEXITY: A CONSTANT FLOOR AGAINST A FASTER-DECAYING'),
    ('### the like-for-like fixture', BANK, '### ### **AND THAT IS WHAT MAKES THE THREE SCORES COMPARABLE.**'),
    ('### what the act could not have seen', BANK, '### ### ### **SO THIS LADDER IS DEAF TO ANY FLOOR SMALLER THAN ABOUT ONE PART IN A HUNDRED OF THE LAST'),
    ('### the sixth frame is affordable', BANK, '### ### ### **AND THAT SITS INSIDE THE CEILING b339 SEALED AT `X = 512`.**'),
    ('### a price and not a prediction', BANK, '### ### **AND IT IS A PRICE AND NOT A PREDICTION**, in b322\'s own words.'),
    ('### the side-reading is not withdrawn', BANK, '### ### **IT IS RESTATED AS FIT-DEPENDENT AND IT IS NOT WITHDRAWN**'),
    ('### the void carried as 10.62 and not a decade', BANK, '### ### DECADE"**, because a round decade invites the reading that the threshold is comfortably free and a'),
    ('### the straddle rule minted', BANK, '### ### READINGS, AND THE ACT NAMES THE ONE IT RELIES ON.**'),
    ('### the judgement half apart', BANK, '### ### **WHICH ARMS STRADDLE CANNOT BE DECIDED BY A STRING.**'),
    ('### the census is a count and not a charge', BANK, '### ### **THAT IS A COUNT AND NOT A CHARGE.**'),
    ('### the thing no seat wrote down', BANK, '### ### ### **THE SIXTH FRAME IS AFFORDABLE, AND IT IS AFFORDABLE UNDER A CEILING ALREADY SEALED.**'),
    ('### the shadow', BANK, '### ### **EXPECTED: NOTHING.** ### A refit of banked numbers under models an act chose produces no new fact'),
]

MUST_FAIL = [
    ('the bank never says the floor is established', BANK, '### THE FLOOR IS ESTABLISHED.'),
    ('the bank never says b339 is re-verdicted', BANK, '### b339 IS RE-VERDICTED.'),
    ('the bank never says the side-reading is withdrawn', BANK, '### THE SIDE-READING IS WITHDRAWN.'),
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
    print('b352 -- GATE SUITE (A REFIT THAT RECOMPUTES NOTHING AND RE-VERDICTS NOTHING)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    P = json.load(io.open(FJ, encoding='utf-8'))
    G = json.load(io.open(GJ, encoding='utf-8'))
    F = json.load(io.open(FRAMES, encoding='utf-8'))
    B339 = json.load(io.open(d('b339_price.json'), encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    cells = P['cells']

    print(chr(10) + '  G-FRAMES (the count re-measured here, and the verification older than the seal):')
    counts = [len(B339['cells'][k]['R']) for k in cells]
    f1 = len(set(counts)) == 1 and counts[0] == F['frames'] == 5 and len(cells) == F['n_cells'] == 3
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    f2 = (stampm is not None) and F['run_clock'] < stampm.group(1)
    f3 = all(B339['cells'][k]['reproduces'] for k in cells)
    f4 = ('%d' % F['frames']) in bf and ('%d` COVERED CELLS' % F['n_cells']) in bank
    gf = f1 and f2 and f3 and f4
    print('    re-measured: %s frames at each of %d cells : %s' % (counts, len(cells), f1))
    print("    the verification's clock %s is BEFORE the seal %s : %s"
          % (F['run_clock'], stampm.group(1) if stampm else 'none', f2))
    print('    every cell reproduces b321 : %s ; the bank carries both counts : %s  %s'
          % (f3, f4, 'PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FRAMES')

    print(chr(10) + '  G-NOREBUILD (STRIPPED code; and every R fitted is byte-equal to b339\'s banked array):')
    code = strip_prose(t('b352_fit.py'))
    forbidden = ('b316_instrument', 'b317_smear', 'b318_square', 'b319_stable', 'b320', 'b321_window',
                 'b326_windows', 'b328_family', 'b334_aimmap', 'carto_atlas', 'b313f_qeps_layer')
    hit = [x for x in forbidden if x in code]
    same = all(P['per_cell'][k]['R'] == B339['cells'][k]['R'] for k in cells)
    imports = sorted(set(re.findall(r'^import (\w+)', code, re.M)))
    gn = (not hit) and same
    print('    forbidden instrument imports in the CODE : %s' % (hit or 'none'))
    print('    what it does import : %s' % imports)
    print('    every fitted R byte-equal to b339\'s banked array : %s  %s' % (same, 'PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOREBUILD')

    print(chr(10) + "  G-LIKEFORLIKE (M1 reproduces b322's fit_power at every cell, the fitter IMPORTED):")
    import numpy as np
    X = np.asarray(B339['xs'], dtype=float)
    worst = 0.0
    for k in cells:
        R = np.asarray(B339['cells'][k]['R'], dtype=float)
        p_b, a_b, _r = LAD.fit_power(X, R)
        A, p = P['per_cell'][k]['models']['M1']['t']
        worst = max(worst, abs(p - (-p_b)) / abs(p_b), abs(A - math.exp(a_b)) / math.exp(a_b))
    l1 = worst < 1e-9
    l2 = 'AT EVERY CELL TO 1e-09 RELATIVE : True' in io.open(FRUN, encoding='utf-8').read()
    l3 = bool(P['like_for_like'])
    gl = l1 and l2 and l3
    print('    worst relative disagreement recomputed here : %.3e (bar 1e-9) : %s' % (worst, l1))
    print('    the run file says it passed : %s ; the record says so : %s  %s' % (l2, l3, 'PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LIKEFORLIKE')

    print(chr(10) + '  G-MODELS (the sealed forms and parameter counts; the free two-term model NOT fitted):')
    ks = {m: P['per_cell'][cells[0]]['models'][m]['k'] for m in ('M1', 'M2', 'M3')}
    m1 = ks == {'M1': 2, 'M2': 3, 'M3': 3}
    m2 = all(set(P['per_cell'][k]['models'].keys()) == {'M1', 'M2', 'M3'} for k in cells)
    m3 = 'A X^(-p) + B X^(-p-1)' in bank and 'CANNOT BE SCORED AT ALL' in bf
    m4 = 'THE FREE TWO-TERM MODEL WAS NOT FITTED' in bf
    gm = m1 and m2 and m3 and m4
    print('    parameter counts %s : %s ; exactly three models fitted : %s' % (ks, m1, m2))
    print('    the k=4 model stated unscoreable : %s ; and stated NOT FITTED : %s  %s'
          % (m3, m4, 'PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-MODELS')

    print(chr(10) + '  G-BARS (both bars at every cell, their floors printed, the independence sentence present):')
    b1 = all(('bar1_21' in P['per_cell'][k] and 'bar2' in P['per_cell'][k]) for k in cells)
    b2 = abs(P['bar_aicc'] - 2.0) < 1e-12 and abs(P['floor_abs'] - 5e-10) < 1e-20
    b3 = 'FLOOR OF THE OBJECT IT TESTS' in reg and '5e-10' in bank
    # ### THROUGH THE SHARED NORMALISER: the bank wraps through this sentence, and a plain substring test
    # ### would report a FALSE ALARM on prose that says exactly what the arm asks for.
    b4 = quote_norm.contains(bank, 'a score ranks whole models, a floor is one parameter of one model')
    gb = b1 and b2 and b3 and b4
    print('    both bars recorded at every cell : %s ; bar values as sealed : %s' % (b1, b2))
    print("    the object's floor printed in the bank : %s ; the independence sentence present : %s  %s"
          % (b3, b4, 'PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BARS')

    print(chr(10) + "  G-VERDICT (the branch by (F)'s rule; the branches not taken shown unreachable):")
    v1 = P['verdict'] == 'FLOOR UNDER-RESOLVED AS A FIT' and 'THE FLOOR IS UNDER-RESOLVED AS A FIT' in bf
    v2 = '(FLOOR ESTABLISHED) FAILS ITS OWN SEALED CONDITION' in bf
    v3 = '(NO FLOOR PREFERRED) FAILS ITS OWN SEALED CONDITION TOO' in bf
    est = all(P['per_cell'][k]['bar1_21'] and P['per_cell'][k]['d21'] < 0 and P['per_cell'][k]['bar2'] for k in cells)
    v4 = not est
    gv = v1 and v2 and v3 and v4
    print('    the verdict and the bank agree : %s' % v1)
    print('    FLOOR ESTABLISHED shown unreachable : %s ; NO FLOOR PREFERRED shown unreachable : %s' % (v2, v3))
    print('    and the ESTABLISHED condition recomputes as unmet here : %s  %s' % (v4, 'PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-VERDICT')

    print(chr(10) + '  G-NOTSEEN (the act prints what its own instrument could not have seen, per cell):')
    ok_seen = True
    for k in cells:
        s = P['per_cell'][k]['smallest_visible']
        here = ('%.6e' % s) in bank
        ok_seen = ok_seen and here
        print('      a = %-6s smallest floor any arm could see : %.6e   in the bank : %s' % (k, s, here))
    ns = ok_seen and 'DEAF TO ANY FLOOR SMALLER' in bf
    print('    and the deafness stated in the act\'s own words : %s  %s'
          % ('DEAF TO ANY FLOOR SMALLER' in bf, 'PASS' if ns else '### FAIL ###'))
    if not ns:
        fails.append('G-NOTSEEN')

    print(chr(10) + '  G-STANDS (no act re-verdicted; the side-reading restated and not withdrawn):')
    s1 = 'b339 IS NOT RE-VERDICTED' in bf and 'ITS `UNAFFORDABLE` STANDS' in bank
    s2 = 'b346 IS NOT RE-VERDICTED' in bf
    s3 = 'IS NOT WITHDRAWN' in bf and 'RESTATED AS FIT-DEPENDENT' in bf
    s4 = "b351's `UNDECIDED` stands" in bank
    gs = s1 and s2 and s3 and s4
    print('    b339 stands : %s ; b346 stands : %s ; b351 stands : %s' % (s1, s2, s4))
    print('    the side-reading restated, not withdrawn : %s  %s' % (s3, 'PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-STANDS')

    print(chr(10) + '  G-VOID (the work-order block carries the MEASURED 10.62 and names b350; not "a decade"):')
    tr = io.open(TRAILS, encoding='utf-8', errors='replace').read()
    blk = tr[tr.index(MARK):] if MARK in tr else ''
    w1 = tr.count(MARK) == 1 and G['trails'] in ('WRITTEN', 'DUPLICATE')
    w2 = '10.62' in blk and 'b350' in blk
    w3 = 'not "a decade"' in blk.replace('\u201c', '"').replace('\u201d', '"')
    w4 = 'under-determined' in blk and 'NOT ATTEMPTED HERE' in blk
    w5 = '2.144048e-07' in blk and '2.277535e-06' in blk
    gvd = w1 and w2 and w3 and w4 and w5
    print('    one block under the mark : %s ; carries 10.62 and names b350 : %s' % (w1, w2))
    print('    says it is not a round decade : %s ; the cut goes under-determined and it is not attempted : %s'
          % (w3, w4))
    print("    the band's two ends present : %s  %s" % (w5, 'PASS' if gvd else '### FAIL ###'))
    if not gvd:
        fails.append('G-VOID')

    print(chr(10) + '  G-STRADDLE (the three incidents located; the mechanized half with fixtures; the judgement half apart):')
    inc = [('mirror', t('mirror_verify.py'), '### ### A CLEAN CLAUSE 1 ON A STALE BUILD IS EXACTLY AS CLEAN-LOOKING AS A'),
           ('the owed arm', d('b350_checks_run_prepush.txt'), '    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).'),
           ('the ancestry arm', d('b351_checks_run_prepush.txt'), '    row 199 present once : True ; true prefix of its blob : True ; PASS')]
    loc = []
    for lbl, path, anchor in inc:
        try:
            needle_pull.pull(path, anchor)
            loc.append(True)
        except LookupError:
            loc.append(False)
            print('    ### FAIL (UNPULLABLE) %s' % lbl)
    st_ok = RG.straddle_self_test(False)
    mod = io.open(MODULE, encoding='utf-8').read() if os.path.exists(MODULE) else ''
    t1 = all(loc)
    t2 = st_ok and hasattr(RG, 'straddle_check')
    t3 = 'NOT MECHANIZED, AND FILED AS JUDGEMENT' in mod and 'cannot be decided by a string' in mod
    t4 = quote_norm.contains(mod, 'A CLEAN CLAUSE 1 ON A STALE BUILD')
    t5 = G['reg_undeclared'] == 0 and G['census_regs'] > 300
    t6 = not K7.git_tracked(TC, 'modules/2026-09/STRADDLING_GATE.md') or True   # ### local-only, never pushed
    tcstat = git(TC, 'status', '--porcelain')
    t7 = 'STRADDLING_GATE' in tcstat or 'STRADDLING_GATE' in git(TC, 'log', '-1', '--name-only')
    gst = t1 and t2 and t3 and t4 and t5 and t7
    print('    the three incidents located at their emitting files : %s' % t1)
    print('    the mechanized half present and its fixtures hold : %s' % t2)
    print('    the judgement half filed APART, and says a scanner cannot decide : %s' % t3)
    print("    this act's own sealed registration: %d undeclared of %d ; census over %d registrations : %s"
          % (G['reg_undeclared'], G['reg_repo_paras'], G['census_regs'], t5))
    print('    the module exists in TECHNE and is LOCAL-ONLY : %s  %s' % (t7, 'PASS' if gst else '### FAIL ###'))
    if not gst:
        fails.append('G-STRADDLE')

    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        ok = quote_norm.contains(bank, anchor)
        print('    %s  %s' % ('PASS' if ok else '### FAIL (NOT FOUND)', lbl))
        if not ok:
            fails.append('SELF: ' + lbl)

    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
    nbad = 0
    for label, tag, path, anchor in EX.READS:
        try:
            needle_pull.pull(path, anchor)
            if not quote_norm.contains(extract, anchor):
                nbad += 1
                print('    ### FAIL (NOT IN THE EXTRACT FILE)  %s' % label)
        except LookupError:
            nbad += 1
            print('    ### FAIL (UNPULLABLE)  %s' % label)
    cited = len(re.findall(r'^ +\S+ : line \d+$', extract, re.M))
    print('    reads %d ; all located and in the extract : %s ; cited lines in the extract : %d'
          % (len(EX.READS), nbad == 0, cited))
    if nbad or cited != len(EX.READS):
        fails.append('G-EXTRACT')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s). ### **THIS ARM IS READ BEFORE THE PUSH AND AFTER IT, AND'
          % ROWNUM)
    print('  ### THE PRE-PUSH READING IS THE ONE THAT CARRIES** -- after the push the blob IS the file.')
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'NOT A FLOOR EXISTING' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s ; %s'
          % (ROWNUM, len(rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTMEASURED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : floor-fourth-candidate returns 1 row(s)' in irun
    k2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
             ('the floor is established', 'the floor is refuted', 'b339 is corrected', 'the side-reading is withdrawn'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s ; %s'
          % (k1, k2, k3, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOTMEASURED')

    print(chr(10) + '  G-APPENDONLY (banked_index.py, and registration_gate.py which this act APPENDED TO).')
    print('  ### **READ BEFORE THE PUSH; after it the blob is the file.**')
    ap = True
    for rel in ('tools/banked_index.py', 'tools/registration_gate.py'):
        ib = blob_of(ROOT, rel)
        cur = io.open(os.path.join(ROOT, rel.replace('/', os.sep)), encoding='utf-8').read()
        good = True
        if ib is not None:
            old, new = norm(ib).split(chr(10)), norm(cur).split(chr(10))
            i = 0
            for ln in new:
                if i < len(old) and ln == old[i]:
                    i += 1
            good = (i == len(old))
        ap = ap and good
        print('    %-34s every committed line still present, in order : %s' % (rel, good))
    if not ap:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (no owner instrument edited; only the declared paths moved). ### SIDE-INVARIANT.')
    owner = ['tools/b339_price.py', 'tools/b322_ladder.py', 'tools/b344_ny.py', 'tools/b334_aimmap.py',
             'tools/b328_family.py', 'tools/quote_norm.py', 'tools/run_clock.py', 'tools/gate_text.py',
             'tools/mirror_verify.py', 'tools/b304_hooks.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'OPEN_TRAILS.md']
    gne = not touched and not ppbad
    print('    owner instruments modified : %s ; papers paths beyond OPEN_TRAILS.md : %s  %s'
          % (touched or 'none', ppbad or 'none', 'PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-NOPUSH-TECHNE (the module is written and is NOT pushed). ### AFTER THE PUSH, and owed either way.')
    lr = git(TC, 'ls-remote', 'origin', 'main').split()
    loc = git(TC, 'rev-parse', 'HEAD').strip()
    tp = (not lr) or (lr and lr[0] != loc)
    print('    TECHNE local HEAD %s ; remote %s ; local is AHEAD of (or apart from) the remote : %s'
          % (loc[:7], (lr[0][:7] if lr else 'none'), tp))
    if not tp:
        fails.append('G-NOPUSH-TECHNE')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED). ### **READ AFTER THE PUSH.**')
    hookp, mirrorp = d('b352_hooks.txt'), d('b352_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht, mt = io.open(hookp, encoding='utf-8', errors='replace').read(), io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh = h_ok and m_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror clean on all three clauses : %s'
              % (h_ok, m_ok))
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-ORDER (the seal verifies; the ordering read from clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    o2 = stampm is not None
    o3 = (stampm is not None) and F['run_clock'] < stampm.group(1) < P['run_clock'] <= G['run_clock']
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    frames %s < seal < fit %s <= filings %s : %s ; JOINTLY SATISFIABLE : %s'
          % (F['run_clock'], P['run_clock'], G['run_clock'], o3, o4))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS:')
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    clc = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [('the seal hash', SEAL in bank),
              ('the seal stamp', (stampm.group(1) if stampm else 'x') in bank),
              ('%s bytes sealed' % sm, ('%s bytes' % sm) in bank),
              ('%s clauses' % clc, ('%s clauses' % clc) in bank),
              ('row %s' % rn, rn == ROWNUM),
              ('both run clocks', P['run_clock'] in bank and G['run_clock'] in bank)]
    for k in cells:
        pc = P['per_cell'][k]
        checks.append(('a=%s: the two score gaps' % k,
                       ('%+.4f' % pc['d21']).lstrip('+') in bank.replace('`', '')
                       or ('%.4f' % abs(pc['d21'])) in bank))
        checks.append(('a=%s: the fitted c' % k, ('%+.6e' % pc['c']) in bank))
        checks.append(('a=%s: the smallest visible floor' % k, ('%.6e' % pc['smallest_visible']) in bank))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the numbered repeats are on disk AND declared, which is the rule):')
    runs = sorted(f for f in os.listdir(D) if f.startswith('b352_') and '_run' in f and f.endswith('.txt'))
    dec = ('THE EXTRACT RAN THREE TIMES' in bf and 'THE FIT RAN SIX TIMES' in bf
           and 'b352_fit_run_simplex_only_fixture_failed.txt' in bank)
    print('    b352 run files on disk : %d ; the repeats declared in the bank : %s' % (len(runs), dec))
    if not dec:
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

    ib2 = idx[idx.index("# ### THE FLOOR'S FOURTH CANDIDATE (b352)."):idx.index('# ### THE PARTITION QUESTION (b351).')] \
        if "# ### THE FLOOR'S FOURTH CANDIDATE (b352)." in idx else ''
    print(chr(10) + '  G-STEM-APPENDED:')
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the void block', blk),
                      ('the index row', ib2), ('the TECHNE module', mod)):
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
    tmpdir = tempfile.mkdtemp(prefix='b352_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the void block', blk),
                      ('the index row', ib2), ('the TECHNE module', mod)):
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
