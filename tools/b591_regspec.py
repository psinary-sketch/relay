# -*- coding: utf-8 -*-
"""b591_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **EVERY CLAUSE CARRIED FROM b590`s SPEC WAS RE-READ AGAINST THIS FACE** (b456`s error): nothing at Zenodo; no
### ### kernel written; one relay instrument edited (the E0 rule, by (R201)(3)) and one test created; no worktree; no prior
### ### bank edited; appends to two ledgers; one TECHNE-Core file created and committed locally, not pushed; no edition.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b591_registration_2026-10-02.txt')
SPEC = os.path.join(ROOT, 'data', 'b591_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions: new versions, files uploaded, records created', 0, 0, 'actions', '### (Z): nothing deposits.'),
    ('platform calls of any kind (Zenodo)', 0, 0, 'calls', '### the head: nothing at Zenodo written or read.'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z).'),
    ('existing kernel files edited', 0, 0, 'files', '### (Z).'),
    ('kernels of the federation written', 0, 0, 'kernels', '### (Z): no kernel is written.'),
    ('kernel tags made', 0, 0, 'tags', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('kernel branches made', 0, 0, 'branches', '### (Z).'),
    ('kernel README edits', 0, 0, 'edits', '### (W).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('build trees deleted', 0, 0, 'trees', '### (Z).'),
    ('clones deleted', 0, 0, 'clones', '### (Z).'),
    ('grades moved on a reading', 0, 0, 'grades', '### (Z): the re-grade corrects a reading; no grade cell moves.'),
    ('grade names minted', 0, 0, 'grades', '### (Z).'),
    ('claims about RH, GRH, h2, BSD, Navier-Stokes, twin primes, P versus NP or any zero beyond a compiled statement', 0, 0, 'claims',
     '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule clauses added by the author`s ruling', 1, 1, 'clauses', '### reading (iii): the E0 rule`s existential-binder clause, (R201)(3).'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### reading (iv): the struck clauses are the author`s, recorded.'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b590 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place', 1, 1, 'tools', '### reading (iii): tools/e0_rule.py, the ruled clause, through the Edit tool.'),
    ('keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited', 0, 0, 'documents', '### (Z).'),
    ('edition files written', 0, 0, 'files', '### (W): none.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core files created', 1, 1, 'files', '### reading (iv): the document, beside the b257 drafts.'),
    ('TECHNE-Core commits made', 1, 1, 'commits', '### reading (iv): the document alone, local.'),
    ('TECHNE-Core pushes', 0, 0, 'pushes', '### reading (iv): not pushed.'),
    ('README.md, REGISTRY.md, ERRATA.md or SPIRAL_MAP.md edits', 0, 0, 'edits', '### (W).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('addendum lines written', 0, 0, 'lines', '### (Z).'),
    ('body sentences of the document written to relay, PLACE-papers or SIDE-global-section', 0, 0, 'sentences', '### reading (iv), (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('questions asked of the author before the seal', 1, 1, 'questions', '### section (0), reading (iv).'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0): the step-zero deletions declared.'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R201).'),
    ('PLACE-papers documents written other than by appending', 0, 0, 'documents', '### (W): none.'),
    ('PLACE-papers documents written at all', 2, 2, 'documents', '### (W): FINDINGS, OPEN_TRAILS.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### reading (iv): the document is not placed in PLACE-papers.'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('mirror zips built', 0, 0, 'zips', '### (W).'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 6, 6, 'files', '### (W): the act`s six, the test among them.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]

def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b591_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    # ### ### **THE FACE-DERIVED CLAUSES ARE MEASURED, NOT TYPED (b488's routed finding).**
    # ### b488 found two carried clauses contradicting its own SEALED face -- one capping tool
    # ### edits at zero while the face named one, one declaring eight bars where the face had no
    # ### (K) section at all -- and nothing caught them, because the demands are TYPED. ###
    # ### **A CLAUSE THAT CANNOT BE FALSIFIED BY ITS OWN FACE IS NOT A BOUND.** ### Every clause
    # ### whose subject IS the face is now read off the face.
    ext = ''
    try:
        ext = io.open(os.path.join(ROOT, 'data', 'b591_extract.txt'),
                      encoding='utf-8', errors='replace').read()
    except Exception:
        pass
    measured = dict(
        ARMS=count_arms(text),
        # ### DISTINCT readings DECLARED, not every mention: a reading referred to from a
        # ### later paragraph is the same reading, and counting mentions inflated it to 10.
        READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
        EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)),
        BARS=len(re.findall(r'^### BAR \d+', text, re.M)),
        PREFACE=len(re.findall(r'^\(P(\d+)\)', ext, re.M)),
    )
    print()
    print('  ### ### **MEASURED OFF THE FACE, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'PREFACE'):
        print('      %-9s %d' % (k, measured[k]))

    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b591_registration_2026-10-02.txt -- b591, LANE THREE ACT EIGHTEEN: THE LOCATED-CLAUSE METHOD DOCUMENT; THE WITNESS RATIO AT DETECTION-REGION; THE E0 RULE`S EXISTENTIAL-BINDER CLAUSE, UNDER (R201)"),
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
