# -*- coding: utf-8 -*-
"""b399_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND TWO VERDICTS AND ONE REFUSAL TO REPAIR:** ### two
### sources verified before a word is read; one sign verdict declared vacuous in its own sentence;
### one identity refuted by a printed value; and zero grades moved in a table this act was invited
### to repair.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b399_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b399_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS OF THE FERRY ------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### section (Z): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)/(K) BAR 10."),
    ("instrument runs", 0, 0, "runs", "### section (A)/(K) BAR 11."),
    ("kernel builds run", 0, 0, "builds", "### section (Z)/(K) BAR 11."),
    ("objects recomputed", 0, 0, "objects",
     "### section (A): the only arithmetic is on figures READ from their owning acts."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)/(K) BAR 11."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("rules struck or amended", 0, 0, "rules", "### section (Z)."),
    ("grades moved or conferred", 0, 0, "grades",
     "### section (G)/(K) BAR 7: the grade move is ROUTED, NOT MADE."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (F): the row is SHARPENED and STILL OWED."),
    ("prior acts` faces, banks or instruments edited", 0, 0, "files", "### section (Z)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (Z)."),

    # ---- STEP ZERO AND THE FACE ------------------------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates", "### section (A)."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)."),
    ("readings of the order declared in advance on this face", 5, 5, "readings",
     "### section (A): the vacuous sign verdict; the refutation by value; the two prime columns; "
     "Addition Three`s half-false premise; and both sources verified."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads",
     "### section (A)/(K) BAR 3: `44` reads, `44` ANCHORED."),

    # ---- ADDITION TWO ----------------------------------------------------------------------------
    ("pinned sources this act quotes", 2, 2, "sources", "### section (B)."),
    ("pinned sources VERIFIED against the corpus`s banked digest", 2, 2, "sources",
     "### section (B)/(K) BAR 1."),
    ("source sentences read before their artefact was verified", 0, 0, "sentences",
     "### section (B)/(K) BAR 1: *a derivation quoted from an unverified copy is not a "
     "derivation.*"),
    ("components HALTED for want of a verified source", 0, 0, "components", "### section (B)."),
    ("source fragments located by page index", 6, 6, "fragments", "### section (A)/(K) BAR 3."),
    ("signs taken from the flattener`s glyphs rather than a quoted sentence", 0, 0, "signs",
     "### section (B): the flattener`s deafness is declared with the reads it enables."),

    # ---- ADDITION ONE ----------------------------------------------------------------------------
    ("links of the sign chain, each with a file and a line", 7, 7, "links", "### section (C)."),
    ("links of the sign chain quoted from the navigator", 0, 0, "links",
     "### section (C)/(K) BAR 4."),
    ("lawful seeds in the record", 3, 3, "seeds", "### section (C): `b318`s support test."),
    ("lawful seeds giving the forbidden sign", 0, 0, "seeds",
     "### section (A)/(C): all three read `0.000000000`."),
    ("sign verdicts issued", 1, 1, "verdicts",
     "### section (C): one of the order`s three, unsoftened."),
    ("sign verdicts stated without the word that scopes them", 0, 0, "verdicts",
     "### section (C)/(K) BAR 5: `VACUOUS` stands in the same sentence as `SURVIVES`."),
    ("prime columns of the record set against the claim", 2, 2, "columns",
     "### section (A): the source`s window and the corpus`s."),
    ("verdicts that depend on which prime column is chosen", 0, 0, "verdicts",
     "### section (A): both read `0.000000000` at all three lawful cells."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("sides of (M) unfolded to what they sum over", 2, 2, "sides", "### section (D)."),
    ("sides described in the other`s language", 0, 0, "sides", "### section (D)."),
    ("sides for which the record gives a VALUE", 2, 2, "sides",
     "### section (D): the draft`s `(L1)` MET."),
    ("constituents quoted without a file and a line", 0, 0, "constituents", "### section (K) BAR 3."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("steps of the attempt, each with an owner and a grade", 4, 4, "steps", "### section (E)."),
    ("verdicts on (M)", 1, 1, "verdicts",
     "### section (E): one of the draft`s three, unsoftened."),
    ("cells at which both sides of (M) are printed", 3, 3, "cells", "### section (E)/(K) BAR 6."),
    ("escapes from the refutation left open", 0, 0, "escapes",
     "### section (E)/(K) BAR 6: normalization, sign convention and truncation, each closed by a "
     "named fact."),
    ("sign conventions under which (M) survives", 0, 0, "conventions",
     "### section (E): `+8.62 = 0` fails as `-8.62 = 0` does."),
    ("corroborations counted toward the verdict", 0, 0, "corroborations",
     "### section (E): the RH-in-one-line remark is LABELLED and carries no weight."),
    ("results typed above their weakest link", 0, 0, "results",
     "### section (E): typed MEASURED-AT-COVERED-CELLS."),
    ("derivations attempted against a refuted identity", 0, 0, "derivations",
     "### section (E): Addition One`s stop governs a refutation BY SIGN and returned SURVIVES."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("obstructions standing after this act", 1, 1, "obstructions",
     "### section (F): the family obstruction, untouched."),
    ("statements named as what the owed row needs instead", 0, 0, "statements",
     "### section (F)/(J): naming one is not in this order."),
    ("coordinates closed", 0, 0, "coordinates", "### section (F)/(Z)."),

    # ---- ADDITION THREE --------------------------------------------------------------------------
    ("stale ranking rows examined", 1, 1, "rows", "### section (G): `FINDINGS.md:3079`."),
    ("cells of the ranking table edited", 0, 0, "cells", "### section (G)/(K) BAR 7."),
    ("verdict sentences of the ranking edited", 0, 0, "sentences", "### section (G)/(K) BAR 7."),
    ("pointers appended", 1, 1, "pointers", "### section (G)/(I)."),
    ("originals preserved verbatim before the write", 1, 1, "originals", "### section (G)."),
    ("lifting acts quoted", 1, 1, "acts", "### section (G): `b333`."),
    ("routed items left without a firable trigger", 0, 0, "items",
     "### section (G): RULING (R23)."),

    # ---- THE CONTACTS ----------------------------------------------------------------------------
    ("compute contacts filed", 3, 3, "contacts", "### section (H)."),
    ("files the contacts are written in", 1, 1, "files",
     "### section (H): the emerging-programmes ledger ONLY."),
    ("bytes written about the contacts in any research-facing document", 0, 0, "bytes",
     "### section (H)/(K) BAR 9."),
    ("claims carried by the contacts", 0, 0, "claims", "### section (H)."),
    ("seeds created", 0, 0, "seeds", "### section (H)."),
    ("promotion criteria set", 0, 0, "criteria", "### section (H)."),
    ("contacts filed without a provenance line", 0, 0, "contacts", "### section (H)."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 12, 12, "bars", "### section (K)."),
    ("bars with a stated floor", 12, 12, "bars", "### section (K): `b347`s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (K): UNPRICED."),
    ("must-fail fixtures", 6, 6, "fixtures", "### section (K): BARS 1, 2, 5, 6, 7 and 9."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (K), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(`b397`)."),
    ("arms measuring a bar this face did not set", 0, 0, "arms", "(`b390`)."),
    ("new `relay` tool files", 5, 5, "files", "### section (I): the cap counts FILES (`b382`)."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (Z)."),
    ("content lost in any edited file", 0, 0, "lines", "### section (K) BAR 8."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (Z)."),
    ("documents reclassified or placed in Tier KC", 0, 0, "documents", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("the census edited", 0, 0, "files", "### section (Z)."),
    ("standards edited", 0, 0, "files", "### section (Z)."),
    ("face rows of the faces ledger edited", 0, 0, "rows",
     "### section (I): the OWED PAIR row`s last cell only."),
    ("correspondence rows edited", 0, 0, "rows", "### section (Z): rows are APPENDED."),
    ("claims withdrawn", 0, 0, "claims", "### section (Z)."),
    ("clusters reshaped", 0, 0, "clusters", "### section (Z)."),
    ("map head notes touched", 0, 0, "notes", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
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
    import re
    return len(set(re.findall(r'\bG-[A-Z0-9]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b399_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    print('  ### ### **THE OPEN CLAUSE, MEASURED RATHER THAN TYPED:** ### ARMS %d' % measured['ARMS'])
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b399_registration_2026-09-10.txt -- b399, "
                             "(M) TESTED BY SIGN, THEN ATTEMPTED"),
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
