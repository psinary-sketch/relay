# -*- coding: utf-8 -*-
"""b630_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Written whole from b629`s spec, every clause re-read against this face: nothing at Zenodo; no kernel written and no Lean build;
### ### two shared instruments edited after the seal under (R240)(3) and (5), each with a new test; appends to two ledgers; one line
### ### appended to data/act_roots.txt; the pages re-emitted; two registry records read once each with no identifier; the bench run twice;
### ### b628`s local intake bank untracked; no orphan at step zero; two questions put to the author before the seal.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b630_registration_2026-10-05.txt')
SPEC = os.path.join(ROOT, 'data', 'b630_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions: new versions, files uploaded, records created', 0, 0, 'actions', '### (Z): nothing deposits.'),
    ('platform calls of any kind (Zenodo)', 0, 0, 'calls', '### the head: nothing at Zenodo written or read.'),
    ('registry records read', 2, 2, 'reads', '### Component 4: arXiv for the conjecture and for Burnol`s bound, once each.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### (R240)(2)(i).'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z).'),
    ('kernel files written', 0, 0, 'files', '### (Z): no kernel touched.'),
    ('kernels of the federation written', 0, 0, 'kernels', '### (Z).'),
    ('kernel tags made', 0, 0, 'tags', '### (Z).'),
    ('kernel branches made', 0, 0, 'branches', '### (Z).'),
    ('Lean builds run', 0, 0, 'builds', '### the ferry: no Lean build this act.'),
    ('fresh probe runs of the generator', 1, 1, 'runs', '### Component 3: the profiled run, whose output serves the ζ page.'),
    ('bench runs', 2, 2, 'runs', '### Component 5: two, compared byte for byte.'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('clones deleted', 0, 0, 'clones', '### (Z).'),
    ('CORRESPONDENCE rows written', 0, 0, 'rows', '### (R240) orders none.'),
    ('grade names minted', 0, 0, 'grades', '### (Z): rule and cell are provenance marks, not grades.'),
    ('table rows graded from the rule', 13, 13, 'rows', '### (R240)(3) and the author`s answer: the rows of v0.24.'),
    ('table rows graded from the rule beyond the rows of v0.24', 0, 0, 'rows', '### the author`s answer, prompt 1: banked, not applied.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A); (Z).'),
    ('claims about d_N beyond the computed range', 0, 0, 'claims', '### (R240)(6).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule clauses added to a shared instrument by the author`s ruling', 2, 2, 'clauses', '### (R240)(3) the provenance column; (5) the probe`s printed reading.'),
    ('correction entries written under the author`s ruling', 0, 0, 'entries', '### (R240) orders none.'),
    ('standing lines entered under the author`s ruling', 1, 1, 'lines', '### (R240)(2)(i): no outbound identifier.'),
    ('clauses entered under the author`s ruling', 2, 2, 'clauses', '### (R240)(3)-(4): provenance; helpers.'),
    ('items entered', 1, 1, 'items', '### (R240)(1): the Nyman registry read.'),
    ('work-orders entered', 1, 1, 'work-orders', '### the author`s answer, prompt 1: W-ORD-TABLE-RULE-GRADES.'),
    ('weight lines entered', 1, 1, 'lines', '### (R240)(1): b629 at its weight.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b629 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place', 2, 2, 'tools', '### (R240)(3), (5): tools/terminal_table.py and tools/chain_page.py, after the seal, through the Edit tool.'),
    ('relay instruments created', 2, 2, 'tools', '### (W): the two tests of those edits.'),
    ('own suite edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('own record-tool edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited other than the generated pages and the ledgers', 0, 0, 'documents', '### (Z).'),
    ('ANNEX, census or synthesis files written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### b628`s full bank stays untracked.'),
    ('generated pages re-emitted', 2, 2, 'pages', '### Component 6: both, one per call, each committed where it changes.'),
    ('mid-act pushes before the act root', 2, 2, 'pushes', '### relay and PLACE-papers by push_gated.sh, so each head the root names is at its remote.'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry: root verifies inside the suite alone.'),
    ('MANIFEST lines written', 0, 0, 'lines', '### OPEN_TRAILS :12929: none this act; no mirror is built.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z): ERRATA untouched.'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('TECHNE-Core pushes', 0, 0, 'pushes', '### (Z).'),
    ('README.md or SPIRAL_MAP.md edits', 0, 0, 'edits', '### (Z).'),
    ('REGISTRY.md appends', 0, 0, 'appends', '### (Z).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### OPEN_TRAILS beneath :12799, MEASURED off the bank.'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('questions asked of the author before the seal', 2, 2, 'questions', '### section (0): one call, two questions, banked by the record tool.'),
    ('questions asked of the author after the seal', 0, 0, 'questions', '### none planned.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R240).'),
    ('PLACE-papers documents written other than by appending or regenerating', 0, 0, 'documents', '### (W).'),
    ('PLACE-papers documents written at all', 4, 3, 'documents', '### (W): FINDINGS, OPEN_TRAILS, the ζ page; the χ page only where it changes.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (W): none.'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('mirror zips built', 0, 0, 'zips', '### (Z): no mirror this act.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b630_arms_prerun.txt.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 8, 8, 'files', '### (W): the act`s own, the step-zero test runner and the bench among them.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b630_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    try:
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b630_tests_stepzero.json'), encoding='utf-8')))
    except Exception:
        tests = 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests)
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANK, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS'):
        print('      %-9s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b630_registration_2026-10-05.txt -- b630, LANE THREE ACT FIFTY-SEVEN: THE NYMAN–BEURLING DISTANCES "
                             "d_N² IN ARB BALLS BESIDE 2λ₁; NEW ROWS GRADED FROM THE RULE WITH PROVENANCE; HELPER ROWS AS OBJECTS; THE "
                             "PROBE HOLD, UNDER (R240)"), "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    print()
    print('  clauses emitted : %d' % len(clauses))
    nz = [c for c in clauses if c['demand']]
    print('  ### ### **CLAUSES WITH A NON-ZERO DEMAND : %d**' % len(nz))
    print('  written : %s' % os.path.basename(SPEC))
    print('=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
