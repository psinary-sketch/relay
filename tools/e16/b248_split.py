# -*- coding: utf-8 -*-
"""b248 COMPONENT 2 -- THE JUNCTION SPLIT, FROM BANKED DATA ONLY.

### **NO FACE-OFF RUNS AND NO RESIDUAL IS RECOMPUTED.** ### This tool reads b242's banked
### per-mode arrays and b37's banked sector columns and splits `-D_dict` into its two named
### pieces. ### It computes no side, no column and no comparison between columns.
###
### ### W-ORD-TE-SPEC, HONOURED IN FORM: ### EVERY BANK'S AXES ARE PRINTED BEFORE ANY NUMBER, AND
### ### THE ONE AXIS MISMATCH IN THE CORPUS (b38's NMODE = 10 against K1's 7) IS NAMED EVEN THOUGH
### ### THIS TOOL DOES NOT USE b38's ROWS.
"""
import io
import json
import os
import sys
import time

PTS = r"D:\relay\data\b242_axis_points.json"
BANK = r"D:\relay\data\b248_split_run.txt"
CELLS = ["2", "3", "4", "8", "9", "12"]

# ### b37's BANKED SECTOR COLUMNS -- axes: EPS_NQ = 700, NU_HALF = 401, S4, SIX decimals,
# ### and ### **NO TRACE IS COMPUTED IN b37 AT ALL** (it substitutes at content).
B37 = {"2": (0.000000, 0.000000), "3": (0.000000, 0.106484), "4": (0.161978, 0.249320),
       "8": (0.317018, 0.561045), "9": (0.473862, 0.608882), "12": (0.518491, 0.714334)}
# ### the ACTIVE-PRIME TERM COUNT per cell, from `left_side`'s own loop conditions as b243
# ### tabulated them (p^k <= a^2 and log p^k <= 2L): 1, 1, 3, 5, 6, 6.
TERMS = {"2": 1, "3": 1, "4": 3, "8": 5, "9": 6, "12": 6}


