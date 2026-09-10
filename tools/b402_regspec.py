# -*- coding: utf-8 -*-
"""b402_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND ONE VERDICT, ONE CORRECTION AND ONE REFUSAL:** ###
### an impossibility stated at a scope with the sentence naming what it does NOT show; the order's
### own phrase quoted and corrected against a verified source rather than improved in silence; and a
### claim the ferry permits only on the record's word, which the record does not give.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b402_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b402_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### section (Z): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)/(K) BAR 10."),
    ("instrument runs", 0, 0, "runs", "### section (Z)/(K) BAR 10: a fold computes nothing."),
    ("kernel builds run", 0, 0, "builds", "### section (Z)/(K) BAR 10."),
    ("objects recomputed", 0, 0, "objects", "### section (Z)/(K) BAR 10."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)/(K) BAR 10."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("rules struck or amended", 0, 0, "rules", "### section (Z)."),
    ("grades moved or conferred", 0, 0, "grades", "### section (K) BAR 6: a fold moves no grade."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("prior acts` faces, banks or instruments edited", 0, 0, "files",
     "### section (A) reading (3): the counter`s stale line is ROUTED, not repaired."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (Z)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (Z): a fold opens and closes nothing."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories",
     "### section (A): Leg 1`s three pushes are read back."),
    ("readings of the order declared in advance on this face", 5, 5, "readings",
     "### section (A): the fold due; the navigator`s count refuted; the counter`s stale line; "
     "the arc`s one statement; and the seat-defect table reaching the last two acts."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### (K) BAR 9."),

    # ---- THE SPAN AND THE THRESHOLD --------------------------------------------------------------
    ("acts in the span this fold covers", 17, 17, "acts",
     "### section (A) reading (1): b385 through b401, from the counter."),
    ("acts of the span the generator writes", 17, 17, "acts", "### (K) BAR 2."),
    ("folding acts included in their own fold", 0, 0, "acts", "### section (A) reading (1)."),
    ("spans typed by this seat rather than read from the counter", 0, 0, "spans",
     "### (K) BAR 2: the generator REFUSES if they disagree."),
    ("thresholds taken from the counter rather than from the ruling", 0, 0, "thresholds",
     "### (K) BAR 3: the counter`s own line on it is STALE."),
    ("navigator count claims printed beside the tool`s and scored", 1, 1, "claims",
     "### (K) BAR 14: sixteen against 17."),
    ("count claims quietly replaced by the right number", 0, 0, "claims", "### (K) BAR 14."),

    # ---- THE FOLD --------------------------------------------------------------------------------
    ("headlines the fold attributes to an act", 17, 17, "headlines", "### (K) BAR 1."),
    ("headlines located by the anchor tool in their own act`s bank", 17, 17, "headlines",
     "### (K) BAR 1: F-NOGRADE, copied as b348 ruled."),
    ("headlines taken from a later act`s summary of an act", 0, 0, "headlines", "### (K) BAR 5."),
    ("sections written when a headline failed to locate", 0, 0, "sections",
     "### (K) BAR 1: the section is not written AT ALL."),
    ("tables the fold section carries", 3, 3, "tables",
     "### section (B): corrections, defective bars, and the seats` own defects."),
    ("scope sentences beside the arc`s one statement", 1, 1, "sentences", "### section (B)."),
    ("acts of the span reached by the seat-defect table", 2, 2, "acts",
     "### (K) BAR 7: the LAST TWO at least, and not only the comfortable ones."),
    ("lines of FINDINGS.md edited", 0, 0, "lines", "### (K) BAR 4: APPENDED TO, NEVER EDITED."),
    ("content lost in any edited file", 0, 0, "lines", "### (K) BAR 4."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 14, 14, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (K): UNPRICED."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (K), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(b348, b373, b400)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(b397)."),
    ("arms reading a repository state without a declared reference", 0, 0, "arms",
     "### (K) BAR 4: b401`s own species -- naming the SIDE alone is half a declaration."),
    ("new `relay` tool files", 6, 5, "files", "### section (A)/(K) BAR 8: the cap is 6 and this leg declares 5."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (Z)."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("the census edited", 0, 0, "files", "### section (Z)."),
    ("standards edited", 0, 0, "files", "### section (Z)."),
    ("face rows of the faces ledger edited", 0, 0, "rows", "### section (Z)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (Z): rows are APPENDED."),
    ("claims withdrawn", 0, 0, "claims", "### section (Z)."),
    ("clusters reshaped", 0, 0, "clusters", "### section (Z)."),
    ("map head notes touched", 0, 0, "notes", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
    ("posture-lock changes", 0, 0, "changes", "### section (Z)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (A)."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]

def count_arms(text):
    return len(set(re.findall(r'\bG-[A-Z0-9]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b402_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
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
    print('  ### ### **THE OPEN CLAUSE, MEASURED RATHER THAN TYPED:** ### ARMS %d'
          % measured['ARMS'])
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b402_registration_2026-09-10.txt -- b402, "
                             "THE FOLD, IF DUE, AS ITS OWN ACT"),
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
