# -*- coding: utf-8 -*-
"""b624_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Written whole from b623`s spec, every clause re-read against this face (b456`s error): nothing at Zenodo; no kernel touched and
### ### no Lean call; one shared relay tool edited by the ruling -- the E0 rule with its test, after the seal, through the Edit tool --
### ### and one created, act_root.py with its test; appends to two ledgers -- FINDINGS (b623`s weight, the entry) and OPEN_TRAILS (the
### ### five readings, the MANIFEST line, the record); data/act_roots.txt begun; the χ page re-emitted where it differs; one relay push
### ### and one PLACE-papers push before the root, besides the closing`s; three prompts before the seal; no table cell moved; no
### ### MANIFEST written and no mirror built; no orphan at step zero.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b624_registration_2026-10-05.txt')
SPEC = os.path.join(ROOT, 'data', 'b624_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions: new versions, files uploaded, records created', 0, 0, 'actions', '### (Z): nothing deposits.'),
    ('platform calls of any kind (Zenodo)', 0, 0, 'calls', '### the head: nothing at Zenodo written or read.'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z): no kernel touched.'),
    ('existing kernel files edited', 0, 0, 'files', '### (Z).'),
    ('kernels of the federation written', 0, 0, 'kernels', '### (Z): no kernel touched.'),
    ('kernel files created', 0, 0, 'files', '### (Z).'),
    ('kernel tags made', 0, 0, 'tags', '### (Z).'),
    ('kernel tags pushed', 0, 0, 'tags', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('kernel branches made', 0, 0, 'branches', '### (Z).'),
    ('kernel README edits', 0, 0, 'edits', '### (W).'),
    ('Lean calls made', 0, 0, 'calls', '### the ferry: this act runs no Lean build; the headers are read from the kernels by git and the pages from their banked probes.'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('build trees deleted', 0, 0, 'trees', '### (Z).'),
    ('clones deleted', 0, 0, 'clones', '### (Z).'),
    ('grades moved on a reading', 0, 0, 'grades', '### (Z): no ledger grade moves; the rule`s read of one node moves, printed beside the table`s.'),
    ('table grade cells moved by this act`s writes', 0, 0, 'cells', '### section (A): the ledger lines carry no grade word beside a backticked name.'),
    ('table rows added', 0, 0, 'rows', '### H58c: the table`s diff expected empty.'),
    ('grade names minted', 0, 0, 'grades', '### (Z): ENCODES-CONCLUSION is the taxonomy`s grade, now an outcome of the rule.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule clauses added to a shared instrument by the author`s ruling', 3, 3, 'clauses', '### (R234)(2) and the answers: the statement`s binders alone, the non-membership, the conclusion as a binder.'),
    ('plan lines entered under the author`s ruling', 0, 0, 'lines', '### (R234) enters none; b625 is named on the trail record.'),
    ('relay lists opened under the author`s ruling', 1, 1, 'lists', '### (R234)(3): data/act_roots.txt, begun with b624`s line.'),
    ('standing lines entered under the author`s ruling', 1, 1, 'lines', '### the author`s answer: the act root in MANIFEST at every mirror build, appended to OPEN_TRAILS addressed to :12210.'),
    ('work-orders entered', 0, 0, 'work-orders', '### (R234) enters none; it lands W-ORD-E0-INDUCTION and W-ORD-ACT-ROOT.'),
    ('readings re-printed beside their clauses', 5, 5, 'readings', '### (R234)(1): b623`s five, each as printed, each its own line.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b623 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place', 2, 2, 'tools', '### (R234)(2): tools/e0_rule.py and tools/test_e0_rule.py, after the seal, through the Edit tool, committed alone.'),
    ('relay instruments created', 2, 2, 'tools', '### (R234)(3): tools/act_root.py and tools/test_act_root.py, through the Write tool, committed alone.'),
    ('own suite edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('own record-tool edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('tier lines re-read under the author`s ruling', 0, 0, 'lines', '### (R234) orders none.'),
    ('living documents given a dated append under the author`s ruling', 0, 0, 'appends', '### (R234) orders none.'),
    ('README dated appends under the author`s ruling', 0, 0, 'appends', '### (R234) orders none.'),
    ('reader packets written in relay', 0, 0, 'packets', '### (R234): none.'),
    ('reader banks written by a session the author opens', 0, 0, 'banks', '### (R234): none.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited other than the generated pages and the two ledgers', 0, 0, 'documents', '### (Z): REGISTRY, README and the rest untouched.'),
    ('back-matter cells of existing documents re-pinned', 0, 0, 'cells', '### (Z).'),
    ('edition files written', 0, 0, 'files', '### (R234) orders none.'),
    ('synthesis rows re-graded', 0, 0, 'rows', '### (R234) orders none.'),
    ('work-list items entered', 0, 0, 'items', '### (R234) orders none.'),
    ('generated pages re-emitted', 2, 1, 'pages', '### Component 3: the χ page, and the ζ page by the page arms` reading; each written only if it differs.'),
    ('planted scratch modules written', 2, 2, 'modules', '### (R234)(2): under the scratchpad, by the test, their absolute paths printed.'),
    ('mid-act pushes before the act root', 2, 2, 'pushes', '### Component 4: relay and PLACE-papers by push_gated.sh, so each head the root names is at its remote.'),
    ('MANIFEST lines written', 0, 0, 'lines', '### the author`s answer: none this act; the standing line governs the next mirror build.'),
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
    ('questions asked of the author before the seal', 3, 3, 'questions', '### section (0): the non-membership, the ENCODES outcome, the MANIFEST line (b624_author_answers.txt).'),
    ('questions asked of the author after the seal', 0, 0, 'questions', '### none.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R234).'),
    ('PLACE-papers documents written other than by appending or regenerating', 0, 0, 'documents', '### (W).'),
    ('PLACE-papers documents written at all', 4, 2, 'documents', '### (W): FINDINGS, OPEN_TRAILS; each page only if its re-emission differs.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (W): none.'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('mirror zips built', 0, 0, 'zips', '### (Z): no mirror this act.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b624_arms_prerun.txt; the act-root arm a source, not declared.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 8, 8, 'files', '### (W): the act`s own six, act_root.py and its test.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b624_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b624_registration_2026-10-05.txt -- b624, LANE THREE ACT FIFTY-ONE: THE E0 GATE`S READING OF INDUCTION "
                             "STEPS, WITH ITS TEST AND THE CHI PAGE RE-EMITTED; THE ACT ROOT CHAINED FROM THIS ACT, UNDER (R234)"),
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
