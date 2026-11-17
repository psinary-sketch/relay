# -*- coding: utf-8 -*-
"""standing/v1360.py -- THE CONTROLS OF v1.36.0, (R368)(6)(i): THE FAST-FORWARD OF A KERNEL'S LOCAL MAIN, in v1359.py's form.

The ruling's words (relay data/b758_ferry.txt :19): "(i) A fast-forward of a kernel's local main to its remote's main, refused where the
local main is not an ancestor of the remote's, read back; its control a refusal on a planted divergent main in a scratch clone; its use here:
SIDE-dirichlet-mod-24's local main, which stands at 597b0869 beside the remote's e5ebdd15, and SIDE-explicit-formula's after each of (4) and
(5)." tools/standing/commit.py v1.36.0 adds `ff main` (ff_refusal, remote_head, ff_plan, ff_route), opened act by act by FF_ACTS apart from
KERNEL_ACTS. BEFORE is commit.py at BASE, executed as a module of its own; AFTER the working file. The planted cases run in scratch
repositories in the system's temporary folder (a bare repository standing for the remote, clones of it standing for the kernel), removed
after; no kernel, no remote and no path of the scratch is touched or printed.

  (table)      ff_refusal: SIDE-dirichlet-mod-24 and SIDE-explicit-formula for b758 None; the relay, PLACE-papers, a third repository, b757
               and b759 refused. BEFORE: no ff_refusal, and `ff` not among the writes.
  (closed)     SIDE-dirichlet-mod-24 for b758 stays closed to every other write: repo_refusal refused, and an `add` in a planted clone refused.
  (out)        a planted clone, a side branch checked out, the remote's main one commit ahead and fetched: BEFORE refused (not a write);
               AFTER main moved by update-ref to the remote's, read back; HEAD and its branch unmoved.
  (equal)      the same clone again: nothing written, main unmoved.
  (in)         a planted clone with main checked out on a clean tree, the remote one commit ahead and fetched: merge --ff-only; HEAD at
               the remote's main, the file's text the remote's.
  (divergent)  THE ORDERED CONTROL: a planted clone whose main carries a commit the remote lacks, the remote ahead and fetched: refused,
               NOT AN ANCESTOR, main unmoved.
  (absent)     a planted clone that has not fetched the remote's new main: refused, NOT IN THE CLONE, main unmoved.
  (args)       `ff side` and `ff main extra` refused before anything is read.
  (diff)       the working commit.py against BASE's: three lines removed (WRITES, the kernel test in write_route, the entry's kernel test).
  (version)    tools/standing/VERSION moved to v1.36.0.

  python -X utf8 -u tools/standing/v1360.py control [table|closed|out|equal|in|divergent|absent|args|diff|version ...] [--bank]
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
BASE = 'f8b607a5'   # ### the relay's HEAD before this change (b758 component 2, step 24)
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
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
PREFIX = 'v1360_'


def base():
    """commit.py at BASE, executed as a module of its own (its __main__ guard keeps main() unrun)."""
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
    """(refused, the message) for a call that may raise either module's Refused or SystemExit; any other exception is raised on."""
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
    """a bare repository standing for a kernel's remote, a work clone that advances it, and clones standing for the kernel; the relay's
    identity in each one's own config; its own write mark. Removed by close(), its root verified first."""

    def __init__(self):
        self.root = tempfile.mkdtemp(prefix=PREFIX)
        self.bare = os.path.join(self.root, 'r.git')
        self.w = os.path.join(self.root, 'w')
        self.mark = os.path.join(self.root, 'mark.json')
        self.id = C1._identity(RELAY)
        g(self.root, 'init', '-q', '--bare', '-b', 'main', self.bare)
        os.mkdir(self.w)
        g(self.w, 'init', '-q', '-b', 'main')
        self._config(self.w)
        g(self.w, 'remote', 'add', 'origin', self.bare)
        self.c0 = self.put(self.w, {'A.lean': 'x0\n'}, 'c0')
        g(self.w, 'push', '-q', 'origin', 'main')

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
        g(self.root, 'clone', '-q', '-c', 'core.autocrlf=false', self.bare, p)   # ### set at the checkout: set after it, the global autocrlf leaves the tree read as changed
        self._config(p)
        return p

    def advance(self, text, msg):
        c = self.put(self.w, {'A.lean': text}, msg)
        g(self.w, 'push', '-q', 'origin', 'main')
        return c

    def ff(self, repo, args=('main',), mod=None, act='b758', key=M24):
        m = mod or C1
        return trial(lambda: m.write_route(key, 'ff', list(args), act=act, repo=repo, mark_path=self.mark))

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


