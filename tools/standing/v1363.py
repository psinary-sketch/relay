# -*- coding: utf-8 -*-
"""standing/v1363.py -- THE CONTROLS OF v1.36.3, (R369)(4)(i): THE ROUTE THAT REMOVES A BRANCH AT A KERNEL'S REMOTE, in v1361.py's form.

The ruling's words (relay data/b759_ferry.txt :15): "(i) THE ROUTE THAT REMOVES A BRANCH AT A KERNEL'S REMOTE: a named branch, not main,
removed at the remote where its remote tip is an ancestor of the remote's main; refused for main, for a name on the kept list and for a tip
that is no ancestor; read back absent. Its controls, in a scratch remote: a refusal on a planted unmerged branch, a refusal on main, a refusal
on a kept name, and one removal read back. Its use: (3)." tools/standing/commit.py v1.36.3 adds `rdelete <branch>` (kept_names,
rdelete_refusal, rdelete_plan, rdelete_route), opened act by act and kernel by kernel by RDELETE_ACTS. BEFORE is commit.py at BASE, executed
as a module of its own; AFTER the working file. The planted cases run in scratch repositories in the system's temporary folder (a bare
repository standing for the remote, a clone of it standing for the kernel), removed after; the cases that remove open the route for a planted
act `bctl` by setting the working module's table and kept reader for the call alone and restoring them after; no kernel, no remote and no path
of the scratch is touched or printed.

  (table)      RDELETE_ACTS opens b759 at the two kernels with (3)'s five names; refused for b758, the relay and a third repository. BEFORE: no
               rdelete_refusal, `rdelete` no write.
  (kept)       the kept list read from tools/b759_worklist.py's KEPT_BRANCHES: SIDE-explicit-formula's names (zq-b730 among them) and
               SIDE-dirichlet-mod-24's push-b757-workflow; each refused at b759 as KEPT; push-b758-coeff and push-b757-mod24 not.
  (main)       THE ORDERED CONTROL: `rdelete main` in a planted remote: refused, the remote's main unmoved.
  (unmerged)   THE ORDERED CONTROL: a planted branch whose tip is no ancestor of the remote's main: refused, UNMERGED, the branch at the remote.
  (keptname)   THE ORDERED CONTROL: a planted kept name, merged and named by the table: refused, KEPT, the branch at the remote.
  (removal)    THE ORDERED CONTROL: a planted merged branch the table names: removed, read back absent; the clone's own branch of the name kept.
  (unnamed)    a merged branch the table does not name: refused; a named branch absent at the remote: refused.
  (closed)     through write_route at b758 in a planted clone: refused, the remote's branch kept.
  (diff)       the working commit.py against BASE's: two lines removed (WRITES, the entry's kernel test).
  (version)    tools/standing/VERSION moved to v1.36.3.

  python -X utf8 -u tools/standing/v1363.py control [table|kept|main|unmerged|keptname|removal|unnamed|closed|diff|version ...] [--bank]
"""
import difflib
import io
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = 'e16d9603'   # ### the relay's HEAD before this change (b759 component 1, step 8, v1.36.2)
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
CTL = 'bctl'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import commit as C1             # noqa: E402  (the working file: AFTER)
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}
PREFIX = 'v1363_'


def base():
    if 'C0' not in _MEMO:
        src = V.show(BASE, 'tools/standing/commit.py')
        m = types.ModuleType('commit_base')
        m.__file__ = os.path.join(S, 'commit.py')
        exec(compile(src, 'commit.py@%s' % BASE, 'exec'), m.__dict__)   # noqa: S102
        _MEMO['C0'] = m
        _MEMO['src0'] = src
    return _MEMO['C0']


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def _r(x):
    return 'None' if x is None else 'REFUSED (%s)' % x[:90]


