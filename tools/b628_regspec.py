# -*- coding: utf-8 -*-
"""b628_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Written whole from b627`s spec, every clause re-read against this face: nothing at Zenodo; Zeta23 built in a clone at its pin
### ### outside every repository; one kernel written -- a docstring on SIDE-explicit-formula`s Simplicity.lean, on a branch, tagged
### ### v0.23; the test repair after the seal; appends to two ledgers; one line appended to data/act_roots.txt; the ζ page re-emitted;
### ### the intake`s full bank local and untracked, its summary committed; two prompts before the seal; no orphan at step zero.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b628_registration_2026-10-05.txt')
SPEC = os.path.join(ROOT, 'data', 'b628_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions: new versions, files uploaded, records created', 0, 0, 'actions', '### (Z): nothing deposits.'),
    ('platform calls of any kind (Zenodo)', 0, 0, 'calls', '### the head: nothing at Zenodo written or read.'),
    ('upstream repositories cloned at a pin, outside every repository the act writes', 1, 1, 'clones', '### (R238)(4): Zeta23 at 3635e748.'),
    ('upstream ls-remote reads', 1, 1, 'reads', '### Component 2: the tag v1.0 peeled at the remote, once.'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z): a docstring, no statement.'),
    ('existing kernel files edited', 1, 1, 'files', '### (R238)(4): SIDEExplicitFormula/Simplicity.lean, a docstring only.'),
    ('kernels of the federation written', 1, 1, 'kernels', '### (W): SIDE-explicit-formula.'),
    ('kernel files created', 0, 0, 'files', '### (Z).'),
    ('kernel tags made', 1, 1, 'tags', '### (R238)(4): v0.23 by push_gated.sh.'),
    ('kernel tags pushed', 1, 1, 'tags', '### (R238)(4).'),
    ('kernel branches made', 1, 1, 'branches', '### (W): cite-b628, pushed by name and kept; the push branch push-b628-kernel besides.'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('kernel README edits', 0, 0, 'edits', '### (W).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('build trees deleted', 0, 0, 'trees', '### (Z).'),
    ('clones deleted', 0, 0, 'clones', '### (Z).'),
    ('CORRESPONDENCE rows written', 0, 0, 'rows', '### (R238) orders none.'),
    ('grade names minted', 0, 0, 'grades', '### (Z).'),
    ('grades moved', 0, 0, 'grades', '### (R238)(4): the grade stays INTERFACES.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule clauses added to a shared instrument by the author`s ruling', 0, 0, 'clauses', '### (R238) orders none.'),
    ('correction entries written under the author`s ruling', 0, 0, 'entries', '### (R238) orders none.'),
    ('plan lines entered under the author`s ruling', 0, 0, 'lines', '### (R238) enters none; b629 is named on the trail record.'),
    ('priced items entered under the author`s ruling', 0, 0, 'items', '### (R238) orders none.'),
    ('standing lines entered under the author`s ruling', 1, 1, 'lines', '### (R238)(2): every test file run at step zero.'),
    ('word lines entered under the author`s ruling', 2, 2, 'lines', '### (R238)(3): the word at :12970 and at :12893.'),
    ('work-orders entered', 0, 0, 'work-orders', '### (R238) orders none in the ledgers; the intake`s lines live in its banks.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b627 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place', 1, 1, 'tools', '### (R238)(2): tools/test_chain_page_b596.py, after the seal through the Edit tool, committed alone.'),
    ('relay instruments created', 0, 0, 'tools', '### (W): none beyond the act`s own.'),
    ('own suite edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('own record-tool edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited other than the generated pages and the ledgers', 0, 0, 'documents', '### (Z).'),
    ('ANNEX, census or synthesis files written', 0, 0, 'files', '### (R238)(5).'),
    ('intake banks pushed in full', 0, 0, 'banks', '### the author`s answer before the seal: the full bank local, untracked.'),
    ('intake summary banks committed', 1, 1, 'banks', '### the author`s answer before the seal.'),
    ('edition files written', 0, 0, 'files', '### (R238) orders none.'),
    ('generated pages re-emitted', 1, 1, 'pages', '### Component 5: the ζ page at v0.23; the χ page unchanged unless its pin moves.'),
    ('mid-act pushes before the act root', 2, 2, 'pushes', '### relay and PLACE-papers by push_gated.sh, so each head the root names is at its remote.'),
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
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### (R238)(2): every test file under tools/, MEASURED off the bank.'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('questions asked of the author before the seal', 2, 2, 'questions', '### section (0): the intake bank`s publication, the document`s version.'),
    ('questions asked of the author after the seal', 0, 0, 'questions', '### none planned but the HOLD of Component 2, if it fires.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R238).'),
    ('PLACE-papers documents written other than by appending or regenerating', 0, 0, 'documents', '### (W).'),
    ('PLACE-papers documents written at all', 3, 3, 'documents', '### (W): FINDINGS, OPEN_TRAILS and the ζ page.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (W): none.'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('mirror zips built', 0, 0, 'zips', '### (Z): no mirror this act.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b628_arms_prerun.txt.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 8, 8, 'files', '### (W): the act`s own, the step-zero test runner among them.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b628_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b628_tests_stepzero.json'), encoding='utf-8')))
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
    spec = {"registration": ("data/b628_registration_2026-10-05.txt -- b628, LANE THREE ACT FIFTY-FIVE: THE 2/3 THEOREM`S AXIOM PROFILE IN "
                             "ITS OWN KERNEL, CITED AT two_thirds, v0.23; THE INTAKE PILOT; THE CARRIED TEST DEFECT REPAIRED, UNDER (R238)"),
            "clauses": clauses}
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
