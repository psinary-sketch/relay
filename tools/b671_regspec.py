# -*- coding: utf-8 -*-
"""b671_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b670's spec by the Write tool, every clause re-written against this face: the citation check as a gate step and on
### ### mid-act answers; the record lines; the plan, the narrowing, the controls, the map and its diagnostic run, the landing; no build, no
### ### merge, no tag, no kernel byte; no outbound search; nothing deposits. The planted rows of (R263)(3) carried for this act's readers.
"""
import io
import json
import gzip
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b671_registration_2026-10-14.txt')
SPEC = os.path.join(ROOT, 'data', 'b671_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched, the draft at v5.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('kernel bytes written', 0, 0, 'bytes', '### N1, (R281)(9).'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (R263)(4).'),
    ('citation checks run before the ferry was banked', 1, 1, 'checks', '### the gate step, standing from b662.'),
    ('citation misses repaired silently', 0, 0, 'misses', '### the gate step.'),
    ('mid-act citation checks appended', 'MIDS', 'MIDS', 'checks', '### (R278)(4), MEASURED off the bank.'),
    ('requests to an outside search service', 0, 0, 'requests', '### no search is ordered in this act.'),
    ('runner dispatches', 0, 0, 'dispatches', '### no build in this act.'),
    ('merges made', 0, 0, 'merges', '### no build in this act.'),
    ('kernel tags made', 0, 0, 'tags', '### no build in this act.'),
    ('narrowed points banked', 'POINTS', 'POINTS', 'points', '### (R281)(4), MEASURED off the narrowed list.'),
    ('on-line points narrowed at σ = ½ by sign', 'ON', 'ON', 'points', '### (R281)(6) H1, MEASURED off the log.'),
    ('off-line points narrowed by count', 'OFF', 'OFF', 'points', '### (R281)(6) H1, MEASURED off the log.'),
    ('points left UNRESOLVED-AT-DEPTH', 'UNRES', 'UNRES', 'points', '### (R281)(6) H1, MEASURED off the log.'),
    ('controls read as fixed before the first Q0 point', 2, 2, 'controls', '### (R281)(5) C1 and C2; N3.'),
    ('map runs on the narrowed balls', 1, 1, 'runs', '### (R281)(6) H3, once.'),
    ('diagnostic map runs with its prints alone changed', 1, 1, 'runs', '### the navigator`s answer on the landing.'),
    ('computation lines of the map changed', 0, 0, 'lines', '### N4.'),
    ('b667 banks edited', 0, 0, 'banks', '### N5.'),
    ('kernel files named by a constant', 0, 0, 'constants', '### (R274)(4), standing.'),
    ('declared suite failures carried at the close', 0, 0, 'failures', '### (G2).'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### the ferry.'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('environment variables set or cleared by the seat', 0, 0, 'variables', '### the ferry: left as they are.'),
    ('record lines landed before the seal', 'LINES', 'LINES', 'lines', '### (R281)(1), (2), (8) and (7); the two Bessel lines; MEASURED.'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('mirror exports built', 0, 0, 'exports', '### none is ordered under (R281).'),
    ('shared tools edited', 0, 0, 'tools', '### (Z).'),
    ('standing arms added', 0, 0, 'arms', '### (R264)(2): the standing arms frozen.'),
    ('holds changed', 0, 0, 'holds', '### the hold stays at 2,560 MB on every host.'),
    ('navigator files read or written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('verdict names minted by the seat', 0, 0, 'verdicts', '### (Z): INSTRUMENT and OBJECT are the navigator`s words.'),
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
    ('README or REGISTRY edits', 0, 0, 'edits', '### N5.'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A).'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### MEASURED off the bank.'),
    ('questions asked of the author before the seal', 'QUESTIONS', 'QUESTIONS', 'questions', '### MEASURED off the answers bank.'),
    ('questions asked of the author after the root', 0, 0, 'questions', '### the answers bank is root-named.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R281).'),
    ('patent-repo files created or edited', 0, 0, 'files', '### (W), N5.'),
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
    ('runner row (the last merged run`s shape)', 'read_runner_row', dict(kernel='SIDE-x', branch='b999-planted', ref='0' * 40, target='X.Y', run_id=1,
                                                                         conclusion='success', artifact_sha256='0' * 64, mem_low=9000, stopped=False,
                                                                         gate='DERIVES', merged=None, tag=None)),
    ('score row', 'read_score_row', ('H3', ['REFUTED', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the map`s reading, the author`s word'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the list`s 163 points'),
    ('square row (the narrowed list`s shape)', 'read_square_row', dict(kind='OFF', idx=0, re='0.66', im='33.65', h='1e-24', count=1)),
    ('narrow row (the log`s shape, ON narrowed by sign)', 'read_narrow_row', dict(kind='ON', idx=0, depth=40, reading='NARROWED', signs=[1, -1])),
]


def planted():
    """each planted row through its reader; a head is first landed in a scratch ledger by the one conversion's append_to, then read by
    read_head. Returns [(shape, ok, what)]."""
    import tempfile
    import b671_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b671_spec_') as d:
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
    print('b671_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    if not CNT.self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2
    P = planted()
    print('  ### (R263)(3) THE PLANTED ROWS, ONE PER SHAPE A SEALED ROUTE READS, EACH THROUGH THE RECORD TOOL`S READER:')
    for shape, ok, what in P:
        print('      %-50s %s -- %s' % (shape, 'READ' if ok else '### REFUSED', what))
    print('  ### ### **PLANTED ROWS %d ; READ %d ; REFUSED %d.**' % (len(P), sum(1 for p in P if p[1]), sum(1 for p in P if not p[1])))
    import b671_record as REC
    ctl = []
    for what, f in (('a runner row missing its keys (b652`s build-row shape)', lambda: REC.read_runner_row(dict(target='X.Y', slot_seen=1, needed=1))),
                    ('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b671_ferry.txt'), '### b999 absent')),
                    ('a square row at count 2', lambda: REC.read_square_row(dict(kind='OFF', idx=0, re='0.5', im='1', h='1e-24', count=2))),
                    ('an ON row narrowed without opposite signs', lambda: REC.read_narrow_row(dict(kind='ON', idx=0, depth=40, reading='NARROWED',
                                                                                                    signs=[1, 1])))):
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
    tests = jcount('b671_tests_stepzero.json', len)
    log = jcount('b671_narrow_log.json', lambda j: j.get('rows') or [])
    try:
        points = len(json.loads(gzip.decompress(open(os.path.join(ROOT, 'data', 'b671_epstein_zeros_narrowed.json.gz'), 'rb').read()))['rows'])
    except Exception:
        points = 0
    lines = sum(jcount(b, lambda j: len(j.get('lines') or [])) for b in ('b671_record_lines.json', 'b671_landing.json', 'b671_bessel_lines.json'))
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b671_author_answers.txt'), encoding='utf-8').read(), re.M))
    except Exception:
        questions = 0
    try:
        mids = len(re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', io.open(os.path.join(ROOT, 'data', 'b671_citation_check.txt'),
                                                                                          encoding='utf-8').read()))
    except Exception:
        mids = 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests,
                    QUESTIONS=questions, POINTS=points, ON=sum(1 for r in log if r['kind'] == 'ON' and r['reading'] == 'NARROWED'),
                    OFF=sum(1 for r in log if r['kind'] == 'OFF' and r['reading'] == 'NARROWED'),
                    UNRES=sum(1 for r in log if r['reading'] != 'NARROWED'), LINES=lines, MIDS=mids)
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'POINTS', 'ON', 'OFF', 'UNRES', 'LINES', 'MIDS'):
        print('      %-10s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b671_registration_2026-10-14.txt -- b671, LANE TWO ACT NINETY-EIGHT, THE RESEARCH ACT: b670 AT ITS WEIGHT; THE "
                             "SEQUENCE LINE; Q0`S POINTS NARROWED TO 10^-24; THE CONTROLS; THE b663 CONTROL ON THE NARROWED BALLS, H3 REFUTED; "
                             "NO KERNEL BYTE, UNDER (R281)"),
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
