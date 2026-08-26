# -*- coding: utf-8 -*-
"""b171 -- the numeric check fixed at registration: the corpus's own SUM t(n)
against the external source's stated eps'(1+) ~ 22.9965.

### THIS IS A COMPARISON, NOT A LICENCE. The source's value is EXTERNAL and enters
marked as such; the corpus's value is its own. Neither is adjusted to meet the other.
"""
import functools, math, sys
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import qeps_layer as Q

SOURCE_VALUE = 22.9965          # EXTERNAL: arXiv 2006.13771, quoted "approximately 22.9965"

print("=" * 86)
print("b171 -- SUM t(n) FROM THE CORPUS'S OWN LAYER vs THE SOURCE'S eps'(1+)")
print("=" * 86)
print("  t(n) := lambda(n)^2 * xi_n(1)^2 / (1 - lambda(n)^2)   [the corpus's own weight]")
print("  the source's sum carries lambda(n)/(1 - lambda(n)^2)  [DIFFERENT WEIGHT]")
print()
print("%6s %8s %20s %20s %16s" % ("NQ", "modes", "SUM t(n)", "SUM lam/(1-lam^2)", "vs 22.9965"))
for NQ in (500, 700, 900, 1100):
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)
    n = len(lam2)
    tn = lam2 / (1 - lam2) * xi1 ** 2
    src_w = np.sqrt(np.abs(lam2)) / (1 - lam2)      # |lambda|/(1-lambda^2), the source's shape
    print("%6d %8d %20.9f %20.9f %16.4f"
          % (NQ, n, float(tn.sum()), float(src_w.sum()), float(tn.sum()) - SOURCE_VALUE))

print()
print("  --- and at the reference cell's truncation, NMODE = 10 ---")
x, w, lam, lam2, xi, xi1, an, dan = Q.layer(700)
tn = lam2[:10] / (1 - lam2[:10]) * xi1[:10] ** 2
print("  SUM_{n<10} t(n) = %.9f      difference from 22.9965 = %+.4f"
      % (float(tn.sum()), float(tn.sum()) - SOURCE_VALUE))
print("  the ten terms: " + ", ".join("%.6f" % v for v in tn))
print()
print("  --- the partial sums, so a truncation reading can be judged rather than assumed ---")
run = 0.0
for i, v in enumerate(tn):
    run += float(v)
    print("     n <= %-2d : SUM t = %14.9f" % (i, run))
print("=" * 86)
