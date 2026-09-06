# -*- coding: utf-8 -*-
"""b345_checks.py -- THE GATE SUITE FOR THE LI CONTROL, RE-RUN.

### ### **THE ARMS (registration section (G)):** `G-RULE` (the tail rule tanh-sinh at both routes, fixed in the sealed
### file before any value, both quotations located in the extract; no panel anywhere uses Gauss-Legendre), `G-ROUTES`
### (route A imported byte-identical to its blob; route B calls no function of route A and no special function of
### mpmath; the shared surface MEASURED off the syntax trees; the kernel fixture -- ### **WHICH THIS ACT EXPECTS TO
### FAIL AND TABLES AS A DEFECTIVE BAR, AND THE ARM THEREFORE REQUIRES THE BANK'S DECLARATION RATHER THAN A PASS**),
### `G-BAR` (the bar as sealed at every index, the pole constant its own column, the verdict by (D)'s rule and no
### other, b340's bank and registration byte-identical after this act), `G-SCOPE` (both certification lists as the
### prior leg listed them, the certificate quoted at its line, the Sonin margin not evaluated), `G-LEDGER`, `G-TRAIL`,
### `G-ROW` / `G-ANCESTOR`, `G-KEY` / `G-NOTEXPLAINED`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`, `G-NUMBERS`,
### `G-TOOLNUM`, `G-ONCE`, the struck-clause and stem sweeps, `G-SHARED`, the hedge audit, the must-fail fixtures;
### re-run after the push. ### **THE PAPERS REPO MOVES, SO THE HOOK AND THE MIRROR ARE OWED.**
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

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
KEYFILE = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
MONO = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
BENCHF = os.path.join(PP, 'internal', 'bench', 'li_bench.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b345_the_li_control_rerun.txt')
REG = d('b345_registration_2026-09-06.txt')
EXTRACT = d('b345_extract_notes.txt')
FERRY = d('b345_ferry_2026-09-06.txt')
CRUN, CJ = d('b345_control_run.txt'), d('b345_control.json')
DRAFT_STOPPED = d('b345_control_draft_unsealed_params_stopped.txt')
FRUN, FJ = d('b345_filings_run.txt'), d('b345_filings.json')
CORR, IDX = d('b345_corr_run.txt'), d('b345_index_run.txt')
SCAN, TERMSCAN, GATE = d('b345_ferry_scan.txt'), d('b345_reg_termscan.txt'), d('b345_reg_gate.txt')
CENSUS, FCEN = d('b345_census.txt'), d('b345_faces_census.txt')
REGSPEC, SATIS = d('b345_regspec_run.txt'), d('audit_b345_reg_satisfiable.txt')
PINS, INDEXQ = d('b345_pins_stepzero.txt'), d('audit_b345_index_query.txt')
PINS_OLD = d('b345_pins_stepzero_under_the_prior_numbering.txt')
SORTIE_PINS = d('b343_pins_sortie.txt')
SEAL = '911122779f5f9ded8a62f5dbe691b5d1a01abf48b49a1075eb85edb8cee1e1a6'
MARK_L, MARK_T = '<!-- b345 update -->', '<!-- b345 trail update -->'
ROWNUM = '193'

OWNED = [BANK, REG, CRUN, CJ, DRAFT_STOPPED, FRUN, FJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, PINS_OLD,
         INDEXQ, GATE, TERMSCAN, d('b345_satisfiable.json'),
         t('b345_extract.py'), t('b345_regspec.py'), t('b345_control.py'), t('b345_filings.py'),
         t('b345_correspondence.py'), t('b345_index_append.py')]

CARRIERS = [
    (t('b345_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
    (SORTIE_PINS, "the b339-b343 sortie's closing pins, belonging to no act, carried by the author's ruling"),
]
NEW_THIS_ACT = {'tools/b345_extract.py', 'tools/b345_regspec.py', 'tools/b345_control.py', 'tools/b345_filings.py',
                'tools/b345_correspondence.py', 'tools/b345_index_append.py', 'tools/b345_checks.py'}

TOOLNUM = [
    ('the two routes, the fixture, the table, the verdict', 'tools/b345_control.py'),
    ("route A, imported and not edited", 'tools/b340_li_control.py'),
    ("lambda_A, lambda_Z, the pole constant, S_inf", 'tools/b327_bridge.py'),
    ('the RESOLVED gate at every index', 'tools/noise_floor.py'),
    ('the L1 block and the trail block', 'tools/b345_filings.py'),
    ('the append-only writer for the ledger', 'tools/b327_faces_row.py'),
    ('row 193', 'tools/b345_correspondence.py'),
    ('the key', 'tools/b345_index_append.py'),
    ('26 clauses', 'tools/b345_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('17001 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('b340 -- the verdict as sealed', d('b340_the_li_family_control.txt'),
     'THE VERDICT AS SEALED: THE DIFFERING CONSTITUENT -- A QUADRATURE FAILURE, THE GATE REFUSING THE SEALED'),
    ('### the sealed refinement, not the identity, failed', d('b340_the_li_family_control.txt'),
     '### REFINEMENT ROUTE, NOT THE IDENTITY, IS WHAT FAILED. ### THE BAR AS SEALED IS NOT MET AND IS NOT REWRITTEN.'),
    ("### the diagnostic's reading, in its own record", d('b340_diagnose_run.txt'),
     '  ### READING: the sealed refinement route (Gauss-Legendre on an infinite panel with a logarithmic tail) is what failed, and not the identity; the bar as sealed is NOT MET and is not rewritten.'),
    ('### tanh-sinh meets the bar', d('b340_diagnose_run.txt'),
     '  ### THE u ROUTE BY TANH-SINH (the same substitution, the other rule) MEETS THE SEALED BAR AGAINST THE THETA ROUTE at every diagnosed index : True'),
    ('### which certifications apply', d('b340_the_li_family_control.txt'),
     '### ### **WHICH CERTIFICATIONS APPLY:** the kernel identity (b333), a property of the kernel; the arrangement'),
    ('### which do not', d('b340_the_li_family_control.txt'),
     "### method. ### **WHICH DO NOT:** Theorem 1's inequality and the Sonin margin (defined on the class only --"),
    ('### not in the lawful class', d('b340_the_li_family_control.txt'),
     '### ### **(4) THE LI TEST FUNCTIONS ARE BUILT, AND THEY ARE NOT IN THE LAWFUL CLASS:** ### `g_n(x) = SUM_j C(n,j)'),
    ("b340's tool -- the theta route", t('b340_li_control.py'),
     '    """### (1/4pi) INT_0^pi [1 - (-1)^n cos n theta] h_+(u(theta)) sec^2(theta/2) dtheta, u = tan(theta/2)/2; tanh-sinh on 4n+4 panels."""'),
    ('the keystone -- the table head', KEYFILE, '| n | \u03bb_A(n) | \u03bb_Z(n) | margin \u03bb_n | agree digits |'),
    ('### the margin positive to 300', KEYFILE,
     '**The margin M(n) = \u03bb_A(n) + \u03bb_Z(n) = \u03bb_n nevertheless stays positive throughout 1 \u2264 n \u2264 300**'),
    ('the monograph -- the certificate at its scope', MONO,
     "partialPositivity_finiteRange` (v0.8.0) certifies \u03bb_n \u2265 0 for n up to Voros's detection threshold N\u2080(T) \u2248 2T\u00b2, with the on-line term's nonnegativity proved"),
    ('the bench -- an instrument, not an argument', BENCHF,
     'print("respects (Keiper 1992; BALANCE_AND_POSITIVITY sec V). This is an instrument, not an argument.")'),
    ("b327 -- one distribution on two families", d('b327_the_faces_ledger.txt'),
     '### ### ### **ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL.**'),
    ('b344 -- the two held axes, printed at every rung', d('b344_the_floor_priced.txt'),
     "### later act can price them without re-running this one: the cut's `tau = 1.0e-06` in force, with `2`"),
    ('### one axis moved is one axis moved', d('b344_the_floor_priced.txt'),
     '### **ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    ('the sortie -- leg 1', FERRY, 'LEG 1 (b344) \u2014 THE LI CONTROL, RE-RUN: the prior leg\'s bar is'),
    ('### (L1)', FERRY, 'The navigator\'s expectations: (L1) the control HOLDS under the'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK, '### ### ### **A FOURTH CONTROL HOLDS.**'),
    ('### that sentence and no more', BANK, '### **THAT SENTENCE AND NO MORE.**'),
    ("### b340's bar is not rewritten", BANK, '### ### **b340\'s BAR IS NOT REWRITTEN. ### ITS VERDICT IS NOT RE-VERDICTED. ### ITS BANK IS NOT EDITED.**'),
    ('### the tail rule sealed before any value', BANK, '### ### **THIS ACT SEALED THAT RULE AS ITS TAIL PANEL\'S QUADRATURE RULE BEFORE ANY VALUE WAS SEEN, AND NO PANEL'),
    ('### the shared surface measured', BANK, '### ### **THE SHARED SURFACE, MEASURED RATHER THAN ASSERTED**'),
    ('### digamma is route A alone', BANK, '### ### **`digamma` IS TAKEN BY ROUTE A ALONE. ### ROUTE B CALLS NO SPECIAL FUNCTION OF `mpmath`, AND NO'),
    ('### the fixture is a defective bar', BANK, '### ### **THE TWO CANNOT BOTH HOLD, AND RUNNING THE FIXTURE IS WHAT SHOWED IT.**'),
    ('### it separates nothing at its own threshold', BANK, '### **AT `1e-25` THE FIXTURE REJECTS THE CORRECT COPY AS WELL'),
    ('### which half carries the defect', BANK, '### **THE DEFECTIVE HALF IS THE'),
    ('### the diagnostic is not route B', BANK, '### **IT IS NOT THIS ACT\'S ROUTE B, AND NO VALUE IN THIS BANK IS COMPUTED WITH IT.**'),
    ('### what is not conferred', BANK, '### **WHAT THE BAR WOULD HAVE LICENSED AND IS'),
    ('### a measurement is not a met bar', BANK, '### instead is a measurement -- agreement to `4.394e-18` -- and ### **A MEASUREMENT IS NOT A MET BAR.**'),
    ('### the doctrine, quoted from itself', BANK, '### **A SEALED BAR FOUND'),
    ('### the drift is the same floor showing up twice', BANK, '### ### TRUNCATION\'S FLOOR SHOWING UP IN THE SECOND PLACE IT WAS ALWAYS GOING TO SHOW UP.**'),
    ('### the certificate is the deposit\'s', BANK, '### ### **THE CERTIFICATE IS THE DEPOSIT\'S AND ITS PREMISES ARE NAMED AND OPEN. ### THIS ACT DID NOT PROVE IT,'),
    ('### the trail stays owed', BANK, '### keep ### **`W-ORD-LI-FAMILY-CONTROL` OWED**'),
    ('### the expectations scored', BANK, "### (9) BOTH SEATS' EXPECTATIONS, SCORED."),
    ('### (E1) the stopped draft', BANK, '### ### **(E1) A DRAFT RAN AT PARAMETERS THIS ACT DID NOT SEAL, AND WAS STOPPED.**'),
    ('### (E2) the defective bar', BANK, '### ### **(E2) THE KERNEL FIXTURE IS A DEFECTIVE BAR, TABLED AND NOT REPAIRED.**'),
    ('### (E2) the audit could not catch it', BANK, '### ### **THE SATISFIABILITY AUDIT DID NOT AND COULD NOT CATCH IT:**'),
    ('### (E3) one name missing from the shared list', BANK, '### ### **(E3) ONE NAME IS MISSING FROM THE SEALED SHARED LIST.**'),
    ('### the work-order prices nothing', BANK, '### ### WITHOUT RE-RUNNING b344.** ### **NOTHING IS PRICED HERE AND NO AXIS IS MOVED.**'),
    ('### what this act does not conclude', BANK, '### ### **NOT THAT b340 IS CORRECTED.**'),
]

