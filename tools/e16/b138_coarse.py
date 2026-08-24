# -*- coding: utf-8 -*-
"""b138 -- COMPONENT 2: the coarse-channel lemma.

### THE CIRCULARITY GATE. Nothing below cites E1-E6 (the ratio tables, the
### sweeps, the disjunction test, or any measured C/F/I). The DERIVATION is
### written in the bank and uses only: Phi_K mean-zero with one crossing
### positive-then-negative (b116, derived), and the b119 split's exact form.
### THIS FILE RUNS ONLY POST-DERIVATION CHECKS, and each is labelled as one.

THE DERIVED IMPLICATION (bank, component 2), grade INHERITED from b116:
    psi_coarse monotone increasing on [0, 2L]  =>  C(L) < 0.
THE WITHHELD STEP: psi_coarse's monotonicity.
THIS FILE TESTS THE WITHHELD STEP NUMERICALLY. That test decides whether the
act's yield is a RELOCATED OPEN or a SECOND REFUTATION.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121

UMAX = 2.0 * math.log(math.sqrt(48.001))
ug = np.load(r"D:\relay\tools\e16\b134_ug.npy")
psi = np.load(r"D:\relay\tools\e16\b134_psiW.npy")   # the REPAIRED density
sg, K, Phi = B121.build_kernel()

print("=" * 78)
print("b138 COMPONENT 2 -- POST-DERIVATION CHECKS ONLY")
print("=" * 78)

# ---- the split, at b119's own definition ----
ss = np.linspace(-2.0, 2.0, 1601)
Kn = np.interp(np.abs(ss), sg, K)
Kn = Kn / float(np.trapezoid(Kn, ss))
coarse = np.array([float(np.trapezoid(Kn * np.interp(np.clip(u + ss, ug[0], ug[-1]), ug, psi), ss))
                   for u in ug])

print("\n--- CHECK 1 (post-derivation): IS psi_coarse MONOTONE INCREASING? ---")
print("  the withheld step, tested. b116 REFUTED the same hypothesis at the RAW")
print("  density: 'Psi is not monotone increasing, 149 descents all above the")
print("  2.774e-05 scale.' The question is whether smoothing removes them.")
d = np.diff(coarse)
du = float(ug[1] - ug[0])
desc = int((d < 0).sum())
print("\n  raw Psi   : descents = %d of %d steps ; worst descent = %.6e"
      % (int((np.diff(psi) < 0).sum()), len(psi) - 1, float(np.diff(psi).min())))
print("  psi_coarse: descents = %d of %d steps ; worst descent = %.6e"
      % (desc, len(coarse) - 1, float(d.min())))
print("  psi_coarse rise: %+.9f -> %+.9f" % (coarse[0], coarse[-1]))
if desc == 0:
    print("\n  ### psi_coarse IS MONOTONE INCREASING on the sampled grid.")
    print("  ### THE WITHHELD STEP HOLDS NUMERICALLY -> the act's yield is a")
    print("  ### RELOCATED OPEN, not a second refutation.")
else:
    print("\n  ### psi_coarse IS NOT MONOTONE: %d descents, worst %.6e" % (desc, d.min()))
    print("  ### against the derivative scale |dpsi_coarse/du|max = %.6e"
          % float(np.abs(d / du).max()))
    print("  ### THE ACT'S YIELD IS A SECOND REFUTATION IF THESE ARE ABOVE THE FLOOR.")
    print("  ### the repaired route's floor on Psi (b134) = 2.774493e-05, axis epsilon")
    print("  ### worst descent as a fraction of that floor: %.3f"
          % (abs(float(d.min())) / 2.774493e-05))

print("\n--- CHECK 2 (post-derivation): DOES THE DERIVED IMPLICATION AGREE? ---")
print("  the implication is: monotone psi_coarse => C(L) < 0. Below, C(L) is")
print("  computed and compared to what the implication would predict. THIS IS A")
print("  CHECK OF A DERIVATION ALREADY WRITTEN, not a premise for it.")
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
print("%6s %18s %14s" % ("a^2", "C(L)", "sign"))
allneg = True
for a2 in CELLS:
    L = math.log(math.sqrt(a2))
    c = float(np.trapezoid(Phi * np.interp(L * sg, ug, coarse, right=coarse[-1]), sg))
    allneg = allneg and (c < 0)
    print("%6d %18.9f %14s" % (a2, c, "neg" if c < 0 else "POS"))
print("\n  ### C(L) < 0 at all nine cells: %s" % allneg)
print("  ### consistent with the derived implication: %s"
      % ("YES" if (allneg or desc > 0) else "NO -- the implication would be contradicted"))

print("\n--- CHECK 3 (post-derivation): Phi_K's STRUCTURE, the derivation's input ---")
sgn = np.sign(Phi)
nz = sgn[sgn != 0]
crossings = int((nz[:-1] != nz[1:]).sum())
print("  INT Phi_K over [0,2] = %.9e  (mean-zero required)" % float(np.trapezoid(Phi, sg)))
print("  sign changes of Phi_K on [0,2] = %d  (exactly one required)" % crossings)
i0 = int(np.argmax(np.sign(Phi[:-1]) != np.sign(Phi[1:])))
print("  crossing at sigma = %.4f  (b116 records 0.6215)" % sg[i0])
print("  positive before, negative after: %s" % (Phi[i0 - 1] > 0 and Phi[i0 + 2] < 0))
print("\n  ### these are the DERIVATION'S INPUTS, re-verified here rather than")
print("  ### assumed. They are b116's derived facts and are not part of E1-E6.")
