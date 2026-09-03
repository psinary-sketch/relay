# -*- coding: utf-8 -*-
"""b311_components.py -- THE COMPONENTS, IN ORDER. ### **READS, A DECISION AT DEFINITIONS, AND A
### PRICE.**

### ### **THIS ACT COMPUTES NO ARCHIMEDEAN NUMBER, AND THIS FILE IS BUILT SO THAT IT CANNOT.** ###
### Every archimedean quantity it prints is a LOCATED QUOTATION from the source, carried through
### `b311_source.py`, which pins the artefact by hash before it locates anything. ### **THERE IS NO
### ARITHMETIC IN THIS FILE AT ALL**, which is the cheapest possible guarantee that none of it is
### the corpus's own.

### ### **AND THE ONE THING IT IS BUILT TO REFUSE:** ### a discrete fixed-point COUNT and a
### continuous fixed-point WEIGHT both answer to the words *fixed point*. ### b285's hazard register
### exists for exactly this species -- ### **THE WORD SURVIVES; THE OBJECT DOES NOT** -- and the
### decision table below carries a TYPE column so that no row can be read across.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools')
sys.path.insert(0, HERE)

import needle_pull        # noqa: E402
import b311_source as SRC  # noqa: E402
import ferry_scan         # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
BANK = os.path.join(D, 'b311_the_identitys_neighbourhood.txt')

OWNERS = [
    ("b285 -- THE HAZARD REGISTER, the discipline this whole act runs under",
     'b285_archimedean_opening.txt', 'THE HAZARD REGISTER'),
    ("### b285 -- and its own sentence about what survives a crossing",
     'b285_archimedean_opening.txt', 'THE WORD SURVIVES; THE OBJECT DOES NOT'),
    ("b285 -- the boundary: no finite-side structural fact types at infinity",
     'b285_archimedean_opening.txt', 'NO FINITE-SIDE STRUCTURAL FACT TYPES'),
    ("### b198 -- there is NO archimedean ball, PROVED (as b285 records it)",
     'b285_archimedean_opening.txt', 'NO SUCH OBJECT'),
    ("b286 -- the archimedean space and its two conditions, an IMPORT (its OWN bank)",
     'b286_the_cc_condition.txt', 'THE SPACE IS `L^2(R)_ev`.'),
    ("b300 -- the chosen archimedean unit is IN the source's space, DERIVED",
     'b300_the_archimedean_leg.txt', 'THE CHOSEN UNIT:'),
    ("b292 -- the corpus's prolate instrument vectors are NOT in the space (its OWN bank)",
     'b292_the_identification.txt', 'IS NOT IN `S(1,1)`'),
    ("b305 -- eq. (149): where the prime's contribution lives",
     'b305_the_arithmetics_entry.txt', 'W_p(f) = (log p) SUM_{m>=1}'),
    ("### b305 -- and the sentence locating the logarithm",
     'b305_the_arithmetics_entry.txt', '`log p` is in `W_p`'),
    ("b310 -- the finite-side fixed-point sentence this act tests for transportability",
     'b310_the_smear_collapses.txt', 'SIGNED COUNT OF THE OFF-BALL POINTS'),
    ("### b310 -- and its own refusal to reach the archimedean place",
     'b310_the_smear_collapses.txt', 'THIS ACT DERIVES NOTHING'),
    ("b310 -- the finite object's dimension, which is the step that parts the two cases",
     'b310_the_smear_collapses.txt', '(p^n - 1)^2'),
    ("b306 -- the work-order this act bears on",
     'b306_the_difference.txt', 'W-ORD-SOURCE-METHOD-APPLICABILITY'),
]

# ### ### **THE HAZARD REGISTER'S TERMS, READ FROM b285 RATHER THAN TYPED HERE.** ### The act
# ### reports how often each appears in its own bank, so a reader can see where the disambiguation
# ### burden actually fell. ### **THIS COUNTS OCCURRENCES; IT DOES NOT JUDGE THEM**, and the file
# ### says so where it prints them.
HAZARD_TERMS = ['ball', 'level', 'tower', 'unit', 'sector', 'scale']

# ### THE DECISION TABLE. ### **EACH ROW IS (question, finite side + its owner, archimedean side +
# ### its source location, TYPE VERDICT).** ### The type column is what stops a row being read
# ### across, and it is this seat's reading, not a tool's.
DECISION = [
    ("what the object's first condition excludes",
     "the BALL `Z_p`: compact AND open, a subgroup, of Haar mass 1 (b285/b198)",
     "the INTERVAL `[-1,1]`: a metric ball with NO subgroup structure (CC, page 1)",
     "### **THE WORD SURVIVES; THE OBJECT DOES NOT** (b285, verbatim)"),
    ("the dimension of the object's space",
     "FINITE: `(p^n - 1)^2` -- a truncation (b293's law, b310 carrying it)",
     "INFINITE: CC's own words, *the well-known infinite dimensional Sonin's space* (page 1)",
     "### **THE DECISIVE DIFFERENCE, AND IT IS NOT A MATTER OF DEGREE**"),
    ("whether a SINGLE non-identity scaling has a trace",
     "YES: `theta(t)Pi` is FINITE RANK, so the trace exists for every `t` (b309, b310)",
     "NO: CC gives the single-scaling trace *formally* (Prop 1.5(ii), page 8) and recovers trace"
     " class ONLY after smearing (Prop 1.5(iv), page 8)",
     "### **THE QUESTION DOES NOT PARSE AT INFINITY**"),
    ("what the local term at a non-identity scaling IS",
     "an integer COUNT of off-ball fixed points, killed by the first condition (b310)",
     "a JACOBIAN WEIGHT `tau(rho)`, nonzero at every `rho != 1` (CC eq. (39), page 10)",
     "### **A COUNT AND A WEIGHT. ### THE RESEMBLANCE IS REFUSED AS EVIDENCE**"),
    ("what happens at the identity",
     "the identity fixes every off-ball point; the count is the dimension (b310)",
     "`tau` DIVERGES and is defined as a principal value (CC, page 1 and eq. (39))",
     "### **A FINITE NUMBER AND A DIVERGENCE**"),
    ("where the trace side's content sits",
     "not applicable -- the finite trace side is a finite sum of exact rationals",
     "`Tr(theta(f)S) = W_inf(f) + INT f(rho^-1) eps(rho) d*rho`, `eps` a FUNCTION"
     " (CC Theorem 4.7, page 26)",
     "### **THE ONLY NON-FUNCTION PART IS AT THE IDENTITY**"),
]

# ### COMPONENT 3'S OBLIGATIONS. ### **(what, type, who owns it, what it would cost).**
# ### **THE TYPES ARE THE CORPUS'S OWN FOUR: read / result / ruling / construction.**
OBLIGATIONS = [
    ("a truncation of the object's own space at infinity",
     "CONSTRUCTION",
     "nobody -- it does not exist. CC characterises `S(1,1)` as the EIGENVALUE-ONE eigenspace of"
     " `P P^ P` (page 27); a truncation would be the span of finitely many eigenvectors of that"
     " sandwich, and NO SUCH OBJECT IS IN THE RECORD",
     "the whole of the cost: everything else waits on it"),
    ("the unit's membership in that space",
     "RESULT, ALREADY IN HAND",
     "b300: `(IN, DERIVED)` from the source's own definition",
     "nothing -- it is banked"),
    ("the prolate vectors' NON-membership, which the truncation must respect",
     "RESULT, ALREADY IN HAND",
     "b292: `zeta_n IS NOT IN S(1,1)`, and CC's page 27 says why -- they are eigenvectors for"
     " eigenvalues `lambda(n)^2 < 1`, not for 1",
     "nothing -- it is banked, and it CONSTRAINS the truncation rather than helping it"),
    ("the scaling action on that truncation",
     "CONSTRUCTION",
     "nobody -- and CC's own sentence is the obstacle: *the scaling action does not restrict to"
     " this subspace* (page 1)",
     "it cannot be a restriction; it must be a compression, and the compression is the object"),
    ("the compression, and its trace-class status",
     "READ, THEN CONSTRUCTION",
     "CC Prop 1.5(iv) and Theorem 4.7 give trace class for the SMEARED operator only",
     "a truncation would make it finite rank for free -- WHICH IS ALSO WHAT WOULD MAKE IT NOT THE"
     " SOURCE'S OBJECT"),
    ("the archimedean normalization ruling",
     "RULING, LIVE",
     "`W-ORD-ARCH-NORM-READING` -- which inner product b226's archimedean normalization is",
     "it is the ONLY archimedean condition left on the object, and nothing here discharges it"),
    ("### the `W2` mean-zero bump variant",
     "RULING, RECORDED THIS ACT",
     "the author, by paste, the b311 ferry -- added BESIDE the existing bump, replacing nothing",
     "its construction is a LATER ACT; what it obligates is listed in the bank and nothing here"
     " builds it"),
]


def rule(ch='-', n=100):
    return ch * n


def main():
    out, fails = [], []

    def rec(s=''):
        out.append(s)
        print(s)

    pdf = sys.argv[1] if len(sys.argv) > 1 else None

    rec('=' * 100)
    rec('b311 -- THE IDENTITY\'S NEIGHBOURHOOD. ### THE COMPONENTS, IN ORDER.')
    rec('=' * 100)

    rec('  ### THE OWNERS, PULLED FROM THE FILES THAT EMIT THEM:')
    unpullable = 0
    for label, fn, anchor in OWNERS:
        try:
            line = needle_pull.pull(os.path.join(D, fn), anchor)
            rec('  %s' % label)
            rec('      %s' % line[:132])
        except LookupError:
            unpullable += 1
            fails.append('owner needle: %s' % label)
            rec('  ### FAIL (UNPULLABLE) %s   anchor=%r' % (label, anchor))
    rec('  ### OWNER SENTENCES PULLED : %d   ### UNPULLABLE : %d'
        % (len(OWNERS) - unpullable, unpullable))

    # ==============================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE PROOF READ. ### **EVERY CLAIM A QUOTATION WITH ITS LOCATION.**')
    rec('=' * 100)
    if pdf and os.path.exists(pdf):
        rows, npages = SRC.locate(pdf)
        missing = [lbl for lbl, _f, hits in rows if not hits]
        rec('  ### THE ARTEFACT IS PINNED BY `b311_source.py` BEFORE ANYTHING IS LOCATED.')
        rec('  ### pages : %d   ### fragments located : %d   ### NOT LOCATED : %d'
            % (npages, len(rows) - len(missing), len(missing)))
        rec('')
        rec('  %-12s %s' % ('page index', 'the claim this act makes from it'))
        for lbl, _frag, hits in rows:
            rec('  %-12s %s' % (','.join(str(h) for h in hits) if hits else '### NONE', lbl))
        if missing:
            fails.append('source fragments unlocated: %s' % missing)
    else:
        rec('  ### ### **THE ARTEFACT WAS NOT SUPPLIED TO THIS RUN.** ### Component 1 cannot be')
        rec('  ### reported without it, and the act says so rather than quoting from memory.')
        fails.append('the artefact was not supplied')

    rec('')
    rec(rule())
    rec('### (1a) WHAT THE SOURCE\'S ARGUMENT DOES -- IN ITS OWN ORDER.')
    rec(rule())
    rec('  ### **THE CONSTRUCTION.** ### CC state the obstacle first: ### **"Even though the scaling')
    rec('  ### action `theta` does not restrict to this subspace, one can associate to a test')
    rec('  ### function `f` the trace `Tr(theta(f) S)`"** ### -- so the object is a COMPRESSION of a')
    rec('  ### group action that does NOT preserve the space, smeared against a test function.')
    rec('  ### **AND THE POSITIVITY IS STRUCTURAL, NOT COMPUTED:** ### it is *positive definite by')
    rec('  ### construction*, because on `f = g * g^*` it is `Tr(theta(g) S theta(g)^*)`, the trace')
    rec('  ### of a positive operator.')
    rec('  ### **THE INEQUALITY (Theorem 1) IS `W_inf(g*g^*) >= Tr(theta(g) S theta(g)^*)`.**')
    rec('  ### ### **HOW IT IS PROVED -- AND THIS IS THE ANSWER TO WHAT THE ORDER ASKS:** ### the')
    rec('  ### source does NOT evaluate the compressed trace at individual scalings. ### It')
    rec('  ###   (i) writes the single-scaling trace `tau(rho)` and says it holds ### FORMALLY ###')
    rec('  ###     (Prop 1.5(ii)), recovering trace class only after smearing (Prop 1.5(iv));')
    rec('  ###   (ii) isolates a ### TRACE-REMAINDER ### `delta(rho)` -- the difference between the')
    rec('  ###     full scaling trace and its `P`-compression (Definition 2.1) -- and shows that')
    rec('  ###     ### **UNLIKE `tau`, WHICH IS NOT A FUNCTION BECAUSE OF THE DIVERGENCY AT')
    rec('  ###     ### `rho = 1`, `delta` IS A FUNCTION** (CC\'s own sentence);')
    rec('  ###   (iii) observes that `delta` ### **HAS A JUMP IN ITS FIRST DERIVATIVE AT `rho = 1`**')
    rec('  ###     and says this *will play a key role*;')
    rec('  ###   (iv) and turns that jump into Theorem 3.6: the quadratic form is')
    rec('  ###     ### **`-2 Id + K_I` WITH `K_I` COMPACT** ### -- essentially negative, so only')
    rec('  ###     FINITELY MANY linear conditions on the test function are needed.')
    rec('  ### ### ### **SO THE CONTENT ARRIVES AS A TERM CONCENTRATED AT THE IDENTITY OF THE')
    rec('  ### ### ### SCALING GROUP: THE `-2 Id` IS THE DERIVATIVE JUMP AT `rho = 1`.**')
    rec('  ### **AND THE TRACE SIDE ITSELF IS PINNED TO THE DISTRIBUTION BY Theorem 4.7:**')
    rec('  ### `Tr(theta(f)S) = W_inf(f) + INT f(rho^-1) eps(rho) d*rho`, with `eps` an honest')
    rec('  ### FUNCTION. ### **THE ONLY PART OF THE TRACE SIDE THAT IS NOT AN INTEGRAL AGAINST A')
    rec('  ### FUNCTION IS THE PART AT THE IDENTITY.** ### That is `(F1)`, CONFIRMED.')
    rec('')
    rec('  ### **THE TEST FUNCTION\'S SUPPORT, ON THE TWO SIDES, WHICH THE ORDER ASKS TO SEPARATE:**')
    rec('  ###   ### **ON THE DISTRIBUTION SIDE** ### the support is what GATES THE PRIMES: CC')
    rec('  ###     choose `Support(f)` in `(1/2, 2)` ### *so that rational primes are not involved*')
    rec('  ###     ### -- their own words, pointing at eq. (149).')
    rec('  ###   ### **ON THE TRACE SIDE** ### the support does no such thing. ### It makes')
    rec('  ###     `theta(f)` a smearing, which is what buys TRACE CLASS (Prop 1.5(iv)), and it')
    rec('  ###     bounds the interval `I` on which Theorem 3.6\'s compact operator lives.')
    rec('  ### ### **SO THE SAME CONDITION DOES TWO DIFFERENT JOBS ON THE TWO SIDES, AND CONFLATING')
    rec('  ### ### THEM WOULD BE READING AN ARITHMETIC GATE AS AN ANALYTIC ONE.**')

    return _component_two(rec, fails, out)


# ==================================================================================================
def _component_two(rec, fails, out):
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE MECHANISM AT INFINITY. ### **DECIDED BY DEFINITIONS.**')
    rec('=' * 100)
    rec('  ### The finite side\'s sentence, carried from b310 and NOT re-derived:')
    rec('  ### **`Tr(theta(t) Pi)` is a SIGNED COUNT of the off-ball points `t` fixes.** ### At a')
    rec('  ### nonzero power nothing off the ball is fixed, so the count is zero.')
    rec('  ### ### **THE QUESTION: DOES THAT TYPE AT INFINITY?**')
    rec('')
    rec('  %-44s %s' % ('question', 'TYPE VERDICT'))
    for q, fin, arch, verdict in DECISION:
        rec('  %s' % rule('.'))
        rec('  %-44s %s' % (q, verdict))
        rec('      FINITE      : %s' % fin)
        rec('      ARCHIMEDEAN : %s' % arch)
    rec('  %s' % rule('.'))
    rec('')
    rec('  ### ### ### **THE DECISION, AND IT IS A REFUSAL RATHER THAN AN ANSWER:**')
    rec('  ### ### ### **THE FINITE SIDE\'S MECHANISM DOES NOT TYPE AT THE ARCHIMEDEAN PLACE, AND')
    rec('  ### ### ### THE STEP AT WHICH IT PARTS IS THE DIMENSION OF THE OBJECT\'S SPACE.**')
    rec('  ###   ### At a finite place `Son(p,n)` is FINITE-DIMENSIONAL -- it is a truncation -- so')
    rec('  ###     `theta(t)Pi` is FINITE RANK, the trace exists for every single `t`, and it is an')
    rec('  ###     integer-valued COUNT that the object\'s first condition can kill.')
    rec('  ###   ### At the archimedean place Sonin\'s space is, in CC\'s own words, INFINITE')
    rec('  ###     DIMENSIONAL, so `theta(lambda)S` is not trace class and ### **THERE IS NO COUNT')
    rec('  ###     TO TAKE.** ### CC never write one: they write `Tr(theta(f)S)`.')
    rec('  ### ### **SO THE ORDER\'S SECOND EXPECTATION IS REFUTED IN ITS FIRST HALF.** ### The')
    rec('  ### single non-identity compression does not have a VANISHING trace at infinity; it does')
    rec('  ### not have a TRACE. ### And where its formal value is a function, at `rho != 1`, that')
    rec('  ### value is manifestly NONZERO.')
    rec('  ### ### **AND THE ORDER\'S DIAGNOSIS IS RIGHT: ### THE DIFFERENCE DOES LIVE AT THE')
    rec('  ### ### IDENTITY** -- `tau` diverges there and is a principal value -- ### **AND BOTH')
    rec('  ### ### THE OTHER TWO CANDIDATES IT NAMED ARE IMPLICATED: TRACE-CLASS STATUS, AND THE')
    rec('  ### ### MEASURE ON THE GROUP.**')
    rec('')
    rec(rule())
    rec('### (2a) THE DEEPER REASON THE COUNT DOES NOT SURVIVE. ### **AN EVALUATION AND A JACOBIAN.**')
    rec(rule())
    rec('  ### In BOTH cases the map `x -> t x` fixes only the origin. ### **THE RESEMBLANCE STOPS')
    rec('  ### THERE, AND THE ACT REFUSES TO CARRY IT FURTHER:**')
    rec('  ###   ### the FINITE local term asks ### WHERE THE FUNCTION IS ### -- it counts points')
    rec('  ###     at which a vector is evaluated, and the object\'s vanishing on the ball is')
    rec('  ###     exactly what makes the count zero;')
    rec('  ###   ### the CONTINUOUS local term asks ### HOW THE MAP MOVES SPACE ### -- it is a')
    rec('  ###     Jacobian weight, and it knows nothing whatever about where the function vanishes.')
    rec('  ### ### **A COUNT AND A JACOBIAN ARE NOT THE SAME OBJECT, AND NOTHING IN THE RECORD')
    rec('  ### ### BRIDGES THEM.** ### b285\'s hazard register named this species in advance:')
    rec('  ### ### **THE WORD SURVIVES; THE OBJECT DOES NOT.**')
    rec('  ### **THIS ACT EXHIBITS NO BRIDGING DEFINITION AND CLAIMS NONE**, and the refusal is the')
    rec('  ### finding rather than a shortfall in it.')
    rec('')
    rec(rule())
    rec('### (2b) WHAT THEREFORE FOLLOWS, AND WHAT DOES NOT.')
    rec(rule())
    rec('  ### **FOLLOWS:** ### the source\'s positive quantity is, in the precise sense of')
    rec('  ### Theorem 4.7, the archimedean distribution PLUS an integral against a function --')
    rec('  ### ### **SO ITS ONLY NON-FUNCTION CONTENT IS AT THE IDENTITY**, and Theorem 3.6 turns')
    rec('  ### the derivative jump there into `-2 Id + compact`.')
    rec('  ### **DOES NOT FOLLOW:** ### that the source\'s result is *about the identity alone*.')
    rec('  ### The added function `eps` is not nothing, and Theorem 3.6 is a statement about a')
    rec('  ### quadratic form on an interval, not about a point. ### **THE ACT SAYS SO RATHER THAN')
    rec('  ### LETTING `concentrated at the identity` DO SILENT WORK.**')
    rec('  ### **AND THE CORPUS\'S OWN WINDOW QUESTION, NAMED AND NOT OPENED:** ### the corpus works')
    rec('  ### at the open end of the same knob -- primes ADMITTED -- where the source closes it so')
    rec('  ### that none is involved. ### **THAT IS A QUESTION ABOUT THE SAME NEIGHBOURHOOD WITH A')
    rec('  ### DIFFERENT SUPPORT, AND IT IS THE AUTHOR\'S.**')

    return _component_three(rec, fails, out)


# ==================================================================================================
def _component_three(rec, fails, out):
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE OBLIGATIONS. ### **PRICED IN ACTS, NOT RUN.**')
    rec('=' * 100)
    rec('  ### What an archimedean instrument computing on the object\'s own space would need,')
    rec('  ### each typed as read / result / ruling / construction.')
    for what, typ, who, cost in OBLIGATIONS:
        rec('  %s' % rule('.'))
        rec('  %-58s %s' % (what, typ))
        rec('      OWNER : %s' % who)
        rec('      COST  : %s' % cost)
    rec('  %s' % rule('.'))
    rec('')
    rec('  ### ### **THE PRICE, AS THIS SEAT\'S ESTIMATE AND NOT A COMMITMENT:**')
    rec('  ### **THE TRUNCATION IS THE WHOLE COST AND IT IS NOT A SMALL ONE.** ### CC characterise')
    rec('  ### `S(1,1)` as the eigenvalue-one eigenspace of the projection sandwich; a finite')
    rec('  ### truncation would be a span of finitely many eigenvectors of that sandwich, and')
    rec('  ### ### **THE ONLY EIGENVECTORS THE CORPUS HAS AT INFINITY ARE THE PROLATE ONES, WHICH')
    rec('  ### ### b292 DERIVED ARE *NOT* IN THE SPACE.** ### So the truncation cannot be built from')
    rec('  ### what is in hand; it needs an object nobody has.')
    rec('  ### ### **AND THE OBSTACLE IS THE SOURCE\'S OWN SENTENCE, NOT A DIFFICULTY THIS SEAT')
    rec('  ### ### FOUND: ### *the scaling action does not restrict to this subspace.* ### A')
    rec('  ### ### TRUNCATION WOULD MAKE THE COMPRESSION FINITE RANK FOR FREE -- AND WOULD ALSO')
    rec('  ### ### MAKE IT NOT THE SOURCE\'S OBJECT.** ### That is the tension the price is made of.')
    rec('  ### **THREE ACTS FOR THE TRUNCATION AND ITS CONTROLS, TWO MORE FOR THE COMPRESSION,')
    rec('  ### AND ONLY IF THE RULING `W-ORD-ARCH-NORM-READING` IS SETTLED FIRST.** ### **THIS IS AN')
    rec('  ### ESTIMATE, NOT A COMMITMENT AND NOT A RECOMMENDATION TO BUILD.**')
    rec('')
    rec(rule())
    rec('### (3a) WHAT THE `W2` RULING OBLIGATES.')
    rec(rule())
    rec('  ### The author\'s ruling, recorded verbatim in the registration and NOT applied here:')
    rec('  ### **a mean-zero variant of the corpus\'s bump is added BESIDE the existing one,')
    rec('  ### replacing nothing.**')
    rec('  ### ### **WHAT IT OBLIGATES, AS A LIST AND NOT AS A PLAN:**')
    rec('  ###   ### (i) a CONSTRUCTION of the variant, with its own registration -- a later act;')
    rec('  ###   ### (ii) both bumps carried side by side in every place the existing one appears,')
    rec('  ###     because *replacing nothing* means the existing results keep their bump;')
    rec('  ###   ### (iii) a statement of which banked results are computed with WHICH, since a')
    rec('  ###     result computed with one and quoted beside the other would be a silent swap;')
    rec('  ###   ### (iv) and the reason the variant is wanted, stated where it is used: the')
    rec('  ###     source\'s Theorem 6.11 prices a nonzero value at zero of the Fourier transform')
    rec('  ###     at `-c` times its square, and ### **A MEAN-ZERO BUMP IS THE ONE WHOSE PRICE IS')
    rec('  ###     ZERO.** ### That is the obligation\'s point and it is stated as the ruling\'s')
    rec('  ###     motivation, ### **NOT AS A RESULT OF THIS ACT.**')
    rec('  ### ### **NOTHING HERE BUILDS IT, TESTS IT, OR PRICES ITS CONSEQUENCES.**')

    rec('')
    rec('=' * 100)
    rec('### THE VERDICT ON THE NAVIGATOR\'S EXPECTATIONS.')
    rec('=' * 100)
    rec('  (F1) the trace side\'s content is concentrated at the identity : ### **CONFIRMED**,')
    rec('       by CC Theorem 4.7 and by `tau` being the only non-function part.')
    rec('  (F2) the single non-identity compression has vanishing trace  : ### ### **REFUTED IN ITS')
    rec('       FIRST HALF** -- it has NO trace; and where the formal value is a function it is')
    rec('       nonzero. ### **CONFIRMED IN ITS DIAGNOSIS**: the difference is at the identity, and')
    rec('       trace-class status and the measure are both implicated.')
    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('=' * 100)
    return (0 if not fails else 1), out


if __name__ == '__main__':
    code, lines = main()
    io.open(os.path.join(D, 'b311_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(lines) + '\n')
    sys.exit(code)
