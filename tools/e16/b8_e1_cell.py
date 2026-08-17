"""B8-RIDERS(1) — THE E1 CELL: the candidate trace on lag-log q data. AUTHOR'S WORD GIVEN.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.
POSITIVITY GUARD ON THE FACE: a positive local trace bears not at all on h2.

THE MEASUREMENT, DERIVED LONGHAND IN THIS REGISTRATION
======================================================
At a finite place the scaling group is DISCRETE: p^Z, step log p. So the compressed action
integrated against a test function g is a SUM over the lags the explicit formula uses:

    theta_p(g) = log p * Sum_k g(k log p) U^k,     U = scaling by p (|p|^{1/2}-normalized),

and the candidate trace T(g) = Tr(theta_p(g) S theta_p(g)*) is a positive sesquilinear form
in the lag data {g(k log p)} with kernel M_{k,k'} = Tr(U^k S U^{k'+}) -- the (alpha) sandwich
shape by construction (T(g) = ||S^{1/2} theta(g)*||_F^2 >= 0).

THE (beta) QUESTION: the coefficient the trace assigns to the pure lag-log q correlation is
    t_k = |Tr(U^k S)|          (the g_k gbar_0 cross-coefficient; q = p^k),
and its q-scaling is read against the two banked conventions, PREDICTED LONGHAND HERE:

    registered  C(q) = 2 sqrt(q) log p     ->  t_k ~ q^{+1/2}: factor sqrt(p) per lag step
    Weil        C(q) = 4 log p / sqrt(q)   ->  t_k ~ q^{-1/2}: factor 1/sqrt(p) per lag step
    ratio (registered/Weil) at lag q: q/2  -- THE FERRY'S "ratio q" IS THE SHAPE-RATIO,
                                              the constant 2 dropped; flagged per Rule 3.

Also reported: d_k = Tr(U^k S U^{k+}) (the diagonal lag mass) and n_k = ||S U^k S||_F (the
norm channel, B8's Q at k = 1) -- so the middle verdict has its named location:

VERDICTS (registered before any number):
    (beta)-CARRYING at named convention   t_k nonzero with fitted q-power ~ +1/2 (registered)
                                          or ~ -1/2 (Weil), consistently across cells
    WEIGHT-PRESENT-IN-NORM-ABSENT-IN-TRACE  t_k = 0 at machine precision while n_k > 0 --
                                          the leak located: the TRACE kills what the NORM
                                          carries (a strictly shell-lowering operator traced
                                          against a projection can vanish identically while
                                          its compressed norm does not)
    NEITHER                               t_k nonzero with some other power; filed, no fit.

Registered expectation from B8's laws: at n = 1 everything compressed vanishes (the
(p^{n-1} - 1) factor); the decisive cells are n >= 2.

CELLS: p in {2,3,5} x n in {1,2,3}, EXCEPT (5,3) where only the trace channel runs (the
N = 15625 projection is handled by the low-rank identity S = I - C^+ C, so Tr(U^k S) =
Tr(U^k) - Tr((C U^k) C^+) is cheap while the norm channel is a dense 15625^2 object --
declared, not silently skipped).

Usage:  python b8_e1_cell.py register | run
"""
import sys
import numpy as np

import b8_sonin_dim as B8

CELLS = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (5, 1), (5, 2), (5, 3)]


def constraints(p, n):
    N, F, ball = B8.model(p, n)
    C = np.vstack([np.eye(N)[ball], F[ball]])
    return N, C


def trace_channel(p, n, kmax):
    """t_k = |Tr(U^k S)| via S = I - C^+ C (cheap at any N)."""
    N, C = constraints(p, n)
    Cp = np.linalg.pinv(C)
    U1 = B8.scaling_matrix(p, n)
    out = []
    Uk = np.eye(N)
    for k in range(1, kmax + 1):
        Uk = U1 @ Uk
        trU = np.trace(Uk)
        # Tr(U^k C^+ C) = Tr(C U^k C^+) = elementwise sum (C U^k)_{ij} (C^+)_{ji}
        trUCC = np.sum((C @ Uk) * Cp.T)
        out.append(abs(complex(trU - trUCC)))
    return out


def full_channels(p, n, kmax):
    """t_k, d_k, n_k with the explicit projection (N <= 729)."""
    N, K = B8.sonin_basis(p, n)
    S = K @ K.conj().T
    U1 = B8.scaling_matrix(p, n)
    t, d, nn = [], [], []
    Uk = np.eye(N)
    for k in range(1, kmax + 1):
        Uk = U1 @ Uk
        t.append(abs(np.trace(Uk @ S)))
        d.append(float(np.real(np.trace(Uk @ S @ Uk.conj().T))))
        nn.append(float(np.linalg.norm(S @ Uk @ S)))
    return t, d, nn


def registration():
    print("=" * 100)
    print("B8-RIDERS(1) — THE E1 CELL · REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("  longhand per-cell convention predictions (coefficient at lag q = p^k):")
    print("  %-6s %-4s %-18s %-18s %-12s" % ("q", "p^k", "registered 2sqrt(q)logp", "Weil 4logp/sqrt(q)", "ratio (=q/2)"))
    import math
    for p in (2, 3, 5):
        for k in (1, 2):
            q = p ** k
            r = 2 * math.sqrt(q) * math.log(p); w = 4 * math.log(p) / math.sqrt(q)
            print("  %-6d %d^%d  %-18.6f %-18.6f %-12.1f" % (q, p, k, r, w, r / w))
    print("=" * 100)
    sys.stdout.flush()


def run():
    print("  %-4s %-4s %-8s %-28s %-28s %-28s" % ("p", "n", "N", "t_k = |Tr(U^k S)|", "d_k = Tr(U^k S U^k+)", "n_k = ||S U^k S||_F"))
    for p, n in CELLS:
        N = p ** (2 * n)
        kmax = 2 * n - 1
        if N <= 729:
            t, d, nn = full_channels(p, n, kmax)
            print("  %-4d %-4d %-8d %-28s %-28s %-28s"
                  % (p, n, N, " ".join("%.4e" % x for x in t),
                     " ".join("%.4e" % x for x in d), " ".join("%.4e" % x for x in nn)))
        else:
            t = trace_channel(p, n, kmax)
            print("  %-4d %-4d %-8d %-28s %-28s %-28s"
                  % (p, n, N, " ".join("%.4e" % x for x in t), "(declared skipped)", "(declared skipped)"))
        sys.stdout.flush()


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
