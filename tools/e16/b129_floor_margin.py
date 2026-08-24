# -*- coding: utf-8 -*-
"""b129 -- THE FLOOR-VERSUS-MARGIN TABLE.

### READS BANKED VALUES AND PERFORMS ARITHMETIC ONLY. No model is evaluated, no
quadrature is built, no verdict is re-graded. Every input below is a number
already in the record, quoted with its source.
"""
import functools
print = functools.partial(print, flush=True)

# ---- banked inputs, each with its source ----
FLOOR = 4.287821e-02          # b128 bank: four-axis maximum, AXIS = NQ
AX = {"NQ": 4.287821e-02, "u": 7.713163e-03,
      "epsilon": 4.797947e-07, "truncation": 2.193267e-02}   # b128 bank
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
BANKED_I = {2: -0.083077396, 3: -0.059667687, 4: -0.060113821, 8: -0.071923801,
            9: -0.073759303, 12: -0.077118973, 16: -0.078592093,
            24: -0.077818000, 48: -0.070591879}              # b117, via b121
MARGIN = {2: 0.064826976, 3: 0.095154244, 4: 0.111534989, 8: 0.133564668,
          9: 0.135216620, 12: 0.137327894, 16: 0.137215854,
          24: 0.134217931, 48: 0.123962521}                  # b119 coarse margins
FINE = {2: 0.018250420, 3: 0.035486557, 4: 0.051421167, 8: 0.061640867,
        9: 0.061457317, 12: 0.060208921, 16: 0.058623761,
        24: 0.056399931, 48: 0.053370642}                    # b119 |fine pairing|
RATIO119 = {2: 0.282, 3: 0.373, 4: 0.461, 8: 0.462, 9: 0.455,
            12: 0.438, 16: 0.427, 24: 0.420, 48: 0.431}      # b119 ratios
REP700 = {2: -0.083119244, 3: -0.059674727, 4: -0.060119335, 8: -0.071921153,
          9: -0.073757871, 12: -0.077115962, 16: -0.078593862,
          24: -0.077815037, 48: -0.070591979}                # b128 repaired @700
EXC = {2: 4.288e-02, 3: 3.113e-02, 4: 2.579e-02, 8: 1.816e-02, 9: 1.716e-02,
       12: 1.505e-02, 16: 1.354e-02, 24: 1.166e-02, 48: 9.689e-03}  # b128 per cell
B121_ONESIGN = -0.028796      # b121 bank: max I over 9 cells AND 4 bases


def flag(r):
    return "CLEAR" if r >= 1.0 else "CAVEAT"


print("=" * 96)
print("THE FLOOR-VERSUS-MARGIN TABLE   (banked values + arithmetic; nothing re-graded)")
print("  the single-axis floor = %.6e ; ITS AXIS = the prolate quadrature size (b128)" % FLOOR)
print("=" * 96)

print("\n[A] THE b117 ENCLOSURES -- |I(L)| banked, against the floor")
print("%6s %16s %14s %12s %9s" % ("a^2", "|I| banked", "floor", "clearance", "flag"))
mn = 9e9
for a2 in CELLS:
    m = abs(BANKED_I[a2]); r = m / FLOOR; mn = min(mn, r)
    print("%6d %16.9f %14.6e %12.3f %9s" % (a2, m, FLOOR, r, flag(r)))
print("  ### worst clearance %.3f -- ALL ROWS %s" % (mn, flag(mn)))

print("\n[B] THE b119 COARSE MARGINS, against the floor")
print("%6s %16s %14s %12s %9s" % ("a^2", "coarse margin", "floor", "clearance", "flag"))
mn = 9e9
for a2 in CELLS:
    r = MARGIN[a2] / FLOOR; mn = min(mn, r)
    print("%6d %16.9f %14.6e %12.3f %9s" % (a2, MARGIN[a2], FLOOR, r, flag(r)))
print("  ### worst clearance %.3f -- ALL ROWS %s" % (mn, flag(mn)))

