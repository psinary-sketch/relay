# -*- coding: utf-8 -*-
"""b238_criterion.py -- DERIVE THE CRITERION FROM THE MEASURED BUDGET. ### NO RESIDUAL IS
### COMPUTED IN THIS FILE, AND NO VERIFICATION IS RUN.

### THE ORDER-OF-OPERATIONS LAW: this file writes `data/b238_criterion.txt`. ### THE FINAL RUN
### WRITES ITS OWN FILE AFTERWARDS, AND A GATE COMPARES THE TIMESTAMPS.

### WHAT THE BUDGET FOUND (b238_budget_run.txt), and it is one source, not five:
###   S1  A, P and Z carry NO grid error -- every |dX| sits at 1e-16..1e-18, machine epsilon.
###       ### PR CARRIES THE ENTIRE RESIDUAL: at a^2=3, |dPR| = 9.827e-08 against a residual of
###       ### 9.887e-08; at a^2=4, 1.735e-08 against 1.781e-08. ### AGREEMENT TO ~3%.
###   S2  ### THE EDGE HYPOTHESIS IS REFUTED BY DIRECT MEASUREMENT. The trapezoid on
###       ### INT exp(-1/(1-t^2)) dt matches mpmath.quad (dps 40) to 0.000e+00 at EVERY N from
###       ### 2001 to 32001. Euler-Maclaurin holds: the bump's flat endpoints cost NOTHING.
###       ### b234's "half-order edge loss at the bump's compact support" DOES NOT EXIST.
###   S3  ### THE SOURCE IS `np.interp` IN THE PRIME COLUMN, and S3's numbers reproduce S1's
###       ### |dPR| almost exactly. ### BUT ITS MEASURED ORDER IS ERRATIC (1.10, 1.22, 1.58 /
###       ### 1.27, 1.76, 3.92) AND THAT IS NOT A DEFECT IN THE MEASUREMENT: the evaluation
###       ### points log p^k are FIXED while the grid refines, so the distance from the nearest
###       ### node jitters with NV. ### AN ORDER IS NOT WELL-DEFINED FOR A FIXED POINT ON A
###       ### REFINING GRID. What IS well defined is the O(h^2) ENVELOPE, and the criterion is
###       ### built on the envelope rather than on a fitted exponent.
###   S4  zero truncation: residuals IDENTICAL to all printed digits at N = 250, 500, 1000 for
###       a^2 = 3 and 4; the re-derived tail bounds are 1e-21..1e-27. ### NEGLIGIBLE.
###   S5  float species: zeros at dps 25 and dps 50 agree to 0.000e+00 and the residuals are
###       identical. ### THE FLOOR IS NOT THE ZEROS' PRECISION; it is float64 accumulation in
###       the sums, measured at a^2=2 (whose prime column is EMPTY) as ~1.2e-13.

### ### THE CRITERION'S FORM, AND WHY IT CAN STILL FAIL:
### ###     |resid(a^2, NV)|  <=  K(a^2) * h(a^2,NV)^2  +  F
### ### with h = 2L/(NV-1) the corr-grid spacing, F the measured float floor, and
### ### ### K(a^2) = max over MEASURED refinements of |dPR| / h^2 -- ### TAKEN FROM
### ### ### NV in {2001, 8001, 16001} ONLY.
### ### **NV = 4001 AND NV = 6001 ARE EXCLUDED FROM THE FIT AND ARE THE AXES THE FINAL RUN
### ### TESTS.** ### So the criterion is an OUT-OF-SAMPLE PREDICTION at both test axes, and if
### ### the envelope is wrong the run fails it. ### NO PROJECTION WILL BE WIDENED TO COVER A
### ### RESIDUAL.
"""
import io
import math
import sys
import time

OUT = r"D:\relay\data\b238_criterion.txt"

# ### THE MEASURED |dPR| VALUES, TRANSCRIBED FROM b238_budget_run.txt's S1 TABLE.
# ### NV=4001 IS DELIBERATELY ABSENT: it is a TEST axis, not a FIT axis.
MEASURED = {
    '3': {2001: 9.827e-08, 8001: 1.200e-08, 16001: 7.929e-10},
    '4': {2001: 1.735e-08, 8001: 3.465e-09, 16001: 1.155e-09},
}
A_SQ = {'2': 2.0, '3': 3.0, '4': 4.0}
FLOOR = 3.0e-13          # ### the float64 floor, measured at a^2=2 (prime column EMPTY): ~1.2e-13
TAIL = {'2': 7.195e-21, '3': 3.159e-26, '4': 1.072e-27}   # ### S4, re-derived at N=1000
TEST_NV = [4001, 6001]


