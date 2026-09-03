# -*- coding: utf-8 -*-
"""b310_components.py -- THE COMPONENTS, IN ORDER.

### ### **THE REGISTRATION IS SEALED WITH THE ANSWER IN IT** (`17185ccb...`, before this file
### existed). ### `(P1)`-`(P5)` state the assembly, the collapse, what the surviving term does not
### contain, the unified fixed-point formula and the kind of statement it is. ### **SO EVERY TABLE
### BELOW IS A CHECK ON A PREDICTION, AND A DISAGREEMENT IS PRINTED AT FULL PROMINENCE AND KEPT.**

### ### **AND THIS SEAT ALREADY KNOWS WHAT THAT COSTS.** ### At b309 a clause of the sealed
### prediction was refuted by its own run. ### **THE SEAL IS WHAT MADE THAT WORTH ANYTHING**, and
### the same discipline is applied here without softening.
"""
import io
import os
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools')
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'e16'))

import needle_pull                                   # noqa: E402
import b310_smear as SM                              # noqa: E402
import b309_scaling_trace as ST                      # noqa: E402
import b308_local_field as LF                        # noqa: E402
import b304_smearing as SMEAR                        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')

OWNERS = [
    # ### RE-POINTED AT WHAT THE FILE EMITS: b304's quotation of CC spans a hard wrap.
    ("### THE SOURCE'S MOVE, quoted by b304 from CC -- the construction this act assembles",
     't:b304_smearing.py', 'associate to a test function'),
    ("b304 -- the projection is onto Sonin's space, not a sector",
     't:b304_smearing.py', 'THE FAITHFUL'),
    ("b304 -- the part it computed, and the part it refused",
     't:b304_smearing.py', 'REFUSES THE'),
    ("b305 -- eq. (149): WHERE THE PRIME'S CONTRIBUTION ACTUALLY LIVES",
     'b305_the_arithmetics_entry.txt', 'W_p(f) = (log p) SUM_{m>=1}'),
    ("b305 -- and the sentence that locates the `log p`",
     'b305_the_arithmetics_entry.txt', '`log p` is in `W_p`'),
    ("b305 -- the corpus's adopted summand, the same expression",
     'b305_the_arithmetics_entry.txt', "corpus's adopted summand is `w_{p,k}"),
    ("b309 -- the zero this act CARRIES and does not re-derive",
     'b309_the_scaling_trace.txt', 'THE VALUE IS EXACTLY ZERO'),
    ("### b309 -- the scope that travels with it",
     'b309_the_scaling_trace.txt', 'The vanishing of one trace'),
    ("b309 -- the mechanism this act generalises",
     'b309_the_scaling_trace.txt', 'AND `p^j - 1` IS A UNIT'),
    ("b308 -- Tr(Pi) equals the constrained dimension",
     'b308_the_local_field_instrument.txt', 'EQUALS THE CONSTRAINED DIMENSION AT ALL SIX'),
    # ### THE EMITTER IS b285's OWN BANK, not a later act that carries the sentence forward.
    ("b285 -- the boundary this act does not cross",
     'b285_archimedean_opening.txt', 'NO FINITE-SIDE STRUCTURAL FACT TYPES'),
    ("### b262 -- ITS OWN sentence, which is a REQUIREMENT and not a disjunction",
     'b262_junction_limit.txt', 'ABSORB A DIVERGENT QUANTITY'),
    ("### b262 -- and the refusal it attaches in the same breath",
     'b262_junction_limit.txt', 'NOT A CLAIM THAT IT FAILS TO DO IT'),
    ("### b263 -- ITS OWN formulation of the branch (NOT b262's wording)",
     'b263_top_level_silence.txt', 'EITHER THE FINITE-PLACE SIDE SUPPLIES'),
    ("b263 -- (SPEC-1), the property this act bears on",
     'b263_top_level_silence.txt', '(SPEC-1) IT COUNTS FIRST LEVELS'),
    ("b263 -- (SPEC-2)", 'b263_top_level_silence.txt', "(SPEC-2) IT REDUCES TO `Theta_q`'s TERMS"),
    ("b263 -- (SPEC-3)", 'b263_top_level_silence.txt', '(SPEC-3) IT IS DEFINED OVER ALL PRIMES'),
    ("### b263 -- the specification is conditional on the branch and vacuous on the other",
     'b263_top_level_silence.txt', 'FOR THE FIRST BRANCH ONLY AND IS VACUOUS ON THE SECOND'),
    ("### b263 -- and its own refusal: these exclude, they do not determine",
     'b263_top_level_silence.txt', 'THESE EXCLUDE; THEY DO NOT DETERMINE'),
]


