# -*- coding: utf-8 -*-
"""b368_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any read of the kernel.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b368_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b368_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A)/(H): nothing deposits, in either branch."),
    ("network calls for text", 0, 0, "calls", "### the pins' and the fetch's ls-remote are the ritual's own; no source is fetched for text."),
    ("deposited artifacts touched", 0, 0, "files", "### section (H)."),
    ("`.lean` files touched", 0, 0, "files", "### section (A)/(D)/(H): the order's own clause, in EITHER branch."),
    ("terminals written", 0, 0, "terminals", "### section (H)."),
    ("statements proved", 0, 0, "statements", "### section (H)."),
    ("builds run", 0, 0, "builds", "### section (C): a profile is READ from a printed record or reported NO PRINTED PROFILE."),
    ("existing sentences of the front document edited", 0, 0, "sentences",
     "### section (D): the append-only test is mechanical -- true prefix of the file and of its blob."),
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (F): no frame, seed, transform, quadrature, fit, score or series. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (F): UNPRICED, and said so rather than left blank."),
    ("exact bars", 3, 3, "bars", "### section (F): the re-derivation bar, the evidence bar, the append-only bar."),
    ("multi-arm bars", 0, 0, "bars", "### section (F): every bar is marked SINGLE-ARM."),
    ("verdict branches on the repair", 2, 2, "branches", "### section (D): append-only reconciliation, or priced and routed."),
    ("branches left unclaimed", 0, 0, "branches", "### section (D): the branch not taken is shown unreachable (b350's rule)."),
    ("figures carried from a prior act rather than re-derived", 0, 0, "figures",
     "### section (B) BAR 1: ADDITION ONE forbids it -- a figure quoted forward is a figure nobody re-measured."),
    ("classifications made without the evidence their kind requires", 0, 0, "classifications",
     "### section (C) BAR 2: a row that cannot produce its evidence takes the weaker kind."),
    ("names classified from their own sound", 0, 0, "names",
     "### section (C): the order's own bar, and the one this seat is most able to break."),
    ("classification kinds available", 4, 4, "kinds", "### section (C): PRESENT, RETIRED, RENAMED, NEVER EXISTED."),
    ("axiom profiles taken from a compile rather than a printed record", 0, 0, "profiles",
     "### section (C): otherwise the row says NO PRINTED PROFILE."),
    ("desk items closed by this act", 0, 0, "items",
     "### section (E)/(H): the sweep produces MARKS, NOT VERDICTS, in the order's own words."),
    ("hooks installed", 0, 0, "hooks",
     "### section (D)/(H): the absence is FILED as a finding; installing one in a repository the order did not name is not this act's to do."),
    ("acts re-verdicted", 0, 0, "acts", "### section (H): b157 and b367 are RE-MEASURED, which is not the same thing."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (F): (R2) is law, and G-BYCONTENT re-measures it with b366's detector."),
    ("relay tools created", 6, 6, "files",
     "the regspec, the extract, the classifier, the desk sweeper, the correspondence writer and the index writer; plus this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("shared utilities created", 0, 0, "files", "none. ### b363's, b366's and b354's helpers are USED, not extended."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (H)."),
    ("TECHNE files written", 1, 1, "files", "### section (E): the desk-freshness module, under modules/2026-09."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### section (E): committed locally, NOT pushed, as every module since b330."),
    ("SIDE-effects files written", 1, 0, "files",
     "### section (D): the front document and no other, and only in the append-only branch; capped at 1, demanded 0 because the branch is not yet decided."),
    ("PLACE-papers files written", 2, 1, "files",
     "### the closing: OPEN_TRAILS.md for the scaffold item's true state; FACES_LEDGER.md only if a row moves. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("faces ledger rows moved", 0, 0, "rows", "### the closing: only if a row moves, and a re-measurement of a front document moves none."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("equivalences compiled", 0, 0, "compilations", "### section (H)."),
    ("bars moved", 0, 0, "bars", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims",
     "### section (H): a classification is about where a declaration is, not about what it would be worth."),
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
     "### section (A-PRE): b361's rule, and what preceded the lock is declared."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b368_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else
                                                    (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": "data/b368_registration_2026-09-08.txt -- b368, THE FRONT DOCUMENT RECONCILED, OR PRICED",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses) and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s' % (len(unsat), unsat if unsat else ''))
    print('  ### ### **CAPS THAT ARE NOT ZERO : %d**' % len(nonzero))
    for c in nonzero:
        print('      %s' % c)
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
