# -*- coding: utf-8 -*-
"""b644_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b643's spec, every clause re-written against this face: the chain read at commit and the additive arm; the watchdog stop;
### ### SIDE-global-section's Interfaces under the stop; the hinges recounted and the census at v0.7.1; the two rosters; the seven patch editions;
### ### the description as synthesis and its readers; the lattice banked; the draft's file set replaced and held after the record (R254)(9).
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b644_registration_2026-10-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b644_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### (R254)(9): publish is the author`s word in a later act.'),
    ('publish calls made', 0, 0, 'calls', '### (R254)(9).'),
    ('drafts updated at the service', 1, 1, 'drafts', '### (R254)(9): draft 23228113, its file set and description, after the record.'),
    ('drafts read back after their update', 1, 1, 'drafts', '### (R254)(9): byte for byte and digest for digest.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N6, OPEN_TRAILS :11864.'),
    ('kernel source files created or edited', 0, 0, 'files', '### N6: builds only.'),
    ('kernel tags made', 0, 0, 'tags', '### N6.'),
    ('kernel branches made', 0, 0, 'branches', '### N6.'),
    ('kernel mains moved', 0, 0, 'mains', '### N6.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### every build before the seal, under the stop.'),
    ('Interfaces modules sent to a build call', 6, 6, 'modules', '### (R254)(5): one per call under (R254)(3).'),
    ('instrument repairs committed', 2, 2, 'repairs', '### (R254)(2)-(3): the chain at commit; the watchdog stop.'),
    ('planted tests created', 3, 3, 'tests', '### the chain at commit, the additive arm, the watchdog stop.'),
    ('relay shared tools edited', 2, 2, 'tools', '### tools/act_root.py and tools/mirror_roster.json.'),
    ('relay shared banks edited', 1, 1, 'banks', '### data/glossary.txt, additively.'),
    ('glossary lines appended', 5, 5, 'lines', '### (R254)(4) and the author`s word: two dated lines and three entries.'),
    ('census editions written', 1, 1, 'editions', '### (R254)(4): v0.7.1 beside v0.7, regenerated once on the author`s word.'),
    ('pages re-emitted into PLACE-papers', 2, 2, 'pages', '### the page clause.'),
    ('companion label edits', 7, 7, 'edits', '### (R254)(7).'),
    ('roster paths appended', 9, 9, 'paths', '### the author`s answer: seven companions and two census editions.'),
    ('description parts', 5, 5, 'parts', '### (R254)(8).'),
    ('description repairs committed alone', 15, 15, 'repairs', '### the author`s word: nine, then six.'),
    ('second-reader runs', 5, 5, 'runs', '### hinge twice, description three times.'),
    ('lattice rows banked', 94, 94, 'rows', '### (R254)(10): a bank, not an edition.'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A).'),
    ('ceiling sentences asserted in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('weight lines entered', 1, 1, 'lines', '### (R254)(1).'),
    ('work-orders marked acted', 2, 2, 'work-orders', '### (R254)(2)-(3).'),
    ('standing clauses entered', 1, 1, 'clauses', '### (R254)(2): shared data files additive.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### (Z).'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### G-SEAL-HASHES.'),
    ('banks the act root names written after it', 0, 0, 'banks', '### (R251)(3).'),
    ('banks the act root names written with CR LF', 0, 0, 'banks', '### the author`s answer at b644.'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('mid-act pushes before the act root', 2, 2, 'pushes', '### relay and PLACE-papers, before the root.'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry.'),
    ('mirror zips built', 1, 1, 'zips', '### (R254)(9), after the last PLACE-papers push.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### (Z).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A).'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('censuses run', 2, 2, 'censuses', '### (G1), late.'),
    ('repositories hard-failing', 0, 0, 'repositories', '### (G1).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### MEASURED off the bank.'),
    ('questions asked of the author before the seal', 'QUESTIONS', 'QUESTIONS', 'questions', '### MEASURED off the answers bank.'),
    ('questions asked of the author after the root', 0, 0, 'questions', '### the answers bank is root-named.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R254).'),
    ('PLACE-papers documents created', 1, 1, 'documents', '### (W): the census at v0.7.1.'),
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
    print('b644_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b644_tests_stepzero.json'), encoding='utf-8')))
    except Exception:
        tests = 0
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b644_author_answers.txt'), encoding='utf-8').read(), re.M))
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
    spec = {"registration": ("data/b644_registration_2026-10-09.txt -- b644, LANE THREE ACT SEVENTY-ONE: THE CHAIN AT COMMIT; THE WATCHDOG STOP; "
                             "THE HINGES RECOUNTED, THE CENSUS AT v0.7.1; THE ROSTERS; THE PATCH EDITIONS; THE DESCRIPTION; THE LATTICE, UNDER (R254)"),
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
