# -*- coding: utf-8 -*-
"""b661_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b659's spec by the Write tool, every clause re-written against this face: the record line; the binding re-read and its
### ### one prompt before any number; the precision rung asked of the author; the map's cells, each with its certifications; the control
### ### beside the map; the dry-run step of the registration gate; no kernel edit; nothing deposits. The planted rows of (R263)(3) carried
### ### for this act's readers, a map cell row among them.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b661_registration_2026-10-13.txt')
SPEC = os.path.join(ROOT, 'data', 'b661_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (Z).'),
    ('kernel files written', 0, 0, 'files', '### (R271)(6), N1.'),
    ('runner dispatches', 0, 0, 'dispatches', '### (R271)(6): no kernel edit, no build.'),
    ('merges made', 0, 0, 'merges', '### (R271)(6).'),
    ('kernel tags made', 0, 0, 'tags', '### (R271)(6).'),
    ('binding banks committed alone before the prompt', 1, 1, 'banks', '### (R271)(3).'),
    ('quantities left unbound', 0, 0, 'quantities', '### (R271)(3), N2.'),
    ('numbers computed before the author`s word', 0, 0, 'numbers', '### (R271)(3), N2.'),
    ('map scripts written under tools/', 1, 1, 'scripts', '### the ferry, Component 3.'),
    ('map cells banked', 'CELLS', 'CELLS', 'cells', '### (R271)(4), MEASURED off the map bank.'),
    ('indices printed beside an uncertified hypothesis', 0, 0, 'indices', '### N3.'),
    ('readings outside the three forms of (R271)(4)', 0, 0, 'readings', '### H1, the author`s word.'),
    ('controls banked beside the map, not readings', 1, 1, 'controls', '### the house standard: an absence carries a control.'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### (R271)(6).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### none on this host at all.'),
    ('record lines landed before the seal', 1, 1, 'lines', '### (R271)(1).'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('shared tools edited', 0, 0, 'tools', '### (Z).'),
    ('standing arms added', 0, 0, 'arms', '### (R264)(2): the standing arms frozen.'),
    ('holds changed', 0, 0, 'holds', '### the hold stays at 2,560 MB on every host.'),
    ('navigator files read or written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('verdict names minted by the seat', 0, 0, 'verdicts', '### (Z).'),
    ('claims about RH or any zero beyond a compiled statement', 0, 0, 'claims', '### section (A).'),
    ('claims about ζ drawn from Z₁', 0, 0, 'claims', '### (R271)(2).'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### (Z).'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### G-SEAL-HASHES.'),
    ('banks the act root names written after it', 0, 0, 'banks', '### (R251)(3).'),
    ('banks the act root names written with CR LF', 0, 0, 'banks', '### the author`s answer at b644.'),
    ('act-root verifies outside the suite', 0, 0, 'verifies', '### the ferry.'),
    ('expectations registered', 'EXPECT', 'EXPECT', 'expectations', '### sections (D), (D2) and (E), MEASURED off the face.'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R271).'),
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
_CERTS = [['H.hev', 'CERTIFIED', 'planted'], ['H.hM', 'CERTIFIED', 'planted']]
PLANTED = [
    ('runner row', 'read_runner_row', dict(kernel='SIDE-x', branch='b999-planted', ref='0' * 40, target='X.Y', run_id=1, conclusion='success',
                                           artifact_sha256='0' * 64, mem_low=9000, stopped=False, gate='DERIVES', merged=None, tag=None)),
    ('runner row, stopped on the runner', 'read_runner_row', dict(kernel='SIDE-x', branch='b999-planted', ref='0' * 40, target='X.Y', run_id=2,
                                                                   conclusion='failure', artifact_sha256=None, mem_low=2400, stopped=True,
                                                                   gate=None, merged=None, tag=None)),
    ('score row', 'read_score_row', ('N3', ['REFUTED IN ONE CLAUSE', 'a planted score text'])),
    ('score row of a hypothesis, vacuous', 'read_score_row', ('H2', ['HELD, VACUOUS', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the kernel`s map, the author`s word'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the map`s cells'),
    ('map cell row with an index', 'read_map_cell', dict(sigma='0.7', t='50.0', certs=_CERTS, reading='j₀ = 30', j0=30)),
    ('map cell row, NONE', 'read_map_cell', dict(sigma='0.7', t='50.0', certs=_CERTS, reading='NONE ≤ J_max')),
    ('map cell row, HYP-UNVERIFIED', 'read_map_cell', dict(sigma='0.7', t='50.0', certs=_CERTS + [['hθ', 'NOT CERTIFIED', 'planted']],
                                                           reading='HYP-UNVERIFIED(hθ)')),
]


def planted():
    """each planted row through its reader; a head is first landed in a scratch ledger by the one conversion's append_to, then read by
    read_head. Returns [(shape, ok, what)]."""
    import tempfile
    import b661_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b661_spec_') as d:
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
    print('b661_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    import b661_record as REC
    ctl = []
    for what, f in (('a runner row missing its keys (b652`s build-row shape)', lambda: REC.read_runner_row(dict(target='X.Y', slot_seen=1, needed=1))),
                    ('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b661_ferry.txt'), '### b999 absent')),
                    ('a map cell whose reading is of another form', lambda: REC.read_map_cell(dict(sigma='0.7', t='50.0', certs=_CERTS, reading='HOLDS'))),
                    ('a map cell with no certifications', lambda: REC.read_map_cell(dict(sigma='0.7', t='50.0', certs=[], reading='NONE ≤ J_max'))),
                    ('a map cell with an index and no j0', lambda: REC.read_map_cell(dict(sigma='0.7', t='50.0', certs=_CERTS, reading='j₀ = 30')))):
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
    tests = jcount('b661_tests_stepzero.json', len)
    cells = jcount('b661_detection_map.json', lambda j: len(j.get('cells') or []))
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b661_author_answers.txt'), encoding='utf-8').read(), re.M))
    except Exception:
        questions = 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S|H)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests,
                    QUESTIONS=questions, CELLS=cells)
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'CELLS'):
        print('      %-10s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b661_registration_2026-10-13.txt -- b661, LANE TWO ACT EIGHTY-EIGHT, THE RESEARCH ACT: b660 AT ITS WEIGHT; "
                             "THE BINDING RE-READ AT v0.28; THE DETECTION-INDEX MAP AT Z1 WITH EVERY HYPOTHESIS CERTIFIED PER CELL, UNDER (R271)"),
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
