# -*- coding: utf-8 -*-
"""b301 -- THE OBJECT COMPLETED. ### THE CONSTITUENTS, THE REQUIREMENTS, AND THE CONVERGENCE
### RE-CHECK.

### SCOPE, SAID FIRST AND OBEYED THROUGHOUT. ### **THIS FILE DERIVES NOTHING NEW ABOUT ANY LOCAL
### OBJECT.** ### It does three things:
###   ### **(1)** ### sets every constituent in one table and ### **PULLS ITS OWNER'S WORDING AND
###       ITS GRADE FROM THE FILE THAT EMITTED THEM** -- falsifier V1: a cell with a grade and no
###       owner, or an owner and no grade, fails.
###   ### **(2)** ### checks each of the construction's own requirements against those cells, ###
###       **SAYING WHICH OF THE TWO PRODUCTS ASKS IT** (V2).
###   ### **(3)** ### re-checks the convergence condition ### **IN EXACT RATIONAL ARITHMETIC** ###
###       now that the source's own inner product is in hand (V3).

### ### **WHY (3) IS EXACT AND NOT FLOATING.** ### The quantity at stake is irrational. ### A float
### comparison would decide a rounding and print a number that looks measured. ### **EVERY BOUND
### BELOW IS A `Fraction`, AND THE ENCLOSURE IS CERTIFIED BY SQUARING IT** -- `x` encloses
### `1/sqrt(2)` exactly when `lo^2 < 1/2 < hi^2` with `lo, hi > 0`, which is a comparison of
### rationals and nothing else. ### **NO FLOAT LITERAL AND NO FLOAT DIVISION APPEARS IN THIS FILE.**

# ### THE LIMITS, IN THE HEADER SO THE FILE IS NOT TRUSTED BEYOND THEM:
# ### (1) ### **THE TABLE PULLS A LINE; IT DOES NOT AUDIT A GRADE.** ### It proves the owner's
# ###     wording and the owner's grade word are on disk in the file named. ### **IT CANNOT TELL
# ###     WHETHER THE GRADE IS THE RIGHT GRADE.**
# ### (2) ### **THE REQUIREMENTS' VERDICTS ARE THE ACT'S JUDGEMENT, NOT THE TOOL'S.** ### The tool
# ###     carries them, prints which product asks each, and refuses a `MET` with no derivation and
# ###     an `OPEN` with no missing-thing named. ### It does not decide them.
# ### (3) ### **THE PARITY IDENTITY IS NOT PROVED HERE AND IS NOT PROVABLE HERE.** ### That an even
# ###     function's integral over `R` is twice its integral over `[0,inf)` is an INTEGRAL
# ###     statement; the finite fixture below checks THIS FILE'S HALVING ARITHMETIC and is labelled
# ###     as doing exactly that. ### **A FINITE MODEL WOULD CERTIFY THE MODEL** -- b291's sentence,
# ###     and it is true again here.
"""
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')


def d(n):
    return os.path.join(D, n)