print("\n[C] THE b119 DOMINANCE ROWS -- status WITHDRAWN TO BASIS (b121)")
print("    *** THE FLOOR IS ON I(L), THE TOTAL PAIRING. IT CANNOT BE APPLIED TO THE")
print("    *** fine/coarse SPLIT COMPONENTS WITHOUT A SEPARATE MEASUREMENT THAT THE")
print("    *** RECORD DOES NOT HAVE. Doing so would be the category mismatch this")
print("    *** seam names as a recurring hazard. The rows below are therefore")
print("    *** FLAGGED FROM b121's DIRECT MEASUREMENT, not from floor arithmetic.")
print("%6s %14s %18s %28s" % ("a^2", "b119 ratio", "dominance clearance", "status (b121, measured)"))
for a2 in CELLS:
    cl = MARGIN[a2] - FINE[a2]
    st = "BASIS-DEPENDENT (1.541/1.432)" if a2 == 2 else "holds at every basis tested"
    print("%6d %14.3f %18.9f %28s" % (a2, RATIO119[a2], cl, st))
print("  ### a^2 = 2 CAVEAT (already withdrawn); the rest CLEAR AT THE BASES TESTED,")
print("      and FOUR of the nine cells (a^2 = 8, 12, 16, 24) were NOT among b121's five")
print("      -- their basis-robustness is UNTESTED, not established.")

print("\n[D] THE b121 ONE-SIGN VERDICT -- and the double-counting trap named")
print("  b121's max I over 9 cells AND 4 bases = %+.9f  (a DIRECT measurement" % B121_ONESIGN)
print("  that already covers the NQ axis; adding the NQ floor to it would DOUBLE-COUNT).")
print("  So the residual exposure is the axes b121 did NOT vary:")
res_single = max(AX["u"], AX["epsilon"], AX["truncation"])
res_add = AX["u"] + AX["epsilon"] + AX["truncation"]
res_disc = AX["u"] + AX["epsilon"]
for nm, v in (("largest single un-varied axis (truncation)", res_single),
              ("additive u + epsilon + truncation", res_add),
              ("additive u + epsilon ONLY (truncation excluded as a MODEL axis)", res_disc)):
    r = abs(B121_ONESIGN) / v
    print("    %-62s %.6e  clearance %.3f  %s" % (nm, v, r, flag(r)))
print("  ### THE VERDICT ROW: CLEAR against the largest single un-varied axis;")
print("  ### CAVEAT against a naive additive combination INCLUDING truncation;")
print("  ### CLEAR against the discretization axes alone. b128 declared truncation")
print("  ### a MODEL axis, so the record carries both readings and asserts neither.")

print("\n[E] DID I(L) REMAIN NEGATIVE AT EVERY TESTED NQ? -- from b128's run data")
print("  bound: I(NQ) <= I(700) + excursion, both banked in b128's G-NQ table")
print("%6s %16s %14s %18s %9s" % ("a^2", "I(700) rep", "excursion", "upper bound", "sign"))
worst = -9e9
for a2 in CELLS:
    ub = REP700[a2] + EXC[a2]; worst = max(worst, ub)
    print("%6d %16.9f %14.3e %18.9f %9s" % (a2, REP700[a2], EXC[a2], ub, "neg" if ub < 0 else "POS"))
print("\n  ### WORST UPPER BOUND OVER ALL NINE CELLS = %+.9f -- STRICTLY NEGATIVE." % worst)
print("  ### ANSWER: YES. I(L) remained negative at every tested NQ value.")
print("  SOURCE: b128 bank, G-NQ table (rep@700 and per-cell excursion columns).")
print("  *** AND THE CROSS-CHECK, which is why the bound is worth computing:")
print("  *** b121 MEASURED the max over its four bases at %+.9f; this bound from" % B121_ONESIGN)
print("  *** b128's independent run gives %+.9f. They agree to %.2e, and the bound" % (worst, abs(worst - B121_ONESIGN)))
print("  *** correctly sits ABOVE the measurement, as a bound must. Two acts, two")
print("  *** routes, one number. ***")
