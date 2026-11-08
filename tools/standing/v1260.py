# -*- coding: utf-8 -*-
"""standing/v1260.py -- THE CONTROLS OF v1.26.0 ((R356)(3)(i)-(viii)), in v1250.py's form: each instance read through the route as it stood before the
repair and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side.
THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the repair is read from the blob at BASE (b745's
closing), not from disk. The free memory is read and printed before each control. Each class may be run alone, one per call, in the foreground;
`--bank` writes the whole set, every class run in the one call. Written at b746 by the Write tool.

  python -X utf8 -u tools/standing/v1260.py control [lock|lockdate|rows|membrane|lsr|readme|repeat|version ...] [--bank]
"""
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
BASE = '946cc80a'   # ### b745's closing, the toolset as v1.25.0 left it
HOLD = 2560
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import act_membrane as MEM      # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import hook as HK               # noqa: E402
import lockdate as LD           # noqa: E402
import lsrread as LSRD          # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def base_src(rel):
    return _git('show', '%s:%s' % (BASE, rel))


def base_mod(rel, name):
    ns = {'__name__': name, '__file__': os.path.join(RELAY, rel)}
    exec(compile(base_src(rel), '%s@%s' % (name, BASE), 'exec'), ns)
    return ns


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.25.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.26.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.26.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _json_at(ref, rel):
    t = _git('show', '%s:%s' % (ref, rel))
    return json.loads(t) if t.strip() else {}


