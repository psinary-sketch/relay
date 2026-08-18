"""B10 — THE ABSORPTION PROOF'S LEMMA CERTIFICATES + THE ORBIT-QUOTIENT CELL.

Relay-only. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.
POSITIVITY GUARD: whatever any quantity's sign on the model, it bears not at all on h2.

ITEM 1 — THE PROOF'S THREE LEMMAS, CERTIFIED (the proof itself is longhand in the spec)
=======================================================================================
The constraint space decomposes: R_E = ball-supported functions; R_F = {f : f-hat supported
on the ball} = the p^n-PERIODIC functions (longhand: f-hat on B <=> invariance under
translation by p^n). The projections are Pi_E = mult by 1_B and Pi_F = the conditional
expectation over p^n-translates. LEMMAS:
    L-A  [Pi_E, Pi_F] = 0 and Pi_E Pi_F = Pi_Z (the orthoprojection onto span{1_B}),
         hence Pi_R = Pi_E + Pi_F - Pi_Z exactly.
    L-B  Tr(U^k Pi_E) = p^{-k/2}   (only fixed point m = 0, inside the ball)
    L-C  Tr(U^k Pi_F) = p^{-k/2}   (the (m, m') count: coprimality forces m' in B)
    L-D  Tr(U^k Pi_Z) = p^{-k/2}   (B is U-invariant and closed: <1_B, U^k 1_B> = p^{n-k/2})
    =>   Tr(U^k Pi_R) = p^{-k/2} = Tr(U^k), so t_k = 0.   [PROVED longhand; certified here]

ITEM 2 — THE ORBIT-QUOTIENT CELL (definition written BEFORE any run)
====================================================================
THE OBJECT: V_inv = { f supported off the ball : f(m') = f(m) whenever m' = p m mod N and
both m, m' off-ball } -- the model realization of functions on the orbit space x ~ px of
the non-ball part (the quotient K_p^x / p^Z at model level). S_quot = orthoprojection onto
V_inv. THE SONIN-TYPE CONDITION TRANSPOSED: support off the ball (the ball-avoidance half).
THE FOURIER HALF DOES NOT DESCEND -- the transform does not commute with x ~ px -- and this
is REGISTERED AS INFORMATIVE, not hidden: the quotient keeps the sandwich shape available
while leaving the Fourier-side Sonin condition behind, exactly as B9's tension predicted a
weight-carrying trace must change the space.
THE QUANTITIES: T_quot(k) = |Tr(U^k S_quot)| and the diagonal/norm channels, k = 1..2n-1.

REGISTERED VERDICT MAP:
    Q1  T_quot(k) NONZERO with Weil-shaped scaling (amplitude ~ q^{-1/2}-type): the
        fixed-point trace now sits at a closed orbit and is NOT absorbed -- column (beta)
        has a trace-shaped candidate at last; POSITIVITY UNKNOWN AND SAID SO.
    Q2  it vanishes again: the leak is deeper than the quotient -- BUT the KNOWN MODEL
        LIMITATION is registered beside it: the truncated U is not invertible, so true
        recurrence exists only on the infinite object; a zero at all n that does NOT
        soften as n grows names the leak "the quotient"; a zero that softens names it
        "the truncation". The discriminator is the n-trend, registered now.
    Q3  third shape, filed openly.

THE LEFSCHETZ WONDER (question grade, registered beside): IF Q1, the quotient trace's
shape (weighted count over closed orbits by period, weight ~ p^{-k/2}, unit log p the
period) is compared LONGHAND AT CITE against (a) the explicit formula's prime-side term
and (b) the banked seat claims (Deninger "periodic orbits related to closed points", at
abstract; CC's arrest sentence "understand the equality as a Lefschetz formula",
ATTRIBUTED). MATCH-IN-SHAPE / NOT; no promotion either way.

Usage:  python b10_cells.py register | run
"""
import sys
import numpy as np

import b8_sonin_dim as B8

CELLS = [(2, 2), (2, 3), (3, 2), (3, 3), (5, 2), (2, 4)]   # (2,4): N=256, the n-trend cell


def projections(p, n):
    N, F, ball = B8.model(p, n)
    PiE = np.diag(ball.astype(float))
    # Pi_F: conditional expectation over translation by p^n
    PiF = np.zeros((N, N))
    step = p ** n
    for m in range(N):
        for t in range(p ** n):
            PiF[m, (m + t * step) % N] = 1.0 / (p ** n)
    onevec = ball.astype(float); onevec /= np.linalg.norm(onevec)
    PiZ = np.outer(onevec, onevec)
    return N, F, ball, PiE, PiF, PiZ


def item1():
    print("--- ITEM 1: LEMMA CERTIFICATES ---")
    print("  %-4s %-4s %-11s %-11s %-34s" % ("p", "n", "[PiE,PiF]", "PiEPiF-PiZ", "|Tr(U^k Pi_X) - p^{-k/2}| max over k, X in {E,F,Z,R}"))
    for p, n in CELLS:
        N, F, ball, PiE, PiF, PiZ = projections(p, n)
        U = B8.scaling_matrix(p, n)
        cA1 = np.linalg.norm(PiE @ PiF - PiF @ PiE)
        cA2 = np.linalg.norm(PiE @ PiF - PiZ)
        PiR = PiE + PiF - PiZ
        errs = []
        Uk = np.eye(N)
        for k in range(1, 2 * n):
            Uk = U @ Uk
            tgt = p ** (-k / 2.0)
            for X in (PiE, PiF, PiZ, PiR):
                errs.append(abs(complex(np.trace(Uk @ X)) - tgt))
        print("  %-4d %-4d %-11.2e %-11.2e %-34.2e" % (p, n, cA1, cA2, max(errs)))
        sys.stdout.flush()


def quotient_basis(p, n):
    """orthonormal basis of V_inv: off-ball functions invariant under m -> pm (both off-ball)."""
    N, F, ball = B8.model(p, n)
    offb = ~ball
    # union-find over the relation m ~ pm when both off-ball
    parent = list(range(N))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[ra] = rb
    for m in range(N):
        if offb[m]:
            m2 = (p * m) % N
            if offb[m2]:
                union(m, m2)
    classes = {}
    for m in range(N):
        if offb[m]:
            classes.setdefault(find(m), []).append(m)
    K = np.zeros((N, len(classes)))
    for j, mem in enumerate(classes.values()):
        for m in mem:
            K[m, j] = 1.0
        K[:, j] /= np.linalg.norm(K[:, j])
    return N, K, len(classes)


def item2():
    print("\n--- ITEM 2: THE ORBIT-QUOTIENT CELL ---")
    print("  %-4s %-4s %-8s %-8s %-30s %-30s" % ("p", "n", "N", "dimVinv", "T_quot(k)=|Tr(U^k Squot)|", "norm ||Squot U^k Squot||_F"))
    for p, n in CELLS:
        N, K, d = quotient_basis(p, n)
        U = B8.scaling_matrix(p, n)
        S = K @ K.T
        ts, ns_ = [], []
        Uk = np.eye(N)
        for k in range(1, 2 * n):
            Uk = U @ Uk
            ts.append(abs(complex(np.trace(Uk @ S))))
            ns_.append(float(np.linalg.norm(S @ Uk @ S)))
        print("  %-4d %-4d %-8d %-8d %-30s %-30s"
              % (p, n, N, d, " ".join("%.5f" % x for x in ts), " ".join("%.5f" % x for x in ns_)))
        sys.stdout.flush()


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("B10 — REGISTRATION. NO MEASURED NUMBER."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    item1()
    item2()


if __name__ == "__main__":
    main()
