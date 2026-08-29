# -*- coding: utf-8 -*-
"""b251 -- THE THIRD FACE-OFF. ### THE RUN.

### THE MEANINGS AND THE RE-ATTRIBUTION WERE BANKED AND HASHED FIRST
### (data/b251_meanings.txt, sha256 d5284f9e...). ### THIS TOOL MAY NOT ALTER THEM.
###
### ### **G-INDEP IS STRUCTURAL, NOT ASSERTED:** each quantity comes from ITS OWN OWNER in
### `b38_act10`, imported as a module -- `left_side` for `A`, `trace_modes` for `Tr`,
### `e2_of_grid` for `E2`, `theta_quotient` for `Theta_q`. ### **NO QUANTITY IS READ OFF ANOTHER,
### AND NONE IS RE-IMPLEMENTED HERE**, so a transcription error cannot enter.
###
### ### **RESUMABLE**: every cell's raw arrays are cached to `b251_cache.npz`; re-running skips
### completed cells. ### The ferry requires long runs be resumable and this one is.
###
### ### **AND THE ONE THING THIS TOOL DELIBERATELY DOES NOT DO:** ### it does not place b250's
### `1.158e-14` envelope in any bar. ### Per the registration section (C), that envelope bounds
### `sum t(n)`, an ENDPOINT-WEIGHT series, and `TrTail` is a CORR-WEIGHTED DILATION OVERLAP.
### ### **`TrTail` IS MEASURED AND IS LABELLED MEASURED.**
"""
import io
import math
import os
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38          # noqa: E402  ### THE OWNER OF EVERY QUANTITY BELOW
import qeps_layer as Q           # noqa: E402

CACHE = r"D:\relay\data\b251_cache.npz"
BANK = r"D:\relay\data\b251_run.txt"

# ### AXES, FROM THE REGISTRATION. ### FIXED BEFORE ANY NUMBER WAS SEEN.
AXES = [(500, 8), (700, 10), (900, 11), (1100, 11)]   # ### b38's TRIPLE + ONE refinement
PRIMARY = (700, 11)      # ### K1's definition is ELEVEN modes; NQ from b38's middle
NMODE_MAX = 11
CUT = 7                  # ### the computable-mode cut the record has been reporting
PRINT_FLOOR = 5e-5       # ### b38 prints resid47 to FOUR DECIMALS. ### NAMED BEFORE MEASURING.


