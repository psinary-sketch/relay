# -*- coding: utf-8 -*-
"""b706_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b705's spec by the Write tool, every clause re-written against this face: the citation check as a gate step; the record
### ### line and the corrigendum; the sort and the seven carry-time repairs; the seventeen pairs renamed in place by git mv, each its own commit;
### ### two kernel mains written (the join's manifest commit, the workflow's probe step), three dispatches, no tag (the join held), no merge, two
### ### scratch branches cut and deleted; the generator extended by ruling; six order lines landed; no outbound fetch; the suite in seven parts,
### ### one call each, three standing arms failing and declared; the mirror after the root; nothing deposits. The planted rows of (R263)(3) for
### ### this act's readers, the defect row's and the runner row's among them.
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
import b706_worklist as K   # noqa: E402

REG = os.path.join(ROOT, 'data', 'b706_registration_2026-10-22.txt')
SPEC = os.path.join(ROOT, 'data', 'b706_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched, the draft at v5.'),
    ('identifiers of the author placed in an outbound request or a workflow file', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes run on this host', 0, 0, 'processes', '### N1.'),
    ('runner dispatches made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: three, the join and the two entry-tag branches; MEASURED off the command bank.'),
    ('kernels created', 0, 0, 'kernels', '### none this act; the join kernel created at b705.'),
    ('commits on the join kernel`s main', 'JOINCOMMITS', 'JOINCOMMITS', 'commits', '### (R316)(4): its manifest commit on b705`s one; MEASURED off the kernel`s main.'),
    ('commits on SIDE-explicit-formula`s main past v0.37', 'MAINS', 'MAINS', 'commits', '### (R316)(5): the workflow`s probe step, one; MEASURED off the first-parent line.'),
    ('kernel merges made', 0, 0, 'merges', '### none: one commit on a main, no merge.'),
    ('tags made or moved', 'TAGSMADE', 'TAGSMADE', 'tags', '### MEASURED off SIDE-explicit-formula`s tags containing v0.37 and the join kernel`s tags (none: the join held).'),
    ('Lean files written on a kernel`s main', 'LEANFILES', 'LEANFILES', 'files', '### MEASURED off SIDE-explicit-formula`s main against v0.37 and the join kernel`s main against 732c1b49.'),
    ('scratch branches cut on a kernel', 'SCRATCH', 'SCRATCH', 'branches', '### (R316)(7): two, prints-b706-v0.1 and prints-b706-v0.2; MEASURED off the print-files banks.'),
    ('scratch branches deleted after their banks, locally and at the remote', 'SCRATCH', 'SCRATCH', 'branches', '### (R316)(7); each by name, one per command.'),
    ('kernel branches deleted beyond the two scratch branches', 0, 0, 'branches', '### (R316)(9) names push-b705-join of the join kernel at step zero alone.'),
    ('lakefiles or workflow files of a kernel edited', 2, 2, 'files', '### (R316)(4)-(5): the join`s lakefile and SIDE-explicit-formula`s workflow, each by the Edit tool.'),
    ('libraries vendored', 0, 0, 'libraries', '### N5.'),
    ('papers cut', 0, 0, 'papers', '### none this act.'),
    ('papers moved or renamed beyond the 17 pairs` git mv', 0, 0, 'papers', '### N5.'),
    ('pairs renamed in place by git mv', 'RENAMED', 'RENAMED', 'pairs', '### (R316)(3); MEASURED off the partners bank.'),
    ('pairs held', 'HELDPAIRS', 'HELDPAIRS', 'pairs', '### (R316)(3); MEASURED off the partners bank.'),
    ('Correspondence cells written by the generator', 'CELLS', 'CELLS', 'cells', '### (R316)(3), into the versioned copies before the rename; MEASURED off the dry bank.'),
    ('faces page writes', 0, 0, 'writes', '### (R316)(8): the join held, no prompt, no row changed.'),
    ('README edits', 0, 0, 'edits', '### none this act.'),
    ('glossary rows appended', 0, 0, 'rows', '### none this act.'),
    ('REGISTRY rows whose version cell moved to the tag', 'RENAMED', 'RENAMED', 'rows', '### (R316)(3), one per pair.'),
    ('orders and annotations entered at OPEN_TRAILS', 'ORDERS', 'ORDERS', 'lines', '### (R316)(3)-(7); MEASURED off the landing bank.'),
    ('generated corrigendum entries', 1, 1, 'entries', '### (R316)(2).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R316)(2): row (26).'),
    ('pages, keystones or ledger lines written beyond the named files', 0, 0, 'lines', '### N5.'),
    ('shared tools edited by ruling', 1, 1, 'tools', '### (R316)(6): tools/correspondence_gen.py by the Edit tool, its control byte for byte.'),
    ('shared tools edited beyond the ruling', 0, 0, 'tools', '### N5.'),
    ('standing arms added', 0, 0, 'arms', '### N5.'),
    ('frozen banks edited', 0, 0, 'banks', '### (Z).'),
    ('outbound fetches by a tool of this act', 0, 0, 'fetches', '### none: git, gh and the push tool alone.'),
    ('commits amended, rebased or rewritten', 0, 0, 'commits', '### data/b692_rules.txt row (1), the ferry.'),
    ('git writes sent two to a message', 0, 0, 'messages', '### the ferry.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (Z).'),
    ('root-chain rows edited', 0, 0, 'rows', '### appended only.'),
    ('citation checks run at step zero', 1, 1, 'checks', '### the gate step, standing from b662; before any delete.'),
    ('citation misses repaired silently', 0, 0, 'misses', '### the gate step.'),
    ('citation misses raised before the component that cites them', 'MISSES', 'MISSES', 'misses', '### MEASURED off the citation bank.'),
    ('mid-act answers acted on before their check', 0, 0, 'answers', '### (R278)(4).'),
    ('answers acted on with their END marker unread', 0, 0, 'answers', '### the paste rule.'),
    ('sealed entries or faces edited in place', 0, 0, 'entries', '### (Z).'),
    ('scores read from a ledger line', 0, 0, 'scores', '### data/b686_rules.txt row (1).'),
    ('suite parts over 590 seconds', 0, 0, 'parts', '### standing; standing-b2 split at this act per data/b684_rules.txt row (1).'),
    ('suite parts moved to the background', 0, 0, 'parts', '### data/b685_rules.txt row (1).'),
    ('suite parts sent two to a call', 0, 0, 'calls', '### data/b685_rules.txt row (1).'),
    ('commands carrying sed', 'SEDS', 'SEDS', 'commands', '### data/b685_rules.txt row (2), MEASURED off the command bank.'),
    ('commands carrying a redirect', 'REDIRECTS', 'REDIRECTS', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('commands piping a read into a shell filter', 'PIPES', 'PIPES', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('commands carrying a pipe of any kind', 'ANYPIPES', 'ANYPIPES', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('commands running an interpreter`s one-line program', 'PYPROGS', 'PYPROGS', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('Read calls above the cap from the anchor on', 'READOFF', 'READOFF', 'reads', '### every call counts from b705, MEASURED off the read bank.'),
    ('delete commands naming more than one branch or carrying a glob', 0, 0, 'commands', '### (R316)(9).'),
    ('delete commands with anything chained after', 0, 0, 'commands', '### data/b694_rules.txt row (1).'),
    ('deletes before the citation check', 0, 0, 'commands', '### b695 (a).'),
    ('carry-time repairs', 'REPAIRS', 'REPAIRS', 'repairs', '### the ferry`s Component 5, MEASURED off the repairs bank.'),
    ('root-route dry runs printed READY before the lock', 1, 1, 'runs', '### data/b706_rules.txt row (1).'),
    ('closing dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### b675 rules row 1.'),
    ('branches deleted beyond the ruling`s list', 0, 0, 'branches', '### (R316)(9) and (7).'),
    ('declared suite failures carried at the close', 'CARRIED', 'CARRIED', 'failures', '### (G2), MEASURED off the face`s declaration line.'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### W-ORD-KEYSTONE-HEADS held.'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('environment variables set or cleared by the seat', 0, 0, 'variables', '### the ferry: left as they are.'),
    ('record lines landed before the seal', 'LINES', 'LINES', 'lines', '### (R316)(1); MEASURED.'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('mirror exports built', 1, 1, 'exports', '### the b670 form, after the root, its roster names as renamed.'),
    ('scratch clones made', 0, 0, 'clones', '### (Z).'),
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
    ('record steps re-run after the root', 0, 0, 'steps', '### the ferry`s Component 6.'),
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
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0), every commit by its hash.'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R316).'),
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


def _need(x):
    if not x:
        raise ValueError('### the reader read nothing')
    return x


PLANTED = [
    ('score row', 'read_score_row', ('N3', ['HELD', 'a planted score text'])),
    ('trail head with a backtick possessive', 'read_head', '### b999 — a planted trail: the page`s probe read, the paper`s cut landed'),
    ('entry title with a backtick possessive', 'read_head', '## The planted entry: the page`s nodes, the README`s line'),
    ('branch row (the branches bank`s shape, a named local row deleted)', 'read_branch_row', dict(repo='D:/x', branch='push-b999-root', where='local',
                                                                                                tip='0' * 40, merged=True, fate='DELETED')),
    ('defect row (the defects bank`s shape, its continuation joined)', 'read_defect_row', ["    (a) THE SEAT'S: A PLANTED DEFECT. Its text,",
                                                                                          '        wrapped.']),
    ('runner row (the runner rows bank`s shape)', 'read_runner_row', dict(kernel='SIDE-x', label='run1', ref='0' * 40, run_id=1, gate='DERIVES')),
]


def planted():
    import tempfile
    import b706_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b706_spec_') as d:
                    led = os.path.join(d, 'LEDGER.md')
                    with open(led, 'wb') as fh:
                        fh.write(b'# a scratch ledger\n')
                    REC.R.append_to(led, '\n' + row + ': planted.\n')
                    got = fn(led, row)
            elif reader == 'read_score_row':
                got = fn(*row)
            elif reader == 'read_defect_row':
                got = _need(fn(row, 0))
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
    import b706_record as REC
    ctl = []
    for what, f in (('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b706_ferry.txt'), '### b999 absent')),
                    ('a branch row with no side', lambda: REC.read_branch_row(dict(repo='D:/x', branch='b', tip='0' * 40, fate='DELETED'))),
                    ('a branch row with a fate of another name', lambda: REC.read_branch_row(dict(repo='D:/x', branch='b', where='local', tip='0' * 40,
                                                                                                fate='GONE'))),
                    ('a branch row with a short tip', lambda: REC.read_branch_row(dict(repo='D:/x', branch='b', where='remote', tip='0' * 7,
                                                                                     fate='DELETED'))),
                    ('a defect row with no letter', lambda: _need(REC.read_defect_row(['    THE SEAT`S: NO LETTER HERE.'], 0))),
                    ('a runner row with a short ref', lambda: REC.read_runner_row(dict(kernel='SIDE-x', label='run1', ref='0' * 7, run_id=1,
                                                                                       gate='DERIVES'))),
                    ('a runner row with a gate of another name', lambda: REC.read_runner_row(dict(kernel='SIDE-x', label='run1', ref='0' * 40, run_id=1,
                                                                                                  gate='MAYBE'))),
                    ('a runner row with a dot in its label', lambda: REC.read_runner_row(dict(kernel='SIDE-x', label='prints-b706-v0.1', ref='0' * 40, run_id=1,
                                                                                              gate='DERIVES'))),
                    ('the repaired defects reader called with no act', lambda: REC.R._defect_short())):
        try:
            f()
            ctl.append((what, False))
        except Exception:
            ctl.append((what, True))
    return ctl


def _git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()


def main(argv):
    print('=' * 100)
    print('b706_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    if not CNT.self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2
    P = planted()
    print('  ### (R263)(3) THE PLANTED ROWS, ONE PER SHAPE A SEALED ROUTE READS, EACH THROUGH THE RECORD TOOL`S READER:')
    for shape, ok, what in P:
        print('      %-58s %s -- %s' % (shape, 'READ' if ok else '### REFUSED', what))
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
    mains = _git(K.EF_DIR, 'rev-list', '--first-parent', '--count', K.EF_V037 + '..main')
    tags_after = [t for t in _git(K.EF_DIR, 'tag', '--contains', K.EF_V037).split(chr(10)) if t.strip() and t.strip() != 'v0.37']
    join_tags = [t for t in _git(K.KERNEL_DIR, 'tag', '--list').split(chr(10)) if t.strip()] if os.path.isdir(K.KERNEL_DIR) else []
    join_commits = _git(K.KERNEL_DIR, 'rev-list', '--count', 'main') if os.path.isdir(K.KERNEL_DIR) else '0'
    leanf = [x for x in (_git(K.EF_DIR, 'diff', '--name-only', K.EF_V037, 'main') + chr(10) + _git(K.KERNEL_DIR, 'diff', '--name-only', K.JOIN_TIP_B705, 'main')).split(chr(10))
             if x.strip().endswith('.lean')]
    pj = jcount('b706_partners.json', lambda j: j.get('rows') or [])
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)),
                    TESTS=jcount('b706_tests_stepzero.json', len), QUESTIONS=tcount('b706_author_answers.txt', r'^### PROMPT '),
                    LINES=jcount('b706_record_lines.json', lambda j: len(j.get('lines') or [])),
                    MISSES=tfirst('b706_citation_check.txt', r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)'),
                    REPAIRS=tfirst('b706_tool_repairs.txt', r'REPAIRS (\d+) ;'),
                    CARRIED=carried(text), DISPATCHES=jcount('b706_commands.json', lambda j: len(j.get('dispatches') or [])),
                    MAINS=int(mains) if mains.isdigit() else 0, TAGSMADE=len(tags_after) + len(join_tags), LEANFILES=len(leanf),
                    JOINCOMMITS=(int(join_commits) - 1) if join_commits.isdigit() else 0,
                    SCRATCH=len([t for t, _b in K.PRINT_BRANCHES if os.path.isfile(os.path.join(ROOT, 'data', 'b706_print_files_prints-b706-%s.json' % t))]),
                    RENAMED=len([r for r in (pj if isinstance(pj, list) else []) if str(r.get('reading', '')).startswith('RENAME')]),
                    HELDPAIRS=len([r for r in (pj if isinstance(pj, list) else []) if not str(r.get('reading', '')).startswith('RENAME')]),
                    CELLS=jcount('b706_partners_dry.json', lambda j: sum(r.get('cells_changed') or 0 for r in (j.get('rows') or []) if r.get('written'))),
                    ORDERS=jcount('b706_orders.json', lambda j: len(j.get('lines') or [])),
                    SEDS=jcount('b706_commands.json', lambda j: len(j.get('seds') or [])),
                    REDIRECTS=jcount('b706_commands.json', lambda j: len(j.get('redirects') or [])),
                    PIPES=jcount('b706_commands.json', lambda j: len(j.get('pipes') or [])),
                    ANYPIPES=jcount('b706_commands.json', lambda j: len(j.get('any_pipes') or [])),
                    PYPROGS=jcount('b706_commands.json', lambda j: len(j.get('py_programs') or [])),
                    READOFF=tfirst('b706_read_calls.txt', r'OFFENCES (\d+) ; THE CAP`S PRECURSORS'))
    print()
    print('  ### ### **MEASURED OFF THE FACE, THE BANKS AND THE KERNELS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'LINES', 'MISSES', 'REPAIRS', 'CARRIED', 'DISPATCHES', 'MAINS', 'TAGSMADE',
              'LEANFILES', 'JOINCOMMITS', 'SCRATCH', 'RENAMED', 'HELDPAIRS', 'CELLS', 'ORDERS', 'SEDS', 'REDIRECTS', 'PIPES', 'ANYPIPES', 'PYPROGS', 'READOFF'):
        print('      %-12s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b706_registration_2026-10-22.txt -- b706, LANE TWO ACT ONE HUNDRED AND THIRTY-THREE, THE RE-CUT ACT: b705 AT ITS "
                             "WEIGHT; THE POST-SEAL FAILURES SORTED AND THREE TOOLS REPAIRED; THE PARTNER COPIES RENAMED IN PLACE; THE JOIN`S MANIFEST; "
                             "THE WORKFLOW`S PROBE STEP; THE GENERATOR`S REACH; THE ENTRY-TAG PRINTS; THE FACES ROW, UNDER (R316)"),
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
