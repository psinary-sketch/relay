# -*- coding: utf-8 -*-
"""b346_checks.py -- THE GATE SUITE FOR THE EXPONENT BY RATE.

### ### **THE ARMS (registration section (G)):** `G-PREMISE` (both clauses computed from the record's own producing
### artifacts, b339's limit arithmetic IMPORTED; the reading by (C)'s rule; the one-axis sentence and the two unmoved
### axes named), `G-AXIS` (the rate along the ARGUMENT with b315's reason quoted; no cutoff quantity computed
### anywhere), `G-CELLS` (exactly b264's converged cells; the excluded rows present and excluded by its criterion,
### with its sentence quoted), `G-ROUTES` (route B calls no function of route A; both evaluators byte-identical to
### their blobs; the shared engine NAMED; the separation stated EXACT BY CONSTRUCTION and never as a measurement --
### ### **AND THE COLLAPSED ARM, WHICH THIS ACT EXPECTS AND TABLES, SO THE ARM REQUIRES THE BANK'S DECLARATION**),
### `G-RATE` (the uncertainty as the largest of three, each printed; the gate on each convention; the verdict by
### (D)'s rule), `G-MEANING` (the bank says what RESOLVED means BEFORE it says the verdict; b313's clause quoted; no
### sentence claims a convention correct), `G-ERRATA` (one block under the mark, the entry byte-identical, the file a
### true prefix of its blob), `G-ROW`, `G-KEY` / `G-NOTEXPLAINED`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`,
### `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, the sweeps, `G-SHARED`, the hedge audit, the must-fail fixtures; re-run after
### the push. ### **THE PAPERS REPO MOVES, SO THE HOOK AND THE MIRROR ARE OWED.**
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
E16 = os.path.join(ROOT, 'tools', 'e16')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
ERRATA = os.path.join(PP, 'ERRATA.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b346_the_exponent_by_rate.txt')
REG = d('b346_registration_2026-09-06.txt')
RULING = d('b346_ruling_2026-09-06.txt')
EXTRACT = d('b346_extract_notes.txt')
FERRY = d('b346_ferry_2026-09-06.txt')
RRUN, RJ = d('b346_rate_run.txt'), d('b346_rate.json')
FRUN, FJ = d('b346_filings_run.txt'), d('b346_filings.json')
CORR, IDX = d('b346_corr_run.txt'), d('b346_index_run.txt')
SCAN, RSCAN, TERMSCAN, GATE = d('b346_ferry_scan.txt'), d('b346_ruling_scan.txt'), d('b346_reg_termscan.txt'), d('b346_reg_gate.txt')
CENSUS, FCEN = d('b346_census.txt'), d('b346_faces_census.txt')
REGSPEC, SATIS = d('b346_regspec_run.txt'), d('audit_b346_reg_satisfiable.txt')
PINS, INDEXQ = d('b346_pins_stepzero.txt'), d('audit_b346_index_query.txt')
SEAL = '880aba8ca466f5007c158efcc9832ddd8e31a048abc47d2e6aca9f9760f9d961'
MARK_E = '<!-- b346 -->'
ENTRY = 'E-2026-09-03-1'
ROWNUM = '194'

OWNED = [BANK, REG, RULING, RRUN, RJ, FRUN, FJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         TERMSCAN, RSCAN, d('b346_satisfiable.json'),
         t('b346_extract.py'), t('b346_regspec.py'), t('b346_rate.py'), t('b346_filings.py'),
         t('b346_correspondence.py'), t('b346_index_append.py')]

CARRIERS = [
    (t('b346_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (RSCAN, "the ruling scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]
NEW_THIS_ACT = {'tools/b346_extract.py', 'tools/b346_regspec.py', 'tools/b346_rate.py', 'tools/b346_filings.py',
                'tools/b346_correspondence.py', 'tools/b346_index_append.py', 'tools/b346_checks.py'}

TOOLNUM = [
    ('the premise, the rate, the uncertainty, the verdict', 'tools/b346_rate.py'),
    ("b339's limit arithmetic, imported", 'tools/b339_limit.py'),
    ("the corpus's convention, imported and not edited", 'tools/e16/b264_eps_decay.py'),
    ("the source's convention, b313's copy, imported and not edited", 'tools/e16/b313f_b264_eps_decay.py'),
    ('the shared prolate layer', 'tools/e16/qeps_layer.py'),
    ('the shared node counts', 'tools/e16/b38_act10.py'),
    ('the RESOLVED gate at both conventions', 'tools/noise_floor.py'),
    ('the ERRATA block', 'tools/b346_filings.py'),
    ('row 194', 'tools/b346_correspondence.py'),
    ('the key', 'tools/b346_index_append.py'),
    ('29 clauses', 'tools/b346_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('20553 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('b339 -- the verdict, UNAFFORDABLE', d('b339_the_exponent_resolved.txt'),
     '### ### **(1) THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED.**'),
    ('### a floor and not zero', d('b339_the_exponent_resolved.txt'),
     '### ### What it says is that the residual the price extrapolated is descending toward a FLOOR and not'),
    ("### the floor's three candidate origins", d('b339_the_exponent_resolved.txt'),
     "### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut's `tau`, the"),
    ('b344 -- the residual converges in NY', d('b344_the_floor_priced.txt'),
     "### CORPUS'S OWN `NY = 512` THE REMAINING TRAVEL IS `7.059e-04`, about a ninth of the floor**; from"),
    ('### one axis moved is one axis moved', d('b344_the_floor_priced.txt'),
     '### **ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    ('b264 -- the decay table head', d('b264_run.txt'),
     '  rho       NG       eps_even         envelope C/rho   rel(NG,2NG)  rel(NQ,2NQ)  rho^1.5*eps    converged'),
    ('### the top converged cell', d('b264_run.txt'),
     '  100       800      1.559480084e-03  1.327819084e+00  2.49e-09     1.21e-09     1.559480084    True'),
    ('### the void rows are not evidence', d('b264_run.txt'),
     '  ### ### VALUE THAT IS WRONG BY ORDERS OF MAGNITUDE. ### THEY ARE NOT EVIDENCE ABOUT'),
    ("### b264's own formula, the exponent in front", d('b264_eps_even_decay.txt'),
     '###   ### **`eps_n(rho) = [lam^2/(1-lam^2)] rho^{-1/2} INT_{1/rho}^{1} A_n(u) A_n(rho u) du`**'),
    ('b315 -- a full power along the argument, none along the cutoff', d('b315_components_run.txt'),
     '    ### ARGUMENT the rate moves a full power; ### **ALONG THE CUTOFF IT DOES NOT MOVE AT'),
    ('b313 -- the exponent is fixed by the source\'s definition', d('b313_the_exponent.txt'),
     "### THE EXPONENT IS FIXED BY THE SOURCE'S OWN DEFINITION OF THE OBJECT THE CORPUS"),
    ('b312 -- eight agree, the ninth is the act', d('b312_the_remainder.txt'),
     '### ### **EIGHT AGREE. ### THE NINTH IS THE WHOLE OF THIS ACT.**'),
    ('the erratum -- the two functions differ by a factor of rho', ERRATA,
     '**The two functions therefore differ by a factor of `\u03c1`, which is not a scalar.**'),
    ("the owner's evaluator, unedited", os.path.join(E16, 'b264_eps_decay.py'),
     '    return lam2 / (1 - lam2) * (r ** -0.5) * I'),
    ("the flipped copy, the source's convention", os.path.join(E16, 'b313f_b264_eps_decay.py'),
     '    return lam2 / (1 - lam2) * (r ** 0.5) * I'),
    ('the order -- leg 2, the exponent by rate', FERRY, 'LEG 2 (b345) \u2014 THE EXPONENT BY RATE: the value-based split is'),
    ('the ruling -- the rate is the principled discriminator', RULING, 'reading makes the rate the principled discriminator rather than'),
]

SELF_NEEDLES = [
    ('the bank states the floor first', BANK, '### ### ### **A FLOOR IS PRESENT. ### SO NO DOMAIN RESOLVES THE EXPONENT BY VALUE.**'),
    ('### and the resolving power', BANK, '### ### ### **AND ON THE RATE AXIS THE QUESTION IS RESOLVED, AT A RESOLVING POWER OF `63.6`.**'),
    ('### no convention is declared correct', BANK, '###   ### **(i) NO CONVENTION IS DECLARED CORRECT.**'),
    ('### the separation was not measured', BANK, '###   ### **(ii) THE SEPARATION WAS NOT MEASURED.**'),
    ('### the floor is not explained', BANK, '###   ### **(iii) THE FLOOR IS NOT EXPLAINED.**'),
    ("### b339's ratios reading is narrower than its sentence", BANK,
     '### ### **AND ONE READING OF b339\'s IS NARROWER THAN ITS SENTENCE, MEASURED HERE AND REPORTED.**'),
    ('### an axis that absorbs the difference cannot show it', BANK, '### ### **AN AXIS THAT ABSORBS THE DIFFERENCE CANNOT SHOW IT.**'),
    ('### exact by construction rather than measured', BANK, '### ### ### **THAT IS THE SEPARATION, AND IT IS EXACT BY CONSTRUCTION RATHER THAN MEASURED.**'),
    ('### the verdict', BANK, '### ### ### **VERDICT: RESOLVED ON THIS AXIS.**'),
    ('### the banked values carry the corpus\'s own', BANK, "### ### ### **THE BANKED VALUES CARRY THE CORPUS'S OWN `r ** -0.5`.**"),
    ('### what resolved is permitted to mean', BANK, '### ### **AND WHAT THAT IS PERMITTED TO MEAN, IN THE SEALED REGISTRATION\'S OWN WORDS, FIXED BEFORE THE'),
    ('### (E1) the collapsed arm', BANK, '### ### **(E1) ONE OF THE SEALED UNCERTAINTY ARMS DID NO WORK, AND THE SEALED PAIRING IS DEFECTIVE.**'),
    ('### the routes are not independent at the top', BANK, '### ### WINDOW, AND THIS ACT SAYS SO RATHER THAN REPORTING THEM AS AGREEING.**'),
    ('### the direction of the risk', BANK, '### ### **THE DIRECTION OF THE RISK, NAMED:**'),
    ('### a bar whose two arms are the same arm', BANK, '### ### THAT ORDER: A BAR WHOSE TWO ARMS ARE THE SAME ARM.**'),
    ('### (E2) the shared engine', BANK, '### ### **(E2) THE TWO EVALUATORS SHARE AN ENGINE, AND IT IS NAMED RATHER THAN CLAIMED ABSENT.**'),
    ("### (E3) the ruling's citation hit", BANK, "### ### **(E3) THE RULING'S CITATION HIT, RULED.**"),
    ('### the expectations scored', BANK, "### (7) BOTH SEATS' EXPECTATIONS, SCORED."),
    ('### what this act does not conclude', BANK, '### ### **NOT THAT A CONVENTION IS CORRECT. ### NOT THAT b313 IS SUPERSEDED. ### NOT THAT THE FLOOR IS'),
]

MUST_FAIL = [
    ('the bank never says a convention is correct', BANK, '### THE SOURCE\'S CONVENTION IS CORRECT.'),
    ('the bank never says the corpus\'s convention is correct', BANK, "### THE CORPUS'S CONVENTION IS CORRECT."),
    ('the bank never says the floor is explained', BANK, '### THE FLOOR IS EXPLAINED.'),
    ('the bank never says b313 is superseded', BANK, '### b313 IS SUPERSEDED.'),
    ('the bank never says the separation was measured', BANK, '### THE SEPARATION WAS MEASURED.'),
]


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def flat(s):
    # ### THE FLATTENER STRIPS **REPEATED** LEADING MARKERS. ### b344's and b345's stripped only one, so a sentence
    # ### continued onto a `### ###` line kept a marker in the MIDDLE of it and no flattened grep could match it.
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^(?:###\s*)+', ' ', s.replace('\u2019', "'"))).strip()


def strip_prose(path):
    """### THE SOURCE WITH ITS COMMENTS AND STRING LITERALS REMOVED. ### **A `G-NO*` ARM THAT GREPS RAW SOURCE FIRES
    ### ON THE ACT'S OWN SENTENCE SAYING THE THING WAS NOT DONE** (b316, b317, b345); this is that species, closed."""
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


