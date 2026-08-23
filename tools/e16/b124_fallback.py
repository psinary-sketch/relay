# -*- coding: utf-8 -*-
"""b124 -- THE FALLBACK ROUTE: spectral (Legendre) reconstruction.

WHY THE PRIMARY FAILED, measured: the Nystrom extension divides by lam_n, and
its relative node error tracks machine-epsilon / lam -- 1.5e-14 at lam^2 ~ 1,
6.1e-08 at 5.8e-09, 3.3e-04 at 2.1e-12, and ~1.0 (total loss) at the four modes
whose lam^2 sits at 1e-16. Exact in theory; unusable at the null-adjacent modes.

WHY THE FALLBACK IS THE RIGHT ROUTE, and it turns on a reading of the ORIGINAL
code: A_n(u) uses np.interp(..., left=0.0, right=0.0). The modes are therefore
NEVER EXTRAPOLATED -- they are evaluated at those dilated abscissae that fall
INSIDE [-1,1] and taken as zero outside. So the repair needs accuracy INSIDE the
interval only, which is exactly where a Legendre series is excellent and where
no division by lam appears.

  c_k = (2k+1)/2 * SUM_j w_j xi(x_j) P_k(x_j)        [exact by Gauss quadrature]
  xi(z) = SUM_k c_k P_k(z)   for |z| <= 1 ; 0 otherwise
"""
import math, sys, functools
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q
import prolate_layer as PL

UMAX = 2.0 * math.log(math.sqrt(48.001))
RHO_MAX = 48.001
NMODE = B38.TRIPLE[1][1]
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
NDEG = 400          # Legendre degree; fixed here, reported


def layer_raw(NQ):
    x, w, mu, psi, psi1 = PL.prolate(NQ)
    lam2 = mu[0::2][:Q.NTERM]
    xi = math.sqrt(2) * psi[:, 0::2][:, :Q.NTERM]
    xi1 = math.sqrt(2) * psi1[0::2][:Q.NTERM]
    s = np.sign(xi1); s[s == 0] = 1.0
    return x, w, lam2, xi * s[None, :]


def legendre_coeffs(x, w, xi, ndeg=NDEG):
    """c[k,n] = (2k+1)/2 * sum_j w_j xi_n(x_j) P_k(x_j). No division by lam."""
    P = np.polynomial.legendre.legvander(x, ndeg)          # (NQ, ndeg+1)
    k = np.arange(ndeg + 1)
    return ((P * w[:, None]).T @ xi) * ((2 * k + 1) / 2.0)[:, None]


def eval_spectral(z, c):
    """xi_n(z) inside [-1,1]; ZERO outside, matching the original semantic."""
    z = np.asarray(z, float)
    inside = np.abs(z) <= 1.0
    out = np.zeros((len(z), c.shape[1]))
    if inside.any():
        P = np.polynomial.legendre.legvander(z[inside], c.shape[0] - 1)
        out[inside] = P @ c
    return out


def A_modes(ug, x, w, c):
    nm = c.shape[1]
    out = np.zeros((nm, len(ug)))
    xi_nodes = eval_spectral(x, c)
    for i, u in enumerate(ug):
        ld = math.exp(u)
        fy = eval_spectral(ld * x, c)
        out[:, i] = math.sqrt(ld) * 0.5 * ((w[:, None] * xi_nodes * fy).sum(0))
    return out


def psi_spec(ug, NQ=700, n_rho=800, nmode=None, ndeg=NDEG):
    x, w, lam2, xi = layer_raw(NQ)
    nm = nmode or min(NMODE, xi.shape[1])
    c = legendre_coeffs(x, w, xi[:, :nm], ndeg)
    A = A_modes(ug, x, w, c)
    xq, wq, lq, l2q, xiq, xi1q, anq, danq = Q.layer(700)
    tn = l2q / (1 - l2q) * xi1q ** 2
    s = tn[:nm] / float(tn[:nm].sum()); sig = float(s[0::2].sum())
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    ee = B38.per_mode_eps_grids(rr)
    E = np.zeros((nm, len(ug)))
    for n in range(min(nm, ee.shape[0])):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    return (A[0::2].sum(0) - sig * A.sum(0)) - (E[0::2].sum(0) - sig * E.sum(0))


def main():
    print("=" * 78)
    print("b124 -- THE FALLBACK: spectral (Legendre) reconstruction, degree %d" % NDEG)
    print("=" * 78)

    x, w, lam2, xi = layer_raw(700)
    c = legendre_coeffs(x, w, xi)
    back = eval_spectral(x, c)
    print("\n--- EXACTNESS AT THE NODES (the warrant) ---")
    print("  max |spectral(x_i) - xi_n(x_i)| = %.3e" % float(np.abs(back - xi).max()))
    print("  per mode:")
    for n in range(11):
        print("    n=%2d  lam2=%.3e  max|err|=%.3e"
              % (n, lam2[n], float(np.abs(back[:, n] - xi[:, n]).max())))
    print("  (Nystrom on the same test: 3.631e+02, its error tracking eps/lam)")

    ug = np.linspace(0.0, UMAX, 160)
    print("\n--- G2: THE NQ-VARIATION TEST ON SPECTRALLY-REPAIRED SAMPLES ---")
    ref = psi_spec(ug, 700)
    worst = 0.0
    for NQ in (600, 800, 900, 1100):
        d = float(np.abs(psi_spec(ug, NQ) - ref).max())
        worst = max(worst, d)
        print("  NQ = %4d   max|dPsi| vs NQ=700 : %.3e" % (NQ, d))
    print("  ### NQ EXCURSION, SPECTRAL : %.3e   (broken: 4.361e-01)" % worst)
    if worst > 0:
        print("      collapse: %.1f x  (%.2f orders)"
              % (4.361e-01 / worst, math.log10(4.361e-01 / worst)))
    print("\n  G2 %s" % ("PASSES" if worst < 4.361e-03 else "*** FAILS ***"))
    np.save(r'D:\relay\tools\e16\_b124_psi_ref.npy', ref)
    np.save(r'D:\relay\tools\e16\_b124_ug.npy', ug)
    print("\n  Psi(0)=%+.9f  Psi(umax)=%+.9f  rise=%+.9f"
          % (ref[0], ref[-1], ref[-1] - ref[0]))


main()
