# -*- coding: utf-8 -*-
"""b240_meanings.py -- THE MEANINGS AND THE CRITERION, BANKED BEFORE ANY NUMBER IS SEEN.

### THIS FILE COMPUTES NO RESIDUAL, RUNS NO INSTRUMENT, AND IMPORTS NO INSTRUMENT MODULE.
### It writes `data/b240_meanings.txt`. ### THE RUN WRITES ITS OWN FILE AFTERWARDS, PRINTS THE
### SHA-256 OF THIS FILE'S OUTPUT INTO IT, AND A GATE COMPARES BOTH THE HASH AND THE MTIMES.
### ### THAT IS b238's MECHANISM, AND IT IS THE ONLY THING THAT MAKES "BEFORE" CHECKABLE.

### THE ORDER-OF-OPERATIONS LAW (b238, author): "the criterion is written from the budget BEFORE
### the final residuals are looked at, and a criterion rewritten after the numbers remains not a
### criterion; varying axes to MEASURE convergence order is lawful, choosing axes to hit a target
### is the named crime."

### THE STANDING CLAUSE (b229, author): "the adopted target may NEVER define, calibrate, or tune
### the left side; the two sides keep independent definitions in every future act."
"""
import hashlib
import io
import math
import time

OUT = r"D:\relay\data\b240_meanings.txt"

# ### THE RIGHT SIDE'S BANKED BUDGET (b238), TRANSCRIBED FROM data/b238_criterion.txt.
# ### K IS THE MEASURED ENVELOPE; F THE FLOAT FLOOR; TAIL THE ZERO-TRUNCATION TAIL.
K_BANKED = {'3': 0.6363, '4': 0.1539}
FLOOR = 3.0e-13
TAIL = {'2': 7.195e-21, '3': 3.159e-26, '4': 1.072e-27}
K_SURROGATE = 0.6363      # ### the LARGEST banked K, used for the cells b238 never measured
CELLS = ['2', '3', '4', '8', '9', '12']
NV_BASE, NV_REFINED = 4001, 6001
S_L = 4.0                 # ### the left side's stability factor, FIXED HERE
D_FACTOR = 10.0           # ### the dissonance factor, FIXED HERE (b238's species: state it first)


def h_of(a_sq, nv):
    """### THE corr-GRID SPACING, b238's own formula: vc runs over [-2L, 2L], 2*NV-1 points."""
    L = math.log(math.sqrt(a_sq))
    return (4.0 * L) / (2 * nv - 2)


def bar_R_banked(lab, nv):
    a_sq = float(lab)
    if lab == '2':
        # ### a^2 = 2's PRIME COLUMN IS EMPTY (corr vanishes at the endpoint u = 2L), so the
        # ### interpolation term is absent. ### THAT IS NOT AN EXEMPTION: it is what the budget
        # ### says about a cell with no interpolated prime terms.
        return FLOOR + TAIL['2'], 0.0, 'BANKED (no K term: prime column empty)'
    K = K_BANKED.get(lab)
    src = 'BANKED (b238, measured envelope)'
    if K is None:
        K = K_SURROGATE
        src = 'SURROGATE (largest banked K; b238 NEVER MEASURED THIS CELL)'
    h = h_of(a_sq, nv)
    tail = TAIL.get(lab, 0.0)
    return K * h * h + FLOOR + tail, h, src


