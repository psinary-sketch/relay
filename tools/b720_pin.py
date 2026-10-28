# -*- coding: utf-8 -*-
"""b720_pin.py -- (R330)(5)(iii), THE PIN'S REMAINDER, LAST AND STOPPABLE: of b718's carried pin-b718-de5ce8a9 branches, the frozen kernels
(SIDE-archimedean, SIDE-frobenius, SIDE-spinor, SIDE-rcurve: "the freeze") and SIDE-cosmo (pages: write) excluded; the six eligible pushed
and dispatched one per message, free memory read before each (beneath 2,560 MB the step is refused); each build read by its run id; a break
printed with its opening error lines and held; nothing repaired. No lean or lake process on this host; no kernel's main touched; no tag.

b718's own routes (tools/b718_pin.py dispatch and read) are called with their rows file and download directory pointed at b720's
(data/b720_pin_rows.json; %TEMP%/b720_pin_artifacts), so no bank of b718 is written; its bump, stop and bank routes are not called.

  plan                 the exclusions with their reasons; per eligible kernel its local branch tip against b718's carried row, on origin or not
  go <kernel>          one kernel: free memory read, the tip checked against b718's carried row, the branch pushed, ls-remote read, then
                       free memory read again and b718's dispatch route (its target rule, its run-id read); appends the dispatch row
  read <kernel> <id>   b718's read route over b720's rows: status, conclusion, build exit, the opening error lines; appends its row
  bank                 writes data/b720_pin.txt and data/b720_pin.json from data/b720_pin_rows.json
"""
import io
import json
import os
import sys
import time

NL = chr(10)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b718_pin as P   # noqa: E402

ROWS = os.path.join(D_, 'b720_pin_rows.json')
P.ROWS = ROWS                                                         # b718's routes append here, not to data/b718_pin_rows.json
P.DL = os.path.join(os.environ.get('TEMP', ROOT), 'b720_pin_artifacts')
B718_ROWS = os.path.join(D_, 'b718_pin_rows.json')                    # read only

FREEZE = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve')
EXCLUDED = dict([(k, 'the freeze: a Phase-1.2 checkpoint kernel, frozen (REGISTRY :711-:720); (R330)(5)(iii)') for k in FREEZE] +
                [('SIDE-cosmo', 'pages: write -- lean_action_ci.yml runs on every push with docgen-action and pages: write, so a branch push may '
                                'publish its pages (b718 HELD); (R330)(5)(iii)')])
ELIGIBLE = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-simplicity', 'SIDE-trivium')
DONE_AT_B718 = 'SIDE-effects'


def carried():
    rs = json.load(io.open(B718_ROWS, encoding='utf-8'))
    return dict((r['kernel'], r) for r in rs if r.get('kind') == 'carried')


def plan():
    assert set(ELIGIBLE) | set(EXCLUDED) | {DONE_AT_B718} == set(P.KERNELS), 'the partition does not cover b718\'s twelve'
    print('### b718\'s twelve: %s dispatched and read at b718 (BUILDS); %d excluded; %d eligible' % (DONE_AT_B718, len(EXCLUDED), len(ELIGIBLE)))
    for k in P.KERNELS:
        if k in EXCLUDED:
            print('  %-22s EXCLUDED: %s' % (k, EXCLUDED[k]))
    cr = carried()
    print('### free memory %d MB (hold %d)' % (P.free_mb(), P.HOLD_MB))
    for k in ELIGIBLE:
        repo = 'D:/' + k
        tip = P.gs(repo, 'rev-parse', 'refs/heads/' + P.BRANCH)
        remote = P.g(repo, 'ls-remote', 'origin', 'refs/heads/' + P.BRANCH)[1].strip()
        print('  %-22s ELIGIBLE: local %s at %s ; b718 carried %s ; equal %s ; on origin %s ; target %s' % (
            k, P.BRANCH, tip[:10], cr.get(k, {}).get('sha', '')[:10], tip == cr.get(k, {}).get('sha'), remote[:10] or False, P.target_of(k)))
    done = [r for r in P.rows_load() if r.get('kind') == 'dispatch']
    print('### b720 dispatch rows so far: %d %s' % (len(done), [r['kernel'] for r in done]))


