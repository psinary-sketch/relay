# -*- coding: utf-8 -*-
"""b246 COMPONENT 2 -- THE TWO TAILS, COMPUTED FROM BANKED PER-MODE DATA.

### THE ORDER-OF-OPERATIONS GATE, BOTH LIMBS: this run prints the DEFINITIONS FILE's OWN sha256,
### and REFUSES unless that file is OLDER ON DISK than this tool. ### EITHER LIMB ALONE IS
### FORGEABLE.
###
### ### W-ORD-TE-SPEC, HONOURED IN FORM: ### EVERY BANK CONSULTED HAS ITS AXES PRINTED, AND THE
### ### RUN **HALTS** ON A MISMATCH IT CAN DETECT. ### b245 filed this work-order because it
### ### compared a SEVEN-mode run to a TEN-mode bank and reported the difference as a finding.
###
### ### THIS TOOL COMPUTES NO SIDE, RUNS NO FACE-OFF, AND RECOMPUTES NO COLUMN. ### It reads
### ### b242's banked per-mode arrays and b37/b38's banked rows, and does arithmetic on them.
"""
import hashlib
import io
import json
import os
import sys
import time

DEFS = r"D:\relay\data\b246_definitions.txt"
PTS = r"D:\relay\data\b242_axis_points.json"
BANK = r"D:\relay\data\b246_tails_run.txt"

K = 7                       # ### RULE MODES K1's realized mode count (modes 0..6).
NTERM = 11                  # ### Lemma F.1's certified ceiling, and b242's banked array length.
FLOOR = 5e-5                # ### b38's own rounding floor (its bank prints resid47 to 4 dp).
CELLS = ["2", "3", "4", "8", "9", "12"]

# ### b37's BANKED SECTOR COLUMNS, S4, EPS_NQ = 700, printed to SIX decimals. ### For cross-check
# ### of the parity split against an independent owner.
B37 = {"2": (1.679428, 1.001814, 0.677615, 0.000000, 0.000000),
       "3": (1.516645, 0.910943, 0.605701, 0.000000, 0.106484),
       "4": (1.374051, 0.834033, 0.540018, 0.161978, 0.249320),
       "8": (1.096239, 0.685514, 0.410725, 0.317018, 0.561045),
       "9": (1.058309, 0.665133, 0.393176, 0.473862, 0.608882),
       "12": (0.975064, 0.620090, 0.354973, 0.518491, 0.714334)}   # E2, E2even, E2odd, Thq, PR
# ### b38's BANKED ROWS, ### NMODE = 10 ### -- quoted ONLY with that axis attached.
B38_ROW = {"2": (4.0486, -2.681242), "3": (3.3740, -2.534072), "4": (3.0478, -2.295425),
           "8": (2.5208, -2.025781), "9": (2.4540, -1.858463), "12": (2.3134, -1.790997)}