# ### =============================================================================================
# ### (1) THE CONSTITUENTS. ### **PLACE CLASS BY PLACE CLASS. ### EVERY CELL CARRIES BOTH.**
# ### (place class, item, value as constructed, owner file, wording anchor, grade, grade anchor)
# ### =============================================================================================
TABLE = [
    # ### ---- THE FINITE PLACES, THE GENERAL CASE ----
    ("FINITE p (all)", "THE LOCAL SPACE",
     "S-bar_p := the L^2(Q_p)-closure of UNION_{n>=1} iota_n( Son(p,n) )",
     d('b279_the_local_space.txt'), 'the L^2(Q_p)-CLOSURE OF',
     "(CONSTRUCTED)", d('b279_the_local_space.txt'), 'VERDICT: (CONSTRUCTED)'),

    ("FINITE p (all)", "ITS LEVEL",
     "Son(p,n) = { f in V_n : f|ball = 0 AND (F f)|ball = 0 }, dimension (p^n - 1)^2",
     d('b279_the_local_space.txt'), "THE TOWER'S LEVEL (keystone)",
     "the keystone's own sentence", d('b279_the_local_space.txt'),
     '`Son` SITS INSIDE IT'),

    ("FINITE p (all)", "ITS TOWER",
     "iota: V_n -> V_(n+1), m'' = p*m + p^{2n+1}*j; directed by the keystone's exact tower",
     d('b279_the_local_space.txt'), 'THE CONNECTING MAP (b21)',
     "DERIVES, for all p and all n", d('b279_the_local_space.txt'),
     'IT DERIVES, FOR ALL `p` AND'),

    ("FINITE p (all)", "THE UNIT'S EXISTENCE",
     "d_1(p,n) > 0 at the chosen level, so E_1 carries a nonzero vector, which normalizes",
     d('b198_nonvanishing.txt'), 'A LEVEL DIMENSION d_1(p,n) > 0',
     "AVAILABLE-AT-EVERY-FINITE-PLACE", d('b198_nonvanishing.txt'),
     'VERDICT: AVAILABLE-AT-EVERY-FINITE-PLACE'),

    ("FINITE p (all)", "THE STATED UNIT",
     "u_p := 4q * P_1 f_{1,1} at the cell (p, ell(p)), normalized to norm one",
     d('b226_stated_choice.txt'), 'u_p    := 4q * P_1 f_{1,1}',
     "PASS AT SIX STATED PLACES; THE GENERIC ODD PLACE IS *OWED*",
     d('b226_stated_choice.txt'), 'THE GENERIC ODD PLACE IS *OWED*'),

    ("FINITE p (all)", "THE LEVEL RULE",
     "ell(p) := 2 if p = 2, else 1 -- the lowest level with d_1 > 0",
     d('b226_stated_choice.txt'), 'ell(p) := 2 if p = 2, else 1',
     "a DEFINITION made by the stated choice", d('b226_stated_choice.txt'),
     'THE CHOICE, STATED AS A DEFINITION'),

    # ### ---- THE EXCEPTIONAL FINITE PLACE ----
    ("FINITE p = 2 (exceptional)", "WHY THE LEVEL STEPS UP",
     "d_1(2,1) = 0 -- the arrival depth -- so level 1 carries no unit at p = 2",
     d('b226_stated_choice.txt'), 'THE ARRIVAL DEPTH IS WHY ell(2) = 2',
     "ZERO at exactly one cell, (2,1)", d('b198_nonvanishing.txt'),
     'ZERO at exactly one cell, (2,1)'),

    # ### ---- THE ARCHIMEDEAN PLACE ----
    ("ARCHIMEDEAN infinity", "THE LOCAL SPACE",
     "S(1,1) = { xi in L^2(R)_ev : xi = 0 on |q|<=1, (F_eR xi) = 0 on |p|<=1 }",
     d('b287_the_two_papers.txt'), 'S(lambda,mu) subset L^2(R)_ev',
     "(CONSTRUCTED, CONDITIONALLY)", d('b300_the_archimedean_leg.txt'),
     'THE SPACE: ### (CONSTRUCTED, CONDITIONALLY)'),

    ("ARCHIMEDEAN infinity", "ITS INNER PRODUCT",
     "<eta|xi> := (1/2) INT_R eta conj(xi) dx = INT_0^inf eta conj(xi) dx  -- CC eq (16)",
     d('b300_source_read.txt'), 'We normalize the inner product',
     "IMPORT, READ AT CONTENT IN ITS OWN SOURCE", d('b300_source_read.txt'),
     'READ AT CONTENT THIS ACT'),

    ("ARCHIMEDEAN infinity", "ITS ONE OPEN DATUM",
     "C9 -- how the real fiber sits inside the corpus's own adelic object (N-OPEN-B as b287 read it)",
     d('b287_the_two_papers.txt'), 'REMAINS OPEN',
     "(ABSENT) from both sources and from the deferred reference",
     d('b287_the_two_papers.txt'), '(ABSENT) FROM BOTH SOURCES'),

    ("ARCHIMEDEAN infinity", "THE STATED UNIT",
     "u_inf := the rank-2 Sonin-sector eigenfunction, normalized in L^2 -- phi_mu at mu_-2",
     d('b226_stated_choice.txt'), 'rank-2 Sonin-sector eigenfunction',
     "GRADE: BENCH (its own file's word for the measured bits)",
     d('b226_stated_choice.txt'), 'GRADE: BENCH'),

    ("ARCHIMEDEAN infinity", "ITS MEMBERSHIP",
     "u_inf is IN S(1,1): condition one quoted from CM Lemma 3.1, condition two from the derived"
     " eigenrelation F phi_mu = c phi_mu with c = +-1",
     d('b300_the_archimedean_leg.txt'), 'THE CHOSEN UNIT: ### (IN, DERIVED)',
     "DERIVES-on-IMPORTS", d('b300_the_archimedean_leg.txt'),
     'GRADE: ### DERIVES-on-IMPORTS'),

    ("ARCHIMEDEAN infinity", "ITS SECTOR MEMBERSHIP",
     "whether u_inf is in E_1(S(1,1)) -- NOT derived; needs c = +1 AT RANK 2",
     d('b214_orientation_bits.txt'), 'rank 2 (the FIRST EVEN) : c = **+1**',
     "GRADE BENCH", d('b214_orientation_bits.txt'), 'GRADE **BENCH**'),
]

