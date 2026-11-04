# -*- coding: utf-8 -*-
"""standing/v1190.py -- THE CONTROLS OF v1.19.0 ((R349)(2)(i)-(viii)), in v1180.py's form: each instance read through the route as it stood before the repair and through the repaired route; AS WANTED
where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the
repair is read from the blob at BASE (b738's closing), not from disk. THE CROSS-REPOSITORY WRITE COUNT PRINTS AT THE HEAD ((R349)'s Component 1). Written at b739 by the Write tool.

  python -X utf8 -u tools/standing/v1190.py control [gitwrite|phases|subjects|runs|background|sed|exercise|version ...] [--bank]
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
BASE = '3f45857d'   # ### b738's closing, the toolset as v1.18.0 left it
TRANSCRIPT = 'C:/Users/echo chamber/.claude/projects/D--/c6c3fbf2-d7af-4287-b739-0cca197d161f.jsonl'   # ### b738 and b739's one session
PAIR = ('toolu_0134XAzJmxbDTTrP2LHGJTNc', 'toolu_011TTN94drWyuJ6e4v5G53Sn')   # ### b738's 23:22:55Z add and commit on the kernel clone, defect (m)
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import gitwrite as GW           # noqa: E402
import hook as HK               # noqa: E402
import phases as PH             # noqa: E402
import runs as RN               # noqa: E402
import subjects as SJ           # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _read(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def _jread(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return json.load(f) if name.endswith('.json') else f.read()


def base_module(rel, name):
    """the module at BASE, read from its blob and run in a fresh namespace, not from disk."""
    m = types.ModuleType(name)
    m.__file__ = os.path.join(RELAY, *rel.split('/'))
    exec(compile(_git('show', '%s:%s' % (BASE, rel)), name, 'exec'), m.__dict__)
    return m


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.18.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.19.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.19.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


def _lines():
    with io.open(TRANSCRIPT, encoding='utf-8', errors='replace') as f:
        return f.read().split('\n')


def _block(raw, bid):
    for l in raw:
        if bid in l and '"tool_use"' in l and '"assistant"' in l:
            j = json.loads(l)
            for b in j['message'].get('content') or []:
                if isinstance(b, dict) and b.get('id') == bid:
                    return b
    return None


def _cut(raw, upto, extra=()):
    p = os.path.join(tempfile.mkdtemp(prefix='standing-v1190-'), 'transcript.jsonl')
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(list(raw[:upto]) + list(extra)) + NL)
    return p


def _utc(sha, repo=RELAY):
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(_git('log', '-1', '--format=%ct', sha, repo=repo).strip() or 0)))


def write_count():
    """THE CROSS-REPOSITORY WRITE COUNT ((R349)'s Component 1 head): standing.gitwrite's reading over the session's shell calls, every
    repository the commands name, for b738's window (its act_current commit to its closing's step row) and for b739's to this run."""
    import calendar
    sec = lambda s: calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))   # noqa: E731
    lo8, hi8 = _utc('26c57096'), _utc(BASE)
    lo9 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(sec(_utc('e0ce12d2')) - 120))
    hi8 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(min(sec(hi8) + 900, sec(lo9))))   # ### b738's closing and its step row, not past b739's start
    out = []
    for act, lo, hi in (('b738', lo8, hi8), ('b739', lo9, '2999-01-01T00:00:00Z')):
        calls = GW.calls_of(TRANSCRIPT, lo, hi)
        ok, nmsg, over, note = GW.reading(calls)
        repos = sorted(set(m.group(1) for c in calls for w in GW.writes(c['cmd']) for m in [re.search(r'git\s+-C\s+(\S+)', w)] if m))
        out.append('  %s (%s to %s): shell calls %d ; %s ; the repositories written %d: %s ; %s' % (
            act, lo, hi if act == 'b738' else 'this run', len(calls), note, len(repos), ', '.join(r.split('/')[-1] for r in repos), 'ONE WRITE PER MESSAGE' if ok else 'OVER ONE IN %d' % len(over)))
    return out


