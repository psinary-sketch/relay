"""CHECKPOINT B6(c) — THE IDENTIFICATION PROBE ON THE CLASS-LABELLED LIFT. ONE CELL.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

THE QUESTION, REGISTERED BEFORE ANY NUMBER
==========================================
The scalar precedent (F.2026-08-17c/d): the FULL operator's offender count on V agrees with
the PURE shift-graph form's count within ONE offender, at r = 1..8. B6 lifts the bench to
K = Q(sqrt(-23)) -- the corpus's witness, Cl = Z/3 -- with class labels on every lag, and
asks: does full-vs-pure agreement survive the lift, PER PSI-COMPONENT?

THE LIFT, MINIMAL AND DECLARED
==============================
  * Lag set: prime-IDEAL powers q = p^k of K with norm N(q) < L, at address log N(q).
    At the cell below the live norms are 2 and 3, both from SPLIT rational primes whose
    prime ideals are NON-PRINCIPAL (2 and 3 are represented by 2x^2+-xy+3y^2, not by
    x^2+xy+6y^2 -- longhand in the report). Their classes generate Z/3 (index a = 1).
  * Class multiplier per address, per component psi_j (j = 0, 1):
        split p, ideals P^k and Pbar^k at the same address:
            m_j(p, k) = psi_j(P)^k + psi_j(Pbar)^k = 2 cos(2 pi j k / 3)
        (j=0: +2 at every k; j=1: -1 at k not = 0 mod 3, +2 at k = 0 mod 3.)
        psi_2 = conj(psi_1) gives the same real form; two distinct components run.
  * Coefficient convention: the bench's REGISTERED pattern lifted per ideal power,
        C_K(q = P^k) = 2 sqrt(N q) log(N P),   effective c_j(N) = C_K * m_j.
    The Weil sensitivity C_w = 4 log(N P)/sqrt(N q) runs BESIDE the table at one omega.
  * A_main: the bench's own certified archimedean part, UNCHANGED. Declared reason:
    B5(a) -- the archimedean factor is CLASS-SILENT, one scalar structure serves every
    component; a K-native Gamma_C density is a NAMED VARIANT, not run, so the probe
    changes exactly one thing (the lag side).
  * V is imposed on every measurement (the 2026-08-15 ruling). Offenders = positive
    eigenvalues of the V-restricted matrix (phi_layer's reading, unchanged).

THE CELL
========
  L = 3.5, omega in {2e-3, 1e-3, 5e-4} (the corpus's triple; per-omega, never averaged).
  Live norms: 2, 3. Addresses round(log2/om), round(log3/om) -- at 1e-3: 693, 1099,
  BOTH ODD -> the graph is BIPARTITE (2-colouring audited in-run, not assumed). No
  prime-ideal square is live (norm 4 needs L > 4), so the cell sits inside the regime
  where the matching-number law is derived.

REGISTERED PREDICTIONS, BOTH BRANCHES LONGHAND
==============================================
P1  PURE counts for psi_0 and psi_1 are EQUAL at each omega -- the bipartite
    weight-independence law covers any nonzero real weights, sign included (psi_1's
    multiplier is -1 at both lags: a global sign on positive weights).
    -> IF NOT: the derived law's stated scope is wrong at its own witness cell, which
       is a first-class finding against the week's law, filed before anything else.
P2  THE PROBE. |full - pure| <= 1 offender PER COMPONENT at every omega -- the scalar
    precedent's margin, now asked of the lift.
    -> BRANCH A (holds): the identification mechanism (full tracks pure) survives the
       class lift at this cell; column (iii)'s bench half extends to the lifted object.
       BENCH-GRADE, ONE CELL -- proved nowhere, and the report says so.
    -> BRANCH B (fails): the class weights interact with A_main beyond the scalar
       precedent -- the finding is the profile of the disagreement (which component,
       which sign). psi_1 is the stress case: its lag terms enter with a GLOBAL
       NEGATIVE sign, the configuration the scalar bench never measured.
GATE  The scalar known-answer row (L = 3 on V, exp1's three targets) must reproduce
      exactly before the probe runs; a gate failure is the result.

Usage:  python b6_class_probe.py register | run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

L_CELL = 3.5
OMEGAS = [2.0e-3, 1.0e-3, 5.0e-4]

# norms live at L=3.5: (norm N, class index a, split multiplicity handled via multiplier)
# split p=2: ideals P2, P2bar, class a=1; split p=3: P3, P3bar, class a=1.
LIVE = [(2, 2, 1), (3, 3, 1)]     # (norm, base rational p, k)
CLASS_INDEX = {2: 1, 3: 1}        # a in Z/3 for the prime ideal above p (sign-free)


def multiplier(j, a, k):
    """psi_j(P)^k + psi_j(Pbar)^k = 2 cos(2 pi j a k / 3)."""
    return 2.0 * math.cos(2.0 * math.pi * j * a * k / 3.0)


def lags_for_component(j, cf):
    out = []
    for N, p, k in LIVE:
        base = cf(N, p)              # lifted convention: cf(Nq, Np) with Nq=N, NP=p
        m = multiplier(j, CLASS_INDEX[p], k)
        out.append(("logN %d (m=%+.0f)" % (N, m), math.log(N), base * m))
    return out


def pure_matrix_V(L, omega, lags):
    """The LAG-ONLY matrix on V — phi_matrix_V minus its archimedean part."""
    M = int(round(math.log(L) / omega))
    t = (np.arange(M) + 0.5) * omega
    A = np.zeros((M, M))
    for lab, ell, c in lags:
        k = int(round(ell / omega))
        if 0 < k < M:
            idx = np.arange(M - k)
            A[idx + k, idx] += 0.5 * c * omega
            A[idx, idx + k] += 0.5 * c * omega
    A = 0.5 * (A + A.T)
    cv = np.exp(-t / 2.0) * omega
    cv /= np.linalg.norm(cv)
    return E1._householder_restrict(A, cv), M


def bipartite_audit(L, omega):
    """2-colouring of the union shift graph; returns (is_bipartite, addresses)."""
    M = int(round(math.log(L) / omega))
    ks = [int(round(math.log(N) / omega)) for N, _, _ in LIVE]
    colour = -np.ones(M, dtype=int)
    ok = True
    for s in range(M):
        if colour[s] >= 0:
            continue
        colour[s] = 0
        stack = [s]
        while stack:
            v = stack.pop()
            for k in ks:
                for w in (v - k, v + k):
                    if 0 <= w < M:
                        if colour[w] < 0:
                            colour[w] = 1 - colour[v]
                            stack.append(w)
                        elif colour[w] == colour[v]:
                            ok = False
    return ok, ks


def registration():
    W = 100
    print("=" * W)
    print("B6(c) — THE CLASS-LABELLED IDENTIFICATION PROBE · REGISTRATION. NO MEASURED NUMBER.")
    print("=" * W)
    print(__doc__)
    print("  the component coefficients at the cell (registered convention):")
    print("  %-8s %-24s %-24s" % ("norm", "psi_0", "psi_1"))
    for N, p, k in LIVE:
        c = E1.coeff(N, p)
        print("  %-8d %-24.6f %-24.6f"
              % (N, c * multiplier(0, CLASS_INDEX[p], k), c * multiplier(1, CLASS_INDEX[p], k)))
    print("=" * W)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    print("  eps'(1+) = %.7f  (target 22.996476)" % e1p)
    nmax = {om: int(round(math.log(L_CELL) / om)) for om in OMEGAS}
    qvs = {}
    for om in OMEGAS:
        t0 = time.time()
        qvs[om] = P._qvals(om, max(nmax[om], int(round(math.log(3.0) / om))), E1.NG_Q)
        print("      [Q_eps table: omega=%.1e, %.1f s]" % (om, time.time() - t0))
        sys.stdout.flush()

    ok, _ = E1.gate(qvs, e1p)
    if not ok:
        print("\n### THE GATE DID NOT PASS. THE PROBE IS NOT RUN. THAT IS THE RESULT.")
        return

    W = 108
    for tag, cf, oms in [("REGISTERED  C_K = 2 sqrt(Nq) log(NP)", E1.coeff, OMEGAS),
                         ("SENSITIVITY  C_w = 4 log(NP)/sqrt(Nq)", E1.coeff_weil, [1.0e-3])]:
        print("\n" + "=" * W)
        print("THE PROBE — %s   ·   L = %.1f" % (tag, L_CELL))
        print("=" * W)
        print("  %-10s %-6s %-11s %-6s %-22s %-22s %s"
              % ("omega", "M", "bipartite", "comp", "PURE (npos/dim)", "FULL (npos/dim)", "|full-pure|"))
        for om in oms:
            bip, ks = bipartite_audit(L_CELL, om)
            for j in (0, 1):
                lags = lags_for_component(j, cf)
                Ap, M = pure_matrix_V(L_CELL, om, lags)
                np_pure = int((np.linalg.eigvalsh(Ap) > 0).sum())
                dim = Ap.shape[0]
                del Ap
                nf, dimf, frac, _ = E1.measure(L_CELL, om, lags, qvs[om], e1p)
                print("  %-10.1e %-6d %-11s psi_%d  %-22s %-22s %d"
                      % (om, M, ("YES (k=%s)" % ",".join(map(str, ks))) if bip else "### NO",
                         j, "%d / %d" % (np_pure, dim), "%d / %d" % (nf, dimf),
                         abs(nf - np_pure)))
                sys.stdout.flush()
        print("=" * W)


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
