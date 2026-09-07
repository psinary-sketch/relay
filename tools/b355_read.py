# -*- coding: utf-8 -*-
"""b355_read.py -- WHAT THE ARRAYS ARE. ### A READ AND A FILING. ### IT COMPUTES NOTHING.

### ### **WHAT IT IMPORTS IS THE WHOLE ARGUMENT THAT IT COMPUTES NOTHING:** ### a needle puller, the step-zero
### anchor tool, the shared normaliser, and a clock. ### **NO FRAME, NO SEED, NO TRANSFORM, NO FIT.**
### ### **THE TWO HYPOTHESES ARE ANSWERED IN THEIR OWN SECTIONS AND NEITHER IN TERMS OF THE OTHER**, because
### `H1` is about the OBJECT and `H3` is about the INSTRUMENT'S REACH, and the answers can point different
### ways. ### **THE THREE LAYERS ARE KEPT APART** (registration section (B)) and each is located at a line.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import quote_norm    # noqa: E402
import run_clock     # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCAN = 'USED THE SCAN'
EQUIV = 'USED THE EQUIVALENCE'
BOTH = 'USED BOTH'
NEITHER = 'USED NEITHER'
TERMS = (SCAN, EQUIV, BOTH, NEITHER)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def show(path, hint, note=''):
    n, line = AF.find(path, hint)
    needle_pull.pull(path, line)
    rec('        %s:%d' % (os.path.relpath(path, ROOT).replace(os.sep, '/'), n))
    rec('          | %s' % line.strip())
    if note:
        rec('          ### %s' % note)
    return n, line


def main():
    rec('=' * 100)
    rec('b355 -- WHAT THE ARRAYS ARE. ### A READ AND A FILING. ### NOTHING IS COMPUTED.')
    rec('=' * 100)
    rec('  ### the consequence terms, and no others : %s' % ' / '.join(TERMS))
    rec('  ### ### **H1 AND H3 ARE ANSWERED SEPARATELY AND NEITHER IN TERMS OF THE OTHER.**')

    # ============================================================ (1) THE THREE LAYERS.
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE THREE LAYERS, EACH LOCATED AT AN EMITTING LINE.')
    rec('-' * 100)
    rec('')
    rec('    ### **LAYER 1 -- THE GENERATING FORMULA.** ### It is the standard smooth bump.')
    show(t('e16/carto_atlas.py'), 'v = np.linspace(-L, L, NV)')
    show(t('e16/carto_atlas.py'), 'w[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))',
         'exp(-1/(1 - t^2)) on |t| < 1 and zero outside: THE TEXTBOOK Cc^infty BUMP')
    rec('    ### ### **SO THE FORMULA THE CODE WRITES DOWN IS IN THE SOURCE\'S CLASS.** ### That much is')
    rec('    ### ### not in doubt and is stated here first, because the answer below is easy to misread as')
    rec('    ### ### saying the corpus never had a smooth function in hand.')
    rec('')
    rec('    ### **LAYER 2 -- THE SAMPLED ARRAY.** ### The formula is evaluated at `NV` nodes and then')
    rec('    ### normalised by a quadrature ON THOSE NODES:')
    show(t('e16/carto_atlas.py'), 'w /= np.trapezoid(w, v)',
         'the normalising constant is the PIECEWISE-LINEAR integral, not the smooth one')
    rec('    ### ### **SO EVEN THE ARRAY IS NOT A PLAIN SAMPLING OF THE SMOOTH BUMP.** ### It is the smooth')
    rec('    ### ### bump rescaled by a constant that only the piecewise-linear reading makes exact.')
    rec('')
    rec('    ### **LAYER 3 -- THE OBJECT INTEGRATED, WHICH IS WHAT THE ORDER ASKS ABOUT.**')
    show(t('b317_smear.py'), 'return np.interp(np.log(rho), self.v, self.w, left=0.0, right=0.0)',
         'evaluation between nodes IS linear interpolation, and zero outside the grid')
    show(t('b317_smear.py'), 'EVALUATION IS PIECEWISE-LINEAR INTERPOLATION OF THAT GRID AND ZERO OUTSIDE IT')
    rec('    ### ### ### **AND THE RECORD GIVES ITS REASON, IN THE SAME BREATH:**')
    show(t('b317_smear.py'), "function this act integrates is the function the corpus's number was formed from")
    rec('    ### ### ### **THAT IS THE ANSWER THE ORDER ASKED FOR, AND IT IS EXPLICIT.** ### The object is')
    rec('    ### ### ### the piecewise-linear interpolant, ### **CHOSEN**, and the reason given is')
    rec('    ### ### ### ### **AGREEMENT WITH THE CORPUS\'S OWN BANKED NUMBERS** -- not membership in the')
    rec('    ### ### ### source\'s class.')
    rec('    ### And the same choice is stated again, at another file and for another object:')
    show(t('b317_smear.py'), 'THE UNION GRID IS NOT A CONVENIENCE EITHER.** ### Each bump is piecewise linear on its')
    show(t('b317_smear.py'), 'rule is EXACT on a piecewise-linear function over a grid containing its breakpoints')
    show(t('b326_closure.py'), "is piecewise linear on b318's uniform grid, and its transform has",
         'and the consequence the record already drew from it: its transform ALIASES')
    show(t('b326_closure.py'), 'alias peaks at every multiple of')

    # ============================================================ (2) H1, ON ITS OWN.
    rec('')
    rec('-' * 100)
    rec('  ### (2) `H1` -- SMOOTHNESS. ### **ANSWERED ON ITS OWN.**')
    rec('-' * 100)
    rec('    ### **WHAT THE EQUIVALENCE REQUIRES:** ### `f in Cc^infty(R)`.')
    rec('    ### **WHAT THE CORPUS INTEGRATES:** ### a piecewise-linear interpolant, by layer 3 above.')
    rec('    ### ### ### **SO THE OBJECT INTEGRATED IS NOT IN THE CLASS THE EQUIVALENCE QUANTIFIES OVER**,')
    rec('    ### ### ### and the record says what it is at an emitting line rather than leaving it to be')
    rec('    ### ### ### inferred. ### `b353` graded this `REFUTABLE` and said the record did not settle')
    rec('    ### ### ### whether the arrays were discretisations or the objects. ### **IT DOES SETTLE IT,')
    rec('    ### ### ### AT `b317_smear.py`, AND b353 DID NOT LOOK AT THAT LINE.**')
    rec('    ### **AND WHAT DOES NOT FOLLOW, SAID IMMEDIATELY:** ### the smooth bump exists, at layer 1,')
    rec('    ### and the piecewise-linear object is uniformly close to it on a fine grid. ### **NOTHING')
    rec('    ### ### HERE SAYS THE TWO GIVE DIFFERENT NUMBERS.** ### What it says is that ### **THE OBJECT')
    rec('    ### ### THE EQUIVALENCE IS ABOUT AND THE OBJECT THE CORPUS INTEGRATES ARE NOT THE SAME**, and')
    rec('    ### ### no act has measured the difference.')

    # ============================================================ (3) H3, ON ITS OWN.
    rec('')
    rec('-' * 100)
    rec('  ### (3) `H3` -- POINTWISE POSITIVITY. ### **ANSWERED ON ITS OWN, AND IT IS A DIFFERENT QUESTION.**')
    rec('-' * 100)
    rec('    ### **WHAT THE EQUIVALENCE REQUIRES:** ### `f^(t) >= 0` for ALL `t`.')
    rec('    ### **WHAT THE CORPUS DOES:**')
    show(t('b318_square.py'), "The scan runs in units of the cell's own width `L = log a`, so a narrow cell is scanned as")
    show(t('b318_square.py'), 'show a function is NOT positive definite by exhibiting a negative value, and it cannot prove')
    rec('    ### ### **THE INSTRUMENT STATES ITS OWN REACH, AND `b353` GRADED IT `UNDECIDABLE FROM THE')
    rec('    ### ### RECORD` ON THAT BASIS. ### THAT GRADE STANDS AND THIS ACT DOES NOT DISTURB IT.**')
    rec('    ### ### ### **AND HERE IS WHY `H3` IS NOT `H1` AND WHY THE ORDER WAS RIGHT TO SEPARATE THEM:**')
    rec('    ### ### ### `H1` fails because of what the object IS. ### `H3` is undecided because of how far')
    rec('    ### ### ### the LOOKING went. ### **AN ANSWER TO EITHER SETTLES NOTHING ABOUT THE OTHER**, and')
    rec('    ### ### ### an act that had merged them would have produced one verdict about "the arrays"')
    rec('    ### ### ### covering two facts that share only a subject.')

    # ============================================================ (4) THE CHECKS, ONE BY ONE.
    rec('')
    rec('-' * 100)
    rec('  ### (4) EVERY BANKED LAWFULNESS CHECK, CLASSIFIED ONE BY ONE.')
    rec('-' * 100)
    rec('    ### ### **THE DISTINCTION THE REGISTRATION FIXED BEFORE ANY CHECK WAS LOOKED AT:** ### for a')
    rec('    ### ### true autocorrelation `f = g conv g-sharp`, `f^ = |g^|^2` and positivity is AUTOMATIC.')
    rec('    ### ### **SO A SCAN APPLIED TO AN OBJECT BUILT AS AN AUTOCORRELATION IS NOT AN INDEPENDENT')
    rec('    ### ### TEST OF CLASS MEMBERSHIP.**')
    checks = []

    def chk(act, what, used, certifies, hint=None, path=None):
        checks.append(dict(act=act, what=what, used=used, certifies=certifies))
        rec('')
        rec('    ### **%s -- %s**' % (act, what))
        rec('      %s' % used)
        rec('      CERTIFIES : %s' % certifies)
        if hint and path:
            show(path, hint)

    chk('b320', 'the square of the seed is in the source\'s class, 13 of 13', BOTH,
        'that the DISCRETE construction behaves like a continuous autocorrelation. ### The object was BUILT '
        'as g conv g-sharp (the equivalence\'s second condition) and THEN scanned for the first. ### **SO THE '
        'SCAN CORROBORATED THE ARITHMETIC, NOT THE CLASS.**',
        "formed with the source's own involution, tested by the source's own Definition 3.1",
        d('b320_the_lawful_function.txt'))
    rec('      ### **AND THE CONTROL THAT KEEPS IT FROM BEING VACUOUS, WHICH b320 RAN ITSELF:**')
    show(d('b320_the_lawful_function.txt'), 'AND THE TEST CAN FAIL:',
         'on a wide-minus-narrow fixture, which is NOT an autocorrelation -- so the scan discriminates')
    rec('      ### ### **THAT CONTROL IS WHY THE SCAN IS WORTH RUNNING AND IS ALSO WHY IT CERTIFIES WHAT')
    rec('      ### ### IT CERTIFIES:** ### it separates objects built as autocorrelations from objects not')
    rec('      ### ### built that way. ### **IT DOES NOT SEPARATE MEMBERS OF THE SOURCE\'S CLASS FROM')
    rec('      ### ### NON-MEMBERS.**')

    chk('b320', "Theorem 1's three conditions, per cell", NEITHER,
        'that the piecewise-linear object has the support the source demands and that its two moments '
        'vanish to 1e-16 and 1e-17. ### **THOSE ARE THE SOURCE\'S OTHER TWO CONDITIONS AND NEITHER IS THE '
        'EQUIVALENCE NOR THE SCAN**; they are measured directly, and b353 graded them MET TO A MEASURED '
        'TOLERANCE.',
        "THEOREM 1's THREE CONDITIONS, PER CELL.", d('b320_the_lawful_function.txt'))

    chk('b320', 'the covered cells named from the check', NEITHER,
        'which widths satisfy the support condition, which is arithmetic on a and not a class test at all.',
        'THE COVERED CELLS ARE NAMED FROM THE CHECK AND NOT FROM THE WISH', d('b320_the_lawful_function.txt'))

    chk('b328', "lawfulness (L1): the source's Definition 3.1 on f, by b318's scan", BOTH,
        'the same thing b320\'s did, at the aimed seeds: that the discrete construction behaves like an '
        'autocorrelation, within the scan\'s reach.',
        'LAWFULNESS, MEASURED AND NOT ASSUMED', d('b328_registration_2026-09-05.txt'))

    chk('b334, b343, b344, b349', 'every aimed seed checked lawful before being charted', BOTH,
        'the same, once per seed. ### **NO ACT IN THIS FAMILY EVER TESTED CLASS MEMBERSHIP INDEPENDENTLY OF '
        'THE CONSTRUCTION**, because every seed in the family is built the same way.')
    show(d('b349_the_room_relative.txt'), 'NEVER DEGENERATES -- IT MEANS THESE THREE DID NOT',
         "b349's own caveat, which is about the SEEDS tried and not about the class")

    rec('')
    rec('    ### ### **AND THE ONE THING THAT WOULD HAVE BEEN AN INDEPENDENT CLASS TEST IS ABSENT FROM THE')
    rec('    ### ### RECORD:** ### a scan of `f^` on an object NOT built as an autocorrelation and claimed')
    rec('    ### ### to be in the class. ### **NO ACT RAN ONE, AND NONE WAS ASKED TO.**')

    # ============================================================ (5) THE BRANCH.
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE BRANCH, BY THE SEALED RULE OF SECTION (C).')
    rec('-' * 100)
    rec('    ### **(THE RECORD DOES NOT STATE IT) -- UNREACHABLE, AND SHOWN SO.** ### Three emitting lines')
    rec('      state it: the interpolating call, the header sentence that names the interpolation, and the')
    rec('      sentence giving the reason. ### **THE RECORD STATES IT.**')
    rec('    ### **(THE RECORD CONTRADICTS ITSELF) -- UNREACHABLE, AND SHOWN SO.** ### The smooth formula')
    rec('      and the piecewise-linear object are stated at DIFFERENT LAYERS and both are stated plainly.')
    rec('      ### **A SMOOTH FORMULA SAMPLED AND THEN INTERPOLATED IS NOT A CONTRADICTION; IT IS A')
    rec('      ### PIPELINE**, and the record describes each stage of it correctly.')
    rec('    ### ### ### **THEREFORE: THE RECORD STATES IT.**')
    verdict = 'THE RECORD STATES IT'
    rec('')
    rec('    ### ### **AND WHAT IT STATES, IN ONE SENTENCE:** ### **THE CORPUS INTEGRATES A PIECEWISE-LINEAR')
    rec('    ### ### INTERPOLANT OF A SAMPLED SMOOTH BUMP, DELIBERATELY, AND THE REASON THE RECORD GIVES IS')
    rec('    ### ### AGREEMENT WITH ITS OWN BANKED NUMBERS.**')
    rec('    ### ### **THAT IS THE FOURTH OUTCOME SECTION (C) ANTICIPATED** -- stated at one layer and')
    rec('    ### ### another, neither missing nor contradictory -- and it is reported under the first branch')
    rec('    ### ### with the layers named, exactly as the registration said it would be.')
    rec('    ### **AND THE REASON MATTERS AS MUCH AS THE FACT:** ### the choice was made for INTERNAL')
    rec('    ### CONSISTENCY, not for class membership. ### **NOBODY TRADED THE CLASS AWAY; THE QUESTION')
    rec('    ### ### WAS NOT BEING ASKED AT THAT LINE.**')

    # ============================================================ (6) WHAT FOLLOWS.
    rec('')
    rec('-' * 100)
    rec('  ### (6) WHAT FOLLOWS, IN THE ORDER\'S OWN TWO CASES.')
    rec('-' * 100)
    rec('    ### **THE ORDER\'S FIRST CASE -- IF THE ARRAYS MEET THE HYPOTHESES:** ### the equivalence')
    rec('    ### applies at each fixed width and the width coordinate is closed AT A WIDTH and open ACROSS')
    rec('    ### widths. ### **THAT CASE DOES NOT ARISE FOR THE OBJECT INTEGRATED**, because `H1` fails')
    rec('    ### there. ### **AND THIS ACT CONFIRMS b353\'S SENTENCE AND DOES NOT STRENGTHEN IT.**')
    rec('    ### **THE ORDER\'S SECOND CASE -- IF THEY DO NOT:** ### the corpus\'s own instrument is outside')
    rec('    ### the statement it was measured against, and the consequence for every banked lawfulness')
    rec('    ### check is named. ### **THAT IS THE CASE, AND SECTION (4) NAMES THEM ONE BY ONE.**')
    rec('    ### ### ### **AND THE CONSEQUENCE IS A RELABELLING AND NOT A DEMOTION:**')
    rec('      ### **EVERY BANKED NUMBER STANDS.** ### Nothing here recomputes one or contradicts one.')
    rec('      ### **EVERY CHECK THAT PASSED STILL PASSED.** ### What changes is the sentence describing')
    rec('        what passing established.')
    rec('      ### **THE OLD READING:** *the seeds are in the source\'s class, tested by the source\'s own')
    rec('        Definition 3.1.*')
    rec('      ### **THE READING THIS ACT SUPPORTS:** *the seeds are built as autocorrelations of a')
    rec('        piecewise-linear interpolant of a sampled smooth bump, and the scan confirms the discrete')
    rec('        construction behaves like a continuous autocorrelation within its reach.*')
    rec('      ### ### **THE SECOND IS NARROWER AND IT IS TRUE. ### THE FIRST WAS NEVER MEASURED.**')
    rec('    ### **AND WHAT IS ROUTED RATHER THAN DECIDED:** ### whether any banked VERDICT turns on the')
    rec('    ### difference. ### **THIS SEAT\'S READING IS THAT NONE DOES**, because every verdict in the')
    rec('    ### family is stated over the corpus\'s own constructed objects and not over the source\'s class')
    rec('    ### -- but ### **THAT IS A READING AND THE AUTHOR MOVES ROWS**, so it is filed and not applied.')
    rec('    ### **NO ERRATA ENTRY IS DRAFTED**, because no verdict was found to turn on it; if the author')
    rec('    ### reads it otherwise, the entry is one act away.')

    rec('')
    rec('-' * 100)
    rec('  ### (7) BOTH SEATS\' EXPECTATIONS, SCORED.')
    rec('-' * 100)
    rec("    ### **THE NAVIGATOR'S (L2)** -- the arrays do not meet the smoothness hypothesis and the")
    rec('    ### consequence is a relabelling of what the lawfulness checks certify, not a defect in any')
    rec('    ### measurement : ### **MET, BOTH HALVES.**')
    rec("    ### **THIS SEAT'S** -- the record states it at both layers, gives a reason, and the reason is")
    rec('    ### internal consistency rather than class membership : ### **MET**, and the reason is quoted')
    rec('    ### at `b317_smear.py` in the sentence about the function the corpus\'s number was formed from.')

    rec('')
    rec('=' * 100)
    rec('  VERDICT : ### **%s**' % verdict)
    rec('  ### ### **AND WHAT IT IS NOT: ### NO VERDICT IS MOVED. ### NO MEASUREMENT IS WRONG. ### THE WIDTH')
    rec('  ### ### COORDINATE IS NOT CLOSED, AND b353\'S SENTENCE IS CONFIRMED AND NOT STRENGTHENED. ### THE')
    rec('  ### ### PARTITION b351 LEFT `UNDECIDED` STAYS `UNDECIDED`.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b355_read_run', LINES)
    io.open(d('b355_read.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(verdict=verdict, terms=list(TERMS), checks=checks,
             layers=['the generating formula', 'the sampled array', 'the object integrated'],
             h1='REFUTABLE, and the record settles it at an emitting line',
             h3='UNDECIDABLE FROM THE RECORD, and that grade stands',
             errata='NOT DRAFTED -- no banked verdict was found to turn on it; routed to the author',
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
