# -*- coding: utf-8 -*-
"""b663_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b662's spec by the Write tool, every clause re-written against this face: the citation check as a gate step; the
### ### record lines; the plan before any Lean; the instance on named premises on a branch, the one dispatch, the merge on its gate reading;
### ### the one tool edit by ruling (the E0 rule's MET line); the computation at the real configuration; the dry-run step; nothing deposits.
### ### The planted rows of (R263)(3) carried for this act's readers, a score row of H1-H4, the instance bank and a computation cell among them.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b663_registration_2026-10-13.txt')
SPEC = os.path.join(ROOT, 'data', 'b663_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (R263)(4).'),
    ('citation checks run before the ferry was banked', 1, 1, 'checks', '### the gate step, standing from b662.'),
    ('citation misses repaired silently', 0, 0, 'misses', '### N2.'),
    ('plan prompts raised before any Lean', 1, 1, 'prompts', '### (R273)(3).'),
    ('rungs built', 0, 0, 'rungs', '### (R273)(3) and the author`s word: all five priced.'),
    ('runner dispatches', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### (R273)(2), (5): one, MEASURED off the instance bank.'),
    ('merges made', 'MERGES', 'MERGES', 'merges', '### (R273)(5): alone on its gate reading, MEASURED.'),
    ('kernel tags made', 'MERGES', 'MERGES', 'tags', '### one per merge, at the next in its series.'),
    ('kernel .lean files written on a main outside a merge', 0, 0, 'files', '### N5.'),
    ('sorry written in a kernel', 0, 0, 'sorries', '### N2.'),
    ('premises proved', 0, 0, 'premises', '### N2: stated, not proved; open.'),
    ('kernel bytes written before the author`s word on the plan', 0, 0, 'bytes', '### (R273)(3).'),
    ('computation cells banked', 'CELLS', 'CELLS', 'cells', '### (R273)(4): the control and Q0, MEASURED off the bank.'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### (Z).'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('lean calls made after the seal', 0, 0, 'calls', '### none on this host at all.'),
    ('record lines landed before the seal', 3, 3, 'lines', '### (R273)(1) and the author`s two work-orders.'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('mirror exports built', 0, 0, 'exports', '### not ruled this act.'),
    ('shared tools edited', 1, 1, 'tools', '### the author`s word on Component 3: tools/e0_rule.py`s MET line, by ruling.'),
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
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A); the MET line by the author`s ruling.'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R273).'),
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
_IROW = dict(name='SIDEExplicitFormula.Schema.planted', axioms=['propext'], std3=True, grade='INTERFACES')
PLANTED = [
    ('score row', 'read_score_row', ('N3', ['HELD ON THE RE-GRADE', 'a planted score text'])),
    ('score row of H4', 'read_score_row', ('H4', ['HELD ON B1', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the kernel`s runner, the author`s word'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the runner`s gate readings'),
    ('instance bank', 'read_instance', dict(run=dict(run_id=1), conclusion='success', sha256='0' * 64, sha_ok=True, mem_low=9000, build_exit='0',
                                            errors=[], rows=[_IROW], H1=True, H2=True, landing='planted')),
    ('control cell with an index', 'read_control_cell', dict(name='Q0 AT planted', base=['0.9', '16.3'], certs=_CERTS, reading='j₀ = 38', j0=38,
                                                            zero_side=dict(held=True))),
    ('control cell with no index', 'read_control_cell', dict(name='THE CONTROL planted', base=['0.8', '29.6'], certs=_CERTS, reading='NONE ≤ J_max')),
]


def planted():
    """each planted row through its reader; a head is first landed in a scratch ledger by the one conversion's append_to, then read by
    read_head. Returns [(shape, ok, what)]."""
    import tempfile
    import b663_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b663_spec_') as d:
                    led = os.path.join(d, 'LEDGER.md')
                    open(led, 'wb').write(b'# a scratch ledger\n')
                    REC.append_to(led, '\n' + row + ': planted.\n')
                    got = fn(led, row)
            elif reader == 'read_score_row':
                got = fn(*row)
            else:
                got = fn(row)
            out.append((shape, got is not None, repr(got)[:120]))
        except Exception as e:
            out.append((shape, False, '%s: %s' % (type(e).__name__, str(e)[:100])))
    return out


def count_arms(text):
    return len(set(re.findall(r'\b[GF]-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b663_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    import b663_record as REC
    ctl = []
    for what, f in (('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b663_ferry.txt'), '### b999 absent')),
                    ('an instance bank without its keys', lambda: REC.read_instance(dict(run={}, rows=[]))),
                    ('a control cell with no certifications', lambda: REC.read_control_cell(dict(name='x', base=['0.8', '29.6'], certs=[],
                                                                                                 reading='NONE ≤ J_max')))):
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
    tests = jcount('b663_tests_stepzero.json', len)
    dispatches = jcount('b663_epstein_instance.json', lambda j: 1 if (j.get('run') or {}).get('run_id') else 0)
    merges = jcount('b663_epstein_instance.json', lambda j: 1 if j.get('merged') else 0)
    cells = jcount('b663_epstein_control.json', lambda j: len(j.get('cells') or []))
    try:
        questions = len(re.findall(r'^### PROMPT ', io.open(os.path.join(ROOT, 'data', 'b663_author_answers.txt'), encoding='utf-8').read(), re.M))
    except Exception:
        questions = 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)), TESTS=tests,
                    QUESTIONS=questions, DISPATCHES=dispatches, MERGES=merges, CELLS=cells)
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'DISPATCHES', 'MERGES', 'CELLS'):
        print('      %-10s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b663_registration_2026-10-13.txt -- b663, LANE TWO ACT NINETY, THE RESEARCH ACT: b662 AT ITS WEIGHT; THE "
                             "EPSTEIN RUNGS READ AND THE PLAN RAISED; THE Q0 CONFIGURATION BUILT ON PREMISES; THE DETECTOR AND THE RATE INDEX "
                             "AT THE REAL CONFIGURATION, UNDER (R273)"),
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
