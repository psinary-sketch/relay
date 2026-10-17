# -*- coding: utf-8 -*-
"""b675_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b674's spec by the Write tool, every clause re-written against this face: the citation check as a gate step and on
### ### mid-act answers; the record line and the corrigenda; the hypotheses read before any sum; the plan raised before any sum; the bench
### ### and its controls in the foreground in parts; the closing tool's repairs and its dry run as a gate step; no build on this host;
### ### nothing deposits. The planted rows of (R263)(3) carried for this act's readers, the bench row's shape among them.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b675_registration_2026-10-16.txt')
SPEC = os.path.join(ROOT, 'data', 'b675_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched, the draft at v5.'),
    ('identifiers of the author placed in an outbound request', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('kernel mains moved', 0, 0, 'moves', '### N5.'),
    ('kernel files written', 0, 0, 'files', '### N5.'),
    ('runner dispatches', 0, 0, 'dispatches', '### no build ordered in this act.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (Z).'),
    ('citation checks run before the ferry was banked', 1, 1, 'checks', '### the gate step, standing from b662.'),
    ('citation misses repaired silently', 0, 0, 'misses', '### the gate step.'),
    ('mid-act citation checks appended', 'MIDS', 'MIDS', 'checks', '### (R278)(4), MEASURED off the bank.'),
    ('web searches whose query names the author', 0, 0, 'searches', '### N5: one search, the theorem`s words alone.'),
    ('sums over the zeros computed before the plan`s prompt was answered', 0, 0, 'sums', '### (R285)(6).'),
    ('off-line real parts printed from the balls', 'REALPARTS', 'REALPARTS', 'parts', '### (R285)(5), MEASURED off the hypotheses bank.'),
    ('bench parts run in the foreground', 'PARTS', 'PARTS', 'parts', '### (R285)(7) and the plan`s section 6, MEASURED off the constants bank.'),
    ('bench parts run detached', 0, 0, 'parts', '### the ferry: foreground under the 600 s limit.'),
    ('bench rows banked', 'BENCHROWS', 'BENCHROWS', 'rows', '### MEASURED off the bench bank.'),
    ('signs UNDECIDED in the bench', 0, 0, 'signs', '### N3, MEASURED off the bench bank.'),
    ('controls banked', 3, 3, 'controls', '### C2`, C2 and H6 by the navigator`s answer on the control.'),
    ('closing-tool repairs at carry', 4, 4, 'repairs', '### (R285)(2): three readings and the capture naming.'),
    ('closing dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R285)(2) rule row 1.'),
    ('rules banked', 'RULES', 'RULES', 'rules', '### MEASURED off the rules bank.'),
    ('branches deleted beyond the ruling`s list', 0, 0, 'branches', '### (R285)(3).'),
    ('remote branches deleted', 2, 2, 'branches', '### (R285)(3): SIDE-window recut-window-b674, SIDE-explicit-formula chi-li-b669.'),
    ('declared suite failures carried at the close', 'CARRIED', 'CARRIED', 'failures', '### (G2), MEASURED off the face`s declaration line.'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### (R285)(10).'),
    ('faces-page lines written', 0, 0, 'lines', '### (R285)(8): the H1-fails landing writes no bench line.'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('environment variables set or cleared by the seat', 0, 0, 'variables', '### the ferry: left as they are.'),
    ('record lines landed before the seal', 'LINES', 'LINES', 'lines', '### (R285)(1); MEASURED.'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('mirror exports built', 0, 0, 'exports', '### none ordered in this act.'),
    ('shared tools edited', 0, 0, 'tools', '### (Z).'),
    ('standing arms added', 0, 0, 'arms', '### (R264)(2): the standing arms frozen.'),
    ('holds changed', 0, 0, 'holds', '### the hold stays at 2,560 MB on every host.'),
    ('navigator files read or written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('claims about RH or any zero beyond a compiled statement or the certified list', 0, 0, 'claims', '### section (A).'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R285).'),
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
    ('score row', 'read_score_row', ('H3', ['REFUTED AT EVERY n', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the kernel`s class read at the object`s balls'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the bound`s onset, were its hypothesis to hold'),
    ('branch row (the branches bank`s shape)', 'read_branch_row', dict(repo='D:/x', branch='push-b999', where='remote', tip='0' * 40, merged=True,
                                                                        fate='DELETED')),
    ('bench row (the bench bank`s shape)', 'read_bench_row', dict(n=63709, P='[-1.7e+46 +/- 4.1e+31]', U='[5.8e9 +/- 1e-3]',
                                                                  PU='[-1.7e+46 +/- 4.1e+31]', sign='NEG', rad=4.07e31)),
    ('runner row (the last merged run`s bank)', 'read_runner_row', dict(kernel='SIDE-window', label='after', ref='0' * 40, run_id=1, gate='DERIVES')),
]


def planted():
    """each planted row through its reader; a head is first landed in a scratch ledger by the one conversion's append_to, then read by
    read_head. Returns [(shape, ok, what)]."""
    import tempfile
    import b675_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b675_spec_') as d:
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
    print('b675_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    import b675_record as REC
    ctl = []
    for what, f in (('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b675_ferry.txt'), '### b999 absent')),
                    ('a branch row with no side', lambda: REC.read_branch_row(dict(repo='D:/x', branch='b', tip='0' * 40, fate='DELETED'))),
                    ('a bench row with a point value for P', lambda: REC.read_bench_row(dict(n=1, P='1.0', U='1', PU='[1 +/- 1]', sign='NEG', rad=1.0))),
                    ('a bench row with another sign word', lambda: REC.read_bench_row(dict(n=1, P='[1 +/- 1]', U='1', PU='[1 +/- 1]', sign='MAYBE', rad=1.0))),
                    ('a runner row of another kernel', lambda: REC.read_runner_row(dict(kernel='SIDE-x', label='after', ref='0' * 40, run_id=1,
                                                                                       gate='DERIVES')))):
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
                    TESTS=jcount('b675_tests_stepzero.json', len), QUESTIONS=tcount('b675_author_answers.txt', r'^### PROMPT '),
                    MIDS=tcount('b675_citation_check.txt', r'ANSWER CITES CHECKED \d+ ; OK \d+ ; MISSES \d+'),
                    LINES=jcount('b675_record_lines.json', lambda j: len(j.get('lines') or [])),
                    REALPARTS=jcount('b675_hypotheses.json', lambda j: len(j.get('points') or [])),
                    PARTS=jcount('b675_li_constants.json', lambda j: len(j.get('parts') or {})),
                    BENCHROWS=jcount('b675_li_bench.json', lambda j: len(j.get('rows') or [])),
                    RULES=tcount('b675_rules.txt', r'^  \(\d+\) '),
                    CARRIED=carried(text))
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'MIDS', 'LINES', 'REALPARTS', 'PARTS', 'BENCHROWS', 'RULES', 'CARRIED'):
        print('      %-10s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b675_registration_2026-10-16.txt -- b675, LANE TWO ACT ONE HUNDRED AND TWO, THE RESEARCH ACT: b674 AT ITS "
                             "WEIGHT; THE KERNEL`S HYPOTHESES READ AT Q0; THE COMPOSITION BOUND INSTANTIATED AND TESTED AGAINST THE "
                             "CERTIFIED ZEROS; THE CLOSING TOOL REPAIRED AT CARRY, UNDER (R285)"),
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