def main_of(repo):
    return g(repo, 'rev-parse', 'refs/heads/main')


def control_table():
    L = ['### (table): THE ROUTE OPENED ACT BY ACT BY FF_ACTS']
    b0 = base()
    before = 'ff_refusal %s ; ff among the writes %s' % ('present' if hasattr(b0, 'ff_refusal') else 'absent', 'ff' in b0.WRITES)
    want_none = [(M24, 'b758'), (EF, 'b758')]
    want_ref = [('relay', 'b758'), ('pp', 'b758'), ('SIDE-lv-conservation', 'b758'), (EF, 'b757'), (M24, 'b757'), (M24, 'b759')]
    a_none = [C1.ff_refusal(k, a) for k, a in want_none]
    a_ref = [C1.ff_refusal(k, a) for k, a in want_ref]
    after = 'None for %s ; refused for %s' % (['%s/%s' % x for x, r in zip(want_none, a_none) if r is None],
                                              ['%s/%s' % x for x, r in zip(want_ref, a_ref) if r is not None])
    return L, case(L, 'table', 'ff_refusal over eight (repository, act) pairs', before, after,
                   not hasattr(b0, 'ff_refusal') and 'ff' not in b0.WRITES,
                   all(r is None for r in a_none) and all(r is not None for r in a_ref) and 'ff' in C1.WRITES), 1


def control_closed():
    L = ['### (closed): SIDE-dirichlet-mod-24 FOR b758 CLOSED TO EVERY OTHER WRITE']

    def run(p):
        k = p.clone('k0')
        b = trial(lambda: base().write_route(M24, 'add', ['A.lean'], act='b758', repo=k, mark_path=p.mark))
        a = trial(lambda: C1.write_route(M24, 'add', ['A.lean'], act='b758', repo=k, mark_path=p.mark))
        return b, a, C1.repo_refusal(M24, 'b758')
    b, a, rr = _planted(run)
    return L, case(L, 'closed', 'an `add` in a planted clone named SIDE-dirichlet-mod-24 for b758 ; repo_refusal after', b, (a, _r(rr)),
                   b[0], a[0] and rr is not None and 'DOES NOT OPEN' in a[1]), 1


def control_out_equal():
    L = ['### (out) AND (equal): MAIN NOT CHECKED OUT, MOVED BY update-ref; THEN NOTHING TO WRITE']

    def run(p):
        k = p.clone('k1')
        g(k, 'checkout', '-q', '-b', 'side')
        c1 = p.advance('x1\n', 'c1')
        g(k, 'fetch', '-q', 'origin')
        head0, m0 = g(k, 'rev-parse', 'HEAD'), main_of(k)
        b = p.ff(k, mod=base())
        a = p.ff(k)
        m1, head1, br1 = main_of(k), g(k, 'rev-parse', 'HEAD'), g(k, 'symbolic-ref', '--short', 'HEAD')
        e = p.ff(k)
        m2 = main_of(k)
        return dict(c0=p.c0, c1=c1, m0=m0, b=b, a=a, m1=m1, head0=head0, head1=head1, br1=br1, e=e, m2=m2)
    r = _planted(run)
    g1 = case(L, 'out', 'a side branch checked out, main %s, the remote`s main %s fetched' % (r['m0'][:8], r['c1'][:8]),
              r['b'], '%s ; main %s ; HEAD %s on %s' % (r['a'][1][:150], r['m1'][:8], r['head1'][:8], r['br1']),
              r['b'][0] and 'is not one of' in r['b'][1],
              not r['a'][0] and r['m1'] == r['c1'] and r['head1'] == r['head0'] == r['c0'] and r['br1'] == 'side' and 'update-ref' in r['a'][1])
    g2 = case(L, 'equal', 'the same clone, ff again', 'n/a (the route absent at BASE)', '%s ; main %s' % (r['e'][1][:120], r['m2'][:8]),
              True, not r['e'][0] and 'ALREADY' in r['e'][1] and r['m2'] == r['c1'])
    return L, g1 + g2, 2


