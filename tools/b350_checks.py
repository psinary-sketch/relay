# -*- coding: utf-8 -*-
"""b350_checks.py -- THE GATE SUITE FOR THE FLOOR'S TWO HELD AXES, PRICED.

### ### **IT IMPORTS `quote_norm` FOR EVERY QUOTATION COMPARISON** -- the sortie's shared normaliser -- and every
### `G-NO*`-shaped arm reads STRIPPED CODE, which is b348's minted rule.
### ### **THE ARMS (registration section (F)):** `G-NOFRAME`, `G-PRICE`, `G-CONFOUND`, `G-BAND`, `G-VERDICT`,
### `G-TRAIL`, `G-ROW`, `G-KEY` / `G-NOTEXPLAINED`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`, `G-HOOK` / `G-MIRROR`,
### `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, the sweeps, `G-SHARED`, the hedge audit, the must-fail fixtures.
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

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b350_the_two_held_axes.txt')
REG = d('b350_registration_2026-09-07.txt')
FERRY = d('b350_ferry_2026-09-07.txt')
EXTRACT = d('b350_extract_notes.txt')
PRUN, PJ = d('b350_price_run.txt'), d('b350_price.json')
FRUN, FJ = d('b350_filings_run.txt'), d('b350_filings.json')
CORR, IDX = d('b350_corr_run.txt'), d('b350_index_run.txt')
SCAN, TERMSCAN, GATE = d('b350_ferry_scan.txt'), d('b350_reg_termscan.txt'), d('b350_reg_gate.txt')
CENSUS, FCEN = d('b350_census.txt'), d('b350_faces_census.txt')
REGSPEC, SATIS = d('b350_regspec_run.txt'), d('audit_b350_reg_satisfiable.txt')
PINS, INDEXQ = d('b350_pins_stepzero.txt'), d('audit_b350_index_query.txt')
SEAL = '24453ba8f2649a1a5e300aa0e2bf535bb1552eb8274138c631b0ea73a2e5e7df'
MARK = '<!-- b350 trail update -->'
ROWNUM = '198'

OWNED = [BANK, REG, FERRY, PRUN, PJ, FRUN, FJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         TERMSCAN, EXTRACT, d('b350_satisfiable.json'),
         t('b350_extract.py'), t('b350_regspec.py'), t('b350_price.py'), t('b350_filings.py'),
         t('b350_correspondence.py'), t('b350_index_append.py')]

CARRIERS = [
    (t('b350_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]
NEW_THIS_ACT = {'tools/b350_extract.py', 'tools/b350_regspec.py', 'tools/b350_price.py', 'tools/b350_filings.py',
                'tools/b350_correspondence.py', 'tools/b350_index_append.py', 'tools/b350_checks.py'}

TOOLNUM = [
    ('the cost, the band, the confounds and the verdict', 'tools/b350_price.py'),
    ('the trail block', 'tools/b350_filings.py'),
    ("b344's printed ladder, READ and not recomputed", 'tools/b344_ny.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 198', 'tools/b350_correspondence.py'),
    ('the key', 'tools/b350_index_append.py'),
    ('29 clauses', 'tools/b350_regspec.py'),
    ('13313 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ("b344 -- why NY and not the cut's tau", d('b344_registration_2026-09-06.txt'),
     "### ### **WHY `NY` AND NOT THE CUT'S `tau`:** ### moving `tau` moves the stable cut, and the cut's rank is"),
    ('b344 -- why NY and not the taper', d('b344_registration_2026-09-06.txt'),
     '### ### **WHY `NY` AND NOT THE TAPER:** ### the taper is `ALPHA` and `BETA`, and b316 records them as the'),
    ('b319 -- 57 times inside that separation', t('b319_stable.py'),
     '# ### `TAU = 1e-6` therefore sits ### **57 TIMES INSIDE THAT SEPARATION** ### and ten orders of'),
    ('b344 -- the residual converges in NY', d('b344_the_floor_priced.txt'),
     "### CORPUS'S OWN `NY = 512` THE REMAINING TRAVEL IS `7.059e-04`, about a ninth of the floor**; from"),
    ('b339 -- the three candidate origins', d('b339_the_exponent_resolved.txt'),
     "### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut's `tau`, the"),
    ('the trail -- its two demands', TRAILS,
     '**What is owed:** the same movement measurement b344 made on `NY`, made on `tau` and on the taper'),
    ('the order -- leg 2', FERRY, "LEG 2 (b350) \u2014 THE FLOOR'S TWO HELD AXES, PRICED from b344's"),
    ('the order -- and price the pricing if an axis cannot be priced', FERRY,
     'axis, say so and price the pricing. The open trail is'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK, '### ### ### **THE FLOOR IS UNEXPLAINED.**'),
    ('### pricing is not measuring', BANK, '### ### **PRICING IS NOT MEASURING, AND NOTHING PRICED HERE\n### ### EXPLAINS ANYTHING.**'),
    ('### the cost is the same for both', BANK, '### ### ### **`89.35` SECONDS OF WALL PER VALUE TRIED, FOR EITHER AXIS.**'),
    ('### the band, and its width', BANK, '### ### ### **THE RANK-PRESERVING BAND IS `(2.144048e-07, 2.277535e-06)`, A FACTOR OF `10.62` WIDE**, and'),
    ('### a fact about the cut, not the residual', BANK, '### ### ### **AND THAT IS A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL.**'),
    ('### the taper gets no room at all', BANK, '### ### ### **SO THE PRINTED FIGURES PRICE NO ROOM FOR THE TAPER AT ALL, AND THIS ACT SAYS SO RATHER THAN'),
    ('### a difference and not a room', BANK, '### ### **EVEN THAT WOULD GIVE A DIFFERENCE AND NOT A ROOM**, because the'),
    ('### the two axes are not symmetric', BANK, '### ### ### **SO THE TWO AXES ARE NOT SYMMETRIC, AND THE ASYMMETRY IS NOT IN THE COST.**'),
    ('### the unexplained part named', BANK, '### ### **THE UNEXPLAINED PART, NAMED:**'),
    ('### the trail is restated, not discharged', BANK, '### ### ### **SO THE TRAIL IS RESTATED, NOT DISCHARGED**, by one appended block on `OPEN_TRAILS.md` under a'),
    ('### the hook and mirror are owed', BANK, '### ### **THE PAPERS REPO THEREFORE MOVES, AND THE HOOK AND THE MIRROR ARE OWED.**'),
    ('### the thing no seat wrote down', BANK, '### ### **AND ONE THING NO SEAT WROTE DOWN AND THE ACT FOUND ANYWAY:**'),
    ('### the shadow', BANK, '### ### **EXPECTED: NOTHING.** ### A price is a statement about what an act would cost, made by an act that'),
]

MUST_FAIL = [
    ('the bank never says the floor is explained', BANK, '### THE FLOOR IS EXPLAINED.'),
    ('the bank never says the trail is discharged', BANK, '### THE TRAIL IS DISCHARGED.'),
    ('the bank never says the band leaves the residual unchanged', BANK, '### THE BAND LEAVES THE RESIDUAL UNCHANGED.'),
    ('the bank never says an axis moved', BANK, '### AN AXIS MOVED.'),
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
    print("b350 -- GATE SUITE (A PRICING ACT THAT MOVES NOTHING)")
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = quote_norm.contains(extract, anchor)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  SELF NEEDLES:')
    bankraw = io.open(BANK, encoding='utf-8').read()
    for lbl, path, anchor in SELF_NEEDLES:
        ok = quote_norm.contains(bankraw, anchor)
        print('    %s  %s' % ('PASS' if ok else '### FAIL (NOT FOUND)', lbl))
        if not ok:
            unpullable += 1
            fails.append(lbl)
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = bankraw
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    P = json.load(io.open(PJ, encoding='utf-8'))
    F = json.load(io.open(FJ, encoding='utf-8'))
    N = json.load(io.open(d('b344_ny.json'), encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()

    print(chr(10) + '  G-NOFRAME (no frame built, no ladder run; the tool imports nothing that computes a residual):')
    code = strip_prose(t('b350_price.py'))
    f1 = not any(x in code for x in ('b316_instrument', 'b317_smear', 'b334_aimmap', 'b328_family', 'b321_window'))
    f2 = 'b344_ny.json' in io.open(t('b350_price.py'), encoding='utf-8').read()
    f3 = P['ladder'] == N['ladder'] and P['walls'] == [r['wall'] for r in N['rows']]
    gf = f1 and f2 and f3
    print('    the CODE imports no instrument that could compute a residual : %s' % f1)
    print("    it reads b344's own record : %s ; its ladder and walls are b344's, unchanged : %s" % (f2, f3))
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-NOFRAME')

    print(chr(10) + '  G-PRICE (all three units reported for BOTH axes, or the act says which it cannot and prices the pricing):')
    p1 = abs(P['wall_total'] - sum(r['wall'] for r in N['rows'])) < 1e-9
    p2 = P['taper_room_priced'] is False and P['taper_pricing_cost'] > 0
    p3 = 'PRICE NO ROOM FOR THE TAPER AT ALL' in bf
    p4 = 'A DIFFERENCE AND NOT A ROOM' in bf
    gp = p1 and p2 and p3 and p4
    print("    the ladder cost is exactly the sum of b344's printed walls : %s" % p1)
    print('    the taper room is recorded as NOT priced, and the pricing is priced : %s' % p2)
    print('    the bank says so, and says even that would give a difference not a room : %s / %s' % (p3, p4))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PRICE')

    print(chr(10) + "  G-CONFOUND (b344's two sealed reasons located VERBATIM at the sealed file, through the shared normaliser):")
    sealed = io.open(d('b344_registration_2026-09-06.txt'), encoding='utf-8', errors='replace').read()
    c1 = all(quote_norm.contains(sealed, r['fragment']) for r in P['reasons'])
    c2 = all(r['found'] and r['line'] for r in P['reasons'])
    c3 = 'CONFOUND THE RANK WITH THE FLOOR' in bf.upper() and 'CONFOUND THE INSTRUMENT WITH THE OBJECT' in bf.upper()
    gc = c1 and c2 and c3
    print("    both reasons located at b344's sealed registration : %s / %s" % (c1, c2))
    print('    the bank names both confounds : %s' % c3)
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CONFOUND')

    print(chr(10) + '  G-BAND (the band is the intersection across the rungs; the cut-not-residual sentence present):')
    lo = max(r['held']['largest_dropped'] for r in N['rows'])
    hi = min(r['held']['smallest_kept'] for r in N['rows'])
    b1 = abs(P['band_lo'] - lo) < 1e-18 and abs(P['band_hi'] - hi) < 1e-18
    b2 = P['tau_inside'] and lo < P['tau'] < hi
    b3 = 'A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL' in bf
    b4 = abs(P['band_factor'] - hi / lo) < 1e-9
    gb = b1 and b2 and b3 and b4
    print('    the band recomputed as the intersection : %s ; tau strictly inside : %s' % (b1, b2))
    print('    the width recomputes : %s ; the cut-not-residual sentence present : %s' % (b4, b3))
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BAND')

    print(chr(10) + "  G-VERDICT (the branch by (D)'s rule; the EXPLAINED branch shown unreachable):")
    v1 = P['verdict'] == 'THE FLOOR IS UNEXPLAINED' and 'THE FLOOR IS UNEXPLAINED' in bf
    v2 = 'EXPLAINED` BRANCH WAS SEALED AS VISIBLY UNREACHABLE' in bf or 'VISIBLY UNREACHABLE' in bf
    v3 = 'THE UNEXPLAINED PART, NAMED' in bf
    gv = v1 and v2 and v3
    print('    the verdict and the bank agree : %s ; the unreachable branch stated : %s ; the part named : %s' % (v1, v2, v3))
    print('    %s' % ('PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-VERDICT')

    print(chr(10) + '  G-TRAIL (one appended block, a true prefix of its blob, the two demands quoted, restated not discharged):')
    tr = io.open(TRAILS, encoding='utf-8').read()
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    blk = tr[tr.index(MARK):] if MARK in tr else ''
    t1 = tr.count(MARK) == 1 and F['trails'] in ('WRITTEN', 'DUPLICATE')
    t2 = (tb is not None) and norm(tr).startswith(norm(tb).rstrip(chr(10)))
    t3 = quote_norm.contains(tr, 'the same movement measurement b344 made on `NY`, made on `tau` and on the taper')
    t4 = 'RESTATED, NOT DISCHARGED' in blk and P['trail'] == 'RESTATED, NOT DISCHARGED'
    gt = t1 and t2 and t3 and t4
    print('    one block under the mark : %s ; a true prefix of its blob : %s' % (t1, t2))
    print("    the trail's own demand located : %s ; the block says RESTATED, NOT DISCHARGED : %s" % (t3, t4))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s):' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'A PRICE IS NOT A MEASUREMENT' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s ; %s' % (ROWNUM, len(rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTEXPLAINED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : held-axes-priced returns 1 row(s)' in irun
    k2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
             ('the band leaves the residual unchanged', 'the trail is discharged',
              'the axes are priced and settled', 'the floor is accounted for'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s ; %s'
          % (k1, k2, k3, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOTEXPLAINED')

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

    print(chr(10) + "  G-NOEDIT (no owner instrument; only OPEN_TRAILS.md touched in the papers repo; TECHNE clean):")
    owner = ['tools/b344_ny.py', 'tools/b319_stable.py', 'tools/b316_instrument.py', 'tools/noise_floor.py',
             'tools/reg_seal.py', 'tools/quote_norm.py', 'tools/run_clock.py', 'tools/gate_text.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'OPEN_TRAILS.md']
    tcstat = [x for x in git(TC, 'status', '--porcelain').splitlines() if x.strip()]
    gne = not touched and not ppbad and not tcstat
    print('    owner instruments modified : %s ; papers paths beyond OPEN_TRAILS.md : %s ; TECHNE dirty : %s ; %s'
          % (touched or 'none', ppbad or 'none', tcstat or 'none', 'PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the ordering read from clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and P['run_clock'] > stampm.group(1) and F['run_clock'] >= P['run_clock']
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; clock %s : %s' % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    seal < price %s <= filings %s : %s ; the audit JOINTLY SATISFIABLE : %s' % (P['run_clock'], F['run_clock'], o3, o4))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED):')
    hookp, mirrorp = d('b350_hooks.txt'), d('b350_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht, mt = io.open(hookp, encoding='utf-8', errors='replace').read(), io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh = h_ok and m_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror: clean on all three clauses : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS:')
    checks = [
        ('the ladder cost %.2f' % P['wall_total'], ('%.2f' % P['wall_total']) in bank),
        ('the band ends', ('%.6e' % P['band_lo']) in bank and ('%.6e' % P['band_hi']) in bank),
        ('the width and the two factors', all(('%.2f' % x) in bank for x in (P['band_factor'], P['fall_factor'], P['rise_factor']))),
        ('the taper pricing cost %.2f' % P['taper_pricing_cost'], ('%.2f' % P['taper_pricing_cost']) in bank),
        ('the two reason lines', all(str(r['line']) in bank for r in P['reasons'])),
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

    print(chr(10) + '  G-ONCE:')
    once = (all(os.path.exists(p) for p in [PRUN, FRUN, CORR, IDX])
            and not os.path.exists(d('b350_price_run2.txt')) and not os.path.exists(d('b350_filings_run2.txt')))
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
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib2 = idx[idx.index("# ### THE FLOOR'S TWO HELD AXES, PRICED (b350)."):idx.index('# ### THE ROOM, RELATIVE BEFORE EXTENDED (b349).')] if "# ### THE FLOOR'S TWO HELD AXES, PRICED (b350)." in idx else ''
    print(chr(10) + '  G-STEM-APPENDED:')
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', blk), ('the index row', ib2)):
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
    tmpdir = tempfile.mkdtemp(prefix='b350_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the trail block', blk), ('the index row', ib2)):
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
