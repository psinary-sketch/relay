# -*- coding: utf-8 -*-
"""b386_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b386_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b386_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (J): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (J)."),
    ("`.lean` files touched", 0, 0, "files", "### section (J)."),
    ("terminals written", 0, 0, "terminals", "### section (J)."),
    ("statements proved", 0, 0, "statements", "### section (J)."),
    ("builds run", 0, 0, "builds", "### section (J)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),

    # ---- STEP ZERO AND THE DECLARED READINGS -----------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378`s gate run as b386, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates",
     "### section (A)/(H) BAR 1."),
    ("readings of the order declared in advance on this face", 6, 6, "readings",
     "### section (A): nine copies not two; every copy recoverable; core.hooksPath in all four; "
     "the repaired line reached only relay; the destroyed backup identified; and the attestation "
     "result known before the lock."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims", "### section (A)."),

    # ---- COMPONENT 1: THE OPTIONS ----------------------------------------------------------------
    ("b385 options reproduced verbatim with their locations", 3, 3, "options",
     "### section (B)/(H) BAR 2: all three, read by the anchor tool from the file that carries "
     "them."),
    ("options invented by this seat", 0, 0, "options",
     "### section (B)/(H) BAR 2: THE AUTHOR DOES NOT RULE ON OPTIONS A SEAT HAS NOT SHOWN HIM."),
    ("options named as implementing (R15)", 1, 1, "options",
     "### section (B): exactly one, with the ruling`s own words beside it."),
    ("options re-worded to make them fit", 0, 0, "options", "### section (B)."),

    # ---- COMPONENT 2: THE REPAIR -----------------------------------------------------------------
    ("tracked guard copies per rostered repository after this act", 1, 1, "copies",
     "### section (C)/(H) BAR 3: (R15) allows exactly one."),
    ("tracked guard copies deleted", 1, 1, "files",
     "### section (C): relay/tools/git-hooks/pre-push, (R15)`s first disposal."),
    ("copies deleted without a printed recoverability proof", 0, 0, "files",
     "### section (C)/(H) BAR 5: THE PROOF IS PRINTED BEFORE THE DELETION, NOT AFTER."),
    ("installer SOURCE constants repointed", 1, 1, "constants",
     "### section (C): at .githooks/pre-push, the file the repositories run."),
    ("rostered repositories whose installed guard is compared against the source`s own blob",
     4, 4, "repositories",
     "### section (C)/(H) BAR 4: LF-normalised, never by filename and never by size alone."),
    ("rostered repositories whose installed guard carries the repaired line after this act",
     4, 4, "repositories", "### section (C)/(H) BAR 4."),
    ("untracked .git/hooks/pre-push copies deleted", 0, 0, "files",
     "### section (C)/(F): (R15)`s THIRD disposal is already in force for them via "
     "core.hooksPath, and deleting them would remove a working fallback the order did not ask to "
     "remove."),
    ("rostered repositories exercised in both polarities", 4, 4, "repositories",
     "### section (C)/(H) BAR 6."),
    ("repositories failing in this act`s hook record", 0, 0, "repositories",
     "### section (C)/(H) BAR 6: b385`s exact predicate, kept."),
    ("gate arms widened to clear a failure", 0, 0, "arms",
     "### section (C): THE FAILING GATE IS CLEARED BY THE REPAIR AND NOT BY THE ARM."),

    # ---- COMPONENT 3: THE INSTALLER`S SECOND DEFECT ----------------------------------------------
    ("installer defects repaired", 1, 1, "defects",
     "### section (D): it must not overwrite a backup it did not create."),
    ("polarities the backup fixture holds in", 2, 2, "polarities",
     "### section (D)/(H) BAR 7: A FIXTURE THAT PASSES IN ONLY ONE POLARITY IS NOT A FIXTURE."),
    ("components routed for want of a face this act wrote itself", 0, 0, "components",
     "### section (D): that would be this seat routing its own omission."),
    ("backups whose lost content is left unidentified", 0, 0, "backups",
     "### section (D): named with its byte count, its digest and the ref it is recoverable from."),

    # ---- COMPONENT 4: THE TWO FILINGS ------------------------------------------------------------
    ("search term lists printed in full", 2, 2, "lists",
     "### section (E): b383`s six and b385`s seven, taken from those acts` own tools."),
    ("attestation sweeps run", 2, 2, "sweeps",
     "### section (E)/(H) BAR 8: the corpus as it stands, and with the b383-b386 records "
     "excluded."),
    ("mechanizable checks filed without their limit stated", 0, 0, "checks",
     "### section (E)/(G): NECESSARY AND NOT SUFFICIENT, as b378`s control rule turned out to "
     "be."),
    ("TECHNE modules written", 1, 1, "files", "### section (E)/(F): beside the arm species."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("paraphrase clauses corrected on the record", 1, 1, "clauses",
     "### section (E)(ii): the manifest clause, marked OVER-STATED with the rule`s own words "
     "beside it."),
    ("rules edited", 0, 0, "rules",
     "### section (E)(ii)/(J): THE CORRECTION IS OF A PARAPHRASE AND NOT OF THE RULE."),

    # ---- THE BARS AND THE ARMS -------------------------------------------------------------------
    ("exact bars", 8, 8, "bars",
     "### section (H): stamped-gate, option, single-source, propagation, recoverability, "
     "exercise, backup, attestation."),
    ("multi-arm bars", 0, 0, "bars", "### section (H)."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352`s rule."),
    ("arms that measure differently on the two sides of the push", 0, 0, "arms",
     "### section (H): b385`s defect, made a bar."),

    # ---- WHAT MOVES ON DISK ----------------------------------------------------------------------
    ("relay tools created", 6, 6, "files",
     "the extract, the regspec, the reg gate, the four-component writer, the desk-and-bank "
     "writer, and this act`s gate suite. ### SIX FILES AND SIX ROLES. ### THE LOCK GATE IS "
     "b378`S, RUN AS b386."),
    ("shared utilities created", 0, 0, "files",
     "### NONE. ### The attestation check is an experiment inside this act`s components and is "
     "not promoted to a shared tool by the act that invented it."),
    ("owner instrument files edited", 1, 1, "files",
     "### section (F): tools/b304_hooks.py, DECLARED ON THIS FACE BEFORE THE ACT, its SOURCE and "
     "its backup defect."),
    ("relay tracked files deleted", 1, 1, "files", "### section (F): tools/git-hooks/pre-push."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (J)."),
    ("relay tracked files written outside tools, data and .githooks", 0, 0, "files", "none."),
    ("TECHNE files written", 1, 1, "files", "### section (F): one module, local."),
    ("SIDE-effects files written", 1, 1, "files",
     "### section (F): .githooks/pre-push, written by the installer, AND NOTHING ELSE."),
    ("SIDE-global-section files written", 2, 2, "files",
     "### section (F): CORRESPONDENCE.md at the closing, and .githooks/pre-push by the "
     "installer."),
    ("PLACE-papers files written", 2, 2, "files",
     "### section (F): OPEN_TRAILS.md appended, and .githooks/pre-push by the installer. ### NO "
     "CORPUS DOCUMENT IS WRITTEN INTO AND REGISTRY.md IS NOT EDITED."),
    ("new tracking documents created", 0, 0, "documents", "### section (J)."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "### section (F)/(J)."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists", "### section (J): restated OPEN by name."),
    ("citation-question movements", 0, 0, "movements",
     "### section (J): restated as awaiting the author and NOT MOVED."),
    ("clusters opened, ranked or prioritised", 0, 0, "clusters", "### section (J)."),
    ("amendments applied", 0, 0, "amendments", "### section (J): the three stay routed."),
    ("archive files touched, moved, renamed or removed", 0, 0, "files", "### section (F)/(J)."),
    ("pins written by this act", 0, 0, "pins", "### section (F)."),
    ("classes ruled", 0, 0, "classes", "### section (J)."),
    ("documents reclassified", 0, 0, "documents", "### section (J)."),
    ("class lines written", 0, 0, "lines", "### section (J)."),
    ("grades moved", 0, 0, "grades", "### section (J)."),
    ("standards edited", 0, 0, "files", "### section (J)."),
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
     "### section (A): every quoted line is read out of its own file at its own line number."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration`s own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]

def main(argv):
    print('=' * 100)
    print('b386_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b386_registration_2026-09-09.txt -- b386, THE GUARD MADE SINGLE-SOURCED",
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
