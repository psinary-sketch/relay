# -*- coding: utf-8 -*-
"""b721_rebuild.py -- (R331)(7)(iii), THE REBUILD AT EACH WAVE 1 KERNEL'S OWN PIN, LAST AND STOPPABLE: SIDE-kernel v1.5 = 0e5233f,
SIDE-lv-conservation v0.10.0 = 93c27ec, and the four checkpoint kernels at (7)(i)'s pins, each built at the Mathlib its own lake-manifest.json
carries (the pin's tree, unchanged). One branch per kernel at the pinned commit, carrying nothing else; where a kernel has no workflow, the
branch carries SIDE-explicit-formula's .github/workflows/build-module.yml copied verbatim and nothing more (one commit on the pin, made by
git plumbing, its author and committer the seat's neutral identity so that no identifier of the author leaves in the push), printed as such.
One dispatch per kernel (six at most), read by its run id; the host's free memory read before each push, dispatch and read, beneath the
2,560 MB hold the step refused. A break printed with its opening error lines and held; nothing repaired. No lean or lake on this host; no
kernel's main or tag touched.

b718's routes (tools/b718_pin.py free_mb, hold_or_exit, gh, dispatch, read, opening_errors) are called with their rows file and download
directory pointed at b721's (data/b721_rebuild_rows.json; %TEMP%/b721_rebuild_artifacts), its branch name, its cap of six and its target
rule pointed at the pin's lakefile; b718's bump, stop and bank routes are not called.

  plan                 per kernel: the pin, its tag, the workflows on main and in the pin's tree, the Mathlib its manifest carries, the target
  branch <kernel>      the branch BRANCH at the pin (or, without a workflow, at the one plumbing commit carrying the workflow); one ref written
  push <kernel>        free memory read; the branch pushed to origin; ls-remote read; one row
  dispatch <kernel>    free memory read; b718's dispatch (build-module.yml at main, -f ref=<the branch's sha>, -f target); for a kernel with
                       no workflow on main, the dispatch at the branch itself, a refusal printed and rowed, nothing retried
  trigger <kernel>     the author's word: a trigger-only change to run on push to BRANCH, its one-line diff formed in memory and the
                       workflow's refusal step run under the TARGET a push carries and under the dispatch target; one row; nothing written
                       to the kernel
  rebranch <kernel>    the author's second word: one plumbing commit on the pushed copy commit, the workflow two lines against its source
                       (the push trigger beside workflow_dispatch; TARGET fixed); the diff printed; one ref moved (update-ref, old value checked)
  push_run <kernel>    free memory read; the fast-forward push, the run's trigger; ls-remote; the run found by branch, event and head sha
  read <kernel> <id>   b718's read route over b721's rows
  bank                 writes data/b721_rebuild.txt from data/b721_rebuild_rows.json
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

BRANCH = 'rebuild-b721'
ROWS = os.path.join(D_, 'b721_rebuild_rows.json')
OUT = os.path.join(D_, 'b721_rebuild.txt')
P.ROWS = ROWS
P.DL = os.path.join(os.environ.get('TEMP', ROOT), 'b721_rebuild_artifacts')
P.BRANCH = BRANCH
P.MAX_DISPATCH = 6
WF_SRC = ('SIDE-explicit-formula', 'HEAD', '.github/workflows/build-module.yml')
WF_PATH = '.github/workflows/build-module.yml'
SEAT = ['-c', 'user.name=b721 rebuild seat', '-c', 'user.email=b721-rebuild@relay.invalid']

PINS = [('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
        ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4')]
PIN = dict((k, (t, p)) for k, t, p in PINS)


def full(k):
    return P.gs('D:/' + k, 'rev-parse', PIN[k][1] + '^{commit}')


def wf_on_main(k):
    return bool(P.show('D:/' + k, 'main', WF_PATH))


def target_at_pin(k):
    if k in P.TARGETS:
        return P.TARGETS[k]
    lf, lt = P.lakefile('D:/' + k, full(k))
    return ' '.join(P.default_targets(lf, lt))


P.target_of = target_at_pin


def plan():
    print('### free memory %d MB (hold %d) ; branch %s ; rows %s' % (P.free_mb(), P.HOLD_MB, BRANCH, os.path.relpath(ROWS, ROOT)))
    for k, tag, p in PINS:
        repo = 'D:/' + k
        f = full(k)
        tags = P.gs(repo, 'tag', '--points-at', f).split()
        man = json.loads(P.show(repo, f, 'lake-manifest.json') or '{}')
        ml = [x.get('rev', '')[:12] for x in man.get('packages', []) if x['name'] == 'mathlib']
        wfp = [x for x in P.gs(repo, 'ls-tree', '--name-only', f, '.github/workflows/').split(NL) if x.strip()]
        local = P.gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH)
        remote = P.g(repo, 'ls-remote', 'origin', 'refs/heads/' + BRANCH)[1].strip()
        tagr = P.g(repo, 'ls-remote', 'origin', 'refs/tags/' + tag)[1].strip()
        print('## %-21s pin %s = %s (tags at it %s; origin tag %s -> %s) ; toolchain %s ; Mathlib %s ; workflows in the pin`s tree %s ; '
              'build-module.yml on main %s ; target %r ; %s local %s, on origin %s' % (
                  k, tag, f[:12], tags, tag, tagr[:12], (P.show(repo, f, 'lean-toolchain') or '').strip(), ml, wfp, wf_on_main(k),
                  target_at_pin(k), BRANCH, local[:10] or None, remote[:10] or None))
    src = P.show('D:/' + WF_SRC[0], WF_SRC[1], WF_SRC[2]) or ''
    print('### the workflow to carry where a kernel has none: %s at %s %s, %d bytes, sha1 blob %s ; identifier screen (orcid, @, the '
          'author`s surname): %s' % (WF_SRC[0], WF_SRC[1], P.gs('D:/' + WF_SRC[0], 'rev-parse', '--short=8', WF_SRC[1]), len(src.encode('utf-8')),
                                     P.gs('D:/' + WF_SRC[0], 'rev-parse', '%s:%s' % (WF_SRC[1], WF_SRC[2]))[:12],
                                     [w for w in ('orcid', '@hotmail', 'Seale') if w.lower() in src.lower()] or 'NONE'))


def branch(k):
    repo = 'D:/' + k
    if P.gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH):
        sys.exit('## %s: branch %s exists; nothing written' % (k, BRANCH))
    f = full(k)
    if wf_on_main(k):
        c, _o, e = P.g(repo, 'branch', BRANCH, f)
        assert c == 0, e
        print('## %s : %s at the pin %s itself, carrying nothing else' % (k, BRANCH, f[:12]))
        return
    src_blob = P.gs('D:/' + WF_SRC[0], 'rev-parse', '%s:%s' % (WF_SRC[1], WF_SRC[2]))
    data = P.show('D:/' + WF_SRC[0], WF_SRC[1], WF_SRC[2])
    b = P.blob(repo, data)
    assert b == src_blob, (b, src_blob)
    c, o, e = P.g(repo, 'ls-tree', f, '.github')
    if o.strip():
        sys.exit('## %s: the pin`s tree has .github (%s); nothing written' % (k, o.strip()))
    c, wft, e = P.g(repo, 'mktree', inp=('100644 blob %s\tbuild-module.yml\n' % b).encode('utf-8'))
    assert c == 0, e
    c, ght, e = P.g(repo, 'mktree', inp=('040000 tree %s\tworkflows\n' % wft.strip()).encode('utf-8'))
    assert c == 0, e
    rows = [l for l in P.gs(repo, 'ls-tree', f).split(NL) if l.strip()] + ['040000 tree %s\t.github' % ght.strip()]
    rows.sort(key=lambda l: l.split('\t', 1)[1] + ('/' if ' tree ' in l else ''))
    c, tree, e = P.g(repo, 'mktree', inp=(NL.join(rows) + NL).encode('utf-8'))
    assert c == 0, e
    msg = ('b721 under (R331)(7)(iii): the rebuild at the pin %s -- %s copied verbatim from %s (blob %s), nothing else; the kernel has no '
           'workflow' % (f[:12], WF_PATH, WF_SRC[0], b[:12]))
    c, cm, e = P.g(repo, *(SEAT + ['commit-tree', tree.strip(), '-p', f, '-m', msg]))
    assert c == 0, e
    cm = cm.strip()
    c, _o, e = P.g(repo, 'branch', BRANCH, cm)
    assert c == 0, e
    print('## %s : %s at %s, parent the pin %s, carrying %s (blob %s, equal to %s`s) and nothing else; author and committer %s' % (
        k, BRANCH, cm[:12], f[:12], WF_PATH, b[:12], WF_SRC[0], P.gs(repo, 'log', '-1', '--format=%an <%ae> / %cn <%ce>', cm)))
    print(P.g(repo, 'diff', '--stat', f, cm)[1].rstrip())


def push(k):
    repo = 'D:/' + k
    if [r for r in P.rows_load() if r.get('kind') == 'push' and r['kernel'] == k]:
        sys.exit('## %s already pushed at b721; nothing done' % k)
    tip = P.gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH)
    if not tip:
        sys.exit('## %s: no local %s; nothing pushed' % (k, BRANCH))
    want = full(k)
    if tip != want and P.gs(repo, 'rev-parse', tip + '^') != want:
        sys.exit('## %s: the tip %s is neither the pin nor its one child; nothing pushed' % (k, tip[:12]))
    fm = P.hold_or_exit('the push of ' + k)
    print('### free memory %d MB (hold %d) ; pushing %s %s at %s' % (fm, P.HOLD_MB, k, BRANCH, tip[:12]))
    c, o, e = P.g(repo, 'push', 'origin', BRANCH)
    print('   git push origin %s: exit %d %s' % (BRANCH, c, (o + e).strip().replace(NL, ' / ')[:300]))
    if c != 0:
        sys.exit('push refused; no row')
    remote = P.g(repo, 'ls-remote', 'origin', 'refs/heads/' + BRANCH)[1].strip()
    print('   ls-remote origin %s: %s ; equal to the tip %s' % (BRANCH, remote[:12], remote.startswith(tip)))
    P.rows_add({'kind': 'push', 'kernel': k, 'sha': tip, 'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'free_mb': fm,
                'remote_equal': remote.startswith(tip)})


def dispatch(k):
    if not [r for r in P.rows_load() if r.get('kind') == 'push' and r['kernel'] == k]:
        sys.exit('## %s: not pushed at b721; nothing dispatched' % k)
    if wf_on_main(k):
        P.dispatch(k)
        return
    repo = 'D:/' + k
    done = [r for r in P.rows_load() if r.get('kind') in ('dispatch', 'dispatch_refused')]
    if len(done) >= P.MAX_DISPATCH or [r for r in done if r['kernel'] == k]:
        sys.exit('## %s: dispatched already, or six reached; nothing dispatched' % k)
    sha = P.gs(repo, 'rev-parse', 'refs/heads/' + BRANCH)
    tgt = target_at_pin(k)
    fm = P.hold_or_exit('the dispatch of ' + k)
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    print('### free memory %d MB (hold %d) ; dispatching %s at its branch %s (no workflow on main), ref %s, target %s' % (
        fm, P.HOLD_MB, k, BRANCH, sha[:12], tgt))
    c, o, e = P.gh('workflow', 'run', 'build-module.yml', '-R', '%s/%s' % (P.OWNER, k), '--ref', BRANCH, '-f', 'ref=' + sha, '-f', 'target=' + tgt)
    print('   gh workflow run: exit %d %s %s' % (c, o.strip(), e.strip()))
    if c != 0:
        P.rows_add({'kind': 'dispatch_refused', 'kernel': k, 'sha': sha, 'target': tgt, 'at': t0, 'free_mb': fm,
                    'refusal': (o + e).strip()[:400]})
        print('   DISPATCH REFUSED: printed and held; nothing retried')
        return
    rid = None
    for _i in range(12):
        time.sleep(5)
        c, o, e = P.gh('run', 'list', '-R', '%s/%s' % (P.OWNER, k), '--workflow', 'build-module.yml', '--event', 'workflow_dispatch', '-L', '5',
                       '--json', 'databaseId,createdAt,status')
        new = [r for r in json.loads(o or '[]') if r['createdAt'] >= t0]
        if new:
            rid = new[-1]['databaseId']
            break
    print('   run id %s (created at or after %s)' % (rid, t0))
    P.rows_add({'kind': 'dispatch', 'kernel': k, 'sha': sha, 'target': tgt, 'at': t0, 'run': rid, 'free_mb': P.free_mb()})


def trigger(k):
    """### the author's word (b721, after the refusal): the copied workflow may change its trigger line alone, to run on push to BRANCH; the
    ### one-line diff printed; nothing on main. Before any commit or push: the diff formed in memory, and the workflow's own refusal step run
    ### (bash, on this host) under the TARGET a push carries -- `${{ inputs.target }}` with no inputs, the empty string -- and under the
    ### dispatch target (the control). An empty TARGET refused means a trigger-only change cannot build: HALTED, nothing written to the
    ### kernel, no run spent. Rowed as kind trigger_halt or trigger_clear."""
    import difflib
    import subprocess
    repo = 'D:/' + k
    wf = P.show(repo, 'refs/heads/' + BRANCH, WF_PATH) or ''
    L = wf.split(NL)
    old, new = '  workflow_dispatch:', '  push: { branches: [%s] }' % BRANCH
    n = [i for i, l in enumerate(L) if l == old]
    print('### %s: %s at %s ; the trigger needle %r yield %d' % (k, WF_PATH, BRANCH, old, len(n)))
    if len(n) != 1:
        sys.exit('needle yield not 1; nothing done')
    M = list(L)
    M[n[0]] = new
    diff = [x for x in difflib.unified_diff(L, M, lineterm='', n=0)][2:]
    print('   THE ONE-LINE DIFF (formed in memory, not committed):')
    for x in diff:
        print('     ' + x)
    i = L.index('      - name: Refuse a target outside the lake grammar')
    case = NL.join(l[10:] for l in L[i + 2:i + 5])
    tgt = target_at_pin(k)
    res = {}
    for t in ('', tgt):
        p = subprocess.run(['bash', '-c', "TARGET='%s'%s%s%secho PASSED" % (t, NL, case, NL)], capture_output=True, text=True)
        res[t] = (p.returncode, (p.stdout + p.stderr).strip())
        print('   the refusal step under TARGET=%r (%s): exit %d %s' % (t, 'a push: inputs.target empty' if not t else 'the control: the '
                                                                        'dispatch target', p.returncode, res[t][1]))
    halt = res[''][0] != 0 and res[tgt][0] == 0
    print('   %s' % ('HALTED: on a push inputs.target is empty and the workflow`s own refusal step exits %d before elan, the cache or lake; '
                     'every trigger-only change leaves TARGET empty (env TARGET reads inputs.target alone), so none can build; nothing '
                     'committed, nothing pushed, no run spent' % res[''][0] if halt else 'NOT HALTED by the refusal step'))
    P.rows_add({'kind': 'trigger_halt' if halt else 'trigger_clear', 'kernel': k, 'diff': diff, 'target': tgt,
                'empty_exit': res[''][0], 'empty_out': res[''][1], 'control_exit': res[tgt][0],
                'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})


PUSH_LINE = '  push: { branches: [%s] }' % BRANCH


def wf_on_push(k):
    """### the author's second word (b721): the copied workflow with two lines against SIDE-explicit-formula's file -- the push trigger,
    ### entered beside workflow_dispatch (replacing that key would orphan its inputs block, which YAML does not allow), and the target
    ### fixed (TARGET: <the pin's target>), since a push carries no inputs. inputs.ref stays: empty on a push, checkout takes the pushed sha."""
    src = P.show('D:/' + WF_SRC[0], WF_SRC[1], WF_SRC[2])
    L = src.split(NL)
    assert L.count('on:') == 1 and L.count('      TARGET: ${{ inputs.target }}') == 1, 'needle yield not 1'
    M = list(L)
    M.insert(M.index('on:') + 1, PUSH_LINE)
    M[M.index('      TARGET: ${{ inputs.target }}')] = '      TARGET: %s' % target_at_pin(k)
    return L, M


def rebranch(k):
    repo = 'D:/' + k
    pushed = [r for r in P.rows_load() if r.get('kind') == 'push' and r['kernel'] == k]
    tip = P.gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH)
    if not pushed or tip != pushed[-1]['sha'] or wf_on_main(k):
        sys.exit('## %s: the tip is not the pushed copy commit, or the kernel has the workflow on main; nothing written' % k)
    import difflib
    L, M = wf_on_push(k)
    diff = [x for x in difflib.unified_diff(L, M, 'SIDE-explicit-formula:' + WF_PATH, BRANCH + ':' + WF_PATH, lineterm='', n=0)]
    print('### %s: THE DIFF AGAINST %s`s %s (at %s):' % (k, WF_SRC[0], WF_PATH, P.gs('D:/' + WF_SRC[0], 'rev-parse', '--short=8', WF_SRC[1])))
    for x in diff:
        print('   ' + x)
    b = P.blob(repo, NL.join(M))
    c, wft, e = P.g(repo, 'mktree', inp=('100644 blob %s\tbuild-module.yml\n' % b).encode('utf-8'))
    assert c == 0, e
    c, ght, e = P.g(repo, 'mktree', inp=('040000 tree %s\tworkflows\n' % wft.strip()).encode('utf-8'))
    assert c == 0, e
    rows = [l for l in P.gs(repo, 'ls-tree', tip).split(NL) if l.strip() and not l.endswith('\t.github')] + ['040000 tree %s\t.github' % ght.strip()]
    rows.sort(key=lambda l: l.split('\t', 1)[1] + ('/' if ' tree ' in l else ''))
    c, tree, e = P.g(repo, 'mktree', inp=(NL.join(rows) + NL).encode('utf-8'))
    assert c == 0, e
    msg = ('b721 under (R331)(7)(iii), the author`s word: %s runs on push to %s with its target fixed (%s), two lines against %s`s file; '
           'the dispatch at the branch was refused (no workflow on main)' % (WF_PATH, BRANCH, target_at_pin(k), WF_SRC[0]))
    c, cm, e = P.g(repo, *(SEAT + ['commit-tree', tree.strip(), '-p', tip, '-m', msg]))
    assert c == 0, e
    cm = cm.strip()
    c, _o, e = P.g(repo, 'update-ref', 'refs/heads/' + BRANCH, cm, tip)
    assert c == 0, e
    print('## %s : %s at %s, parent %s (the pushed copy commit), author and committer %s ; tree change:' % (
        k, BRANCH, cm[:12], tip[:12], P.gs(repo, 'log', '-1', '--format=%an <%ae> / %cn <%ce>', cm)))
    print(P.g(repo, 'diff', '--stat', tip, cm)[1].rstrip())
    P.rows_add({'kind': 'rebranch', 'kernel': k, 'sha': cm, 'parent': tip, 'diff': diff, 'target': target_at_pin(k),
                'at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})


def push_run(k):
    """### the second push (fast-forward from the pushed copy commit to rebranch's commit); the push is the run's trigger, the sixth run
    ### (the remaining dispatch); its run found by the branch and event, rowed as a dispatch (via push)."""
    repo = 'D:/' + k
    rb = [r for r in P.rows_load() if r.get('kind') == 'rebranch' and r['kernel'] == k]
    done = [r for r in P.rows_load() if r.get('kind') == 'dispatch']
    if not rb or [r for r in P.rows_load() if r.get('kind') == 'push2' and r['kernel'] == k] or len(done) >= P.MAX_DISPATCH:
        sys.exit('## %s: no rebranch row, pushed already, or six runs reached; nothing pushed' % k)
    tip = P.gs(repo, 'rev-parse', 'refs/heads/' + BRANCH)
    if tip != rb[-1]['sha']:
        sys.exit('## %s: the tip is not rebranch`s commit; nothing pushed' % k)
    fm = P.hold_or_exit('the push of ' + k)
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    print('### free memory %d MB (hold %d) ; pushing %s %s at %s (fast-forward from %s)' % (fm, P.HOLD_MB, k, BRANCH, tip[:12], rb[-1]['parent'][:12]))
    c, o, e = P.g(repo, 'push', 'origin', BRANCH)
    print('   git push origin %s: exit %d %s' % (BRANCH, c, (o + e).strip().replace(NL, ' / ')[:300]))
    if c != 0:
        sys.exit('push refused; no row')
    remote = P.g(repo, 'ls-remote', 'origin', 'refs/heads/' + BRANCH)[1].strip()
    print('   ls-remote origin %s: %s ; equal to the tip %s' % (BRANCH, remote[:12], remote.startswith(tip)))
    P.rows_add({'kind': 'push2', 'kernel': k, 'sha': tip, 'at': t0, 'free_mb': fm, 'remote_equal': remote.startswith(tip)})
    rid = None
    for _i in range(24):
        time.sleep(5)
        c, o, e = P.gh('run', 'list', '-R', '%s/%s' % (P.OWNER, k), '--branch', BRANCH, '--event', 'push', '-L', '5',
                       '--json', 'databaseId,createdAt,status,headSha')
        new = [r for r in json.loads(o or '[]') if r['createdAt'] >= t0 and r['headSha'] == tip]
        if new:
            rid = new[-1]['databaseId']
            break
    print('   run id %s (event push, head %s, created at or after %s)' % (rid, tip[:12], t0))
    P.rows_add({'kind': 'dispatch', 'kernel': k, 'sha': tip, 'target': target_at_pin(k), 'at': t0, 'run': rid, 'free_mb': P.free_mb(),
                'via': 'push'})


def fro_line(reads, disp):
    k = 'SIDE-frobenius'
    if k not in disp:
        return 'SIDE-frobenius HELD, ITS DISPATCH REFUSED, A TRIGGER-ONLY CHANGE HALTED (EMPTY TARGET REFUSED)'
    if k not in reads:
        return 'SIDE-frobenius RUN ON PUSH (THE AUTHOR`S TWO LINES), NOT READ'
    return 'SIDE-frobenius RUN ON PUSH (THE AUTHOR`S TWO LINES): %s' % reads[k]['verdict']


def bank():
    rs = P.rows_load()
    pushes = dict((r['kernel'], r) for r in rs if r['kind'] == 'push')
    disp = dict((r['kernel'], r) for r in rs if r['kind'] == 'dispatch')
    refused = dict((r['kernel'], r) for r in rs if r['kind'] == 'dispatch_refused')
    reads = {}
    for r in rs:
        if r['kind'] == 'read':
            reads[r['kernel']] = r
    builds = sum(1 for r in reads.values() if r['verdict'] == 'BUILDS')
    out = ['b721 -- (R331)(7)(iii): THE REBUILD AT EACH WAVE 1 KERNEL`S OWN PIN, LAST AND STOPPABLE -- one branch %s per kernel at its pin, '
           'one dispatch each, read by its run id (%s)' % (BRANCH, time.strftime('%Y-%m-%d', time.gmtime())), '',
           '### Written by tools/b721_rebuild.py bank from data/b721_rebuild_rows.json (its push, dispatch and read routes; b718`s dispatch and',
           '### read routes pointed at b721`s rows). Each kernel at the Mathlib its own manifest carries; nothing repaired; no main or tag touched;',
           '### no lean or lake process on this host; the free memory read before each push, dispatch and read against the 2,560 MB hold.',
           '### THE READING OF "where a kernel has no workflow": no build-module.yml on its main (the dispatch reads the workflow from main);',
           '### five mains carry it, so five branches stand at their pins carrying nothing; SIDE-frobenius has none, and its branch carries',
           '### SIDE-explicit-formula`s build-module.yml verbatim in one commit on the pin, its author and committer the seat`s neutral identity',
           '### (b721 rebuild seat <b721-rebuild@relay.invalid>), no identifier of the author in it. The pins` own trees carry a workflow at',
           '### SIDE-kernel alone (build.yml, triggered by a push to main only, so the branch push ran nothing).', '',
           'PUSHED %d ; DISPATCHED %d (six at most) ; DISPATCH REFUSED %d ; READ %d ; BUILDS %d OF 6 ; HELD (BREAKS) %d ; NOT READ %d' % (
               len(pushes), len(disp), len(refused), len(reads), builds, sum(1 for r in reads.values() if r['verdict'].startswith('HELD')),
               len(disp) - len(reads)), '']
    for k, tag, p in PINS:
        pu = pushes.get(k)
        line = '  %-21s %s = %s' % (k, tag, p)
        if not pu:
            out.append(line + ' : NOT PUSHED, carried')
            continue
        line += ' ; pushed %s (host free %d MB, origin equal %s)' % (pu['sha'][:10], pu['free_mb'], pu['remote_equal'])
        if k in refused:
            out.append(line + ' ; DISPATCH REFUSED (host free %d MB): %s ; HELD' % (refused[k]['free_mb'], refused[k]['refusal'].replace(NL, ' / ')))
            for th in [r for r in rs if r['kind'] in ('trigger_halt', 'trigger_clear') and r['kernel'] == k]:
                out.append('      THE AUTHOR`S WORD (a trigger-only change to run on push to %s; nothing on main), read at %s:' % (BRANCH, th['at']))
                out += ['      diff | ' + x for x in th['diff']]
                out.append('      the workflow`s refusal step under the TARGET a push carries (inputs.target empty): exit %d "%s" ; under the '
                           'dispatch target %r (the control): exit %d' % (th['empty_exit'], th['empty_out'], th['target'], th['control_exit']))
                out.append('      %s' % ('HALTED: no trigger-only change can build (env TARGET reads inputs.target alone); nothing committed or '
                                         'pushed, no run spent; a second line (the target) is the author`s to rule' if th['kind'] == 'trigger_halt'
                                         else 'NOT HALTED by the refusal step'))
            for rb in [r for r in rs if r['kind'] == 'rebranch' and r['kernel'] == k]:
                out.append('      THE AUTHOR`S SECOND WORD (the target fixed beside the push trigger), read at %s: %s at %s, parent %s ; the diff '
                           'against %s`s file:' % (rb['at'], BRANCH, rb['sha'][:10], rb['parent'][:10], WF_SRC[0]))
                out += ['      diff | ' + x for x in rb['diff']]
            for p2 in [r for r in rs if r['kind'] == 'push2' and r['kernel'] == k]:
                out.append('      pushed %s (host free %d MB, origin equal %s), the push the run`s trigger' % (p2['sha'][:10], p2['free_mb'], p2['remote_equal']))
            if k not in disp:
                continue
            p2s = [r for r in rs if r['kind'] == 'push2' and r['kernel'] == k]
            line = '  %-21s %s = %s ; the run triggered by the push of %s' % (k, tag, p, p2s[-1]['sha'][:10] if p2s else '-')
        d = disp.get(k)
        if not d:
            out.append(line + ' ; NOT DISPATCHED, carried')
            continue
        r = reads.get(k)
        if not r:
            out.append(line + ' ; run %s (target %s): NOT READ, carried' % (d['run'], d['target']))
            continue
        out.append(line + ' ; run %s at %s (target %s, host free %d MB): %s %s ; build exit %s ; memory low %s MB ; sorry warnings %d ; '
                   'host free %d MB at the read ; %s' % (r['run'], d['at'], d['target'], d['free_mb'], r['status'], r['conclusion'], r['build_exit'],
                                                       r['mem_low_mb'], r['sorry_warnings'], r['free_mb'], r['verdict']))
        for l in r['error_lines']:
            out.append('      | ' + l[:220])
        bad = [s for s in r.get('steps', []) if s[1] not in ('success', 'skipped', None)]
        if bad:
            out.append('      steps not succeeding: %s -- the run`s conclusion is theirs; the build exit is read from the artifact' % bad)
        ax =[l for l in r.get('axioms_lines', []) if 'axiom' in l.lower()][:12]
        for l in ax:
            out.append('      axioms | ' + l[:220])
    sor = ['%s (sorry warnings %d; sorryAx in %s)' % (k, r['sorry_warnings'],
                                                       [l.split("'")[1] for l in r.get('axioms_lines', []) if 'sorryAx' in l and "'" in l] or 'no axiom line read')
           for k, r in sorted(reads.items()) if r['sorry_warnings']]
    out += ['', '## THE GRADE',
            '  BUILDS means the build exit 0 under the hold, read from the run`s artifact. A build carrying a sorry builds and is not complete:',
            '  %s.' % ('; '.join(sor) if sor else 'none carries one'),
            '', '### ### **%d OF 6 WAVE 1 KERNELS BUILD AT THEIR OWN PINS (%s) ; %s ; RUNS %d ; '
            'NOTHING REPAIRED ; NO MAIN OR TAG TOUCHED.**' % (builds, ('ONE WITH A SORRY: ' + sor[0].split(' ')[0]) if len(sor) == 1 else
                                                           ('%d WITH A SORRY' % len(sor)), fro_line(reads, disp), len(disp))]
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline='\n').write(NL.join(out) + NL)
    os.replace(OUT + '.tmp', OUT)
    print(NL.join(out))
    print('written data/b721_rebuild.txt')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'plan':
        plan()
    elif a[0] == 'branch':
        branch(a[1])
    elif a[0] == 'push':
        push(a[1])
    elif a[0] == 'dispatch':
        dispatch(a[1])
    elif a[0] == 'read':
        P.read(a[1], a[2])
    elif a[0] == 'rebranch':
        rebranch(a[1])
    elif a[0] == 'push_run':
        push_run(a[1])
    elif a[0] == 'trigger':
        trigger(a[1])
    elif a[0] == 'bank':
        bank()
