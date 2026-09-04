# -*- coding: utf-8 -*-
"""b316_checks.py -- THE GATE SUITE FOR AN INSTRUMENT BUILD.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### **`G-NOTRACE`** ### -- the order's central constraint. ### **NO TRACE IS COMPUTED AND NO
###     ### SMEAR IS ASSEMBLED**, and the must-fail fixtures are the sentences act two's number
###     would have produced. ### An instrument that works tempts its builder to point it.
###   ### **`G-NOTACHECK`** ### -- ### **THE ONE THIS ACT NEARLY BREACHED.** ### b308's law: a
###     control that cannot fire reads as a pass. ### The asymptotic control on the derived unit
###     cannot discriminate an eigenvalue from a non-eigenvalue, and the bank must SAY SO.
###   ### **`G-NOREFUTE`** ### -- an unconfirmed reproduction is not a refutation. ### **b300 IS NOT
###     ### RE-VERDICTED AND IS NOT CALLED WRONG**, and the fixtures are the sentences that would
###     have said otherwise.
###   ### **`G-NOFLOAT`** ### -- no float literal decides anything in the runner. ### Grid
###     parameters and tolerances are declared; findings come out of the instrument.
###   ### **`G-ARMS`** ### -- every discrimination arm in this act is shown ABLE to fire, or is
###     reported as unable. ### **THE INSTRUMENT'S FIRST DEFECT WAS CAUGHT BY AN ARM AND NOT BY
###     ### INSPECTION**, which is the whole argument for carrying them.
"""
import io
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

