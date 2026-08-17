"""A_MAIN IDENTIFIED — what are the 2-3 positive directions of the remainder on V?

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

WHY THIS SITTING EXISTS
========================
The sawtooth NPOS(S_k) = (M - nullity)/2 is a THEOREM about the pure lag form. The measured
operator is A = A_main + c(omega/2) S_k restricted to V, and it agrees with the theorem to
within ONE offender at every cell tested (r = 1 .. 4.3). Two wonders are held open by the
same fact:

    ### A_main IS NOT NEGATIVE SEMIDEFINITE. It has 2-3 POSITIVE EIGENVALUES on V
    ### (measured 2026-08-17 at L = 4.6, 5.5, 7.0: 2, 3, 3 out of 1525-1945 dimensions).

That is the whole obstacle. If those few directions are a FIXED subspace -- the same
functions at every L -- then a bound on their coupling to the lag form closes both wonders
at once. If they MOVE with L, the obstacle is not a fixed finite-dimensional defect and must
be named as moving.

THE QUESTION, POSED EXACTLY
============================
### ARE THE POSITIVE DIRECTIONS OF A_main THE SAME 2-3 DIRECTIONS ACROSS L, OR L-DEPENDENT?

Measured at L in {4.6, 8, 16}, omega = 1e-3 throughout, so the t-grid spacing is identical
and the shorter windows are literal PREFIXES of the longer. Overlaps are therefore taken in
the UNSCALED coordinate t by zero-extension -- no interpolation, no rescaling -- and also in
the RESCALED coordinate u = t/log L, because those two disagree exactly when the answer is
"the modes follow the window" rather than "the modes follow the lag".

WHAT IS MEASURED, PER POSITIVE EIGENVECTOR
===========================================
  parity      <v, reverse(v)> / <v,v>   -> +1 even about the window midpoint, -1 odd
  nodes       number of sign changes
  centroid    of v^2 in t, and in t/log L
  head mass   fraction of v^2 lying in the first log 2 of the window
  smoothness  ||second difference of v|| / (||v|| / omega^2), a dimensionless roughness
  RAYLEIGH    v^T S_k v / v^T v         -> the coupling to the lag form, which is the
                                           quantity a closing bound would have to control
  overlap     against the log-2 K_I low modes, and pairwise across L

REGISTERED EXPECTATION, AND BOTH BRANCHES LONGHAND
===================================================
### REGISTERED: FIXED SUBSPACE, AND IT IS THE log-2 LOW MODES.
The corpus's log-2 gate carries three appreciable K_I eigenvalues with parities even / odd /
even and a cliff at n = 3 (0.0289); the first is the even offender with c_0 ~ 0.951 and the
second is the odd one. The expectation is that A_main's positive directions ARE those modes:
same count at every L, unscaled pairwise overlaps near 1, head mass concentrated in the first
log 2, parities even then odd.

  IF FIXED: the positive index of A_main is a fixed finite defect living at the lag's own
  scale. Then |NPOS(A) - NPOS(S_k)| is bounded by that index for every L, which is exactly
  the bound the sawtooth's operator half needs; and the coefficient silence follows from the
  same bound, since a fixed subspace cannot track a coefficient that scales the rest.
  ### BOTH WONDERS CLOSE ON ONE MEASURED CONSTANT.

  IF L-DEPENDENT -- the count grows with L, or the unscaled overlaps fall while the RESCALED
  ones stay high (modes following the window, not the lag) -- then there is no fixed defect
  to bound. ### THE OBSTACLE IS NAMED AS MOVING, correction twenty is written from it, and
  the sawtooth's operator half stays bench-grade with a reason rather than a slack.

  A third outcome is registered because it is genuinely possible: the count is fixed but the
  modes are neither the log-2 modes nor stable -- ### a fixed-DIMENSION, moving-DIRECTION
  defect, which bounds the count but not the coupling, closing wonder one and not wonder two.

Usage:  python amain_identify.py register
        python amain_identify.py run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

LOG2 = math.log(2.0)
LS = [4.6, 8.0, 16.0]
OM = 1.0e-3


def registration():
    print("=" * 110)
    print("A_MAIN IDENTIFIED — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 110)
    print(__doc__)
    print("  L values: %s   omega = %.1e   grids M = %s"
          % (LS, OM, [int(round(math.log(L) / OM)) for L in LS]))
    print("  k_2 = round(log 2 / omega) = %d  (the log-2 window is the first %d grid points)"
          % (round(LOG2 / OM), round(LOG2 / OM)))
    print("=" * 110)
    sys.stdout.flush()


def amain_V(L, omega, qv, e1p):
    """(A_main restricted to V, the Householder vector u, M) — no prime term at all."""
    M = int(round(math.log(L) / omega))
    t = (np.arange(M) + 0.5) * omega
    d = t[:, None] - t[None, :]
    Y = np.where(d >= 0, np.exp(d / 2.0), 0.0) * omega
    del d
    N = qv[np.abs(np.arange(M)[:, None] - np.arange(M)[None, :])] * (omega / (2 * e1p))
    N *= -1.0
    N[np.diag_indices(M)] += 1.0
    N *= (-2 * e1p)
    A = omega * (Y.T @ N @ Y)
    del Y, N
    A = 0.5 * (A + A.T)
    cv = np.exp(-t / 2.0) * omega
    cv /= np.linalg.norm(cv)
    u = cv.copy()
    s = 1.0 if u[0] >= 0.0 else -1.0
    u[0] += s
    nu2 = float(u @ u)
    a = 2.0 / nu2
    Au = A @ u
    uAu = float(u @ Au)
    A -= a * np.outer(u, Au)
    A -= a * np.outer(Au, u)
    A += (a * a * uAu) * np.outer(u, u)
    return A[1:, 1:], u, M


def lift(w, u):
    """Map a V-coordinate vector w (length M-1) back to the full grid: v = H [0; w]."""
    z = np.concatenate(([0.0], w))
    return z - (2.0 * (u @ z) / (u @ u)) * u


def shift_rayleigh(v, k):
    """v^T S_k v / v^T v with (S_k)_ij = 1 iff |i-j| = k."""
    M = len(v)
    if k >= M:
        return 0.0
    return float(2.0 * np.dot(v[k:], v[:-k]) / np.dot(v, v))


def profile(v, omega, M):
    t = (np.arange(M) + 0.5) * omega
    w = v / np.linalg.norm(v)
    par = float(w @ w[::-1])
    nodes = int(np.sum(np.diff(np.sign(w[np.abs(w) > 1e-12])) != 0))
    p2 = w ** 2
    cent_t = float(p2 @ t)
    k2 = int(round(LOG2 / omega))
    head = float(p2[:min(k2, M)].sum())
    d2 = w[2:] - 2 * w[1:-1] + w[:-2]
    rough = float(np.linalg.norm(d2) / (omega ** 2) / max(np.linalg.norm(w), 1e-300))
    return par, nodes, cent_t, cent_t / (M * omega), head, rough


def log2_low_modes(omega, e1p, qv, nmodes=3):
    """The K_I low modes on the log-2 window — the corpus's own gate eigenvectors."""
    M2 = int(round(LOG2 / omega))
    ks = np.arange(M2)
    A = qv[np.abs(ks[:, None] - ks[None, :])] * (omega / (2 * e1p))
    val, vec = np.linalg.eigh(A)
    o = np.argsort(val)[::-1]
    return val[o][:nmodes], vec[:, o][:, :nmodes], M2


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    need = int(round(math.log(max(LS)) / OM))
    t0 = time.time()
    qv = P._qvals(OM, need, E1.NG_Q)
    print("      [Q_eps table: omega=%.1e, nmax=%d, %.1f s]\n" % (OM, need, time.time() - t0))

    lv, lvec, M2 = log2_low_modes(OM, e1p, qv)
    print("=" * 110)
    print("THE log-2 K_I LOW MODES (the corpus's gate), on %d grid points" % M2)
    print("=" * 110)
    for j in range(3):
        w = lvec[:, j]
        par = float(w @ w[::-1])
        print("  mode %d: eigenvalue %-12.6f parity %+.4f (%s)"
              % (j, lv[j], par, "EVEN" if par > 0 else "ODD"))
    print("  banked gate triple: 1.051772 / 0.687924 / 0.029692, parities even/odd/even")

    k2 = int(round(LOG2 / OM))
    store = {}
    for L in LS:
        print("\n" + "=" * 110)
        print("L = %.1f" % L)
        print("=" * 110)
        A, u, M = amain_V(L, OM, qv, e1p)
        ev, evec = np.linalg.eigh(A)
        pos = np.where(ev > 0)[0]
        print("  M = %d   dim V = %d   ### NPOS(A_main) = %d   lam_max = %.6e  lam_min = %.6e"
              % (M, M - 1, len(pos), float(ev[-1]), float(ev[0])))
        vs = []
        print("  %-4s %-14s %-9s %-6s %-11s %-11s %-11s %-12s %s"
              % ("#", "eigenvalue", "parity", "nodes", "centroid t", "centroid u", "head mass",
                 "roughness", "RAYLEIGH vs S_k"))
        for j in pos[::-1]:
            v = lift(evec[:, j], u)
            vs.append(v)
            par, nodes, ct, cu, head, rough = profile(v, OM, M)
            print("  %-4d %-14.6e %+.4f (%s) %-6d %-11.5f %-11.5f %-11.5f %-12.4g %+.6f"
                  % (len(vs) - 1, float(ev[j]), par, "EVEN" if par > 0 else "ODD ",
                     nodes, ct, cu, head, rough, shift_rayleigh(v, k2)))
        store[L] = vs
        # overlap with the log-2 low modes, on the first k2 grid points
        print("\n  overlap with the log-2 K_I low modes (first %d points, renormalized):" % M2)
        for i, v in enumerate(vs):
            head = v[:M2]
            nh = np.linalg.norm(head)
            if nh < 1e-14:
                print("    v%d : head is numerically zero" % i)
                continue
            head = head / nh
            ovl = [abs(float(head @ lvec[:, j])) for j in range(3)]
            print("    v%d : |<v,mode0>| = %.4f   |<v,mode1>| = %.4f   |<v,mode2>| = %.4f"
                  % (i, ovl[0], ovl[1], ovl[2]))
        sys.stdout.flush()

    print("\n" + "=" * 110)
    print("ACROSS L — the question the sitting was called to answer")
    print("=" * 110)
    print("  counts: %s" % ", ".join("L=%.1f -> %d" % (L, len(store[L])) for L in LS))
    print("\n  UNSCALED overlaps (same omega, shorter zero-extended — no rescaling):")
    for a in range(len(LS)):
        for b in range(a + 1, len(LS)):
            La, Lb = LS[a], LS[b]
            print("    L=%.1f vs L=%.1f" % (La, Lb))
            for i, va in enumerate(store[La]):
                row = []
                for j, vb in enumerate(store[Lb]):
                    n = min(len(va), len(vb))
                    x, y = va[:n], vb[:n]
                    row.append(abs(float(x @ y) / (np.linalg.norm(x) * np.linalg.norm(y))))
                print("      v%d : %s" % (i, "  ".join("%.4f" % r for r in row)))

    print("\n  RESCALED overlaps (u = t/log L, linear interpolation to 2000 points):")
    grid = np.linspace(0.0, 1.0, 2000)
    resc = {}
    for L in LS:
        resc[L] = []
        for v in store[L]:
            M = len(v)
            uu = (np.arange(M) + 0.5) / M
            w = np.interp(grid, uu, v)
            resc[L].append(w / max(np.linalg.norm(w), 1e-300))
    for a in range(len(LS)):
        for b in range(a + 1, len(LS)):
            La, Lb = LS[a], LS[b]
            print("    L=%.1f vs L=%.1f" % (La, Lb))
            for i, va in enumerate(resc[La]):
                row = [abs(float(va @ vb)) for vb in resc[Lb]]
                print("      v%d : %s" % (i, "  ".join("%.4f" % r for r in row)))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
