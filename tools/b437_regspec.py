# -*- coding: utf-8 -*-
"""b437_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b437_registration_2026-09-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b437_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### section (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### section (Z).'),
    ('platform calls of any kind', 0, 0, 'calls', '### section (Z): the ls-remote reads are the pins`, the pushes the ritual`s.'),
    ('kernel .lean files touched', 0, 0, 'files', '### section (Z): SIDE-window is READ at its pin and not touched.'),
    ('kernel builds', 0, 0, 'builds', '### section (Z).'),
    ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### section (Z).'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('candidate zeros, seeds, families or arrangements constructed', 0, 0, 'candidates', '### section (Z).'),
    ('claims about RH, h2 or zeta', 0, 0, 'claims', '### section (Z).'),
    ('claims that the criterion is violated, satisfied globally, or tested', 0, 0, 'claims', '### section (Z) and (X): the instrument sums on-line ordinates.'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z): b436`s least of all.'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### section (Z).'),
    ('register rows or ledger rows edited', 0, 0, 'rows', '### section (Z).'),
    ('cells of FACES_LEDGER.md written', 0, 0, 'cells', '### section (Z): the register stays frozen at six.'),
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
    ('counts or values the seat predicts on this face', 0, 0, 'predictions', '### section (J): C10.'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),

    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('pre-push guard runs at step zero', 0, 0, 'runs', '### section (A): deferred to the close.'),
    ('readings of the order declared in advance on this face', 8, 8, 'readings', '### section (A): (0) to (7).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A): the extract reports 0 over 20 reads.'),
    ('routed citations corrected with both locations named', 1, 1, 'citations', '### section (A): b436`s bump-normalization citation.'),
    ('prior banks edited to make that correction', 0, 0, 'files', '### section (A): b436`s bank is NOT edited.'),

    ('author rulings ratified by this paste', 1, 1, 'rulings', '### reading (1): (R48).'),
    ('rulings extended beyond their own words', 0, 0, 'rulings', '### (K) BAR 9.'),
    ('lanes opened', 1, 1, 'lanes', '### section (A): THE INSTRUMENT LANE, FOR THE WINDOW LADDER ONLY.'),
    ('lanes opened beyond the one the ruling names', 0, 0, 'lanes', '### section (A) and (K) BAR 10.'),
    ('disproof lanes opened', 0, 0, 'lanes', '### (K) BAR 10: its trigger`s condition is NAMED and the disposition ROUTED.'),
    ('triggers named rather than left to be noticed', 1, 1, 'triggers', '### section (A): b432`s, whose condition (R48) meets.'),
    ('lanes left open at this act`s end', 0, 0, 'lanes', '### section (A): the lane closes at this act`s end.'),
    ('new instruments built', 0, 0, 'instruments', '### (K) BAR 9: more rungs, the same instrument.'),
    ('instrument files edited', 0, 0, 'files', '### (K) BAR 9: not one line of five named files.'),
    ('files written in SIDE-window', 0, 0, 'files', '### section (W): read at its pin, not touched.'),

    ('ladder pins read', 1, 1, 'pins', '### reading (1): SIDE-window at its own HEAD, tree checked clean.'),
    ('ladder non-claims carried at prominence', 1, 1, 'statements', '### reading (1) and (K) BAR 1.'),
    ('columns in which the ladder`s W and the corpus`s W_inf are written for each other', 0, 0, 'columns', '### (K) BAR 1.'),
    ('compiled ladder values recomputed and checked', 17, 17, 'values', '### reading (2): W 2 through W 18.'),
    ('rungs assigned before the recomputation agreed with the compiled table', 0, 0, 'rungs', '### (K) BAR 2.'),
    ('measured cells tabled against their rungs', 13, 13, 'cells', '### reading (2): b321`s thirteen.'),

    ('new cells computed in the extension', 24, 22, 'cells', '### section (SPAN): TWENTY-TWO, CAP TWENTY-FOUR, and the closing prints the actual list.'),
    ('radii computed outside the declared span', 0, 0, 'radii', '### (K) BAR 8.'),
    ('trends extrapolated past the last cell actually run', 0, 0, 'extrapolations', '### (K) BAR 8.'),
    ('banked cells reproduced before any new one was asked for', 1, 1, 'cells', '### (K) BAR 3: a = 3.0.'),
    ('cells whose identity was not re-checked', 0, 0, 'cells', '### (K) BAR 4.'),
    ('cells dropped without being reported', 0, 0, 'cells', '### (K) BAR 4.'),
    ('cells whose pole term was not checked', 0, 0, 'cells', '### section (S).'),
    ('negative-Z cells read as a crossing', 0, 0, 'cells', '### (K) BAR 6 and (X) clause (1).'),

    ('radii at which the floor is priced by this act', 3, 0, 'radii', '### section (SPAN): AT MOST THREE, and the number is measured.'),
    ('ratio readings printed without the floor`s reach stated', 0, 0, 'readings', '### (K) BAR 7.'),

    ('sections stating what a crossing means, written before any new value', 1, 1, 'sections', '### section (X) and (K) BAR 5.'),
    ('readings fitted to numbers already seen', 0, 0, 'readings', '### (K) BAR 5.'),

    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### section (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms scanning source without stripping comments', 0, 0, 'arms', '### (K) BAR 11.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms matching a banked table without normalising line endings', 0, 0, 'arms', '### (K) BAR 11.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 11: A2.'),
    ('act numbers matched unbounded inside a git SHA', 0, 0, 'arms', '### (K) BAR 11.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### section (G2): 0.'),
    ('report lines broken mid-token by the wrapper', 0, 0, 'lines', '### (K) BAR 11.'),
    ('misses patched rather than printed', 0, 0, 'misses', '### (K) BAR 12.'),

    ('new `relay` act-tool files named on this face', 6, 6, 'files', '### (W): extract, regspec, reg_gate, components, checks, desk_bank.'),
    ('further `relay` act tools under the (R47) generator', 2, 0, 'files', '### (W): THE BOUND IS 2, and the closing prints the actual list against it.'),
    ('write-list entries naming a class rather than a path or a generator', 0, 0, 'entries', '### (W) and (R47).'),
    ('existing `relay` tools edited in place', 1, 1, 'tools', '### (W): banked_index.py, which the key step writes.'),
    ('corpus documents written other than by append', 0, 0, 'documents', '### (W): OPEN_TRAILS and CORRESPONDENCE, APPENDED ONLY.'),
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
    print('b437_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b437_registration_2026-09-12.txt -- b437, "
                             "THE WINDOW OPENED BY RUNGS"),
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