MUST_FAIL = [
    ('the bank never says b340 is corrected', BANK, '### b340 IS CORRECTED.'),
    ('the bank never says the family is lawful', BANK, '### THE LI FAMILY IS LAWFUL.'),
    ('the bank never says the trail is paid', BANK, '### THE TRAIL IS PAID.'),
    ('the bank never says the fixture passed', BANK, '### THE KERNEL FIXTURE PASSED.'),
    ('the bank never confers from the failed bar', BANK, "### ROUTE B's KERNEL IS CORRECT AT THE SEALED TOLERANCE."),
]


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def flat(s):
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^###\s*', ' ', s.replace('\u2019', "'"))).strip()


def strip_prose(path):
    """### THE SOURCE WITH ITS COMMENTS AND STRING LITERALS REMOVED. ### **A `G-NO*` ARM THAT GREPS RAW SOURCE
    ### FIRES ON THE ACT'S OWN SENTENCE SAYING THE THING WAS NOT DONE** (b316, b317); this is that species, closed."""
    src2 = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src2)
    spans = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and hasattr(n, 'lineno'):
            spans.append((n.lineno, n.end_lineno))
    lines = src2.split(chr(10))
    keep = []
    for i, ln in enumerate(lines, 1):
        if any(a <= i <= b for a, b in spans):
            continue
        keep.append(ln.split('#')[0])
    return chr(10).join(keep)


