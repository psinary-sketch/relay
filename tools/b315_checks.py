# -*- coding: utf-8 -*-
"""b315_checks.py -- THE GATE SUITE FOR A READ AND A RE-DERIVATION.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### **`G-NOREVERDICT`** ### -- the act corrects a REASON two acts carried. ### Its must-fail
###     fixtures are the sentences a re-verdict would have produced. ### **A CORRECTION THAT REMOVES
###     ### A CAUTION IS THE EASIEST THING IN THIS RECORD TO OVERSTATE.**
###   ### **`G-NOLICENCE`** ### -- and the second-easiest: ### **REMOVING A WRONG REASON FOR
###     ### REFUSING TO READ A COLUMN IS NOT A REASON TO READ IT.**
###   ### **`G-NOEDIT`** ### -- the owner instruments byte-identical to `git HEAD`, checked AFTER
###     the run.
###   ### **`G-CONVERGED`** ### -- every rate and envelope statement read on cells passing b264's
###     OWN two-axis test, not a ceiling number.
###   ### **`G-COVERAGE`** ### -- the new kernel gate was written, RUN, and FAILED, with nothing
###     repaired. ### **A GATE ADDED IN THE STATE WHERE IT PASSES TELLS NOBODY ANYTHING.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b302_kernel as KRN  # noqa: E402

D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS = ['tools/e16/qeps_layer.py', 'tools/e16/b38_act10.py',
          'tools/e16/b264_eps_decay.py', 'tools/e16/carto_atlas.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def e(n):
    return os.path.join(E16, n)


BANK = d('b315_the_calibration_and_the_rate.txt')
REG = d('b315_registration_2026-09-03.txt')
RUN = d('b315_components_run.txt')
COV = d('b315_coverage_gate.txt')
SCAN = d('b315_ferry_scan.txt')
FERRY = d('b315_ferry_2026-09-03.txt')
CENSUS = d('b315_census.txt')

OWNED = [RUN, COV, CENSUS, d('b315_corr_row.txt'), d('b315_index_query.txt'),
         d('b315_index_run.txt'), d('b315_pins_stepzero.txt'), d('b315_regspec_run.txt'),
         d('b315_satisfiable.json'), d('b315_rows.json'),
         t('b315_regspec.py'), t('b315_correspondence.py'), t('b315_run.py'),
         t('b315_coverage_gate.py')]

CARRIERS = [
    (t('b315_checks.py'), 'its own fixtures'),
    (t('b315_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("the atlas's disclaimed register", e('carto_atlas.py'), 'No sign claim is made'),
    ("### the atlas's calibration bracket", e('carto_atlas.py'),
     'sign fixed BY the E2 calibration'),
    ("### the atlas's `E2` tolerance -- the OTHER E2", e('carto_atlas.py'),
     'E2 pass tolerance on the explicit-formula residual'),
    ("### the atlas's registered claims", e('carto_atlas.py'), 'E1-E4 stand registered VERBATIM'),
    ("### the operation that computes A", e('carto_atlas.py'), 'A = float(np.trapezoid'),
    ("### the operation that forms the residual", e('carto_atlas.py'),
     'residual=Z - (P - PR + A)'),
    ("### and the verdict line that names E2", e('carto_atlas.py'), 'E2 VERDICT'),
    ("b38's own A, in its own file", e('b38_act10.py'), 'A = float(np.trapezoid'),
    ("b264 -- the envelope", d('b264_eps_even_decay.txt'), '`|eps_even(x)| <= C_even / x`'),
    ("### b264 -- the sharp rate", d('b264_eps_even_decay.txt'),
     '`x^{3/2} eps_even(x) -> K_even'),
    ("### b264 -- M_even", d('b264_eps_even_decay.txt'),
     'M_even = INT_1^inf eps_even(x) dx/x'),
    ("### b264 -- the cutoff asymptote, ITS derivation", d('b264_eps_even_decay.txt'),
     'E2even(a) * log a -> p(0) * M_even'),
    ("### b264 -- why the second convergence axis exists", d('b264_eps_even_decay.txt'),
     'THE REGISTERED CONVERGENCE TEST CANNOT SEE THE ERROR THAT BINDS'),
    ("b233 -- the two claims are different", d('b233_the_arrangement.txt'),
     'THOSE ARE DIFFERENT CLAIMS'),
    ("b235 -- a sign warranted by a calibration", d('b235_phase11_conventions.txt'),
     'sign warranted by a calibration is an instrument fact, not a text'),
    ("b242's law, as b261 carries it", d('b261_e2even_monotone.txt'),
     'A MEASURED RATE IS NOT A TAIL BOUND'),
    ("b15's ceiling, as b261 carries it", d('b261_e2even_monotone.txt'),
     'AT A FINITE CUTOFF DECIDES NOTHING GLOBAL'),
    ("b200 -- the double-name species", d('b200_sector_naming.txt'), 'THE DOUBLE-NAME SPECIES'),
    ("b312 -- the sentence this act corrects the reason of", d('b312_the_remainder.txt'),
     'sign fixed BY the E2 calibration'),
    ("b313 -- the caution this act corrects", d('b313_the_exponent.txt'),
     'ITS SIGN WAS CALIBRATED'),
    ("b250 -- the convention-bearing step", d('b250_m4_derivation.txt'), 'from `rho^{-1/2}`'),
    ("b266 -- the asymptote it quotes", d('b266_state_of_the_shadow.txt'), 'derived asymptote'),
]

SELF_NEEDLES = [
    ('bank states the six answers first', BANK, 'THE ANSWERS, FIRST'),
    ('bank gives the sign-only verdict', BANK, 'THE CALIBRATION FIXES A SIGN ONLY'),
    ('### bank names the double name', BANK, 'ONE NAME FOR TWO OBJECTS'),
    ('bank gives the SURVIVES verdict', BANK, 'VERDICT: ### SURVIVES'),
    ('bank promotes the column to nothing', BANK, 'PROMOTED TO NOTHING'),
    ('### bank refuses the licence reading', BANK, 'NOT A LICENCE TO INTERPRET'),
    ('bank says the refusal stands on a stronger ground', BANK,
     'AND THE SECOND GROUND IS THE STRONGER ONE'),
    ('bank gives the coverage gate result', BANK, 'AND IT FAILS'),
    ('bank says why a failing gate is the point', BANK, 'WHOSE FIRING'),
    ('bank names both coverage counts', BANK, 'THE TWO COUNTS DIFFER AND BOTH ARE PRINTED'),
    ('bank gives the line numbers', BANK, 'carto_atlas.py:66'),
    ('bank cites the corpus own earlier reads', BANK, 'THIS ACT DID NOT FIND IT FIRST'),
    ('bank gives the independence result', BANK, 'dependence on the remainder'),
    ('bank names the positive control', BANK, 'A SENTENCE ABOUT THE SEARCH'),
    ('bank gives the A plus E2 table', BANK, 'A+E2 banked'),
    ('bank gives the constant envelope', BANK, 'THE NEW ENVELOPE IS A CONSTANT'),
    ('bank calls the envelope a loss', BANK, 'A LOSS, NOT A NEUTRAL RESTATEMENT'),
    ('bank gives the sharp rate', BANK, 'THE SAME CONSTANT'),
    ('bank uses b264 two-axis test', BANK, 'TWO-AXIS TEST'),
    ('bank gives the ladder', BANK, 'VIOLATIONS OF THE NEW CONSTANT ENVELOPE'),
    ('bank calls the envelope vacuous', BANK, 'VACUOUS IN THE LIMIT'),
    ('bank cites b264 for the dilation route', BANK, 'THE ROUTE IS b264'),
    ('bank gives the cutoff order result', BANK, 'WHAT'),
    ('### bank owns the negative-integral defect', BANK, 'A NEGATIVE VALUE FOR AN INTEGRAL'),
    ('bank says where the ceiling is', BANK, 'THE CEILING IS WHERE THE EVALUATOR FAILS'),
    ('bank says the tail is uncontrolled', BANK, 'NO RIGOROUS TAIL BOUND'),
    ('bank reports the bench as direction-only', BANK, 'NOT IN THE ASYMPTOTIC REGIME'),
    ('bank bounds the bearing', BANK, 'BEARING ONLY'),
    ('bank carries b242 law', BANK, 'A MEASURED RATE IS NOT A TAIL'),
    ('bank gives component 3', BANK, 'WHAT MOVES IN THE RECORD'),
    ('bank says component 3 is not a sweep', BANK, 'A READING AND NOT A SWEEP'),
    ('bank gives the F1 verdict', BANK, 'CONFIRMED, BOTH HALVES'),
    ('bank gives the F2 verdict', BANK, 'REFINED IN ITS SECOND'),
    ('bank restates the object three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank keeps M-2 unchanged under its cap', BANK, 'UNDER b310'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'DAYS PAST BOTH'),
    ('bank records the W2 ruling', BANK, 'RECORDED AND UNAPPLIED'),
    ('bank restates the kernel-coverage order', BANK, 'W-ORD-KERNEL-COVERAGE'),
    ('bank restates the absolute-path order', BANK, 'W-ORD-ABSOLUTE-PATHS'),
    ('bank files the source-tail order', BANK, 'W-ORD-SOURCE-TAIL'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank names the next act with its cost', BANK, 'THE TRUNCATION NOBODY OWNS'),
    ('bank reports the census with its scope', BANK, 'TOTAL MISSING : 0'),
    ('bank states what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('bank declares its deviations', BANK, 'DEVIATIONS, DECLARED'),
    ('registration splits what it precedes', REG, 'THE COMPONENTS HAVE RUN'),
    ('registration caps pre-asymptotic constants', REG,
     'constants read off pre-asymptotic cells'),
    ('registration records both expectations', REG, 'the cancellation SURVIVES'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives the SURVIVES verdict', RUN, 'VERDICT: SURVIVES'),
    ('the run gives the two-axis stop', RUN, 'first cell that FAILS the two-axis test'),
    ('the coverage log reports the failure', COV, 'GATE FAILS'),
    ('the coverage log names both counts', COV, 'MODULES WITH A PRINT TARGET AND NOT IMPORTED'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### ### **`G-NOREVERDICT`.**
    ('b312 is not re-verdicted', BANK, 'b312 IS RE-VERDICTED.'),
    ('b313 is not re-verdicted', BANK, 'b313 IS RE-VERDICTED.'),
    ('no banked number is called wrong', BANK, 'THE BANKED NUMBERS ARE WRONG.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('b264 is not re-verdicted', BANK, 'b264 IS RE-VERDICTED.'),
    # ### **`G-NOLICENCE` -- the sentences a licence to interpret would have produced.**
    ('the column is not interpreted', BANK, 'THE CANCELLATION MEANS THE TERMS ARE EQUAL.'),
    ('no identity is claimed', BANK, 'E2 IS MINUS A.'),
    ('the caution is not simply dropped', BANK, 'THE COLUMN MAY NOW BE READ.'),
    # ### **THE DERIVATION'S OWN LIMITS.**
    ('the constant is not certified', BANK, 'THE CUTOFF CONSTANT IS CERTIFIED.'),
    ('no tail bound is claimed', BANK, 'THE TAIL IS BOUNDED.'),
    ('the branch is not decided', BANK, 'THE BRANCH IS DECIDED.'),
    ('the archimedean side is not spoken for', BANK, 'THE ARCHIMEDEAN SIDE VANISHES.'),
    # ### **THE STANDING CAPS.**
    ('nothing is repaired in the kernel', BANK, 'THE MODULES ARE ADDED.'),
    ('no instrument is edited', BANK, 'THE OWNER INSTRUMENT IS EDITED.'),
    ('M-2 is not verdicted', BANK, 'M-2 IS UNSATISFIABLE.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]

TOOLNUM = [
    ("the calibration read, the independence check and both columns", 'tools/b315_run.py'),
    ("the kernel-coverage gate's two counts", 'tools/b315_coverage_gate.py'),
    ("the owner instrument the columns run through", 'tools/e16/b38_act10.py'),
    ("the archimedean term's own file", 'tools/e16/carto_atlas.py'),
    ("the ladder's evaluator and its NG law", 'tools/e16/b264_eps_decay.py'),
    ("b313's flipped copies, read and never written", 'tools/e16/b313f_b38_act10.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b315_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b315_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b315_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b315_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b315' in x)


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b315 -- GATE SUITE (A READ AND A RE-DERIVATION)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (pulled from emitting files):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)
    print('    ### **THE FIRST FIVE ARE `G-NOREVERDICT` AND THE NEXT THREE ARE `G-NOLICENCE`:')
    print('    ### the sentences an act that overstated a correction would have written. ###')
    print('    ### **REMOVING A WRONG REASON FOR REFUSING TO READ A COLUMN IS NOT A REASON TO')
    print('    ### ### READ IT.**')

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()
    cov = io.open(COV, encoding='utf-8').read()

    print('\n  G-COVERAGE (the gate was written, RUN, and FAILED, with nothing repaired):')
    ran = 'GATE FAILS' in cov and 'NOT IMPORTED : 24' in cov and 'NOT IN THE PROFILE            : 91' in cov
    fx = "THE GATE'S OWN FIXTURES" in cov and 'PASS' in cov
    print('    gate ran and failed with both counts : %s ; its own fixtures ran : %s' % (ran, fx))
    if not (ran and fx):
        fails.append('G-COVERAGE')

    print('\n  G-NOEDIT (the owner instruments byte-identical to git HEAD, checked AFTER the run):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    if dirty:
        fails.append('G-NOEDIT')

    print('\n  G-CONVERGED (rates read on cells passing b264\'s OWN two-axis test):')
    twoaxis = ("TWO-AXIS TEST" in run and 'first cell that FAILS the two-axis test' in run
               and 'CONV_BAR' in run)
    print('    the two-axis test is in the path and its stopping point is printed : %s' % twoaxis)
    if not twoaxis:
        fails.append('G-CONVERGED')

    print('\n  G-NOFIT (no constant read off pre-asymptotic cells):')
    nofit = ('NOT IN THE ASYMPTOTIC REGIME' in bank
             and 'CONFIRMS THE DIRECTION AND NOT THE' in run)
    print('    the bench is reported as checking direction, not constant : %s' % nofit)
    if not nofit:
        fails.append('G-NOFIT')

    print('\n  G-NOLEAN / G-NOPAPERS / G-ANCESTOR:')
    l1 = subprocess.run(['git', '-C', ROOT, 'status', '--short', '--', '*.lean'],
                        capture_output=True, text=True).stdout.strip()
    l2 = subprocess.run(['git', '-C', SIDE, 'status', '--short', '--', '*.lean'],
                        capture_output=True, text=True).stdout.strip()
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    pfx = now.startswith(head.rstrip('\n'))
    print('    `.lean` changed -- relay : %r ; SIDE : %r' % (l1, l2))
    print('    PLACE-papers tracked changes : %d ; table is a TRUE PREFIX : %s'
          % (len(tracked), pfx))
    if l1 or l2:
        fails.append('G-NOLEAN')
    if tracked:
        fails.append('G-NOPAPERS')
    if not pfx:
        fails.append('G-ANCESTOR')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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
            for h in sh:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-30s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an '
                              'achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        if ferry_scan.scan_text(text, struck, stem_list)[0]:
            fired_disc += 1
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s'
          % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-SEAL:')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    print('    seal intact : %s  %s' % (intact, 'PASS' if intact else '### FAIL ###'))
    if not intact:
        fails.append('G-SEAL')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        for x in gh:
            print('        FLAGGED: %s' % str(x)[:96])
        if gh:
            fails.append('graded hedges in %s' % lbl)

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 10
    print('\n' + '=' * 100)
    print('### COUNTS, PRINTED BY THIS TOOL SO THE BANK NEVER TYPES ONE AT A SHELL:')
    print('    owner needles %d   self needles %d   must-fail fixtures %d'
          % (len(OWNER_NEEDLES), len(SELF_NEEDLES), len(MUST_FAIL)))
    print('    declared carriers %d   toolnum rows %d' % (len(CARRIERS), len(TOOLNUM)))
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
