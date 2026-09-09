# -*- coding: utf-8 -*-
"""b377_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b377_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b377_satisfiable.json')

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

    # ---- STEP ZERO ----------------------------------------------------------------------------------
    ("pre-lock gates the lock reads", 7, 7, "gates",
     "### section (A): the ferry scan, both censuses, the pins, the registration gate, the term scan and the satisfiability audit, read by b376's tool run as b377."),
    ("pre-lock gates left unread by the lock", 0, 0, "gates", "### section (A)/(H) BAR 1."),
    ("lock-gate tools rebuilt rather than inherited", 0, 0, "files",
     "### section (A): a cure that has to be rebuilt every act is not a cure."),
    ("prior locked faces edited", 0, 0, "files",
     "### section (A)/(J): b375's defective first face included."),
    ("claims that the lock gate proves each gate was run against the right bytes", 0, 0, "claims",
     "### section (A): it checks that each record CARRIES ITS PASS PHRASE, and says so."),

    # ---- COMPONENT 1: THE ROLE CLAUSE ---------------------------------------------------------------
    ("author role clauses banked verbatim with their location", 1, 1, "clauses",
     "### section (D): the author's own words, quoted and not paraphrased."),
    ("rulings drawn from the role clause", 0, 0, "rulings",
     "### section (D): a clause that bears on one axis does not rule a question that spans two."),
    ("axes the role clause is claimed to settle", 0, 0, "axes",
     "### section (D): it speaks to the role axis and not to the apparatus axis, and this is stated not inferred."),

    # ---- COMPONENT 2: THE FIVE OPTIONS --------------------------------------------------------------
    ("options reproduced whole from b376", 5, 5, "options",
     "### section (D): the author rules from the text and not from a summary."),
    ("options summarised rather than quoted", 0, 0, "options",
     "### section (D): the order says QUOTED WHOLE."),
    ("options given a bearing line that recommends", 0, 0, "options",
     "### section (D)/(H) BAR 8: whether and how the clause bears, without recommending."),

    # ---- COMPONENT 3: THE BRANCH --------------------------------------------------------------------
    ("documents in the branch population", 6, 6, "documents",
     "### section (C)/(E): those declaring TIER K and scoring no traversable row. ### THE NOT-DETERMINABLE ONES ARE NOT AMONG THEM."),
    ("documents taking neither arm of the branch", 0, 0, "documents", "### section (H) BAR 5."),
    ("documents taking both arms of the branch", 0, 0, "documents", "### section (H) BAR 5."),
    ("terminals written into an appended table without being located and checked at a kernel",
     0, 0, "terminals",
     "### section (E)/(H) BAR 3: a row a stranger cannot traverse would be worse than the absence it replaced."),
    ("pins written that were copied from another document or from a row", 0, 0, "pins",
     "### section (E)/(H) BAR 4: (R9)'s forward half. ### THE PIN IS THIS ACT'S OWN READING OF THAT KERNEL'S HEAD."),
    ("appended tables in documents where a named terminal could not be located", 0, 0, "tables",
     "### section (E): if a single terminal cannot be located, THE WHOLE DOCUMENT TAKES ARM 2."),
    ("existing bytes changed in any document written into", 0, 0, "bytes",
     "### section (F)/(H) BAR 2: the committed blob stays a TRUE PREFIX."),
    ("declarations moved, demoted or annotated as wrong", 0, 0, "declarations",
     "### section (C): a document says what it says."),
    ("axiom profiles computed rather than read from the kernel's own recorded output", 0, 0, "profiles",
     "### section (F)."),

    # ---- THE AMENDMENT ------------------------------------------------------------------------------
    ("not-determinable documents reported and left", 2, 2, "documents",
     "### section (C): NOT DETERMINABLE IS NOT ABSENT."),
    ("not-determinable documents repaired", 0, 0, "documents", "### section (C)/(H) BAR 6."),
    ("not-determinable documents routed as lacking", 0, 0, "documents", "### section (C)/(H) BAR 6."),
    ("not-determinable documents counted among the six", 0, 0, "documents", "### section (C)/(H) BAR 6."),
    ("wider-question measurements taken by this act", 0, 0, "measurements",
     "### section (C)/(G): the amendment names the question and forbids the measurement."),
    ("banked column-(d) figures restated as anything but a floor", 0, 0, "figures",
     "### section (C): it was taken against one layer and is a FLOOR against the wider question."),

    # ---- COMPONENT 4: THE TWO FILINGS ---------------------------------------------------------------
    ("filings made", 2, 2, "filings",
     "### the census's definition-versus-operation drift, and the clusters with registry rows and no keystone."),
    ("filings opened as work", 0, 0, "filings",
     "### the order says FILED and NOT OPENED."),
    ("census documents repaired by this act", 0, 0, "documents",
     "### repairing the census belongs to the ruling."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 8, 8, "bars",
     "### section (H): lock-gate, append-only, terminal, pin, branch, not-determinable, quotation, no-ruling."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 8, 8, "files",
     "the regspec, the extract, the reg gate, the branch executor, the evidence assembler, the desk "
     "sweeper, the bank writer and this act's gate suite. ### THE LOCK GATE IS b376'S, RUN AS b377, "
     "AND IS NOT REBUILT."),
    ("shared utilities created", 0, 0, "files", "none."),
    ("owner instrument files edited", 0, 0, "files", "this act licenses none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (J)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files", "### CORRESPONDENCE.md at the closing."),
    ("PLACE-papers files written outside OPEN_TRAILS and the arm-1 documents", 0, 0, "files",
     "### section (F): the count of arm-1 documents is NOT PREDICTED -- the branch decides it -- so the clause forbids the wrong file rather than predicting a number."),
    ("new tracking documents created", 0, 0, "documents", "### section (J)."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists", "### section (J): restated OPEN by name."),
    ("kernels opened without being named in the bank", 0, 0, "kernels",
     "### section (E): this act DOES open kernels, which b376 did not. ### How many is not predicted; that each is named is required."),
    ("pins written that were not read from a kernel head by this act", 0, 0, "pins",
     "### section (E)/(H) BAR 4: (R9)'s forward half. ### Every pin written is recorded in this act's bank."),
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
    print('b377_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b377_registration_2026-09-08.txt -- b377, THE UNBLOCKED OBLIGATION",
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
