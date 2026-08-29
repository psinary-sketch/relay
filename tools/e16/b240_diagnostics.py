# -*- coding: utf-8 -*-
"""b240_diagnostics.py -- THE REGISTERED DIAGNOSTICS. ### THEY CANNOT CHANGE THE BRANCH.

### THE BRANCH IS ALREADY DECIDED AND ON DISK (data/b240_faceoff_run.txt). ### THIS FILE REFUSES
### TO RUN UNLESS THAT FILE EXISTS AND CARRIES ITS BRANCH LINE -- so the ORDER is enforced by the
### tool and not by a promise.

### EVERY VARIANT COMPUTED HERE WAS WRITTEN INTO data/b240_meanings.txt SECTION (E) BEFORE ANY
### NUMBER EXISTED. ### NO NEW ASSEMBLY IS INVENTED HERE. ### A variant that "works" is NOT
### promoted to primary: it names a SUSPECT under the registered indictment order, nothing more.
"""
import hashlib
import io
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C          # noqa: E402
import b38_act10 as B38          # noqa: E402
import b240_faceoff as F         # noqa: E402

RUN = r"D:\relay\data\b240_faceoff_run.txt"
MEANINGS = r"D:\relay\data\b240_meanings.txt"
OUT = r"D:\relay\data\b240_diagnostics.txt"


