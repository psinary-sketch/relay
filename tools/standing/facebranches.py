# -*- coding: utf-8 -*-
"""standing/facebranches.py -- v1.24.0, (R354)(2)(v)-(vi), b743 events (10), (11): THE FACE'S BRANCH LIST AND THE KERNEL PUSH BEFORE THE ROOT.

(v) A push-* branch the act makes on a kernel is made by this tool, which enters it in the face's branch list, data/<act>_face_branches.json
(appended by design after the lock, outside the LOCKED rule, standing.hook.lock_exempt), so G-KERNELS-UNTOUCHED reads the act's own branches as
the act's: the arm's kernels-now has the listed branches taken out before it is compared with the face (fold/checks.tpl kernels_untouched).
b743's seat made push-b743-sitting by hand at its root and the arm failed on it (events (11)); N5 fell on the same branch.
(vi) Where the list names a kernel write, the kernel push is ordered before the root and the order printed: `order` reads each listed kernel's
main against its remote (one remote read per kernel, one kernel per call where the seat sends them) and prints the push before `record root`.
b743's `record root` refused on SIDE-explicit-formula's main ahead of its remote and the push was moved before it (events (10)).
Written at b744 by the Write tool.

  python -X utf8 -u tools/standing/facebranches.py make <kernel> <branch> <sha>   the branch made and listed, one git write
  python -X utf8 -u tools/standing/facebranches.py list                           the list printed
  python -X utf8 -u tools/standing/facebranches.py order <kernel>                 the kernel's main against its remote, the order printed
"""
import json
import os
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(os.path.dirname(S))
D = os.path.join(RELAY, 'data')
NL = '\n'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def _git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def _act():
    with open(os.path.join(D, 'act_current.json'), encoding='utf-8') as f:
        return json.load(f)['act']


def path(act):
    return os.path.join(D, '%s_face_branches.json' % act)


def listed(act, data=None):
    """[{kernel, branch, sha, at}] -- the act's list, empty where none was made."""
    p = os.path.join(data or D, '%s_face_branches.json' % act)
    if not os.path.exists(p):
        return []
    with open(p, encoding='utf-8') as f:
        return json.load(f).get('branches') or []


def strip(kern_now, rows):
    """the arm's kernels-now with each listed branch taken out of its kernel's branch list (the third field); pure."""
    out = {}
    for k, v in (kern_now or {}).items():
        drop = set(r['branch'] for r in rows if r.get('kernel') == k)
        out[k] = [v[0], v[1], sorted(b for b in v[2] if b not in drop)] + list(v[3:]) if drop and isinstance(v, (list, tuple)) and len(v) > 2 else v
    return out


def make(act, kernel, branch, sha):
    if not branch.startswith('push-%s-' % act):
        raise SystemExit('facebranches: the branch %r is not the act`s push-%s-* form' % (branch, act))
    repo = 'D:/' + kernel
    r = _git(repo, 'branch', branch, sha)
    if r.returncode != 0:
        raise SystemExit('facebranches: git branch exit %d: %s -- NOTHING LISTED' % (r.returncode, (r.stderr or r.stdout).strip()[:200]))
    full = _git(repo, 'rev-parse', branch).stdout.strip()
    rows = listed(act) + [dict(kernel=kernel, branch=branch, sha=full, at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))]
    s = json.dumps(dict(act=act, branches=rows), indent=1) + NL
    with open(path(act) + '.tmp', 'wb') as f:
        f.write(s.encode('utf-8'))
    os.replace(path(act) + '.tmp', path(act))
    return rows[-1]


def order(rows, kernel, local_main, remote_main):
    """(vi): the lines of the order for one kernel, pure: where the list names a branch on the kernel and its main is ahead of the remote's,
    the push before the root; else nothing to order."""
    mine = [r for r in rows if r.get('kernel') == kernel]
    if not mine:
        return False, ['  %s: no branch of the act listed; nothing ordered before the root' % kernel]
    if local_main and remote_main and local_main != remote_main:
        return True, ['  THE ORDER ((R354)(2)(vi)): 1. push %s %s (main %s, the remote %s) ; 2. read the remote back ; 3. `record root`' % (
            kernel, mine[-1]['branch'], local_main[:8], remote_main[:8])]
    return False, ['  %s: main %s level with its remote; the root waits on nothing here' % (kernel, (local_main or '')[:8])]


def main(argv):
    act = _act()
    if argv[:1] == ['make'] and len(argv) == 4:
        r = make(act, argv[1], argv[2], argv[3])
        print('  made and listed: %s %s at %s (data/%s_face_branches.json)' % (r['kernel'], r['branch'], r['sha'][:8], act))
        return 0
    if argv[:1] == ['list']:
        for r in listed(act):
            print('  %s %s %s %s' % (r['kernel'], r['branch'], r['sha'][:8], r['at']))
        return 0
    if argv[:1] == ['order'] and len(argv) == 2:
        repo = 'D:/' + argv[1]
        loc = _git(repo, 'rev-parse', 'main').stdout.strip()
        rem = (_git(repo, 'ls-remote', 'origin', 'refs/heads/main').stdout.split() or [''])[0]
        need, L = order(listed(act), argv[1], loc, rem)
        print(NL.join(L))
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
