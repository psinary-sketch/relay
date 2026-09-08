# -*- coding: utf-8 -*-
"""b365_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before the read.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b365_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b365_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A)/(H): nothing deposits, in every branch."),
    ("network calls for text", 0, 0, "calls", "### section (H): NO NEW SOURCE IS FETCHED. ### The pinned rendering on disk is the only text read."),
    ("sources fetched", 0, 0, "sources", "### section (A): the cap forbids it."),
    ("deposited artifacts touched", 0, 0, "files", "### section (H)."),
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (F): no frame, seed, transform, quadrature, fit, score or series. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (F): UNPRICED, and said so rather than left blank."),
    ("exact bars", 3, 3, "bars", "### section (F): the quotation bar, the separation bar, the ledger-pass bar."),
    ("multi-arm bars", 0, 0, "bars", "### section (F): every bar is marked SINGLE-ARM."),
    ("verdict branches", 3, 3, "branches", "### section (E): located and covers / located and does not cover / not located."),
    ("branches left unclaimed", 0, 0, "branches", "### section (E): a branch not taken is shown unreachable (b350's rule)."),
    ("grades moved in either direction", 0, 0, "grades",
     "### section (E)/(H): the cap's last clause is absolute, and it binds every branch."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (H)."),
    ("faces promoted", 0, 0, "faces", "### section (H)."),
    ("statements attributed to the source without a located quotation", 0, 0, "statements",
     "### section (F) BAR 1: pulled by the anchor tool with its line, into the extract, before any argument."),
    ("judgements printed as quotations", 0, 0, "judgements",
     "### section (F) BAR 2: what the source states and what this record concludes are printed apart and marked apart."),
    ("ledger rows examined outside the bounded pass", 0, 0, "rows",
     "### section (B): the rows citing b358 and b361, and nothing wider; each reported by its own identifier."),
    ("ledger rows appended or rewritten", 0, 0, "rows", "### the closing: the writer runs only if a row moves, and a read moves none."),
    ("findings re-verdicted", 0, 0, "findings", "### section (H): b358's circularity finding is untouched in every branch."),
    ("acts re-verdicted", 0, 0, "acts", "### section (H): b358, b361, b363 and b364 stand as banked."),
    ("thresholds ruled by this seat", 0, 0, "thresholds",
     "### section (D): the fold threshold is PROPOSED to the author and fixed by ruling, not here."),
    ("mechanized arms shipped for the wrong-arm species", 0, 0, "arms",
     "### section (D): the mint has NO mechanizable half and the module says so in its own header."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### section (D): committed locally, NOT pushed, as every module since b330."),
    ("TECHNE files written", 1, 1, "files", "### section (D): the module, under modules/2026-09."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (H)."),
    ("arms comparing a line number of a file outside this act", 0, 0, "arms",
     "### section (F): b364's finding, applied the day after it was filed."),
    ("relay tools created", 6, 6, "files",
     "the regspec, the extract, the reader, the mint-and-threshold writer, the correspondence writer and the index writer; plus this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("shared utilities created", 0, 0, "files", "none. ### b363's helper is USED, not extended."),
    ("PLACE-papers files written", 1, 0, "files",
     "0 unless the branch taken files something there; capped at 1, and the mirror is owed if and only if the repo moves."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("equivalences compiled", 0, 0, "compilations", "### section (H): nothing compiled, no bridge typed."),
    ("bars moved", 0, 0, "bars", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),
    ("corrections to the source", 0, 0, "corrections",
     "### section (E): a finding about this record's reading is NOT a correction of the source."),
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
     "### section (A-PRE): b361's rule, and the pre-lock grep is declared rather than concealed."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b365_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b365_registration_2026-09-07.txt -- b365, THE OWED READ, PAID",
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
