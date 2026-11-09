# -*- coding: utf-8 -*-
"""standing/v1290.py -- THE CONTROLS OF v1.29.0 ((R359)(3)(i)-(vi), (xi); b748 events (2), defects (b), (c), (d), (g), (j), (k), (l), (o), (r)), in
v1281.py's form: each instance read through the route as it stood before the repair (tools/standing/ at BASE, v1.28.1's commit, loaded from its
blobs) and through the repaired route on disk; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no
failing side. THE COMPILE CONTROL RUNS FIRST. The free memory is read and printed before each control. Written at b749 by the Write tool; no
identifier of the author is read into any string here.

  python -X utf8 -u tools/standing/v1290.py control [calls|scanbank|plain|reader|carry|log|version ...] [--bank]
"""
import importlib.util
import inspect
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
BASE = '791341fd'   # ### v1.28.1's commit at b748 Component 4, the routes before this repair
B748_SESSION = 'C:/Users/echo chamber/.claude/projects/D--/4fe446f7-cbef-42cd-9f79-d5164f63b12d.jsonl'   # ### b748's session (act_current prev_session)
B747 = ('7d34b587', 'bc1feeb5', '8b73b2a8')   # ### b747's closing head, its closing commit, its lock
HOLD = 2560
SCRATCH = os.environ.get('TEMP') or tempfile.gettempdir()
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import actlog as AL             # noqa: E402
import actmodule as AM          # noqa: E402
import carry as CA              # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import gitwrite as GW           # noqa: E402
import hook as H                # noqa: E402
import relaypath as RP          # noqa: E402
import repeat as RPT            # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def show(ref, rel, repo=RELAY):
    return _git('show', '%s:%s' % (ref, rel), repo=repo).replace('\r', '')


def old(rel, name):
    """tools/standing/<rel> as BASE left it, loaded from its blob under another name (its imports resolve against tools/standing on disk)."""
    d = tempfile.mkdtemp(dir=SCRATCH)
    p = os.path.join(d, name + '.py')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(show(BASE, 'tools/standing/' + rel))
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    shutil.rmtree(d, ignore_errors=True)
    return m


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.28.1): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.29.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.29.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _try(fn):
    try:
        return True, fn()
    except SystemExit as e:
        return False, 'REFUSED: %s' % str(e)[:130]
    except Exception as e:  # noqa: BLE001 -- either module's own Refused class
        if type(e).__name__ == 'Refused':
            return False, 'REFUSED: %s' % str(e)[:130]
        raise


# ================================================================================ (calls) (3)(i): ONE CALL OF THE TOOL PER MESSAGE
def b748_root_message():
    """the shell calls of b748's session from 04:12:00Z to 04:12:30Z, by message: the root message (an add and the root commit, both calls of
    the tool, uM4oJVYk1r) and the commit re-sent alone (aifrfH1QEv)."""
    return GW.calls_of(B748_SESSION, '2026-11-09T04:12:00', '2026-11-09T04:12:30')


