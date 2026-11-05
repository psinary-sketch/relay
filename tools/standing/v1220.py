# -*- coding: utf-8 -*-
"""standing/v1220.py -- THE CONTROLS OF v1.22.0 ((R352)(2)(i)-(vi)), in v1210.py's form: each instance read through the route as it stood before the repair and through
the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST
AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the repair is read from the blob at BASE (b741's closing), not from disk. Written at b742 by
the Write tool.

  python -X utf8 -u tools/standing/v1220.py control [dispatch|remote|counter|slips|repeat|version ...] [--bank]
"""
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import types

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
BASE = '13498fd2'   # ### b741's closing, the toolset as v1.21.0 left it
B741_TRANSCRIPT = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', '352ad3f4-37c5-4360-b9c6-cb7368f5f805.jsonl')
B742_TRANSCRIPT = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', 'c66dda9f-cc02-473a-b740-111b6d66dec3.jsonl')
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import counter as CNT           # noqa: E402
import dispatchrows as DR       # noqa: E402
import figbank as FB            # noqa: E402
import harnessmoves as HM       # noqa: E402
import remotecache as RCACHE    # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def base_module(rel, name):
    """the module at BASE, read from its blob and run in a fresh namespace, not from disk."""
    m = types.ModuleType(name)
    m.__file__ = os.path.join(RELAY, *rel.split('/'))
    exec(compile(_git('show', '%s:%s' % (BASE, rel)), name, 'exec'), m.__dict__)
    return m


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.21.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.22.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.22.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


# ### b741's dispatch 2 (data/b741_dispatch_rows.json :9), the word it rode on (data/b741_author_answers.txt :7), the word's first commit
D2 = dict(kernel='SIDE-explicit-formula', item='G1+G2', n=2, workflow='build-module.yml', at_ref='main', sha='de4810da5d3cfc524002630959b32e4ebc30ce66',
          target='SIDEExplicitFormula.Schema.ZQ.OffZero.Series SIDEExplicitFormula.Schema.ZQ.OffZero.Sums', run=41935365948, at='2026-11-04T23:38:52Z')
D2_READ = (4705, '2026-11-04T23:38:52Z')
WORD9 = ('data/b741_author_answers.txt', '="(K) kernel route"')
WORD2 = ('data/b742_author_answers.txt', 'The author’s word amending (R352)(3)')


def control_dispatch():
    L, g, n = ['### (dispatch) (R352)(2)(i), b741 DEFECT (q): A DISPATCH CONDITIONED ON THE AUTHOR`S WORD WAITS ON THE COMMIT CARRYING THAT WORD, ITS HASH IN THE ROW'], 0, 0
    old = base_module('tools/standing/dispatchrows.py', 'old_dispatchrows')
    try:
        old.row('dispatch', D2_READ, **D2)
        o_ok = 'ACCEPTED, no licence asked'
    except ValueError as e:
        o_ok = 'refused: %s' % e
    try:
        DR.licence(*WORD9, by=D2['at'])
        n_ref = 'NOT REFUSED'
    except DR.Refused as e:
        n_ref = str(e)
    try:
        DR.row('dispatch', D2_READ, **D2)
        n_row = 'ACCEPTED'
    except DR.Refused as e:
        n_row = str(e)
    n += 1
    g += case(L, 'dispatch', 'b741`s dispatch 2 replayed (run 41935365948, 23:38:52Z), riding on the word "(K) kernel route" (data/b741_author_answers.txt :7)',
              'dispatchrows at %s: the row %s' % (BASE, o_ok), 'licence at 23:38:52Z: %s ; the row with no licence: %s' % (n_ref[:170], n_row[:120]),
              o_ok.startswith('ACCEPTED'), n_ref.startswith('### NOT DISPATCHED') and 'THE ROW REFUSED' in n_row)
    lic = DR.licence(*WORD9)
    r9 = DR.row('dispatch', (D2_READ[0], lic['committed_at']), **dict(D2, at=lic['committed_at'], licence=lic))
    n += 1
    g += guard(L, 'dispatch', 'the same dispatch after the word`s commit: the licence read with no bound, the row carrying it accepted at the commit`s time',
               'licence %s (data/b741_author_answers.txt :%d, committed %s) ; the row`s licence %s' % (lic['commit'][:8], lic['line'], lic['committed_at'], r9['licence']['commit'][:8]),
               lic['commit'].startswith('1c74cfcf') and r9['licence']['commit'] == lic['commit'])
    l2 = DR.licence(*WORD2)
    n += 1
    g += guard(L, 'dispatch', 'b742`s own word (data/b742_author_answers.txt :10), the licence every b742 dispatch row names',
               'licence %s (the word first met at :%d, the RESULT line beside :10) committed %s' % (l2['commit'][:8], l2['line'], l2['committed_at']), l2['commit'].startswith('1f96d4ea'))
    return L, g, n


