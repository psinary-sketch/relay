# -*- coding: utf-8 -*-
"""standing/v1210.py -- THE CONTROLS OF v1.21.0 ((R351)(2)(i)-(vii)), in v1200.py's form: each instance read through the route as it stood before the repair and through the repaired route; AS WANTED
where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the
repair is read from the blob at BASE (b740's closing), not from disk. THE ONE-CALL COMMIT TOOL PRINTS AT THE HEAD ((R351)'s Component 1): b740's commit events replayed under it in a scratch repository
outside data/ and tools/ (git run by argument list, the old route's PowerShell double-quoted string run by PowerShell itself). Written at b741 by the Write tool.

  python -X utf8 -u tools/standing/v1210.py control [commit|hashed|writes|postseal|touch|next|version ...] [--bank]
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
import types

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
BASE = 'fe2150b3'   # ### b740's closing, the toolset as v1.20.0 left it
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import gitwrite as GW           # noqa: E402
import hook as HK               # noqa: E402
import nextact as NXA           # noqa: E402
import postseal as PSL          # noqa: E402
import subjects as SJ           # noqa: E402


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
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.20.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.21.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.21.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


def _scratch_repo():
    """a scratch git repository outside data/ and tools/, one commit, a file staged; its data directory holding b740's lock gate bank alone."""
    root = tempfile.mkdtemp(prefix='standing-v1210-')
    repo = os.path.join(root, 'repo')
    data = os.path.join(root, 'data')
    os.makedirs(repo)
    os.makedirs(data)
    for a in (('init', '-q'), ('config', 'user.name', 'control'), ('config', 'user.email', 'control@localhost'), ('config', 'core.autocrlf', 'false')):
        _git(*a, repo=repo)
    shutil.copy(os.path.join(D, 'b740_lockgate.json'), os.path.join(data, 'b740_lockgate.json'))
    _stage(repo, 'f0')
    _git('commit', '-q', '-m', 'control: the first commit', repo=repo)
    return root, repo, data


