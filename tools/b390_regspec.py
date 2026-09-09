# -*- coding: utf-8 -*-
"""b390_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any write of this act.
### ### **AND THIS ACT'S FACE IS WIDE, SO THE CLAUSES THAT MATTER MOST ARE THE ONES THAT BOUND THE
### ### WIDTH:** ### one repair, seven routed, zero grades moved, zero classes ruled, zero claims
### withdrawn, zero lines deleted.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b390_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b390_satisfiable.json')
PP = r'D:\MY-DOwnloads\PLACE-papers'
AMC = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### section (K): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (K)."),
    ("`.lean` files touched", 0, 0, "files", "### section (G)/(K)."),
    ("builds run", 0, 0, "builds",
     "### section (G)/(H): ### **`ls-remote` SAYS A REF EXISTS; IT DOES NOT SAY THE KERNEL "
     "COMPILES.**"),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (G)/(K)."),
    ("kernel branches merged, pushed or created", 0, 0, "branches", "### section (G)."),
    ("terminals written", 0, 0, "terminals", "### section (K)."),
    ("statements proved", 0, 0, "statements", "### section (K)."),
    ("new mathematics", 0, 0, "statements", "### section (K)."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (G)/(K)."),

    # ---- STEP ZERO AND THE DECLARED READINGS -----------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378`s gate run as b390, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(I)."),
    ("readings of the order declared in advance on this face", 5, 5, "readings",
     "### section (A): the census names two and the order asks for one; the subject is the "
     "oldest of the sixteen and already reconciled on 2026-08-12; (F1) is at risk of refutation; "
     "one of eight routed items is repairable; and the document`s own repair precedent is set "
     "twice in its own headings."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left without an anchor", 0, 0, "reads",
     "### section (A): 42 reads, 0 without an anchor, 23 anchors differing from the typed hint."),

    # ---- COMPONENT 0: THE ROUTED CORRECTIONS -----------------------------------------------------
    ("routed items swept and classified", 8, 8, "items", "### section (B)."),
    ("routed items repaired by this act", 1, 1, "items",
     "### section (B)/(I) BAR 3: ### **THE MAP`S CROSS-DOMAIN FEDERATION COLUMN, AND NOTHING "
     "ELSE.**"),
    ("routed items named with the reason they are not repaired", 7, 7, "items",
     "### section (B)/(I) BAR 3."),
    ("rulings treated as repairs", 0, 0, "items",
     "### section (A)/(B): ### **A WIDE FACE DOES NOT MAKE A RULING REPAIRABLE**, however small "
     "the edit would be."),
    ("live kernel checks recalled rather than re-run", 0, 0, "checks",
     "### section (B): ### **A KERNEL RECALLED IS NOT A KERNEL READ**, and the repair rests on "
     "the read."),
    ("names removed from the map without a trace left in the row", 0, 0, "names",
     "### section (B)/(I) BAR 4: `(R4)` -- ### **PRESERVE BY QUOTATION, REPAIR BY EDIT.**"),

    # ---- COMPONENT 1: THE SUBJECT ----------------------------------------------------------------
    ("keystones the census names as the two the era moved most", 2, 2, "keystones",
     "### section (A)/(C)."),
    ("keystones this act reads whole", 1, 1, "keystones", "### section (C): the order asks one."),
    ("subjects chosen by the seat`s preference", 0, 0, "choices",
     "### section (A)/(C)/(I) BAR 2: the rule is stated BEFORE the subject is named."),
    ("candidates measured before the choice", 2, 2, "candidates", "### section (C)/(I) BAR 2."),
    ("correspondence tables the subject carries", 2, 2, "tables",
     "### section (C): the original of 2026-07-12 and the standard`s of 2026-08-12."),
    ("correspondence tables merged or summed into one figure", 0, 0, "tables",
     "### section (C): ### **THEY WERE WRITTEN TO TWO DIFFERENT STANDARDS AND A COUNT THAT SUMS "
     "THEM DESCRIBES NEITHER.**"),
    ("grades translated out of the document`s own vocabulary", 0, 0, "grades",
     "### section (C)/(I) BAR 7."),

    # ---- COMPONENT 2: WHAT BEARS ON IT -----------------------------------------------------------
    ("anchors in the population", 11, 11, "anchors", "### section (D): all 11 resolving."),
    ("anchors opened and read at their own line", 11, 11, "anchors", "### section (D)."),
    ("buckets reported", 3, 3, "buckets",
     "### section (D)/(I) BAR 6: ALREADY SAYS IT / SUPERSEDES SOMETHING IT SAYS / DOES NOT "
     "CARRY IT."),
    ("buckets suppressed because they were empty", 0, 0, "buckets",
     "### section (D)/(I) BAR 6: ### **AN EMPTY MIDDLE BUCKET IS THE RESULT THAT REFUTES (F1)**, "
     "and it is reported as plainly as a full one."),
    ("bucket placements decided by a substring hit alone", 0, 0, "placements",
     "### section (D): ### **A MENTION IS NOT A CARRIAGE** -- the mechanical pass says where to "
     "look and the bucketing is read by hand."),
    ("bucketed items carrying a quotation from only one side", 0, 0, "items",
     "### section (D): the record`s line AND the keystone`s line, each at its own line number. "
     "### **A ONE-SIDED QUOTATION IS A SUMMARY OF THE OTHER SIDE**, which the order forbids by "
     "name. ### Stated as a zero so it is checkable rather than as a total this act cannot "
     "know before the component runs."),

    # ---- COMPONENT 3: THE REPAIR -----------------------------------------------------------------
    ("lines deleted from the keystone", 0, 0, "lines",
     "### section (E)/(I) BAR 4: the document`s own precedent is ### **APPEND AND ANNOTATE; DO "
     "NOT REWRITE.**"),
    ("sections of the keystone rewritten", 0, 0, "sections",
     "### section (E): ### **NOTHING IN §§I–IV IS REWRITTEN**, which is the document`s own "
     "closing sentence about itself."),
    ("grades moved", 0, 0, "grades", "### section (E)/(G)/(K): each is a ruling."),
    ("classes changed", 0, 0, "classes", "### section (E)/(G)/(K): each is a ruling."),
    ("claims withdrawn", 0, 0, "claims", "### section (E)/(G)/(K): each is a ruling."),
    ("grade words minted by this seat", 0, 0, "words",
     "### section (E)/(I) BAR 7: every grade written is a word the front door already uses."),
    ("repairs made and repairs routed counted together", 0, 0, "counts",
     "### section (E): they are counted ### **SEPARATELY.**"),

    # ---- COMPONENT 4: THE PRICE ------------------------------------------------------------------
    ("samples the price is extrapolated from", 1, 1, "samples",
     "### section (F)/(I) BAR 8: ### **ONE SAMPLE IS ONE SAMPLE** ### and the extrapolation says "
     "so."),
    ("ways this sample is unrepresentative, named", 2, 2, "ways",
     "### section (F)/(I) BAR 8: it was already reconciled once, and its pins all resolve."),
    ("figures estimated rather than measured from a recorded clock", 0, 0, "figures",
     "### section (F)."),
    ("schedules proposed", 0, 0, "schedules",
     "### section (F): ### **A PRICE, NOT A PLAN**, and the next keystone is the author`s."),

    # ---- THE CLOSING -----------------------------------------------------------------------------
    ("rulings restated as awaiting the author", 3, 3, "rulings",
     "### section (K): the citation question, the five clusters` reshaping, the deposit rule."),
    ("clusters named with what changed in each", 5, 5, "clusters",
     "### section (K): from b388`s own record -- 3 GREW, 2 NEW."),
    ("rulings answered by this act", 0, 0, "rulings", "### section (K)."),
    ("lists closed", 0, 0, "lists", "### section (K): the four stay OPEN."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (I)."),
    ("bars with a stated floor", 8, 8, "bars",
     "### section (I): `b347`'s rule -- ### **A BAR WITHOUT A FLOOR IS NOT A BAR.**"),
    ("numerical bars on a computed quantity", 0, 0, "bars",
     "### section (I): ### **THIS ACT COMPUTES NOTHING ABOUT THE OBJECT**, and says UNPRICED "
     "rather than leaving it blank."),
    ("must-fail fixtures", 4, 4, "fixtures", "### section (I): BARS 2, 3, 4 and 6."),
    ("gate arms declared", "ARMS", "ARMS", "arms",
     "### section (I): named, and each written by content. ### COUNTED OFF THIS FACE`S OWN TEXT "
     "BY THIS FILE -- and ### **THE WILDCARD MENTION `G-NO*` IS NOT AN ARM** (`b348`'s "
     "use-and-mention species)."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms",
     "### section (I): stripped code or tool output only (`b348`, `b373`) -- ### **BUT A POSITIVE "
     "ARM READS THE CODE ITSELF** (`b386`)."),
    ("arms written by address rather than content", 0, 0, "arms",
     "RULING (R2). ### And ### **A LINE NUMBER IS AN ADDRESS** -- `b389`'s catch, inherited."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "### section (I): `G-PRESERVED` and `G-SECTIONS` diff against the PRE-ACT BLOB and never "
     "within the run (`b352`, `b388`, `b389`)."),
    ("new `relay` tool files", 6, 6, "files",
     "### section (G): the cap counts FILES (`b382`), and this act is at it exactly."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("untracked run records of earlier acts committed", 0, 0, "files", "### section (G)."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "### section (G): RULING (R16)."),

    # ---- THE STANDING NOTHINGS OF THE PROGRAMME --------------------------------------------------
    ("documents reclassified", 0, 0, "documents", "### section (K)."),
    ("registry rows edited", 0, 0, "rows", "### section (G)/(K)."),
    ("standards edited", 0, 0, "files", "### section (K)."),
    ("amendments applied", 0, 0, "amendments", "### section (K): b383`s three stay routed."),
    ("correspondence rows edited", 0, 0, "rows", "### section (G)/(K): rows are APPENDED."),
    ("clusters added, split, merged or renamed in either map", 0, 0, "clusters",
     "### section (G)/(K)."),
    ("map head notes touched", 0, 0, "notes", "### section (G): `(R18)`'s notes stand."),
    ("other corpus documents written into", 0, 0, "documents",
     "### section (G): the census, the keystone not taken, FINDINGS, CASCADE_ANCHORS_CORRECTED, "
     "EXCLUSION_ENGINE, REGISTRY, README, THE_LOAD_BEARING_MAP and INTERFACE_CONSERVATION are "
     "### **READ AND NOT TOUCHED.**"),
    ("faces promoted", 0, 0, "faces", "### section (K)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (K)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (K)."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (K): ### **NO CLAIM IN EITHER DIRECTION.**"),
    ("posture-lock changes", 0, 0, "changes", "### section (K)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (K): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A)/(B): every quoted line read at its own line number; every ref read live."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration`s own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    """### **THE NAMED ARMS ON THE FACE.** ### `G-NO*` IS A WILDCARD MENTION AND IS NOT AN ARM."""
    import re
    return len(set(re.findall(r'\bG-[A-Z0-9]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b390_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    measured = dict(ARMS=count_arms(text))
    print()
    print('  ### ### **THE OPEN CLAUSES, MEASURED RATHER THAN TYPED:**')
    for k in sorted(measured):
        print('      %-8s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b390_registration_2026-09-09.txt -- b390, THE FIRST "
                             "PROOFREADING PASS"),
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