def _phases(text):
    m = re.search(r'the banks and the state (\d+);.*?the prior banks \(not in this part\) (\d+); the act-root chain`s part (\d+);', text or '')
    t = re.search(r'### the run took (\d+) s', text or '')
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(t.group(1)) if t else None) if m else None


def _slow_table():
    """the post-push standing-b2c run that took 2047 s: its own bank was overwritten by the re-run; its lines survive in session 352ad3f4's transcript (07:00:05Z, the output file read)."""
    if not os.path.exists(B741_TRANSCRIPT):
        return None, 'the transcript absent'
    with open(B741_TRANSCRIPT, encoding='utf-8', errors='replace') as f:
        for l in f:
            if 'the act-root chain`s part 1970' in l and '"type":"user"' in l:
                j = json.loads(l)
                for b in j['message']['content']:
                    if isinstance(b, dict) and b.get('type') == 'tool_result':
                        t = b['content'] if isinstance(b['content'], str) else ''
                        return _phases(t), j.get('timestamp')
    return None, 'not found'


def control_remote():
    L, g, n = ['### (remote) (R352)(2)(ii), b741 EVENT (4): THE POST-PUSH CHAIN`S CAUSE; ONE REMOTE READ PER REPOSITORY PER SUITE RUN, CACHED, EACH READ TIMED; THE HARNESS`S MOVE ITS OWN ACT'], 0, 0
    pre = _phases(io.open(os.path.join(D, 'b741_checks_standing-b2c.txt'), encoding='utf-8').read())
    re_ = _phases(io.open(os.path.join(D, 'b741_checks_postpush_standing-b2c.txt'), encoding='utf-8').read())
    slow, at = _slow_table()
    L += ['  THE PHASE TABLES OF standing-b2c, SIDE BY SIDE (seconds: the banks and the state | the prior banks | the act-root chain`s part | the run):',
          '      pre-push   (data/b741_checks_standing-b2c.txt :5)              %s' % (' | '.join('%5s' % x for x in pre) if pre else 'UNREAD'),
          '      post-push  (the run moved to the background; transcript %s) %s' % (at, ' | '.join('%5s' % x for x in slow) if slow else 'UNREAD'),
          '      post-push  re-run in the foreground (data/b741_checks_postpush_standing-b2c.txt :5) %s' % (' | '.join('%5s' % x for x in re_) if re_ else 'UNREAD')]
    lsr = [json.load(io.open(os.path.join(D, f), encoding='utf-8')) for f in ('b741_lsr_standing-b2c.json', 'b741_lsr_postpush_standing-b2c.json')]
    cnt = [(len(x['lsr']), max(x['lsr'].values())) for x in lsr]
    L += ['  THE REMOTE READS: the pre-push part %d repositories, at most %d each (data/b741_lsr_standing-b2c.json); the re-run %d, at most %d (data/b741_lsr_postpush_standing-b2c.json);' % (cnt[0] + cnt[1]),
          '    the slow run`s own remote-read bank was overwritten by the re-run (the bank names the file, not the run), and v1.21.0 timed no read: its count is not banked',
          '    and no read`s time was recorded. THE CAUSE, AS THE BANKS ALLOW IT TO BE NAMED: the excess (%s s over %s) sits wholly in the act-root chain`s phase, the phase that holds' % (
              (slow[2] - re_[2]) if slow and re_ else '?', re_[2] if re_ else '?'),
          '    the part`s remote reads (act_root.verify through b616_claims.remote_refs: the tags` peels and the heads against the remote mains, 38 repositories); the other phases',
          '    moved by at most 3 s; the seat`s reading at the time (python and git live, "probably slow ls-remote calls") is a process listing, not a measurement. The repair',
          '    reads each repository once per suite run and times every read, so a slow read is printed by its repository and its seconds the next time.']
    n += 1
    g += guard(L, 'remote', 'the three tables read; the chain phase the only one to move (the slow run`s chain phase over 5 times the re-run`s; the other phases within 15 s)',
               'pre %s ; slow %s ; re-run %s' % (pre, slow, re_), bool(pre and slow and re_) and slow[2] > 5 * re_[2] and abs(slow[0] - re_[0]) <= 15 and abs(slow[1] - re_[1]) <= 15)
    # ### the cache: two parts of one suite run, each its own process (its own memo), reading the same repositories
    calls = []

    def fake(path):
        calls.append(path)
        return {'refs/heads/main': 'f' * 40}
    repos = ['D:/relay', 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-explicit-formula']
    old_parts = []
    for _part in range(2):
        memo = {}
        for p in repos:
            if p not in memo:
                memo[p] = fake(p)
        old_parts.append(len(calls))
    old_reads = len(calls)
    calls.clear()
    key = 'control_v1220_%d' % int(time.time() * 1000)
    logs = []
    for _part in range(2):
        lg = {}
        rr = RCACHE.wrap(fake, key, lg)
        for p in repos:
            rr(p)
        logs.append(lg)
    new_reads = len(calls)
    try:
        os.remove(RCACHE._path(key))
    except OSError:
        pass
    n += 1
    g += case(L, 'remote', 'two parts of one suite run over three repositories, each part its own process',
              'per-process memo (b616_claims.remote_refs): %d reads' % old_reads, 'the run cache: %d reads, the second part`s %s' % (
                  new_reads, ', '.join('%s %s' % (os.path.basename(p), 'cached' if v['cached'] else 'read') for p, v in logs[1].items())),
              old_reads == 2 * len(repos), new_reads == len(repos) and all(v['cached'] for v in logs[1].values()) and all('secs' in v for v in logs[0].values()))
    # ### the part re-run under the repair: b741's standing-b2c over b740's banks (`fold.py checks --prev --part standing-b2c --act b741`), twice, in
    # ### the foreground at b742's Component 1; the membrane refused each write (b741's root names its prevrun bank), so the figures are read from
    # ### this session's transcript, as the slow run's are from b741's
    runs = []
    if os.path.exists(B742_TRANSCRIPT):
        with open(B742_TRANSCRIPT, encoding='utf-8', errors='replace') as f:
            for l in f:
                if '"type":"user"' in l and 'THE REMOTE READS OF THIS SUITE RUN (key b740_prev_' in l and 'standing-b2c' in l:
                    j = json.loads(l)
                    for b in j['message']['content']:
                        if isinstance(b, dict) and b.get('type') == 'tool_result':
                            t = b['content'] if isinstance(b['content'], str) else ' '.join(x.get('text', '') for x in b['content'] if isinstance(x, dict))
                            m = re.search(r'read by this part (\d+) ; from the run cache (\d+) ; the reads` seconds ([\d.]+) ; the slowest (\S+) ([\d.]+) s', t)
                            ph = _phases(t)
                            if m and ph:
                                runs.append((j.get('timestamp'), ph, int(m.group(1)), int(m.group(2)), float(m.group(3)), m.group(4), float(m.group(5))))
    for r in runs:
        L += ['  THE PART RE-RUN UNDER THE REPAIR at %s: phases %s ; read %d, cached %d, the reads` seconds %.1f, the slowest %s %.2f s' % r]
    if runs:
        L += ['  THE CAUSE, MEASURED: under the repair the part`s %d remote reads took %.1f s in all (the slowest %.2f s) inside a %d s chain phase, and the warm run with no read' % (
                  runs[0][2], runs[0][4], runs[0][6], runs[0][1][2]),
              '    at all still took %d s there; the chain phase is local work (the banks read at their commits). The remote reads explain the slow run`s %s s excess only if' % (
                  runs[1][1][2] if len(runs) > 1 else -1, (slow[2] - re_[2]) if slow and re_ else '?'),
              '    one read stalled for most of it, and no bank of b741 names a repository or a time: THE RULING`S NAMED CAUSE IS NOT ESTABLISHED BY THE BANKS. The repair lands',
              '    as ordered (one read per repository per suite run, cached) and times every read, so a stall is named by its repository and its seconds when it recurs.']
    n += 1
    g += guard(L, 'remote', 'the part re-run under the repair, cold then warm: the cold run reads 38 repositories once each and times them; the warm run reads none and takes them from the run cache',
               '%d runs read from the transcript' % len(runs), len(runs) >= 2 and runs[0][2] == 38 and runs[0][3] == 0 and runs[1][2] == 0 and runs[1][3] == 38)
    k1 = RCACHE.run_key('b742', 'run', ('D:/relay',))
    k2 = RCACHE.run_key('b742', 'prerun', ('D:/relay',))
    n += 1
    g += guard(L, 'remote', 'the run key: a mode or a remote-tracking ref that moves gives another key, so the post-push run reads its own remotes',
               '%s ; %s' % (k1, k2), k1 != k2 and k1.startswith('b742_run_'))
    mv = HM.moves(B741_TRANSCRIPT)
    bg = [b for b in HM.seat_bg(B741_TRANSCRIPT) if 'standing-b2c' in b['command'] and 'postpush' in b['command']]
    old_n1 = io.open(os.path.join(D, 'b741_closing.txt'), encoding='utf-8').read()
    o_bg = re.search(r'suite parts sent in the background: (\d+)', old_n1)
    n += 1
    g += case(L, 'remote', 'b741`s post-push standing-b2c, moved to the background by the harness at its 600 s timeout (task bh6cl8npl)',
              'N1`s figure (data/b741_closing.txt :152) "suite parts sent in the background: %s", the harness`s move named nowhere' % (o_bg.group(1) if o_bg else '?'),
              '%s ; the b2c post-push call the seat sent in the background: %d' % (HM.line(B741_TRANSCRIPT)[:200], len(bg)),
              bool(o_bg) and o_bg.group(1) == '0' and 'harness' not in old_n1.split('suite parts sent in the background')[1][:200].lower(),
              any(m['task'] == 'bh6cl8npl' and 'standing-b2c' in m['command'] for m in mv) and not bg)
    return L, g, n


def control_counter():
    L, g, n = ['### (counter) (R352)(2)(iii), b741 TOUCH ROW (28): THE COUNTER COMPOSED ONCE FROM THE DEFECTS AND EVENTS BANKS, ITS SET NAMED; b741`S FIGURES WITH THEIR CAUSE'], 0, 0
    touch = io.open(os.path.join(D, 'b741_touch.txt'), encoding='utf-8').read().replace('\r', '').split(NL)[34]
    fd = subprocess.run(['git', '-C', 'D:/MY-DOwnloads/PLACE-papers', 'show', 'efce669:FINDINGS.md'], capture_output=True).stdout.decode('utf-8', 'replace').replace('\r', '').split(NL)[13600]
    cl = io.open(os.path.join(D, 'b741_closing.txt'), encoding='utf-8').read().replace('\r', '').split(NL)[4]
    figs = [re.search(r'CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) (?:of|OF) (\d+)', x) for x in (touch, fd, cl)]
    figs = [tuple(int(v) for v in m.groups()) if m else None for m in figs]
    # ### the items as the closing commit holds them, each event with the time its own row carries; each printer's set: every defect (all lettered
    # ### before the lock) and the events whose time precedes the printer's commit. The entry was composed in the working tree between event (1)
    # ### (05:08:38Z) and event (2) (06:03:34Z): no relay commit holds that set (the events bank first committed at 605b5641 with three rows)
    td, te = _git('show', '13498fd2:data/b741_defects.txt'), _git('show', '13498fd2:data/b741_events.txt')
    it = CNT.items(td, te)
    etime = dict(('event (%s)' % m.group(1), '2026-11-05T%sZ' % m.group(2)) for m in re.finditer(r"(?m)^    \((\d+)\) [^\]]*\]: (\d\d:\d\d:\d\d)Z", te))
    ct = lambda repo, sha: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(_git('log', '-1', '--format=%ct', sha, repo=repo).strip())))  # noqa: E731
    at = [('the touch read at the lock', 'relay 9d37eea8', ct(RELAY, '9d37eea8')), ('the entry at the pre-root', 'PLACE-papers 0ff5443f', ct('D:/MY-DOwnloads/PLACE-papers', '0ff5443f')),
          ('the closing', 'relay 13498fd2', ct(RELAY, '13498fd2'))]
    cs = [CNT.tally([x for x in it if x[0].startswith('defect') or etime.get(x[0], '9') <= t], 'b741', r) for _w, r, t in at]
    L += ['  THE THREE FIGURES b741 PRINTED: the touch read`s row (28) %s (data/b741_touch.txt :35); FINDINGS :13601 %s (PLACE-papers efce669); the closing %s (data/b741_closing.txt :5)' % tuple(figs)]
    L += ['  THE EVENTS` OWN TIMES: ' + ', '.join('%s %s' % kv for kv in sorted(etime.items()))]
    L += ['  THE ONE COMPOSER AT EACH PRINTER`S MOMENT: ' + ' ; '.join('%s (%s, %s) %s' % (w, r, t, CNT.line(c)) for (w, r, t), c in zip(at, cs))]
    c01, c12 = CNT.cause(cs[0], cs[1]), CNT.cause(cs[1], cs[2])
    L += ['  THE CAUSE: the touch read to the entry adds %s (entered after the lock, before the seal); the entry to the closing adds %s' % (
        ', '.join(c01['only_second']) or 'none', ', '.join(c12['only_second']) or 'none')]
    old_named = any('defects' in x and 'events' in x and re.search(r'\(defects \d+, events \d+\)', x) for x in (touch, fd, cl))
    n += 1
    g += case(L, 'counter', 'b741`s three figures, each against the one composer at the commit of its moment',
              'three printers, no set named in any (%s)' % ('a set named' if old_named else 'none names its set'),
              'the composer at the lock, the entry and the closing equals each figure in turn: %s' % [(c['claim'], c['close'], c['repeat'], c['total']) == f for c, f in zip(cs, figs)],
              not old_named, all((c['claim'], c['close'], c['repeat'], c['total']) == f for c, f in zip(cs, figs)) and c01['only_second'] == ['event (1)'])
    return L, g, n