def mp_attrs(path, funcs):
    tree = ast.parse(io.open(path, encoding='utf-8').read())
    out = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            for n in ast.walk(node):
                if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == 'mp':
                    out.add(n.attr)
    return out


def calls(path, funcs):
    """### every NAME this act's route-B functions call, so a call into route A would be visible."""
    tree = ast.parse(io.open(path, encoding='utf-8').read())
    out = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            for n in ast.walk(node):
                if isinstance(n, ast.Call):
                    f = n.func
                    if isinstance(f, ast.Name):
                        out.add(f.id)
                    elif isinstance(f, ast.Attribute):
                        base = f.value.id if isinstance(f.value, ast.Name) else '?'
                        out.add(base + '.' + f.attr)
    return out


ROUTE_B = {'psi_hand', 'first_omitted', 'h_plus_B', 'reG_B', 'I_u_B'}
ROUTE_A = {'I_theta', 'h_plus', 'reG_closed'}


def main():
    fails = []
    print('=' * 100)
    print('b345 -- GATE SUITE (A CONTROL RE-RUN, AND A SEALED FIXTURE THAT COULD NOT SEPARATE)')
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
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    K = json.load(io.open(CJ, encoding='utf-8'))
    F = json.load(io.open(FJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    KD = K['kernel_diagnostic'] or {}

    print(chr(10) + '  G-RULE (the tail rule tanh-sinh at both routes, fixed in the sealed file before any value; no Gauss-Legendre anywhere):')
    r1 = "**THE TAIL PANEL'S QUADRATURE RULE, FIXED HERE AND BEFORE ANY VALUE: TANH-SINH.**" in reg
    r2 = '**NO PANEL OF EITHER ROUTE USES' in reg and 'GAUSS-LEGENDRE.**' in flat(reg)
    q1 = 'the same `u` route by tanh-sinh meets the sealed bar' in reg
    q2 = 'Gauss-Legendre on an infinite panel with a\n### logarithmic tail) is what failed' in reg or 'Gauss-Legendre on an infinite panel with a' in reg
    src = io.open(t('b345_control.py'), encoding='utf-8').read()
    meth = set(re.findall(r"method='([a-z-]+)'", src))
    usesA = ('LC.I_theta' in src) and ('LC.I_u' not in src)
    gr = r1 and r2 and q1 and q2 and meth == {'tanh-sinh'} and usesA
    print('    the rule fixed in the sealed file : %s ; the no-Gauss-Legendre sentence : %s' % (r1, r2))
    print("    b340's two quotations located in the sealed file : %s / %s" % (q1, q2))
    print("    quadrature methods named in this act's instrument : %s ; route A's theta route called and its Gauss-Legendre route NOT : %s"
          % (sorted(meth), usesA))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RULE')

    print(chr(10) + '  G-ROUTES (route A imported unedited; route B disjoint and free of special functions; the fixture, and what this act does with it):')
    a_blob = blob_of(ROOT, 'tools/b340_li_control.py')
    a_now = io.open(t('b340_li_control.py'), encoding='utf-8').read()
    a_same = (a_blob is not None) and norm(a_blob) == norm(a_now)
    ub, ua = mp_attrs(t('b345_control.py'), ROUTE_B), mp_attrs(t('b340_li_control.py'), ROUTE_A)
    special = {'digamma', 'zeta', 'gamma', 'loggamma', 'psi', 'polygamma', 'besselj', 'erf', 'ei', 'li'}
    no_special = not (ub & special)
    cb = calls(t('b345_control.py'), ROUTE_B)
    no_a = not (cb & (ROUTE_A | {'LC.' + x for x in ROUTE_A}))
    shared = sorted(ub & ua)
    elementary = {'log', 'exp', 'atan', 'sqrt', 'mpc', 'mpf', 'pi', 're', 'workdps', 'tan', 'sin', 'cos', 'inf'}
    not_named = [x for x in shared if x not in elementary]
    # ### the fixture. ### **THIS ACT EXPECTS IT TO FAIL AND TABLES IT; THE ARM THEREFORE ASKS FOR THE DECLARATION,
    # ### NOT FOR A PASS. ### A PASS WOULD ALSO SATISFY THE ARM -- WHAT WOULD NOT IS A FAILURE LEFT UNDECLARED.**
    fx = K['kernel_fixture']
    declared = ('(E2) THE KERNEL FIXTURE IS A DEFECTIVE BAR, TABLED AND NOT REPAIRED' in bank
                and 'A MEASUREMENT IS NOT A MET BAR' in bank
                and 'NOT CONFERRED' in flat(bank).upper())
    tracks = all(abs(float(p['true']) - float(p['omitted'])) <= float(p['omitted']) for p in K['kernel_points'])
    discr = K['kernel_broken_fails']
    diag_ok = bool(KD.get('would_pass')) and 'IT IS NOT THIS ACT' in bank
    e3 = '(E3) ONE NAME IS MISSING FROM THE SEALED SHARED LIST' in bank and 'quad' in bank
    gro = a_same and no_special and no_a and (fx or (declared and tracks and discr and diag_ok)) and (not not_named or e3)
    print("    route A byte-identical to its blob : %s" % a_same)
    print('    route B takes from mpmath : %s ; special functions among them : %s ; calls into route A : %s'
          % (sorted(ub), sorted(ub & special) or 'none', sorted(cb & (ROUTE_A | {'LC.' + x for x in ROUTE_A})) or 'none'))
    print('    the shared surface, measured : %s ; of those NOT arithmetic-or-elementary : %s'
          % (shared, not_named or 'none'))
    print('    the sealed fixture passed : %s ; the failure DECLARED as a defective bar in the bank : %s' % (fx, declared))
    print('    the measured miss tracks the first dropped term at every point : %s ; the broken copy fails : %s' % (tracks, discr))
    print('    the diagnostic isolates one named half and is marked as not this act\'s route B : %s' % diag_ok)
    print('    the unnamed shared name declared as (E3) : %s' % e3)
    print('    %s' % ('PASS' if gro else '### FAIL ###'))
    if not gro:
        fails.append('G-ROUTES')

    print(chr(10) + "  G-BAR (the bar as sealed at every index; the pole constant its own column; the verdict by (D)'s rule; b340 untouched):")
    tab = K['table']
    recomputed = all((float(r['miss']) <= float(r['bar'])) and (float(r['drift']) <= float(r['bar'])) and r['gate'] == 'RESOLVED' for r in tab)
    verdict_rule = (K['verdict'] == 'A FOURTH CONTROL HOLDS') == (K['n_hold'] == len(tab) and recomputed)
    pole_col = all('pole' in r for r in tab) and float(K['pole_worst']) < 1e-30
    idxs = [r['n'] for r in tab]
    import b340_li_control as LC_
    krows, khead = LC_.keystone_table()
    idx_ok = idxs == [r['n'] for r in krows] and len(idxs) == 22 and khead == K['keystone_head_line']
    b340_bank_blob = blob_of(ROOT, 'data/b340_the_li_family_control.txt')
    b340_reg_blob = blob_of(ROOT, 'data/b340_registration_2026-09-06.txt') or blob_of(ROOT, 'data/b340_registration_2026-09-05.txt')
    b340_same = (b340_bank_blob is not None) and norm(b340_bank_blob) == norm(io.open(d('b340_the_li_family_control.txt'), encoding='utf-8').read())
    gb = recomputed and verdict_rule and pole_col and idx_ok and b340_same
    print('    the bar recomputed from the record at all %d indices : %s ; the verdict follows (D)\'s rule and no other : %s' % (len(tab), recomputed, verdict_rule))
    print('    the pole constant carried as its own column, worst |L_n[log s] - 1| = %s : %s' % (K['pole_worst'], pole_col))
    print("    the indices are the keystone's own, unchanged after any value : %s" % idx_ok)
    print("    b340's bank byte-identical to its blob after this act : %s" % b340_same)
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BAR')

    print(chr(10) + '  G-SCOPE (both certification lists as the prior leg listed them; the certificate at its line; the Sonin margin not evaluated):')
    run = io.open(CRUN, encoding='utf-8').read()
    s1 = 'WHICH APPLY: the kernel identity (b333)' in run and 'WHICH DO NOT: Theorem 1' in run
    s2 = 'NOT IN THE LAWFUL CLASS' in run and 'three of three' in run
    s3 = ('line %d' % K['cert_line']) in run and ('line %d' % K['bench_line']) in run
    code_only = strip_prose(t('b345_control.py'))
    s4 = 'SONIN MARGIN IS NOT DEFINED ON THIS FAMILY AT ALL' in run and 'sonin' not in code_only.lower()
    s5 = K['all_margins_positive'] and 'POSITIVITY IN A FINITE RANGE IS NOT' in run
    gs = s1 and s2 and s3 and s4 and s5
    print('    both lists printed : %s ; the family not in the class, re-stated : %s' % (s1, s2))
    print('    the certificate at monograph line %s and the bench at line %s : %s' % (K['cert_line'], K['bench_line'], s3))
    print('    the Sonin margin named as undefined here and never computed : %s' % s4)
    print("    the deposit's margin positive at all indices and restated at its scope : %s" % s5)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SCOPE')

    print(chr(10) + '  G-LEDGER (one block through the writer naming L1, the words, and what is measured and what is not; a true prefix of its blob):')
    led = io.open(LEDGER, encoding='utf-8').read()
    lb = blob_of(PP, 'FACES_LEDGER.md')
    l1 = led.count(MARK_L) == 1 and F['faces'] in ('WRITTEN', 'DUPLICATE')
    l2 = '**L1**' in led[led.index(MARK_L):] and 'ONE DISTRIBUTION ON TWO FAMILIES' in led[led.index(MARK_L):]
    blk = led[led.index(MARK_L):]
    l3 = '**MEASURED:**' in blk and '**NOT MEASURED:**' in blk and 'W-ORD-LI-FAMILY-CONTROL' in blk and 'not defined on this family at all' in blk
    l4 = (lb is not None) and norm(led).startswith(norm(lb).rstrip(chr(10)))
    gl = l1 and l2 and l3 and l4
    print('    one block, through the writer : %s ; names L1 and carries the words : %s' % (l1, l2))
    print('    measured / not measured set out, the trail named still owed : %s ; a true prefix of its blob : %s' % (l3, l4))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LEDGER')

    print(chr(10) + '  G-TRAIL (one appended block under the b345 mark; the trail given an ID; b344\'s figures quoted; nothing priced):')
    tr = io.open(TRAILS, encoding='utf-8').read()
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    N = json.load(io.open(d('b344_ny.json'), encoding='utf-8'))
    tblk = tr[tr.index(MARK_T):] if MARK_T in tr else ''
    t1 = tr.count(MARK_T) == 1 and F['trails'] in ('WRITTEN', 'DUPLICATE')
    t2 = F['trail_id'] in tblk and F['trail_id'] not in tr[:tr.index(MARK_T)] if MARK_T in tr else False
    t3 = all(('%.6e' % r['held']['smallest_kept']) in tblk and ('%.6e' % r['held']['distance']) in tblk for r in N['rows'])
    t4 = '1.0e-06' in tblk and '`ALPHA = 1.0`' in tblk and '`BETA = 1.0`' in tblk
    t5 = 'WITHOUT RE-RUNNING b344' in tblk and 'Nothing is priced here and no axis is moved' in tblk
    t6 = (tb is not None) and norm(tr).startswith(norm(tb).rstrip(chr(10)))
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    one block under the mark : %s ; the trail ID %s is new to the file : %s' % (t1, F['trail_id'], t2))
    print("    b344's per-rung held figures quoted at every rung : %s ; tau and the taper quoted : %s" % (t3, t4))
    print('    the sentence that it is priceable WITHOUT re-running b344, and nothing priced : %s ; a true prefix of its blob : %s' % (t5, t6))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    gw = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT' in rows[0] and anc
    print('    row %s present once : %s ; NO TERMINAL with the reason : %s ; table a true prefix of its blob : %s'
          % (ROWNUM, len(rows) == 1, bool(rows and 'NO TERMINAL, AND THE REASON' in rows[0]), anc))
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTEXPLAINED (one key, one row; the must-not-hit queries NO KEY; the answer refuses the overreadings):')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = irun.count("li-control-rerun key/row already present") == 1 and 'READ BACK : li-control-rerun returns 1 row(s)' in irun
    k2 = all(('%-40s NO KEY after  : True  PASS' % q) in irun for q in
             ('b340 corrected', 'the li family is lawful', 'the trail is paid', 'the formula closed on the li family'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row, read back : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s' % (k1, k2, k3))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOTEXPLAINED')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    ib_blob = blob_of(ROOT, 'tools/banked_index.py')
    ap = True
    if ib_blob is not None:
        old, new = norm(ib_blob).split(chr(10)), norm(idx).split(chr(10))
        i = 0
        for ln in new:
            if i < len(old) and ln == old[i]:
                i += 1
        ap = (i == len(old))
    print('    %s' % ap)
    if not ap:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (no owner instrument edited; the deposit and HANDOFF clean; only this act\'s paths touched):')
    owner = ['tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py', 'tools/b319_stable.py',
             'tools/b320_weil.py', 'tools/b321_window.py', 'tools/b326_windows.py', 'tools/b334_aimmap.py',
             'tools/b340_li_control.py', 'tools/b327_bridge.py', 'tools/noise_floor.py', 'tools/reg_seal.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if not (x[3:].strip() in ('FACES_LEDGER.md', 'OPEN_TRAILS.md'))]
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    gn = not touched and not ppbad and hand and dep
    print('    owner instruments modified : %s ; papers-repo paths beyond the two filings : %s' % (touched or 'none', ppbad or 'none'))
    print('    HANDOFF.md clean : %s ; the deposited monograph clean : %s' % (hand, dep))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the registration sealed before the instrument ran; the audit as it stands):')
    raw = open(REG, 'rb').read()
    body = raw.split(('=' * 100 + chr(10) + '### THE REGISTRATION SEAL').encode())[0]
    h = hashlib.sha256(body).hexdigest()
    o1 = (h == SEAL) and (SEAL in raw.decode('utf-8', 'replace'))
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', raw.decode('utf-8', 'replace'))
    o2 = stampm is not None
    o3 = os.path.getmtime(CRUN) > os.path.getmtime(REG)
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes to the banked hash : %s ; the seal block carries its own clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    the instrument\'s run file is younger than the sealed registration : %s ; the audit reads JOINTLY SATISFIABLE : %s' % (o3, o4))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED):')
    hookp, mirrorp = d('b345_hooks.txt'), d('b345_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht, mt = io.open(hookp, encoding='utf-8', errors='replace').read(), io.open(mirrorp, encoding='utf-8', errors='replace').read()
        gh = ('REFUSED' not in ht.upper() or 'refuses' in ht) and 'MIRROR' in mt.upper()
        print('    hook record present : True ; mirror record present : True')
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    checks = []
    checks.append(('the verdict at %d of %d' % (K['n_hold'], len(tab)), ('**%d of the %d**' % (K['n_hold'], len(tab))) in bank))
    checks.append(('worst miss %s' % K['worst_miss'], ('`%s`' % K['worst_miss']) in bank))
    checks.append(('worst drift %s' % K['worst_drift'], ('`%s`' % K['worst_drift']) in bank))
    checks.append(('the keystone column %s' % K['worst_keystone'], ('`%s`' % K['worst_keystone']) in bank))
    checks.append(('the pole constant %s' % K['pole_worst'], ('`%s`' % K['pole_worst']) in bank))
    checks.append(('the two radii %s' % K['radii_worst'], ('`%s`' % K['radii_worst']) in bank))
    checks.append(("the source's (4.11) %s" % K['routeB_worst'], ('`%s`' % K['routeB_worst']) in bank))
    checks.append(('the kernel worst %s' % K['kernel_worst'], ('`%s`' % K['kernel_worst']) in bank))
    crun = io.open(CRUN, encoding='utf-8').read()
    dg = re.search(r'worst true (\S+) ;[\s\S]{0,200}?broken smallest (\S+) ;', crun)
    checks.append(('the diagnostic %s and %s, as its run file printed them' % (dg.group(1), dg.group(2)),
                   ('`%s`' % dg.group(1)) in bank and ('`%s`' % dg.group(2)) in bank))
    checks.append(('the six fixture points', all(p['true'] in bank and p['omitted'] in bank and p['broken'].replace('0.02469', '2.469e-02') for p in K['kernel_points'])))
    checks.append(("the keystone's lambda_Z %s" % K['keystone_lamZ_worst'], ('`%s`' % K['keystone_lamZ_worst']) in bank))
    checks.append(('the keystone head line %d' % K['keystone_head_line'], ('line %d' % K['keystone_head_line']) in bank))
    checks.append(('the certificate line %d and the bench line %d' % (K['cert_line'], K['bench_line']),
                   ('line %d' % K['cert_line']) in bank and ('line %d' % K['bench_line']) in bank))
    checks.append(('every table row (I_A, drift, lamA, miss)',
                   all(r['I_A'] in bank and r['lamA'] in bank for r in tab)))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank))
    sm = re.search(r'### bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    checks.append(('%s clauses' % cl, ('%s clauses' % cl) in bank))
    checks.append(('the seal hash', SEAL in bank))
    checks.append(('the seal stamp %s' % (stampm.group(1) if stampm else ''), (stampm.group(1) if stampm else 'x') in bank))
    checks.append(('the trail ID %s' % F['trail_id'], F['trail_id'] in bank))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the stopped draft kept under its own name):')
    once_ok = (all(os.path.exists(p) for p in [CRUN, FRUN, CORR, IDX, DRAFT_STOPPED])
               and not os.path.exists(d('b345_control_run2.txt'))
               and not os.path.exists(d('b345_filings_run2.txt'))
               and os.path.exists(PINS_OLD) and os.path.exists(SORTIE_PINS))
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
    fired_disc = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                        ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                     if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    lblk = led[led.index(MARK_L):] if MARK_L in led else ''
    ib = idx[idx.index('# ### THE LI CONTROL, RE-RUN (b345).'):idx.index("# ### THE FLOOR PRICED")] if '# ### THE LI CONTROL, RE-RUN (b345).' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the ledger block, the trail block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the ledger block', lblk), ('the trail block', tblk), ('the index row', ib)):
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the two blocks and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b345_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the ledger block', lblk), ('the trail block', tblk), ('the index row', ib)):
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
