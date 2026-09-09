# -*- coding: utf-8 -*-
"""b382_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any write of this act.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b382_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b382_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (J): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (J): read and counted, never edited."),
    ("`.lean` files touched", 0, 0, "files", "### section (J)."),
    ("terminals written", 0, 0, "terminals", "### section (J)."),
    ("statements proved", 0, 0, "statements", "### section (J)."),
    ("builds run", 0, 0, "builds", "### section (J)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),

    # ---- STEP ZERO AND THE DECLARED READINGS ---------------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378's gate run as b382, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates",
     "### section (A)/(H) BAR 1."),
    ("readings of the order declared in advance on this face", 4, 4, "readings",
     "### section (A): what QUOTED NOT SUMMARISED means; that the conclusion is about METHOD; what NAMED AS COMPLETE means; and that naming the untracked records is not committing them."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims",
     "### section (A): the standing clause."),

    # ---- COMPONENT 1: THE ACCOUNT --------------------------------------------------------------------
    ("acts the account covers", 7, 7, "acts",
     "### section (B): b375 through b381, each with what it asked, what it found and what it left."),
    ("claims about a prior act carried without a quoted line", 0, 0, "claims",
     "### section (B)/(H) BAR 2: every claim is anchored in that act's own bank."),
    ("quoted lines that fail to re-read at their own line number", 0, 0, "lines",
     "### section (B)/(H) BAR 2: a quotation that does not re-read is a HARD FAILURE."),
    ("things the order names by name that the account does not carry", 0, 0, "things",
     "### section (B)/(H) BAR 3: the three tests, the definition's drift, the four widenings, the two features and the control, and the standing count."),
    ("figures in the account with no quoted line or banked JSON behind them", 0, 0, "figures",
     "### section (A)/(B): the connective prose is this seat's; the figures are not."),

    # ---- COMPONENT 2: THE CONCLUSION -----------------------------------------------------------------
    ("conclusions stated", 1, 1, "conclusions",
     "### section (C): one, about METHOD, and the order says so twice."),
    ("classes ruled", 0, 0, "classes", "### section (C)/(J): this act closes evidence and does not rule."),
    ("declaration rules ordered", 0, 0, "rules",
     "### section (C)/(H) BAR 5: the obligations are PRICED and NOT ORDERED. ### A PRICE IS NOT A PROPOSAL."),
    ("branches carrying a preference word", 0, 0, "branches", "### section (C)/(H) BAR 5."),
    ("readings of the role count re-measured", 3, 3, "readings",
     "### section (C)/(H) BAR 4: b376 strict, b376 broad, and b381's purpose-statement reading, all three printed."),
    ("load-bearing figures carried from a prior act rather than re-measured", 0, 0, "figures",
     "### section (C): the count the second half of the conclusion rests on is re-measured here."),
    ("proofs claimed that no structural feature reads role", 0, 0, "proofs",
     "### section (C)/(G): TWO FAILED FEATURES ARE EVIDENCE AND NOT PROOF, declared before the number exists."),
    ("obligations priced without a figure from the record", 0, 0, "obligations",
     "### section (G): where the record does not count it, the price is NAMED UNPRICED rather than estimated."),

    # ---- COMPONENT 3: THE CAUTION --------------------------------------------------------------------
    ("cautions recorded with the exemplar set", 1, 1, "cautions",
     "### section (D)/(H) BAR 7: in the evidence file and in the trail block."),
    ("claims that nothing rests on the set made without checking the record", 0, 0, "claims",
     "### section (D): checked against b381's banked JSON, not repeated from it."),
    ("exemplar sets inherited rather than re-derived", 0, 0, "sets",
     "### section (D): if it is ever reused it is re-derived."),

    # ---- COMPONENT 4: THE OPEN ITEMS -----------------------------------------------------------------
    ("open lists closed", 0, 0, "lists", "### section (E)/(J): all four restated OPEN by name."),
    ("open items restated for the ruling", 4, 4, "items",
     "### section (E): the four lists, the registry drift, the six clusters, and the floor."),
    ("desk items closed", 1, 1, "items",
     "### section (E)/(H) BAR 8: exactly one, and it is the sequence itself."),
    ("registry-drift filings closed", 0, 0, "filings",
     "### section (E)/(J): it stays open and is the author's under (R14)."),
    ("column-(d) figures re-measured", 0, 0, "figures",
     "### section (E): b377's amendment forbade it and no later order has lifted that."),

    # ---- THE EVIDENCE FILE ---------------------------------------------------------------------------
    ("ruling-evidence files finalised", 1, 1, "files",
     "### section (A)/(F)/(H) BAR 6: named complete AS THIS SEQUENCE'S PRODUCT."),
    ("lines edited in the evidence file", 0, 0, "lines",
     "### section (H) BAR 6: the finalisation is an APPENDED block and nothing above it moves."),
    ("new tracking documents created in the corpus", 0, 0, "documents",
     "### section (A)/(F): the standing prohibition since b375, and this act creates none."),

    # ---- THE UNTRACKED RECORDS -----------------------------------------------------------------------
    ("untracked run records of earlier acts committed by this act", 0, 0, "files",
     "### section (F)/(H) BAR 9: b381's incident and its lesson. ### NAMING THEM IS NOT COMMITTING THEM."),
    ("untracked run records named in this act's record", 1, None, "files",
     "### section (A)/(H) BAR 9: named so a later act does not rediscover them as a defect."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 9, 9, "bars",
     "### section (H): stamped-gate, quotation, anchored-claim, re-measured-count, no-order, evidence-epilogue, caution, open-items, untracked-records."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 6, 6, "files",
     "the regspec, the extract, the reg gate, the account-and-conclusion writer, the desk sweeper, the bank writer and this act's gate suite -- SIX FILES, because this act ASSEMBLES AND CONCLUDES rather than measuring, and needs no new instrument. ### THE LOCK GATE IS b378'S, RUN AS b382."),
    ("shared utilities created", 0, 0, "files",
     "### NONE. ### This act builds no instrument: it reads seven banks and concludes. ### A SHARED UTILITY WITH NO SECOND CALLER IS A FILE, NOT A UTILITY."),
    ("owner instrument files edited", 0, 0, "files", "this act licenses none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (J)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files", "### CORRESPONDENCE.md at the closing."),
    ("PLACE-papers files written", 1, 1, "files",
     "### section (F): OPEN_TRAILS.md, appended. ### NO CORPUS DOCUMENT IS WRITTEN INTO AT ALL AND REGISTRY.md IS NOT EDITED."),
    ("new tracking documents created", 0, 0, "documents", "### section (J)."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists", "### section (J): restated OPEN by name."),
    ("kernels opened without a positive control on the sweep", 0, 0, "kernels",
     "### section (A)/(H) BAR 3."),
    ("pins written by this act", 0, 0, "pins",
     "### section (F): no corpus document is written into, so no row and no pin is written."),
    ("documents selected by their path rather than by their own declaration", 0, 0, "documents",
     "### section (B): the account's subjects are this sequence's own acts, named by the order."),
    ("classes ruled", 0, 0, "classes", "### section (J)."),
    ("documents reclassified", 0, 0, "documents", "### section (J)."),
    ("class lines written", 0, 0, "lines", "### section (C)/(J): no declaration is moved."),
    ("grades moved", 0, 0, "grades", "### section (J)."),
    ("equivalences compiled", 0, 0, "compilations", "### section (J)."),
    ("bars moved", 0, 0, "bars", "### section (J)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (J)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (J)."),
    ("faces promoted", 0, 0, "faces", "### section (J)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (J)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (J)."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (J): no claim in either direction."),
    ("posture-lock changes", 0, 0, "changes", "### section (J)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (J): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (B)/(C): every figure is re-read from a bank or a banked JSON, and the load-bearing count is re-measured."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b382_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    print('  ITS SELF-TEST, RUN HERE BEFORE IT IS TRUSTED:')
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
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": "data/b382_registration_2026-09-09.txt -- b382, THE SEQUENCE STOPPED AND THE EVIDENCE CLOSED",
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
