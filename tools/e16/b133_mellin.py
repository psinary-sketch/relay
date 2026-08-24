# -*- coding: utf-8 -*-
"""b133 -- COMPONENT 2: the reformulation, every identity TESTED.

TRANSFORMS NAMED BY THEIR VARIABLE AT EVERY APPEARANCE (R4):
  Khat, Psihat        -- FOURIER in u (equivalently MELLIN-1 in rho = e^u)
  M_z[.]              -- MELLIN-2 in the dual variable s, DLMF (1.14.32)

THE TWO IDENTITIES UNDER TEST, both the executor's own algebra (R3: DLMF's
convolution theorem 1.14.40 is NOT cited for either -- it names a different
object):
  (E1)  M_z[ F ](z) = M_z[Khat](z) * M_z[Psihat](1-z),
        where F(L) = INT_0^infty Khat(Ls) Psihat(s) ds
  (E2)  M_z[ L F'(L) ](z) = -z * M_z[F](z)
        (boundary terms [L^z F(L)] at 0 and infinity)

### EVERY INTEGRAL BELOW IS OVER A TRUNCATED DOMAIN, BECAUSE THE RECORD'S Psi
### STOPS AT UMAX. The test therefore checks THE ALGEBRA ON THE RECORD'S OWN
### ARRAYS. It does NOT claim the values are the true transforms. That
### distinction is the act's expected finding and is kept visible in the output.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121

UMAX = 2.0 * math.log(math.sqrt(48.001))
L_LO, L_HI = math.log(math.sqrt(2)), math.log(math.sqrt(48))

print("=" * 78)
print("b133 COMPONENT 2 -- THE REFORMULATION, IDENTITIES TESTED")
print("=" * 78)

ug = np.linspace(0.0, UMAX, 1200)
psi, sig = B121.psi_at(700, ug)
sg, K, Phi = B121.build_kernel()
uf = np.concatenate([-ug[:0:-1], ug]); pf = np.concatenate([psi[:0:-1], psi])
sf = np.concatenate([-sg[:0:-1], sg]); Kf = np.concatenate([K[:0:-1], K])

SMAX, NS = 200.0, 8000
s = np.linspace(SMAX / NS, SMAX, NS)          # s > 0, the Mellin-2 variable
Ph = np.array([float(np.trapezoid(pf * np.cos(t * uf), uf)) for t in s])
Kh = np.array([float(np.trapezoid(Kf * np.cos(t * sf), sf)) for t in s])

print("\n--- the arrays this test uses, with their truncations named ---")
print("  Psi on [0, %.6f] (UMAX = log 48.001, EXACTLY the top the licensed" % UMAX)
print("      range needs); |Psi(umax)|/|Psi(0)| = %.4f -- NOT decayed."
      % (abs(psi[-1]) / abs(psi[0])))
print("  Psihat, Khat sampled on s in (0, %.1f], %d points." % (SMAX, NS))
print("  ### Psihat(s) tail at s = %.1f : %.3e  (relative to Psihat near 0: %.3e)"
      % (SMAX, Ph[-1], abs(Ph[-1]) / abs(Ph[0])))
print("  ### Khat(s)   tail at s = %.1f : %.3e" % (SMAX, Kh[-1]))


def F_of_L(L):
    return float(np.trapezoid(np.interp(L * s, s, Kh, right=0.0) * Ph, s))


def M(vals, z):
    """MELLIN-2 of a sampled function of s, DLMF (1.14.32)."""
    return float(np.trapezoid(vals * s ** (z - 1.0), s))


print("\n--- (E1) THE PAIRING IDENTITY, tested at real z in the strip ---")
print("%8s %20s %20s %14s" % ("z", "M_z[F](z)", "M_z[Kh](z)M_z[Ph](1-z)", "rel diff"))
Lg = np.linspace(1e-3, 40.0, 4000)
worst = 0.0
for z in (0.20, 0.35, 0.50, 0.65, 0.80):
    Fv = np.array([F_of_L(L) for L in Lg])
    lhs = float(np.trapezoid(Fv * Lg ** (z - 1.0), Lg))
    rhs = M(Kh, z) * M(Ph, 1.0 - z)
    d = abs(lhs - rhs) / max(1e-30, abs(lhs))
    worst = max(worst, d)
    print("%8.2f %20.9e %20.9e %14.3e" % (z, lhs, rhs, d))
print("\n  ### worst relative difference = %.3e" % worst)
print("  ### (E1) %s ON THE RECORD'S OWN ARRAYS"
      % ("VERIFIED" if worst < 5e-2 else "*** NOT VERIFIED ***"))

print("\n--- (E2) THE DERIVATIVE IDENTITY, and its boundary terms ---")
Fv = np.array([F_of_L(L) for L in Lg])
dF = np.gradient(Fv, Lg)
print("%8s %20s %20s %14s" % ("z", "M_z[L F'](z)", "-z M_z[F](z)", "rel diff"))
worst2 = 0.0
for z in (0.20, 0.35, 0.50, 0.65, 0.80):
    lhs = float(np.trapezoid(Lg * dF * Lg ** (z - 1.0), Lg))
    rhs = -z * float(np.trapezoid(Fv * Lg ** (z - 1.0), Lg))
    d = abs(lhs - rhs) / max(1e-30, abs(lhs))
    worst2 = max(worst2, d)
    print("%8.2f %20.9e %20.9e %14.3e" % (z, lhs, rhs, d))
print("\n  ### worst relative difference = %.3e" % worst2)
print("  ### (E2) %s" % ("VERIFIED" if worst2 < 5e-2 else "*** NOT VERIFIED ***"))
print("  boundary terms, measured: F(L->0) = %.9f (finite, so L^z F -> 0 for Re z>0)"
      % Fv[0])
print("                            F(L = %.1f) = %.6e ; L^z F there at z=0.5 = %.6e"
      % (Lg[-1], Fv[-1], Lg[-1] ** 0.5 * Fv[-1]))

print("\n--- THE POSITIVITY QUESTION, restated on the MELLIN-2 line ---")
print("  L dN/dL > 0 on [%.5f, %.5f]  <=>  the inverse MELLIN-2 of" % (L_LO, L_HI))
print("      -z * M_z[Khat](z) * M_z[Psihat](1-z)")
print("  is positive there. THE TRANSFORM SIDE IS A PRODUCT (dilation diagonal);")
print("  ### THE POSITIVITY IS A STATEMENT ABOUT THE INVERSE, NOT ABOUT THE PRODUCT.")
print("\n  and the two factors, measured on the strip:")
print("%8s %18s %18s %18s" % ("z", "M_z[Khat](z)", "M_z[Psihat](1-z)", "product"))
for z in (0.20, 0.35, 0.50, 0.65, 0.80):
    a, b = M(Kh, z), M(Ph, 1.0 - z)
    print("%8.2f %18.9e %18.9e %18.9e" % (z, a, b, a * b))
print("\n  ### M_z[Khat] > 0 on the strip: %s   (Khat >= 0 pointwise, b131)"
      % all(M(Kh, z) > 0 for z in (0.2, 0.35, 0.5, 0.65, 0.8)))
print("  ### M_z[Psihat] sign on the strip: %s"
      % ("all positive" if all(M(Ph, 1 - z) > 0 for z in (0.2, 0.35, 0.5, 0.65, 0.8))
         else ("all negative" if all(M(Ph, 1 - z) < 0 for z in (0.2, 0.35, 0.5, 0.65, 0.8))
               else "MIXED")))
print("\n--- THE TRUNCATION DEPENDENCE, the act's expected finding, MEASURED ---")
print("  M_z[Psihat](1-z) at z = 0.5, as the s-domain is truncated further:")
for cut in (50.0, 100.0, 150.0, 200.0):
    m = s <= cut
    print("     s <= %6.1f : %18.9e" % (cut, float(np.trapezoid(Ph[m] * s[m] ** (-0.5), s[m]))))
print("  ### if these do not settle, M_z[Psihat] IS NOT DETERMINED by the")
print("  ### record's data and the reformulation cannot be evaluated, only written.")