D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS = ['tools/e16/qeps_layer.py', 'tools/e16/b38_act10.py',
          'tools/e16/b264_eps_decay.py', 'tools/e16/carto_atlas.py',
          'tools/e16/b205_prolate.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def e(n):
    return os.path.join(E16, n)


BANK = d('b316_the_archimedean_instrument.txt')
REG = d('b316_registration_2026-09-04.txt')
RUN = d('b316_components_run.txt')
COV = d('b316_coverage_gate.txt')
SCAN = d('b316_ferry_scan.txt')
FERRY = d('b316_ferry_2026-09-03.txt')
CENSUS = d('b316_census.txt')

OWNED = [RUN, COV, CENSUS, d('b316_corr_row.txt'), d('b316_index_query.txt'),
         d('b316_index_run.txt'), d('b316_pins_stepzero.txt'), d('b316_regspec_run.txt'),
         d('b316_reg_termscan.txt'), d('b316_satisfiable.json'), d('b316_rows.json'),
         t('b316_regspec.py'), t('b316_correspondence.py'), t('b316_run.py'),
         t('b316_instrument.py')]

CARRIERS = [
    (t('b316_checks.py'), 'its own fixtures'),
    (t('b316_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("b292 -- the finding this instrument re-measures", d('b292_the_identification.txt'),
     'IS NOT IN `S(1,1)`'),
    ("### b292 -- and the route it took, which is NOT this one",
     d('b292_the_identification.txt'), "fails Sonin's second condition"),
    ("b300 -- the unit whose membership did not reproduce", d('b300_the_archimedean_leg.txt'),
     'THE CHOSEN UNIT'),
    ("### b300 -- its own sentence keeping the two vectors apart",
     d('b300_the_archimedean_leg.txt'), 'b292 CLAIMED NOTHING ABOUT'),
    ("### b300 -- eq. (16), which discharges the norm ruling",
     d('b300_the_archimedean_leg.txt'), 'EQUATION (16), THE'),
    ("b308's law, in b308's own words", d('b308_the_local_field_instrument.txt'),
     'A CONTROL THAT CANNOT FIRE READS EXACTLY LIKE A CONTROL THAT PASSED'),
    ("b309 -- the trace is not defined until an ambient is named",
     d('b309_the_scaling_trace.txt'), 'AMBIENT IS NAMED'),
    ("b285's boundary, verbatim", d('b285_archimedean_opening.txt'),
     'THE WORD SURVIVES; THE OBJECT DOES NOT'),
    ("b15's law, as b261 carries it", d('b261_e2even_monotone.txt'),
     'AT A FINITE CUTOFF DECIDES NOTHING GLOBAL'),
    ("the solver this act used and did not write", e('b205_prolate.py'), 'def yI_eval'),
    ("### and its marcher", e('b205_prolate.py'), 'def integrate_in'),
    ("the layer the discrimination vector comes from", e('qeps_layer.py'), 'def layer'),
    ("b313 -- the exponent this instrument uses", d('b313_the_exponent.txt'),
     "THE SOURCE'S EXPONENT"),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST'),
    ('bank says the instrument exists', BANK, 'THE INSTRUMENT EXISTS'),
    ('bank gives the sharpened sentence', BANK, 'WHICH CONDITION BREAKS'),
    ('bank confirms b292 by a second route', BANK, 'SECOND AND INDEPENDENT ROUTE'),
    ('### bank gives the UNCONFIRMED verdict', BANK, 'IS NOT CONFIRMED'),
    ('### bank calls it the hard result and negative', BANK, 'A NEGATIVE ONE'),
    ('bank reports the refuted explanation', BANK, 'TESTED AND REFUSED'),
    ('bank reports the control as not-a-check', BANK, 'REPORTED AS NOT-A-CHECK'),
    ('bank names the three causes', BANK, 'THIS ACT CHOOSES NONE'),
    ('bank declares the instrument uncertified for membership', BANK,
     'NOT YET CERTIFIED FOR MEMBERSHIP QUESTIONS'),
    ('bank files the membership order', BANK, 'W-ORD-ARCH-MEMBERSHIP'),
    ('bank refuses to re-verdict b300', BANK, 'b300 IS NOT RE-VERDICTED'),
    ('bank carries b15 law', BANK, 'DECIDES NOTHING GLOBAL'),
    ('bank gives the four normalizations', BANK, 'THE FOUR NORMALIZATIONS'),
    ('bank discharges the norm ruling by the source', BANK,
     'IS DISCHARGED, AND BY THE SOURCE'),
    ('bank bounds the discharge to the additive arm', BANK, 'THE ADDITIVE ARM ONLY'),
    ('bank gives the sign chain', BANK, 'THE SIGN CHAIN, QUOTED'),
    ('bank gives the dimension table', BANK, 'THE DIMENSION GROWS WITHOUT BOUND'),
    ('bank refuses to derive the rank', BANK, 'MEASURES IT AND DOES NOT'),
    ('bank gives the leakage table', BANK, 'LEAVES THE SPACE'),
    ('bank marks the exact facts as exact', BANK, 'BY DISJOINT SUPPORT'),
    ('bank gives the transform control both ways', BANK, 'CANNOT FAIL IS NOT A CHECK'),
    ('bank owns the grid defect', BANK, 'TIED THE TRANSFORM GRID TO THE FUNCTION GRID'),
    ('bank says the arm caught it', BANK, 'NOT BY INSPECTION'),
    ('bank owns the rank-claim defect', BANK, 'THE TABLE WAS RIGHT AND THE SENTENCE WAS WRONG'),
    ('bank declares its deviations', BANK, 'DEVIATIONS, DECLARED'),
    ('bank lists what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank carries the quotation law against itself', BANK,
     'A QUOTATION OF A QUOTATION IS NOT A SOURCE'),
    ('bank lists capabilities and limits', BANK, "THE INSTRUMENT'S CAPABILITIES AND LIMITS"),
    ('bank names act two and does not compute it', BANK, 'NAMED, AND NOT COMPUTED'),
    ('bank restates the object three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank keeps M-2 unchanged under its cap', BANK, "UNDER b310's CAP"),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK'),
    ('bank records the W2 ruling', BANK, 'RECORDED AND UNAPPLIED'),
    ('bank restates the kernel-coverage order', BANK, 'W-ORD-KERNEL-COVERAGE'),
    ('bank restates the absolute-path order', BANK, 'W-ORD-ABSOLUTE-PATHS'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank reports the census with its scope', BANK, 'TOTAL MISSING : 0'),
    ('bank gives the shadow', BANK, 'EXPECTED NOTHING'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('registration splits what it precedes', REG, 'THE COMPONENTS HAVE RUN'),
    ('registration caps the trace', REG, 'NO TRACE IS COMPUTED AND NO'),
    ('registration caps the dead control', REG, 'CANNOT FIRE READS AS A PASS'),
    ('registration records the unconfirmed arm', REG, 'DID NOT CONFIRM'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run reports the unconfirmed reproduction separately', RUN, '### UNCONFIRMED:'),
    ('the run carries the discrimination sweep', RUN, 'THE ARM FIRES'),
    ('the run carries the taper diagnostic', RUN, 'HARD-CUTOFF EXPLANATION WAS TESTED'),
    ('the coverage log reports the failure', COV, 'GATE FAILS'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### ### **`G-NOTRACE` -- the sentences act two's number would have produced.**
    ('no trace is computed', BANK, 'THE COMPRESSED TRACE IS COMPUTED.'),
    ('no smear is assembled', BANK, 'THE SMEARED TRACE IS ASSEMBLED.'),
    ('the prediction is not tested', BANK, 'THE PREDICTION IS CONFIRMED.'),
    ('the prediction is not pre-refuted either', BANK, 'THE PREDICTION IS REFUTED.'),
    # ### **`G-NOREFUTE` -- an unconfirmed reproduction is not a refutation.**
    ('b300 is not re-verdicted', BANK, 'b300 IS RE-VERDICTED.'),
    ('b300 is not called wrong', BANK, 'b300 IS WRONG.'),
    ('the unit is not declared outside the space', BANK, 'u_inf IS NOT IN THE SPACE.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('b292 is not re-verdicted', BANK, 'b292 IS RE-VERDICTED.'),
    # ### **`G-NOTACHECK` -- the sentence a dead control would have been reported as.**
    ('the asymptotic control is not called a pass', BANK, 'THE ASYMPTOTIC CONTROL PASSES.'),
    ('the construction is not certified', BANK, 'THE CONSTRUCTION IS CERTIFIED.'),
    # ### **THE INSTRUMENT'S OWN LIMITS.**
    ('membership is not decided', BANK, 'THE MEMBERSHIP IS DECIDED.'),
    ('the truncation is not called the space', BANK, 'THE TRUNCATION IS THE SPACE.'),
    ('no p-adic reach is claimed', BANK, 'THE p-ADIC ZERO CARRIES OVER.'),
    # ### **THE STANDING CAPS.**
    ('nothing is repaired in the kernel', BANK, 'THE MODULES ARE ADDED.'),
    ('no instrument is edited', BANK, 'THE OWNER INSTRUMENT IS EDITED.'),
    ('M-2 is not verdicted', BANK, 'M-2 IS UNSATISFIABLE.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]

TOOLNUM = [
    ("the space, the operators and every measurement on them", 'tools/b316_instrument.py'),
    ("the components, the sweeps and the two diagnostics", 'tools/b316_run.py'),
    ("the kernel-coverage gate's two counts", 'tools/b315_coverage_gate.py'),
    ("the solver the archimedean unit comes from", 'tools/e16/b205_prolate.py'),
    ("the layer the discrimination vector comes from", 'tools/e16/qeps_layer.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b316_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b316_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b316_correspondence.py'),
    ("the index key's read-back and must-not-hit arms", 'tools/b316_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b316' in x)

# ### **THE ONLY FLOAT LITERALS A DECIDING RUNNER MAY CARRY**: grid parameters, dilations and
# ### tolerances, which are DECLARED and are not findings. ### Everything else must come out of the
# ### instrument. ### **THIS LIST IS THE DECLARATION, AND THE GATE READS THE SOURCE AGAINST IT.**
FLOAT_OK = {'0.5', '1.0', '1.25', '1.5', '2.0', '3.0', '4.0', '8.0', '16.0', '32.0', '48.0',
            '64.0', '96.0', '0.7', '0.01', '1e-8', '1e-3', '1e-9', '1e-12', '1e-300', '2.5', '0.0', '1.1'}


def strip_text(src):
    """### **THE GATE READS CODE, NOT PROSE.** ### A numeral inside a docstring, a printed sentence
    ### or a format specifier decides nothing -- `Definition 4.4` and a width in `%.4f` are not
    ### findings, and a gate that flagged them would be measuring the act's writing rather than its
    ### arithmetic. ### **SO STRINGS AND COMMENTS ARE REMOVED BEFORE THE SCAN**, and what remains is
    ### what runs. ### **AND `strip_fixture` SHOWS IT STILL CATCHES A LITERAL IN CODE**, which is
    ### the only thing that makes this gate worth having."""
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
    """### **BOTH ARMS.** ### It must remove a numeral in prose AND keep one in code."""
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
    print('b316 -- GATE SUITE (AN INSTRUMENT BUILD)')
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
    print('    ### **THE FIRST FOUR ARE `G-NOTRACE`, THE NEXT FIVE `G-NOREFUTE`, THE NEXT TWO')
    print('    ### ### `G-NOTACHECK`:** ### the sentences an act that overstated an instrument, or')
    print('    ### a negative reproduction, or a dead control, would have written.')

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()
    cov = io.open(COV, encoding='utf-8').read()

    print('\n  G-NOTRACE (no trace computed, no smear assembled -- read off the emitting files):')
    src = io.open(t('b316_run.py'), encoding='utf-8').read()
    ins = io.open(t('b316_instrument.py'), encoding='utf-8').read()
    said = ('NO TRACE IS COMPUTED AND NO SMEAR IS ASSEMBLED' in bank
            and 'NO TRACE IS COMPUTED AND NO SMEAR IS ASSEMBLED' in run)
    coded = not re.search(r'\bnp\.trace\b|\bdef .*trace|\.trace\(', src + ins)
    print('    the act says so : %s ; and no trace is taken anywhere in the two tools : %s'
          % (said, coded))
    if not (said and coded):
        fails.append('G-NOTRACE')

    print('\n  G-NOTACHECK (b308\'s law: a control that cannot fire is reported as not-a-check):')
    dead = ('REPORTED AS NOT-A-CHECK' in bank and 'REPORTED AS NOT-A-CHECK' in run
            and 'Indistinguishable' in bank)
    named = 'A CONTROL THAT CANNOT FIRE READS AS A PASS' in bank
    print('    the dead control is named and reported as not-a-check : %s ; b308 cited : %s'
          % (dead, named))
    if not (dead and named):
        fails.append('G-NOTACHECK')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('the transform control', 'CANNOT FAIL IS NOT A CHECK' in run),
            ('the membership sweep, via zeta_0', 'THE ARM FIRES' in run),
            ('the taper diagnostic', 'TESTED AND IT FAILED' in run),
            ('the asymptotic control -- REPORTED UNABLE', 'COULD NOT FIRE' in run),
            ('the unitarity fixture, both directions', 'ARMS 3, 5 AND 8' in run)]
    for lbl, ok_ in arms:
        print('    %-46s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
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
    print('    float literals in b316_run.py : %d ; UNDECLARED : %d %s'
          % (len(lits), len(extra), extra if extra else ''))
    if extra:
        fails.append('G-NOFLOAT')
    print('    ### **THE DECLARED ONES ARE GRID PARAMETERS, DILATIONS AND TOLERANCES.** ### None of')
    print('    ### them is a finding, and every finding in this act comes out of the instrument.')

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
