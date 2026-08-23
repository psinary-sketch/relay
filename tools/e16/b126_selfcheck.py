# -*- coding: utf-8 -*-
"""b126 SELF-CHECK on the instrument, before any verdict rests on it.
(1) NMODE at content, and the known answer reconciled arithmetically.
(2) the spectrum with its separations, so 'floor' and 'well-separated' are
    quoted rather than recalled.
(3) WHAT F2 ACTUALLY VARIED -- stated as code, not as a label.
"""
import functools, math, sys
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

NMODE = B38.TRIPLE[1][1]
print("(1) NMODE read at content from B38.TRIPLE[1][1] = %d" % NMODE)
print("    B38.TRIPLE = %r" % (B38.TRIPLE,))
x, w, lam, lam2, xi, xi1, an, dan = Q.layer(700)
tn = lam2 / (1 - lam2) * xi1 ** 2
s = tn[:NMODE] / float(tn[:NMODE].sum())
sig = float(s[0::2].sum())
n_even = len(range(0, NMODE, 2))
print("    even modes among 0..%d : %d" % (NMODE - 1, n_even))
print("    sigma_even              : %.12f" % sig)
print("    %d - %.9f * %d = %+.9f   vs standing -1.165002987"
      % (n_even, sig, NMODE, n_even - sig * NMODE))

print("\n(2) THE SPECTRUM AT NQ=700, with separations")
print("%4s %16s %18s %16s" % ("n", "lam2", "sep to next", "1/(1-lam2)"))
for n in range(NMODE):
    sep = float(lam2[n] - lam2[n + 1]) if n + 1 < len(lam2) else float("nan")
    print("%4d %16.6e %18.6e %16.6e" % (n, lam2[n], sep, 1.0 / (1.0 - lam2[n])))
print("    NOTE, a held axis: NMODE is pinned to the REFERENCE CELL's count (10).")
print("    B38.TRIPLE's 900 cell carries 11 modes; this act holds the mode count")
print("    fixed while NQ varies, so that NQ changes ONE thing and not two.")

print("\n(3) WHAT F1/F2 ACTUALLY VARIED -- named as objects, not as labels")
print("    F2 varied ONLY sigma_even (the MASS weights t_n = lam2/(1-lam2)*xi(1)^2).")
print("    sigma_even across NQ, to show what F2's near-zero share is a fact about:")
for NQ in (600, 700, 800, 900, 1100):
    _, _, _, l2, _, x1, _, _ = Q.layer(NQ)
    t = l2 / (1 - l2) * x1 ** 2
    ss = t[:NMODE] / float(t[:NMODE].sum())
    v = float(ss[0::2].sum())
    print("      NQ=%4d  sigma_even = %.12f   (dev from ref %+.3e)" % (NQ, v, v - sig))
print("    *** THE QUADRATURE WEIGHTS w ARE **NOT** FROZEN BY F2. They vary with")
print("    NQ inside A_n at every configuration, so F2's 0.0%% share EXCLUDES the")
print("    mass-weight denominator (H1's object) and EXCLUDES NOTHING ELSE.")