def go(k):
    repo = 'D:/' + k
    if [r for r in P.rows_load() if r.get('kind') == 'dispatch' and r['kernel'] == k]:
        sys.exit('## %s already dispatched at b720; nothing done' % k)
    fm = P.hold_or_exit('the push of ' + k)
    tip = P.gs(repo, 'rev-parse', 'refs/heads/' + P.BRANCH)
    want = carried().get(k, {}).get('sha')
    print('### free memory %d MB (hold %d) ; %s local %s at %s ; b718 carried %s ; equal %s' % (
        fm, P.HOLD_MB, k, P.BRANCH, tip[:10], (want or '')[:10], tip == want))
    if tip != want:
        sys.exit('## %s: the local tip is not b718\'s carried commit; nothing pushed' % k)
    c, o, e = P.g(repo, 'push', 'origin', P.BRANCH)
    print('   git push origin %s: exit %d %s' % (P.BRANCH, c, (o + e).strip().replace(NL, ' / ')[:300]))
    if c != 0:
        sys.exit('push refused; nothing dispatched')
    remote = P.g(repo, 'ls-remote', 'origin', 'refs/heads/' + P.BRANCH)[1].strip()
    print('   ls-remote origin %s: %s ; equal to the tip %s' % (P.BRANCH, remote[:12], remote.startswith(tip)))
    P.rows_add({'kind': 'push', 'kernel': k, 'sha': tip, 'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'free_mb': fm,
                'remote_equal': remote.startswith(tip)})
    P.dispatch(k)


def bank():
    rs = P.rows_load()
    pushes = [r for r in rs if r['kind'] == 'push']
    disp = [r for r in rs if r['kind'] == 'dispatch']
    reads = {}
    for r in rs:
        if r['kind'] == 'read':
            reads[r['kernel']] = r
    builds = [k for k in ELIGIBLE if reads.get(k, {}).get('verdict') == 'BUILDS']
    out = ['b720 -- (R330)(5)(iii): THE PIN\'S REMAINDER, LAST AND STOPPABLE -- b718\'s carried branches %s (Mathlib %s, %s), the freeze and '
           'SIDE-cosmo excluded, the eligible pushed and dispatched one per message, each read by its run id (%s)' % (
               P.BRANCH, P.TARGET_REV, P.TOOLCHAIN, time.strftime('%Y-%m-%d', time.gmtime())), '',
           '### Written by tools/b720_pin.py bank from data/b720_pin_rows.json (the rows its go route and b718\'s dispatch and read routes, pointed',
           '### at b720\'s rows file, appended). The branches are b718\'s bump commits, unchanged (each tip checked against b718\'s carried row before',
           '### its push); no kernel\'s main touched, no tag cut, nothing repaired; no lean or lake process on this host.', '',
           'THE PIN AT %d OF %d ELIGIBLE (BUILDS) ; PUSHED %d ; DISPATCHED %d ; READ %d ; HELD (BREAKS) %d ; NOT READ %d ; EXCLUDED %d ; AT b718 1 (%s, BUILDS)' % (
               len(builds), len(ELIGIBLE), len(pushes), len(disp), len(reads),
               sum(1 for r in reads.values() if r['verdict'].startswith('HELD')), len(disp) - len(reads), len(EXCLUDED), DONE_AT_B718), '']
    for k in P.KERNELS:
        if k in EXCLUDED:
            out.append('  %-22s EXCLUDED: %s' % (k, EXCLUDED[k]))
            continue
        if k == DONE_AT_B718:
            out.append('  %-22s at b718: run 40587516142, BUILDS (data/b718_pin.txt)' % k)
            continue
        p = [r for r in pushes if r['kernel'] == k]
        d = [r for r in disp if r['kernel'] == k]
        if not d:
            out.append('  %-22s ELIGIBLE, NOT DISPATCHED at b720%s' % (k, (' (pushed %s at %s)' % (p[0]['sha'][:10], p[0]['at'])) if p else ' (not pushed)'))
            continue
        d = d[0]
        r = reads.get(k)
        pre = '  %-22s pushed %s (host free %s MB) ; run %s at %s (target %s, host free %s MB)' % (
            k, d['sha'][:10], p[0]['free_mb'] if p else '?', d['run'], d['at'], d['target'], d['free_mb'])
        if not r:
            out.append(pre + ': NOT READ, carried')
            continue
        out.append(pre + ': %s %s ; build exit %s ; memory low %s MB ; sorry warnings %d ; host free %d MB at the read ; %s' % (
            r['status'], r['conclusion'], r['build_exit'], r['mem_low_mb'], r['sorry_warnings'], r['free_mb'], r['verdict']))
        for l in r['error_lines']:
            out.append('      | ' + l[:220])
    t = NL.join(out) + NL
    j = json.dumps({'eligible': ELIGIBLE, 'excluded': EXCLUDED, 'push': pushes, 'dispatch': disp, 'read': list(reads.values())},
                   indent=1, ensure_ascii=False) + NL
    io.open(os.path.join(D_, 'b720_pin.txt'), 'w', encoding='utf-8', newline='\n').write(t)
    io.open(os.path.join(D_, 'b720_pin.json'), 'w', encoding='utf-8', newline='\n').write(j)
    print(t)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['plan']:
        plan()
    elif len(a) == 2 and a[0] == 'go' and a[1] in ELIGIBLE:
        go(a[1])
    elif len(a) == 3 and a[0] == 'read' and a[1] in ELIGIBLE:
        P.read(a[1], a[2])
    elif a == ['bank']:
        bank()
    else:
        sys.exit(__doc__)
