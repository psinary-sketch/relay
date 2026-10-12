# -*- coding: utf-8 -*-
"""b653_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b652's spec by the Write tool, every clause re-written against this face: the record lines; the margin rule on completed
### ### runs; the seal order; the elided cells completed and cut; the hosted runner, its workflow files and its two dispatches; the merges on its
### ### gate readings; the b638 test; nothing deposits.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b653_registration_2026-10-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b653_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (R263)(4).'),
    ('workflow files written', 2, 2, 'files', '### (R263)(4): one per kernel a branch of this act touches.'),
    ('runner dispatches', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### (R263)(4): once per branch, MEASURED off the runner rows.'),
    ('merges made', 'MERGES', 'MERGES', 'merges', '### (R263)(4): each alone on its gate reading, MEASURED.'),
    ('kernel tags made', 'MERGES', 'MERGES', 'tags', '### (R263)(4): one per merge, at the next in its series.'),
    ('kernel .lean files edited on a branch', 3, 3, 'files', '### (R263)(5): the three elided blocks` files.'),
    ('kernel .lean files edited on a main', 0, 0, 'files', '### N5: a main moves by a merge and the workflow file only.'),
    ('elided cells completed', 3, 3, 'cells', '### (R263)(5).'),
    ('lean calls made after the seal', 0, 0, 'calls', '### none on this host at all.'),
    ('test edits committed', 1, 1, 'edits', '### (R263)(6): test_chain_page_b638.py case (1).'),
    ('record lines landed before the seal', 3, 3, 'lines', '### (R263)(1)-(3).'),
    ('holds changed', 0, 0, 'holds', '### the hold stays at 2,560 MB on every host.'),
    ('navigator files read or written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('verdict names minted by the seat', 0, 0, 'verdicts', '### (Z).'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R263).'),
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


# ### (R263)(3), THE SEAL ORDER: one planted row of every shape a sealed route reads, each run through the record tool's own reader (its READERS)
# ### before the spec is emitted; a reader that raises, or returns nothing, refuses the spec. b651's (m)(n) and b652's (l) are the cases.
PLANTED = [
    ('runner row', 'read_runner_row', dict(kernel='SIDE-x', branch='b999-planted', ref='0' * 40, target='X.Y', run_id=1, conclusion='success',
                                           artifact_sha256='0' * 64, mem_low=9000, stopped=False, gate='DERIVES', merged=None, tag=None)),
    ('runner row, stopped on the runner', 'read_runner_row', dict(kernel='SIDE-x', branch='b999-planted', ref='0' * 40, target='X.Y', run_id=2,
                                                                   conclusion='failure', artifact_sha256=None, mem_low=2400, stopped=True,
                                                                   gate=None, merged=None, tag=None)),
    ('score row', 'read_score_row', ('N3', ['REFUTED IN ONE CLAUSE', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the kernel`s runner, the author`s word'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the runner`s gate readings'),
]


def planted():
    """each planted row through its reader; a head is first landed in a scratch ledger by the one conversion's append_to, then read by
    read_head. Returns [(shape, ok, what)]."""
    import tempfile
    import b653_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b653_spec_') as d:
                    led = os.path.join(d, 'LEDGER.md')
                    open(led, 'wb').write(b'# a scratch ledger\n')
                    REC.append_to(led, '\n' + row + ': planted.\n')
                    got = fn(led, row)
            elif reader == 'read_score_row':
                got = fn(*row)
            else:
                got = fn(row)
            out.append((shape, bool(got), repr(got)[:120]))
        except Exception as e:
            out.append((shape, False, '%s: %s' % (type(e).__name__, str(e)[:100])))
    return out


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b653_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    if not CNT.self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2
    P = planted()
    print('  ### (R263)(3) THE PLANTED ROWS, ONE PER SHAPE A SEALED ROUTE READS, EACH THROUGH THE RECORD TOOL`S READER:')
    for shape, ok, what in P:
        print('      %-44s %s -- %s' % (shape, 'READ' if ok else '### REFUSED', what))
    print('  ### ### **PLANTED ROWS %d ; READ %d ; REFUSED %d.**' % (len(P), sum(1 for p in P if p[1]), sum(1 for p in P if not p[1])))
    # ### the control: each reader refuses a row of another shape (b652's (l): a build row read for keys it did not carry)
    import b653_record as REC
    ctl = []
    for what, f in (('a runner row missing its keys (b652`s build-row shape)', lambda: REC.read_runner_row(dict(target='X.Y', slot_seen=1, needed=1))),
                    ('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b653_ferry.txt'), '### b999 absent'))):
        try:
            f()
            ctl.append((what, False))
        except Exception:
            ctl.append((what, True))
    for what, ok in ctl:
        print('      CONTROL %-60s %s' % (what, 'REFUSED, AS WANTED' if ok else '### READ -- THE READER IS VACUOUS'))
    if not all(ok for _w, ok in ctl):
        print('  ### REFUSING TO EMIT A SPEC: A READER TOOK A ROW OF ANOTHER SHAPE.')
        return 4
    if not all(p[1] for p in P):
        print('  ### REFUSING TO EMIT A SPEC: A SEALED ROUTE`S READER FAILED ON A PLANTED ROW.')
        return 4
    text = io.open(REG, encoding='utf-8').read() if os.path.exists(REG) else ''
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
    tests = jcount('b653_tests_stepzero.json', len)
    rows = lambda j: j.get('rows') or []   # noqa: E731
    dispatches = jcount('b653_runner_rows.json', lambda j: sum(1 for r in rows(j) if r.get('run_id')))
    merges = jcount('b653_runner_rows.json', lambda j: sum(1 for r in rows(j) if r.get('merged')))
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b653_author_answers.txt'), encoding='utf-8').read(), re.M))
    except Exception:
        questions = 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests,
                    QUESTIONS=questions, DISPATCHES=dispatches, MERGES=merges)
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'DISPATCHES', 'MERGES'):
        print('      %-10s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b653_registration_2026-10-12.txt -- b653, LANE THREE ACT EIGHTY: b652 AT ITS WEIGHT; THE MARGIN RULE ON "
                             "COMPLETED RUNS; THE HOSTED RUNNER; THE ELIDED CELLS; THE b638 TEST, UNDER (R263)"),
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
