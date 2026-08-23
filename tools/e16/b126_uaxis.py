# -*- coding: utf-8 -*-
"""b126 -- THE U-AXIS READING. RECORDED AS A DEVIATION: an added READING of
component 2's own quantity along its other axis. No new hypothesis, no new
sample family -- the same A_n(u) arrays, tabulated against u instead of
against n.

WHY IT IS DECISIVE BETWEEN THE TWO SURVIVING SUSPECTS:
  at u = 0 the dilation is the identity, np.interp(x, x, f) returns f EXACTLY,
  and no interpolation of a dilated copy occurs at all. Whatever deviation
  survives at u = 0 is therefore the QUADRATURE WEIGHTS' scaling (suspect 1)
  and cannot be the dilation (suspect 2).
  A deviation that is ~0 at u = 0 and grows with u is the dilation.
"""
import functools, math, sys
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

UMAX = 2.0 * math.log(math.sqrt(48.001))
NMODE = B38.TRIPLE[1][1]
REF, NQS = 700, (600, 800, 900, 1100)
_c = {}


def layer(NQ):
    if NQ not in _c:
        _c[NQ] = Q.layer(NQ)
    return _c[NQ]


def A_modes(ug, NQ):
    x, w, lam, lam2, xi, xi1, an, dan = layer(NQ)
    out = np.zeros((NMODE, len(ug)))
    for n in range(NMODE):
        f = xi[:, n]
        for i, u in enumerate(ug):
            ld = math.exp(u)
            fy = np.interp(ld * x, x, f, left=0.0, right=0.0)
            out[n, i] = math.sqrt(ld) * 0.5 * float((w * f * fy).sum())
    return out


ug = np.linspace(0.0, UMAX, 200)
A = {NQ: A_modes(ug, NQ) for NQ in (REF,) + NQS}

print("=" * 78)
print("b126 -- THE U-AXIS READING  (deviation: added reading, no new samples)")
print("=" * 78)
print("\n(A) A_n(0) ACROSS NQ -- the identity dilation, where interp is exact.")
print("    derived fact: A_n(0) = 1 for every mode.")
print("%4s %18s %18s %18s" % ("n", "A_n(0) at ref", "worst |A_n(0)-1|", "worst dev vs ref"))
for n in range(NMODE):
    wa = max(abs(A[NQ][n, 0] - 1.0) for NQ in (REF,) + NQS)
    wd = max(abs(A[NQ][n, 0] - A[REF][n, 0]) for NQ in NQS)
    print("%4d %18.12f %18.6e %18.6e" % (n, A[REF][n, 0], wa, wd))
w0 = max(max(abs(A[NQ][n, 0] - A[REF][n, 0]) for NQ in NQS) for n in range(NMODE))
print("\n  ### WORST PER-MODE DEVIATION AT u = 0, OVER ALL NQ AND ALL MODES: %.6e" % w0)

print("\n(B) THE DEVIATION AS A FUNCTION OF u  (max over modes and over NQ)")
print("%10s %10s %18s" % ("u", "dilation", "max_n,NQ |dA_n(u)|"))
for i in range(0, len(ug), 20):
    d = max(float(np.abs(A[NQ][:, i] - A[REF][:, i]).max()) for NQ in NQS)
    print("%10.4f %10.4f %18.6e" % (ug[i], math.exp(ug[i]), d))
i = len(ug) - 1
d = max(float(np.abs(A[NQ][:, i] - A[REF][:, i]).max()) for NQ in NQS)
print("%10.4f %10.4f %18.6e" % (ug[i], math.exp(ug[i]), d))

print("\n  ### THE READING:")
print("  deviation at u = 0 (identity dilation) : %.6e" % w0)
d_end = d
print("  deviation at u = %.4f (dilation %.2f) : %.6e" % (ug[-1], math.exp(ug[-1]), d_end))
if w0 < 1e-9 < d_end:
    print("  SUSPECT (1) THE QUADRATURE WEIGHTS' SCALING: **EXCLUDED** -- with the")
    print("    dilation switched off the evaluation is exact to %.1e; the weight" % w0)
    print("    scaling is sound, and the executor's own registered expectation FAILS.")
    print("  SUSPECT (2) THE DILATION INTERACTION: **LOCATED** -- the deviation is")
    print("    created by the dilation and by nothing else in the evaluation.")
else:
    print("  the u = 0 deviation is NOT negligible; suspect (1) SURVIVES and the")
    print("  two are NOT separated by this reading.")
