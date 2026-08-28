# -*- coding: utf-8 -*-
"""b233_resid_diag.py -- WHAT ACTUALLY BOUNDS THE RESIDUAL. A DIAGNOSTIC, NOT A VERIFICATION.

### b233 REGISTERED, IN ADVANCE: "the truncation tail, not the mathematics, bounds the residual."
### ### THAT REGISTERED EXPECTATION WAS REFUTED BY THE RUN. The tail bounds came out at 1e-21
### to 1e-27 while the residuals sat at 1e-13 (a^2=2) and ~1e-8 (a^2=3, 4). ### THE RESIDUAL IS
### NOT THE TAIL.

### THIS SCRIPT DOES NOT RE-GRADE ANYTHING AND DOES NOT RESCUE THE VERDICT. ### It tests ONE
### hypothesis about where the residual comes from, so the failure is DIAGNOSED rather than
### merely reported:

###   HYPOTHESIS -- the prime column's `np.interp(ln, vc, corr)` is LINEAR interpolation on the
###   `corr` grid, whose error is O((dv)^2). ### PREDICTION: the residual is independent of the
###   zero-side truncation N (already observed), and SCALES LIKE 1/NV^2 -- doubling the v-grid
###   should cut it by about four. ### And at a^2 = 2 the prime column is EMPTY (PR = 0 exactly),
###   so on this hypothesis that cell should show a residual orders smaller. ### ALREADY OBSERVED.

### ### IF THE SCALING HOLDS, THE DIAGNOSIS IS THE INSTRUMENT'S QUADRATURE, NOT THE FORMULA.
### ### IF IT DOES NOT, THE DIAGNOSIS IS WRONG AND IS REPORTED WRONG.
"""
import io
import json
import math
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C        # noqa: E402
import b38_act10 as B38        # noqa: E402

CACHE = (r"C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--"
         r"\2bde398e-07cf-4dd0-8608-0a3b93e6f10a\scratchpad\b233_zeros.json")
CELLS = [(2, "2"), (3, "3"), (4, "4")]
PRIMES = (2, 3, 5)


def main():
    gam = np.array(json.load(io.open(CACHE, encoding='utf-8'))[:1000], dtype=float)
    print("=" * 92)
    print("b233 -- RESIDUAL DIAGNOSTIC. ### NOT A VERIFICATION, NOT A RE-GRADE.")
    print("=" * 92)
    print("### THE REGISTERED CRITERION (tail-bounded) FAILED. THIS ASKS WHY, AND CAN SAY 'WRONG'.")
    print("\n  %-6s %8s %14s %14s %10s" % ("a^2", "NV", "PR", "residual", "ratio"))
    base_nv = C.NV
    for a_sq, tag in CELLS:
        a = math.sqrt(a_sq)
        prev = None
        for nv in (2001, 4001, 8001, 16001):
            C.NV = nv
            C._KERN = None
            v, w, corr, vc, L = B38.family(a)
            A, P, PR = B38.left_side(a, PRIMES, v, w, corr, vc, L)
            g = C.hhat(*C.bump(a), gam)
            Z = 2.0 * float(np.sum(g * g))
            resid = Z - (P - PR + A)
            ratio = (abs(prev / resid) if prev not in (None, 0.0) and resid != 0.0 else float('nan'))
            print("  %-6s %8d %14.9f %14.3e %10.2f" % (tag, nv, PR, resid, ratio))
            prev = resid
        print()
    C.NV = base_nv
    C._KERN = None
    print("=" * 92)
    print("  ### READ THE `ratio` COLUMN: ~4.0 on each doubling of NV means O((dv)^2) --")
    print("  ### LINEAR INTERPOLATION IN THE PRIME COLUMN. ### Anything else refutes the")
    print("  ### hypothesis, and the act reports it refuted.")
    print("  ### a^2 = 2 CARRIES PR = 0 EXACTLY (no prime power <= 2 other than 2 itself at the")
    print("  ### cutoff), so on this hypothesis its residual is a DIFFERENT, much smaller effect.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
