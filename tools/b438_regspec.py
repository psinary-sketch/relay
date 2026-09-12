# -*- coding: utf-8 -*-
"""b438_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b438_registration_2026-09-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b438_satisfiable.json')

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
    ('routes proposed, priced or opened', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('candidate zeros, seeds, families or arrangements constructed', 0, 0, 'candidates', '### section (Z) and (K) BAR 9.'),
    ('claims about RH, h2, zeta or any zero', 0, 0, 'claims', '### section (Z).'),
    ('claims that the criterion is tested', 0, 0, 'claims', '### (K) BAR 8: the zero side is inherited and the act says so.'),
    ('criterion readings taken from the second family', 0, 0, 'readings', '### (K) BAR 6: it is not lawful and carries none.'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z).'),
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
    ('counts or values the seat predicts on this face', 0, 0, 'predictions', '### section (J): C10.'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),

    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('readings of the order declared in advance on this face', 7, 7, 'readings', '### section (A): (0) to (6).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A): 0 over 12 reads.'),

    ('author rulings ratified by this paste', 1, 1, 'rulings', '### reading (0): (R49).'),
    ('rulings extended beyond their own words', 0, 0, 'rulings', '### (K) BAR 9.'),
    ('lanes opened', 1, 1, 'lanes', '### section (A): the instrument lane, in (R49)`s scope.'),
    ('lanes opened beyond the one the ruling names', 0, 0, 'lanes', '### section (Z).'),
    ('disproof lanes opened', 0, 0, 'lanes', '### (K) BAR 10: its trigger fired at (R48) and its disposition waits on the author.'),
    ('lanes left open at this act`s end', 0, 0, 'lanes', '### section (A).'),
    ('new instruments built', 0, 0, 'instruments', '### (K) BAR 9.'),
    ('instrument files edited', 0, 0, 'files', '### (K) BAR 9.'),
    ('new families defined', 0, 0, 'families', '### (K) BAR 9: both families are ones the record already holds.'),
    ('cells computed beyond b437`s span', 0, 0, 'cells', '### (K) BAR 9 and reading (6).'),

    ('test functions identified from the instrument`s own source', 1, 1, 'functions', '### reading (1): the AIMED seed.'),
    ('moments the seed is solved to vanish', 2, 2, 'moments', '### reading (1).'),
    ('cells decomposed term by term', 35, 35, 'cells', '### reading (2): all thirty-five.'),
    ('routes of (149) run', 2, 2, 'routes', '### reading (2).'),
    ('route pairs offered as independent that share code', 0, 0, 'pairs', '### reading (2): the (149) pair is declared SINGLE-ARM.'),
    ('identities reported as if they were measurements', 0, 0, 'verdicts', '### (K) BAR 1.'),
    ('terms whose sign is asserted rather than printed', 0, 0, 'terms', '### (K) BAR 2.'),

    ('archimedean routes used to locate the radius', 2, 2, 'routes', '### reading (4): and they share no code.'),
    ('tolerances left unstated before the comparison', 0, 0, 'tolerances', '### (K) BAR 4.'),
    ('radii banked on one route alone', 0, 0, 'radii', '### (K) BAR 4.'),
    ('sign changes of h+ located', 1, 1, 'zeros', '### reading (5): u0 = 6.289835989, a property of the digamma.'),
    ('second families evaluated for the crossing question', 1, 1, 'families', '### reading (5).'),
    ('second families used for a criterion reading', 0, 0, 'families', '### (K) BAR 6.'),

    ('cells past the room', 1, 1, 'cells', '### reading (6): exactly one, at a = 5.656854.'),
    ('trends drawn through a single point', 0, 0, 'trends', '### (K) BAR 7.'),
    ('criterion readings taken without saying the zero side is inherited', 0, 0, 'readings', '### (K) BAR 8.'),

    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### section (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms scanning source without stripping comments', 0, 0, 'arms', '### (K) BAR 11.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms matching a banked table without normalising line endings', 0, 0, 'arms', '### (K) BAR 11.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 11: A2.'),
    ('format strings printed without their arguments', 0, 0, 'lines', '### (K) BAR 11: b437`s stray-placeholder defect, now an arm.'),
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
    print('b438_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b438_registration_2026-09-12.txt -- b438, "
                             "WHAT ALTERNATES THE SIGN, AND WHERE THE ROOM CLOSES"),
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
