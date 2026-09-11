# -*- coding: utf-8 -*-
"""b414_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### **AND THE CLAUSES THAT MATTER MOST BOUND A BUILD.** ### Every act from `b403` to `b413`
### could write `.lean files touched : 0` and be done. ### This one cannot. ### So the zero
### clauses are re-aimed: not *nothing was written*, but ### **NOTHING EXISTING WAS EDITED, NO
### ### TERMINAL CARRIES AN AXIOM, AND THE PRIOR PROFILE IS STILL A TRUE BYTE PREFIX.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b414_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b414_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### (K) BAR 9: NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### (K) BAR 9."),
    ("platform calls of any kind", 0, 0, "calls", "### (K) BAR 9."),
    ("files under `outputs/` touched", 0, 0, "files", "### section (W)."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("branches merged, fetched or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("grades moved, conferred or minted", 0, 0, "grades", "### (K) BAR 5."),
    ("premises discharged", 0, 0, "premises", "### (K) BAR 5."),
    ("doors restated at a new depth", 0, 0, "doors", "### (K) BAR 5."),
    ("routes proposed, priced or opened on a bright verdict", 0, 0, "routes", "### section (Z)."),
    ("kappa values measured or certified", 0, 0, "values", "### section (Z)."),
    ("channels opened", 0, 0, "channels", "### section (Z)."),
    ("rows of `FACES_LEDGER.md` written", 0, 0, "rows",
     "### section (Z): the register stays FROZEN at six."),
    ("rows retired or lists closed", 0, 0, "rows", "### section (Z)."),
    ("folds run", 0, 0, "folds", "### section (Z)."),
    ("rules struck, amended, widened or re-ruled", 0, 0, "rules", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files", "### section (Z)."),
    ("banked ferries edited", 0, 0, "files", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("FERRY_STANDING clauses added", 0, 0, "clauses", "### section (Z)."),
    ("in-place repairs of any original sentence", 0, 0, "repairs", "### (K) BAR 8 / (Z)."),
    ("orientation-layer lines edited", 0, 0, "lines", "### section (Z)."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 10."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted without measurement", 0, 0, "counts", "### section (Z)."),
    ("run records read from a directory listing", 0, 0, "records", "### (K) BAR 11."),
    ("arms trusted because a previous act trusted them", 0, 0, "arms", "### (K) BAR 11."),
    ("expectations scored over a set this face does not name", 0, 0, "expectations", "### (R26)."),
    ("scores averaged to one word where premise and conclusion differ", 0, 0, "scores",
     "### (R27)."),
    ("results applied to an object of a kind they do not quantify over", 0, 0, "results",
     "### (R28)."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("act numbers claimed by an unclosed ferry", 0, 0, "numbers", "### section (A): A1."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories hard-failing at step zero", 0, 0, "repositories", "### section (A)."),
    ("readings of the order declared in advance on this face", 8, 8, "readings",
     "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads", "### section (A)."),
    ("survey sentences found wrong and repaired BEFORE the lock", 1, 1, "sentences",
     "### section (A): declared, not hidden."),
    ("survey sentences found wrong and left standing", 0, 0, "sentences", "### section (A)."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),

    # ---- COMPONENT 1 -- THE MODULE RULED ----------------------------------------------------------
    ("modules the ruling chooses between", 2, 2, "modules",
     "### section (C): the axiom-free module and the interfaces module."),
    ("Mathlib imports anywhere in `Core/`", 0, 0, "imports", "### section (C): MEASURED."),
    ("Mathlib imports added by this act", 0, 0, "imports", "### section (C)."),
    ("primitives the predicate adds, named exactly", 1, 1, "primitives", "### section (C)."),
    ("ruling antecedents settled by opinion rather than by a build", 0, 0, "antecedents",
     "### section (C)."),

    # ---- COMPONENT 2 -- THE CLAUSE STATED ---------------------------------------------------------
    ("general clauses stated without their proof", 1, 1, "clauses", "### section (D)."),
    ("`sorry` occurrences written by this act, in any polarity", 0, 0, "occurrences",
     "### (K) BAR 2."),
    ("`Prop`-valued definitions standing in for an unproved result", 0, 0, "definitions",
     "### (K) BAR 6: the kernel`s idiom keeps open statements OFF the compiled surface."),
    ("kernel modules carrying the NAMED OPEN STATEMENT idiom, found by description", 4, 4,
     "modules", "### section (D): MEASURED, not this seat`s name for the idiom."),
    ("existing `.lean` files whose content is edited", 0, 0, "files", "### (K) BAR 3."),
    ("lines deleted or reordered in `AllPrints.lean`", 0, 0, "lines", "### (K) BAR 3."),
    ("theorems of `FiniteSideSeal.lean` restated, renamed or superseded", 0, 0, "theorems",
     "### (K) BAR 3."),

    # ---- COMPONENT 3 -- THE CONTROL FROM THE KERNEL ------------------------------------------------
    ("positive controls run before any verdict", 1, 1, "controls", "### (K) BAR 4."),
    ("cells the control must reproduce before any verdict", 7, 7, "cells",
     "### (K) BAR 4: on a control short of seven the verdict is WITHHELD."),
    ("new kernel terminals added by this act", 0, None, "terminals", "### MEASURED."),
    ("new terminals whose axiom profile is NOT read from the printed stdout", 0, 0, "terminals",
     "### (K) BAR 1."),
    ("new terminals reporting a NON-EMPTY axiom profile", 0, 0, "terminals",
     "### (K) BAR 2: any non-empty profile REFUSES THE BANK."),
    ("bases the kernel re-decides", 0, None, "bases", "### MEASURED -- the yield is printed."),
    ("bases the kernel cannot afford, stated with the reason", 0, None, "bases",
     "### section (E): an affordability limit is NOT a result about the arithmetic."),
    ("affordability limits reported as results about the arithmetic", 0, 0, "limits",
     "### section (E)."),

    # ---- COMPONENT 4 -- THE TWENTY-EIGHT ----------------------------------------------------------
    ("sentences `b413` counted unqualified, re-read from its record", 28, 28, "sentences",
     "### section (F)."),
    ("sentences repaired by this act", 0, 0, "sentences", "### (K) BAR 8."),
    ("groups the twenty-eight are sorted into, kept apart", 2, 2, "groups", "### (R27)."),

    # ---- COMPONENT 5 -- THE PRICE -----------------------------------------------------------------
    ("prices re-taken now that the statement exists", 1, 1, "prices", "### section (G)."),
    ("upper bounds invented to look decisive", 0, 0, "bounds", "### (K)."),

    # ---- THE ADDITION -----------------------------------------------------------------------------
    ("navigator errors entered verbatim", 1, 1, "errors", "### (K) BAR 12."),
    ("navigator errors paraphrased, softened or argued with", 0, 0, "errors", "### (K) BAR 12."),
    ("kernel caveats quoted from the file rather than from a description", 1, 1, "caveats",
     "### section (H)."),
    ("decided cells the file`s own caveat would exclude", 0, 0, "cells",
     "### section (H): MEASURED -- which is why it went unchallenged."),

    # ---- THE APPARATUS ----------------------------------------------------------------------------
    ("bars declared", 12, 12, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K)."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("arms built by this act not run over this act`s own bank", 0, 0, "arms", "### (K) BAR 11."),
    ("arms scanning source without stripping comments and docstrings", 0, 0, "arms",
     "### (K) BAR 11."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 11."),
    ("prose-reading arms that match before folding markup away", 0, 0, "arms", "### (K) BAR 11."),
    ("arms reading a needle from a sibling artefact rather than the one they name", 0, 0, "arms",
     "### (K) BAR 11."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 11: A2."),
    ("inherited arms not re-pointed at this act", 0, 0, "arms", "### (K) BAR 11."),
    ("arms naming their reference by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("report lines broken mid-token by the wrapper", 0, 0, "lines", "### (K) BAR 11."),
    ("act numbers read out of a commit hash", 0, 0, "numbers", "### (K) BAR 11."),
    ("backslashes written through a quoted heredoc", 0, 0, "backslashes", "### (K) BAR 11."),
    ("new `relay` act-tool files", 6, 6, "files", "### (W) KIND 6."),
    ("shared instruments newly created", 0, 0, "instruments", "### (W)."),
    ("new `.lean` modules added to the kernel", 1, 1, "modules", "### (W) KIND 1."),
    ("build artefacts committed", 0, 0, "artefacts",
     "### (W): `build/` and `*.olean` are ignored by the kernel`s own `.gitignore`, READ."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### section (W)."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b414_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    if not CNT.self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2
    text = io.open(REG, encoding='utf-8').read()
    n, hits = CNT.count_predictions(text)
    print()
    print('  registration : %s' % os.path.basename(REG))
    print('  bytes/lines  : %d / %d' % (len(text.encode('utf-8')), len(text.splitlines())))
    print('  ### ARTIFACT-COUNT PREDICTIONS FOUND : %d' % n)
    for ln, txt in hits:
        print('      line %-4d  %s' % (ln, txt))
    measured = dict(ARMS=count_arms(text))
    print()
    print('  ### ### **THE OPEN CLAUSE, MEASURED RATHER THAN TYPED:** ### ARMS %d'
          % measured['ARMS'])
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b414_registration_2026-09-10.txt -- b414, THE PREDICATE NAMED, "
                             "AND THE GENERAL CLAUSE STATED WITHOUT ITS PROOF"),
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    print()
    print('  clauses emitted : %d' % len(clauses))
    nz = [c for c in clauses if c['demand']]
    print('  ### ### **CLAUSES WITH A NON-ZERO DEMAND : %d**' % len(nz))
    for c in nz:
        print('      %-62s demand %-4s cap %s' % (c['clause'][:62], c['demand'], c['cap']))
    print('  written : %s' % os.path.basename(SPEC))
    print('=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
