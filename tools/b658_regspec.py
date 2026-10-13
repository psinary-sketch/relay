# -*- coding: utf-8 -*-
"""b658_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b657's and b654's specs by the Write tool, every clause re-written against this face: the record lines; the splitter
### ### repaired with its planted test; the statement drafted and traced before any Lean; the one prompt; the branch and its three files;
### ### the print list from print_targets.txt on the author's word; the one dispatch; the merge on its gate reading; the dry-run step of the
### ### registration gate; nothing deposits. The planted rows of (R263)(3) carried for this act's readers, a trace row among them.
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

REG = os.path.join(ROOT, 'data', 'b658_registration_2026-10-12.txt')
SPEC = os.path.join(ROOT, 'data', 'b658_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (R263)(4).'),
    ('workflow files written on a main outside a merge', 0, 0, 'files', '### N5, as the author`s word on the print list reads it.'),
    ('workflow files edited on the branch', 1, 1, 'files', '### the author`s word: the print step reads print_targets.txt.'),
    ('runner dispatches', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### (R268)(4): once per branch, MEASURED off the runner rows.'),
    ('merges made', 'MERGES', 'MERGES', 'merges', '### (R268)(4): alone on its gate reading, MEASURED.'),
    ('kernel tags made', 'MERGES', 'MERGES', 'tags', '### (R268)(4): one per merge, v0.28.'),
    ('kernel files written on the branch', 'FILES', 'FILES', 'files', '### (R268)(4): MEASURED off the kernel`s diff.'),
    ('kernel .lean files written on a main outside a merge', 0, 0, 'files', '### N5.'),
    ('sorry reaching a kernel main', 0, 0, 'sorries', '### N3.'),
    ('excluded-zero hypotheses in the statement', 0, 0, 'hypotheses', '### the author`s word: the clause struck as the navigator`s.'),
    ('hypotheses of the statement untraced to the ζ proof', 0, 0, 'hypotheses', '### N2.'),
    ('Lean written before the author`s word on the statement', 0, 0, 'files', '### (R268)(3).'),
    ('bench numbers computed', 0, 0, 'numbers', '### (R268)(4): no bench number this act.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### none on this host at all.'),
    ('record lines landed before the seal', 2, 2, 'lines', '### (R268)(1), (2).'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('shared tools edited', 1, 1, 'tools', '### (R268)(2): the splitter, through the Edit tool.'),
    ('planted tests added', 1, 1, 'tests', '### (R268)(2): the splitter`s.'),
    ('kernel files of SIDE-lv-conservation edited', 0, 0, 'files', '### (R268)(2): the two emphases listed, not edited.'),
    ('standing arms added', 0, 0, 'arms', '### (R264)(2): the standing arms frozen.'),
    ('mirror exports built', 0, 0, 'exports', '### not ruled this act.'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R268).'),
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
# ### before the spec is emitted; a reader that raises, or returns nothing, refuses the spec.
PLANTED = [
    ('runner row', 'read_runner_row', dict(kernel='SIDE-x', branch='b999-planted', ref='0' * 40, target='X.Y', run_id=1, conclusion='success',
                                           artifact_sha256='0' * 64, mem_low=9000, stopped=False, gate='DERIVES', merged=None, tag=None)),
    ('runner row, stopped on the runner', 'read_runner_row', dict(kernel='SIDE-x', branch='b999-planted', ref='0' * 40, target='X.Y', run_id=2,
                                                                   conclusion='failure', artifact_sha256=None, mem_low=2400, stopped=True,
                                                                   gate=None, merged=None, tag=None)),
    ('score row', 'read_score_row', ('N3', ['REFUTED IN ONE CLAUSE', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the kernel`s runner, the author`s word'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the runner`s gate readings'),
    ('trace row', 'read_trace_row', '  H7  θ : ℝ, hθ0 : 0 ≤ θ -- CONSUMED AT RateIndex.lean :40, :130 -- a planted trace'),
    ('trace row consumed at no line', 'read_trace_row', '  H12  the planted binder -- CONSUMED AT NO LINE -- a planted reason'),
]


def planted():
    """each planted row through its reader; a head is first landed in a scratch ledger by the one conversion's append_to, then read by
    read_head. Returns [(shape, ok, what)]."""
    import tempfile
    import b658_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b658_spec_') as d:
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
    print('b658_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    import b658_record as REC
    ctl = []
    for what, f in (('a runner row missing its keys (b652`s build-row shape)', lambda: REC.read_runner_row(dict(target='X.Y', slot_seen=1, needed=1))),
                    ('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b658_ferry.txt'), '### b999 absent')),
                    ('a trace row with no consuming line', lambda: REC.read_trace_row('  H1  H -- consumed somewhere')),
                    ('a trace row naming no hypothesis', lambda: REC.read_trace_row('  X1  H -- CONSUMED AT RateIndex.lean :37 -- x'))):
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
    tests = jcount('b658_tests_stepzero.json', len)
    rows = lambda j: j.get('rows') or []   # noqa: E731
    dispatches = jcount('b658_runner_rows.json', lambda j: sum(1 for r in rows(j) if r.get('run_id')))
    merges = jcount('b658_runner_rows.json', lambda j: sum(1 for r in rows(j) if r.get('merged')))
    files = len([x for x in subprocess.run(['git', '-C', 'D:/SIDE-explicit-formula', 'diff', '--name-only', '111e418', 'main'], capture_output=True,
                                           text=True).stdout.split(chr(10)) if x.strip()])
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b658_author_answers.txt'), encoding='utf-8').read(), re.M))
    except Exception:
        questions = 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests,
                    QUESTIONS=questions, DISPATCHES=dispatches, MERGES=merges, FILES=files)
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'DISPATCHES', 'MERGES', 'FILES'):
        print('      %-10s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b658_registration_2026-10-12.txt -- b658, LANE TWO ACT EIGHTY-FIVE, THE RESEARCH ACT: b657 AT ITS WEIGHT; "
                             "THE SPLITTER REPAIRED; E1 OVER A CONFIGURATION STATED, BUILT ON THE RUNNER AND MERGED, UNDER (R268)"),
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
