# -*- coding: utf-8 -*-
"""b253 -- FILE THE INDEX KEYS. ### APPEND ONLY.
### `m2inf-ruling` and `quadrature-binding` were queried BEFORE any step and both returned NO KEY.
"""
import io

PATH = r"D:\relay\tools\banked_index.py"

KEY_ANCHOR = ("    'mode-sum-limit': ['the mode sum limit', 'does the mode sum converge', "
              "'tr[n] decay',\n"
              "                       'the corr-weighted mode sum', 'w(n) ~ C/n', "
              "'the archimedean trace series'],\n")
KEY_NEW = (
    "    'm2inf-ruling': ['the m2inf ruling', 'rule m-2-inf', 'q1', 'the r-label match',\n"
    "                     'which construction denotes', 'the quoted-n law'],\n"
    "    'quadrature-binding': ['the quadrature binding', 'T.value := A + E2 - Delta_-',\n"
    "                           'the re-bound realization', 'the mode sum demoted'],\n"
)

ROW_ANCHOR = ("     'data/b252_mode_sum_limit.txt; data/b252_run.txt; data/b252_meanings.txt; '\n"
              "     'data/b251_m2inf_dossier.txt; reports/2026-08-29-the-mode-sums-limit.md'),\n")
ROW_NEW = (
    "    ('m2inf-ruling', 'b253 (filings + one ruled re-binding at support-voice)',\n"
    "     \"the author's RULE M-2-inf Q1 executed: the QUADRATURE construction (left_side's \"\n"
    "     'one-axis integral) is the archimedean object the identity left column denotes; the '\n"
    "     'per-cell realization of C2+D1 RE-BOUND to it; the mode sum (trace_modes) DEMOTED to a '\n"
    "     'truncation diagnostic under the standing QUOTED-N law. ### **THE DEFINITION DOES NOT '\n"
    "     'MOVE -- C2, D1, RULE Q O1 and RULE MODES K1 all stand; ONLY THE PER-CELL '\n"
    "     \"REALIZATION'S BINDING MOVED.** ### File E docstring only: comment-stripped HEAD vs \"\n"
    "     'work = **19 code lines both sides, IDENTICAL**. ### CORRESPONDENCE row 94, six cells, '\n"
    "     'read back',\n"
    "     '### **THE R-LABEL MATCH IS HALTED AS AMBIGUOUS AND ROUTED TO THE AUTHOR.** ### Q1 '\n"
    "     'wording is R-I headline verbatim, but Q1 DECLINES R-I consequent (it demotes the mode '\n"
    "     'sum to a DIAGNOSTIC, not an APPROXIMATION, and b252 refuted the approximation reading), '\n"
    "     \"while the ferry OWN disclosed consequence -- 'removes ... BY DEFINITION' -- is R-III's \"\n"
    "     \"('THE SHORTFALL IS AN ARTEFACT OF THE PAIRING RATHER THAN A DEFICIT'). ### **WHAT \"\n"
    "     'TURNS ON IT: UNDER R-I b254 NUMBERS ARE A DEFICIT STILL OWED; UNDER R-III THEY ARE THE '\n"
    "     'RESIDUE OF A PAIRING ERROR. ### THE TWO READINGS ASSIGN OPPOSITE MEANINGS TO b254 '\n"
    "     'ENTIRE TABLE.** ### b237 governs -- an executor does not settle a definition. '\n"
    "     '### R-II is excluded cleanly (Q1 names the quadrature; R-II names the mode sum). '\n"
    "     '### **THE HALT HALTS THE MATCH ONLY: the re-binding is derived from Q1 OWN WORDS and '\n"
    "     'the owners lines and does NOT consume the R-label, so every other component executed '\n"
    "     'in full.** ### **AND THE EXECUTOR REGISTERED THE AMBIGUITY BEFORE WEIGHING THE '\n"
    "     'DOSSIER TEXT** (registration section (D)). ### Q1 is DEFINITIONAL ONLY; b252 '\n"
    "     'divergence remains a BENCH READING. ### NO FACE-OFF RAN. ### M-2..M-5 open',\n"
    "     'data/b253_m2inf_ruling.txt; data/b253_registration_2026-08-29.txt; '\n"
    "     'Interfaces/FiniteInstanceIdentity.lean; CORRESPONDENCE.md row 94; '\n"
    "     'reports/2026-08-29-the-m2inf-ruling.md'),\n"
    "    ('quadrature-binding', 'b253 (derived from the owners lines, shown not asserted)',\n"
    "     '### **THE RE-BOUND REALIZATION: `T.value := A + E2 - Delta_-`**, `A` being '\n"
    "     '`b38_act10.left_side` one-axis integral in which NO mode index appears. ### DERIVED: '\n"
    "     'from `b36_act8.py:184` `resid47 = Tr_full - (A + E2)`, i.e. (i) `Tr_full = A + E2 + '\n"
    "     'resid47`; with the ruled binding (ii) `T.value := Tr_full + E2 - Delta_-`, substituting '\n"
    "     'construction for construction gives (iii) `T.value := A + E2 - Delta_-`. ### The '\n"
    "     'combination is UNCHANGED; only which construction realizes the archimedean trace moved',\n"
    "     '### ### **AND THE COST DISCLOSED IN THE EXECUTOR OWN VOICE, WHICH THE FERRY DISCLOSURE '\n"
    "     'DID NOT NAME: `T.value^OLD - T.value^NEW = E2 + resid47` -- THE RE-BINDING REMOVES '\n"
    "     '`resid47` *AND ONE `E2` TERM*, because the old assembly carried `E2` TWICE (once in the '\n"
    "     'combination, once inside `Tr_full` comparison against `A + E2`).** ### The ferry '\n"
    "     'disclosed consequence named `resid47` alone (~61-70% of the measured shortfall per b251 '\n"
    "     'table, itself a PARTIAL SUM AT N = 11). ### **THE REGISTRATION BANKED THE DUTY TO CHECK '\n"
    "     'THIS *BEFORE* THE RE-BINDING WAS WRITTEN, SO FINDING IT COULD NOT LOOK LIKE A '\n"
    "     'CONCESSION MADE AFTER THE FACT.** ### In shortfall algebra: OLD `L - R = resid47 + '\n"
    "     '2*E2 - Delta_- + (PR - Theta_q)` (exactly b251 measured decomposition); NEW `L - R = '\n"
    "     'E2 - Delta_- + (PR - Theta_q)`. ### **THE SIZE OF THE REMAINDER IS NOT COMPUTED: THAT '\n"
    "     'IS A FACE-OFF AND b253 RAN NONE. ### IT IS b254 WORK.**',\n"
    "     'data/b253_m2inf_ruling.txt; data/b253_filings.txt; '\n"
    "     'Interfaces/FiniteInstanceIdentity.lean'),\n"
)


def main():
    txt = io.open(PATH, encoding="utf-8").read()
    if "'m2inf-ruling'" in txt:
        print("  ### already filed, untouched.")
        return
    for name, anchor in (("KEYS", KEY_ANCHOR), ("ROWS", ROW_ANCHOR)):
        if txt.count(anchor) != 1:
            print("  ### REFUSED: %s anchor hit %d times." % (name, txt.count(anchor)))
            return
    txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW)
    txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW)
    io.open(PATH, "w", encoding="utf-8").write(txt)
    print("  FILED: m2inf-ruling, quadrature-binding.")


if __name__ == "__main__":
    main()
