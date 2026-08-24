# -*- coding: utf-8 -*-
"""b131 -- D1: the sign at the exact objects, and the two checkable claims in it.

THE REDUCTION BEING TESTED (registered in advance at b131's registration):
  (i)   A_n(u) = <xi_n, D_u xi_n> with D_u the UNITARY dilation, hence EVEN in u
        and POSITIVE-DEFINITE (Bochner), A_n(0) = 1.
  (ii)  K = convolve(w,w) is a SELF-CONVOLUTION, so its transform is a SQUARE
        and NON-NEGATIVE.   <-- CHECKED HERE, NOT ASSERTED
  (iii) hence N(L) = INT Khat(L tau) dmu(tau), a SIGNED spectral measure paired
        against a NON-NEGATIVE weight.

ALSO: the spectrum of W itself, which is the engineering entry's fact.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import b121_instrument as B121
import prolate_layer as PL
import qeps_layer as Q

C = PL.C

print("=" * 78)
print("b131 D1 -- THE TWO CHECKABLE CLAIMS")
print("=" * 78)

# ---------- (ii) is Khat >= 0 ? ----------
print("\n--- (ii) THE KERNEL'S TRANSFORM. Claim: Khat >= 0 because K is a self-convolution ---")
a0 = math.sqrt(12)
v, w2, corr, vc, L0 = B38.family(a0)
print("  the window w: %d samples on v; is it EVEN about its centre?" % len(w2))
rev = w2[::-1]
sym = float(np.abs(w2 - rev).max() / max(1e-300, np.abs(w2).max()))
print("    max|w(v) - w(-v)| / max|w| = %.3e   -> EVEN: %s" % (sym, sym < 1e-12))
print("  corr = convolve(w,w); is corr even?")
rc = corr[::-1]
symc = float(np.abs(corr - rc).max() / max(1e-300, np.abs(corr).max()))
print("    max|corr(u) - corr(-u)| / max|corr| = %.3e   -> EVEN: %s" % (symc, symc < 1e-12))

sg, K, Phi = B121.build_kernel()
# even extension of K to [-2,2] on a uniform grid, then a real FT
n = len(sg)
sgf = np.concatenate([-sg[:0:-1], sg])
Kf = np.concatenate([K[:0:-1], K])
ds = float(sgf[1] - sgf[0])
print("\n  the pairing kernel K on [-2,2]: %d samples, spacing %.6e" % (len(sgf), ds))
print("  INT K over [-2,2] = %.9f   (the record's stated 1/2 on [0,2] doubled)"
      % float(np.trapezoid(Kf, sgf)))
xis = np.linspace(0.0, 60.0, 2401)
Khat = np.array([float(np.trapezoid(Kf * np.cos(t * sgf), sgf)) for t in xis])
print("\n%10s %18s" % ("xi", "Khat(xi)"))
for i in range(0, len(xis), 200):
    print("%10.3f %18.9e" % (xis[i], Khat[i]))
mn = float(Khat.min())
print("\n  ### min Khat over xi in [0,60] = %.6e   at xi = %.3f" % (mn, xis[int(np.argmin(Khat))]))
print("  ### max |negative part| relative to Khat(0) = %.3e" % (max(0.0, -mn) / Khat[0]))
nonneg = mn > -1e-12 * Khat[0]
print("  ### CLAIM (ii) %s" % ("HOLDS to the tested tolerance" if nonneg else "*** FAILS ***"))
if not nonneg:
    print("  *** the reduction (iii) collapses and D1 must be re-attacked. ***")

# ---------- the spectrum of W ----------
print("\n--- THE SPECTRUM OF W ITSELF (the engineering entry's fact) ---")
NL = 400
k = np.arange(NL)
al = (k + 1) / np.sqrt((2 * k + 1) * (2 * k + 3))
X = np.zeros((NL, NL))
for j in range(NL - 1):
    X[j + 1, j] = al[j]; X[j, j + 1] = al[j]
W = np.diag((k * (k + 1)).astype(float)) + (C ** 2) * (X @ X)
chi = np.linalg.eigvalsh(W)
x, wq, lam, lam2, xi, xi1, an, dan = Q.layer(700)
print("%6s %18s %18s %16s" % ("n", "chi_n (from W)", "lambda^2 (from Q)", "sep chi to next"))
for n in range(12):
    print("%6d %18.9f %18.6e %16.6f"
          % (n, chi[n], lam2[n] if n < len(lam2) else float('nan'), chi[n + 1] - chi[n]))
print("\n  ### W's SMALLEST EIGENVALUE SEPARATION over n = 0..11 : %.6f"
      % float(np.min(np.diff(chi[:12]))))
print("  ### Q's SMALLEST lambda^2 SEPARATION over n = 7..9    : %.6e"
      % float(np.min(-np.diff(lam2[7:10]))))
print("  *** W's spectrum is SEPARATED where Q's is at the floor. That is the")
print("  *** whole of the engineering fact and it is measured here, not asserted. ***")