def control_in():
    L = ['### (in): MAIN CHECKED OUT ON A CLEAN TREE, MOVED BY merge --ff-only']

    def run(p):
        k = p.clone('k2')
        c1 = p.advance('x1\n', 'c1')
        g(k, 'fetch', '-q', 'origin')
        a = p.ff(k)
        txt = io.open(os.path.join(k, 'A.lean'), encoding='utf-8').read()
        return c1, a, g(k, 'rev-parse', 'HEAD'), main_of(k), txt, g(k, 'status', '--porcelain', '--untracked-files=no')
    c1, a, head, m, txt, st = _planted(run)
    return L, case(L, 'in', 'main checked out, the remote`s main %s fetched' % c1[:8], 'n/a (the route absent at BASE)',
                   '%s ; HEAD %s ; main %s ; the file %r ; tracked changes %d' % (a[1][:120], head[:8], m[:8], txt, len([l for l in st.split(NL) if l])),
                   True, not a[0] and head == m == c1 and txt == 'x1\n' and not st and 'merge --ff-only' in a[1]), 1


def control_divergent():
    L = ['### (divergent): THE ORDERED CONTROL, A PLANTED DIVERGENT MAIN']

    def run(p):
        k = p.clone('k3')
        d = p.put(k, {'B.lean': 'local\n'}, 'a local commit the remote lacks')
        c1 = p.advance('x1\n', 'c1')
        g(k, 'fetch', '-q', 'origin')
        b = p.ff(k, mod=base())
        a = p.ff(k)
        return d, c1, b, a, main_of(k), g(k, 'rev-parse', 'refs/remotes/origin/main')
    d, c1, b, a, m, tr = _planted(run)
    return L, case(L, 'divergent', 'main %s carrying a commit the remote lacks ; the remote`s main %s fetched (tracking %s)' % (d[:8], c1[:8], tr[:8]),
                   b, '%s ; main %s' % (a[1][:150], m[:8]), b[0], a[0] and 'NOT AN ANCESTOR' in a[1] and m == d), 1


def control_absent():
    L = ['### (absent): THE REMOTE`S NEW MAIN NOT IN THE CLONE']

    def run(p):
        k = p.clone('k4')
        c1 = p.advance('x1\n', 'c1')
        a = p.ff(k)
        return c1, a, main_of(k)
    c1, a, m = _planted(run)
    return L, case(L, 'absent', 'the remote`s main %s, not fetched ; main %s' % (c1[:8], m[:8]), 'n/a (the route absent at BASE)',
                   '%s ; main %s' % (a[1][:150], m[:8]), True, a[0] and 'NOT IN THE CLONE' in a[1] and m != c1), 1


def control_args():
    L = ['### (args): THE ROUTE TAKES main ALONE']

    def run(p):
        k = p.clone('k5')
        return p.ff(k, args=('side',)), p.ff(k, args=('main', 'extra'))
    x, y = _planted(run)
    return L, case(L, 'args', '`ff side` and `ff main extra`', 'n/a (the route absent at BASE)', [x, y], True,
                   x[0] and y[0] and 'main ALONE' in x[1] and 'main ALONE' in y[1]), 1


def control_diff():
    L = ['### (diff): THE WORKING commit.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    d = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    rem = [l[1:].strip() for l in d if l[0] == '-']
    heads = ('WRITES = (', 'if kern:', "if argv[0] not in ('relay', 'pp'):")
    ok = len(rem) == 3 and all(any(r.startswith(h) for h in heads) for r in rem)
    return L, case(L, 'diff', 'lines removed from BASE`s file', 'BASE`s file read, %d lines' % len(s0),
                   '%d removed, %d added ; the removed: %s' % (len(rem), sum(1 for l in d if l[0] == '+'), [r[:40] for r in rem]),
                   len(s0) > 900, ok), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.9', ver == 'v1.36.0'), 1


CONTROLS = dict(table=control_table, closed=control_closed, out=control_out_equal, equal=control_out_equal, **{'in': control_in},
                divergent=control_divergent, absent=control_absent, args=control_args, diff=control_diff, version=control_version)
ORDER = ('table', 'closed', 'out', 'in', 'divergent', 'absent', 'args', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    asked = ['out' if a == 'equal' else a for a in argv[1:]]
    names = [a for a in ORDER if a in asked] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.0, (R368)(6)(i): THE FAST-FORWARD OF A KERNEL`S LOCAL MAIN (%s)' % (
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
    out.append('### ### **v1.36.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1360.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
