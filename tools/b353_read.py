# -*- coding: utf-8 -*-
"""b353_read.py -- THE WIDTH COORDINATE'S MISSING STATEMENT. ### A READ AND A PRICING. ### IT COMPUTES NOTHING.

### ### **WHAT IT IMPORTS IS THE WHOLE ARGUMENT THAT IT COMPUTES NOTHING:** a needle puller, the shared
### normaliser, and a clock. ### **NO TRANSFORM, NO SEED, NO FIT, NO SCORE.**
### ### **THE STATUSES ARE THE SEALED FOUR** (registration section (C)), and every hypothesis is graded
### ### **TWICE** -- against the source's class as the source defines it, and against the corpus's constructed
### objects -- with the two gradings labelled and never merged.
### ### **THE BRANCH IS PICKED BY GRADING (i) ALONE**, as section (D) fixed before any hypothesis had a status.
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

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MET = 'MET'
TOL = 'MET TO A MEASURED TOLERANCE'
REF = 'REFUTABLE'
UND = 'UNDECIDABLE FROM THE RECORD'
STATUSES = (MET, TOL, REF, UND)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def cite(path, anchor):
    needle_pull.pull(path, anchor)
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    for i, ln in enumerate(txt, 1):
        if quote_norm.contains(ln, anchor):
            return i, ln.strip()
    raise LookupError(anchor)


def show(path, anchor, note=''):
    n, ln = cite(path, anchor)
    rec('        %s:%d' % (os.path.relpath(path, ROOT).replace(os.sep, '/'), n))
    rec('          | %s' % ln)
    if note:
        rec('          ### %s' % note)
    return n


def main():
    S = json.load(io.open(d('b353_source.json'), encoding='utf-8'))
    src = S['source']
    rec('=' * 100)
    rec("b353 -- THE WIDTH COORDINATE'S MISSING STATEMENT. ### A READ UNDER THE IMPORT BAR, AND A PRICING.")
    rec('=' * 100)
    rec('  ### THE SEALED STATUSES, AND NO OTHERS : %s' % ' / '.join(STATUSES))
    rec('  ### ### **THE HYPOTHESES ARE GRADED TWICE AND THE TWO GRADINGS ARE NEVER MERGED.**')

    # ================================================================= (1) THE STATEMENT, LOCATED.
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE STATEMENT, LOCATED IN A REAL SOURCE AND PINNED.')
    rec('-' * 100)
    rec('    source   : arXiv %s -- %s' % (src['arxiv'], src['title']))
    rec('    authors  : %s ; submitted %s' % (src['authors'], src['submitted']))
    rec('    pinned   : sha256 %s' % src['sha256'])
    rec('               %d bytes, from %s' % (src['bytes'], src['pdf_url']))
    rec('    read at  : %s   ### the PDF carries no text layer the reader could use' % src['html_read'])
    rec('    grade    : ### **%s** (import bar, b233)' % src['grade'])
    rec('')
    rec('    ### ### **THIS IS THE CORPUS\'S OWN ARC SOURCE, NOT A NEW ONE.** ### The record already carries')
    rec('    ### it as the paper whose Definition 3.1 and Theorem 1 the corpus tests against at every cell.')
    rec('')
    rec('    ### ### **THE STATEMENT OF THE SHAPE THE ORDER NAMES -- `PROPOSITION 2`, BOAS-KAC:**')
    for lbl, q in S['quotes']:
        if 'BOAS-KAC' in lbl:
            for i in range(0, len(q), 92):
                rec('      | %s' % q[i:i + 92])
    rec('    ### ### **IT IS AN EQUIVALENCE, AND THAT IS STRONGER THAN A DENSITY STATEMENT.** ### It does not')
    rec('    ### approximate the class by a subfamily; ### **IT EXHAUSTS IT.** ### Every positive-definite')
    rec('    ### `f` supported in `[-A, A]` IS `g * g^*` for some `g` supported in `[-A/2, A/2]`.')
    rec('    ### ### **SO POSITIVITY OF THE WEIL FUNCTIONAL ON THE SEED FAMILY AT HALF-WIDTH CARRIES TO THE')
    rec('    ### ### WHOLE ADMISSIBLE CLASS AT FULL WIDTH, WITH NO LIMIT ARGUMENT AND NO TOPOLOGY.**')
    rec('    ### ### **AND THE ORDER ASKED FOR A DENSITY OR APPROXIMATION STATEMENT; WHAT THE SOURCE CARRIES')
    rec('    ### ### IS BETTER IN KIND AND WEAKER IN REACH, AND THE DIFFERENCE IS THIS ACT\'S WHOLE CONTENT.**')

    # ================================================================= (2) THE HYPOTHESES, TWICE.
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE HYPOTHESES, UNFOLDED AND GRADED TWICE.')
    rec('-' * 100)
    H = []

    rec('')
    rec('    ### **(H1) `f in Cc^infty(R)` -- SMOOTH, COMPACTLY SUPPORTED.**')
    rec('      ### GRADING (i), AGAINST THE SOURCE\'S CLASS : ### **%s.**' % MET)
    rec('        The source\'s own class in Theorem 1 is `g in Cc^infty(R+*)`, and the class in its RH')
    rec('        criterion is `Cc^infty(R+*)`. ### The hypothesis IS the class.')
    rec('      ### GRADING (ii), AGAINST THE CORPUS\'S CONSTRUCTED OBJECTS : ### **%s**, and the record says' % REF)
    rec('      ### it in its own words:')
    show(t('b326_closure.py'), "### `f = autocorrelation(seed)` is piecewise linear on b318's uniform grid, and its transform has")
    show(t('b317_smear.py'), '### ### **THE UNION GRID IS NOT A CONVENIENCE EITHER.** ### Each bump is piecewise linear on its')
    rec('        ### ### **A PIECEWISE-LINEAR FUNCTION IS NOT `C^infty`. ### IT IS NOT EVEN `C^1`.**')
    rec('        ### **AND WHAT THAT DOES AND DOES NOT MEAN, SAID CAREFULLY:** the corpus\'s arrays are a')
    rec('        ### NUMERICAL REPRESENTATION, and whether the record intends them as discretisations of')
    rec('        ### smooth functions or as the objects themselves is ### **A QUESTION THE RECORD DOES NOT')
    rec('        ### SETTLE.** ### What is refutable is the hypothesis about the objects AS CONSTRUCTED.')
    H.append(dict(id='H1', text='f in Cc^infty(R), compactly supported', source=MET, corpus=REF))

    rec('')
    rec('    ### **(H2) `supp f subset [-A, A]` -- COMPACT SUPPORT AT A NAMED WIDTH.**')
    rec('      ### GRADING (i) : ### **%s.** ### It is the source\'s own restriction.' % MET)
    rec('      ### GRADING (ii) : ### **%s**, by construction -- every seed is built on a finite grid.' % MET)
    rec('      ### ### **AND THIS IS THE COORDINATE AT ISSUE.** ### The source states its own instance at')
    rec('      ### `supp` in `(1/2, 2)`:')
    for lbl, q in S['quotes']:
        if 'WHY THE SUPPORT IS RESTRICTED' in lbl:
            for i in range(0, len(q), 92):
                rec('        | %s' % q[i:i + 92])
    show(t('b334_aimmap.py'), 'REACHING = (40.0, 81.0)',
         "and the reaching legs sit at a = 40 and 81, FAR outside the source's own interval")
    H.append(dict(id='H2', text='supp f subset [-A, A]', source=MET, corpus=MET))

    rec('')
    rec('    ### **(H3) `f^ >= 0` POINTWISE -- THE SOURCE\'S DEFINITION 3.1.**')
    rec('      ### GRADING (i) : ### **%s.** ### It is one side of the equivalence and is stated exactly.' % MET)
    rec('      ### GRADING (ii) : ### **%s**, and the corpus\'s own tool says why:' % UND)
    show(t('b318_square.py'), '### show a function is NOT positive definite by exhibiting a negative value, and it cannot prove')
    rec('        ### ### **THE TEST IS A SCAN OVER A FINITE INTERVAL IN `t`, AND `POINTWISE` MEANS ALL `t`.**')
    rec('        ### The record reports `13 of 13` passing with minima four to eight orders inside its floor,')
    rec('        ### ### **AND THAT IS A RANGE RESULT WHERE THE HYPOTHESIS IS A GLOBAL ONE.**')
    rec('        ### **NOT REFUTABLE:** nothing in the record exhibits a negative value. ### **NOT MET:** a')
    rec('        ### scan does not establish a pointwise claim, and the instrument says so itself.')
    H.append(dict(id='H3', text='f^ >= 0 pointwise (Definition 3.1)', source=MET, corpus=UND))

    rec('')
    rec("    ### **(H4) THE SOURCE'S TWO VANISHING CONDITIONS** -- Theorem 1 also asks the transform to")
    rec('    ### vanish at `i/2` and at `0`; the corpus tests them as part of Theorem 1\'s three conditions.')
    rec('      ### GRADING (i) : ### **%s.** ### They are exact conditions defining an ideal:' % MET)
    for lbl, q in S['quotes']:
        if 'IDEAL' in lbl:
            for i in range(0, len(q), 92):
                rec('        | %s' % q[i:i + 92])
    rec('      ### GRADING (ii) : ### **%s.**' % TOL)
    show(d('b320_the_lawful_function.txt'), "### ### **(1c) THEOREM 1's THREE CONDITIONS, PER CELL.**",
         'the measured values run at 1e-16 and 1e-17, which is a number against a bar and not a vanishing')
    rec('        ### ### **THE CONDITIONS AS STATED ARE EXACT AND THE RECORD MEETS THEM AS NUMBERS.** ###')
    rec('        ### That is the sealed status `%s`, and it is NOT `%s`.' % (TOL, MET))
    H.append(dict(id='H4', text='transform vanishes at i/2 and 0', source=MET, corpus=TOL))

    # ================================================================= (3) THE VERDICT.
    rec('')
    rec('-' * 100)
    rec("  ### (3) THE VERDICT, BY THE SEALED BRANCH RULE OF SECTION (D).")
    rec('-' * 100)
    rec('    %-4s %-42s %-22s %s' % ('', 'hypothesis', 'grading (i) SOURCE', 'grading (ii) CORPUS'))
    for h in H:
        rec('    %-4s %-42s %-22s %s' % (h['id'], h['text'][:42], h['source'], h['corpus']))
    fail_i = [h['id'] for h in H if h['source'] in (REF,)]
    all_i = all(h['source'] == MET for h in H)
    rec('')
    rec('    ### **(EXISTS BUT DOES NOT APPLY) -- UNREACHABLE, AND SHOWN SO.** ### It is taken when a')
    rec('      hypothesis FAILS FOR THE SOURCE\'S OWN CLASS. ### Failing hypotheses in grading (i) : %s'
        % (fail_i if fail_i else 'NONE'))
    rec('    ### **(NO SUCH STATEMENT LOCATED) -- UNREACHABLE, AND SHOWN SO.** ### A statement of the named')
    rec('      shape IS located, in the corpus\'s own source, quoted above and pinned by hash.')
    rec('    ### ### ### **THEREFORE: A STATEMENT EXISTS.**')
    verdict = 'A STATEMENT EXISTS' if all_i else 'EXISTS BUT DOES NOT APPLY'
    rec('')
    rec('    ### ### **AND GRADING (ii) IS REPORTED HERE AT FULL PROMINENCE, WHERE SECTION (D) PUT IT,')
    rec('    ### ### RATHER THAN BEING ALLOWED TO PICK THE BRANCH:**')
    rec('    ### ### **AGAINST THE CORPUS\'S CONSTRUCTED OBJECTS, ONE HYPOTHESIS IS REFUTABLE, ONE IS')
    rec('    ### ### UNDECIDABLE FROM THE RECORD, ONE IS MET ONLY TO A MEASURED TOLERANCE, AND ONE IS MET.**')
    rec('    ### **A DEFECT IN THE CORPUS\'S NUMERICS IS A FACT ABOUT THE CORPUS AND NOT ABOUT WHETHER THE')
    rec('    ### LITERATURE CARRIES THE STATEMENT** -- and both facts are in this act, labelled.')

    # ================================================================= (4) WHY IT DOES NOT CLOSE THE WIDTH.
    rec('')
    rec('-' * 100)
    rec('  ### (4) AND IT DOES NOT CLOSE THE WIDTH COORDINATE. ### **THE ACT\'S CENTRAL FINDING.**')
    rec('-' * 100)
    rec('    ### ### **THE LOCATED STATEMENT IS INDEXED BY `A`, AND EVERY CONCLUSION IT GIVES IS AT THAT')
    rec('    ### ### SAME `A`.** ### It carries the seed family at `A/2` onto the admissible class at `A`.')
    rec('    ### ### **IT SAYS NOTHING WHATEVER ABOUT PASSING FROM ONE `A` TO A LARGER ONE.**')
    rec('    ### And the criterion it serves quantifies over the union of ALL supports:')
    for lbl, q in S['quotes']:
        if 'RH CRITERION' in lbl:
            for i in range(0, len(q), 92):
                rec('      | %s' % q[i:i + 92])
    rec('    ### ### **SO THE CLASS THE ORDER CALLS "the whole admissible class" IS A UNION OVER THE WIDTH')
    rec('    ### ### COORDINATE, AND THE LOCATED STATEMENT IS A FAMILY OF STATEMENTS INDEXED BY IT.**')
    rec('    ### ### **AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS.**')
    rec('')
    rec('    ### **AND THE SEARCH FOR THE CROSSING STATEMENT, RECORDED, INCLUDING WHAT IT DID NOT FIND:**')
    for what, res in S['misses']:
        rec('      - %s' % what)
        rec('        -> %s' % res)
    rec('    ### ### **THAT IS AN ABSENCE OF READING AND NOT AN ABSENCE OF LITERATURE.** ### One source was')
    rec('    ### ### read at content; two web searches were run; one publisher copy refused the fetch. ###')
    rec('    ### ### **NOTHING HERE SAYS THE LITERATURE CARRIES NO SUCH STATEMENT.**')

    # ================================================================= (5) THE PRICE.
    rec('')
    rec('-' * 100)
    rec('  ### (5) WHAT CLOSING THE WIDTH COORDINATE WOULD REQUIRE, PRICED AND NOT ATTEMPTED.')
    rec('-' * 100)
    rec('    ### ### **THE MISSING STATEMENT, TYPED AS A SENTENCE THAT WOULD HAVE TO BE TRUE:**')
    missing = ('there is a bound on the Weil functional over the admissible class at support A that is '
               'UNIFORM IN A -- or an argument that non-negativity at every finite A implies it on the '
               'union over all A')
    rec('      "%s."' % missing)
    rec('    ### ### **AND WHY THE SECOND HALF IS NOT AUTOMATIC**, said plainly because it looks as if it')
    rec('    ### ### should be: the union is an increasing union, and non-negativity of a functional on each')
    rec('    ### ### member of an increasing family DOES give it on the union ### **IF THE FUNCTIONAL IS THE')
    rec('    ### ### SAME FUNCTIONAL ON EACH.** ### The record does not establish that the object it')
    rec('    ### ### evaluates at `a = 40` is the same functional it evaluates at `a = 1.41`; b334 measured')
    rec('    ### ### that the square and the remainder are ### **NOT REACHED** ### at the reaching widths.')
    rec('    ### ### **SO THE MISSING STATEMENT IS NOT A LIMIT ARGUMENT ANYONE HAS DECLINED TO WRITE. ### IT')
    rec('    ### ### IS A STATEMENT ABOUT AN INSTRUMENT THAT DOES NOT REACH.**')
    rec('')
    rec('    ### ### **THE PRICE, IN THE ONLY UNIT THIS ACT CAN HONESTLY OFFER:**')
    rec('      ### **THE LOCATED HALF COSTS NOTHING FURTHER.** ### Boas-Kac is banked in the corpus\'s own')
    rec('      ### source; the corpus already builds its `f` as `g * g^#`, so it is already inside the')
    rec('      ### family the equivalence names, at every covered cell.')
    rec('      ### **THE CROSSING HALF IS UNPRICEABLE FROM BANKED FIGURES.** ### There is no rung, box,')
    rec('      ### cell, frame or aim in the record whose count would scale to it, because ### **THE WORK IT')
    rec('      ### NAMES IS A PROOF AND NOT A RUN.** ### An act that priced it in seconds would be pricing')
    rec('      ### a computation nobody has proposed.')
    rec('      ### **AND PRICING THE PRICING IS UNPRICEABLE TOO**, for the same reason, and the act says so')
    rec('      ### rather than manufacture a number. ### b350 priced a pricing where the record printed a')
    rec('      ### ladder; here the record prints nothing of the kind.')
    rec('    ### ### **IT IS NOT ATTEMPTED. ### THE CEILING FORBIDS IT AND THE ACT DOES NOT WANT TO.**')

    # ================================================================= (6) THE COVERAGE CLASS.
    rec('')
    rec('-' * 100)
    rec('  ### (6) THE COVERAGE CLASS, FILED BESIDE THE VERDICT AND NOT INSIDE IT.')
    rec('-' * 100)
    rec('    ### ### **THE PHASE COORDINATE\'S VANISHING-TRANSFORM CLASS IS A COVERAGE CLASS, NOT A FAILURE')
    rec('    ### ### CLASS.** ### A failure class is a way the margin could fail; a coverage class is a')
    rec('    ### region the instrument does not report on. ### When the seed\'s transform vanishes the')
    rec('    ### quadruple\'s term is zero whatever the angle is and the angle is undefined, so the sign')
    rec('    ### condition ### **DOES NOT REPORT ON IT AT ALL** -- which is silence, not a negative reading.')
    rec('    ### **b349\'s OWN WORDS ON EXACTLY THIS CLASS, FROM THE ACT THAT LOOKED FOR IT:**')
    show(d('b349_the_room_relative.txt'), '### ### NEVER DEGENERATES -- IT MEANS THESE THREE DID NOT.**')
    show(d('b349_the_room_relative.txt'), '### ### DEGENERATE.** ### The window is')
    rec('    ### ### **FILING IT AS A FAILURE CLASS WOULD BE A CLAIM THE RECORD DOES NOT HOLD.** ### Filing')
    rec('    ### ### it as nothing would lose the one class the phase coordinate\'s algebra cannot see.')

    # ================================================================= (7) THE IMPORT BAR, DISCHARGED.
    rec('')
    rec('-' * 100)
    rec('  ### (7) THE IMPORT BAR, DISCHARGED.')
    rec('-' * 100)
    rec('    ### the located statement (Boas-Kac, as Proposition 2 of the pinned source) : ### **%s**'
        % src['grade'])
    rec('    ### is an internal verification TOOL-REACHABLE? ### **NO, AND THE REASON IS NOT SHYNESS:**')
    rec('    ### verifying it internally means proving a factorisation theorem, and ### **THIS ACT MAY')
    rec('    ### CONSTRUCT NO ARGUMENT.** ### No work-order is opened, and the bar asks for one only where')
    rec('    ### an internal verification is tool-reachable.')
    rec('    ### ### **WHAT WOULD BE TOOL-REACHABLE AND IS NOT A VERIFICATION:** ### checking that a corpus')
    rec('    ### ### `f` passing Definition 3.1 factors as `g * g^#` with a `g` of half the support. ###')
    rec('    ### ### **THAT WOULD BE CIRCULAR HERE**, because the corpus BUILDS its `f` as `g * g^#` by')
    rec('    ### ### construction; the check would confirm the construction and say nothing about Boas-Kac.')
    rec('    ### ### **SO IT IS NOT OFFERED AS A BENCH VERIFICATION**, and naming why is the point.')

    # ================================================================= (8) EXPECTATIONS.
    rec('')
    rec('-' * 100)
    rec('  ### (8) BOTH SEATS\' EXPECTATIONS, SCORED.')
    rec('-' * 100)
    und = [h['id'] for h in H if h['corpus'] == UND]
    rec("    ### **THE NAVIGATOR'S (L2)** -- a statement exists in the literature and at least one hypothesis")
    rec('    ### is undecidable from the record : ### **MET, BOTH HALVES.** ### The statement exists and is')
    rec('    ### the corpus\'s own source\'s Proposition 2; and %s is `%s`, because the corpus\'s'
        % (', '.join(und), UND))
    rec('    ### positive-definiteness test is a scan over a finite interval where the hypothesis is')
    rec('    ### pointwise. ### **AND MORE THAN THE EXPECTATION ASKED:** one hypothesis is also `%s`' % REF)
    rec('    ### against the objects as constructed, and one is met only to a measured tolerance.')
    rec("    ### **THIS SEAT'S** -- whatever is located will be indexed by the support and will give an")
    rec('    ### exhaustion AT a width rather than a passage BETWEEN widths : ### **MET.** ### `Proposition')
    rec('    ### 2` is indexed by `A` and concludes at `A`; the width coordinate survives it intact.')

    rec('')
    rec('=' * 100)
    rec('  VERDICT : ### **%s**' % verdict)
    rec('  ### ### **AND WHAT IT IS NOT: ### THE WIDTH COORDINATE IS NOT CLOSED BY THIS ACT. ### NO CLASS IS')
    rec('  ### ### PROVED OR SPANNED. ### THE PARTITION b351 LEFT `UNDECIDED` STAYS `UNDECIDED`. ### THE')
    rec('  ### ### CLAUSE HAS NOT MOVED.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b353_read_run', LINES)
    io.open(d('b353_read.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(hypotheses=H, verdict=verdict, statuses=list(STATUSES), source=src,
             missing=missing, undecidable=und, refutable=[h['id'] for h in H if h['corpus'] == REF],
             tolerance=[h['id'] for h in H if h['corpus'] == TOL],
             grading_i_all_met=bool(all_i), grading_i_failures=fail_i,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
