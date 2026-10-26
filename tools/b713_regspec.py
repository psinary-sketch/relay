# -*- coding: utf-8 -*-
"""b713_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b712's spec by tools/b713_carry.py (the act names substituted) and its clauses re-written by the Edit tool against this face:
### ### the citation check as a gate step; the record lines and the corrigendum; the faces ledger head's :8 and the re-cut's additive check on
### ### the author's word; the six repairs of (R323)(4) and standing clauses v4; the -15 research (the list, the predictions committed alone
### ### first, the onsets, the coefficients) and the source pin; no kernel written, no dispatch, no lean on this host; the suite in seven
### ### parts, one call each; the mirror after the root; the report tool unsealed; nothing deposits. The planted rows
### ### of (R263)(3) for this act's readers, the defect row's and the runner row's among them (the runner row with the gate NOT DERIVES, the
### ### port runs' shape).
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402
import b713_worklist as K   # noqa: E402

REG = os.path.join(ROOT, 'data', 'b713_registration_2026-10-25.txt')
SPEC = os.path.join(ROOT, 'data', 'b713_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched, the draft at v5.'),
    ('identifiers of the author placed in an outbound request or a workflow file', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes started by the seat on this host', 0, 0, 'processes', '### N1; MEASURED off the command bank (the seat`s own commands).'),
    ('lean processes run on this host by a test', 0, 0, 'processes', '### N1: the lean-running test reads lean`s banked prints.'),
    ('runner dispatches made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none; MEASURED off the command bank.'),
    ('runs dispatched and read this act', 'RUNS', 'RUNS', 'runs', '### N1: none; MEASURED off the dispatch bank (absent this act).'),
    ('kernels created', 0, 0, 'kernels', '### none this act.'),
    ('commits on any kernel`s main', 0, 0, 'commits', '### none: every main unmoved.'),
    ('commits on the port branch of SIDE-lv-conservation', 'PORTCOMMITS', 'PORTCOMMITS', 'commits', '### none: port-b707 at b712`s tip cb0aea56; MEASURED off the branch`s log from that tip to the branch now.'),
    ('scratch branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('push branches cut on a kernel for the push procedure', 0, 0, 'branches', '### none this act.'),
    ('kernel merges made', 0, 0, 'merges', '### none.'),
    ('tags made or moved', 'TAGSMADE', 'TAGSMADE', 'tags', '### none; MEASURED off SIDE-explicit-formula`s tags past v0.37, SIDE-lv-conservation`s containing b712`s port tip and the join kernel`s beyond v0.1.0.'),
    ('Lean files written on a kernel', 'LEANFILES', 'LEANFILES', 'files', '### none; MEASURED off the port branch`s files from b712`s tip.'),
    ('port branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('kernel branches deleted', 1, 1, 'branches', '### (R323)(7): push-b712-join of SIDE-faces-join, local, by name at step zero; port-b707 KEPT.'),
    ('toolchain, manifest, lakefile or workflow files of a kernel written', 0, 0, 'files', '### none.'),
    ('libraries vendored', 0, 0, 'libraries', '### N5.'),
    ('papers cut', 0, 0, 'papers', '### none this act (the re-cut is b712`s).'),
    ('commits on the re-cut branch', 1, 1, 'commits', '### (R323)(2)(iii): the two MISSING Correspondence lines restored by the Edit tool on recut-b712-silence (0aeca834).'),
    ('papers moved, renamed or written beyond the re-cut`s restored lines', 0, 0, 'papers', '### N5.'),
    ('re-cut branches pushed', 1, 1, 'branches', '### (R323)(2)(iii): recut-b712-silence in branch mode.'),
    ('re-cut branches merged', 0, 0, 'merges', '### N5: the re-cut is not merged.'),
    ('faces ledger head lines edited', 1, 1, 'lines', '### (R323)(2)(ii), N3: FACES_LEDGER.md :8, by the Edit tool.'),
    ('pairs renamed in place by git mv', 0, 0, 'pairs', '### none this act (b706`s).'),
    ('Correspondence cells written by the generator', 0, 0, 'cells', '### none: no page write this act.'),
    ('Correspondence cells written by hand', 0, 0, 'cells', '### none.'),
    ('faces page writes', 0, 0, 'writes', '### none this act.'),
    ('README edits', 0, 0, 'edits', '### none this act.'),
    ('glossary rows appended', 0, 0, 'rows', '### none this act.'),
    ('REGISTRY rows changed', 0, 0, 'rows', '### none this act.'),
    ('orders and annotations entered at OPEN_TRAILS before the seal', 0, 0, 'lines', '### none before the seal.'),
    ('generated corrigendum entries', 1, 1, 'entries', '### (R323)(3).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R323)(3): row (33).'),
    ('faces ledger update blocks appended', 0, 0, 'blocks', '### none this act (the head`s :8 edit its one write).'),
    ('binary banks written beside a text hashes bank', 'BINARIES', 'BINARIES', 'banks', '### the list`s and the coefficients` hashes banks; MEASURED off the hashes banks present.'),
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R323)(5): the list, the predictions, the onsets and the coefficients; MEASURED off the banks present.'),
    ('numbers computed for a registration not read from its commit', 0, 0, 'numbers', '### N2: the registrations read unchanged from 67a02388.'),
    ('onsets computed before the predictions` commit', 0, 0, 'onsets', '### N2: the predictions committed alone (be4db146) before any onset bank.'),
    ('pages, keystones or ledger lines written beyond the named files', 0, 0, 'lines', '### N5.'),
    ('shared tools written by ruling', 'SHAREDTOOLS', 'SHAREDTOOLS', 'tools', '### (R323)(4): tools/act_close.py (new) and tools/push_gated.sh (repaired); MEASURED off the worklist`s lists.'),
    ('shared data files rewritten by ruling', 0, 0, 'files', '### none this act.'),
    ('shared banks written by ruling', 1, 1, 'banks', '### (R323)(4): data/standing_clauses_v4.txt.'),
    ('shared tools edited beyond the ruling', 0, 0, 'tools', '### N5.'),
    ('standing arms added', 0, 0, 'arms', '### N5.'),
    ('frozen banks edited', 0, 0, 'banks', '### (Z).'),
    ('outbound fetches by a tool of this act', 0, 0, 'fetches', '### none: git, gh and the push tool alone.'),
    ('outbound fetches by the seat', 2, 2, 'fetches', '### (R323)(6): the source pin`s abstract page and PDF at arxiv.org, by curl with its own default headers; one web search.'),
    ('commits amended, rebased or rewritten', 0, 0, 'commits', '### data/b692_rules.txt row (1), the ferry.'),
    ('git writes sent two to a message', 0, 0, 'messages', '### the ferry.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (Z).'),
    ('root-chain rows edited', 0, 0, 'rows', '### appended only.'),
    ('citation checks run at step zero', 1, 1, 'checks', '### the gate step, standing from b662; before any delete (run once to its bank after a dry run).'),
    ('citation misses repaired silently', 0, 0, 'misses', '### the gate step.'),
    ('citation misses raised or entered before the component that cites them', 'MISSES', 'MISSES', 'misses', '### MEASURED off the citation bank.'),
    ('mid-act answers acted on before their tool check', 0, 0, 'answers', '### (R278)(4): no mid-act prompt this act.'),
    ('answers acted on with their END marker unread', 0, 0, 'answers', '### the paste rule.'),
    ('sealed entries or faces edited in place', 0, 0, 'entries', '### (Z).'),
    ('scores read from a ledger line', 0, 0, 'scores', '### data/b686_rules.txt row (1).'),
    ('suite parts over 590 seconds', 0, 0, 'parts', '### standing; seven parts as b706 split them.'),
    ('suite parts moved to the background', 0, 0, 'parts', '### data/b685_rules.txt row (1).'),
    ('suite parts sent two to a call', 0, 0, 'calls', '### data/b685_rules.txt row (1).'),
    ('commands carrying sed', 'SEDS', 'SEDS', 'commands', '### data/b685_rules.txt row (2), MEASURED off the command bank.'),
    ('commands carrying a redirect', 'REDIRECTS', 'REDIRECTS', 'commands', '### the ferry, MEASURED off the command bank (none this act).'),
    ('commands piping a read into a shell filter', 'PIPES', 'PIPES', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('commands carrying a pipe of any kind', 'ANYPIPES', 'ANYPIPES', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('commands running an interpreter`s one-line program', 'PYPROGS', 'PYPROGS', 'commands', '### the ferry, MEASURED off the command bank.'),
    ('Read calls above the cap from the anchor on', 'READOFF', 'READOFF', 'reads', '### every call counts from b705, MEASURED off the read bank; the opening`s whole read lettered (a).'),
    ('delete commands naming more than one branch or carrying a glob', 0, 0, 'commands', '### (R323)(7).'),
    ('delete commands with anything chained after', 0, 0, 'commands', '### data/b694_rules.txt row (1).'),
    ('deletes before the citation check', 0, 0, 'commands', '### b695 (a).'),
    ('repairs of (R323)(4)', 'REPAIRS', 'REPAIRS', 'repairs', '### the six repairs; MEASURED off the repairs bank.'),
    ('carried tools read beyond the spans their banks name', 'WHOLEREADS', 'WHOLEREADS', 'tools', '### data/b712_rules.txt row (1); MEASURED off the defects bank`s rows.'),
    ('root-route dry runs printed READY before the lock', 1, 1, 'runs', '### data/b706_rules.txt row (1).'),
    ('closing dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### b675 rules row 1.'),
    ('branches deleted beyond the ruling`s list', 0, 0, 'branches', '### (R323)(7).'),
    ('declared suite failures carried at the close', 'CARRIED', 'CARRIED', 'failures', '### (G2), MEASURED off the face`s declaration line.'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### W-ORD-KEYSTONE-HEADS held.'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('environment variables set or cleared by the seat', 1, 1, 'variables', '### the ferry: left as they are (the push tool`s own capture variable given to it alone); one set for one command`s process (PYTHONIOENCODING on the closing`s dry run), defect (k).'),
    ('record lines landed before the seal', 'LINES', 'LINES', 'lines', '### (R323)(1); MEASURED.'),
    ('predictions banks committed alone before any onset bank', 'PREDFIRST', 'PREDFIRST', 'banks', '### N2; MEASURED off the relay log since the act`s base.'),
    ('dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### (R267)(2), standing.'),
    ('mirror exports built', 1, 1, 'exports', '### the b670 form, after the root.'),
    ('report tools sealed', 0, 0, 'tools', '### a report and not an arm; data/b708_rules.txt row (1).'),
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
    ('questions asked of the author before the seal', 0, 0, 'questions', '### none: the root`s prompt alone, after the seal ((R323)(8)).'),
    ('questions asked of the author at the root', 'QUESTIONS', 'QUESTIONS', 'questions', '### MEASURED off the answers bank (the root`s prompt, once).'),
    ('questions asked of the author after the root', 0, 0, 'questions', '### the answers bank is root-named.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0), every commit by its hash.'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R323).'),
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
    ('runner row with the gate NOT DERIVES (the port runs` shape)', 'read_runner_row', dict(kernel='SIDE-x', label='port', ref='0' * 40, run_id=1, gate='NOT DERIVES')),
]


def planted():
    import tempfile
    import b713_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b713_spec_') as d:
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
    import b713_record as REC
    ctl = []
    for what, f in (('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b713_ferry.txt'), '### b999 absent')),
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
                    ('a runner row with a dot in its label', lambda: REC.read_runner_row(dict(kernel='SIDE-x', label='prints-v0.17', ref='0' * 40, run_id=1,
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


def _pred_first():
    """N2: the predictions' commit carries the predictions banks alone, and no onset bank is committed at or before it (the relay log since
    the act's base, oldest first)."""
    rows = _git(ROOT, 'log', '--reverse', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', 'data/b713_predictions.txt', 'data/b713_onsets.txt').split(chr(10))
    rows = [r.strip() for r in rows if r.strip()]
    if not rows or rows[0] != K.PRED_RELAY:
        return False
    alone = sorted(f for f in _git(ROOT, 'show', '--name-only', '--format=', K.PRED_RELAY).split(chr(10)) if f.strip())
    return alone == ['data/b713_predictions.json', 'data/b713_predictions.txt']


def refresh_commands(bank='b713_commands.json'):
    """(R323)(3)(v), standing clauses v3: THE COMMAND SCREEN READS A FRESH BANK -- the command bank rewritten by the record tool's `commands`
    route in this step, before the face's counts are read from it (b712's face read ANYPIPES 7 from a bank last written before its eighth
    pipe, events :3). Returns the bank's `at` stamp after the refresh, or None where the refresh did not write it."""
    p = os.path.join(ROOT, 'data', bank)
    t0 = time.time()
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(ROOT, 'tools', 'b713_record.py'), 'commands'], capture_output=True,
                       text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0 or not os.path.exists(p) or os.path.getmtime(p) < t0:
        return None
    try:
        return json.load(io.open(p, encoding='utf-8')).get('at')
    except Exception:
        return None


