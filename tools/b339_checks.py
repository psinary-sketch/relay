# -*- coding: utf-8 -*-
"""b339_checks.py -- THE GATE SUITE FOR THE EXPONENT RESOLVED (LEG 1: A PRICE, UNAFFORDABLE AT THE SEALED CEILING).

### ### **THE ARMS (registration (F), F1-F8):** `G-PRICE` (the inputs located, the ladder reproduced, the rate and price
### recomputed live through the imported fitter, the ceiling as sealed), `G-GATE` (no cell fits, no frame built, no run
### file of a resolve tool exists), `G-RUN` (not exercised: the gate closed the run), `G-VERDICT` (UNAFFORDABLE everywhere
### the act speaks), `G-ERRATUM` (ERRATA byte-identical to its blob), `G-LEDGER` (one block, append-only), `G-ROW` /
### `G-ANCESTOR`, `G-KEY` / `G-NOPREFERENCE`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`, `G-HOOK` / `G-MIRROR`, `G-NUMBERS`,
### `G-ONCE`, the struck-clause and stem sweeps, `G-SHARED`, `G-TOOLNUM`, the hedge audit, the must-fail fixtures.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import b322_ladder as LA  # noqa: E402
import b317_smear as SM   # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
ERRATA = os.path.join(PP, 'ERRATA.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b339_the_exponent_resolved.txt')
REG = d('b339_registration_2026-09-06.txt')
EXTRACT = d('b339_extract_notes.txt')
PRUN, PJ = d('b339_price_run.txt'), d('b339_price.json')
LRUN, LJ = d('b339_limit_run.txt'), d('b339_limit.json')
LEDRUN, LEDRR = d('b339_ledger_run.txt'), d('b339_ledger_rerun.txt')
CORR, CORRR = d('b339_corr_run.txt'), d('b339_corr_rerun.txt')
IDX, IDXR = d('b339_index_run.txt'), d('b339_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b339_ferry_scan.txt'), d('b339_reg_termscan.txt'), d('b339_reg_gate.txt')
CENSUS, FCEN = d('b339_census.txt'), d('b339_faces_census.txt')
REGSPEC, SATIS = d('b339_regspec_run.txt'), d('audit_b339_reg_satisfiable.txt')
PINS, INDEXQ = d('b339_pins_stepzero.txt'), d('audit_b339_index_query.txt')
HOOKS, MIRROR = d('b339_hooks.txt'), d('b339_mirror.txt')
SEAL = '1182f2638287bed831eec0ddec1b5b9b70ebb49cb25ee9fbd10f7f0a21310270'
MARK = '<!-- b339 update -->'
ROWNUM = '187'

OWNED = [BANK, REG, PRUN, PJ, LRUN, LJ, LEDRUN, LEDRR, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, d('b339_satisfiable.json'),
         t('b339_extract.py'), t('b339_regspec.py'), t('b339_price.py'), t('b339_limit.py'), t('b339_ledger.py'), t('b339_correspondence.py'), t('b339_index_append.py')]

CARRIERS = [
    (t('b339_checks.py'), 'its own fixtures'),
    (d('b339_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("b321_window -- the source exponent", t('b321_window.py'), 'import b313f_qeps_layer as EF       # noqa: E402  ### the SOURCE exponent  (rho ** +0.5)'),
    ("### the corpus's banked exponent", t('b321_window.py'), "import b313r_qeps_layer as ER       # noqa: E402  ### the corpus's banked exponent (rho ** -0.5)"),
    ('### the source copy, its line', t('e16/b313f_qeps_layer.py'), 'out[k] = float((lam2 / (1 - lam2) * (r ** 0.5) * I).sum())'),
    ("### the corpus copy, its line", t('e16/b313r_qeps_layer.py'), 'out[k] = float((lam2 / (1 - lam2) * (r ** -0.5) * I).sum())'),
    ('b321 -- frame 5 of the ladder', d('b321_the_window_opened.txt'), '    262      5        8.599100561        0.182113440        0.023223882'),
    ('### a = 1.3 in the separation table', d('b321_the_window_opened.txt'), '    1.3    0.158889558      0.157908477      0.000981080    0.023223882      PASSES'),
    ('### a = 1.35', d('b321_the_window_opened.txt'), '    1.35   0.186481766      0.184544767      0.001936999    0.020792865      PASSES'),
    ('### a = 1.41', d('b321_the_window_opened.txt'), '    1.41   0.221284108      0.217290580      0.003993528    0.018807781      PASSES'),
    ('b322 -- the price is the ratio', d('b322_the_membership.txt'), 'PRICE IS THE RATIO.**'),
    ('### a price is not a prediction', d('b322_the_membership.txt'), 'A PRICE IS NOT A PREDICTION.**'),
    ('### an extrapolation labelled as one', d('b322_the_membership.txt'), 'IT IS AN EXTRAPOLATION OF A FITTED SLOPE AND IT IS LABELLED AS ONE.'),
    ('### the fitter', t('b322_ladder.py'), 'def fit_power(xs, ys):'),
    ('b323 -- the two rates', d('b323_the_fold.txt'), "rate is now known: the instrument's own residual falls as `X^-1.324` while the unit's falls as"),
    ('b317 -- the domain axis', t('b317_smear.py'), 'DOMAIN_AXIS = ((1024, 8.0, NY_FIXED), (2048, 16.0, NY_FIXED), (4096, 32.0, NY_FIXED),'),
    ('ERRATA -- quotable only with its convention named', ERRATA, 'is quotable only with its convention named.'),
    ('the sortie -- leg 1', d('b339_ferry_2026-09-06.txt'), 'LEG 1 (b339) \u2014 THE EXPONENT RESOLVED: price the domain the'),
    ('### the three verdicts', d('b339_ferry_2026-09-06.txt'), 'prefers \u2014 (RESOLVED, the convention named, its consequence for'),
    ('### the sealed rule governs', d('b339_ferry_2026-09-06.txt'), 'bar moved; the sealed rule from b322 governs.'),
    ('### (L1) stated', d('b339_ferry_2026-09-06.txt'), 'navigator\'s expectations, registered here: (L1) the price fits'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### (1) the verdict', BANK, 'THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED.'),
    ('### the question stays under-resolved', BANK, "rule, with the new figure its price."),
    ('### (2) the price labelled', BANK, 'THE PRICE, PER CELL, AN EXTRAPOLATION OF A FITTED SLOPE AND LABELLED AS ONE'),
    ('### the gate closes the run', BANK, 'the price) closes the run.'),
    ('### (3) the side reading labelled', BANK, 'THE SIDE READING, LABELLED, NOT A VERDICT ARM'),
    ('### not a preference', BANK, 'THAT IS NOT A PREFERENCE:'),
    ('### the floor', BANK, 'floor is what the next pricing must price;'),
    ('### (4) L1 not met', BANK, "NOT MET at this ceiling**"),
    ("### the seat's not met", BANK, 'NOT MET** (it'),
    ('### (5) the row, the block, the key', BANK, 'THE ROW, THE BLOCK, THE KEY:'),
    ('### no bar moved', BANK, 'NO BAR MOVED. NO CANDIDATE PREFERRED. NO GRADE CONFERRED. NO ACT RE-VERDICTED. TECHNE NOT'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives the instruments', BANK, 'THE INSTRUMENTS AND THEIR JUDGEMENT.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED:"),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, 'NEXT, BY THE SORTIE: LEG 2, b340, THE LI FAMILY CONTROL.'),
    ('registration -- sealed before the price', REG, 'SEALED BEFORE THE PRICE IS COMPUTED, BEFORE ANY FRAME IS BUILT, AND BEFORE ANY VALUE OF THE'),
    ('registration -- the ceiling', REG, "**ONE ACT'S CEILING, FIXED HERE AND NOT AFTER THE PRICE:**"),
    ('registration -- the split criterion', REG, '**THE SPLIT CRITERION, FIXED HERE:**'),
    ('registration -- the gate', REG, '**THE GATE ON THE RUN:**'),
    ('registration -- unaffordable defined', REG, "**UNAFFORDABLE** when no cell's `X_req` is at or below"),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('price run -- the gate', PRUN, 'THE GATE ON THE RUN (sealed): the cells whose X_req <= 512 : NONE -- UNAFFORDABLE'),
    ('price run -- the ladder reproduced', PRUN, 'THE LADDER REPRODUCED FROM THE RECORD AT EVERY CELL : YES'),
    ('limit run -- not a verdict', LRUN, 'NOT A VERDICT. ### NO CANDIDATE PREFERRED. ### REPORTED FOR THE NEXT PRICING.'),
]

MUST_FAIL = [
    ('the bank never says a bar moved', BANK, '### ### **A BAR MOVED.**'),
    ("the bank never says the source's formula is proved", BANK, "### ### **THE SOURCE'S FORMULA IS PROVED.**"),
    ('the bank never says the price fits', BANK, '### ### **THE PRICE FITS.**'),
    ('the bank never says the identity prefers a convention', BANK, "### ### **THE IDENTITY PREFERS THE SOURCE'S CONVENTION.**"),
    ('the bank never says RESOLVED as its verdict', BANK, '### ### **THE VERDICT: RESOLVED.**'),
    ('the bank never says a price is a prediction', BANK, '### ### **A PRICE IS A PREDICTION.**'),
]

TOOLNUM = [
    ('the price per cell, the rates, the ratios, the ceiling', 'tools/b339_price.py'),
    ('the limit reading, the offsets, the ratios of the descent', 'tools/b339_limit.py'),
    ('row 187', 'tools/b339_correspondence.py'),
    ('the ledger block', 'tools/b339_ledger.py'),
    ('the key', 'tools/b339_index_append.py'),
    ('25 clauses', 'tools/b339_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('15337 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b339_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the fitter', 'tools/b322_ladder.py'),
    ("the record's weil and Tr", 'tools/b320_run.py'),
]
NEW_THIS_ACT = {'tools/b339_price.py', 'tools/b339_limit.py', 'tools/b339_ledger.py', 'tools/b339_correspondence.py', 'tools/b339_index_append.py',
                'tools/b339_regspec.py', 'tools/b339_extract.py', 'tools/b339_checks.py'}


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def subsequence(old_lines, new_lines):
    i = 0
    for ln in new_lines:
        if i < len(old_lines) and ln == old_lines[i]:
            i += 1
    return i == len(old_lines)


def nums_in(s):
    return [float(x) for x in re.findall(r'-?\d+(?:\.\d+)?', s)]


def main():
    fails = []
    print('=' * 100)
    print('b339 -- GATE SUITE (THE EXPONENT RESOLVED: A PRICE UNDER b322\'s SEALED RULE, UNAFFORDABLE AT THE SEALED CEILING)')
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
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    P = json.load(io.open(PJ, encoding='utf-8'))
    L = json.load(io.open(LJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    err = io.open(ERRATA, encoding='utf-8', errors='replace').read()
    lb = blob_of(PP, 'FACES_LEDGER.md') or ''
    committed = MARK in lb
    rec = json.load(io.open(d('b320_rows.json'), encoding='utf-8'))
    XS = [fk[1] for fk in SM.DOMAIN_AXIS]

    print(chr(10) + '  G-PRICE (F1: the inputs from the record, the ladder reproduced, the rate and the price recomputed live through the imported fitter, the ceiling as sealed):')
    weil = {float(r['a']): float(r['weil']) for r in rec['rows']}
    gp = P['ceiling_x'] == 512.0 and P['split'] == 0.5 and P['reproduces'] and P['xs'] == XS and '`X = 512`, `N = 65536`' in reg and '`R <= s/2`' in reg
    for k, c in P['cells'].items():
        a = float(k)
        tr = [float(x) for x in rec['axes'][k]['domain']]
        R = [weil[a] - x - c['int_ef'] for x in tr]
        p, A, rms = LA.fit_power(XS, R)
        xr = 128.0 * (R[-1] / (0.5 * c['s'])) ** (1.0 / abs(p))
        same = abs(p - c['p']) < 1e-12 and abs(xr - c['x_req']) < 1e-6 and max(abs(u - v) for u, v in zip(R, c['R'])) < 1e-12
        gp = gp and same and (xr > 512.0) == (not c['fits'])
        print('    a = %-5s  R recomputed equal %s ; p live %.6f vs recorded %.6f ; X_req live %.1f vs recorded %.1f ; fits %s : %s' % (k, max(abs(u - v) for u, v in zip(R, c['R'])) < 1e-12, p, c['p'], xr, c['x_req'], c['fits'], same))
    print('    ceiling 512 %s ; split 1/2 %s ; ladder reproduced %s ; the registration names both : %s' % (P['ceiling_x'] == 512.0, P['split'] == 0.5, P['reproduces'], ('`X = 512`, `N = 65536`' in reg and '`R <= s/2`' in reg)))
    print('    %s' % gp)
    if not gp:
        fails.append('G-PRICE')

    print(chr(10) + '  G-GATE (F2: no cell fits; no frame built; no resolve run file exists; no cell added or moved after the price):')
    gg = P['fits'] == [] and all(not c['fits'] and c['x_req'] > 512.0 for c in P['cells'].values()) and not os.path.exists(d('b339_resolve_run.txt')) and not os.path.exists(t('b339_resolve.py')) and sorted(P['cells'], key=float) == [str(x) for x in rec['covered']]
    print('    fits %s ; resolve tool absent %s ; the cells are the record\'s covered cells %s : %s' % (P['fits'], not os.path.exists(t('b339_resolve.py')), sorted(P['cells'], key=float) == [str(x) for x in rec['covered']], gg))
    if not gg:
        fails.append('G-GATE')
    print(chr(10) + '  G-RUN (F3): NOT EXERCISED -- the gate closed the run; nothing to check and nothing claimed.')

    print(chr(10) + '  G-VERDICT (F4: UNAFFORDABLE everywhere the act speaks -- the price run, the bank, the row, the ledger block, the index row; the side reading labelled):')
    r187 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| %s |' % ROWNUM)]
    blk = led[led.index(MARK):] if MARK in led else ''
    ib = idx[idx.index('# ### THE EXPONENT PRICED (b339'):idx.index('# ### THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD (b338')] if '# ### THE EXPONENT PRICED (b339' in idx else ''
    gv = ('NONE -- UNAFFORDABLE' in io.open(PRUN, encoding='utf-8').read() and 'THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL' in bank
          and len(r187) == 1 and 'UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL' in r187[0] and 'NO CANDIDATE PREFERRED' in r187[0]
          and 'UNAFFORDABLE at the sealed ceiling at every covered cell' in blk and 'NO CANDIDATE PREFERRED' in blk
          and 'UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL' in ib and 'NO CANDIDATE PREFERRED' in ib
          and 'NOT A VERDICT' in io.open(LRUN, encoding='utf-8').read() and 'NOT A VERDICT ARM' in bank)
    print('    %s' % gv)
    if not gv:
        fails.append('G-VERDICT')

    print(chr(10) + '  G-ERRATUM (F5: the verdict is not RESOLVED, so ERRATA.md is byte-identical to its blob):')
    eb = blob_of(PP, 'ERRATA.md') or ''
    ge = norm(err) == norm(eb) and '<!-- b339' not in err
    print('    identical %s ; no b339 mark %s : %s' % (norm(err) == norm(eb), '<!-- b339' not in err, ge))
    if not ge:
        fails.append('G-ERRATUM')

    print(chr(10) + '  G-LEDGER (F6: one block through the writer naming F2 and K6; the ledger a true prefix of its blob; every row line present):')
    pre_rows = [ln for ln in norm(lb).split(chr(10)) if ln.startswith('| ')]
    gl = (led.count(MARK) == 1 and '**F2** (the Sonin margin) and **S1**, constituent **K6**' in blk and norm(led).startswith(norm(lb).rstrip(chr(10)))
          and all(ln in norm(led) for ln in pre_rows) and 'WRITTEN' in io.open(LEDRUN, encoding='utf-8').read() and 'DUPLICATE' in io.open(LEDRR, encoding='utf-8').read())
    print('    mark once %s ; names F2 and K6 %s ; prefix of blob %s (committed %s) ; rows preserved %d ; written then duplicate %s : %s'
          % (led.count(MARK) == 1, '**F2** (the Sonin margin) and **S1**, constituent **K6**' in blk, norm(led).startswith(norm(lb).rstrip(chr(10))), committed, len(pre_rows), 'WRITTEN' in io.open(LEDRUN, encoding='utf-8').read(), gl))
    if not gl:
        fails.append('G-LEDGER')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r187) == 1 and 'NO TERMINAL, AND THE REASON: A PRICE, NOT A MEASUREMENT' in r187[0] and 'M-2' in r187[0] and norm(tbl).startswith(norm(head).rstrip(chr(10)))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOPREFERENCE (one row; the must-not-hit queries NO KEY; the answer says a price is not a prediction, no candidate preferred):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('exponent-resolved')
    gk = o.count('act      :') == 1 and 'A PRICE IS NOT A PREDICTION' in o and 'NO CANDIDATE PREFERRED' in o and 'UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL' in o
    for s in ('the convention resolved', "the source's convention preferred", 'the exponent measured'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOPREFERENCE')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (owner instruments, sealed files, the deposit, TECHNE, HANDOFF, the banks read: no tracked change beyond the act's files):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md',
              'tools/e16/b313f_qeps_layer.py', 'tools/e16/b313r_qeps_layer.py', 'tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py',
              'tools/b319_stable.py', 'tools/b320_weil.py', 'tools/b320_run.py', 'tools/b321_window.py', 'tools/b322_ladder.py', 'data/b320_rows.json',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b321_the_window_opened.txt', 'data/b322_the_membership.txt', 'data/b323_the_fold.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('FACES_LEDGER.md')]
    st_t = git(TC, 'status', '--porcelain').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond the ledger) %s ; TECHNE %r ; deposit %r : %s' % (st_r, st_s, st_p, st_t, dep, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the price, the side reading, the block, the row, the key and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b339_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b339_price.py'), PRUN, PJ, LRUN, LEDRUN, LEDGER, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b339_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b339_checks_run.txt')) else ''
        after = 'the price, the side reading, the block, the row, the key and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the price, the side reading, the block, the row, the key and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
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
    for k in ('1.3', '1.35', '1.41'):
        c = P['cells'][k]
        ln = [x for x in bank.splitlines() if x.strip().startswith('###     a = %s' % k)]
        got = nums_in(ln[0].split(':', 1)[1].replace('R(128)/s', 'ratio').replace('X^', 'X')) if ln else []
        want = [c['ratio_now'], c['p'], c['rms'], c['p_last'], c['x_req'], c['x_req'] / 128.0, c['x_req_last']]
        ok = len(got) >= 7 and all(abs(g - w) <= 0.006 * max(1.0, abs(w)) for g, w in zip(got[:7], want))
        checks.append(('the price line at a = %s' % k, ok))
    lim_want = [L['1.3']['off_ef'] / P['cells']['1.3']['s'], L['1.3']['off_er'] / P['cells']['1.3']['s'], L['1.35']['off_ef'] / P['cells']['1.35']['s'], L['1.35']['off_er'] / P['cells']['1.35']['s'],
                L['1.41']['off_ef'] / P['cells']['1.41']['s'], L['1.41']['off_er'] / P['cells']['1.41']['s']]
    seg = bank[bank.index('puts `m_inf` ABOVE BOTH CANDIDATES'):bank.index('THAT IS NOT A PREFERENCE')]
    got = [float(x) for x in re.findall(r'`(\d+\.\d+) s`', seg)]
    checks.append(('the six limit offsets in separations', len(got) == 6 and all(abs(g - w) <= 0.06 for g, w in zip(got, lim_want))))
    rat = [float(x) for x in re.findall(r'\((\d\.\d+), (\d\.\d+), (\d\.\d+) at `a = 1.3`\)', bank)[0]] if re.search(r'\((\d\.\d+), (\d\.\d+), (\d\.\d+) at `a = 1.3`\)', bank) else []
    checks.append(('the three descent ratios at a = 1.3', len(rat) == 3 and all(abs(g - w) <= 0.006 for g, w in zip(rat, L['1.3']['ratios']))))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    checks.append(('the cheapest cell X = 812 against 512, factor 6.34', abs(P['cells']['1.41']['x_req'] - 812) < 0.5 and abs(P['cells']['1.41']['x_req'] / 128.0 - 6.34) < 0.005 and '`X = 812` against a ceiling of' in bank and 'a factor `6.34`' in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded):')
    once_ok = all(os.path.exists(p) for p in [PRUN, PJ, LRUN, LJ, LEDRUN, LEDRR, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b339_price_run2.txt')) and not os.path.exists(d('b339_corr_rerun2.txt'))
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

    print(chr(10) + '  G-STEM-APPENDED (row %s, the ledger block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, r187[0] if r187 else ''), ('the ledger block', blk), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-18s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
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
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-64s %-34s exists=%s tracked=%s' % (what[:64], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the block and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b339_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, r187[0] if r187 else ''), ('the ledger block', blk), ('the index row', ib)):
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
