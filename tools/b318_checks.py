# -*- coding: utf-8 -*-
"""b318_checks.py -- THE GATE SUITE FOR A COMPUTATION AND A DEFINITIONAL DECISION.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### **`G-NOSUB`** ### -- ### **THE ONE THE WHOLE ACT RESTS ON.** ### The square's
###     nonnegativity is worth stating only because it is a SUM OF SQUARES. ### A version that formed
###     it as a difference of two norms would be arithmetically equal and evidentially worthless.
###     ### The gate reads `square_trace`'s own body, STRIPPED of prose, and refuses a subtraction.
###   ### **`G-NOWEIL`** ### -- b317 computed one side of the source's inequality. ### **THIS ACT
###     ### COMPUTES NEITHER**, and the gate reads the emitting files rather than the bank's promise.
###   ### **`G-NOBUILD318`** ### -- the rank-stable scheme is SPECIFIED and NOT BUILT.
###   ### **`G-NOREVERDICT`** ### -- ### **THE ONE THIS ACT COULD MOST EASILY HAVE BREACHED.** ### It
###     found that b317's object is not the source's. ### The bank must RE-LABEL and must not
###     re-verdict, and the must-fail fixtures are the sentences a seat enjoying that would have
###     written.
###   ### **`G-SCANDIRECTION`** ### -- the class scan proves the NEGATIVE only. ### An act that used
###     a nonnegative scan as proof of positive-definiteness would be trusting a finite interval.
###   ### **`G-NOUNIT`** ### -- carried from b317, over STRIPPED code, which is b317's own lesson.
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
import b317_checks as K7  # noqa: E402  ### the stripper, IMPORTED not copied

D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS = ['tools/e16/carto_atlas.py', 'tools/e16/qeps_layer.py', 'tools/e16/b205_prolate.py',
          'tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/noise_floor.py',
          'tools/b305_source.py', 'tools/b317_extract.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def e(n):
    return os.path.join(E16, n)


BANK = d('b318_the_forced_sign.txt')
REG = d('b318_registration_2026-09-04.txt')
RUN = d('b318_components_run.txt')
COV = d('b318_coverage_gate.txt')
SCAN = d('b318_ferry_scan.txt')
FERRY = d('b318_ferry_2026-09-04.txt')
CENSUS = d('b318_census.txt')
EXTRACT = d('b318_extract_notes.txt')

OWNED = [RUN, COV, CENSUS, EXTRACT, d('b318_corr_row.txt'), d('b318_index_query.txt'),
         d('b318_index_run.txt'), d('b318_pins_stepzero.txt'), d('b318_regspec_run.txt'),
         d('b318_reg_termscan.txt'), d('b318_satisfiable.json'), d('b318_satisfiable_run.txt'),
         d('b318_rows.json'),
         t('b318_regspec.py'), t('b318_correspondence.py'), t('b318_run.py'),
         t('b318_square.py'), t('b318_extract.py')]

CARRIERS = [
    (t('b318_checks.py'), 'its own fixtures'),
    (t('b318_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

# ### **THE OWNER NEEDLES ARE PULLED FROM THE EXTRACT FILE FOR THE SOURCE**, which is what the order
# ### says: the read happened once, under its own pin, and the PDF is not re-opened by the gate.
OWNER_NEEDLES = [
    ("the source's square form, from the extract", EXTRACT, 'when evaluated on f'),
    ("### and that it is the trace of a positive operator", EXTRACT, 'of a positive operator'),
    ("Definition 3.1, the class test, from the extract", EXTRACT, 'is pointwise positive'),
    ("Theorem 1's interval on g, from the extract", EXTRACT, 'have support in the interval'),
    ("### the source's own counterexample", EXTRACT, 'but for which'),
    ("### the autocorrelation form in the introduction", EXTRACT, 'gpxyqgpyqdy'),
    ("the eigenvalue-one characterization the scheme is specified from", EXTRACT,
     'is the eigenspace of'),
    ("b317 -- the act this one judges, in its own words",
     d('b317_the_trace_on_the_object.txt'), 'A NUMBER THAT LANDS WHERE A BROKEN CHAIN'),
    ("b316 -- the limit this act may not cross",
     d('b316_the_archimedean_instrument.txt'), 'NOT YET CERTIFIED FOR MEMBERSHIP QUESTIONS'),
    ("the variant this act judges, in its emitting file", t('b317_smear.py'),
     'def mean_zero_variant'),
    ("### and the smear column, recomputed by importing it", t('b317_smear.py'),
     'def compressed_trace'),
    ("the projector whose rank is printed beside every number", t('b316_instrument.py'),
     'def subspace'),
    ("the corpus's bump, in its emitting file", e('carto_atlas.py'), 'def bump'),
    ("the floor/drift gate, in its own file", t('noise_floor.py'), 'def gate'),
    ("b285's boundary, verbatim", d('b285_archimedean_opening.txt'),
     'THE WORD SURVIVES; THE OBJECT DOES NOT'),
    ("b308's law, in b308's own words", d('b308_the_local_field_instrument.txt'),
     'A CONTROL THAT CANNOT FIRE READS EXACTLY LIKE A CONTROL THAT PASSED'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('bank gives the square verdict', BANK, 'THE SQUARE IS NONNEGATIVE AT EVERY CELL'),
    ('### bank names the constituent and says it is proved', BANK,
     'THE FIRST DIFFERING CONSTITUENT IS NAMED AND PROVED'),
    ('### and names it as the second application', BANK, 'APPLICATION OF THE SCALING OPERATOR'),
    ('bank gives the class verdict', BANK, 'NOT POSITIVE DEFINITE AT ANY CELL'),
    ('### bank says the sign change violates nothing', BANK,
     'THE SIGN CHANGE IS NOT A VIOLATION OF ANYTHING'),
    ('### bank states the letter', BANK, 'A CANDIDATE `g`'),
    ('bank reports the reach and its cause', BANK, 'THE REACH IS EMPTY AND THE RANK IS WHY'),
    ('bank carries the no-subtraction fact', BANK, 'PERFORMS NO SUBTRACTION ANYWHERE'),
    ('bank says which statement is finite-decidable', BANK,
     'ONE THING IN THIS ACT IS FINITE-DECIDABLE AND IT IS SAID WHICH'),
    ('### bank keeps the re-labelling apart from a re-verdict', BANK,
     'A re-labelling is not a re-verdict'),
    ('bank files the rank order', BANK, 'W-ORD-RANK-STABLE-SUBSPACE'),
    ('bank updates the window-class order', BANK, 'W-ORD-WINDOW-CLASS'),
    ('bank carries the membership order forward', BANK, 'W-ORD-ARCH-MEMBERSHIP'),
    ('bank owns the imported finder', BANK, "IMPORTS b317's FINDER RATHER THAN COPYING IT"),
    ('bank declares its deviations', BANK, 'DEVIATIONS, DECLARED.'),
    ('bank lists what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK.'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank marks the archimedean leg', BANK, 'DERIVED-NOT-CONFIRMED'),
    ('bank keeps M-2 unchanged under its cap', BANK, "UNDER b310's CAP"),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK'),
    ('bank reports the census with its scope', BANK, 'TOTAL MISSING : 0'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('bank names the membership act as next', BANK, 'THE MEMBERSHIP ACT, NAMED AS NEXT.'),
    ('### bank says the scheme is not built', BANK, 'SPECIFIED AND NOT BUILT'),
    ('bank says no unit is used', BANK, 'NO UNIT IS USED ANYWHERE IN THIS ACT'),
    ('bank quantifies the rank effect', BANK, 'TWO ORDERS OF MAGNITUDE'),
    ('registration names the act', REG, 'THE FORCED SIGN'),
    ('registration seals before any value', REG, 'SEALED BEFORE ANY VALUE AT ANY BANKED CELL'),
    ('### registration records that no probe preceded it', REG,
     'NO FEASIBILITY PROBE PRECEDED THIS SEAL'),
    ('registration carries the expectation', REG, 'THE NAVIGATOR'),
    ('### registration forbids re-verdicting b317', REG, 'IT MAY NOT RE-VERDICT b317'),
    ('registration caps the subtraction', REG, 'NO SUBTRACTION IS PERFORMED ANYWHERE'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives the class count', RUN, 'POSITIVE DEFINITE IN DEFINITION 3.1 SENSE'),
    ('the run reports the square never negative', RUN,
     'CELLS AT WHICH THE SQUARE IS NEGATIVE ANYWHERE : 0'),
    ('### the run reports the smear negative at five', RUN,
     'CELLS AT WHICH THE SMEAR IS NEGATIVE ANYWHERE  : 5'),
    ('the run reports the reach', RUN, 'CELLS INSIDE THE REACH : 0 OF 6'),
    ('### the run reports the noise gate refusing', RUN, 'REFUSED -- 6 of 12'),
    ('the run decides the nonnegativity', RUN, 'nonnegative : True'),
    ('the run reports the identity holding', RUN, 'THE TWO ARE THE SAME OBJECT'),
    ('the run selects the form branch', RUN, '(iii) the variant fails the form condition'),
    ('the extract reports nothing missing', EXTRACT, 'SOURCE FRAGMENTS NOT FOUND : 0'),
    ('the coverage log reports the failure', COV, 'GATE FAILS'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### **`G-NOREVERDICT` -- the sentences a seat enjoying this result would have written.**
    ('b317 is not re-verdicted', BANK, 'b317 IS RE-VERDICTED.'),
    ('b317 is not called wrong', BANK, 'b317 IS WRONG.'),
    ('b317 numbers are not called wrong', BANK, "b317's NUMBERS ARE WRONG."),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('the corpus values are not called wrong', BANK, 'THE CORPUS VALUES ARE WRONG.'),
    # ### **`G-SCANDIRECTION` -- a finite scan does not prove the positive.**
    ('nothing is called positive definite', BANK, 'THE VARIANT IS POSITIVE DEFINITE.'),
    ('the bump is not called positive definite', BANK, 'THE BUMP IS POSITIVE DEFINITE.'),
    # ### **`G-NOWEIL` -- neither side of the inequality.**
    ('the inequality is not evaluated', BANK, 'THE INEQUALITY IS EVALUATED.'),
    ('positivity is not verified', BANK, 'WEIL POSITIVITY IS VERIFIED.'),
    ("the source's theorem is not called confirmed", BANK, "THE SOURCE'S THEOREM IS CONFIRMED."),
    # ### **`G-NOBUILD318` -- the scheme is specified, not built.**
    ('the scheme is not built', BANK, 'THE RANK-STABLE SCHEME IS BUILT.'),
    ('no subspace is rebuilt', BANK, 'THE SUBSPACE IS REBUILT.'),
    # ### **`G-NOUNIT` / membership.**
    ('no unit is placed in the space', BANK, 'THE UNIT IS IN THE SPACE.'),
    ('membership is not decided', BANK, 'THE MEMBERSHIP IS DECIDED.'),
    # ### **CONVERGENCE.**
    ('the number is not called converged', BANK, 'THE NUMBER HAS CONVERGED.'),
    ('the reach is not called non-empty', BANK, 'THE REACH IS NON-EMPTY.'),
    # ### **THE STANDING CAPS.**
    ('nothing is repaired in the kernel', BANK, 'THE MODULES ARE ADDED.'),
    ('no instrument is edited', BANK, 'THE OWNER INSTRUMENT IS EDITED.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('nothing about the identity', BANK, 'THE IDENTITY IS AFFECTED.'),
    ('nothing about the roster', BANK, 'THE ROSTER IS AFFECTED.'),
    ('no p-adic reach is claimed', BANK, 'THE p-ADIC ZERO CARRIES OVER.'),
]

TOOLNUM = [
    ("the square, the class test and the autocorrelation", 'tools/b318_square.py'),
    ("the components, the axes, the reach and the decision", 'tools/b318_run.py'),
    ("the source fragments, located and quoted", 'tools/b318_extract.py'),
    ("### the finder those fragments were located with", 'tools/b317_extract.py'),
    ("the variant, the kernel and the smear column", 'tools/b317_smear.py'),
    ("the space, the projector and the rank", 'tools/b316_instrument.py'),
    ("the corpus's bump", 'tools/e16/carto_atlas.py'),
    ("the floor/drift verdicts", 'tools/noise_floor.py'),
    ("the source pin and the flattener", 'tools/b305_source.py'),
    ("the kernel-coverage gate's two counts", 'tools/b315_coverage_gate.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b318_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b318_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b318_correspondence.py'),
    ("the index key's read-back and must-not-hit arms", 'tools/b318_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b318' in x)

# ### **THE ONLY FLOAT LITERALS THE DECIDING RUNNER MAY CARRY**: a control-frame grid parameter, a
# ### percent for display, and tolerances. ### **EVERY BAR LIVES IN `b318_square.py` AND EVERY FRAME
# ### IN `b317_smear.py`**, and `G-BARSEALED` re-measures them against the sealed registration.
# ### `0.0` and `1.0` are the two points this act's own verdicts are STATED AGAINST -- a sign test
# ### against zero, and "more than one grid point" -- and neither is a finding.
FLOAT_OK = {'0.0', '1.0', '8.0', '100.0', '1e-9', '1e-300'}


def main():
    fails = []
    print('=' * 100)
    print('b318 -- GATE SUITE (A COMPUTATION AND A DEFINITIONAL DECISION)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (the source ones pulled from the EXTRACT FILE, not the PDF):')
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
    sqsrc = io.open(t('b318_square.py'), encoding='utf-8').read()
    src = io.open(t('b318_run.py'), encoding='utf-8').read()
    code = K7.strip_text(src) + K7.strip_text(sqsrc)

    print('\n  G-NOSUB (the square is a SUM OF SQUARES -- read off `square_trace`\'s own body):')
    body = sqsrc.split('def square_trace(')[1].split('\ndef ')[0]
    bodycode = K7.strip_text(body)
    # ### the only `-` the body may contain is the projector's own `K - (K @ Q) @ Q.T`, which is the
    # ### FORMATION of the matrix whose entries are then squared, not a subtraction of two norms.
    accum = re.search(r'acc\s*\+=\s*float\(np\.sum\(R \* R\)\)', bodycode)
    nosub_on_acc = not re.search(r'acc\s*-=|acc\s*=\s*[^;\n]*-\s*float', bodycode)
    said = 'PERFORMS NO SUBTRACTION ANYWHERE' in bank
    print('    the accumulator is a sum of squares : %s ; nothing is subtracted from it : %s'
          % (bool(accum), nosub_on_acc))
    print('    and the act says so : %s' % said)
    print('    ### **THE ONE `-` IN THE BODY IS `K - (K @ Q) @ Q.T`, WHICH FORMS THE MATRIX** whose')
    print('    ### entries are then squared. ### That is the projector, not a difference of norms.')
    if not (accum and nosub_on_acc and said):
        fails.append('G-NOSUB')

    print('\n  G-NOWEIL (neither side of the source\'s inequality is computed):')
    said_w = 'W_infinity` IS NOT COMPUTED' in reg or 'W_infinity` is not computed' in reg
    coded_w = not re.search(r'def .*weil|W_infinity\s*=|def .*w_inf|def .*distribution', code)
    print('    the registration says so : %s ; and no distribution is computed in either tool : %s'
          % (said_w, coded_w))
    if not (said_w and coded_w):
        fails.append('G-NOWEIL')

    print('\n  G-NOBUILD318 (the rank-stable scheme is SPECIFIED and NOT BUILT):')
    said_b = 'SPECIFIED AND NOT BUILT' in bank
    coded_b = not re.search(r'def .*rank_stable|def .*pin_rank|top_r|eigenspace_select', code)
    print('    the act says so : %s ; and no such routine exists in either tool : %s'
          % (said_b, coded_b))
    if not (said_b and coded_b):
        fails.append('G-NOBUILD318')

    print('\n  G-NOREVERDICT (a re-labelling is not a re-verdict):')
    rl = ('A re-labelling is not a re-verdict' in bank
          and 'RE-LABELLED' in bank
          and 'ITS PREDICTION SCORE STANDS AS b317 STATED IT' in bank)
    print('    the bank re-labels and refuses the re-verdict reading : %s' % rl)
    if not rl:
        fails.append('G-NOREVERDICT')

    print('\n  G-SCANDIRECTION (the class scan proves the NEGATIVE only):')
    sd = ('DOES NOT PROVE' in bank and 'DOES NOT PROVE' in run
          and 'this act only ever uses the first direction' in bank.lower()
          or 'only ever uses the first direction' in bank)
    print('    the reach of the scan is stated with its result : %s' % bool(sd))
    if not sd:
        fails.append('G-SCANDIRECTION')

    print('\n  G-NOUNIT (no archimedean unit is constructed -- over STRIPPED code, b317\'s lesson):')
    said_u = 'NO UNIT IS USED ANYWHERE IN THIS ACT' in bank
    coded_u = not re.search(r'sonin_unit|\bMU_SONIN\b|taper\(|asymptotics\(|far_bound\(', code)
    print('    the act says so : %s ; and no unit call appears in either tool : %s'
          % (said_u, coded_u))
    if not (said_u and coded_u):
        fails.append('G-NOUNIT')

    print('\n  G-BARSEALED (the bars the tools use are the bars the SEALED registration carries):')
    import b318_square as SQ
    import b317_smear as SM
    b1 = 'ONE PER CENT, RELATIVE' in reg and abs(SQ.BAR_IDENTITY - 0.01) < 1e-12
    b2 = 'FIVE PER CENT' in reg and abs(SM.BAR_REACH - 0.05) < 1e-12
    b3 = ('[0, 64/L]' in run) and abs(SQ.PD_TMAX_OVER_L - 64.0) < 1e-12
    print('    (B2) one per cent in the seal and BAR_IDENTITY matches : %s' % b1)
    print('    (B3) FIVE PER CENT in the seal and b317\'s BAR_REACH matches : %s' % b2)
    print('    (B1) the scan interval printed by the run matches the tool : %s' % b3)
    if not (b1 and b2 and b3):
        fails.append('G-BARSEALED')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('the class test, both directions (fixtures i and ii)', '(ii)   wide minus narrow' in run),
            ('the identity, both directions (fixtures vi and vii)', '(vii)  the same against' in run),
            ('the arithmetic nonnegativity', 'nonnegative : True' in run),
            ('the identity control at three cells', 'THE TWO ARE THE SAME OBJECT' in run),
            ('the rank guard on resolution of the first row', 'point(s)' in run),
            ('the noise-floor gate -- REPORTED REFUSING', 'REFUSED -- 6 of 12' in run)]
    for lbl, ok_ in arms:
        print('    %-56s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
    if not all(x for _l, x in arms):
        fails.append('G-ARMS')

    print('\n  G-NOFLOAT (no undeclared float literal in the deciding runner):')
    sq_, sl_ = K7.strip_fixture()
    print('    STRIPPER FIXTURE (imported from b317): quiet=%s loud=%s  %s'
          % (sq_, sl_, 'PASS' if (sq_ and sl_) else '### FAIL ###'))
    if not (sq_ and sl_):
        fails.append('G-NOFLOAT (fixture)')
    rcode = K7.strip_text(src)
    lits = set()
    for m in re.finditer(r'(?<![\w.])(\d+\.\d*(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![\w.])', rcode):
        lits.add(m.group(1))
    extra = sorted(x for x in lits if x not in FLOAT_OK)
    print('    float literals in b318_run.py : %d ; UNDECLARED : %d %s'
          % (len(lits), len(extra), extra if extra else ''))
    if extra:
        fails.append('G-NOFLOAT')

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
        tr = K7.git_tracked(ROOT, tool)
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
