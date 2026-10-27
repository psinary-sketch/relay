# -*- coding: utf-8 -*-
"""b718_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### Carried from b717's spec by tools/b718_carry.py (the act names substituted) and its clauses re-written by the Edit tool against this face
### ### (Component 7): the citation check as a gate step; the record lines and the corrigendum ((R328)(1)-(2)); the arms' tags and the counter;
### ### the registrations read unchanged and committed first, nothing at a new discriminant beyond its class number and forms ((R328)(4), N2);
### ### the derivation graded, its Lean statement priced; the toolset at v1.2.0 ((R328)(7)); the pin's branches, its one dispatch read by its
### ### run id, nine carried and two held ((R328)(8), N1); the watch's annotation naming nothing of the outside collection ((R328)(9)); the
### ### step-zero deletes ((R328)(10)); no main moved, no tag, no lean on this host; the suite in seven parts, one call each;
### ### the mirror after the root; the report tool unsealed; nothing deposits, no GitHub release. The planted rows
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
import b718_worklist as K   # noqa: E402

REG = os.path.join(ROOT, 'data', 'b718_registration_2026-10-27.txt')
SPEC = os.path.join(ROOT, 'data', 'b718_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ('records published at any service', 0, 0, 'records', '### N5.'),
    ('publish calls made', 0, 0, 'calls', '### N5.'),
    ('deposit drafts touched', 0, 0, 'drafts', '### N5: the deposit route untouched, the draft at v5.'),
    ('identifiers of the author placed in an outbound request or a workflow file', 0, 0, 'identifiers', '### N5.'),
    ('lean or lake processes started by the seat on this host', 0, 0, 'processes', '### N1; MEASURED off the command bank (the seat`s own commands).'),
    ('lean processes run on this host by a test', 0, 0, 'processes', '### N1: the lean-running test reads lean`s banked prints.'),
    ('runner dispatches made outside the pin tool', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none; MEASURED off the command bank.'),
    ('runner dispatches made by the pin tool', 'PINDISP', 'PINDISP', 'dispatches', '### (R328)(8), N1: twelve at most, stopped at one by the author`s word (Option 2); MEASURED off data/b718_pin_rows.json.'),
    ('runs dispatched and read by their run ids', 'RUNS', 'RUNS', 'runs', '### (R328)(8), N1: run 40587516142, BUILDS; MEASURED off the pin`s rows (each read row`s run id among the dispatches).'),
    ('runs dispatched and not read', 'UNREAD', 'UNREAD', 'runs', '### N1; MEASURED off the same rows.'),
    ('kernels created', 0, 0, 'kernels', '### none this act.'),
    ('commits on any kernel`s main', 0, 0, 'commits', '### N5: every main unmoved.'),
    ('commits on the port branch of SIDE-lv-conservation', 'PORTCOMMITS', 'PORTCOMMITS', 'commits', '### none: port-b707 at cb0aea56; MEASURED off the branch`s log from that tip to the branch now.'),
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### (R328)(8): pin-b718-de5ce8a9, one commit each on main`s tree by git plumbing; MEASURED off the twelve kernels` refs.'),
    ('pin branches pushed to a kernel`s origin', 'PINPUSHED', 'PINPUSHED', 'branches', '### (R328)(8): SIDE-effects` alone, for its dispatch; the nine carried unpushed by the author`s word; MEASURED off the rows (a dispatch row each).'),
    ('scratch branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('push branches cut on a kernel for the push procedure', 0, 0, 'branches', '### none this act.'),
    ('kernel merges made', 0, 0, 'merges', '### none.'),
    ('tags made or moved', 'TAGSMADE', 'TAGSMADE', 'tags', '### N5: none; MEASURED off SIDE-explicit-formula`s tags past v0.37, SIDE-lv-conservation`s containing the port tip but b714`s v0.14.0, and the join kernel`s beyond v0.1.0.'),
    ('GitHub releases created', 0, 0, 'releases', '### N5.'),
    ('commits on SIDE-lv-conservation`s main or its deposit', 0, 0, 'commits', '### N5: main d38f3e8c untouched.'),
    ('Lean files written on a kernel', 'LEANFILES', 'LEANFILES', 'files', '### the pin`s lakefile.lean on each pin branch whose lakefile is Lean (its Mathlib require, one of the three files of (R328)(8)), no module source; none on the port branch; MEASURED off the port branch and the pin branches against their bases.'),
    ('port branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('kernel branches deleted', 0, 0, 'branches', '### none: port-b707 KEPT; the pin branches carried.'),
    ('branches deleted at step zero', 5, 5, 'branches', '### (R328)(10): relay push-b717-closing, push-b717-preroot, push-b717-record; PLACE-papers push-b717-preroot, push-b717-record; each local, by name, after --merged listed it (data/b718_stepzero.txt :37-:40).'),
    ('toolchain, lakefile or manifest files written on a pin branch', 'PINFILES', 'PINFILES', 'files', '### (R328)(8): lean-toolchain, the lakefile`s Mathlib require and lake-manifest.json, three per branch; MEASURED off each pin branch against main.'),
    ('workflow files of a kernel written', 0, 0, 'files', '### none: SIDE-frobenius held for its missing workflow rather than given one.'),
    ('libraries vendored', 0, 0, 'libraries', '### N5.'),
    ('papers cut', 0, 0, 'papers', '### none this act.'),
    ('commits on the re-cut branch', 0, 0, 'commits', '### none: recut-b712-silence deleted at b717`s step zero, its tip 0aeca834 merged by b714 at a86c9429.'),
    ('re-cut branches merged', 0, 0, 'merges', '### none this act.'),
    ('re-cut branches deleted', 0, 0, 'branches', '### none this act (b717`s).'),
    ('keystone opening paragraphs written to main', 0, 0, 'paragraphs', '### none this act.'),
    ('companion correspondence files written on main', 0, 0, 'files', '### none this act.'),
    ('census editions written on main', 0, 0, 'editions', '### none this act: the census v0.8.3 read by the touch read, not written.'),
    ('day papers edited on main', 0, 0, 'papers', '### none this act.'),
    ('papers moved, renamed or written beyond FINDINGS and OPEN_TRAILS', 0, 0, 'papers', '### N5.'),
    ('faces ledger head lines edited', 0, 0, 'lines', '### none this act.'),
    ('pairs renamed in place by git mv', 0, 0, 'pairs', '### none this act (b706`s).'),
    ('Correspondence cells written by the generator', 0, 0, 'cells', '### none: no page write this act.'),
    ('Correspondence cells written by hand', 0, 0, 'cells', '### none.'),
    ('faces page writes', 0, 0, 'writes', '### none this act.'),
    ('README edits', 0, 0, 'edits', '### none this act.'),
    ('glossary rows appended', 0, 0, 'rows', '### none this act.'),
    ('REGISTRY rows changed', 0, 0, 'rows', '### none this act: the two cells priced for b719 ((R328)(9)).'),
    ('orders and annotations entered at OPEN_TRAILS before the seal', 1, 1, 'lines', '### (R328)(9): W-ORD-QUASI-RH-FIELD-WATCH annotated at :16126 (PLACE-papers f6f6df50), the line reworded in place at 54a01285 before any push (defect (t)), Status OPEN, WATCH.'),
    ('outside collection names written to a ledger', 'OUTSIDE', 'OUTSIDE', 'names', '### b641`s form (defect (t) repaired): the names in relay data/b718_watch.txt alone; MEASURED off OPEN_TRAILS :16126 by tools/b641_record.py OAI_NEEDLES.'),
    ('generated corrigendum entries', 1, 1, 'entries', '### (R328)(2).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R328)(2): row (38).'),
    ('faces ledger update blocks appended', 0, 0, 'blocks', '### none this act.'),
    ('binary banks written beside a text hashes bank', 'BINARIES', 'BINARIES', 'banks', '### none this act; MEASURED off the hashes banks present.'),
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R328)(4)-(8): the decomposition, the derivation, the registrations, A0, the class controls, the replay and the pin; MEASURED off the banks present.'),
    ('registrations read unchanged from their commit', 1, 1, 'registrations', '### (R328)(4)(i), N2: data/b716_registrations.txt (ii) and its count control at dc5e808f, blob for blob at HEAD.'),
    ('registrations committed alone before any figure at their discriminants', 1, 1, 'registrations', '### (R328)(4)(iv), N2: data/b718_registrations.txt at 8146404b, an ancestor of the derivation`s commit.'),
    ('banks holding a figure at a new discriminant beyond its class number and forms', 'N2BANKS', 'N2BANKS', 'banks', '### N2; MEASURED off relay data/ by the record tool`s N2_FORBIDDEN.'),
    ('registrations` numbers changed after their commit', 0, 0, 'numbers', '### N2.'),
    ('derivation grades claiming more than the bank`s', 0, 0, 'sentences', '### N3: the record tool`s N3_OVERCLAIM over the entry.'),
    ('Lean statements of the derivation written or compiled', 0, 0, 'statements', '### (R328)(4)(iii): priced in data/b718_derivation_price.txt.'),
    ('pages, keystones or ledger lines written beyond the named files', 0, 0, 'lines', '### N5.'),
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R328)(7): tools/standing/ at v1.2.0 -- allow.py, close.py, replay.py and VERSION changed, classes.py, keystone.py, manifest.py and needles.py new; MEASURED off the worklist`s lists.'),
    ('shared data files rewritten by ruling', 0, 0, 'files', '### none this act.'),
    ('shared banks written by ruling', 3, 3, 'banks', '### (R328)(3), (10): data/act_current.json and data/standing_clauses_v7.txt at step zero; data/arm_tags.json re-pointed at Component 7 (defect (v)).'),
    ('harness settings files written', 0, 0, 'files', '### none: the hook in D:/.claude/settings.json unedited.'),
    ('dispatches made with free memory beneath the hold', 'BENEATH', 'BENEATH', 'dispatches', '### the author`s word: stop there, enter it and report; MEASURED off the defects bank (defect (r): 2490 MB at the first dispatch, the refusal then put in the pin tool).'),
    ('shared tools edited beyond the ruling', 0, 0, 'tools', '### N5.'),
    ('standing arms added', 0, 0, 'arms', '### N5.'),
    ('frozen banks edited', 0, 0, 'banks', '### (Z).'),
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the pin`s dispatch and read and the watch`s read by gh with its own token, each URL the repository`s own address, no identifier of the author in any header, input or payload.'),
    ('outbound fetches by the seat', 0, 0, 'fetches', '### none.'),
    ('commits amended, rebased or rewritten', 0, 0, 'commits', '### data/b692_rules.txt row (1), the ferry.'),
    ('git writes sent two to a message', 0, 0, 'messages', '### the ferry.'),
    ('secrets added to a repository', 0, 0, 'secrets', '### (Z).'),
    ('root-chain rows edited', 0, 0, 'rows', '### appended only.'),
    ('citation checks run at step zero', 1, 1, 'checks', '### the gate step, standing from b662; before any delete (run once to its bank after a dry run).'),
    ('citation misses repaired silently', 0, 0, 'misses', '### the gate step.'),
    ('citation misses raised or entered before the component that cites them', 'MISSES', 'MISSES', 'misses', '### MEASURED off the citation bank.'),
    ('mid-act answers acted on before their tool check', 'ACTEDBEFORE', 'ACTEDBEFORE', 'answers', '### (R278)(4): the author`s word at Component 5 acted on before its check (defect (y)); MEASURED off the defects bank.'),
    ('answers acted on with their END marker unread', 0, 0, 'answers', '### the paste rule.'),
    ('sealed entries or faces edited in place', 0, 0, 'entries', '### (Z).'),
    ('scores read from a ledger line', 0, 0, 'scores', '### data/b686_rules.txt row (1).'),
    ('suite parts over 590 seconds', 0, 0, 'parts', '### standing; seven parts as b706 split them.'),
    ('suite parts moved to the background', 0, 0, 'parts', '### data/b685_rules.txt row (1).'),
    ('suite parts sent two to a call', 0, 0, 'calls', '### data/b685_rules.txt row (1).'),
    ('commands carrying sed', 'SEDS', 'SEDS', 'commands', '### data/b685_rules.txt row (2), MEASURED off the command bank.'),
    ('commands carrying a redirect', 'REDIRECTS', 'REDIRECTS', 'commands', '### the ferry, MEASURED off the command bank: defect (b), refused by the hook before it ran.'),
    ('commands piping a read into a shell filter', 'PIPES', 'PIPES', 'commands', '### the ferry, MEASURED off the command bank: defects (a), (q), each refused by the hook before it ran.'),
    ('commands carrying a pipe of any kind', 'ANYPIPES', 'ANYPIPES', 'commands', '### the ferry, MEASURED off the command bank: defects (a), (p), (q), (s), (w) -- (p) the bar inside quotes the hook did not refuse.'),
    ('commands running an interpreter`s one-line program', 'PYPROGS', 'PYPROGS', 'commands', '### the ferry, MEASURED off the command bank: defects (k), (o).'),
    ('Read calls above the cap from the anchor on', 'READOFF', 'READOFF', 'reads', '### every call counts from b705, MEASURED off the read bank: defects (f), (n), (u), (x).'),
    ('delete commands naming more than one branch or carrying a glob', 0, 0, 'commands', '### standing (memory feedback_delete_only_verified_absolute_path).'),
    ('delete commands with anything chained after', 0, 0, 'commands', '### data/b694_rules.txt row (1).'),
    ('deletes before the citation check', 0, 0, 'commands', '### b695 (a).'),
    ('arms tagged CLAIM or CLOSE', 'TAGGED', 'TAGGED', 'arms', '### (R328)(2): data/arm_tags.json; MEASURED off its tags.'),
    ('events and defects of the act left untagged', 'UNTAGGED', 'UNTAGGED', 'items', '### (R328)(2): the counter`s untagged rows; MEASURED off the defects and events banks.'),
    ('carried tools read beyond the spans their banks name', 'WHOLEREADS', 'WHOLEREADS', 'tools', '### data/b717_rules.txt row (1); MEASURED off the defects bank`s rows.'),
    ('root-route dry runs printed READY False before the lock', 0, 0, 'runs', '### data/b706_rules.txt row (1); v5 row (76): READY True the seal`s evidence.'),
    ('root-route dry runs run before the lock', 1, 1, 'runs', '### the ferry`s Component 5: run once.'),
    ('closing dry-run steps printed CLEAN before the lock', 1, 1, 'steps', '### b675 rules row 1.'),
    ('branches deleted beyond the step zero`s list', 0, 0, 'branches', '### port-b707 kept.'),
    ('declared suite failures carried at the close', 'CARRIED', 'CARRIED', 'failures', '### (G2), MEASURED off the face`s declaration line.'),
    ('numbers of this act entered in a keystone', 0, 0, 'numbers', '### no bench number in a keystone; the names` pins are repositories, tags and lines.'),
    ('shared-bank lines changed in place', 0, 0, 'lines', '### (R254)(2).'),
    ('deletes naming a variable or a glob', 0, 0, 'commands', '### the ferry.'),
    ('environment variables set or cleared by the seat', 0, 0, 'variables', '### the ferry: left as they are (the push tool`s own capture variable given to it alone).'),
    ('record lines landed before the seal', 'LINES', 'LINES', 'lines', '### (R328)(1); MEASURED.'),
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
    ('PLACE-papers ERRATA entries written', 0, 0, 'entries', '### none this act.'),
    ('TECHNE-Core files created or edited', 0, 0, 'files', '### (Z).'),
    ('SPIRAL_MAP.md edits', 0, 0, 'edits', '### (Z).'),
    ('FINDINGS lines moved', 0, 0, 'lines', '### (Z).'),
    ('ferry parts received', 1, 1, 'parts', '### section (A).'),
    ('struck-clause hits in the ferry scan', 0, 0, 'hits', '### section (A).'),
    ('test files run at step zero', 'TESTS', 'TESTS', 'files', '### none: (R328)`s Component 0 lists no test run (data/b718_stepzero.txt :53-:55); MEASURED off the bank (absent).'),
    ('words of the author received before the seal', 'PRESEAL', 'PRESEAL', 'words', '### one: Option 2 at Component 5, on the seat`s halt; MEASURED off data/b718_author_words_preseal.txt.'),
    ('questions asked of the author at the root', 'QUESTIONS', 'QUESTIONS', 'questions', '### MEASURED off the answers bank (the root`s prompt, once).'),
    ('questions asked of the author after the root', 0, 0, 'questions', '### the answers bank is root-named.'),
    ('readings of the order declared in advance on this face', 'READINGS', 'READINGS', 'readings', '### section (A), MEASURED off the face.'),
    ('readings taken silently', 0, 0, 'readings', '### section (A).'),
    ('component steps taken before the lock and not declared', 0, 0, 'steps', '### section (0), every commit by its hash.'),
    ('author rulings ratified and entered', 1, 1, 'rulings', '### the ferry: (R328).'),
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
    import b718_record as REC
    out = []
    for shape, reader, row in PLANTED:
        fn = getattr(REC, reader)
        try:
            if reader == 'read_head':
                with tempfile.TemporaryDirectory(prefix='b718_spec_') as d:
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
    import b718_record as REC
    ctl = []
    for what, f in (('a score row of another shape', lambda: REC.read_score_row('X9', 'HELD')),
                    ('a head the ledger does not carry', lambda: REC.read_head(os.path.join(ROOT, 'data', 'b718_ferry.txt'), '### b999 absent')),
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


def refresh_commands(bank='b718_commands.json'):
    """(R328)(3)(v), standing clauses v3: THE COMMAND SCREEN READS A FRESH BANK -- the command bank rewritten by the record tool's `commands`
    route in this step, before the face's counts are read from it (b717's face read ANYPIPES 7 from a bank last written before its eighth
    pipe, events :3). Returns the bank's `at` stamp after the refresh, or None where the refresh did not write it."""
    p = os.path.join(ROOT, 'data', bank)
    t0 = time.time()
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(ROOT, 'tools', 'b718_record.py'), 'commands'], capture_output=True,
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
    print('  ### (R328)(3)(v) THE COMMAND BANK REFRESHED IN THIS STEP: %s' % (fresh or '### NOT REFRESHED'))
    if not fresh:
        print('  ### REFUSING TO EMIT A SPEC FROM A COMMAND BANK NOT WRITTEN IN THIS STEP.')
        return 4
    print('b718_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    lv_tags_after = [t for t in _git(K.LV_DIR, 'tag', '--contains', K.PORT_TIP).split(chr(10)) if t.strip() and t.strip() != K.LV_TAG]
    join_tags = [t for t in _git(K.JOIN_DIR, 'tag', '--list').split(chr(10)) if t.strip()] if os.path.isdir(K.JOIN_DIR) else []
    port_commits = _git(K.LV_DIR, 'rev-list', '--count', '%s..refs/heads/%s' % (K.PORT_TIP, K.PORT_BRANCH))
    lean_files = [f for f in _git(K.LV_DIR, 'diff', '--name-only', K.PORT_TIP, K.PORT_NEW_TIP).split(chr(10)) if f.strip().endswith('.lean')]
    first_relay = (_git(ROOT, 'rev-list', '--reverse', '%s..HEAD' % K.PRE_RELAY).split(chr(10)) or [''])[0].strip()
    # ### (R328)(8): the pin's branches read in each of the twelve kernels -- the branch's files against main, its .lean files among them
    pin_refs = dict((k, _git('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PIN_BRANCH)) for k in K.PIN_KERNELS)
    pin_files = dict((k, [f for f in _git('D:/' + k, 'diff', '--name-only', 'main', 'refs/heads/' + K.PIN_BRANCH).split(chr(10)) if f.strip()])
                     for k, h in pin_refs.items() if h)
    pin_rows = jcount('b718_pin_rows.json', lambda j: j) or []
    pin_d = [r for r in pin_rows if r.get('kind') == 'dispatch']
    pin_r = set((r.get('kernel'), str(r.get('run'))) for r in pin_rows if r.get('kind') == 'read')
    import b641_record as R41
    import b718_record as REC
    ot_l = io.open(os.path.join(K.PP, 'OPEN_TRAILS.md'), encoding='utf-8').read().replace(chr(13), '').split(chr(10))
    watch_row = ot_l[K.WATCH_LINE - 1] if len(ot_l) >= K.WATCH_LINE else ''
    measured = dict(ARMS=count_arms(text), READINGS=len(set(re.findall(r'\*\*READING \((\d+)\) --', text))),
                    EXPECT=len(re.findall(r'\*\*\((?:N|S)\d\)\*\*', text)), BARS=len(re.findall(r'^### BAR \d+', text, re.M)),
                    TESTS=jcount('b718_tests_stepzero.json', len), QUESTIONS=tcount('b718_author_answers.txt', r'^### PROMPT '),
                    LINES=jcount('b718_record_lines.json', lambda j: len(j.get('lines') or [])),
                    MISSES=tfirst('b718_citation_check.txt', r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)'),
                    PINDISP=len(pin_d), UNREAD=len([r for r in pin_d if (r['kernel'], str(r.get('run'))) not in pin_r]),
                    PINBRANCHES=len([k for k, h in pin_refs.items() if h]), PINPUSHED=len(pin_d),
                    PINFILES=sum(len(v) for v in pin_files.values()),
                    OUTSIDE=len([n_ for n_ in R41.OAI_NEEDLES if n_ in watch_row]),
                    N2BANKS=len([n_ for n_ in os.listdir(os.path.join(ROOT, 'data')) if REC.N2_FORBIDDEN.match(n_)]),
                    STANDINGWRITTEN=len(K.STANDING_NEW + K.STANDING_CHANGED),
                    ACTEDBEFORE=tcount('b718_defects.txt', r"^    \([a-z]\) THE SEAT'S \[[^]]*\]: the author's word .* acted on .*before its cites were checked"),
                    BENEATH=tcount('b718_defects.txt', r'^    \([a-z]\) .*dispatch .*beneath the 2,560 MB hold'),
                    TAGGED=jcount('arm_tags.json', lambda j: len(j.get('tags') or {})),
                    UNTAGGED=len(__import__('b718_record')._counter()['untagged']),
                    PRESEAL=tcount('b718_author_words_preseal.txt', r'^## \(\d+\) '),
                    CARRIED=carried(text), DISPATCHES=jcount('b718_commands.json', lambda j: len(j.get('dispatches') or [])),
                    RUNS=len([r for r in pin_d if (r['kernel'], str(r.get('run'))) in pin_r]),
                    PORTCOMMITS=int(port_commits) if port_commits.isdigit() else 0,
                    LEANFILES=len(lean_files) + sum(1 for v in pin_files.values() for f in v if f.endswith('.lean')),
                    TAGSMADE=len(lv_tags_after) + len(ef_tags_after) + len([t for t in join_tags if t != K.JOIN_TAG[0]]),
                    ORDERS=jcount('b718_order_lines.json', lambda j: len(j.get('lines') or [])),
                    BINARIES=len([f for f in os.listdir(os.path.join(ROOT, 'data')) if re.match(r'^b718_\w+_hashes\.txt$', f)]),
                    COMPUTE=len([n_ for n_ in ('decomp', 'derivation', 'registrations', 'a0', 'classes_controls', 'replay', 'pin')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b718_%s.txt' % n_))]),
                    WHOLEREADS=len(re.findall(r"^    \([a-z]\) THE SEAT'S: THE CARRIED (?:SUITE|TOOLS?) READ BEYOND THE SPANS",
                                              io.open(os.path.join(ROOT, 'data', 'b718_defects.txt'), encoding='utf-8').read(), re.M)),
                    SEDS=jcount('b718_commands.json', lambda j: len(j.get('seds') or [])),
                    REDIRECTS=jcount('b718_commands.json', lambda j: len(j.get('redirects') or [])),
                    PIPES=jcount('b718_commands.json', lambda j: len(j.get('pipes') or [])),
                    ANYPIPES=jcount('b718_commands.json', lambda j: len(j.get('any_pipes') or [])),
                    PYPROGS=jcount('b718_commands.json', lambda j: len(j.get('py_programs') or [])),
                    READOFF=tfirst('b718_read_calls.txt', r'OFFENCES (\d+) ; THE CAP`S PRECURSORS'))
    print()
    print('  ### ### **MEASURED OFF THE FACE, THE BANKS AND THE KERNELS, NOT TYPED:**')
    for k in ('ARMS', 'READINGS', 'EXPECT', 'BARS', 'TESTS', 'QUESTIONS', 'PRESEAL', 'LINES', 'MISSES', 'PINDISP', 'UNREAD', 'PINBRANCHES', 'PINPUSHED',
              'PINFILES', 'OUTSIDE', 'N2BANKS', 'STANDINGWRITTEN', 'ACTEDBEFORE',
              'TAGGED', 'UNTAGGED', 'BENEATH', 'CARRIED', 'DISPATCHES', 'RUNS', 'PORTCOMMITS',
              'LEANFILES', 'TAGSMADE', 'ORDERS', 'BINARIES', 'COMPUTE', 'WHOLEREADS', 'SEDS', 'REDIRECTS',
              'PIPES', 'ANYPIPES', 'PYPROGS', 'READOFF'):
        print('      %-12s %d' % (k, measured[k]))
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f) for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else (cap if dem is None else dem)),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b718_registration_2026-10-27.txt -- b718, THE DERIVATION ACT: b717 AT ITS WEIGHT; THE CORRIGENDUM; THE STANDING "
                             "LINE OF CONSISTENCY; THE COEFFICIENT LAW READ THROUGH THE CLASS GROUP; THE CONTROLS` RIPE WORK; TWO READS; THE TOOLSET "
                             "AT v1.2.0; THE FEDERATION PIN, LAST AND STOPPABLE, UNDER (R328)"),
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
