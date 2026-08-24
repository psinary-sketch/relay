# -*- coding: utf-8 -*-
"""b128 -- G-NQ's remaining clause: THE NEW FLOOR ACROSS ALL FOUR AXES.

Run AFTER the gate failed, because component 4's re-scope filing needs the
floor. This is documenting the halt, not a second attempt: nothing is tuned,
no route is rebuilt, no threshold is touched.

THE FLOOR-AXIS LAW GOVERNS: every figure is quoted WITH ITS AXIS, and the floor
is the MAXIMUM over the four, never one axis passed off as the instrument's.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121
import b128_repair as R

CELLS = R.CELLS
UMAX = R.UMAX


def pairings(NQ=700, npts=400, n_rho=800, nmode=None):
    ug = np.linspace(0.0, UMAX, npts)
    psi, sig = B121.psi_at(NQ, ug, n_rho=n_rho) if nmode is None else _psi_trunc(NQ, ug, n_rho, nmode)
    return {a2: R.I_repaired(math.log(math.sqrt(a2)), ug, psi) for a2 in CELLS}


def _psi_trunc(NQ, ug, n_rho, nmode):
    """psi_at with the mode count truncated -- the truncation axis."""
    import b38_act10 as B38, qeps_layer as Q
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)
    nm = nmode
    tn = lam2 / (1 - lam2) * xi1 ** 2
    s = tn[:nm] / float(tn[:nm].sum())
    sig = float(s[0::2].sum())
    A = np.zeros((nm, len(ug)))
    for n in range(nm):
        f = xi[:, n]
        for i, u in enumerate(ug):
            ld = math.exp(u)
            fy = np.interp(ld * x, x, f, left=0.0, right=0.0)
            A[n, i] = math.sqrt(ld) * 0.5 * float((w * f * fy).sum())
    rr = np.exp(np.linspace(1e-4, math.log(R.__dict__.get('RHO_MAX', 48.001)), n_rho))
    ee = B38.per_mode_eps_grids(rr)
    E = np.zeros((nm, len(ug)))
    for n in range(min(nm, ee.shape[0])):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    return (A[0::2].sum(0) - sig * A.sum(0)) - (E[0::2].sum(0) - sig * E.sum(0)), sig


def spread(base, others):
    return max(max(abs(o[a2] - base[a2]) for a2 in CELLS) for o in others)


print("=" * 78)
print("b128 -- THE NEW FLOOR ACROSS ALL FOUR AXES  (floor-axis law governs)")
print("  quantity: THE PAIRINGS I(L), repaired route, nine cells")
print("  reference configuration: NQ = 700, u = 400, n_rho = 800, NMODE = 10")
print("=" * 78)
ref = pairings()

rows = []
print("\n[axis 1] THE QUADRATURE SIZE NQ  {600, 800, 900}")
v = spread(ref, [pairings(NQ=n) for n in (600, 800, 900)])
rows.append(("NQ (prolate quadrature size)", "600/800/900", v)); print("   %.6e" % v)

print("[axis 2] THE u GRID  {200, 800}")
v = spread(ref, [pairings(npts=n) for n in (200, 800)])
rows.append(("u grid", "200/800", v)); print("   %.6e" % v)

print("[axis 3] THE EPSILON GRID n_rho  {400, 1600}")
v = spread(ref, [pairings(n_rho=n) for n in (400, 1600)])
rows.append(("epsilon grid n_rho", "400/1600", v)); print("   %.6e" % v)

print("[axis 4] TRUNCATION, the mode count  {7, 9}")
v = spread(ref, [pairings(nmode=n) for n in (7, 9)])
rows.append(("truncation (mode count)", "7/9", v)); print("   %.6e" % v)

print("\n" + "-" * 78)
print("%-32s %-14s %16s" % ("AXIS", "varied over", "spread"))
for a, o, s in rows:
    print("%-32s %-14s %16.6e" % (a, o, s))
floor = max(s for _, _, s in rows)
worst = [a for a, _, s in rows if s == floor][0]
print("-" * 78)
print("### THE FLOOR IS THE MAXIMUM OVER THE FOUR AXES : %.6e" % floor)
print("### AND ITS AXIS IS NAMED : %s" % worst)
print("    smallest b119 coarse margin  = 0.064826976  -> floor/margin = %.3f"
      % (floor / 0.064826976))
print("    b117's quoted floor (u/eps only, its axes) = 2.774e-05  -> understated by %.0fx"
      % (floor / 2.774e-05))
print("    max I(L) over cells at the reference = %.9f" % max(ref.values()))
print("    ### the one-sign margin against THIS floor: %.9f"
      % (abs(max(ref.values())) - floor))
print("    strictly negative with the floor subtracted: %s"
      % (abs(max(ref.values())) - floor > 0))
