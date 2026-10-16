# -*- coding: utf-8 -*-
"""b673_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b672's spec by the Write tool, every clause re-written against this face: the citation check as a gate step and on
### ### mid-act answers; the record lines; the plan and the control before any Lean; the attempt on the branch, its dispatches one per tree
### ### state, the landing, the walk, H5; the merge and its tag; no build on this host; no outbound search; nothing deposits. The planted
### ### rows of (R263)(3) carried for this act's readers, the landing row among them.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b673_registration_2026-10-16.txt')
SPEC = os.path.join(ROOT, 'data', 'b673_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched, the draft at v5.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('kernel mains moved but by the merges of Component 4', 0, 0, 'moves', '### N5.'),
    ('kernel files written beyond the branch files', 0, 0, 'files', '### N5.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (R263)(4).'),
    ('citation checks run before the ferry was banked', 1, 1, 'checks', '### the gate step, standing from b662.'),
    ('citation misses repaired silently', 0, 0, 'misses', '### the gate step.'),
    ('mid-act citation checks appended', 'MIDS', 'MIDS', 'checks', '### (R278)(4), MEASURED off the bank.'),
    ('requests to an outside search service', 0, 0, 'requests', '### no search is ordered in this act.'),
    ('runner dispatches, one per tree state', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### (R283)(5), rules row 1, MEASURED off the runner bank.'),
    ('declarations landed DERIVES', 'DERIVES', 'DERIVES', 'declarations', '### N3, MEASURED off the landing bank.'),
    ('declarations left open on main', 0, 0, 'declarations', '### N3.'),
    ('sorry in code on main in the act`s files', 0, 0, 'lines', '### N3.'),
    ('merges made', 1, 1, 'merges', '### Component 4.'),
    ('kernel tags made', 1, 1, 'tags', '### Component 4: v0.32.'),
    ('ζ objects in the closure of S5 at the tip', 0, 0, 'objects', '### N4, H3.'),
    ('statements printed side by side for H5', 2, 2, 'statements', '### N4, H5.'),
    ('prompts raised before any Lean on the plan', 1, 1, 'prompts', '### (R283)(3).'),
    ('control signs printed with their least n before any Lean', 2, 2, 'signs', '### N2, H6.'),
    ('kernel files named by a constant', 0, 0, 'constants', '### (R274)(4), standing.'),
    ('declared suite failures carried at the close', 'CARRIED', 'CARRIED', 'failures', '### (G2), MEASURED off the face`s declaration line.'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### (R283)(6): the drafts written to no keystone.'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('environment variables set or cleared by the seat', 0, 0, 'variables', '### the ferry: left as they are.'),
    ('record lines landed before the seal', 'LINES', 'LINES', 'lines', '### (R283)(1) and Component 4; MEASURED.'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('mirror exports built', 1, 1, 'exports', '### at the close, after the last PLACE-papers push.'),
    ('shared tools edited', 0, 0, 'tools', '### (Z).'),
    ('standing arms added', 0, 0, 'arms', '### (R264)(2): the standing arms frozen.'),
    ('holds changed', 0, 0, 'holds', '### the hold stays at 2,560 MB on every host.'),
    ('navigator files read or written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
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
    ('README or REGISTRY edits', 0, 0, 'edits', '### the ferry: README and REGISTRY unwritten.'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A).'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### MEASURED off the bank.'),
    ('questions asked of the author before the seal', 'QUESTIONS', 'QUESTIONS', 'questions', '### MEASURED off the answers bank.'),
    ('questions asked of the author after the root', 0, 0, 'questions', '### the answers bank is root-named.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0).'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R283).'),
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
    ('score row', 'read_score_row', ('H6', ['HELD', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the converse`s landing, the author`s word'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the walk`s 254 declarations'),
    ('landing row (the landing bank`s shape)', 'read_landing_row', dict(name='X.y', landing='DERIVES', axioms=[], file='X.lean', line=1, obstruction=None)),
    ('narrowed square row (b671`s list, the control`s input)', 'read_square_row', dict(kind='OFF', idx=0, re='0.95', im='16.29', h='1e-30', count=1)),
]


def planted():
    """each planted row through its reader; a head is first landed in a scratch ledger by the one conversion's append_to, then read by
    read_head. Returns [(shape, ok, what)]."""
    import tempfile
    import b673_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b673_spec_') as d:
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


def carried(text):
    """the arms the face declares failing on real state before the lock, by name: the backticked arm names on its declaration line."""
    m = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(text.split()))
    return len(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', m.group(1)))) if m else 0


def main(argv):
    print('=' * 100)
    print('b673_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    import b673_record as REC
    ctl = []
    for what, f in (('a runner row missing its keys (b652`s build-row shape)', lambda: REC.read_runner_row(dict(target='X.Y', slot_seen=1, needed=1))),
                    ('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b673_ferry.txt'), '### b999 absent')),
                    ('a landing row of another landing', lambda: REC.read_landing_row(dict(name='X.y', landing='MERGED'))),
                    ('an open landing without its obstruction', lambda: REC.read_landing_row(dict(name='X.y', landing='NOT COMPILED',
                                                                                                   obstruction=None))),
                    ('a square row of count two', lambda: REC.read_square_row(dict(kind='ON', idx=1, re='0.5', im='14', h='1e-9', count=2)))):
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

    def tcount(name, pat):
        try:
            return len(re.findall(pat, io.open(os.path.join(ROOT, 'data', name), encoding='utf-8').read(), re.M))
        except Exception:
            return 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)),
                    TESTS=jcount('b673_tests_stepzero.json', len), QUESTIONS=tcount('b673_author_answers.txt', r'^### PROMPT '),
                    MIDS=tcount('b673_citation_check.txt', r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+'),
                    LINES=sum(jcount(b, lambda j: len(j.get('lines') or [])) for b in ('b673_record_lines.json', 'b673_record_lines_c4.json')),
                    DISPATCHES=jcount('b673_runner_rows.json', lambda j: len(j.get('rows') or [])),
                    DERIVES=jcount('b673_landing.json', lambda j: sum(1 for r in j.get('rows') or [] if r.get('landing') == 'DERIVES')),
                    CARRIED=carried(text))
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'MIDS', 'LINES', 'DISPATCHES', 'DERIVES', 'CARRIED'):
        print('      %-10s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b673_registration_2026-10-16.txt -- b673, LANE TWO ACT ONE HUNDRED, THE RESEARCH ACT: b672 AT ITS WEIGHT; "
                             "V4 AND V5 ON THE CONFIGURATION; THE GENERIC LI CONVERSE, THE χ CONVERSE AND THE χ-LI EQUIVALENCE; THE NATIVE "
                             "ζ CONVERSE BESIDE THE VENDORED ONE; v0.32, UNDER (R283)"),
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
