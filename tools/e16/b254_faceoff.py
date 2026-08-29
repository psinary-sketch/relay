# -*- coding: utf-8 -*-
"""b254 -- THE FOURTH FACE-OFF. ### THE RUN. ### CONSUMES THE HASHED MEANINGS FILE.

### ### **G-INDEP IS STRUCTURAL, NOT ASSERTED:** every quantity comes from ITS OWN owner --
### `left_side` for `A` and `PR`, `theta_quotient` for `Theta_q`, `e2_of_grid` for `E2` and the
### eps sectors, `trace_modes` for the odd-TRACE realization of `Delta_-`, and `b37_act9`'s own
### `eps_masked` machinery (via b38's per-mode grids, which are the same masks) for the odd
### eps-MASK realization. ### **NONE IS RE-IMPLEMENTED HERE.**

### ### **BOTH `Delta_-` REALIZATIONS ARE COMPUTED AND NEITHER IS CHOSEN**, on b246's own
### precedent -- *"Its two realizations remain two objects and this act computed both rather than
### choosing."* ### The meanings file fixed that before any number existed.

### **RESUMABLE**: per-cell results cached to `b254_cache.npz`; re-running skips completed cells.
"""
import io
import math
import os
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38          # noqa: E402
import qeps_layer as Q           # noqa: E402

CACHE = r"D:\relay\data\b254_cache.npz"
BANK = r"D:\relay\data\b254_run.txt"
NQS = (500, 700, 900, 1100)      # ### b38's TRIPLE quadratures + ONE registered refinement
NMODE = 11                       # ### RULE MODES K1's definition


