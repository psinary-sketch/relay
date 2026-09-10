# -*- coding: utf-8 -*-
"""b401_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b401_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b401_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS OF THE FERRY ------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### section (Z): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)/(K) BAR 11."),
    ("instrument runs", 0, 0, "runs", "### section (Z)/(K) BAR 11."),
    ("kernel builds run", 0, 0, "builds", "### section (A)/(K) BAR 6: the lane is PARKED."),
    ("objects recomputed", 0, 0, "objects", "### section (K) BAR 11: this leg computes nothing."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)/(K) BAR 11."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("rules struck or amended", 0, 0, "rules", "### section (Z)."),
    ("grades moved or conferred", 0, 0, "grades", "### section (F)/(K) BAR 7."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (F): the row is EXTENDED and STAYS OWED."),
    ("prior acts` faces, banks or instruments edited", 0, 0, "files",
     "### section (Z): the SIDE-window README stale count is ROUTED, not repaired."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (Z)."),

    # ---- STEP ZERO AND THE WRITE LIST ------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads",
     "### section (A)/(K) BAR 2: 14 reads, 14 ANCHORED."),
    ("readings of the order declared in advance on this face", 5, 5, "readings",
     "### section (A): the search verdict; the vacuous uniformity; the different object; the "
     "stale README count; and the shared index."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### (K) BAR 10."),

    # ---- THE SOURCES -----------------------------------------------------------------------------
    ("pinned sources this leg quotes", 2, 2, "sources", "### section (B)."),
    ("pinned sources VERIFIED against the corpus`s banked digest", 2, 2, "sources",
     "### section (B)/(K) BAR 1."),
    ("source sentences read before their artefact was verified", 0, 0, "sentences",
     "### section (B)/(K) BAR 1."),
    ("source fragments located by page index", 12, 12, "fragments", "### section (B)."),
    ("source statements imported that the record already owns", 0, 0, "statements",
     "### section (C)/(K) BAR 5: b358 and b361 are CITED, not re-imported."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("verdicts on the absent element", 1, 1, "verdicts",
     "### section (C): one of the draft`s three, unsoftened."),
    ("matcher shapes tried over the corpus", 5, 5, "shapes",
     "### section (C)/(K) BAR 3: a limit found by one matcher is a property of that matcher."),
    ("matchers whose yield is left unprinted", 0, 0, "matchers", "### (K) BAR 3."),
    ("reasons the located statement is not the missing element", 3, 3, "reasons",
     "### section (C): wrong family, wrong comparison quantity, wrong kind of hypothesis."),
    ("hypotheses decided by this leg that a prior act left inherited", 0, 0, "hypotheses",
     "### section (C): H-CUSP stays b358`s and b361`s."),

    # ---- ADDITION ONE ----------------------------------------------------------------------------
    ("uniformity verdicts issued", 1, 1, "verdicts", "### section (D)."),
    ("uniformity verdicts stated without the word that scopes them", 0, 0, "verdicts",
     "### section (D)/(K) BAR 4: VACUOUSLY stands in the same sentence as UNIFORM."),
    ("prime-by-prime openings priced", 0, 0, "pricings",
     "### section (D): the branch is entered and its consequence is NOT drawn."),
    ("indices the located correction term carries", 1, 1, "indices",
     "### section (D): the Li index n, and no prime index at all."),

    # ---- ADDITION TWO ----------------------------------------------------------------------------
    ("kernels read whole rather than by name", 1, 1, "kernels", "### section (E)."),
    ("axiom profiles read from a run", 0, 0, "profiles",
     "### section (A)/(K) BAR 6: READ FROM A PRINTED PROFILE, and the act says so."),
    ("stale counts found on another repository`s face", 1, 1, "counts",
     "### section (A) reading (4)."),
    ("stale counts repaired by this leg", 0, 0, "counts", "### section (Z): ROUTED."),
    ("objects the one-prime window is decided to bound", 1, 1, "objects",
     "### section (E): a COUNT, at no support at all."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("instances added to the uniformity row", 1, 1, "instances", "### section (F)."),
    ("instances added without naming what they share with an existing one", 0, 0, "instances",
     "### section (F)/(K) BAR 15."),
    ("equivalences typed between any two instances", 0, 0, "equivalences",
     "### section (F): the row`s refusal is restated VERBATIM."),
    ("ledger cells rewritten rather than appended to", 0, 0, "cells", "### (K) BAR 8."),
    ("content lost in any edited file", 0, 0, "lines", "### (K) BAR 8."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 15, 15, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars",
     "### section (K): UNPRICED -- this leg computes no object."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (K), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(b348, b373, b400)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(b397)."),
    ("arms measuring a bar this face did not set", 0, 0, "arms", "(b390)."),
    ("arms reading a repository state without a declared side", 0, 0, "arms", "(b352)."),
    ("new `relay` tool files", 6, 6, "files", "### section (A)/(K) BAR 9."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (Z)."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (Z)."),
    ("documents reclassified or placed in Tier KC", 0, 0, "documents", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("the census edited", 0, 0, "files", "### section (Z)."),
    ("standards edited", 0, 0, "files", "### section (Z)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (Z): rows are APPENDED."),
    ("claims withdrawn", 0, 0, "claims", "### section (Z)."),
    ("clusters reshaped", 0, 0, "clusters", "### section (Z)."),
    ("map head notes touched", 0, 0, "notes", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
    ("coordinates closed", 0, 0, "coordinates", "### section (Z)."),
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
    print('b401_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b401_registration_2026-09-10.txt -- b401, "
                             "THE ABSENT ELEMENT SEARCHED, AND THE FOURTH SITE"),
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