def main():
    w = []
    p = w.append
    p("=" * 100)
    p("b240 -- THE MEANINGS AND THE CRITERION. ### BANKED BEFORE ANY INSTRUMENT RUNS.")
    p("### WRITTEN AT %s (local). ### NO SIDE HAS BEEN COMPUTED AT ANY CELL." %
      time.strftime('%Y-%m-%dT%H:%M:%S'))
    p("=" * 100)
    p("")
    p("### THE CEILING, QUOTED FROM THE DEPOSIT'S OWN LAW AND GOVERNING EVERY LINE BELOW:")
    p('###   b14: "a FINITE-PLACE-SET OBJECT AT A FINITE MODEL CUTOFF -- the complete roster is')
    p('###         the double limit (all places, cutoff to infinity) and STAYS OPEN whatever this')
    p('###         act shows."')
    p('###   b15: "A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL."')
    p("### ### NO BRANCH OF THIS ACT DISCHARGES, WEAKENS, OR MOVES h2 OR THE REGISTER SENTENCE.")
    p('### ### THE REGISTER SENTENCE, QUOTED UNCHANGED: "RH reduced to a single located clause,')
    p('### ### reduction machine-verified. h2 is the clause." ### NOTHING HERE CLAIMS MORE.')
    p("")
    p("=" * 100)
    p("(A) THE FOUR BRANCHES AND WHAT EACH ONE MEANS. ### FIXED HERE, IN THESE WORDS.")
    p("=" * 100)
    p("")
    p("### (CONSONANT) -- |L - R| within the combined bar at EVERY cell.")
    p("###   MEANS: the identity's FORM is corroborated AT FINITE CELLS AT BENCH, with bars")
    p("###   annotated MEASURED-NOT-CERTIFIED. ### NOTHING GLOBAL. ### h2 EXACTLY AS OPEN AS")
    p("###   BEFORE. ### It does NOT mean the identity is proved, and it does NOT promote any")
    p("###   asset's grade: b237 graded all four channels PARTIAL and this act moves none of them.")
    p("")
    p("### (DISSONANT) -- a residual beyond the combined bar by the registered factor D = %g" % D_FACTOR)
    p("###   at any cell.")
    p("###   MEANS: A FINDING, REPORTED AT FULL PROMINENCE. ### AND THE INDICTMENT ORDER IS")
    p("###   REGISTERED HERE, IN ADVANCE, SO THAT NO SUSPECT IS CONVICTED BY PLACEMENT:")
    p("###     SUSPECT 1 -- THE UNCERTIFIED ENVELOPE AND THE AXES (b238's amber). The right")
    p("###       side's bars are MEASURED, NOT CERTIFIED; b238's own bound was exceeded at one")
    p("###       cell of six by 4%; and for a^2 in {8,9,12} the K below is a SURROGATE, not a")
    p("###       measurement. ### THIS SUSPECT IS FIRST BECAUSE IT IS THE ONE THIS EXECUTOR")
    p("###       ALREADY KNOWS IS WEAK.")
    p("###     SUSPECT 2 -- THE PER-CELL REALIZATIONS' NORMALIZATIONS, and the species is named:")
    p("###       ### THE THREE-NORMALIZATIONS SPECIES -- (i) the ε-channel's normalization (does")
    p("###       Tr_full ALREADY CARRY an E2, so that T := Tr_full + E2 + Δ₋ counts it twice?),")
    p("###       (ii) the quotient trace's volume normalization ('(N-forced) modulo the cited")
    p("###       class-richness lemma', §18), (iii) the test function's own normalization (`corr`")
    p("###       = w ⋆ w with w unit-mass, against the ledger's convention).")
    p("###     SUSPECT 3 -- THE ASSEMBLY CONVENTIONS: the sign and role of Θ_q inside `Q.value`,")
    p("###       and the restricted-product assembly the ruling's rider explicitly does NOT")
    p("###       perform (M-2 open).")
    p("###     SUSPECT 4, AND ONLY LAST -- THE FORM ITSELF, `T + Q = wInf - wPrimes`.")
    p("###   ### NO SUSPECT IS SKIPPED AND NONE IS CONVICTED BY PLACEMENT: the order says which")
    p("###   ### is EXAMINED first, never which is GUILTY. ### A dissonance is evidence about the")
    p("###   ### ASSEMBLY THIS ACT PERFORMED before it is evidence about the identity.")
    p("")
    p("### (INDETERMINATE) -- bar < |L - R| <= D * bar at some cell, with no cell dissonant.")
    p("###   MEANS: ### W-ORD-IMP1-ENVELOPE BECOMES THE GATE TO ANY VERDICT. No verdict is")
    p("###   written on either side until the envelope is re-derived as a true envelope.")
    p("")
    p("### (HALT) -- a gate fired: any C0 void gate, the ε mask algebra, the kernel-cache gate,")
    p("###   the timestamp/hash gate, or the G-INDEP gate. ### MEANS: NO TABLE IS READ AS DATA.")
    p("")
    p("### THE ACT'S BRANCH FROM THE CELLS, FIXED HERE: any HALT -> (HALT); else any DISSONANT")
    p("### -> (DISSONANT); else any INDETERMINATE -> (INDETERMINATE); else (CONSONANT).")
    p("")
    p("=" * 100)
    p("(B) THE TWO SIDES, EACH FROM ITS OWN OWNERS. ### NEITHER DEFINES THE OTHER.")
    p("=" * 100)
    p("")
    p("### LEFT -- per the EXECUTED M-1 RULING (b239), quoted verbatim:")
    p('###   "RULE M-1: C2, per-cell instrument realization standing until M-4 closes; Δ₋\'s')
    p('###    bookkeeping (M-4) named as the definition\'s open debt in the correspondence row."')
    p("###   ### L := T.value + Q.value  with  T.value := Tr_full + E2 + Δ₋  and  Q.value := Θ_q")
    p("###   Tr_full := sum over modes of `b38_act10.trace_modes(a, corr, vc, L, NQ, NMODE)`")
    p("###   E2      := `b38_act10.e2_of_grid(a, corr, vc, L, rr, ee_full)`")
    p("###   Δ₋      := `b38_act10.e2_of_grid(a, corr, vc, L, rr, ee_odd)` -- §17's ODD-INDEX")
    p("###              t(n) series, the odd CC-index mask, via `b37_act9.eps_masked(rr, odd)`;")
    p("###              banked at the ε′(1⁺) pin, 8.8191383 of 22.9964757.")
    p("###   Θ_q     := `b38_act10.theta_quotient(a, S4, corr, vc, L)`, on `V_inv`.")
    p("###   ### Q.value TAKES Θ_q AS THE INSTRUMENT RETURNS IT. ### NO SIGN IS INSERTED: no")
    p("###   ### ruling authorizes one, and inserting one to help the columns meet would be")
    p("###   ### exactly b229's named crime. ### The sign question is SUSPECT 3, and it is")
    p("###   ### probed by a registered DIAGNOSTIC (section E) that CANNOT change the branch.")
    p("")
    p("### RIGHT -- the adopted ledger at the atlas's convention (b232/b233/b235, re-signed at")
    p("### b235 to `wInf := +A`):  ### R := A - PR")
    p("###   A  := `b38_act10.left_side(...)[0]` -- the archimedean column")
    p("###   PR := `b38_act10.left_side(...)[2]` -- the prime column, the adopted `wPrimes`")
    p("")
    p("### SPACES AND CELL-SPECIES, SAID AT EVERY USE (b219/b221):")
    p("###   the cells are ### DIAGONAL a^2 CELLS (2,3,4,8,9,12) -- the banked six.")
    p("###   Tr_full, E2, Δ₋ live on the ### PROLATE/SONIN SPACE at the archimedean place,")
    p("###     test-function paired -- NOT `V_inv`, NOT `S̄_v`.")
    p("###   Θ_q sums over ### LOCAL (p,n) CELLS indexed by the staircase at a DIAGONAL a^2 cell,")
    p("###     on ### `V_inv` -- two cell-species in one formula, and they are not the same name.")
    p("###   A, PR are ### LEDGER columns at the same DIAGONAL a^2 cell.")
    p("")
    p("=" * 100)
    p("(C) EVERY ε, CONSTANT AND AXIS -- FROM THE INSTRUMENTS' OWN BANKED DEFAULTS, QUOTED HERE")
    p("    BEFORE THE RUN. ### NOTHING BELOW MAY MOVE AFTER A RESIDUAL IS SEEN.")
    p("=" * 100)
    p("  place set                : S4 = {inf, 2, 3, 5}         (b38_act10.S4)")
    p("  cells                    : a^2 in 2, 3, 4, 8, 9, 12    (b38_act10.CELLS)")
    p("  atlas NV (base)          : %d      ### the atlas's OWN committed default" % NV_BASE)
    p("  atlas NV (refinement)    : %d      ### b238's other TEST axis (both have banked bounds)"
      % NV_REFINED)
    p("  atlas NU / UMAX / TOL    : 12001 / 600.0 / 1e-3        (carto_atlas, committed constants)")
    p("  mode axis (base)         : (NQ, NMODE) = (700, 10)     ### b38's TRIPLE, middle entry")
    p("  mode axis (refinement)   : (NQ, NMODE) = (900, 11)     ### b38's TRIPLE, third entry")
    p("  ε layer                  : EPS_NQ = 700, EPS_NG = 400, EPS_NRHO = 240")
    p("  ε grid                   : rr = exp(linspace(1e-4, log(12.001), 240))")
    p("  u-half grid              : NU_HALF = 401")
    p("  ### THE KERNEL CACHE HAZARD, NAMED: `carto_atlas.kernel` caches on first call and is")
    p("  ### keyed on NOTHING. It is safe here ONLY because NU and UMAX never change, and a gate")
    p("  ### asserts exactly that. ### A cache keyed on nothing is a stale value waiting for a")
    p("  ### second axis.")
    p("")
    p("=" * 100)
    p("(D) THE CRITERION. ### DERIVED FROM b238's BANKED BUDGET AND THE LEFT SIDE'S OWN G-STAB")
    p("    SPREAD -- ### AND FROM NOTHING THIS ACT HAS MEASURED, BECAUSE IT HAS MEASURED NOTHING.")
    p("=" * 100)
    p("")
    p("  bar_R(cell) := K(a^2) * h^2 + F + tail(a^2),  h = 4L / (2*NV - 2)   [b238's own form]")
    p("     K from b238's MEASURED envelope where b238 measured it (a^2 = 3, 4);")
    p("     ### K := %.4f (the LARGEST banked K) as a declared SURROGATE at a^2 = 8, 9, 12," % K_SURROGATE)
    p("     ### WHICH b238 NEVER MEASURED. ### That is an extrapolation ACROSS CELLS and it is")
    p("     ### itself uncertified: it inherits b238's amber AND WIDENS IT. Said here, before.")
    p("     F = %.3e (the float64 floor, measured at a^2 = 2); tail from b238's S4." % FLOOR)
    p("  ### AND ONE FLOOR, REGISTERED IN ADVANCE: bar_R := max(bar_R_banked, |R(refined) - R(base)|).")
    p("  ### A MEASURED SPREAD LARGER THAN THE PROJECTION MAKES THE PROJECTION THE WRONG BAR, and")
    p("  ### b238 already found the projection exceeded at one cell of six. ### THIS IS NOT")
    p("  ### WIDENING A PROJECTION TO COVER A RESIDUAL: the residual is |L - R| and it is not in")
    p("  ### this formula; the floor is the right side's own disagreement with itself.")
    p("")
    p("  bar_L(cell) := %g * max( |L(NV refined) - L(base)| , |L(mode refined) - L(base)| )" % S_L)
    p("     ### the left side's OWN G-STAB spread over its TWO registered refinements, times a")
    p("     ### factor fixed HERE. ### The left side's bar comes from the left side alone.")
    p("")
    p("  combined bar := bar_L + bar_R.")
    p("  ### THE TWO BARS ARE ADDED, NOT COMBINED IN QUADRATURE: these are envelopes, not")
    p("  ### standard deviations, and adding is the conservative reading of an envelope.")
    p("")
    p("--- THE BANKED RIGHT-SIDE BARS AT THE BASE AXIS, PRINTED BEFORE THE RUN ---")
    p("  %-5s %14s %14s   %s" % ("a^2", "h", "bar_R (banked)", "source"))
    for lab in CELLS:
        b, h, src = bar_R_banked(lab, NV_BASE)
        p("  %-5s %14.6e %14.6e   %s" % (lab, h, b, src))
    p("")
    p("=" * 100)
    p("(E) THE REGISTERED DIAGNOSTICS. ### THEY CANNOT CHANGE THE BRANCH. ### FIXED HERE.")
    p("=" * 100)
    p("  ### THE BRANCH IS DECIDED BY THE PRIMARY READING ALONE -- L := (Tr_full + E2 + Δ₋) + Θ_q")
    p("  ### against R := A - PR. ### The variants below exist ONLY to name a suspect if the")
    p("  ### primary reading is dissonant, and they are written down BEFORE any number so that a")
    p("  ### later 'the other assembly works' cannot be a discovery made to order.")
    p("    V1 (suspect 2, ε double-count)  : L1 := Tr_full + Δ₋ + Θ_q")
    p("    V2 (suspect 3, Θ_q's sign)      : L2 := Tr_full + E2 + Δ₋ - Θ_q")
    p("    V3 (both)                       : L3 := Tr_full + Δ₋ - Θ_q")
    p("    V4 (the corpus's own anatomy)   : D_dict := (Θ_q - PR) + (Δ₋ - 2*E2)   [§20(a)]")
    p("  ### V4 IS A PRIOR SIGHTING (section F) AND IS COMPUTED ONLY IN THE DIAGNOSTIC BLOCK,")
    p("  ### AFTER THE BRANCH IS DECIDED AND RECORDED. ### It is not in the criterion.")
    p("")
    p("=" * 100)
    p("(F) G-PRIOR -- PRIOR SIGHTINGS OF NEAR-COMPARISONS, LISTED AS HISTORICAL AND")
    p("    ### NOT CONSULTED FOR THE CRITERION.")
    p("=" * 100)
    p("  1. ### §20(a)'s COLUMNS -- `A - PR` at these same six diagonal cells with the per-cell")
    p("     anatomy `D = -resid47 - 2*E2 + Δ₋ + (Θ_q - PR)` checking exactly (b38/b37 banks).")
    p("  2. ### act 12's RESIDUAL COLLAPSE -- the raw mode terms measured >= 0 at every cell.")
    p("  3. ### §25(c)'s NUMERICAL HALF -- the `E₁` positive form <= the full Sonin form (L2).")
    p("  ### ALL THREE ARE COMPARISONS THAT TOUCHED BOTH COLUMNS. ### NONE OF THEIR NUMBERS")
    p("  ### ENTERS THE CRITERION ABOVE: the criterion is b238's budget plus this act's own")
    p("  ### G-STAB spread, and nothing else. ### They are listed so a later reader can see that")
    p("  ### the executor knew they existed and did not quarry them for a bar.")
    p("")
    p("=" * 100)
    p("(G) G-INDEP -- THE SHARED-COMPONENT AUDIT, WRITTEN BEFORE THE RUN.")
    p("=" * 100)
    p("  ### SHARED, AND EACH SHARING IS THE IDENTITY'S OWN CONTENT:")
    p("    · the cell `a` and `L = log a` -- ### the identity is stated AT a cell; two sides at")
    p("      two different cells are two different statements.")
    p("    · the test function: `w = carto_atlas.bump(a)` and `corr = w ⋆ w` on `vc` -- ### THE")
    p("      IDENTITY IS AN IDENTITY FOR ONE TEST FUNCTION. ### Evaluating the sides at different")
    p("      g would not be leakage-free rigour; it would be comparing two different claims.")
    p("    · the place set S4 -- ### the roster is part of the statement, not of either side.")
    p("    · the atlas constants NV, NU, UMAX -- instrument constants, committed in carto_atlas.")
    p("  ### NOT SHARED: the ε layer (EPS_*) and the mode axis are LEFT-ONLY; the ζ-ordinates and")
    p("    the ψ-kernel are RIGHT-ONLY (A) plus the prime staircase (PR).")
    p("  ### THE LEAKAGE TEST, AND IT IS RUN, NOT ASSERTED: no left-side function takes a")
    p("    right-side output as an argument and none calls `left_side`; and `left_side` neither")
    p("    calls nor receives `trace_modes`, `e2_of_grid`, `theta_quotient`. ### The run checks")
    p("    this by INSPECTING THE INSTRUMENTS' OWN SOURCE, and a HALT follows if it fails.")
    p("")
    p("=" * 100)
    p("(H) THE HONEST EXPECTATION, REGISTERED BEFORE THE RUN, WITH THE EXECUTOR'S OWN EXPECTED")
    p("    BRANCH AT EVERY CELL. ### WRITTEN FROM THE INSTRUMENTS' SOURCE, NOT FROM ANY NUMBER.")
    p("=" * 100)
    p("  ### THE ALGEBRA I CAN READ WITHOUT RUNNING ANYTHING. `b38_act10` computes")
    p("  ###     resid = Tr_full - A - E2_full        (its own `resid47` column)")
    p("  ### so ### Tr_full = A + E2 + resid47 ### IDENTICALLY, BY THE INSTRUMENT'S DEFINITION.")
    p("  ### Substituting into the primary reading:")
    p("  ###     L - R = (A + E2 + resid47 + E2 + Δ₋ + Θ_q) - (A - PR)")
    p("  ###           = ### 2*E2 + Δ₋ + resid47 + Θ_q + PR")
    p("  ### EVERY TERM ON THAT RIGHT-HAND SIDE IS AN O(1)-SCALE COLUMN OF THIS BENCH, NOT A")
    p("  ### BAR-SCALE QUANTITY. ### SO I EXPECT ### (DISSONANT) AT EVERY ONE OF THE SIX CELLS,")
    p("  ### INCLUDING a^2 = 2 (where PR and Θ_q vanish because `corr` vanishes at u = 2L, but")
    p("  ### 2*E2 + Δ₋ + resid47 does not).")
    p("  ### ### AND I NAME THE SUSPECT I EXPECT, IN ADVANCE, WITHOUT PROMOTING IT PAST THE")
    p("  ### ### REGISTERED ORDER: ### SUSPECT 2's FIRST LIMB -- `Tr_full` ALREADY CARRIES AN E2")
    p("  ### ### BY THE INSTRUMENT'S OWN ARITHMETIC, so `T := Tr_full + E2 + Δ₋` COUNTS THE")
    p("  ### ### ε-CHANNEL TWICE. ### That is a statement about THE ASSEMBLY THIS ACT WAS TOLD")
    p("  ### ### TO PERFORM, not about the identity's form, and the indictment order says so.")
    p("  ### ### I REGISTER IT HERE SO THAT IF THE NUMBERS SAY OTHERWISE, THE RECORD SHOWS I WAS")
    p("  ### ### WRONG -- and if they say this, THE PREDICTION IS ON RECORD BEFORE THE NUMBER.")
    p("  ### AND THE COROLLARY, REGISTERED WITH IT: ### A DISSONANT BRANCH HERE IS NOT EVIDENCE")
    p("  ### AGAINST THE IDENTITY. ### The ruling that fixed `T.value` was explicitly a PER-CELL")
    p("  ### realization with an OPEN DEBT (M-4) and an OPEN ASSEMBLY (M-2). ### An assembly with")
    p("  ### two named open items is the FIRST thing a dissonance indicts.")
    p("")
    p("=" * 100)
    p("### WHAT NO BRANCH OF THIS ACT MAY DO: move h2; move the register sentence; move any")
    p("### asset's grade; promote `Θ_q` or any channel past PARTIAL; discharge M-2..M-5; certify")
    p("### the right side's bars; deposit anything. ### THE CEILING ABOVE GOVERNS ALL FOUR.")
    p("=" * 100)

    txt = "\n".join(w) + "\n"
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write(txt)
    hh = hashlib.sha256(txt.encode('utf-8')).hexdigest()
    print(txt[:0])
    print("banked: %s" % OUT)
    print("sha256: %s" % hh)
    print("### THE MEANINGS ARE ON DISK. ### NO INSTRUMENT HAS RUN.")


if __name__ == '__main__':
    main()
