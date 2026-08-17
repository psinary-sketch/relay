"""LEMMA 5.2 ON THE WIDE RANGE — the critical-path item, attacked from the supplied formulas.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

WHAT IS ON DISK AND WHAT IS NOT — SAID FIRST, BECAUSE IT BOUNDS EVERY VERDICT BELOW
====================================================================================
ON DISK, at content, supplied 2026-08-15 and banked in qeps_layer.py's docstring:
    (b) xi_n^an and its derivative, DECLARED ENTIRE; zeta_n
    (c) eps(rho), their (85), with the support law: integrand lives only on [rho^-1, 1]
    (d) Qeps(rho), their Prop 5.3 / eq. (100), the three-term C_n(rho)
    (e) K_I, N_I    (f) V, Y+, Phi
    Lemma F.1's truncation claim, as a sentence: "first 11 terms uniform to 1e-11"

NOT ON DISK: ### CC's STATEMENT OF LEMMA 5.2, AND CC's PROOF OF IT.
    What the corpus records is two banked facts, both from the 2026-08-13 ferry supply
    (relay reports/2026-08-13-attempt1-sitting7-read-banks-transfer.md 1.4):
        "Prop 5.5 | hypothesis 'I subset [-log 2, log 2] of length <= log 2'"
        "Lemma 5.2 | derived for rho in (1,2]"
    and sitting 7's identification of what the debt actually is:
        "THE (Qeps) SERIES' VALIDITY ON (1,3] IS EXACTLY Lemma 5.2's un-re-derived
         extension."

### THEREFORE THIS ACT DOES NOT AUDIT CC's PROOF. IT CANNOT: the proof is not here.
### WHAT IT DOES IS RE-DERIVE FROM THE SUPPLIED FORMULAS, which is a different act with a
### different scope, and the verdict is stated at that scope and no wider.
    Kin, standing and binding here: A RETRIEVAL GLOSS IS NOT THE SOURCE. The Apostol rider
    was reported BLOCKED rather than filled in from recall; the same discipline applies to a
    lemma statement I do not hold.

THE STRUCTURAL RE-DERIVATION, DONE ON PAPER BEFORE ANY NUMBER (recorded here, then tested)
==========================================================================================
Write the supplied (100) with the eigenvalue factors made explicit:

    Qeps(rho) = sum_n [lam_n^2/(1-lam_n^2)] C_n(rho)

    C_n(rho) = rho^(1/2)  int_{1/rho}^{1} [x (xi^an)'(x)][rho x (xi^an)'(rho x)] dx
             + rho^(-3/2) (xi^an)'(1/rho) xi^an(1)
             - rho^(3/2)  xi^an(1) (xi^an)'(rho)

Every occurrence of xi^an carries a 1/lam, by its own supplied definition
(b): xi_n^an = (2/lam) int_0^1 xi_n cos(2 pi t x) dt. Define the LAMBDA-FREE quantities

    A_n(X) :=  2 int_0^1 xi_n(t) cos(2 pi t X) dt        = lam_n * xi_n^an(X)
    D_n(X) := -4 pi int_0^1 t xi_n(t) sin(2 pi t X) dt   = lam_n * (xi_n^an)'(X)

Every term of C_n is a PRODUCT OF EXACTLY TWO of these, so C_n = Chat_n / lam_n^2 with

    Chat_n(rho) = rho^(1/2)  int_{1/rho}^{1} [x D_n(x)][rho x D_n(rho x)] dx
                + rho^(-3/2) D_n(1/rho) A_n(1)
                - rho^(3/2)  A_n(1) D_n(rho)

### AND THEN THE PREFACTOR CANCELS EXACTLY:

    [lam_n^2/(1-lam_n^2)] * C_n(rho) = Chat_n(rho) / (1 - lam_n^2)

### THE Qeps SERIES CARRIES NO EIGENVALUE-DECAY FACTOR AT ALL. The lam^2 that looks like it
### supplies convergence is consumed by the two analytic continuations, and 1/(1-lam_n^2)
### tends to 1. Convergence rests ENTIRELY on Chat_n(rho) -> 0, i.e. on the decay of the
### prolate functions' own Fourier transforms sampled at frequencies up to rho.

TWO SEPARATE QUESTIONS, WHICH THE VERDICT MUST NOT CONFLATE
-----------------------------------------------------------
(Q1) THE FORMULA. Does (100) as an expression have a rho-restriction?
     Structurally: NO, and this is settled on paper. xi^an and (xi^an)' are DECLARED ENTIRE
     by the supplied (b); the integral runs over [1/rho, 1], a bounded interval inside (0,1]
     for every rho >= 1; the two boundary terms evaluate entire functions at the finite
     points 1/rho, 1, rho. ### NO STEP IN (100) DEGRADES AT rho = 2, AT rho = 3, OR ANYWHERE.
     The overlap [rho^-1, 1] SHRINKS as rho grows, which is the opposite of an obstruction.
(Q2) THE SERIES. Does sum_n Chat_n(rho)/(1-lam_n^2) converge, and does the 11-term
     truncation hold, at each rho? ### THIS IS NOT SETTLED ON PAPER and it is what this file
     measures. It is also exactly what sitting 7 named the debt to be.

REGISTERED PREDICTIONS, BOTH BRANCHES LONGHAND, BEFORE ANY NUMBER IS READ
=========================================================================
P-STRUCT  The lambda-cancellation above is exact, so the 11-term partial sum of
          Chat_n/(1-lam^2) must reproduce qeps_layer.Qeps(rho) to quadrature precision at
          every rho. ### BLOCKING: if it does not, the re-derivation is wrong and no verdict
          is read from anything below.

P-A  (the REGIME-FREE branch, written out) IF |Chat_n(rho)| decays geometrically in n at
     every rho tested, with the 11-term tail staying below ~1e-10 relative, THEN the series
     inherits no rho-restriction from its truncation either, Lemma F.1's constant travels,
     ### the debt clears for every banked row, and the record's dependency notes retire in
     one pass.

P-B  (the REGIME-BOUND branch, written out) IF the required term count GROWS with rho -- as
     the structure suggests it must, since Chat_n samples xi_n's transform at frequencies up
     to rho and a prolate function of index n has no small transform below its own
     bandwidth -- THEN the obstruction is NOT in the formula but in the TRUNCATION, the
     affected rows are exactly those computed at NTERM = 11 beyond the rho where 11 stops
     sufficing, ### and the honest repair is to raise NTERM per rho rather than to bound rho.
     The verdict then names rho*(11) := the largest rho at which 11 terms hold to 1e-11.

     ### P-B IS THE PREDICTION THIS FILE EXPECTS TO LAND, AND IT IS WRITTEN DOWN AS SUCH SO
     ### THAT LANDING IT COUNTS FOR LESS AND FAILING IT COUNTS FOR MORE.

P-C  Qeps(rho) is smooth across rho = 2 and rho = 3 -- no kink, no pole, no branch. A
     representation that genuinely failed past rho = 2 would almost always show it here.
     ### A NULL HERE IS WEAK EVIDENCE AND IS LABELLED WEAK: smoothness of a computed
     truncation cannot certify a series it truncates.

Usage:  python lemma52_probe.py register
        python lemma52_probe.py run
"""
import math
import sys

