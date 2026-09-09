# -*- coding: utf-8 -*-
"""b378_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b378_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b378_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (J): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (J): read and counted, never edited."),
    ("`.lean` files touched", 0, 0, "files", "### section (J)."),
    ("terminals written", 0, 0, "terminals", "### section (J)."),
    ("statements proved", 0, 0, "statements", "### section (J)."),
    ("builds run", 0, 0, "builds", "### section (J)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),

    # ---- STEP ZERO: THE HOLE CLOSED IN THE TOOL ------------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): the ferry scan, both censuses, the pins, the registration gate, the term scan, the clause spec and the satisfiability audit."),
    ("pre-lock gates left unread by the lock", 0, 0, "gates", "### section (A)/(H) BAR 1."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): the registration gate, the term scan, the clause spec and the satisfiability audit. ### EACH MUST CARRY A sha256 STAMP EQUAL TO THIS FACE."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates",
     "### section (A)/(H) BAR 1: an absent claim is not a true one."),
    ("polarities the lock gate is fixtured in", 4, 4, "polarities",
     "### section (A): clean permits; a missing phrase, A STALE DIGEST, and a missing stamp each refuse FOR THAT GATE."),
    ("owner instruments edited to close the hole", 0, 0, "files",
     "### section (A)/(F): the shared gates are not modified; their RECORDS are stamped."),
    ("claims that the stamp proves the gate vouched for itself", 0, 0, "claims",
     "### section (A): it is the CALLER'S claim about what it fed the gate, and the face says so."),

    # ---- WHICH PART OF THE DRAFT IS TAKEN ------------------------------------------------------------
    ("draft components taken", 3, 3, "components",
     "### section (B): the names no kernel declares; the lock gate's hole; one NOT DETERMINABLE document by hand."),
    ("draft components taken without the reading being declared", 0, 0, "components",
     "### section (B): the fourth component is NOT taken and the reading is on this face in advance."),
    ("clusters opened", 0, 0, "clusters",
     "### section (B)/(J): FILED and NOT OPENED, as b377 left them."),

    # ---- ADDITION ONE: EVERY REF ---------------------------------------------------------------------
    ("identifiers carried forward for re-search", 37, 37, "identifiers",
     "### section (C): b377's 36 declared-nowhere plus 1 declared in more than one kernel. ### NAMED FROM b377'S BANKED JSON, NOT TYPED."),
    ("identifiers left unclassified by the re-search", 0, 0, "identifiers",
     "### section (C)/(H) BAR 4: every one receives exactly one classification."),
    ("identifiers given more than one classification", 0, 0, "identifiers", "### section (H) BAR 4."),
    ("kernels searched at main only", 0, 0, "kernels",
     "### section (C)/(H) BAR 2: every branch and every tag."),
    ("refs typed rather than enumerated live from the repository", 0, 0, "refs",
     "### section (C)/(H) BAR 2."),
    ("held branches named by a document and not searched", 0, 0, "branches",
     "### section (C): THE_RESIDUE_OF_RH names word-pairing-interface in its own text."),
    ("earlier figures restated as anything but an upper bound at one ref", 0, 0, "figures",
     "### section (C): the order requires it said plainly."),

    # ---- ADDITION TWO: THE TWO CONVENTIONS -----------------------------------------------------------
    ("conventions the matcher accepts", 2, 2, "conventions",
     "### section (D): bare, as the older documents write it; dotted, as the newer ones do."),
    ("matchers trusted without fixtures in both polarities", 0, 0, "matchers",
     "### section (D)/(H) BAR 3."),
    ("matchers trusted without a discrimination arm", 0, 0, "matchers",
     "### section (D)/(H) BAR 3: a matcher that accepts everything is not a matcher."),
    ("documents rewritten into the other convention", 0, 0, "documents",
     "### section (D): both dialects are correct in their own terms and NONE IS REWRITTEN."),
    ("costs of the earlier narrowness left unstated", 0, 0, "costs",
     "### section (D): it selected the six, and where else it may have cost the same is stated."),

    # ---- ADDITION THREE: THE ARCHIVES ----------------------------------------------------------------
    ("archive files confirmed on a filename alone", 0, 0, "files",
     "### section (E)/(H) BAR 6: the export is FLAT and derives names from paths. ### A NAME MATCH IS NOT EVIDENCE OF IDENTITY."),
    ("archive files reported without a verdict", 0, 0, "files",
     "### section (E): CONFIRMED PRESENT with path and digest, or NOT CONFIRMED with what is missing."),
    ("archive files removed, moved or renamed", 0, 0, "files",
     "### section (E)/(F)/(H) BAR 5: the removal is the author's."),
    ("wider archive counts presented as the ordered report", 0, 0, "counts",
     "### section (E): the ordered population is what the mirror carries; the rest is CONTEXT and labelled so."),

    # ---- THE HAND READ -------------------------------------------------------------------------------
    ("not-determinable documents read by hand", 1, 1, "documents",
     "### section (B): the draft says do ONE of the two."),
    ("declarations moved by the hand read", 0, 0, "declarations",
     "### the outcome is a mark, not a class, and the draft says do not move the declaration either way."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 7, 7, "bars",
     "### section (H): stamped-gate, every-ref, two-dialect, correction, no-rewrite, archive-evidence, no-ruling."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 11, 11, "files",
     "gate_hash (SHARED), the lock gate, the regspec, the extract, the reg gate, the "
     "terminal re-search, the archive confirmation, the hand read, the desk sweeper, the "
     "bank writer and this act's gate suite."),
    ("shared utilities created", 1, 1, "files",
     "### tools/gate_hash.py -- it stamps a gate record with the sha256 of what the gate read."),
    ("owner instrument files edited", 0, 0, "files", "this act licenses none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (J)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files", "### CORRESPONDENCE.md at the closing."),
    ("PLACE-papers files written", 1, 1, "files",
     "### section (F): OPEN_TRAILS.md, appended. ### NO CORPUS DOCUMENT IS WRITTEN INTO BY THIS ACT AT ALL."),
    ("new tracking documents created", 0, 0, "documents", "### section (J)."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists", "### section (J): restated OPEN by name."),
    ("kernels opened without every ref searched being printed", 0, 0, "kernels",
     "### section (C)/(H) BAR 2: the refs are enumerated live and printed."),
    ("pins written by this act", 0, 0, "pins",
     "### section (F): no corpus document is written into, so no row and no pin is written."),
    ("documents selected by their path rather than by their own declaration", 0, 0, "documents",
     "### section (C): the population comes from b376's banked scores, which read content."),
    ("classes ruled", 0, 0, "classes", "### section (J)."),
    ("documents reclassified", 0, 0, "documents", "### section (J)."),
    ("class lines written", 0, 0, "lines", "### section (C)/(J): no declaration is moved."),
    ("grades moved", 0, 0, "grades", "### section (J)."),
    ("equivalences compiled", 0, 0, "compilations", "### section (J)."),
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
     "### section (A-PRE): Component 1's finding was visible before the lock and is declared there."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b378_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b378_registration_2026-09-08.txt -- b378, THE REFS WIDENED",
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
