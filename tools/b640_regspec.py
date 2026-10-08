# -*- coding: utf-8 -*-
"""b640_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b639's spec, every clause re-written against this face: the shared status tool carried and extended after the seal, each
### ### committed alone with its test; the work-orders appended; the description recomposed; the reader staged off drive D and run by the author;
### ### the draft updated (its zip and its description) and read back, nothing published without the word; no kernel source written.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b640_registration_2026-10-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b640_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('draft versions made at the service', 0, 0, 'versions', '### the draft 23228113 stands from b639; none is made.'),
    ('drafts updated at the service', 1, 1, 'drafts', '### (R250)(7): its zip and its description, once.'),
    ('files replaced in the draft', 1, 1, 'files', '### (R250)(7): the mirror`s zip.'),
    ('records published at the service', 1, 0, 'records', '### on the author`s word "publish" alone.'),
    ('records other than 21539167 written at the service', 0, 0, 'records', '### (R250)(7).'),
    ('route steps run before the mirror', 0, 0, 'steps', '### (R250)(7): the mirror before the draft`s update.'),
    ('route steps run before the seal', 0, 0, 'steps', '### section (0).'),
    ('identifiers of the author placed in an outbound request beyond the record`s own metadata', 0, 0, 'identifiers', '### (R240)(2)(i).'),
    ('token prints, logs or banks', 0, 0, 'prints', '### (R110).'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z).'),
    ('existing kernel files edited', 0, 0, 'files', '### (Z).'),
    ('kernels of the federation written', 0, 0, 'kernels', '### (Z).'),
    ('kernel files created', 0, 0, 'files', '### (Z).'),
    ('kernel tags made', 0, 0, 'tags', '### (Z).'),
    ('kernel branches made', 0, 0, 'branches', '### (Z).'),
    ('module builds by the standing route', 0, 0, 'builds', '### the ferry: no Lean build this act.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### the reader`s test ran at step zero, detached.'),
    ('fresh probe runs of the page generator', 0, 0, 'runs', '### the pages re-emit from banked probes.'),
    ('second-reader sessions launched by the seat', 0, 0, 'sessions', '### (R250)(6): the author runs the reader.'),
    ('second-reader sessions run by the author', 1, 1, 'sessions', '### (R250)(6): one, off D:\\.'),
    ('ls-remote reads of a repository beyond its one per run', 0, 0, 'reads', '### the ferry.'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (R250)(3): the five are the ruling`s.'),
    ('premise heads classed at five statuses', 50, 50, 'heads', '### (R250)(3), MEASURED off the status bank.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('rule edits', 0, 0, 'edits', '### (Z): the rule and its tests unedited.'),
    ('table rows retired', 0, 0, 'rows', '### (R250) orders none.'),
    ('clauses entered under the author`s ruling', 1, 1, 'clauses', '### (R250)(3): the five-status clause beneath the criterion.'),
    ('work-order blocks entered', 1, 1, 'blocks', '### (R250)(4): one line per open premise not already carried.'),
    ('weight lines entered', 1, 1, 'lines', '### (R250)(1): b639 at its weight.'),
    ('census editions written', 0, 0, 'editions', '### (R250)(8): v0.7 is the next act`s.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay shared tools created under the author`s ruling', 2, 2, 'tools', '### (R250)(3): tools/premise_status.py and tools/test_premise_status.py.'),
    ('relay shared tools edited under the author`s ruling', 1, 1, 'tools', '### (R250)(3): tools/premise_status.py, the five statuses, through the Edit tool.'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### G-SEAL-HASHES.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited other than the pages and the ledgers', 0, 0, 'documents', '### (Z): README, REGISTRY and the glossary untouched.'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('generated pages re-emitted', 2, 0, 'pages', '### Component 7: where a cell moves.'),
    ('mid-act pushes before the act root', 4, 4, 'pushes', '### Component 6 (relay, PLACE-papers) and before the root (relay, PLACE-papers).'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry.'),
    ('MANIFEST lines written', 1, 1, 'lines', '### OPEN_TRAILS :12929.'),
    ('mirror builder edits', 0, 0, 'edits', '### (R96).'),
    ('mirror zips built', 1, 1, 'zips', '### (R250)(7).'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z).'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('TECHNE-Core pushes', 0, 0, 'pushes', '### (Z).'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### (Z).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A).'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1).'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### MEASURED off the bank.'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0).'),
    ('questions asked of the author before the seal', 'QUESTIONS', 'QUESTIONS', 'questions', '### section (0), MEASURED off the answers bank.'),
    ('questions asked of the author after the seal', 3, 2, 'questions', '### (R250)(6)-(7): the reader`s hold and the deposit prompt.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R250).'),
    ('PLACE-papers documents written at all', 4, 2, 'documents', '### (W): FINDINGS, OPEN_TRAILS; each page where a cell moves.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (W).'),
    ('SIDE-explicit-formula tracked files written', 0, 0, 'files', '### (Z).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (Z).'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('files written outside every repository but the scratchpad, the mirror`s zip and stage and the reader`s directory', 0, 0, 'files', '### (W).'),
    ('closings edited', 0, 0, 'closings', '### (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### (Z).'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 9, 9, 'files', '### (W): the act`s seven and the shared status tool with its test.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b640_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b640_tests_stepzero.json'), encoding='utf-8')))
    except Exception:
        tests = 0
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b640_author_answers.txt'), encoding='utf-8').read(), re.M))
    except Exception:
        questions = 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests,
                    QUESTIONS=questions)
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS'):
        print('      %-9s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b640_registration_2026-10-08.txt -- b640, LANE THREE ACT SIXTY-SEVEN: THE PREMISE STATUS SPLIT TO FIVE AND THE "
                             "OPEN PREMISES GIVEN WORK-ORDERS; THE DEPOSIT DESCRIPTION`S ASSUMPTION SECTION RECOMPOSED; A SECOND READER FOR "
                             "LEGIBILITY; THE DRAFT 23228113 UPDATED AND HELD AT THE SAME PROMPT, UNDER (R250)"),
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


