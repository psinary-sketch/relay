# -*- coding: utf-8 -*-
"""asof.py -- THE SUITE'S AS-OF COMMIT, (R178)(2)(ii), written at b568.

### ### **THE RULING.** *A sealed face is a statement about the tree at its closing push. The suite gains an as-of commit:
### each arm that reads the relay tree reads it at the commit named in the face's closing push-out bank, not at HEAD.*
### ### **THE OCCASION.** b566's suite, re-run after b567 closed, failed G-NUMBER-UNCLAIMED (it globbed the live data
### directory for a successor's registration) and, after b567's appended lines, G-PRIORBANK-UNCHANGED (it compared the
### live prior banks with origin/main): each compared a sealed face against the tree as it stands.
### ### **WHAT THIS MODULE GIVES A SUITE.** `relay_asof(root, data, act)`: the relay commit a face's closing push-out bank
### names -- the `tip` of the `push_gated: repo ...` line, accepted only when the bank's `main read back at the remote`
### line names the same SHA and the commit exists locally; `None` when the bank is absent (the act's own closing run, before
### its push) or does not read back equal, and the suite then reads live, as before. `names_at`, `blob_at` and `ids_at`
### read the tree at that commit. `from_argv` lets a test point a suite at another commit (`--as-of <sha>`), which is how
### the test shows a claim false at a commit still fails. ### **SCOPE, AS THE FERRY GIVES IT: THE TREE-READING ARMS.** An
### arm that reads a named bank's content (an addendum line a later ruling appended) is not re-pointed by this module.
"""
import os
import re
import subprocess

TIP = re.compile(r'^push_gated: repo .* ; branch (\S+) ; tip ([0-9a-f]{40}) ;', re.M)
BACK = re.compile(r'^push_gated: main read back at the remote: ([0-9a-f]{40})\s*$', re.M)


def _git(root, *a):
    r = subprocess.run(['git', '-C', root] + list(a), capture_output=True)
    return r.returncode, r.stdout


def parse_pushout(text):
    """### RETURN the SHA when the bank's tip and its read-back agree, else None."""
    t, b = TIP.findall(text or ''), BACK.findall(text or '')
    if len(t) == 1 and len(b) == 1 and t[0][1] == b[0]:
        return b[0]
    return None


def relay_asof(root, data, act):
    p = os.path.join(data, '%s_closing_push_out.txt' % act)
    if not os.path.isfile(p):
        return None
    sha = parse_pushout(open(p, 'rb').read().decode('utf-8', 'replace').replace('\r', ''))
    if sha and _git(root, 'cat-file', '-e', sha + '^{commit}')[0] == 0:
        return sha
    return None


def from_argv(argv, default):
    """### `--as-of <sha>` on the command line, else the bank's commit."""
    if '--as-of' in argv:
        return argv[argv.index('--as-of') + 1]
    return default


def names_at(root, rev, prefix):
    """### the paths under `prefix` (a directory, no trailing slash) in the tree at `rev`, relative to it."""
    rc, out = _git(root, 'ls-tree', '-r', '--name-only', rev, '--', prefix + '/')
    if rc:
        return []
    n = len(prefix) + 1
    return [x[n:] for x in out.decode('utf-8', 'replace').split('\n') if x.strip()]


def blob_at(root, rev, path):
    rc, out = _git(root, 'show', '%s:%s' % (rev, path))
    return None if rc else out


def ids_at(root, rev, prefix):
    """### {path: blob id} under `prefix` at `rev`."""
    rc, out = _git(root, 'ls-tree', '-r', rev, '--', prefix + '/')
    res = {}
    if rc:
        return res
    for line in out.decode('utf-8', 'replace').split('\n'):
        if '\t' in line:
            meta, path = line.split('\t', 1)
            res[path] = meta.split()[2]
    return res


def self_test():
    """### the parser on synthetic banks, both polarities."""
    a, b = '1' * 40, '2' * 40
    ok = parse_pushout('push_gated: repo /d/relay ; branch push-x ; tip %s ; checkout before main\n'
                       'push_gated: main read back at the remote: %s\n' % (a, a)) == a
    ok = ok and parse_pushout('push_gated: repo /d/relay ; branch push-x ; tip %s ; checkout before main\n'
                              'push_gated: main read back at the remote: %s\n' % (a, b)) is None
    ok = ok and parse_pushout('push_gated: main read back at the remote: %s\n' % a) is None
    ok = ok and parse_pushout('') is None
    return ok