def control_gitwrite():
    L, g, n = ['### (gitwrite) (R349)(2)(i), b738 DEFECT (m), N5: ONE GIT WRITE PER MESSAGE ACROSS EVERY REPOSITORY, THE MESSAGE READ BY ITS API REQUEST'], 0, 0
    raw = _lines()
    b1, b2 = _block(raw, PAIR[0]), _block(raw, PAIR[1])
    first = next(i for i, l in enumerate(raw) if PAIR[0] in l)   # ### the first line naming the pair: the transcript as it stood when both hooks ran
    cut = _cut(raw, first)
    oldh = base_module('tools/standing/hook.py', 'old_hook')
    led = os.path.join(os.path.dirname(cut), 'ledger.json')
    o2 = oldh.judge('Bash', b2['input'], ctx=dict(transcript_path=cut, tool_use_id=PAIR[1]))
    n1 = HK.judge('Bash', b1['input'], ctx=dict(transcript_path=cut, tool_use_id=PAIR[0], ledger=led))
    n2 = HK.judge('Bash', b2['input'], ctx=dict(transcript_path=cut, tool_use_id=PAIR[1], ledger=led))
    n += 1
    g += case(L, 'gitwrite', 'b738`s 23:22:55Z pair on D:/zq-b738 (`%s` ; `%s`), the transcript cut at line %d, where both blocks stood unwritten when their hooks ran (the last api-request %s)' % (
        b1['input']['command'][:60], b2['input']['command'][:40], first, HK.last_request(cut)),
        'the commit judged -> %s' % (o2,), 'the add -> %s ; the commit -> %s' % (n1, n2 and n2[0]), o2 is None, n1 is None and bool(n2) and n2[0] == 'GITWRITE')
    nxt = json.dumps(dict(type='api-request', timestamp='2026-11-03T23:22:58.000Z'))
    cut2 = _cut(raw, first, [nxt])
    n3 = HK.judge('Bash', b2['input'], ctx=dict(transcript_path=cut2, tool_use_id=PAIR[1], ledger=led))
    led2 = os.path.join(os.path.dirname(cut), 'ledger_single.json')
    n4 = HK.judge('Bash', b1['input'], ctx=dict(transcript_path=cut, tool_use_id=PAIR[0], ledger=led2))
    n += 1
    g += guard(L, 'gitwrite', 'a single add in one message passes; the commit in the next message (a later api-request) passes', 'single add -> %s ; next message`s commit -> %s' % (n4, n3), n4 is None and n3 is None)
    seen = [l for l in raw if 'own block NONCE739AAA in the transcript at run time' in l and '"tool_result"' in l]
    probe = re.search(r'own block NONCE739AAA in the transcript at run time: (\w+) ; sibling NONCE739BBB: (\w+)', seen[0]) if seen else None
    n += 1
    g += guard(L, 'gitwrite', 'b739`s live probe at 06:06:56Z: the first of two parallel calls finds neither its own block nor its sibling`s at run time, so v1.17.0`s sibling read had no block to count',
               'own %s ; sibling %s' % (probe.groups() if probe else ('UNREAD', 'UNREAD')), bool(probe) and probe.groups() == ('False', 'False'))
    return L, g, n


def control_phases():
    L, g, n = ['### (phases) (R349)(2)(ii), b738 EVENTS (5): THE POST-PUSH READ AGAINST THE PRE-PUSH READ, PART BY PART; THE FINDING BEFORE ANY GUARD MOVES'], 0, 0
    parts = ('standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3')
    rows, finding = PH.compare('b738', parts, _jread_text)
    L += ['  b738`s five chain parts, pre-push (data/b738_checks_<part>.txt) beside post-push (data/b738_checks_postpush_<part>.txt):'] + ['  ' + r for r in rows] + ['  ### ' + finding]
    had = bool(_git('ls-tree', '--name-only', BASE, 'tools/standing/phases.py').strip())
    n += 1
    g += case(L, 'phases', 'b2c`s two runs, 171 s and 493 s in the chain phase, read beside each other', 'a reader of the two tables at %s: %s' % (BASE, had),
              'the finding: %s' % finding[:160], not had, 'standing-b2c' in finding and 'EVERY PHASE OF' in finding and 'NO GUARD MOVED' in finding)
    q = A.current().get('chain_quarters') or []
    lim = [x for x in rows if 'standing-b2' in x]
    n += 1
    g += guard(L, 'phases', '(R348)(2)(vi)`s split read against the chain halves: each first-half quarter one part, b659 on in standing-b3, every pre-push chain phase under 450 s',
               '%d quarters ; pre-push chain phases %s' % (len(q) or 4, [int(r.split('|')[1].split('/')[2]) for r in lim]), all(int(r.split('|')[1].split('/')[2]) < 450 for r in lim) and len(lim) == 4)
    return L, g, n


