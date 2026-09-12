# -*- coding: utf-8 -*-
"""b439_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b439_registration_2026-09-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b439_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### section (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### section (Z).'),
    ('platform calls of any kind', 0, 0, 'calls', '### section (Z): the ls-remote reads are the pins`, the pushes the ritual`s.'),
    ('kernel .lean files touched', 0, 0, 'files', '### section (Z).'),
    ('kernel builds', 0, 0, 'builds', '### section (Z).'),
    ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### section (Z).'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened', 0, 0, 'routes', '### section (Z): Component 4 is PRICED and NOT OPENED.'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('candidate zeros, seeds, families or arrangements constructed', 0, 0, 'candidates', '### section (Z) and (K) BAR 9.'),
    ('claims about RH, h2, zeta or any zero', 0, 0, 'claims', '### section (Z).'),
    ('objects compiled for the window kernel', 0, 0, 'objects', '### (K) BAR 9: the three facts are NAMED and not built.'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z): b438`s least of all.'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### section (Z).'),
    ('register rows or ledger rows edited', 0, 0, 'rows', '### section (Z).'),
    ('cells of FACES_LEDGER.md written', 0, 0, 'cells', '### section (Z): frozen at six.'),
    ('seventh sites entered', 0, 0, 'sites', '### section (Z).'),
    ('bridges typed between any two of the six sites', 0, 0, 'bridges', '### section (Z).'),
    ('sites of the witness arc attempted', 0, 0, 'sites', '### section (Z): checkpointed after (iv).'),
    ('lane verdicts changed by the seat', 0, 0, 'verdicts', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('tuples or kernel figures moved', 0, 0, 'values', '### section (Z).'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 11.'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### section (J), (R26).'),
    ('scores averaged to one word where their clauses differ', 0, 0, 'scores', '### section (J), (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### (R28).'),
    ('counts or values the seat predicts on this face', 0, 0, 'predictions', '### section (J): C10; the shape in reading (1) is a derivation and is scored like any prediction.'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),

    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('readings of the order declared in advance on this face', 6, 6, 'readings', '### section (A): (0) to (5).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A): 0 over 6 reads.'),
    ('measurements taken before the lock and not declared on this face', 0, 0, 'measurements', '### section (A): the coefficient read is declared.'),

    ('author rulings ratified by this paste', 0, 0, 'rulings', '### section (A): none; (R50) was ratified at b438`s close.'),
    ('addendum slots declared in the write list', 1, 1, 'slots', '### (W) and (R50): data/b439_addendum.txt, present whether used or not.'),
    ('addendum slots carrying anything but a verbatim quotation', 0, 0, 'slots', '### (K) BAR 10.'),
    ('lanes opened', 0, 0, 'lanes', '### section (Z): both remain PARKED.'),
    ('disproof lanes opened', 0, 0, 'lanes', '### section (Z): its trigger fired at (R48) and its disposition waits on the author.'),
    ('new instruments built', 0, 0, 'instruments', '### (K) BAR 9.'),
    ('instrument files edited', 0, 0, 'files', '### (K) BAR 9.'),
    ('new families defined', 0, 0, 'families', '### (K) BAR 9.'),

    ('integrands quoted from the construction`s own source', 2, 2, 'integrands', '### reading (1): the first moment and the second.'),
    ('radii at which the coefficients are printed', 6, 6, 'radii', '### reading (1).'),
    ('radii at which the profile`s own zero is located', 6, 3, 'radii', '### reading (1): AT LEAST THREE, and the number is measured.'),
    ('derivations offered in place of a measurement', 0, 0, 'derivations', '### (K) BAR 1.'),
    ('faces whose declared shape is exempt from scoring', 0, 0, 'faces', '### (K) BAR 2.'),

    ('prime powers whose weight is printed', 10, 10, 'values', '### reading (2): every one the instrument admits below sixteen.'),
    ('b438 sentences quoted before being corrected', 1, 1, 'quotations', '### (K) BAR 3.'),
    ('b438 bank files edited to make the correction', 0, 0, 'files', '### (K) BAR 3.'),
    ('navigator arithmetic adopted without checking', 0, 0, 'claims', '### (K) BAR 4.'),
    ('replacements adopted on either party`s word', 0, 0, 'claims', '### (K) BAR 4: the printed profile values decide.'),

    ('search hits for u0 hand-read at their own line', 5, 0, 'hits', '### (K) BAR 5: AT MOST FIVE PATTERNS, and the number read is measured.'),
    ('constants called NAMED on the strength of digits alone', 0, 0, 'constants', '### (K) BAR 5.'),
    ('archimedean routes used to locate u0', 2, 2, 'routes', '### (K) BAR 6: and they share no code.'),
    ('tolerances left unstated before the comparison', 0, 0, 'tolerances', '### (K) BAR 6.'),
    ('values banked on one route alone', 0, 0, 'values', '### (K) BAR 6.'),
    ('identifications offered where only a location is held', 0, 0, 'claims', '### (K) BAR 7.'),

    ('conditionals answered as if their premise held', 0, 0, 'conditionals', '### (K) BAR 8.'),
    ('prices reported', 1, 1, 'prices', '### reading (4): READ / MEASUREMENT / BUILD.'),
    ('prices guessed where pricing would require a run', 0, 0, 'prices', '### section (S).'),
    ('finite facts named for the window kernel', 3, 3, 'facts', '### reading (4).'),
    ('finite facts repeated from b438 without qualification', 0, 0, 'facts', '### (K) BAR 9: the second is qualified by Component 1.'),

    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### section (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms scanning source without stripping comments', 0, 0, 'arms', '### (K) BAR 11.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms matching a banked table without normalising line endings', 0, 0, 'arms', '### (K) BAR 11.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 11: A2.'),
    ('format strings printed without their arguments', 0, 0, 'lines', '### (K) BAR 11.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### section (G2): 0.'),
    ('report lines broken mid-token by the wrapper', 0, 0, 'lines', '### (K) BAR 11.'),
    ('misses patched rather than printed', 0, 0, 'misses', '### (K) BAR 12.'),

    ('new `relay` act-tool files named on this face', 6, 6, 'files', '### (W).'),
    ('further `relay` act tools under the (R47) generator', 2, 0, 'files', '### (W): THE BOUND IS 2.'),
    ('write-list entries naming a class rather than a path or a generator', 0, 0, 'entries', '### (W) and (R47).'),
    ('existing `relay` tools edited in place', 1, 1, 'tools', '### (W): banked_index.py.'),
    ('corpus documents written other than by append', 0, 0, 'documents', '### (W).'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('TECHNE commits', 0, 0, 'commits', '### section (W).'),
    ('ad-hoc shell-typed numbers in the bank', 0, 0, 'count', 'RULING (3).'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b439_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b439_registration_2026-09-12.txt -- b439, "
                             "THE FIXED PROFILE, THE FIXED POINT, AND ONE ARITHMETIC CLAIM"),
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
