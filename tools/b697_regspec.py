# -*- coding: utf-8 -*-
"""b697_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b696's spec by the Write tool, every clause re-written against this face: the citation check as a gate step; the record
### ### line; the faces rows and readings printed before any page, the prompt raised before any page write, the control byte for byte, the page
### ### by the generator in two lines; the tie rule printed before the name, the kernel cut in b676's form, the quotation search before the
### ### merge, the distance after at or below the distance before, no Correspondence cell by hand; the third face priced and not computed; the
### ### runner once per tree state and no lean; the suite in six parts, one call each; the mirror after the root; nothing deposits. The planted
### ### rows of (R263)(3) for this act's readers.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b697_registration_2026-10-21.txt')
SPEC = os.path.join(ROOT, 'data', 'b697_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched, the draft at v5.'),
    ('identifiers of the author placed in an outbound request or a workflow file', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('runner dispatches made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### the ferry: once per tree state, MEASURED off the command bank.'),
    ('runner dispatches of a tree already built', 0, 0, 'dispatches', '### the ferry.'),
    ('runner readings taken before the artifact`s sha256 agreed', 0, 0, 'readings', '### the ferry.'),
    ('faces rows printed before any page write', 4, 4, 'rows', '### N2, (R307)(2).'),
    ('pages written before the prompt was answered', 0, 0, 'pages', '### the ferry.'),
    ('controls re-emitting the committed page byte for byte', 1, 1, 'controls', '### N4.'),
    ('page lines differing from the committed page', 'PAGELINES', 'PAGELINES', 'lines', '### N4, MEASURED off the diff bank.'),
    ('node-list lines changed beyond :168', 0, 0, 'lines', '### (R307)(2).'),
    ('tie-break rules printed before the document was named', 1, 1, 'rules', '### N2, (R307)(3).'),
    ('documents cut', 1, 1, 'documents', '### (R307)(3).'),
    ('kernel declarations changed', 0, 0, 'declarations', '### b676`s form: comments only.'),
    ('prints differing before and after the cut', 0, 0, 'terminals', '### N3.'),
    ('quotation searches run after the merge', 0, 0, 'searches', '### N3, data/b690_rules.txt row (2).'),
    ('quoting lines entered as residues', 'RESIDUES', 'RESIDUES', 'lines', '### data/b690_rules.txt row (2), MEASURED off the cut bank.'),
    ('rows outside LICENSED/CITED after the cut', 'AFTER', 'AFTER', 'rows', '### N3, MEASURED off the cut bank.'),
    ('Correspondence cells written by hand', 0, 0, 'cells', '### N3.'),
    ('Correspondence cells written by the generator', 0, 0, 'cells', '### (R307)(3): a kernel`s cut.'),
    ('terms computed for the third face', 0, 0, 'terms', '### N5, (R307)(4).'),
    ('arithmetic-limit plans committed alone', 1, 1, 'plans', '### (R307)(4).'),
    ('shared tools edited', 0, 0, 'tools', '### N5.'),
    ('standing arms added', 0, 0, 'arms', '### N5.'),
    ('frozen banks edited', 0, 0, 'banks', '### (Z).'),
    ('outbound fetches by a tool of this act', 0, 0, 'fetches', '### N5.'),
    ('commits amended, rebased or rewritten', 0, 0, 'commits', '### data/b692_rules.txt row (1), the ferry.'),
    ('git writes sent two to a message', 0, 0, 'messages', '### the ferry; b694 (l).'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (Z).'),
    ('root-chain rows edited', 0, 0, 'rows', '### appended only.'),
    ('citation checks run at step zero', 1, 1, 'checks', '### the gate step, standing from b662; before any delete ((R307)(6)).'),
    ('citation misses repaired silently', 0, 0, 'misses', '### the gate step.'),
    ('citation misses raised before the component that cites them', 'MISSES', 'MISSES', 'misses', '### MEASURED off the citation bank.'),
    ('mid-act answers acted on before their check', 0, 0, 'answers', '### (R278)(4).'),
    ('answers acted on with their END marker unread', 0, 0, 'answers', '### the paste rule.'),
    ('sealed entries or faces edited in place', 0, 0, 'entries', '### (Z).'),
    ('scores read from a ledger line', 0, 0, 'scores', '### data/b686_rules.txt row (1).'),
    ('suite parts over 590 seconds', 0, 0, 'parts', '### standing.'),
    ('suite parts moved to the background', 0, 0, 'parts', '### data/b685_rules.txt row (1).'),
    ('suite parts sent two to a call', 0, 0, 'calls', '### data/b685_rules.txt row (1).'),
    ('commands carrying sed', 0, 0, 'commands', '### data/b685_rules.txt row (2).'),
    ('commands carrying a redirect', 'REDIRECTS', 'REDIRECTS', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('commands piping a read into a shell filter', 'PIPES', 'PIPES', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('commands running an interpreter`s one-line program', 'PYPROGS', 'PYPROGS', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('delete commands naming more than one branch or carrying a glob', 0, 0, 'commands', '### (R307)(5).'),
    ('delete commands with anything chained after', 0, 0, 'commands', '### data/b694_rules.txt row (1).'),
    ('deletes before the citation check', 0, 0, 'commands', '### (R307)(6), b695 (a).'),
    ('carry-time repairs', 'REPAIRS', 'REPAIRS', 'repairs', '### the ferry`s Component 5, MEASURED off the repairs bank.'),
    ('closing dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### b675 rules row 1.'),
    ('branches deleted beyond the ruling`s list', 0, 0, 'branches', '### (R307)(5).'),
    ('declared suite failures carried at the close', 'CARRIED', 'CARRIED', 'failures', '### (G2), MEASURED off the face`s declaration line.'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### (R307)(7).'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('environment variables set or cleared by the seat', 0, 0, 'variables', '### the ferry: left as they are.'),
    ('record lines landed before the seal', 'LINES', 'LINES', 'lines', '### (R307)(1); MEASURED.'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('mirror exports built', 1, 1, 'exports', '### the b670 form, after the root.'),
    ('holds changed', 0, 0, 'holds', '### the hold stays at 2,560 MB on every host.'),
    ('navigator files read or written', 0, 0, 'files', '### (Z).'),
    ('local intake banks committed', 0, 0, 'banks', '### (Z).'),
    ('Zeta23 or vendored files edited or added', 0, 0, 'files', '### (Z).'),
    ('worktrees made', 0, 0, 'worktrees', '### (Z).'),
    ('grade names minted by the seat', 0, 0, 'grades', '### (Z).'),
    ('status names minted by the seat', 0, 0, 'statuses', '### (Z).'),
    ('claims about RH or any zero', 0, 0, 'claims', '### section (A).'),
    ('rules struck, amended or widened by the seat', 0, 0, 'rules', '### section (A).'),
    ('locked faces edited', 0, 0, 'faces', '### (Z).'),
    ('own closing-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own suite edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('own record-tool edits after the seal', 0, 0, 'edits', '### OPEN_TRAILS :13307.'),
    ('sealed tools whose hash differs at the close', 0, 0, 'tools', '### G-SEAL-HASHES.'),
    ('banks the act root names written after it', 0, 0, 'banks', '### (R251)(3).'),
    ('banks the act root names not committed and pushed at its recorded commit', 0, 0, 'banks', '### G-ROOT-BANKS-COMMITTED.'),
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
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R307).'),
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


PLANTED = [
    ('score row', 'read_score_row', ('N3', ['HELD', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the kernel`s header re-cut, the page`s line regenerated'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the kernel`s header re-cut, the face`s plan priced'),
    ('branch row (the branches bank`s shape, a named local row deleted)', 'read_branch_row', dict(repo='D:/x', branch='push-b999-root', where='local',
                                                                                                tip='0' * 40, merged=True, fate='DELETED')),
    ('branch row (the branches bank`s shape, the remote row deleted)', 'read_branch_row', dict(repo='D:/x', branch='recut-x-b999', where='remote',
                                                                                             tip='0' * 40, merged=True, fate='DELETED')),
    ('table summary line (the per-document table`s shape)', 'read_table_sum',
     '### ### **SIDE-x: ROWS 5 ; MATCHES 4 ; UNDERSTATES 0 ; OVERREACHES 1 ; UNLICENSED 0 ; A ROW WITHOUT A VERDICT 0 ;**'),
    ('runner row (the runner rows bank`s shape)', 'read_runner_row', dict(kernel='SIDE-x', label='after', ref='0' * 40, run_id=1, gate='DERIVES')),
]


def planted():
    import tempfile
    import b697_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b697_spec_') as d:
                    led = os.path.join(d, 'LEDGER.md')
                    with open(led, 'wb') as fh:
                        fh.write(b'# a scratch ledger\n')
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
    m = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(text.split()))
    return len(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', m.group(1)))) if m else 0


def controls():
    import b697_record as REC
    ctl = []
    for what, f in (('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b697_ferry.txt'), '### b999 absent')),
                    ('a branch row with no side', lambda: REC.read_branch_row(dict(repo='D:/x', branch='b', tip='0' * 40, fate='DELETED'))),
                    ('a branch row with a fate of another name', lambda: REC.read_branch_row(dict(repo='D:/x', branch='b', where='local', tip='0' * 40,
                                                                                                fate='GONE'))),
                    ('a branch row with a short tip', lambda: REC.read_branch_row(dict(repo='D:/x', branch='b', where='remote', tip='0' * 7,
                                                                                     fate='DELETED'))),
                    ('a table summary of another shape', lambda: REC.read_table_sum('### ### **SIDE-x: ROWS five ;**')),
                    ('a runner row with a short ref', lambda: REC.read_runner_row(dict(kernel='SIDE-x', label='after', ref='0' * 7, run_id=1,
                                                                                       gate='DERIVES')))):
        try:
            f()
            ctl.append((what, False))
        except Exception:
            ctl.append((what, True))
    return ctl


def main(argv):
    print('=' * 100)
    print('b697_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    ctl = controls()
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

    def tfirst(name, pat, k=1):
        try:
            m = re.search(pat, io.open(os.path.join(ROOT, 'data', name), encoding='utf-8').read())
            return int(m.group(k)) if m else 0
        except Exception:
            return 0

    def tlines(name, pat):
        try:
            m = re.search(pat, io.open(os.path.join(ROOT, 'data', name), encoding='utf-8').read())
            return len([x for x in m.group(1).split(',') if x.strip()]) if m else 0
        except Exception:
            return 0
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)),
                    TESTS=jcount('b697_tests_stepzero.json', len), QUESTIONS=tcount('b697_author_answers.txt', r'^### PROMPT '),
                    LINES=jcount('b697_record_lines.json', lambda j: len(j.get('lines') or [])),
                    MISSES=tfirst('b697_citation_check.txt', r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)'),
                    REPAIRS=tfirst('b697_tool_repairs.txt', r'REPAIRS (\d+) ;'),
                    CARRIED=carried(text), DISPATCHES=jcount('b697_commands.json', lambda j: len(j.get('dispatches') or [])),
                    REDIRECTS=jcount('b697_commands.json', lambda j: len(j.get('redirects') or [])),
                    PIPES=jcount('b697_commands.json', lambda j: len(j.get('pipes') or [])),
                    PYPROGS=jcount('b697_commands.json', lambda j: len(j.get('py_programs') or [])),
                    PAGELINES=tlines('b697_faces_diff.txt', r'LINES DIFFERING ([:\d, ]+?) ;'),
                    RESIDUES=jcount('b697_cut.json', lambda j: len(j.get('residues') or [])),
                    AFTER=jcount('b697_cut.json', lambda j: int(j.get('after') or 0)))
    print()
    print('  ### ### **MEASURED OFF THE FACE AND THE BANKS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'LINES', 'MISSES', 'REPAIRS', 'CARRIED', 'DISPATCHES', 'REDIRECTS',
              'PIPES', 'PYPROGS', 'PAGELINES', 'RESIDUES', 'AFTER'):
        print('      %-12s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b697_registration_2026-10-21.txt -- b697, LANE TWO ACT ONE HUNDRED AND TWENTY-FOUR, THE RE-CUT ACT: b696 AT "
                             "ITS WEIGHT; THE WEIL-FACE LINE AT Q0 REGENERATED; SIDE-simplicity RE-CUT UNDER THE QUOTATION RULE; THE "
                             "ARITHMETIC-LIMIT FACE PRICED, UNDER (R307)"),
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    with open(SPEC + '.tmp', 'wb') as fh:
        fh.write(d)
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