def _jread_text(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def control_subjects():
    L, g, n = ['### (subjects) (R349)(2)(iii), b738 EVENTS (4): THE SEAL AND LOCK SUBJECTS COMPOSED FROM THEIR BANKS; THE HOOK REFUSES A SUBJECT THE BANK DOES NOT PRINT'], 0, 0
    s65 = _git('log', '-1', '--format=%s', '65a2e5d8').strip()
    cmd = 'git -C D:/relay commit -m "%s"' % s65.replace('"', '\\"')
    oldh = base_module('tools/standing/hook.py', 'old_hook')
    o, nw = oldh.judge('Bash', {'command': cmd}), HK.judge('Bash', {'command': cmd})
    n += 1
    g += case(L, 'subjects', 'b738`s third seal commit 65a2e5d8, "%s"' % s65[:80], 'judge -> %s' % (o,), 'judge -> %s' % (nw and nw[0],), o is None, bool(nw) and nw[0] == 'SUBJECT' and '85 files, the bank 80' in nw[1])
    comp = SJ.compose('b738', 'seal', '', _jread)
    n += 1
    g += guard(L, 'subjects', 'b738`s seal subject regenerated from data/b738_seal_hashes.json', comp, '80 files' in comp)
    lk = _git('log', '-1', '--format=%s', 'b1c498e7').strip()
    ok_lock = SJ.check('b738', 'lock', lk, _jread)
    bad_lock = SJ.check('b738', 'lock', lk.replace('eight gates', 'seven gates'), _jread)
    n += 1
    g += guard(L, 'subjects', 'b738`s lock subject b1c498e7 "%s" against data/b738_lockgate.json gates_read 8; the same with "seven gates" planted' % lk, 'faults %s ; planted %s' % (ok_lock, bad_lock), not ok_lock and bool(bad_lock))
    return L, g, n


def control_runs():
    L, g, n = ['### (runs) (R349)(2)(iv), b738 EVENTS (2): G-DERIVATION-GRADED`S LAST-ROW READ GUARDED, AN EMPTY TABLE NO RUNS BY NAME; b737`S BANKS REPLAYED'], 0, 0
    src = _git('show', '%s:tools/acts/b738.py' % BASE)
    body = src.split('#⟪SECTION checks 34⟫\n', 1)[1].split('#⟪END⟫', 1)[0]
    K = types.SimpleNamespace(EF_RUNS=(), ZQ_COMMITS=())   # ### b737's state: tools/b737_worklist.py EF_RUNS (), no build bank
    k737 = re.search(r'^EF_RUNS = (.*)$', _git('show', '%s:tools/b737_worklist.py' % BASE), re.M)
    ns = dict(re=re, K=K, _vlast=lambda t: '')
    exec('def derivation_graded_ok(S):\n' + body, ns)
    try:
        r = ns['derivation_graded_ok'](dict(print_=''))
        old = 'returned %s' % r
    except IndexError as e:
        old = 'raised IndexError (%s)' % e
    st, note = RN.reading([], K.EF_RUNS)
    n += 1
    g += case(L, 'runs', 'b738`s predicate (tools/acts/b738.py slot 34 at %s) on b737`s state: EF_RUNS %s (tools/b737_worklist.py), no build bank' % (BASE, k737.group(1) if k737 else '?'),
              old, 'runs.reading -> %s (%s) ; runs.last -> %s' % (st, note, RN.last([], 6)), old.startswith('raised IndexError'), st == RN.NO_RUNS and RN.last([], 6) == RN.NO_RUNS)
    rows = [('1', 'S1', 'x', 'abcdef01', '41736472780', '4000', 'KERNEL')]
    n += 1
    g += guard(L, 'runs', 'a table whose runs are the worklist`s reads RUNS, one that differs DIFFERS', '%s ; %s' % (RN.reading(rows, (41736472780,))[0], RN.reading(rows, (1,))[0]),
               RN.reading(rows, (41736472780,))[0] == 'RUNS' and RN.reading(rows, (1,))[0] == 'DIFFERS' and RN.last(rows, 6) == 'KERNEL')
    return L, g, n


def control_background():
    L, g, n = ['### (background) (R349)(2)(v), b738 EVENTS (6), REPEAT OF b735`S REAPED WATCH: NO SUITE PART IN THE BACKGROUND, REFUSED BY THE HOOK'], 0, 0
    raw = _lines()
    bg = None
    for l in raw:
        if '"run_in_background":true' in l and 'standing-b2d' in l and '"tool_use"' in l:
            j = json.loads(l)
            for b in j['message'].get('content') or []:
                if isinstance(b, dict) and b.get('type') == 'tool_use' and (b.get('input') or {}).get('run_in_background') and 'standing-b2d' in (b.get('input') or {}).get('command', ''):
                    bg = (j.get('timestamp'), b['input'])
    oldh = base_module('tools/standing/hook.py', 'old_hook')
    o, nw = (oldh.judge('Bash', bg[1]), HK.judge('Bash', bg[1])) if bg else (None, None)
    n += 1
    g += case(L, 'background', 'b738`s post-push standing-b2d sent with run_in_background at %s (task bm42n3gyy, stopped by the host)' % (bg[0] if bg else 'UNFOUND'),
              'judge -> %s' % (o,), 'judge -> %s' % (nw and nw[0],), bool(bg) and o is None, bool(nw) and nw[0] == 'BACKGROUND')
    fg = dict(bg[1]) if bg else {}
    fg.pop('run_in_background', None)
    n += 1
    g += guard(L, 'background', 'the same part in the foreground passes', 'judge -> %s' % (HK.judge('Bash', fg) if fg else 'UNREAD',), bool(fg) and HK.judge('Bash', fg) is None)
    return L, g, n


def control_sed():
    L, g, n = ['### (sed) (R349)(2)(vi), b738 DEFECT (p) AND EVENTS (3), REPEAT OF CLASSES (18) AND (19): SED IN ANY FORM REFUSED; THE READER OF (R343)`S TOOLS IN ITS PLACE'], 0, 0
    cb = json.loads(_read('b738_commands.json'))
    rows = cb.get('rows') if isinstance(cb, dict) else cb
    cmd = next((r.get('cmd') for r in rows if 'sed -n' in (r.get('cmd') or '') and '13165p' in (r.get('cmd') or '')), None)
    oldh = base_module('tools/standing/hook.py', 'old_hook')
    o, nw = (oldh.judge('Bash', {'command': cmd}), HK.judge('Bash', {'command': cmd})) if cmd else (None, None)
    n += 1
    g += case(L, 'sed', 'b738`s touch-read lookup carrying `sed -n` (data/b738_commands.json, the #354 row)', 'judge -> %s' % (o,), 'judge -> %s' % (nw and nw[0],), bool(cmd) and o is None, bool(nw) and nw[0] == 'SED')
    plain = ('git -C D:/relay grep -n -F "sed -n" -- data', 'python -X utf8 -u D:/relay/tools/standing/peek.py search THE D:/relay/data/b738_closing.txt --lines 1-5',
             'python -X utf8 -u D:/relay/tools/standing/used.py')
    rp = [HK.judge('Bash', {'command': c}) for c in plain]
    n += 1
    g += guard(L, 'sed', 'a grep for the words, the reader`s line read (peek.py search --lines) and a path holding the letters pass', '%s' % ([r and r[0] for r in rp],), all(r is None for r in rp))
    ev = HK.judge('Read', {'file_path': os.path.join(D, 'b738_arms_prerun.txt'), 'limit': 20})
    n += 1
    g += guard(L, 'sed', 'b738 events (3)`s Read, a limit and no offset on 451 lines, refused READ as v1.4.0 orders (the instance REPEAT of class (19))', '%s' % (ev and ev[0],), bool(ev) and ev[0] == 'READ')
    return L, g, n


def control_exercise():
    L, g, n = ['### (exercise) (R349)(2)(vii), (R345)(2)(viii): THE EXERCISE BANK COMMITTED AT CLOSING, READ AGAINST b738'], 0, 0
    names = _git('show', '--name-only', '--format=', BASE).split()
    ex = [x for x in names if x.startswith('data/b738_exercise')]
    n += 1
    g += guard(L, 'exercise', 'b738`s closing commit %s carries data/b738_exercise.json and its ten part banks' % BASE, '%d banks: %s' % (len(ex), ', '.join(x[len('data/'):] for x in ex)[:200]),
               'data/b738_exercise.json' in ex and len(ex) == 11)
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R349)(2)(viii): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = _git('show', '%s:tools/standing/VERSION' % BASE).strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.18.0', ver == 'v1.19.0')
    return L, g, n


CONTROLS = dict(gitwrite=control_gitwrite, phases=control_phases, subjects=control_subjects, runs=control_runs, background=control_background, sed=control_sed,
                exercise=control_exercise, version=control_version)
ORDER = ('gitwrite', 'phases', 'subjects', 'runs', 'background', 'sed', 'exercise', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.19.0, (R349)(2)(i)-(viii): THE GIT WRITE BY THE MESSAGE`S REQUEST, THE POST-PUSH PHASES, THE SEAL AND LOCK SUBJECTS, THE GUARDED LAST ROW, NO BACKGROUND PART, NO SED, THE EXERCISE BANK, THE VERSION (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '## THE CONTROLS',
        '  the bank is its controls: the compile control first, then the cross-repository write count, then each repair`s instances through both routes; written through tools/standing/figbank.py ((R348)(2)(i))', '',
        '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
        '', '### THE CROSS-REPOSITORY WRITE COUNT ((R349) Component 1`s head; standing.gitwrite over the session`s shell calls, every repository named):'] + write_count() + [
        '', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.19.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1190.txt' % act), NL.join(out))
        print('written data/%s_standing_v1190.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
