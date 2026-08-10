# -*- coding: utf-8 -*-
"""W-ORD-JOIN act 1(c): the regularized determinant of (s - Theta)/2pi.

Theta = the weight operator of the T-action's grading on pi_*((THH(Z) (x) Q)^{hT}) = Q[u],
|u| = -2, so spec(Theta) = {0, -2, -4, ...} = {-2n : n >= 0}, multiplicity one.

Two independent derivations + numerical verification of every special value used.
"""
from mpmath import mp, mpf, mpc, zeta, gamma, loggamma, log, pi, sqrt, exp, diff

mp.dps = 40

print("=" * 78)
print("ROUTE 1 - via the Hurwitz zeta of the eigenvalue sequence")
print("=" * 78)
print("  eigenvalues of (s - Theta)/2pi : (s + 2n)/(2pi) = (s/2 + n)/pi ,  n >= 0")
print("  write z = s/2 ;  the sequence is { (z+n)/pi }")
print()
print("  log det = -d/dw|_0 [ sum_n ((z+n)/pi)^{-w} ] = -d/dw|_0 [ pi^w * zeta_H(w,z) ]")
print("          = -[ log(pi) * zeta_H(0,z) + zeta_H'(0,z) ]")
print()
print("  special values used (both verified numerically below):")
print("     zeta_H(0,z)  = 1/2 - z")
print("     zeta_H'(0,z) = log Gamma(z) - (1/2) log(2 pi)      [Lerch]")
print()
print("  => log det = -log(pi)(1/2 - z) - log Gamma(z) + (1/2) log(2 pi)")
print("            =  z log pi - log Gamma(z) + (1/2) log 2")
print("  => det     =  sqrt(2) * pi^z / Gamma(z)")
print("  with z = s/2 :  det = sqrt(2) * pi^{s/2} / Gamma(s/2)")
print("  and Gamma_R(s) = pi^{-s/2} Gamma(s/2)  =>  det = sqrt(2) * Gamma_R(s)^{-1}")

print()
print("=" * 78)
print("ROUTE 2 - via the classical regularized product, independent of route 1")
print("=" * 78)
print("  classical:  prod_{n>=0} (z+n)  =  sqrt(2 pi) / Gamma(z)")
print("  scaling  :  prod_{n>=0} c*a_n  =  c^{zeta(0)} * prod a_n , zeta(0)=zeta_H(0,z)=1/2-z")
print("  here c = 1/pi :")
print("     det = (1/pi)^{1/2 - z} * sqrt(2 pi)/Gamma(z) = pi^{z-1/2} sqrt(2 pi)/Gamma(z)")
print("     pi^{-1/2} sqrt(2 pi) = sqrt(2)   =>   det = sqrt(2) pi^z / Gamma(z)")
print("  ROUTES AGREE.")

print()
print("=" * 78)
print("NUMERICAL VERIFICATION of every special value and of the final identity")
print("=" * 78)


def zetaH(w, z):
    return zeta(w, z)


ok = True
for z in (mpf('0.7'), mpf('1.3'), mpc('1.1', '0.4'), mpf('2.5')):
    v0 = zetaH(0, z)
    want0 = mpf('0.5') - z
    d0 = diff(lambda w: zetaH(w, z), mpf('0'))
    want1 = loggamma(z) - log(2 * pi) / 2
    e0, e1 = abs(v0 - want0), abs(d0 - want1)
    ok = ok and e0 < mpf('1e-25') and e1 < mpf('1e-20')
    print("  z=%-14s zeta_H(0,z) err %.2e   zeta_H'(0,z) err %.2e" % (mp.nstr(z, 6), e0, e1))

print()
print("  final identity check:  det(s) =?= sqrt(2) * Gamma_R(s)^{-1}")
for s in (mpf('2.0'), mpf('3.5'), mpc('1.4', '0.9')):
    z = s / 2
    logdet = -(log(pi) * (mpf('0.5') - z) + (loggamma(z) - log(2 * pi) / 2))
    det = exp(logdet)
    rhs = sqrt(2) * (pi ** (s / 2)) / gamma(s / 2)
    err = abs(det - rhs)
    ok = ok and err < mpf('1e-25')
    print("  s=%-14s det=%-26s  sqrt2/Gamma_R = %-26s err %.2e"
          % (mp.nstr(s, 6), mp.nstr(det, 10), mp.nstr(rhs, 10), err))

print()
print("  THE CONSTANT, explicitly:  det_inf((s-Theta)/2pi) / Gamma_R(s)^{-1} = sqrt(2) = %s"
      % mp.nstr(sqrt(2), 20))
print("  ALL CHECKS PASS:", ok)
