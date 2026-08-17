"""THE MATCHED-PAIR CONTROL — same grid dimension, different window.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

WHY THIS CONTROL EXISTS
========================
The third window returned ### NPOS(A_main) = 37 at L = 256 (r = 8, M = 5545), against 5 at
r = 4 and 8 at r = 6, and the u-family stopped matching by node count. Before any of that is
reported as a finding about the WINDOW, it has to be separated from a finding about the GRID:
M grew from 2773 to 4159 to 5545 at the same time r grew from 4 to 6 to 8, and the two are
confounded in every cell measured so far.

    ### THE CORPUS'S OWN INSTRUMENT FOR EXACTLY THIS: the matched-pair collision -- two points
    ### at the same value of one variable, differing in the other. Its spread measures directly
    ### what the reading says is not there.

AND THE COLLISION IS FREE HERE, BECAUSE THE ARITHMETIC HANDS IT OVER:

    L = 16,  omega = 1e-3  ->  M = 2773,  k = 693,  r = 4.0014
    ### L = 256, omega = 2e-3  ->  M = 2773,  k = 347,  r = 7.9914

### THE SAME GRID DIMENSION, TO THE POINT. Same matrix size, same eigensolver, same everything
### except the window the grid is spread over.

REGISTERED, BOTH BRANCHES LONGHAND, BEFORE THE RUN
===================================================
C1  IF NPOS(A_main) at (L=256, 2e-3) comes out LARGE -- comparable to the 37 measured at
    (L=256, 1e-3) -- then ### THE COUNT IS DRIVEN BY r, NOT BY M. The jump from 8 to ~37
    between r = 6 and r = 8 is a property of the window, the family genuinely reorganises,
    and the scaling limit filed on two windows is refuted by the third.

C2  IF it comes out SMALL -- comparable to the 5 measured at (L=16, 1e-3), which has the same
    M -- then ### THE COUNT IS DRIVEN BY M, NOT BY r, the 37 at the finer grid is a
    resolution effect, and the whole third-window verdict has to be re-read as an instrument
    statement before it can be read as a mechanism statement.

C3  Reported either way: the positive spectrum's MAGNITUDES, so that eigenvalues sitting at
    the numerical floor can be separated from real ones. At (L=256, 1e-3) the positive list
    ran down to 3.6e-8, three orders below the smallest robust positive at r = 6, and a count
    that includes those is not the same quantity as a count that does not.
    ### A THRESHOLD SWEEP IS PRINTED SO THE COUNT CAN BE READ AT A STATED FLOOR.

Usage:  python ladder_control.py
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1
from amain_identify import amain_V

LOG2 = math.log(2.0)
CELLS = [(16.0, 1.0e-3), (256.0, 2.0e-3), (64.0, 1.5e-3)]
FLOORS = [0.0, 1e-6, 1e-5, 1e-4]


def main():
    print("=" * 108)
    print("THE MATCHED-PAIR CONTROL — REGISTRATION, then measurement")
    print("=" * 108)
    print(__doc__)
    print("  %-8s %-9s %-8s %-7s %-9s" % ("L", "omega", "M", "k", "r = M/k"))
    for L, om in CELLS:
        M = int(round(math.log(L) / om))
        k = int(round(LOG2 / om))
        print("  %-8.0f %-9.1e %-8d %-7d %-9.4f" % (L, om, M, k, M / k))
    print("=" * 108)
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    sys.stdout.flush()

    e1p = Q.epsprime1()
    print("  %-8s %-9s %-8s %-9s %s"
          % ("L", "omega", "M", "r", "NPOS(A_main) at floor 0 / 1e-6 / 1e-5 / 1e-4"))
    for L, om in CELLS:
        M0 = int(round(math.log(L) / om))
        t0 = time.time()
        qv = P._qvals(om, M0, E1.NG_Q)
        A, u, M = amain_V(L, om, qv, e1p)
        ev = np.linalg.eigvalsh(A)
        del A
        k = int(round(LOG2 / om))
        counts = [int((ev > f).sum()) for f in FLOORS]
        pos = ev[ev > 0]
        print("  %-8.0f %-9.1e %-8d %-9.4f %-4d / %-4d / %-4d / %-4d      [%.0fs]"
              % (L, om, M, M / k, counts[0], counts[1], counts[2], counts[3], time.time() - t0))
        if len(pos):
            print("        largest %.4e   smallest positive %.4e   |lam_min| %.4e"
                  % (float(pos[-1]), float(pos[0]), abs(float(ev[0]))))
        del qv, ev
        sys.stdout.flush()

    print("\n" + "=" * 108)
    print("  READ: the first two rows share M = 2773 exactly. If their counts differ, the")
    print("  driver is r (C1). If they agree, the driver is M (C2).")
    print("=" * 108)


if __name__ == "__main__":
    main()
