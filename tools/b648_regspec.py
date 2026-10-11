# -*- coding: utf-8 -*-
"""b648_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b647's spec by the Write tool, every clause re-written against this face: the 37 sorry lines classified and repaired by
### ### the author's word; the two pages through the table, three template repairs, the pages re-emitted; the census at v0.8 and a second
### ### reader; the h2 row; the re-cut order; the record lines; nothing deposits.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b648_registration_2026-10-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b648_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### (R258)(7): the draft held at v4.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### the ferry: the deposit route untouched this act.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('kernel source edits made before the author`s answer', 0, 0, 'edits', '### (R258)(2), N1.'),
    ('kernel mains moved by the author`s answer', 'MAINS', 'MAINS', 'mains', '### (R258)(2): the quarantines merged; MEASURED off the kernels.'),
    ('kernel branches made by the author`s answer', 'BRANCHES', 'BRANCHES', 'branches', '### (R258)(2); MEASURED off the kernels.'),
    ('kernel tags made', 0, 0, 'tags', '### N5.'),
    ('kernel ERRATA-form files written', 2, 2, 'files', '### the author`s answer: each quarantined name and statement in the kernel`s file.'),
    ('kernel docstrings edited on a main', 0, 0, 'docstrings', '### (R258)(5): the h2 re-cut proposed, not applied.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### every build before the seal, under the watchdog.'),
    ('template repairs committed alone', 3, 3, 'repairs', '### (R258)(3), each through the Edit tool.'),
    ('pages re-emitted', 2, 2, 'pages', '### (R258)(3), one per call.'),
    ('node lists written', 2, 2, 'lists', '### repair 3`s mark, b643`s lists byte for byte beneath it.'),
    ('page tables banked', 2, 2, 'tables', '### (R258)(3): before and after the re-emission.'),
    ('census editions written', 1, 1, 'editions', '### (R258)(4): v0.8 beside v0.7.1.'),
    ('PLACE-papers documents created', 1, 1, 'documents', '### the census at v0.8.'),
    ('readers run from a directory with no project memory', 1, 1, 'readers', '### (R258)(4).'),
    ('h2 rows banked', 1, 1, 'rows', '### (R258)(5).'),
    ('re-cut order banks written', 1, 1, 'banks', '### (R258)(6).'),
    ('weight lines entered', 1, 1, 'lines', '### (R258)(1).'),
    ('sorry-breach lines entered', 1, 1, 'lines', '### (R258)(2).'),
    ('correction lines entered', 1, 1, 'lines', '### the author`s answer: the rule unenforced on legacy code.'),
    ('glossary entries appended', 0, 0, 'entries', '### the glossary unedited this act.'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('verdict names minted by the seat', 0, 0, 'verdicts', '### the four are b645`s ruling`s.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A).'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### (Z).'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### G-SEAL-HASHES.'),
    ('banks the act root names written after it', 0, 0, 'banks', '### (R251)(3).'),
    ('banks the act root names written with CR LF', 0, 0, 'banks', '### the author`s answer at b644.'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('PLACE-papers ERRATA entries written', 0, 0, 'entries', '### (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### (Z).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A).'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### MEASURED off the bank.'),
    ('questions asked of the author before the seal', 'QUESTIONS', 'QUESTIONS', 'questions', '### MEASURED off the answers bank.'),
    ('questions asked of the author after the root', 0, 0, 'questions', '### the answers bank is root-named.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R258).'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('closings edited', 0, 0, 'closings', '### (Z).'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def kernel_moves():
    """(mains moved, branches made) since b647's kernel face (relay data/b647_kernels_face.json), read from each kernel's refs."""
    try:
        face = json.load(io.open(os.path.join(ROOT, 'data', 'b647_kernels_face.json'), encoding='utf-8'))['kernels']
    except Exception:
        return 0, 0
    mains = branches = 0
    for k, v in face.items():
        p = 'D:/' + k
        r = subprocess.run(['git', '-C', p, 'rev-parse', '--short=7', 'main'], capture_output=True, text=True)
        mains += r.stdout.strip() != v[0]
        r = subprocess.run(['git', '-C', p, 'branch', '--format=%(refname:short)'], capture_output=True, text=True)
        branches += len(set(x for x in r.stdout.split() if x.strip()) - set(v[2]))
    return mains, branches


def main(argv):
    print('=' * 100)
    print('b648_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b648_tests_stepzero.json'), encoding='utf-8')))
    except Exception:
        tests = 0
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b648_author_answers.txt'), encoding='utf-8').read(), re.M))
    except Exception:
        questions = 0
    mains, branches = kernel_moves()
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests,
                    QUESTIONS=questions, MAINS=mains, BRANCHES=branches)
    print()
    print('  ### ### **MEASURED OFF THE FACE, THE BANKS AND THE KERNELS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'MAINS', 'BRANCHES'):
        print('      %-9s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b648_registration_2026-10-10.txt -- b648, LANE THREE ACT SEVENTY-FIVE: THE SORRY LINES CLASSIFIED FOR THE "
                             "AUTHOR`S WORD; THE TWO PAGES THROUGH THE TABLE AND RE-EMITTED; THE KEYSTONE CENSUS AT v0.8; THE h2 ROW; THE RE-CUT "
                             "ORDER TO THE AUTHOR, UNDER (R258)"),
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
