# -*- coding: utf-8 -*-
"""b255 -- FILE THE INDEX KEY. ### APPEND ONLY.
### `limit-profile` was queried BEFORE any step and returned NO KEY.
"""
import io

PATH = r"D:\relay\tools\banked_index.py"

KEY_ANCHOR = ("    'the-balance': ['the balance', 'Delta_- - E2 vs PR - Theta_q', "
              "'E2even vs Theta_q - PR',\n"
              "                    'the balance residual', 'the two Delta_- realizations'],\n")
KEY_NEW = (
    "    'limit-profile': ['the limit profile', 'the cutoff ladder', 'the balance along a^2',\n"
    "                      'the junction sawtooth', 'the staircase sawtooth', 'sixteen cells'],\n"
)

ROW_ANCHOR = ("     'data/b254_fourth_face_off.txt; data/b254_run.txt; data/b246_two_tails.txt'),\n")
ROW_NEW = (
    "    ('limit-profile', 'b255 (bounded bench act; the ladder priced before it was fixed)',\n"
    "     'the balance measured along the cutoff axis over SIXTEEN cells, a^2 = 2 to 100. '\n"
    "     '### **THE PRICING RAN FIRST AND KEPT NO BALANCE VALUE**, so the ladder was chosen by '\n"
    "     'AFFORDABILITY and the order on disk makes that checkable. ### Four cost walls measured: '\n"
    "     '**(W1) the eps rho-grid ended at a^2 = 12.001 AND FAILED SILENTLY** -- np.interp clamps '\n"
    "     'rather than raising, so every cell past 12 would have carried a wrong E2 with no error; '\n"
    "     'rebuilt to rho_max 100.001, EPS_NRHO 240 -> 445. **(W2) Theta_q scaling_matrix is dense '\n"
    "     'N = p^(2n): a^2 = 100 -> N = 4096, ~22 s; a^2 = 128 -> N = 16384, 2.1 GB, >= 1690 s for '\n"
    "     'p = 2 alone -- REFUSED ON COST, recorded before any value existed.**',\n"
    "     '### **BRANCH (MIXED), AND THE SPLIT IS THE FINDING: |resid(A)| ALTERNATES GROW/SHRINK UP '\n"
    "     'TO a^2 = 20, THEN EIGHT CONSECUTIVE SHRINKS TO a^2 = 100** (1.001813 down to 0.486920, '\n"
    "     'more than halving). ### **(RELAXES) IS NOT TAKEN: the banked rule forbids reading an '\n"
    "     'oscillating stretch as a relaxation with an excuse.** ### **THE STRUCTURAL FINDING: THE '\n"
    "     'JUNCTION (PR - Theta_q) IS A SAWTOOTH LOCKED TO b17 STAIRCASE.** ### Between staircase '\n"
    "     'steps it RISES -- six transitions, six rises, no exceptions; at steps it FALLS at six of '\n"
    "     'nine, and on the upper ladder (a^2 >= 20) at ALL FOUR steps while rising at ALL FIVE '\n"
    "     'non-steps. ### Mechanism read off the columns: PR rises smoothly toward 1 while Theta_q '\n"
    "     'rises in JUMPS, gaining a level at each step. ### E2even by contrast FALLS MONOTONICALLY '\n"
    "     'at all sixteen cells. ### **NO SIGN-EVENT, AND THE REASON IS STRUCTURAL: resid = '\n"
    "     '-(E2even + junction) with BOTH terms positive at every cell, and a sum of two positives '\n"
    "     'cannot cross zero.** ### **THE EXECUTOR REGISTERED (RELAXES) ON THE LOWER LADDER AND '\n"
    "     'DECLINED THE UPPER -- THAT IS THE REVERSE OF WHAT HAPPENED, and the falsifier was too '\n"
    "     'coarse to catch it; both reported.** ### G-REPRO debt of the grid rebuild REGISTERED '\n"
    "     'BEFORE IT WAS PAID and PAID: worst deviation 5.64e-06 against b254 six cells, inside the '\n"
    "     '1e-4 band by 18x; b254 NOT re-verdicted. ### **NO FIT, NO SLOPE, NO EXTRAPOLATED LIMIT '\n"
    "     'IS BANKED (b242 governs). ### THE WORD LIMIT IS IN THE TITLE AND IN NONE OF THE '\n"
    "     'CONCLUSIONS.** ### Cell-species said: S4 = (2,3,5) is FIXED, so 7 never enters -- the '\n"
    "     'ladder measures powers of a fixed prime set, not a growing place set',\n"
    "     'data/b255_limit_profile.txt; data/b255_run.txt; data/b255_pricing.txt; '\n"
    "     'data/b255_meanings.txt; reports/2026-08-29-the-limit-profile.md'),\n"
)


def main():
    txt = io.open(PATH, encoding="utf-8").read()
    if "'limit-profile'" in txt:
        print("  ### already filed, untouched.")
        return
    for name, anchor in (("KEYS", KEY_ANCHOR), ("ROWS", ROW_ANCHOR)):
        if txt.count(anchor) != 1:
            print("  ### REFUSED: %s anchor hit %d times." % (name, txt.count(anchor)))
            return
    txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW)
    txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW)
    io.open(PATH, "w", encoding="utf-8").write(txt)
    print("  FILED: limit-profile.")


if __name__ == "__main__":
    main()