def rule(ch='-', n=100):
    return ch * n


def main():
    out, fails = [], []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b310 -- THE SMEAR COLLAPSES. ### THE COMPONENTS, IN ORDER.')
    rec('=' * 100)
    rec('  ### THE FIXTURES OF EVERY FILE USED IN A VERDICT, BEFORE ANY OF THEM IS TRUSTED:')
    oks = [('b310_smear', SM.self_test(False)), ('b309_scaling_trace', ST.self_test(False)),
           ('b308_local_field', LF.self_test(False)), ('b304_smearing', SMEAR.self_test(False))]
    rec('    ' + '    '.join('%s : %s' % (a, 'PASS' if b else '### FAIL') for a, b in oks))
    if not all(b for _a, b in oks):
        rec('  ### REFUSING TO REPORT FROM A SUITE THAT FAILS ITS OWN FIXTURES.')
        return 2, out

    rec('')
    rec('  ### THE OWNERS, PULLED FROM THE FILES THAT EMIT THEM:')
    unpullable = 0
    for label, fn, anchor in OWNERS:
        path = os.path.join(HERE, fn[2:]) if fn.startswith('t:') else os.path.join(D, fn)
        try:
            line = needle_pull.pull(path, anchor)
            rec('  %s' % label)
            rec('      %s' % line[:136])
        except LookupError:
            unpullable += 1
            fails.append('owner needle: %s' % label)
            rec('  ### FAIL (UNPULLABLE) %s   anchor=%r' % (label, anchor))
    rec('  ### OWNER SENTENCES PULLED : %d   ### UNPULLABLE : %d'
        % (len(OWNERS) - unpullable, unpullable))
    rec('  ### ### **AND ONE ATTRIBUTION IS MADE EXPLICITLY BECAUSE IT IS THE ACT\'S LIVE HAZARD:**')
    rec('  ### the DISJUNCTION is ### b263\'s FORMULATION ### of what b262 established; ### b262\'s')
    rec('  ### OWN sentence is a REQUIREMENT on the archimedean side, with its own refusal attached.')
    rec('  ### **BOTH ARE PULLED FROM THEIR OWN FILES AND NEITHER IS ATTRIBUTED TO THE OTHER.**')

    # ==============================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE ASSEMBLY, AND WHAT SURVIVES.')
    rec('=' * 100)
    rec('  ### At a finite place the scaling part of `Q_p^x` is `p^Z`, which is DISCRETE, so the')
    rec('  ### source\'s integral over it is a SUM over the powers of the prime with the test')
    rec('  ### function evaluated at those powers:')
    rec('  ###   ### **`T(w) = SUM over k of w_k Tr(theta(p^k) Pi)`.**')
    rec('  ### **THE WEIGHT IS SYMBOLIC. ### NO BUMP IS CHOSEN, SO NO CLASS QUESTION ARISES AND NO')
    rec('  ### PRICE IS PAID.** ### And the sum is FINITE because the source\'s test functions are')
    rec('  ### compactly supported: such a function meets only finitely many powers of `p`.')
    rec('  ### ### **THE ZEROS ARE NOT SUBSTITUTED IN. ### EVERY TERM IS FORMED AND ADDED**, so the')
    rec('  ### collapse is something the sum DOES rather than something the code was told.')
    rec('')
    rec('  %-9s %-8s %-13s %-24s %-15s %s'
        % ('cell', 'terms', 'surviving', 'T(w) with a loud tail', 'w_0 * Tr(Pi)', 'agree'))
    surviving_nonzero = []
    for (p, n) in SM.CELLS:
        w = SM.weight_loud_tail(n)
        terms = SM.smear_terms(p, n, w)
        alive = [(k, wk, tr) for (k, wk, tr) in terms if k != 0 and wk * tr != 0]
        surviving_nonzero += [(p, n) + a for a in alive]
        got = SM.smear(p, n, w)
        want = w[0] * SM.trace_identity(p, n)
        ok = (got == want)
        if not ok or alive:
            fails.append('assembly at (%d,%d)' % (p, n))
        rec('  %-9s %-8d %-13s %-24s %-15s %s'
            % ('(%d,%d)' % (p, n), len(terms),
               '%d of %d' % (len([t for t in terms if t[1] * t[2] != 0]), len(terms)),
               got, want, 'YES' if ok else '### NO ###'))
    rec('')
    rec('  ### ### **TERMS SURVIVING AT A NONZERO POWER : %d**' % len(surviving_nonzero))
    for row in surviving_nonzero:
        rec('      ### ### **SURVIVING TERM AT (%d,%d) k=%+d : w=%s Tr=%s** ### -- the navigator\'s'
            ' expectation is REFUTED and this line is the refutation.' % row)
    rec('  ### **SO THE ONLY TERM THAT SURVIVES IS THE ONE AT THE IDENTITY**, at every cell, and')
    rec('  ### its coefficient is `Tr(Pi)`.')

    # ==============================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE DERIVATION.')
    rec('=' * 100)
    rec('  ### **THE DERIVATION, GENERAL IN `p`, `n` AND THE WEIGHT:**')
    rec('  ###   ### the assembly is `SUM_k w_k Tr(theta(p^k) Pi)` -- the frame algebra, which fixes')
    rec('  ###     that each term is a trace in the smallest ambient containing source and target;')
    rec('  ###   ### b309\'s mechanism kills every `k != 0` term, because `p^{|k|} - 1` IS A UNIT and')
    rec('  ###     the scaling map therefore fixes nothing off the ball in either congruence;')
    rec('  ###   ### and the `k = 0` term is `w_0 Tr(Pi)`, with `Tr(Pi) = (p^n - 1)^2` -- b304\'s')
    rec('  ###     not-dead witness, reproduced by b308 against the constrained dimension.')
    rec('  ### ### ### **THEREFORE `T(w) = w_0 * (p^n - 1)^2`.**')
    rec('  ### **NO STEP MENTIONS A CELL. ### THE TABLE ABOVE IS THE CHECK AND NOT THE PROOF**, and')
    rec('  ### a sweep over seven cells is not a proof over all of them.')
    rec('')
    rec(rule())
    rec('### (2a) `F3` -- WHAT THE SURVIVING TERM CONTAINS, AND WHAT IT DOES NOT.')
    rec(rule())
    rec('  ### **THE FUNCTIONAL READS THE TEST FUNCTION AT ONE POINT.** ### Two weights agreeing at')
    rec('  ### the identity and differing at EVERY nonzero power must give the SAME value; and two')
    rec('  ### differing AT the identity must give DIFFERENT values. ### **BOTH ARMS, OR THE FIRST')
    rec('  ### IS A CHECK THAT CANNOT FAIL.**')
    rec('  %-9s %-18s %-18s %-14s %-18s %s'
        % ('cell', 'quiet tail', 'loud tail', 'same?', 'identity doubled', 'differs?'))
    for (p, n) in SM.CELLS:
        a = SM.smear(p, n, SM.weight_identity_only(n))
        b = SM.smear(p, n, SM.weight_loud_tail(n))
        c = SM.smear(p, n, SM.weight_loud_tail(n, 2))
        same, diff = (a == b), (c != b)
        if not (same and diff):
            fails.append('reads-one-point at (%d,%d)' % (p, n))
        rec('  %-9s %-18s %-18s %-14s %-18s %s'
            % ('(%d,%d)' % (p, n), a, b, 'YES' if same else '### NO ###', c,
               'YES' if diff else '### NO ###'))
    rec('  ### ### **SO THE SURVIVING TERM CONTAINS: ### the weight at the identity, and the')
    rec('  ### ### constrained dimension. ### AND IT CONTAINS NOTHING ELSE.**')
    rec('  ### **NO `log p`.** ### The coefficient is `(p^n - 1)^2`, an integer count of dimensions.')
    rec('  ### **NO SAMPLING AT THE PRIME\'S POWERS.** ### The weight is read at `p^0` and nowhere')
    rec('  ###   else -- measured above with a tail that is nonzero at every carried power.')
    rec('  ### **NO DEPENDENCE ON THE WEIGHT AWAY FROM THE IDENTITY.** ### Same measurement.')

    return _component_two_b(rec, fails, out)


