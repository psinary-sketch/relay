# -*- coding: utf-8 -*-
"""b168 -- THE LEFT-ENDPOINT REPAIR: three gates, then Delta, then the family.

### ONE RUN DOES EVERYTHING, because importing the incumbent instruments re-runs
their own mains and that cost is paid once.
### NOTHING BEYOND THE CAP: UMAX = ln(RHO_MAX) is unchanged.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121
import b134_wroute as WR
import b168_epsgrid as EG

CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
NLEG, NGQ, NQ = 300, 160, 700
UMAX = WR.UMAX
BANKED_PSI0 = -1.165002987
BANKED_SUMA = 1.443987343e-01
B134_IW = {2: -0.141878140, 3: -0.101477080, 4: -0.094958250, 8: -0.096080946,
           9: -0.096586799, 12: -0.097074298, 16: -0.096237114, 24: -0.092834735,
           48: -0.082552767}
# b155/b110 banked, for the post-derivation check
DEV12, RATIO12, B155_DMU = -0.007261299, 1.6461, 0.004435

sg, K, Phi = B121.build_kernel()
ug = np.linspace(0.0, UMAX, 400)


def pairing(L, arr, grid=None):
    g = ug if grid is None else grid
    return float(np.trapezoid(Phi * np.interp(L * sg, g, arr, right=arr[-1]), sg))


def build(nleg=NLEG, ngq=NGQ, nq=NQ, n_rho=800, grid=None, repaired=True):
    g = ug if grid is None else grid
    E = EG.E_modes(g, n_rho=n_rho, repaired=repaired)
    psi, A, sig = WR.psi_W(g, nleg, ngq, nq, E)
    return psi, A.sum(0) - E.sum(0), sig, A, E


print("=" * 92)
print("b168 -- THE LEFT-ENDPOINT REPAIR")
print("=" * 92)

# ===================== G-L =====================
print("\n--- G-L  THE REPAIRED GRID EVALUATES AT rho = 1, NO CLAMP, NO EXTRAPOLATION ---")
rr_i, rr_r = EG.incumbent_grid(), EG.repaired_grid()
ee_r = EG.eps_on(rr_r)
print("  incumbent first node : %.10f   ### the defect" % rr_i[0])
print("  repaired  first node : %.10f" % rr_r[0])
print("  sum_n e_n at the repaired first node : %.17g" % float(ee_r[:EG.NMODE, 0].sum()))
print("  ### the value came FROM THE ROUTINE's own empty-range branch, not by hand.")
gl = (rr_r[0] == 1.0) and (float(ee_r[:EG.NMODE, 0].sum()) == 0.0)
print("  node is exactly 1.0 : %s ; sum is exactly 0.0 : %s"
      % (rr_r[0] == 1.0, float(ee_r[:EG.NMODE, 0].sum()) == 0.0))
print("### G-L : %s" % ("PASS" if gl else "FAIL -- HALT"))
if not gl:
    sys.exit(1)

psi_r, delta_r, sig, A_r, E_r = build(repaired=True)
psi_i, delta_i, _, A_i, E_i = build(repaired=False)

# ===================== G-K =====================
print("\n--- G-K  Delta(0) = 10, THE DERIVED KNOWN ANSWER (the gate that fired at b167) ---")
gk = abs(delta_r[0] - 10.0)
print("  incumbent Delta(0) = %.12f   |dev| = %.3e   ### b167's failure, reproduced"
      % (delta_i[0], abs(delta_i[0] - 10.0)))
print("  repaired  Delta(0) = %.12f   |dev| = %.3e   tol 1e-9" % (delta_r[0], gk))
print("### G-K : %s" % ("PASS" if gk < 1e-9 else "FAIL -- HALT"))
if gk >= 1e-9:
    sys.exit(1)

# ===================== G-R =====================
print("\n--- G-R  THE INCUMBENT REPRODUCES (to printed digits), AND EVERY MOVEMENT IS SHOWN ---")
print("%-26s %20s %20s %14s" % ("object", "repaired", "banked/incumbent", "movement"))
m1 = psi_r[0] - BANKED_PSI0
m1i = psi_i[0] - BANKED_PSI0
print("%-26s %20.12f %20.9f %14.3e" % ("Psi_W(0) vs banked", psi_r[0], BANKED_PSI0, m1))
print("%-26s %20.12f %20.12f %14.3e"
      % ("Psi_W(0) rep vs incumbent", psi_r[0], psi_i[0], psi_r[0] - psi_i[0]))
m2 = A_r.sum(0)[-1] - BANKED_SUMA
print("%-26s %20.12e %20.9e %14.3e" % ("sum_n A_n(UMAX)", A_r.sum(0)[-1], BANKED_SUMA, m2))
worst_iw, worst_move = 0.0, 0.0
print("\n  b134's I_W column:")
print("%8s %20s %20s %14s %14s" % ("a^2", "I_W repaired", "I_W banked", "vs banked", "vs incumbent"))
for a2 in CELLS:
    L = math.log(math.sqrt(a2))
    ir, ii = pairing(L, psi_r), pairing(L, psi_i)
    worst_iw = max(worst_iw, abs(ir - B134_IW[a2]))
    worst_move = max(worst_move, abs(ir - ii))
    print("%8d %20.12f %20.9f %14.3e %14.3e" % (a2, ir, B134_IW[a2], ir - B134_IW[a2], ir - ii))
print("\n  worst |I_W repaired - banked|    = %.3e   (b167's incumbent run: 4.824e-10)" % worst_iw)
print("  ### worst |repaired - incumbent| = %.3e   ### THE REPAIR'S OWN FOOTPRINT" % worst_move)
print("\n  ### THE PREDICTED MOVEMENT (registered before the run, e2):")
print("      Psi_W(0) moves by phi_e(0), the cancellation residue b115 banked at -1.42e-11")
print("      and b167 reproduced at -1.422267621e-11.")
print("      ### MEASURED movement of Psi_W(0), repaired - incumbent = %+.12e" % (psi_r[0] - psi_i[0]))
gr = (abs(m1) < 5e-10) and (abs(m2) < 1e-9) and (worst_iw < 1e-9)
print("\n### G-R : %s   ### criterion: reproduction TO PRINTED DIGITS"
      % ("PASS" if gr else "FAIL -- HALT"))
if not gr:
    sys.exit(1)
print("### ALL THREE GATES PASS. THE MEASUREMENT IS LICENSED, AND NOT BEFORE.")

# ===================== DELTA =====================
print("\n" + "=" * 92)
print("COMPONENT 2a -- DELTA ON THE LICENSED RANGE (repaired grid)")
print("=" * 92)
print("%10s %20s %20s %20s" % ("u", "sum_n A_n", "sum_n e_n", "Delta"))
for u in (0.0, 0.0970, 0.2523, 0.5045, 0.9993, 1.5039, 1.9987, 2.5032, 2.9980, 3.5025, UMAX):
    i = int(np.argmin(np.abs(ug - u)))
    print("%10.5f %20.9f %20.9f %20.9f" % (ug[i], A_r.sum(0)[i], E_r.sum(0)[i], delta_r[i]))
print("\n  Delta(0) = %.9f ; Delta(umax) = %.9f ; gross change = %+.9f"
      % (delta_r[0], delta_r[-1], delta_r[-1] - delta_r[0]))
print("  max|Delta| = %.9f ; min Delta = %+.9f ; sign changes = %d"
      % (np.abs(delta_r).max(), delta_r.min(),
         int((np.sign(delta_r[:-1]) != np.sign(delta_r[1:])).sum())))

# ===================== THE FLOOR =====================
print("\n" + "=" * 92)
print("COMPONENT 2b -- DELTA'S FLOOR ON EVERY INPUT AXIS (the floor-axis law)")
print("=" * 92)
axes = {}
for nl in (200, 400):
    axes['NLEG %d vs %d' % (nl, NLEG)] = float(np.abs(build(nleg=nl)[1] - delta_r).max())
for ng in (80, 240):
    axes['NGQ %d vs %d' % (ng, NGQ)] = float(np.abs(build(ngq=ng)[1] - delta_r).max())
for nq in (600, 800, 900):
    axes['NQ %d vs %d' % (nq, NQ)] = float(np.abs(build(nq=nq)[1] - delta_r).max())
for nr in (400, 1600):
    axes['n_rho %d vs 800' % nr] = float(np.abs(build(n_rho=nr)[1] - delta_r).max())
for npts in (200, 800):
    g2 = np.linspace(0.0, UMAX, npts)
    axes['u-grid %d vs 400' % npts] = float(
        np.abs(np.interp(ug, g2, build(grid=g2)[1]) - delta_r).max())
for k in sorted(axes, key=lambda z: -axes[z]):
    print("     %-22s : %.6e" % (k, axes[k]))
worst_axis = max(axes, key=lambda z: axes[z])
FLOOR = axes[worst_axis]
print("\n  ### DELTA'S FLOOR = MAX OVER ALL AXES = %.6e" % FLOOR)
print("  ### ITS AXIS = %s" % worst_axis)
print("  Psi_W's floor for comparison = 8.195851e-10, axis NQ via sigma_even (b134 G-D)")
print("  ### DELTA'S NQ AXIS MEASURES %.3e   ### Delta contains no sigma_even"
      % max(axes[k] for k in axes if k.startswith('NQ')))

# ===================== THE POST-DERIVATION CHECK =====================
print("\n--- THE SHIFT LAW AGAINST b155's BANKED d(mu) (a post-derivation check) ---")
d_from_law = -DEV12 / RATIO12
print("  b166's derived law: D_mu(c) = D_sigma(c) + (mu - sigma_even)*resid_N/|A|")
print("  erasing the a^2=12 deviation needs d(mu) = %.9f" % d_from_law)
print("  b155 banked                                = %.9f" % B155_DMU)
print("  ### residual = %.3e, and its source is stated: b155 computed from b109's ROUNDED"
      % abs(d_from_law - B155_DMU))
print("  ### -0.0073; from b110's -0.007261299 the law gives the value above. Neither is")
print("  ### wrong at its own input. ### THIS CHECK IS INDEPENDENT OF Delta.")

# ===================== THE FAMILY =====================
print("\n" + "=" * 92)
print("COMPONENT 2c -- THE ONE-SIGN VERDICT ACROSS THE FAMILY (P3)")
print("=" * 92)
print("  ### I_mu(L) = I_sigma(L) + (sigma_even - mu)*J(L),  J(L) = <PhiK, Delta(L.)>")
print("  sigma_even (layer, NQ=%d) = %.12f" % (NQ, sig))
Ls = np.linspace(math.log(math.sqrt(2)), math.log(math.sqrt(48)), 601)
Isig = np.array([pairing(L, psi_r) for L in Ls])
J = np.array([pairing(L, delta_r) for L in Ls])
print("\n%8s %14s %20s %20s" % ("a^2", "L", "I_sigma(L)", "J(L)"))
for a2 in CELLS:
    L = math.log(math.sqrt(a2))
    print("%8d %14.6f %20.12f %20.12f" % (a2, L, pairing(L, psi_r), pairing(L, delta_r)))
print("\n  sweep: max I_sigma = %+.9f ; J in [%+.9f, %+.9f] ; J sign changes = %d"
      % (Isig.max(), J.min(), J.max(),
         int((np.sign(J[:-1]) != np.sign(J[1:])).sum())))

dmax, dmin, Lhi, Llo = np.inf, -np.inf, None, None
for L, i0, j0 in zip(Ls, Isig, J):
    if j0 > 0:
        b = -i0 / j0
        if b < dmax:
            dmax, Lhi = b, L
    elif j0 < 0:
        b = -i0 / j0
        if b > dmin:
            dmin, Llo = b, L
mu_lo = sig - dmax if np.isfinite(dmax) else -np.inf
mu_hi = sig - dmin if np.isfinite(dmin) else np.inf
print("\n  ### d = sigma_even - mu admissible for I_mu(L) < 0 at EVERY swept L:")
print("      d in (%s, %s)" % ("%.9f" % dmin if np.isfinite(dmin) else "-inf",
                               "%.9f" % dmax if np.isfinite(dmax) else "+inf"))
print("  ### THEREFORE THE ONE-SIGN PROPERTY HOLDS EXACTLY FOR")
print("      ### mu in (%s, %s)"
      % ("%.9f" % mu_lo if np.isfinite(mu_lo) else "-inf",
         "%.9f" % mu_hi if np.isfinite(mu_hi) else "+inf"))
if np.isfinite(mu_lo):
    print("      binding L at the lower end = %.6f  (a^2 = %.4f)" % (Lhi, math.exp(2 * Lhi)))
if np.isfinite(mu_hi):
    print("      binding L at the upper end = %.6f  (a^2 = %.4f)" % (Llo, math.exp(2 * Llo)))
print("\n  b38's member mu = %.9f  : INSIDE = %s" % (sig, bool(mu_lo < sig < mu_hi)))
print("  the free end   mu = 0        : INSIDE = %s" % bool(mu_lo < 0.0 < mu_hi))
print("  mu = 1                       : INSIDE = %s" % bool(mu_lo < 1.0 < mu_hi))
print("  the illustrative bracket [0,1] wholly inside = %s"
      % bool(mu_lo < 0.0 and 1.0 < mu_hi))
print("\n  margins at named members (max I_mu over the sweep; Delta's floor %.3e):" % FLOOR)
for nm, mu in (("b38's member", sig), ("mu = 0", 0.0), ("mu = 1", 1.0), ("mu = 0.5", 0.5)):
    Im = Isig + (sig - mu) * J
    print("     %-16s max I_mu = %+.9f   strictly negative: %s" % (nm, Im.max(), bool(Im.max() < 0)))
np.save(r"D:\relay\tools\e16\b168_delta.npy", delta_r)
np.save(r"D:\relay\tools\e16\b168_ug.npy", ug)
print("\n  (Delta and its u grid saved.)")
print("=" * 92)
