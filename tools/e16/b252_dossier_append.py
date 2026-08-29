# -*- coding: utf-8 -*-
"""b252 -- APPEND THE FACT TO THE M-2-inf DOSSIER. ### APPEND ONLY.

### ### **b251's TEXT IS NOT REWRITTEN, NOT DELETED, NOT BACKDATED** (b240's append-only law).
### The dossier's section (5) asked, in b251's own words, *"If the mode sum converges to something,
### WHAT? b251 did not establish that it converges at all"*. ### **b252 ANSWERS THAT ITEM WITH A
### MEASUREMENT -- NOT WITH A DERIVATION, AND THE APPENDIX SAYS WHICH.**
"""
import io

PATH = r"D:\relay\data\b251_m2inf_dossier.txt"

APPENDIX = u"""
====================================================================================================
### **APPENDIX, APPENDED AT b252 (2026-08-29). ### THE TEXT ABOVE IS b251's AND IS UNCHANGED.**
====================================================================================================
### Section (5) above listed, as item (ii), what would move this dossier: *"A derivation that
### `Tr_inf = A + E2` (or that it fails), at content. ### If the mode sum converges to something,
### **WHAT?** ### b251 did not establish that it converges at all."*
### ### **b252 ANSWERS THAT ITEM -- WITH A MEASUREMENT, NOT A DERIVATION. ### THE DISTINCTION IS
### ### THE FIRST THING THIS APPENDIX SAYS, BECAUSE IT IS WHAT LIMITS EVERYTHING BELOW IT.**

### **THE FACT, WITH ITS TABLE:** ### the corr-weighted mode sum was measured at extended precision
### to `N = 20` (prolate index 40, `mu_20 = 7.162e-80`), past the float64 veil, at all six cells.
### ### ### **BRANCH (DIVERGES/WANDERS): `S_N` DOES NOT SETTLE AT ANY CELL**, missing the
### ### ### registered 1%-of-`|S_N|` settling threshold by **7.5x to 11.3x**.
### ### **`n * w(n)` RISES AND FLATTENS TOWARD A NONZERO CONSTANT AT EVERY CELL** (1.876, 1.194,
### ### 0.949, 0.635, 0.601, 0.533), i.e. ### **`w(n) ~ C/n`, WHOSE SUM DIVERGES LOGARITHMICALLY**,
### and the log form checks against `S_20 - S_10` to about 6%.
### ### **AND THE LIMIT ON THAT, IN THE SAME BREATH: THIS IS A MEASURED DECAY LAW OVER n = 0..20,
### ### NOT A THEOREM. ### b242's RULE GOVERNS -- A MEASURED RATE IS NOT A TAIL BOUND.** ### The
### divergence is the reading the measured form implies; ### **it is not proved and is not banked
### as proved.**

### **WHAT THIS DOES TO THE THREE READINGS -- STATED AS BEARING, NOT AS A RULING.**
### ### **THIS DOSSIER IS STILL OPEN AND b252 STILL CHOOSES NOTHING (b237).**
###   **(R-I) THE QUADRATURE IS THE OBJECT.** ### The measurement is CONSISTENT with it: the mode
###     sum would then be a construction that does not converge to the object, which is a strong
###     statement about the construction and none about the object.
###   **(R-II) THE MODE SUM IS THE OBJECT.** ### ### **THE MEASUREMENT BEARS HARDEST HERE: AN
###     OBJECT DEFINED AS THE LIMIT OF A SUM THAT DOES NOT SETTLE IS NOT DEFINED BY THAT LIMIT.**
###     ### That is bearing, not refutation -- a different summation or regularization could still
###     ### denote, and b252 did not test one.
###   **(R-III) THEY COMPUTE DIFFERENT OBJECTS.** ### Untouched by the measurement either way.

### ### **AND THE NAME `Delta_2real` MUST NOW BE READ WITH CARE.** ### b251 defined it as
### `Tr_inf - A - E2` and computed it at `N = 10`. ### ### **THE MEASUREMENT DOES NOT FIND A
### ### `Tr_inf` FOR IT TO BE. ### b251's NUMBER IS A PARTIAL SUM AT `N = 10`, AND THE NAME
### ### PRESUMED A LIMIT.** ### **b251's BRANCH IS NOT RE-VERDICTED** -- a banked branch is not
### re-verdicted because a later act explains it (b246's rule) -- ### **BUT ANY FUTURE ACT QUOTING
### `Delta_2real` MUST QUOTE ITS `N` WITH IT.**

### ### **AND A SECOND FACT b251 COULD NOT HAVE HAD.** ### b38's float64 eigenvectors for `n >= 7`
### are ### **NOISE** (b242's `n_last = 6`, confirmed here from the other side: b38's `tr[n]` for
### `n >= 7` collapse by up to 62x and wander non-monotonically while the clean values decay
### smoothly). ### **SO b251's `TrTail(7)` OF 0.0805 AT `a^2 = 2` WAS BUILT FROM NOISE; THE CLEAN
### VALUE OVER THE SAME MODES IS 0.801 -- TEN TIMES LARGER -- AND OVER `n = 7..20` IT IS 2.024.**
### ### **THIS WAS REGISTERED AS A POSSIBLE FINDING IN b252's MEANINGS FILE BEFORE ANY COMPUTATION
### ### RAN, AND IT IS FILED AS A FACT ABOUT b251's INPUTS, NOT AS A CHARGE AGAINST b251.**

### **THE CARD, IN THE SHAPE THE BANKED BRANCH GIVES IT -- ### CITATION-SHAPED, AND NOT DECIDED.**
### The meanings file fixed, before any number: *"(DIVERGES/WANDERS) ... MEANS: only the quadrature
### reading denotes, and the card's ruling is citation-shaped."*
### ### **THE RULING REQUESTED OF THE AUTHOR IS THEREFORE:** ### *given that the corr-weighted mode
### sum does not settle on the measured range and its terms go like `C/n`, which construction does
### `W_inf` in `T + Q = W_inf - W_primes` denote?* ### ### **THE QUESTION IS UNCHANGED FROM b251.
### ### WHAT HAS CHANGED IS THAT IT NOW CITES A TABLE.**
### ### **b252 EXPRESSES NO PREFERENCE, CLOSES NOTHING, AND DEPOSITS NOTHING.**
### SOURCES: `data/b252_mode_sum_limit.txt`; `data/b252_run.txt`; `data/b252_meanings.txt`
### (sha256 `0c562286...77be`, banked before any computation).
====================================================================================================
"""


def main():
    t = io.open(PATH, encoding="utf-8").read()
    if "APPENDED AT b252" in t:
        print("  ### already appended, untouched.")
        return
    # ### the prefix must survive byte-for-byte; verified after the write.
    io.open(PATH, "w", encoding="utf-8", newline="\n").write(t + APPENDIX)
    back = io.open(PATH, encoding="utf-8").read()
    ok = back.startswith(t) and back.endswith(APPENDIX)
    print("  APPENDED: %d bytes added" % len(APPENDIX))
    print("  prefix byte-for-byte intact : %s" % ("YES" if back.startswith(t) else "### NO"))
    print("  read-back ok                : %s" % ("YES" if ok else "### NO"))


if __name__ == "__main__":
    main()
