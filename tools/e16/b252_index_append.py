# -*- coding: utf-8 -*-
"""b252 -- FILE THE INDEX KEY. ### APPEND ONLY.
### `mode-sum-limit` was queried BEFORE any computation and returned NO KEY. ### Keyed ON FILING.
"""
import io

PATH = r"D:\relay\tools\banked_index.py"

KEY_ANCHOR = ("    'two-realizations': ['the two-realizations term', 'delta_2real', 'm-2-inf', "
              "'m2inf',\n"
              "                         'the archimedean identity question', "
              "'quadrature versus mode sum'],\n")
KEY_NEW = (
    "    'mode-sum-limit': ['the mode sum limit', 'does the mode sum converge', 'tr[n] decay',\n"
    "                       'the corr-weighted mode sum', 'w(n) ~ C/n', 'the archimedean trace "
    "series'],\n"
)

ROW_ANCHOR = ("     'data/b251_m2inf_dossier.txt; data/b251_meanings.txt; "
              "data/b251_third_face_off.txt'),\n")
ROW_NEW = (
    "    ('mode-sum-limit', 'b252 (bounded bench act; the b249 instrument extended)',\n"
    "     'DOES the corr-weighted archimedean mode sum `Tr` converge, and to what? ### Measured at '\n"
    "     'EXTENDED PRECISION to **N = 20 (prolate index 40, mu_20 = 7.162e-80)**, past the '\n"
    "     'float64 veil, at all six cells, with the quadrature object `A + E2` computed beside it '\n"
    "     'from ITS OWN owners. ### Instrument: b249 solve scheme at dps 120 / NQ_e 120, overlaps '\n"
    "     'by Gauss-Legendre with nodes ON THE TRUE SUPPORT and BARYCENTRIC interpolation',\n"
    "     '### **BRANCH (DIVERGES/WANDERS) AT EVERY CELL.** ### `S_N` misses the registered '\n"
    "     '1%-of-|S_N| settling threshold by 7.5x to 11.3x. ### **AND THE THRESHOLD-FREE EVIDENCE "
    "IS '\n"
    "     'THE DECAY LAW: `n*w(n)` RISES AND FLATTENS TOWARD A NONZERO CONSTANT AT EVERY CELL** '\n"
    "     '(1.876, 1.194, 0.949, 0.635, 0.601, 0.533), i.e. **w(n) ~ C/n**, whose sum diverges '\n"
    "     'logarithmically; the log form checks against S_20 - S_10 to about 6%. ### **LIMIT IN "
    "THE '\n"
    "     'SAME BREATH: A MEASURED DECAY LAW OVER n = 0..20 IS NOT A THEOREM -- b242 rule, a '\n"
    "     'measured rate is not a tail bound. ### THE DIVERGENCE IS THE READING THE FORM IMPLIES '\n"
    "     'AND IS NOT BANKED AS PROVED.** ### **THE EXACT FACT `A_n(0) = 1` FOR EVERY n WAS "
    "DERIVED '\n"
    "     'FROM SOURCE BEFORE THE INSTRUMENT WAS BUILT AND THE INSTRUMENT REPRODUCES IT TO "
    "3.0e-13**; '\n"
    "     'G-EQ 4.4e-120; G-REPRO-A 3.076e-15 (machine precision); G-SELF agrees to 8.5e-16 up to '\n"
    "     'n = 15 and **COVERS ONLY THAT RANGE, WHICH THE ACT SAYS RATHER THAN LETTING THE GATE "
    "NAME '\n"
    "     'IMPLY MORE**. ### **AND THE FINDING REGISTERED IN ADVANCE AS AN EXPECTED FAILURE: b38 '\n"
    "     'FLOAT64 EIGENVECTORS FOR n >= 7 ARE NOISE** -- its tr[n] collapse by up to 62x and "
    "wander '\n"
    "     'non-monotonically while the clean values decay smoothly (b242 n_last = 6, seen from the '\n"
    "     'other side). ### **CONSEQUENCE FOR b251, FILED AS A FACT NOT A RE-VERDICT: its "
    "TrTail(7) '\n"
    "     'of 0.0805 at a^2 = 2 was built from noise; the clean value over the same modes is 0.801, '\n"
    "     'TEN TIMES LARGER, and over n = 7..20 it is 2.024. ### b251 BRANCH STANDS AS BANKED "
    "(b246 '\n"
    "     'rule).** ### **AND `Delta_2real := Tr_inf - A - E2` HAS NO LIMIT TO BE: b251 number is a '\n"
    "     'PARTIAL SUM AT N = 10 AND THE NAME PRESUMED A LIMIT** -- any future act quoting it must '\n"
    "     'quote its N. ### **NO RULING ON M-2-inf AND NO READING CHOSEN**; the dossier is APPENDED '\n"
    "     'with the fact, prefix byte-for-byte intact, and the card is CITATION-SHAPED per the '\n"
    "     'pre-banked MEANS. ### b250 envelope NAMED AND NEVER APPLIED, on b251 precedent',\n"
    "     'data/b252_mode_sum_limit.txt; data/b252_run.txt; data/b252_meanings.txt; '\n"
    "     'data/b251_m2inf_dossier.txt; reports/2026-08-29-the-mode-sums-limit.md'),\n"
)


def main():
    txt = io.open(PATH, encoding="utf-8").read()
    if "'mode-sum-limit'" in txt:
        print("  ### already filed, untouched.")
        return
    for name, anchor in (("KEYS", KEY_ANCHOR), ("ROWS", ROW_ANCHOR)):
        if txt.count(anchor) != 1:
            print("  ### REFUSED: %s anchor hit %d times." % (name, txt.count(anchor)))
            return
    txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW)
    txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW)
    io.open(PATH, "w", encoding="utf-8").write(txt)
    print("  FILED: mode-sum-limit.")


if __name__ == "__main__":
    main()