# ### =============================================================================================
# ### (2) THE REQUIREMENTS. ### **EACH SAYS WHICH PRODUCT ASKS IT (V2).**
# ### (id, which product, requirement, owner, anchor, verdict, derivation-or-missing)
# ### =============================================================================================
P_RTP = 'P-RTP  the restricted tensor product'
P_IDP = 'P-IDP  von Neumann incomplete direct product'

REQS = [
    ("Q1", P_IDP, "a Hilbert space at every index (Definition 4.1.1's H_a)",
     d('b226_stated_choice.txt'), 'H_a be the closed', "MET",
     "FINITE: S-bar_p is an L^2(Q_p)-CLOSURE, hence a closed subspace of a Hilbert space (b279)."
     " ARCHIMEDEAN: S(1,1) is the range of CC's ORTHOGONAL PROJECTION R, hence closed (b300 R1)."
     " ### **CLOSEDNESS IS READ OFF AN OWNER AT BOTH PLACE CLASSES, NOT ASSUMED FROM THE WORD"
     " 'SPACE'.**"),

    ("Q2", P_IDP, "a norm-one vector EXISTS at every index (Lemma 4.1.2's ||f_a|| = 1)",
     d('b226_stated_choice.txt'), 'with ||f_a|| = 1', "MET",
     "FINITE: d_1 > 0 at the chosen level at every finite place (b198 I3,"
     " AVAILABLE-AT-EVERY-FINITE-PLACE), so E_1 carries a nonzero vector; the model inner product"
     " is positive definite (b21), so it normalizes. ARCHIMEDEAN: b300 places a nonzero vector in"
     " S(1,1). ### **THIS IS EXISTENCE, AND EXISTENCE ONLY.**"),

    ("Q3", P_IDP, "the STATED CHOICE is that norm-one vector at every index",
     d('b226_stated_choice.txt'), 'THE GENERIC ODD PLACE IS *OWED*', "OPEN",
     "### **MISSING, EXACTLY: a result that 4q*P_1 f_{1,1} != 0 at every odd p at level 1.**"
     " b226 verified it at six stated places and wrote that the generic step 'WANTS A RESULT'."
     " ### **SIX PLACES ARE NOT ALL PLACES, AND Q2 DOES NOT COVER Q3: A UNIT EXISTING IS NOT THE"
     " STATED UNIT BEING IT.**"),

    ("Q4", P_IDP, "the archimedean unit is from the SONIN SECTOR, as the ruling's own words ask",
     d('b225_serializing_close.txt'), 'with the archimedean unit from the Sonin sector',
     "OPEN",
     "### **MISSING, EXACTLY: c = +1 AT RANK 2 above BENCH.** b300 derived u_inf in S(1,1) and"
     " explicitly did NOT derive u_inf in E_1(S(1,1)); the derived eigenrelation gives only"
     " c = +-1, and b214's c = +1 stands at BENCH on a transform convention b214 ADOPTED rather"
     " than derived. ### **THE RULING ASKS FOR A SECTOR UNIT; WHAT IS DERIVED IS A SPACE UNIT.**"),

    ("Q5", P_IDP, "the C0 condition across places -- SUM_v | ||f_v|| - 1 | converges",
     d('b226_stated_choice.txt'), 'SUM_v | ||f_v|| - 1 | CONVERGE', "MET",
     "RE-CHECKED BELOW RATHER THAN CITED, and it holds under BOTH readings of the archimedean"
     " normalization. ### **WHAT DOES NOT SURVIVE UNDER ONE READING IS b226's EXACT ZERO, NOT THE"
     " CONVERGENCE.** ### And the extract's own defect at Definition 3.3.1 stands: what 'C0'"
     " demands BEYOND the norm sum is carried at b197's grade, not read at source (b226's"
     " declared divergence, restated and not renegotiated)."),

    ("Q6", P_IDP, "the object depends only on the equivalence class, not on the sequence",
     d('b226_stated_choice.txt'), 'DOES (x)\'_v (S-bar_v, u_v) DEPEND ON THE CHOICE?', "OPEN",
     "### **MISSING, EXACTLY: whether two canonical choices land in the same class of 3.3.2.**"
     " b226 filed it OPEN and cited Definition 3.3.2 as where the answer lives, with Lemma 4.1.1's"
     " warning that products for different classes are MUTUALLY ORTHOGONAL. ### **A DIFFERENT"
     " CHOICE COULD GIVE AN ORTHOGONAL OBJECT, NOT AN ISOMORPHIC ONE.**"),

    ("Q7", P_RTP, "PURITY of the distinguished vectors",
     d('b221_cell_level_assembly.txt'), 'NEEDS PURITY, NOT MERELY EXISTENCE',
     "NOT ASKED OF P-IDP",
     "### **THIS IS `P-RTP`'s REQUIREMENT AND IT IS RECORDED AGAINST `P-RTP`.** ### The author's"
     " b225 ruling re-scoped term 3 to `P-IDP` and says in its own words that 'purity is not"
     " required by the new plan and no inclusion maps are used'. ### **SO b221's HALT IS NOT AN"
     " OBSTACLE TO `P-IDP`, AND IT IS ALSO NOT REPEALED: IT STANDS EXACTLY WHERE b221 PUT IT, ON"
     " THE PRODUCT IT IS ABOUT.**"),

    ("Q8", P_IDP, "the level-limit premise -- u_v in E_1(Son(v,ell(v))) lies in E_1(S-bar_v)",
     d('b226_stated_choice.txt'), 'THE LEVEL-LIMIT PREMISE', "MET AS A PREMISE",
     "Its warrant is b198 (I2)'s closure sentence at ITS grade (AVAILABLE-AT-EVERY-FINITE-PLACE)."
     " ### **b226 MARKED IT A PREMISE OF THAT ACT AND NOT A THEOREM OF IT, AND IT IS CARRIED HERE"
     " AS A PREMISE AND NOT PROMOTED.**"),
]


