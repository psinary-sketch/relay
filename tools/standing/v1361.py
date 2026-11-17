# -*- coding: utf-8 -*-
"""standing/v1361.py -- THE CONTROLS OF v1.36.1, (R368)(6)(ii): THE PUSH OF A NAMED COMMIT TO A NAMED NON-MAIN BRANCH, NOT FORCED, in v1360.py's form.

The ruling's words (relay data/b758_ferry.txt :19): "(ii) A push of a named commit to a named non-main branch of a kernel, not forced, refused
where the branch's remote tip is not an ancestor, read back; its control a refusal on a planted non-ancestor. It has no use in this act once
(5) lands, zq-b730 staying at 1e658870; it is built for the acts after." tools/standing/commit.py v1.36.1 adds `pushto <commit> <branch>`
(pushto_refusal, pushto_name_refusal, pushto_plan, pushto_route), opened act by act by PUSHTO_ACTS, which opens no act. BEFORE is commit.py at
BASE, executed as a module of its own; AFTER the working file. The planted cases run in scratch repositories in the system's temporary folder
(a bare repository standing for the remote, clones of it standing for the kernel), removed after; the cases that push open the route for a
planted act `bctl` by setting the working module's table for the call alone and restoring it after; no kernel, no remote and no path of the
scratch is touched or printed.

  (table)      PUSHTO_ACTS opens no act: pushto_refusal refused for both kernels at b758 and b759; a planted table opening
               SIDE-explicit-formula for bctl: None there, the relay and the other kernel refused. BEFORE: no pushto_refusal, `pushto` no write.
  (closed)     through write_route at b758 in a planted clone: refused, the remote's branch not made.
  (name)       main, master, HEAD, refs/heads/x, -f, a..b, x.lock, x/ refused; zq-b730 and push-b759-x taken.
  (new)        an absent branch: made at the commit, read back.
  (forward)    the branch's tip an ancestor of the commit: moved forward, read back.
  (equal)      the tip equal to the commit: nothing pushed.
  (nonanc)     THE ORDERED CONTROL: a planted commit that is not a descendant of the branch's remote tip: refused, NOT AN ANCESTOR, the remote's
               branch unmoved.
  (unknown)    the branch's remote tip moved by another clone and not fetched: refused, NOT IN THE CLONE, the remote's branch unmoved.
  (args)       one argument, and main as the branch: refused before anything is pushed.
  (diff)       the working commit.py against BASE's: two lines removed (WRITES, the entry's kernel test).
  (version)    tools/standing/VERSION moved to v1.36.1.

  python -X utf8 -u tools/standing/v1361.py control [table|closed|name|new|nonanc|unknown|args|diff|version ...] [--bank]
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
BASE = 'fd45f4c5'   # ### the relay's HEAD before this change (b758 component 4, step 25, v1.36.0)
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
PREFIX = 'v1361_'


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
        return False, str(fn())[:200]
    except SystemExit as e:
        return True, str(e)[:200]
    except Exception as e:  # noqa: BLE001
        if type(e).__name__ == 'Refused':
            return True, str(e)[:200]
        raise


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0:
        raise RuntimeError('the planted repository`s git %s exit %d: %s' % (a[0], r.returncode, (r.stderr or r.stdout).strip()[:160]))
    return r.stdout.strip()


class Planted(object):
    """a bare repository standing for a kernel's remote with main at c0, and a clone of it standing for the kernel; removed by close()."""

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
        g(w, 'push', '-q', 'origin', 'main')
        self.k = self.clone('k')

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

    def push(self, args, act=CTL, mod=None, repo=None):
        m = mod or C1
        saved = getattr(m, 'PUSHTO_ACTS', None)
        if act == CTL and saved is not None:
            m.PUSHTO_ACTS = {CTL: (EF,)}
        try:
            return trial(lambda: m.write_route(EF, 'pushto', list(args), act=act, repo=repo or self.k, mark_path=self.mark))
        finally:
            if saved is not None:
                m.PUSHTO_ACTS = saved

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
    L = ['### (table): THE ROUTE OPENED ACT BY ACT BY PUSHTO_ACTS, WHICH OPENS NO ACT']
    b0 = base()
    before = 'pushto_refusal %s ; pushto among the writes %s' % ('present' if hasattr(b0, 'pushto_refusal') else 'absent', 'pushto' in b0.WRITES)
    real = [C1.pushto_refusal(k, a) for k, a in ((EF, 'b758'), (M24, 'b758'), (EF, 'b759'))]
    pl = {CTL: (EF,)}
    planted = [C1.pushto_refusal(k, CTL, table=pl) for k in (EF, 'relay', M24)]
    after = 'PUSHTO_ACTS %r ; at b758/b759 refused %s ; the planted table: %s' % (C1.PUSHTO_ACTS, [r is not None for r in real], [_r(x)[:40] for x in planted])
    return L, case(L, 'table', 'pushto_refusal at the real table and at a planted one', before, after,
                   not hasattr(b0, 'pushto_refusal') and 'pushto' not in b0.WRITES,
                   C1.PUSHTO_ACTS == {} and all(r is not None for r in real) and planted[0] is None and planted[1] is not None
                   and planted[2] is not None and 'pushto' in C1.WRITES), 1


