# -*- coding: utf-8 -*-
"""b254 -- FILE THE INDEX KEYS. ### APPEND ONLY.
### `fourth-face-off` and `the-balance` were queried BEFORE any step; both returned NO KEY.
"""
import io

PATH = r"D:\relay\tools\banked_index.py"

KEY_ANCHOR = ("    'quadrature-binding': ['the quadrature binding', "
              "'T.value := A + E2 - Delta_-',\n"
              "                           'the re-bound realization', 'the mode sum demoted'],\n")
KEY_NEW = (
    "    'fourth-face-off': ['the fourth face-off', 'the identity at cells', 'the bench shadow',\n"
    "                        'the imbalance profile', 'L - R under the re-binding'],\n"
    "    'the-balance': ['the balance', 'Delta_- - E2 vs PR - Theta_q', 'E2even vs Theta_q - PR',\n"
    "                    'the balance residual', 'the two Delta_- realizations'],\n"
)

ROW_ANCHOR = ("     'data/b253_m2inf_ruling.txt; data/b253_filings.txt; '\n"
              "     'Interfaces/FiniteInstanceIdentity.lean'),\n")
ROW_NEW = (
    "    ('fourth-face-off', 'b254 (bench computation under the re-bound realization)',\n"
    "     'the identity measured at six cells as the TWO-TERM balance its algebra now is: '\n"
    "     'L := (A + E2 - Delta_-) + (-Theta_q), R := A - PR, so L - R = (E2 - Delta_-) + '\n"
    "     '(PR - Theta_q) -- the `A` cancelling identically. ### **THAT COMPOSITION IS '\n"
    "     'ALGEBRAIC-RESTATEMENT AND WAS LABELLED SO IN THE HASH-GATED MEANINGS FILE BEFORE THE '\n"
    "     'RUN; the evidence is the SIZES, SIGNS and CELL-PROFILES only.** ### Every term also '\n"
    "     'tabulated alone; G-INDEP structural; G-STAB at b38 TRIPLE plus one refinement NQ=1100',\n"
    "     '### **BRANCH (IMBALANCED), AT EVERY CELL, UNDER *BOTH* Delta_- REALIZATIONS.** '\n"
    "     '### Under (A), the odd eps-MASK (the ruling rider names it): residual -1.001814 to '\n"
    "     '-0.800154, beyond bars by FOURTEEN ORDERS. ### Under (B), the odd TRACE modes '\n"
    "     '(b36_act8.py:172, quotable only as Dneg(N = 11, float64 modes, suspect above n = 6)): '\n"
    "     'residual -0.061581 to -0.533354, beyond bars by 1.50x to 31x -- **and the 1.50x at '\n"
    "     'a^2 = 2 is reported as marginal rather than rounded away.** ### **SIGN UNIFORMLY '\n"
    "     'NEGATIVE: SIX CELLS, TWO REALIZATIONS, TWELVE ENTRIES, ONE SIGN.** ### **NEITHER '\n"
    "     'PROFILE IS MONOTONE IN a^2** and the non-monotonicity is reported, not smoothed. '\n"
    "     '### (MIXED) is EXCLUDED and the a^2 = 2 row is why: PR = Theta_q = 0 identically -- '\n"
    "     'the primes vanish -- **and the cell is imbalanced anyway.** ### **THIS IS NOT EVIDENCE '\n"
    "     'AGAINST THE IDENTITY (b15: a finite cell decides NOTHING global) AND NO DEFICIT '\n"
    "     'LANGUAGE IS USED (R-III governs). ### IT IS EVIDENCE ABOUT THE *REALIZATION*.** '\n"
    "     '### h2 stands exactly as open as before',\n"
    "     'data/b254_fourth_face_off.txt; data/b254_run.txt; data/b254_meanings.txt; '\n"
    "     'reports/2026-08-29-the-fourth-face-off.md'),\n"
    "    ('the-balance', 'b254 (both Delta_- realizations computed, neither chosen)',\n"
    "     '`(Delta_- - E2) ?= (PR - Theta_q)` per cell. ### **Delta_- HAS TWO REALIZATIONS AND '\n"
    "     'b246 EXPLICITLY DECLINED TO CHOOSE** -- *\"Its two realizations remain two objects and '\n"
    "     'this act computed both rather than choosing\"*. ### (A) the odd eps-MASK E2odd '\n"
    "     '(b37_act9.eps_masked, what sec 17 and File E name); (B) the odd TRACE modes Dneg '\n"
    "     '(b36_act8.py:172, the only executable assembly -- **and a MODE SUM, hence the object Q1 '\n"
    "     'demoted**). ### b254 computed BOTH and chose NEITHER, on b246 own precedent',\n"
    "     '### **THE ALGEBRAIC REDUCTION, DERIVED BEFORE THE RUN: under (A), Delta_- - E2 = '\n"
    "     'E2odd - (E2even + E2odd) = -E2even, so the balance IS `E2even ?= Theta_q - PR`.** '\n"
    "     '### At a^2 = 2 that is `E2even ?= 0`, and E2even = 1.001814 is a sum of eps sectors -- '\n"
    "     '**the cell cannot balance under (A) unless E2even vanishes, and it does not.** '\n"
    "     '### **A STRUCTURAL FINDING THE BAR COLUMN MADE VISIBLE: under (A) NOTHING IN THE '\n"
    "     'BALANCE IS A MODE SUM** -- E2even, E2odd, PR and Theta_q are all fixed at the eps and '\n"
    "     'carto axes and do not move with NQ at all, so (A) bar is the eps mask certificate '\n"
    "     '(8.882e-16) alone, **and Q1 demotion and b252 divergence are entirely irrelevant to '\n"
    "     'it -- a stronger reason than the rider own.** ### Under (B) the balance DOES carry a '\n"
    "     'mode sum, and with it b252 suspicion and b253 QUOTED-N law. ### **THE TWO '\n"
    "     'REALIZATIONS DISAGREE MATERIALLY (16.3x at a^2 = 2) AND AGREE ON THE VERDICT** -- so '\n"
    "     'the registered condition that would have made the disagreement the act REAL FINDING '\n"
    "     'DID NOT FIRE, and it is not claimed. ### **AND ONE OF THIS ACT OWN THREE CHARGES '\n"
    "     'AGAINST THE RIDER CITATION WAS WITHDRAWN: b246 contains BOTH \"by mode 7\" and '\n"
    "     '\"CONVERGED BY MODE 6\", in two sentences about two quantities. ### THE HARNESS CAUGHT '\n"
    "     'IT BY REFUSING A GATE WHOSE MUST-FAIL FIXTURE PASSED, AND THE HASH-GATED MEANINGS FILE '\n"
    "     'WAS *NOT* EDITED (b244/b246 precedent) -- THE GATE WAS FIXED AND THE ERROR DISCLOSED.**',\n"
    "     'data/b254_fourth_face_off.txt; data/b254_run.txt; data/b246_two_tails.txt'),\n"
)


def main():
    txt = io.open(PATH, encoding="utf-8").read()
    if "'fourth-face-off'" in txt:
        print("  ### already filed, untouched.")
        return
    for name, anchor in (("KEYS", KEY_ANCHOR), ("ROWS", ROW_ANCHOR)):
        if txt.count(anchor) != 1:
            print("  ### REFUSED: %s anchor hit %d times." % (name, txt.count(anchor)))
            return
    txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW)
    txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW)
    io.open(PATH, "w", encoding="utf-8").write(txt)
    print("  FILED: fourth-face-off, the-balance.")


if __name__ == "__main__":
    main()
