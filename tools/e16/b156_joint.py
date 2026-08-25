# -*- coding: utf-8 -*-
"""b156 -- THE T-JOINT's instrument.

### WHAT THIS DOES: locates the apportionment-free candidate inside b154's family
### and prices the difference, from b38's OWN RECORDED COLUMNS.

### WHAT IT DOES NOT DO: propose an identification. ### NAMING A FORMABLE FORMULA
### IS NOT PROPOSING IT. No formula here is recommended, endorsed, called correct,
### or offered as "the natural one" -- a formula offered as the natural one would
### be a definition in everything but name, and the executor never makes the
### author's definitions. ### NO BENCH VALUE IS PROMOTED.
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# b38's recorded columns, read at content from data/b38_2026-08-18.txt.
# (a^2, A, W_plus, resid_N, E2even, f_cell)
CELLS = [
    (2,  -1.990528, -1.37813, 4.0486, 1.00181, 0.6923),
    (3,  -1.908900, -1.26715, 3.3740, 0.91094, 0.6638),
    (4,  -1.786498, -1.16716, 3.0478, 0.83403, 0.6533),
    (8,  -1.525474, -0.95494, 2.5208, 0.68551, 0.6260),
    (9,  -1.488337, -0.92343, 2.4540, 0.66513, 0.6204),
    (12, -1.405398, -0.85622, 2.3134, 0.62009, 0.6092),
]
SIG = 0.616500298741
BAR = "=" * 78


def head(s):
    print("\n" + BAR); print(s); print(BAR)


head("J1 -- THE APPORTIONMENT-FREE CANDIDATE, LOCATED IN b154's FAMILY.")
print("  b38's definition, summed over the even sector:")
print("     W+(mu) = SUM_even tr_n_raw - SUM_even E2_n - mu * resid_N")
print("  The apportionment-free formula uses the two PER-MODE objects alone --")
print("  b36's raw dilation traces and act 9's exactly mode-diagonal eps parts,")
print("  neither of which carries any apportionment freedom (b154's R3):")
print("     T_obj := SUM_even tr_n_raw - SUM_even E2_n")
print("  ### SO T_obj = W+(0) IDENTICALLY. IT IS THE FAMILY MEMBER AT SHARE ZERO --")
print("  ### the member charging the WHOLE residual to the odd sector.")
print("  ### THE VOID GATE IS SATISFIED: the shares are 0 and 1, which sum to 1.")
print()
print("  cell    W+(sigma_even)   T_obj = W+(0)    difference      |diff| / |A|")
for a2, A, Wp, r, e2e, f in CELLS:
    tobj = Wp + SIG * r
    print("  %4d      %+9.5f      %+9.5f     %+9.5f      %8.4f"
          % (a2, Wp, tobj, tobj - Wp, abs(tobj - Wp) / abs(A)))
print()
print("  ### THE TWO CANDIDATES DIFFER BY sigma_even * resid_N, WHICH EXCEEDS THE")
print("  ### CERTIFIED COLUMN AT EVERY CELL -- and they differ IN SIGN.")
print("  ### THIS IS NOT A NEW FINDING. It is b155's price, already banked, seen")
print("  ### at two named points of the same one-parameter family. A large")
print("  ### difference between two UNPINNED choices restates the price; it does")
print("  ### not measure anything.")

head("J2 -- THE CERTIFIED COLUMN ENTERS THE CLOSED EQUATION TWICE.")
print("  b38's closed equation:  D_closed = (A - PR) - ((W+ + E2even) - Thq)")
print("  and resid_N := Tr_raw_N - A - E2_N, so ### A IS AN INPUT TO W+ ITSELF:")
print("     W+(mu) = T_obj - mu * (Tr_raw_N - A - E2_N)   ->   dW+/dA = + mu")
print("  Hence   ### d(D_closed)/dA = 1 - mu.")
print()
print("  ### THE LEDGER COLUMN APPEARS ON BOTH SIDES OF THE COMPARISON, and the")
print("  ### two appearances DO NOT CANCEL -- they net to (1 - mu).")
print("     at b38's registered share, mu = sigma_even : coefficient %.6f" % (1 - SIG))
print("     at the apportionment-free member, mu = 0   : coefficient %.6f" % 1.0)
print("  ### SO THE TWO CANDIDATE IDENTIFICATIONS DIFFER NOT ONLY IN VALUE BUT IN")
print("  ### HOW THE CLOSED EQUATION DEPENDS ON THE CERTIFIED COLUMN.")
print("  ### THIS IS A STATEMENT ABOUT b38's CONSTRUCTION, NOT ABOUT WHETHER THE")
print("  ### IDENTITY HOLDS. (I-differ) stands exactly as recorded, cited at its")
print("  ### grade, never re-interpreted and never extended.")

head("J3 -- WHAT THIS SETTLES, AND WHAT IT DOES NOT.")
print("  SETTLED: an identification of file E's archimedean term that does not")
print("    route through a sector apportionment IS FORMABLE from recorded ground,")
print("    with owners -- and it lands INSIDE b154's family, at share zero.")
print("  ### NOT SETTLED, AND NOT THE EXECUTOR'S TO SETTLE: which member is right.")
print("  ### A MEMBER IS NOT AN ESCAPE. Choosing 'subtract nothing' is as much a")
print("  ### definitional choice as choosing 'apportion by t-mass', and b155's")
print("  ### PHYSICAL verdict applies to it verbatim: the identity's residual moves")
print("  ### with the share at rate resid_N, which is recorded nonzero everywhere.")
print("  ### THEREFORE nu's PHYSICALITY IS NOT MOOT AND ROUTE A IS STILL OWED.")
print()
