# -*- coding: utf-8 -*-
"""b362_read.py -- THE FIVE COMPONENTS OF LEG 2, EACH ON QUOTED TEXT.

### ### **NO SCANNER INFERS A JUDGEMENT FROM PROSE HERE** -- `b357`'s incident. ### Every classification
### below is ### **DECLARED DATA**, stated by this seat, with the quotation it rests on located by the
### anchor tool and printed beside it. ### The tool makes the chain visible and REFUSES when a link is
### missing; it does not decide.
### ### **AND IT COMPUTES NOTHING.** ### No distance is evaluated at any index, by any route, at any
### precision. ### `G-NOCOMPUTE` re-measures that on stripped code rather than trusting this docstring.
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
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b361_ferry_2026-09-07.txt')
S1 = d('b362_source_baezduarte0202141.txt')
S2 = d('b362_source_baezduarte_abs0202141.txt')
S3 = d('b362_source_burnol0103058.txt')
S5 = d('b362_source_baezduarte0205003.txt')
B321 = d('b321_the_window_opened.txt')
REG358 = d('b358_registration_2026-09-07.txt')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def show(label, path, hint, indent='      '):
    n, line = AF.find(path, hint)
    rec('%s%s' % (indent, label))
    rec('%s  %s : line %d' % (indent, os.path.basename(path), n))
    rec('%s  | %s' % (indent, line.rstrip()[:190]))
    return n, line.rstrip()


def head(t):
    rec('')
    rec('-' * 100)
    rec('  %s' % t)
    rec('-' * 100)


def main():
    rec('=' * 100)
    rec('b362 -- THE APPROXIMATION REGISTER, READ UNDER A CAP.')
    rec('=' * 100)

    # ================================================================================================
    head("### (i) THE STATEMENT. ### **THE HINT IS QUOTED FIRST, SO A READER SEES WHAT WAS SEARCHED ON.**")
    rec('  ### **THE HINT, AND ITS OWN PROVENANCE, AT THE BANKED FERRY:**')
    show('the order says where the hint comes from:', FERRY,
         'from recall and NOT from any file, that the hypothesis has a')
    show('the hint itself:', FERRY, 'Nyman\u2013Beurling criterion, that a fixed function lies in the')
    show('and the variant it names:', FERRY, 'sequence of distances tends to zero \u2014 with a variant due to')
    rec('')
    rec('  ### **THE STATEMENTS, LOCATED AT PINNED SOURCES, WITH THEIR HYPOTHESES UNFOLDED ONE BY ONE.**')
    rec('')
    rec('  ### ### **THE CLASSICAL CRITERION.** ### Its setting first, then the statement:')
    show('the setting, and what the letters are:', S3,
         'The context in which our construction takes place is that of t he Nyman-Beurling formulation')
    show('the family, and the parameter range it is taken over:', S3,
         'of K consisting of the \ufb01nite linear combinations of the function s t')
    show('and the criterion itself, as a theorem, attributed:', S3,
         'Theorem 1.1 (Nyman [14], Beurling [3]) The Riemann Hypothesis holds if and only if')
    rec('')
    rec('      ### **THE HYPOTHESES, UNFOLDED FROM THE SOURCE\u2019S OWN TEXT:**')
    for h in ('(H1) the space is `K = L2(]0, inf[, dt)`, over the complex numbers;',
              '(H2) `chi` is the indicator function of the interval `]0, 1]`;',
              '(H3) `rho` is the fractional part;',
              '(H4) `B_lambda` is the FINITE linear combinations of `t -> rho(theta/t)` for `lambda <= theta <= 1`;',
              '(H5) the parameter satisfies `0 < lambda < 1`;',
              '(H6) and the criterion is over the UNION of the `B_lambda`, closed.'):
        rec('        %s' % h)
    rec('')
    rec('  ### ### **THE VARIANT THE HINT NAMES.** ### Its setting, its family, and its theorem:')
    show('the letters, at the second source:', S1,
         'We denote the fractional part of x by \u03c1(x) = x \u2212 [x], and let \u03c7 stand')
    show('the space:', S1, 'where the main object of interest is the subspace of Beurling functions ,')
    show('the family, over a REAL parameter:', S1,
         'de\ufb01ned as the linear hull of the family {\u03c1a|1 \u2264 a \u2208 R} with')
    show('the restriction that makes the variant:', S1,
         'The much smaller subspace Bnat of natural Beurling functions is generated')
    show('and the theorem:', S1, 'Theorem 1.1. The Riemann hypothesis is equivalent to the statement that')
    show('the same statement on a second, independent surface:', S2,
         'By the Nyman-Beurling criterion the Riemann hypothesis is equivalent to the statement')
    rec('')
    rec('  ### ### **AND THE ONE THING THE SOURCE SAYS THAT THE HINT DOES NOT:**')
    show('the criterion is quoted in a MODIFIED form, and the original is a different space:', S1,
         'Nyman-Beurling criterion ([13], [6]) states, in a slig htly')
    show('the caveat itself:', S1,
         'modi\ufb01ed form [4] (the original formulation is related to L2(0, 1)), that the')
    rec('')
    hint_status = 'CONFIRMED, WITH ONE CORRECTION'
    rec('  ### ### ### **THE HINT: %s.**' % hint_status)
    rec('  ### **CONFIRMED, CLAUSE BY CLAUSE:** ### a fixed function -- the indicator of an interval;')
    rec('  ### the closed span of a family of dilations -- the linear hull of `rho(theta/t)` over a range')
    rec('  ### of `theta`; the equivalence to the hypothesis -- stated as a theorem at both sources; and')
    rec('  ### **THE VARIANT DUE TO THE AUTHOR THE HINT NAMES, RESTRICTING THE FAMILY** -- from a real')
    rec('  ### parameter to the naturals, which is exactly what the hint said it does.')
    rec('  ### ### **THE CORRECTION, QUOTED AND NOT PARAPHRASED:** ### the located statements are set in')
    rec('  ### `L2(0, inf)`, and the source itself flags that this is a MODIFIED form -- *"the original')
    rec('  ### formulation is related to L2(0, 1)"*. ### **THE HINT NAMED NO SPACE, AND THE TWO SPACES ARE')
    rec('  ### ### NOT THE SAME OBJECT**, so the record carries which one it holds rather than which one a')
    rec('  ### recollection meant.')
    rec('  ### ### **AND THIS IS NOT A CRITICISM.** ### A recollection that omits a side condition is a')
    rec('  ### recollection; the act quotes the source and moves on.')

    # ================================================================================================
    head('### (ii) THE STRUCTURAL QUESTION. ### **DECIDED FROM THE QUOTED STATEMENTS, NOT FROM THE HINT.**')
    show('the quantity a finite instance computes, defined as an infimum over the family:', S3,
         'the Hilbert-space distance inff \u2208B \u03bb \u2016\u03c7 \u2212f \u2016. We have')
    rec('')
    tests = [
        ('does the quantity\u2019s definition mention the zeros of the function', False,
         'it is a Hilbert-space distance from an indicator to a span of dilations of the fractional part'),
        ('does it mention any hypothesis about them', False, 'no hypothesis appears in the definition'),
        ('is the finite object an infimum over a SUBSET of the family', True,
         'a finite span of the `rho_a` sits inside `B_lambda` for `lambda` at or below the smallest step'),
    ]
    for what, val, why in tests:
        rec('    %-62s : %-5s   %s' % (what, val, why))
    unconditional = (not tests[0][1]) and (not tests[1][1]) and tests[2][1]
    rec('')
    rec('    ### ### ### **SO A FINITE INSTANCE IS AN UNCONDITIONAL UPPER BOUND : %s**' % unconditional)
    rec('    ### **AND THE REASON IS ONE LINE AND IT IS STRUCTURAL:** ### an infimum over a subset is at')
    rec('    ### least the infimum over the whole, so EXHIBITING ANY MEMBER OF THE FINITE SPAN BOUNDS THE')
    rec('    ### DISTANCE ABOVE. ### **THE FINITE COMPUTATION CONSULTS NO ZEROS AND INHERITS NO SIGN**;')
    rec('    ### it is not an approximation TO the quantity of interest, it is a BOUND ON it.')
    rec('    ### ### **AND THE TWO OBJECTS ARE KEPT APART, AS THE LOCKED FACE REQUIRED:** ### the finite')
    rec('    ### instance is unconditional; ### **THE CRITERION IT SERVES IS AN EQUIVALENCE WHOSE PROOF IS')
    rec('    ### ### ANOTHER MATTER ENTIRELY**, and this act verifies no proof and may not.')
    rec('')
    rec('  ### ### **THE SHORTFALL COMPARISON THE ORDER DEMANDS, AND BOTH HALVES OF IT.**')
    show('the shortfall the window act found, in its own words:', B321,
         '### ### OWN DISTANCE FROM THE ANSWER**, and reporting this control as having settled the exponent')
    rec('')
    rec('    ### ### **THIS REGISTER DOES NOT CARRY THAT SHORTFALL, AND THE REASON IS STRUCTURAL AND NOT')
    rec('    ### ### CIRCUMSTANTIAL.** ### The window act\u2019s instrument stood at a DISTANCE from the exact')
    rec('    ### statement, and that distance was larger than the difference it was asked to resolve. ###')
    rec('    ### **HERE THERE IS NO SUCH DISTANCE TO BE LARGER THAN ANYTHING**: a finite value IS a valid')
    rec('    ### bound on the exact quantity, so there is no residual between the instrument and the answer')
    rec('    ### for a signal to hide under.')
    rec('    ### ### ### **AND THE SHORTFALL IT CARRIES INSTEAD, SAID EXACTLY:** ### **THE CRITERION IS A')
    rec('    ### ### ### STATEMENT ABOUT A LIMIT, AND THE FINITE SIDE IS BOUNDED AWAY FROM ZERO AT EVERY')
    rec('    ### ### ### INDEX BY AN UNCONDITIONAL THEOREM.** ### Section (iii) quotes that theorem. ###')
    rec('    ### **SO NO FINITE COMPUTATION CAN EVER BE EVIDENCE FOR THE CRITERION\u2019S AFFIRMATIVE BRANCH**')
    rec('    ### -- not because the instrument is weak, but because the thing it computes is known in')
    rec('    ### advance to be positive at every index, and the question is only about the limit.')
    rec('    ### ### **A REGISTER WITHOUT THE SHORTFALL YOU KNOW IS NOT A REGISTER WITHOUT A SHORTFALL.**')

    # ================================================================================================
    head('### (iii) THE OBSTRUCTION. ### THE RATE, WITH THE TWO SIDES KEPT APART.')
    rec('  ### ### **THE UNCONDITIONAL SIDE -- AND IT IS A LOWER BOUND.**')
    show('the theorem, attributed to its four authors:', S3,
         'Theorem 1.2 (B\u00b4 aez-Duarte, Balazard, Landreau and Saias [2]) Let us write D(\u03bb) for')
    show('what it bounds:', S3, 'the Hilbert-space distance inff \u2208B \u03bb \u2016\u03c7 \u2212f \u2016. We have')
    show('and the improvement that counts multiplicities:', S3, 'Theorem 1.3 We have:')
    rec('')
    rec('  ### ### **THE CONDITIONAL SIDE -- AND IT IS AN UPPER BOUND. ### MARKED AT FULL PROMINENCE.**')
    show('### **UNDER THE RIEMANN HYPOTHESIS**, at the sequel:', S5,
         'second version di\ufb00ers from the \ufb01rst in showing that under the Riemann')
    show('the approximant it is achieved by:', S5, 'hypothesis the distance between \u03c7 and \u2212')
    show('and its order:', S5, 'order (log log n)\u2212')
    rec('')
    rec('  ### ### **THE CIRCULARITY CHECK, RUN AS THE LI READ RAN IT.** ### Its three questions, carried')
    rec('  ### from that act\u2019s own locked face:')
    show('question (i):', REG358,
         "**(i)** Does the statement's own hypothesis list contain the hypothesis under study, by name?")
    show('question (iii), the one that matters:', REG358,
         '**(iii)** Does the ERROR TERM -- as opposed to the main term -- depend on it, even where the main')
    rec('')
    circ = [
        ('the criterion (both forms)', 'NOT CIRCULAR',
         'the hypothesis is one SIDE of an equivalence, not an item in a hypothesis list; a criterion is a '
         'translation and not a conditional result'),
        ('the lower bound on the rate', 'NOT CIRCULAR',
         'the theorem carries no hypothesis; the source states that if the hypothesis FAILS the result is '
         'true but trivial, so the assumption in the PROOF is a case split and not a condition on the '
         'statement; and there is no error term for (iii) to bite on'),
        ('the upper bound on the rate', '### CIRCULAR AT (i) ###',
         'the statement is made *"under the Riemann hypothesis"*, in the source\u2019s own words, and is '
         'unavailable without it'),
    ]
    rec('    %-34s %-24s %s' % ('statement', 'circularity', 'why'))
    for what, verdict, why in circ:
        rec('    %-34s %-24s %s' % (what, verdict, why))
    show('and the sentence that settles the lower bound\u2019s status:', S3,
         'If the Riemann Hypothesis fails this result is true but trivi al as the left-hand side then take')
    show('with its continuation:', S3,
         'value +\u221e. So we will assume that the Riemann Hypothesis holds. The sum on the right-hand')
    rec('')
    rec('  ### ### ### **SO THE REGISTER\u2019S ASYMMETRY, STATED ONCE: ### WHAT IS UNCONDITIONAL HERE IS THE')
    rec('  ### ### ### OBSTRUCTION, AND WHAT WOULD BE PROGRESS IS CONDITIONAL.** ### The lower bound on the')
    rec('  ### distance holds whatever is true; the upper bound holds under the hypothesis.')
    rec('')
    rec('  ### ### **AND THE UNIFORMITY OBSTRUCTION: WHERE IT REAPPEARS, AND IN WHAT SHAPE.**')
    rec('  ### **IT REAPPEARS, AND IT TAKES A DIFFERENT SHAPE: A RATE.** ### What the record would hold in')
    rec('  ### this register is a family indexed by a reach -- a value of the distance at each finite reach')
    rec('  ### -- and what the criterion needs is a statement about the LIMIT of that family. ### That is')
    rec('  ### the same shape the other instances have.')
    rec('  ### ### **AND WHAT IS DIFFERENT, WHICH IS THE PART WORTH RECORDING:** ### this register')
    rec('  ### **QUANTIFIES WHAT IS MISSING.** ### The other instances say the record holds instances and needs a')
    rec('  ### class; here an unconditional theorem says HOW SLOWLY the indexed family can possibly')
    rec('  ### approach its limit. ### **A SHAPE WITH A RATE ON IT IS STILL THE SAME SHAPE**, and the rate')
    rec('  ### is what makes the finite side hopeless rather than merely incomplete.')
    rec('  ### ### ### **AND NO BRIDGE IS TYPED.** ### Nothing is claimed about the relation of this')
    rec('  ### instance to any other -- not that they are the same problem, not that discharging one would')
    rec('  ### touch another, and not that they have a common cause.')
    show("the deposit's own law, at the deposited file:", DEP,
         'while deliberately **not** compiling the cross-register equivalences, since to compile')
    # ### **THE PHRASE GOES ON ONE LINE ON PURPOSE.** ### The flattener strips markers only at the START
    # ### of a line, and these lines are indented, so a phrase broken across two of them keeps a marker in
    # ### the middle of itself and no comparison can find it. ### That is the wrapping species again, and
    # ### the cure is the emitter and not a shorter needle.
    rec('      ### **AND THE PHRASE ITSELF, PRINTED RATHER THAN LEFT INSIDE A 950-BYTE LINE:**')
    rec('      *"while deliberately **not** compiling the cross-register equivalences, since to compile '
        '\"discharge one and you discharge all five\" would be to compile RH-equivalence itself"*'
        % ())
    rec('  ### ### **THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS**, and a fourth that rhymes is a')
    rec('  ### fourth.')

    # ================================================================================================
    head('### (iv) THE PRICING. ### **NOT ATTEMPTED.**')
    rec('  ### **WHAT AN INSTRUMENT IN THIS REGISTER WOULD COMPUTE**, named from the located statements:')
    rec('    the Gram matrix of the family up to a finite reach, the inner products of the indicator')
    rec('    against each member, and the norm of the indicator -- then the distance as the residual of a')
    rec('    least-squares projection. ### **NOTHING IN THAT LIST MENTIONS A ZERO**, which is (ii)\u2019s')
    rec('    finding restated as a build.')
    rec('')
    rec('  ### **WHAT IT WOULD HAVE TO REPRODUCE BEFORE ANY NUMBER OF ITS OWN WAS TRUSTED** -- and this is')
    rec('  ### where the pricing stops:')
    rec('    ### ### **THE RECORD HOLDS NOTHING IN THIS REGISTER TO REPRODUCE.** ### No banked value, no')
    rec('    ### control, no fixture. ### The corpus has never entered it.')
    rec('    ### **SO THE CONTROL WOULD HAVE TO COME FROM THE LITERATURE, AND THE LITERATURE\u2019S NUMBERS')
    rec('    ### ARE NAMED AT A REFERENCE THIS ACT DID NOT FETCH:**')
    show('the numerical explorations, named:', S3,
         '5.5 to give the exact order of decrease of the quantity D(\u03bb) and the numerical explorations')
    show('and whose they are:', S3,
         'reported by B\u00b4 aez-Duarte, Balazard, Landreau and Saias in [ 2] seem to support this.')
    rec('    ### ### **THAT REFERENCE IS A JOURNAL ARTICLE, NOT AN ADDRESS THIS ACT FETCHED**, and nothing')
    rec('    ### from it is quoted at first hand. ### **AN ABSENCE OF READING, NOT AN ABSENCE OF')
    rec('    ### LITERATURE.**')
    rec('')
    rec('  ### **HOW A FLOOR WOULD BE TOLD FROM AN INSTRUMENT\u2019S EDGE, GIVEN A SLOWLY DECAYING QUANTITY.**')
    rec('    ### The corpus has two fresh incidents and they prescribe the answer between them: one act')
    rec('    ### could not separate a sign change from a rank saturation because both arrived at the same')
    rec('    ### step; the next separated them by MOVING A PARAMETER THAT WAS NOT THE ONE UNDER STUDY and')
    rec('    ### watching whether the value moved.')
    rec('    ### ### ### **SO THE ANSWER IS A CONTROL AND NOT A HOPE:** ### **NO VALUE IN THIS REGISTER IS')
    rec('    ### ### ### READ UNTIL IT HAS BEEN COMPUTED AT TWO SETTINGS OF A PARAMETER THE OBJECT DOES')
    rec('    ### ### ### NOT DEPEND ON, AND AGREED.** ### For a least-squares residual on a nearly')
    rec('    ### dependent family the obvious candidate is the working precision, and the corpus\u2019s own')
    rec('    ### rule follows: a bar is stated with the floor of the object it tests, or marked UNPRICED.')
    rec('    ### ### **AND WHAT THIS ACT DOES NOT ESTABLISH:** ### that the floor in this register IS the')
    rec('    ### conditioning. ### **THAT IS A GUESS ABOUT NUMERICS AND THIS ACT MEASURED NOTHING**; what')
    rec('    ### is established is the SHAPE of the control, which is the corpus\u2019s own and not this')
    rec('    ### register\u2019s.')
    rec('')
    rec('  ### ### ### **AND THE PRICING IN ACTS CANNOT BE GIVEN FROM WHAT IS LOCATED, SO THE PRICING IS')
    rec('  ### ### ### PRICED.** ### The first act in this register could not be an instrument act, because')
    rec('  ### an instrument with no control is a number with no standing. ### **THE FIRST ACT WOULD HAVE')
    rec('  ### ### TO BE A READ: locate and pin the numerical table the sources name, or establish that it')
    rec('  ### ### is not at a fetchable address.** ### That is one act, and until it is done the price of')
    rec('  ### the instrument act is unpriceable -- which is `b350`\u2019s and `b353`\u2019s move, not a new one.')

    # ================================================================================================
    head('### (v) THE VERDICT.')
    verdict = 'LOCATED BUT NOT WORTH OPENING'
    rec('  ### ### ### **%s** -- at the reach the record can afford, and the reason is quoted.' % verdict)
    rec('')
    rec('  ### **THE OTHER TWO BRANCHES, SHOWN UNREACHABLE RATHER THAN LEFT UNCLAIMED:**')
    rec('    ### **(NO USABLE STATEMENT LOCATED) -- UNREACHABLE.** ### Statements of the named shape are')
    rec('      located at pinned sources, quoted, and their hypotheses unfolded; the hint is CONFIRMED with')
    rec('      one correction. ### **THE BRANCH FAILS ITS OWN CONDITION.**')
    rec('    ### **(A REGISTER WORTH OPENING) -- UNREACHABLE, AND SHOWN SO.** ### It demands a first act')
    rec('      that can be PRICED. ### The first act cannot be priced from what is located, because the')
    rec('      only control the literature offers is at a reference this act did not fetch; and the act')
    rec('      after it would compute a quantity an unconditional theorem already bounds away from zero at')
    rec('      every reach. ### **A REGISTER WHOSE FIRST ACT IS A READ TO FIND A CONTROL IS NOT A REGISTER')
    rec('      ### WORTH OPENING; IT IS A REGISTER WORTH READING FURTHER**, and those are different things.')
    rec('')
    rec('  ### ### **THE REASON, QUOTED:** ### the criterion is a statement about a limit, and the')
    rec('  ### unconditional lower bound puts the finite side above zero at every reach -- so a finite')
    rec('  ### instrument here can only ever confirm what the lower bound already guarantees.')
    rec('  ### ### **AND THE HONEST OTHER HALF, WHICH THIS ACT WILL NOT SUPPRESS:** ### there IS one')
    rec('  ### measurement in this register that would not be vacuous -- whether the product of the')
    rec('  ### distance and the square root of the log approaches the constant the lower bound names. ###')
    rec('  ### **THAT IS A MEASUREMENT ABOUT A CONJECTURE AND NOT ABOUT THE CRITERION**, one of the located')
    rec('  ### sources says the reported numerics *"seem to support"* it, and ### **IT IS FILED AS A')
    rec('  ### ### SENTENCE AND NOT AS A PROPOSAL. ### IT OPENS NOTHING.**')
    rec('')
    rec('  ### **IN EVERY BRANCH, AND IN THIS ONE:** ### **THE CLAUSE HAS NOT MOVED. ### THE PARTITION')
    rec('  ### STAYS UNDECIDED. ### THE PENTAGON\u2019S REFUSAL GOVERNS. ### NO FACE IS PROMOTED. ### THE')
    rec('  ### REGISTER IS NOT ADOPTED.**')

    rec('')
    rec('=' * 100)
    rec('  ### ### **VERDICT: %s.**' % verdict)
    rec('  ### The hint: %s. ### The finite instance: UNCONDITIONAL. ### The obstruction: A RATE, with the'
        % hint_status)
    rec('  ### unconditional side a LOWER bound and the conditional side an UPPER bound.')
    rec('=' * 100)
    p = run_clock.write(D, 'b362_read', LINES)
    io.open(d('b362_read.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(hint_status=hint_status, finite_instance_unconditional=bool(unconditional),
             carries_window_shortfall=False,
             shortfall_carried='the criterion is a limit statement and the finite side is bounded away '
                               'from zero at every index by an unconditional theorem',
             circularity=[dict(statement=w, verdict=v, why=y) for w, v, y in circ],
             uniformity='REAPPEARS, AS A RATE', bridge_typed=False, verdict=verdict,
             register_adopted=False, face_promoted=False, distances_evaluated=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
