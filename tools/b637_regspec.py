# -*- coding: utf-8 -*-
"""b637_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b636's spec, every clause re-written against this face: nothing at Zenodo and nothing deposited; no kernel source
### ### written and nothing built; the rule rewritten with its tests, the generator edited with its test and the roster edited, each after
### ### the seal and committed alone; the table regenerated; no README append; no mirror; no question before the seal.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b637_registration_2026-10-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b637_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('deposit actions: new versions, files uploaded, records created', 0, 0, 'actions', '### (Z): nothing deposits.'),
    ('platform calls of any kind (Zenodo)', 0, 0, 'calls', '### the head: nothing at Zenodo written or read.'),
    ('registry records read', 0, 0, 'reads', '### (R247) orders none.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### (R240)(2)(i), standing; the ferry`s N5.'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z): no kernel source touched.'),
    ('existing kernel files edited', 0, 0, 'files', '### (Z).'),
    ('kernels of the federation written', 0, 0, 'kernels', '### (Z): no kernel source touched.'),
    ('kernel files created', 0, 0, 'files', '### (Z).'),
    ('kernel tags made', 0, 0, 'tags', '### (Z).'),
    ('kernel tags pushed', 0, 0, 'tags', '### (Z).'),
    ('kernel branches made', 0, 0, 'branches', '### (Z).'),
    ('module builds by the standing route', 0, 0, 'builds', '### the ferry: nothing is built this act.'),
    ('closure builds run in parallel under the hold', 0, 0, 'builds', '### OPEN_TRAILS :13067.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### the readers read the banks; the planted declarations are read as text, never built.'),
    ('calls made with any token', 0, 0, 'calls', '### (Z).'),
    ('fresh probe runs of the page generator', 0, 0, 'runs', '### the pages re-emit from b632`s lists and b635`s banked probes.'),
    ('second-reader sessions launched by the seat', 0, 0, 'sessions', '### (R247) orders no reader this act.'),
    ('ls-remote reads of a repository beyond its one', 0, 0, 'reads', '### the ferry; root verifies inside the suite alone.'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('CORRESPONDENCE rows written', 0, 0, 'rows', '### (R247) orders none.'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z): a binder reaching no class raises and is printed as a bug, never a grade.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('binder classes in the classification', 26, 26, 'classes', '### (R247)(4)(i): kind × typing × form, MEASURED off the prototype before the seal.'),
    ('planted declarations whose expectation is fixed after a reading', 0, 0, 'declarations', '### (R247)(4)(i): fixed in the bank before any reading.'),
    ('table rows whose grade moves under the rewritten rule', 1801, 0, 'rows', '### (R247)(4)(iii): at most the graded rows, MEASURED at Component 4.'),
    ('table rows made a kind and not a grade', 32, 32, 'rows', '### (R247)(2): the 27 the upstream mark reaches and the five Mathlib names.'),
    ('table rows retired', 0, 0, 'rows', '### (R247) orders none.'),
    ('correction entries written under the author`s ruling', 0, 0, 'entries', '### (R247) orders none.'),
    ('standing lines entered under the author`s ruling', 2, 2, 'lines', '### (R247)(2)-(3): the upstream clause and the name clause beneath :12955.'),
    ('amendments entered to a standing form', 0, 0, 'amendments', '### (R247) orders none.'),
    ('items entered', 0, 0, 'items', '### (R247) orders none.'),
    ('work-orders entered', 0, 0, 'work-orders', '### (R247) orders none.'),
    ('weight lines entered', 1, 1, 'lines', '### (R247)(1): b636 at its weight.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b636 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place under the author`s ruling', 5, 5, 'tools', '### (R247)(4)-(5): e0_rule.py and its two tests, terminal_table.py, mirror_roster.json.'),
    ('relay instruments created', 1, 1, 'tools', '### (W): the generator`s test, test_terminal_table_b637.py.'),
    ('relay data files written outside the act`s own names', 0, 0, 'files', '### (W): every bank is b637_* but the regenerated table and the roots line.'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307: sealed means unedited by any means.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### OPEN_TRAILS :13307: G-SEAL-HASHES.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited other than the generated pages and the ledgers', 0, 0, 'documents', '### (Z).'),
    ('census files written', 0, 0, 'files', '### (R247)(4)(v): the counts banked for v0.6, no census edition.'),
    ('ANNEX or synthesis files written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### b628`s full bank stays untracked.'),
    ('generated pages re-emitted', 2, 0, 'pages', '### Component 5: each only where a cell moves.'),
    ('mid-act pushes before the act root', 2, 2, 'pushes', '### relay and PLACE-papers by push_gated.sh, so each head the root names is at its remote.'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry: root verifies inside the suite alone.'),
    ('MANIFEST lines written', 0, 0, 'lines', '### no mirror this act.'),
    ('roster entries appended', 3, 3, 'entries', '### (R247)(5): v5.18, v0.6 and v0.5 at the roster`s end, no slot moving.'),
    ('mirror builder edits', 0, 0, 'edits', '### (R96); (R247)(5).'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z): ERRATA untouched.'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('TECHNE-Core pushes', 0, 0, 'pushes', '### (Z).'),
    ('README.md appends', 0, 0, 'appends', '### (R247) orders none.'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### (Z).'),
    ('REGISTRY.md appends', 0, 0, 'appends', '### (Z).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### OPEN_TRAILS beneath :12799, MEASURED off the bank.'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('questions asked of the author before the seal', 0, 0, 'questions', '### section (0): none; the precedence order reached every reading.'),
    ('questions asked of the author after the seal', 1, 0, 'questions', '### the ferry: what the precedence order does not reach.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R247).'),
    ('PLACE-papers documents written other than by appending or regenerating', 0, 0, 'documents', '### (W).'),
    ('PLACE-papers documents written at all', 4, 2, 'documents', '### (W): FINDINGS, OPEN_TRAILS; each page where it moves.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (W): none.'),
    ('SIDE-structural-error-correction tracked files written', 0, 0, 'files', '### (Z).'),
    ('SIDE-explicit-formula tracked files written', 0, 0, 'files', '### (Z).'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('files written outside every repository but the scratchpad', 0, 0, 'files', '### (W): the planted module lives in the scratchpad.'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('mirror zips built', 0, 0, 'zips', '### (R247) orders none; the roster is edited for the next build.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b637_arms_prerun.txt.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 8, 8, 'files', '### (W): the act`s seven and the generator`s test.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b637_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b637_tests_stepzero.json'), encoding='utf-8')))
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
    spec = {"registration": ("data/b637_registration_2026-10-07.txt -- b637, LANE THREE ACT SIXTY-FOUR: THE BINDER GRAMMAR -- THE E0 RULE AS A "
                             "TOTAL FUNCTION OVER A FINITE CLASSIFICATION, NAMES REMOVED FROM THE READING, BOTH READERS RERUN OVER BOTH "
                             "KERNELS, THE 20 UNNAMED ROWS READ BY CLASS; UPSTREAM ROWS AS KIND; THE MIRROR`S ROSTER AT THE CURRENT EDITIONS, "
                             "UNDER (R247)"), "clauses": clauses}
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
