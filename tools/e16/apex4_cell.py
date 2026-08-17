"""THE FOURTH APEX — L = 256, r = 8.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

The derived count for the pure lag form is NPOS(S_k) = (M - nullity)/2, M = qk + s,
nullity = s (q even) or k - s (q odd). Even q is an apex: NPOS = (q/2)k and 2*NPOS = M.
r = log L / log 2 = 8 at L = 256, so the continuum prediction is 1/2 — the FOURTH apex,
after L = 4, 16, 64.

### AND THE DISCRETIZATION DECIDES WHICH TOOTH THE GRID IS ACTUALLY ON, which is registered
### here as its own finding rather than discovered afterwards:

    omega = 2e-3 : M = round(log 256 / omega) = 2773, k = 347.  2773 / 347 = 7.9914
                   -> q = 7 (ODD), s = 344, nullity = k - s = 3, NPOS = 1385
                   ### the grid lands on the SEVENTH tooth, not the eighth, by rounding
    omega = 1e-3 : M = 5545, k = 693.  5545 / 693 = 8.0014
                   -> q = 8 (EVEN), s = 1, nullity = s = 1, NPOS = 2772 = (M-1)/2
                   ### the grid lands on the eighth tooth: 2772/5544 = 0.500000 EXACTLY

The ferry charters omega = 2e-3. Both are run, because the pair is the point: the same L,
two grids, two different teeth, and the chain formula predicts each from its own (M, k).
### A CONTINUUM PREDICTION OF 1/2 AT L = 256 IS TRUE OF THE LIMIT AND FALSE OF THE 2e-3 GRID,
### and saying so before the run is cheaper than explaining it after.

REGISTERED, both branches longhand:
  IF both cells land within 3 offenders of their own chain prediction, the sawtooth stands at
  r = 1..8, the fourth apex is confirmed at the grid that reaches it, and the near-miss at
  omega = 2e-3 is confirmed as rounding rather than as a failure of the law.
  IF the 2e-3 cell lands near 1/2 instead of at 1385, the chain formula is wrong about which
  tooth a grid sits on, which would be a finding about the discretization and not about the
  law.

Usage:  python apex4_cell.py register | run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1
from wonder1_freeze import chain_npos

LOG2 = math.log(2.0)
L = 256.0
OMEGAS = [2.0e-3, 1.0e-3]
TOL = 3


def registration():
    print("=" * 104)
    print("THE FOURTH APEX — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 104)
    print(__doc__)
    print("  %-10s %-8s %-7s %-6s %-6s %-7s %-10s %-12s %s"
          % ("omega", "M", "k", "q", "s", "null", "CHAIN", "fraction", "tooth"))
    for om in OMEGAS:
        M = int(round(math.log(L) / om))
        k = int(round(LOG2 / om))
        c, q, s, nul = chain_npos(M, k)
        print("  %-10.1e %-8d %-7d %-6d %-6d %-7d %-10d %-12.6f %s"
              % (om, M, k, q, s, nul, c, c / (M - 1),
                 "APEX (q even)" if q % 2 == 0 else "odd tooth (q odd)"))
    print("=" * 104)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    lags = [x for x in E1.lag_schedule(L) if x[0] == "log 2"]
    print("  %-10s %-8s %-14s %-10s %-12s %-12s %s"
          % ("omega", "M", "measured", "CHAIN", "fraction", "predicted", "verdict"))
    for om in OMEGAS:
        t0 = time.time()
        qv = P._qvals(om, int(round(math.log(L) / om)), E1.NG_Q)
        n, dim, frac, M = E1.measure(L, om, lags, qv, e1p)
        k = int(round(LOG2 / om))
        c, q, s, nul = chain_npos(M, k)
        print("  %-10.1e %-8d %-14s %-10d %-12.6f %-12.6f %s  [%.0fs]"
              % (om, M, "%d/%d" % (n, dim), c, frac, c / dim,
                 "### LANDS (%+d)" % (n - c) if abs(n - c) <= TOL else "### FAILS (%+d)" % (n - c),
                 time.time() - t0))
        sys.stdout.flush()
        del qv


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