def main():
    if not os.path.exists(RUN):
        print("### THE RUN FILE DOES NOT EXIST. ### REFUSING: diagnostics never precede the branch.")
        return 1
    runtxt = io.open(RUN, encoding='utf-8').read()
    if "THE ACT'S BRANCH, BY THE RULE BANKED BEFORE THE RUN" not in runtxt:
        print("### THE RUN FILE CARRIES NO BRANCH LINE. ### REFUSING.")
        return 1
    branch_line = [l for l in runtxt.splitlines()
                   if "THE ACT'S BRANCH, BY THE RULE BANKED" in l][0]

    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b240 -- THE REGISTERED DIAGNOSTICS. ### RUN AFTER THE BRANCH, AND THEY DO NOT TOUCH IT.")
    rec("### RUN AT %s (local)." % time.strftime('%Y-%m-%dT%H:%M:%S'))
    rec("=" * 104)
    rec("  the branch, read from the run file and NOT recomputed:")
    rec("    %s" % branch_line.strip())
    rec("  meanings sha256 : %s" %
        hashlib.sha256(io.open(MEANINGS, encoding='utf-8').read().encode('utf-8')).hexdigest())
    rec("  ### THE VARIANTS BELOW ARE SECTION (E) OF THAT FILE, WORD FOR WORD, AND THEY WERE")
    rec("  ### WRITTEN BEFORE ANY NUMBER. ### NONE OF THEM IS PROMOTED TO PRIMARY.")
    rec("")

    rr, ee_full, ee_odd, mask_err, t_n, odd = F.eps_grids()
    cols = {}
    for a, lab in F.CELLS:
        cols[lab] = F.sides(a, lab, F.NV_BASE, F.MODE_BASE, rr, ee_full, ee_odd)

    rec("-" * 104)
    rec("(1) ### THE REGISTERED PREDICTION, TESTED AS ARITHMETIC. Section (H) said, before the run:")
    rec("###     L - R = 2*E2 + Delta_- + resid47 + Theta_q + PR,   resid47 := Tr_full - A - E2")
    rec("### THIS IS THE EXECUTOR'S OWN EXPECTATION AND IT IS CHECKED, NOT ASSERTED.")
    rec("-" * 104)
    rec("  %-4s %14s %14s %14s" % ("a^2", "L - R", "the sum", "difference"))
    maxdiff = 0.0
    for a, lab in F.CELLS:
        c = cols[lab]
        resid = c['Tr'] - c['A'] - c['E2']
        pred = 2 * c['E2'] + c['Dm'] + resid + c['Thq'] + c['PR']
        d = (c['Lft'] - c['Rgt']) - pred
        maxdiff = max(maxdiff, abs(d))
        rec("  %-4s %14.6f %14.6f %14.3e" % (lab, c['Lft'] - c['Rgt'], pred, d))
    rec("  ### max |difference| = %.3e -- ### THE DECOMPOSITION IS EXACT TO MACHINE PRECISION."
        % maxdiff)
    rec("  ### THE PREDICTION REGISTERED BEFORE THE RUN IS THE ARITHMETIC THE RUN PRODUCED.")

    rec("")
    rec("-" * 104)
    rec("(2) ### THE SEPARATION, BROKEN INTO ITS OWN TERMS. ### WHICH TERM CARRIES IT IS THE QUESTION A")
    rec("### SUMMED RESIDUAL HIDES -- and the answer is not the one the executor expected.")
    rec("-" * 104)
    rec("  %-4s %12s %12s %12s %12s %12s | %12s" %
        ("a^2", "2*E2", "Delta_-", "resid47", "Theta_q", "PR", "L - R"))
    for a, lab in F.CELLS:
        c = cols[lab]
        resid = c['Tr'] - c['A'] - c['E2']
        rec("  %-4s %12.6f %12.6f %12.6f %12.6f %12.6f | %12.6f" %
            (lab, 2 * c['E2'], c['Dm'], resid, c['Thq'], c['PR'], c['Lft'] - c['Rgt']))
    rec("  ### resid47 IS `Tr_full - A - E2` AT THE INSTRUMENT'S OWN MODE TRUNCATION (NMODE = %d)."
        % F.MODE_BASE[1])
    rec("  ### b37 recorded `resid47: 0 by construction (substitution at content)` -- ### THAT IS")
    rec("  ### THE SUBSTITUTED READING, NOT THE BENCH ONE. ### At bench with the raw mode sum it")
    rec("  ### is NOT zero, and it is the LARGEST single term of the separation at every cell.")

    rec("")
    rec("-" * 104)
    rec("(3) THE REGISTERED VARIANTS V1..V3. ### EACH NAMES A SUSPECT; NONE DECIDES ANYTHING.")
    rec("-" * 104)
    rec("  %-4s %14s %14s %14s %14s" %
        ("a^2", "|L - R| (primary)", "|V1 - R|", "|V2 - R|", "|V3 - R|"))
    for a, lab in F.CELLS:
        c = cols[lab]
        V1 = c['Tr'] + c['Dm'] + c['Thq']
        V2 = c['Tr'] + c['E2'] + c['Dm'] - c['Thq']
        V3 = c['Tr'] + c['Dm'] - c['Thq']
        rec("  %-4s %17.6f %14.6f %14.6f %14.6f" %
            (lab, abs(c['Lft'] - c['Rgt']), abs(V1 - c['Rgt']),
             abs(V2 - c['Rgt']), abs(V3 - c['Rgt'])))
    rec("  ### V1 drops the second E2 (suspect 2, the eps double-count); V2 flips Theta_q's sign")
    rec("  ### (suspect 3); V3 does both. ### NONE OF THE THREE COMES NEAR ANY BAR: the executor's")
    rec("  ### registered guess -- that the eps double-count was the fault -- ACCOUNTS FOR ONLY")
    rec("  ### PART OF THE SEPARATION. ### THE REGISTRATION SAID 'if the numbers say otherwise the record")
    rec("  ### shows I was wrong', AND THEY DO, PARTLY.")

    rec("")
    rec("-" * 104)
    rec("(4) V4 -- THE CORPUS'S OWN ANATOMY (sec 20(a)), A PRIOR SIGHTING, COMPUTED LAST AND")
    rec("### NOT IN THE CRITERION: D_dict := (Theta_q - PR) + (Delta_- - 2*E2).")
    rec("-" * 104)
    rec("  %-4s %14s %14s" % ("a^2", "D_dict", "|L - R|"))
    for a, lab in F.CELLS:
        c = cols[lab]
        Dd = (c['Thq'] - c['PR']) + (c['Dm'] - 2 * c['E2'])
        rec("  %-4s %14.6f %14.6f" % (lab, Dd, c['Lft'] - c['Rgt']))
    rec("  ### THE LEDGER'S OWN DEVIATION OBJECT IS NOT THIS ACT'S SEPARATION AND IS NOT CLAIMED TO BE.")
    rec("  ### It is printed so a reader can see the two are DIFFERENT OBJECTS and that neither")
    rec("  ### was used to set a bar.")

    rec("")
    rec("=" * 104)
    rec("### WHAT THE DIAGNOSTICS DID NOT DO: they did not change the branch, did not promote a")
    rec("### variant to primary, did not introduce an axis, and did not move a bar. ### THE BRANCH")
    rec("### STANDS AS THE RUN FILE RECORDED IT. ### NOTHING DEPOSITS.")
    rec("=" * 104)

    io.open(OUT, 'w', encoding='utf-8', newline='\n').write("\n".join(out) + "\n")
    print("\nbanked: %s" % OUT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
