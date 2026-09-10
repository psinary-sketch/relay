# -*- coding: utf-8 -*-
"""b396_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND A FACE THE ORDER MADE WIDE:** ### one string,
### twenty-four lines, eight exclusions, zero deletions, zero bytes in the next leg's scope.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b396_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b396_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (F)/(J): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (F)/(J)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (F)."),
    ("`.lean` files touched", 0, 0, "files", "### section (F)."),
    ("builds run", 0, 0, "builds", "### section (F)."),
    ("repositories cloned", 0, 0, "repositories", "### section (F)."),
    ("kernel branches fetched, merged, pushed or created", 0, 0, "branches", "### section (F)."),
    ("corpus documents edited", 0, 0, "documents",
     "### section (F)/(J): ### **NO CORPUS DOCUMENT IS EDITED AT ALL.**"),
    ("prior acts` instruments repaired or edited", 0, 0, "instruments",
     "### section (F)/(G): ### **NAMING A BODY OF WORK IS NOT DOING IT.**"),
    ("prior acts` faces or banks edited", 0, 0, "files", "### section (F)."),
    ("statements proved", 0, 0, "statements", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),

    ("pre-lock gates the lock reads", 8, 8, "gates", "### section (A)."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(H)."),
    ("readings of the order declared in advance on this face", 8, 8, "readings",
     "### section (A): the premise discharged; grep is not the instrument; the funnel; three "
     "discarded filters; what makes a figure at risk; the disjoint sets; preserved blocks "
     "structurally identifiable; and the price inputs read."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS", 0, 0, "reads",
     "### section (A): `12` reads, `12` ANCHORED."),
    ("extract reads left ABSENT", 0, 0, "reads", "### section (A)."),

    # ---- ADDITION ONE, THE SWEEP`S OWN PREMISE ----------------------------------------------------
    ("forms of one narrow matcher the fixture carries", 3, 3, "forms",
     "### section (A)/(H) BAR 2: a raw-string regex, an escaped regex, and ### **A FORM WITH NO "
     "REGEX AT ALL.**"),
    ("forms the detector failed to find", 0, 0, "forms", "### section (A)/(H) BAR 2."),
    ("wide fixtures the detector fired on", 0, 0, "fixtures",
     "### section (A): without a negative control a fixture shows the detector FIRES, not that "
     "it DISCRIMINATES."),
    ("axes the figure filter is tested on", 2, 2, "axes",
     "### section (A): narrow+ordinary QUIET, and wide+absence QUIET."),
    ("deafnesses named in the instrument itself", 5, 5, "deafnesses",
     "### section (A): ### **STATED IN THE TOOL AND NOT ONLY IN THE BANK.**"),

    # ---- COMPONENT 1, THE SWEEP ------------------------------------------------------------------
    ("`tools/b*.py` instruments parsed", 856, 856, "instruments", "### section (A)."),
    ("instruments that failed to parse and were not said so", 0, 0, "instruments",
     "### section (B)."),
    ("instruments carrying at least one narrow test", 407, 407, "instruments", "### section (A)."),
    ("instruments carrying at least one at-risk figure", 64, 64, "instruments", "### section (A)."),
    ("at-risk figures", 82, 82, "figures",
     "### section (A)/(B): ### **THE PRODUCT IS A LIST, NOT A COUNT OF REGEXES.**"),
    ("filters tried and discarded before the lock", 3, 3, "filters",
     "### section (A)/(H) BAR 3: kept 374/407, 350/380 and 79/82."),
    ("filters discarded without their yield printed", 0, 0, "filters",
     "### section (A): ### **A TIGHTENING MADE IN SILENCE IS ONE NOBODY CAN AUDIT** (`b381`)."),
    ("at-risk entries with no instrument, line, bound name and report", 0, 0, "entries",
     "### section (H) BAR 4."),
    ("narrow instruments counted as at risk with no negative finding on them", 0, 0, "instruments",
     "### section (B): ### **NARROW IS NOT A DEFECT.**"),

    # ---- COMPONENT 2, THE RE-RUNS ----------------------------------------------------------------
    ("findings re-run with a widened predicate", 6, 6, "findings",
     "### section (A)/(C): the cheapest three AND the most exposed three."),
    ("re-runs reporting only one yield", 0, 0, "re-runs", "### section (C)/(H) BAR 5."),
    ("re-runs whose widening was stated after the run", 0, 0, "re-runs",
     "### section (C): ### **A RE-RUN TUNED TO ITS RESULT IS `b380`'S FORBIDDEN DIRECTION.**"),
    ("re-runs left without a CONFIRMED / MOVED / REFUTED verdict", 0, 0, "re-runs",
     "### section (C)."),
    ("sets of three the order`s two criteria produce", 2, 2, "sets",
     "### section (A)/(H) BAR 6: cheapest `b307 b318 b323`; most exposed `b392 b326 b332`."),
    ("members the two sets share", 0, 0, "members",
     "### section (A): ### **THEY ARE DISJOINT, AND THE ACT SAYS SO.**"),
    ("sets left unrun", 0, 0, "sets", "### section (A)/(H) BAR 6: ### **ALL SIX ARE RUN.**"),

    # ---- COMPONENT 3, THE PRICE ------------------------------------------------------------------
    ("keystones priced", 10, 10, "keystones", "### section (D): the ten `b395` showed reachable."),
    ("keystones read by this act", 0, 0, "keystones",
     "### section (D): ### **THEY ARE PRICED, NOT READ.**"),
    ("rates invented rather than read from the act that measured them", 0, 0, "rates",
     "### section (A)/(D): `b394`'s own component JSON."),
    ("floors promoted into estimates", 0, 0, "figures",
     "### section (D)/(H) BAR 8: ### **A PRICE BUILT ON A FLOOR IS A FLOOR.**"),
    ("ways the rate`s sample is unrepresentative, named", 1, 1, "ways",
     "### section (D): `b394` read ### *the reachable ones.*"),

    # ---- ADDITION THREE, THE PRESERVATION HAZARD -------------------------------------------------
    ("rules filed for the preservation hazard", 1, 1, "rules", "### section (E)."),
    ("owner instruments edited", 1, 1, "instruments",
     "### section (F): `anchor_from_file.py`, one added mode."),
    ("added modes that are on by default", 0, 0, "modes",
     "### section (E)/(H) BAR 7: ### **THE DEFAULT IS UNCHANGED.**"),
    ("existing callers whose behaviour moves", 0, 0, "callers",
     "### section (H) BAR 7: ### **AN OWNER INSTRUMENT WIDENED WITHOUT MOVING ONE READER.**"),
    ("halves of the rule, listed apart", 2, 2, "halves",
     "### section (E): the mechanized half and the judgement half."),
    ("judgement halves claimed as mechanized", 0, 0, "halves", "### section (E)/(G)."),
    ("TECHNE modules written", 1, 1, "modules",
     "### section (E)/(F): ### **LOCAL ONLY, NOT PUSHED.**"),
    ("TECHNE modules pushed", 0, 0, "modules", "### section (F)."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (H)."),
    ("bars with a stated floor", 8, 8, "bars", "### section (H): `b347`'s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (H)."),
    ("must-fail fixtures", 6, 6, "fixtures", "### section (H): BARS 2, 3, 4, 5 and 7."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (H), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "every diff arm measures against the PRE-ACT BLOB (`b352`)."),
    ("new `relay` tool files", 8, 8, "files", "### section (F): the cap counts FILES (`b382`)."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (F)."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (J)."),
    ("documents reclassified or placed in Tier KC", 0, 0, "documents", "### section (F)/(J)."),
    ("registry rows edited", 0, 0, "rows", "### section (F)/(J)."),
    ("the census edited", 0, 0, "files", "### section (F)/(J)."),
    ("standards edited", 0, 0, "files", "### section (F)/(J)."),
    ("correspondence tables written, extended or re-graded", 0, 0, "tables", "### section (J)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (F)/(J): rows are APPENDED."),
    ("grades moved", 0, 0, "grades", "### section (J)."),
    ("claims withdrawn", 0, 0, "claims", "### section (J)."),
    ("clusters reshaped", 0, 0, "clusters", "### section (F)/(J)."),
    ("map head notes touched", 0, 0, "notes", "### section (F)."),
    ("lists closed", 0, 0, "lists", "### section (J): the four stay OPEN."),
    ("faces promoted", 0, 0, "faces", "### section (J)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (J)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (J)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (J)."),
    ("posture-lock changes", 0, 0, "changes", "### section (J)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (J)."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (A)."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    import re
    return len(set(re.findall(r'\bG-[A-Z0-9]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b396_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    print('  ### ### **THE OPEN CLAUSE, MEASURED RATHER THAN TYPED:** ### ARMS %d' % measured['ARMS'])
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b396_registration_2026-09-10.txt -- b396, THE RECONCILIATION BATCHED"),
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
