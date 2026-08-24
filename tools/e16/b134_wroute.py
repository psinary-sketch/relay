# -*- coding: utf-8 -*-
"""b134 -- THE SECOND ATTEMPT: the W-diagonalization route, four gates in order.

THE ROUTE, and it is A HYBRID as the registration declared:
  xi_n  <- diagonalise W = diag(k(k+1)) + c^2 X^2 in the orthonormal Legendre
           basis, take eigenvector index 2n (pin P1: even indices only),
           normalise to INT xi^2 = 2 (pin P2: xi_n = sqrt(2) psi_{2n}).
           A POLYNOMIAL. Evaluable anywhere. No interpolation, no 1/lambda.
  lambda_n^2 <- STILL FROM Q's eigh. NO GATE HERE TESTS IT.

  A_n(u) = sqrt(L) * (1/2) INT_{-1/L}^{1/L} xi_n(x) xi_n(L x) dx,  L = e^u
           the integrand is a POLYNOMIAL on the surviving interval, so a
           Gauss-Legendre rule of order NGQ is EXACT once 2*deg < 2*NGQ-1.
           NGQ IS AN EXPLICIT AXIS, per the registration.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import prolate_layer as PL
import qeps_layer as Q

C = PL.C
NMODE = 10
UMAX = 2.0 * math.log(math.sqrt(48.001))
RHO_MAX = 48.001
KNOWN = -1.165002987


def wbasis(nleg):
    k = np.arange(nleg)
    a = (k + 1) / np.sqrt((2 * k + 1) * (2 * k + 3))
    X = np.zeros((nleg, nleg))
    for j in range(nleg - 1):
        X[j + 1, j] = a[j]; X[j, j + 1] = a[j]
    W = np.diag((k * (k + 1)).astype(float)) + (C ** 2) * (X @ X)
    chi, V = np.linalg.eigh(W)
    return chi, V[:, 0::2][:, :NMODE] * math.sqrt(2.0)   # P1 even index, P2 norm


def legvals(nleg, x):
    P = np.zeros((nleg, len(x))); P[0] = 1.0
    if nleg > 1: P[1] = x
    for k in range(1, nleg - 1):
        P[k + 1] = ((2 * k + 1) * x * P[k] - k * P[k - 1]) / (k + 1)
    for k in range(nleg):
        P[k] *= math.sqrt((2 * k + 1) / 2.0)
    return P


def A_W(ug, A_coef, nleg, ngq):
    """A_n(u) on the W route -- polynomial evaluation, exact quadrature."""
    gx, gw = np.polynomial.legendre.leggauss(ngq)
    out = np.zeros((NMODE, len(ug)))
    for i, u in enumerate(ug):
        lam = math.exp(u)
        h = min(1.0, 1.0 / lam)              # surviving interval [-h, h]
        xs = gx * h; ws = gw * h
        Px = legvals(nleg, xs)               # xi_n at x
        Py = legvals(nleg, lam * xs)         # xi_n at the DILATED point, EXACT
        f = A_coef.T @ Px
        g = A_coef.T @ Py
        out[:, i] = math.sqrt(lam) * 0.5 * ((ws * f * g).sum(axis=1))
    return out


def E_modes(ug, n_rho=800):
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    ee = B38.per_mode_eps_grids(rr)
    E = np.zeros((NMODE, len(ug)))
    for n in range(min(NMODE, ee.shape[0])):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    return E


def sigma_from_Q(NQ):
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)
    tn = lam2[:NMODE] / (1 - lam2[:NMODE]) * xi1[:NMODE] ** 2
    s = tn / float(tn.sum())
    return float(s[0::2].sum()), lam2[:NMODE]


def psi_W(ug, nleg, ngq, NQ, E=None):
    chi, Ac = wbasis(nleg)
    A = A_W(ug, Ac, nleg, ngq)
    sig, _ = sigma_from_Q(NQ)
    if E is None:
        E = E_modes(ug)
    return (A[0::2].sum(0) - sig * A.sum(0)) - (E[0::2].sum(0) - sig * E.sum(0)), A, sig


def main():
    print("=" * 78)
    print("b134 -- THE SECOND ATTEMPT: the W route, four gates")
    print("=" * 78)
    ug = np.linspace(0.0, UMAX, 400)
    E = E_modes(ug)
    NLEG, NGQ = 300, 160

    # ---------------- G-A ----------------
    print("\n--- G-A  THE KNOWN ANSWER, FIRST AND ABSOLUTE ---")
    print("%8s %20s %16s" % ("NQ", "Psi_W(0)", "dev from known"))
    worst = 0.0
    for NQ in (600, 700, 800, 900):
        p, A, sig = psi_W(ug, NLEG, NGQ, NQ, E)
        d = abs(p[0] - KNOWN); worst = max(worst, d)
        print("%8d %20.9f %16.3e" % (NQ, p[0], d))
    print("\n  A_n(0) on the W route (must be 1 for every mode, by P2):")
    _, A0, _ = psi_W(np.array([0.0]), NLEG, NGQ, 700, E_modes(np.array([0.0])))
    print("   " + " ".join("%.9f" % v for v in A0[:, 0]))
    ga = worst < 1e-9
    print("  ### worst |dev| = %.3e   (criterion < 1e-9)" % worst)
    print("### G-A : %s" % ("PASS" if ga else "FAIL -- HALT"))
    if not ga:
        print("*** STOP-LOSS: the attempt ends. Route to component 4. ***"); return

    # ---------------- G-B ----------------
    print("\n--- G-B  THE COMPLETENESS REFEREE ---")
    try:
        import mpmath
        target = 2.0 * (float(mpmath.si(4 * math.pi)) / (4 * math.pi) + 1.0)
    except Exception as e:
        target = float('nan'); print("  mpmath unavailable: %s" % e)
    print("  Selecta Remark 4.5, quoted from the layer's pins:")
    print("     delta(1) = sum lambda(n)^2 = 2(Si(4pi)/(4pi) + 1) = %.12f" % target)
    for NQ in (700, 900):
        _, l2 = sigma_from_Q(NQ)
        print("     NQ=%d : sum lambda(n)^2 = %.12f   dev %.3e"
              % (NQ, l2.sum(), abs(l2.sum() - target)))
    _, l2 = sigma_from_Q(700)
    gb = abs(l2.sum() - target) < 1e-6
    print("  ### G-B : %s" % ("PASS" if gb else "FAIL -- HALT"))
    print("  *** AND WHAT IT DOES NOT TEST, DECLARED IN THE REGISTRATION: this")
    print("  *** identity is a statement about the EIGENVALUES. It tests the W")
    print("  *** route's EIGENVECTORS NOT AT ALL. The pass is weak and is so marked.")
    if not gb:
        print("*** STOP-LOSS: the attempt ends. ***"); return

    # ---------------- G-C ----------------
    print("\n--- G-C  THE MODE-WISE VALIDITY TABLE (the gate that carries weight) ---")
    x, w, lam, lam2, xi, xi1, anq, danq = Q.layer(700)
    NRM = float((w * xi[:, 0] ** 2).sum())
    print("%5s %14s %26s %26s" % ("mode", "lambda^2", "W/Q agreement (0-6)", "W-internal flatness (7-9)"))
    rows, ok_c = [], True
    Pq = legvals(NLEG, x)
    chi, Ac = wbasis(NLEG)
    xiW_at_nodes = Ac.T @ Pq                       # W modes sampled at Q's nodes
    for n in range(NMODE):
        ov = abs(float((w * xi[:, n] * xiW_at_nodes[n]).sum()) / NRM)
        flats = []
        for nl in (100, 200, 400):
            _, Ac2 = wbasis(nl)
            m = min(nl, NLEG)
            v1 = Ac[:m, n] / np.linalg.norm(Ac[:m, n])
            v2 = Ac2[:m, n] / np.linalg.norm(Ac2[:m, n])
            flats.append(1.0 - abs(float(v1 @ v2)))
        if n <= 6:
            entry = "|<xi_Q,xi_W>| = %.9f" % ov
            good = ov > 1 - 1e-6
        else:
            entry = ""
            good = max(flats) < 1e-10
        rows.append((n, lam2[n], entry, "1-|ov| @NLEG 100/200/400: " +
                     "/".join("%.1e" % f for f in flats), good))
        ok_c = ok_c and good
    for n, l2v, e1, e2, good in rows:
        print("%5d %14.6e %26s %26s  %s" % (n, l2v, e1, "", "OK" if good else "**"))
        print("      %s" % e2)
    print("\n### G-C : %s" % ("PASS" if ok_c else "FAIL -- HALT"))
    print("  ### EVERY MODE HAS AN ENTRY. Modes 0-6 by comparison with Q where Q")
    print("  ### is trustworthy; modes 7-9 by W-INTERNAL FLATNESS, since no")
    print("  ### comparison exists. The table cannot report success on 0-6 alone.")
    if not ok_c:
        print("*** STOP-LOSS: the attempt ends. ***"); return

    # ---------------- G-D ----------------
    print("\n--- G-D  THE b121 NQ TEST, AND THE ROUTE'S OWN AXES ---")
    pref, _, _ = psi_W(ug, NLEG, NGQ, 700, E)
    exc_nq = max(float(np.abs(psi_W(ug, NLEG, NGQ, NQ, E)[0] - pref).max())
                 for NQ in (600, 800, 900))
    print("  Psi excursion over NQ in {600,800,900} : %.6e" % exc_nq)
    print("  against b121's incumbent 4.361e-01 -> collapse of %.1f orders"
          % (math.log10(4.361e-01 / max(exc_nq, 1e-300))))
    print("\n  *** AND THE PASS IS NEAR-VACUOUS, AS THE REGISTRATION DECLARED.")
    print("  *** W does not depend on NQ at all; the only residual dependence is")
    print("  *** sigma_even. This measures that the parameter was removed.")
    print("\n  ### THE ROUTE'S OWN AXES, which is where its real floor lives:")
    for nl in (200, 400):
        d = float(np.abs(psi_W(ug, nl, NGQ, 700, E)[0] - pref).max())
        print("     NLEG %3d vs %3d : %.6e" % (nl, NLEG, d))
    for ng in (80, 240):
        d = float(np.abs(psi_W(ug, NLEG, ng, 700, E)[0] - pref).max())
        print("     NGQ  %3d vs %3d : %.6e" % (ng, NGQ, d))
    axes = [float(np.abs(psi_W(ug, nl, NGQ, 700, E)[0] - pref).max()) for nl in (200, 400)] + \
           [float(np.abs(psi_W(ug, NLEG, ng, 700, E)[0] - pref).max()) for ng in (80, 240)]
    floor = max(max(axes), exc_nq)
    print("\n  ### THE ROUTE'S FLOOR = MAX OVER ALL AXES = %.6e" % floor)
    print("  ### ITS AXIS = %s" % ("NLEG or NGQ (the route's own)" if max(axes) >= exc_nq else "NQ"))
    print("### G-D : %s" % ("PASS" if floor < 4.288e-02 / 10 else "FAIL"))

    # ---------------- the incumbent comparison ----------------
    print("\n--- Psi_W AGAINST Psi_Q (expected to DIFFER off u=0; that is the repair) ---")
    import b121_instrument as B121
    pq, _ = B121.psi_at(700, ug)
    print("  |Psi_W - Psi_Q| at u=0        : %.3e   (must be ~0: the incumbent is right there)"
          % abs(pref[0] - pq[0]))
    print("  max |Psi_W - Psi_Q| over u    : %.6e" % float(np.abs(pref - pq).max()))
    print("  Psi_W(umax) = %+.9f ; Psi_Q(umax) = %+.9f" % (pref[-1], pq[-1]))
    np.save(r"D:\relay\tools\e16\b134_psiW.npy", pref)
    np.save(r"D:\relay\tools\e16\b134_ug.npy", ug)
    print("\n  (Psi_W and its u grid saved for components 2-3.)")


main()
