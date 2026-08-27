# -*- coding: utf-8 -*-
"""b212 -- COMPONENT 1: THE GATES. Each a halt. Every number carries its axes."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, pi, cos, fabs, sqrt
from b212_odd import (psi_parity_at, beta_alpha_parity, beta_parity, scan_roots, refine)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RES = [dict(dps=40, N=26, xmax=35, nsteps=180, order=16, ncoef=220),
       dict(dps=50, N=30, xmax=40, nsteps=250, order=18, ncoef=260),
       dict(dps=60, N=34, xmax=40, nsteps=400, order=20, ncoef=300)]
AX = RES[1]
PARAMS = [(2 * pi, '2 pi', mpf(-220)), (4 * pi, '4 pi', mpf(-200)), (6 * pi, '6 pi', mpf(-260))]


def ax_s(a):
    return "dps%d N%d x%d ns%d ord%d nc%d" % (a['dps'], a['N'], a['xmax'], a['nsteps'],
                                              a['order'], a['ncoef'])


print("b212 -- COMPONENT 1: THE GATES.")
print("INSTRUMENT: relay tools/e16/b205_prolate.py (banked b205, UNCHANGED, imported).")
print("### EACH GATE IS A HALT. ### NO ODD SIGN IS READ UNTIL G-PARITY PASSES AT ALL THREE.")
print()

# =====================================================================  G-PARITY
print("=" * 100)
print("### G-PARITY -- THE INTERLEAVING, REPRODUCED IN THIS ACT'S OWN RUN, AT ALL THREE PARAMETERS.")
print("### b210 MEASURED ONLY tau = 2 pi AND 4 pi, AND THAT MEASUREMENT WAS ITSELF b210's ONE")
print("### DEVIATION -- an addition to its registration. ### tau = 6 pi HAS NEVER BEEN MEASURED.")
print("=" * 100)
mp.dps = AX['dps']
gp = {}
allpass = True
for tau, name, lo in PARAMS:
    t0 = time.time()
    ev = [refine(tau, 'even', a, b, AX) for a, b in scan_roots(tau, 'even', lo, mpf(-5), mpf(1), AX)]
    od = [refine(tau, 'odd', a, b, AX) for a, b in scan_roots(tau, 'odd', lo, mpf(-5), mpf(1), AX)]
    ev.sort(reverse=True); od.sort(reverse=True)
    merged = sorted([(m, 'even') for m in ev] + [(m, 'odd') for m in od], reverse=True)
    ok = all(par == ('odd' if i % 2 == 1 else 'even') for i, (m, par) in enumerate(merged, 1))
    gp[name] = merged
    print("  tau = %-5s axes: %s   (%.0fs)" % (name, ax_s(AX), time.time() - t0))
    print("    even roots: %d   odd roots: %d   merged ranks: %d" % (len(ev), len(od), len(merged)))
    print("    rank : parity  eigenvalue")
    for i, (m, par) in enumerate(merged, 1):
        flag = '' if par == ('odd' if i % 2 == 1 else 'even') else '   <<< OUT OF PATTERN'
        print("     %-3d : %-5s  %s%s" % (i, par, mp.nstr(m, 16), flag))
    print("    ### STRICT ODD/EVEN ALTERNATION BY RANK: %s" % ("YES" if ok else "NO"))
    print("    ### RANK 2 IS %s   (RRT's caption: 'First even negative eigenvalue mu_-2')"
          % merged[1][1].upper())
    print()
    allpass = allpass and ok
print("  ### G-PARITY VERDICT: %s" % ("**PASS** at all three parameters" if allpass else "### FAIL"))
if not allpass:
    print("  ### HALT. NO ODD SIGN IS READ.")
    sys.exit(1)
print()

# =====================================================================  G-REPRO-ODD
print("=" * 100)
print("### G-REPRO-ODD -- THE COSINE SOLUTION'S ODE RESIDUAL, AND ITS NORMALIZATION AGAINST")
print("### THE ODD ASYMPTOTIC **AT GENERIC POINTS AND NOT AT ZEROS OF THE LEADING TERM**.")
print("### b205's LESSON: a ratio tested where its denominator vanishes reports the test's own")
print("### arithmetic and nothing about the object.")
print("=" * 100)
mp.dps = 60
tau = 2 * pi
mu = mpf('-20.5')
N = 34
print("  tau = 2 pi   mu = %s (a generic NON-eigenvalue: the gate tests the SOLUTION, not a root)"
      % mp.nstr(mu, 8))
print("  N = %d terms in the asymptotic series; f'' by central difference h = 1e-15 at dps 60.")
print()
print("  --- (1) ODE RESIDUAL  (x^2-1) f'' + 2x f' + (tau^2 x^2 - mu) f ,  RELATIVE ---")
h = mpf('1e-15')
for X in (25, 30, 35, 40):
    Xm = mpf(X)
    f, df = psi_parity_at(mu, tau, Xm, N, 'odd')
    fp_, _ = psi_parity_at(mu, tau, Xm + h, N, 'odd')
    fm_, _ = psi_parity_at(mu, tau, Xm - h, N, 'odd')
    d2 = (fp_ - 2 * f + fm_) / (h * h)
    res = (Xm * Xm - 1) * d2 + 2 * Xm * df + (tau * tau * Xm * Xm - mu) * f
    scale = fabs((tau * tau * Xm * Xm - mu) * f)
    print("    x = %-3d   |residual| / |(tau^2 x^2 - mu) f| = %s" % (X, mp.nstr(fabs(res) / scale, 6)))
print()
print("  --- (2) NORMALIZATION  psi_odd(x) * x / (-cos(tau x))  ->  1,  AT GENERIC POINTS ---")
print("      ### POINTS CHOSEN SO |cos(tau x)| IS NOT SMALL. |cos| PRINTED SO THE READER CAN SEE")
print("      ### THE DENOMINATOR IS NOT NEAR A ZERO.")
for X in (mpf('25.0'), mpf('30.0'), mpf('35.0'), mpf('40.0'), mpf('50.0')):
    f, _ = psi_parity_at(mu, tau, X, N, 'odd')
    c = cos(tau * X)
    ratio = (f * X / (-c)).real
    print("    x = %-6s  |cos(tau x)| = %-10s  ratio = %-22s  |ratio - 1| = %s"
          % (mp.nstr(X, 6), mp.nstr(fabs(c), 5), mp.nstr(ratio, 18), mp.nstr(fabs(ratio - 1), 6)))
print()
print("  --- (2b) THE CONTROL: THE SAME RATIO AT A NEAR-ZERO OF cos(tau x) ---")
print("      ### RUN TO SHOW THE GATE'S OWN FAILURE MODE, NOT TO PASS IT.")
xz = mpf('25.25')          # tau*x = 2pi*25.25 -> cos near zero
f, _ = psi_parity_at(mu, tau, xz, N, 'odd')
c = cos(tau * xz)
print("    x = %-6s  |cos(tau x)| = %-12s  ratio = %s"
      % (mp.nstr(xz, 6), mp.nstr(fabs(c), 5), mp.nstr((f * xz / (-c)).real, 12)))
print("      ### THIS NUMBER IS ABOUT THE DENOMINATOR AND NOT ABOUT psi_odd, WHICH IS EXACTLY")
print("      ### WHY THE GATE FORBIDS TESTING THERE.")
print()
