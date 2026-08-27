# -*- coding: utf-8 -*-
"""b210 -- THE INTERLEAVING CHECK. An ADDITION to the registered work, recorded as such.

   ### WHY. Component 2's read establishes that RRT's subscript is a RANK and that mu_-2 is
   ### the FIRST **EVEN** negative eigenvalue -- which FORCES rank 1 to be the first ODD one
   ### and the even sub-family to be exactly the even ranks. ### THAT LAST STEP IS AN
   ### INFERENCE FROM TWO FIGURE CAPTIONS AND Corollary 4(iv). It is cheap to measure instead.

   Corollary 4(iv), quoted: "The leading term of the asymptotic expansion of phi at +infinity
   is proportional to sin(2 pi Lambda x)/x if phi is EVEN and is proportional to
   cos(2 pi Lambda x)/x if phi is ODD."

   So the ODD family is reached by replacing the instrument's psi with the COSINE solution.
   Everything else -- y_I, x_0, the analyticity condition that defines an eigenvalue -- is
   unchanged. If the read is right, the odd eigenvalues INTERLEAVE the even ones.

   ### THIS TESTS THE READ. IT PROVES NOTHING ABOUT THE PAPER.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, mpc, sqrt, pi, exp, fabs
from b205_prolate import V_coeffs, yI_eval, integrate_in

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def psi_parity_at(mu, tau, xm, N, parity):
    """parity='even' -> asymptotic to -sin(tau x)/x   (the instrument's psi)
       parity='odd'  -> asymptotic to -cos(tau x)/x"""
    out = []
    for sgn in (-1, +1):
        V = V_coeffs(mu, tau, N, sgn)
        s = mpc(0, 1) * sgn * tau
        u = mp.zero; du = mp.zero
        for n, Vn in enumerate(V):
            u += Vn / (xm ** n)
            du += -n * Vn / (xm ** (n + 1))
        g = u / xm
        dg = du / xm - u / (xm ** 2)
        out.append((exp(s * xm) * g, exp(s * xm) * (s * g + dg)))
    (fm, dfm), (fp, dfp) = out
    if parity == 'even':
        return (fm - fp) / mpc(0, 2), (dfm - dfp) / mpc(0, 2)
    return -(fm + fp) / 2, -(dfm + dfp) / 2


def beta_parity(mu, tau, parity, dps=50, N=30, xmax=40, nsteps=250, order=18, ncoef=260):
    mp.dps = dps
    tau = mpf(tau); mu = mpf(mu)
    x0 = sqrt(mpf(2))
    p, dp = psi_parity_at(mu, tau, mpf(xmax), N, parity)
    p, dp = integrate_in(mu, tau, mpf(xmax), x0, p, dp, nsteps, order)
    v, dv = yI_eval(mu, tau, x0, ncoef)
    return ((x0 * x0 - 1) * (p * dv - dp * v)).real


AX = dict(dps=50, N=30, xmax=40, nsteps=250, order=18, ncoef=260)


def roots(tau, parity, lo, hi, step=mpf(1)):
    br = []; mu = mpf(hi); prev = None
    while mu > lo:
        b = beta_parity(mu, tau, parity, **AX)
        if prev is not None and (prev[1] > 0) != (b > 0):
            br.append((prev[0], mu))
        prev = (mu, b)
        mu -= step
    out = []
    for a, b in br:
        lo_, hi_ = min(a, b), max(a, b)
        x0_, x1_ = mpf(lo_), mpf(hi_)
        f0 = beta_parity(x0_, tau, parity, **AX)
        f1 = beta_parity(x1_, tau, parity, **AX)
        for _ in range(40):
            if f1 == f0: break
            x2 = x1_ - f1 * (x1_ - x0_) / (f1 - f0)
            if not (lo_ <= x2 <= hi_): x2 = (lo_ + hi_) / 2
            f2 = beta_parity(x2, tau, parity, **AX)
            x0_, f0, x1_, f1 = x1_, f1, x2, f2
            if fabs(x1_ - x0_) < mpf('1e-30'): break
        out.append(x1_)
    return sorted(out, reverse=True)


if __name__ == '__main__':
    mp.dps = 50
    for tau, name, lo in ((2 * pi, '2 pi', mpf(-220)), (4 * pi, '4 pi', mpf(-200))):
        ev = roots(tau, 'even', lo, mpf(-5))
        od = roots(tau, 'odd',  lo, mpf(-5))
        print("=" * 92)
        print("### tau = %s   axes: dps50 N30 x40 ns250 ord18 nc260" % name)
        print("  EVEN roots (%d): %s" % (len(ev), ', '.join(mp.nstr(m, 14) for m in ev)))
        print("  ODD  roots (%d): %s" % (len(od), ', '.join(mp.nstr(m, 14) for m in od)))
        merged = sorted([(m, 'even') for m in ev] + [(m, 'odd') for m in od], reverse=True)
        print("  MERGED, descending (rank 1 = least negative):")
        ok = True
        for i, (m, par) in enumerate(merged, 1):
            want = 'odd' if i % 2 == 1 else 'even'
            flag = '' if par == want else '   <<< NOT THE ALTERNATING PATTERN'
            if par != want: ok = False
            print("    rank %-3d %-22s %-5s%s" % (i, mp.nstr(m, 16), par, flag))
        print("  ### STRICT ODD/EVEN ALTERNATION BY RANK: %s" % ("YES" if ok else "NO"))
        print("  ### AND THE READ PREDICTS rank 2 = the FIRST EVEN. MEASURED: rank 2 is %s."
              % merged[1][1].upper())
        print()
