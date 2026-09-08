# -*- coding: utf-8 -*-
"""b364_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any read of the suite
### under diagnosis and before any run of it.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b364_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b364_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A)/(H): nothing deposits, in every branch."),
    ("network calls to any platform", 0, 0, "calls", "### section (A): this act makes none beyond the pins' ls-remote."),
    ("deposited artifacts touched", 0, 0, "files", "### section (H)."),
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (E): no frame, seed, transform, quadrature, fit, score or series. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (E): UNPRICED, and said so rather than left blank."),
    ("exact bars", 3, 3, "bars", "### section (E): the quotation bar, the location bar, the unchanged bar."),
    ("multi-arm bars", 0, 0, "bars", "### section (E): every bar is marked SINGLE-ARM."),
    ("verdict branches", 3, 3, "branches", "### section (C): environmental / real / undecided."),
    ("branches left unclaimed", 0, 0, "branches", "### section (C): a branch not taken is shown unreachable (b350's rule)."),
    ("branches decided before the diagnosis is seen", 3, 3, "branches",
     "### section (C): fixed in this file, and section (A-PRE) declares what was and was not read first."),
    ("arms repaired", 0, 0, "arms", "### section (A)/(D): DO NOT REPAIR-TO-PASS is the order's own phrase and is a bar."),
    ("predicates paraphrased rather than quoted", 0, 0, "predicates",
     "### section (E) BAR 1: the arm's predicate is quoted from its own suite by the anchor tool."),
    ("banked suites run at their own location", 1, 1, "suites",
     "### section (E) BAR 2: b357's suite, run where it lives, UNEDITED, its verdict line reported verbatim."),
    ("banked suites edited", 0, 0, "files", "### section (D): NOT ONE, and the proof is byte-for-byte against the blob."),
    ("banks edited", 0, 0, "files", "### section (D)."),
    ("index files edited", 0, 0, "files", "### section (D): tools/banked_index.py is READ by the arm and is not written by the diagnosis."),
    ("run files of other acts edited", 0, 0, "files", "### section (D)."),
    ("copies left on disk after the run", 0, 0, "files", "### section (D): a copy is made, run, and deleted in a finally."),
    ("verdicts moved by this seat", 0, 0, "verdicts", "### section (A)/(H): in every branch."),
    ("acts re-verdicted", 0, 0, "acts", "### section (H): b357 stands exactly as banked, and so does b363."),
    ("relay tools created", 6, 6, "files",
     "the regspec, the extract, the diagnosis runner, the correspondence writer, the index writer and this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("shared utilities created", 0, 0, "files", "none. ### b363's helper is USED, not extended."),
    ("TECHNE files written", 0, 0, "files", "none in this leg."),
    ("PLACE-papers files written", 1, 0, "files",
     "### section (F): 0 unless the branch taken files something there; capped at 1, and the mirror is owed if and only if the repo moves."),
    ("faces ledger rows appended or rewritten", 0, 0, "rows", "### the closing: the writer runs only if a row moves, and a gate diagnosis moves no face."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act; a finding for the author is not an ERRATA entry."),
    ("equivalences compiled", 0, 0, "compilations", "### section (H): nothing compiled, no bridge typed."),
    ("ledger rows moved", 0, 0, "rows", "### section (H)."),
    ("bars moved", 0, 0, "bars", "### section (H)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (H)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (H): the order's own refusal."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("posture-lock changes", 0, 0, "changes", "### section (H)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (H): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): b361's rule. ### Every figure is read from a file or a run."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b364_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b364_registration_2026-09-07.txt -- b364, THE COPY THAT DID NOT REPRODUCE",
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
