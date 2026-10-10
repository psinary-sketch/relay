# -*- coding: utf-8 -*-
"""b646_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b645's spec, every clause re-written against this face: the edit-route arm and its planted test; the seven companions
### ### through the intake form; the MET list's one line and the re-grade; the description at v3, the fourth reader, the draft held; the
### ### seat's memory through the table; the record lines; nothing published.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b646_registration_2026-10-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b646_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### (R256)(4): the draft held.'),
    ('publish calls made', 0, 0, 'calls', '### (R256)(4).'),
    ('deposit drafts whose description is replaced', 1, 1, 'drafts', '### (R256)(4): the draft`s description replaced, read back, held.'),
    ('deposit draft files touched', 0, 0, 'files', '### (R256)(4): the description alone.'),
    ('identifiers of the author placed in an outbound request beyond the record`s own metadata', 0, 0, 'identifiers', '### N5, OPEN_TRAILS :11864.'),
    ('kernel source files created or edited', 0, 0, 'files', '### N5.'),
    ('kernel tags made', 0, 0, 'tags', '### N5.'),
    ('kernel branches made', 0, 0, 'branches', '### N5.'),
    ('kernel mains moved', 0, 0, 'mains', '### N5.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### every build before the seal, under the stop.'),
    ('editions, pages or census editions re-cut', 0, 0, 'editions', '### (R256)(3): no re-cut this act.'),
    ('arm files created', 2, 2, 'files', '### (R256)(2): tools/edit_route.py and its planted test.'),
    ('companion tables banked', 7, 7, 'tables', '### (R256)(3).'),
    ('MET-list lines added', 1, 1, 'lines', '### (R256)(4)(d).'),
    ('premise-structure names entered by ruling', 1, 1, 'names', '### (R256)(4)(d): TrivialSummandPremise`.'),
    ('composition rules added', 4, 4, 'rules', '### (R256)(4)(a)-(d).'),
    ('readers run from a directory with no project memory', 1, 1, 'readers', '### (R256)(4).'),
    ('seat-memory tables banked', 1, 1, 'tables', '### (R256)(5).'),
    ('weight lines entered', 1, 1, 'lines', '### (R256)(1).'),
    ('outsider lines entered', 1, 1, 'lines', '### (R256)(7).'),
    ('work-order lines entered', 1, 1, 'lines', '### (R256)(2), (5).'),
    ('research-arc entries opened', 1, 1, 'entries', '### (R256)(6).'),
    ('next-act input files committed', 0, 0, 'files', '### the author`s word: the navigator`s export stays untracked.'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('verdict names minted by the seat', 0, 0, 'verdicts', '### (R256)(3): the four are b645`s ruling`s.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A).'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### (Z).'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('instrument edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307: the instrument is sealed with the act`s tools.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### G-SEAL-HASHES.'),
    ('banks the act root names written after it', 0, 0, 'banks', '### (R251)(3).'),
    ('banks the act root names written with CR LF', 0, 0, 'banks', '### the author`s answer at b644.'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z): a retirement is proposed, not filed.'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R256).'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (Z): no edition this act.'),
    ('SIDE-global-section tracked files written', 0, 0, 'files', '### (Z): build products under its ignored build tree only.'),
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


def main(argv):
    print('=' * 100)
    print('b646_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b646_tests_stepzero.json'), encoding='utf-8')))
    except Exception:
        tests = 0
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b646_author_answers.txt'), encoding='utf-8').read(), re.M))
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
    spec = {"registration": ("data/b646_registration_2026-10-09.txt -- b646, LANE THREE ACT SEVENTY-THREE: THE EDIT-ROUTE ARM; THE SEVEN "
                             "COMPANIONS; THE DESCRIPTION AT v3, THE MET LIST WIDENED, A FOURTH READER, THE DRAFT HELD; THE SEAT`S MEMORY; "
                             "THE CROSS-FIELD RESONANCES ENTRY, UNDER (R256)"),
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