def main(argv):
    print('=' * 100)
    fresh = refresh_commands()
    print('  ### (R323)(3)(v) THE COMMAND BANK REFRESHED IN THIS STEP: %s' % (fresh or '### NOT REFRESHED'))
    if not fresh:
        print('  ### REFUSING TO EMIT A SPEC FROM A COMMAND BANK NOT WRITTEN IN THIS STEP.')
        return 4
    print('b713_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    ef_tags_after = [t for t in _git(K.EF_DIR, 'tag', '--contains', K.EF_V037).split(chr(10)) if t.strip() and t.strip() != 'v0.37']
    lv_tags_after = [t for t in _git(K.LV_DIR, 'tag', '--contains', K.PORT_TIP).split(chr(10)) if t.strip()]
    join_tags = [t for t in _git(K.JOIN_DIR, 'tag', '--list').split(chr(10)) if t.strip()] if os.path.isdir(K.JOIN_DIR) else []
    port_commits = _git(K.LV_DIR, 'rev-list', '--count', '%s..refs/heads/%s' % (K.PORT_TIP, K.PORT_BRANCH))
    lean_files = [f for f in _git(K.LV_DIR, 'diff', '--name-only', K.PORT_TIP, K.PORT_NEW_TIP).split(chr(10)) if f.strip().endswith('.lean')]
    first_relay = (_git(ROOT, 'rev-list', '--reverse', '%s..HEAD' % K.PRE_RELAY).split(chr(10)) or [''])[0].strip()
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)),
                    TESTS=jcount('b713_tests_stepzero.json', len), QUESTIONS=tcount('b713_author_answers.txt', r'^### PROMPT '),
                    LINES=jcount('b713_record_lines.json', lambda j: len(j.get('lines') or [])),
                    MISSES=tfirst('b713_citation_check.txt', r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)'),
                    REPAIRS=jcount('b713_tool_repairs.json', lambda j: len(j.get('repairs') or [])),
                    CARRIED=carried(text), DISPATCHES=jcount('b713_commands.json', lambda j: len(j.get('dispatches') or [])),
                    RUNS=jcount('b713_dispatches.json', lambda j: len([r for r in j.get('rows') or [] if r.get('run_id')])),
                    PORTCOMMITS=int(port_commits) if port_commits.isdigit() else 0, LEANFILES=len(lean_files),
                    TAGSMADE=len(lv_tags_after) + len(ef_tags_after) + len([t for t in join_tags if t != K.JOIN_TAG[0]]),
                    ORDERS=jcount('b713_order_lines.json', lambda j: len(j.get('lines') or [])),
                    BINARIES=len([f for f in os.listdir(os.path.join(ROOT, 'data')) if re.match(r'^b713_\w+_hashes\.txt$', f)]),
                    COMPUTE=len([n_ for n_ in ('list', 'predictions', 'onsets', 'coeffs') if os.path.exists(os.path.join(ROOT, 'data', 'b713_%s.txt' % n_))]),
                    SHAREDTOOLS=len(K.REPAIRED_TOOLS) + len(K.NEW_TOOLS),
                    PREDFIRST=1 if _pred_first() else 0,
                    WHOLEREADS=len(re.findall(r"^    \([a-z]\) THE SEAT'S: THE CARRIED (?:SUITE|TOOLS?) READ BEYOND THE SPANS",
                                              io.open(os.path.join(ROOT, 'data', 'b713_defects.txt'), encoding='utf-8').read(), re.M)),
                    SEDS=jcount('b713_commands.json', lambda j: len(j.get('seds') or [])),
                    REDIRECTS=jcount('b713_commands.json', lambda j: len(j.get('redirects') or [])),
                    PIPES=jcount('b713_commands.json', lambda j: len(j.get('pipes') or [])),
                    ANYPIPES=jcount('b713_commands.json', lambda j: len(j.get('any_pipes') or [])),
                    PYPROGS=jcount('b713_commands.json', lambda j: len(j.get('py_programs') or [])),
                    READOFF=tfirst('b713_read_calls.txt', r'OFFENCES (\d+) ; THE CAP`S PRECURSORS'))
    print()
    print('  ### ### **MEASURED OFF THE FACE, THE BANKS AND THE KERNELS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'LINES', 'MISSES', 'REPAIRS', 'CARRIED', 'DISPATCHES', 'RUNS', 'PORTCOMMITS',
              'LEANFILES', 'TAGSMADE', 'ORDERS', 'BINARIES', 'COMPUTE', 'SHAREDTOOLS', 'PREDFIRST', 'WHOLEREADS', 'SEDS', 'REDIRECTS',
              'PIPES', 'ANYPIPES', 'PYPROGS', 'READOFF'):
        print('      %-12s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b713_registration_2026-10-25.txt -- b713, LANE TWO ACT ONE HUNDRED AND FORTY, THE RESEARCH ACT AT DISCRIMINANT -15: "
                             "b712 AT ITS WEIGHT; THE AUTHOR`S WORD ON THREE ITEMS; THE CORRIGENDUM; STANDING CLAUSES v4 AND THE SIX REPAIRS; THE ZERO LIST, "
                             "THE PREDICTIONS, THE ONSETS AND THE COEFFICIENTS AT -15; THE SOURCE PIN, UNDER (R323)"),
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