def trial(fn):
    try:
        return False, str(fn())[:220]
    except SystemExit as e:
        return True, str(e)[:220]
    except Exception as e:  # noqa: BLE001
        if type(e).__name__ == 'Refused':
            return True, str(e)[:220]
        raise


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0:
        raise RuntimeError('the planted repository`s git %s exit %d: %s' % (a[0], r.returncode, (r.stderr or r.stdout).strip()[:160]))
    return r.stdout.strip()


class Planted(object):
    """a bare repository standing for a kernel's remote with main at c0 then c1, and a clone of it standing for the kernel; removed by close()."""

    def __init__(self):
        self.root = tempfile.mkdtemp(prefix=PREFIX)
        self.bare = os.path.join(self.root, 'r.git')
        self.mark = os.path.join(self.root, 'mark.json')
        self.id = C1._identity(RELAY)
        g(self.root, 'init', '-q', '--bare', '-b', 'main', self.bare)
        w = os.path.join(self.root, 'w')
        os.mkdir(w)
        g(w, 'init', '-q', '-b', 'main')
        self._config(w)
        g(w, 'remote', 'add', 'origin', self.bare)
        self.c0 = self.put(w, {'A.lean': 'x0\n'}, 'c0')
        self.c1 = self.put(w, {'A.lean': 'x1\n'}, 'c1')
        g(w, 'push', '-q', 'origin', 'main')
        g(w, 'push', '-q', 'origin', '%s:refs/heads/merged' % self.c0)
        g(w, 'push', '-q', 'origin', '%s:refs/heads/keep-x' % self.c0)
        g(w, 'push', '-q', 'origin', '%s:refs/heads/other' % self.c0)
        g(w, 'checkout', '-q', '-b', 'side', self.c0)
        self.x = self.put(w, {'B.lean': 'sibling\n'}, 'a sibling of c1, not on main')
        g(w, 'push', '-q', 'origin', 'side')
        self.k = self.clone('k')
        g(self.k, 'branch', '-q', 'merged', 'origin/merged')

    def _config(self, r):
        g(r, 'config', 'user.email', self.id[0])
        g(r, 'config', 'user.name', self.id[1])
        g(r, 'config', 'core.autocrlf', 'false')

    def put(self, repo, files, msg):
        for k, v in files.items():
            with open(os.path.join(repo, k), 'w', encoding='utf-8', newline='\n') as f:
                f.write(v)
        g(repo, 'add', '--', *files)
        g(repo, 'commit', '-q', '-m', msg)
        return g(repo, 'rev-parse', 'HEAD')

    def clone(self, name):
        p = os.path.join(self.root, name)
        g(self.root, 'clone', '-q', '-c', 'core.autocrlf=false', self.bare, p)
        self._config(p)
        return p

    def remote(self, branch):
        r = subprocess.run(['git', '-C', self.bare, 'rev-parse', '-q', '--verify', 'refs/heads/%s' % branch], capture_output=True, text=True)
        return r.stdout.strip()

    def local(self, branch):
        r = subprocess.run(['git', '-C', self.k, 'rev-parse', '-q', '--verify', 'refs/heads/%s' % branch], capture_output=True, text=True)
        return r.stdout.strip()

    def rdel(self, name, act=CTL, mod=None, names=('merged', 'side', 'keep-x', 'gone', 'main'), kept=('keep-x',)):
        m = mod or C1
        saved_t = getattr(m, 'RDELETE_ACTS', None)
        saved_k = getattr(m, 'kept_names', None)
        if act == CTL and saved_t is not None:
            m.RDELETE_ACTS = {CTL: {EF: tuple(names)}}
            m.kept_names = lambda a_, k_: tuple(kept)
        try:
            return trial(lambda: m.write_route(EF, 'rdelete', [name], act=act, repo=self.k, mark_path=self.mark))
        finally:
            if saved_t is not None:
                m.RDELETE_ACTS = saved_t
                m.kept_names = saved_k

    def close(self):
        r = os.path.abspath(self.root)
        if not (os.path.isabs(r) and os.path.basename(r).startswith(PREFIX)
                and os.path.normcase(os.path.dirname(r)) == os.path.normcase(os.path.abspath(tempfile.gettempdir()))):
            raise RuntimeError('THE SCRATCH ROOT NOT VERIFIED, NOTHING REMOVED')

        def onerr(fn, p, _e):
            os.chmod(p, stat.S_IWRITE)
            fn(p)
        shutil.rmtree(r, onerror=onerr)


