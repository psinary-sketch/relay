# -*- coding: utf-8 -*-
"""b639_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b638's spec, every clause re-written against this face: one draft version of the monograph's record made through the
### ### (R110) route and read back, published on the author's word alone; no kernel source written and nothing built; the roster edited and
### ### committed alone at step zero; the premise heads classed by status before any description; the mirror built after the Component 1
### ### push and before the draft; README, REGISTRY and the glossary taking dated lines on publish alone; the questions put before the seal.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b639_registration_2026-10-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b639_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('draft versions made at the service', 1, 1, 'versions', '### (R249)(4) PART ONE: one new version of record 21539167, as a draft.'),
    ('records published at the service', 1, 0, 'records', '### (R249)(4) PART TWO: on the author`s word "publish" alone; none on "hold".'),
    ('records other than 21539167 written at the service', 0, 0, 'records', '### the author`s answers before the seal.'),
    ('second new versions requested', 0, 0, 'requests', '### the route`s step refuses to run twice.'),
    ('route steps run before the mirror', 0, 0, 'steps', '### (R249)(3): the mirror before the draft.'),
    ('route steps run before the seal', 0, 0, 'steps', '### section (0).'),
    ('platform reads per route step', 1, 1, 'reads', '### the ferry: the service read once per step, its reading printed.'),
    ('registry reads of the DOI', 1, 0, 'reads', '### H73d: once, on publish.'),
    ('identifiers of the author placed in an outbound request beyond the record`s own metadata', 0, 0, 'identifiers', '### (R240)(2)(i); the ferry`s N5.'),
    ('token prints, logs or banks', 0, 0, 'prints', '### (R110): the token in the Authorization header alone.'),
    ('existing kernel .lean declarations of the federation edited', 0, 0, 'declarations', '### (Z): no kernel source touched.'),
    ('existing kernel files edited', 0, 0, 'files', '### (Z).'),
    ('kernels of the federation written', 0, 0, 'kernels', '### (Z).'),
    ('kernel files created', 0, 0, 'files', '### (Z).'),
    ('kernel tags made', 0, 0, 'tags', '### (Z).'),
    ('kernel tags pushed', 0, 0, 'tags', '### (Z).'),
    ('kernel branches made', 0, 0, 'branches', '### (Z).'),
    ('module builds by the standing route', 0, 0, 'builds', '### the ferry: no Lean build this act.'),
    ('closure builds run in parallel under the hold', 0, 0, 'builds', '### OPEN_TRAILS :13067.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### the reader`s test ran at step zero, detached; no lean call after the seal.'),
    ('fresh probe runs of the page generator', 0, 0, 'runs', '### the pages re-emit from b638`s lists and b635`s banked probes.'),
    ('second-reader sessions launched by the seat', 0, 0, 'sessions', '### (R249) orders none.'),
    ('ls-remote reads of a repository beyond its one per run', 0, 0, 'reads', '### the ferry; root verifies inside the suite alone.'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('worktrees deleted', 0, 0, 'worktrees', '### (Z).'),
    ('CORRESPONDENCE rows written', 0, 0, 'rows', '### (R249) orders none.'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (R249)(2): the four statuses are the ruling`s.'),
    ('premise heads classed by status', 50, 50, 'heads', '### (R249)(2): the census`s 50, MEASURED off the status bank.'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A); (Z).'),
    ('priority sentences', 0, 0, 'sentences', '### section (A).'),
    ('ceiling sentences written in the corpus', 0, 0, 'sentences', '### (Z): the description quotes README`s sentences whole.'),
    ('rule edits', 0, 0, 'edits', '### (Z): the rule and its tests unedited.'),
    ('table rows retired', 0, 0, 'rows', '### (R249) orders none.'),
    ('correction entries written under the author`s ruling', 0, 0, 'entries', '### (R249) orders none.'),
    ('standing lines entered under the author`s ruling', 0, 0, 'lines', '### (R249) orders none.'),
    ('census method items entered', 1, 1, 'items', '### (R249)(2): the status column, priced for v0.7.'),
    ('work-orders entered', 1, 1, 'work-orders', '### the author`s answer before the seal: the companions` patch versions.'),
    ('weight lines entered', 1, 1, 'lines', '### (R249)(1): b638 at its weight.'),
    ('census editions written', 0, 0, 'editions', '### (R249)(2): no census edition this act.'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### section (Z): the faces of b566-b638 are not edited.'),
    ('prior acts` banks edited', 0, 0, 'files', '### (Z).'),
    ('relay tools edited in place under the author`s ruling', 1, 1, 'tools', '### (R249)(3): the roster, committed alone at step zero.'),
    ('relay instruments created beyond the act`s own', 0, 0, 'tools', '### (W).'),
    ('relay data files written outside the act`s own names, the table and the roots line', 1, 0, 'files', '### (W): relay data/glossary.txt`s deposit entry, on publish alone.'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307: sealed means unedited by any means.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### OPEN_TRAILS :13307: G-SEAL-HASHES.'),
    ('existing keystones edited or annotated', 0, 0, 'keystones', '### (Z).'),
    ('existing documents edited other than the pages, the ledgers and the dated lines on publish', 0, 0, 'documents', '### (Z).'),
    ('ANNEX or synthesis files written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### b628`s full bank stays untracked.'),
    ('generated pages re-emitted', 2, 0, 'pages', '### Component 4: each page where the glossary`s deposit entry changes it, on publish.'),
    ('mid-act pushes before the act root', 4, 4, 'pushes', '### Component 1 (relay, PLACE-papers) and before the root (relay, PLACE-papers), by push_gated.sh.'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry: root verifies inside the suite alone.'),
    ('MANIFEST lines written', 1, 1, 'lines', '### OPEN_TRAILS :12929: the root line, in the stage.'),
    ('roster entries appended', 1, 1, 'entries', '### (R249)(3): THE_KEYSTONE_CENSUS_v0_6 beside v0_5.'),
    ('mirror builder edits', 0, 0, 'edits', '### (R96).'),
    ('mirror zips built', 1, 1, 'zips', '### (R249)(3): after the Component 1 push and before the draft.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D) and (E), MEASURED off the face.'),
    ('ERRATA entries written', 0, 0, 'entries', '### (Z): ERRATA untouched.'),
    ('cells of row U1 written, or sites re-kinded', 0, 0, 'cells', '### section (Z).'),
    ('lists of the four closed', 0, 0, 'lists', '### section (Z).'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('TECHNE-Core pushes', 0, 0, 'pushes', '### (Z).'),
    ('README.md dated lines', 1, 0, 'lines', '### (R249)(4) PART TWO: the deposit note, on publish alone.'),
    ('REGISTRY.md dated lines', 1, 0, 'lines', '### (R249)(4) PART TWO: the deposit row, on publish alone.'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### (Z).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A): part 1 of 1, received IN FULL.'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('banned-stem hits in the ferry file', 0, 0, 'hits', '### section (A).'),
    ('censuses run at step zero', 2, 2, 'censuses', '### (G1): TOTAL MISSING 0, both.'),
    ('repositories hard-failing at step zero', 0, 0, 'repositories', '### (G1).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### OPEN_TRAILS beneath :12799, MEASURED off the bank.'),
    ('orphan processes of earlier sessions stopped at step zero', 0, 0, 'processes', '### section (0): none matched.'),
    ('questions asked of the author before the seal', 'QUESTIONS', 'QUESTIONS', 'questions', '### section (0), MEASURED off the answers bank.'),
    ('questions asked of the author after the seal', 2, 1, 'questions', '### (R249)(4): the one prompt of Component 2; otherwise what the precedence order does not reach.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R249).'),
    ('PLACE-papers documents written other than by appending, regenerating or a dated line', 0, 0, 'documents', '### (W).'),
    ('PLACE-papers documents written at all', 6, 2, 'documents', '### (W): FINDINGS, OPEN_TRAILS; README, REGISTRY and each page on publish.'),
    ('PLACE-papers documents created', 0, 0, 'documents', '### (W).'),
    ('SIDE-structural-error-correction tracked files written', 0, 0, 'files', '### (Z).'),
    ('SIDE-explicit-formula tracked files written', 0, 0, 'files', '### (Z).'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W).'),
    ('SIDE-global-section files written', 0, 0, 'files', '### (W): none.'),
    ('files written outside every repository but the scratchpad and the mirror`s zip and stage', 0, 0, 'files', '### (W).'),
    ('closings edited', 0, 0, 'closings', '### section (Z).'),
    ('lines removed from any document', 0, 0, 'lines', '### section (Z).'),
    ('bars declared', 'BARS', 'BARS', 'bars', '### MEASURED: this face has no (K) section.'),
    ('gate arms declared', 'ARMS', 'ARMS', 'arms', '### section (G2), counted off this face.'),
    ('arms declared on the face and not run at HEAD before the seal', 0, 0, 'arms', '### (R202)(3): b639_arms_prerun.txt.'),
    ('arms built by this act not run over this act`s own bank', 0, 0, 'arms', '### (G2).'),
    ('substring tests for a tool`s verdict', 0, 0, 'tests', '### A2.'),
    ('new `relay` tool files named on this face', 7, 7, 'files', '### (W): the act`s seven.'),
    ('files of a KIND the write list does not name', 0, 0, 'files', '### section (W).'),
    ('files staged by `-A`', 0, 0, 'commands', 'b381.'),
    ('artifact counts predicted in this registration', 0, None, 'predictions', 'RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED.'),
]


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b639_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        tests = len(json.load(io.open(os.path.join(ROOT, 'data', 'b639_tests_stepzero.json'), encoding='utf-8')))
    except Exception:
        tests = 0
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b639_author_answers.txt'), encoding='utf-8').read(), re.M))
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
    spec = {"registration": ("data/b639_registration_2026-10-07.txt -- b639, LANE THREE ACT SIXTY-SIX: THE DEPOSIT ON THE (R110) ROUTE -- THE 50 "
                             "PREMISE HEADS CLASSED BY STATUS, THE DESCRIPTION IN THE READER`S ORDER, THE FILES WITH THEIR DIGESTS, A DRAFT READ BACK "
                             "FROM THE SERVICE, THE AUTHOR`S WORD; THE ROSTER AT CENSUS v0.6 AND THE MIRROR REBUILT, UNDER (R249)"),
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
