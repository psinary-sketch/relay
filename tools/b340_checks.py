# -*- coding: utf-8 -*-
"""b340_checks.py -- THE GATE SUITE FOR THE LI FAMILY CONTROL (LEG 2 OF THE SORTIE b339-b343).

### ### **THE ARMS (registration (F), F1-F8):** `G-BUILT` (the two fixtures pass on the record run and fail on their altered
### inputs), `G-LAWFUL` (the three failed conditions and the two lists stated; a must-fail on the family lawful), `G-BAR` (the bar
### as sealed recomputed from the record at every index; the verdict by (D)'s rule; the diagnostic's reading beside it and not
### in place of it), `G-INDICES` (the keystone's rows, read live), `G-SCOPE` (the certificate at its line; the bench's sentence;
### no Sonin margin), `G-LEDGER`, `G-ROW` / `G-ANCESTOR`, `G-KEY` / `G-NOTTHEOBJECT`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`,
### `G-HOOK` / `G-MIRROR`, `G-NUMBERS`, `G-ONCE`, the struck-clause and stem sweeps, `G-SHARED`, `G-TOOLNUM`, the hedge audit,
### the must-fail fixtures; re-run after the push.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

import mpmath as mp

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
KEY = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')
MONO = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b340_the_li_family_control.txt')
REG = d('b340_registration_2026-09-06.txt')
EXTRACT = d('b340_extract_notes.txt')
CRUN1, CRUN2, CRUN3, CJ = d('b340_control_run.txt'), d('b340_control_run2.txt'), d('b340_control_run3.txt'), d('b340_control.json')
DRUN, DJ = d('b340_diagnose_run.txt'), d('b340_diagnose.json')
LEDRUN, LEDRR = d('b340_ledger_run.txt'), d('b340_ledger_rerun.txt')
CORR, CORRR = d('b340_corr_run.txt'), d('b340_corr_rerun.txt')
CORRX1, CORRX2 = d('b340_corr_run_refused.txt'), d('b340_corr_run_refused2.txt')
IDX, IDXR = d('b340_index_run.txt'), d('b340_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b340_ferry_scan.txt'), d('b340_reg_termscan.txt'), d('b340_reg_gate.txt')
CENSUS, FCEN = d('b340_census.txt'), d('b340_faces_census.txt')
REGSPEC, SATIS = d('b340_regspec_run.txt'), d('audit_b340_reg_satisfiable.txt')
PINS, INDEXQ = d('b340_pins_stepzero.txt'), d('audit_b340_index_query.txt')
HOOKS, MIRROR = d('b340_hooks.txt'), d('b340_mirror.txt')
SEAL = '945b145cc84b76f5b8df135d2fbcd2461b48ebe29a45675d0e303482a1f9e116'
MARK = '<!-- b340 update -->'
ROWNUM = '188'

OWNED = [BANK, REG, CRUN1, CRUN2, CRUN3, CJ, DRUN, DJ, LEDRUN, LEDRR, CORR, CORRR, CORRX1, CORRX2, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, d('b340_satisfiable.json'),
         t('b340_extract.py'), t('b340_regspec.py'), t('b340_li_control.py'), t('b340_diagnose.py'), t('b340_ledger.py'), t('b340_correspondence.py'), t('b340_index_append.py')]

CARRIERS = [
    (t('b340_checks.py'), 'its own fixtures'),
    (d('b340_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ('the source -- (3.2)', d('b327_source_text.txt'), 'The special test functions Gn(s) \u2208 L corresponding to the Li coe\ufb03cients are'),
    ('### Theorem 3.1', d('b327_source_text.txt'), 'Theorem 3.1. Let\u03c0 be an irreducible cuspidal unitary automorphic representation of GL(N ),'),
    ('### (4.6)', d('b327_source_text.txt'), '\u03bbn(\u03c0) = S\u221e(n,\u03c0 ) \u2212Sf (n,\u03c0 \u2228) +\u03b4(\u03c0), (4.6)'),
    ('### (4.11)', d('b327_source_text.txt'), '2j )\u03b6 \u2217(j), (4.11)'),
    ('the keystone -- the split', KEY, 'f_A(s) = log s + log\u0393(s/2) \u2212 (s/2)\u00b7log \u03c0  (archimedean)'),
    ('### the table head', KEY, '| n | \u03bb_A(n) | \u03bb_Z(n) | margin \u03bb_n | agree digits |'),
    ('### n = 1', KEY, '| 1 | \u22120.554119955935 | 0.577215664902 | **0.0230957089661** | 258 |'),
    ('the bench -- f_A', BENCH, '    return mp.log(s) + mp.loggamma(s / 2) - (s / 2) * mp.log(mp.pi)'),
    ('### an instrument, not an argument', BENCH, 'print("respects (Keiper 1992; BALANCE_AND_POSITIVITY sec V). This is an instrument, not an argument.")'),
    ('b327 -- the derivation (d)', d('b327_the_faces_ledger.txt'), '### ### **`lambda_A(n) = S_inf(n) + 1`**, and `lambda_Z(n) = -S_f(n)`.'),
    ('### the family outside the class', d('b327_the_faces_ledger.txt'), "function whose inverse Mellin transform has no compact support, so the Li family lies outside"),
    ('### the fourth control priced', d('b327_the_faces_ledger.txt'), '### ### **THE FOURTH CONTROL, PRICED AND NOT RUN:** ### the explicit formula closed on the Li family'),
    ('b326 -- the kernel', t('b326_windows.py'), 'def kernel_zeta(U):'),
    ("b333 -- the corpus's A is the source's W_inf", d('b333_the_archimedean_term_derived.txt'), "### `tau = 0.5, 3, 17`, worst `1.972e-31`. ### **THE CORPUS'S `A(f)` IS THE SOURCE'S `W_inf(f) = -W_R(f)`**,"),
    ('b321 -- the arrangement', d('b321_the_window_opened.txt'), '### and the identity is ### **`Z = P - PR + A`**.'),
    ("b320 -- Theorem 1's three conditions", d('b320_the_lawful_function.txt'), "### ### 1.41.** ### Theorem 1 asks three things of the seed. ### **THE SUPPORT CONDITION IS THE ONLY"),
    ('the ledger -- row R4, the certificate', LEDGER, "DEPOSITED -- section 27.3, lines 1779 and 1796; compiled as STRUCTURE only, `Register4_positivity`"),
    ('the monograph -- the certificate', MONO, "partialPositivity_finiteRange` (v0.8.0) certifies \u03bb_n \u2265 0 for n up to Voros's detection threshold N\u2080(T) \u2248 2T\u00b2, with the on-line term's nonnegativity proved"),
    ('the sortie -- leg 2', d('b340_ferry_2026-09-06.txt'), 'LEG 2 (b340) \u2014 THE LI FAMILY CONTROL: the Li test functions'),
    ('### the two verdicts', d('b340_ferry_2026-09-06.txt'), 'values. A fourth control if it holds; the differing constituent'),
    ('### (L2)', d('b340_ferry_2026-09-06.txt'), 'fourth control holds with the pole constant carried; (L3) the'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### (1) the verdict as sealed', BANK, 'THE VERDICT AS SEALED: THE DIFFERING CONSTITUENT -- A QUADRATURE FAILURE, THE GATE REFUSING THE SEALED'),
    ('### (2) the identity by the theta route', BANK, 'THE IDENTITY ITSELF, BY THE THETA ROUTE AGAINST TWO INDEPENDENT ROUTES:'),
    ('### (3) the diagnosis', BANK, 'THE DIAGNOSIS, A READING BESIDE THE VERDICT AND NOT IN ITS PLACE**'),
    ('### the bar not rewritten', BANK, 'THE BAR AS SEALED IS NOT MET AND IS NOT REWRITTEN.'),
    ('### (4) not in the lawful class', BANK, 'THE LI TEST FUNCTIONS ARE BUILT, AND THEY ARE NOT IN THE LAWFUL CLASS:'),
    ('### which apply', BANK, 'WHICH CERTIFICATIONS APPLY:'),
    ('### which do not', BANK, 'WHICH DO NOT:'),
    ('### (5) the certificate restated', BANK, "THE DEPOSIT'S FINITE-RANGE POSITIVITY, RESTATED AT ITS SCOPE BESIDE THE VALUES:"),
    ('### (6) L2 scored', BANK, "THE NAVIGATOR'S (L2)"),
    ('### the seat scored', BANK, "THIS SEAT'S"),
    ('### what stays owed', BANK, 'WHAT STAYS OWED ON `W-ORD-LI-FAMILY-CONTROL`:'),
    ('### no grade moved', BANK, 'NO GRADE MOVED. NO BAR REWRITTEN. NO SONIN MARGIN ON THE LI FAMILY. NO ACT RE-VERDICTED. TECHNE NOT'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives the instruments', BANK, 'THE INSTRUMENTS AND THEIR JUDGEMENT.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED:"),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, 'NEXT, BY THE SORTIE: LEG 3, b341, THE TWO COEFFICIENTS.'),
    ('registration -- sealed before the build', REG, 'SEALED BEFORE THE LI TEST FUNCTIONS ARE BUILT, BEFORE THE KERNEL IS INTEGRATED AGAINST ANY OF'),
    ('registration -- not in the lawful class', REG, "THEIR LAWFULNESS BY THE SOURCE'S DEFINITION, STATED: THEY ARE NOT IN THE LAWFUL CLASS.**"),
    ('registration -- the bar', REG, "**THE BAR, b327's IDENTITY:**"),
    ('registration -- the differing constituent defined', REG, '**THE DIFFERING CONSTITUENT** when it'),
    ('registration -- a bar not met is not rewritten', REG, 'A bar not met is not rewritten.'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('run 3 -- the verdict', CRUN3, 'VERDICT: THE DIFFERING CONSTITUENT -- the bar fails at'),
    ('run 3 -- what differs', CRUN3, 'what differs: a quadrature failure (the gate refusing).'),
    ('run 3 -- no zero side', CRUN3, 'NO ZERO SIDE AND NO FINITE SIDE EVALUATED ; NO SONIN MARGIN DEFINED ON THE FAMILY ; NO GRADE MOVED'),
    ('the diagnostic -- the reading', DRUN, 'READING: the sealed refinement route (Gauss-Legendre on an infinite panel with a logarithmic tail) is what failed, and not the identity; the bar as sealed is NOT MET and is not rewritten.'),
]

MUST_FAIL = [
    ('the bank never says the family is lawful', BANK, '### ### **THE LI FAMILY IS LAWFUL.**'),
    ('the bank never says the Sonin margin is defined on it', BANK, '### ### **THE SONIN MARGIN IS DEFINED ON THE LI FAMILY.**'),
    ('the bank never says the bar is rewritten', BANK, '### ### **THE BAR IS REWRITTEN.**'),
    ('the bank never confers the fourth control as its verdict', BANK, '### ### **VERDICT: A FOURTH CONTROL.**'),
    ('the bank never says lambda_n >= 0 for all n', BANK, '### ### **LAMBDA_N >= 0 FOR ALL N.**'),
    ('the bank never says the trail is paid', BANK, '### ### **W-ORD-LI-FAMILY-CONTROL IS PAID.**'),
]

TOOLNUM = [
    ('I(n), the fixtures, the bar, the drift, the columns', 'tools/b340_li_control.py'),
    ('the tail panel, the reading', 'tools/b340_diagnose.py'),
    ('row 188', 'tools/b340_correspondence.py'),
    ('the ledger block', 'tools/b340_ledger.py'),
    ('the key', 'tools/b340_index_append.py'),
    ('26 clauses', 'tools/b340_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('17784 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b340_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the bench loader and (4.11)', 'tools/b327_bridge.py'),
    ('the noise-floor gate', 'tools/noise_floor.py'),
]
NEW_THIS_ACT = {'tools/b340_li_control.py', 'tools/b340_diagnose.py', 'tools/b340_ledger.py', 'tools/b340_correspondence.py', 'tools/b340_index_append.py',
                'tools/b340_regspec.py', 'tools/b340_extract.py', 'tools/b340_checks.py'}


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


def main():
    fails = []
    print('=' * 100)
    print('b340 -- GATE SUITE (THE LI FAMILY CONTROL: THE DIFFERING CONSTITUENT AS SEALED, THE IDENTITY BY ONE ROUTE, THE DIAGNOSIS BESIDE IT)')
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
    J = json.load(io.open(CJ, encoding='utf-8'))
    DG = json.load(io.open(DJ, encoding='utf-8'))
    run1 = io.open(CRUN1, encoding='utf-8').read()
    run2 = io.open(CRUN2, encoding='utf-8').read()
    run3 = io.open(CRUN3, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    lb = blob_of(PP, 'FACES_LEDGER.md') or ''
    committed = MARK in lb

    print(chr(10) + '  G-BUILT (F1: the two fixtures pass on the record run and fail on their altered inputs; the first two runs\' fixture failures declared):')
    gb = J['f1'] and J['f2'] and '(F1)' in run3 and 'altered coefficient' in run3 and 'the wrong n misses by' in run3 and "the altered input's smallest miss" in run3 \
        and ('### FAIL ###' in run1) and ('### FAIL ###' in run2) and 'F1' in bank and 'F2' in bank and J['run_file'] == 'b340_control_run3.txt'
    print('    f1 %s ; f2 %s ; the record run is run 3 %s ; runs 1 and 2 carry the fixture failures %s / %s : %s' % (J['f1'], J['f2'], J['run_file'] == 'b340_control_run3.txt', '### FAIL ###' in run1, '### FAIL ###' in run2, gb))
    if not gb:
        fails.append('G-BUILT')

    print(chr(10) + '  G-LAWFUL (F2: the three failed conditions and the two lists in the bank):')
    gl = all(x in bank for x in ('the support', 'the two vanishing conditions', 'even', 'WHICH CERTIFICATIONS APPLY:', 'WHICH DO NOT:', 'Three of three'))
    print('    %s' % gl)
    if not gl:
        fails.append('G-LAWFUL')

    print(chr(10) + '  G-BAR (F3: the bar recomputed at every index; holds_all False as the drift exceeds it; the identity within the bar at every index by the theta route; the verdict by the rule; the diagnostic beside it):')
    ok_bar = True
    for row in J['table']:
        with mp.workdps(50):
            la = mp.mpf(row['lamA'])
            bar = mp.mpf('1e-9') * max(mp.mpf(1), abs(la))
            miss = abs(mp.mpf(row['I_theta']) + 1 - la)
            drift = abs(mp.mpf(row['I_theta']) - mp.mpf(row['I_u']))
            # ### the record prints bar, miss and drift to three significant figures (mp.nstr(x, 3)); the recomputation is compared at that grain
            ok_bar = ok_bar and abs(bar - mp.mpf(row['bar'])) <= bar * mp.mpf('1e-2') and (miss <= bar) == (mp.mpf(row['miss']) <= mp.mpf(row['bar'])) and abs(drift - mp.mpf(row['drift'])) <= mp.mpf('1e-2') * drift
            ok_bar = ok_bar and (row['holds'] == bool(miss <= bar and drift <= bar and row['gate'] == 'RESOLVED'))
    gbar = ok_bar and (not J['holds_all']) and J['n_identity'] == len(J['indices']) and J['n_hold'] == 0 and J['what'] == 'a quadrature failure (the gate refusing)' \
        and 'VERDICT: THE DIFFERING CONSTITUENT' in run3 and DG['tail_carries'] and DG['u_ts_meets_bar'] and 'A READING, NOT A VERDICT' in io.open(DRUN, encoding='utf-8').read()
    print('    bars and verdicts recomputed %s ; holds_all %s ; identity within the bar at %d of %d ; what %r ; diagnostic: tail carries %s, u by tanh-sinh meets the bar %s : %s'
          % (ok_bar, J['holds_all'], J['n_identity'], len(J['indices']), J['what'], DG['tail_carries'], DG['u_ts_meets_bar'], gbar))
    if not gbar:
        fails.append('G-BAR')

    print(chr(10) + "  G-INDICES (F4: the keystone's rows, read live from the owner file):")
    ktxt = io.open(KEY, encoding='utf-8').read().splitlines()
    head = '| n | \u03bb_A(n) | \u03bb_Z(n) | margin \u03bb_n | agree digits |'
    i0 = ktxt.index(head)
    live = []
    for ln in ktxt[i0 + 2:]:
        if not ln.startswith('|'):
            break
        live.append(int(ln.strip().strip('|').split('|')[0].strip()))
    gi = live == J['indices'] and J['keystone_head_line'] == i0 + 1 and len(live) == 22
    print('    %s (%d rows, head at line %d)' % (gi, len(live), i0 + 1))
    if not gi:
        fails.append('G-INDICES')

    print(chr(10) + "  G-SCOPE (F5: the certificate quoted at its line; the bench's sentence at its line; no Sonin margin; margins positive at every index):")
    mono = io.open(MONO, encoding='utf-8', errors='replace').read().splitlines()
    gs = J['cert_line'] is not None and J['cert_sentence'] in mono[J['cert_line'] - 1] and 'no further' in J['cert_sentence'] and J['bench_line'] is not None \
        and 'NOT evidence of the kind the criterion' in io.open(BENCH, encoding='utf-8').read().splitlines()[J['bench_line'] - 1] and J['all_margins_positive'] \
        and 'NO SONIN MARGIN DEFINED ON THE FAMILY' in run3 and ('line %d' % J['cert_line']) in bank and 'no further' in bank
    print('    %s (certificate at line %s; the bench at line %s)' % (gs, J['cert_line'], J['bench_line']))
    if not gs:
        fails.append('G-SCOPE')

    blk = led[led.index(MARK):] if MARK in led else ''
    print(chr(10) + '  G-LEDGER (F6: one block through the writer naming L1 and F1-L1; the ledger a true prefix of its blob; the trail still OWED in its words):')
    pre_rows = [ln for ln in norm(lb).split(chr(10)) if ln.startswith('| ')]
    gld = (led.count(MARK) == 1 and '**L1** and the pair **F1\u2013L1**' in blk and 'stays OWED' in blk and norm(led).startswith(norm(lb).rstrip(chr(10)))
           and all(ln in norm(led) for ln in pre_rows) and 'WRITTEN' in io.open(LEDRUN, encoding='utf-8').read() and 'DUPLICATE' in io.open(LEDRR, encoding='utf-8').read())
    print('    mark once %s ; names L1 and F1-L1 %s ; stays OWED %s ; prefix of blob %s (committed %s) ; rows preserved %d : %s'
          % (led.count(MARK) == 1, '**L1** and the pair **F1\u2013L1**' in blk, 'stays OWED' in blk, norm(led).startswith(norm(lb).rstrip(chr(10))), committed, len(pre_rows), gld))
    if not gld:
        fails.append('G-LEDGER')

    r188 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| %s |' % ROWNUM)]
    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    headb = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r188) == 1 and 'NO TERMINAL, AND THE REASON: A CONTROL AT ONE CONSTITUENT' in r188[0] and 'M-2' in r188[0] and 'NOT in the lawful class' in r188[0] and norm(tbl).startswith(norm(headb).rstrip(chr(10)))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTTHEOBJECT (one row; the must-not-hit queries NO KEY; the answer says the instrument not the object, not in the class, the sides owed):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('li-family-control')
    gk = o.count('act      :') == 1 and 'A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT' in o and 'THE SONIN MARGIN IS NOT DEFINED ON IT' in o and 'STAY OWED' in o
    for s in ('the li family lawful', 'the sonin margin on the li family', 'lambda_n positive for all n'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOTTHEOBJECT')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (the keystone, the bench, the owner instruments, sealed files, the deposit, TECHNE, HANDOFF: no tracked change beyond the act's files):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md',
              'tools/b327_bridge.py', 'tools/b326_windows.py', 'tools/b321_window.py', 'tools/noise_floor.py', 'tools/e16/carto_atlas.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b327_the_faces_ledger.txt', 'data/b327_source_text.txt', 'data/b333_the_archimedean_term_derived.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('FACES_LEDGER.md')]
    st_t = git(TC, 'status', '--porcelain').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    key_bench = git(PP, 'status', '--porcelain', '--', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', 'internal/bench/li_bench.py', 'ERRATA.md').strip()
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep and not key_bench
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond the ledger) %s ; the keystone, the bench, ERRATA %r ; TECHNE %r ; deposit %r : %s' % (st_r, st_s, st_p, key_bench, st_t, dep, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the instrument, the diagnostic, the block, the row, the key and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b340_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b340_li_control.py'), t('b340_diagnose.py'), CRUN1, CRUN2, CRUN3, CJ, DRUN, LEDRUN, LEDGER, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b340_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b340_checks_run.txt')) else ''
        after = 'the instrument, the diagnostic, the block, the row, the key and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the instrument, the diagnostic, the block, the row, the key and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
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
    for key, label in (('worst_miss', 'worst |I + 1 - lambda_A|'), ('worst_drift', 'worst drift'), ('worst_keystone', "worst against the keystone's column"), ('radii_worst', 'the two radii'),
                       ('pole_worst', 'the pole constant'), ('routeB_worst', 'route B'), ('worst_f1', 'fixture F1'), ('worst_f2', 'fixture F2'), ('keystone_lamZ_worst', "the keystone's lambda_Z")):
        checks.append(('%s %s' % (label, J[key]), ('`%s`' % J[key]) in bank))
    checks.append(('%d indices, identity at %d' % (len(J['indices']), J['n_identity']), ('%d tabulated indices' % len(J['indices'])) in bank and J['n_identity'] == 22 and 'at all 22 indices' in bank))
    dl = DG['parts']
    checks.append(('the diagnostic indices %s' % DG['indices'], all(('`n = %d`' % n) in bank for n in DG['indices'])))
    checks.append(('tail GL-TS at n = 130 %s' % dl['130']['tail_gl_minus_ts'], ('`%s`' % dl['130']['tail_gl_minus_ts']) in bank))
    checks.append(('u by tanh-sinh vs theta at n = 130 %s' % dl['130']['u_ts_vs_theta'], ('`%s`' % dl['130']['u_ts_vs_theta']) in bank))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    for what, ok in checks:
        print('    %-52s %s' % (what[:52], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded and numbered):')
    once_ok = all(os.path.exists(p) for p in [CRUN1, CRUN2, CRUN3, CJ, DRUN, DJ, LEDRUN, LEDRR, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b340_control_run4.txt')) and not os.path.exists(d('b340_diagnose_run2.txt'))
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

    ib = idx[idx.index('# ### THE LI FAMILY CONTROL (b340'):idx.index('# ### THE EXPONENT PRICED (b339')] if '# ### THE LI FAMILY CONTROL (b340' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the ledger block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, r188[0] if r188 else ''), ('the ledger block', blk), ('index row', ib)):
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
    tmpdir = tempfile.mkdtemp(prefix='b340_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, r188[0] if r188 else ''), ('the ledger block', blk), ('the index row', ib)):
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