def control_calls():
    L, g, n = ['### (calls) (R359)(3)(i), b748 events (2): THE ONE-CALL TOOL REFUSES A CALL WHILE ANOTHER GIT WRITE LANDED IN THE SAME MESSAGE, READING THE REQUEST STAMP THE HOOK RECORDS'], 0, 0
    OC = old('commit.py', 'commit_v1281')
    calls = b748_root_message()
    n += 1
    g += guard(L, 'calls', 'b748`s calls read from its session 4fe446f7, 04:12:00Z-04:12:30Z (the control: the instance found, not none)',
               '; '.join('%s %s %s' % (c['ts'][11:23], c['mid'][-10:], ' '.join(c['cmd'].split())[:60]) for c in calls), len(calls) >= 3)
    # ### the root message replayed as the ledger would hold it had the hook let both through: each call a record under its message's id
    recs = [dict(request=c['mid'], id='replay-%d' % k, at=c['ts'], cmd=c['cmd'], refused=None) for k, c in enumerate(calls)]
    root = [r for r in recs if 'commit.py relay root' in r['cmd']]
    first_root = root[0] if root else None
    upto = recs[:recs.index(first_root) + 1] if first_root else recs
    o_has = hasattr(OC, 'message_refusal')
    bad, note = CM.message_refusal(upto, ['relay', 'root'])
    n += 1
    g += case(L, 'calls', 'b748`s root message %s: `commit.py relay add <the root banks>` then `commit.py relay root ...`, the second call through the tool' % (first_root or {}).get('request', '?')[-10:],
              'message_refusal %s ; the tool wrote under its write mark, each call alone in its process (b748: the hook refused the second, the tool nothing)' % ('DEFINED' if o_has else 'UNDEFINED'),
              (bad or note)[:150], not o_has, bool(bad) and 'ANOTHER GIT WRITE LANDED IN THIS MESSAGE' in bad)
    again = [r for r in recs if r['request'] != (first_root or {}).get('request') and 'commit.py relay root' in r['cmd']]
    b2, n2 = CM.message_refusal(recs[:recs.index(again[0]) + 1] if again else [], ['relay', 'root'])
    n += 1
    g += guard(L, 'calls', 'the root commit re-sent alone in its own message (%s) is not refused' % (again[0]['request'][-10:] if again else '?'), b2 or n2, bool(again) and b2 is None)
    sib = [dict(r, refused='GITWRITE') if 'relay add' in r['cmd'] else r for r in upto]
    b3, n3 = CM.message_refusal(sib, ['relay', 'root'])
    n += 1
    g += guard(L, 'calls', 'a sibling the hook refused (nothing ran) is not counted', b3 or n3, b3 is None)
    rd_ = [dict(request='m1', at='t', cmd='git -C D:/relay status --porcelain', refused=None), dict(request='m1', at='t', cmd='python -X utf8 -u tools/standing/commit.py relay "component 1" "x"', refused=None)]
    b4, n4 = CM.message_refusal(rd_, ['relay', 'component 1'])
    n += 1
    g += guard(L, 'calls', 'a read beside the commit in its message is not a write', b4 or n4, b4 is None)
    bare = [dict(request='m2', at='t', cmd='cd D:/relay && git add data/x.txt', refused=None), dict(request='m2', at='t', cmd='python -X utf8 -u tools/standing/commit.py relay "component 1" "x"', refused=None)]
    b5, n5 = CM.message_refusal(bare, ['relay', 'component 1'])
    n += 1
    g += guard(L, 'calls', 'the bare `git add` beside the commit in its message is a git write: the commit refused', (b5 or n5)[:120], bool(b5))
    lp = os.path.join(tempfile.mkdtemp(dir=SCRATCH), 'calls.jsonl')
    sess = A.current().get('session') or ''
    H.record_call(dict(transcript_path='C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sess, tool_use_id='control'), 'Bash', dict(command='git status'), None, path=lp)
    got = CM.calls_tail(lp)
    shutil.rmtree(os.path.dirname(lp), ignore_errors=True)
    n += 1
    g += guard(L, 'calls', 'the hook`s record_call writes one record carrying the message`s request stamp (this session`s transcript)', json.dumps(got[-1] if got else {})[:150],
               len(got) == 1 and bool(got[0].get('request')) and got[0].get('cmd') == 'git status')
    return L, g, n


# ================================================================================ (scanbank) (3)(ii): THE PER-COMMIT SCAN'S OWN BANK
def control_scanbank():
    L, g, n = ['### (scanbank) (R359)(3)(ii), b748 defect (r): THE SCAN BEFORE EACH COMMIT APPENDS TO data/<act>_address_scan_commits.txt; THE ACT`S SCAN BANK, WHICH THE ROOT ROUTE NAMES, IS NOT REWRITTEN'], 0, 0
    OC = old('commit.py', 'commit_v1281')
    gates = AL.by_phase('b748', 'gate')
    carried = [h[:8] for h in gates if 'data/b748_address_scan.txt' in _git('show', '--name-only', '--format=', h).split(NL)]
    n += 1
    g += guard(L, 'scanbank', 'b748`s gate commits read by their step rows (the instances: %d)' % len(gates), ' '.join(h[:8] for h in gates), len(gates) == 6)
    ob = show(BASE, 'tools/standing/commit.py')
    src = ob[ob.index('def run_scan('):ob.index('def carry_check(')]   # ### the route before, read from its blob
    act = A.current().get('act')
    bank = os.path.join(D, '%s_address_scan.txt' % act)
    before = open(bank, 'rb').read() if os.path.exists(bank) else None
    sd = tempfile.mkdtemp(dir=SCRATCH)
    try:
        ok_, out = _try(lambda: CM.run_scan(act, 'the (scanbank) control', bank_dir=sd))
        after = open(bank, 'rb').read() if os.path.exists(bank) else None
        cb = os.path.join(sd, A.scan_commits_name(act))
        runs = open(cb, encoding='utf-8').read().count('## THE SCAN BEFORE THE COMMIT') if os.path.exists(cb) else 0
    finally:
        shutil.rmtree(sd, ignore_errors=True)
    n += 1
    g += case(L, 'scanbank', 'the scan before a commit (run_scan), and the act`s scan bank data/%s_address_scan.txt across it' % act,
              'run_scan passes --bank (%s): the root-named bank rewritten at every commit; b748`s gate commits carrying it: %s; rootdry READY False 51 of 53 at 0b8ad609 till restored (defect (r))' % ("'--bank'" in src, ' '.join(carried) or 'none'),
              'run %s ; the act`s scan bank %s ; the per-commit bank runs %d' % ('CLEAN' if ok_ else out, 'UNCHANGED' if before == after else '### CHANGED', runs),
              "'--bank'" in src and bool(carried), ok_ and before == after and runs == 1)
    rx = re.search(r"EXCLUDE_KINDS = P7\.EXCLUDE_KINDS \+ r'([^']*)'", io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read())
    n += 1
    g += guard(L, 'scanbank', 'the per-commit bank an excluded kind of the root route (record.tpl EXCLUDE_KINDS), after the lock by design (post_lock_appended), a bookkeeping file (repeat.bookkeeping_only)',
               'excluded %s ; post-lock %s ; bookkeeping %s' % (bool(rx and 'address_scan_commits' in rx.group(1)), 'data/b749_address_scan_commits.txt' in A.post_lock_appended('b749'),
                                                               RPT.bookkeeping_only(['data/b749_steps.json', 'data/b749_address_scan_commits.txt'], 'b749')),
               bool(rx and 'address_scan_commits' in rx.group(1)) and 'data/b749_address_scan_commits.txt' in A.post_lock_appended('b749') and RPT.bookkeeping_only(['data/b749_address_scan_commits.txt'], 'b749'))
    n += 1
    g += guard(L, 'scanbank', 'the act`s scan bank and the post-lock bank keep their names (written at the scan`s step and after the lock)', '%s ; %s' % (A.scan_bank_name('b749', False), A.scan_bank_name('b749', True)),
               A.scan_bank_name('b749', False) == 'b749_address_scan.txt' and A.scan_bank_name('b749', True) == 'b749_address_scan_postlock.txt')
    return L, g, n


# ================================================================================ (plain) (3)(iii): NO COMMIT WITHOUT THE SCAN
def control_plain():
    L, g, n = ['### (plain) (R359)(3)(iii), b748 defects (b), (d): THE COMMIT TOOL RUNS THE SCAN ITSELF AND A COMMIT WITHOUT IT IS REFUSED -- BY THE TOOL (no scanner=False) AND BY THE HOOK (a plain git write)'], 0, 0
    OH = old('hook.py', 'hook_v1281')
    OC = old('commit.py', 'commit_v1281')
    seq = GW.calls_of(B748_SESSION, '2026-11-08T21:32:20', '2026-11-08T21:32:40')
    add_ = [c for c in seq if 'git add' in c['cmd']]
    n += 1
    g += guard(L, 'plain', 'be4a5a0d`s sequence read from b748`s session (the instances: the add and the commit)', '; '.join('%s %s' % (c['ts'][11:23], ' '.join(c['cmd'].split())[:70]) for c in seq), len(seq) >= 2 and bool(add_))
    for what, cmd in (('be4a5a0d`s add, by plain git (b748 21:32:26Z)', add_[0]['cmd'] if add_ else 'cd D:/relay && git add data/b747_relay_push-b747-closing_push_out.txt'),
                      ('b747`s step-zero commit by plain git, the row chained after it (b746`s form, its session 01:55:06Z)', 'git commit -q -m "b746 step zero: x" && python -X utf8 -u tools/standing/fold.py record step relay')):
        o = OH.judge('Bash', dict(command=cmd))
        w = H.judge('Bash', dict(command=cmd))
        n += 1
        g += case(L, 'plain', '%s: %s' % (what, ' '.join(cmd.split())[:90]), 'judge -> %s' % (o[0] if o else 'ALLOWED'), 'judge -> %s' % (w[0] if w else 'ALLOWED'),
                  o is None or o[0] != 'PLAINGIT', bool(w) and w[0] == 'PLAINGIT')
    cmd = 'git -C D:/relay branch -d push-b747-closing'
    o, w = OH.judge('Bash', dict(command=cmd)), H.judge('Bash', dict(command=cmd))
    n += 1
    g += guard(L, 'plain', 'a branch delete by plain git (b748 #56: %s) refused as PLAINGIT; v1.28.1 read it as %s' % (cmd, o[0] if o else 'ALLOWED'), 'judge -> %s' % (w[0] if w else 'ALLOWED'),
               bool(w) and w[0] == 'PLAINGIT')
    r = tempfile.mkdtemp(dir=SCRATCH)
    dd = os.path.join(r, 'data')
    try:
        os.makedirs(dd)
        _git('init', '-q', repo=r)
        _git('-c', 'user.email=x@x.invalid', '-c', 'user.name=x', 'commit', '-q', '--allow-empty', '-m', 'base', repo=r)
        io.open(os.path.join(r, 'a.txt'), 'w', encoding='utf-8').write('a\n')
        _git('add', 'a.txt', repo=r)
        o_ok, o = _try(lambda: OC.run(r, 'component 1', 'a planted commit', act='b999', data=dd, row_writer=lambda *a: (0, 'no row'), scanner=False))
        o_made = _git('rev-list', '--count', 'HEAD', repo=r).strip()
        io.open(os.path.join(r, 'b.txt'), 'w', encoding='utf-8').write('b\n')
        _git('add', 'b.txt', repo=r)
        n_ok, nw = _try(lambda: CM.run(r, 'component 1', 'a planted commit', act='b999', data=dd, row_writer=lambda *a: (0, 'no row'), scanner=False))
        n_made = _git('rev-list', '--count', 'HEAD', repo=r).strip()
    finally:
        shutil.rmtree(r, ignore_errors=True)
    n += 1
    g += case(L, 'plain', 'run(<scratch repository>, component 1, scanner=False): a commit with the scan skipped',
              '%s ; commits now %s' % ('COMMITTED' if o_ok else o, o_made), '%s ; commits now %s' % ('COMMITTED' if n_ok else nw, n_made),
              o_ok and o_made == '2', not n_ok and n_made == '2' and 'WITHOUT THE SCAN' in nw)
    for what, cmd in (('the one-call tool`s add', 'python -X utf8 -u tools/standing/commit.py relay add data/b749_rules.txt'),
                      ('a status read', 'git -C D:/relay status --porcelain'), ('a branch listing', 'git -C D:/relay branch --merged main --list "push-b748-*"')):
        w = H.judge('Bash', dict(command=cmd))
        n += 1
        g += guard(L, 'plain', '%s is not a plain git write: %s' % (what, cmd[:70]), 'judge -> %s' % (w[0] if w else 'ALLOWED'), w is None or w[0] != 'PLAINGIT')
    return L, g, n


# ================================================================================ (reader) (3)(iv): A READER OF THE RECORD REFUSES A NONEXISTENT PATH
def control_reader():
    L, g, n = ['### (reader) (R359)(3)(iv), b748 defect (j): EVERY READER OF THE RECORD REFUSES A PATH THE REPOSITORY DOES NOT HOLD AND PRINTS IT (relaypath.rows_of, grep_of)'], 0, 0
    ORP = old('relaypath.py', 'relaypath_v1281')
    o_has = hasattr(ORP, 'grep_of')
    raw = _git('grep', '-n', 'Epstein', '--', 'CLUSTERS.md', repo=PP)
    n_ok, nw = _try(lambda: RP.grep_of(PP, 'CLUSTERS.md', 'Epstein', out=[]))
    n += 1
    g += case(L, 'reader', 'b748`s first line-bank dry: the cluster table read by a grep of PLACE-papers CLUSTERS.md for the instance',
              'git grep -> %r, printed NONE (a vacuous read; grep_of %s)' % (raw[:40], 'DEFINED' if o_has else 'UNDEFINED'), nw if not n_ok else 'READ %r' % (nw,),
              raw == '' and not o_has, not n_ok and 'CLUSTERS.md' in nw and 'resolves to no file' in nw)
    out = []
    ok_, rows = _try(lambda: RP.rows_of(PP, 'SPIRAL_MAP.md', 264, 286, out=out))
    tab = [l for l in (rows if ok_ else []) if l.startswith('|') and not re.match(r'^\|[\s\-:|]+\|?\s*$', l)]
    n += 1
    g += guard(L, 'reader', 'SPIRAL_MAP.md :264-:286 read with its row count (the cluster table b748 read after the catch: 8 cluster rows, none naming the instance)',
               '%s ; table rows %d (header included) ; a row naming the instance: %s' % (out[0].strip() if out else '', len(tab), any('Epstein' in l for l in tab)),
               ok_ and len(rows) == 23 and len(tab) >= 8)
    n_ok2, nw2 = _try(lambda: RP.rows_of(PP, 'NO_SUCH_FILE.md', out=[]))
    n += 1
    g += guard(L, 'reader', 'rows_of a file the repository does not hold refuses, printing the path', nw2, not n_ok2 and 'NO_SUCH_FILE.md' in nw2)
    return L, g, n


# ================================================================================ (carry) (3)(v): THE CARRY BESIDE THE RULING, ROW BY ROW; THE KEPT ROW BY THE TOOL
def control_carry():
    L, g, n = ['### (carry) (R359)(3)(v), b748 defects (c), (o): THE CARRY PRINTS EVERY CARRIED CITATION ROW BESIDE THE RULING AND REFUSES A COMMIT IT DOES NOT NAME; THE STEP-ZERO KEPT ROW WRITTEN BY THE TOOL'], 0, 0
    OCA = old('carry.py', 'carry_v1281')
    subs = (('b748', 'b749'), ('b747', 'b748'))
    sub2 = (('b747', 'b748'), ('b746', 'b747'))
    a748, a747 = show('HEAD', 'tools/acts/b748.py'), show('HEAD', 'tools/acts/b747.py')
    w748, w747 = show('HEAD', 'tools/b748_worklist.py'), show('HEAD', 'tools/b747_worklist.py')
    fer = show('HEAD', 'data/b748_ferry.txt')
    # ### b748's module as the carry left it: each citation section b747's after the substitution (the rows b748 rewrote before its check)
    pb = dict((k, a747[s:e]) for k, s, e in AM.blocks(a747))
    out, last = [], 0
    for k, s, e in AM.blocks(a748):
        out.append(a748[last:s])
        out.append(CA.substitute(pb[k], sub2) if (k[:2] == ('SECTION', 'citation') and k in pb) else a748[s:e])
        last = e
    carried = ''.join(out) + a748[last:]
    nsec = sum(1 for k, s, e in AM.blocks(carried) if k[:2] == ('SECTION', 'citation') and k in pb and carried[s:e] == CA.substitute(pb[k], sub2))
    Lo, ro = OCA.ruled(carried, a747, w748, w747, fer, sub2)
    Ln, rn = CA.ruled(carried, a747, w748, w747, fer, sub2)
    r4 = [r for r in rn if r[0] == 'R4']
    n += 1
    g += case(L, 'carry', 'b748`s module with its %d citation sections as carried from b747 (before b748 rewrote 1 and 4), beside data/b748_ferry.txt' % nsec,
              'REFUSED %d (%s)' % (len(ro), ', '.join(sorted(set(r[0] for r in ro))) or 'none'), 'REFUSED %d, R4 %d: %s' % (len(rn), len(r4), '; '.join(r[1] for r in r4)[:110]),
              not any(r[0] == 'R4' for r in ro) and not [r for r in ro if 'citation' in r[1]], bool(r4) and any(r[1] in ('SECTION citation 1', 'SECTION citation 4') for r in r4))
    rows_printed = [l for l in Ln if l.startswith('  SECTION citation')]
    n += 1
    g += guard(L, 'carry', 'every carried citation section printed with its rows and commits beside the ruling', '%d sections printed, e.g. %s' % (len(rows_printed), rows_printed[0].strip()[:90] if rows_printed else ''), len(rows_printed) == nsec)
    a749, w749 = io.open(os.path.join(T, 'acts', 'b749.py'), encoding='utf-8').read(), io.open(os.path.join(T, 'b749_worklist.py'), encoding='utf-8').read()
    L9, r9 = CA.ruled(a749, a748, w749, w748, io.open(os.path.join(D, 'b749_ferry.txt'), encoding='utf-8').read(), subs)
    n += 1
    g += guard(L, 'carry', 'b749`s module and worklist as they stand, beside data/b749_ferry.txt: none refused', L9[-1].strip()[:120], not r9)
    s46 = (show('HEAD', 'data/b748_stepzero.txt').split(NL) + [''] * 50)[45]
    row = CA.kept_row('b749')
    n += 1
    g += case(L, 'carry', 'the step-zero row "KEPT as banked:" (b748`s :46, by hand) against the tool`s row from the branch listing', s46.strip()[:100],
              row[:60] + ' ... port-b707 %s' % ('NAMED (cb0aea56)' if 'port-b707 (cb0aea56)' in row else '### ABSENT'),
              'port-b707' not in s46 and not hasattr(OCA, 'kept_row'), 'port-b707 (cb0aea56)' in row and 'zq-b730 (1e658870)' in row and 'push-b749-' not in row)
    return L, g, n


# ================================================================================ (log) (3)(vi): A PRIOR ACT'S LOG TO ITS LOCK, BY STEP ROWS
def control_log():
    L, g, n = ['### (log) (R359)(3)(vi), b748 defects (g), (l): A CONTROL READING A PRIOR ACT`S LOG READS IT TO THAT ACT`S LOCK AND CHOOSES COMMITS BY STEP ROWS (actlog.py), NOT BY GREP'], 0, 0
    o_gate = [h for h in _git('log', '--format=%H', '--grep=^b747 gate', 'c19fde00').split(NL) if h]
    n_gate = AL.by_phase('b747', 'gate')
    lk = AL.lock('b747')
    before_lock = bool(lk) and all(subprocess.run(['git', '-C', RELAY, 'merge-base', '--is-ancestor', h, lk]).returncode == 0 for h in n_gate)
    n += 1
    g += case(L, 'log', 'the (gate) case: b747`s gate commits (b748 (g): the replay read to c19fde00 and missed 88f39b22)',
              '%d by grep to c19fde00: %s ; 88f39b22 %s' % (len(o_gate), ' '.join(h[:8] for h in o_gate), 'PRESENT' if any(h.startswith('88f39b22') for h in o_gate) else 'ABSENT'),
              '%d by step rows, to the lock %s: %s ; 88f39b22 %s' % (len(n_gate), (lk or '?')[:8], ' '.join(h[:8] for h in n_gate), 'PRESENT' if any(h.startswith('88f39b22') for h in n_gate) else 'ABSENT'),
              not any(h.startswith('88f39b22') for h in o_gate), len(n_gate) == 6 and any(h.startswith('88f39b22') for h in n_gate) and before_lock)
    o_rows = [h for h in _git('log', '--format=%H', '--grep=the step row', '%s~40..%s' % (B747[1], B747[0])).split(NL) if h]
    n_rows = AL.step_rows_commits('b747')
    n += 1
    g += case(L, 'log', 'the (rows) case: b747`s step-rows commits (b748 (l): `--grep=the step row` took 0c118109, a component commit)',
              '%d by grep: %s ; 0c118109 %s' % (len(o_rows), ' '.join(h[:8] for h in o_rows), 'TAKEN' if any(h.startswith('0c118109') for h in o_rows) else 'NOT TAKEN'),
              '%d by step rows (commits no row names, touching the step bank alone): %s ; 0c118109 %s' % (len(n_rows), ' '.join(h[:8] for h in n_rows), 'TAKEN' if any(h.startswith('0c118109') for h in n_rows) else 'NOT TAKEN'),
              any(h.startswith('0c118109') for h in o_rows), bool(n_rows) and not any(h.startswith('0c118109') for h in n_rows) and all(_git('log', '-1', '--format=%s', h).startswith('b747 ') for h in n_rows))
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R359)(3)(xi): THE STANDING VERSION PRINTED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = show(BASE, 'tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.28.1', ver == 'v1.29.0')
    return L, g, n


CONTROLS = {'calls': control_calls, 'scanbank': control_scanbank, 'plain': control_plain, 'reader': control_reader, 'carry': control_carry,
            'log': control_log, 'version': control_version}
ORDER = ('calls', 'scanbank', 'plain', 'reader', 'carry', 'log', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.29.0, (R359)(3)(i)-(vi), (xi): ONE CALL OF THE TOOL PER MESSAGE, THE PER-COMMIT SCAN`S OWN BANK, NO COMMIT '
           'WITHOUT THE SCAN, THE RECORD`S READERS REFUSING A MISSING PATH, THE CARRY ROW BY ROW AND THE KEPT ROW BY THE TOOL, A PRIOR ACT`S LOG BY STEP ROWS (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per repair: %s' % ' ; '.join(per))
    out.append('### ### **v1.29.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1290.txt' % act), NL.join(out))
        print('written data/%s_standing_v1290.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
