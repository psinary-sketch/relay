# -*- coding: utf-8 -*-
"""b643_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b642's spec, every clause re-written against this face: the two reader repairs, each with its planted test, committed alone;
### ### the rerun; the lists' pin lines; the fresh probes; the two pages re-emitted; the glossary extended; the census at v0.7 from the banks; the
### ### Pi-0-1 sources sought; the second reader; no kernel written; nothing deposited; the face sealed after Components 2-6 (R253)(8).
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b643_registration_2026-10-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b643_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published or drafts made or updated at any service', 0, 0, 'records', '### (R253)(7): the deposit held.'),
    ('platform calls made', 0, 0, 'calls', '### the ferry: nothing deposits.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5, OPEN_TRAILS :11864.'),
    ('kernels of the federation written', 0, 0, 'kernels', '### N5: no kernel source touched.'),
    ('kernel files created or edited', 0, 0, 'files', '### N5.'),
    ('kernel tags made', 0, 0, 'tags', '### N5.'),
    ('kernel branches made', 0, 0, 'branches', '### N5.'),
    ('kernel mains moved', 0, 0, 'mains', '### N5.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### (R253)(8): the reader, the probes and the dependency print before the seal.'),
    ('reader repairs committed', 2, 2, 'repairs', '### (R253)(3)(a)-(b): each alone with its planted test.'),
    ('planted tests created', 2, 2, 'tests', '### (R253)(3).'),
    ('relay shared tools edited', 2, 2, 'tools', '### (R253)(3): tools/e0_rule.py and tools/b378_terminals.py, the textual reader`s pattern.'),
    ('relay shared banks edited', 1, 1, 'banks', '### (R253)(5)(a): data/glossary.txt.'),
    ('glossary entries added', 6, 6, 'entries', '### (R253)(5)(a) and the author`s answer: the five ruled and CHAIN.'),
    ('node-list editions written', 2, 2, 'lists', '### (R253)(4): the pin lines alone moved.'),
    ('pages re-emitted into PLACE-papers', 2, 2, 'pages', '### (R253)(4).'),
    ('census editions written', 1, 1, 'editions', '### (R253)(5): v0.7 beside v0.6.'),
    ('premise heads in the census table', 50, 50, 'heads', '### (R253)(5)(b).'),
    ('Pi-0-1 sources sought', 2, 2, 'sources', '### (R253)(5)(d): Kreisel; Davis, Matijasevic and Robinson.'),
    ('second-reader runs', 1, 1, 'runs', '### (R253)(6).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z): the six are the ruling`s.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z).'),
    ('table rows retired', 0, 0, 'rows', '### (R253) orders none.'),
    ('weight lines entered', 1, 1, 'lines', '### (R253)(1): b642 at its weight.'),
    ('work-orders entered', 1, 1, 'work-orders', '### (R253)(2): W-ORD-WATCHDOG-STOP.'),
    ('defect lines entered for the navigator', 1, 1, 'lines', '### (R253)(1): defect (j) as recorded.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### (Z).'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z): the glossary is the shared bank the ruling orders extended.'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### G-SEAL-HASHES.'),
    ('banks the act root names written after it', 0, 0, 'banks', '### (R251)(3), G-ACTROOT-LAST.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited other than the ledgers and the two pages', 0, 0, 'documents', '### (Z): README, REGISTRY, the census at v0.6, the companions untouched.'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('mid-act pushes before the act root', 2, 2, 'pushes', '### relay and PLACE-papers, before the root.'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry.'),
    ('mirror zips built', 0, 0, 'zips', '### the ferry orders none.'),
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
    ('questions asked of the author after the seal', 2, 0, 'questions', '### only what the precedence order does not reach.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R253).'),
    ('PLACE-papers documents written at all', 5, 5, 'documents', '### (W): FINDINGS, OPEN_TRAILS, the two pages, the census at v0.7.'),
    ('PLACE-papers documents created', 1, 1, 'documents', '### (W): the census at v0.7.'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (Z).'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('files written outside every repository but the scratchpad and the reader`s directory', 0, 0, 'files', '### (W).'),
    ('closings edited', 0, 0, 'closings', '### (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### (Z): the pages regenerated whole, the census beside v0.6.'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 9, 9, 'files', '### (W): the act`s seven and the two planted tests.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b643_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b643_tests_stepzero.json'), encoding='utf-8')))
    except Exception:
        tests = 0
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b643_author_answers.txt'), encoding='utf-8').read(), re.M))
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
    spec = {"registration": ("data/b643_registration_2026-10-08.txt -- b643, LANE THREE ACT SEVENTY: THE TWO READERS REPAIRED AND RERUN; THE PAGES "
                             "AT v0.26; THE KEYSTONE CENSUS AT v0.7; THE PI-0-1 FORM SOUGHT AT SOURCE; THE SECOND READER, UNDER (R253)"),
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
