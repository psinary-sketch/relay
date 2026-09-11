# -*- coding: utf-8 -*-
"""b420_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b420_registration_2026-09-11.txt')
SPEC = os.path.join(ROOT, 'data', 'b420_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### (K) BAR 9.'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### (K) BAR 9.'),
    ('platform calls of any kind', 0, 0, 'calls', '### (K) BAR 9; section (Z).'),
    ('kernel .lean files touched other than SinglePrimeFactor.lean', 0, 0, 'files', '### (K) BAR 1.'),
    ('terminals added or moved', 0, 0, 'terminals', '### (K) BAR 1.'),
    ('bytes by which the regenerated profile differs from its blob at the pin', 0, 0, 'bytes', '### (W) KIND 5.'),
    ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted.'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated at a new depth', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened on a bright verdict', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('channels opened', 0, 0, 'channels', '### section (Z).'),
    ('rows of `FACES_LEDGER.md` added', 0, 0, 'rows', '### (K) BAR 8: an entry on row U1 is not a row.'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z).'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z).'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('orientation-layer lines edited', 0, 0, 'lines', '### section (Z).'),
    ('tuples or kernel figures moved', 0, 0, 'values', '### (K) BAR 2.'),
    ('claims about h2, in either direction', 0, 0, 'claims', '### (K) BAR 10.'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('verdicts on M-2', 0, 0, 'verdicts', 'carried from b310.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 11.'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### section (J), (R26).'),
    ('scores averaged to one word where premise and conclusion differ', 0, 0, 'scores', '### section (J), (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### (R28).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('author rulings ratified by this paste', 1, 1, 'rulings', '### section (A): (R36).'),
    ('author rulings extended beyond what they say', 0, 0, 'rulings', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A).'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('readings of the order declared in advance on this face', 7, 7, 'readings', '### section (A): (0) to (6).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('extract reads left AMBIGUOUS or ABSENT', 0, 0, 'reads', '### section (A).'),
    ('survey run records overwritten', 0, 0, 'records', '### section (A).'),
    ('orientation citations read by address', 0, 0, 'citations', '### section (A): by marker.'),
    ('bytes of the lock gate or the scan changed', 0, 0, 'bytes', '### (K) BAR 4.'),
    ('instrument items recorded without a trigger that can fire', 0, 0, 'items', '### (A) reading (1): (R23).'),
    ('instrument lanes opened', 0, 0, 'lanes', '### (A) reading (1).'),
    ('words of an annotated file lost or reordered', 0, 0, 'words', '### (K) BAR 2.'),
    ('correspondence rows edited in place', 0, 0, 'rows', '### (K) BAR 3: row 263 unedited.'),
    ('sentences of any banked ferry edited', 0, 0, 'sentences', '### (K) BAR 3.'),
    ('QUALIFIED sentences listed beside their terminal', 8, 8, 'sentences', '### (A) reading (2).'),
    ('parts of the step priced in Component 2', 2, 2, 'parts', '### (A) reading (3).'),
    ('probes compiled for Component 2 or Component 4', 0, 0, 'probes', '### (K) BAR 5.'),
    ('kernel-write clauses of b419`s face re-read', 8, 8, 'clauses', '### section (E).'),
    ('standing clauses added from Component 3', 0, 0, 'clauses', '### section (E).'),
    ('hypotheses of Theorem 3.1 read one by one', 5, 5, 'hypotheses', '### (A) reading (5).'),
    ('verdicts of Component 4', 1, 1, 'verdicts', '### section (F): exactly one of three.'),
    ('ferry paraphrases deciding over their source', 0, 0, 'paraphrases', '### (K) BAR 6.'),
    ('entries on row U1 on any verdict but INSTANCE', 0, 0, 'entries', '### (K) BAR 8.'),
    ('entries on row U1 on INSTANCE', 1, 0, 'entries', '### (W) KIND 9: demand MEASURED at the verdict.'),
    ('bridges typed', 0, 0, 'bridges', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('bars declared', 12, 12, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms scanning source without stripping comments AND string literals', 0, 0, 'arms', '### (K) BAR 11.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 11.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 11: A2.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### (K) BAR 11.'),
    ('report lines broken mid-token by the wrapper', 0, 0, 'lines', '### (K) BAR 11.'),
    ('new `relay` act-tool files', 6, 6, 'files', '### (W) KIND 1.'),
    ('shared instruments newly created', 0, 0, 'instruments', '### (W): walker_guard IMPORTED.'),
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
    print('b420_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b420_registration_2026-09-11.txt -- b420, THE PROOF CITED, "
                             "THE LOCK RULED, AND THE LEMMA AIMED AT THE RIGHT OBJECT"),
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
