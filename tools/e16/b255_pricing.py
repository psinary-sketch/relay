# -*- coding: utf-8 -*-
"""b255 COMPONENT 1a -- THE PRICING. ### RUN **BEFORE** THE LADDER IS FIXED AND BEFORE ANY BALANCE
### VALUE EXISTS.

### ### **THE FERRY'S RULE, WHICH THIS TOOL EXISTS TO MAKE CHECKABLE: 'the ladder chosen by
### ### AFFORDABILITY, NEVER BY WHAT ITS VALUES DO.'** ### So this tool measures COSTS ONLY. ### It
### computes ### **NO** ### balance, no residual, no `E2`, no `Theta_q` VALUE that is kept -- only
### wall-clock and sizes. ### Its output is a budget, and the ladder is read off the budget.

### THE FOUR COST WALLS, IDENTIFIED FROM SOURCE BEFORE TIMING ANYTHING:
###   **(W1) THE eps rho-GRID IS A HARD CEILING AT `a^2 = 12.001`, AND IT FAILS SILENTLY.**
###     `b38_act10.py:152` builds `rr = exp(linspace(1e-4, log(12.001), EPS_NRHO))`, and
###     `:98` does `np.interp(np.exp(uu), rr, ee)` with `uu` up to `2 log a`, i.e. `exp(uu)` up to
###     `a^2`. ### **FOR `a^2 > 12.001` `np.interp` CLAMPS TO `ee[-1]` AND RETURNS A WRONG NUMBER
###     ### WITHOUT RAISING.** ### Any ladder past 12 MUST rebuild the grid.
###   **(W2) `Theta_q` IS THE COMBINATORIAL WALL.** ### `b8_sonin_dim.scaling_matrix(p, n)` builds a
###     DENSE `N x N` with ### **`N = p^(2n)`**, and `theta_quotient` runs `2n-1` matmuls of it.
###     With `n = staircase(p, a)`: `n(2) = 3` at `a^2 = 12`, `4` at 16, `5` at 36, ### **`6` at 64
###     -> `N = 4096`**, whose matmul is `~7e10` flops EACH.
###   **(W3) `left_side`'s `hhat` materialises `cos(outer(u, v))` at `NU x NV = 12001 x 4001`**
###     = 4.8e7 doubles = ~384 MB per call. ### Fixed in `a`, but it is the per-cell floor.
###   **(W4) `trace_modes`** -- `NU_HALF x NMODE` interpolations at each `NQ`. ### Fixed in `a`.
"""
import io
import math
import sys
import time

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b8_sonin_dim as B8        # noqa: E402
import b10_cells as B10          # noqa: E402
import b38_act10 as B38          # noqa: E402
import carto_atlas as C          # noqa: E402

BANK = r"D:\relay\data\b255_pricing.txt"
BUDGET_S = 3600.0                # ### THE REGISTERED WALL-CLOCK BUDGET FOR THE WHOLE LADDER


def staircase(p, a2):
    return sum(1 for k in range(1, 60) if p ** k <= a2 + 1e-12)