def _planted(fn):
    p = Planted()
    try:
        return fn(p)
    finally:
        p.close()


def control_table():
    L = ['### (table): THE ROUTE OPENED ACT BY ACT AND KERNEL BY KERNEL BY RDELETE_ACTS']
    b0 = base()
    before = 'rdelete_refusal %s ; rdelete among the writes %s' % ('present' if hasattr(b0, 'rdelete_refusal') else 'absent', 'rdelete' in b0.WRITES)
    t = C1.RDELETE_ACTS
    want = {'b759': {EF: ('push-b757-join', 'push-b757-coeff', 'push-b758-land', 'push-b758-coeff'), M24: ('push-b757-mod24',)}}
    shut = [C1.rdelete_refusal(k, a, n, kept=()) for k, a, n in ((EF, 'b758', 'push-b758-coeff'), ('relay', 'b759', 'push-b758-coeff'),
                                                                  ('SIDE-kernel', 'b759', 'push-b758-coeff'))]
    after = 'RDELETE_ACTS %r ; refused at b758, the relay, a third repository %s' % (t, [x is not None for x in shut])
    return L, case(L, 'table', 'the table as (R369)(3) names the five, and the shut cases', before, after,
                   not hasattr(b0, 'rdelete_refusal') and 'rdelete' not in b0.WRITES,
                   t == want and all(x is not None for x in shut) and 'rdelete' in C1.WRITES), 1


def control_kept():
    L = ['### (kept): THE KEPT LIST READ FROM tools/b759_worklist.py']
    ke, km = C1.kept_names('b759', EF), C1.kept_names('b759', M24)
    r = [C1.rdelete_refusal(M24, 'b759', 'push-b757-workflow'), C1.rdelete_refusal(EF, 'b759', 'zq-b730'),
         C1.rdelete_refusal(EF, 'b759', 'push-b758-coeff'), C1.rdelete_refusal(M24, 'b759', 'push-b757-mod24')]
    return L, case(L, 'kept', 'the kept names by kernel and the refusals at b759 (push-b757-workflow, zq-b730 ; push-b758-coeff, push-b757-mod24)',
                   'n/a (the route absent at BASE)', 'EF kept %d %s ; M24 kept %s ; %s' % (len(ke), list(ke), list(km), [_r(x)[:60] for x in r]),
                   True, 'zq-b730' in ke and km == ('push-b757-workflow',) and 'push-b758-coeff' not in ke
                   and r[0] is not None and 'KEPT LIST' in r[0] and r[1] is not None and 'KEPT LIST' in r[1] and r[2] is None and r[3] is None), 1