def main():
    if not os.path.exists(PTS):
        print("### REFUSED -- b242's banked per-mode points are not on disk.")
        return 1
    pts = json.load(io.open(PTS, encoding="utf-8"))
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b248 COMPONENT 2 -- THE JUNCTION SPLIT. ### FROM BANKED DATA ONLY.")
    rec("### RUN AT %s (local)." % time.strftime("%Y-%m-%dT%H:%M:%S"))
    rec("=" * 104)
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL.'")
    rec("### h2 UNCHANGED. ### NOTHING DEPOSITS.")
    rec("### **NO FACE-OFF RUNS. ### NO RESIDUAL IS RECOMPUTED. ### NO COLUMNS ARE COMPARED.**")
    rec("")
    rec("-" * 104)
    rec("W-ORD-TE-SPEC -- THE AXES OF EVERY BANK CONSULTED, PRINTED BEFORE ANY NUMBER.")
    rec("-" * 104)
    rec("  b242 per-mode bank : NQ=700  NMODE_CAP=11  NTERM=11  EPS_NQ=700  NU_HALF=401  S4")
    rec("                       atlas NV=4001. ### fields used: E2n[], E2full")
    rec("  b37 sector bank    : EPS_NQ=700  NU_HALF=401  S4  ### SIX decimals")
    rec("                       ### **NO TRACE IS COMPUTED IN b37** -- it substitutes at content.")
    rec("                       ### fields used: Thq, PR")
    rec("  b38 row bank       : NQ=700  ### NMODE=10 ###  -- ### **NAMED AND NOT USED HERE.**")
    rec("                       That axis differs from K1's seven and is the trap b245 fell into.")
    rec("  ### THE MASK CERTIFICATE, RE-DERIVED FROM THE ARRAYS AND NOT QUOTED:")
    worst = 0.0
    for c in CELLS:
        d = pts["trunc|%s" % c]
        worst = max(worst, abs(sum(d["E2n"]) - d["E2full"]))
    ok = worst <= 1e-10
    rec("  ###   max|sum_n E2n - E2full| = %.2e  %s   ### it is what licenses the parity split."
        % (worst, "PASS" if ok else "### FAIL"))
    if not ok:
        rec("\n### HALT -- the mask certificate failed. No table follows.")
        io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return 0
    rec("")

    rec("=" * 104)
    rec("THE SECOND OBJECT SPLIT INTO ITS TWO NAMED PIECES.")
    rec("###   `-D_dict = (E2full + E2even) + (PR - Theta_q)`")
    rec("###   ARCHIMEDEAN PIECE := `E2full + E2even`   ### sector arithmetic on the eps series")
    rec("###   JUNCTION PIECE    := `PR - Theta_q`      ### the finite-place pairing")
    rec("=" * 104)
    rec("  %-5s %8s %14s %14s %16s %16s %14s %10s"
        % ("a^2", "terms", "E2full", "E2even", "ARCHIMEDEAN", "JUNCTION", "-D_dict", "junc %"))
    rows = {}
    for c in CELLS:
        d = pts["trunc|%s" % c]
        E2n = d["E2n"]
        e2full = d["E2full"]
        e2even = sum(E2n[n] for n in range(len(E2n)) if n % 2 == 0)
        thq, pr = B37[c]
        arch = e2full + e2even
        junc = pr - thq
        tot = arch + junc
        rows[c] = dict(arch=arch, junc=junc, tot=tot, terms=TERMS[c])
        rec("  %-5s %8d %14.9f %14.9f %16.9f %16.9f %14.9f %9.2f%%"
            % (c, TERMS[c], e2full, e2even, arch, junc, tot, 100.0 * junc / tot if tot else 0.0))
    rec("")

    rec("-" * 104)
    rec("THE REGISTERED PREDICTION, JUDGED IN ITS TWO LIMBS SEPARATELY.")
    rec("### 'THE JUNCTION PIECE VANISHES AT a^2 = 2 AND GROWS WITH THE ACTIVE PRIMES.'")
    rec("-" * 104)
    limb1 = (rows["2"]["junc"] == 0.0)
    rec("  LIMB 1 -- vanishes at a^2 = 2 : junction = %.17g   ### **%s**"
        % (rows["2"]["junc"], "CONFIRMED" if limb1 else "REFUTED"))
    seq = [(TERMS[c], rows[c]["junc"], c) for c in CELLS]
    mono = all(seq[i][1] <= seq[i + 1][1] + 1e-15 for i in range(len(seq) - 1))
    rec("  LIMB 2 -- monotone non-decreasing in the active-prime count:")
    rec("            terms    : %s" % "  ".join("%d" % t for t, _, _ in seq))
    rec("            junction : %s" % "  ".join("%.6f" % j for _, j, _ in seq))
    rec("            ### **%s**" % ("CONFIRMED" if mono else "REFUTED"))
    if not mono:
        bad = [(seq[i + 1][2], seq[i][1], seq[i + 1][1])
               for i in range(len(seq) - 1) if seq[i + 1][1] < seq[i][1] - 1e-15]
        for cell, prev, cur in bad:
            rec("            ### DROP at a^2 = %s: %.6f -> %.6f" % (cell, prev, cur))
    rec("")
    rec("  ### ### **THE PREDICTION IS %s.**"
        % ("CONFIRMED IN BOTH LIMBS" if (limb1 and mono)
           else ("HALF RIGHT -- LIMB 1 CONFIRMED, LIMB 2 REFUTED" if limb1
                 else "REFUTED")))
    rec("  ### **A PREDICTION THAT IS HALF RIGHT IS REPORTED AS HALF RIGHT AND NOT AS CONFIRMED.**")
    rec("")
    rec("### WHAT THIS RUN DID NOT DO: it ran no face-off, recomputed no residual, compared no")
    rec("### columns, and decided no arrangement. ### NOTHING DEPOSITS.")
    rec("=" * 104)
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)
    return 0


if __name__ == "__main__":
    sys.exit(main())
