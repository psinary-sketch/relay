"""PROLATE LAYER — rebuilt from PRIMARY (classical) definitions, and certified.

WHY THIS FILE EXISTS. The sitting-11/12 apparatus was never banked: the twenty
sittings of 2026-08-13 produced reports and no code. This rebuilds the part of that
apparatus that CAN be rebuilt from primary definitions the executor can read --
the Slepian prolate layer -- and certifies it against the numbers the relay reports
banked. It does NOT rebuild Connes-Consani's Q_eps: see the boundary note at the foot.

THE PRIMARY DEFINITION USED (Slepian-Pollak 1961; classical, not CC-specific):

    the time-and-band limiting operator on [-1,1], with the corpus's fixed c = 2*pi,

        (Q f)(x) = \\int_{-1}^{1} sin(c (x-y)) / (pi (x-y)) f(y) dy,      c = 2 pi

    whose eigenvalues are lambda(0) > lambda(1) > ... in (0,1) and whose
    eigenfunctions are the prolate spheroidal wave functions xi_n, taken here with
    the L^2[-1,1] normalisation \\int_{-1}^{1} xi_n^2 = 1.

    c = 2*pi is the corpus's own fixed value (sitting-4 correction: "Landau-Widom
    inapplicable -- c = 2*pi is FIXED"), and it is what "concentrated in [-1,1] in
    both position and frequency" gives under the e^{2 pi i x y} Fourier convention.

METHOD. Gauss-Legendre quadrature on [-1,1] with NQ nodes; the symmetrised matrix
A = W^{1/2} K W^{1/2} has eigenvalues lambda(n) directly. Endpoint values xi_n(1) are
NOT extrapolated from the grid -- they are obtained from the eigenfunction equation
itself, xi_n(1) = (1/lambda_n) \\int K(1,y) xi_n(y) dy, which is exact up to quadrature.

Run:  python prolate_layer.py [NQ ...]
"""
import math
import numpy as np  # mpmath is used once, for Si(4pi); no scipy dependency

C = 2.0 * math.pi


def kernel(x, y):
    d = x - y
    out = np.empty_like(d)
    small = np.abs(d) < 1e-12
    out[~small] = np.sin(C * d[~small]) / (math.pi * d[~small])
    out[small] = C / math.pi
    return out


def prolate(NQ):
    x, w = np.polynomial.legendre.leggauss(NQ)
    K = kernel(x[:, None], x[None, :])
    sw = np.sqrt(w)
    A = (sw[:, None] * K) * sw[None, :]
    A = 0.5 * (A + A.T)
    vals, vecs = np.linalg.eigh(A)
    idx = np.argsort(vals)[::-1]
    lam = vals[idx]
    V = vecs[:, idx]
    # eigenfunction samples, L2[-1,1]-normalised
    xi = V / sw[:, None]
    # xi_n(1) from the eigenfunction equation, not from the grid
    k1 = kernel(np.ones(NQ), x)
    xi1 = (k1 * w) @ xi / lam
    return x, w, lam, xi, xi1


def certify(NQ):
    x, w, lam, xi, xi1 = prolate(NQ)
    out = {}
    out["NQ"] = NQ
    out["sum_lam"] = lam.sum()
    out["sum_lam2"] = (lam ** 2).sum()
    out["sum_lam2_xi1sq"] = float(((lam ** 2) * (xi1 ** 2)).sum())
    out["lam6"] = lam[:6].tolist()
    out["xi1_6"] = np.abs(xi1[:6]).tolist()
    return out


if __name__ == "__main__":
    import sys
    NQs = [int(a) for a in sys.argv[1:]] or [400, 700]

    # the banked targets, transcribed from the relay reports
    T_sum_lam2 = 2.237484834940            # sitting 9 row (i), computed
    T_sum_lam2_target = 2.237484834942     # sitting 9 row (i), target 2(Si(4pi)/4pi + 1)
    T_sum_lam2_xi1sq = 2.0                 # sitting 9 row (ii), "2 exactly"
    T_xi1 = [0.02618, 0.60948, 2.41323, 3.52614, 4.09936, 4.57184]  # sitting 9 row (v)

    # the identity target, recomputed here rather than trusted from the report
    import mpmath
    si4pi = float(mpmath.si(4 * math.pi))
    ident = 2 * (si4pi / (4 * math.pi) + 1)

    print("independent value of 2(Si(4pi)/4pi + 1) = %.12f" % ident)
    print("   report's stated target                = %.12f" % T_sum_lam2_target)
    print("   agree to                              = %.2e" % abs(ident - T_sum_lam2_target))
    print()

    for NQ in NQs:
        r = certify(NQ)
        print("=" * 74)
        print("NQ = %d" % NQ)
        print("  sum lambda(n)      = %.12f      [trace, analytic value 4]" % r["sum_lam"])
        print("  sum lambda(n)^2    = %.12f" % r["sum_lam2"])
        print("      vs banked        %.12f   delta = %.2e" % (T_sum_lam2, abs(r["sum_lam2"] - T_sum_lam2)))
        print("      vs identity      %.12f   delta = %.2e" % (ident, abs(r["sum_lam2"] - ident)))
        print("  sum lam^2 xi(1)^2  = %.12f" % r["sum_lam2_xi1sq"])
        print("      vs banked 2      %.12f   delta = %.2e" % (T_sum_lam2_xi1sq,
                                                              abs(r["sum_lam2_xi1sq"] - T_sum_lam2_xi1sq)))
        print("  first six lambda(n): " + ", ".join("%.9f" % v for v in r["lam6"]))
        print("  |xi_n(1)| computed : " + ", ".join("%.5f" % v for v in r["xi1_6"]))
        print("  |xi_n(1)| banked   : " + ", ".join("%.5f" % v for v in T_xi1))
        d = [abs(a - b) for a, b in zip(r["xi1_6"], T_xi1)]
        print("  abs deltas         : " + ", ".join("%.2e" % v for v in d))
        print("  rail |xi_n(1)| <= (2pi)^(2n+1/2): " +
              ("HOLDS" if all(v <= (2 * math.pi) ** (2 * n + 0.5)
                              for n, v in enumerate(r["xi1_6"])) else "FAILS"))

# ── BOUNDARY OF THIS FILE, STATED SO IT IS NOT MISTAKEN FOR THE WHOLE INSTRUMENT ──
#
# This rebuilds the PROLATE LAYER only. It does NOT rebuild:
#   * Connes-Consani's Q_eps (the ferry's "eq. (100)") -- the equation is not on disk
#     and was never executor-read; the corpus records the CC prolate/semilocal line as
#     NOT READ (OPEN_TRAILS: "API returned 429 ... NOT READ. Untested."), and sitting 5
#     banked its CC data as NAVIGATOR-SUPPLIED, explicitly "NOT (EXECUTOR-READ)".
#   * the Y+ map, the constrained subspace ghat(-i/2) = 0, or the lag-log2 form.
#   * therefore NOT the log-3 spectrum, the omega-triple, the three negative fractions
#     at L = 3, the five-point delta/L table, or C = 0.3448.
#
# Writing Q_eps from a remembered equation number would produce a DIFFERENT operator
# whose agreement or disagreement with the banked numbers would be uninterpretable.
# That is the false ledger sitting 12 itself refused to produce.
