# -*- coding: utf-8 -*-
"""b400_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND ONE VERDICT, ONE CORRECTION AND ONE REFUSAL:** ###
### an impossibility stated at a scope with the sentence naming what it does NOT show; the order's
### own phrase quoted and corrected against a verified source rather than improved in silence; and a
### claim the ferry permits only on the record's word, which the record does not give.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b400_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b400_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS OF THE FERRY ------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### section (Z): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)/(K) BAR 11."),
    ("instrument runs", 0, 0, "runs", "### section (Z)/(K) BAR 11."),
    ("kernel builds run", 0, 0, "builds", "### section (Z)/(K) BAR 11."),
    ("objects recomputed", 0, 0, "objects",
     "### section (K) BAR 11: the one arithmetic is prime powers in an interval, and it banks "
     "nothing."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)/(K) BAR 11."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("rules struck or amended", 0, 0, "rules", "### section (Z)."),
    ("grades moved or conferred", 0, 0, "grades", "### section (F)/(K) BAR 7."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (F): the row is ANSWERED IN PART and STAYS OWED."),
    ("prior acts` faces, banks or instruments edited", 0, 0, "files",
     "### section (Z): `b321`s convention split is ROUTED, not repaired."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (Z)."),

    # ---- STEP ZERO, THE WRITE LIST AND THE INCIDENT -----------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories",
     "### section (A): the clause is answered rather than left silent."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads",
     "### section (A)/(K) BAR 2: `23` reads, `23` ANCHORED."),
    ("readings of the order declared in advance on this face", 5, 5, "readings",
     "### section (A): the fourth verdict; the order`s half-false phrase; `(N5)`s structural "
     "reason; a prior face`s two conventions; and the refused one-question claim."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("orders carried by reference and left unreadable at a file", 0, 0, "orders",
     "### section (A): the adopted draft is banked verbatim with its provenance."),
    ("incidents at step zero declared on this face", 1, 1, "incidents",
     "### section (A)/(K) BAR 15: `b373_pins.json`, overwritten and restored."),
    ("prior acts` banked records left overwritten", 0, 0, "records",
     "### section (A): restored BYTE-IDENTICAL to the committed blob, verified pre-push."),

    # ---- THE SOURCES -----------------------------------------------------------------------------
    ("pinned sources this act quotes", 2, 2, "sources", "### section (B)."),
    ("pinned sources VERIFIED against the corpus`s banked digest", 2, 2, "sources",
     "### section (B)/(K) BAR 1."),
    ("source sentences read before their artefact was verified", 0, 0, "sentences",
     "### section (B)/(K) BAR 1."),
    ("components HALTED for want of a verified source", 0, 0, "components", "### section (B)."),
    ("source fragments located by page index", 8, 8, "fragments", "### section (B)."),
    ("signs taken from the flattener`s glyphs rather than a quoted sentence", 0, 0, "signs",
     "### section (B)."),

    # ---- COMPONENT 1, THE CONSTRAINT SET ----------------------------------------------------------
    ("constraints in the set", 8, 8, "constraints", "### section (C)."),
    ("constraints carrying a file and a line", 8, 8, "constraints", "### section (C)/(K) BAR 2."),
    ("constraints taken from the navigator", 0, 0, "constraints", "### section (C)/(K) BAR 3."),
    ("constraints the record holds at DERIVES", 2, 2, "constraints",
     "### section (C): `C-V` and `C-VI` only, and the face says which rather than levelling them."),
    ("constraints stated without a grade", 0, 0, "constraints", "### section (C)."),

    # ---- COMPONENT 2, THE VERDICT -----------------------------------------------------------------
    ("verdicts on the bridge", 1, 1, "verdicts",
     "### section (D): one of the order`s four, unsoftened."),
    ("impossibility claims made without the scope they are derived at", 0, 0, "claims",
     "### section (D)/(K) BAR 4."),
    ("sentences naming what the obstruction does NOT show", 1, 1, "sentences",
     "### section (D)/(K) BAR 4: in the same section as the claim."),
    ("equivalences compiled", 0, 0, "equivalences",
     "### section (D)/(F): the deposit`s refusal governs and is quoted beside the rows."),
    ("correspondences chosen to make an identity come out", 0, 0, "correspondences",
     "### section (D): a chosen correspondence is COMPILED, not DERIVED."),
    ("replacements for (M) named", 0, 0, "statements",
     "### section (D): the fourth verdict names a QUESTION and not a statement."),
    ("questions typed at the window", 1, 1, "questions", "### section (D): `(Q400)`."),
    ("questions typed without their absent element named", 0, 0, "questions",
     "### section (D): the one absent element is named and it is the only one."),
    ("questions opened by this act", 0, 0, "questions", "### section (D): `(Q400)` is NOT OPENED."),
    ("cautions carried from the window act", 1, 1, "cautions",
     "### section (D): and the distinction that keeps it from being a closure is stated with it."),

    # ---- COMPONENT 3 ------------------------------------------------------------------------------
    ("banked cells surveyed", 13, 13, "cells", "### section (E)."),
    ("lawful cells", 3, 3, "cells", "### section (E)."),
    ("lawful cells admitting a prime power", 0, 0, "cells", "### section (E): `(N5)`."),
    ("membership lists compared cell by cell rather than by a count of matches", 13, 13, "lists",
     "### section (E): (`b396`)."),
    ("prior faces edited to make a comparison agree", 0, 0, "faces", "### section (E)/(Z)."),

    # ---- THE LEDGERS ------------------------------------------------------------------------------
    ("ledger files this act appends to", 2, 2, "files",
     "### section (F): `FACES_LEDGER.md` and `OPEN_TRAILS.md`."),
    ("ledger cells rewritten rather than appended to", 0, 0, "cells", "### section (F)/(K) BAR 8."),
    ("content lost in any edited file", 0, 0, "lines", "### section (K) BAR 8."),
    ("work-order triggers changed", 0, 0, "triggers",
     "### section (F): `W-ORD-LI-WEIL-BRIDGE` stays at THE AUTHOR`S WORD."),
    ("routed items left without a firable trigger", 0, 0, "items", "RULING (R23)."),
    ("claims that the bridge and the clause are one question", 0, 0, "claims",
     "### section (A) reading (5)/(K) BAR 6: the record`s words do not carry it."),

    # ---- THE APPARATUS ----------------------------------------------------------------------------
    ("bars declared", 15, 15, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars",
     "### section (K): UNPRICED -- this act computes no object."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (K), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(`b397`)."),
    ("arms measuring a bar this face did not set", 0, 0, "arms", "(`b390`)."),
    ("arms reading a repository state without a declared side", 0, 0, "arms", "(`b352`)."),
    ("new `relay` tool files", 6, 6, "files",
     "### section (A)/(K) BAR 9: the cap counts FILES (`b382`), the desk/bank writer included "
     "(`b399`s own defect, repaired here)."),
    ("files this act writes that section (A) does not name", 0, 0, "files", "### (K) BAR 10."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (Z)."),

    # ---- THE STANDING NOTHINGS --------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (Z)."),
    ("documents reclassified or placed in Tier KC", 0, 0, "documents", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("the census edited", 0, 0, "files", "### section (Z)."),
    ("standards edited", 0, 0, "files", "### section (Z)."),
    ("face rows of the faces ledger edited", 0, 0, "rows",
     "### section (F): the OWED cells only, appended to."),
    ("correspondence rows edited", 0, 0, "rows", "### section (Z): rows are APPENDED."),
    ("claims withdrawn", 0, 0, "claims", "### section (Z)."),
    ("clusters reshaped", 0, 0, "clusters", "### section (Z)."),
    ("map head notes touched", 0, 0, "notes", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
    ("coordinates closed", 0, 0, "coordinates", "### section (Z)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (Z)."),
    ("posture-lock changes", 0, 0, "changes", "### section (Z)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (A)."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    return len(set(re.findall(r'\bG-[A-Z0-9]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b400_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b400_registration_2026-09-10.txt -- b400, "
                             "THE BRIDGE RESTATED, OR THE PAIR DECLARED TWO OBJECTS"),
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