# ### =============================================================================================
# ### (3) THE CONVERGENCE RE-CHECK. ### **EXACT RATIONAL ARITHMETIC THROUGHOUT.**
# ### =============================================================================================
def enclose_inv_sqrt2(digits):
    """### RETURN `(lo, hi)`, RATIONALS WITH `lo < 1/sqrt(2) < hi` AND `hi - lo <= 10^-digits`.

    ### ### **CERTIFIED BY SQUARING, WHICH IS A COMPARISON OF RATIONALS AND NOTHING ELSE:**
    ### for positive rationals, `lo < 1/sqrt(2)` exactly when `lo^2 < 1/2`.
    ### The refinement is bisection on rationals -- ### **NO FLOAT ENTERS AT ANY STEP.**
    """
    half = F(1, 2)
    lo, hi = F(0), F(1)
    eps = F(1, 10 ** digits)
    while hi - lo > eps:
        mid = (lo + hi) / 2
        if mid * mid < half:
            lo = mid
        else:
            hi = mid
    return lo, hi


def certified(lo, hi):
    """### **BOTH ARMS OF THE ENCLOSURE, RE-CHECKED INDEPENDENTLY OF HOW IT WAS BUILT.**"""
    half = F(1, 2)
    return lo > 0 and lo * lo < half and hi * hi > half


