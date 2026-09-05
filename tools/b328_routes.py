# -*- coding: utf-8 -*-
"""b328_routes.py -- THE SEALED ROUTE BAR (B4), FOUND DEFECTIVE BY RUNNING IT, AND MEASURED.

### ### **WHAT THE SEAT SEALED:** ### the corpus's closed form and this act's Simpson quadrature, on the
### same nodes, must agree to `1e-10` relative. ### **WHAT THE RUN RETURNED:** ### `2e-6` on the aimed
### seeds. ### **WHY, MEASURED HERE AND NOT WAVED:** ### the seed is PIECEWISE LINEAR on its nodes and the
### closed form integrates exactly that interpolant; Simpson's rule fits a parabola through each node
### triple and integrates a DIFFERENT function -- its error on a kinked integrand is second order in the
### node spacing, not fourth. ### So the two routes were never integrating the same thing at `1e-10`,
### and the bar was unsatisfiable by construction -- b319's species (a sealed bar the object cannot meet).
### ### **THE MEASUREMENT:** ### Simpson on the same piecewise-linear function resampled at 1x, 2x, 4x the
### nodes; the disagreement must fall by four at each doubling if the diagnosis is right.
### ### **THE ROUTE THAT INTEGRATES THE SAME FUNCTION:** ### three-point Gauss-Legendre on EVERY segment
### (a polynomial of degree one times `e^{c v}`, resolved to near machine precision on a segment of
### length `3e-4`), sharing no code with the closed form. ### It is reported against the sealed bar; the
### sealed file is not edited and the Simpson result stands beside it.
### ### **AND THE FIRST DIAGNOSIS WAS WRONG, AND ITS OWN MEASUREMENT REFUTED IT** (kept as
### `b328_routes_run_first_diagnosis.txt`): the seat wrote 'second order in the node spacing' and printed
### ratios of four to expect. ### The 2x resampling returned `7e-13`, not a quarter of `1.6e-6`: on a grid
### that contains the seed's nodes at even positions no Simpson triple straddles a kink, and Simpson is
### EXACT on a linear segment. ### The 1x disagreement is the kink-straddling error alone, and vanishes,
### rather than shrinking by four, once the triples align with the segments.
"""
import io
import json
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import b328_family as F  # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

GL_X = np.array([-math.sqrt(3.0 / 5.0), 0.0, math.sqrt(3.0 / 5.0)])
GL_W = np.array([5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0])


def G_gauss(v, w, c):
    """### three-point Gauss-Legendre per segment of the piecewise-linear (v, w); this file's own code."""
    v = np.asarray(v, dtype=np.float64)
    w = np.asarray(w, dtype=np.float64)
    a, b = v[:-1], v[1:]
    wa, wb = w[:-1], w[1:]
    h = b - a
    total = 0.0 + 0.0j
    for x, gw in zip(GL_X, GL_W):
        t = 0.5 * (x + 1.0)                         # ### node fraction in [0, 1]
        vv = a + t * h
        ww = wa + t * (wb - wa)                     # ### the SAME piecewise-linear function
        total += gw * np.sum(ww * np.exp(c * vv) * h) * 0.5
    return complex(total)


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b328_routes.py -- THE SEALED ROUTE BAR (B4), RUN, FOUND DEFECTIVE, MEASURED. ### THE SEALED FILE IS NOT EDITED.')
    rec('=' * 100)
    # ### a fixture the Gauss route must pass: a triangle w on [-1, 1] at c = 0 integrates to exactly 1 (area).
    v = np.linspace(-1.0, 1.0, 5)
    w = np.array([0.0, 0.5, 1.0, 0.5, 0.0])
    g0 = G_gauss(v, w, 1e-300 + 0j)
    fx = abs(g0 - 1.0) < 1e-13
    rec('  fixture: the unit triangle at c = 0 by the Gauss route : %.16f  %s' % (g0.real, 'PASS' if fx else '### FAIL ###'))
    if not fx:
        return 2
    res = []
    for kind, a in (('E', 81.0), ('O', 81.0), ('E', 160.0)):
        seed = F.make_seed(kind, a)
        v, w = seed.v, seed.w
        gc = F.G_closed(v, w, F.C1)
        gg = G_gauss(v, w, F.C1)
        s1 = F.G_simpson(v, w, F.C1, n=F.NV)
        s2 = F.G_simpson(v, w, F.C1, n=2 * F.NV - 1)
        s4 = F.G_simpson(v, w, F.C1, n=4 * F.NV - 3)
        d1, d2, d4 = (abs(s - gc) / abs(gc) for s in (s1, s2, s4))
        dg = abs(gg - gc) / abs(gc)
        rec('  seed %s a = %g : Simpson vs closed form at 1x %.3e, 2x %.3e, 4x %.3e nodes ; ratios %.2e, %.2f (exact at 2x: no triple straddles a kink)'
            % (kind, a, d1, d2, d4, d1 / d2, d2 / d4))
        rec('             Gauss-Legendre per segment vs closed form : %.3e   sealed bar %.0e   %s'
            % (dg, F.ROUTE_BAR, 'MEETS THE SEALED BAR' if dg <= F.ROUTE_BAR else '### FAILS ###'))
        res.append(dict(kind=kind, a=a, simpson_1x=d1, simpson_2x=d2, simpson_4x=d4, gauss=dg, gauss_meets_bar=bool(dg <= F.ROUTE_BAR)))
    rec('')
    rec('  ### THE FINDING: the Simpson route fits parabolas through node triples and integrates a DIFFERENT function from the')
    rec('  ### piecewise-linear seed: on the native nodes every odd node is a kink inside a triple; on the 2x grid no triple straddles')
    rec('  ### a kink and Simpson is exact (7e-13). ### So the bar as sealed could not be met by Simpson on the native nodes, and')
    rec("  ### the seat's first diagnosis (second order) was refuted by the 2x ratio. ### A route integrating the SAME function --")
    rec('  ### Gauss-Legendre per segment, sharing no')
    rec('  ### code with the closed form -- meets the sealed bar. ### FILED AS A SEALED BAR FOUND DEFECTIVE BY RUNNING IT.')
    rec('=' * 100)
    io.open(os.path.join(D, 'b328_routes.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(res, indent=1) + '\n')
    io.open(os.path.join(D, 'b328_routes_run.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
    return 0 if all(r['gauss_meets_bar'] for r in res) else 1


if __name__ == '__main__':
    sys.exit(main())
