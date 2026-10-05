# -*- coding: utf-8 -*-
"""b623_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **EVERY CLAUSE CARRIED FROM b622`s SPEC WAS RE-READ AGAINST THIS FACE** (b456`s error): nothing at Zenodo; one kernel
### ### written (its artefact module, on a branch, tagged v0.2.2), nine tags pushed as they stood and none moved; two shared relay tools
### ### edited by the author`s answer -- push_gated.sh and its test, after the seal, through the Edit tool -- and one record-tool edit by
### ### (R233)(3); appends to two ledgers -- FINDINGS (b622`s weight, the entry) and OPEN_TRAILS (the clause, the standing line, the
### ### work-orders, the record); REGISTRY`s dated row update; five housekeeping lists; two prompts, before the seal; both pages
### ### re-emitted from their banked probes; 62 table rows added, no table cell moved; no mirror built; no orphan at step zero.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b623_registration_2026-10-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b623_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions: new versions, files uploaded, records created', 0, 0, 'actions', '### (Z): nothing deposits.'),
    ('platform calls of any kind (Zenodo)', 0, 0, 'calls', '### the head: nothing at Zenodo written or read.'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z): no kernel declaration is edited.'),
    ('existing kernel files edited', 0, 0, 'files', '### (Z): the artefact is a new file; the build file is not edited.'),
    ('kernels of the federation written', 1, 1, 'kernels', '### (R233)(5)(b): SIDE-structural-error-correction, its artefact module alone.'),
    ('kernel files created', 1, 1, 'files', '### (R233)(5)(b): AxiomCheck.lean on the branch.'),
    ('kernel tags made', 1, 1, 'tags', '### (R233)(5)(b): v0.2.2, made by push_gated.sh at the read-back.'),
    ('kernel tags pushed as they stood', 12, 9, 'tags', '### (R233)(5)(a): the cited tags, one per call, by push_gated.sh`s existing-tag mode.'),
    ('kernel tags moved or re-pointed', 0, 0, 'tags', '### (R233)(5)(a).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('kernel branches made', 2, 2, 'branches', '### (R233)(5)(b): the artefact branch, kept, and its push branch, deleted by name after the read-back.'),
    ('kernel README edits', 0, 0, 'edits', '### (W).'),
    ('Lean calls made', 4, 4, 'calls', '### (R233)(5)(b): three module builds and the prints, each a detached call watched from the foreground.'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('build trees deleted', 0, 0, 'trees', '### (Z).'),
    ('clones deleted', 0, 0, 'clones', '### (Z).'),
    ('grades moved on a reading', 0, 0, 'grades', '### (Z): no grade moves.'),
    ('table grade cells moved by this act`s writes', 0, 0, 'cells', '### section (A): the ledger lines and REGISTRY`s note carry no grade word beside a backticked name.'),
    ('table rows added', 62, 62, 'rows', '### (R233)(5)(b): the de-alignment kernel`s declarations, each printed in the artefact.'),
    ('grade names minted', 0, 0, 'grades', '### (Z).'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule clauses added by the author`s ruling', 1, 1, 'clauses', '### (R233)(2): the bundle clause, appended to OPEN_TRAILS addressed to :12266.'),
    ('plan lines entered under the author`s ruling', 0, 0, 'lines', '### (R233) enters none; b624 is named on the trail record.'),
    ('relay lists opened under the author`s ruling', 5, 5, 'lists', '### (R233)(5)(a) and the author`s answer: five kernels` housekeeping lists created.'),
    ('standing lines entered under the author`s ruling', 1, 1, 'lines', '### (R233)(3): the test count, appended to OPEN_TRAILS addressed to :12799.'),
    ('work-orders entered', 4, 4, 'work-orders', '### (R233)(4): PLATT-RUNG, NYMAN-BEURLING-FACE, DEDEKIND-INSTANCE, MARGIN-BENCH, priced, not started.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b622 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place', 2, 2, 'tools', '### the author`s answer before the seal: tools/push_gated.sh and tools/test_push_gated.sh, after the seal, through the Edit tool, committed alone.'),
    ('own suite edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('own record-tool edits after the seal under the author`s ruling', 1, 1, 'edits', '### (R233)(3): count_cases, through the Edit tool, with its test, committed alone after the tool as sealed.'),
    ('tier lines re-read under the author`s ruling', 0, 0, 'lines', '### (R233) orders none; b557`s tier bank is re-read, no tier moved.'),
    ('living documents given a dated append under the author`s ruling', 0, 0, 'appends', '### (R233) orders none; REGISTRY`s row update is its own clause.'),
    ('README dated appends under the author`s ruling', 0, 0, 'appends', '### (R233) orders none.'),
    ('reader packets written in relay', 0, 0, 'packets', '### (R233): no packet this act.'),
    ('reader banks written by a session the author opens', 0, 0, 'banks', '### (R233): none.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z): the current versions, the census and SPIRAL_MAP are not edited.'),
    ('existing documents edited other than the generated pages and the two ledgers', 1, 1, 'documents', '### (W): REGISTRY alone, by its dated row update, (R233)(5)(a).'),
    ('back-matter cells of existing documents re-pinned', 0, 0, 'cells', '### (Z).'),
    ('edition files written', 0, 0, 'files', '### (R233) orders none.'),
    ('synthesis rows re-graded', 0, 0, 'rows', '### (R233) orders none.'),
    ('residue sentences of other documents written in this act', 0, 0, 'sentences', '### (R233) orders none.'),
    ('work-list items entered', 0, 0, 'items', '### (R233) orders none.'),
    ('relay work-list files written', 0, 0, 'files', '### (R233) orders none.'),
    ('generated pages re-emitted', 2, 2, 'pages', '### Component 4: both, from their banked probes, after the kernel tag, each written only if it differs.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z): ERRATA untouched.'),
    ('ERRATA dated lines appended', 0, 0, 'lines', '### (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('TECHNE-Core pushes', 0, 0, 'pushes', '### (Z).'),
    ('README.md or SPIRAL_MAP.md edits', 0, 0, 'edits', '### (Z): README and SPIRAL_MAP untouched.'),
    ('REGISTRY.md appends', 1, 1, 'appends', '### (R233)(5)(a): one dated row update in REGISTRY`s own form, committed alone.'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('addendum lines written', 0, 0, 'lines', '### (Z): no (R177) addendum line; the seven work-list addenda are relay files of the b558 form.'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('questions asked of the author before the seal', 2, 2, 'questions', '### section (0): how the cited tags are pushed and what a citation is, which the ruling`s letter and the precedence order do not reach (b623_author_answers.txt).'),
    ('questions asked of the author after the seal', 0, 0, 'questions', '### none.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R233).'),
    ('PLACE-papers documents written other than by appending, regenerating or creating an edition', 0, 0, 'documents', '### (W): REGISTRY by appending.'),
    ('PLACE-papers documents written at all', 5, 3, 'documents', '### (W): FINDINGS, OPEN_TRAILS, REGISTRY; each page only if its re-emission differs.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (W): none.'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z): no existing document is edited.'),
    ('mirror zips built', 0, 0, 'zips', '### (Z): no mirror this act; the refresh is the consolidation`s sixth act.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b623_arms_prerun.txt.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 7, 7, 'files', '### (W): the act`s own, the count test among them.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b623_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    measured = dict(
        ARMS=count_arms(text),
        READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
        EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)),
        BARS=len(re.findall(r'^### BAR \d+', text, re.M)),
    )
    print()
    print('  ### ### **MEASURED OFF THE FACE, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS'):
        print('      %-9s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b623_registration_2026-10-04.txt -- b623, LANE THREE ACT FIFTY: THE UNPUSHED TAGS SETTLED BY CITATION, "
                             "THE DE-ALIGNMENT KERNEL`S AXIOM ARTEFACT PRINTED AND ITS ROWS ENTERED, FOUR WORK-ORDERS AND ONE ARM, UNDER (R233)"),
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
