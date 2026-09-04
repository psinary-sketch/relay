# -*- coding: utf-8 -*-
"""b317_checks.py -- THE GATE SUITE FOR A COMPUTATION ON A CERTIFIED INSTRUMENT.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### **`G-NOUNIT`** ### -- the order's first line. ### **NO UNIT IS USED ANYWHERE.** ### b316
###     declared the instrument NOT CERTIFIED for membership, and an act that quietly built b300's
###     unit to see where it landed would be using it for exactly that. ### RE-MEASURED against the
###     emitting files rather than against the bank's promise.
###   ### **`G-NOTCONFIRMED`** ### -- ### **THE ONE THIS ACT COULD MOST EASILY HAVE BREACHED.** ###
###     The registered prediction's number landed. ### A link it rests on is measured FALSE. ### The
###     bank must say SCORED and must not say CONFIRMED, and the must-fail fixture is the sentence a
###     seat that had enjoyed its own result would have written.
###   ### **`G-NOTCONVERGED`** ### -- the reach is EMPTY and the noise-floor gate REFUSES 8 of 12.
###     ### **A NUMBER THAT IS NOT CONVERGED MAY NOT BE REPORTED AS ONE**, and the band statement is
###     the only form the scoring is allowed to take.
###   ### **`G-BANDFULL`** ### -- the band must run over the WHOLE registered domain sweep. ### A
###     first draft banded over three frames of five, which is cheaper and is not what the seal says.
###   ### **`G-BARSEALED`** ### -- ### **THE BARS THE TOOL USES MUST BE THE BARS THE SEAL CARRIES.**
###     ### A bar that lived only in the runner could be moved after the fact without leaving a mark.
###   ### **`G-ONESIDE`** ### -- the mean-zero column is ONE side of the source's inequality. ### The
###     other side is not computed in any direction.
###   ### **`G-RANKGUARD`** ### -- b316's own defect species as a cap: a saturated constraint set.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_smear as SM  # noqa: E402

D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS = ['tools/e16/carto_atlas.py', 'tools/e16/qeps_layer.py', 'tools/e16/b205_prolate.py',
          'tools/b316_instrument.py', 'tools/noise_floor.py', 'tools/b305_source.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def e(n):
    return os.path.join(E16, n)


BANK = d('b317_the_trace_on_the_object.txt')
REG = d('b317_registration_2026-09-04.txt')
RUN = d('b317_components_run.txt')
COV = d('b317_coverage_gate.txt')
SCAN = d('b317_ferry_scan.txt')
FERRY = d('b317_ferry_2026-09-04.txt')
CENSUS = d('b317_census.txt')
EXTRACT = d('b317_extract_notes.txt')

OWNED = [RUN, COV, CENSUS, EXTRACT, d('b317_corr_row.txt'), d('b317_index_query.txt'),
         d('b317_index_run.txt'), d('b317_pins_stepzero.txt'), d('b317_regspec_run.txt'),
         d('b317_reg_termscan.txt'), d('b317_satisfiable.json'), d('b317_satisfiable_run.txt'),
         d('b317_rows.json'),
         t('b317_regspec.py'), t('b317_correspondence.py'), t('b317_run.py'),
         t('b317_smear.py'), t('b317_extract.py')]

CARRIERS = [
    (t('b317_checks.py'), 'its own fixtures'),
    (t('b317_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("b316 -- the prediction this act scores", d('b316_the_archimedean_instrument.txt'),
     'THE NAVIGATOR'),
    ("### b316 -- the limit this act may not cross",
     d('b316_the_archimedean_instrument.txt'), 'NOT YET CERTIFIED FOR MEMBERSHIP QUESTIONS'),
    ("### b316 -- what it named for act two and did not compute",
     d('b316_the_archimedean_instrument.txt'), 'NAMED, AND NOT COMPUTED'),
    ("### b316 -- the fact the prediction rests on, promoted to nothing",
     d('b316_the_archimedean_instrument.txt'), 'PROMOTED TO NOTHING'),
    ("b285's boundary, verbatim", d('b285_archimedean_opening.txt'),
     'THE WORD SURVIVES; THE OBJECT DOES NOT'),
    ("b308's law, in b308's own words", d('b308_the_local_field_instrument.txt'),
     'A CONTROL THAT CANNOT FIRE READS EXACTLY LIKE A CONTROL THAT PASSED'),
    ("b309 -- the trace is not defined until an ambient is named",
     d('b309_the_scaling_trace.txt'), 'AMBIENT IS NAMED'),
    ("b300 -- the unit this act does NOT use", d('b300_the_archimedean_leg.txt'),
     'THE CHOSEN UNIT'),
    ("the corpus's own bump, in its emitting file", e('carto_atlas.py'), 'def bump'),
    ("### and the channel its archimedean number comes from", e('carto_atlas.py'),
     'def channels'),
    ("the projector this act compresses with, in b316's file", t('b316_instrument.py'),
     'def subspace'),
    ("### and the scaling action it integrates", t('b316_instrument.py'), 'def scaling'),
    ("the floor/drift gate, in its own file", t('noise_floor.py'), 'def gate'),
    ("the normalisation this act's extract tool should have carried from the start",
     t('b305_source.py'), 'NFKD'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('bank says the number exists', BANK, 'THE NUMBER EXISTS'),
    ('bank gives the score', BANK, 'SCORES AS SMALL AT THIRTEEN CELLS OF THIRTEEN'),
    ('### bank refuses the confirmation', BANK, 'AND THE PREDICTION IS NOT CONFIRMED'),
    ('### bank says the fifth link is false', BANK, 'MEASURED FALSE'),
    ('bank attributes the cancellation to the bump', BANK, 'THE CANCELLATION IS THE BUMP'),
    ('### bank reports the reach as empty', BANK, 'THE REACH IS EMPTY'),
    ('### bank reports the gate refusing', BANK, 'REFUSES EIGHT PAIRS OF TWELVE'),
    ('bank owns the ligature defect', BANK, 'A LIGATURE MISS LOOKS EXACTLY LIKE AN ABSENT'),
    ('### bank says the corpus already owned the fix', BANK, 'THE CORPUS ALREADY OWNED THE FIX'),
    ('bank carries the route control both ways', BANK, 'A ROUTE AGREEMENT THAT CANNOT FAIL'),
    ('bank marks the one exact fact', BANK, 'THE ONE EXACT FACT IN THIS ACT'),
    ('bank quotes the sign chain', BANK, 'THE SIGN CHAIN, QUOTED FROM THE ACTS'),
    ('bank refuses the re-verdict reading', BANK, 'NAMING TWO QUANTITIES DIFFERENT'),
    ('bank refuses to state the inequality', BANK, 'ONE SIDE OF AN INEQUALITY IS NOT THE'),
    ('bank files the window-class order', BANK, 'W-ORD-WINDOW-CLASS'),
    ('bank carries the membership order forward', BANK, 'W-ORD-ARCH-MEMBERSHIP'),
    ('bank declares its deviations', BANK, 'DEVIATIONS, DECLARED.'),
    ('bank lists what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK.'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank marks the archimedean leg', BANK, 'DERIVED-NOT-CONFIRMED'),
    ('bank keeps M-2 unchanged under its cap', BANK, "UNDER b310's CAP"),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK'),
    ('bank reports the census with its scope', BANK, 'TOTAL MISSING : 0'),
    ('bank gives the shadow', BANK, 'EXPECTED NOTHING'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('### bank owns its registration design defect', BANK, 'A DESIGN DEFECT OF THE REGISTRATION'),
    ('bank names the membership act as next', BANK, 'THE MEMBERSHIP ACT, NAMED AS NEXT.'),
    ('### and names it a definitional decision', BANK,
     'A DEFINITIONAL DECISION, NOT A FURTHER MEASUREMENT'),
    ('bank says no unit is used', BANK, 'NO UNIT IS USED ANYWHERE IN THIS'),
    ('bank explains the grid drift as a rank step', BANK, 'A STEP IN THE RANK IS A STEP IN THE'),
    ('registration seals before any value', REG, 'SEALED BEFORE ANY VALUE AT ANY BANKED CELL'),
    ('registration caps the unit', REG, 'NO UNIT IS USED ANYWHERE IN THIS ACT'),
    ('### registration declares the probe that preceded it', REG,
     'THE DEVIATION THAT PRECEDED THE SEAL'),
    ('registration carries the rank guard', REG, 'THE RANK GUARD'),
    ('registration forbids evaluating the inequality', REG, 'IT MAY NOT EVALUATE THE SOURCE'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives the score', RUN, 'CELLS SCORING SMALL : 13 OF 13'),
    ('the run reports the rank guard clean', RUN, '0 CELL(S) REFUSED'),
    ('### the run reports the noise gate refusing', RUN, 'REFUSED -- 8 of 12'),
    ('### the run says the fifth link moved against the prediction', RUN,
     'IT MOVED AGAINST THE PREDICTION'),
    ('the run carries the route arm', RUN, 'A ROUTE AGREEMENT THAT CANNOT FAIL IS NOT A CHECK'),
    ('the run names the under-resolved node', RUN, 'WHICH IS BELOW ONE'),
    ('the run marks the exact fact', RUN, 'EXACT, AND IT IS THE ONE EXACT FACT'),
    ('the extract reports nothing missing', EXTRACT, 'SOURCE FRAGMENTS NOT FOUND : 0'),
    ('the coverage log reports the failure', COV, 'GATE FAILS'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### **`G-NOTCONFIRMED` -- the sentences a seat enjoying its own result would have written.**
    ('the prediction is not called confirmed', BANK, 'THE PREDICTION IS CONFIRMED.'),
    ('the chain is not called intact', BANK, 'THE SIGN CHAIN HOLDS.'),
    ('the cancellation is not given a home', BANK, 'THE CANCELLATION HAS A HOME.'),
    # ### **`G-NOTCONVERGED`.**
    ('the number is not called converged', BANK, 'THE NUMBER HAS CONVERGED.'),
    ('the reach is not called non-empty', BANK, 'THE REACH IS NON-EMPTY.'),
    # ### **`G-NOUNIT` / `G-NOMEMBER`.**
    ('no unit is placed in the space', BANK, 'THE UNIT IS IN THE SPACE.'),
    ('membership is not decided', BANK, 'THE MEMBERSHIP IS DECIDED.'),
    ('the number is not read as b300 s', BANK, 'THE NUMBER IS b300 OBJECT.'),
    # ### **`G-ONESIDE`.**
    ('the inequality is not evaluated', BANK, 'THE INEQUALITY IS EVALUATED.'),
    ('positivity is not claimed', BANK, 'WEIL POSITIVITY IS VERIFIED.'),
    # ### **`G-NOREFUTE` -- a measurement about a window is not a verdict on an act.**
    ('b300 is not re-verdicted', BANK, 'b300 IS RE-VERDICTED.'),
    ('the corpus values are not called wrong', BANK, 'THE CORPUS VALUES ARE WRONG.'),
    ('the atlas is not re-verdicted', BANK, 'THE ATLAS IS RE-VERDICTED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    # ### **THE STANDING CAPS.**
    ('nothing is repaired in the kernel', BANK, 'THE MODULES ARE ADDED.'),
    ('no instrument is edited', BANK, 'THE OWNER INSTRUMENT IS EDITED.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('M-2 is not verdicted', BANK, 'M-2 IS UNSATISFIABLE.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('nothing about the identity', BANK, 'THE IDENTITY IS AFFECTED.'),
    ('nothing about the roster', BANK, 'THE ROSTER IS AFFECTED.'),
    ('no p-adic reach is claimed', BANK, 'THE p-ADIC ZERO CARRIES OVER.'),
]

TOOLNUM = [
    ("the trace, the two test functions and the two routes", 'tools/b317_smear.py'),
    ("the components, the axes, the reach and the score", 'tools/b317_run.py'),
    ("the source fragments, located and quoted", 'tools/b317_extract.py'),
    ("the space, the projector and the scaling action", 'tools/b316_instrument.py'),
    ("the corpus's bump and its banked archimedean values", 'tools/e16/carto_atlas.py'),
    ("the floor/drift verdicts", 'tools/noise_floor.py'),
    ("the source pin and the flattener", 'tools/b305_source.py'),
    ("the kernel-coverage gate's two counts", 'tools/b315_coverage_gate.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b317_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b317_correspondence.py'),
    ("the index key's read-back and must-not-hit arms", 'tools/b317_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b317' in x)

# ### **THE ONLY FLOAT LITERALS THE DECIDING RUNNER MAY CARRY**: a control-frame grid parameter, a
# ### percent for display, and tolerances. ### **EVERY BAR AND EVERY FRAME LIVES IN `b317_smear.py`**,
# ### which is where the sealed registration's (4) and (5) are carried, and `G-BARSEALED` re-measures
# ### them against the registration's own text.
FLOAT_OK = {'8.0', '100.0', '1e-1', '1e-4', '1e-9', '1e-300'}


def strip_text(src):
    """### **THE GATE READS CODE, NOT PROSE.** ### Imported in spirit from b316 and re-stated here
    ### because this act's runner is a different file; the FIXTURE below is what makes it worth
    ### having, and it must both remove a numeral in prose and keep one in code."""
    dq, sq = chr(34), chr(39)
    tdq, tsq = dq * 3, sq * 3
    out, i, n = [], 0, len(src)
    while i < n:
        c = src[i]
        if c == '#':
            j = src.find(chr(10), i)
            i = n if j < 0 else j
        elif c == dq or c == sq:
            three = src[i:i + 3]
            q = three if three in (tdq, tsq) else c
            j = src.find(q, i + len(q))
            i = n if j < 0 else j + len(q)
        else:
            out.append(c)
            i += 1
    return ''.join(out)


