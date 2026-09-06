# -*- coding: utf-8 -*-
"""b343_checks.py -- THE GATE SUITE FOR THE MAP'S NEXT REACH (LEG 5 OF THE SORTIE b339-b343).

### ### **THE ARMS (registration (F), F1-F9):** `G-GRID` (exactly the sealed heights and widths, none added or moved),
### `G-ROUTES` (two routes and the gate on every quantity; b334's comparator fixture firing), `G-SHARED` (the two heights
### shared with b334's coarse grid against its bank), `G-CROSSING` (the verdict by the sealed rule and no other),
### `G-FRAME` (three frames, the rank and dimension at each, both conventions named), `G-FLOOR` (the reading in the
### sealed words and no wider), `G-LEDGER`, `G-ROW` / `G-ANCESTOR`, `G-KEY` / `G-NOTAPROOF`, `G-APPENDONLY`, `G-NOEDIT`,
### `G-ORDER`, `G-HOOK` / `G-MIRROR`, `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, the struck-clause and stem sweeps, `G-SHARED-STEM`,
### the hedge audit, the must-fail fixtures; re-run after the push.
"""
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

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b343_the_maps_next_reach.txt')
REG = d('b343_registration_2026-09-06.txt')
EXTRACT = d('b343_extract_notes.txt')
F40, F81 = d('b343_fine_40.json'), d('b343_fine_81.json')
R40, R81 = d('b343_fine_40_run.txt'), d('b343_fine_81_run.txt')
CJ, CRUN = d('b343_crossing.json'), d('b343_crossing_run.txt')
FJ, FRUN = d('b343_frames.json'), d('b343_frames_run.txt')
LEDRUN, LEDRR = d('b343_ledger_run.txt'), d('b343_ledger_rerun.txt')
CORR, CORRR = d('b343_corr_run.txt'), d('b343_corr_rerun.txt')
IDX, IDXR = d('b343_index_run.txt'), d('b343_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b343_ferry_scan.txt'), d('b343_reg_termscan.txt'), d('b343_reg_gate.txt')
CENSUS, FCEN = d('b343_census.txt'), d('b343_faces_census.txt')
REGSPEC, SATIS = d('b343_regspec_run.txt'), d('audit_b343_reg_satisfiable.txt')
PINS, INDEXQ = d('b343_pins_stepzero.txt'), d('audit_b343_index_query.txt')
HOOKS, MIRROR = d('b343_hooks.txt'), d('b343_mirror.txt')
SEAL = '31d1c873b7e34c8290c1f8973369750678aea0dedadc28d69f1a058574bda952'
MARK = '<!-- b343 update -->'
ROWNUM = '191'
GRID = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]

OWNED = [BANK, REG, F40, F81, R40, R81, CJ, CRUN, FJ, FRUN, LEDRUN, LEDRR, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, d('b343_satisfiable.json'),
         t('b343_extract.py'), t('b343_regspec.py'), t('b343_reach.py'), t('b343_crossing.py'), t('b343_ledger.py'), t('b343_correspondence.py'), t('b343_index_append.py')]

