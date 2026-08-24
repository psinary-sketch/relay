# -*- coding: utf-8 -*-
"""b134 -- COMPONENTS 2 and 3: the re-runs on repaired ground, and the asking.

Runs ONLY because all four gates passed. Psi_W is the repaired density; the
b119 split machinery is reproduced from b119_dominance.py's own definition,
quoted there as
    psi_coarse(u) = int_{-2}^{+2} K(s) Psi(u+s) ds   [K normalized to mass 1]
    psi_fine(u)   = Psi(u) - psi_coarse(u)
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121
import b134_wroute as WR

CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
FLOOR = 8.195851e-10          # the route's floor, b134 G-D, AXIS = NQ via sigma_even
B119_RATIO = {2: 0.282, 3: 0.373, 4: 0.461, 8: 0.462, 9: 0.455,
              12: 0.438, 16: 0.427, 24: 0.420, 48: 0.431}

ug = np.load(r"D:\relay\tools\e16\b134_ug.npy")
psi = np.load(r"D:\relay\tools\e16\b134_psiW.npy")
sg, K, Phi = B121.build_kernel()
psiQ, _ = B121.psi_at(700, ug)

print("=" * 78)
print("b134 COMPONENTS 2-3 -- THE RE-RUNS AND THE ASKING (gates passed)")
print("=" * 78)

# ---------------- P2 : Psi re-profiled ----------------
print("\n--- P2a  Psi RE-PROFILED ON THE W ROUTE ---")
print("  Psi_W(0)      = %+.9f   (known -1.165002987)" % psi[0])
print("  Psi_W(umax)   = %+.9f   [Psi_Q(umax) = %+.9f]" % (psi[-1], psiQ[-1]))
print("  gross rise    = %+.9f   [Q: %+.9f]" % (psi[-1] - psi[0], psiQ[-1] - psiQ[0]))
print("  max|Psi_W|    = %.9f    min Psi_W = %+.9f" % (np.abs(psi).max(), psi.min()))
d = np.diff(psi)
dq = np.diff(psiQ)
print("  sign changes in dPsi : W = %d ; Q = %d   ### THE FINE STRUCTURE'S CHANGE"
      % (int((np.sign(d[:-1]) != np.sign(d[1:])).sum()),
         int((np.sign(dq[:-1]) != np.sign(dq[1:])).sum())))
print("  ### THE REFINEMENT-STABLE SCALE, WITH ITS AXES: %.6e" % FLOOR)
print("      axis = NQ, entering ONLY through sigma_even (the part the route did")
print("      not replace). The route's own axes NLEG and NGQ sit at ~2e-13.")

# ---------------- P2b : the one-sign verdict ----------------
print("\n--- P2b  THE ONE-SIGN VERDICT RE-RUN ON REPAIRED GROUND ---")


def I_of(L, arr):
    q = np.interp(L * sg, ug, arr, right=arr[-1])
    return float(np.trapezoid(Phi * q, sg))


print("%6s %18s %18s %14s" % ("a^2", "I_W(L)", "I_Q(L) (incumbent)", "difference"))
IW = {}
for a2 in CELLS:
    L = math.log(math.sqrt(a2))
    IW[a2] = I_of(L, psi)
    print("%6d %18.9f %18.9f %14.3e" % (a2, IW[a2], I_of(L, psiQ), abs(IW[a2] - I_of(L, psiQ))))
mx = max(IW.values())
print("\n  ### max I_W over the nine cells = %+.9f" % mx)
Ls = np.linspace(math.log(math.sqrt(2)), math.log(math.sqrt(48)), 601)
sweep = np.array([I_of(L, psi) for L in Ls])
print("  ### max I_W over the 601-point sweep = %+.9f at L = %.6f"
      % (sweep.max(), Ls[int(np.argmax(sweep))]))
print("  ### margin against the route's floor: %.9f - %.3e = %+.9f"
      % (abs(sweep.max()), FLOOR, abs(sweep.max()) - FLOOR))
print("  ### STRICTLY NEGATIVE ACROSS CELLS AND SWEEP: %s" % (sweep.max() < 0))
print("  *** AND THE BASIS AXIS, WHICH NO LONGER EXISTS AS A KNOB: W's spectrum")
print("  *** is simple (smallest separation 7.709623), so the prolate basis is")
print("  *** UNIQUE. b121's 'basis variation' was varying NOISE, not a basis.")

# ---------------- P3 : the asking ----------------
print("\n" + "=" * 78)
print("--- P3  THE ONE ASKING, SPENT: THE DOMINANCE QUESTION ON REPAIRED GROUND ---")
print("=" * 78)
ss = np.linspace(-2.0, 2.0, 801)
Kn = np.interp(np.abs(ss), sg, K)
Kn = Kn / float(np.trapezoid(Kn, ss))


def psi_ext(uq, arr):
    return np.interp(np.clip(uq, ug[0], ug[-1]), ug, arr)


coarse = np.array([float(np.trapezoid(Kn * psi_ext(u + ss, psi), ss)) for u in ug])
fine = psi - coarse
print("  psi_coarse endpoint rise = %+.9f  (%.1f%% of Psi_W's)"
      % (coarse[-1] - coarse[0], 100 * (coarse[-1] - coarse[0]) / (psi[-1] - psi[0])))
print("  max|psi_fine| = %.6f ; max|psi_coarse| = %.6f"
      % (np.abs(fine).max(), np.abs(coarse).max()))
print("\n%6s %18s %18s %16s %10s %10s" %
      ("a^2", "coarse pairing", "fine pairing", "sum (= I_W)", "ratio", "b119"))
worst_r, dominated = 0.0, True
for a2 in CELLS:
    L = math.log(math.sqrt(a2))
    cq = float(np.trapezoid(Phi * np.interp(L * sg, ug, coarse, right=coarse[-1]), sg))
    fq = float(np.trapezoid(Phi * np.interp(L * sg, ug, fine, right=fine[-1]), sg))
    r = abs(fq) / abs(cq)
    worst_r = max(worst_r, r); dominated = dominated and (r < 1.0)
    print("%6d %18.9f %18.9f %16.9f %10.3f %10.3f"
          % (a2, cq, fq, cq + fq, r, B119_RATIO[a2]))
print("\n  ### WORST RATIO OVER THE NINE CELLS = %.3f   (b119's was 0.462)" % worst_r)
print("  ### DOMINATED AT ALL NINE CELLS: %s" % dominated)
dense = []
for L in np.linspace(math.log(math.sqrt(2)), math.log(math.sqrt(48)), 60):
    cq = float(np.trapezoid(Phi * np.interp(L * sg, ug, coarse, right=coarse[-1]), sg))
    fq = float(np.trapezoid(Phi * np.interp(L * sg, ug, fine, right=fine[-1]), sg))
    dense.append(abs(fq) / abs(cq))
print("  ### 60-POINT SWEEP: worst ratio %.3f ; dominated at %d of 60"
      % (max(dense), sum(1 for r in dense if r < 1.0)))
print("\n  THE BASIS SWEEP, ANSWERED STRUCTURALLY RATHER THAN BY SAMPLING:")
print("    the recorded basis, b121's alternates and any fresh draw ALL COLLAPSE")
print("    to ONE basis on the W route -- W is NQ-independent and its spectrum is")
print("    simple, so there is no basis freedom to sweep. Seed structure: NONE.")
print("\n  ### THE VERDICT, QUOTED FROM ITS REGISTERED BRANCH:")
print("      %s" % ("BRANCH (a) -- dominance holds; RESTORED at its grade on repaired ground"
                    if dominated else
                    "BRANCH (b) -- fails or stays basis-dependent; third-outcome cell"))
