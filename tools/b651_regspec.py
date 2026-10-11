# -*- coding: utf-8 -*-
"""b651_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b649's spec by the Write tool, every clause re-written against this face: the four first rows and the seam; the resolver
### ### repaired with its planted cases; the census at v0.8.1 and the glossary's entries; the restated lines measured, none merged; the
### ### docstrings read into sentence rows, none edited, two plain comments re-cut on a local branch beneath the hold; the navigator's rows;
### ### the record lines; nothing deposits.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b651_registration_2026-10-11.txt')
SPEC = os.path.join(ROOT, 'data', 'b651_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('kernel mains moved', 0, 0, 'mains', '### N5: no merge was made.'),
    ('merges made', 0, 0, 'merges', '### (R261)(6)-(7): every build beneath the hold.'),
    ('kernel tags made', 0, 0, 'tags', '### (R261)(7): the branch deferred, untagged.'),
    ('kernel branches made', 1, 1, 'branches', '### (R261)(7): docstrings-SIDE-kernel, local.'),
    ('kernel .lean files edited on a branch', 1, 1, 'files', '### (R261)(7): Kernel/PerpendicularCrossing.lean alone.'),
    ('kernel .lean files edited on a main', 0, 0, 'files', '### N5.'),
    ('plain comments re-cut', 2, 2, 'comments', '### (R261)(7): :98 and :144.'),
    ('kernel docstrings edited', 0, 0, 'docstrings', '### the author`s answers before the seal: the sentence reading first.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### every build before the seal, under the watchdog.'),
    ('generator edits committed', 3, 3, 'edits', '### (R261)(3)(a), (4), (5): chain_page.py, axiom_claim.py, licensed_table.py.'),
    ('planted tests written', 3, 3, 'tests', '### one per generator edit.'),
    ('glossary entries appended', 7, 7, 'entries', '### (R261)(3)(a): the superseding entry; (R261)(5): six.'),
    ('glossary supersession marks appended', 1, 1, 'marks', '### (R261)(3)(a).'),
    ('node lists written', 1, 1, 'lists', '### (R261)(3)(b): the chi list.'),
    ('page re-emissions committed', 4, 4, 'commits', '### one page per call, two at Component 2 and two at Component 4.'),
    ('census editions written', 1, 1, 'editions', '### (R261)(5): v0.8.1 beside v0.8.'),
    ('dated lines appended to a keystone file', 1, 1, 'lines', '### (R261)(3)(d): the simplicity file.'),
    ('dated correction lines on OPEN_TRAILS', 1, 1, 'lines', '### (R261)(3)(c): the seam.'),
    ('work-order trigger lines entered', 1, 1, 'lines', '### the author`s answer: W-ORD-VERDICT-INSTRUMENT`s trigger fired.'),
    ('weight lines entered', 1, 1, 'lines', '### (R261)(1).'),
    ('delivery clause lines entered', 1, 1, 'lines', '### (R261)(2).'),
    ('terminal-table rows moved', 1, 1, 'rows', '### (R261)(3)(c): the seam`s def, CONFLICT to DERIVES.'),
    ('holds changed', 0, 0, 'holds', '### the author`s answer at b644.'),
    ('navigator files read or written', 0, 0, 'files', '### (R261)(8).'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('verdict names minted by the seat', 0, 0, 'verdicts', '### UNBOUND is the author`s word at this act.'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R261).'),
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
    print('b651_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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

    def jcount(name, f):
        try:
            return f(json.load(io.open(os.path.join(ROOT, 'data', name), encoding='utf-8')))
        except Exception:
            return 0
    tests = jcount('b651_tests_stepzero.json', len)
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b651_author_answers.txt'), encoding='utf-8').read(), re.M))
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
    spec = {"registration": ("data/b651_registration_2026-10-11.txt -- b651, LANE THREE ACT SEVENTY-EIGHT: THE RE-CUTS OPENED; THE RESOLVER; THE "
                             "CENSUS AT v0.8.1; THE RESTATED LINES; THE LARGEST KERNEL`S DOCSTRINGS; THE NAVIGATOR`S ROWS, UNDER (R261)"),
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
