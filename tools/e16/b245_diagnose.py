# -*- coding: utf-8 -*-
"""b245 -- THE T-E DIAGNOSTIC. ### RUN **AFTER** THE BRANCH, AND IT DOES NOT TOUCH IT.

### T-E failed. ### THE BRANCH IS (DISSONANT-BEYOND) BY THE RULE BANKED BEFORE ANY NUMBER AND
### THIS TOOL CANNOT CHANGE THAT. ### It exists to name the term, in the registered indictment
### order, SUSPECT 1 FIRST.
###
### THE HYPOTHESIS, AND IT IS CHECKABLE TO FIVE FIGURES: ### b38's bank of 2026-08-18 was
### computed at ### **NMODE = 10** (b38's TRIPLE middle entry). ### This act runs at
### ### **NMODE = 7** (RULE MODES K1). ### If that is the whole of the deviation, then
### ###   `|run - bank| == tr[7] + tr[8] + tr[9]`
### exactly, cell by cell, where those three mode terms are read from ### **b242's INDEPENDENTLY
### BANKED per-mode table** and not recomputed here.
### ### **IF IT DOES NOT MATCH, THE DEVIATION IS SOMETHING ELSE AND THE ACT MUST SAY SO.**
"""
import io
import json
import os
import sys

BANK = r"D:\relay\data\b245_te_diagnosis.txt"
B242PTS = r"D:\relay\data\b242_axis_points.json"
RUN = r"D:\relay\data\b245_faceoff_run.txt"

# ### b38's AND b37's BANKED VALUES OF 2026-08-18, quoted at the precision the banks carry.
BANK38 = {"2": (4.0486, -2.681242), "3": (3.3740, -2.534072), "4": (3.0478, -2.295425),
          "8": (2.5208, -2.025781), "9": (2.4540, -1.858463), "12": (2.3134, -1.790997)}
CELLS = ["2", "3", "4", "8", "9", "12"]


def run_LmR():
    """### READ THE RUN'S OWN `L - R` FROM ITS BANKED OUTPUT. ### Not recomputed: this tool
    ### must not be able to move the number it is diagnosing."""
    out = {}
    started = False
    for line in io.open(RUN, encoding="utf-8"):
        if "THE ALGEBRAIC RESTATEMENT" in line:
            started = True
        if started:
            p = line.split()
            if len(p) == 4 and p[0] in CELLS:
                try:
                    out[p[0]] = float(p[1])
                except ValueError:
                    pass
    return out


def main():
    if not os.path.exists(B242PTS):
        print("### REFUSED -- b242's banked per-mode points are not on disk.")
        return 1
    pts = json.load(io.open(B242PTS, encoding="utf-8"))
    lmr = run_LmR()
    if len(lmr) != 6:
        print("### REFUSED -- could not read all six L-R values from the run file (got %d)."
              % len(lmr))
        return 1

    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b245 -- THE T-E DIAGNOSTIC. ### RUN AFTER THE BRANCH AND IT DOES NOT TOUCH IT.")
    rec("=" * 104)
    rec("### THE BRANCH STANDS AS THE RUN RECORDED IT: ### **(DISSONANT-BEYOND)**, by the rule")
    rec("### banked before any number. ### THIS TOOL NAMES THE TERM; IT DOES NOT RE-BRANCH.")
    rec("### CEILING (b15): a finite-place-set object at a finite cutoff decides nothing global.")
    rec("### h2 UNCHANGED. ### NOTHING DEPOSITS.")
    rec("")
    rec("### THE HYPOTHESIS: b38's bank ran at NMODE = 10; RULE MODES K1 runs this act at")
    rec("### NMODE = 7. ### The three withheld modes are 7, 8 and 9, and b242 banked them")
    rec("### INDEPENDENTLY. ### If they are the whole deviation, the columns below agree.")
    rec("")
    rec("  %-5s %16s %16s %16s %14s" % ("a^2", "|run - bank|", "tr[7]+tr[8]+tr[9]",
                                        "difference", "verdict"))
    worst = 0.0
    for c in CELLS:
        rb, db = BANK38[c]
        dev = abs(lmr[c] - (rb - db))
        tr = pts["trunc|%s" % c]["tr"]
        withheld = tr[7] + tr[8] + tr[9]
        d = abs(dev - withheld)
        worst = max(worst, d)
        rec("  %-5s %16.9f %16.9f %16.3e %14s"
            % (c, dev, withheld, d, "MATCH" if d < 5e-5 else "### NO"))
    rec("")
    rec("  ### max |difference| = %.3e" % worst)
    rec("  ### THE RESIDUAL TOLERANCE IS 5e-5 AND NOT TIGHTER FOR ONE STATED REASON:")
    rec("  ### b38's bank prints `resid47` to FOUR DECIMALS, so 5e-5 is the bank's own")
    rec("  ### rounding floor and nothing finer is readable from it.")
    rec("")
    rec("-" * 104)
    rec("WHAT THIS MEANS, AND WHAT IT DOES NOT.")
    rec("-" * 104)
    if worst < 5e-5:
        rec("### ### **SUSPECT 1 IS INDICTED AND CONVICTED, FIRST IN THE REGISTERED ORDER.**")
        rec("### ### T-E's FAILURE IS THE K1 TRUNCATION, TO THE BANK'S OWN ROUNDING FLOOR.")
        rec("### The deviation is EXACTLY the three sub-floor modes b38 summed and K1 excludes --")
        rec("### and b242 measured those same modes to be numerically meaningless: their")
        rec("### eigenvalues sit at 1e-16, and including them degrades the NQ-spread by 61x-249x.")
        rec("### ### **SO T-E DID NOT DETECT INSTRUMENT DRIFT. IT DETECTED THE RULING DOING")
        rec("### ### EXACTLY WHAT IT WAS RULED TO DO.**")
        rec("### ### AND THE EXECUTOR'S OWN ERROR, NAMED: ### **T-E WAS MIS-SPECIFIED AT")
        rec("### ### REGISTRATION.** ### I registered a cross-check against a bank computed at a")
        rec("### ### MODE COUNT THE RULING HAD JUST CHANGED, and set its tolerance at 1e-5 as")
        rec("### ### though the two were comparable. ### THEY ARE NOT, AND I SHOULD HAVE SEEN IT:")
        rec("### ### b244 is the act that changed NMODE from 10 to 7, and I wrote both files.")
        rec("### ### **THE BRANCH STANDS. ### A BANKED RULE IS NOT REVISED BECAUSE THE EXECUTOR")
        rec("### ### LATER UNDERSTANDS WHY IT FIRED.**")
    else:
        rec("### ### THE HYPOTHESIS IS REFUTED. ### The deviation is NOT the withheld modes,")
        rec("### ### and an UNACCOUNTED TERM STANDS AT FULL PROMINENCE. ### Suspect 2 (the M-4")
        rec("### ### term) and then suspect 3 (the three-normalizations species) follow in the")
        rec("### ### registered order.")
    rec("=" * 104)
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)
    return 0


if __name__ == "__main__":
    sys.exit(main())
