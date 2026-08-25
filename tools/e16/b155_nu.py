# -*- coding: utf-8 -*-
"""b155 -- THE NU ACT's instrument.

### WHAT THIS DOES AND DOES NOT DO. It evaluates, at b38's OWN RECORDED COLUMNS,
### the nu-dependence of the identity's finite instance, and prices the freedom.
### IT DOES NOT SPLIT resid_N. The corpus defines only the SUM (b38 names two
### parts and defines neither), the mode count is CAPPED at NTERM = 11 by Lemma
### F.1's uniformity, and b130's ruling makes a mode-count variation a MODEL
### SENSITIVITY rather than a refinement of one object's parts -- so any D_N/R_N
### printed here would rest on a definition the executor made. NONE IS PRINTED.

### EVERY NUMBER BELOW IS A PRICE OR A DIAGNOSTIC. NONE IS A CANONICITY.
### No nu is recommended, endorsed, or called correct by this file.
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# b38's recorded columns, read at content from data/b38_2026-08-18.txt.
# (a^2, A, resid_N, f_cell, D_closed, W_minus, minus_E2even, Thq_minus_PR)
CELLS = [
    (2,  -1.990528, 4.0486, 0.6923, -1.614208, -0.61239, -1.00181, +0.00000),
    (3,  -1.908900, 3.3740, 0.6638, -1.659175, -0.64175, -0.91094, -0.10648),
    (4,  -1.786498, 3.0478, 0.6533, -1.540711, -0.61934, -0.83403, -0.08734),
    (8,  -1.525474, 2.5208, 0.6260, -1.500075, -0.57053, -0.68551, -0.24403),
    (9,  -1.488337, 2.4540, 0.6204, -1.365057, -0.56490, -0.66513, -0.13502),
    (12, -1.405398, 2.3134, 0.6092, -1.365108, -0.54917, -0.62009, -0.19584),
]
SIG = 0.616500298741          # sigma_even, the t-mass even share (b35, recorded)
BAR = "=" * 78


def head(s):
    print("\n" + BAR)
    print(s)
    print(BAR)


head("C0 -- THE READ-BACK CHECK. b38's own components must rebuild its own column.")
print("  D_closed_alt = W_minus - E2even + (Thq - PR), against the recorded D_closed")
worst = 0.0
for a2, A, r, f, dc, wm, mE2, thpr in CELLS:
    alt = wm + mE2 + thpr
    d = abs(alt - dc)
    worst = max(worst, d)
    print("   a^2=%-3d  alt=%+.6f  recorded=%+.6f  |diff|=%.2e" % (a2, alt, dc, d))
print("  ### max |diff| = %.2e -- the two printed forms agree, so the components" % worst)
print("  ### this act differentiates are the ones b38 actually recorded.")
print("  ### SPECIES: an AGREEMENT check between two forms of one recorded row.")
print("  ### It is NOT an error bound and is not quoted as one.")

head("C1 -- THE NU-DERIVATIVE OF THE IDENTITY'S FINITE INSTANCE (the census, as arithmetic).")
print("  The census is a READ, done in the bank. Its arithmetic consequence is here:")
print("  D_closed      = (A - PR) - ((W+ + E2even) - Thq)   ->  d/dmu = + resid_N")
print("  D_closed_alt  =  W- - E2even + (Thq - PR)          ->  d/dmu = + resid_N")
print("  ### BOTH PRINTED FORMS GIVE THE SAME DERIVATIVE. Independent of each other,")
print("  ### because W+ and W- move oppositely and the void gate holds them summed.")
print()
print("  cell   resid_N   d(D_closed)/dmu   |derivative|/|A|")
for a2, A, r, f, dc, wm, mE2, thpr in CELLS:
    print("  %4d  %8.4f      %+9.4f          %8.4f" % (a2, r, r, abs(r / A)))
print("  ### THE DERIVATIVE IS NOWHERE ZERO -- resid_N is recorded nonzero at every")
print("  ### cell. So on the owner-quotable list PROPER (without the flagged")
print("  ### requirement), the verdict is PHYSICAL UNCONDITIONALLY.")

head("C1b -- THE MU THAT WOULD ZERO THE IDENTITY'S RESIDUAL, CELL BY CELL.")
print("  ### THIS IS A DIAGNOSTIC, NOT A RECOMMENDATION. It asks: COULD the freedom")
print("  ### this act named account for the recorded difference? It does not")
print("  ### re-interpret (I-differ), which stands exactly as b38 recorded it.")
print()
print("  cell   D_closed    mu_required = sigma_even - D_closed/resid_N")
mus = []
for a2, A, r, f, dc, wm, mE2, thpr in CELLS:
    mu = SIG - dc / r
    mus.append(mu)
    print("  %4d  %+.6f    %.6f" % (a2, dc, mu))
spread = max(mus) - min(mus)
print()
print("  ### SPREAD ACROSS THE SIX CELLS: %.6f" % spread)
print("  ### ALL SIX EXCEED 1: min = %.6f, max = %.6f" % (min(mus), max(mus)))
print("  ### A SINGLE mu MUST SERVE EVERY CELL -- it is a definitional choice, not a")
print("  ### per-cell one. Six different values are required, none of them a share.")
print("  ### ANSWER: THE FREEDOM CANNOT ACCOUNT FOR THE RECORDED DIFFERENCE.")

head("C2 -- THE PRICE. The freedom's size, split-free, against the certified column.")
print("  Without the flagged requirement the freedom rides the WHOLE residual, and")
print("  resid_N IS recorded. Over the illustrative bracket mu in [0, 1]:")
print()
print("  cell    W+ range = |resid_N|    |A|        range/|A|     f_cell range width")
for a2, A, r, f, dc, wm, mE2, thpr in CELLS:
    print("  %4d       %8.4f          %8.6f    %8.4f      %8.4f"
          % (a2, abs(r), abs(A), abs(r / A), abs(r / A)))
print()
print("  ### THE ADMISSIBLE W+ RANGE EXCEEDS THE CERTIFIED COLUMN ITSELF AT EVERY")
print("  ### CELL, by factors %.2f to %.2f." % (min(abs(r / A) for _, A, r, _, _, _, _, _ in CELLS),
                                                max(abs(r / A) for _, A, r, _, _, _, _, _ in CELLS)))
print("  ### AXIS, per the floor-axis law: this range is a CONFIGURATION span over an")
print("  ### unpinned definitional parameter. It is NOT a discretization floor, NOT an")
print("  ### error bar, and NOT a model sensitivity. It is what the record leaves free.")

head("C2b -- THE CROSSING QUESTION, ANSWERED ON BOTH READINGS, UNDER THE GUARD.")
print("  b109 recorded f - sigma_even declining and crossing between a^2 = 8 and 12.")
print("  A uniform shift of the share by dmu moves each cell's deviation by")
print("  dmu * resid_N/|A| -- ### A CELL-DEPENDENT AMOUNT, not a rigid offset.")
print()
last = CELLS[-1]
a2, A, r, f, dc, wm, mE2, thpr = last
dev_last = f - SIG
need = abs(dev_last) / abs(r / A)
print("  The only negative deviation is a^2 = %d at %+.4f." % (a2, dev_last))
print("  ### IT IS ERASED BY dmu = %.6f -- %.2f parts in a thousand." % (need, need * 1000))
print()
print("  cell   f - sigma_even   after dmu = +%.6f" % need)
for a2, A, r, f, dc, wm, mE2, thpr in CELLS:
    print("  %4d      %+.4f            %+.4f" % (a2, f - SIG, (f - SIG) + need * abs(r / A)))
print("  ### EVERY DEVIATION IS THEN POSITIVE: THE CROSSING IS GONE.")
print()
print("  ### READING 1 -- WITHOUT the flagged requirement (freedom over the whole")
print("  ### residual): ### YES. A shift of %.4f in an unpinned parameter erases it." % need)
print()
SPAN = 1.0 - SIG
thresh = abs(dev_last) * abs(A) / SPAN
print("  ### READING 2 -- WITH the flagged requirement (freedom over the truncation")
print("  ### part R_N only): ### UNDECIDED, because R_N is unmeasured. The threshold:")
print("  ### the crossing is movable within nu in [sigma_even, 1] IFF")
print("  ###     R_N >= |dev| * |A| / (1 - sigma_even) = %.6f at a^2 = %d," % (thresh, last[0]))
print("  ### which is %.4f%% of that cell's recorded resid_N = %.4f." % (100 * thresh / last[2], last[2]))
print("  ### SO ROUTE B HAS A TARGET AND NOT JUST A NAME.")
print()
print("  ### THE GUARD, RIDING: the crossing's LOCATION carries ZERO interpretive")
print("  ### weight here and in anything citing this. Nothing above says the freedom")
print("  ### DOES move the crossing, or that the crossing means anything. It says")
print("  ### only what it would COST to move it. ### NOTICED IS NOT EARNED.")
print()
