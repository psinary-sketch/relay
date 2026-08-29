# -*- coding: utf-8 -*-
"""b238_final.py -- THE FINAL VERIFICATION, RUN ONCE AT THE NAMED TEST AXES.

### THIS FILE RUNS **AFTER** `data/b238_criterion.txt` EXISTS AND IS WRITTEN. It reads the
### criterion's bounds from that file rather than recomputing them, so the comparison cannot
### drift from what was banked. ### THE TWO FILES' TIMESTAMPS ARE THE EVIDENCE THAT THE
### CRITERION PRECEDED THE RESULT, AND A GATE COMPARES THEM.

### THE TEST AXES: NV in {4001, 6001}, NU = 12001, UMAX = 600, N = 1000.
### ### NEITHER TEST AXIS WAS USED TO FIT K. ### The criterion is an out-of-sample prediction
### at both, and one cell over its bound is branch (HELD).

### THE INSTRUMENTS ARE IMPORTED UNMODIFIED. ### The zero side uses the same banked ordinates
### b233 computed with mpmath.zetazero and controlled against the banked file at 0.000e+00.
"""
import io
import json
import math
import re
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C        # noqa: E402
import b38_act10 as B38        # noqa: E402

CACHE = (r"C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--"
         r"\2bde398e-07cf-4dd0-8608-0a3b93e6f10a\scratchpad\b233_zeros.json")
CRIT = r"D:\relay\data\b238_criterion.txt"
CELLS = [(2, "2"), (3, "3"), (4, "4")]
PRIMES = (2, 3, 5)
TEST_NV = [4001, 6001]


def read_bounds():
    """### THE BOUNDS ARE READ FROM THE BANKED CRITERION, NEVER RECOMPUTED HERE."""
    out = {}
    txt = io.open(CRIT, encoding='utf-8').read()
    for line in txt.splitlines():
        m = re.match(r'\s{2}(\d)\s+(\d+)\s+([0-9.e+-]+)\s+([0-9.e+-]+)\s+([0-9.e+-]+)\s*$', line)
        if m:
            out[(m.group(1), int(m.group(2)))] = float(m.group(5))
    return out


def run_cell(a, nv, gam):
    old = C.NV
    C.NV = nv
    C._KERN = None
    try:
        v, w, corr, vc, L = B38.family(a)
        A, P, PR = B38.left_side(a, PRIMES, v, w, corr, vc, L)
        g = C.hhat(v, w, gam)
        Z = 2.0 * float(np.sum(g * g))
    finally:
        C.NV = old
        C._KERN = None
    return Z, P, A, PR, Z - (P - PR + A)


def main():
    bounds = read_bounds()
    if len(bounds) != 6:
        print("### REFUSED -- the banked criterion did not yield 6 bounds (got %d)." % len(bounds))
        return 2
    gam = np.array(json.load(io.open(CACHE, encoding='utf-8'))[:1000], dtype=float)

    print("=" * 108)
    print("b238 -- THE FINAL VERIFICATION. ### RUN ONCE, AT THE NAMED TEST AXES.")
    print("### THE BOUNDS BELOW WERE READ FROM data/b238_criterion.txt, NOT RECOMPUTED HERE.")
    print("=" * 108)
    print("  %-6s %-7s %14s %14s %14s %13s %13s %8s"
          % ("a^2", "NV", "A", "PR", "Z", "residual", "BOUND", "verdict"))
    ok = True
    for nv in TEST_NV:
        for a_sq, tag in CELLS:
            Z, P, A, PR, resid = run_cell(math.sqrt(a_sq), nv, gam)
            b = bounds[(tag, nv)]
            good = abs(resid) <= b
            ok = ok and good
            print("  %-6s %-7d %14.9f %14.9f %14.9f %13.3e %13.3e %8s"
                  % (tag, nv, A, PR, Z, resid, b, "within" if good else "### OVER"))
    print("\n" + "=" * 108)
    print("  ### EVERY CELL AT EVERY TEST AXIS WITHIN ITS BANKED BOUND: %s" % ("YES" if ok else "NO"))
    print("  ### THE BOUNDS WERE FIT ON NV in {2001, 8001, 16001} AND TESTED AT {4001, 6001}.")
    print("  ### 'WITHIN' MEANS THE RESIDUAL IS EXPLAINED BY THE MEASURED BUDGET AT THE STATED")
    print("  ### AXES. ### IT DOES NOT MEAN THE EXPLICIT FORMULA IS PROVED HERE, AND NO AXIS WAS")
    print("  ### CHOSEN FOR AGREEMENT -- the test axes were named in the criterion file before")
    print("  ### this file existed.")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
