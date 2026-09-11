# -*- coding: utf-8 -*-
"""b416_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### **AND THE CLAUSES THAT MATTER MOST BOUND A BUILD.** ### Every act from `b403` to `b413`
### could write `.lean files touched : 0` and be done. ### This one cannot. ### So the zero
### clauses are re-aimed: not *nothing was written*, but ### **NOTHING EXISTING WAS EDITED, NO
### ### TERMINAL CARRIES AN AXIOM, AND THE PRIOR PROFILE IS STILL A TRUE BYTE PREFIX.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b416_registration_2026-09-11.txt')
SPEC = os.path.join(ROOT, 'data', 'b416_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions', 0, 0, 'actions', '### (K) BAR 9.'),
    ('bytes written at Zenodo, in any branch', 0, 0, 'bytes', '### (K) BAR 9.'),
    ('platform calls of any kind', 0, 0, 'calls', '### (K) BAR 9.'),
    ('`.lean` files touched', 0, 0, 'files', '### (K) BAR 1: the kernel lane READS.'),
    ('kernel builds run', 0, 0, 'builds', '### (K) BAR 1.'),
    ('terminals added, renamed or restated', 0, 0, 'terminals', '### (K) BAR 1.'),
    ('repositories cloned', 0, 0, 'repositories', '### section (Z).'),
    ('branches merged, fetched or checked out', 0, 0, 'branches', '### section (Z): the push branch excepted, under Rule 4.10.'),
    ('grades moved, conferred or minted', 0, 0, 'grades', '### section (C).'),
    ('premises discharged', 0, 0, 'premises', '### section (C).'),
    ('doors restated at a new depth', 0, 0, 'doors', '### section (Z).'),
    ('routes proposed, priced or opened on a bright verdict', 0, 0, 'routes', '### section (Z).'),
    ('kappa values measured or certified', 0, 0, 'values', '### section (Z).'),
    ('channels opened', 0, 0, 'channels', '### section (Z).'),
    ('rows of `FACES_LEDGER.md` written', 0, 0, 'rows', '### section (Z): FROZEN at six.'),
    ('rows retired or lists closed', 0, 0, 'rows', '### section (Z).'),
    ('folds run', 0, 0, 'folds', '### section (Z).'),
    ('rules struck, amended, widened or re-ruled', 0, 0, 'rules', '### section (Z): (R32) is EXECUTED, not extended.'),
    ('FERRY_STANDING clauses added', 0, 0, 'clauses', '### section (Z).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### section (Z).'),
    ('banked ferries edited', 0, 0, 'files', '### section (Z).'),
    ('orientation-layer lines edited', 0, 0, 'lines', '### section (Z).'),
    ('in-place repairs of an original sentence of any corpus document', 0, 0, 'repairs', '### section (Z): the one in-place edit is a relay TOOL path, (W) KIND 3.'),
    ('claims about h2, in either direction', 0, 0, 'claims', '### (K) BAR 10.'),
    ('aggregations stated', 0, 0, 'statements', 'M-2 IS OWED AND STAYS OWED.'),
    ('verdicts on M-2', 0, 0, 'verdicts', 'carried from b310.'),
    ('counts adopted without measurement', 0, 0, 'counts', '### section (Z).'),
    ('arms trusted because a previous act trusted them', 0, 0, 'arms', '### (K) BAR 11.'),
    ('expectations scored over a set this face does not name', 0, 0, 'expectations', '### (R26).'),
    ('scores averaged to one word where premise and conclusion differ', 0, 0, 'scores', '### (R27).'),
    ('results applied to an object of a kind they do not quantify over', 0, 0, 'results', '### (R28).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, receipt IN FULL.'),
    ('ferry scan hits', 0, 0, 'hits', '### section (A).'),
    ('act numbers claimed by an unclosed ferry', 0, 0, 'numbers', '### section (A): A1.'),
    ('author rulings ratified by this paste', 1, 1, 'rulings', '### section (A): (R32).'),
    ('author rulings extended beyond what they say', 0, 0, 'rulings', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### section (A): TOTAL MISSING 0 each.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### section (A).'),
    ('readings of the order declared in advance on this face', 8, 8, 'readings', '### section (A).'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('extract reads left AMBIGUOUS or ABSENT', 0, 0, 'reads', '### section (A).'),
    ('components the act reports on, per component and not per class', 2, 2, 'components', '### section (C): n1 and n4.'),
    ('documents named as owning the component definitions', 1, None, 'documents', '### section (C): MEASURED.'),
    ('universality sentences quoted from the owner', 1, 1, 'sentences', '### section (C).'),
    ('universality claims tested against the kernel declarations', 1, 1, 'claims', '### section (C).'),
    ('tuple values taken from recollection rather than from the declarations', 0, 0, 'values', '### section (C).'),
    ('prices printed for deriving n1 at class A', 1, 1, 'prices', '### section (D).'),
    ('`.lean` files written by this act', 0, 0, 'files', '### section (D): PRICED; NOT BUILT.'),
    ('bridges read for their supply pattern', 2, 2, 'bridges', '### section (D).'),
    ('tools repaired by this act', 1, 1, 'tools', '### (K) BAR 8: b371_hookpath.py only.'),
    ('dated tools found by description', 0, None, 'tools', '### MEASURED.'),
    ('dated tools found by a static hit and reported without being run', 0, 0, 'tools', '### (K) BAR 7.'),
    ('dated tools repaired that the write list does not name', 0, 0, 'tools', '### (K) BAR 8.'),
    ('fixture polarities run on the repaired tool', 2, 2, 'polarities', '### section (E).'),
    ('annotations drafted for the seal`s caveat', 1, 1, 'annotations', '### section (F).'),
    ('annotations applied to the sealed file', 0, 0, 'annotations', '### (K) BAR 4.'),
    ('sha256 of the sealed file printed, before and after', 2, 2, 'digests', '### (K) BAR 4.'),
    ('words struck from the original caveat', 0, 0, 'words', '### section (F): the annotation is ADDITIVE.'),
    ('positive controls run before the count they validate', 1, 1, 'controls', '### (K) BAR 6.'),
    ('counts reported on a failed control', 0, 0, 'counts', '### (K) BAR 6.'),
    ('kernel caveats counted by description', 0, None, 'caveats', '### MEASURED.'),
    ('kernel caveats graded by this act', 0, 0, 'caveats', '### section (G).'),
    ('Reader copies located by digest', 1, 1, 'copies', '### (H).'),
    ('bytes of the Reader`s body edited', 0, 0, 'bytes', '### (K) BAR 2.'),
    ('clauses in the Reader`s currency note', 3, 3, 'clauses', '### (H): exactly what (R32) says.'),
    ('class lines written in the Reader`s head', 1, 1, 'lines', '### (H).'),
    ('scheme lines written in the Reader`s head', 1, 1, 'lines', '### (H).'),
    ('registry rows written for the Reader', 1, 1, 'rows', '### (H).'),
    ('existing carriers cross-referenced from the row', 3, 3, 'carriers', '### (H).'),
    ('lines stating the lineage', 1, 1, 'lines', '### (H): on the row and nowhere else.'),
    ('files of the separate continuation written or quoted into a corpus document', 0, 0, 'files', '### (K) BAR 3.'),
    ('findings about the Reader written into the Reader`s body', 0, 0, 'findings', '### (K) BAR 12.'),
    ('SVG figures written under `outputs/`', 1, 1, 'figures', '### (I).'),
    ('other files under `outputs/` touched', 0, 0, 'files', '### (I).'),
    ('kinds the figure distinguishes', 4, 4, 'kinds', '### (I): generator, consecutive, inclusion, jump.'),
    ('grades the figure carries', 0, 0, 'grades', '### (K) BAR 5.'),
    ('citations of the figure as evidence', 0, 0, 'citations', '### (K) BAR 5.'),
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
    ('shared instruments newly created', 0, 0, 'instruments', '### (W).'),
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
    print('b416_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b416_registration_2026-09-11.txt -- b416, THE PREDICATE NAMED, "
                             "AND THE GENERAL CLAUSE STATED WITHOUT ITS PROOF"),
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