CARRIERS = [
    (t('b343_checks.py'), 'its own fixtures'),
    (d('b343_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("the draft -- component 2", d('b342_executor_draft_2026-09-06.txt'), "COMPONENT 2 \u2014 THE MAP'S NEXT REACH: the aim-map at the two heights the"),
    ('### the finer grid between 2 and 8', d('b342_executor_draft_2026-09-06.txt'), 'archimedean term and the prime sum nearly cancel) on a finer height grid'),
    ('### the crossing looked for', d('b342_executor_draft_2026-09-06.txt'), 'A_z \u2212 PR_z through zero looked for and its absence or presence stated;'),
    ("### the residual's growth with the square's rank", d('b342_executor_draft_2026-09-06.txt'), "and the identity residual's growth with the square's rank at one aimed"),
    ('### a measurement of the instrument', d('b342_executor_draft_2026-09-06.txt'), 'stated as a measurement of the instrument and not of the theorem.'),
    ('### a finer chart is a finer chart', d('b342_executor_draft_2026-09-06.txt'), 'COMPONENT 3 \u2014 WHAT IT SAYS AND DOES NOT: the modules bind nothing; a'),
    ('b334 -- the narrowest point at a = 40', d('b334_chart_run.txt'), '  reaching  a = 40    : A_z - PR_z smallest at gamma = 4.000000 : +0.000577751 [-]'),
    ('### at a = 81', d('b334_chart_run.txt'), '  reaching  a = 81    : A_z - PR_z smallest at gamma = 4.000000 : +0.000507481 [-]'),
    ("### b334's sealed grid", t('b334_aimmap.py'), 'GAMMAS = (4.0, 8.0, 12.0, 14.134725, 16.290215720390393, 20.0, 25.0, 29.551761098629115, 33.650101, 40.0,'),
    ('### the reference and grid frames', t('b334_aimmap.py'), 'FRAME_GRID = tuple(SM.GRID_AXIS[2])   # ### (8192, 32, NY): rank constant against the reference'),
    ('b317 -- the grid axis', t('b317_smear.py'), 'GRID_AXIS = ((2048, 32.0, NY_FIXED), (4096, 32.0, NY_FIXED),'),
    ('### NY fixed', t('b317_smear.py'), 'NY_FIXED = 512        # ### one NY throughout, so each axis moves one thing'),
    ('b321 -- the source exponent', t('b321_window.py'), 'import b313f_qeps_layer as EF       # noqa: E402  ### the SOURCE exponent  (rho ** +0.5)'),
    ("### the corpus's banked exponent", t('b321_window.py'), "import b313r_qeps_layer as ER       # noqa: E402  ### the corpus's banked exponent (rho ** -0.5)"),
    ('ERRATA -- quotable only with its convention named', os.path.join(PP, 'ERRATA.md'), 'is quotable only with its convention named.'),
    ("b339 -- the floor, and what the next pricing must price", d('b339_the_exponent_resolved.txt'), "### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut's `tau`, the"),
    ('the sortie -- leg 5', d('b343_ferry_2026-09-06.txt'), "LEG 5 (b343) \u2014 THE MAP'S NEXT REACH: the finer height grid"),
    ('### a finer chart is a finer chart (the ferry)', d('b343_ferry_2026-09-06.txt'), 'finer chart is a finer chart.'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### (1) the finer grid verdict', BANK, 'THE FINER GRID, THIRTEEN HEIGHTS AT TWO WIDTHS:'),
    ('### (2) the shared heights', BANK, "THE TWO HEIGHTS SHARED WITH b334's COARSE GRID REPRODUCE ITS BANKED VALUES"),
    ('### (3) the residual against the frame', BANK, 'THE RESIDUAL AGAINST THE FRAME, AT ONE AIMED SEED:'),
    ('### the rank did not move', BANK, 'THE AXIS THE DRAFT NAMES HOLDS THE RANK FIXED'),
    ('### the floor reading', BANK, "b339's FLOOR"),
    ('### (4) what it does not say', BANK, 'A FINER CHART IS A FINER CHART.'),
    ('### the reaching widths outside both reaches', BANK, "OUTSIDE THE SQUARE'S REACH AND OUTSIDE THE EPS EVALUATOR'S"),
    ('### no grade moved', BANK, 'NO GRADE MOVED. NO BAR MOVED. K6 STAYS WHERE ITS OWN ACTS LEFT IT. NOTHING DEPOSITS.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives the instruments', BANK, 'THE INSTRUMENTS AND THEIR JUDGEMENT.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED"),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('registration -- sealed before any seed', REG, 'SEALED BEFORE ANY SEED IS BUILT AT A NEW HEIGHT, BEFORE ANY FRAME IS BUILT, AND BEFORE ANY VALUE'),
    ('registration -- the grid fixed', REG, '**THE GRID, FIXED HERE AND NOT AFTER ANY VALUE:**'),
    ('registration -- the crossing defined', REG, '**THE CROSSING, DEFINED HERE:**'),
    ('registration -- the reading rule', REG, '**THE READING RULE, FIXED HERE:**'),
    ('registration -- the rank does not move on that axis', REG, "RESIDUAL'S GROWTH WITH THE SQUARE'S RANK, AND ON THAT AXIS THE RANK DOES NOT MOVE**"),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('the crossing record -- the verdict', CRUN, 'THE VERDICT ON THE FINER GRID :'),
    ('the crossing record -- a finer chart', CRUN, 'A FINER CHART IS A FINER CHART.'),
    ('the frames record -- the reading rule', FRUN, 'THE READING, BY THE SEALED RULE OF SECTION (D), AND NO WIDER:'),
    ('the frames record -- what moved', FRUN, '### WHAT MOVED AND WHAT DID NOT:'),
]

MUST_FAIL = [
    ('the bank never says the room cannot cross', BANK, '### ### **THE ROOM CANNOT CROSS.**'),
    ('the bank never says the floor is explained', BANK, "### ### **b339'S FLOOR IS EXPLAINED.**"),
    ('the bank never says a chart is a proof', BANK, '### ### **THE CHART IS A PROOF.**'),
    ('the bank never says a grade moved', BANK, '### ### **A GRADE MOVED.**'),
    ('the bank never says the square was reached at a reaching width', BANK, '### ### **THE SQUARE IS REACHED AT THE REACHING WIDTHS.**'),
]

TOOLNUM = [
    ('the finer grid, its quantities and gates', 'tools/b343_reach.py'),
    ('the crossing verdict and the shared heights', 'tools/b343_crossing.py'),
    ('the ledger block', 'tools/b343_ledger.py'),
    ('row 191', 'tools/b343_correspondence.py'),
    ('the key', 'tools/b343_index_append.py'),
    ('25 clauses', 'tools/b343_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('16181 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b343_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ("the aim-map's grid, seed, quantities and gate", 'tools/b334_aimmap.py'),
    ('the stable cut', 'tools/b319_stable.py'),
    ('the square', 'tools/b318_square.py'),
]
NEW_THIS_ACT = {'tools/b343_reach.py', 'tools/b343_crossing.py', 'tools/b343_ledger.py', 'tools/b343_correspondence.py', 'tools/b343_index_append.py',
                'tools/b343_regspec.py', 'tools/b343_extract.py', 'tools/b343_checks.py'}


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def flat(s):
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^###\s*', ' ', s.replace('\u2019', "'"))).strip()


def subsequence(old_lines, new_lines):
    i = 0
    for ln in new_lines:
        if i < len(old_lines) and ln == old_lines[i]:
            i += 1
    return i == len(old_lines)


def main():
    fails = []
    print('=' * 100)
    print("b343 -- GATE SUITE (THE MAP'S NEXT REACH: A FINER CHART, AND A MEASUREMENT OF THE INSTRUMENT)")
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
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
    bf = flat(bank)
    C = json.load(io.open(CJ, encoding='utf-8'))
    F = json.load(io.open(FJ, encoding='utf-8'))
    A40 = json.load(io.open(F40, encoding='utf-8'))
    A81 = json.load(io.open(F81, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    lb = blob_of(PP, 'FACES_LEDGER.md') or ''
    committed = MARK in lb

    print(chr(10) + '  G-GRID (F1: exactly the sealed heights at exactly the sealed widths; none added, removed or moved):')
    g40 = sorted(r['gamma'] for r in A40['rows'])
    g81 = sorted(r['gamma'] for r in A81['rows'])
    gg = g40 == GRID and g81 == GRID and A40['a'] == 40.0 and A81['a'] == 81.0 and A40['grid'] == GRID and C['grid'] == GRID
    print('    a = 40 : %s ; a = 81 : %s : %s' % (g40 == GRID, g81 == GRID, gg))
    if not gg:
        fails.append('G-GRID')

    print(chr(10) + "  G-ROUTES (F2: every aim carries its two transforms, its witness, its two prime routes and the gate's verdict):")
    need = ('arch_z', 'arch_z_route2', 'arch_z_150', 'prime_z', 'prime_z_route2', 'arch_q', 'arch_q_route2', 'finite_q', 'gate', 'room_z', 'room_q')
    gr = all(all(k in r for k in need) for r in A40['rows'] + A81['rows']) \
        and all(set(r['gate']) >= {'places_z', 'places_q', 'arch_z', 'arch_q'} for r in A40['rows'] + A81['rows']) \
        and "the like-for-like comparator's fixture fires" in io.open(R40, encoding='utf-8').read() \
        and "the like-for-like comparator's fixture fires" in io.open(R81, encoding='utf-8').read()
    print('    %s (26 aims, every field and every gate present; b334\'s comparator fixture fired at both widths)' % gr)
    if not gr:
        fails.append('G-ROUTES')

    print(chr(10) + "  G-SHARED (F3: gamma = 4 and 8 at both widths against b334's banked values):")
    gs = len(C['shared']) == 4 and C['shared_worst'] <= 1e-12 and ('%.3e' % C['shared_worst']) in bank
    print('    %d shared points ; worst relative %.3e : %s' % (len(C['shared']), C['shared_worst'], gs))
    if not gs:
        fails.append('G-SHARED')

    print(chr(10) + '  G-CROSSING (F4: the verdict by the sealed rule, recomputed from the rows):')
    live = []
    for a, J in (('40.0', A40), ('81.0', A81)):
        rows = sorted(J['rows'], key=lambda r: r['gamma'])
        signs = [(r['gamma'], r['gate']['places_z']['sign'], r['room_z']) for r in rows if r['gate']['places_z']['sign'] in ('+', '-')]
        refused = [r['gamma'] for r in rows if r['gate']['places_z']['sign'] not in ('+', '-')]
        pairs = [(signs[i][0], signs[i + 1][0]) for i in range(len(signs) - 1) if signs[i][1] != signs[i + 1][1]]
        pos = [g for g, s, v in signs if v < 0]
        # ### the crossing tool prints the width with %g; the recomputation must format it the same way or it compares
        # ### '40.0' against '40' and calls a formatting difference a disagreement.
        live.append(('A CROSSING, LOCATED at a = %g' % float(a)) if (pairs or pos) else (('REFUSED at a = %g' % float(a)) if refused else ('NO CROSSING at a = %g' % float(a))))
    gc = ' ; '.join(live) == C['verdict'] and C['verdict'] in bank
    print('    recomputed %r ; recorded %r ; in the bank %s : %s' % (' ; '.join(live), C['verdict'], C['verdict'] in bank, gc))
    if not gc:
        fails.append('G-CROSSING')

    print(chr(10) + '  G-FRAME (F5: three frames with rank and dimension; both conventions named; the identity control at each):')
    fr = F['frames']
    gf = [r['frame'] for r in fr] == [[4096, 32.0, 512], [8192, 32.0, 512], [16384, 32.0, 512]] \
        and all('rank' in r and 'dim' in r and 'R_EF' in r and 'R_ER' in r for r in fr) \
        and any('SOURCE convention' in k for k in F['remainder']) and any('CORPUS convention' in k for k in F['remainder']) \
        and all(r['identity'] < 1e-6 for r in fr)
    print('    frames %s ; both conventions named %s ; identity control below 1e-6 at each %s : %s'
          % ([r['frame'] for r in fr], any('SOURCE convention' in k for k in F['remainder']) and any('CORPUS convention' in k for k in F['remainder']),
             all(r['identity'] < 1e-6 for r in fr), gf))
    if not gf:
        fails.append('G-FRAME')

    print(chr(10) + "  G-FLOOR (F6: the reading in the sealed words and no wider; nothing concluded about tau, the taper or NY):")
    wide = [p for p in ('the taper is the origin', 'tau is the origin', 'NY is the origin', 'the floor is explained') if p.lower() in bf.lower()]
    gfl = ('untouched' in bf and "b339's floor" in bf.lower().replace("b339's floor", "b339's floor")) and not wide \
        and (('grid resolution at fixed domain is not the origin' in bf.lower()) if F['unchanged'] else ('nothing is concluded about' in bf.lower()))
    print('    the bank carries the sealed reading %s ; wider claims found %s : %s' % (('grid resolution at fixed domain is not the origin' in bf.lower()) or ('nothing is concluded about' in bf.lower()), wide, gfl))
    if not gfl:
        fails.append('G-FLOOR')

    blk = led[led.index(MARK):] if MARK in led else ''
    print(chr(10) + '  G-LEDGER (F7: one block through the writer naming S1 and K6; the ledger a true prefix of its blob):')
    pre_rows = [ln for ln in norm(lb).split(chr(10)) if ln.startswith('| ')]
    gl = (led.count(MARK) == 1 and '**S1**, constituent **K6**' in blk and 'NO GRADE MOVED' in blk and norm(led).startswith(norm(lb).rstrip(chr(10)))
          and all(ln in norm(led) for ln in pre_rows) and 'WRITTEN' in io.open(LEDRUN, encoding='utf-8').read() and 'DUPLICATE' in io.open(LEDRR, encoding='utf-8').read())
    print('    mark once %s ; names S1/K6 %s ; prefix of blob %s (committed %s) ; rows preserved %d : %s'
          % (led.count(MARK) == 1, '**S1**, constituent **K6**' in blk, norm(led).startswith(norm(lb).rstrip(chr(10))), committed, len(pre_rows), gl))
    if not gl:
        fails.append('G-LEDGER')

    r191 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| %s |' % ROWNUM)]
    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    headb = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r191) == 1 and 'NO TERMINAL, AND THE REASON: A CHART AND AN INSTRUMENT MEASUREMENT' in r191[0] and 'M-2' in r191[0] and norm(tbl).startswith(norm(headb).rstrip(chr(10)))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTAPROOF (one row; the must-not-hit queries NO KEY; the answer says a finer chart, the reaches, no grade moved):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('map-next-reach')
    gk = o.count('act      :') == 1 and 'A FINER CHART IS A FINER CHART' in o and "OUTSIDE THE SQUARE'S AND THE EPS EVALUATOR'S REACH" in o and 'NO GRADE MOVED' in o
    for s in ('the room cannot cross', 'the floor explained', 'the residual grows with rank'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOTAPROOF')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (owner instruments, sealed files, the deposit, TECHNE, HANDOFF: no tracked change beyond the act's files):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md',
              'tools/b334_aimmap.py', 'tools/b326_windows.py', 'tools/b321_window.py', 'tools/b319_stable.py', 'tools/b318_square.py', 'tools/b317_smear.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b334_the_aim_map.txt', 'data/b339_the_exponent_resolved.txt', 'data/b334_chart_run.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('FACES_LEDGER.md')]
    st_t = git(TC, 'status', '--porcelain').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond the ledger) %s ; TECHNE %r ; deposit %r : %s' % (st_r, st_s, st_p, st_t, dep, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the instrument, the crossing, the block, the row, the key and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b343_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    sat_ok = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8', errors='replace').read()
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [F40, F81, R40, R81, CJ, FJ, LEDRUN, LEDGER, CORR, IDX, BANK])
        how = 'file times (pre-commit; no post-seal marking on this registration, so the seal time stands)'
    else:
        pre = io.open(d('b343_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b343_checks_run.txt')) else ''
        after = 'the instrument, the crossing, the block, the row, the key and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and sat_ok and after
    print('    seal verifies %s ; hash equals the literal %s ; the audit reads JOINTLY SATISFIABLE %s ; the instrument, the crossing, the block, the row, the key and the bank after the seal %s [%s] : %s'
          % (intact, rawhash == SEAL, sat_ok, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    if committed:
        print('    the ledger committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    the ledger not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    checks = []
    for a, J in (('40.0', A40), ('81.0', A81)):
        n = C['per_width'][a]['narrowest']
        checks.append(('a = %s narrowest %.2f %+.9f' % (a, n['gamma'], n['room_z']),
                       ('%+.9f' % n['room_z']) in bank and ('%.2f' % n['gamma']) in bank))
    checks.append(('shared worst %.3e' % C['shared_worst'], ('%.3e' % C['shared_worst']) in bank))
    checks.append(('the rank %d' % fr[0]['rank'], ('%d' % fr[0]['rank']) in bank))
    checks.append(('the residual under EF %s' % [round(r['R_EF'], 9) for r in fr], all(('%+.9f' % r['R_EF']) in bank for r in fr)))
    checks.append(('the relative changes %.3e / %.3e' % (F['rel_EF'], F['rel_ER']), ('%.3e' % max(F['rel_EF'], F['rel_ER'])) in bank))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    checks.append(('26 aims', '26 aims' in bank and len(A40['rows']) + len(A81['rows']) == 26))
    for what, ok in checks:
        print('    %-52s %s' % (what[:52], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded and numbered):')
    once_ok = all(os.path.exists(p) for p in [R40, R81, F40, F81, CJ, CRUN, FJ, FRUN, LEDRUN, LEDRR, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b343_fine_40_run2.txt'))
    print('    %s' % once_ok)
    if not once_ok:
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
            print('    ### %-40s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for h in (ch + sh)[:6]:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-36s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                        ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                     if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib = idx[idx.index("# ### THE MAP'S NEXT REACH (b343"):idx.index('# ### THE TWO RULES AS MODULES (b342')] if "# ### THE MAP'S NEXT REACH (b343" in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the ledger block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, r191[0] if r191 else ''), ('the ledger block', blk), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-18s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED-STEM:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED-STEM')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-64s %-34s exists=%s tracked=%s' % (what[:64], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the block and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b343_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, r191[0] if r191 else ''), ('the ledger block', blk), ('the index row', ib)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, gh, ua = hedge_audit.audit(path)
        print('    %-36s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(gh), len(ua)))
        for s2 in gh:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
