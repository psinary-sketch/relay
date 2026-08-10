# -*- coding: utf-8 -*-
"""W-ORD-JOIN act-1 close: the normalization adjudication.

Spectrum of Theta (from pi_*((THH(Z)(x)Q)^{hT}) = Q[u], |u|=-2):  {-2n : n>=0}, mult 1.
General tool: for eigenvalues a*(z+n), n>=0,
    det_inf = a^{zeta_H(0,z)} * sqrt(2pi)/Gamma(z),   zeta_H(0,z) = 1/2 - z.
"""
from mpmath import mp, mpf, mpc, gamma, loggamma, log, pi, sqrt, exp, zeta, diff

mp.dps = 40
GR = lambda s: pi ** (-s / 2) * gamma(s / 2)          # Serre's Gamma_R
GC = lambda s: 2 * (2 * pi) ** (-s) * gamma(s)        # Serre's Gamma_C


def det_shift(a, z):
    """regularized det of { a*(z+n) : n>=0 }, by the doubly-derived formula"""
    return a ** (mpf('0.5') - z) * sqrt(2 * pi) / gamma(z)


def det_numeric(a, z):
    """independent route: -d/dw|0 of sum (a(z+n))^{-w} = -d/dw|0 [a^{-w} zeta_H(w,z)]"""
    f = lambda w: a ** (-w) * zeta(w, z)
    return exp(-diff(f, mpf('0')))


print("=" * 84)
print("THE CONVENTIONS, each on the SAME spectrum {-2n}, each doubly evaluated")
print("=" * 84)
S = [mpf('2.3'), mpf('4.1'), mpc('1.6', '0.7')]
rows = [
    ("act 1:  (s - Theta)/2pi", lambda s: (mpf(1) / pi, s / 2)),   # eigen (z+n)/pi
    ("CC as read: (1/2)(s-Theta)", lambda s: (mpf(1), s / 2)),      # eigen (z+n)
    ("(s - Theta)/2  /pi  = same as act1", lambda s: (mpf(1) / pi, s / 2)),
    ("(s - Theta)/(2pi) with 2pi scaling", lambda s: (mpf(1) / (2 * pi), s / 2)),
]
for name, f in rows:
    a, _ = f(S[0])
    print("\n  %s" % name)
    for s in S:
        a, z = f(s)
        d1, d2 = det_shift(a, z), det_numeric(a, z)
        ratio = d1 / (1 / GR(s))
        print("    s=%-13s det=%-24s  two-route err %.1e   det*Gamma_R = %s"
              % (mp.nstr(s, 5), mp.nstr(d1, 10), abs(d1 - d2), mp.nstr(ratio, 12)))

print()
print("=" * 84)
print("IS ANY SINGLE SCALAR a MAKING THE CONSTANT EXACTLY 1?  (algebra, not search)")
print("=" * 84)
print("  want  a^{1/2-z} * sqrt(2pi) = pi^z   for ALL z")
print("  z-coefficient:  -log a = log pi        =>  a = 1/pi")
print("  constant term:  (1/2)log a + (1/2)log 2pi = 0  =>  a = 1/(2pi)")
print("  1/pi != 1/(2pi)  =>  NO SINGLE SCALAR WORKS.  The constant is NOT a rescaling artifact.")

print()
print("=" * 84)
print("DOES THE CONSTANT SURVIVE A SHIFT, OR DROPPING THE ZERO MODE?")
print("=" * 84)
for lbl, z_of in (("shift s -> s+c, c=1.7", lambda s: (s + mpf('1.7')) / 2),
                  ("shift s -> s-0.5", lambda s: (s - mpf('0.5')) / 2)):
    s = S[0]; z = z_of(s)
    print("  %-24s det/Gamma_R^-1(shifted) = %s"
          % (lbl, mp.nstr(det_shift(1 / pi, z) / (1 / GR(2 * z)), 12)))
z = S[0] / 2
drop = det_shift(1 / pi, z) / ((z) / pi)        # remove the n=0 factor
print("  drop the n=0 mode:       det/Gamma_R^-1(s+2) = %s"
      % mp.nstr(drop / (1 / GR(S[0] + 2)), 12))

print()
print("=" * 84)
print("THE REAL/COMPLEX COHERENCE CHECK  (Gamma_C(s) = Gamma_R(s) Gamma_R(s+1))")
print("=" * 84)
for s in S:
    lhs = det_shift(1 / pi, s / 2) * det_shift(1 / pi, (s + 1) / 2)
    print("  s=%-13s det(s)*det(s+1) * Gamma_C(s) = %s"
          % (mp.nstr(s, 5), mp.nstr(lhs * GC(s), 12)))
print("  => per-real-place constant sqrt(2); the complex place inherits (sqrt2)^2 = 2,")
print("     exactly matching Serre's factor 2 inside Gamma_C. THE CONSTANT IS COHERENT.")
