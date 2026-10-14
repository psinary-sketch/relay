# -*- coding: utf-8 -*-
"""b670_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b669's spec by the Write tool, every clause re-written against this face: the citation check as a gate step and on
### ### mid-act answers; the weight line; the ten acts, the four readings, the methods, the items; one outbound search; no build, no merge,
### ### no tag, no kernel byte; the mirror export; nothing deposits. The planted rows of (R263)(3) carried for this act's readers.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b670_registration_2026-10-14.txt')
SPEC = os.path.join(ROOT, 'data', 'b670_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N4, N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('kernel bytes written', 0, 0, 'bytes', '### N1, (R280)(6).'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (R263)(4).'),
    ('citation checks run before the ferry was banked', 1, 1, 'checks', '### the gate step, standing from b662.'),
    ('citation misses repaired silently', 0, 0, 'misses', '### N2.'),
    ('mid-act citation checks appended', 'MIDS', 'MIDS', 'checks', '### (R278)(4), MEASURED off the bank.'),
    ('requests to the arXiv listing API', 1, 1, 'requests', '### (R280)(5), item 1`s trigger (a), once.'),
    ('runner dispatches', 0, 0, 'dispatches', '### no build in this act.'),
    ('merges made', 0, 0, 'merges', '### no build in this act.'),
    ('kernel tags made', 0, 0, 'tags', '### no build in this act.'),
    ('ten-act rows banked', 'ACTS', 'ACTS', 'rows', '### (R280)(2), MEASURED off the bank.'),
    ('method rows banked', 'METHODS', 'METHODS', 'rows', '### (R280)(4) and the answer on the methods table, MEASURED.'),
    ('readings banked of the four', 'READS', 'READS', 'readings', '### (R280)(3), MEASURED: the four banks present.'),
    ('cells written without a cite', 0, 0, 'cells', '### N2.'),
    ('kinds or methods supplied from outside the banks', 0, 0, 'kinds', '### N2.'),
    ('sentences saying the corpus is consistent', 0, 0, 'sentences', '### N3.'),
    ('kernel files named by a constant', 0, 0, 'constants', '### (R274)(4), standing.'),
    ('declared suite failures carried at the close', 0, 0, 'failures', '### (G2).'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### the ferry.'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('environment variables set or cleared by the seat', 0, 0, 'variables', '### the ferry: left as they are.'),
    ('record lines landed before the seal', 5, 5, 'lines', '### (R280)(1) the weight line; (5) the four OPEN_TRAILS lines.'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('mirror exports built', 1, 1, 'exports', '### (R280)(7), after the last PLACE-papers push.'),
    ('shared tools edited', 0, 0, 'tools', '### (Z).'),
    ('standing arms added', 0, 0, 'arms', '### (R264)(2): the standing arms frozen.'),
    ('holds changed', 0, 0, 'holds', '### the hold stays at 2,560 MB on every host.'),
    ('navigator files read or written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z): a status the reader cannot find reads NOT STATED.'),
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
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z), N5.'),
    ('TECHNE_TOOLKIT lines banked beyond its name and counts', 0, 0, 'lines', '### N5.'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R280).'),
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
    ('score row', 'read_score_row', ('N3', ['HELD', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the kernel`s reading, the author`s word'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the reading`s four figures'),
    ('act row', 'read_act_row', dict(act='b661', cells=dict(lane=dict(value='LANE TWO', cite='data/b661_closing.txt :3')))),
    ('method row, READY', 'read_method_row', dict(method='a planted method', acts=['b998', 'b999'], banks=['b999_x.txt'],
                                                  defects=['b999 (a) data/b999_defects.txt :1'], reading='READY')),
    ('method row, NOT YET USED TWICE', 'read_method_row', dict(method='a planted method', acts=['b999'], banks=['b999_x.txt'], defects=[],
                                                               reading='NOT YET USED TWICE')),
    ('order row', 'read_order_row', dict(name='W-ORD-PLANTED', line=1, act='b999', status='NOT STATED', age=0)),
]


def planted():
    """each planted row through its reader; a head is first landed in a scratch ledger by the one conversion's append_to, then read by
    read_head. Returns [(shape, ok, what)]."""
    import tempfile
    import b670_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b670_spec_') as d:
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
    print('b670_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    import b670_record as REC
    ctl = []
    for what, f in (('a runner row missing its keys (b652`s build-row shape)', lambda: REC.read_runner_row(dict(target='X.Y', slot_seen=1, needed=1))),
                    ('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b670_ferry.txt'), '### b999 absent')),
                    ('an act row with a cell without its cite', lambda: REC.read_act_row(dict(act='b661', cells=dict(lane=dict(value='x', cite=''))))),
                    ('a method row whose reading the cells do not give', lambda: REC.read_method_row(dict(method='x', acts=['b999'], banks=['x'],
                                                                                                         defects=['d'], reading='READY'))),
                    ('an order row without its age', lambda: REC.read_order_row(dict(name='W-ORD-X', line=1, status='OPEN')))):
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
    tests = jcount('b670_tests_stepzero.json', len)
    acts = jcount('b670_ten_acts.json', lambda j: len(j.get('rows') or []))
    methods = jcount('b670_methods.json', lambda j: len(j.get('rows') or []))
    reads = sum(1 for b in ('b670_licensed_table.json', 'b670_correspondence.json', 'b670_ceiling.json', 'b670_work_orders.json')
                if os.path.exists(os.path.join(ROOT, 'data', b)))
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b670_author_answers.txt'), encoding='utf-8').read(), re.M))
    except Exception:
        questions = 0
    try:
        mids = len(re.findall(r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', io.open(os.path.join(ROOT, 'data', 'b670_citation_check.txt'),
                                                                                          encoding='utf-8').read()))
    except Exception:
        mids = 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests,
                    QUESTIONS=questions, ACTS=acts, METHODS=methods, READS=reads, MIDS=mids)
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'ACTS', 'METHODS', 'READS', 'MIDS'):
        print('      %-10s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b670_registration_2026-10-14.txt -- b670, LANE ONE ACT NINETY-SEVEN, THE READING ACT: b669 AT ITS WEIGHT; THE TEN "
                             "ACTS b660-b669; THE FOUR READINGS, READING 1 OF 2; THE METHODS; THE ITEMS; NO KERNEL BYTE, UNDER (R280)"),
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