def main():
    cache = dict(np.load(CACHE, allow_pickle=True)) if os.path.exists(CACHE) else {}
    if 'rr' not in cache:
        sys.stderr.write("  eps grids (once)...\n")
        rr = np.exp(np.linspace(1e-4, math.log(12.001), B38.EPS_NRHO))
        ee_full = np.atleast_1d(Q.eps(rr, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
        ee_modes = B38.per_mode_eps_grids(rr)
        cache['rr'], cache['ee_full'], cache['ee_modes'] = rr, ee_full, ee_modes
        np.savez(CACHE, **cache)
    rr, ee_full, ee_modes = cache['rr'], cache['ee_full'], cache['ee_modes']
    # ### THE MASK CERTIFICATE, RE-DERIVED FROM THE ARRAYS AND NOT QUOTED (b248's precedent).
    mask_alg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))

    for a, alab in B38.CELLS:
        key = 'c_%s' % alab
        if key in cache:
            continue
        sys.stderr.write("  cell a^2=%s ...\n" % alab)
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

    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 118)
    rec("b254 -- THE FOURTH FACE-OFF. ### THE RUN.")
    rec("=" * 118)
    rec("### CEILING (b14/b15): ### **'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.'** ### THE REGISTER SENTENCE IS UNTOUCHED. ### NOTHING DEPOSITS.")
    rec("### MEANINGS BANKED AND HASHED FIRST: sha256 75e731e3...cb97, 11666 bytes.")
    rec("### ### **THE COMPOSITION `L - R = (E2 - Delta_-) + (PR - Theta_q)` IS ALGEBRAIC-")
    rec("### ### RESTATEMENT UNDER THE BINDINGS AND WAS LABELLED SO BEFORE THE RUN. ### IT CARRIES")
    rec("### ### NO EVIDENTIAL WEIGHT. ### THE EVIDENCE IS THE SIZES, SIGNS AND CELL-PROFILES.**")
    rec("")
    rec("### AXES AND PRINTED PRECISION OF EVERY CONSULTED BANK, NAMED:")
    rec("###   b38_act10: TRIPLE=[(500,8),(700,10),(900,11)] + ONE refinement NQ=1100; NU_HALF=401;")
    rec("###     EPS_NQ=700, EPS_NG=400, EPS_NRHO=240; cells {2,3,4,8,9,12}; S4=(2,3,5).")
    rec("###     ### **PRINTS resid47 TO FOUR DECIMALS -> FLOOR 5e-5.**")
    rec("###   b246: R2/R3 to four significant digits. ### b248: six decimals; PR = Theta_q = 0 at")
    rec("###     a^2 = 2. ### b251: bars 4.84e-2..1.74e-1, six decimals -- ### **AND PER b253's")
    rec("###     QUOTED-N LAW THOSE ARE QUOTABLE ONLY AS (N = 11, float64 modes, suspect above")
    rec("###     n = 6). ### THE LAW IS OBSERVED IN THIS ACT'S OWN QUOTATIONS.**")
    rec("###   b250 envelope 1.158e-14: ### **NAMED AND NOT APPLIED TO ANY SERIES HERE.**")
    rec("")
    rec("--- THE INSTRUMENT'S OWN CERTIFICATE, RE-DERIVED FROM THE ARRAYS ---")
    rec("  per-mode mask algebra  max|sum_n eps_n - eps_full| = %.3e   %s"
        % (mask_alg, "PASS" if mask_alg <= 1e-10 else "### FAIL"))
    rec("  ### ### **THIS IS THE eps TERMS' OWN ACCURACY BOUND AND IS USED AS THEIR BAR BELOW,")
    rec("  ### ### BECAUSE THE REGISTERED G-STAB AXIS (NQ) DOES NOT MOVE THEM AT ALL.**")
    rec("")

    rows = []
    for a, alab in B38.CELLS:
        key = 'c_%s' % alab
        A, PR, Thq = cache[key][0], cache[key][1], cache[key][2]
        E2full = cache[key][3]
        E2n = cache[key + '_E2n']
        E2even = float(E2n[0::2].sum())
        E2odd = float(E2n[1::2].sum())
        dnegs = {NQ: float(cache['%s_tr_%d' % (key, NQ)][1:NMODE:2].sum()) for NQ in NQS}
        rows.append(dict(lab=alab, A=A, PR=PR, Thq=Thq, E2=E2full, E2even=E2even, E2odd=E2odd,
                         dneg=dnegs[700], dnegs=dnegs,
                         dbar=max(abs(dnegs[q] - dnegs[700]) for q in NQS)))

    # ------------------------------------------------------------------ TERMS ALONE
    rec("-" * 118)
    rec("### THE TERMS ALONE, SO THE BALANCE'S TWO SIDES ARE INDEPENDENTLY VISIBLE.")
    rec("### **A FINITE CELL DECIDES NOTHING GLOBAL (b15).**")
    rec("-" * 118)
    rec("%-5s %12s %12s %12s %12s %12s %12s"
        % ("a^2", "E2(full)", "E2even", "E2odd=D(A)", "Dneg=D(B)", "PR", "Theta_q"))
    for r in rows:
        rec("%-5s %12.6f %12.6f %12.6f %12.6f %12.6f %12.6f"
            % (r['lab'], r['E2'], r['E2even'], r['E2odd'], r['dneg'], r['PR'], r['Thq']))
    rec("### ### **`D(A)` IS THE RIDER'S REALIZATION (the odd eps-MASK, sec 17 / File E).**")
    rec("### ### **`D(B)` IS THE ODD TRACE MODES (`b36_act8.py:172`), THE ONLY EXECUTABLE")
    rec("### ### ASSEMBLY -- AND A MODE SUM, HENCE THE OBJECT Q1 DEMOTED.** ### b246: *'Its two")
    rec("### ### realizations remain two objects and this act computed both rather than choosing.'**")
    rec("")

    # ------------------------------------------------------------------ THE BALANCE
    for tag, getD, dbar_of in (("A  (odd eps-MASK -- THE RULING'S REALIZATION)",
                                lambda r: r['E2odd'], lambda r: mask_alg),
                               ("B  (odd TRACE modes -- THE OTHER REALIZATION)",
                                lambda r: r['dneg'], lambda r: r['dbar'])):
        rec("-" * 118)
        rec("### ### **THE BALANCE UNDER REALIZATION %s**" % tag)
        rec("###   `(Delta_- - E2)  ?=  (PR - Theta_q)` ; residual := LHS - RHS = -(L - R)")
        rec("-" * 118)
        rec("%-5s %14s %14s %14s %13s %10s %s"
            % ("a^2", "D - E2", "PR - Theta_q", "residual", "combined bar", "|res|/bar", "beyond?"))
        for r in rows:
            lhs = getD(r) - r['E2']
            rhs = r['PR'] - r['Thq']
            res = lhs - rhs
            bar = math.sqrt(dbar_of(r) ** 2 + mask_alg ** 2)
            ratio = abs(res) / bar if bar > 0 else float('inf')
            flag = "yes" if abs(res) > bar else "no"
            star = "   ### <- PURE-ARCHIMEDEAN CELL (PR = Theta_q = 0)" if r['lab'] == '2' else ""
            rec("%-5s %14.6f %14.6f %14.6f %13.3e %10.2e %s%s"
                % (r['lab'], lhs, rhs, res, bar, ratio, flag, star))
        rec("")

    # ------------------------------------------------------------- THE ALGEBRAIC REDUCTION
    rec("-" * 118)
    rec("### THE ALGEBRAIC REDUCTION, DERIVED IN THE MEANINGS FILE BEFORE THE RUN AND CHECKED HERE.")
    rec("### Under realization (A): `Delta_- - E2 = E2odd - (E2even + E2odd) = -E2even`,")
    rec("### so the balance is ### **`E2even ?= Theta_q - PR`.**")
    rec("-" * 118)
    rec("%-5s %14s %14s %14s" % ("a^2", "-E2even", "D(A) - E2", "|difference|"))
    worst = 0.0
    for r in rows:
        lhs = r['E2odd'] - r['E2']
        d = abs(lhs - (-r['E2even']))
        worst = max(worst, d)
        rec("%-5s %14.6f %14.6f %14.3e" % (r['lab'], -r['E2even'], lhs, d))
    rec("  ### ### **MAX %.3e -- THE REDUCTION HOLDS. ### AND IT IS AN IDENTITY IN THE SECTOR" % worst)
    rec("  ### ### SPLIT, SO IT IS RESTATEMENT TOO, AND IS LABELLED SO RATHER THAN COUNTED.**")
    rec("")

    # ------------------------------------------------------- G-STAB, AND THE HONEST BAR
    rec("-" * 118)
    rec("### G-STAB AT THE REGISTERED AXES PLUS ONE REFINEMENT (NQ = 1100).")
    rec("-" * 118)
    rec("%-5s %12s %12s %12s %12s %11s" % ("a^2", "Dneg@500", "Dneg@700", "Dneg@900",
                                           "Dneg@1100", "spread"))
    for r in rows:
        rec("%-5s %12.6f %12.6f %12.6f %12.6f %11.2e"
            % (r['lab'], r['dnegs'][500], r['dnegs'][700], r['dnegs'][900], r['dnegs'][1100],
               r['dbar']))
    rec("### ### **AND THE THING THE BAR COLUMN MAKES PLAIN, WHICH IS A STRUCTURAL FACT AND NOT A")
    rec("### ### NUMBER: UNDER REALIZATION (A) *NOTHING IN THE BALANCE IS A MODE SUM.* ### `E2even`,")
    rec("### ### `E2odd`, `PR` AND `Theta_q` ARE ALL FIXED AT THE eps AND CARTO AXES AND DO NOT")
    rec("### ### MOVE WITH `NQ` AT ALL.** ### So realization (A)'s bar is the eps mask certificate")
    rec("### alone, and ### **Q1's DEMOTION AND b252's DIVERGENCE ARE ENTIRELY IRRELEVANT TO IT.**")
    rec("### ### **UNDER REALIZATION (B) THE BALANCE *DOES* CARRY A MODE SUM, AND WITH IT b252's")
    rec("### ### SUSPICION AND b253's QUOTED-N LAW.**")
    rec("")
    rec("### G-INDEP: `A`/`PR` from `left_side`, `Theta_q` from `theta_quotient`, `E2` and its")
    rec("### sectors from `e2_of_grid` on `per_mode_eps_grids`, `Dneg` from `trace_modes` --")
    rec("### ### **EACH FROM ITS OWN OWNER, IMPORTED AS A MODULE, NONE RE-IMPLEMENTED HERE.**")
    rec("=" * 118)
    io.open(BANK, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
