# -*- coding: utf-8 -*-
"""b320_checks.py -- THE GATE SUITE FOR A CONSTRUCTION, A COMPUTATION, AND A CONTROL.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### **`G-NOWIDEN`** ### -- ### **THE ONE THIS ACT COULD MOST EASILY HAVE BREACHED, AND VERY
###     ### NEARLY THE WHOLE POINT OF IT.** ### The control FAILED on the first run. ### The order
###     forbade widening, tuning or re-barring anything to make it pass. ### This arm proves the bar
###     did not move: ### **the sealed registration's hash is unchanged and its seal verifies**, the
###     covered-cell set is still all three of Theorem 1's conditions, the class floor is still
###     `1e-09`, and the bank states at full prominence that the first verdict was `FAILS`.
###   ### **`G-NOWINDOW`** ### -- the ten uncovered cells are computed and printed with no claim.
###     ### The bank must say the theorem does not cover them AND must not contain any sentence
###     reading the inequality's holding there as evidence.
###   ### **`G-NOUNIT`** ### -- ### **NO UNIT IS USED AND NONE IS DEFINED.** ### b319's order forced
###     a call; this act's order forbids one again, so the cap returns to b317's and b318's shape.
###     ### **THE SCAN IS OVER STRIPPED CODE**, because b317's version of this gate fired on the
###     act's own docstring.
###   ### **`G-CORROB`** ### -- ### **A SECOND AND INDEPENDENT ROUTE TO THE LEFT-HAND SIDE.** ### Two
###     defects got past two rounds of fixtures on one route. ### This arm requires the second route
###     to exist, to agree, and ### **TO BE ABLE TO DISAGREE** -- a corroboration that agreed with
###     anything would corroborate nothing.
###   ### **`G-FAILFIRST`** ### -- the record must carry the failing run. ### A bank that reported
###     only the second run would be a true document assembled to give a false impression.
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
import b317_checks as K7  # noqa: E402  ### the stripper and git helper, IMPORTED not copied

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS = ['tools/e16/carto_atlas.py', 'tools/e16/qeps_layer.py', 'tools/e16/b205_prolate.py',
          'tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py',
          'tools/b319_stable.py', 'tools/noise_floor.py', 'tools/b305_source.py',
          'tools/b317_extract.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b320_the_lawful_function.txt')
REG = d('b320_registration_2026-09-04.txt')
RUN = d('b320_components_run.txt')
COR = d('b320_corroboration.txt')
READ = d('b320_b319_read.txt')
SCAN = d('b320_ferry_scan.txt')
FERRY = d('b320_ferry_2026-09-04.txt')
CENSUS = d('b320_census.txt')
EXTRACT = d('b320_extract_notes.txt')

OWNED = [RUN, COR, READ, CENSUS, EXTRACT, d('b320_index_query.txt'),
         d('b320_pins_stepzero.txt'), d('b320_regspec_run.txt'), d('b320_reg_termscan.txt'),
         d('b320_satisfiable.json'), d('b320_satisfiable_run.txt'), d('b320_rows.json'),
         d('b320_corr_run.txt'),
         t('b320_regspec.py'), t('b320_correspondence.py'), t('b320_run.py'),
         t('b320_weil.py'), t('b320_extract.py'), t('b320_b319_read.py'),
         t('b320_corroborate.py')]

CARRIERS = [
    (t('b320_checks.py'), 'its own fixtures'),
    (t('b320_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("Theorem 1's three conditions, from the extract", EXTRACT, 'Theorem 1'),
    ("Definition 3.1, from the extract", EXTRACT, 'positive definite'),
    ("(53), the archimedean functional, from the extract", EXTRACT, 'W_'),
    ("(38), the principal value, from the extract", EXTRACT, 'value, (38) gives the Weil'),
    ("### and (39), the kernel the assembly is checked against", EXTRACT, 'tau'),
    ("b318 -- the square this act takes as its right-hand side", t('b318_square.py'),
     'def square_trace'),
    ("### and the product this act tests for class membership", t('b318_square.py'),
     'def autocorrelation'),
    ("### and the transform the class test reads", t('b318_square.py'), 'def fhat'),
    ("b319 -- the space both sides are computed on", t('b319_stable.py'), 'def stable_subspace'),
    ("b317 -- the seed this act squares", t('b317_smear.py'), 'def mean_zero_variant'),
    ("### and the cells it is squared at", t('b317_smear.py'), 'def atlas_cells'),
    ("the corpus's own digamma kernel, at its emitting file",
     os.path.join(ROOT, 'tools', 'e16', 'carto_atlas.py'), 'def kernel'),
    ("the floor/drift gate", t('noise_floor.py'), 'def gate'),
    ("b318 -- the reading this act settles by measurement", d('b318_the_forced_sign.txt'),
     'A CANDIDATE `g`'),
    ("b319 -- the bar this act corrects", d('b319_the_stable_rank.txt'),
     'THE BAR THIS ACT SEALED IS DEFECTIVE'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('bank gives the class verdict', BANK, 'POSITIVE DEFINITE IN DEFINITION 3.1'),
    ('### bank carries the arm that can fail', BANK, 'A CLASS TEST EVERYTHING PASSES IS NOT ONE'),
    ('bank names the covered cells from the check', BANK, 'THE COVERED CELLS ARE NAMED FROM'),
    ('bank gives the control verdict', BANK, 'VERDICT : HOLDS'),
    ('### bank reports the control at every frame', BANK, '27 OF 27 FRAMES'),
    ('### bank states the FIRST verdict was FAILS', BANK,
     "BUT THIS ACT'S FIRST REPORTED VERDICT WAS `FAILS`"),
    ('### bank states that no bar was moved', BANK, 'NO BAR WAS MOVED'),
    ('### bank names the failing constituent as its own', BANK,
     'MY OWN IMPLEMENTATION OF THE SOURCE'),
    ('### bank states the registration was not re-sealed', BANK,
     'THE REGISTRATION WAS NOT RE-SEALED'),
    ('bank gives the failure-and-repair its own section', BANK, 'THE FAILURE AND THE REPAIR'),
    ('### bank refuses the two-instances-of-one-mistake fixture', BANK,
     'AN AGREEMENT BETWEEN TWO INSTANCES OF THE SAME MISTAKE IS'),
    ('### bank reports the expectation half refuted', BANK, 'HALF RIGHT AND HALF REFUTED'),
    ('### and says which way the margin actually goes', BANK, 'IT GROWS'),
    ('bank reports the reach non-empty', BANK, 'THE REACH IS NON-EMPTY FOR THE FIRST TIME IN THIS'),
    ('### and that the corrected bar was fixed first', BANK, 'BEFORE ANY VALUE WAS'),
    ('### bank reports the noise gate refusing', BANK, '3 OF 6, ALL DOMAIN'),
    ('### bank refuses the size of its own margins', BANK, 'ITS SIZE IS NOT CERTIFIED AT ANY'),
    ('bank refuses the theorem reading', BANK, 'NO THEOREM IS PROVED HERE'),
    ('bank refuses the window', BANK, 'NO WINDOW IS OPENED'),
    ('bank refuses the unit', BANK, 'NO UNIT IS USED, ANYWHERE'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 remains owed under its cap'),
    ('bank reports the corroboration', BANK, 'WORST DIFFERENCE ACROSS ALL THIRTEEN CELLS'),
    ('bank files the defect against b319 without editing it', BANK,
     'ONE PROSE-VS-TABLE DEFECT IS FILED AGAINST b319'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### and says what it does NOT keep', BANK, 'NOT KEPT, AND EXPLICITLY DISCLAIMED'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('### and names the window act', BANK, 'THE WINDOW ACT'),
    ('### and names the fold as still due', BANK, 'AND THE FOLD, FROM b314 ONWARD, IS DUE'),
    ('registration names the act', REG, 'THE LAWFUL FUNCTION AND THE CONTROL'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives the control verdict', RUN, 'VERDICT : HOLDS'),
    ('the run names the covered cells', RUN, 'THE COVERED CELLS, NAMED FROM THE CHECK : 1.3, 1.35'),
    ('the run reports the reach', RUN, 'COVERED CELLS INSIDE THE REACH : 3 OF 3'),
    ('the run reports the noise gate refusing', RUN, 'REFUSED -- 3 of 6'),
    ('### the run refuses the uncovered cells', RUN,
     'THE THEOREM DOES NOT COVER THESE CELLS AND NEITHER DOES THIS ACT'),
    ('the corroboration reports its worst difference', COR,
     'WORST DIFFERENCE ACROSS ALL THIRTEEN CELLS'),
    ('### and states the two routes share no code', COR, 'THE TWO ROUTES SHARE NO CODE'),
    ('the read files the defect', READ, 'PROSE-VS-TABLE DEFECTS FILED AGAINST b319'),
    ('the extract reports nothing missing', EXTRACT, 'SOURCE FRAGMENTS NOT FOUND : 0'),
]

MUST_FAIL = [
    # ### **`G-NOWIDEN` -- the sentences an act that wanted its control would have written.**
    ('the bar is not widened', BANK, 'THE BAR IS WIDENED.'),
    ('the covered set is not enlarged', BANK, 'THE COVERED SET IS ENLARGED.'),
    ('the floor is not lowered', BANK, 'THE FLOOR IS LOWERED.'),
    ('no cell is dropped to make it pass', BANK, 'THE FAILING CELL IS DROPPED.'),
    ('the registration is not re-sealed', BANK, 'THE REGISTRATION IS RE-SEALED.'),
    # ### **`G-NOWINDOW`.**
    ('the window is not opened', BANK, 'THE WINDOW IS OPEN.'),
    ('the uncovered cells are not read as evidence', BANK, 'THE UNCOVERED CELLS CONFIRM IT.'),
    ('the theorem is not extended', BANK, 'THE THEOREM EXTENDS.'),
    # ### **THE CONTROL IS NOT A RESULT ABOUT THE OBJECT.**
    ('no theorem is proved', BANK, 'THE THEOREM IS PROVED.'),
    ('positivity is not claimed', BANK, 'WEIL POSITIVITY HOLDS.'),
    ('the operator is not called positive', BANK, 'THE OPERATOR IS POSITIVE.'),
    ('the margin size is not certified', BANK, 'THE MARGIN IS CONVERGED.'),
    # ### **`G-NOUNIT`.**
    ('the unit is not used', BANK, 'THE UNIT IS USED.'),
    ('membership is not decided', BANK, 'THE MEMBERSHIP IS DECIDED.'),
    # ### **`G-NOREVERDICT`.**
    ('b318 is not re-verdicted', BANK, 'b318 IS RE-VERDICTED.'),
    ('b319 is not re-verdicted', BANK, 'b319 IS RE-VERDICTED.'),
    ('b319 is not edited', BANK, "b319's BANK IS CORRECTED."),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    # ### **THE STANDING CAPS.**
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('nothing about the identity', BANK, 'THE IDENTITY IS AFFECTED.'),
    ('no p-adic reach is claimed', BANK, 'THE p-ADIC ZERO CARRIES OVER.'),
]

TOOLNUM = [
    ("the archimedean Weil distribution, from (53) and (38)", 'tools/b320_weil.py'),
    ("### the same quantity by a second and independent route", 'tools/b320_corroborate.py'),
    ("the components, the covered cells, the reach and the control", 'tools/b320_run.py'),
    ("the read of b319's bank against its own table", 'tools/b320_b319_read.py'),
    ("the source fragments, located", 'tools/b320_extract.py'),
    ("### the finder those fragments were located with", 'tools/b317_extract.py'),
    ("the square and the autocorrelation", 'tools/b318_square.py'),
    ("the subspace both sides are computed on", 'tools/b319_stable.py'),
    ("the seed, the kernel and the cells", 'tools/b317_smear.py'),
    ("the grid scheme and the projector", 'tools/b316_instrument.py'),
    ("the corpus's digamma kernel", 'tools/e16/carto_atlas.py'),
    ("the floor/drift verdicts", 'tools/noise_floor.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b320_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b320_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers", 'tools/b320_correspondence.py'),
    ("the index keys' read-back arms", 'tools/b320_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b320' in x)

# ### **THE DECLARED LITERALS IN THE DECIDING RUNNER, AND WHERE EACH COMES FROM.**
# ### `0.0`, `1.0`, `2.0` are the points the act's own comparisons are stated against.
# ### `100.0` is a percent for display; `1e-9` is the sealed class floor AND the sealed Theorem 1
# ### tolerance; `0.05` is the sealed five per cent reach bar; `1e-300` is a divide guard.
# ### ### **AND `0.5, 1.5, 32.0` ARE THE FRAME AND SUPPORT CONSTANTS OF THE INSTRUMENT AS BUILT**,
# ### imported from b316/b317 and reproduced here only where a display needs the number.
# ### **AND `0.5772156649015329` IS EULER'S CONSTANT, WHICH DECIDES NOTHING HERE.** ### It appears
# ### in ONE display line: the note that the MEASURED `C_R` from (38) lands on `gamma + log(2 pi)`.
# ### **THE DEFINITION OF `C_R` IS (38) AND THE MEASUREMENT IS INDEPENDENT OF THIS NUMBER**; if the
# ### line were deleted every value in the act would be unchanged.
FLOAT_OK = {'0.0', '1.0', '2.0', '100.0', '1e-9', '1e-300', '0.05', '0.5', '1.5', '32.0',
            '0.5772156649015329'}

# ### **THE SEALED HASH, WRITTEN HERE BEFORE THE CONTROL WAS RE-RUN.** ### `G-NOWIDEN` compares the
# ### registration's live seal against this literal. ### If the act had re-sealed to make the
# ### control pass, this arm would fire.
SEAL = '6f1c1e1389c302c380d9ebc7f3e3a2b7b68d35953e07ba36ef3a6cd238093af8'


def main():
    fails = []
    print('=' * 100)
    print('b320 -- GATE SUITE (A CONSTRUCTION, A COMPUTATION, AND A CONTROL)')
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
    cor = io.open(COR, encoding='utf-8').read()
    reg = io.open(REG, encoding='utf-8').read()
    src = io.open(t('b320_run.py'), encoding='utf-8').read()
    wl = io.open(t('b320_weil.py'), encoding='utf-8').read()
    cr = io.open(t('b320_corroborate.py'), encoding='utf-8').read()
    code = K7.strip_text(src) + K7.strip_text(wl) + K7.strip_text(cr)

    print('\n  G-NOWIDEN (the control failed first, and NOTHING was moved to make it pass):')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    same = SEAL in reg
    floor = 'THE FLOOR IS THE SEALED `-1e-09`' in bank or '-1.0e-09' in run
    three = 'THE COVERED CELLS, NAMED FROM THE CHECK : 1.3, 1.35, 1.41' in run
    said = ("BUT THIS ACT'S FIRST REPORTED VERDICT WAS `FAILS`" in bank
            and 'NO BAR WAS MOVED' in bank
            and 'THE REGISTRATION WAS NOT RE-SEALED' in bank)
    print('    the seal verifies : %s ; the hash is the one written BEFORE the re-run : %s'
          % (intact, same))
    print('    the class floor is still the sealed one : %s ; still three covered cells : %s'
          % (floor, three))
    print('    and the bank states the FAILS, the unmoved bar and the unbroken seal : %s' % said)
    print('    ### **THE HASH IN THIS GATE IS A LITERAL.** ### It was written from the seal the')
    print('    ### registration carried before the failing run. ### An act that re-sealed to make')
    print('    ### its control pass would fire this arm and could not silence it by editing the')
    print('    ### registration, because the comparison is against a constant in the gate.')
    if not (intact and same and floor and three and said):
        fails.append('G-NOWIDEN')

    print('\n  G-NOWINDOW (the uncovered cells are data, and carry no claim):')
    nw = ('THE THEOREM DOES NOT COVER THESE CELLS AND NEITHER DOES THIS ACT' in run
          and 'NO WINDOW IS OPENED' in bank)
    print('    the run and the bank both refuse them : %s' % nw)
    if not nw:
        fails.append('G-NOWINDOW')

    print('\n  G-NOUNIT (no unit is used, and none is defined -- scanned over STRIPPED code):')
    sq_, sl_ = K7.strip_fixture()
    print('    STRIPPER FIXTURE (imported from b317): quiet=%s loud=%s' % (sq_, sl_))
    if not (sq_ and sl_):
        fails.append('G-NOUNIT (fixture)')
    used = re.search(r'sonin_unit|unit_vector|def\s+unit', code)
    print('    any unit definition or call in this act\'s stripped code : %s' % bool(used))
    print('    ### **b317 AND b318 CAPPED THIS THE SAME WAY AND b317\'s VERSION FIRED ON ITS OWN')
    print('    ### ### DOCSTRING**, because it scanned raw source. ### This one strips first.')
    if used:
        fails.append('G-NOUNIT')

    print('\n  G-CORROB (a second route to the left-hand side, able to agree AND to disagree):')
    m = re.search(r'WORST DIFFERENCE ACROSS ALL THIRTEEN CELLS : ([0-9.eE+-]+)', cor)
    worst = float(m.group(1)) if m else None
    agrees = worst is not None and worst < 1e-3
    candisagree = 'deliberately halved' in cor and '1.233e+00' in cor
    coarse = 'as it must be' in cor
    shares = 'THE TWO ROUTES SHARE NO CODE' in cor
    print('    worst difference across the cells : %s ; agrees : %s' % (worst, agrees))
    print('    the halved-kernel arm breaks the agreement : %s' % candisagree)
    print('    the too-coarse-grid arm is visibly wrong : %s' % coarse)
    print('    and the routes are stated to share no code : %s' % shares)
    print('    ### **A SECOND ROUTE THAT AGREED WITH ANYTHING WOULD CORROBORATE NOTHING**, which is')
    print('    ### why the halved-kernel arm is required to FAIL and is checked here.')
    if not (agrees and candisagree and coarse and shares):
        fails.append('G-CORROB')

    print('\n  G-FAILFIRST (the record carries the failing run, not only the holding one):')
    ff = ("BUT THIS ACT'S FIRST REPORTED VERDICT WAS `FAILS`" in bank
          and 'THE FAILURE AND THE REPAIR' in bank
          and 'MY OWN IMPLEMENTATION OF THE SOURCE' in bank)
    tbl = io.open(TABLE, encoding='utf-8').read()
    inrow = "THIS ACT'S FIRST REPORTED VERDICT WAS FAILS" in tbl
    print('    the bank carries it at full prominence : %s' % ff)
    print('    ### and so does the correspondence row, where a reader arrives first : %s' % inrow)
    if not (ff and inrow):
        fails.append('G-FAILFIRST')

    print('\n  G-EXPECT (the registered expectation is scored, including the half that is wrong):')
    ex = ('HALF RIGHT AND HALF REFUTED' in bank and 'IT GROWS' in bank)
    print('    the refuted half is reported as loudly as the confirmed one : %s' % ex)
    if not ex:
        fails.append('G-EXPECT')

    print('\n  G-SIZE (the margin\'s SIGN is claimed and its SIZE is refused):')
    sz = ('ITS SIZE IS NOT CERTIFIED AT ANY' in bank and 'REFUSED -- 3 of 6' in run
          and '3 OF 6, ALL DOMAIN' in bank)
    print('    the noise gate refuses, and the bank carries that refusal : %s' % sz)
    if not sz:
        fails.append('G-SIZE')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('the class test, able to reject (b318 fixture ii)', 'A CLASS TEST EVERYTHING' in bank),
            ('the assembly against the source\'s own (39)', '1.842e-16' in run),
            ('### and against a deliberately halved (39)', '3.767e-02' in run),
            ('the constant, measured across straddling widths', '(i-b)' in run),
            ('the assembly, invariant under a grid change', '(vi-b)' in run),
            ('the second route, able to disagree', '1.233e+00' in cor),
            ('the noise-floor gate -- REPORTED REFUSING', 'REFUSED -- 3 of 6' in run)]
    for lbl, ok_ in arms:
        print('    %-56s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
    if not all(x for _l, x in arms):
        fails.append('G-ARMS')

    print('\n  G-NOFLOAT (no undeclared float literal in the deciding runner):')
    rcode = K7.strip_text(src)
    lits = set()
    for m in re.finditer(r'(?<![\w.])(\d+\.\d*(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![\w.])', rcode):
        lits.add(m.group(1))
    extra = sorted(x for x in lits if x not in FLOAT_OK)
    print('    float literals in b320_run.py : %d ; UNDECLARED : %d %s'
          % (len(lits), len(extra), extra if extra else ''))
    if extra:
        fails.append('G-NOFLOAT')

    print('\n  G-NOEDIT (the owner instruments byte-identical to git HEAD, checked AFTER the run):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    if dirty:
        fails.append('G-NOEDIT')

    print('\n  G-NOPAPERS / G-ANCESTOR:')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    pfx = now.startswith(head.rstrip('\n'))
    print('    PLACE-papers tracked changes : %d ; table is a TRUE PREFIX : %s'
          % (len(tracked), pfx))
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

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN),
                      ('the corroboration', COR), ('the read', READ)]:
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
