# -*- coding: utf-8 -*-
"""b241 -- THE SIBLING READ, MEASURED. ### A READ, NOT A FACE-OFF.

### WHAT THIS TOOL IS FOR, AND THE ONLY THING IT IS FOR.
### b241's component (a) decides BY QUOTATION that `b38_act10.py` and `b36_act8.py`
### define `resid47` by TWO DIFFERENT FORMULAS:
###     b38_act10.py:182   resid = TrN - A - E2N      ### E2N = the 10-of-11-MODE partial sum
###     b36_act8.py :184   resid47 = Tr_full - (A + E2)   ### E2 = the FULL eps, all 11 modes
### ### THE VERDICT IS ALREADY MADE FROM THE CHARACTERS AND THIS TOOL DOES NOT MAKE IT.
### ### THIS TOOL ANSWERS ONE FURTHER QUESTION, WHICH THE ACT'S OWN TEST (T2) OBLIGES IT TO
### ### ANSWER: ### DOES THE AMENDMENT MOVE A NUMBER? ### An amendment to a warrant that
### ### silently also moves a column would be a different kind of finding, and the act must
### ### not report the first while concealing the second.
###
### ### IT COMPUTES NO SIDE, ASSEMBLES NO IDENTITY, AND COMPARES NO COLUMNS. ### It calls
### ### b38's own functions at b38's own committed defaults and prints the difference between
### ### two of b38's own intermediate quantities. ### NOTHING HERE IS A FACE-OFF AND NOTHING
### ### HERE MAY BE CITED AS ONE.
"""
import io
import math
import os
import sys

sys.path.insert(0, r"D:\relay\tools\e16")
import numpy as np                      # noqa: E402
import b38_act10 as B38                 # noqa: E402
import qeps_layer as Q                  # noqa: E402

BANK = r"D:\relay\data\b241_sibling_read.txt"
MODE = (700, 10)                        # ### b38's TRIPLE, middle entry -- b240's MODE_BASE


def main():
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b241 -- THE SIBLING READ, MEASURED. ### A READ. ### NO SIDE IS ASSEMBLED AND NO")
    rec("### IDENTITY IS EVALUATED. ### THE VERDICT ON (a) IS MADE BY QUOTATION, NOT HERE.")
    rec("=" * 104)
    rec("### THE CEILING STILL GOVERNS: b15 -- 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF")
    rec("### DECIDES NOTHING GLOBAL.' ### h2 UNCHANGED. ### NOTHING DEPOSITS.")
    rec("")
    rec("### THE TWO SOURCE LINES THIS TOOL MEASURES THE DISTANCE BETWEEN:")
    rec("###   b38_act10.py:182   resid = TrN - A - E2N")
    rec("###   b36_act8.py :184   resid47 = Tr_full - (A + E2)")
    rec("### and the structural fact that makes them different objects, read from source:")
    rec("###   qeps_layer.py:41   NTERM = 11")
    rec("###   b38_act10.py:63    NMODE = min(NMODE, xi.shape[1])   ->  min(10, 11) = 10")
    rec("### ### SO b38 SUMS TEN OF THE ELEVEN PER-MODE eps MASKS AND b36 USES ALL ELEVEN.")
    rec("")

    NQ, NMODE_REQ = MODE
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    rec("  NTERM (len lam2) read live from the layer : %d" % len(lam2))
    rec("  xi.shape[1] read live from the layer      : %d" % xi.shape[1])
    rec("  NMODE requested / NMODE used              : %d / %d"
        % (NMODE_REQ, min(NMODE_REQ, xi.shape[1])))
    rec("")

    rr = np.exp(np.linspace(1e-4, math.log(12.001), B38.EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
    ee_modes = B38.per_mode_eps_grids(rr)

    # ### b38's OWN MASK-ALGEBRA GATE, RE-RUN HERE AND NOT ASSUMED. ### It is the thing that
    # ### licenses calling the ten-mode sum and the full eps THE SAME OBJECT at two truncations
    # ### rather than two unrelated objects.
    mode_alg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))
    ok = mode_alg <= 1e-10
    rec("  ### b38's OWN mask-algebra gate, RE-RUN: max|sum_n eps_n - eps_full| = %.2e  %s"
        % (mode_alg, "PASS" if ok else "FAIL"))
    if not ok:
        rec("  ### GATE FAILED -- VOID. No table follows.")
        io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return
    rec("  ### THAT PASS IS WHAT LETS THIS ACT SAY 'ONE OBJECT AT TWO TRUNCATIONS' RATHER")
    rec("  ### THAN 'TWO OBJECTS'. ### It is b38's own gate and this tool did not invent it.")
    rec("")

    rec("-" * 104)
    rec("THE TWO resid47 FORMULAS AT THE SIX BANKED DIAGONAL CELLS, AT b38's OWN DEFAULTS.")
    rec("### resid_b38 := TrN - A - E2N   (ten modes)   ### resid_b36 := Tr_full - (A + E2full)")
    rec("-" * 104)
    rec("%-6s %14s %14s %14s %14s %14s"
        % ("a^2", "E2N (10)", "E2full (11)", "E2full - E2N", "resid_b38", "resid_b36"))
    worst_e2, worst_rs = 0.0, 0.0
    for a, alab in B38.CELLS:
        v, w2, corr, vc, L = B38.family(a)
        A, P, PR = B38.left_side(a, B38.S4, v, w2, corr, vc, L)
        tr = B38.trace_modes(a, corr, vc, L, NQ, NMODE_REQ)
        N = len(tr)
        E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rr, ee_modes[n]) for n in range(N)])
        E2N = float(E2n.sum())
        E2full = B38.e2_of_grid(a, corr, vc, L, rr, ee_full)
        TrN = float(tr.sum())
        r38 = TrN - A - E2N
        r36 = TrN - (A + E2full)
        worst_e2 = max(worst_e2, abs(E2full - E2N))
        worst_rs = max(worst_rs, abs(r38 - r36))
        rec("%-6s %14.9f %14.9f %14.9f %14.9f %14.9f"
            % (alab, E2N, E2full, E2full - E2N, r38, r36))
    rec("")
    rec("  ### max |E2full - E2N|      = %.3e   (the ELEVENTH mode's own eps contribution)"
        % worst_e2)
    rec("  ### max |resid_b38 - resid_b36| = %.3e" % worst_rs)
    rec("")
    rec("-" * 104)
    rec("WHAT THIS MEASUREMENT DOES AND DOES NOT LICENSE. ### READ BEFORE CITING IT.")
    rec("-" * 104)
    rec("### IT DOES: quantify the distance between two source lines that the act has already")
    rec("### ruled, BY QUOTATION, to be different formulas. ### The act's own test (T2) requires")
    rec("### the direction and size of any movement to be disclosed beside the verdict, and this")
    rec("### is that disclosure.")
    rec("### IT DOES NOT: decide (a). ### (a) IS DECIDED BY THE CHARACTERS OF b38_act10.py:182")
    rec("### AND b36_act8.py:184, AND A SMALL DIFFERENCE WOULD NOT MAKE TWO FORMULAS ONE.")
    rec("### ### A WARRANT IS NOT REPAIRED BY THE NUMBER IT HAPPENS TO PRODUCE. ### If the two")
    rec("### ### formulas agree to machine precision the finding is UNCHANGED: b240's")
    rec("### ### registration cited b38_act10 for a line b36_act8 contains, and that is a")
    rec("### ### misattribution whatever it costs in digits.")
    rec("### NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. ### NOTHING DEPOSITS.")
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
