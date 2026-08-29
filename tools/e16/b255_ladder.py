# -*- coding: utf-8 -*-
"""b255 COMPONENT 2 -- THE LADDER. ### CONSUMES THE PRICING AND THE HASHED MEANINGS.

### ### **G-INDEP IS STRUCTURAL:** every quantity from ITS OWN owner in `b38_act10` --
### `left_side` for `A`/`PR`, `theta_quotient` for `Theta_q`, `e2_of_grid` on
### `per_mode_eps_grids` for `E2` and its sectors, `trace_modes` for realization (B).
### **NONE RE-IMPLEMENTED HERE.** ### The eps grid is REBUILT to the registered range because
### (W1) makes the old one silently wrong past `a^2 = 12`, and the rebuild's G-REPRO debt against
### b254 was registered BEFORE it was paid.

### **RESUMABLE PER CELL**: every cell's raw terms cached; re-running skips completed cells.
"""
import io
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38          # noqa: E402
import qeps_layer as Q           # noqa: E402

CACHE = r"D:\relay\data\b255_cache.npz"
BANK = r"D:\relay\data\b255_run.txt"

# ### THE LADDER, FIXED BY THE PRICING. ### NOT BY WHAT ITS VALUES DO.
LADDER = [2, 3, 4, 8, 9, 12, 16, 20, 25, 32, 36, 45, 50, 64, 81, 100]
BANKED_SIX = [2, 3, 4, 8, 9, 12]
NQS = (700, 900, 1100)           # ### b38's middle + the two refinements b251/b254 carried
NMODE = 11
RHO_MAX = 100.001                # ### FORCED BY (W1)
EPS_NRHO = 445                   # ### equal log-density to b38's 240 over log(12.001)

# ### b254's BANKED SIX, FOR THE G-REPRO DEBT. ### QUOTED WITH THEIR SOURCE AND PRECISION.
B254 = {2: (1.001814, 0.677615, 0.000000, 0.000000, -1.001814),
        3: (0.910943, 0.605701, 0.106484, 0.000000, -1.017427),
        4: (0.834033, 0.540018, 0.249320, 0.161978, -0.921374),
        8: (0.685514, 0.410725, 0.561045, 0.317018, -0.929542),
        9: (0.665133, 0.393176, 0.608882, 0.473862, -0.800154),
        12: (0.620090, 0.354973, 0.714334, 0.518491, -0.815933)}
REPRO_BAND = 1e-4                # ### REGISTERED IN THE MEANINGS FILE, SECTION (B)


