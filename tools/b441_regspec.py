# -*- coding: utf-8 -*-
"""b441_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b441_registration_2026-09-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b441_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### section (Z).'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### section (Z).'),
    ('platform calls of any kind', 0, 0, 'calls', '### section (Z): the pins` ls-remote reads and the ritual`s pushes excepted.'),
    ('.lean files written or edited in any repository', 0, 0, 'files', '### section (Z).'),
    ('kernel builds', 0, 0, 'builds', '### section (Z).'),
    ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('addresses resolved or documents fetched', 0, 0, 'reads', '### section (Z).'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('candidate zeros, seeds, families or arrangements constructed', 0, 0, 'candidates', '### section (Z).'),
    ('claims about RH, h2 or any zero beyond quoting a verified source', 0, 0, 'claims', '### section (Z).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z) and (K) BAR 9: b440`s least of all.'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z): the refused first paste is preserved, not edited.'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### section (Z).'),
    ('register rows or ledger rows written or edited', 0, 0, 'rows', '### section (Z).'),
    ('cells of the register written', 0, 0, 'cells', '### section (Z): the freeze at six stands.'),
    ('seventh sites entered', 0, 0, 'sites', '### section (Z).'),
    ('bridges typed between any two of the six sites', 0, 0, 'bridges', '### section (Z).'),
    ('sites of the witness arc reopened or attempted', 0, 0, 'sites', '### section (Z): site (ii) is quoted, not re-attempted.'),
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
    ('statements imported', 0, 0, 'statements', '### reading (2): PRICED, nothing imported.'),
    ('cells replaced', 0, 0, 'cells', '### reading (2).'),
    ('TECHNE pushes', 0, 0, 'pushes', '### section (Z).'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### reading (1): the located line stays unedited.'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A): 0 reported.'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A): 0 reported in this paste.'),
    ('refused first pastes preserved under their own names', 1, 1, 'pastes', '### section (A).'),
    ('act numbers claimed by an unclosed ferry other than its own refused paste', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('readings of the order declared in advance on this face', 5, 5, 'readings', '### section (A): (0) to (4).'),
    ('survey findings declared before the face', 4, 4, 'findings', '### section (A): (S1) to (S4).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('survey anchor misses', 0, 0, 'misses', '### section (A).'),
    ('measurements taken before the lock', 0, 0, 'measurements', '### section (A): the survey classified and counted vocabulary only.'),
    ('author rulings ratified by this paste', 0, 0, 'rulings', '### section (A).'),
    ('addendum slots declared in the write list', 1, 1, 'slots', '### (W) and (R50): data/b441_addendum.txt.'),
    ('addendum slots carrying anything but a verbatim quotation', 0, 0, 'slots', '### (K) BAR 10.'),
    ('lanes opened', 0, 0, 'lanes', '### section (Z).'),
    ('disproof lanes opened', 0, 0, 'lanes', '### section (Z): (R51) stands.'),
    ('new instruments built', 0, 0, 'instruments', '### section (Z).'),
    ('instrument files edited', 0, 0, 'files', '### section (Z).'),
    ('new families defined', 0, 0, 'families', '### section (Z).'),
    ('near lines quoted whole and restated', 3, 3, 'lines', '### reading (1).'),
    ('near lines edited', 0, 0, 'lines', '### reading (1): SPIRAL_MAP.md:114 stays unedited.'),
    ('halves of the identification verdicted apart', 2, 2, 'halves', '### reading (1), (R27).'),
    ('routes for the counting half', 2, 1, 'routes', '### (K) BAR 5: AT LEAST ONE; the second is run, not asserted, and the two share no code.'),
    ('tolerances left unstated before a comparison', 0, 0, 'tolerances', '### (K) BAR 5.'),
    ('measured identities filed as theorems', 0, 0, 'filings', '### (K) BAR 6.'),
    ('source statements re-graded as this seat`s measurement', 0, 0, 'statements', '### (K) BAR 4.'),
    ('ledger update blocks appended through the writer', 1, 0, 'blocks', '### reading (1): AT MOST ONE, and only if every quotation verifies.'),
    ('quotations appended that the writer could not verify', 0, 0, 'quotations', '### section (S).'),
    ('sentences entered under someone other than their writer', 0, 0, 'sentences', '### (K) BAR 1.'),
    ('verified-source candidates priced', 5, 1, 'candidates', '### reading (2): AT LEAST ONE of the five; any not quotable is named NOT QUOTABLE.'),
    ('uniformity answers given without the source`s own quantifier', 0, 0, 'answers', '### (K) BAR 7.'),
    ('site (ii) failure steps quoted from the writer`s block', 2, 2, 'steps', '### reading (2): B3 and B5.'),
    ('acts whose push-side predicate is read as first committed', 11, 11, 'acts', '### reading (3)(ii): b430 to b440.'),
    ('suites read from the working tree only', 0, 0, 'suites', '### (K) BAR 8.'),
    ('closings re-verdicted', 0, 0, 'closings', '### reading (3)(ii).'),
    ('TECHNE modules written', 1, 1, 'modules', '### reading (3)(iii).'),
    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 11.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 11: A2.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### section (G2): 0.'),
    ('misses patched rather than printed', 0, 0, 'misses', '### (K) BAR 12.'),
    ('new `relay` act-tool files named on this face', 7, 7, 'files', '### (W).'),
    ('further `relay` act tools under the (R47) generator', 2, 0, 'files', '### (W): THE BOUND IS 2.'),
    ('write-list entries naming a class rather than a path or a generator', 0, 0, 'entries', '### (W) and (R47).'),
    ('existing `relay` tools edited in place', 1, 1, 'tools', '### (W): banked_index.py.'),
    ('corpus documents written other than by append', 0, 0, 'documents', '### (W).'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('ad-hoc shell-typed numbers in the bank', 0, 0, 'count', 'RULING (3).'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b441_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b441_registration_2026-09-12.txt -- b441, "
                             "THE IDENTIFICATION FILED, THE OVERSTATEMENT CORRECTED, AND TWO FILINGS"),
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
