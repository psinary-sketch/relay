# -*- coding: utf-8 -*-
"""b372_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b372_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b372_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (H): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (H)."),
    ("`.lean` files touched", 0, 0, "files", "### section (H)."),
    ("terminals written", 0, 0, "terminals", "### section (H)."),
    ("statements proved", 0, 0, "statements", "### section (H)."),
    ("builds run", 0, 0, "builds",
     "### section (C)/(D)/(H): every profile is READ as a printed record."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),

    # ---- COMPONENT 1 -------------------------------------------------------------------------------
    ("repositories whose end-of-line attribute is verified", 4, 4, "repositories",
     "### section (B) BAR 1: every repository the roster names."),
    ("repositories written to that already carried the attribute", 0, 0, "repositories",
     "### section (B): the order's own instruction -- say so rather than writing it twice."),
    ("existing attribute lines replaced rather than preserved", 0, 0, "lines",
     "### section (B): a path-scoped line is PRESERVED and the repository-wide line is added beside it."),
    ("working files deleted to force a checkout", 0, 0, "files",
     "### section (B)/(H): the fresh checkout is taken into a scratch directory. ### b371's destructive incident."),
    ("scratch branches created or reset in any repository", 0, 0, "branches",
     "### section (H): b371's destructive incident, named so the shape cannot recur quietly."),
    ("repositories renormalised", 0, 0, "repositories",
     "### section (B): an attribute added today does not normalise a tree checked out yesterday, and this act does not renormalise one."),
    ("attribute checks run in one polarity only", 0, 0, "checks",
     "### section (F) BAR 2: with the attribute suppressed the same extraction must FAIL to match."),
    ("durability claimed beyond what a tracked file gives", 0, 0, "claims",
     "### section (B): what is fixed is what the NEXT checkout produces."),

    # ---- COMPONENT 2 -------------------------------------------------------------------------------
    ("README candidates read at content", 2, 2, "documents",
     "### section (C): both the exclusion kernel's and the construction kernel's."),
    ("README documents repaired", 1, 0, "documents",
     "### section (C): only the one the order's DESCRIPTION fits, and only if a number rather than a claim is at stake."),
    ("files written in the exclusion kernel's README", 0, 0, "files",
     "### section (C)/(H): nothing there is repaired by this act."),
    ("label-versus-description discrepancies absorbed silently", 0, 0, "discrepancies",
     "### section (C): b367's species -- reported at full prominence."),
    ("figures whose scope is asserted without a sentence that states it", 0, 0, "figures",
     "### section (C) BAR 4: a sum that happens to match is not a scope."),
    ("figures restated with a new number instead of removed", 0, 0, "figures",
     "### section (C): REMOVED rather than restated, unless the document can name the ref it holds at."),
    ("originals edited without a verbatim copy banked first", 0, 0, "originals",
     "### section (F) BAR 3: preserve by quotation, repair by edit -- (R4), unamended."),
    ("claims rewritten rather than routed", 0, 0, "claims",
     "### section (C): if the repair would rewrite a claim rather than a number, it is ROUTED."),

    # ---- COMPONENT 3 -------------------------------------------------------------------------------
    ("flagged rows classified", 12, 12, "rows",
     "### section (D): the set b371 flagged, re-anchored by content and not re-derived."),
    ("rows repaired", 0, 0, "rows",
     "### section (D)/(H): the order's own cap -- the classification is the product."),
    ("pins added to any row", 0, 0, "pins",
     "### section (D)/(H): (R8) makes that a separate ruling, priced and not attempted."),
    ("classification words used beyond the four the order ruled", 0, 0, "words",
     "### section (D): PRESENT, RETIRED, RENAMED, ABSENT, and no fifth."),
    ("pinless rows opened at a pin", 0, 0, "rows",
     "### section (D): a pinless row is opened at the kernel's live head, and nowhere else."),
    ("pinned rows opened at a head rather than at their pin", 0, 0, "rows",
     "### section (D) BAR 5."),
    ("heads written into a row", 0, 0, "heads",
     "### section (A)/(D): (R8) -- the head is recorded in this act's own bank and NEVER in the row."),
    ("pinless verdicts left unmarked as checked at head", 0, 0, "verdicts",
     "### section (D) BAR 5: weaker than a pinned row's check, and the record says why."),
    ("retirement verdicts without the kernel's own record quoted", 0, 0, "verdicts",
     "### section (F) BAR 6: RETIRED is the kernel's record quoted, not this seat's inference from absence."),
    ("rename verdicts without a successor located", 0, 0, "verdicts", "### section (F) BAR 6."),
    ("kernels read through the working tree rather than through a ref", 0, 0, "kernels",
     "### section (D): git show <ref>:<path>, so a check at a pin is a check at that pin (b309)."),
    ("routings acted on rather than reported", 0, 0, "routings",
     "### section (D): what a classification implies for the papers is reported and routed, not acted on."),

    # ---- THE DESK ----------------------------------------------------------------------------------
    ("desk items closed without a killing file and date", 0, 0, "items",
     "### section (E): a closure without a killing file is an opinion."),
    ("desk items confirmed from this act's own paperwork", 0, 0, "items",
     "### section (E): b368's defect, mechanised in the sweeper."),
    ("acts re-verdicted", 0, 0, "acts", "### section (H)."),

    # ---- THE BARS ----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (F): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (F): UNPRICED, and said so rather than left blank."),
    ("exact bars", 7, 7, "bars",
     "### section (F): attribute, polarity, preservation, scope, ref, retirement-evidence, no-repair."),
    ("multi-arm bars", 0, 0, "bars", "### section (F): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (F): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms",
     "### section (F): b352's rule, and b370's incident (vi)."),

    # ---- WHAT MOVES ON DISK ------------------------------------------------------------------------
    ("relay tools created", 12, 12, "files",
     "the regspec, the extract, the gate suite, the reg gate, the attribute tool, the README tool, "
     "the batch classifier, the desk sweeper, the trail writer, the correspondence writer, the index "
     "writer and the bank writer."),
    ("shared utilities created", 0, 0, "files", "none."),
    ("owner instrument files edited", 0, 0, "files",
     "none is licensed by this order; any instrument moving is a failure of the run."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (H)."),
    ("relay tracked files written outside tools and data", 1, 1, "files",
     "### section (B): the attribute file, and no other."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 1, 1, "files",
     "### section (B): the attribute file, and no other."),
    ("SIDE-global-section files written", 2, 1, "files",
     "### section (C): the README if a number is repaired; and CORRESPONDENCE.md at the closing."),
    ("PLACE-papers files written", 1, 0, "files",
     "### section (E): OPEN_TRAILS.md for each item that closes. ### NO ROW IS TOUCHED. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("SIDE-kernel files written", 0, 0, "files",
     "### section (D): it is opened READ-ONLY for one row and is not on the roster."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
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
    ("federation-wide surface sweeps opened", 0, 0, "sweeps",
     "### section (H): (R6)'s second pass stays shut."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (H): the order's own refusal."),
    ("posture-lock changes", 0, 0, "changes", "### section (H)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (H): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): the reconnaissance that identified Component 2's object is declared there."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b372_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b372_registration_2026-09-08.txt -- b372, THE README, THE EOL PIN, "
                            "AND THE FIRST BATCH",
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