def control_flow():
    L = ['### (main), (unmerged), (keptname), (removal), (unnamed): ONE PLANTED REMOTE, main AT c1']

    def run(p):
        out = dict(c0=p.c0, c1=p.c1, x=p.x)
        out['b'] = p.rdel('merged', mod=base())
        out['main'] = p.rdel('main')
        out['main_after'] = p.remote('main')
        out['side'] = p.rdel('side')
        out['side_after'] = p.remote('side')
        out['keep'] = p.rdel('keep-x')
        out['keep_after'] = p.remote('keep-x')
        out['other'] = p.rdel('other')
        out['other_after'] = p.remote('other')
        out['gone'] = p.rdel('gone')
        out['rm'] = p.rdel('merged')
        out['rm_after'] = p.remote('merged')
        out['rm_local'] = p.local('merged')
        return out
    r = _planted(run)
    n = 0
    n += case(L, 'main', 'THE ORDERED CONTROL: `rdelete main`', 'n/a', '%s ; the remote`s main %s' % (r['main'][1][:120], r['main_after'][:8]),
              True, r['main'][0] and 'MAIN' in r['main'][1] and r['main_after'] == r['c1'])
    n += case(L, 'unmerged', 'THE ORDERED CONTROL: side at a planted sibling of c1 (%s), no ancestor of main' % r['x'][:8], 'n/a',
              '%s ; the remote`s side %s' % (r['side'][1][:140], r['side_after'][:8]), True,
              r['side'][0] and 'UNMERGED' in r['side'][1] and r['side_after'] == r['x'])
    n += case(L, 'keptname', 'THE ORDERED CONTROL: keep-x at c0, merged, named by the table, on the planted kept list', 'n/a',
              '%s ; the remote`s keep-x %s' % (r['keep'][1][:120], r['keep_after'][:8]), True,
              r['keep'][0] and 'KEPT LIST' in r['keep'][1] and r['keep_after'] == r['c0'])
    n += case(L, 'removal', 'THE ORDERED CONTROL: merged at c0, an ancestor of main, named', r['b'],
              '%s ; the remote`s merged %s ; the clone`s own merged %s' % (r['rm'][1][:150], r['rm_after'][:8] or 'ABSENT', r['rm_local'][:8]),
              r['b'][0] and 'is not one of' in r['b'][1],
              not r['rm'][0] and 'ABSENT' in r['rm'][1] and not r['rm_after'] and r['rm_local'] == r['c0'])
    n += case(L, 'unnamed', 'other at c0, merged, not named ; gone, named, absent at the remote', 'n/a',
              '%s ; the remote`s other %s ; %s' % (r['other'][1][:100], r['other_after'][:8], r['gone'][1][:90]), True,
              r['other'][0] and 'DOES NOT NAME' in r['other'][1] and r['other_after'] == r['c0'] and r['gone'][0] and 'ABSENT' in r['gone'][1])
    return L, n, 5


def control_closed():
    L = ['### (closed): AT b758, THROUGH write_route, IN A PLANTED CLONE']

    def run(p):
        return p.rdel('merged', act='b758'), p.remote('merged')
    a, m = _planted(run)
    return L, case(L, 'closed', '`rdelete merged` at b758', 'n/a', '%s ; the remote`s merged %s' % (a[1][:140], m[:8] or 'absent'),
                   True, a[0] and 'DOES NOT OPEN' in a[1] and bool(m)), 1


def control_diff():
    L = ['### (diff): THE WORKING commit.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    d = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    rem = [l[1:].strip() for l in d if l[0] == '-']
    heads = ('WRITES = (', "if argv[0] not in ('relay', 'pp') and argv[1] not in ('ff', 'pushto'):")
    ok = len(rem) == 2 and all(any(r.startswith(h) for h in heads) for r in rem)
    return L, case(L, 'diff', 'lines removed from BASE`s file', 'BASE`s file read, %d lines' % len(s0),
                   '%d removed, %d added ; the removed: %s' % (len(rem), sum(1 for l in d if l[0] == '+'), [r[:48] for r in rem]),
                   len(s0) > 1000, ok), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.2', ver == 'v1.36.3'), 1


CONTROLS = dict(table=control_table, kept=control_kept, main=control_flow, closed=control_closed, diff=control_diff, version=control_version)
ORDER = ('table', 'kept', 'main', 'closed', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    asked = ['main' if a in ('unmerged', 'keptname', 'removal', 'unnamed') else a for a in argv[1:]]
    names = [a for a in ORDER if a in asked] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.3, (R369)(4)(i): THE ROUTE THAT REMOVES A BRANCH AT A KERNEL`S REMOTE (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'the planted repositories in the system`s temporary folder, removed after each case, no path printed; written through '
           'tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (tools/standing/commit.py at %s) and after (the working file)' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, gd, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, gd, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + gd, tn + c
        per.append('(%s) %d of %d' % (k, gd, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.36.3: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1363.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