def control_lock():
    L, g, n = ['### (lock) (R356)(3)(i), b745 events (1), N4: THE LOCK BLOCK WRITTEN AFTER THE LOCK -- reg_seal.py --lock inside the lock tool'], 0, 0
    old_has = 'lock_check' in base_src('tools/standing/commit.py')
    rec5 = _json_at('af0330bb', 'data/b745_lockgate.json')
    face5 = _git('show', 'af0330bb:data/%s' % rec5.get('face'))
    try:
        CM.lock_check(face5, rec5)
        new5 = 'ACCEPTED'
    except CM.Refused as e:
        new5 = 'REFUSED (%s)' % str(e)[:150]
    n += 1
    g += case(L, 'lock', 'b745`s sequence replayed: the face %s as it stood in the lock commit af0330bb (no lock block; reg_seal --lock ran after, its block first committed in 2959bc55)' % rec5.get('face'),
              'commit.py at %s reads no face (lock_check %s): the lock commit made without the block' % (BASE, 'PRESENT' if old_has else 'ABSENT'),
              'lock_check: %s' % new5, not old_has, new5.startswith('REFUSED'))
    rec4 = _json_at('ae688949', 'data/b744_lockgate.json')
    face4 = _git('show', 'ae688949:data/%s' % rec4.get('face'))
    try:
        c4 = CM.lock_check(face4, rec4)
        new4 = 'ACCEPTED (%s)' % ' ; '.join(c.strip() for c in c4)
    except CM.Refused as e:
        new4 = 'REFUSED (%s)' % str(e)[:150]
    n += 1
    g += guard(L, 'lock', 'b744`s sequence replayed: the face %s in its lock commit ae688949, the block in the commit' % rec4.get('face'), 'lock_check: %s' % new4, new4.startswith('ACCEPTED'))
    src = open(os.path.join(S, 'commit.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'lock', 'the lock phase of run() calls lock_face (reg_seal --lock, the add, the staged blob through lock_check) before the commit',
               'lock_runner in preflight %s ; lock_face in run %s' % ('lock_runner()' in src, 'lock_face(repo, act, read, data)' in src),
               'lock_runner()' in src and 'lock_face(repo, act, read, data)' in src)
    return L, g, n


def _old_n4_lock(act, face_rel, pre, end):
    """the route before the repair, as b745's act module read N4's lock: the face's `locked at (UTC)` line, then the first relay commit at or after
    that time carrying the face."""
    face = _git('show', '%s:%s' % (end, face_rel))
    m = re.search(r'locked at \(UTC\) : (\S+)', face)
    if not m:
        return None, None
    import calendar
    lock = calendar.timegm(time.strptime(m.group(1), '%Y-%m-%dT%H:%M:%SZ'))
    rows = [l.split(' ', 1) for l in _git('log', '--reverse', '--format=%H %ct', '%s..%s' % (pre, end)).split(NL) if l.strip()]
    return m.group(1), next((h for h, ct in rows if int(ct) >= lock and face_rel in _git('show', '--name-only', '--format=', h).split()), None)


def control_lockdate():
    L, g, n = ['### (lockdate) (R356)(3)(ii): THE TWO READERS OF ONE DATE -- one reader, the lock row`s commit in data/<act>_steps.json'], 0, 0
    iso, old_n4 = _old_n4_lock('b745', 'data/b745_registration_2026-11-07.txt', '7d448774', BASE)
    old_ceiling = 'af0330bb'   # ### b745's ceiling: the lock given by hand in the seat's scratch (relay data/b745_events.txt, the ceiling at the root prompt)
    rows = (_json_at(BASE, 'data/b745_steps.json').get('rows') or [])
    new = LD.lock_commit(rows)
    n += 1
    g += case(L, 'lockdate', 'b745`s two readings replayed: N4 by the face`s block (locked at %s) and the ceiling by hand' % iso,
              'N4 %s ; the ceiling %s' % ((old_n4 or 'NONE')[:8], old_ceiling), 'N4 and the ceiling both by lockdate.lock_commit: %s' % (new or 'NONE')[:8],
              (old_n4 or '')[:8] != old_ceiling, bool(new) and new.startswith('af0330bb'))
    act_src = open(os.path.join(T, 'acts', 'b746.py'), encoding='utf-8').read()
    rp_src = open(os.path.join(S, 'rootprompt.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'lockdate', 'both readers call the one: the act module`s _post_lock_edits and rootprompt.ceiling_at_lock',
               'LD.lock_of in the act module %s ; in rootprompt %s ; the face`s `locked at` read by N4 %s' % (
                   'LD.lock_of(ACT' in act_src, 'LD.lock_of(act' in rp_src, "m = re.search(r'locked at" in act_src),
               'LD.lock_of(ACT' in act_src and 'LD.lock_of(act' in rp_src and "m = re.search(r'locked at" not in act_src)
    two = [dict(phase='lock', commit='a' * 40, repo='relay'), dict(phase='lock', commit='b' * 40, repo='relay')]
    try:
        LD.lock_commit(two)
        r2 = 'READ'
    except ValueError as e:
        r2 = 'REFUSED (%s)' % e
    n += 1
    g += guard(L, 'lockdate', 'two lock rows in one step bank', r2, r2.startswith('REFUSED'))
    return L, g, n


def control_rows():
    L, g, n = ['### (rows) (R356)(3)(iii), b745 events (2), REPEAT b744 (4): THE ROW IN THE COMMIT`S CALL FOR EVERY ACT COMMIT'], 0, 0
    old = base_mod('tools/standing/commit.py', 'commit_base')
    rd = CM.reader(D)
    for h in ('eaca4c35', 'e9c339ed'):
        subj = _git('log', '-1', '--format=%s', h).strip()
        head = 'b745 step zero: '
        words = subj[len(head):] if subj.startswith(head) else subj
        try:
            old['preflight']('b745', 'step zero', words, RELAY, [], rd)
            o = 'ACCEPTED'
        except Exception as e:  # noqa: BLE001
            o = 'REFUSED (%s)' % str(e)[:110]
        got = []
        try:
            s2 = CM.act_check('b745', 'step zero', words)
            rc, row = (lambda k, p, f: (got.append((k, p, f)) or 0, 'row %s %s %s' % (k, p, f[:8])))('relay', 'step zero', _git('rev-parse', h).strip())
            nw = '"%s" ; %s (exit %d) in the same call' % (s2[:70], row, rc)
            ok = s2 == subj and got and rc == 0
        except CM.Refused as e:
            nw, ok = 'REFUSED (%s)' % e, False
        n += 1
        g += case(L, 'rows', 'relay %s replayed through the commit tool ("%s")' % (h, subj[:80]),
                  'commit.py at %s: %s -- the commit made by hand, its row written after the lock' % (BASE, o), nw, o.startswith('REFUSED'), ok)
    try:
        CM.act_check('b746', 'component 1', '')
        e1 = 'ACCEPTED'
    except CM.Refused as e:
        e1 = 'REFUSED (%s)' % str(e)[:80]
    n += 1
    g += guard(L, 'rows', 'an act commit with no words', e1, e1.startswith('REFUSED'))
    return L, g, n


def control_membrane():
    L, g, n = ['### (membrane) (R356)(3)(iv), b745 events (5)-(6): THE MEMBRANE`S "NOTHING WRITTEN" THAT WROTE ONE FILE'], 0, 0
    tmp = tempfile.mkdtemp(prefix='v1260_mem_')
    try:
        os.makedirs(os.path.join(tmp, 'data'))
        subprocess.run(['git', '-C', tmp, 'init', '-q'], capture_output=True)
        roots = os.path.join(tmp, 'data', 'act_roots.txt')
        io.open(roots, 'w', encoding='utf-8', newline='\n').write('b745 c831a2103261ed73 3c30761b\n')
        subprocess.run(['git', '-C', tmp, 'add', 'data/act_roots.txt'], capture_output=True)
        stray = os.path.join(tmp, 'data', 'b745_chain_half_nsm1_--quiet.json')
        io.open(stray, 'w', encoding='utf-8', newline='\n').write('{}\n')
        old = base_mod('tools/act_membrane.py', 'membrane_base')
        o = old['refuses']('b745', '--quiet', None, roots)
        new, done = MEM.line('b745', '--quiet', None, roots, root=tmp, since=0)
        n += 1
        g += case(L, 'membrane', 'b745`s stray replayed: data/b745_chain_half_nsm1_--quiet.json planted untracked in a test tree, the bank name `--quiet` refused',
                  '"%s" with the stray standing -- %s' % (o[-60:], 'NOTHING WRITTEN asserted' if 'NOTHING WRITTEN' in o else 'no assertion'),
                  '"%s" ; the stray now %s' % (new[-170:], 'GONE' if not os.path.exists(stray) else 'STANDING'),
                  'NOTHING WRITTEN' in o,
                  'b745_chain_half_nsm1_--quiet.json' in new and 'DELETED' in new and not os.path.exists(stray))
        new2, _d = MEM.line('b745', '--quiet', None, roots, root=tmp, since=0)
        n += 1
        g += guard(L, 'membrane', 'the same refusal with no stray', '"%s"' % new2[-80:], 'NOTHING WRITTEN' in new2 and 'no stray' in new2)
        old_file = os.path.join(tmp, 'data', 'b745_chain_half_nsm1_--quiet_old.json')
        io.open(old_file, 'w', encoding='utf-8', newline='\n').write('{}\n')
        os.utime(old_file, (time.time() - 3600, time.time() - 3600))
        new3, _d = MEM.line('b745', '--quiet', None, roots, root=tmp, since=time.time() - 60)
        n += 1
        g += guard(L, 'membrane', 'an untracked file carrying the name but written before the route began (an hour old)', 'the file %s' % (
            'STANDING, not taken for a stray' if os.path.exists(old_file) else 'DELETED'), os.path.exists(old_file))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return L, g, n


def control_lsr():
    L, g, n = ['### (lsr) (R356)(3)(v), b745 events (8): THE REMOTE READ RETRIED AND THE CACHED PASS'], 0, 0
    a1 = json.load(open(os.path.join(D, 'b745_lsr_postpush_standing-a2_attempt1.json'), encoding='utf-8'))
    a2 = json.load(open(os.path.join(D, 'b745_lsr_postpush_standing-a2.json'), encoding='utf-8'))
    old1 = bool(a1['lsr']) and all(v <= 1 for v in a1['lsr'].values())
    v1 = LSRD.verdict(a1['lsr'], a1['times'])
    n += 1
    g += case(L, 'lsr', 'relay data/b745_lsr_postpush_standing-a2_attempt1.json (the run of record): SIDE-simplicity 2 calls in one read',
              'lsr_ok: %s -- G-LSREMOTE-ONE-PER-REPO failed on a retry' % old1, 'verdict %s ; %s' % (v1[0], ' ; '.join(v1[1])),
              not old1, v1[0] == 'PASS' and any(e.startswith('RETRIED D:/SIDE-simplicity') for e in v1[1]))
    t2 = a2['times']
    old2 = all(v_.get('reads', 0) <= 1 for v_ in t2.values())   # ### the arm at BASE where no call was made: every read from the cache counts as a pass
    v2 = LSRD.verdict(a2['lsr'], t2)
    n += 1
    g += case(L, 'lsr', 'relay data/b745_lsr_postpush_standing-a2.json (the re-run): %d repositories, every one from the run cache' % len(t2),
              'the arm read %s -- a PASS on no read' % ('PASS' if old2 else 'FAIL'), 'verdict %s ; %s' % (v2[0], ' ; '.join(v2[1])), old2, v2[0] == 'CACHED')
    v3 = LSRD.verdict({'D:/X': 3}, {'D:/X': dict(reads=1, secs=1.0, cached=False)})
    n += 1
    g += guard(L, 'lsr', 'three calls on one repository (the arm`s plant)', 'verdict %s ; %s' % v3, v3[0] == 'FAIL')
    v4 = LSRD.verdict({'D:/X': 2}, {'D:/X': dict(reads=1, secs=9.0, cached=False, attempts=[6.5, 2.5])})
    n += 1
    g += guard(L, 'lsr', 'a retry with its two timings recorded (b616_claims.ATTEMPTS through remotecache.wrap)', 'verdict %s ; %s' % v4,
               v4[0] == 'PASS' and '6.50 s and 2.50 s' in ' '.join(v4[1]))
    tpl = open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'lsr', 'the suite`s arm and table read lsrread (the predicate, the CACHED verdict counted vacuous, the bank`s class)',
               'LSRD.ok %s ; cached -> vac %s ; classed in the bank %s' % ('LSRD.ok(' in tpl, 'vac = vac or cached' in tpl, 'classed=lsv[0]' in tpl),
               'LSRD.ok(' in tpl and 'vac = vac or cached' in tpl and 'classed=lsv[0]' in tpl)
    return L, g, n


