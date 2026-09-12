# -*- coding: utf-8 -*-
"""b427_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b427_registration_2026-09-11.txt')
SPEC = os.path.join(ROOT, 'data', 'b427_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### (K) BAR 10.'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### (K) BAR 10.'),
    ('platform calls of any kind', 0, 0, 'calls', '### (K) BAR 10; section (Z): the arXiv reads are reading (3)`s.'),
    ('kernel .lean files touched', 0, 0, 'files', '### (K) BAR 1.'),
    ('kernel builds', 0, 0, 'builds', '### (K) BAR 1.'),
        ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened on a bright verdict', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('channels opened', 0, 0, 'channels', '### section (Z).'),
    ('rows of `FACES_LEDGER.md` rewritten', 0, 0, 'rows', '### (K) BAR 2: one APPENDED block, 0 rows rewritten.'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z).'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('orientation-layer lines edited', 0, 0, 'lines', '### section (Z).'),
    ('tuples or kernel figures moved', 0, 0, 'values', '### section (Z).'),
    ('claims about h2, in either direction', 0, 0, 'claims', '### (K) BAR 11.'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('verdicts on M-2', 0, 0, 'verdicts', 'carried from b310.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 12.'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### section (J), (R26).'),
    ('scores averaged to one word where premise and conclusion differ', 0, 0, 'scores', '### section (J), (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### (R28).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A).'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('readings of the order declared in advance on this face', 6, 6, 'readings', '### section (A): (0) to (5).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('extract reads left AMBIGUOUS or ABSENT', 0, 0, 'reads', '### section (A).'),
    ('survey run records overwritten', 0, 0, 'records', '### section (A).'),
    ('orientation citations read by address', 0, 0, 'citations', '### section (A): by marker.'),
    ('searches or fetches before the lock', 0, 0, 'reads', '### section (A): the corpus only.'),
    ('candidates beyond the declared cap', 0, 0, 'candidates', '### (K) BAR 5: TWENTY.'),
    ('candidates failed without a quoted step', 0, 0, 'candidates', '### (K) BAR 4.'),
    ('fits, samples or likelihoods computed', 0, 0, 'computations', '### (K) BAR 6.'),
    ('steps each candidate is attempted by', 3, 3, 'steps', '### (A) reading (4): S1 CLASS, S2 HELD, S3 FORM.'),
    ('author rulings ratified by this paste', 0, 0, 'rulings', '### section (A): none; (R38) and (R39) were ratified at b426.'),
    ('rulings extended beyond their own words', 0, 0, 'rulings', '### section (A).'),
    ('lane documents edited', 0, 0, 'documents', '### section (Z).'),
    ('register rows edited', 0, 0, 'rows', '### section (Z).'),
    ('bytes of row U1`s line changed', 0, 0, 'bytes', '### (K) BAR 2.'),
    ('witness cells written', 0, 0, 'cells', '### (K) BAR 2: only if a candidate holds.'),
    ('seventh sites entered', 0, 0, 'sites', '### (K) BAR 2: the freeze at six stands.'),
    ('search hits read and not printed with a reason', 0, 0, 'hits', '### (K) BAR 3.'),
    ('site (i) counts typed rather than read off its bank', 0, 0, 'counts', '### (K) BAR 7.'),
    ('lane verdicts changed by the seat', 0, 0, 'verdicts', '### (K) BAR 2.'),
    ('lane verdicts stated by the seat', 0, 0, 'verdicts', '### (K) BAR 2.'),
    ('ferry paraphrases deciding over their source', 0, 0, 'paraphrases', '### (K) BAR 8.'),
    ('corpus bytes changed other than by append', 0, 0, 'bytes', '### (K) BAR 9.'),
    ('bridges typed', 0, 0, 'bridges', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 12.'),
    ('arms scanning source without stripping comments AND string literals', 0, 0, 'arms', '### (K) BAR 12.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 12.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 12: A2.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### (K) BAR 12.'),
    ('report lines broken mid-token by the wrapper', 0, 0, 'lines', '### (K) BAR 12.'),
    ('new `relay` act-tool files', 6, 6, 'files', '### (W) KIND 1.'),
    ('existing `relay` tools edited in place', 0, 0, 'tools', '### (W).'),
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
    print('b427_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b427_registration_2026-09-11.txt -- b427, SORTIE LEG 2, THE WITNESS ARC AT SITE (ii)"),
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
