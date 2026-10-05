# -*- coding: utf-8 -*-
"""b622_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **EVERY CLAUSE CARRIED FROM b621`s SPEC WAS RE-READ AGAINST THIS FACE** (b456`s error): nothing at Zenodo; no kernel
### ### written, tagged or branched; two shared relay tools edited by the ruling -- the generator and its test, after the seal, through
### ### the Edit tool -- and no suite or record-tool edit after the seal; appends to two ledgers -- FINDINGS (b621`s weight, the entry)
### ### and OPEN_TRAILS (the offer, the record); README`s dated append; one edition created beside its current version; the 39
### ### sentences entered in fourteen relay work-list files; one prompt, before the seal; both pages re-emitted from their banked probes,
### ### twice; no table cell moved; no mirror built; no orphan at step zero.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b622_registration_2026-10-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b622_satisfiable.json')

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
    ('Lean calls made', 0, 0, 'calls', '### readings (vii)-(viii): both pages from their banked probes.'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('build trees deleted', 0, 0, 'trees', '### (Z).'),
    ('clones deleted', 0, 0, 'clones', '### (Z).'),
    ('grades moved on a reading', 0, 0, 'grades', '### (Z): no grade moves.'),
    ('table grade cells moved by this act`s writes', 0, 0, 'cells', '### section (A): the ledger lines carry no grade word beside a backticked name; the edition is no ledger.'),
    ('grade names minted', 0, 0, 'grades', '### (Z).'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule clauses added by the author`s ruling', 1, 1, 'clauses', '### (R232)(1): the offer taken, appended to OPEN_TRAILS addressed to the form`s clause :12839.'),
    ('plan lines entered under the author`s ruling', 0, 0, 'lines', '### (R232) enters none; b623 is named on the trail record.'),
    ('relay lists opened under the author`s ruling', 0, 0, 'lists', '### none.'),
    ('standing lines entered under the author`s ruling', 0, 0, 'lines', '### (R232) enters none.'),
    ('work-orders entered', 0, 0, 'work-orders', '### (R232) enters none; it lands W-ORD-QUANTIFIER-COLUMN with DENSITY.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b621 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place', 2, 2, 'tools', '### (R232)(4): tools/chain_page.py and tools/test_chain_page_b596.py, after the seal, through the Edit tool, committed alone.'),
    ('own suite edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('own record-tool edits after the seal under the author`s ruling', 0, 0, 'edits', '### (Z): none.'),
    ('tier lines re-read under the author`s ruling', 0, 0, 'lines', '### (R232) orders none.'),
    ('living documents given a dated append under the author`s ruling', 0, 0, 'appends', '### (R232) orders none; README`s append is its own clause.'),
    ('README dated appends under the author`s ruling', 1, 1, 'appends', '### (R232)(3): one paragraph beside the (R183)(3) sentence and the live-line refresh, committed alone.'),
    ('reader packets written in relay', 0, 0, 'packets', '### (R232): no packet this act.'),
    ('reader banks written by a session the author opens', 0, 0, 'banks', '### (R232): none.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z): the current versions, the census, REGISTRY and SPIRAL_MAP are not edited; the editions are new files beside them.'),
    ('existing documents edited other than the generated pages and the two ledgers', 1, 1, 'documents', '### (W): README alone, by (R232)(3).'),
    ('back-matter cells of existing documents re-pinned', 0, 0, 'cells', '### (Z): the carried back matter is re-pinned inside v0.6, a new file; no existing document`s cell moves.'),
    ('edition files written', 1, 1, 'files', '### (R232)(4): the sieve`s v0.6 beside v0.5.'),
    ('synthesis rows re-graded', 0, 0, 'rows', '### (R232) orders none.'),
    ('residue sentences of other documents written in this act', 0, 0, 'sentences', '### (R232)(2): entered as work-list items, no document written.'),
    ('work-list items entered', 39, 39, 'items', '### (R232)(2): OPEN_TRAILS :12851`s sentences, in their documents` b558 work-lists and in addenda beside them.'),
    ('relay work-list files written', 14, 14, 'files', '### (R232)(2): seven work-lists appended, seven addenda created, relay data/b558_editions/.'),
    ('generated pages re-emitted', 2, 2, 'pages', '### readings (vii)-(viii): both, from their banked probes, with the column and again after v0.6, each written only if it differs.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z): ERRATA untouched.'),
    ('ERRATA dated lines appended', 0, 0, 'lines', '### (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('TECHNE-Core pushes', 0, 0, 'pushes', '### (Z).'),
    ('README.md or SPIRAL_MAP.md edits', 1, 1, 'edits', '### (W): README`s dated append and refresh, one commit; SPIRAL_MAP untouched.'),
    ('REGISTRY.md appends', 0, 0, 'appends', '### (Z): REGISTRY unedited.'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('addendum lines written', 0, 0, 'lines', '### (Z): no (R177) addendum line; the seven work-list addenda are relay files of the b558 form.'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('questions asked of the author before the seal', 1, 1, 'questions', '### section (0): the one prompt on an object node`s shape cell, which the ruling`s letter and the precedence order do not reach (b622_author_answers.txt).'),
    ('questions asked of the author after the seal', 0, 0, 'questions', '### none.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R232).'),
    ('PLACE-papers documents written other than by appending, regenerating or creating an edition', 1, 1, 'documents', '### (W): README, its dated append and refresh by (R232)(3).'),
    ('PLACE-papers documents written at all', 6, 4, 'documents', '### (W): FINDINGS, OPEN_TRAILS, README, the sieve`s v0.6; each page only if its re-emission differs.'),
    ('PLACE-papers documents created', 1, 1, 'documents', '### (W): the sieve`s v0.6; none retired.'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z): no existing document is edited.'),
    ('mirror zips built', 0, 0, 'zips', '### (Z): no mirror this act; the refresh is the consolidation`s sixth act.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b622_arms_prerun.txt.'),
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
    print('b622_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b622_registration_2026-10-04.txt -- b622, LANE THREE ACT FORTY-NINE: THE QUANTIFIER COLUMN, THE PAGES "
                             "RE-EMITTED, THE SIEVE`S HAND MARKS REPLACED, README`S SUPPORTABLE SENTENCE, THE 39 SENTENCES ENTERED, UNDER (R232)"),
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
