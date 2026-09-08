# -*- coding: utf-8 -*-
"""b371_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b371_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b371_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (H): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (H)."),
    ("`.lean` files touched", 0, 0, "files", "### section (H)."),
    ("terminals written", 0, 0, "terminals", "### section (H)."),
    ("statements proved", 0, 0, "statements", "### section (H)."),
    ("builds run", 0, 0, "builds",
     "### section (B)/(H): the profile is READ as a printed record."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),

    ("settling verdicts emitted", 1, 1, "verdicts",
     "### section (B) BAR 1: one, and one of the two ruled words."),
    ("verdict words invented beyond the two ruled", 0, 0, "words",
     "### section (B): SCOPE-DEPENDENT or STALE, and no third."),
    ("scopes claimed without a document that states them", 0, 0, "scopes",
     "### section (B) BAR 1: a sum that happens to match is not a scope; a sentence that names it is."),
    ("profile counts read from a working file without its blob", 0, 0, "counts",
     "### section (B) BAR 2: b309's rule for this repository."),
    ("descriptions rewritten by this seat in the scope-dependent branch", 0, 0, "edits",
     "### section (B)/(H): the wording is ROUTED to the author."),
    ("adjacent findings repaired rather than routed", 0, 0, "findings",
     "### section (B): the README figures are recorded and routed, as b369 recorded the count claim it was not sent to repair."),

    ("rows checked", 0, 0, "rows", "### section (C)/(H): `audit nothing` is the order's own clause."),
    ("kernels opened for a row", 0, 0, "kernels", "### section (C)/(H)."),
    ("inventory fields not present in the row they are taken from", 0, 0, "fields",
     "### section (C) BAR 3."),
    ("completeness claimed for the row predicate", 0, 0, "claims",
     "### section (C): PREDICATE_ONE_SHAPE -- the sweep reports the shapes it matched and the rows it rejected."),
    ("rows without a pin reported as sweep misses rather than findings", 0, 0, "rows",
     "### section (C): a row without a pin cannot be checked the way (R6) specifies."),
    ("price parts reported separately", 3, 3, "parts",
     "### section (C): one row, the whole set, and the split."),
    ("ranking criteria invented by this seat", 0, 0, "criteria",
     "### section (C): the order supplied pin age, count-versus-terminal, and kernel moved since."),
    ("cross-references presented as checks", 0, 0, "references",
     "### section (C): comparing a name against the record's own banked classification opens no kernel and verifies no row."),

    ("hook outcomes chosen", 1, 1, "outcomes",
     "### section (D): made durable OR struck, and the order forbids both."),
    ("hook outcomes chosen by preference rather than by test", 0, 0, "outcomes",
     "### section (D): the choice is made by what the tracked path can actually carry."),
    ("repositories whose guard is exercised in both polarities", 4, 4, "repositories",
     "### section (D) BAR 4: an unexercised hook is an assertion."),
    ("residual manual steps left unnamed", 0, 0, "steps",
     "### section (D): the hooks-path setting is LOCAL CONFIG and a clone still runs no guard until someone sets it."),
    ("durability described as complete when it is not", 0, 0, "claims",
     "### section (D): what travels is the GUARD, not the configuration."),
    ("owner instrument files edited", 1, 1, "files",
     "### section (D): the hook exerciser, named on this face BEFORE the edit; any other instrument moving is still a failure."),
    ("guards moved without their exerciser following", 0, 0, "guards",
     "### section (D): GUARD_WITH_NOTHING_LISTENING, already in this record's lore."),
    ("superseded hook copies deleted", 0, 0, "files",
     "### section (D): the old location is left inert and the second copy is named as both a net and a trap."),

    ("desk items closed without a killing file and date", 0, 0, "items",
     "### section (E) BAR 5: a closure without a killing file is an opinion."),
    ("items closed on the order's say-so rather than on evidence", 0, 0, "items",
     "### section (E): the rule (R7) states is that the killing file is NAMED."),
    ("acts re-verdicted", 0, 0, "acts",
     "### section (A)/(H): (R7) reverses a disposition three acts carried; that is the author's ruling."),

    ("quantities computed about the object", 0, 0, "quantities",
     "### section (F): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (F): UNPRICED, and said so rather than left blank."),
    ("exact bars", 5, 5, "bars",
     "### section (F): settling, profile, inventory, polarity, closure."),
    ("multi-arm bars", 0, 0, "bars", "### section (F): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (F): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms",
     "### section (F): b352's rule, and b370's incident (vi)."),

    ("relay tools created", 8, 8, "files",
     "the regspec, the extract, the settler, the inventory, the hook mover, the desk sweeper, the bank writer and the trail writer; plus this act's suite and its correspondence and index writers."),
    ("shared utilities created", 0, 0, "files", "none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (H)."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 1, 1, "files",
     "### section (D): the tracked guard, and no other."),
    ("SIDE-global-section files written", 1, 1, "files",
     "### section (D): the tracked guard. ### The DESCRIPTION is account metadata, not a file in this repository."),
    ("PLACE-papers files written", 3, 2, "files",
     "### section (D)/(E): the tracked guard; OPEN_TRAILS.md for each item that closes; FACES_LEDGER.md only if a row moves. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("faces ledger rows moved", 0, 0, "rows", "### only if a row moves."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("equivalences compiled", 0, 0, "compilations", "### section (H)."),
    ("bars moved", 0, 0, "bars", "### section (H)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (H)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (H)."),
    ("faces promoted", 0, 0, "faces", "### section (H)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (H)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (H): the order's own refusal."),
    ("posture-lock changes", 0, 0, "changes", "### section (H)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (H): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): what preceded the lock is declared in unusual detail, because the read that settles Component 1 was begun before it."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b371_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b371_registration_2026-09-08.txt -- b371, THE AUDIT'S FIRST TARGET, "
                            "THE DESK CLOSED, THE HOOK MADE DURABLE",
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
