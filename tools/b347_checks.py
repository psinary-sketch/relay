# -*- coding: utf-8 -*-
"""b347_checks.py -- THE GATE SUITE FOR THE THREE REPAIRS AND THE TWO RULES.

### ### **THIS SUITE USES `gate_text.flat` -- THE UTILITY THIS ACT BUILT -- AND DEFINES NO FLATTENER OF ITS OWN.**
### That is the point of (E): the next suite inherits the repair instead of the defect, and this is the first suite
### to do it.
### ### **THE ARMS (registration section (I)):** `G-CLOCK`, `G-PRICE`, `G-FLAT`, `G-RULE`, `G-GATE`, `G-TWOROUTES`,
### `G-STANDING`, `G-ROW`, `G-KEY` / `G-NOTEXPLAINED`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`, `G-PAPERS`,
### `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, the sweeps, `G-SHARED`, the hedge audit, the must-fail fixtures; re-run after
### the push.
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
import gate_text         # noqa: E402  ### THE REPAIRED FLATTENER, FROM THE UTILITY THIS ACT BUILT
import run_clock         # noqa: E402
import registration_gate as RG  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
MOD = os.path.join(TC, 'modules', '2026-09')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FS = os.path.join(ROOT, 'tools', 'FERRY_STANDING.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b347_the_three_repairs.txt')
REG = d('b347_registration_2026-09-06.txt')
ORDER = d('b347_order_2026-09-06.txt')
EXTRACT = d('b347_extract_notes.txt')
RRUN, RJ = d('b347_repairs_run.txt'), d('b347_repairs.json')
CORR, IDX = d('b347_corr_run.txt'), d('b347_index_run.txt')
SCAN, TERMSCAN, GATE = d('b347_ferry_scan.txt'), d('b347_reg_termscan.txt'), d('b347_reg_gate.txt')
CENSUS, FCEN = d('b347_census.txt'), d('b347_faces_census.txt')
REGSPEC, SATIS = d('b347_regspec_run.txt'), d('audit_b347_reg_satisfiable.txt')
PINS, INDEXQ = d('b347_pins_stepzero.txt'), d('audit_b347_index_query.txt')
SEAL = 'd7f1eae15389fcd732ee99900f739297fa1a42863e67b7f02b3c9862c6052a52'
ROWNUM = '195'

OWNED = [BANK, REG, ORDER, RRUN, RJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, TERMSCAN,
         d('b347_satisfiable.json'),
         t('b347_extract.py'), t('b347_regspec.py'), t('b347_repairs.py'), t('b347_correspondence.py'),
         t('b347_index_append.py'), t('run_clock.py'), t('gate_text.py')]

CARRIERS = [
    (t('b347_checks.py'), 'its own fixtures'),
    (ORDER, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]
NEW_THIS_ACT = {'tools/b347_extract.py', 'tools/b347_regspec.py', 'tools/b347_repairs.py',
                'tools/b347_correspondence.py', 'tools/b347_index_append.py', 'tools/b347_checks.py',
                'tools/run_clock.py', 'tools/gate_text.py'}

TOOLNUM = [
    ('the five components and every census', 'tools/b347_repairs.py'),
    ("the run file's clock and its fixtures", 'tools/run_clock.py'),
    ('the repaired flattener and its fixtures', 'tools/gate_text.py'),
    ('the two bar-floor arms and their fixtures', 'tools/registration_gate.py'),
    ("the audit's named numerical limit", 'tools/reg_satisfiable.py'),
    ('FERRY_STANDING v2 and its live counts', 'tools/b335_standing.py'),
    ('row 195', 'tools/b347_correspondence.py'),
    ('the key', 'tools/b347_index_append.py'),
    ('31 clauses', 'tools/b347_regspec.py'),
    ('21740 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('b345 -- the fixture is a defective bar', d('b345_the_li_control_rerun.txt'),
     '### ### **THE TWO CANNOT BOTH HOLD, AND RUNNING THE FIXTURE IS WHAT SHOWED IT.**'),
    ('b345 -- why a run file needs a clock', d('b345_the_li_control_rerun.txt'),
     '### ### RUNNING ITS OWN SUITE TWICE.**'),
    ('b346 -- the arm that did no work', d('b346_the_exponent_by_rate.txt'),
     '### ### **(E1) ONE OF THE SEALED UNCERTAINTY ARMS DID NO WORK, AND THE SEALED PAIRING IS DEFECTIVE.**'),
    ('b346 -- the shared engine', d('b346_the_exponent_by_rate.txt'),
     '### ### **(E2) THE TWO EVALUATORS SHARE AN ENGINE, AND IT IS NAMED RATHER THAN CLAIMED ABSENT.**'),
    ("b344 -- the seal's own clock", t('reg_seal.py'), "CLOCK = '### sealed at (UTC) : '"),
    ('b322 -- the weaker of the two', d('b322_components_run.txt'),
     '  ### ### ### **THE ACT TAKES THE WEAKER OF THE TWO: ### UNDER-RESOLVED.** ###'),
    ('FERRY_STANDING -- the seat adds none by hand', t('FERRY_STANDING.md'),
     'RULE: a clause is STANDING when a majority of the range carries it (8 or more of 15); a clause below that is listed as FREQUENT, NOT STANDING; the seat adds none by hand'),
    ('the ruling that ordered the act-number clause', d('b344_ruling_2026-09-06.txt'),
     'behaviour and is banked as such. Add to FERRY_STANDING v2, when'),
    ('the order -- the rule over both species', ORDER, '(1) The bar-floor rule is stated over BOTH species and the'),
    ('the order -- the two-routes third clause', ORDER, '(2) The two-routes module gains the third clause by appended'),
    ('the order -- the flattener and its reach', ORDER, '(3) The flattener defect is repaired in the gate utility once,'),
    ('the order -- the fold is next', ORDER, 'After b347, the board returns to mathematics and the next act'),
]

SELF_NEEDLES = [
    ('the bank states what the act is first', BANK, '### ### ### **A SHARPER INSTRUMENT IS NOT A RESULT.**'),
    ('### the clock does not reach backwards', BANK, '###   ### **(i) THE CLOCK DOES NOT REACH BACKWARDS.**'),
    ('### the audit is named and priced, not closed', BANK,
     '###   ### **(ii) THE AUDIT\'S NUMERICAL LIMIT IS NAMED AND PRICED. ### IT IS NOT CLOSED.**'),
    ('### the gate matches text', BANK, '###   ### **(iii) THE GATE MATCHES TEXT.**'),
    ('### no past act is re-verdicted', BANK, '###   ### **(iv) NO PAST ACT IS RE-VERDICTED.**'),
    ('### not one run file can be given a clock', BANK, "### ### **NOT ONE OF THEM CAN BE GIVEN ONE.**"),
    ('### the price is not a plan', BANK, '### ### **A PRICE IS NOT A PREDICTION AND THIS IS NOT A PLAN.**'),
    ('### the count is a lower bound', BANK, '###   ### **IT IS A LOWER BOUND.**'),
    ('### an untaken branch is not an unmatched arm', BANK,
     '### **A PHRASE IN AN UNTAKEN BRANCH IS NOT AN UNMATCHED ARM.**'),
    ('### the defect points toward false alarm', BANK, '### to match made its gate ### **FAIL, NOT PASS.**'),
    ('### the rule itself', BANK, '### ### ### **THE RULE:** ### **A NUMERICAL BAR IS STATED WITH THE FLOOR OF THE OBJECT IT TESTS; A BAR'),
    ('### a quiet row is quiet because there was nothing to look at', BANK,
     '### ### **A QUIET ROW IS MOSTLY QUIET BECAUSE THERE WAS NOTHING FOR THE ARM TO LOOK AT, NOT BECAUSE THE ARM'),
    ('### the act did not exempt itself', BANK, '### ### **AND THIS ACT DID NOT EXEMPT ITSELF.**'),
    ('### carried and not fixed', BANK, '### ### **THAT IS CARRIED AND NOT FIXED. ### THE FILE IS SEALED.**'),
    ('### the modules are not pushed', BANK, '### ### **PRIVATE, LOCAL-ONLY, NOT PUSHED.**'),
    ('### author-ruled, not measured', BANK, '### ### **THE ACT-NUMBER CLAUSE SITS IN ITS OWN SECTION, MARKED `AUTHOR-RULED, NOT MEASURED`**'),
    ('### the scan was not taught it', BANK, '### ### **AND THE SCAN HAS NOT BEEN TAUGHT THE CLAUSE.**'),
    ('### the expectations scored', BANK, "### (7) BOTH SEATS' EXPECTATIONS, SCORED."),
    ('### (b) refuted', BANK, '### ### **THIS SEAT\'S (b)** -- the bar-floor census fires on MORE past registrations than it clears :'),
    ('### what this act does not conclude', BANK, '### ### **NOT THAT ANY PAST ACT WAS WRONG.'),
]

MUST_FAIL = [
    ('the bank never says the audit is closed', BANK, '### THE AUDIT IS CLOSED.'),
    ('the bank never says a past act was wrong', BANK, '### A PAST ACT WAS WRONG.'),
    ('the bank never says the clock dates the old runs', BANK, '### THE CLOCK DATES THE OLD RUNS.'),
    ('the bank never calls a repair a result', BANK, '### A SHARPER INSTRUMENT IS A RESULT.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def main():
    fails = []
    print('=' * 100)
    print('b347 -- GATE SUITE (THREE REPAIRS, TWO RULES, AND AN ACT CAUGHT BY ITS OWN NEW ARM)')
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
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    R = json.load(io.open(RJ, encoding='utf-8'))
    C, Dd, E, F, G = R['C'], R['D'], R['E'], R['F'], R['G']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    run = io.open(RRUN, encoding='utf-8').read()

    print(chr(10) + "  G-CLOCK (a parseable instant and the next number; both polarities; the limit in the file; the census):")
    c1 = run_clock.self_test(verbose=False)
    c2 = run_clock.read_stamp(RRUN) is not None and R['run_clock'] == run_clock.read_stamp(RRUN)
    src = io.open(t('run_clock.py'), encoding='utf-8').read()
    c3 = 'THE CLOCK IS OUTSIDE EVERYTHING THAT VERIFIES' in src and 'IT RECOVERS NOTHING ABOUT ANY RUN FILE WRITTEN BEFORE IT' in src
    c4 = C['with_clock'] == 0 and C['runs'] > 0
    gc = c1 and c2 and c3 and c4
    print('    the four fixtures : %s ; this act\'s own run file carries its clock (%s) : %s' % (c1, R['run_clock'], c2))
    print('    the limit stated in the tool where the line is written : %s' % c3)
    print('    the census: %d run files, %d carried a clock before this act : %s' % (C['runs'], C['with_clock'], c4))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CLOCK')

    print(chr(10) + "  G-PRICE (the limit named in the audit's own output; the price a COUNT; existing verdicts unchanged):")
    p1 = Dd['named'] and Dd['verdict_unchanged']
    p2 = Dd['carry'] == Dd['pairable'] + Dd['hand'] and Dd['hand'] > 0
    p3 = 'NAMED AND PRICED' in bf.upper() and 'IT IS NOT CLOSED' in bf.upper()
    p4 = 'A PRICE IS NOT A PREDICTION AND THIS IS NOT A PLAN' in bf
    gp = p1 and p2 and p3 and p4
    print('    named in the output and b346\'s verdict unchanged : %s ; the counts add up (%d = %d + %d) : %s'
          % (p1, Dd['carry'], Dd['pairable'], Dd['hand'], p2))
    print('    the bank says named and priced, not closed : %s ; and that a price is not a plan : %s' % (p3, p4))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PRICE')

    print(chr(10) + '  G-FLAT (one utility; both polarities; the reach measured; every past copy byte-identical to its blob):')
    f1 = gate_text.self_test(verbose=False)
    own_src = io.open(t('b347_checks.py'), encoding='utf-8').read()
    f2 = (re.search(r'(?m)^def flat\(', own_src) is None) and ('import gate_text' in own_src)
    same = []
    for c in ('b342_checks.py', 'b343_checks.py', 'b344_checks.py', 'b345_checks.py', 'b346_checks.py'):
        b = blob_of(ROOT, 'tools/' + c)
        same.append(b is not None and norm(b) == norm(io.open(t(c), encoding='utf-8').read()))
    f3 = all(same)
    f4 = len(E['weakened']) >= 0 and 'IT IS A LOWER BOUND' in bf.upper()
    gf = f1 and f2 and f3 and f4
    print('    the four fixtures : %s ; this suite defines NO flattener of its own and uses the utility : %s' % (f1, f2))
    print('    every past checks file byte-identical to its blob : %s (%s)' % (f3, same))
    print('    the reach reported as a LOWER BOUND : %s ; arms weakened : %s' % (f4, E['weakened']))
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FLAT')

    print(chr(10) + '  G-RULE (both species in the rule; both incidents in the module; the September shape; local, NOT PUSHED):')
    mod = io.open(os.path.join(MOD, 'BAR_FLOOR_RULE.md'), encoding='utf-8').read()
    r1 = all(h in mod for h in ('## WHAT IT DOES', '## WHEN IT APPLIES', '## WHAT IT REFUSES', '## PROVENANCE'))
    r2 = 'b345' in mod and 'b346' in mod and '4.4e-18' in mod and '1e-25' in mod
    r3 = 'confers none' in mod and 'resolving-power rule' in mod
    tc_head = git(TC, 'rev-parse', '--short', 'HEAD').strip()
    tc_remote = subprocess.run(['git', '-C', TC, 'ls-remote', 'origin', 'main'], capture_output=True, text=True,
                               encoding='utf-8', errors='replace').stdout.split()
    r4 = bool(tc_head) and (not tc_remote or not tc_remote[0].startswith(tc_head))
    r5 = not git(TC, 'status', '--porcelain').strip()
    gr = r1 and r2 and r3 and r4 and r5
    print('    the September shape : %s ; both incidents with their figures : %s ; grade-honest and named as b322\'s case : %s' % (r1, r2, r3))
    print('    TECHNE local HEAD %s ; its remote does NOT carry it (NOT PUSHED) : %s ; its tree clean : %s' % (tc_head, r4, r5))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RULE')

    print(chr(10) + "  G-GATE (both arms; both polarities; the index-query arm untouched; the census; this act's own file gated):")
    g1 = RG.bar_floor_self_test(verbose=False)
    g2 = F['index_arm']
    g3 = F['registrations'] > 0 and F['would_fire'] + F['clear'] == F['registrations']
    g4 = F['own']['arm_misses'] >= 1 and 'AND THIS ACT DID NOT EXEMPT ITSELF' in bf
    gate_src = io.open(t('registration_gate.py'), encoding='utf-8').read()
    g5 = 'THEY MATCH TEXT' in gate_src and 'THE INDEX-QUERY GATE' in gate_src
    gg = g1 and g2 and g3 and g4 and g5
    print('    six fixtures, both polarities : %s ; the index-query arm still fires and still clears : %s' % (g1, g2))
    print('    the census adds up (%d fire + %d clear = %d) : %s' % (F['would_fire'], F['clear'], F['registrations'], g3))
    print("    this act's own registration fires on %d arm(s) and the bank says so : %s" % (F['own']['arm_misses'], g4))
    print('    the gate states its own reach and keeps its original header : %s' % g5)
    print('    %s' % ('PASS' if gg else '### FAIL ###'))
    if not gg:
        fails.append('G-GATE')

    print(chr(10) + '  G-TWOROUTES (one appended block; the module a true prefix of its prior bytes; the clause; b346 cited):')
    tr = io.open(os.path.join(MOD, 'TWO_ROUTES.md'), encoding='utf-8').read()
    trb = blob_of(TC, 'modules/2026-09/TWO_ROUTES.md')
    prev = subprocess.run(['git', '-C', TC, 'show', 'HEAD~1:modules/2026-09/TWO_ROUTES.md'], capture_output=True)
    prevtxt = prev.stdout.decode('utf-8', 'replace') if prev.returncode == 0 else None
    w1 = tr.count('<!-- b347 -->') == 1
    w2 = (prevtxt is not None) and norm(tr).startswith(norm(prevtxt).rstrip(chr(10)))
    w3 = 'one estimator' in tr and 'wearing two names' in tr and 'shared engine is named' in tr
    w4 = 'b346' in tr[tr.index('<!-- b347 -->'):]
    gw = w1 and w2 and w3 and w4
    print('    one block under the mark : %s ; a TRUE PREFIX of its prior committed bytes : %s' % (w1, w2))
    print("    the clause in the order's words : %s ; b346 cited in the block : %s" % (w3, w4))
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-TWOROUTES')

    print(chr(10) + '  G-STANDING (v2 by the generator; counts re-measured live; the author-ruled clause marked; the scan NOT taught):')
    fs = io.open(FS, encoding='utf-8').read()
    s1 = re.search(r'^VERSION: 2$', fs, re.M) is not None
    ck = subprocess.run([sys.executable, t('b335_standing.py'), '--check'], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    s2 = 'counts disagreeing with the file 0' in (ck.stdout or '') and 'VERSION in file 2' in (ck.stdout or '')
    s3 = '## AUTHOR-RULED CLAUSES (NOT MEASURED)' in fs and 'NOT MEASURED; carried by no count' in fs
    s4 = 'b344_ruling_2026-09-06.txt' in fs
    scan_src = io.open(t('ferry_scan.py'), encoding='utf-8').read()
    s5 = ('act number' not in scan_src.lower()) and 'THE SCAN HAS NOT BEEN TAUGHT THIS CLAUSE' in fs
    gs = s1 and s2 and s3 and s4 and s5
    print('    VERSION 2 : %s ; --check re-measures live with 0 disagreeing : %s' % (bool(s1), s2))
    print('    the clause in its own section, marked NOT MEASURED : %s ; the ruling cited : %s' % (s3, s4))
    print('    the scan was NOT taught the clause, and the file says so : %s' % s5)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-STANDING')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'EVERY LINE OF THIS ACT IS ABOUT AN INSTRUMENT' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTEXPLAINED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : bar-floor-rule returns 1 row(s)' in irun
    k2 = all(('%-40s NO KEY after  : True  PASS' % q) in irun for q in
             ('the audit is closed', 'the past acts are corrected', 'a sharper instrument is a result', 'the clock dates the old runs'))
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

    print(chr(10) + '  G-NOEDIT / G-PAPERS (no owner instrument; the papers repo untouched, so the hook and the mirror are NOT OWED):')
    owner = ['tools/e16/b264_eps_decay.py', 'tools/e16/qeps_layer.py', 'tools/b340_li_control.py',
             'tools/b327_bridge.py', 'tools/noise_floor.py', 'tools/reg_seal.py', 'tools/b339_limit.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    nohook = not os.path.exists(d('b347_hooks.txt')) and not os.path.exists(d('b347_mirror.txt'))
    gn = not touched and not ppstat and nohook and 'THE HOOK AND THE MIRROR ARE NOT OWED' in bf
    print('    owner instruments modified : %s ; papers-repo dirty paths : %s' % (touched or 'none', ppstat or 'none'))
    print('    no hook or mirror record written, and the bank says they are not owed : %s' % (nohook and 'THE HOOK AND THE MIRROR ARE NOT OWED' in bf))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOEDIT/G-PAPERS')

    print(chr(10) + '  G-ORDER (the seal verifies through its owning tool; the seal clock; the audit as it stands):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    # ### AND THE ORDERING, WHICH THIS ACT CAN NOW STATE FROM THE RUN FILE'S OWN CLOCK RATHER THAN FROM AN mtime.
    o3 = (stampm is not None) and (R['run_clock'] is not None) and (R['run_clock'] > stampm.group(1))
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes to the banked hash : %s ; the seal block carries its clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print("    ### AND THE ORDERING IS READ FROM TWO CLOCKS, NOT FROM FILE TIMES: seal %s < run %s : %s"
          % (stampm.group(1) if stampm else '?', R['run_clock'], o3))
    print('    the audit reads JOINTLY SATISFIABLE : %s' % o4)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    checks = [
        ('the run-file census %d / %d' % (C['runs'], C['with_clock']), ('`%d`' % C['runs']) in bank and ('`%d`' % C['with_clock']) in bank),
        ('the price counts', all(('`%d`' % x) in bank for x in (Dd['registrations'], Dd['carry'], Dd['pairable'], Dd['hand']))),
        ('the reach table', all(str(r['phrases']) in bank and str(r['both']) in bank for r in E['rows'])),
        ('the weakened count', ('`%d`' % len(E['weakened'])) in bank and (E['weakened'][0][1] in bf if E['weakened'] else True)),
        ('the census counts', all(('`%d`' % x) in bank for x in (F['registrations'], F['would_fire'], F['clear']))),
        ("this act's own arm miss and its line", ('`%d`' % F['own']['arm_misses']) in bank and ('`%d`' % F['own']['lines'][0][0]) in bank),
        ('the run clock %s' % R['run_clock'], R['run_clock'] in bank),
        ('the seal stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the seal hash', SEAL in bank),
    ]
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    checks.append(('%s clauses' % cl, ('%s clauses' % cl) in bank))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank))
    tch = git(TC, 'rev-parse', '--short', 'HEAD').strip()
    checks.append(('the TECHNE commit %s' % tch, ('`%s`' % tch) in bank))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path):')
    once = (all(os.path.exists(p) for p in [RRUN, CORR, IDX])
            and not os.path.exists(d('b347_repairs_run2.txt')))
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

    ib2 = idx[idx.index('# ### THE THREE REPAIRS AND THE TWO RULES (b347).'):idx.index('# ### THE EXPONENT BY RATE (b346).')] if '# ### THE THREE REPAIRS AND THE TWO RULES (b347).' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the module, the appended block, the index row, swept):' % ROWNUM)
    blk = tr[tr.index('<!-- b347 -->'):] if '<!-- b347 -->' in tr else ''
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the new module', mod), ('the appended block', blk), ('the index row', ib2)):
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
        print('    %-46s %-38s exists=%s tracked=%s' % (what[:46], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the module, the block and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b347_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the new module', mod),
                      ('the appended block', blk), ('the index row', ib2)):
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
