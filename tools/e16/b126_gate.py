# -*- coding: utf-8 -*-
"""b126 -- THE GATE ON THIS ACT'S OWN INSTRUMENT.
Reproduce-before-extend, applied to b126_localization's baseline: run it at
B121'S EXACT AXES (u grid 400 points, NQ in {600,800,900}) and check that the
baseline column reproduces b121's recorded 4.361e-01.
Then show the same quantity at 200 points, so the difference is attributed to
the u grid at content and not by assertion.
"""
import functools, math, sys
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121

UMAX = 2.0 * math.log(math.sqrt(48.001))
print("=" * 78)
print("b126 -- THE GATE: this act's baseline against b121's recorded figure")
print("=" * 78)
print("  the callee is b121_instrument.psi_at ITSELF -- the incumbent's own code,")
print("  not a re-implementation, so the comparison cannot drift.\n")
print("%8s %10s %16s" % ("u pts", "NQ set", "worst |dPsi|"))
for npts in (400, 200):
    ug = np.linspace(0.0, UMAX, npts)
    ref, _ = B121.psi_at(700, ug)
    for nqset in ((600, 800, 900), (600, 800, 900, 1100)):
        worst = 0.0
        for NQ in nqset:
            p, _ = B121.psi_at(NQ, ug)
            worst = max(worst, float(np.abs(p - ref).max()))
        print("%8d %10s %16.6e" % (npts, "%d..%d" % (nqset[0], nqset[-1]), worst))
print("\n  b121 RECORDED (u pts 400, NQ 600..900) : 4.361e-01")
print("  ### the reconciliation is the U GRID, read at content from b121 line 73.")
