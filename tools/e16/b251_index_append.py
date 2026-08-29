# -*- coding: utf-8 -*-
"""b251 -- FILE THE INDEX KEYS. ### APPEND ONLY.

### `third-face-off` and `two-realizations` were queried BEFORE any step ran and both returned
### NO KEY. ### They are keyed here, ON FILING, as the registration said.
"""
import io

PATH = r"D:\relay\tools\banked_index.py"

KEY_ANCHOR = ("    's2-decay-route': ['the s2 decay route', 'eigenvalue decay at fixed c', "
              "'factorial decay',\n"
              "                       'degenerate kernel truncation', 'the zero-import bound'],\n")
KEY_NEW = (
    "    'third-face-off': ['the third face-off', 'third faceoff', 'the columns with m4 paid',\n"
    "                       'the shortfall decomposed', 'the accounting of L - R'],\n"
    "    'two-realizations': ['the two-realizations term', 'delta_2real', 'm-2-inf', 'm2inf',\n"
    "                         'the archimedean identity question', 'quadrature versus mode sum'],\n"
)

ROW_ANCHOR = ("     'data/b250_m4_derivation.txt; data/b250_derivation_checks.txt'),\n")
ROW_NEW = (
    "    ('third-face-off', 'b251 (bench computation + one re-attribution)',\n"
    "     'the bench shortfall L - R computed at six cells with M-4 paid, and decomposed into '\n"
    "     'THREE NAMED PIECES: Delta_2real (the two-realizations term), 2*E2full - Dneg (the '\n"
    "     'RULED BINDING C2+D1 own terms, tabulated though NOT a suspect), and the junction piece '\n"
    "     '(PR - Theta_q). ### Sides under C2+D1, Q := -Theta_q, K1. ### G-INDEP structural (each '\n"
    "     'quantity from its OWN owner in b38_act10, none re-implemented); G-STAB across NQ = 500, '\n"
    "     '700, 900 plus ONE refinement at 1100',\n"
    "     '### **BRANCH (IMPOSTER-NAMED) ON ITS ACCOUNTING LIMB.** ### Delta_2real carries '\n"
    "     '**60.775% to 69.995% of L - R at EVERY cell** -- the dominant term without exception; '\n"
    "     'the third piece 30.005%-34.546%; the junction piece 0.000%-5.874%, the smallest of the '\n"
    "     'three everywhere. ### **MAX LEFTOVER 1.78e-15: NOTHING BEYOND THE THREE NAMED PIECES, '\n"
    "     'SO (DISSONANT-BEYOND) IS NOT TRIGGERED.** ### **LIMB 2 -- the envelope line -- IS '\n"
    "     'STRUCK AS INAPPLICABLE, NOT FALSIFIED, AND THE STRIKE WAS BANKED BEFORE THE RUN**: see '\n"
    "     'two-realizations. ### **THE BARS ARE WIDE AND THE ACT SAYS SO** -- TrTail sits at 43%% '\n"
    "     'to 71%% of the G-STAB bar, so the identification is CONSISTENT rather than SHARP, and '\n"
    "     '**the spread does NOT shrink monotonically with NQ**, so convergence of the mode sum '\n"
    "     'was NOT established. ### **THE FORM IS NOT INDICTED: no act has produced evidence '\n"
    "     'against T + Q = wInf - wPrimes.** ### A number in this act OWN prose was WRONG and gate '\n"
    "     '8 caught it -- the share range was read off the run rounded table by taking the LAST '\n"
    "     'ROW as the minimum instead of scanning the column; corrected to three decimals and '\n"
    "     'disclosed in the bank section (D.1)',\n"
    "     'data/b251_third_face_off.txt; data/b251_run.txt; data/b251_meanings.txt; '\n"
    "     'reports/2026-08-29-the-third-face-off.md'),\n"
    "    ('two-realizations', 'b251 (re-attribution derived before the run)',\n"
    "     '### **WHAT THE FACE-OFF `resid47` TERM ACTUALLY IS.** ### Both owners that state the '\n"
    "     'residue line state the SAME thing -- b38_act10.py:182 `resid = TrN - A - E2N` and '\n"
    "     'b36_act8.py:184 `resid47 = Tr_full - (A + E2)` -- so ### **resid47 IS ALREADY A '\n"
    "     'TWO-REALIZATIONS DIFFERENCE**: the archimedean trace built as a MODE SUM (trace_modes, '\n"
    "     'a corr-weighted dilation overlap) minus the same object built as a QUADRATURE '\n"
    "     '(left_side, a single U-axis integral with NO mode index), less E2. ### The split: '\n"
    "     '**resid47(NMODE) = Delta_2real - TrTail(NMODE)**',\n"
    "     '### **THE NAME `resid47` CONCEALED THE SPECIES. ### IT IS NOT A REMAINDER OR AN ERROR '\n"
    "     'TERM BUT A DISAGREEMENT BETWEEN TWO DEFINITIONS**, filed as **M-2-inf** with a dossier '\n"
    "     'OPENED AND NOT DECIDED (b237), stating three readings (R-I quadrature is the object, '\n"
    "     'R-II mode sum is, R-III they compute different objects and the identity names one) '\n"
    "     'with **NO preference expressed and no evidence distinguishing them**. ### **THE '\n"
    "     'DECOMPOSITION ITSELF IS ALGEBRAIC-RESTATEMENT AND WAS DECLARED SO IN THE HASH-GATED '\n"
    "     'MEANINGS FILE BEFORE THE RUN** -- an identity that cannot fail cannot testify; the '\n"
    "     'evidence is the SIZE question only. ### **AND b250 ENVELOPE WAS REFUSED FOR THIS TAIL '\n"
    "     'BEFORE THE RUN, ON b247 DOUBLE-NAME RULING**: 1.158e-14 bounds sum t(n), an ENDPOINT '\n"
    "     'weight series, while TrTail is a corr-weighted dilation overlap -- two functionals of '\n"
    "     'the same eigenfunctions with NO derivation between them. ### **THE MEASUREMENT SETTLES '\n"
    "     'THE SCALE OF THE ERROR AVOIDED: TrTail IS 2.9e12 TO 7.0e12 TIMES LARGER THAN THE '\n"
    "     'ENVELOPE.** ### b250 is NOT re-verdicted; what was corrected is the ferry APPLICATION '\n"
    "     'of it',\n"
    "     'data/b251_m2inf_dossier.txt; data/b251_meanings.txt; data/b251_third_face_off.txt'),\n"
)


def main():
    txt = io.open(PATH, encoding="utf-8").read()
    if "'third-face-off'" in txt:
        print("  ### already filed, untouched.")
        return
    for name, anchor in (("KEYS", KEY_ANCHOR), ("ROWS", ROW_ANCHOR)):
        if txt.count(anchor) != 1:
            print("  ### REFUSED: %s anchor hit %d times." % (name, txt.count(anchor)))
            return
    txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW)
    txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW)
    io.open(PATH, "w", encoding="utf-8").write(txt)
    print("  FILED: third-face-off, two-realizations.")


if __name__ == "__main__":
    main()