def control_slips():
    L, g, n = ['### (slips) (R352)(2)(iv): b741`S TWO POST-CLOSING SLIPS -- THE READ REFUSAL IN THE HOOK`S BANK; THE CHAINED GIT WRITE REFUSED, (R347)(2)(ii)/(R349)(2)(i) LANDING'], 0, 0
    hr = io.open(os.path.join(D, 'b742_hook_refusals.txt'), encoding='utf-8').read().replace('\r', '').split(NL)
    n += 1
    g += guard(L, 'slips', 'data/b742_hook_refusals.txt :1, the Read of data/b741_closing.txt after b741`s closing commit, refused READ',
               hr[0][:120], '| READ |' in hr[0] and 'b741_closing.txt' in hr[0] and hr[0].startswith('2026-11-05T07:24:51Z'))
    n += 1
    g += guard(L, 'slips', 'data/b742_hook_refusals.txt :2, b741`s closing commit sent in the message that carried its add, refused GITWRITE (one git write per message, the repair of (R347)(2)(ii) and (R349)(2)(i) at work); nothing committed by that call, the closing committed alone after it (13498fd2, 07:26:10Z)',
               hr[1][:120], '| GITWRITE |' in hr[1] and 'b741 closing:' in hr[1] and 'a second git write in one message' in hr[1])
    return L, g, n


