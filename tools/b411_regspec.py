# -*- coding: utf-8 -*-
"""b411_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b411_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b411_satisfiable.json')

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
    ("instrument numbers renumbered, moved or reassigned", 0, 0, "numbers",
     "### (K) BAR 3: (R30) keeps the screen`s number; the act NAMES the free one and assigns it "
     "to nothing."),
    ("class symbols renumbered, in any document", 0, 0, "symbols", "### section (Z)."),
    ("grades moved, conferred or minted", 0, 0, "grades", "### (K) BAR 7."),
    ("kappa values measured or certified", 0, 0, "values", "### (K) BAR 7."),
    ("channels opened", 0, 0, "channels", "### (K) BAR 7."),
    ("routes proposed, priced or opened on a bright verdict", 0, 0, "routes", "### (K) BAR 7."),
    ("rows of `FACES_LEDGER.md` written", 0, 0, "rows",
     "### section (Z): the register stays FROZEN at six."),
    ("sites entered in row U1", 0, 0, "sites", "### section (Z)."),
    ("folds run", 0, 0, "folds", "### section (Z)."),
    ("rules struck, amended, widened or re-ruled", 0, 0, "rules",
     "### section (Z): (R29) and (R30) are the AUTHOR`S and are EXECUTED, not minted."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z)."),
    ("rows retired", 0, 0, "rows", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files",
     "### section (Z): b410 is CORRECTED on one count, not edited."),
    ("banked ferries edited", 0, 0, "files", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (Z): rows are APPENDED."),
    ("FERRY_STANDING clauses added", 0, 0, "clauses", "### section (Z)."),
    ("calibration rows removed from the family", 0, 0, "rows",
     "### (K) BAR 8: an UNSOURCED mark is not a removal, and the mark is CONDITIONAL."),
    ("bridges typed", 0, 0, "bridges", "### section (Z)."),
    ("theorems reported as applying where a condition is unchecked", 0, 0, "theorems",
     "### section (D)."),
    ("navigator assertions adopted without a test", 0, 0, "assertions",
     "### (K) BAR 1: the ADDITION is TESTED, not adopted on his word."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 12."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted without measurement", 0, 0, "counts", "### section (Z)."),
    ("counts carried from a previous act without re-measurement", 0, 0, "counts",
     "### (K) BAR 5: b410`s `12` is RE-MEASURED here and it has MOVED."),
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

    # ---- COMPONENT 1 -- THE JOIN, (R29) ----------------------------------------------------------
    ("cross-reference lines written", 2, 2, "lines",
     "### section (C): one in each document, under (R29)."),
    ("documents whose original text is altered by the join", 0, 0, "documents", "### (K) BAR 2."),
    ("headings, numbers or definitions changed by the join", 0, 0, "items", "### (K) BAR 2/BAR 3."),
    ("each cross-reference read back in the file it names", 2, 2, "reads", "### (K) BAR 2."),

    # ---- COMPONENT 2 -- THE COLLISION, (R30) -----------------------------------------------------
    ("free instrument numbers named", 1, 1, "numbers", "### section (D)."),
    ("rename costs priced, in both directions", 2, 2, "prices", "### section (D)."),
    ("citations touched by this act`s pricing", 0, 0, "citations",
     "### (K) BAR 3: the price is PRINTED, not paid."),

    # ---- COMPONENT 3 AND THE ADDITION ------------------------------------------------------------
    ("instruments that grade a cited claim, found by description", 0, None, "instruments",
     "### (K) BAR 6: MEASURED, and reported ABSENT only on a control that PASSED."),
    ("positive controls on the grading search", 1, 1, "controls", "### (K) BAR 6."),
    ("verdicts on what would price the import", 1, 1, "verdicts", "### section (E)."),
    ("navigator assertions tested against the gate`s own words", 1, 1, "assertions",
     "### (K) BAR 1."),
    ("statements of what the gate`s price IS and is NOT", 2, 2, "statements", "### section (E)."),

    # ---- COMPONENT 4 -----------------------------------------------------------------------------
    ("certificates located or reported unlocatable", 1, 1, "certificates", "### section (F)."),
    ("routes the certificate names", 0, None, "routes", "### section (F): MEASURED."),
    ("reproducibility marks checked against the banked record", 5, 5, "marks", "### section (F)."),
    ("UNSOURCED marks written", 0, None, "marks",
     "### (K) BAR 8: MEASURED -- written IF AND ONLY IF the certificate is unlocatable."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 12, 12, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("arms built by this act not run over this act`s own bank", 0, 0, "arms",
     "### (K) BAR 10: b410`s lesson, carried as a bar."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 11."),
    ("arms scanning source without stripping comments and docstrings", 0, 0, "arms",
     "### (K) BAR 11: b410`s `G-NOBORROWEDBAR` fired on its own comment."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 11."),
    ("prose-reading arms that match before folding markup away", 0, 0, "arms", "### (K) BAR 11."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 11: A2, inherited."),
    ("inherited arms not re-pointed at this act", 0, 0, "arms", "### (K) BAR 11."),
    ("arms demanding a number a previous act happened to produce", 0, 0, "arms", "### (K) BAR 11."),
    ("arms naming their reference by address rather than content", 0, 0, "arms", "### (K) BAR 11."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("report lines broken mid-token by the wrapper", 0, 0, "lines",
     "### (K) BAR 11: b410`s wrapper split a word and an arm then measured the wrapper."),
    ("text handles opened for write before the bytes are encoded", 0, 0, "handles",
     "### (K) BAR 11: b405`s zero-byte husk."),
    ("backslashes written through a quoted heredoc", 0, 0, "backslashes",
     "### (K) BAR 11: the trap fired TWICE at b410."),
    ("new `relay` act-tool files", 6, 6, "files", "### (W) KIND 8."),
    ("shared instruments newly created", 0, 0, "instruments",
     "### (W): this act creates none; `gate_spine.py` is AMENDED additively, if at all."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### section (W)."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    return len(set(re.findall(r'\bG-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b411_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b411_registration_2026-09-10.txt -- b411, THE JOIN, THE COLLISION, THE IMPORT "
                             "PRICED AS AN IMPORT, AND THE CERTIFICATE LOCATED"),
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