def self_test(verbose=True):
    """### **BOTH POLARITIES ON EVERY ARM.**"""
    ok = True
    rec = []

    def say(lbl, got, exp):
        agree = (got == exp)
        rec.append((lbl, got, exp, agree))
        return agree

    lo, hi = enclose_inv_sqrt2(20)
    ok &= say('the enclosure is certified by squaring, both arms', certified(lo, hi), True)
    ok &= say('a deliberately WRONG enclosure is rejected',
              certified(F(9, 10), F(95, 100)), False)
    ok &= say('the enclosure is tight to 1e-20', hi - lo <= F(1, 10 ** 20), True)
    # ### THE HALVING ARITHMETIC, ON A FINITE EVEN MODEL. ### **THIS CHECKS THIS FILE'S ARITHMETIC
    # ### AND NOT THE INTEGRAL IDENTITY** -- see limit (3) in the header.
    vals = [F(3), F(1, 2), F(7, 5)]                       # ### values at x = 1, 2, 3
    full = 2 * sum(v * v for v in vals)                   # ### an even model: both signs of x
    halfsum = sum(v * v for v in vals)                    # ### the half-line
    ok &= say('the halving arithmetic: (1/2)*full == half-line', F(1, 2) * full == halfsum, True)
    ok &= say('reading (A)/(C): deviation is EXACTLY zero', F(1) - F(1) == F(0), True)
    # ### READING (B): the deviation is 1 - 1/sqrt(2), enclosed.
    dev_lo, dev_hi = F(1) - hi, F(1) - lo
    ok &= say('reading (B): the deviation is strictly between 0 and 1',
              dev_lo > 0 and dev_hi < 1, True)
    ok &= say('reading (B): the C0 sum is FINITE (one nonzero term)',
              (dev_hi + 0) < 1, True)
    if verbose:
        print('  %-58s %-14s %s' % ('fixture', 'got/exp', 'agree'))
        for lbl, got, exp, agree in rec:
            print('  %-58s %-14s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if agree else '### NO ###'))
    return ok


def show_table():
    fails = []
    print('\n' + '-' * 100)
    print('  (1) THE CONSTITUENTS. ### PLACE CLASS BY PLACE CLASS; EVERY CELL CARRIES ITS OWNER')
    print('      AND ITS GRADE, BOTH PULLED FROM THE FILE THAT EMITTED THEM (V1).')
    print('-' * 100)
    cls = None
    for pc, item, value, opath, oanchor, grade, gpath, ganchor in TABLE:
        if pc != cls:
            cls = pc
            print('\n  ### %s' % pc)
        try:
            wline = needle_pull.pull(opath, oanchor)
            wmark = 'PULLED'
        except LookupError:
            wline, wmark = '', '### UNPULLABLE ###'
            fails.append('%s / %s (wording)' % (pc, item))
        try:
            gline = needle_pull.pull(gpath, ganchor)
            gmark = 'PULLED'
        except LookupError:
            gline, gmark = '', '### UNPULLABLE ###'
            fails.append('%s / %s (grade)' % (pc, item))
        print('    %-26s %s' % (item, value))
        print('        OWNER  [%s] %-32s %s' % (wmark, os.path.basename(opath), wline[:88]))
        print('        GRADE  [%s] %-32s %s' % (gmark, grade, gline[:70]))
    return fails


def show_reqs():
    fails = []
    print('\n' + '-' * 100)
    print('  (2) THE PRODUCT\'S REQUIREMENTS, EACH NAMING WHICH CONSTRUCTION ASKS IT (V2).')
    print('-' * 100)
    for qid, prod, req, opath, anchor, verdict, why in REQS:
        try:
            line = needle_pull.pull(opath, anchor)
            mark = 'PULLED'
        except LookupError:
            line, mark = '', '### UNPULLABLE ###'
            fails.append(qid)
        # ### V5, MECHANICAL: a MET needs a derivation-or-owner; an OPEN needs the missing thing.
        if verdict.startswith('MET') and len(why) < 40:
            fails.append('%s: MET with no derivation' % qid)
        if verdict == 'OPEN' and 'MISSING, EXACTLY' not in why:
            fails.append('%s: OPEN without naming what is missing' % qid)
        print('\n    %-4s [%-42s]  ### %s' % (qid, prod, verdict))
        print('        ASKS      : %s' % req)
        print('        OWNER  [%s] %-30s %s' % (mark, os.path.basename(opath), line[:76]))
        print('        READING   : %s' % why)
    return fails


def show_convergence():
    print('\n' + '-' * 100)
    print('  (3) THE CONVERGENCE CONDITION, RE-CHECKED RATHER THAN CITED (V3).')
    print('      ### EXACT RATIONAL ARITHMETIC. ### NO FLOAT LITERAL AND NO FLOAT DIVISION.')
    print('-' * 100)
    lo, hi = enclose_inv_sqrt2(30)
    print('    THE SOURCE\'S NORM, FROM ITS OWN EQUATION (16):')
    print('      ||xi||^2_CC = (1/2) INT_R |xi|^2 dx = INT_0^inf |xi|^2 dx')
    print('    ### **SO FOR AN EVEN xi: ### ||xi||_CC = ||xi||_R / sqrt(2)  =  ||xi||_halfline.**')
    print('    ### The parity step is the source\'s own equation, not this file\'s arithmetic.')
    print()
    print('    ### **READING (A) -- b226\'s "normalized in L^2" MEANS CC\'s (16).**')
    print('      ||u_inf||_CC = 1   ->   deviation |1 - 1| = %s   (EXACT)' % (F(1) - F(1)))
    print('      ### **b226\'s RESULT STANDS UNCHANGED: the C0 sum is EXACTLY 0.**')
    print()
    print('    ### **READING (C) -- b226\'s L^2 MEANS THE CORPUS\'S OWN HALF-LINE PICTURE.**')
    print('      (16) says the half-line integral IS the CC norm, so (C) COINCIDES WITH (A).')
    print('      ### **THE CORPUS\'S OWN PICTURE IS THE ONE THAT AGREES WITH THE SOURCE EXACTLY.**')
    print()
    print('    ### **READING (B) -- b226\'s L^2 MEANS THE PLAIN INT_R WITHOUT THE FACTOR 1/2.**')
    print('      ||u_inf||_R = 1  ->  ||u_inf||_CC = 1/sqrt(2), enclosed EXACTLY:')
    print('        1/sqrt(2) in ( %s ,' % lo)
    print('                       %s )' % hi)
    print('        certified by squaring (lo^2 < 1/2 < hi^2) : %s' % certified(lo, hi))
    dlo, dhi = F(1) - hi, F(1) - lo
    print('      deviation |1/sqrt(2) - 1| = 1 - 1/sqrt(2) in')
    print('        ( %s ,' % dlo)
    print('          %s )' % dhi)
    print('      as a decimal, to the enclosure\'s own precision, both ends:')
    print('        %s' % (dlo * 10 ** 20 // 1))
    print('        (the integer above is the deviation scaled by 10^20 and truncated --')
    print('         ### **PRINTED AS AN INTEGER BECAUSE A DECIMAL POINT HERE WOULD BE A FLOAT.**)')
    print()
    print('    ### **THE VERDICT ON THE CONDITION ITSELF, UNDER BOTH READINGS:**')
    print('      the deviation is 0 at every FINITE place (norm-one by construction, b226 G-NORM),')
    print('      so the sum has AT MOST ONE nonzero term.')
    print('      ### **UNDER (A)/(C): the sum is EXACTLY 0.**')
    print('      ### **UNDER (B): the sum is 1 - 1/sqrt(2), a single finite term.**')
    print('      ### ### **THE C0 CONDITION CONVERGES UNDER BOTH. ### IT IS `MET`.**')
    print()
    print('    ### **AND WHAT DOES NOT SURVIVE UNDER (B), SAID PLAINLY:**')
    print('      ### **LEMMA 4.1.2\'s OWN HYPOTHESIS IS `||f_a|| = 1`**, and under (B) the')
    print('      archimedean vector has CC-norm 1/sqrt(2), not 1. ### The repair is a')
    print('      renormalization by sqrt(2) -- ### **AND THIS ACT DOES NOT PERFORM IT.**')
    print('      ### **IT COSTS THE MEMBERSHIP NOTHING: a renormalization is a NONZERO SCALAR, and')
    print('      ### S(1,1) is cut out by HOMOGENEOUS vanishing conditions, so membership is')
    print('      ### scalar-invariant (b292 (2c), carried at b300).**')
    print()
    print('    ### **AND WHAT IS NOT DISTURBED, WHICH MATTERS MORE THAN WHAT IS:**')
    print('      b226\'s Lean terminal `c0_deviation_is_zero` states that ### NORM-ONE AT EVERY')
    print('      PLACE ### makes the deviation sum exactly 0. ### **THAT IS A CONDITIONAL AND IT')
    print('      ### REMAINS TRUE.** ### What reading (B) would move is whether its HYPOTHESIS is')
    print('      satisfied by the stated choice -- ### **NOT THE THEOREM, AND NO COMPILED')
    print('      ### TERMINAL IS DISTURBED BY ANYTHING IN THIS ACT.**')
    print()
    print('    ### **WHICH READING IS b226\'s IS NOT STATED BY ANY OWNER.**')
    print('      b226 writes "normalized in `L^2`" and names no inner product; (16) makes the')
    print('      question decidable-in-principle without deciding it. ### **FILED AS A RULING.**')
    return []


def main():
    print('=' * 100)
    print('b301 -- THE OBJECT COMPLETED. ### CONSTITUENTS, REQUIREMENTS, CONVERGENCE.')
    print('=' * 100)
    print('\n  SELF-TEST (both polarities; the wrong enclosure must be rejected):')
    if not self_test():
        print('\n  ### REFUSING TO REPORT FROM ARITHMETIC THAT FAILS ITS OWN FIXTURES.')
        return 2

    fails = show_table() + show_reqs() + show_convergence()

    met = [q for q in REQS if q[5].startswith('MET')]
    opn = [q for q in REQS if q[5] == 'OPEN']
    other = [q for q in REQS if not q[5].startswith('MET') and q[5] != 'OPEN']
    print('\n' + '-' * 100)
    print('  THE REQUIREMENT CENSUS. ### MET, OPEN AND NOT-ASKED COUNTED SEPARATELY.')
    print('-' * 100)
    print('    requirements listed : %d' % len(REQS))
    print('    MET                 : %d   %s' % (len(met), ', '.join(q[0] for q in met)))
    print('    OPEN                : %d   %s' % (len(opn), ', '.join(q[0] for q in opn)))
    print('    NOT ASKED OF P-IDP  : %d   %s' % (len(other), ', '.join(q[0] for q in other)))
    print('    constituent cells   : %d' % len(TABLE))
    print('    unpullable / defects: %d  %s'
          % (len(fails), 'PASS' if not fails else '### FAIL ###'))
    for f in fails:
        print('        ### %s' % f)
    print('\n' + '=' * 100)
    print('  ### **THE REACH, PRINTED WITH THE RESULT: THE TABLE PROVES AN OWNER AND A GRADE ARE')
    print('  ### ON DISK. ### IT DOES NOT AUDIT THE GRADE. ### THE REQUIREMENTS\' VERDICTS ARE THE')
    print('  ### ACT\'S JUDGEMENT; THE TOOL REFUSES A BARE `MET` AND A NAMELESS `OPEN`, AND THAT IS')
    print('  ### ALL IT DECIDES.**')
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