def control_repeat():
    L, g, n = ['### (repeat) (R352)(2)(v), b741 EVENT (1): THE COMMIT TOOL`S REFUSAL OF THE PRE-RUN SENT UNDER THE LOCK HEADING, PRINTED AS REPEAT'], 0, 0
    msg = 'A LOCK ROW STANDS: the commit after the lock takes phase `seal`, and the seal record must exist first'
    old = base_module('tools/standing/commit.py', 'old_commit')
    o = 'repeat_of' in old.__dict__
    new = CM.repeat_of(msg, 'b741')
    n += 1
    g += case(L, 'repeat', 'b741`s event (1), the refusal "%s" at 05:08:38Z' % msg[:60],
              'commit.py at %s: the refusal printed with no class (repeat_of defined: %s)' % (BASE, o), 'the refusal`s class: %s' % new,
              not o, new == 'REPEAT of b740 event (4)')
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R352)(2)(vi): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = _git('show', '%s:tools/standing/VERSION' % BASE).strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.21.0', ver == 'v1.22.0')
    return L, g, n


CONTROLS = dict(dispatch=control_dispatch, remote=control_remote, counter=control_counter, slips=control_slips, repeat=control_repeat, version=control_version)
ORDER = ('dispatch', 'remote', 'counter', 'slips', 'repeat', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.22.0, (R352)(2)(i)-(vi): THE DISPATCH`S LICENCE, THE POST-PUSH CHAIN`S CAUSE AND THE RUN CACHE, THE COUNTER COMPOSED ONCE, THE TWO POST-CLOSING SLIPS, THE REFUSAL AS REPEAT, THE VERSION (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '## THE CONTROLS',
        '  the bank is its controls: the compile control first, then the dispatch`s licence at the head, then each repair`s instances through both routes; written through tools/standing/figbank.py ((R348)(2)(i))', '',
        '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
        '', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.22.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1220.txt' % act), NL.join(out))
        print('written data/%s_standing_v1220.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