def control_readme():
    L, g, n = ['### (readme) (R356)(3)(vi): G-README-CURRENCY`S REASON PRINTED FROM ITS BANK; THE README LINE CARRIED TO A SITTING ON THE AUTHOR`S NUMBER'], 0, 0
    fl = io.open(os.path.join(D, 'b745_standing_figures.txt'), encoding='utf-8').read().split(NL)
    l58 = fl[57] if len(fl) > 57 else ''
    rm = _git('show', 'HEAD:README.md', repo=PP).split(NL)
    l164 = rm[163] if len(rm) > 163 else ''
    L += ['  relay data/b745_standing_figures.txt :58: %s' % l58.strip(), '  PLACE-papers README.md :164 at HEAD: %s' % l164.strip()[:200]]
    n += 1
    g += guard(L, 'readme', 'the reason: README 1 against b744`s 0 at :58; the line it names cites v0.37 where the tag is v0.38; brought current by no hand of this act',
               'README 1 at :58 %s ; v0.37 on :164 %s' % ('README 1' in l58, 'v0.37' in l164), 'README 1' in l58 and 'v0.37' in l164)
    return L, g, n


def control_repeat():
    L, g, n = ['### (repeat) (R356)(3)(vii): THE HOOK`S REFUSALS, REPEAT, THE INSTANCES PRINTED'], 0, 0
    rows = [l for l in io.open(os.path.join(D, 'b746_hook_refusals.txt'), encoding='utf-8').read().split(NL) if l.strip()]
    kinds = {}
    for r in rows:
        k = r.split(' | ')[1] if ' | ' in r else '?'
        kinds[k] = kinds.get(k, 0) + 1
    L += ['  relay data/b746_hook_refusals.txt: %d refusal(s) by the hook at b746 so far: %s' % (len(rows), ', '.join('%s %d' % kv for kv in sorted(kinds.items())))]
    for cmd, want in (('git log | head -3', 'PIPE'), ("python - <<'EOF'\nprint(1)\nEOF", 'REDIR')):
        j = HK.judge('Bash', {'command': cmd}, RELAY)
        n += 1
        g += guard(L, 'repeat', 'a Bash command of the refused kind %s (an instance this act repeated)' % want, 'judged %s' % (j[0] if j else 'ALLOWED'), bool(j) and j[0] == want)
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R356)(3)(viii): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = base_src('tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.25.0', ver == 'v1.26.0')
    return L, g, n


CONTROLS = {'lock': control_lock, 'lockdate': control_lockdate, 'rows': control_rows, 'membrane': control_membrane, 'lsr': control_lsr,
            'readme': control_readme, 'repeat': control_repeat, 'version': control_version}
ORDER = ('lock', 'lockdate', 'rows', 'membrane', 'lsr', 'readme', 'repeat', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.26.0, (R356)(3)(i)-(viii): THE LOCK BLOCK IN THE LOCK COMMIT, THE ONE READER OF THE LOCK DATE, THE ROW '
           'FOR EVERY ACT COMMIT, THE MEMBRANE`S LINE FROM THE WORKING TREE, THE RETRIED AND THE CACHED REMOTE READ, G-README-CURRENCY`S REASON, THE REPEAT '
           'REFUSALS, THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    for k in names:
        out.append(free_line())
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.26.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1260.txt' % act), NL.join(out))
        print('written data/%s_standing_v1260.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
