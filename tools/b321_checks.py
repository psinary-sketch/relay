# -*- coding: utf-8 -*-
"""b321_checks.py -- THE GATE SUITE FOR TWO CONTROLS AND AN OPENED WINDOW.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-FORCED`** ### -- ### **THE ONE THIS ACT COULD MOST EASILY HAVE BREACHED, AND IT
###     ### IS NOT A CAP ON AN ACTION BUT ON A SENTENCE.** ### The window's balance came out
###     non-positive at 10 of 10 cells. ### That count is FORCED: the pole term vanishes for a lawful
###     `f`, so the places sum IS minus the zero side, and the zero side is a sum of squared moduli
###     over an ordinate library holding only zeros ON the line. ### **A BANK THAT PRINTED `10 OF 10`
###     ### WITHOUT THAT WOULD BE A TRUE DOCUMENT ASSEMBLED TO GIVE A FALSE IMPRESSION**, and this
###     arm requires the bank, the run AND the index row to carry it.
###   ### **`G-NOREAD`** ### -- the balance is INTERPRETED BY NOBODY. ### The registration caps
###     `interpretations of the window's balance` at zero and the must-fail lines re-measure it.
###   ### **`G-REFUTED`** ### -- the order said the identity closes the exponent question if it
###     holds. ### It held and it did not. ### **THE ACT MUST REPORT THAT AGAINST ITSELF**, with the
###     other copy's numbers printed, and this arm requires it.
###   ### **`G-NOWIDEN`** ### -- one quadrature pair missed the sealed `1e-06`. ### **THE BAR DID NOT
###     ### MOVE.** ### The seal hash is a literal in this file, written before the controls ran.
###   ### **`G-REPRO`** ### -- the re-formed channels reproduce `carto_atlas.channels` on the atlas's
###     OWN bump. ### **A RE-IMPLEMENTATION THAT CANNOT REPRODUCE ITS ORIGINAL IS AN OVERWRITE.**
###   ### **`G-NOUNIT`** ### -- no unit is used and none is defined, scanned over STRIPPED code.
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

# ### **THE OWNERS. ### THE e16 FILES AND EVERY PRIOR ACT'S TOOL ARE IMPORTED, NEVER EDITED.**
OWNERS = ['tools/e16/carto_atlas.py', 'tools/e16/qeps_layer.py', 'tools/e16/b205_prolate.py',
          'tools/e16/zeta_ordinates.py', 'tools/e16/b313f_qeps_layer.py',
          'tools/e16/b313r_qeps_layer.py', 'tools/e16/prolate_layer.py',
          'tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py',
          'tools/b319_stable.py', 'tools/b320_weil.py', 'tools/noise_floor.py',
          'tools/b305_source.py', 'tools/b317_extract.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b321_the_window_opened.txt')
REG = d('b321_registration_2026-09-04.txt')
RUN = d('b321_components_run.txt')
FIX = d('b321_window_fixtures.txt')
SCAN = d('b321_ferry_scan.txt')
FERRY = d('b321_ferry_2026-09-04.txt')
CENSUS = d('b321_census.txt')
EXTRACT = d('b321_extract_notes.txt')

OWNED = [RUN, FIX, CENSUS, EXTRACT, d('b321_index_query.txt'), d('b321_index_run.txt'),
         d('b321_pins_stepzero.txt'), d('b321_regspec_run.txt'), d('b321_reg_termscan.txt'),
         d('b321_satisfiable.json'), d('b321_satisfiable_run.txt'), d('b321_rows.json'),
         t('b321_regspec.py'), t('b321_correspondence.py'), t('b321_run.py'),
         t('b321_window.py'), t('b321_extract.py')]

CARRIERS = [
    (t('b321_checks.py'), 'its own fixtures'),
    (t('b321_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("Theorem 4.7 -- the EQUALITY, from the extract", EXTRACT, 'Theorem 4.7 Let S be'),
    ("### and (84), the remainder it names", EXTRACT, 'which is given, for'),
    ("(1) -- the explicit formula, from the extract", EXTRACT, 'equivalent to the negativity'),
    ("(148) -- the same formula with its signs", EXTRACT, 'takes the form'),
    ("(149) -- the finite place", EXTRACT, 'runs over all places'),
    ("### the archimedean sign, in the source's own sentence", EXTRACT, 'is proven'),
    ("Proposition C.1 -- the criterion itself", EXTRACT, 'Positivity criterion'),
    ("(61) -- the exponent at its defining site", EXTRACT, 'its action is given by'),
    ("the remainder under the SOURCE exponent -- the b313 flipped copy",
     os.path.join(ROOT, 'tools', 'e16', 'b313f_qeps_layer.py'), 'r ** 0.5'),
    ("### and the corpus's banked exponent, for the contrast",
     os.path.join(ROOT, 'tools', 'e16', 'b313r_qeps_layer.py'), 'r ** -0.5'),
    ("the settled chain, at its emitting file",
     os.path.join(ROOT, 'tools', 'e16', 'carto_atlas.py'), 'def channels'),
    ("### and its sign convention, in the atlas's own header",
     os.path.join(ROOT, 'tools', 'e16', 'carto_atlas.py'), 'sign fixed BY the E2 calibration'),
    ("the zero library", os.path.join(ROOT, 'tools', 'e16', 'zeta_ordinates.py'), 'def build'),
    ("the archimedean distribution -- b320", t('b320_weil.py'), 'def weil'),
    ("the product and the square -- b318", t('b318_square.py'), 'def autocorrelation'),
    ("the space -- b319", t('b319_stable.py'), 'def stable_subspace'),
    ("b320 -- the margins this act tests against", d('b320_the_lawful_function.txt'),
     'VERDICT : HOLDS'),
    ("b313 -- the reading this act rests its exponent on", d('b313_the_exponent.txt'),
     'THE RESIDUE IS NOT THE EXPONENT'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('bank gives the identity verdict', BANK, 'THE IDENTITY CONTROL HOLDS'),
    ('### bank refuses the exponent claim the order expected', BANK,
     'BUT IT DOES NOT CLOSE THE EXPONENT QUESTION'),
    ('### and says the other copy passes too', BANK, 'PASSES EVERY'),
    ('### and says why a measurement cannot settle it', BANK,
     'AN INSTRUMENT CANNOT DISCRIMINATE BETWEEN TWO CANDIDATES THAT LIE CLOSER TOGETHER THAN ITS'),
    ('bank gives the explicit-formula verdict', BANK, 'THE EXPLICIT-FORMULA CONTROL HOLDS'),
    ('bank states the second route shares no code', BANK, 'THEY SHARE NO CODE'),
    ('### bank says the window count is FORCED', BANK,
     'THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION'),
    ('### and names the first reason', BANK, 'THE POLE TERM VANISHES IDENTICALLY FOR A LAWFUL'),
    ('### and the second', BANK, 'BEFORE A SINGLE PRIME IS SUMMED'),
    ('### and refuses its own headline', BANK,
     'IS THEREFORE THE SHAPE OF THE ARITHMETIC AND NOT A MEASUREMENT OF THE OBJECT'),
    ('bank reports the one real measurement here', BANK,
     'THE PRIME SUM CHANGES SIGN TWICE ALONG THE LADDER'),
    ('bank reports the prime-against-margin fact', BANK,
     'THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL OF THIS LADDER'),
    ('bank reports the noise gate refusing', BANK, 'THE NOISE-FLOOR GATE STILL REFUSES 3 OF 6'),
    ('bank refuses the theorem reading', BANK, 'NO THEOREM IS PROVED HERE'),
    ('### bank carries the finite-window sentence', BANK, 'DECIDES NOTHING GLOBAL'),
    ('### bank states that no bar moved', BANK, 'NO BAR WAS MOVED, NO CELL DROPPED'),
    ('### and how the quadrature defect was met', BANK,
     'THE BAR DID NOT MOVE. ### THE QUADRATURE DID MORE WORK'),
    ('bank gives the defect its own section', BANK, 'ONE QUADRATURE DEFECT, FOUND BY A SEALED BAR'),
    ('bank states the rule the lore gains', BANK, 'THE TWO-ROUTES RULE'),
    ('### and the re-implementation law', BANK, 'A RE-IMPLEMENTATION THAT CANNOT REPRODUCE'),
    ('bank declares the numbering difference', BANK, 'ONE NUMBERING DIFFERENCE'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 remains owed under its cap'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK IS RESTATED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### and that nothing is kept', BANK, 'NOTHING IS KEPT'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('### and names the membership act', BANK, 'THE MEMBERSHIP ACT'),
    ('### and names the fold as still due', BANK, 'AND THE FOLD, FROM b314 ONWARD, IS DUE'),
    ('registration names the act', REG, 'THE WINDOW OPENED'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives the identity verdict', RUN, 'VERDICT -- THE IDENTITY CONTROL : HOLDS'),
    ('the run gives the formula verdict', RUN, 'VERDICT -- THE EXPLICIT-FORMULA CONTROL : HOLDS'),
    ('### the run scores the other exponent copy', RUN,
     'THE CORPUS COPY PASSES THE SAME ARMS AT 3 OF 3 CELLS'),
    ('### the run measures the vanishing pole term', RUN, 'THE POLE TERM VANISHES AT EVERY CELL'),
    ('the run counts the non-positive totals', RUN,
     'CELLS ABOVE THE BOUNDARY WHOSE FINITE-INSTANCE TOTAL IS NON-POSITIVE'),
    ('the run quotes what the criterion asks for', RUN,
     'THE CRITERION ASKS FOR A NON-POSITIVE TOTAL'),
    ('the run reports the noise gate refusing', RUN, 'REFUSED -- 3 of 6'),
    ('the extract reports nothing missing', EXTRACT, 'SOURCE FRAGMENTS NOT FOUND : 0'),
]

MUST_FAIL = [
    # ### **`G-NOREAD` -- the sentences a window act would be tempted to write.**
    ('the balance is not read as evidence', BANK, 'THE BALANCE CONFIRMS IT.'),
    ('the criterion is not decided', BANK, 'THE CRITERION IS SATISFIED.'),
    ('RH is not addressed', BANK, 'RH HOLDS.'),
    ('the window is not called a confirmation', BANK, 'THE WINDOW CONFIRMS THE HYPOTHESIS.'),
    ('the count is not called evidence', BANK, 'TEN OF TEN IS EVIDENCE.'),
    ('the finite instance is not generalised', BANK, 'THE BALANCE IS NEGATIVE IN GENERAL.'),
    # ### **`G-REFUTED` -- and the sentence that would have hidden it.**
    ('the exponent is not called settled', BANK, 'THE EXPONENT QUESTION IS CLOSED.'),
    ('the corpus copy is not called refuted', BANK, 'THE CORPUS EXPONENT IS REFUTED.'),
    # ### **`G-NOWIDEN`.**
    ('the bar is not widened', BANK, 'THE BAR IS WIDENED.'),
    ('the tolerance is not loosened', BANK, 'THE TOLERANCE IS LOOSENED.'),
    ('the registration is not re-sealed', BANK, 'THE REGISTRATION IS RE-SEALED.'),
    ('no cell is dropped', BANK, 'THE FAILING CELL IS DROPPED.'),
    # ### **THE CONTROLS ARE NOT RESULTS ABOUT THE OBJECT.**
    ('no theorem is proved', BANK, 'THE THEOREM IS PROVED.'),
    ('positivity is not claimed', BANK, 'WEIL POSITIVITY HOLDS.'),
    ('the margin size is not certified', BANK, 'THE MARGIN IS CONVERGED.'),
    # ### **THE STANDING CAPS.**
    ('the unit is not used', BANK, 'THE UNIT IS USED.'),
    ('membership is not decided', BANK, 'THE MEMBERSHIP IS DECIDED.'),
    ('no act is re-verdicted', BANK, 'b320 IS RE-VERDICTED.'),
    ('b313 is not re-verdicted', BANK, 'b313 IS RE-VERDICTED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('nothing about the identity', BANK, "THE IDENTITY'S TRUTH IS DECIDED."),
    ('nothing about the roster', BANK, 'THE ROSTER IS COMPLETE.'),
]

TOOLNUM = [
    ("the remainder integral and the four channels", 'tools/b321_window.py'),
    ("the two controls, the window and the slack", 'tools/b321_run.py'),
    ("the source fragments, located", 'tools/b321_extract.py'),
    ("### the finder those fragments were located with", 'tools/b317_extract.py'),
    ("the remainder under the source's exponent", 'tools/e16/b313f_qeps_layer.py'),
    ("### and under the corpus's, for the contrast", 'tools/e16/b313r_qeps_layer.py'),
    ("the settled chain and the digamma kernel", 'tools/e16/carto_atlas.py'),
    ("the zero ordinates", 'tools/e16/zeta_ordinates.py'),
    ("the archimedean distribution from (38)", 'tools/b320_weil.py'),
    ("the square and the autocorrelation", 'tools/b318_square.py'),
    ("the subspace both sides are computed on", 'tools/b319_stable.py'),
    ("the seed, the kernel and the cells", 'tools/b317_smear.py'),
    ("the grid scheme and the projector", 'tools/b316_instrument.py'),
    ("the floor/drift verdicts", 'tools/noise_floor.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b321_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b321_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers", 'tools/b321_correspondence.py'),
    ("the index keys' read-back arms", 'tools/b321_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b321' in x)

# ### **THE DECLARED LITERALS IN THE DECIDING RUNNER, AND WHERE EACH COMES FROM.**
# ### `1e-6` is (B1d); `1e-3` is (B2), and the runner asserts it EQUALS the atlas's own `TOL`
# ### rather than restating it from memory. ### `2.0` is the `sqrt` argument for the boundary
# ### `2^{1/2}`, which is Theorem 1's support condition and not a threshold this act picked.
# ### `0.0` and `1e-300` are a comparison point and a divide guard.
FLOAT_OK = {'0.0', '1e-6', '1e-3', '2.0', '1e-300'}

# ### **THE SEALED HASH, WRITTEN HERE BEFORE ANY CONTROL WAS RUN.** ### `G-NOWIDEN` compares the
# ### registration's live seal against this literal, so a bar moved after a value was seen cannot be
# ### hidden by editing the registration.
SEAL = '8a5107e9fccb7a587e4ccdd56ac75142afcb2412a894914b672f91d449a29d37'


def main():
    fails = []
    print('=' * 100)
    print('b321 -- GATE SUITE (TWO CONTROLS AND AN OPENED WINDOW)')
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
    reg = io.open(REG, encoding='utf-8').read()
    fix = io.open(FIX, encoding='utf-8').read()
    src = io.open(t('b321_run.py'), encoding='utf-8').read()
    win = io.open(t('b321_window.py'), encoding='utf-8').read()
    code = K7.strip_text(src) + K7.strip_text(win)
    idx = io.open(t('banked_index.py'), encoding='utf-8').read()

    print('\n  G-FORCED (the window count is FORCED, and the record says so in three places):')
    inbank = ('THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION' in bank
              and 'THE POLE TERM VANISHES IDENTICALLY FOR A LAWFUL' in bank
              and 'BEFORE A SINGLE PRIME IS SUMMED' in bank)
    inrun = ('THE POLE TERM VANISHES AT EVERY CELL' in run
             and 'AND THAT SETTLES THE SIGN OF THE TOTAL BEFORE THE TOTAL IS COMPUTED' in run)
    inidx = 'FORCED BY THE SHAPE OF THE COMPUTATION' in idx
    print('    the bank carries it, with both reasons : %s' % inbank)
    print('    the run carries it BEFORE the total is taken : %s' % inrun)
    print('    ### and the index row hands it back on query : %s' % inidx)
    print('    ### **THE RUN PRINTS IT BEFORE THE TOTAL AND NOT AFTER, WHICH IS THE WHOLE POINT.**')
    print('    ### A reader who reaches the `10 of 10` has already been told it could not have come')
    print('    ### out otherwise. ### **A COUNT THAT COULD NOT HAVE COME OUT THE OTHER WAY IS NOT A')
    print('    ### ### RESULT**, and this arm is what stops the record from implying it is one.')
    if not (inbank and inrun and inidx):
        fails.append('G-FORCED')

    print('\n  G-NOREAD (the balance is interpreted by nobody):')
    nr = ('AND NOBODY IN THIS ACT INTERPRETS ANY OF IT' in bank
          and 'interpreted by nobody in this act' in run.lower()
          or 'INTERPRETED BY NOBODY IN THIS ACT' in bank)
    print('    the bank and the run both refuse the reading : %s' % nr)
    if not nr:
        fails.append('G-NOREAD')

    print('\n  G-REFUTED (the order expected the exponent settled; the act reports it was not):')
    rf = ('BUT IT DOES NOT CLOSE THE EXPONENT QUESTION' in bank
          and 'THE CORPUS COPY PASSES THE SAME ARMS AT 3 OF 3 CELLS' in run
          and 'IT HELD, AND IT DID NOT' in io.open(TABLE, encoding='utf-8').read())
    print('    bank, run and correspondence row all carry the refutation : %s' % rf)
    print('    ### **THE ACT REPORTS AGAINST ITS OWN ORDER HERE**, with the other copy\'s numbers')
    print('    ### printed beside its own, and that is the only way the report is worth anything.')
    if not rf:
        fails.append('G-REFUTED')

    print('\n  G-NOWIDEN (a sealed bar was missed and the bar did not move):')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    same = SEAL in reg
    declared = ('THE BAR DID NOT MOVE. ### THE QUADRATURE DID MORE WORK' in bank
                and 'ONE QUADRATURE DEFECT, FOUND BY A SEALED BAR' in bank)
    barlive = "BAR_TWOROUTE = 1e-6" in src
    print('    the seal verifies : %s ; the hash is the one written BEFORE the controls : %s'
          % (intact, same))
    print('    the runner still carries the sealed 1e-06 : %s' % barlive)
    print('    and the bank declares the defect and the response : %s' % declared)
    if not (intact and same and declared and barlive):
        fails.append('G-NOWIDEN')

    print('\n  G-REPRO (the re-implementation reproduces its original on the original\'s own input):')
    m = re.search(r'worst channel difference : ([0-9.eE+-]+)', fix)
    worst = float(m.group(1)) if m else None
    rp = worst is not None and worst < 1e-12
    print('    worst channel difference against `carto_atlas.channels` : %s' % worst)
    print('    ### **A RE-IMPLEMENTATION THAT CANNOT REPRODUCE ITS ORIGINAL IS AN OVERWRITE**, and')
    print('    ### nothing else in this act would be worth reading if this arm failed.')
    if not rp:
        fails.append('G-REPRO')

    print('\n  G-NOUNIT (no unit used and none defined -- scanned over STRIPPED code):')
    sq_, sl_ = K7.strip_fixture()
    print('    STRIPPER FIXTURE (imported from b317): quiet=%s loud=%s' % (sq_, sl_))
    if not (sq_ and sl_):
        fails.append('G-NOUNIT (fixture)')
    used = re.search(r'sonin_unit|unit_vector|def\s+unit', code)
    print('    any unit definition or call in this act\'s stripped code : %s' % bool(used))
    if used:
        fails.append('G-NOUNIT')

    print('\n  G-SIGNS (every sign quoted from an owner, and the owner named):')
    sg = ('is proven' in io.open(EXTRACT, encoding='utf-8').read()
          and 'sign fixed BY the E2 calibration' in win
          and 'THE NAVIGATOR SUPPLIED NONE OF THEM' in win)
    print('    the source sentence, the atlas header, and the disclaimer : %s' % sg)
    if not sg:
        fails.append('G-SIGNS')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('the channels, able to disagree on a halved input', 'differs, as it must' in fix),
            ('the two exponent copies, measurably different', 'they DIFFER' in fix),
            ('the remainder integral, linear in eps', 'with eps halved' in fix),
            ('(149) by two expressions, agreeing', 'written out' in fix),
            ('the second route to the archimedean term', 'WORST DIFFERENCE' in run),
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
    print('    float literals in b321_run.py : %d ; UNDECLARED : %d %s'
          % (len(lits), len(extra), extra if extra else ''))
    if extra:
        fails.append('G-NOFLOAT')

    print('\n  G-NOEDIT (the owner instruments byte-identical to git HEAD, checked AFTER the run):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    print('    ### **THE b313 COPIES ARE IN THIS LIST.** ### They are copies, and a copy that gets')
    print('    ### edited by the act that uses it is no longer evidence of anything.')
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

    print('\n  G-SHARED (the stem sweep at extended scope):')
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
        print('    %-52s %-36s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN),
                      ('the fixtures', FIX)]:
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