def control_closed():
    L = ['### (closed): AT b758, THROUGH write_route, IN A PLANTED CLONE']

    def run(p):
        b = p.push([p.c0, 'side'], act='b758', mod=base())
        a = p.push([p.c0, 'side'], act='b758')
        return b, a, p.remote('side')
    b, a, side = _planted(run)
    return L, case(L, 'closed', '`pushto <c0> side` at b758', b, '%s ; the remote`s side %s' % (a, side[:8] or 'absent'),
                   b[0] and 'is not one of' in b[1], a[0] and 'DOES NOT OPEN' in a[1] and not side), 1


def control_name():
    L = ['### (name): THE BRANCH FORM']
    bad = ['main', 'master', 'HEAD', 'Main', 'refs/heads/x', '-f', 'a..b', 'x.lock', 'x/', 'a b']
    good = ['zq-b730', 'push-b759-x', 'w/x.1']
    rb = [C1.pushto_name_refusal(n) is not None for n in bad]
    rg = [C1.pushto_name_refusal(n) is None for n in good]
    return L, case(L, 'name', 'refused %s ; taken %s' % (bad, good), 'n/a (the route absent at BASE)', (rb, rg), True, all(rb) and all(rg)), 1


def control_flow():
    L = ['### (new), (forward), (equal), (nonanc): ONE PLANTED REMOTE, THE BRANCH side']

    def run(p):
        k = p.k
        b = p.push([p.c0, 'side'], mod=base())
        new = p.push([p.c0, 'side'])
        s1 = p.remote('side')
        c1 = p.put(k, {'A.lean': 'x1\n'}, 'c1')
        fw = p.push([c1, 'side'])
        s2 = p.remote('side')
        eq = p.push([c1, 'side'])
        s3 = p.remote('side')
        g(k, 'checkout', '-q', '-b', 'other', p.c0)
        x = p.put(k, {'B.lean': 'sibling\n'}, 'a sibling of c1, not its descendant')
        na = p.push([x, 'side'])
        s4 = p.remote('side')
        return dict(c0=p.c0, c1=c1, x=x, b=b, new=new, s1=s1, fw=fw, s2=s2, eq=eq, s3=s3, na=na, s4=s4)
    r = _planted(run)
    n = 0
    n += case(L, 'new', 'the branch side absent at the remote, `pushto <c0> side`', r['b'], '%s ; the remote`s side %s' % (r['new'][1][:140], r['s1'][:8]),
              r['b'][0], not r['new'][0] and r['s1'] == r['c0'] and 'the branch made' in r['new'][1])
    n += case(L, 'forward', 'side at c0, `pushto <c1> side`, c1 a child of c0', 'n/a', '%s ; the remote`s side %s' % (r['fw'][1][:140], r['s2'][:8]),
              True, not r['fw'][0] and r['s2'] == r['c1'] and 'moved forward' in r['fw'][1])
    n += case(L, 'equal', 'side at c1, `pushto <c1> side` again', 'n/a', '%s ; the remote`s side %s' % (r['eq'][1][:120], r['s3'][:8]),
              True, not r['eq'][0] and 'ALREADY' in r['eq'][1] and r['s3'] == r['c1'])
    n += case(L, 'nonanc', 'THE ORDERED CONTROL: side at c1, `pushto <x> side`, x a planted sibling of c1 (%s)' % r['x'][:8], 'n/a',
              '%s ; the remote`s side %s' % (r['na'][1][:150], r['s4'][:8]), True,
              r['na'][0] and 'NOT AN ANCESTOR' in r['na'][1] and r['s4'] == r['c1'])
    return L, n, 4


