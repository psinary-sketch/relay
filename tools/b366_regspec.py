# -*- coding: utf-8 -*-
"""b366_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b366_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b366_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A)/(I): nothing deposits, in every branch."),
    ("network calls for text", 0, 0, "calls", "### section (I): no source is fetched; the pins' ls-remote is the ritual's own."),
    ("sources fetched", 0, 0, "sources", "### section (I)."),
    ("deposited artifacts touched", 0, 0, "files", "### section (I)."),
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (G): no frame, seed, transform, quadrature, fit, score or series. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (G): UNPRICED, and said so rather than left blank."),
    ("exact bars", 3, 3, "bars", "### section (G): the enumeration bar, the detector bar, the unedited bar."),
    ("multi-arm bars", 0, 0, "bars", "### section (G): every bar is marked SINGLE-ARM."),
    ("verdict branches on the rewrite rule", 2, 2, "branches",
     "### section (H): a fixture-backed helper, or a work-order with its price. ### The order fixes both."),
    ("branches left unclaimed", 0, 0, "branches", "### section (H): a branch not taken is shown unreachable (b350's rule)."),
    ("rulings made by this seat", 0, 0, "rulings",
     "### section (A)/(I): R1, R2 and R3 are the author's; this act executes them."),
    ("thresholds set by this seat", 0, 0, "thresholds", "### section (I): R1 is RECORDED here, not set here."),
    ("past suites edited", 0, 0, "files",
     "### section (C)/(I): NOT ONE, and the proof is byte-for-byte against the committed blobs at both ends."),
    ("arms rewritten in place", 0, 0, "arms", "### section (A): a rewrite RULE is a thing a later act applies."),
    ("dated arms cured by this act", 0, 0, "arms", "### section (I): the sweep classifies and prices; it does not cure."),
    ("past verdicts withdrawn", 0, 0, "verdicts", "### section (I): none, and b363's control is RELABELLED, which is not the same thing."),
    ("acts re-verdicted", 0, 0, "acts", "### section (I): b357, b363, b364 and b365 stand as banked."),
    ("counts predicted for the sweep in this registration", 0, 0, "counts",
     "### section (C): the count is the act's evidence, and a registration that named a figure would score its own survey against itself."),
    ("arms counted from memory rather than from a suite's own code", 0, 0, "arms",
     "### section (G) BAR 1: an arm the tool cannot attribute is reported as unattributed, never dropped."),
    ("classification values available", 2, 2, "values", "### section (C): STANDING or DATED, each with its reason."),
    ("classifications of flagged arms inferred by a scanner", 0, 0, "classifications",
     "### section (C): DECLARED BY THIS SEAT with the code quoted beside it -- b357's cure."),
    ("detectors believed before they are scored", 0, 0, "detectors",
     "### section (G) BAR 2: it must find the one confirmed instance and hold fixtures in BOTH polarities."),
    ("figures reported as one that the order asked for apart", 0, 0, "figures",
     "### section (C): how many dated arms exist, and how many are one substitution from standing."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (G): an act that swept for dated arms and shipped one would have refuted itself."),
    ("shared utilities created", 1, 1, "files",
     "### section (C): the rewrite helper, IF the order's own test puts it on that side; otherwise 0 and a work-order instead."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### section (D): committed locally, NOT pushed, as every module since b330."),
    ("TECHNE files written", 1, 1, "files", "### section (D): the dated-arm module, under modules/2026-09."),
    ("faces ledger blocks appended", 1, 1, "blocks", "### section (E): one, on row U1, through the ledger's own writer, for R3 only."),
    ("faces ledger rows rewritten", 0, 0, "rows", "### section (E): the writer appends; no row above is touched."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (E)/(I): R3's word is the author's and is APPLIED, not conferred."),
    ("faces promoted", 0, 0, "faces", "### section (I)."),
    ("relay tools created", 6, 6, "files",
     "the regspec, the extract, the sweep, the mint, the ledger-row writer and the correspondence writer; plus the index writer and this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none. ### The rewrite helper, if written, is NEW."),
    ("PLACE-papers files written", 1, 1, "files", "### section (E): FACES_LEDGER.md and no other. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("equivalences compiled", 0, 0, "compilations", "### section (I)."),
    ("bars moved", 0, 0, "bars", "### section (I)."),
    ("new mathematics", 0, 0, "statements", "### section (I)."),
    ("findings re-verdicted", 0, 0, "findings", "### section (I): b358's circularity finding is untouched."),
    ("coordinates closed", 0, 0, "coordinates", "### section (I)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (I)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (I): the order's own refusal."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("posture-lock changes", 0, 0, "changes", "### section (I)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (I): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): b361's rule, and the pre-lock survey is declared rather than concealed."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b366_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b366_registration_2026-09-07.txt -- b366, THE DATED-ARM SWEEP",
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