def _stage(repo, name):
    with open(os.path.join(repo, name + '.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('%s %s\n' % (name, time.time()))
    _git('add', '--', name + '.txt', repo=repo)


def _rows_writer(data, act):
    """the step row written into the scratch data directory's step bank, the record tool's row shape and the time it was written."""
    def w(key, phase, full):
        p = os.path.join(data, '%s_steps.json' % act)
        j = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else dict(rows=[])
        ct = int(_git('log', '-1', '--format=%ct', full, repo=key).strip())
        j['rows'].append(dict(repo='relay', commit=full, ct=ct, phase=phase, rowed=time.time(), subject=_git('log', '-1', '--format=%s', full, repo=key).strip()[:120]))
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(j, f)
        return 0, 'row %d %s' % (len(j['rows']), phase)
    return w


def control_commit():
    L, g, n = ['### (commit) (R351)(2)(i), b740 EVENTS (1), (2), (4): THE ONE-CALL COMMIT TOOL -- THE SUBJECT COMPOSED FROM THE BANK, THE COMMIT, THE ROW, IN THAT ORDER, NO SHELL BETWEEN'], 0, 0
    read9 = CM.reader(D)
    subj = SJ.compose('b740', 'lock', '', read9)
    root, repo, data = _scratch_repo()
    L.append('  ### the scratch repository %s (outside data/ and tools/); the composed subject of b740`s lock, from data/b740_lockgate.json: "%s"' % (repo, subj))
    # ### event (1): the old route, git commit -m in a PowerShell double-quoted string, run by PowerShell
    _stage(repo, 'f1')
    subprocess.run(['powershell', '-NoProfile', '-Command', 'git -C "%s" commit -q -m "%s"' % (repo, subj)], capture_output=True, text=True)
    old_back = _git('log', '-1', '--format=%s', repo=repo).strip()
    _stage(repo, 'f2')
    full, new_back = CM.commit(repo, subj)
    n += 1
    g += case(L, 'commit', 'event (1): b740`s lock subject carrying a backtick (relay 15b587de landed "%s")' % _git('log', '-1', '--format=%s', '15b587de').strip(),
              'a PowerShell double-quoted git commit -m, read back "%s"' % old_back, 'tools/standing/commit.py by argument list, read back "%s"' % new_back,
              old_back != subj, new_back == subj)
    # ### event (2): the gate, gate, lock sequence under the tool; the old step bank's order read from relay data/b740_steps.json
    r9 = json.load(open(os.path.join(D, 'b740_steps.json'), encoding='utf-8'))['rows']
    li = next(i for i, r in enumerate(r9) if r['phase'] == 'lock')
    late = [c[:8] for i, r in enumerate(r9) if i > li and r['phase'] == 'gate' for c in (r.get('commits') or [r['commit']])]
    root2, repo2, data2 = _scratch_repo()
    w = _rows_writer(data2, 'b740')
    done = []
    for ph, words in (('gate', 'the first gate commit'), ('gate', 'the second gate commit'), ('lock', '')):
        _stage(repo2, ph + str(len(done)))
        done.append(CM.run(repo2, ph, words, act='b740', data=data2, row_writer=w))
    rows = json.load(open(os.path.join(data2, 'b740_steps.json'), encoding='utf-8'))['rows']
    order_ok = [r['phase'] for r in rows] == ['gate', 'gate', 'lock'] and all(rows[k]['rowed'] <= rows[2]['rowed'] for k in (0, 1))
    n += 1
    g += case(L, 'commit', 'event (2): the lock and two gate commits rowed after the lock (relay data/b740_steps.json row %d the lock, a gate row after it for %s)' % (li + 1, ', '.join(late)),
              'the step bank`s rows: gate rows after the lock row %s' % (late or 'none'),
              'three calls, gate, gate, lock: rows %s, each written in its call, the gates` before the lock`s %s' % ([r['phase'] for r in rows], order_ok),
              bool(late), order_ok and all(d['equal'] for d in done))
    # ### event (4): the seal subject before the seal record; and the pre-seal commit headed `lock` that the step bank rowed `seal`
    _stage(repo2, 'seal')
    head0 = _git('rev-parse', 'HEAD', repo=repo2).strip()
    try:
        CM.run(repo2, 'seal', 'the pre-run', act='b740', data=data2, row_writer=w)
        sealed_refused = None
    except CM.Refused as e:
        sealed_refused = str(e)
    head1 = _git('rev-parse', 'HEAD', repo=repo2).strip()
    n += 1
    g += guard(L, 'commit', 'event (4): a seal commit before data/b740_seal_hashes.json exists (the hook refused the shell`s at 20:23Z; the tool refuses before git runs)',
               'refused "%s" ; HEAD unmoved %s' % ((sealed_refused or 'NOT REFUSED')[:70], head0 == head1), bool(sealed_refused) and head0 == head1)
    r12 = [r for r in r9 if r['commit'].startswith('3f13ca05')]
    head_word = r12[0]['subject'].split(':')[0].split()[-1] if r12 else None
    try:
        CM.run(repo2, 'lock', 'the pre-run', act='b740', data=data2, row_writer=w)
        lock2 = None
    except CM.Refused as e:
        lock2 = str(e)
    head2 = _git('rev-parse', 'HEAD', repo=repo2).strip()
    n += 1
    g += case(L, 'commit', 'event (4): the commit after the lock and before the seal (relay 3f13ca05): its subject`s head and its row`s phase',
              'subject head `%s`, row phase `%s`' % (head_word, r12[0]['phase'] if r12 else None),
              'a second `lock` refused before the commit: "%s" ; HEAD unmoved %s' % ((lock2 or 'NOT REFUSED')[:60], head1 == head2),
              bool(r12) and head_word != r12[0]['phase'], bool(lock2) and head1 == head2)
    # ### the shell route closed: the hook refuses a gate, lock or seal commit typed into a shell
    j = HK.judge('PowerShell', {'command': 'git -C D:/relay commit -m "%s"' % subj})
    jg = HK.judge('PowerShell', {'command': 'git -C D:/relay commit -m "b741 gate: a gate commit"'})
    oldhk = base_module('tools/standing/hook.py', 'old_hook')
    ojg = oldhk.judge('PowerShell', {'command': 'git -C D:/relay commit -m "b741 gate: a gate commit"'})
    n += 1
    g += case(L, 'commit', 'the shell route: b740`s lock subject and a gate subject typed into git commit -m',
              'the hook at %s on the gate subject: %s' % (BASE, ojg and ojg[0] or 'ALLOWED'), 'the hook: lock %s ; gate %s' % (j and j[0], jg and jg[0]),
              not ojg, bool(j) and j[0] == 'SUBJECT' and bool(jg) and jg[0] == 'SUBJECT')
    L.append('  ### the scratch repositories stay in place: %s, %s' % (root, root2))
    return L, g, n


def control_hashed():
    L, g, n = ['### (hashed) (R351)(2)(ii), b740 (m), N4: THE HAND EDIT OF A JSON BANK -- AN EDIT OR WRITE OF A BANK ITS TOOL WROTE, REFUSED BY THE HOOK'], 0, 0
    p = os.path.join(D, 'b740_corrigendum.json')
    oldhk = base_module('tools/standing/hook.py', 'old_hook')
    olock = oldhk.locked_bank(p, RELAY, 'b740')
    t_lock = int(_git('log', '--diff-filter=A', '--format=%ct', '--', 'data/b740_lockgate.json').split()[-1])
    t_corr = int(_git('log', '--diff-filter=A', '--format=%ct', '--', 'data/b740_corrigendum.json').split()[-1])
    nb = HK.hashed_bank(p, RELAY, 'b740')
    n += 1
    g += case(L, 'hashed', 'b740 (m): an Edit of data/b740_corrigendum.json (named in data/b740_bank_hashes.json) at Component 1, before the lock',
              'the hook at %s: LOCKED wants the lock, the bank committed %s and the lock gate %s, the lock not come (locked_bank %s) -> ALLOWED' % (
                  BASE, time.strftime('%H:%M:%SZ', time.gmtime(t_corr)), time.strftime('%H:%M:%SZ', time.gmtime(t_lock)), olock),
              'hashed_bank -> %s -> HASHED' % nb, t_corr < t_lock, nb == 'b740_corrigendum.json')
    ev, st, fr = (HK.hashed_bank(os.path.join(D, x), RELAY, 'b740') for x in ('b740_events.txt', 'b740_steps.json', 'b740_stepzero.txt'))
    n += 1
    g += guard(L, 'hashed', 'the exclusion read (lock_exempt, (R343)(2)(vi)): the events bank, the step bank and a hand-written bank pass', 'events %s ; steps %s ; stepzero %s' % (ev, st, fr),
               ev is None and st is None and fr is None)
    return L, g, n


def control_writes():
    L, g, n = ['### (writes) (R351)(2)(iii), b740 (b), N5, REPEAT b738 (m), b736 (b): THE GIT-WRITE COUNT READS A CHAINED COMMAND AS ITS WRITES'], 0, 0
    rf = io.open(os.path.join(D, 'b740_hook_refusals.txt'), encoding='utf-8').read().split(NL)
    cmd = json.loads(rf[1].split(' | ')[3])
    n += 1
    g += guard(L, 'writes', 'b740 (b), data/b740_hook_refusals.txt :2, the chained add and commit: its writes, and the hook`s verdict',
               'writes %d ; the hook %s' % (len(GW.writes(cmd)), (HK.judge('Bash', {'command': cmd}) or ('ALLOWED',))[0]), len(GW.writes(cmd)) == 2 and (HK.judge('Bash', {'command': cmd}) or ('',))[0] == 'GITWRITE')
    oldgw = base_module('tools/standing/gitwrite.py', 'old_gitwrite')
    c1 = 'python -X utf8 -u D:/relay/tools/standing/commit.py relay lock'
    c2 = 'git -C D:/relay add data/x.txt && ' + c1
    n += 1
    g += case(L, 'writes', 'the one-call commit tool`s run, alone and chained after an add',
              'gitwrite at %s: %d and %d' % (BASE, len(oldgw.writes(c1)), len(oldgw.writes(c2))), 'gitwrite: %d and %d, the hook on the chained %s' % (
                  len(GW.writes(c1)), len(GW.writes(c2)), (HK.judge('PowerShell', {'command': c2}) or ('ALLOWED',))[0]),
              len(oldgw.writes(c1)) == 0, len(GW.writes(c1)) == 1 and len(GW.writes(c2)) == 2 and (HK.judge('PowerShell', {'command': c2}) or ('',))[0] == 'GITWRITE')
    return L, g, n


def control_postseal():
    L, g, n = ['### (postseal) (R351)(2)(iv), b740 EVENTS (5), REPEAT b736 (8): THE EXCLUDE LIST BEFORE ANY READ AFTER THE SEAL; THE ARM`S FAILURE PRINTED AS SUCH'], 0, 0
    tpl0 = _git('show', '%s:tools/standing/fold/checks.tpl' % BASE)
    tpl1 = io.open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    note = PSL.note('b740')
    n += 1
    g += case(L, 'postseal', 'b740`s failing reading of G-RULE-POSTSEAL-READ (data/b740_checks.txt :16 lists it failing), read with its ordinal',
              'checks.tpl at %s: the arm`s predicate unwrapped (%s), its failure printed without an ordinal' % (BASE, 'PSL.wrap' not in tpl0),
              'checks.tpl wraps it (%s); b740`s reading: "%s"' % ('PSL.wrap(pred' in tpl1, note.strip(' ;')), 'PSL.wrap' not in tpl0,
              'PSL.wrap(pred' in tpl1 and 'b736' in note and 'b740' not in note)
    out = CM.excludes()
    n += 1
    g += guard(L, 'postseal', 'the exclude list the commit tool prints after a seal commit (hook.py excludes, read from tools/rule_arms.py)', out[:150],
               'THE POST-SEAL READ RULE' in out and 'OPEN_TRAILS' in out)
    pr = PSL.failed_before('b741')
    n += 1
    g += guard(L, 'postseal', 'the ordinal from the suite banks, not typed: the acts listing the arm LIVE FAILING before b741 (the ruling`s "third" counts the REPEAT rows b736 (8) and b740 (5))',
               '%d acts: %s' % (len(pr), ', '.join(pr)), 'b736' in pr and 'b740' in pr)
    return L, g, n


def control_touch():
    L, g, n = ['### (touch) (R351)(2)(v): THE TOUCH READ`S TWO DIFFERS ROWS NAMED WITH THEIR CAUSE'], 0, 0
    t = io.open(os.path.join(D, 'b740_touch.txt'), encoding='utf-8').read().replace('\r', '').split(NL)
    rows = [l for l in t if re.match(r'^  \((19|26)\) ', l)]
    named = [(l[2:6].strip(), 'DIFFERS' in l, re.search(r"defect \((?:a|b)'\)", l).group(0) if re.search(r"defect \((?:a|b)'\)", l) else None) for l in rows]
    n += 1
    g += guard(L, 'touch', 'data/b740_touch.txt :38 "DIFFERS 2", rows (19) and (26) read with the defect each names as its cause', ' ; '.join('%s DIFFERS %s cause %s' % x for x in named),
               len(named) == 2 and all(x[1] and x[2] for x in named) and 'DIFFERS 2' in t[37])
    return L, g, n


def control_next():
    L, g, n = ['### (next) (R351)(2)(vi): THE CLOSING`S CARRIED ITEM FROM THE AUTHOR`S ANSWERS BANK'], 0, 0
    cl = io.open(os.path.join(D, 'b740_closing.txt'), encoding='utf-8').read().replace('\r', '').split(NL)
    i = cl.index('### CARRIED FORWARD.')
    items = cl[i + 1:]
    items = items[:next((k for k, l in enumerate(items) if l.startswith('=')), len(items))]
    old_a = next(l for l in items if l.startswith('    (a) '))
    new_a = next(l for l in NXA.carried('b740', items) if l.startswith('    (a) '))
    n += 1
    g += case(L, 'next', 'b740`s closing regenerated: item (a) against data/b740_author_answers.txt :17',
              'data/b740_closing.txt :%d "%s..."' % (i + 2, old_a.strip()[:70]), '"%s..."' % new_a.strip()[:140],
              '(c7)' not in old_a, '(c7)' in new_a and 'to SP3' in new_a)
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R351)(2)(vii): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = _git('show', '%s:tools/standing/VERSION' % BASE).strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.20.0', ver == 'v1.21.0')
    return L, g, n


CONTROLS = dict(commit=control_commit, hashed=control_hashed, writes=control_writes, postseal=control_postseal, touch=control_touch, next=control_next, version=control_version)
ORDER = ('commit', 'hashed', 'writes', 'postseal', 'touch', 'next', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.21.0, (R351)(2)(i)-(vii): THE ONE-CALL COMMIT TOOL, THE HAND EDIT OF A TOOL`S BANK, THE CHAINED WRITE COUNT, THE POST-SEAL READ, THE TOUCH READ`S DIFFERS, THE CARRIED NEXT ACT, THE VERSION (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '## THE CONTROLS',
        '  the bank is its controls: the compile control first, then the one-call commit tool at the head, then each repair`s instances through both routes; written through tools/standing/figbank.py ((R348)(2)(i))', '',
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
    out.append('### ### **v1.21.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1210.txt' % act), NL.join(out))
        print('written data/%s_standing_v1210.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