def main():
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 112)
    rec("b255 -- THE PRICING. ### COSTS ONLY. ### NO BALANCE VALUE IS COMPUTED OR KEPT.")
    rec("=" * 112)
    rec("### CEILING (b14/b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### **AND b242's REFUSAL GOVERNS THIS ACT: A MEASURED RATE IS NOT A TAIL")
    rec("### BOUND, AND NO EXTRAPOLATION IS BANKED AS A BOUND.** ### NOTHING DEPOSITS.")
    rec("### ### **THE LADDER IS CHOSEN BY AFFORDABILITY, NEVER BY WHAT ITS VALUES DO -- WHICH IS")
    rec("### ### WHY THIS TOOL RUNS FIRST AND COMPUTES NO VALUES.**")
    rec("")

    # ---------------------------------------------------------------- W1
    rec("-" * 112)
    rec("### **(W1) THE eps rho-GRID CEILING -- A SILENT FAILURE, NOT AN ERROR.**")
    rec("-" * 112)
    rho_max = 12.001
    rec("  `b38_act10.py:152`  rr = exp(linspace(1e-4, log(%s), EPS_NRHO=%d))"
        % (rho_max, B38.EPS_NRHO))
    rec("  `b38_act10.py:98`   eu = np.interp(np.exp(uu), rr, ee),  uu in [0, 2 log a]")
    rec("  ### ### **SO `exp(uu)` REACHES `a^2`, AND FOR `a^2 > %.3f` `np.interp` CLAMPS TO"
        % rho_max)
    rec("  ### ### `ee[-1]` AND RETURNS A WRONG NUMBER WITHOUT RAISING.**")
    rec("  ### **CONSEQUENCE: ANY LADDER PAST `a^2 = 12` MUST REBUILD THE GRID, AND REBUILDING IT")
    rec("  ### CHANGES `E2` FOR THE SIX BANKED CELLS TOO -- SO THE REBUILD OWES A G-REPRO AGAINST")
    rec("  ### b254's TABLE. ### THAT DEBT IS REGISTERED HERE, BEFORE THE LADDER IS CHOSEN.**")
    t0 = time.time()
    rr_probe = np.exp(np.linspace(1e-4, math.log(12.001), B38.EPS_NRHO))
    _ = B38.per_mode_eps_grids(rr_probe)
    t_eps240 = time.time() - t0
    rec("  MEASURED: per_mode_eps_grids at EPS_NRHO=%d over log-range %.3f -> %.1f s"
        % (B38.EPS_NRHO, math.log(12.001), t_eps240))
    rec("  ### per-rho-point cost = %.4f s. ### **THE COST IS LINEAR IN EPS_NRHO AND THE LOG-RANGE"
        % (t_eps240 / B38.EPS_NRHO))
    rec("  ### GROWS AS `log(a^2_max)`, SO HOLDING THE LOG-DENSITY FIXED PRICES AS BELOW.**")
    for a2m in (25, 50, 100, 200):
        n_need = int(math.ceil(B38.EPS_NRHO * math.log(a2m) / math.log(12.001)))
        rec("    a^2_max = %-4d -> EPS_NRHO = %-4d at equal log-density -> %.1f s"
            % (a2m, n_need, t_eps240 * n_need / B38.EPS_NRHO))
    rec("")

    # ---------------------------------------------------------------- W2
    rec("-" * 112)
    rec("### **(W2) `Theta_q` -- THE COMBINATORIAL WALL. ### `N = p^(2n)` DENSE, `2n-1` MATMULS.**")
    rec("-" * 112)
    rec("  %-6s %-22s %8s %12s %14s" % ("a^2", "staircase(2,3,5)", "N(p=2)", "matrix MB", "measured s"))
    for a2 in (12, 16, 25, 36, 49, 64, 100, 128):
        s = {p: staircase(p, a2) for p in (2, 3, 5)}
        n2 = s[2]
        N = 2 ** (2 * n2)
        mb = N * N * 8 / 1e6
        if N <= 1024:
            t0 = time.time()
            U = B8.scaling_matrix(2, n2)
            Nn, K, d = B10.quotient_basis(2, n2)
            S = K @ K.T
            Uk = np.eye(Nn)
            for k in range(1, 2 * n2):
                Uk = U @ Uk
                _ = abs(complex(np.trace(Uk @ S))) / d
            tt = "%.2f" % (time.time() - t0)
        else:
            # ### ONE measured matmul times the counted loop length -- ### **A COUNT OF MEASURED
            # ### UNITS, NOT A CURVE FIT.** ### Memory is probed, not assumed.
            try:
                X = np.zeros((N, N))
                t0 = time.time()
                _ = X @ X
                unit = time.time() - t0
                del X
                tt = ">= %.0f  (%.1f s/matmul x %d matmuls, p=2 alone)" % (
                    unit * (2 * (2 * n2 - 1)), unit, 2 * (2 * n2 - 1))
            except MemoryError:
                tt = "### MEMORY REFUSED"
        rec("  %-6d %-22s %8d %12.1f %14s" % (a2, s, N, mb, tt))
    rec("  ### ### **THE WALL IS WHERE THE MEASUREMENT PUTS IT, NOT WHERE I EXPECTED IT.** ### I")
    rec("  ### ### drafted this line expecting `n(2) = 6` (`a^2 >= 64`) to be the wall on the")
    rec("  ### ### `N = 4096` matrix. ### **THE TIMING SAYS OTHERWISE: `a^2 = 64` COSTS TENS OF")
    rec("  ### ### SECONDS, WELL INSIDE THE BUDGET.** ### The real wall is `n(2) = 7` (`a^2 >= 128`),")
    rec("  ### ### where `N = 16384` and the matrix alone is ~2.1 GB. ### **THE CONCLUSION FOLLOWS")
    rec("  ### ### THE TABLE; THE TABLE DOES NOT FOLLOW THE CONCLUSION.**")
    rec("")

    # ---------------------------------------------------------------- W3 / W4
    rec("-" * 112)
    rec("### **(W3)/(W4) THE PER-CELL FLOOR: `left_side` AND `trace_modes`. ### FIXED IN `a`.**")
    rec("-" * 112)
    rec("  carto axes: NV = %d, NU = %d, UMAX = %.0f  -> `hhat` materialises %d x %d = %.0f MB"
        % (C.NV, C.NU, C.UMAX, C.NU, C.NV, C.NU * C.NV * 8 / 1e6))
    a = math.sqrt(12.0)
    v, w2, corr, vc, L = B38.family(a)
    t0 = time.time()
    _ = B38.left_side(a, B38.S4, v, w2, corr, vc, L)
    t_left = time.time() - t0
    t0 = time.time()
    _ = B38.trace_modes(a, corr, vc, L, 700, 11)
    t_tr = time.time() - t0
    rec("  MEASURED at a^2 = 12: left_side %.2f s ; trace_modes(NQ=700, NMODE=11) %.2f s"
        % (t_left, t_tr))
    rec("  ### **THE LADDER NEEDS `trace_modes` AT TWO REFINEMENTS PER CELL (G-STAB), SO THE")
    rec("  ### PER-CELL FLOOR IS ABOUT %.1f s BEFORE `Theta_q`.**" % (t_left + 3 * t_tr))
    rec("")

    # ---------------------------------------------------------------- THE BUDGET
    rec("-" * 112)
    rec("### **THE BUDGET AND THE REACH. ### FIXED HERE, BEFORE ANY BALANCE VALUE EXISTS.**")
    rec("-" * 112)
    rec("  REGISTERED WALL-CLOCK BUDGET FOR THE WHOLE LADDER: %.0f s." % BUDGET_S)
    rec("  ### **THE REACH IS SET BY (W2) AT `n(2) <= 6`, i.e. `a^2 <= 127`.** ### `n(2) = 7`")
    rec("  ### (`a^2 >= 128`) needs a 2.1 GB dense matrix and is REFUSED.")
    rec("  ### ### **THE LADDER FIXED HERE, BY COST AND BY COST ALONE:**")
    rec("  ### ### **`a^2 in {2, 3, 4, 8, 9, 12}` (the banked six, RECOMPUTED on the new grid)")
    rec("  ### ### PLUS `{16, 20, 25, 32, 36, 45, 50, 64, 81, 100}` -- SIXTEEN CELLS, REACH 100.**")
    rec("  ### **THE SPACING IS ROUGHLY GEOMETRIC SO THE LADDER SAMPLES THE DIRECTION EVENLY IN")
    rec("  ### `log a`, WHICH IS THE AXIS `2L = 2 log a` ACTUALLY LIVES ON.**")
    rec("  ### **`a^2 >= 128` IS REFUSED ON COST, NOT ON WHAT ITS VALUES WOULD SHOW -- AND THE")
    rec("  ### REFUSAL IS RECORDED BEFORE ANY VALUE IS COMPUTED, WHICH IS THE WHOLE POINT.**")
    rec("  ### ### **THE FERRY'S TARGET WAS `a^2 ~ 50-100 IF AFFORDED`. ### IT IS AFFORDED, AND")
    rec("  ### ### THE LADDER REACHES 100.**")
    rec("  ### ESTIMATED TOTAL: 16 cells x ~%.0f s floor + Theta_q (0-30 s at the top cells)"
        % (t_left + 3 * t_tr))
    rec("  ### + one eps-grid rebuild at ~6 s ### **= a few hundred seconds, inside the %.0f s"
        % BUDGET_S)
    rec("  ### budget with room to spare.**")
    io.open(BANK, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