def calls(path, funcs):
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
                        out.add((f.value.id if isinstance(f.value, ast.Name) else '?') + '.' + f.attr)
    return out


def main():
    fails = []
    print('=' * 100)
    print('b346 -- GATE SUITE (A PREMISE TESTED, A DIFFERENT AXIS MEASURED, AND AN ARM THAT COLLAPSED)')
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
    R = json.load(io.open(RJ, encoding='utf-8'))
    F = json.load(io.open(FJ, encoding='utf-8'))
    P, K = R['premise'], R['rate']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    run = io.open(RRUN, encoding='utf-8').read()

    print(chr(10) + "  G-PREMISE (both clauses from the record's own artifacts; the reading by (C)'s rule; the one-axis sentence):")
    p1 = P['c1'] and all(r['above_both'] for r in P['rows'])
    p2 = P['c2'] and P['frac'] < 1.0
    p3 = (P['present'] == (p1 and p2)) and 'A FLOOR IS PRESENT' in bank
    p4 = 'THE FLOOR IS NOT EXPLAINED' in bank and "the cut's `tau` and the taper are named" in bf
    imported = 'b339_limit.json' in io.open(t('b346_rate.py'), encoding='utf-8').read()
    p5 = ('b339' in bf) and imported
    gp = p1 and p2 and p3 and p4 and p5
    print('    (C1) the limit above BOTH candidates at every covered cell : %s' % p1)
    print("    (C2) the whole remaining travel in NY is %.4f of b339's floor, strictly less than one : %s" % (P['frac'], p2))
    print('    the reading follows (C)\'s rule and the bank states it : %s ; the one-axis limit stated : %s' % (p3, p4))
    print("    b339's own record is the source of (C1) rather than a re-implementation : %s" % p5)
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PREMISE')

    print(chr(10) + '  G-AXIS (the rate along the ARGUMENT, with b315\'s reason quoted; no cutoff quantity computed):')
    a1 = 'AN AXIS THAT ABSORBS THE DIFFERENCE CANNOT SHOW IT' in bank
    a2 = 'the rate moves a full power' in bf and 'IT DOES NOT MOVE AT ALL' in bf
    code = strip_prose(t('b346_rate.py'))
    a3 = ('cutoff' not in code.lower()) and ('E2even' not in code) and ('log a' not in code)
    ga = a1 and a2 and a3
    print("    the bank states the reason and quotes b315 at both halves : %s / %s" % (a1, a2))
    print('    no cutoff quantity appears in the instrument\'s CODE (comments and strings stripped) : %s' % a3)
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-AXIS')

    print(chr(10) + "  G-CELLS (exactly b264's converged cells; the excluded rows excluded by ITS criterion):")
    b264 = io.open(d('b264_run.txt'), encoding='utf-8').read()
    marked = [int(m.group(1)) for m in re.finditer(r'(?m)^\s*(\d+)\s+\d+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+True\s*$', b264)]
    c1 = K['cells'] == marked
    c2 = all(str(x) in bank for x in K['dropped']) and 'ARE NOT EVIDENCE ABOUT' in bank
    c3 = "BY b264's CRITERION AND NOT BY A CHOICE THIS ACT MAKES" in bf
    gc = c1 and c2 and c3
    print("    the cells used are exactly b264's converged marking %s : %s" % (marked, c1))
    print("    the excluded rows named in the bank with b264's own sentence : %s ; excluded by its criterion, said : %s" % (c2, c3))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CELLS')

    print(chr(10) + '  G-ROUTES (route B calls no function of route A; both evaluators unedited; the shared engine NAMED; the collapsed arm DECLARED):')
    ob = blob_of(ROOT, 'tools/e16/b264_eps_decay.py')
    fb = blob_of(ROOT, 'tools/e16/b313f_b264_eps_decay.py')
    r1 = (ob is not None) and norm(ob) == norm(io.open(os.path.join(E16, 'b264_eps_decay.py'), encoding='utf-8').read())
    r2 = (fb is not None) and norm(fb) == norm(io.open(os.path.join(E16, 'b313f_b264_eps_decay.py'), encoding='utf-8').read())
    cb = calls(t('b346_rate.py'), {'route_B'})
    r3 = 'route_A' not in cb
    r4 = 'A SHARED ENGINE IS A SHARED ERROR SOURCE' in bf and 'EPS_NQ' in bank
    r5 = 'EXACT BY CONSTRUCTION' in bank and 'THE SEPARATION WAS NOT MEASURED' in bank
    # ### the collapsed arm: this act EXPECTS it and TABLES it, so the arm asks for the declaration, not for a pass.
    collapsed = K['collapse']
    r6 = (not collapsed) or ('(E1) ONE OF THE SEALED UNCERTAINTY ARMS DID NO WORK' in bank
                             and 'TABLED AND NOT REPAIRED' in flat(bank).upper()
                             and 'IT CAN ONLY LEAVE' in bank)
    gr = r1 and r2 and r3 and r4 and r5 and r6
    print("    the owner's evaluator byte-identical to its blob : %s ; b313's copy byte-identical : %s" % (r1, r2))
    print('    route B calls no function of route A : %s (its calls: %s)' % (r3, sorted(cb)))
    print('    the shared engine named in the bank : %s ; the separation stated exact by construction : %s' % (r4, r5))
    print('    the arms collapsed : %s ; DECLARED in the bank as (E1) with the risk direction named : %s' % (collapsed, r6))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-ROUTES')

    print(chr(10) + "  G-RATE (the uncertainty as the largest of three, each printed; the gate at both conventions; the verdict by (D)'s rule):")
    u = max(K['u1'], K['u2'], K['u3'])
    t1 = abs(u - R['uncertainty']) < 1e-18
    t2 = all(('(u%d)' % i) in run for i in (1, 2, 3))
    t3 = K['gate_ok'] and ('RESOLVED' in run)
    t4 = (R['verdict'] == 'RESOLVED') == (K['gate_ok'] and R['separation'] > R['uncertainty'])
    t5 = abs(R['resolving_power'] - R['separation'] / R['uncertainty']) < 1e-9
    gt = t1 and t2 and t3 and t4 and t5
    print('    the uncertainty is the largest of the three : %s ; all three printed : %s' % (t1, t2))
    print('    the noise-floor gate RESOLVED at both conventions : %s' % t3)
    print("    the verdict follows (D)'s rule and no other : %s ; the resolving power recomputes : %s" % (t4, t5))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-RATE')

    print(chr(10) + '  G-MEANING (the bank says what RESOLVED means BEFORE the verdict; b313 quoted; no convention called correct):')
    i_mean = bank.find('WHAT THAT IS PERMITTED TO MEAN')
    i_verd = bank.find('VERDICT: RESOLVED ON THIS AXIS')
    m1 = bank.find('NO CONVENTION IS DECLARED CORRECT') < i_verd  # ### the refusal precedes the verdict
    m2 = "THE EXPONENT IS FIXED BY THE SOURCE'S OWN DEFINITION" in bf
    m3 = 'IT DOES NOT MEAN THAT A CONVENTION IS CORRECT' in bank
    m4 = i_mean > 0 and 'FIXED BEFORE THE' in bank
    m5 = 'IT DOES NOT MEAN THAT A CONVENTION IS CORRECT' in reg  # ### and it was sealed
    gm = m1 and m2 and m3 and m4 and m5
    print('    the refusal appears before the verdict in the bank : %s' % m1)
    print("    b313's clause quoted : %s ; the limit stated : %s ; and it was SEALED before any figure : %s" % (m2, m3, m5))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-MEANING')

    print(chr(10) + '  G-ERRATA (one block under the mark, against the named entry, the entry byte-identical, a true prefix of its blob):')
    er = io.open(ERRATA, encoding='utf-8').read()
    eb = blob_of(PP, 'ERRATA.md')
    e1 = er.count(MARK_E) == 1 and F['errata'] in ('WRITTEN', 'DUPLICATE')
    blk = er[er.index(MARK_E):] if MARK_E in er else ''
    e2 = ENTRY in blk and 'mechanical test' in blk
    e3 = (eb is not None) and norm(er).startswith(norm(eb).rstrip(chr(10)))

    def entry_text(s):
        i = s.index('## %s' % ENTRY)
        j = s.find(chr(10) + '## ', i + 1)
        return s[i:j if j > 0 else len(s)]
    e4 = (eb is not None) and entry_text(norm(er)) == entry_text(norm(eb))
    e5 = 'no new entry is opened' in blk.lower() and 'not make either convention correct' in blk
    ge = e1 and e2 and e3 and e4 and e5
    print('    one block under the mark : %s ; it names the entry and its test : %s' % (e1, e2))
    print('    the file a true prefix of its blob : %s ; the named entry BYTE-IDENTICAL to its blob : %s' % (e3, e4))
    print('    the block refuses the two overreadings : %s' % e5)
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-ERRATA')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    gw = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'A RESOLVING POWER IS A PROPERTY OF THE INSTRUMENT' in rows[0] and anc
    print('    row %s present once : %s ; NO TERMINAL with the reason : %s ; true prefix of its blob : %s'
          % (ROWNUM, len(rows) == 1, bool(rows and 'NO TERMINAL, AND THE REASON' in rows[0]), anc))
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTEXPLAINED (one key, one row; the must-not-hit queries NO KEY; the answer refuses the overreadings):')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : exponent-by-rate returns 1 row(s)' in irun
    k2 = all(('%-38s NO KEY after  : True  PASS' % q) in irun for q in
             ('the convention is correct', 'the floor is explained', 'b313 is superseded', 'the exponent is settled'))
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

    print(chr(10) + "  G-NOEDIT (no owner instrument edited; the deposit and HANDOFF clean; only this act's papers path touched):")
    owner = ['tools/e16/b264_eps_decay.py', 'tools/e16/b313f_b264_eps_decay.py', 'tools/e16/qeps_layer.py',
             'tools/e16/b38_act10.py', 'tools/b339_limit.py', 'tools/b313_flip.py', 'tools/noise_floor.py',
             'tools/reg_seal.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'ERRATA.md']
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    gn = not touched and not ppbad and hand and dep
    print('    owner instruments modified : %s ; papers-repo paths beyond ERRATA.md : %s' % (touched or 'none', ppbad or 'none'))
    print('    HANDOFF.md clean : %s ; the deposited monograph clean : %s' % (hand, dep))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies through its owning tool; the seal clock; the audit as it stands):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    text_reg = io.open(REG, encoding='utf-8', errors='replace').read()
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in text_reg)
    o1 = o1 and hashlib.sha256(norm(text_reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', text_reg)
    o2 = stampm is not None
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    span = max(os.path.getmtime(x) for x in (REG, RRUN)) - min(os.path.getmtime(x) for x in (REG, RRUN))
    times_carry = span > 60.0
    o3 = (os.path.getmtime(RRUN) > os.path.getmtime(REG)) if times_carry else None
    o3ok = bool(o3) if times_carry else ('THE ORDERING IS NOT RECOVERABLE FROM FILE TIMES AFTER A CHECKOUT' in bank)
    go = o1 and o2 and o3ok and o4
    print('    the seal recomputes to the banked hash : %s ; the seal block carries its own clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    file times still carry the ordering (spread %.1f s) : %s' % (span, times_carry))
    if times_carry:
        print("    the instrument's run file is younger than the sealed registration : %s" % o3)
    else:
        print('    ### THE CHECKOUT REWROTE EVERY MTIME (b345 (E4)); the bank must declare it : %s' % o3ok)
    print('    the audit reads JOINTLY SATISFIABLE : %s' % o4)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED):')
    hookp, mirrorp = d('b346_hooks.txt'), d('b346_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht, mt = io.open(hookp, encoding='utf-8', errors='replace').read(), io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh = h_ok and m_ok
        print('    hook: 0 repos failing and all three byte-identical : %s ; mirror: clean on all three clauses : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    checks = []
    checks.append(('the uncertainty %.6e' % R['uncertainty'], ('%.6e' % R['uncertainty']) in bank))
    checks.append(('the resolving power %.1f' % R['resolving_power'], ('%.1f' % R['resolving_power']) in bank))
    checks.append(('the slope at the top %.9f' % R['slope_top'], ('%.9f' % R['slope_top']) in bank))
    checks.append(('the two distances', ('%.6e' % R['d_corpus']) in bank and ('%.6e' % R['d_source']) in bank))
    checks.append(('the three uncertainty arms', all(('%.6e' % x) in bank for x in (K['u1'], K['u2'], K['u3']))))
    checks.append(('the whole-window diagnostic %.6e and %.1f' % (K['whole_window'], K['resolving_whole']),
                   ('%.6e' % K['whole_window']) in bank and ('%.1f' % K['resolving_whole']) in bank))
    checks.append(('the premise fraction %.4f' % P['frac'], ('%.4f' % P['frac']) in bank))
    checks.append(('the ladder residual', all(('%+.9f' % x) in bank for x in P['residual'])))
    checks.append(('the extrapolated limit and the travel',
                   ('%+.9f' % P['limit']) in bank and ('%.3e' % P['travel']) in bank and ('%+.9f' % P['floor']) in bank))
    checks.append(('every (C1) row', all(('%.9f' % r['m_inf']) in bank and ('%.9f' % r['off_ef']) in bank for r in P['rows'])))
    checks.append(('every eps value, both conventions',
                   all(('%.15e' % x) in bank for x in K['eps_corpus']) and all(('%.15e' % x) in bank for x in K['eps_source'])))
    checks.append(('every route A slope', all(('%.9f' % x) in bank for x in K['routeA_corpus'] + K['routeA_source'])))
    checks.append(('the G-REPRO worst %.3e' % K['repro'], ('%.3e' % K['repro']) in bank))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank))
    sm = re.search(r'### bytes sealed : (\d+)', text_reg).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    checks.append(('%s clauses' % cl, ('%s clauses' % cl) in bank))
    checks.append(('the seal hash', SEAL in bank))
    checks.append(('the seal stamp', (stampm.group(1) if stampm else 'x') in bank))
    checks.append(('the NQ %d' % K['NQ'], ('%d' % K['NQ']) in bank))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path):')
    once_ok = (all(os.path.exists(p) for p in [RRUN, FRUN, CORR, IDX])
               and not os.path.exists(d('b346_rate_run2.txt'))
               and not os.path.exists(d('b346_filings_run2.txt')))
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

    ib = idx[idx.index('# ### THE EXPONENT BY RATE (b346).'):idx.index('# ### THE LI CONTROL, RE-RUN (b345).')] if '# ### THE EXPONENT BY RATE (b346).' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the errata block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the errata block', blk), ('the index row', ib)):
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
        print('    %-56s %-38s exists=%s tracked=%s' % (what[:56], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the errata block and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b346_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the errata block', blk), ('the index row', ib)):
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
