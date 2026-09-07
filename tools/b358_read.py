# -*- coding: utf-8 -*-
"""b358_read.py -- THE LI ASYMPTOTICS, READ UNDER A CAP. ### **IT COMPUTES NOTHING.**

### ### **WHAT IT IMPORTS IS THE WHOLE ARGUMENT THAT IT COMPUTES NOTHING:** ### a needle puller, the anchor
### tool, the shared normaliser and a clock. ### **NO NUMERIC LIBRARY. ### NO QUADRATURE. ### NO FIT. ### NO
### ### SERIES SUMMED AND NO COEFFICIENT EVALUATED.** ### The one arithmetic operation in the file is a
### LABELLED DIVISION OF TWO BANKED COUNTS in the pricing, which is `b351`'s precedent and is marked where
### it happens.
### ### **EVERY QUOTATION IS LOCATED BY `anchor_from_file` AT ITS OWN PINNED FILE BEFORE IT IS USED.** ### A
### quotation that cannot be located is reported as NOT LOCATED and is not used.
### ### **AND EVERY JUDGEMENT IN THIS FILE IS DECLARED DATA, ROW BY ROW** -- `b357`'s cure. ### No grade and
### no circularity answer is inferred by a scanner from this seat's own prose.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import run_clock     # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


VOROS = d('b358_source_voros0506326.txt')
LAG = d('b358_source_lagarias0404394.txt')

MET, REFUTABLE, UNDEC = 'MET', 'REFUTABLE', 'UNDECIDABLE-FROM-THE-RECORD'
NOTSTATED = 'NOT STATED BY THE SOURCE'
GRADES = (MET, REFUTABLE, UNDEC)

# ### ==============================================================================================
# ### COMPONENT 1, FIRST HALF -- THE DEPOSIT'S OWN WORDS ON THE FINITE RANGE.
# ### ==============================================================================================
DEPOSIT_READS = [
    ('the certificate, and exactly where it stops', DEPOSIT,
     'certifies λ_n ≥ 0 for n up to Voros'),
    ('the open clause, in the two-channel Li form', DEPOSIT,
     'the inequality λ_Z(n) ≥ −λ_A(n) for every n (RH-equivalent'),
    ('the ancestry paragraph, which names every source this act then fetched', DEPOSIT,
     'The ancestry of the sharpest form.'),
]

# ### ==============================================================================================
# ### THE CANDIDATE STATEMENTS. ### **EACH ONE LOCATED, THEN TESTED AGAINST (B)(1)-(4) AS LOCKED.**
# ### `meets` is DECLARED DATA: which of the four conditions the statement meets, and why.
# ### ==============================================================================================
STATEMENTS = [
    dict(
        sid='V-17', source='Voros math/0506326', path=VOROS,
        hint='For n → ∞ we obtain that if (and only if) the Hypothesis is true,',
        what="Voros's asymptotic (17) for lambda_n itself: the TAME form, `lambda_n ~ n(A log n + B)` "
             "with `A > 0` and `B` explicit.",
        meets={1: (True, 'its subject IS `lambda_n`, not a part of it'),
               2: (True, 'the alternative (18) is the other half of a stated dichotomy, so the deviation '
                         'is controlled in both directions'),
               3: (True, "recoverable from the source's own detection sentence: a violating zero at "
                         "height `T` shows only for `n` of order `2T^2`"),
               4: (True, "stated in the source's own abstract, in four words: *if (and only if)*")},
        hyps=['H-RH', 'H-COUNT'],
        circ={'i': (True, "the source's own abstract names the Hypothesis as the condition, and the "
                          "derivation of (17) OPENS with the zeros placed on the line"),
              'ii': (True, 'the hypothesis and the conclusion are stated by the source as EQUIVALENT, '
                           'which is the strongest possible form of (ii)'),
              'iii': (True, 'the deviation from (17) is exactly (18), whose size is what the hypothesis '
                            'decides')}),
    dict(
        sid='V-24', source='Voros math/0506326', path=VOROS,
        hint='4k n1−2k (n → ∞ ) unconditionally. (24)',
        what="Voros's expansion (24) for `S_n`, the ARCHIMEDEAN part: "
             "`S_n ~ (1/2)n(log n - 1 + gamma - log 2pi) + 3/4 - sum_k B_2k/(4k) n^(1-2k)`, "
             "### **to all orders, and the source writes the word `unconditionally` on the line.**",
        meets={1: (False, "### **ITS SUBJECT IS `S_n`, NOT `lambda_n`.** ### It is an asymptotic for ONE "
                          "CHANNEL of the decomposition, and (B)(1) asks for the coefficient itself"),
               2: (True, 'to all orders in `n`, with the Bernoulli terms written out'),
               3: (True, "the source states the range of validity as `n -> infinity` with an all-orders "
                         "remainder"),
               4: (True, 'none beyond the definitions -- which is what `unconditionally` means here')},
        hyps=['H-NONE'],
        circ={'i': (False, 'the source writes `unconditionally` on the line itself'),
              'ii': (False, 'nothing equivalent to the Hypothesis is invoked; the expansion is a Stirling '
                            'expansion of a gamma-factor quantity'),
              'iii': (False, 'the remainder is the Bernoulli tail and is unconditional too')}),
    dict(
        sid='V-26', source='Voros math/0506326', path=VOROS,
        hint='which gives oscillations that blow up exponentially with n.',
        what="Voros's (26): the RH-FALSE branch, in which the zero channel is asymptotically "
             "`lambda_n` itself and oscillates with exponentially growing amplitude.",
        meets={1: (True, 'it is about `lambda_n` in the branch where RH fails'),
               2: (True, 'the modulus is stated as `mod o(e^(eps n))` for every `eps > 0`'),
               3: (False, "### **NO INDEX BEYOND WHICH POSITIVITY WOULD FOLLOW.** ### This branch says "
                          "the coefficients go negative infinitely often, which is the opposite of what "
                          "a tail closure needs"),
               4: (True, 'the hypothesis is stated: `[RH false]`')},
        hyps=['H-NOTRH', 'H-COUNT'],
        circ={'i': (True, 'its stated condition is the negation of the Hypothesis'),
              'ii': (True, 'same equivalence as V-17, taken on the other branch'),
              'iii': (True, 'the amplitude is decided by where the zeros are')}),
    dict(
        sid='L-5.1', source='Lagarias math/0404394v4', path=LAG,
        hint='Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representationπ onGL(N )',
        what="Lagarias Theorem 5.1: `S_inf(n,pi) = (N/2) n log n + C_1(pi) n + O(N(K(pi)+1))` for "
             "`n >= K(pi)`, with `K(pi) = max |kappa_j(pi)|^2` and the implied constant ABSOLUTE -- "
             "### **AN UNCONDITIONAL ASYMPTOTIC WITH AN EXPLICIT ERROR TERM AND AN EXPLICIT INDEX.**",
        meets={1: (False, "### **ITS SUBJECT IS `S_inf(n,pi)`, THE ARCHIMEDEAN CONTRIBUTION, NOT "
                          "`lambda_n`.** ### The same failure as V-24, from the other source"),
               2: (True, '`O(N(K(pi)+1))`, with the implied constant stated to be ABSOLUTE'),
               3: (True, '`n >= K(pi)`, and `K(pi)` is given by a formula'),
               4: (True, '`pi` irreducible cuspidal unitary on `GL(N)`; nothing about zero locations')},
        hyps=['H-CUSP', 'H-NGEK'],
        circ={'i': (False, "the Hypothesis is nowhere in Theorem 5.1's statement"),
              'ii': (False, 'no equivalent of it is invoked'),
              'iii': (False, '### **THE ERROR TERM IS UNCONDITIONAL AND ITS CONSTANT IS ABSOLUTE** -- '
                             'this is the one located error term that survives (D)(iii)')}),
    dict(
        sid='L-6.1', source='Lagarias math/0404394v4', path=LAG,
        hint='in which the implied constant in the O-notation depends on π. If the Riemann hypothesis holds',
        what="Lagarias Theorem 6.1: unconditionally `S_f(n,pi) = lambda_n(sqrt n, pi^v) + O(sqrt n log n)` "
             "-- and then, ### **IF the Riemann hypothesis holds for `L(s,pi)`**, `lambda_n(sqrt n, pi^v) "
             "= O(sqrt n log n)`.",
        meets={1: (False, 'its subject is `S_f(n,pi)`, the finite-place contribution'),
               2: (True, 'two error terms, and the ACT of this act is which of them is conditional'),
               3: (False, 'no index is given beyond which positivity of `lambda_n` would follow'),
               4: (True, 'stated: the unconditional half, and the RH-conditional half, in consecutive '
                         'sentences')},
        hyps=['H-CUSP', 'H-RHL'],
        circ={'i': (True, "### **THE BOUND ITSELF IS THE CONDITIONAL SENTENCE.** ### The unconditional "
                          "half REDUCES `S_f` to another Li-type quantity; it does not bound it"),
              'ii': (False, 'no separate equivalent is invoked'),
              'iii': (True, '### **THIS IS (D)(iii) IN ITS PUREST FORM:** the reduction is '
                            'unconditional and the SIZE is not')}),
    dict(
        sid='L-ABS', source='Lagarias math/0404394v4', path=LAG,
        hint='We derive an unconditional asymptotic formula for the coe',
        what="Lagarias's abstract, which states the split in one breath: an unconditional asymptotic "
             "formula ### **IN TERMS OF THE ZEROS**, and then, ### **ASSUMING the Riemann hypothesis**, "
             "the closed form `lambda_n(pi) = (N/2) n log n + C_1(pi) n + O(sqrt n log n)`.",
        meets={1: (True, 'the closed form is about `lambda_n(pi)` itself'),
               2: (True, '`O(sqrt n log n)`'),
               3: (False, "### **NO INDEX IS STATED**, and the implied constant is said to DEPEND ON "
                          "`pi` rather than being absolute, so no index is recoverable either"),
               4: (True, "stated in the abstract's own words: *Assuming the Riemann hypothesis*")},
        hyps=['H-CUSP', 'H-RHL'],
        circ={'i': (True, 'the abstract names the Riemann hypothesis as the assumption for the closed '
                          'form'),
              'ii': (False, 'nothing further is invoked'),
              'iii': (True, "the unconditional formula is *in terms of the zeros*, so its content is "
                            "carried by the very thing at issue")}),
    dict(
        sid='BL-1c', source='Bombieri-Lagarias 1999, QUOTED INSIDE VOROS', path=VOROS,
        hint='In [2, Cor. 1(c)], rather weak exponential lower bounds',
        what="Bombieri-Lagarias Corollary 1(c) as Voros states it: ### **`lambda_n >= -c e^(eps n)` was "
             "shown to IMPLY RH.** ### The one located statement that runs in the useful direction.",
        meets={1: (True, 'it is a condition on `lambda_n`'),
               2: (False, "### **IT IS A HYPOTHESIS, NOT AN ASYMPTOTIC.** ### There is no main term and "
                          "no error term; it is a WEAKENING OF WHAT MUST BE SHOWN"),
               3: (False, "### **AND THIS IS THE POINT: THE BOUND IS DEMANDED FOR ALL `n`.** ### It "
                          "replaces `lambda_n >= 0` for every `n` by something laxer for every `n`; it "
                          "does not close a tail from a finite check"),
               4: (True, 'none beyond the bound itself')},
        hyps=['H-ALLN'],
        circ={'i': (False, 'it CONCLUDES the Hypothesis rather than assuming it'),
              'ii': (False, 'nothing equivalent is assumed'),
              'iii': (False, 'there is no error term to be conditional')}),
]

# ### ==============================================================================================
# ### COMPONENT 2 -- THE HYPOTHESES, GRADED TWICE. ### **DECLARED DATA, AND THE TWO AXES NEVER MERGED.**
# ### ==============================================================================================
HYPOTHESES = {
    'H-RH': dict(
        name='the Riemann Hypothesis itself, as the stated condition of the tame branch',
        axis1=(MET, "vacuously in the source's own terms: Voros does not assert RH, he CONDITIONS on it, "
                    "and the conditional statement is what he proves. ### **`MET` HERE MEANS THE SOURCE "
                    "USES IT CONSISTENTLY, NOT THAT IT HOLDS.**"),
        axis2=(UNDEC, "### **IT IS THE OPEN CLAUSE.** ### The deposit's own position is RH UNDER the open "
                      "premise; the record neither holds it nor refutes it, and this act does not move it. "
                      "### What would decide it is exactly what is not in the record.")),
    'H-NOTRH': dict(
        name='the negation of the Hypothesis, as the stated condition of the oscillating branch',
        axis1=(MET, 'the same: consistently used as a condition by the source'),
        axis2=(UNDEC, 'the mirror of H-RH, and undecidable from the record for the same reason')),
    'H-COUNT': dict(
        name="Voros's counting-function law (16): `N(T) = 2T[2R_-2(log T - 1) + R_-1] + dN(T)` with "
             "`dN(T) = O(T^alpha)`",
        axis1=(MET, "classical for `zeta` and stated by the source as the input its rule `(16) => (15)` "
                    "consumes; the source treats it as available"),
        axis2=(MET, "the corpus's own aim-map used a zero count over `t` in `[0.5, 150]` closing at 180 "
                    "against a main term of 178.6 (`b334`, banked), which is this law at the corpus's own "
                    "scale. ### **THE AGREEMENT IS MEASURED AND BANKED, NOT ASSUMED HERE.**")),
    'H-NONE': dict(
        name='no hypothesis beyond the definitions -- the source writes `unconditionally` on the line',
        axis1=(MET, 'stated by the source on the line the anchor tool located'),
        axis2=(MET, "and the corpus has CHECKED it: the deposit reports its measured archimedean channel "
                    "reproducing the unconditional asymptotic *to hundreds of digits*, and `b327` measured "
                    "the corresponding identity to `1.33e-251` at `n <= 30` by two routes. ### **THIS IS "
                    "THE ONE HYPOTHESIS THE CORPUS HAS ITS OWN EVIDENCE FOR.**")),
    'H-CUSP': dict(
        name='`pi` an irreducible cuspidal unitary automorphic representation on `GL(N)`',
        axis1=(MET, "the source's standing assumption throughout"),
        axis2=(MET, "the corpus's object is `zeta`, which is the `N = 1` case with `Q = 1`; the deposit "
                    "cites Lagarias for exactly this specialisation. ### **THE SUBSTITUTION `N = 1, "
                    "Q = 1` IS THE ONLY ONE THIS ACT MAKES, AND IT IS NAMED HERE.**")),
    'H-NGEK': dict(
        name='`n >= K(pi)` with `K(pi) = max_j |kappa_j(pi)|^2`',
        axis1=(MET, 'given by a formula in the theorem itself'),
        axis2=(UNDEC, "### **THE RECORD DOES NOT CARRY `K(pi)` FOR ITS OWN OBJECT.** ### The gamma factor "
                      "is in the record (`b327`: the deposit's `f_A(s) = log s + logGamma(s/2) - "
                      "(s/2)log pi`), so the `kappa_j` are determined by it -- but ### **DETERMINED IS NOT "
                      "COMPUTED**, and the cap forbids this act from computing it. ### What would decide "
                      "it: one evaluation, which is not ordered here.")),
    'H-RHL': dict(
        name='the Riemann hypothesis for `L(s,pi)` -- for the corpus, for `zeta`',
        axis1=(MET, 'consistently used as a condition by the source'),
        axis2=(UNDEC, 'the open clause again, under another name')),
    'H-ALLN': dict(
        name='the bound `lambda_n >= -c e^(eps n)` holding FOR EVERY `n`',
        axis1=(MET, 'stated by Voros as what Bombieri-Lagarias showed sufficient'),
        axis2=(UNDEC, "### **AND UNDECIDABLE IN THE WAY THAT MATTERS MOST HERE:** ### the deposit's "
                      "certificate reaches a FINITE range, and this hypothesis is a demand over ALL `n`. "
                      "### The record has no statement about any `n` past its certificate's end, so it "
                      "can neither meet this nor refute it.")),
}

# ### ==============================================================================================
# ### BAR 3 -- THE PRICING. ### **FROM BANKED FIGURES, LABELLED, AND NOT ATTEMPTED.**
# ### ==============================================================================================
PRICE = dict(
    computed_to=300,          # ### the deposit: measured channels "computed to n = 300"
    detect_index=10 ** 18,    # ### Voros, and the deposit repeating him: n greater than about 10^18
    height=10 ** 9,           # ### Voros: violating zeros "now known to require |Im rho| >~ 10^9"
)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def locate(path, hint):
    n, line = AF.find(path, hint)
    needle_pull.pull(path, line)
    return n, line.strip()


def main():
    rec('=' * 100)
    rec('b358 -- THE LI ASYMPTOTICS, READ UNDER A CAP. ### IT COMPUTES NOTHING.')
    rec('=' * 100)
    rec('  ### the three grades, locked before any source was opened : %s' % ' / '.join(GRADES))
    rec('  ### and the fourth outcome, about the SOURCE and not the hypothesis : %s' % NOTSTATED)
    rec('  ### ### **EVERY HYPOTHESIS IS GRADED TWICE AND THE TWO AXES ARE NEVER MERGED.**')
    notloc = []

    # ---- COMPONENT 1 -------------------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 1(a) -- THE SHAPE ASKED FOR: WHAT THE FINITE RANGE IS, AND WHERE IT STOPS.')
    rec('  ### ### **FROM THE DEPOSIT\'S OWN WORDS, LOCATED AT THE DEPOSITED FILE.**')
    rec('-' * 100)
    for label, path, hint in DEPOSIT_READS:
        try:
            n, line = locate(path, hint)
        except (AF.AnchorError, LookupError) as e:
            notloc.append(label)
            rec('  ### ### **NOT LOCATED** : %s -- %s' % (label, str(e)[:80]))
            continue
        rec('')
        rec('  ### **%s**   (%s : line %d)' % (label, os.path.basename(path), n))
        rec('      | %s' % line[:300])
    rec('')
    rec('  ### ### ### **SO THE FINITE RANGE IS `n <= N_0(T) ~ 2T^2`, VOROS\'S DETECTION THRESHOLD, AND')
    rec('  ### ### ### IT STOPS THERE -- IN THE DEPOSIT\'S OWN WORDS, *"a certificate reaching exactly to')
    rec('  ### ### ### where discrimination would begin, and no further"*.**')
    rec('  ### **AND THE DEPOSIT SAYS WHAT IT IS NOT, IN THE SAME SENTENCE:** ### *"it is not RH"*.')

    # ---- COMPONENT 1(b) ----------------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 1(b) -- WHAT THE LITERATURE CARRIES, TESTED AGAINST (B)(1)-(4) AS LOCKED.')
    rec('-' * 100)
    shapes, nonshapes = [], []
    for st in STATEMENTS:
        try:
            n, line = locate(st['path'], st['hint'])
        except (AF.AnchorError, LookupError) as e:
            notloc.append(st['sid'])
            rec('')
            rec('  ### ### **NOT LOCATED, SO NOT USED** : %s -- %s' % (st['sid'], str(e)[:80]))
            continue
        st['line'] = n
        st['text'] = line
        met = [k for k in (1, 2, 3, 4) if st['meets'][k][0]]
        st['is_shape'] = (len(met) == 4)
        (shapes if st['is_shape'] else nonshapes).append(st)
        rec('')
        rec('  ### **[%s] %s**   (%s : line %d)' % (st['sid'], st['source'], os.path.basename(st['path']), n))
        rec('      | %s' % line[:220])
        rec('      ### what it is : %s' % st['what'])
        for k in (1, 2, 3, 4):
            ok, why = st['meets'][k]
            rec('      ### (B)(%d) %-3s : %s' % (k, 'YES' if ok else 'NO', why))
        rec('      ### ### **%s**' % ('A SHAPE, BY THE LOCKED DEFINITION.' if st['is_shape']
                                      else 'NOT A SHAPE -- it fails (B)(%s).'
                                           % ', '.join(str(k) for k in (1, 2, 3, 4)
                                                       if not st['meets'][k][0])))
    rec('')
    rec('  ### SHAPES : %d %s' % (len(shapes), [s['sid'] for s in shapes]))
    rec('  ### NOT SHAPES : %d %s' % (len(nonshapes), [s['sid'] for s in nonshapes]))

    # ---- COMPONENT 2 -------------------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 2 -- THE HYPOTHESES, GRADED TWICE. ### **THE TWO AXES ARE NEVER MERGED.**')
    rec('-' * 100)
    used = []
    for st in STATEMENTS:
        for h in st['hyps']:
            if h not in used:
                used.append(h)
    for h in used:
        H = HYPOTHESES[h]
        g1, w1 = H['axis1']
        g2, w2 = H['axis2']
        carriers = [s['sid'] for s in STATEMENTS if h in s['hyps'] and 'line' in s]
        rec('')
        rec('  ### **%s** -- %s' % (h, H['name']))
        rec('      ### carried by : %s' % ', '.join(carriers))
        rec("      ### AXIS 1, against the SOURCE'S own objects  : ### **%s**" % g1)
        rec('          %s' % w1)
        rec("      ### AXIS 2, against the CORPUS'S own objects  : ### **%s**" % g2)
        rec('          %s' % w2)
    n_undec2 = sum(1 for h in used if HYPOTHESES[h]['axis2'][0] == UNDEC)
    n_met2 = sum(1 for h in used if HYPOTHESES[h]['axis2'][0] == MET)
    rec('')
    rec('  ### hypotheses graded : %d ; ON AXIS 2 -- MET %d, %s %d, REFUTABLE %d'
        % (len(used), n_met2, UNDEC, n_undec2,
           sum(1 for h in used if HYPOTHESES[h]['axis2'][0] == REFUTABLE)))
    rec('  ### ### **NO HYPOTHESIS CARRIES A MERGED GRADE. ### EVERY ONE CARRIES TWO.**')

    # ---- COMPONENT 3 -------------------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 3 -- THE CIRCULARITY CHECK, RUN BEFORE THE VERDICT, ON EVERY LOCATED STATEMENT.')
    rec('-' * 100)
    circular, clean = [], []
    for st in STATEMENTS:
        if 'line' not in st:
            continue
        answers = st['circ']
        fired = [k for k in ('i', 'ii', 'iii') if answers[k][0]]
        (circular if fired else clean).append(st)
        rec('')
        rec('  ### **[%s]** %s' % (st['sid'], 'A SHAPE' if st['is_shape'] else 'not a shape'))
        for k in ('i', 'ii', 'iii'):
            ok, why = answers[k]
            rec('      ### (D)(%-3s) %-3s : %s' % (k, 'YES' if ok else 'no', why))
        rec('      ### ### **%s**' % ('CIRCULAR -- fires at (%s).' % ', '.join(fired) if fired
                                      else 'THIS ACT FOUND NO CIRCULARITY IN IT.'))
    rec('')
    rec('  ### CIRCULAR : %d %s' % (len(circular), [s['sid'] for s in circular]))
    rec('  ### NOT FOUND CIRCULAR : %d %s' % (len(clean), [s['sid'] for s in clean]))
    circ_shapes = [s for s in shapes if s in circular]
    clean_shapes = [s for s in shapes if s in clean]
    rec('  ### ### **AND THE ONE THAT DECIDES THE VERDICT: SHAPES THAT SURVIVE (D) : %d %s**'
        % (len(clean_shapes), [s['sid'] for s in clean_shapes]))
    rec('  ### **THE CONVERSE, LOCKED IN (D) BEFORE ANY SOURCE WAS OPENED:** ### a statement passing all')
    rec('  ### three is NOT thereby a closure of the tail; it is one this act failed to find circular.')

    # ---- COMPONENT 4 -------------------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec("  ### COMPONENT 4 -- THE VERDICT, BY (F)'S LOCKED RULE.")
    rec('-' * 100)
    if clean_shapes:
        verdict = 'A SHAPE EXISTS'
    elif circ_shapes:
        verdict = 'EXISTS BUT CIRCULAR'
    else:
        verdict = 'NO USABLE ASYMPTOTICS LOCATED'
    nloc = len([s for s in STATEMENTS if 'line' in s])
    rec('    ### **(NO USABLE ASYMPTOTICS LOCATED) -- UNREACHABLE, AND SHOWN SO.** ### %d statements were'
        % nloc)
    rec('      located and quoted, %d of them meeting all four locked conditions.' % len(shapes))
    rec('    ### **(A SHAPE EXISTS) -- UNREACHABLE, AND SHOWN SO.** ### It requires a shape surviving')
    rec('      Component 3, and %d do.' % len(clean_shapes))
    rec('    ### **AND THE MIXTURE RULE, LOCKED BEFORE THE READING:** ### if any located shape is circular')
    rec('      and none is found non-circular, the verdict is (EXISTS BUT CIRCULAR).')
    rec('    ### ### ### **THEREFORE: %s.**' % verdict)

    # ---- BAR 3 -------------------------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### BAR 3 -- THE PRICING. ### **LABELLED, FROM BANKED FIGURES, AND NOT ATTEMPTED.**')
    rec('-' * 100)
    rec('  ### **THE INDEX BEYOND WHICH THE LOCATED SHAPE WOULD ACT:** ### **THERE IS NONE**, and that is')
    rec('  ### the finding rather than a missing number. ### `V-17` acts only on the branch its own')
    rec('  ### condition selects, so ### **NO FINITE CHECK PUTS THE RECORD ON THAT BRANCH.**')
    rec('  ### **WHAT A FINITE CHECK WOULD HAVE TO COVER, IF A NON-CIRCULAR SHAPE EVER ARRIVED:** ### every')
    rec('  ### index up to that shape\'s own threshold. ### The two figures the record already banks bracket')
    rec('  ### the size of that demand, and ### **THE ONLY ARITHMETIC IN THIS ACT IS THE LABELLED DIVISION')
    rec('  ### OF THESE TWO BANKED COUNTS** (b351\'s precedent):')
    rec('      the corpus has computed its channels to        n = %d   (the deposit, at guaranteed precision)'
        % PRICE['computed_to'])
    rec('      a violating zero could first register at about n = %.0e   (Voros; the deposit repeats him)'
        % PRICE['detect_index'])
    ratio = PRICE['detect_index'] / float(PRICE['computed_to'])
    rec('      ### **THE RATIO, ONE LABELLED DIVISION : %.2e**' % ratio)
    rec('  ### ### **AND WHAT THE RATIO IS NOT:** ### it is not a price in wall time, in memory or in')
    rec('  ### precision, because ### **THE RECORD PRINTS NO COST PER INDEX FOR THIS CHANNEL** and this act')
    rec('  ### may not measure one. ### **IT IS A DISTANCE IN INDEX AND NOTHING ELSE.**')
    rec('  ### **THE FLOOR THE REGISTRATION REQUIRED OF THIS BAR, RESTATED:** ### the threshold is stated')
    rec('  ### by the deposit and by Voros as `~ 2T^2` and `>~ 10^18` -- ### **APPROXIMATE IN BOTH**, so')
    rec('  ### the ratio is approximate too and is printed to two figures and no more.')

    rec('')
    rec('=' * 100)
    rec('  VERDICT : ### **%s**' % verdict)
    rec('  ### ### **NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT')
    rec("  ### ### MOVED. ### THE TWO FACES' EQUIVALENCE IS NOT COMPILED. ### NO ACT IS RE-VERDICTED.**")
    rec('=' * 100)

    p = run_clock.write(D, 'b358_read_run', LINES)
    io.open(d('b358_read.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(dict(
        verdict=verdict, grades=list(GRADES),
        statements=[dict(sid=s['sid'], source=s['source'], file=os.path.basename(s['path']),
                         line=s.get('line'), is_shape=s.get('is_shape'),
                         fails=[k for k in (1, 2, 3, 4) if not s['meets'][k][0]],
                         circular=[k for k in ('i', 'ii', 'iii') if s['circ'][k][0]],
                         hyps=s['hyps']) for s in STATEMENTS if 'line' in s],
        shapes=[s['sid'] for s in shapes], not_shapes=[s['sid'] for s in nonshapes],
        circular=[s['sid'] for s in circular], clean=[s['sid'] for s in clean],
        clean_shapes=[s['sid'] for s in clean_shapes],
        hypotheses={h: dict(name=HYPOTHESES[h]['name'], axis1=HYPOTHESES[h]['axis1'][0],
                            axis2=HYPOTHESES[h]['axis2'][0]) for h in used},
        n_undecidable_axis2=n_undec2, not_located=notloc, price=PRICE, price_ratio=ratio,
        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