def strip_fixture():
    nl, dq = chr(10), chr(34)
    prose = 'x = 1  # see Theorem 9.87' + nl + 'print(' + dq + 'v 9.87' + dq + ')'
    quiet = '9.87' not in strip_text(prose)
    loud = '9.87' in strip_text('x = 9.87  # a real one')
    return quiet, loud


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b317 -- GATE SUITE (A COMPUTATION ON A CERTIFIED INSTRUMENT)')
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

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()
    cov = io.open(COV, encoding='utf-8').read()
    reg = io.open(REG, encoding='utf-8').read()
    smear = io.open(t('b317_smear.py'), encoding='utf-8').read()
    src = io.open(t('b317_run.py'), encoding='utf-8').read()

    print('\n  G-NOUNIT (no archimedean unit is constructed -- read off the emitting files):')
    # ### ### **THE CODE IS STRIPPED FIRST, AND THAT IS THIS GATE'S OWN LESSON, LEARNED TWICE.**
    # ### The first version scanned the RAW source and FAILED -- on the runner's own docstring
    # ### sentence saying `INS.sonin_unit` is never called. ### **A GATE THAT FLAGS A SENTENCE
    # ### ### SAYING A THING IS NOT DONE IS MEASURING THE ACT'S WRITING AND NOT ITS ARITHMETIC**,
    # ### which is exactly what `G-NOFLOAT` strips prose to avoid. ### Same stripper, same reason.
    said = 'NO UNIT IS USED ANYWHERE IN THIS' in bank
    unit_code = strip_text(src) + strip_text(smear)
    coded = not re.search(r'sonin_unit|\bMU_SONIN\b|taper\(|asymptotics\(|far_bound\(', unit_code)
    print('    the act says so : %s ; and no unit call appears in either tool : %s' % (said, coded))
    print('    ### **THE SCAN IS OVER STRIPPED CODE.** ### A docstring saying the unit is never')
    print('    ### called is not a call, and the first version of this gate could not tell.')
    if not (said and coded):
        fails.append('G-NOUNIT')

    print('\n  G-NOTCONFIRMED (the number landed; a link it rests on is measured false):')
    scored = 'SCORES AS SMALL AT THIRTEEN CELLS OF THIRTEEN' in bank
    refused = 'AND THE PREDICTION IS NOT CONFIRMED' in bank and 'MEASURED FALSE' in bank
    inrun = 'IT MOVED AGAINST THE PREDICTION' in run
    print('    scored : %s ; refused the confirmation : %s ; the run says which link : %s'
          % (scored, refused, inrun))
    if not (scored and refused and inrun):
        fails.append('G-NOTCONFIRMED')

    print('\n  G-NOTCONVERGED (an empty reach and a refusing gate are reported as such):')
    empty = 'THE REACH IS EMPTY' in bank and 'REFUSES EIGHT PAIRS OF TWELVE' in bank
    band = 'BAND statement' in bank or 'BAND STATEMENT' in bank
    gatefired = 'REFUSED -- 8 of 12' in run
    print('    the reach is empty and said so : %s ; scoring is a band : %s ; gate fired : %s'
          % (empty, band, gatefired))
    if not (empty and band and gatefired):
        fails.append('G-NOTCONVERGED')

    print('\n  G-BANDFULL (the band runs over the WHOLE registered domain sweep):')
    full = tuple(SM.SWEEP_FRAMES) == tuple(SM.DOMAIN_AXIS)
    xs = [f[1] for f in SM.SWEEP_FRAMES]
    print('    SWEEP_FRAMES == DOMAIN_AXIS : %s ; X = %s' % (full, xs))
    print('    ### **A FIRST DRAFT BANDED OVER THREE OF THE FIVE.** ### The seal says *the domain')
    print('    ### sweep*, which is the registered axis in full, and the narrowest cell moves.')
    if not full:
        fails.append('G-BANDFULL')

    print('\n  G-BARSEALED (the bars the tool uses are the bars the SEALED registration carries):')
    b1 = ('|A(a)| / %d' % int(SM.BAR_SMALL)) in reg
    b2 = ('FIVE PER CENT' in reg) and abs(SM.BAR_REACH - 0.05) < 1e-12
    b3 = ('NY = 512' in reg) and SM.NY_FIXED == 512
    print('    (B1) `|A(a)| / %d` present in the seal : %s' % (int(SM.BAR_SMALL), b1))
    print('    (B2) FIVE PER CENT present and BAR_REACH == %.2f : %s' % (SM.BAR_REACH, b2))
    print('    (5)  NY = %d present and NY_FIXED matches : %s' % (SM.NY_FIXED, b3))
    print('    ### **A BAR THAT LIVED ONLY IN THE RUNNER COULD BE MOVED AFTER THE FACT WITHOUT')
    print('    ### ### LEAVING A MARK.** ### These three read the sealed file and the tool together.')
    if not (b1 and b2 and b3):
        fails.append('G-BARSEALED')

    print('\n  G-ONESIDE (the mean-zero column is one side; the other is not computed):')
    oneside = 'ONE SIDE OF AN INEQUALITY IS NOT THE' in bank
    nootherside = not re.search(r'def .*weil|W_infinity\s*=|def .*w_inf', unit_code)
    print('    the act says so : %s ; and no distribution is computed in either tool : %s'
          % (oneside, nootherside))
    if not (oneside and nootherside):
        fails.append('G-ONESIDE')

    print('\n  G-RANKGUARD (b316\'s defect species, capped and re-measured):')
    guard = '0 CELL(S) REFUSED' in run and 'NY/X' in run
    print('    the guard ran at every frame and refused none : %s' % guard)
    if not guard:
        fails.append('G-RANKGUARD')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('the identity control, exact and re-run at every frame',
             'THE ONE EXACT FACT IN THIS ACT' in run),
            ('the two routes, and the halved-kernel arm',
             'A ROUTE AGREEMENT THAT CANNOT FAIL IS NOT A CHECK' in run),
            ('### the route control\'s excluded region, named and sized',
             'WHICH IS BELOW ONE' in run),
            ('the class test, in both directions',
             'THE CORPUS BUMP IS NOT IN THE SOURCE eq. (54) CLASS AND THE VARIANT IS' in run),
            ('the rank guard', '0 CELL(S) REFUSED' in run),
            ('the noise-floor gate -- REPORTED REFUSING', 'REFUSED -- 8 of 12' in run)]
    for lbl, ok_ in arms:
        print('    %-56s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
    if not all(x for _l, x in arms):
        fails.append('G-ARMS')

    print('\n  G-NOFLOAT (no undeclared float literal in the deciding runner):')
    sq, sl = strip_fixture()
    print('    STRIPPER FIXTURE: quiet on a numeral in prose : %s ; loud on one in code : %s  %s'
          % (sq, sl, 'PASS' if (sq and sl) else '### FAIL ###'))
    if not (sq and sl):
        fails.append('G-NOFLOAT (fixture)')
    code = strip_text(src)
    lits = set()
    for m in re.finditer(r'(?<![\w.])(\d+\.\d*(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![\w.])', code):
        lits.add(m.group(1))
    extra = sorted(x for x in lits if x not in FLOAT_OK)
    print('    float literals in b317_run.py : %d ; UNDECLARED : %d %s'
          % (len(lits), len(extra), extra if extra else ''))
    if extra:
        fails.append('G-NOFLOAT')
    print('    ### **THE DECLARED ONES ARE A CONTROL-FRAME PARAMETER, A PERCENT FOR DISPLAY, AND')
    print('    ### ### TOLERANCES.** ### Every bar and every frame lives in the tool, checked above.')

    print('\n  G-NOEDIT (the owner instruments byte-identical to git HEAD, checked AFTER the run):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    if dirty:
        fails.append('G-NOEDIT')

    print('\n  G-COVERAGE (the kernel gate re-run and still failing, with nothing repaired):')
    ran = ('GATE FAILS' in cov and 'NOT IMPORTED : 24' in cov)
    print('    gate ran and failed with its counts : %s' % ran)
    if not ran:
        fails.append('G-COVERAGE')

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
        for s in gh:
            print('      ### GRADED HEDGE: %s' % s[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print('\n' + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d' % unpullable)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
