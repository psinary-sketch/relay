# -*- coding: utf-8 -*-
"""b361_read.py -- THE QUOTATION STEP, THE BRANCH TEST, AND THE DECISION OR THE HALT.

### ### **NO SCANNER INFERS A JUDGEMENT FROM PROSE HERE.** ### `b357`'s incident is the reason: an act
### whose subject was a check that confirms rather than tests built one, by grepping its own commentary
### for a word. ### **SO THE BRANCH IS DECLARED DATA, STATED LINE BY LINE BY THIS SEAT**, with every
### quotation it rests on located by the anchor tool and printed beside it. ### The tool's job is to make
### the chain visible and to REFUSE when a link is missing, not to decide.
### ### **AND ONE THING THIS FILE COMPUTES, AND ONLY ONE:** ### the square of a value the identification
### produces. ### Everything else is a quotation or a declared judgement.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


B358 = d('b358_the_li_asymptotics.txt')
DRAFT = d('b360_closing.txt')
SRC = d('b358_source_lagarias0404394.txt')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def q(path, hint):
    """### THE ANCHOR, READ FROM THE FILE. ### **RAISES RATHER THAN GUESSING.**"""
    n, line = AF.find(path, hint)
    return n, line.rstrip()


def show(label, path, hint, indent='      '):
    n, line = q(path, hint)
    rec('%s%s' % (indent, label))
    rec('%s  %s : line %d' % (indent, os.path.basename(path), n))
    rec('%s  | %s' % (indent, line[:190]))
    return n, line


