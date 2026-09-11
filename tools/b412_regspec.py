# -*- coding: utf-8 -*-
"""b412_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND A CLASSIFICATION, A COUNT AND THREE ARMS:** ### a
### sweep whose subject is the seal and not the words; an amendment made by the standing file's own
### mechanism without bumping the version every live ferry cites; and a reading that names two
### clauses and refuses to derive whether they can be met.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b412_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b412_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### (Z)/(K) BAR 12: NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)."),
    ("files under `outputs/` touched", 0, 0, "files", "### (K) BAR 4: DEPOSITED, excluded."),
    ("kernel builds run", 0, 0, "builds", "### section (Z): both lanes PARKED."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)."),
    ("axiom profiles read or inferred", 0, 0, "profiles", "### section (Z)."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("grades moved, conferred or minted", 0, 0, "grades",
     "### (K) BAR 2: `F-NOGRADE` makes the claim MECHANICAL, not asserted."),
    ("acts re-verdicted by the fold", 0, 0, "acts", "### (K) BAR 2."),
    ("new mathematics in the fold section", 0, 0, "results", "### (K) BAR 2."),
    ("folded acts summarised as overturning another", 0, 0, "acts",
     "### (K) BAR 3: `F-NOSUPERSEDE`, where the record says they answer different questions."),
    ("one-statements manufactured for a fold that carries none", 0, 0, "statements",
     "### (K) BAR 6: the ferry says QUOTED AND NONE SUMMARISED; what is absent is REPORTED."),
    ("doors restated at a depth the record did not move them to", 0, 0, "doors", "### (K) BAR 7."),
    ("prior text of the orientation layer edited", 0, 0, "documents",
     "### (K) BAR 5: the prior text is preserved as a TRUE PREFIX."),
    ("routed items discharged by this act", 0, 0, "items", "### (K) BAR 8."),
    ("routes proposed, priced or opened on a bright verdict", 0, 0, "routes", "### (K) BAR 9."),
    ("instruments built for the reach question", 0, 0, "instruments", "### (K) BAR 9."),
    ("kappa values measured or certified", 0, 0, "values", "### section (Z)."),
    ("channels opened", 0, 0, "channels", "### section (Z)."),
    ("instrument numbers assigned, moved or reconciled", 0, 0, "numbers", "### section (Z)."),
    ("class symbols renumbered, in any document", 0, 0, "symbols", "### section (Z)."),
    ("rows of `FACES_LEDGER.md` written", 0, 0, "rows",
     "### section (Z): the register stays FROZEN at six."),
    ("rows retired or lists closed", 0, 0, "rows", "### section (Z)."),
    ("rules struck, amended, widened or re-ruled", 0, 0, "rules",
     "### section (Z): (R31) is the AUTHOR`S and is EXECUTED, not minted."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files", "### section (Z)."),
    ("banked ferries edited", 0, 0, "files", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("FERRY_STANDING clauses added", 0, 0, "clauses", "### section (Z)."),
    ("in-place repairs of any original sentence", 0, 0, "repairs", "### (W)/(Z)."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 12."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted without measurement", 0, 0, "counts", "### section (Z)."),
    ("spans typed rather than read from the tool", 0, 0, "spans", "### (K) BAR 1."),
    ("run records read from a directory listing", 0, 0, "records", "### (K) BAR 11."),
    ("arms trusted because a previous act trusted them", 0, 0, "arms", "### (K) BAR 11."),
    ("expectations scored over a set this face does not name", 0, 0, "expectations", "### (R26)."),
    ("scores averaged to one word where premise and conclusion differ", 0, 0, "scores",
     "### (R27)."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("act numbers claimed by an unclosed ferry", 0, 0, "numbers", "### section (A): A1."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("readings of the order declared in advance on this face", 6, 6, "readings", "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads", "### section (A)."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),

    # ---- COMPONENT 1 -- THE FOLD -----------------------------------------------------------------
    ("span counts printed", 2, 2, "counts",
     "### (K) BAR 1: the TOOL`S count and the FOLD`S span, and they differ by the filing act."),
    ("acts in the folded span", 9, 9, "acts", "### section (C): b403 through b411."),
    ("fold sections written", 1, 1, "sections", "### (W) KIND 9."),
    ("mechanical no-grade arms run over the fold", 1, 1, "arms", "### (K) BAR 2: `F-NOGRADE`."),
    ("mechanical no-supersede arms run over the fold", 1, 1, "arms", "### (K) BAR 3."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("acts of the span classified object-versus-record", 9, 9, "acts", "### section (D)."),
    ("statements about the object counted", 0, None, "statements", "### section (D): MEASURED."),
    ("borderline classifications named rather than rounded", 0, None, "cases",
     "### (K) BAR 10: MEASURED, and each named."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("routed items inventoried", 0, None, "items", "### section (E): MEASURED."),
    ("routed items given an act, a cost and an owner", 0, None, "items", "### (K) BAR 8."),

    # ---- COMPONENT 4 -----------------------------------------------------------------------------
    ("prices printed for the reach instrument", 1, 1, "prices", "### section (F)."),
    ("verdicts on whether the corpus has the parts", 1, 1, "verdicts", "### section (F)."),

    # ---- COMPONENT 5 -- THE ORIENTATION LAYER, (R31) ---------------------------------------------
    ("orientation objects read at their own date", 2, 2, "objects", "### section (G)."),
    ("acts-behind figures printed, one per object", 2, 2, "figures", "### section (G)."),
    ("orientation objects brought current", 2, 2, "objects", "### section (G)."),
    ("one-statements quoted verbatim from their own fold section", 0, None, "statements",
     "### (K) BAR 6: MEASURED -- only the folds that carry one can supply one."),
    ("folds reported as carrying no one-statement", 0, None, "folds", "### (K) BAR 6: MEASURED."),
    ("doors whose depth the arc moved", 0, None, "doors",
     "### (K) BAR 7: MEASURED by a search with a positive control, not asserted."),
    ("old depths preserved beside any new one", 0, None, "depths", "### (K) BAR 7."),
    ("before-and-after line counts printed for the digest", 2, 2, "counts", "### section (G)."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 12, 12, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("arms built by this act not run over this act`s own bank", 0, 0, "arms", "### (K) BAR 11."),
    ("arms scanning source without stripping comments and docstrings", 0, 0, "arms",
     "### (K) BAR 11."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 11."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 11."),
    ("prose-reading arms that match before folding markup away", 0, 0, "arms", "### (K) BAR 11."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 11: A2, inherited."),
    ("inherited arms not re-pointed at this act", 0, 0, "arms", "### (K) BAR 11."),
    ("arms demanding a number a previous act happened to produce", 0, 0, "arms", "### (K) BAR 11."),
    ("arms naming their reference by address rather than content", 0, 0, "arms", "### (K) BAR 11."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("report lines broken mid-token by the wrapper", 0, 0, "lines", "### (K) BAR 11."),
    ("act numbers read out of a commit hash", 0, 0, "numbers",
     "### (K) BAR 11: the survey`s first counter read `b515e6b` as an act."),
    ("text handles opened for write before the bytes are encoded", 0, 0, "handles",
     "### (K) BAR 11."),
    ("backslashes written through a quoted heredoc", 0, 0, "backslashes", "### (K) BAR 11."),
    ("new `relay` act-tool files", 6, 6, "files", "### (W) KIND 8."),
    ("shared instruments newly created", 0, 0, "instruments", "### (W)."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### section (W)."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    """### **THE FOLD ARMS CARRY THE `F-` PREFIX, BY `b348`'S OWN CONVENTION.**

    ### A counter that saw only `G-` reported `87` where the face declares `91`, and the suite's
    ### declared-versus-run reconciliation would then have failed on four arms that are real.
    ### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES.**
    """
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b412_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b412_registration_2026-09-10.txt -- b412, THE CLASSIFICATION ARC FOLDED, AND THE "
                             "ORIENTATION LAYER BROUGHT CURRENT"),
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