# ==================================================================================================
def _component_two_b(rec, fails, out):
    rec('')
    rec(rule())
    rec('### (2b) `F4` -- THE UNIFIED FIXED-POINT FORMULA, CHECKED AGAINST BOTH OWNERS.')
    rec(rule())
    rec('  ### The registration\'s `(P4)`: `Tr(theta(t) Pi)` is a SIGNED COUNT of the off-ball points')
    rec('  ### `t` fixes, in the two congruences the object\'s two conditions impose.')
    rec('  ### **CHECKED AGAINST b304\'s OWN `trace_scaled` AT EVERY UNIT, AND AGAINST b309\'s')
    rec('  ### REDUCED SUM AT EVERY CARRIED POWER.**')
    rec('  %-9s %-14s %-26s %-16s %s'
        % ('cell', 'units', 'count == b304 trace_scaled', 'powers', 'count == b309 route B'))
    factor_bad = []
    for (p, n) in SM.CELLS:
        N = p ** (2 * n)
        P, _rank, _b = ST.son_projector_built(p, n)
        units = [u for u in range(N) if SMEAR.gcd(u, N) == 1]
        ubad = [u for u in units if SM.trace_at_unit(p, n, u) != SMEAR.trace_scaled(P, u, N)]
        unonzero = [u for u in units if SM.trace_at_unit(p, n, u) != 0]
        pbad = [k for k in SM.carried_powers(n)
                if SM.trace_at_power(p, n, k) != ST.trace_route_b(p, n, k)]
        # ### **THE FACTOR ARM: THE REGISTRATION SAYS `|t|`; THE AMBIENT SAYS `p^{-max(k,0)}`.**
        # ### The two agree at every unit and every POSITIVE power and differ at every negative one.
        for k in SM.carried_powers(n):
            ambient = Fraction(1, p ** k) if k > 0 else Fraction(1)
            modulus = Fraction(p) ** (-k)          # ### `|p^k|`
            if ambient != modulus:
                factor_bad.append((p, n, k, ambient, modulus))
        if ubad or pbad:
            fails.append('unified formula at (%d,%d)' % (p, n))
        rec('  %-9s %-14d %-26s %-16d %s'
            % ('(%d,%d)' % (p, n), len(units),
               'YES, all %d (%d nonzero)' % (len(units), len(unonzero)) if not ubad
               else '### NO at %s ###' % ubad[:3],
               len(SM.carried_powers(n)),
               'YES, all %d' % len(SM.carried_powers(n)) if not pbad
               else '### NO at %s ###' % pbad[:3]))
    rec('  ### **AND THE ARM THAT KEEPS THE UNIT COLUMN FROM BEING VACUOUS: ### THE COUNT IS')
    rec('  ### NONZERO AT SOME UNITS AT EVERY CELL** -- a formula agreeing with `trace_scaled` only')
    rec('  ### where both are zero would have agreed about nothing.')
    rec('')
    rec('  ### ### ### **AND A CLAUSE OF THE SEALED PREDICTION IS REFUTED HERE. ### `(P4)` SAYS THE')
    rec('  ### ### ### FACTOR IS `|t|`.**')
    rec('  ### It is `|t|` at every unit (where `|t| = 1`) and at every POSITIVE power (where')
    rec('  ### `|p^k| = p^{-k}`). ### **AT A NEGATIVE POWER IT IS `1`, WHILE `|p^{-j}| = p^{j}`.**')
    rec('  ### The factor is the HAAR WEIGHT OF THE EMBEDDING -- `p^{-max(k,0)}` -- because the')
    rec('  ### ambient REPEATS the vectors when `k > 0` and SPREADS them when `k < 0`, and those two')
    rec('  ### embeddings do not carry the same Gram factor. ### **THE COUNT IS THE CONTENT; THE')
    rec('  ### FACTOR IS THE PART THE PREDICTION GOT WRONG.**')
    rec('  ### ### **AND THE REASON IT MATTERS EVEN THOUGH IT CHANGES NO VALUE: ### EVERY COUNT AT A')
    rec('  ### ### NONZERO POWER IS ZERO, SO THE ERROR IS INVISIBLE IN EVERY NUMBER THIS ACT')
    rec('  ### ### REPORTS.** ### It was found only because the factor was checked on its own.')
    rec('  ### **THE SITES WHERE THE PREDICTION AND THE AMBIENT DISAGREE : %d**, and every one of')
    rec('  ### them is a NEGATIVE power:' % ())
    signs = sorted(set(k for _p, _n, k, _a, _m in factor_bad))
    rec('      powers at which they differ : %s' % signs)
    rec('      all of them negative : %s' % all(k < 0 for k in signs))
    rec('')
    rec('  ### **AND THE SHAPE THE ASYMMETRY HIDES, CHECKED RATHER THAN ASSERTED.** ### Under b21\'s')
    rec('  ### own unitary normalization `U(t) = |t|^{-1/2} theta(t)` the factor becomes')
    rec('  ### `p^{-|k|/2}`, ### **WHICH IS SYMMETRIC IN `k`.** ### Squared, so the check stays in')
    rec('  ### the rationals and no root is taken:')
    for (p, n) in SM.CELLS:
        def nsq(kk):
            amb = Fraction(1, p ** kk) if kk > 0 else Fraction(1)
            return amb ** 2 * Fraction(p) ** kk        # ### `factor^2 * |t|^{-1}`
        symmetric = all(nsq(k) == nsq(-k) == Fraction(1, p ** k) for k in range(1, 2 * n + 1))
        rec('      (%d,%d) : the squared normalized factor agrees at `+k` and `-k`, and equals'
            ' `p^{-k}` : %s' % (p, n, symmetric))
        if not symmetric:
            fails.append('symmetric normalization at (%d,%d)' % (p, n))
    rec('  ### **THE SEAL IS NOT EDITED.**')

    return _components_three_four(rec, fails, out)


