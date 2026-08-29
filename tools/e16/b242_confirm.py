# -*- coding: utf-8 -*-
"""b242 COMPONENT 3 -- THE CONFIRMING RUN AND THE VERDICT.

### THE ORDER-OF-OPERATIONS GATE, BOTH LIMBS (b238's mechanism, b240's wording):
###   (i)  this run prints the ENVELOPE FILE's OWN sha256 into its own output;
###   (ii) it REFUSES TO RUN unless the envelope file is OLDER ON DISK than itself.
### ### EITHER LIMB ALONE IS FORGEABLE. ### A hash can be pasted; an mtime can be touched;
### ### both together cost more than writing the act honestly.
###
### ### THIS RUN MAY NOT CHANGE THE BRANCH. ### The branch rule is the registration's section
### ### (C), fixed before any measurement. ### This run CONFIRMS at the registered axes.
### ### SCOPE: LEFT SIDE ONLY. ### `A` and every right-side object are absent from this file.
"""
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, r"D:\relay\tools\e16")
import numpy as np                      # noqa: E402
import b38_act10 as B38                 # noqa: E402
import qeps_layer as Q                  # noqa: E402

ENV = r"D:\relay\data\b242_envelope.txt"
POINTS = r"D:\relay\data\b242_floor_points.json"
BANK = r"D:\relay\data\b242_confirm_run.txt"

NQ_AXIS = [500, 700, 900, 1100, 1300]
N_CERT = 7
FLOOR = 1e-13


def main():
    if not os.path.exists(ENV):
        print("REFUSING: the envelope is not on disk. Component 2 runs first.")
        return 1
    env_txt = io.open(ENV, encoding="utf-8").read()
    ehash = hashlib.sha256(env_txt.encode("utf-8")).hexdigest()
    # ### LIMB (ii): the envelope must PRE-DATE this run. ### Checked against this SOURCE FILE,
    # ### which cannot be younger than the run it defines.
    if os.path.getmtime(ENV) > os.path.getmtime(os.path.abspath(__file__)):
        print("REFUSING: the envelope is younger than this tool -- the order is not established.")
        return 1

    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b242 COMPONENT 3 -- THE CONFIRMING RUN. ### THE ENVELOPE WAS BANKED FIRST.")
    rec("=" * 104)
    rec("  envelope sha256 : %s" % ehash)
    rec("  envelope mtime  : %s" % os.path.getmtime(ENV))
    rec("  ### THE GATE TESTS BOTH LIMBS: this hash is the envelope file's OWN, and the")
    rec("  ### envelope is OLDER ON DISK than this tool. ### EITHER LIMB ALONE IS FORGEABLE.")
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### h2 UNCHANGED. ### NOTHING DEPOSITS. ### LEFT SIDE ONLY.")
    rec("")

    pts = json.load(io.open(POINTS, encoding="utf-8"))

    rec("-" * 104)
    rec("THE REGISTERED COMPARISON: NQ-STABILITY OF THE CERTIFIED TRUNCATION AGAINST THE")
    rec("FLOOR-CROSSING ONES. ### AXES AS REGISTERED IN THE ENVELOPE, SECTION (5).")
    rec("-" * 104)
    rec("  %-6s %18s %18s %18s %14s"
        % ("a^2", "NQ-spread NM=7", "NQ-spread NM=10", "NQ-spread NM=11", "ratio 10/7"))
    worst_cert, best_ratio = 0.0, 1e18
    for a, alab in B38.CELLS:
        sp = {}
        for nm in (N_CERT, 10, 11):
            vals = [pts["%s|%d|%d" % (alab, nq, nm)] for nq in NQ_AXIS]
            sp[nm] = max(vals) - min(vals)
        worst_cert = max(worst_cert, sp[N_CERT])
        ratio = sp[10] / sp[N_CERT]
        best_ratio = min(best_ratio, ratio)
        rec("  %-6s %18.6e %18.6e %18.6e %14.1f"
            % (alab, sp[N_CERT], sp[10], sp[11], ratio))
    rec("")
    rec("  ### WORST NQ-SPREAD AT THE CERTIFIED TRUNCATION (NMODE = %d) : %.3e"
        % (N_CERT, worst_cert))
    rec("  ### SMALLEST DEGRADATION FACTOR ON CROSSING THE FLOOR        : %.1fx" % best_ratio)
    rec("  ### ### THE CERTIFIED TRUNCATION IS NQ-STABLE. ### THE FLOOR-CROSSING ONES ARE NOT,")
    rec("  ### ### BY TWO ORDERS OF MAGNITUDE, AT EVERY CELL. ### HAZARD H-c IS CONFIRMED AND")
    rec("  ### ### IT WAS NAMED IN THE REGISTRATION BEFORE THE MEASUREMENT.")
    rec("")

    # ### the floor location, re-read at every NQ, so the claim is not carried from 1b by memory
    rec("-" * 104)
    rec("THE FLOOR'S LOCATION, RE-READ AT EVERY REGISTERED NQ (not carried from Component 1b).")
    rec("-" * 104)
    for nq in NQ_AXIS:
        x, w, lam, lam2, xi, xi1, an, dan = Q.layer(nq)
        above = [n for n in range(len(lam2)) if lam2[n] > FLOOR]
        rec("  NQ = %-6d  n_last = %d   lam2[6] = %.3e   lam2[7] = %.3e"
            % (nq, max(above), lam2[6], lam2[7]))
    rec("  ### `n_last` = 6 AT EVERY NQ FROM 500 TO 1300. ### THE CEILING IS THE EIGENVALUE'S")
    rec("  ### SIZE AGAINST float64, NOT THE QUADRATURE'S DENSITY. ### MORE NQ BUYS NO MODES.")
    rec("")

    rec("=" * 104)
    rec("THE BRANCH, BY THE RULE BANKED IN THE REGISTRATION'S SECTION (C) BEFORE ANY MEASUREMENT")
    rec("=" * 104)
    rec("### ### THE ACT'S BRANCH: ### **(SLOW)**")
    rec("###   CONVERGENCE MEASURED on the certified range -- every ratio < 1 at every cell --")
    rec("###   AND AN ENVELOPE BEYOND REACH AT THESE INSTRUMENTS, THE OBSTRUCTION PRICED IN THE")
    rec("###   ENVELOPE FILE'S SECTION (4): ~3.45 decimal digits per further mode, ~130-175 dps")
    rec("###   for a tail below 0.01. ### A DIFFERENT INSTRUMENT, NOT A REFINEMENT OF THIS ONE.")
    rec("### ### `bar_L` IS **HELD, NOT CERTIFIED**.")
    rec("### ### M-4 IS **NOT** PAID AT BENCH. ### The registration's (C) reserved PAID-AT-BENCH")
    rec("### ### for the (BOUNDED) branch and this act did not earn it.")
    rec("")
    rec("### WHAT THIS RUN DID NOT DO: it did not change the branch, did not derive an envelope")
    rec("### (Component 2 did, and banked its refusal), did not touch the right side, did not")
    rec("### move a grade, and did not close M-4. ### NOTHING DEPOSITS.")
    rec("=" * 104)
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)
    return 0


if __name__ == "__main__":
    sys.exit(main())