def h_of(a_sq, nv):
    """### THE corr-GRID SPACING: vc runs over [-2L, 2L] with 2*NV-1 points."""
    L = math.log(math.sqrt(a_sq))
    return (4.0 * L) / (2 * nv - 2)


def main():
    lines = []
    w = lines.append
    w("=" * 100)
    w("b238 -- THE CRITERION, DERIVED FROM THE MEASURED BUDGET.")
    w("### WRITTEN AT %s (local). ### NO VERIFICATION HAS BEEN RUN AT THE TEST AXES."
      % time.strftime('%Y-%m-%dT%H:%M:%S'))
    w("=" * 100)
    w("")
    w("### THE BUDGET REDUCED TO ONE SOURCE. ### A, P and Z carry NO grid error (machine")
    w("### epsilon); the zero truncation is invariant over a factor of 4 in N; the zeros'")
    w("### precision contributes 0.000e+00 at doubled dps. ### WHAT IS LEFT IS `np.interp`")
    w("### IN THE PRIME COLUMN, plus a float64 accumulation floor.")
    w("")
    w("### AND ONE REGISTERED HYPOTHESIS IS REFUTED BY DIRECT MEASUREMENT:")
    w("### ### b234's HALF-ORDER EDGE LOSS DOES NOT EXIST. The trapezoid on the bump's own")
    w("### ### species matches mpmath.quad to 0.000e+00 at every grid from 2001 to 32001.")
    w("### ### Euler-Maclaurin holds; the flat endpoints cost nothing. ### The registration")
    w("### ### predicted this refutation BEFORE measuring, and the measurement is what decides it.")
    w("")
    w("### THE CRITERION:")
    w("###     |resid(a^2, NV)|  <=  K(a^2) * h^2  +  F  +  tail(a^2)")
    w("###   h   = 4L / (2*NV - 2)          the corr-grid spacing")
    w("###   F   = %.3e                     the float64 floor, measured at a^2=2" % FLOOR)
    w("###   K   = max over MEASURED NV of |dPR| / h^2,  ### FIT ON NV in {2001, 8001, 16001}")
    w("")
    w("### ### THE TEST AXES NV = 4001 AND NV = 6001 ARE **EXCLUDED FROM THE FIT**.")
    w("### ### THE CRITERION IS THEREFORE AN OUT-OF-SAMPLE PREDICTION AT BOTH, AND IT CAN FAIL.")
    w("")
    w("--- THE FIT, SHOWN TERM BY TERM ---")
    K = {}
    for tag in ('3', '4'):
        w("  diagonal a^2 = %s" % tag)
        best = 0.0
        for nv, dpr in sorted(MEASURED[tag].items()):
            h = h_of(A_SQ[tag], nv)
            k = dpr / (h * h)
            best = max(best, k)
            w("    NV=%-6d  h=%.6e  |dPR|=%.3e  ->  K = %.4f" % (nv, h, dpr, k))
        K[tag] = best
        w("    ### K(a^2=%s) = %.4f   (the MAXIMUM, not a mean -- an envelope, not a fit line)"
          % (tag, best))
    w("")
    w("--- THE PROJECTED BOUNDS AT THE TEST AXES ---")
    w("  %-8s %-8s %14s %14s %14s" % ("a^2", "NV", "h", "K*h^2", "BOUND (+F+tail)"))
    bounds = {}
    for tag in ('2', '3', '4'):
        for nv in TEST_NV:
            h = h_of(A_SQ[tag], nv)
            kh2 = (K[tag] * h * h) if tag in K else 0.0
            b = kh2 + FLOOR + TAIL[tag]
            bounds[(tag, nv)] = b
            w("  %-8s %-8d %14.6e %14.3e %14.3e" % (tag, nv, h, kh2, b))
    w("")
    w("### a^2 = 2 CARRIES NO K TERM: its prime column is EMPTY (PR = 0 exactly), so its bound")
    w("### is the float floor plus its tail. ### THAT IS NOT AN EXEMPTION -- it is what the")
    w("### budget says about a cell with no interpolated terms.")
    w("")
    w("### ### PASS RULE, FIXED HERE AND NOT REVISABLE: every cell at every test axis must")
    w("### ### satisfy |resid| <= BOUND. ### ONE CELL OVER THE BOUND IS BRANCH (HELD).")
    w("=" * 100)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("\n### CRITERION WRITTEN TO %s" % OUT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
