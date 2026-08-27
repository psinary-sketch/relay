# -*- coding: utf-8 -*-
"""b214 -- THE RUN. G-SONIN first, then G-RATIO, G-STAB, then the bits."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, mpc, pi, fabs, sqrt
from b212_odd import refine, beta_alpha_parity
from b214_transform import yI_blocks, yI_at, Fphi

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("b214 -- THE ORIENTATION BITS -- THE RAW RUN.")
print("### THE TRANSFORM CONVENTION, STATED ONCE: (F f)(y) = INT f(x) e^{+2 pi i x y} dx,")
print("### the continuum limit of b19's centered DFT. ### THE KEYSTONE'S F^2 = parity DOES NOT")
print("### PICK THE SIGN; IT IS ADOPTED HERE. ### The odd bit flips under the conjugate")
print("### convention (b203) and is printed both ways. ### The even bit is convention-free.")
print()

AXR = dict(dps=40, N=26, xmax=35, nsteps=180, order=16, ncoef=220)   # root-finding axes


def case(tau, tname, parity, lo, hi, label, settings):
    mp.dps = 50
    mu = refine(tau, parity, mpf(lo), mpf(hi), AXR)
    _, al = beta_alpha_parity(mu, tau, parity, **AXR)
    print("=" * 104)
    print("### %s   tau = %s   parity = %s" % (label, tname, parity.upper()))
    print("    mu = %s      alpha = %s" % (mp.nstr(mu, 20), mp.nstr(al, 14)))
    print("=" * 104)
    out = {}
    for si, (X, nst, order, ncoef, N, M, nsub, dps) in enumerate(settings):
        mp.dps = dps
        X = mpf(X)
        t0 = time.time()
        blocks, h = yI_blocks(mu, tau, X, nst, order, ncoef)
        ax = "dps%d X%d nsteps%d order%d ncoef%d N%d M%d nsub%d" % (dps, X, nst, order, ncoef, N, M, nsub)
        print("  --- axes: %s ---" % ax)

        if si == 0:
            print("  ### G-SONIN -- F phi(y) ON 0 <= y < 1. ### THE OBJECT'S OWN CONTROL,")
            print("  ### AND THE STRONGEST AVAILABLE: phi is in the Sonin space, so F phi MUST")
            print("  ### vanish there. Nothing in the construction forces it to.")
            scale = mp.zero
            vals = []
            for y in ('0.0', '0.15', '0.37', '0.61', '0.83', '0.97'):
                yy = mpf(y)
                F, tail, bd = Fphi(mu, tau, yy, parity, al, blocks, h, X, N, ncoef, order, M, nsub)
                vals.append((yy, F))
                print("      y = %-6s   |F phi(y)| = %s" % (y, mp.nstr(abs(F), 6)))
            print()

        print("  ### G-RATIO -- F phi(y) / phi(y) AT GENERIC y > 1.")
        print("  ### |phi(y)| PRINTED SO THE READER SEES THE DENOMINATOR IS NOT NEAR A ZERO")
        print("  ### (b205's lesson, inherited).")
        rats = []
        big = mp.zero
        for y in ('1.31', '1.73', '2.29', '2.87', '3.41', '4.13'):
            yy = mpf(y)
            F, tail, bd = Fphi(mu, tau, yy, parity, al, blocks, h, X, N, ncoef, order, M, nsub)
            ph = yI_at(mu, tau, yy, blocks, h, ncoef)
            r = F / ph
            rats.append(r)
            big = max(big, abs(F))
            print("      y = %-5s |phi| = %-14s  ratio = %-30s |ratio| = %s"
                  % (y, mp.nstr(fabs(ph), 6), mp.nstr(r, 14), mp.nstr(abs(r), 14)))
        spread = max(abs(r - rats[0]) for r in rats)
        unimod = max(abs(abs(r) - 1) for r in rats)
        print("      ### spread across y  : %s" % mp.nstr(spread, 6))
        print("      ### ||ratio| - 1| max: %s" % mp.nstr(unimod, 6))
        print("      ### tail (last y)    : %s   IBP truncation bound %s"
              % (mp.nstr(tail, 8), mp.nstr(bd, 6)))
        if si == 0 and 'vals' in dir():
            pass
        out[ax] = (rats[0], spread, unimod)
        print("      elapsed %.0fs" % (time.time() - t0))
        print()
    return mu, al, out


SET = [(40, 400, 18, 260, 30, 34, 40, 50),
       (50, 600, 20, 300, 34, 38, 48, 55)]

r = {}
r['even2pi'] = case(2 * pi, '2 pi', 'even', -21, -20, 'RANK 2 (the FIRST EVEN) -- THE BIT epsilon', SET)
r['odd2pi'] = case(2 * pi, '2 pi', 'odd', -7.5, -6.5, 'RANK 1 (the FIRST ODD) -- THE ORIENTATION BIT', SET)
r['even4pi'] = case(4 * pi, '4 pi', 'even', -40, -39, "(P4) mu_-2 AT tau = 4 pi -- THE b205 CHECK", SET[:1])