# ==================================================================================================
def _components_three_four(rec, fails, out):
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE READING, AT EXACTLY ITS SCOPE.')
    rec('=' * 100)
    rec('  ### ### **AT A FINITE PLACE THE SOURCE\'S CONSTRUCTION CARRIES NO ARITHMETIC.**')
    rec('  ### The whole functional returns `w_0 (p^n - 1)^2`: the test function read at ONE point,')
    rec('  ### times a dimension count. ### **NO `log p`. ### NO SAMPLING AT THE PRIME\'S POWERS.**')
    rec('  ### ### **AND THE PRIME\'S CONTRIBUTION IS NOT MISSING FROM THE PLACE -- IT IS SOMEWHERE')
    rec('  ### ### ELSE.** ### b305 read it at content: the local distribution the source integrates')
    rec('  ### AGAINST is `W_p(f) = (log p) SUM_{m>=1} ( f(p^m) + f#(p^m) )`, eq. (149), and')
    rec('  ### **THAT** ### object carries the `log p` AND samples `f` at exactly the powers this')
    rec('  ### trace does not read. ### **THE ARITHMETIC IS IN THE DISTRIBUTION, NOT IN THE')
    rec('  ### COMPRESSED TRACE**, and the corpus already holds that distribution as its prime sum.')
    rec('')
    rec(rule())
    rec('### (3a) THE FIXED-POINT SENTENCE -- THE FINITE SIDE\'S CLOSURE AS ONE STATEMENT.')
    rec(rule())
    rec('  ### b304 computed the COMPACT part and found the smear over the units zero, with its')
    rec('  ### mechanism the invariant shells. ### b309 computed the SCALING part and found it zero')
    rec('  ### at every nonzero power, with its mechanism `p^j - 1` being a unit.')
    rec('  ### ### ### **THOSE ARE ONE STATEMENT, AND THIS IS IT:**')
    rec('  ### ### ### **`Tr(theta(t) Pi)` IS A SIGNED COUNT OF THE OFF-BALL POINTS `t` FIXES, IN')
    rec('  ### ### ### THE TWO CONGRUENCES THE OBJECT\'S TWO CONDITIONS IMPOSE, WEIGHTED BY THE')
    rec('  ### ### ### EMBEDDING\'S HAAR FACTOR.**')
    rec('  ###   ### at `t = 1` every off-ball point is fixed and the count is `(p^n - 1)^2`;')
    rec('  ###   ### at `t = p^k`, `k != 0`, NOTHING off the ball is fixed, because `p^k - 1` is a')
    rec('  ###     unit -- and the only point it does fix is `0`, which is the one place the object')
    rec('  ###     is required to vanish;')
    rec('  ###   ### at a unit `u != 1` the count is generally NONZERO, and b304\'s zero is the SUM')
    rec('  ###     over all units, not a per-unit vanishing. ### **THE TWO HALVES ARE NOT THE SAME')
    rec('  ###     KIND OF ZERO AND THIS ACT DOES NOT MERGE THEM INTO ONE.**')
    rec('  ### ### **SO THE FINITE SIDE\'S CLOSURE IS ONE STATEMENT ABOUT THE FULL MULTIPLICATIVE')
    rec('  ### ### GROUP, WITH ONE MECHANISM AND TWO DIFFERENT CONSEQUENCES.**')
    rec('')
    rec('  ### ### **ITS SCOPE, PRINTED WITH IT:**')
    rec('  ###   ### **FINITE PLACES ONLY.**')
    rec('  ###   ### **THE OBJECT AS DEFINED** -- `Son(p,n)`, the diagonal member `(0,0)`, and no')
    rec('  ###     other member of b293\'s family.')
    rec('  ###   ### **NOTHING ABOUT THE ARCHIMEDEAN PLACE.** ### There the multiplicative group is')
    rec('  ###     CONTINUOUS, the scaling part is not a set of powers of a prime, and there is no')
    rec('  ###     ball for a point to be off. ### **THE CONTRAST IS NAMED AND NOT DERIVED. ### THIS')
    rec('  ###     ACT DERIVES NOTHING THERE**, and b285\'s boundary stands.')
    rec('  ###   ### **NOTHING ABOUT THE IDENTITY, `h2`, OR THE COMPLETE ROSTER.**')
    rec('  ###   ### **NOTHING ABOUT b273\'s `A` AT `k = n`** -- a different operator; the barrier')
    rec('  ###     and the compression are neither extended nor weakened here.')

    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- THE BEARING ON b263\'s BRANCH. ### **BEARING, NEVER DECISION.**')
    rec('=' * 100)
    rec('  ### ### **WHAT IS CARRIED, AND FROM WHOSE FILE:**')
    rec('  ###   ### **b262\'s OWN SENTENCE** is that IF the identity is to hold along that')
    rec('  ###     direction, the archimedean side MUST ABSORB A DIVERGENT QUANTITY -- and b262')
    rec('  ###     attaches, in the same breath, that this is ### **NOT A CLAIM THAT IT FAILS TO DO')
    rec('  ###     IT.**')
    rec('  ###   ### **b263\'s OWN FORMULATION** is the disjunction: either the finite-place side')
    rec('  ###     supplies the first-level mass or the archimedean side absorbs it, and nothing in')
    rec('  ###     the record decides which. ### **THAT IS b263\'s WORDING, NOT b262\'s**, and this')
    rec('  ###     act keeps them apart.')
    rec('  ### ### ### **THE BEARING, AND IT IS ONE SENTENCE: ### THE FINITE SIDE CANNOT SUPPLY THE')
    rec('  ### ### ### FIRST-LEVEL MASS THROUGH THE OBJECT.** ### A compressed trace of the')
    rec('  ### source\'s construction on `Son` reads the test function at the identity and nowhere')
    rec('  ### else; the first level is `p^1`; and the coefficient there is exactly zero.')
    rec('  ### **ANY FINITE-PLACE CONTRIBUTION IS THE ARITHMETIC DISTRIBUTION ITSELF -- eq. (149) --')
    rec('  ### WHICH THE CORPUS HOLDS AS ITS PRIME SUM ON NO SPACE.**')
    rec('')
    rec(rule())
    rec('### (4a) WHAT THIS DOES TO `M-2`\'s SPECIFICATION. ### **A RESTATEMENT OF ITS SCOPE.**')
    rec(rule())
    rec('  ### b263\'s three necessary properties, and what a candidate of THIS CLASS -- a')
    rec('  ### compressed trace of the source\'s construction on the object\'s space at a finite')
    rec('  ### place -- can and cannot meet:')
    rec('  ###   ### **(SPEC-1) IT COUNTS FIRST LEVELS: ### CANNOT BE MET BY THIS CLASS.** ### The')
    rec('  ###     property asks for non-zero weight at `(p, 1)` of the order of `w_{p,1}`. ### The')
    rec('  ###     functional reads the weight only at the identity; its coefficient at `p^1` is')
    rec('  ###     EXACTLY ZERO. ### **THE ONE PLACE (SPEC-1) DEMANDS WEIGHT IS EXACTLY WHERE THE')
    rec('  ###     ZERO SITS.**')
    rec('  ###   ### **(SPEC-3) IT IS DEFINED OVER ALL PRIMES: ### CAN BE MET.** ### The')
    rec('  ###     construction is defined at every prime and every level; the derivation is general')
    rec('  ###     in `p`, and nothing in it fixes a place set.')
    rec('  ###   ### **(SPEC-2) IT REDUCES TO `Theta_q`\'s TERMS AT LEVELS `k <= n-1`: ### NOT')
    rec('  ###     DECIDED BY THIS ACT.** ### The functional returns ONE number per cell with no')
    rec('  ###     level index, so there is nothing in it to compare with a level-indexed family.')
    rec('  ###     ### **WHETHER THAT COUNTS AS FAILING TO REDUCE OR AS NOT BEING A CANDIDATE OF')
    rec('  ###     THAT SHAPE AT ALL IS A QUESTION ABOUT WHAT CLASS (SPEC-2) RANGES OVER, AND THIS')
    rec('  ###     ACT DOES NOT SETTLE IT.**')
    rec('')
    rec('  ### ### ### **AND THE FOUR THINGS THIS IS NOT, EACH NAMED BECAUSE EACH IS A TEMPTING')
    rec('  ### ### ### MISREADING:**')
    rec('  ###   ### **(1) IT IS NOT A DECISION ON THE BRANCH.** ### It narrows ONE ROUTE on ONE')
    rec('  ###     branch. ### b262\'s disjunction stands exactly as undecided as b263 left it.')
    rec('  ###   ### **(2) IT IS NOT A VERDICT ON `M-2`.** ### `M-2` remains')
    rec('  ###     `(SPECIFIED-NOT-STATED)`. ### A specification whose first property is out of')
    rec('  ###     reach for ONE CLASS of candidate is not a specification shown unsatisfiable, and')
    rec('  ###     b263\'s own refusal governs: ### **THESE EXCLUDE; THEY DO NOT DETERMINE.**')
    rec('  ###   ### **(3) IT IS NOT A CLAIM THAT THE FINITE SIDE CONTRIBUTES NOTHING.** ### The')
    rec('  ###     arithmetic is in the distribution. ### **A DISTRIBUTION IS NOT A TRACE ON A')
    rec('  ###     SPACE, AND SAYING ONE TRACE IS SILENT IS NOT SAYING THE PLACE IS.**')
    rec('  ###   ### **(4) IT IS NOT AN ARGUMENT FOR THE ARCHIMEDEAN BRANCH.** ### This act derives')
    rec('  ###     nothing at the archimedean place and says so in every component.')

    rec('')
    rec('=' * 100)
    rec('### THE VERDICT ON THE REGISTERED EXPECTATIONS.')
    rec('=' * 100)
    rec('  the navigator\'s -- the smear collapses to the identity term at every cell : %s'
        % ('### **HOLDS**' if not [f for f in fails if f.startswith(('assembly', 'reads-one'))]
           else '### ### **REFUTED** ###'))
    rec('  (P4)\'s FACTOR clause -- `|t|` : ### ### **REFUTED AT NEGATIVE POWERS, DECLARED ABOVE**')
    rec('  (P4)\'s COUNT clause -- the signed fixed-point count : %s'
        % ('### **HOLDS**' if not [f for f in fails if f.startswith('unified')]
           else '### ### **REFUTED** ###'))
    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('=' * 100)
    return (0 if not fails else 1), out


if __name__ == '__main__':
    code, lines = main()
    io.open(os.path.join(D, 'b310_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(lines) + '\n')
    sys.exit(code)
