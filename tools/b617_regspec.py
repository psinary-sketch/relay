# -*- coding: utf-8 -*-
"""b617_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **EVERY CLAUSE CARRIED FROM b616`s SPEC WAS RE-READ AGAINST THIS FACE** (b456`s error): nothing at Zenodo; no kernel
### ### written, tagged or branched; no shared relay tool edited, no suite edit after the seal; appends to three ledgers -- FINDINGS
### ### (b616`s weight, the entry), OPEN_TRAILS (the 2G fact items, the living documents` currency, the record) and ERRATA (three
### ### entries); one edition file created beside v0.4, no existing document edited; both pages re-emitted from their banked probes; no
### ### mirror built; no orphan at step zero; no prompt before the seal.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b617_registration_2026-10-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b617_satisfiable.json')

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
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('kernel branches made', 0, 0, 'branches', '### (Z).'),
    ('kernel README edits', 0, 0, 'edits', '### (W).'),
    ('Lean calls made', 0, 0, 'calls', '### reading (x): both pages from their banked probes.'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('build trees deleted', 0, 0, 'trees', '### (Z).'),
    ('clones deleted', 0, 0, 'clones', '### (Z).'),
    ('grades moved on a reading', 0, 0, 'grades', '### (Z): the edition reads its own rows` verdicts; it grades nothing in the table.'),
    ('grade names minted', 0, 0, 'grades', '### (Z).'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule clauses added by the author`s ruling', 0, 0, 'clauses', '### (R227) adds none.'),
    ('plan lines entered under the author`s ruling', 2, 2, 'lines', '### Component 1: the 2G fact items (R227)(2); the living documents` currency, b618, (R227)(3).'),
    ('relay lists opened under the author`s ruling', 0, 0, 'lists', '### Component 1: none.'),
    ('standing lines entered under the author`s ruling', 0, 0, 'lines', '### (R227) enters none.'),
    ('work-orders entered', 0, 0, 'work-orders', '### (R227) enters none.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b616 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place', 0, 0, 'tools', '### (Z): no shared tool.'),
    ('own suite edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('tier lines re-read under the author`s ruling', 0, 0, 'lines', '### (R227) orders none.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z): the sieve`s earlier versions, the six syntheses, the 2G papers, the living documents, the census and SPIRAL_MAP are not edited.'),
    ('existing documents edited other than the generated pages and the three ledgers', 0, 0, 'documents', '### (W): FINDINGS, OPEN_TRAILS and ERRATA, appended only.'),
    ('back-matter cells of existing documents re-pinned', 0, 0, 'cells', '### (Z): the carried back-matter cells are re-pinned in v0.5, the new file; no existing document`s cell moves.'),
    ('edition files written', 1, 1, 'files', '### reading (iv): phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md beside v0.4.'),
    ('generated pages re-emitted', 2, 2, 'pages', '### reading (x): both, from their banked probes, each written only if it differs.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 3, 3, 'entries', '### (R227)(2): three, through tools/errata_append.py, committed alone.'),
    ('ERRATA dated lines appended', 0, 0, 'lines', '### (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('TECHNE-Core pushes', 0, 0, 'pushes', '### (Z).'),
    ('README.md, REGISTRY.md or SPIRAL_MAP.md edits', 0, 0, 'edits', '### (W).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('addendum lines written', 0, 0, 'lines', '### (Z): no addendum this act.'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('questions asked of the author before the seal', 0, 0, 'questions', '### section (0): none; the precedence order reached every reading.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R227).'),
    ('PLACE-papers documents written other than by appending, regenerating or the edition beside', 0, 0, 'documents', '### (Z).'),
    ('PLACE-papers documents written at all', 6, 4, 'documents', '### (W): FINDINGS, OPEN_TRAILS, ERRATA, the edition; each page only if its re-emission differs.'),
    ('PLACE-papers documents created', 1, 1, 'documents', '### (W): the edition file alone.'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z): no existing document is edited.'),
    ('mirror zips built', 0, 0, 'zips', '### (Z): no mirror this act; the refresh is the consolidation`s sixth act.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b617_arms_prerun.txt.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 6, 6, 'files', '### (W): the act`s own.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    """### **AN ARM IS AN ARM WHATEVER LETTER ITS FAMILY USES** -- `b413`'s counter, carried."""
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b617_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b617_registration_2026-10-04.txt -- b617, LANE THREE ACT FORTY-FOUR: THE SIEVE AT v0.5, THE TEN "
                             "CONCLUSIONS AS ROWS; THE 2G FINDINGS AND THREE ERRATA; THE LIVING DOCUMENTS` CURRENCY ENTERED FOR b618, UNDER (R227)"),
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
