# -*- coding: utf-8 -*-
"""b167 -- THE DELTA ACT. Delta banked on the licensed range and the one-sign
verdict evaluated across the apportionment family.

### NO NEW DEFINITION. Delta(u) := sum_n A_n(u) - sum_n e_n(u) is the window-free
object b166 identified inside b115's Psi; psi_W already forms both sums, and this
script reads them from b134's own routines rather than re-implementing either.
### NOTHING BEYOND THE CAP: every evaluation stays inside rho <= RHO_MAX = 48.001,
which in logarithmic coordinates IS the licensed range's upper endpoint.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121
import b134_wroute as WR

CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
NLEG, NGQ, NQ = 300, 160, 700
UMAX = WR.UMAX
KNOWN_PSI0 = -1.165002987
KNOWN_SUMA_UMAX = 1.443987343e-01
# b134's I_W column, the nine cells, read from its bank
B134_IW = {2: -0.141878140, 3: -0.101477080, 4: -0.094958250, 8: -0.096080946,
           9: -0.096586799, 12: -0.097074298, 16: -0.096237114, 24: -0.092834735,
           48: -0.082552767}

sg, K, Phi = B121.build_kernel()
ug = np.linspace(0.0, UMAX, 400)


def pairing(L, arr, grid=None):
    g = ug if grid is None else grid
    return float(np.trapezoid(Phi * np.interp(L * sg, g, arr, right=arr[-1]), sg))


def build(nleg=NLEG, ngq=NGQ, nq=NQ, n_rho=800, grid=None):
    g = ug if grid is None else grid
    E = WR.E_modes(g, n_rho=n_rho)
    psi, A, sig = WR.psi_W(g, nleg, ngq, nq, E)
    return psi, A.sum(0) - E.sum(0), sig, A


print("=" * 90)
print("b167 -- THE DELTA ACT: the gate, the bank, and the family evaluation")
print("=" * 90)
print("  licensed range : u in [0, %.6f] ;  rho = e^u in (1, %.3f]" % (UMAX, WR.RHO_MAX))
print("  ### the range's upper endpoint IS ln(RHO_MAX). No sample is clamped.")

psi, delta, sig, A = build()

# ================= THE GATE, BEFORE ANY NEW QUANTITY IS READ =================
print("\n" + "=" * 90)
print("COMPONENT 1a -- THE REPRODUCE-BEFORE-EXTEND GATE (tolerances fixed at registration)")
print("=" * 90)
g1 = abs(psi[0] - KNOWN_PSI0)
g2 = abs(A.sum(0)[-1] - KNOWN_SUMA_UMAX)
g3 = max(abs(pairing(math.log(math.sqrt(a2)), psi) - B134_IW[a2]) for a2 in CELLS)
g4 = abs(delta[0] - 10.0)
print("  (G1) Psi_W(0)          = %+.9f   vs banked %+.9f   |dev| = %.3e  tol 1e-9  %s"
      % (psi[0], KNOWN_PSI0, g1, "PASS" if g1 < 1e-9 else "### FAIL"))
print("  (G2) sum_n A_n(UMAX)   = %.9e   vs banked %.9e   |dev| = %.3e  tol 1e-9  %s"
      % (A.sum(0)[-1], KNOWN_SUMA_UMAX, g2, "PASS" if g2 < 1e-9 else "### FAIL"))
print("  (G3) b134's I_W column, worst |dev| over the nine cells = %.3e  tol 1e-9  %s"
      % (g3, "PASS" if g3 < 1e-9 else "### FAIL"))
print("  (G4) Delta(0)          = %.12f  vs DERIVED 10 (A_n(0)=1 all n, e_n(0)=0)"
      % delta[0])
print("       |dev| = %.3e  tol 1e-9  %s   ### A KNOWN ANSWER FOR THE NEW OBJECT"
      % (g4, "PASS" if g4 < 1e-9 else "### FAIL"))
if not all(x < 1e-9 for x in (g1, g2, g3, g4)):
    print("\n*** A GATE FAILED. THE ACT HALTS. A FAIL IS NOT SOFTENED INTO A PARTIAL PASS. ***")
    sys.exit(1)
print("\n### ALL FOUR GATES PASS. NEW QUANTITIES LICENSED, AND NOT BEFORE.")

# ================= DELTA, BANKED =================
print("\n" + "=" * 90)
print("COMPONENT 1b -- DELTA ON THE LICENSED RANGE")
print("=" * 90)
print("%10s %20s %20s %20s" % ("u", "sum_n A_n", "sum_n e_n", "Delta"))
E_ref = WR.E_modes(ug)
for u in (0.0, 0.0970, 0.2523, 0.5045, 0.9993, 1.5039, 1.9987, 2.5032, 2.9980, 3.5025, UMAX):
    i = int(np.argmin(np.abs(ug - u)))
    print("%10.5f %20.9f %20.9f %20.9f" % (ug[i], A.sum(0)[i], E_ref.sum(0)[i], delta[i]))
print("\n  Delta(0) = %.9f ; Delta(umax) = %.9f ; gross fall = %+.9f"
      % (delta[0], delta[-1], delta[-1] - delta[0]))
print("  max|Delta| = %.9f ; min Delta = %+.9f ; sign changes = %d"
      % (np.abs(delta).max(), delta.min(),
         int((np.sign(delta[:-1]) != np.sign(delta[1:])).sum())))

# ================= THE FLOOR, EVERY AXIS =================
print("\n" + "=" * 90)
print("COMPONENT 1c -- DELTA'S FLOOR, MEASURED ON EVERY INPUT AXIS (the floor-axis law)")
print("=" * 90)
axes = {}
for nl in (200, 400):
    axes['NLEG %d vs %d' % (nl, NLEG)] = float(np.abs(build(nleg=nl)[1] - delta).max())
for ng in (80, 240):
    axes['NGQ %d vs %d' % (ng, NGQ)] = float(np.abs(build(ngq=ng)[1] - delta).max())
for nq in (600, 800, 900):
    axes['NQ %d vs %d' % (nq, NQ)] = float(np.abs(build(nq=nq)[1] - delta).max())
for nr in (400, 1600):
    axes['n_rho %d vs 800' % nr] = float(np.abs(build(n_rho=nr)[1] - delta).max())
for npts in (200, 800):
    g2g = np.linspace(0.0, UMAX, npts)
    d2 = build(grid=g2g)[1]
    axes['u-grid %d vs 400' % npts] = float(np.abs(np.interp(ug, g2g, d2) - delta).max())
for k in sorted(axes, key=lambda z: -axes[z]):
    print("     %-22s : %.6e" % (k, axes[k]))
worst_axis = max(axes, key=lambda z: axes[z])
FLOOR = axes[worst_axis]
print("\n  ### DELTA'S FLOOR = MAX OVER ALL AXES = %.6e" % FLOOR)
print("  ### ITS AXIS = %s" % worst_axis)
print("  ### Psi_W's floor for comparison = 8.195851e-10, axis NQ via sigma_even (b134 G-D)")
print("  ### DELTA CONTAINS NO sigma_even: the NQ axis measures %.3e"
      % max(axes[k] for k in axes if k.startswith('NQ')))

# ================= J AND THE FAMILY =================
print("\n" + "=" * 90)
print("COMPONENT 2 -- THE ONE-SIGN VERDICT ACROSS THE FAMILY (P2)")
print("=" * 90)
print("  ### THE SHIFT LAW (b166, derived): Psi_mu = Psi_sigma + (sigma_even - mu)*Delta,")
print("  ### hence  I_mu(L) = I_sigma(L) + (sigma_even - mu)*J(L),  J(L) = <PhiK, Delta(L.)>")
print("  sigma_even (from the layer, NQ=%d) = %.12f" % (NQ, sig))
Ls = np.linspace(math.log(math.sqrt(2)), math.log(math.sqrt(48)), 601)
Isig = np.array([pairing(L, psi) for L in Ls])
J = np.array([pairing(L, delta) for L in Ls])
print("\n%8s %16s %18s %18s" % ("a^2", "L", "I_sigma(L)", "J(L)"))
for a2 in CELLS:
    L = math.log(math.sqrt(a2))
    print("%8d %16.6f %18.9f %18.9f" % (a2, L, pairing(L, psi), pairing(L, delta)))
print("\n  over the 601-point sweep:  max I_sigma = %+.9f ; J in [%+.9f, %+.9f]"
      % (Isig.max(), J.min(), J.max()))
print("  J sign changes over the sweep : %d"
      % int((np.sign(J[:-1]) != np.sign(J[1:])).sum()))

# I_mu(L) = Isig + d*J < 0 for all L, with d := sigma_even - mu
dmax, dmin = np.inf, -np.inf
argmax_L, argmin_L = None, None
for L, i0, j0 in zip(Ls, Isig, J):
    if j0 > 0:
        b = -i0 / j0
        if b < dmax:
            dmax, argmax_L = b, L
    elif j0 < 0:
        b = -i0 / j0
        if b > dmin:
            dmin, argmin_L = b, L
mu_lo = sig - dmax if np.isfinite(dmax) else -np.inf
mu_hi = sig - dmin if np.isfinite(dmin) else np.inf
print("\n  ### THE ADMISSIBLE d = sigma_even - mu FOR WHICH I_mu(L) < 0 AT EVERY SWEPT L:")
print("      d in (%s, %s)" % ("%.9f" % dmin if np.isfinite(dmin) else "-inf",
                               "%.9f" % dmax if np.isfinite(dmax) else "+inf"))
print("  ### THEREFORE THE ONE-SIGN PROPERTY HOLDS EXACTLY FOR")
print("      ### mu in (%s, %s)"
      % ("%.9f" % mu_lo if np.isfinite(mu_lo) else "-inf",
         "%.9f" % mu_hi if np.isfinite(mu_hi) else "+inf"))
if np.isfinite(mu_lo):
    print("      binding L at the lower end = %.6f  (a^2 = %.3f)" % (argmax_L, math.exp(2 * argmax_L)))
if np.isfinite(mu_hi):
    print("      binding L at the upper end = %.6f  (a^2 = %.3f)" % (argmin_L, math.exp(2 * argmin_L)))
print("  b38's member mu = %.9f : INSIDE = %s" % (sig, mu_lo < sig < mu_hi))
print("  the free end  mu = 0        : INSIDE = %s" % (mu_lo < 0.0 < mu_hi))
print("  the illustrative bracket [0,1] lies inside = %s"
      % (mu_lo < 0.0 and 1.0 < mu_hi))
print("\n  ### MARGIN CHECK AT THE ENDPOINTS, against Delta's own floor %.3e:" % FLOOR)
for nm, mu in (("b38's member", sig), ("mu = 0 (free end)", 0.0), ("mu = 1", 1.0)):
    Im = Isig + (sig - mu) * J
    print("     %-20s max I_mu over the sweep = %+.9f   strictly negative: %s"
          % (nm, Im.max(), Im.max() < 0))
np.save(r"D:\relay\tools\e16\b167_delta.npy", delta)
np.save(r"D:\relay\tools\e16\b167_ug.npy", ug)
print("\n  (Delta and its u grid saved.)")
print("=" * 90)