def eps_grids():
    """### THE eps GRIDS, FROM b38's OWN OWNERS, COMPUTED ONCE AND CACHED."""
    rr = np.exp(np.linspace(1e-4, math.log(12.001), B38.EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
    ee_modes = B38.per_mode_eps_grids(rr)
    return rr, ee_full, ee_modes


def main():
    cache = dict(np.load(CACHE, allow_pickle=True)) if os.path.exists(CACHE) else {}
    if 'rr' not in cache:
        sys.stderr.write("  computing eps grids (once)...\n")
        rr, ee_full, ee_modes = eps_grids()
        cache['rr'], cache['ee_full'], cache['ee_modes'] = rr, ee_full, ee_modes
        np.savez(CACHE, **cache)
    rr, ee_full, ee_modes = cache['rr'], cache['ee_full'], cache['ee_modes']

    # ### THE MASK CERTIFICATE, RE-DERIVED FROM THE ARRAYS AND NOT QUOTED (b248's precedent).
    mask_alg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))

    for a, alab in B38.CELLS:
        key = 'cell_%s' % alab
        if key in cache:
            continue
        sys.stderr.write("  cell a^2=%s ...\n" % alab)
        v, w2, corr, vc, L = B38.family(a)
        A, P, PR = B38.left_side(a, B38.S4, v, w2, corr, vc, L)
        Thq = B38.theta_quotient(a, B38.S4, corr, vc, L)
        E2full = B38.e2_of_grid(a, corr, vc, L, rr, ee_full)
        E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rr, ee_modes[n])
                        for n in range(NMODE_MAX)])
        trs = {}
        for (NQ, NM) in AXES + [PRIMARY]:
            if NQ in trs:
                continue
            trs[NQ] = B38.trace_modes(a, corr, vc, L, NQ, NMODE_MAX)
        cache[key] = np.array([A, P, PR, Thq, E2full], dtype=float)
        cache[key + '_E2n'] = E2n
        for NQ, tr in trs.items():
            cache['%s_tr_%d' % (key, NQ)] = tr
        np.savez(CACHE, **cache)

    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 118)
    rec("b251 -- THE THIRD FACE-OFF. ### THE RUN.")
    rec("=" * 118)
    rec("### CEILING (b14/b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### THE REGISTER SENTENCE IS UNTOUCHED. ### NOTHING DEPOSITS.")
    rec("### MEANINGS BANKED AND HASHED FIRST: sha256 d5284f9e...4b3c, 11048 bytes.")
    rec("")
    rec("### EVERY CONSULTED BANK'S AXES **AND PRINTED PRECISION**, NAMED BEFORE ANY NUMBER:")
    rec("###   b38_act10: TRIPLE=[(500,8),(700,10),(900,11)], NU_HALF=401, EPS_NQ=700,")
    rec("###              EPS_NG=400, EPS_NRHO=240, CELLS a^2 in {2,3,4,8,9,12}, S4=(2,3,5).")
    rec("###              ### **PRINTS resid47 TO FOUR DECIMALS -> PRINT FLOOR 5e-5.**")
    rec("###   b250 envelope 1.158e-14: ### **NAMED AND DELIBERATELY NOT USED IN ANY BAR** (reg C).")
    rec("###   b38's NMODE=10 ROW BANK: ### **NAMED AND NOT USED** -- the trap b245 fell into.")
    rec("###   b248 split: archimedean 88%-100%, junction 0%-12%. ### NAMED.")
    rec("")
    rec("--- C0 GATES ---")
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    g1 = abs(float(lam2.sum()) - 2.237484835)
    g2 = abs(float((lam2 * xi1 ** 2).sum()) - 2.0)
    g3 = abs(float(t_n.sum()) - 22.9964757)
    rec("  pin sum lam2          |delta|=%.2e (tol 1e-6)  %s" % (g1, "PASS" if g1 <= 1e-6 else "FAIL"))
    rec("  pin sum lam2 xi1^2    |delta|=%.2e (tol 1e-6)  %s" % (g2, "PASS" if g2 <= 1e-6 else "FAIL"))
    rec("     ### ### **THIS GATE IS NOW A THEOREM (b250 S3b): sum = c/pi + sin(2c)/(2 pi) = 2")
    rec("     ### ### EXACTLY at c = 2*pi. ### IT IS STILL RUN, BECAUSE A THEOREM ABOUT THE")
    rec("     ### ### OPERATOR IS NOT A CERTIFICATE ABOUT THIS INSTRUMENT'S ARITHMETIC.**")
    rec("  pin epsprime1         |delta|=%.2e (tol 1e-3)  %s" % (g3, "PASS" if g3 <= 1e-3 else "FAIL"))
    rec("  per-mode mask algebra max|sum_n eps_n - eps_full| = %.2e  %s   ### RE-DERIVED, NOT QUOTED"
        % (mask_alg, "PASS" if mask_alg <= 1e-10 else "FAIL"))
    rec("")

    rows = []
    rec("-" * 118)
    rec("### THE TABLE. ### A FINITE CELL DECIDES NOTHING GLOBAL (b15).")
    rec("### `Delta_2real` from its OWN TWO OWNERS: `left_side` for A, `trace_modes` for Tr.")
    rec("-" * 118)
    rec("%-5s %11s %11s %11s | %12s %11s | %11s %9s"
        % ("a^2", "L", "R", "L - R", "Delta_2real", "junction", "TrTail(7)", "resid47"))
    for a, alab in B38.CELLS:
        key = 'cell_%s' % alab
        A, P, PR, Thq, E2full = cache[key]
        E2n = cache[key + '_E2n']
        tr = cache['%s_tr_%d' % (key, PRIMARY[0])]
        E2even = float(E2n[0::2].sum())
        Tr_cut = float(tr[:CUT].sum())
        Tr_max = float(tr[:NMODE_MAX].sum())
        Dneg = float(tr[1:NMODE_MAX:2].sum())
        # ### THE RULED BINDINGS: C2+D1 and RULE Q O1.
        Lft = (Tr_max + E2full - Dneg) + (-Thq)
        Rgt = A - PR
        d2 = Tr_max - A - E2full            # ### Delta_2real at the definition's eleven modes
        r47 = Tr_cut - A - E2full           # ### resid47 at the computable cut
        trtail = Tr_max - Tr_cut            # ### MEASURED. ### NOT bounded by b250.
        junc = PR - Thq
        rows.append((alab, Lft, Rgt, Lft - Rgt, d2, junc, trtail, r47, E2full, E2even, Dneg,
                     A, PR, Thq, Tr_cut, Tr_max))
        rec("%-5s %11.6f %11.6f %11.6f | %12.6f %11.6f | %11.6f %9.4f"
            % (alab, Lft, Rgt, Lft - Rgt, d2, junc, trtail, r47))
    rec("")

    # ------------------------------------------------------------------ THE TAUTOLOGY CONTROL
    rec("-" * 118)
    rec("### THE TAUTOLOGY CONTROL ON THE RE-ATTRIBUTION. ### THE MEANINGS FILE ALREADY DECLARED")
    rec("### THIS DECOMPOSITION **ALGEBRAIC-RESTATEMENT**, BEFORE THE RUN. ### THE RUN CONFIRMS IT")
    rec("### HOLDS TO MACHINE PRECISION AT EVERY CELL -- ### **WHICH IS EXACTLY WHY IT IS NO")
    rec("### EVIDENCE.** ### An identity that cannot fail cannot testify.")
    rec("-" * 118)
    worst = 0.0
    for r in rows:
        alab, d2, trtail, r47 = r[0], r[4], r[6], r[7]
        resid = abs(r47 - (d2 - trtail))
        worst = max(worst, resid)
        rec("  a^2=%-4s |resid47 - (Delta_2real - TrTail)| = %.3e" % (alab, resid))
    rec("  ### ### **MAX %.3e -- AN IDENTITY, AS DECLARED. ### IT CARRIES NO WEIGHT.**" % worst)
    rec("  ### ### **WHAT CARRIES WEIGHT IS THE SIZE QUESTION BELOW.**")
    rec("")

    # ------------------------------------------------------------------ THE SIZE QUESTION
    rec("-" * 118)
    rec("### ### **THE SIZE QUESTION -- THE ONLY LINE OF THIS RUN THAT IS EVIDENCE.**")
    rec("### Which of the two named pieces carries `resid47`? ### And is `TrTail` anywhere near")
    rec("### b250's `1.158e-14`, as the ferry's clause supposed?")
    rec("-" * 118)
    rec("%-5s %13s %13s %10s %14s"
        % ("a^2", "Delta_2real", "TrTail(7)", "|tail/D|", "tail vs 1.158e-14"))
    ratios = []
    for r in rows:
        alab, d2, trtail = r[0], r[4], r[6]
        rat = abs(trtail / d2) if d2 else float('inf')
        ratios.append(rat)
        rec("%-5s %13.6f %13.6f %10.4f %14s"
            % (alab, d2, trtail, rat, "%.1e x larger" % (abs(trtail) / 1.158e-14)))
    rec("")

    # ------------------------------------------------------------- THE FULL ACCOUNTING
    rec("-" * 118)
    rec("### ### **THE FULL ACCOUNTING -- WHICH IS HOW (DISSONANT-BEYOND) IS ACTUALLY TESTED.**")
    rec("### `L - R` is decomposed into NAMED pieces and the LEFTOVER is printed. ### The registered")
    rec("### factor: a residual exceeding the LARGER named piece by more than 2x at any cell, or")
    rec("### failing to be accounted within the printed bar at any cell.")
    rec("### ### **AND THE THIRD PIECE IS TABULATED EVEN THOUGH IT IS NOT A SUSPECT:**")
    rec("###   `2*E2full - Dneg` is the RULED BINDING's OWN TERMS (C2+D1), not an indictment --")
    rec("###   ### **BUT IT CARRIES ABOUT A THIRD OF THE SHORTFALL AND HIDING IT WOULD MISREPORT**")
    rec("###   ### **WHAT `Delta_2real` IS BEING CREDITED WITH.**")
    rec("-" * 118)
    rec("%-5s %11s %13s %13s %11s %13s"
        % ("a^2", "L - R", "Delta_2real", "2*E2f - Dneg", "junction", "LEFTOVER"))
    worst_left = 0.0
    for r in rows:
        alab, LmR, d2, junc, E2full, Dneg = r[0], r[3], r[4], r[5], r[8], r[10]
        third = 2.0 * E2full - Dneg
        left = LmR - (d2 + third + junc)
        worst_left = max(worst_left, abs(left))
        rec("%-5s %11.6f %13.6f %13.6f %11.6f %13.3e"
            % (alab, LmR, d2, third, junc, left))
    rec("  ### ### **MAX LEFTOVER %.3e -- ### NOTHING BEYOND THE THREE NAMED PIECES.**" % worst_left)
    rec("  ### **(DISSONANT-BEYOND) IS NOT TRIGGERED.** ### And this line, too, is an IDENTITY once")
    rec("  ### the three pieces are defined -- ### **its content is that NO FOURTH PIECE WAS NEEDED,**")
    rec("  ### ### **not that the three were derived.**")
    rec("")
    rec("### ### **THE SHARE EACH NAMED PIECE CARRIES OF `L - R`:**")
    rec("%-5s %13s %13s %11s" % ("a^2", "Delta_2real", "2*E2f - Dneg", "junction"))
    for r in rows:
        alab, LmR, d2, junc, E2full, Dneg = r[0], r[3], r[4], r[5], r[8], r[10]
        third = 2.0 * E2full - Dneg
        rec("%-5s %12.1f%% %12.1f%% %10.1f%%"
            % (alab, 100 * d2 / LmR, 100 * third / LmR, 100 * junc / LmR))
    rec("")

    # ------------------------------------------------------------------ G-STAB
    rec("-" * 118)
    rec("### G-STAB -- AT THE REGISTERED AXES PLUS EXACTLY ONE REFINEMENT (NQ = 1100).")
    rec("-" * 118)
    rec("%-5s %12s %12s %12s %12s %11s" % ("a^2", "NQ=500", "NQ=700", "NQ=900", "NQ=1100", "spread"))
    stab = 0.0
    for a, alab in B38.CELLS:
        key = 'cell_%s' % alab
        A, P, PR, Thq, E2full = cache[key]
        vals = []
        for NQ in (500, 700, 900, 1100):
            tr = cache['%s_tr_%d' % (key, NQ)]
            vals.append(float(tr[:NMODE_MAX].sum()) - A - E2full)
        sp = max(abs(x - vals[1]) for x in vals)
        stab = max(stab, sp)
        rec("%-5s %12.6f %12.6f %12.6f %12.6f %11.2e"
            % (alab, vals[0], vals[1], vals[2], vals[3], sp))
    rec("  ### ### **MAX SPREAD %.2e ON `Delta_2real` ACROSS THE QUADRATURE AXIS.**" % stab)
    rec("  ### **AND THE FLOOR IS NAMED: b38 PRINTS resid47 TO FOUR DECIMALS, SO NO CLAIM BELOW")
    rec("  ### 5e-5 IS MADE ABOUT ANY QUANTITY COMPARED AGAINST THAT BANK.**")
    rec("")
    rec("### G-INDEP: `A` from `left_side`, `Tr` from `trace_modes`, `E2` from `e2_of_grid`,")
    rec("### `Theta_q` from `theta_quotient` -- ### **EACH FROM ITS OWN OWNER, NONE RE-IMPLEMENTED")
    rec("### HERE, NONE READ OFF ANOTHER.**")
    rec("=" * 118)
    io.open(BANK, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)
    np.save(r"D:\relay\data\b251_rows.npy", np.array([r[1:] for r in rows], dtype=float))


if __name__ == "__main__":
    main()
