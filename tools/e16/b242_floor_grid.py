# -*- coding: utf-8 -*-
"""b242 COMPONENT 1b -- THE EIGENVALUE FLOOR, TESTED. ### STILL NO ENVELOPE.

### THE QUESTION THIS ANSWERS, AND IT IS HAZARD H-c OF THE REGISTRATION, NAMED BEFORE THE
### MEASUREMENT: ### AXIS 2 SHOWED `Tr_full(10)` DOES NOT CONVERGE IN NQ -- increments
### 5.9e-03, 1.76e-01, 1.42e-02, 4.37e-02 at a^2 = 2, NON-MONOTONE. ### AND AXIS 1 SHOWED
### `tr[n]` FALLING SMOOTHLY TO n = 6 AND THEN GOING NON-MONOTONE (0.0513, 0.0034, 0.0131,
### 0.0128 at a^2 = 2).
###
### ### BOTH ANOMALIES SIT AT THE SAME PLACE: `lam2` REACHES 4.7e-16 AT n = 7. ### An
### ### eigenvector for a near-degenerate eigenvalue at the float64 floor is arbitrary within
### ### its near-null space -- so it CHANGES WITH NQ, and a trace built on it is noise wearing
### ### a mode index.
###
### THE TEST: `Tr_full(NMODE, NQ)` on a GRID. ### If the NQ instability lives entirely in the
### floor modes, the partial sums up to n = 6 will be NQ-STABLE and the ones past it will not.
### ### THAT IS A FALSIFIABLE PREDICTION AND THIS TOOL IS ALLOWED TO REFUTE IT.
###
### ### SCOPE: LEFT SIDE ONLY. ### `A` never enters this file at all -- not even as a constant.
### ### NO ENVELOPE IS DERIVED HERE.
"""
import io
import json
import math
import os
import sys

sys.path.insert(0, r"D:\relay\tools\e16")
import numpy as np                      # noqa: E402
import b38_act10 as B38                 # noqa: E402
import qeps_layer as Q                  # noqa: E402
import prolate_layer as PL              # noqa: E402

BANK = r"D:\relay\data\b242_floor_grid.txt"
CACHE = r"D:\relay\data\b242_floor_points.json"

NQ_AXIS = [500, 700, 900, 1100, 1300]
NM_AXIS = [4, 5, 6, 7, 8, 9, 10, 11]
FLOOR = 1e-13                           # ### the float64 eigenvalue floor, stated not fitted


def main():
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    cache = json.load(io.open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

    rec("=" * 104)
    rec("b242 COMPONENT 1b -- THE EIGENVALUE FLOOR, TESTED. ### HAZARD H-c OF THE REGISTRATION.")
    rec("=" * 104)
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### h2 UNCHANGED. ### NOTHING DEPOSITS. ### LEFT SIDE ONLY; `A` absent.")
    rec("")

    # ---- where is the floor, per NQ? read from the layer, not assumed
    rec("-" * 104)
    rec("THE FLOOR, READ FROM THE LAYER AT EACH NQ. ### `lam2_n` against the float64 floor %.0e."
        % FLOOR)
    rec("### THE LAST MODE ABOVE THE FLOOR IS THE LAST MODE THAT MEANS ANYTHING.")
    rec("-" * 104)
    rec("  %-6s %-9s %s" % ("NQ", "n_last", "lam2 by mode (n = 0..10)"))
    floors = {}
    for nq in NQ_AXIS:
        x, w, lam, lam2, xi, xi1, an, dan = Q.layer(nq)
        above = [n for n in range(len(lam2)) if lam2[n] > FLOOR]
        n_last = max(above) if above else -1
        floors[nq] = n_last
        rec("  %-6d %-9d %s" % (nq, n_last, " ".join("%.1e" % v for v in lam2)))
    rec("  ### `n_last` IS THE HIGHEST MODE WHOSE EIGENVALUE IS ABOVE THE FLOOR.")
    rec("  ### EVERY MODE PAST IT IS AN EIGENVECTOR OF A NUMERICALLY DEGENERATE EIGENVALUE.")
    rec("")

    # ---- the grid
    rec("=" * 104)
    rec("THE GRID: Tr_full(NMODE, NQ). ### THE PREDICTION UNDER TEST: partial sums up to the")
    rec("### floor are NQ-STABLE; partial sums past it are NOT.")
    rec("=" * 104)

    verdict_rows = []
    for a, alab in B38.CELLS:
        rec("")
        rec("  a^2 = %s" % alab)
        rec("  %-7s %s" % ("NMODE", "".join("%16s" % ("NQ=%d" % nq) for nq in NQ_AXIS)
                           + "%16s" % "spread"))
        for nm in NM_AXIS:
            vals = []
            for nq in NQ_AXIS:
                key = "%s|%d|%d" % (alab, nq, nm)
                if key in cache:
                    vals.append(cache[key])
                else:
                    v, w2, corr, vc, L = B38.family(a)
                    tr = B38.trace_modes(a, corr, vc, L, nq, nm)
                    val = float(np.sum(tr))
                    cache[key] = val
                    json.dump(cache, io.open(CACHE, "w", encoding="utf-8"), indent=1,
                              sort_keys=True)
                    vals.append(val)
            spread = max(vals) - min(vals)
            rec("  %-7d %s%16.3e" % (nm, "".join("%16.9f" % v for v in vals), spread))
            verdict_rows.append((alab, nm, spread))

    # ---- the summary that answers H-c
    rec("")
    rec("=" * 104)
    rec("THE ANSWER TO H-c: NQ-SPREAD AS A FUNCTION OF WHERE THE SUM IS TRUNCATED.")
    rec("=" * 104)
    rec("  %-6s %s" % ("a^2", "".join("%13s" % ("NM=%d" % nm) for nm in NM_AXIS)))
    for a, alab in B38.CELLS:
        row = [s for (c, nm, s) in verdict_rows if c == alab]
        rec("  %-6s %s" % (alab, "".join("%13.3e" % s for s in row)))
    rec("")
    rec("  ### READ THE ROW LEFT TO RIGHT: the NQ-spread of the TRUNCATED trace.")
    rec("  ### A jump at the column where the floor is crossed is the signature H-c predicts.")
    rec("")
    rec("### WHAT THIS RUN DID NOT DO: it derived NO envelope and certified NOTHING; `A` and")
    rec("### every right-side object are absent. ### NOTHING DEPOSITS.")
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