def control_unknown():
    L = ['### (unknown): THE REMOTE TIP MOVED BY ANOTHER CLONE, NOT FETCHED']

    def run(p):
        g(p.k, 'push', '-q', 'origin', '%s:refs/heads/side' % p.c0)
        g(p.k, 'fetch', '-q', 'origin')
        k2 = p.clone('k2')
        y = p.put(k2, {'C.lean': 'y\n'}, 'y')
        g(k2, 'push', '-q', 'origin', '%s:refs/heads/side' % y)
        a = p.push([p.c0, 'side'])
        return y, a, p.remote('side')
    y, a, side = _planted(run)
    return L, case(L, 'unknown', 'side moved to %s by another clone, the clone not fetched' % y[:8], 'n/a',
                   '%s ; the remote`s side %s' % (a[1][:150], side[:8]), True, a[0] and 'NOT IN THE CLONE' in a[1] and side == y), 1


def control_args():
    L = ['### (args): ONE ARGUMENT, AND main AS THE BRANCH']

    def run(p):
        return p.push([p.c0]), p.push([p.c0, 'main']), p.remote('main')
    x, y, m = _planted(run)
    return L, case(L, 'args', '`pushto <c0>` and `pushto <c0> main`', 'n/a', [x, y], True,
                   x[0] and 'NAMES ITS COMMIT AND ITS BRANCH' in x[1] and y[0] and 'NOT A NON-MAIN BRANCH NAME' in y[1]), 1


def control_diff():
    L = ['### (diff): THE WORKING commit.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    d = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    rem = [l[1:].strip() for l in d if l[0] == '-']
    heads = ('WRITES = (', "if argv[0] not in ('relay', 'pp') and argv[1] != 'ff':")
    ok = len(rem) == 2 and all(any(r.startswith(h) for h in heads) for r in rem)
    return L, case(L, 'diff', 'lines removed from BASE`s file', 'BASE`s file read, %d lines' % len(s0),
                   '%d removed, %d added ; the removed: %s' % (len(rem), sum(1 for l in d if l[0] == '+'), [r[:48] for r in rem]),
                   len(s0) > 1000, ok), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.0', ver == 'v1.36.1'), 1


CONTROLS = dict(table=control_table, closed=control_closed, name=control_name, new=control_flow, unknown=control_unknown,
                args=control_args, diff=control_diff, version=control_version)
ORDER = ('table', 'closed', 'name', 'new', 'unknown', 'args', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    asked = ['new' if a in ('forward', 'equal', 'nonanc') else a for a in argv[1:]]
    names = [a for a in ORDER if a in asked] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.1, (R368)(6)(ii): THE PUSH OF A NAMED COMMIT TO A NAMED NON-MAIN BRANCH, NOT FORCED (%s)' % (
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
    out.append('### ### **v1.36.1: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1361.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