import numpy as np

import prolate_layer as PL
import qeps_layer as Q

RHOS = [1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 20.0]
NMAX = 48          # far beyond Lemma F.1's 11
NQ = 700
NG = 400


def registration():
    print("=" * 100)
    print("LEMMA 5.2 ON THE WIDE RANGE — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 100)
    print(__doc__)
    print("  rho ladder:", RHOS)
    print("  terms computed per rho:", NMAX, " (Lemma F.1's claim is about the first 11)")
    print("=" * 100)
    sys.stdout.flush()


def layer(nmax=NMAX, nq=NQ):
    """xi_n on the Gauss grid (P1/P2 pins) plus the LAMBDA-FREE transforms A_n, D_n."""
    x, w, mu, psi, psi1 = PL.prolate(nq)
    lam2 = mu[0::2][:nmax]
    xi = math.sqrt(2) * psi[:, 0::2][:, :nmax]
    xi1 = math.sqrt(2) * psi1[0::2][:nmax]
    s = np.sign(xi1); s[s == 0] = 1.0
    xi = xi * s[None, :]

    def A(X):
        X = np.atleast_1d(np.asarray(X, float))
        return (np.cos(2 * math.pi * np.outer(X, x)) * w) @ xi

    def D(X):
        X = np.atleast_1d(np.asarray(X, float))
        return -2 * math.pi * ((np.sin(2 * math.pi * np.outer(X, x)) * (w * x)) @ xi)

    return lam2, A, D


def chat(rho, lam2, A, D, ng=NG):
    """Chat_n(rho), lambda-free, for n = 0 .. len(lam2)-1."""
    lo, hi = 1.0 / rho, 1.0
    gx, gw = np.polynomial.legendre.leggauss(ng)
    t = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
    jac = 0.5 * (hi - lo)
    d1 = D(t)
    d2 = D(rho * t)
    integ = ((t[:, None] * d1) * (rho * t[:, None] * d2) * (gw[:, None] * jac)).sum(0)
    a1 = A(np.array([1.0]))[0]
    return (rho ** 0.5) * integ \
        + (rho ** -1.5) * D(np.array([1.0 / rho]))[0] * a1 \
        - (rho ** 1.5) * a1 * D(np.array([rho]))[0]


def run():
    lam2, A, D = layer()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")

    # ---------------------------------------------------------------- P-STRUCT, blocking
    print("=" * 100)
    print("P-STRUCT (BLOCKING) — the lambda-cancellation, against qeps_layer's own Qeps")
    print("=" * 100)
    print("  %-8s %-22s %-22s %s" % ("rho", "sum_{n<11} Chat/(1-lam2)", "qeps_layer.Qeps", "rel. diff"))
    ok = True
    for r in RHOS:
        c = chat(r, lam2, A, D)
        mine = float((c[:11] / (1 - lam2[:11])).sum())
        theirs = float(Q.Qeps(r, NQ, NG))
        rel = abs(mine - theirs) / max(abs(theirs), 1e-30)
        ok = ok and rel < 1e-9
        print("  %-8.1f %-22.12g %-22.12g %.2e %s"
              % (r, mine, theirs, rel, "" if rel < 1e-9 else "### MISMATCH"))
        sys.stdout.flush()
    print("\n  P-STRUCT: %s" % ("PASS — the re-derivation is the same object"
                                if ok else "### FAIL — nothing below is read"))
    if not ok:
        return

    # ---------------------------------------------------------------- P-A / P-B
    print("\n" + "=" * 100)
    print("P-A / P-B — TERM DECAY AND THE TRUNCATION, PER rho")
    print("=" * 100)
    print("  %-7s %-13s %-13s %-13s %-11s %-11s %s"
          % ("rho", "|term_0|", "|term_10|", "max|term_n>=11|", "tail>=11", "|Qeps|", "n for 1e-11 rel"))
    rows = []
    for r in RHOS:
        c = chat(r, lam2, A, D)
        term = c / (1 - lam2)
        total = float(term.sum())
        tail = float(np.abs(term[11:]).sum())
        # smallest N with |sum_{n<N} - total| <= 1e-11 * |total|
        need = NMAX
        for N in range(1, NMAX + 1):
            if abs(float(term[:N].sum()) - total) <= 1e-11 * max(abs(total), 1e-300):
                need = N
                break
        rows.append((r, term, total, tail, need))
        print("  %-7.1f %-13.4e %-13.4e %-13.4e %-11.3e %-11.4g %s"
              % (r, abs(term[0]), abs(term[10]), np.abs(term[11:]).max(), tail, total,
                 ("%d" % need) if need < NMAX else "### > %d" % NMAX))
        sys.stdout.flush()

    print("\n  --- per-rho term ladder, |term_n|, n = 0 .. 15 ---")
    for r, term, total, tail, need in rows:
        print("  rho=%-6.1f %s" % (r, " ".join("%8.1e" % abs(v) for v in term[:16])))

    print("\n  --- the 11-term truncation's RELATIVE error, per rho ---")
    print("  %-8s %-16s %-16s %s" % ("rho", "sum_{n<11}", "sum_{n<%d}" % NMAX, "rel. error of 11 terms"))
    worst_ok = None
    for r, term, total, tail, need in rows:
        p11 = float(term[:11].sum())
        rel = abs(p11 - total) / max(abs(total), 1e-300)
        flag = "within 1e-11" if rel <= 1e-11 else ("### %d terms needed" % need if need < NMAX
                                                   else "### >%d terms" % NMAX)
        if rel <= 1e-11:
            worst_ok = r
        print("  %-8.1f %-16.10g %-16.10g %.2e   %s" % (r, p11, total, rel, flag))
    print("\n  rho*(11) — the largest rho on this ladder at which 11 terms hold to 1e-11: %s"
          % (("%.1f" % worst_ok) if worst_ok else "### none on the ladder"))

    # ---------------------------------------------------------------- P-C
    print("\n" + "=" * 100)
    print("P-C — SMOOTHNESS OF Qeps ACROSS rho = 2 AND rho = 3 (weak evidence, labelled weak)")
    print("=" * 100)
    for centre in (2.0, 3.0, 4.0):
        h = 1e-3
        g = np.array([centre - 2 * h, centre - h, centre, centre + h, centre + 2 * h])
        v = np.array([float(Q.Qeps(float(t), NQ, NG)) for t in g])
        d1m = (v[1] - v[0]) / h
        d1p = (v[4] - v[3]) / h
        d2 = (v[3] - 2 * v[2] + v[1]) / h ** 2
        print("  rho=%.1f  Qeps=%.9g   left slope %.7g | right slope %.7g   jump %.2e   Qeps'' %.6g"
              % (centre, v[2], d1m, d1p, abs(d1p - d1m), d2))
    print("\n  A kink would show as a slope jump of the order of the slope itself.")


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