def main():
    if not os.path.exists(DEFS):
        print("### REFUSED -- the definitions file is not on disk.")
        return 1
    dtxt = io.open(DEFS, encoding="utf-8").read()
    dhash = hashlib.sha256(dtxt.encode("utf-8")).hexdigest()
    if os.path.getmtime(DEFS) > os.path.getmtime(os.path.abspath(__file__)):
        print("### REFUSED -- the definitions file is younger than this tool.")
        return 1
    pts = json.load(io.open(PTS, encoding="utf-8"))

    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b246 COMPONENT 2 -- THE TWO TAILS. ### THE RUN.")
    rec("### RUN AT %s (local)." % time.strftime("%Y-%m-%dT%H:%M:%S"))
    rec("=" * 104)
    rec("  definitions sha256 : %s" % dhash)
    rec("  ### BOTH LIMBS: this hash is the definitions file's OWN, and that file is OLDER ON")
    rec("  ### DISK than this tool. ### EITHER LIMB ALONE IS FORGEABLE.")
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL.'")
    rec("### h2 UNCHANGED. ### NOTHING DEPOSITS. ### NO FACE-OFF IS RUN AND NO COLUMN RECOMPUTED.")
    rec("")

    # ------------------------------------------------- W-ORD-TE-SPEC AXIS BLOCK
    rec("-" * 104)
    rec("W-ORD-TE-SPEC -- EVERY CONSULTED BANK'S AXES, PRINTED, AND THE MISMATCHES NAMED.")
    rec("-" * 104)
    rec("  b242 per-mode bank : NQ=700  NMODE_CAP=11  NTERM=11  EPS_NQ=700  EPS_NG=400")
    rec("                       EPS_NRHO=240  NU_HALF=401  S4={inf,2,3,5}  atlas NV=4001")
    rec("  b37 sector bank    : EPS_NQ=700  NU_HALF=401  S4   ### NO TRACE COMPUTED IN b37")
    rec("  b38 row bank       : NQ=700  ### NMODE=10 ###  EPS_NQ=700  NU_HALF=401  S4")
    rec("  THIS RUN           : all tails and resid47 computed from the b242 arrays at")
    rec("                       ### **K = %d MODES (RULE MODES K1)** ###" % K)
    rec("  ### ### THE MISMATCH, NAMED RATHER THAN MET LATER: ### **b38's ROWS ARE AT NMODE = 10")
    rec("  ### ### AND THIS RUN IS AT 7.** ### Any comparison to them is LABELLED and its")
    rec("  ### ### tolerance set to b38's own 4-decimal floor. ### **THAT IS THE EXACT TRAP b245")
    rec("  ### ### FELL INTO, AND IT IS WHY W-ORD-TE-SPEC EXISTS.**")
    halt = False
    for c in CELLS:
        d = pts["trunc|%s" % c]
        if len(d["tr"]) != NTERM or len(d["E2n"]) != NTERM:
            rec("  ### HALT -- cell %s array length is not %d." % (c, NTERM))
            halt = True
    rec("  array-length gate  : %s (all six cells carry %d per-mode entries)"
        % ("PASS" if not halt else "### FAIL", NTERM))
    # ### THE MASK CERTIFICATE, RE-DERIVED FROM THE ARRAYS RATHER THAN CITED.
    worst_mask = 0.0
    for c in CELLS:
        d = pts["trunc|%s" % c]
        worst_mask = max(worst_mask, abs(sum(d["E2n"]) - d["E2full"]))
    ok = worst_mask <= 1e-10
    halt |= not ok
    rec("  mask certificate   : max|sum_n E2n - E2full| = %.2e  %s   ### RE-DERIVED, NOT CITED"
        % (worst_mask, "PASS" if ok else "### FAIL"))
    rec("  ### **THAT CERTIFICATE IS WHAT LICENSES SPLITTING THE eps SERIES BY PARITY AT ALL.**")
    if halt:
        rec("\n### ### THE ACT'S BRANCH: ### **(HALT)** -- an axis or certificate gate fired.")
        io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return 0
    rec("")

    # ------------------------------------------------------------- THE TAILS
    R = {}
    for c in CELLS:
        d = pts["trunc|%s" % c]
        tr, E2n, A, E2full = d["tr"], d["E2n"], d["A"], d["E2full"]
        r = {}
        r["Tr_K"] = sum(tr[:K])
        r["resid47_K"] = r["Tr_K"] - A - E2full
        r["A"] = A
        r["E2full"] = E2full
        r["Dm"] = d["Dm"]
        # (R1) trace tail beyond K, by parity
        r["R1_even"] = sum(tr[n] for n in range(K, NTERM) if n % 2 == 0)
        r["R1_odd"] = sum(tr[n] for n in range(K, NTERM) if n % 2 == 1)
        # (R2) eps tail beyond K, by parity
        r["R2_even"] = sum(E2n[n] for n in range(K, NTERM) if n % 2 == 0)
        r["R2_odd"] = sum(E2n[n] for n in range(K, NTERM) if n % 2 == 1)
        # (R3) full eps sectors
        r["R3_even"] = sum(E2n[n] for n in range(NTERM) if n % 2 == 0)
        r["R3_odd"] = sum(E2n[n] for n in range(NTERM) if n % 2 == 1)
        # the raw odd trace slice -- b36_act8.py:172's object
        r["Dneg_raw"] = sum(tr[n] for n in range(NTERM) if n % 2 == 1)
        e2b, eeb, eob, thq, pr = B37[c]
        r["Thq"], r["PR"] = thq, pr
        r["D_dict_owner"] = (thq - pr) + (r["Dm"] - 2.0 * E2full)
        r["SECTOR_SPLIT_DIFF"] = r["Dneg_raw"] - r["Dm"]
        R[c] = r

    rec("=" * 104)
    rec("THE TAILS, ALL THREE READINGS, PRINTED WHATEVER THEY SAY. ### (R1) IS THE PRIMARY.")
    rec("=" * 104)
    rec("  %-5s %13s %13s %13s %13s %13s %13s"
        % ("a^2", "R1_even", "R1_odd", "R2_even", "R2_odd", "R3_even", "R3_odd"))
    for c in CELLS:
        r = R[c]
        rec("  %-5s %13.9f %13.9f %13.3e %13.3e %13.9f %13.9f"
            % (c, r["R1_even"], r["R1_odd"], r["R2_even"], r["R2_odd"],
               r["R3_even"], r["R3_odd"]))
    rec("  ### (R3) IS sec 17's OWN SECTOR SPLIT, AND `R3_odd` IS `Delta_-` BY sec 19's ROW.")
    rec("")

    rec("-" * 104)
    rec("THE TWO `D_dict` OWNERS, BOTH COMPUTED, BOTH PRINTED. ### b241 (4.5): 'DIFFERENT")
    rec("OBJECTS, SAME NAME, ONE CORPUS.'")
    rec("-" * 104)
    rec("  %-5s %16s %16s %16s %16s"
        % ("a^2", "D_dict_owner", "b38 banked", "Dneg_raw", "SECTOR_SPLIT_DIFF"))
    for c in CELLS:
        r = R[c]
        rec("  %-5s %16.9f %16.6f %16.9f %16.9f"
            % (c, r["D_dict_owner"], B38_ROW[c][1], r["Dneg_raw"], r["SECTOR_SPLIT_DIFF"]))
    rec("  ### `D_dict_owner` vs b38's banked column: agreement is the parity-split cross-check.")
    rec("  ### `SECTOR_SPLIT_DIFF := Dneg_raw - Delta_-` is the ferry's '(raw odd slice - masked")
    rec("  ### odd series)'. ### IT IS **NOT** `D_dict` AND IS NOT CALLED SO.")
    rec("")

    # -------------------------------------------------------------- THE TESTS
    rec("=" * 104)
    rec("THE FIVE TESTS, AT THE BANDS REGISTERED BEFORE ANY NUMBER. ### FLOOR = %.0e" % FLOOR)
    rec("=" * 104)
    v = {}

    rec("--- T-1 IDENTITY: |D_dict_owner - (-TAIL_odd)| <= FLOOR, primary reading (R1).")
    t1 = True
    for c in CELLS:
        r = R[c]
        d = abs(r["D_dict_owner"] - (-r["R1_odd"]))
        ok = d <= FLOOR
        t1 &= ok
        rec("      a^2 = %-4s  D_dict = %+.9f   -TAIL_odd(R1) = %+.9f   |diff| = %.3e  %s"
            % (c, r["D_dict_owner"], -r["R1_odd"], d, "ok" if ok else "### FAIL"))
    v["T-1"] = t1
    rec("      ### T-1: %s" % ("PASS" if t1 else "### FAIL"))

    rec("--- T-2 RECOMPOSITION: |(resid47 + D_dict) - (TAIL_even + TAIL_odd)| <= FLOOR, (R1).")
    t2 = True
    for c in CELLS:
        r = R[c]
        lhs = r["resid47_K"] + r["D_dict_owner"]
        rhs = r["R1_even"] + r["R1_odd"]
        d = abs(lhs - rhs)
        ok = d <= FLOOR
        t2 &= ok
        rec("      a^2 = %-4s  lhs = %+.9f   rhs = %+.9f   |diff| = %.3e  %s"
            % (c, lhs, rhs, d, "ok" if ok else "### FAIL"))
    v["T-2"] = t2
    rec("      ### T-2: %s" % ("PASS" if t2 else "### FAIL"))

    rec("--- T-3 THE RATIO (the one-mechanism signature): (TAIL_even+TAIL_odd)/TAIL_even")
    rec("---     must lie in [1.673, 1.785] at every cell. ### THE BAND IS NOT WIDENED.")
    t3 = True
    for c in CELLS:
        r = R[c]
        den = r["R1_even"]
        rat = (r["R1_even"] + r["R1_odd"]) / den if den else float("inf")
        ok = 1.673 <= rat <= 1.785
        t3 &= ok
        rec("      a^2 = %-4s  ratio(R1) = %.6f   %s" % (c, rat, "in band" if ok else "### OUT"))
    v["T-3"] = t3
    rec("      ### T-3: %s" % ("PASS" if t3 else "### FAIL"))
    rec("      ### the same ratio under the alternates, printed so the ONE-OBJECT hypothesis")
    rec("      ### gets its best shot and not so a flattering reading can be chosen:")
    for c in CELLS:
        r = R[c]
        r2 = ((r["R2_even"] + r["R2_odd"]) / r["R2_even"]) if r["R2_even"] else float("nan")
        r3 = ((r["R3_even"] + r["R3_odd"]) / r["R3_even"]) if r["R3_even"] else float("nan")
        rec("          a^2 = %-4s  ratio(R2) = %14.6f   ratio(R3) = %.6f" % (c, r2, r3))

    rec("--- T-4 CELL-PROFILE: TAIL_odd/TAIL_even MONOTONE in a^2 and max/min <= 1.5, (R1).")
    prof = [R[c]["R1_odd"] / R[c]["R1_even"] for c in CELLS]
    mono = all(prof[i] >= prof[i + 1] for i in range(len(prof) - 1)) or \
           all(prof[i] <= prof[i + 1] for i in range(len(prof) - 1))
    spread = max(prof) / min(prof) if min(prof) else float("inf")
    t4 = mono and spread <= 1.5
    v["T-4"] = t4
    for c, p in zip(CELLS, prof):
        rec("      a^2 = %-4s  TAIL_odd/TAIL_even = %.6f" % (c, p))
    rec("      monotone = %s   max/min = %.4f   ### T-4: %s"
        % (mono, spread, "PASS" if t4 else "### FAIL"))

    rec("--- T-5 (the executor's own): |resid47 + 2*A| <= 1e-3 at EVERY cell.")
    rec("---     Noticed at a^2 = 2 ONLY while reading; five of the six are genuinely untested.")
    t5 = True
    for c in CELLS:
        r = R[c]
        d = abs(r["resid47_K"] + 2.0 * r["A"])
        ok = d <= 1e-3
        t5 &= ok
        rec("      a^2 = %-4s  resid47(K=7) = %+.9f   -2A = %+.9f   |diff| = %.3e  %s"
            % (c, r["resid47_K"], -2.0 * r["A"], d, "ok" if ok else "### FAIL"))
    v["T-5"] = t5
    rec("      ### T-5: %s" % ("PASS" if t5 else "### FAIL"))
    rec("")

    # ------------------------------------------------------------- THE BRANCH
    rec("=" * 104)
    rec("THE BRANCH, BY THE RULES BANKED BEFORE ANY COMPUTATION.")
    rec("=" * 104)
    for k in ("T-1", "T-2", "T-3", "T-4", "T-5"):
        rec("  %-5s : %s" % (k, "PASS" if v[k] else "### FAIL"))
    core = all(v[k] for k in ("T-1", "T-2", "T-3", "T-4"))
    # ### the alternates, scored the same way, for the (MIXED) branch.
    alt_ok = False
    for tag, ev, od in (("R2", "R2_even", "R2_odd"), ("R3", "R3_even", "R3_odd")):
        a1 = all(abs(R[c]["D_dict_owner"] + R[c][od]) <= FLOOR for c in CELLS)
        a2 = all(abs((R[c]["resid47_K"] + R[c]["D_dict_owner"]) - (R[c][ev] + R[c][od]))
                 <= FLOOR for c in CELLS)
        a3 = all(R[c][ev] and 1.673 <= (R[c][ev] + R[c][od]) / R[c][ev] <= 1.785 for c in CELLS)
        if a1 and a2 and a3:
            alt_ok = True
            rec("  ### ALTERNATE READING %s PASSES T-1..T-3." % tag)
    rec("")
    if core:
        rec("### ### THE ACT'S BRANCH: ### **(ONE OBJECT)**")
    elif alt_ok:
        rec("### ### THE ACT'S BRANCH: ### **(MIXED)** -- the primary fails, an alternate passes.")
    else:
        rec("### ### THE ACT'S BRANCH: ### **(TWO OBJECTS)**")
        rec("###   MEANS, IN THE BANKED WORDS: ### **AT FULL PROMINENCE**, and ### **THE TWO")
        rec("###   TERMS STAY SEPARATELY OWNED.** ### M-4 covers `resid47` and NOT the other")
        rec("###   term, and ### **NO SENTENCE ABOUT PAYING M-4 PAYING THE WHOLE SHORTFALL MAY")
        rec("###   BE WRITTEN.**")
    rec("")
    rec("### b245's BRANCH IS NOT REVISED BY THIS ACT. ### NO FACE-OFF WAS RUN AND NO COLUMN")
    rec("### RECOMPUTED. ### NO GRADE MOVED. ### M-2..M-5 STAND OPEN. ### NOTHING DEPOSITS.")
    rec("=" * 104)
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)
    return 0


if __name__ == "__main__":
    sys.exit(main())
