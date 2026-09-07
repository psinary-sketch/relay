# -*- coding: utf-8 -*-
"""b357_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE any file of the act is written.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b357_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b357_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("ledger rows edited", 0, 0, "rows", "### section (A): a READ. Not one byte of the four ledgers changes."),
    ("verdicts moved", 0, 0, "verdicts", "section (A)."),
    ("acts re-verdicted", 0, 0, "acts", "section (H)."),
    ("checks demoted", 0, 0, "checks", "### section (H): every check that passed still passed."),
    ("ledgers read", 4, 4, "ledgers", "### section (B): FINDINGS, FACES_LEDGER, CORRESPONDENCE, banked_index."),
    ("row statuses available", 3, 3, "statuses", "### section (C): SAYS THE WIDER SENTENCE / SAYS THE NARROWER SENTENCE / SILENT."),
    ("findings kept apart", 2, 2, "findings", "### section (C): the attribution fault and the membership question, never merged."),
    ("tables produced", 1, 1, "tables", "section (F): G-TABLE, one table."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (E): this act computes nothing."),
    ("exact bars", 1, 1, "bars", "section (E): the located row, marked SINGLE-ARM with its floor."),
    ("ERRATA entries opened", 0, 0, "entries", "### section (D): an entry is DRAFTED and ROUTED, never opened by this seat."),
    ("ERRATA entries drafted", 1, 1, "drafts", "### section (D): if the second branch is taken; the draft lives in this act's own files."),
    ("relay tools created", 3, 3, "files", "the extract, the read, and this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none: everything is READ."),
    ("PLACE-papers files written", 0, 0, "files", "### none: the hook and the mirror are NOT owed, and that is CHECKED."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("faces ledger rows appended", 0, 0, "rows", "none in this leg."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("ledger rows moved", 0, 0, "rows", "section (H)."),
    ("bars moved", 0, 0, "bars", "section (H)."),
    ("grades conferred by a seat", 0, 0, "grades", "section (H)."),
    ("proofs attempted", 0, 0, "proofs", "section (A)."),
    ("new mathematics", 0, 0, "statements", "section (A)."),
    ("claims that a ledger row is false", 0, 0, "claims", "### section (C): the wider sentence is not necessarily false."),
    ("claims about the quantifier", 0, 0, "claims", "section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "section (H)."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("deposited texts touched", 0, 0, "files", "none."),
    ("sealed files edited", 0, 0, "files", "none."),
    ("mirror roster rows changed", 0, 0, "rows", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b357_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    clauses = [{"clause": c, "cap": cap, "demand": (n if dem is None else dem), "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": "data/b357_registration_2026-09-07.txt -- b357, WHAT THE LEDGERS SAY THE CHECKS CERTIFY", "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses) and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s' % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s' % (len(unsat), unsat if unsat else ''))
    print('  ### ### **CAPS THAT ARE NOT ZERO : %d**' % len(nonzero))
    for c in nonzero:
        print('      %s' % c)
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
