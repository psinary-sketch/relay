# -*- coding: utf-8 -*-
"""b359_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b359_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b359_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A): NOTHING IS DEPOSITED AND NOTHING IS WRITTEN AT ZENODO, in every branch."),
    ("writes to any platform", 0, 0, "writes", "### section (G) Bar 1: the fetch is ONE READ-ONLY GET. ### RE-MEASURED by G-NODEPOSIT on STRIPPED code."),
    ("deposited artifacts touched", 0, 0, "files", "### section (K): the records are immutable at their versions."),
    ("read-only fetches", 1, 1, "fetches", "section (G) Bar 1."),
    ("ranks in the precedence", 3, 3, "ranks", "### section (B): REGISTRY > README > SPIRAL_MAP for deposits."),
    ("repairs running AWAY from the source of truth", 0, 0, "repairs", "### section (B): toward it, never the reverse."),
    ("deposit fields repaired from disk", 0, 0, "fields", "### section (B): disk for live pins only, never for deposits."),
    ("REGISTRY.md writes", 0, 0, "writes", "### section (E): it is the source of truth and this act READS it."),
    ("statuses available per claim", 3, 3, "statuses", "### section (C): CURRENT / STALE / SILENT."),
    ("pins recalled rather than resolved", 0, 0, "pins", "### section (D): every asserted pin by ls-remote, or UNRESOLVED."),
    ("deposit-pins merged with working heads", 0, 0, "merges", "### section (D): they are not the same object, and the ruling is quoted."),
    ("sentences edited in README.md or SPIRAL_MAP.md", 0, 0, "sentences", "### section (E): APPEND-ONLY; a stale sentence is left as written and corrected by an appended note."),
    ("currency notes appended when nothing is stale", 0, 0, "notes", "### section (E): if nothing is stale, nothing is appended."),
    ("mirror rebuilds", 1, 1, "rebuilds", "### section (F): AFTER the repair, verified on all three clauses."),
    ("verdict branches", 4, 4, "branches", "### section (H): three, plus the source-of-truth-versus-fetch outcome."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (G): this act computes nothing."),
    ("exact bars", 4, 4, "bars", "### section (G): the fetch, the anchor, the pin, and the append-only bar."),
    ("multi-arm bars naming what makes the arms independent", 1, 1, "bars", "### section (G) Bar 4: the working copy and the blob see different things."),
    ("claims classified without being located by the anchor tool", 0, 0, "claims", "### section (G) Bar 2."),
    ("relay tools created", 4, 4, "files", "the fetch, the extract, the read, and this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("PLACE-papers files written", 3, None, "files", "### README.md and/or SPIRAL_MAP.md if stale, and FACES_LEDGER.md always. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("faces ledger rows appended", 1, 1, "rows", "### row U1's update block with b358's finding, NAMED-ONLY."),
    ("faces ledger rows rewritten", 0, 0, "rows", "### rows above are never rewritten; an update names the row it bears on."),
    ("equivalences compiled", 0, 0, "compilations", "### section (K): nothing compiled; the deposit's refusal is quoted."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("ledger rows moved", 0, 0, "rows", "section (K)."),
    ("bars moved", 0, 0, "bars", "section (K)."),
    ("grades conferred by a seat", 0, 0, "grades", "section (K)."),
    ("acts re-verdicted", 0, 0, "acts", "section (K)."),
    ("proofs attempted", 0, 0, "proofs", "section (K)."),
    ("new mathematics", 0, 0, "statements", "section (K)."),
    ("coordinates closed", 0, 0, "coordinates", "section (K)."),
    ("claims about the quantifier", 0, 0, "claims", "section (K)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "section (K)."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("posture-lock changes", 0, 0, "changes", "### section (K): the posture lock is separate and is not touched by a currency pass."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
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
    spec = {"registration": "data/b359_registration_2026-09-07.txt -- b359, THE LEDGER CURRENCY PASS", "clauses": clauses}
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