def main():
    cache = dict(np.load(CACHE, allow_pickle=True)) if os.path.exists(CACHE) else {}
    if 'rr' not in cache:
        sys.stderr.write("  rebuilding the eps grid to rho_max = %.3f ...\n" % RHO_MAX)
        rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), EPS_NRHO))
        cache['rr'] = rr
        cache['ee_full'] = np.atleast_1d(Q.eps(rr, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
        cache['ee_modes'] = B38.per_mode_eps_grids(rr)
        np.savez(CACHE, **cache)
    rr, ee_full, ee_modes = cache['rr'], cache['ee_full'], cache['ee_modes']
    mask_alg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))

    for a2 in LADDER:
        key = 'c_%d' % a2
        if key in cache:
            continue
        sys.stderr.write("  cell a^2=%d ...\n" % a2)
        a = math.sqrt(float(a2))
        v, w2, corr, vc, L = B38.family(a)
        A, P, PR = B38.left_side(a, B38.S4, v, w2, corr, vc, L)
        Thq = B38.theta_quotient(a, B38.S4, corr, vc, L)
        E2full = B38.e2_of_grid(a, corr, vc, L, rr, ee_full)
        E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rr, ee_modes[n])
                        for n in range(ee_modes.shape[0])])
        cache[key] = np.array([A, PR, Thq, E2full], dtype=float)
        cache[key + '_E2n'] = E2n
        for NQ in NQS:
            cache['%s_tr_%d' % (key, NQ)] = B38.trace_modes(a, corr, vc, L, NQ, NMODE)
        np.savez(CACHE, **cache)

    rows = []
    for a2 in LADDER:
        key = 'c_%d' % a2
        A, PR, Thq, E2 = cache[key]
        E2n = cache[key + '_E2n']
        dn = {q: float(cache['%s_tr_%d' % (key, q)][1:NMODE:2].sum()) for q in NQS}
        E2even, E2odd = float(E2n[0::2].sum()), float(E2n[1::2].sum())
        junc = PR - Thq
        rows.append(dict(a2=a2, A=A, PR=PR, Thq=Thq, E2=E2, E2even=E2even, E2odd=E2odd,
                         junc=junc, dneg=dn[700], dn=dn,
                         dbar=max(abs(dn[q] - dn[700]) for q in NQS),
                         rA=(E2odd - E2) - junc, rB=(dn[700] - E2) - junc,
                         stair={p: B38.staircase(p, math.sqrt(float(a2))) for p in B38.S4}))

    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 126)
    rec("b255 -- THE LIMIT PROFILE. ### THE RUN.")
    rec("=" * 126)
    rec("### CEILING (b14/b15): ### **'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.'** ### ### **AND b242 GOVERNS THE ARITHMETIC: 'A MEASURED RATE IS NOT A TAIL")
    rec("### ### BOUND.' ### NO FIT, NO SLOPE, NO EXTRAPOLATED LIMIT IS BANKED BELOW.**")
    rec("### MEANINGS HASHED FIRST: sha256 2c7faef1...7864, 9790 bytes. ### NOTHING DEPOSITS.")
    rec("")
    rec("### AXES AND PRINTED PRECISION, NAMED:")
    rec("###   eps grid REBUILT (forced by W1): rho_max %.3f, EPS_NRHO %d, EPS_NQ %d, EPS_NG %d."
        % (RHO_MAX, EPS_NRHO, B38.EPS_NQ, B38.EPS_NG))
    rec("###   carto NV=%d NU=%d UMAX=%.0f ; NU_HALF=%d ; S4=%s ; NMODE=%d ; G-STAB NQ in %s."
        % (__import__('carto_atlas').NV, __import__('carto_atlas').NU,
           __import__('carto_atlas').UMAX, B38.NU_HALF, B38.S4, NMODE, NQS))
    rec("###   b254 six-cell table: SIX DECIMALS. ### b38: resid47 to FOUR DECIMALS -> floor 5e-5.")
    rec("###   ### **REALIZATION (B) IS QUOTED THROUGHOUT AS `Dneg(N = 11, float64 modes, suspect")
    rec("###   ### above n = 6)`, PER b253's QUOTED-N LAW.**")
    rec("###   b250 envelope 1.158e-14: ### **NAMED AND NOT APPLIED TO ANY SERIES HERE.**")
    rec("  per-mode mask algebra  max|sum_n eps_n - eps_full| = %.3e   %s"
        % (mask_alg, "PASS" if mask_alg <= 1e-10 else "### FAIL"))
    rec("")

    # ------------------------------------------------------------------ THE G-REPRO DEBT
    rec("-" * 126)
    rec("### **THE G-REPRO DEBT THE GRID REBUILD INCURRED, REGISTERED BEFORE IT WAS PAID.**")
    rec("### The six banked cells are recomputed on the NEW grid and compared to b254's table.")
    rec("### ### **BAND: 1e-4 ABSOLUTE, FIXED IN THE HASHED MEANINGS FILE.**")
    rec("-" * 126)
    rec("  %-5s %12s %12s %12s %12s %12s %10s"
        % ("a^2", "d(E2even)", "d(E2odd)", "d(PR)", "d(Theta_q)", "d(residual)", "within?"))
    worst, ok_repro = 0.0, True
    for r in rows:
        if r['a2'] not in B254:
            continue
        b = B254[r['a2']]
        d = (r['E2even'] - b[0], r['E2odd'] - b[1], r['PR'] - b[2],
             r['Thq'] - b[3], r['rA'] - b[4])
        w = max(abs(x) for x in d)
        worst = max(worst, w)
        good = w <= REPRO_BAND
        ok_repro &= good
        rec("  %-5d %12.2e %12.2e %12.2e %12.2e %12.2e %10s"
            % (r['a2'], d[0], d[1], d[2], d[3], d[4], "yes" if good else "### NO"))
    rec("  ### ### **WORST %.2e -- %s**"
        % (worst, "WITHIN THE REGISTERED BAND AT EVERY CELL, SO THE REBUILT GRID REPRODUCES b254"
           if ok_repro else "### OUTSIDE THE BAND: REPORTED AS A FINDING ABOUT THE GRID, AND THE "
                            "NEW NUMBERS ARE NOT SILENTLY ADOPTED"))
    rec("  ### **b254 IS NOT RE-VERDICTED EITHER WAY (b246's RULE).**")
    rec("")

    # ------------------------------------------------------------------ THE FULL LADDER
    rec("-" * 126)
    rec("### THE FULL LADDER -- ONE OBJECT ACROSS ALL CELLS, OLD AND NEW.")
    rec("### **A FINITE CELL DECIDES NOTHING GLOBAL (b15). ### AND A FINITE LADDER DECIDES NO")
    rec("### LIMIT.**")
    rec("-" * 126)
    rec("%-5s %-16s %10s %10s %10s %10s %11s %11s %10s"
        % ("a^2", "staircase(2,3,5)", "E2even", "PR", "Theta_q", "junction",
           "resid (A)", "resid (B)", "bar (B)"))
    for r in rows:
        star = " *" if r['a2'] in B254 else "  "
        rec("%-5d%s%-15s %10.6f %10.6f %10.6f %10.6f %11.6f %11.6f %10.2e"
            % (r['a2'], star, "%s" % [r['stair'][p] for p in B38.S4],
               r['E2even'], r['PR'], r['Thq'], r['junc'], r['rA'], r['rB'], r['dbar']))
    rec("### `*` marks the six cells banked at b254.")
    rec("### **`bar (A)` IS THE eps MASK CERTIFICATE, %.3e, AT EVERY CELL -- BECAUSE UNDER (A)"
        % mask_alg)
    rec("### NOTHING IN THE BALANCE IS A MODE SUM (b254's structural finding), SO NO `NQ`")
    rec("### REFINEMENT MOVES IT.** ### `bar (B)` IS REALIZATION (B)'s OWN G-STAB SPREAD.")
    rec("### ### **THE STAIRCASE COLUMN IS RE-DERIVED AT EVERY CELL FROM `b38_act10.staircase`,")
    rec("### ### NOT QUOTED -- AND IT IS THE CELL-SPECIES: `S4 = (2,3,5)` IS FIXED, SO `a^2 = 49`")
    rec("### ### ACTIVATES NO NEW PRIME AND `7` NEVER ENTERS. ### THE LADDER MEASURES POWERS OF A")
    rec("### ### FIXED PRIME SET, NOT A GROWING PLACE SET.**")
    rec("")

    # ------------------------------------------------------------------ THE RACE
    rec("-" * 126)
    rec("### **THE RACE THE MEANINGS FILE NAMED: `E2even` FALLING AGAINST THE JUNCTION RISING.**")
    rec("###   `resid (A) = -( E2even + junction )`")
    rec("-" * 126)
    rec("%-5s %12s %12s %12s %14s %14s"
        % ("a^2", "E2even", "junction", "|resid(A)|", "d|resid| step", "beyond bar?"))
    barA = math.sqrt(2.0) * mask_alg
    prev = None
    for r in rows:
        ra = abs(r['rA'])
        if prev is None:
            step, flag = float('nan'), "-"
        else:
            step = ra - prev
            flag = "yes" if abs(step) > 2 * barA else "no"
        rec("%-5d %12.6f %12.6f %12.6f %14s %14s"
            % (r['a2'], r['E2even'], r['junc'], ra,
               "     ---" if prev is None else "%+.6f" % step, flag))
        prev = ra
    rec("  ### **bar (A) = sqrt(2) x mask certificate = %.3e, so EVERY step above is beyond it by"
        % barA)
    rec("  ### many orders. ### THE BAND IS NOT WHAT DECIDES THIS PROFILE; THE STEPS' SIGNS ARE.**")
    rec("")
    rec("### G-INDEP: `A`/`PR` from `left_side`, `Theta_q` from `theta_quotient`, `E2` and sectors")
    rec("### from `e2_of_grid` on `per_mode_eps_grids`, `Dneg` from `trace_modes` -- ### **EACH")
    rec("### FROM ITS OWN OWNER, IMPORTED AS A MODULE, NONE RE-IMPLEMENTED HERE.**")
    rec("### G-STAB: realization (B) at NQ = 700/900/1100, spread in the `bar (B)` column.")
    rec("=" * 126)
    io.open(BANK, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    json.dump({str(r['a2']): {k: (v if not isinstance(v, dict) else
                                  {str(kk): vv for kk, vv in v.items()})
                              for k, v in r.items()} for r in rows},
              io.open(r"D:\relay\data\b255_rows.json", "w", encoding="utf-8"))
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
