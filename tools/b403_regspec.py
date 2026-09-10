# -*- coding: utf-8 -*-
"""b403_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b403_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b403_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### section (Z): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)/(K) BAR 11."),
    ("instrument runs", 0, 0, "runs", "### section (Z)/(K) BAR 11."),
    ("kernel builds run", 0, 0, "builds", "### section (K) BAR 11: the lane is PARKED."),
    ("objects recomputed", 0, 0, "objects", "### section (Z)/(K) BAR 11."),
    ("`.lean` files touched", 0, 0, "files",
     "### (K) BAR 11: SIDE-window`s source is READ and its .lean files are not touched."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("`.git/hooks/pre-push` copies installed", 0, 0, "files",
     "### (K) BAR 15: the installer WRITES when run and the audit lane is PARKED."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("rules struck or amended", 0, 0, "rules", "### section (Z)."),
    ("grades moved or conferred", 0, 0, "grades", "### section (Z)."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces",
     "### section (C): b321`s face is NOT edited; the item stays ROUTED."),
    ("prior acts` banks edited", 0, 0, "files",
     "### (K) BAR 7: b401`s bank is not edited; both readings are printed."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (Z)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (Z)."),
    ("instances added to any ledger row", 0, 0, "instances", "### (K) BAR 8."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads",
     "### section (A): 12 reads, 12 ANCHORED."),
    ("readings of the order declared in advance on this face", 7, 7, "readings",
     "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### (K) BAR 10."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("sites in the counter carrying the stale sentence", 3, 3, "sites", "### section (B)."),
    ("prior instruments of this seat edited", 1, 1, "instruments",
     "### section (B): tools/b363_span.py, and it is this seat`s own."),
    ("prior instruments of another seat edited", 0, 0, "instruments", "### section (C)."),
    ("originals replaced without being preserved in the file", 0, 0, "originals",
     "### section (B)/(K) BAR 2."),
    ("fold-derived fields compared against a banked run", 7, 7, "fields",
     "### (K) BAR 5: folds, spans, shortest, longest, middle, last_fold, span_starts_at."),
    ("fold-derived fields that moved", 0, 0, "fields",
     "### (K) BAR 5: a move would ROUTE the repair and revert it."),
    ("runs of the counter banked", 2, 2, "runs", "### (K) BAR 6: before and after."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("rules invoked by the Addition and located in the record", 1, 1, "rules",
     "### section (C)/(K) BAR 1: b371`s precedent, applied at b372."),
    ("rules paraphrased from the ferry rather than quoted from their act", 0, 0, "rules",
     "### (K) BAR 1."),
    ("prior repairs the Addition names", 2, 2, "repairs", "### section (A) reading (3)."),
    ("prior repairs the Addition names correctly", 1, 1, "repairs",
     "### section (A) reading (3): both are on SIDE-global-section; the second is the "
     "construction kernel`s README and not the exclusion kernel`s."),
    ("files of another owner repaired by this act", 1, 1, "files",
     "### section (C): SIDE-window`s README."),
    ("files of another owner routed rather than repaired", 1, 1, "files",
     "### section (C): b321`s locked face."),
    ("figures removed rather than restated", 1, 1, "figures", "### (K) BAR 3."),
    ("figures restated with a ref", 0, 0, "figures",
     "### section (A) reading (5): the carve-out does not reach a tree that ships no profile."),
    ("originals banked verbatim before their edit", 1, 1, "originals", "### (K) BAR 2."),
    ("claims strengthened or weakened by the edit", 0, 0, "claims", "### (K) BAR 4."),
    ("claims rewritten rather than numbers", 0, 0, "claims",
     "### section (A) reading (5): removal leaves the claim exactly as strong as it was."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("write-list residues printed", 1, 1, "residues",
     "### section (D): printed whether empty or not."),
    ("species minted by this act", 0, 0, "species",
     "### section (D): the order forbids minting until a fourth act shows the same gap twice."),
    ("acts with a clean KINDS residue before this one", 2, 2, "acts", "### section (D)."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 15, 15, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (K): UNPRICED."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (K), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(b348, b373, b400)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(b397)."),
    ("arms reading a repository state without a named reference", 0, 0, "arms",
     "### (K) BAR 2: b401`s species."),
    ("new `relay` tool files", 6, 6, "files", "### section (A)/(K) BAR 9."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
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
    print('b403_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b403_registration_2026-09-10.txt -- b403, "
                             "THE THREE ROUTED ITEMS, DISCHARGED OR RULED"),
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
