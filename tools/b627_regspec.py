# -*- coding: utf-8 -*-
"""b627_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Written whole from b626`s spec, every clause re-read against this face: nothing at Zenodo; no kernel touched and no Lean
### ### call; SIDE-global-section`s CORRESPONDENCE gains one row by relay tools/corr_row.py; the generator and its test edited after the
### ### seal, and this act`s closing tool`s carried section; appends to two ledgers; one line appended to data/act_roots.txt; both pages
### ### re-emitted where they differ; the zero table read once; the bench run twice; three prompts before the seal; no MANIFEST written
### ### and no mirror built; no orphan at step zero, the seat`s own stopped search`s children stopped by PID before the seal.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b627_registration_2026-10-05.txt')
SPEC = os.path.join(ROOT, 'data', 'b627_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions: new versions, files uploaded, records created', 0, 0, 'actions', '### (Z): nothing deposits.'),
    ('platform calls of any kind (Zenodo)', 0, 0, 'calls', '### the head: nothing at Zenodo written or read.'),
    ('zero tables read', 1, 1, 'reads', '### Component 3: Odlyzko`s zeros2, read once, its URL and count printed.'),
    ('publisher pages read', 0, 0, 'reads', '### (R237) orders none.'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z).'),
    ('existing kernel files edited', 0, 0, 'files', '### (Z): no kernel touched.'),
    ('kernels of the federation written', 1, 1, 'kernels', '### (W): SIDE-global-section (one CORRESPONDENCE row).'),
    ('kernel files created', 0, 0, 'files', '### (Z).'),
    ('kernel tags made', 0, 0, 'tags', '### (Z).'),
    ('kernel tags pushed', 0, 0, 'tags', '### (Z).'),
    ('Lean calls', 0, 0, 'calls', '### the ferry: no Lean build this act.'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('kernel branches made', 0, 0, 'branches', '### (Z).'),
    ('kernel README edits', 0, 0, 'edits', '### (W).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('build trees deleted', 0, 0, 'trees', '### (Z).'),
    ('clones deleted', 0, 0, 'clones', '### (Z).'),
    ('CORRESPONDENCE rows written', 1, 1, 'rows', '### (R237)(2): the seam equivalence`s, superseding row 383.'),
    ('grade names minted', 0, 0, 'grades', '### (Z).'),
    ('shape words entered by the author`s ruling', 1, 1, 'words', '### (R237)(3): BOUNDED.'),
    ('claims about RH or any zero not in the table', 0, 0, 'claims', '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule clauses added to a shared instrument by the author`s ruling', 1, 1, 'clauses', '### (R237)(3): the BOUNDED reading in the generator.'),
    ('correction entries written under the author`s ruling', 2, 2, 'entries', '### (R237)(2): the OPEN_TRAILS directive and the CORRESPONDENCE row.'),
    ('plan lines entered under the author`s ruling', 0, 0, 'lines', '### (R237) enters none; b628 is named on the trail record.'),
    ('priced items entered under the author`s ruling', 0, 0, 'items', '### (R237) orders none.'),
    ('relay lists opened under the author`s ruling', 0, 0, 'lists', '### (R237): none.'),
    ('standing lines entered under the author`s ruling', 1, 1, 'lines', '### (R237)(4): the closing form.'),
    ('work-orders entered', 0, 0, 'work-orders', '### (R237) orders none.'),
    ('readings re-printed beside their clauses', 0, 0, 'readings', '### (R237) orders none.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b626 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place', 2, 2, 'tools', '### (R237)(3): tools/chain_page.py and tools/test_chain_page_b596.py, after the seal through the Edit tool, committed alone.'),
    ('relay instruments created', 0, 0, 'tools', '### (W): none beyond the act`s own.'),
    ('own suite edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none; the suite`s repair is Component 0`s, before the seal.'),
    ('own record-tool edits after the seal under the author`s ruling', 1, 1, 'edits', '### (R237)(4): tools/b627_closing.py`s carried section, through the Edit tool, committed alone.'),
    ('tier lines re-read under the author`s ruling', 0, 0, 'lines', '### (R237) orders none.'),
    ('living documents given a dated append under the author`s ruling', 0, 0, 'appends', '### (R237) orders none.'),
    ('README dated appends under the author`s ruling', 0, 0, 'appends', '### (R237) orders none.'),
    ('reader packets written in relay', 0, 0, 'packets', '### (R237): none.'),
    ('reader banks written by a session the author opens', 0, 0, 'banks', '### (R237): none.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited other than the generated pages and the ledgers', 0, 0, 'documents', '### (Z).'),
    ('back-matter cells of existing documents re-pinned', 0, 0, 'cells', '### (Z).'),
    ('edition files written', 0, 0, 'files', '### (R237) orders none.'),
    ('synthesis rows re-graded', 0, 0, 'rows', '### (R237) orders none.'),
    ('work-list items entered', 1, 1, 'items', '### (R237)(3): the sieve`s shape column at its next version.'),
    ('generated pages re-emitted', 2, 2, 'pages', '### Component 2: each written only where it differs.'),
    ('bench runs', 2, 2, 'runs', '### Component 4: the run and its byte-for-byte repetition, each in the foreground in batches.'),
    ('mid-act pushes before the act root', 3, 3, 'pushes', '### relay, PLACE-papers and SIDE-global-section by push_gated.sh, so each head the root names is at its remote.'),
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
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('child processes of the seat`s own stopped search stopped by PID before the seal', 2, 2, 'processes', '### section (0): grep 2356 and head 34588.'),
    ('questions asked of the author before the seal', 3, 3, 'questions', '### section (0): the fit, the window, the certification (b627_author_answers.txt).'),
    ('questions asked of the author after the seal', 0, 0, 'questions', '### none planned.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R237).'),
    ('PLACE-papers documents written other than by appending or regenerating', 0, 0, 'documents', '### (W).'),
    ('PLACE-papers documents written at all', 4, 4, 'documents', '### (W): FINDINGS, OPEN_TRAILS and both pages.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (W): none.'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 1, 1, 'files', '### (W): CORRESPONDENCE.md, one row appended by the row writer.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('mirror zips built', 0, 0, 'zips', '### (Z): no mirror this act.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b627_arms_prerun.txt.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 7, 7, 'files', '### (W): the act`s own, the bench script among them.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b627_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)))
    print()
    print('  ### ### **MEASURED OFF THE FACE, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS'):
        print('      %-9s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b627_registration_2026-10-05.txt -- b627, LANE THREE ACT FIFTY-FOUR: THE POSITIVITY MARGIN AT HEIGHT; "
                             "THE SEAM EQUIVALENCE RULED; THE BOUNDED SHAPE; THE CLOSING FORM AMENDED, UNDER (R237)"), "clauses": clauses}
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
