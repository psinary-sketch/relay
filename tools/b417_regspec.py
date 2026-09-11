# -*- coding: utf-8 -*-
"""b417_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### **THE CLAUSES THAT MATTER MOST ARE THE ONES A SEAT COULD QUIETLY BREAK:** ### no half of the
### contradiction edited, no ruling by a seat, no byte of the Reader's body, no escaped write left
### standing, and no push of the species module.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b417_registration_2026-09-11.txt')
SPEC = os.path.join(ROOT, 'data', 'b417_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### (K) BAR 9.'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### (K) BAR 9.'),
    ('platform calls of any kind', 0, 0, 'calls', '### (K) BAR 9; section (Z).'),
    ('`.lean` files touched', 0, 0, 'files', '### (K) BAR 1.'),
    ('kernel builds run', 0, 0, 'builds', '### (K) BAR 1.'),
    ('terminals added, renamed or restated', 0, 0, 'terminals', '### (K) BAR 1.'),
    ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted, under Rule 4.10.'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (Z).'),
    ('premises discharged', 0, 0, 'premises', '### section (Z).'),
    ('doors restated at a new depth', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened on a bright verdict', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('channels opened', 0, 0, 'channels', '### section (Z).'),
    ('rows of `FACES_LEDGER.md` written', 0, 0, 'rows', '### section (Z): FROZEN at six.'),
    ('rows retired or lists closed', 0, 0, 'rows', '### section (Z).'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z): (R33) and (R34) are EXECUTED, not extended.'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z).'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('orientation-layer lines edited', 0, 0, 'lines', '### section (Z).'),
    ('registry rows written', 0, 0, 'rows', '### section (W).'),
    ('claims about h2, in either direction', 0, 0, 'claims', '### (K) BAR 10.'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('verdicts on M-2', 0, 0, 'verdicts', 'carried from b310.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 11.'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### section (J), (R26).'),
    ('scores averaged to one word where premise and conclusion differ', 0, 0, 'scores', '### section (J), (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### section (C), (R28).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('amendments carried on the face as arriving before the lock', 1, 1, 'amendments', '### section (A).'),
    ('ferry scan hits', 0, 0, 'hits', '### section (A).'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('author rulings ratified by this paste', 2, 2, 'rulings', '### section (A): (R33) and (R34).'),
    ('author rulings extended beyond what they say', 0, 0, 'rulings', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0 each.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('readings of the order declared in advance on this face', 12, 12, 'readings', '### section (A): (0) to (11).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('extract reads left AMBIGUOUS or ABSENT', 0, 0, 'reads', '### section (A).'),
    ('survey run records overwritten', 0, 0, 'records', '### section (A): run 1 kept.'),
    ('orientation citations read by address', 0, 0, 'citations', '### section (A): by marker.'),
    ('defect reports put to the author', 1, 1, 'reports', '### section (C).'),
    ('words of the universality sentence edited', 0, 0, 'words', '### (K) BAR 2.'),
    ('tuple values edited', 0, 0, 'values', '### (K) BAR 2.'),
    ('sentences of this act`s record saying which half is wrong', 0, 0, 'sentences', '### (K) BAR 2, (R34).'),
    ('citation shapes run', 2, 2, 'shapes', '### section (C).'),
    ('residue paragraphs scored without a printed reading', 0, 0, 'paragraphs', '### (K) BAR 7.'),
    ('header figures compared with the formula', 4, 4, 'figures', '### section (D).'),
    ('classes whose load-bearing question is decided', 2, 2, 'classes', '### section (D): B and D.'),
    ('resolutions whose moved figures are printed', 2, 2, 'resolutions', '### section (R34).'),
    ('tools repaired by this act', 1, 1, 'tools', '### (K) BAR 4: b369_hygiene.py only.'),
    ('snapshot runs of the repaired tool before its live run', 1, None, 'runs', '### (K) BAR 4: at least one, MEASURED.'),
    ('live runs of the repaired tool before its snapshot run', 0, 0, 'runs', '### (K) BAR 4.'),
    ('escaped writes left standing without being named', 0, 0, 'writes', '### (K) BAR 4.'),
    ('prior-act records left differing after the live run', 0, 0, 'records', '### section (E).'),
    ('verdict lines of the repaired tool edited', 0, 0, 'lines', '### (K) BAR 4.'),
    ('backups swept whose bytes are not in an object store', 0, 0, 'files', '### (K) BAR 5.'),
    ('fixture polarities run on the new instrument', 2, 2, 'polarities', '### section (H).'),
    ('shared instruments newly created', 1, 1, 'instruments', '### (W) KIND 4.'),
    ('species modules filed', 1, 1, 'modules', '### (W) KIND 9.'),
    ('commits pushed from TECHNE-Core', 0, 0, 'commits', '### (K) BAR 13.'),
    ('untracked TECHNE modules not this act`s staged', 0, 0, 'files', '### section (H).'),
    ('caveats marked without the predicate of (F)', 0, 0, 'caveats', '### section (F).'),
    ('caveats found by the unchanged description', 0, None, 'caveats', '### MEASURED.'),
    ('caveats graded by this act', 0, 0, 'caveats', '### section (F).'),
    ('positive controls run before the count they validate', 4, None, 'controls', '### (K) BAR 6: MEASURED, at least four.'),
    ('counts reported on a failed control', 0, 0, 'counts', '### (K) BAR 6.'),
    ('clauses added to the Reader`s head', 1, 1, 'clauses', '### (K) BAR 3, (R33).'),
    ('words of the Reader`s existing head clauses changed', 0, 0, 'words', '### (K) BAR 3.'),
    ('bytes of the Reader`s body edited', 0, 0, 'bytes', '### (K) BAR 3.'),
    ('primes named in the added clause beyond the ruling`s seven', 0, 0, 'primes', '### section (G): the ruling is not extended.'),
    ('readings priced for the ruling', 2, 2, 'readings', '### section (I).'),
    ('readings adopted by this seat', 0, 0, 'readings', '### section (I).'),
    ('sentences of the bank joining the slots and the fifteen', 0, 0, 'sentences', '### (K) BAR 8, the amendment.'),
    ('defects in prior records or other documents repaired by this act', 0, 0, 'repairs', '### (K) BAR 12.'),
    ('bars declared', 13, 13, 'bars', '### section (K).'),
    ('numerical bars on a computed quantity', 0, 0, 'bars', '### (K).'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (K) BAR 11.'),
    ('arms scanning source without stripping comments AND string literals', 0, 0, 'arms', '### (K) BAR 11.'),
    ('prose-reading arms that match before folding markup away', 0, 0, 'arms', '### (K) BAR 11.'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### (K) BAR 11: A2.'),
    ('inherited arms not re-pointed at this act', 0, 0, 'arms', '### (K) BAR 11.'),
    ('report lines broken mid-token by the wrapper', 0, 0, 'lines', '### (K) BAR 11.'),
    ('new `relay` act-tool files', 6, 6, 'files', '### (W) KIND 1.'),
    ('existing `relay` tools edited in place', 1, 1, 'tools', '### (W) KIND 3.'),
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
    print('b417_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b417_registration_2026-09-11.txt -- b417, THE CONTRADICTION PUT "
                             "TO ITS OWNER, AND THE SECOND TOOL CLEARED"),
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