def main():
    rec('=' * 100)
    rec('b361 -- THE HELD ITEM, QUOTED THEN BRANCHED.')
    rec('=' * 100)

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec("  ### (a) THE FOUR OBJECTS THE ORDER NAMES, EACH LOCATED AT ITS OWN FILE.")
    rec('-' * 100)
    rec('')
    rec('  ### **(1) THE ITEM.**')
    show('the item, given its own sentence by the act that raised it:', B358,
         'H-NGEK` DESERVES ITS OWN SENTENCE.')
    show('and the constant, with where its determinant sits:', B358,
         '`K(\u03c0) = max_j |\u03ba_j(\u03c0)|\u00b2`, and the corpus HAS the gamma factor that determines')
    show('and the sentence that made it a candidate at all:', B358,
         'it, and ### **ONE EVALUATION WOULD DECIDE IT.** ### That is named here and is NOT ordered.')
    rec('')
    rec("  ### **(2) ITS GRADE, AS ITS OWN ACT LEFT IT.** ### **NOT AS THIS ACT WOULD PHRASE IT.**")
    show("the axis-2 counts, in b358's own words:", B358,
         "ON AXIS 2, AGAINST THE CORPUS'S OWN OBJECTS: `MET` 3")
    show('the axis-1 counts beside them:', B358, 'ON AXIS 1, AGAINST THE SOURCES')
    show('the class the item sits in:', B358, 'THE FIVE THAT ARE `UNDECIDABLE-FROM-THE-RECORD`')
    show('and the item named inside it, with the reason:', B358,
         'refute it; and ### `H-NGEK` is the interesting one')
    rec('')
    rec('      ### ### **SO THE GRADE, AS ITS OWN ACT LEFT IT: ### `UNDECIDABLE-FROM-THE-RECORD` ON THE')
    rec('      ### ### CORPUS AXIS, AND `MET` ON THE SOURCE AXIS** -- and b358 fixed what `MET` means')
    rec('      ### there: that the source uses the hypothesis consistently in its own setting, NOT that it')
    rec('      ### holds. ### **THE TWO GRADES ARE NEVER MERGED AND THIS ACT DOES NOT MERGE THEM.**')
    rec('')
    rec('  ### **(3) THE CAP CLAUSE THAT FORBADE DECIDING IT.**')
    show('the clause, at the same bank:', B358,
         'THE RECORD ALREADY HOLDS. ### DETERMINED IS NOT COMPUTED**, the cap forbids this act')
    rec('')
    rec("  ### **(4) THE SENTENCE CLAIMING IT LIES OUTSIDE THE PARKING RULING.**")
    rec('      ### ### **IT IS THIS SEAT\'S OWN, WRITTEN IN A DRAFT, AND IT IS QUOTED AS A DRAFT\'S CLAIM')
    rec('      ### ### AND NOT AS A RULING.**')
    show('the draft names the item:', DRAFT, 'b361 -- `H-NGEK` DECIDED. ### **ONE EVALUATION')
    show('and claims it lies outside the parking:', DRAFT,
         'the record already holds, ### **AND IT IS NOT AN INSTRUMENT RUN** -- no frame')

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### (b) THE BRANCH TEST, APPLIED TO THE QUOTED TEXT. ### **DECLARED DATA, NOT INFERRED.**')
    rec('-' * 100)
    tests = [
        ('does deciding it build or recompute an instrument frame', False,
         'the item is a constant in a source theorem; no frame appears in its statement'),
        ('does it run a ladder', False, 'no ladder appears in its statement'),
        ('does it move a quadrature axis', False, 'no axis appears in its statement'),
        ('does it evaluate a transform, a quadrature, a fit or a series', False,
         'the constant is a maximum of squared moduli of parameters read off a factorization'),
        ('does it require a new measurement', False,
         'every quantity it needs is displayed in the pinned source'),
        ('is it a bounded evaluation of a NAMED constant', True,
         '`K(pi)` is named and defined by (5.3) in the pinned source'),
    ]
    for what, val, why in tests:
        rec('    %-62s : %-5s   %s' % (what, val, why))
    branch = 'A' if (not any(v for _w, v, _y in tests[:5]) and tests[5][1]) else 'B'
    rec('')
    rec('    ### ### **BRANCH TAKEN : %s -- %s**' % (branch, 'DECIDE' if branch == 'A' else 'HALT'))
    rec('    ### **AND THE OTHER BRANCH IS SHOWN UNREACHABLE RATHER THAN LEFT UNCLAIMED:** ### branch B is')
    rec('    ### taken only when the item needs a frame, a measurement, or something the parking ruling')
    rec('    ### covers. ### **NONE OF THE FIVE IS TRUE OF THE QUOTED ITEM**, so branch B fails its own')
    rec('    ### condition.')
    rec('    ### ### **AND THE DRAFT\'S CLAIM IS TESTED RATHER THAN INHERITED:** ### the draft said the')
    rec('    ### item is not an instrument run. ### **THIS ACT AGREES, AND IT AGREES ON THE QUOTED TEXT')
    rec('    ### AND NOT ON THE DRAFT\'S SAY-SO** -- the five tests above are read off the item\'s own')
    rec('    ### sentence, which names a constant and a maximum and nothing else.')
    if branch != 'A':
        rec('')
        rec('  ### HALTED. ### NOTHING IS DECIDED.')
        p = run_clock.write(D, 'b361_read', LINES)
        return 0

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### BAR 2 -- THE DEFINITION, LOCATED AT CONTENT IN THE PINNED SOURCE. ### **OR NO EVALUATION.**')
    rec('-' * 100)
    links = [
        ('(2.1) the Euler product factorization', '\u039b(s,\u03c0 ) := Q(\u03c0)'),
        ('(2.2) the archimedean factor', '\u0393 R(s +\u03baj(\u03c0)), (2.2)'),
        ('(2.2) and what the kappa are', 'in which \u03baj(\u03c0) are certain constants and'),
        ('(2.3) Gamma_R itself', '\u0393 R(s) := \u03c0\u2212 s'),
        ('(5.3) the constant, defined', 'K(\u03c0) = max'),
        ('(5.3) and the quantity it maximises', '|\u03baj(\u03c0)|2, (5.3)'),
        ('the same definition restated inside the proof',
         'Now we suppose that n \u2265K(\u03c0) := max {|\u03bak(\u03c0)|2 : 1 \u2264k \u2264N }'),
    ]
    for label, hint in links:
        show(label, SRC, hint)
    rec('')
    rec('    ### ### **BAR 2 : THE DEFINITION IS LOCATED AT CONTENT AND QUOTED. ### THE EVALUATION MAY')
    rec('    ### ### PROCEED.**')

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec("  ### THE CORPUS'S OBJECT INSIDE THE SOURCE'S OWN NOTATION, AND WHAT THE SOURCE STATES OF IT.")
    rec('-' * 100)
    for label, hint in [
        ("the source's own completed L-function for the trivial representation",
         '\u039b(s,\u03c0 triv ) = \u03c0\u2212 s'),
        ('and the line that finishes it, and marks it the one exception',
         '2 )\u03b6(s). This function has simple poles at s = 0 and s = 1.'),
        ('the conductor, STATED by the source and not inferred', 'using Q(\u03c0triv) = 1.'),
    ]:
        show(label, SRC, hint)

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### THE ROUTE, PRINTED STEP BY STEP. ### **AN IDENTIFICATION OF TWO QUOTED FORMULAE, AND ONE')
    rec('  ### PIECE OF ARITHMETIC.**')
    rec('-' * 100)
    src_text = io.open(SRC, encoding='utf-8', errors='replace').read()
    stated = [s for s in ('\u03ba1(\u03c0triv)', '\u03ba1(\u03c0 triv )', 'K(\u03c0triv)', 'K(\u03c0 triv )')
              if s in src_text]
    rec('')
    rec('    ### ### **FIRST, WHAT THE SOURCE DOES NOT SAY, BECAUSE THE ROUTE TURNS ON IT:**')
    rec('    ### the source is searched for a stated value of the trivial representation\'s archimedean')
    rec('    ### parameter or of its `K`. ### **STRINGS FOUND : %d %s**' % (len(stated), stated or ''))
    rec('    ### ### **SO THE VALUE IS NOT QUOTED FROM THE SOURCE. ### IT IS IDENTIFIED FROM TWO OF THE')
    rec('    ### ### SOURCE\'S OWN DISPLAYED FORMULAE, AND THIS ACT SAYS SO RATHER THAN LETTING A PINNED')
    rec('    ### ### CITATION CARRY A VALUE THE SOURCE NEVER WRITES.**')
    rec('')
    rec('    STEP 1  N = 1, because the representation is on GL(1) -- the source\'s own words at the')
    rec('            trivial-representation line above.')
    rec('    STEP 2  (2.1) at that representation, with Q = 1 STATED by the source:')
    rec('                Lambda(s, pi_triv)  =  L_inf(s, pi_triv) . zeta(s)')
    rec('            and the source states Lambda(s, pi_triv) = pi^(-s/2) Gamma(s/2) . zeta(s).')
    rec('    STEP 3  so  L_inf(s, pi_triv)  =  pi^(-s/2) Gamma(s/2)  =  Gamma_R(s)  by (2.3).')
    rec('    STEP 4  and (2.2) at N = 1 says  L_inf(s, pi_triv) = Gamma_R(s + kappa_1).')
    rec('    STEP 5  ### **THE IDENTIFICATION:** ### Gamma_R(s + kappa_1) = Gamma_R(s) as meromorphic')
    rec('            functions of s, so the two have the same poles, and the shift is zero:')
    rec('                kappa_1(pi_triv) = 0.')
    kappa = 0
    K = abs(kappa) ** 2
    rec('    STEP 6  ### **THE ONE PIECE OF ARITHMETIC IN THIS ACT**, by (5.3) at N = 1:')
    rec('                K(pi_triv) = max_j |kappa_j|^2 = |%d|^2 = %d' % (kappa, K))
    rec('')
    rec('    ### ### ### **SO THE INDEX CONDITION OF THEOREM 5.1 READS `n >= 0` FOR THE CORPUS\'S OBJECT,')
    rec('    ### ### ### AND IS SATISFIED AT EVERY INDEX THE CORPUS COMPUTES.**')
    rec('    ### **AND THE ERROR TERM COLLAPSES WITH IT:** ### (5.1) carries `O(N(K(pi)+1))`, which at')
    rec('    ### `N = 1` and `K = 0` is `O(1)` -- with the implied constant ABSOLUTE, which is the half')
    rec('    ### that distinguishes (5.1) from the introduction\'s (1.12).')

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### BAR 3 -- WHAT THIS ROUTE IS DEAF TO. ### **PRINTED, NOT IMPLIED.**')
    rec('-' * 100)
    for label, hint in [
        ("Theorem 5.1's own hypothesis, which the corpus's object does not satisfy as written",
         'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
        ('and the grade that question already carries, which is b358\'s and is NOT disturbed here',
         '`H-CUSP` (`\u03c0` cuspidal on `GL(N)`): the corpus'),
    ]:
        show(label, B358 if 'H-CUSP' in hint else SRC, hint)
    rec('')
    rec('    ### ### **(i) THE ROUTE INHERITS `H-CUSP` AND DOES NOT DECIDE IT.** ### Theorem 5.1 is stated')
    rec('    ### for an IRREDUCIBLE CUSPIDAL representation, and the trivial representation of GL(1) is')
    rec('    ### the one the source itself marks as the exception -- it is the only one whose completed')
    rec('    ### L-function is not entire. ### **THE SOURCE APPLIES ITS OWN RESULTS TO IT ANYWAY, UNDER A')
    rec('    ### ### STATED CONVENTION**, and `b358` graded that question `MET` on the corpus axis. ###')
    rec('    ### **THIS ACT STANDS ON THAT GRADE AND CONFERS NONE.** ### If `H-CUSP` were ever regraded,')
    rec('    ### this decision would move with it.')
    rec('    ### ### **(ii) IT IS DEAF TO ANY CONVENTION UNDER WHICH THE SOURCE MEANS SOMETHING ELSE BY')
    rec('    ### ### `L_inf` FOR THIS REPRESENTATION.** ### The identification reads (2.1)-(2.3) as')
    rec('    ### applying verbatim to `pi_triv`; the source displays `Lambda(s, pi_triv)` in exactly that')
    rec('    ### shape, which is why the reading is available -- and it is a reading.')
    rec('    ### ### **(iii) IT IS DEAF TO THE RENDERING.** ### The quotations come from text extracted')
    rec('    ### from the pinned PDF, and no bar in this act checks a transcription against the typeset')
    rec('    ### original. ### That is `b353`\'s seam and it stands.')
    rec('    ### ### **(iv) AND IT DECIDES AN INDEX CONDITION AND NOTHING ELSE.** ### The tail is closed')
    rec('    ### by the ZERO channel, which has no unconditional bound at all. ### **NOTHING HERE MOVES')
    rec('    ### THE TAIL, AND THE CIRCULARITY FINDING STANDS EXACTLY WHERE `b358` LEFT IT.**')

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### THE THING NO SEAT WROTE DOWN, AND THE READING FOUND ANYWAY.')
    rec('-' * 100)
    for label, hint in [
        ("the source's INTRODUCTION already states the asymptotic for every index", 'that for all n \u2265 1,'),
        ('with this error term', '2n logn +C1(\u03c0) n +O (1), (1.12)'),
        ('### and THIS implied constant DEPENDS ON pi', 'and the implied constant in the O(1) term depends on \u03c0. Here'),
        ('against the theorem\'s error term', 'n logn +C1(\u03c0) n +O (N (K(\u03c0) + 1)). (5.1)'),
        ('### whose implied constant is ABSOLUTE', 'and the implied constant in the O-notation is absolute.'),
    ]:
        show(label, SRC, hint)
    rec('')
    rec('    ### ### ### **SO THE SOURCE ALWAYS HELD TWO STATEMENTS, AND THE INDEX CONDITION BELONGS TO')
    rec('    ### ### ### ONLY ONE OF THEM.** ### `(1.12)` holds for every `n >= 1` and pays for it with a')
    rec('    ### constant that depends on the representation; `(5.1)` has an ABSOLUTE constant and pays')
    rec('    ### for it with the condition `n >= K(pi)`. ### **THE QUESTION `H-NGEK` ASKS WAS NEVER')
    rec('    ### ### WHETHER THE ASYMPTOTIC HOLDS. ### IT WAS WHETHER THE ABSOLUTE-CONSTANT VERSION HOLDS')
    rec('    ### ### EVERYWHERE**, and for the corpus\'s object it does, because the condition is vacuous.')
    rec('    ### **AND NOBODY HAD PUT THE TWO STATEMENTS SIDE BY SIDE**, including `b358`, which quoted')
    rec('    ### `(5.1)` and not `(1.12)`.')

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### DOES THE DECISION MOVE THE ROW? ### **DECLARED DATA, WITH THE ROW\'S OWN SENTENCE QUOTED.**')
    rec('-' * 100)
    show("the row this act's result bears on, and where b358 and b359 put the tail finding:", FACES,
         'THE COUNTABLE FACE')
    rec('')
    rec('    ### **THE TEST, AS THE LOCKED REGISTRATION FIXED IT:** ### the row moves when this act\'s')
    rec('    ### result changes what the row says the record holds about the hypothesis the item names.')
    rec('    ### **THE ROW SAYS THE ARCHIMEDEAN CHANNEL IS UNCONDITIONAL WITH AN EXPLICIT ERROR TERM,')
    rec('    ### ### `O(N(K(pi)+1))` FOR `n >= K(pi)`, WITH THE IMPLIED CONSTANT ABSOLUTE.**')
    rec('    ### **AFTER THIS ACT THE RECORD HOLDS TWO THINGS THE ROW DOES NOT CARRY:** ### that for the')
    rec('    ### corpus\'s object the index condition is VACUOUS, and that the error term is therefore')
    rec('    ### `O(1)` with an absolute constant.')
    moves = True
    rec('    ### ### **SO THE ROW MOVES : %s**, by an APPENDED UPDATE BLOCK through the ledger\'s own'
        % moves)
    rec('    ### writer, naming the row it bears on. ### **NO ROW ABOVE IS EDITED AND NO GRADE IS')
    rec('    ### CONFERRED: `NAMED-ONLY` STANDS**, because a vacuous index condition establishes nothing')
    rec('    ### that could lift a naming -- the tail is still closed by the channel that has no')
    rec('    ### unconditional bound.')
    rec('    ### ### **AND THIS REFUTES THE NAVIGATOR\'S SECOND CLAUSE, WHICH IS WHAT AN EXPECTATION IS')
    rec('    ### ### FOR.**')

    rec('')
    rec('=' * 100)
    rec('  ### ### **VERDICT: DECIDED.** ### `K(pi_triv) = 0`; the index condition of Theorem 5.1 is')
    rec('  ### ### satisfied at every index the corpus computes; `H-NGEK` moves off')
    rec('  ### ### `UNDECIDABLE-FROM-THE-RECORD` on the corpus axis, at the scope printed above.')
    rec('  ### **AND WHAT IS NOT DECIDED: `H-CUSP` IS INHERITED, THE TAIL IS UNTOUCHED, THE CIRCULARITY')
    rec('  ### FINDING STANDS, AND NO GRADE IS CONFERRED BY THIS SEAT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b361_read', LINES)
    io.open(d('b361_read.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(branch=branch, verdict='DECIDED', kappa=kappa, K=K,
             value_stated_in_source=bool(stated), stated_strings=stated,
             definition_located=True, row_moves=bool(moves), row='U1',
             hypothesis_status_before='UNDECIDABLE-FROM-THE-RECORD',
             hypothesis_status_after='MET (by the criterion b358 itself fixed for that axis)',
             row_grade='NAMED-ONLY, UNCHANGED', grade_conferred_by_seat=False, inherits='H-CUSP',
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
