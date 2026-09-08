# -*- coding: utf-8 -*-
"""b369_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any write of this act.
### ### **AND THIS ACT'S SPEC CARRIES TWO CLAUSES WHOSE DEMAND IS NON-ZERO WHERE EVERY PRIOR ACT'S WAS
### ### ZERO:** ### the front document IS edited and an owner instrument IS edited, both because the
### order sends this act to do it. ### **A CAP THAT SAYS `0` WHERE THE ORDER SAYS `DO IT` IS NOT A
### ### DISCIPLINE, IT IS A LIE**, so the caps are stated at what the order licenses and no wider.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b369_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b369_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (H): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (H)."),
    ("`.lean` files touched", 0, 0, "files", "### section (A)/(H): the order's own clause under (R4)."),
    ("terminals written", 0, 0, "terminals", "### section (H)."),
    ("statements proved", 0, 0, "statements", "### section (H)."),
    ("builds run", 0, 0, "builds", "### section (H): no profile is computed."),
    ("axiom profiles computed", 0, 0, "profiles", "### section (H)."),

    # ---- (R4): THE EDIT THIS ACT IS SENT TO MAKE, CAPPED AT WHAT THE ORDER LICENSES ------------------
    ("front-document list rows replaced", 7, 7, "rows",
     "### section (B): the located rows and no others; the count is the located set, read BEFORE the edit."),
    ("front-document sentences edited outside the list rows", 0, 0, "sentences",
     "### section (B) BAR 3: the bounded-edit bar -- every byte outside the rows and the appended block is its blob's."),
    ("front-document blocks appended", 1, 1, "blocks",
     "### section (B): the currency block gains the verbatim preservation and the supersession notice."),
    ("original list rows preserved verbatim in the same file", 7, 7, "rows",
     "### section (B) BAR 1: byte-for-byte against the lines read before the edit."),
    ("names the classification calls ABSENT remaining in the repaired list", 0, 0, "names",
     "### section (B) BAR 2: a CONTENT predicate over the list's own rows, never a line count."),
    ("sentences of b368's block edited", 0, 0, "sentences",
     "### section (B)/(H): they are NAMED and marked SUPERSEDED; another act's record is not rewritten."),
    ("sentences dated by this act and left unnamed", 0, 0, "sentences",
     "### section (B): the cost of (R4) is reported at full prominence, not left for a reader to trip over."),
    ("figures carried from a prior act rather than re-derived", 0, 0, "figures",
     "### section (B): b368's figures are a COMPARISON ONLY and never an input to the count."),
    ("names classified from their own sound", 0, 0, "names",
     "### section (C): the standing bar, and the case that differs only in case is refused again."),
    ("successors named for a retired name", 0, 0, "successors", "### section (C)."),
    ("retirement reasons asserted beyond the kernel's own record", 0, 0, "reasons",
     "### section (C): (R5) -- where the record is silent, the act says the record is silent."),

    # ---- COMPONENT 2 ---------------------------------------------------------------------------------
    ("owner instrument files edited", 2, 2, "files",
     "### section (D): the pins roster and the hook exerciser's roster, both named on this face BEFORE the edit; any other instrument moving is still a failure."),
    ("repositories added to the pins roster", 1, 1, "repositories", "### section (D1)."),
    ("hooks installed", 1, 1, "hooks",
     "### section (D2): the exclusion kernel's, byte-identical to the repository's own tracked copy."),
    ("installed hooks adapted rather than copied", 0, 0, "hooks",
     "### section (D2): byte-identical to the tracked source -- not similar, not adapted."),
    ("hooks installed without being exercised in both polarities", 0, 0, "hooks",
     "### section (D2) BAR 4: an unexercised hook is an assertion."),

    # ---- COMPONENT 3 ---------------------------------------------------------------------------------
    ("repositories audited", 0, 0, "repositories", "### section (E)/(H): `audit nothing` is the order's own cap."),
    ("public surfaces read for correctness", 0, 0, "surfaces", "### section (E)/(H)."),
    ("claims checked against any kernel", 0, 0, "claims", "### section (E)/(H)."),
    ("repositories graded", 0, 0, "repositories", "### section (E)."),
    ("federation enumerations taken from recall rather than live", 0, 0, "enumerations",
     "### section (E): a list typed from memory is the species DESK_FRESHNESS was minted against."),
    ("count-shaped strings reported as claims", 0, 0, "strings",
     "### section (E): a count-shaped string is not a claim and this act does not call it one."),
    ("ranking criteria invented by this seat", 0, 0, "criteria",
     "### section (E): the order supplied the criterion; this act does not silently reweight it."),
    ("price parts reported separately", 3, 3, "parts",
     "### section (E): one repository, the whole federation, and the split between mechanical and read."),
    ("hint clauses scored", 2, 2, "clauses",
     "### section (E): (H1) and (H2), each CONFIRMED / CORRECTED / NOT LOCATED, against what is found."),

    # ---- THE BARS AND THE SUITE ----------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (F): no frame, seed, transform, quadrature, fit, score or series. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (F): UNPRICED, and said so rather than left blank."),
    ("exact bars", 4, 4, "bars", "### section (F): preservation, export, bounded-edit, polarity."),
    ("multi-arm bars", 0, 0, "bars", "### section (F): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (F): (R2) is law, and G-BYCONTENT re-measures it with b366's detector."),
    ("arms whose side is left undeclared", 0, 0, "arms",
     "### section (F): b352's rule, and b368's incident (vii) -- G-REF is side-dependent and says so."),

    # ---- THE RECORD ----------------------------------------------------------------------------------
    ("relay tools created", 7, 7, "files",
     "the regspec, the extract, the classifier-and-repair, the hygiene tool, the pass pricer, the trail writer and the bank writer; plus this act's suite and its correspondence and index writers."),
    ("shared utilities created", 0, 0, "files", "none. ### b363's, b366's and b354's helpers are USED, not extended."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (H)."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal: private until the provisionals."),
    ("SIDE-effects files written", 1, 1, "files", "### section (B): the front document and no other."),
    ("PLACE-papers files written", 2, 1, "files",
     "### the closing: OPEN_TRAILS.md for the front document's state after (R4); FACES_LEDGER.md only if a row moves. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("faces ledger rows moved", 0, 0, "rows", "### the closing: only if a row moves, and a repair of a front document moves none."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none. ### THE FOLD IS THE NEXT ACT'S, AND THIS ONE DRAFTS IT."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("desk items closed by this act", 0, 0, "items",
     "### the closing: the sweep produces MARKS, NOT VERDICTS, in the order's own words."),
    ("acts re-verdicted", 0, 0, "acts",
     "### section (H): b368 is RE-MEASURED and its disposition SUPERSEDED BY A RULING, which is the author's act."),
    ("equivalences compiled", 0, 0, "compilations", "### section (H)."),
    ("bars moved", 0, 0, "bars", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (H)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (H)."),
    ("faces promoted", 0, 0, "faces", "### section (H)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (H)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (H): the order's own refusal."),
    ("posture-lock changes", 0, 0, "changes", "### section (H)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (H): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): what preceded the lock is declared, and the hint is scored against the files."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b369_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b369_registration_2026-09-08.txt -- b369, THE LIST REPAIRED, THE "
                            "ROSTER MENDED, THE PASS PRICED",
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
