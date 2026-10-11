# -*- coding: utf-8 -*-
"""test_no_sorry_main.py -- THE PLANTED TEST OF tools/no_sorry_main.py, under (R259)(2)(a).

### A scratch copy of one kernel (a local clone of SIDE-archimedean's main into the system's temp directory, never a repository of the
### corpus): (1) as it stands the arm PASSES; (2) with one `sorry` inserted in a lean_lib file and committed to the copy's main the arm FAILS
### and names that file and line; (3) the same `sorry` inside a comment and a string, the arm PASSES; (4) the `sorry` on a branch
### sorry-quarantine-* with main clean, the arm PASSES (a quarantine branch is not main); (5) the copy's main ahead of what the remote
### reads, the arm FAILS on the unequal pair. The remote is the copy's own refs, given to the tool -- no network read. The commits carry a
### test identity, never the author's.
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import no_sorry_main as N   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ENV = dict(os.environ, GIT_AUTHOR_NAME='planted-test', GIT_AUTHOR_EMAIL='planted@test.invalid', GIT_COMMITTER_NAME='planted-test',
           GIT_COMMITTER_EMAIL='planted@test.invalid')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, env=ENV)


def head(repo):
    return git(repo, 'rev-parse', 'HEAD').stdout.strip()


def main():
    tmp = tempfile.mkdtemp(prefix='b649_nsm_')
    cp = os.path.join(tmp, 'SIDE-archimedean')
    subprocess.run(['git', 'clone', '-q', '--no-hardlinks', 'D:/SIDE-archimedean', cp], capture_output=True, env=ENV)
    git(cp, 'checkout', '-q', 'main')
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-96s %s' % (label, 'PASS' if cond else '### FAIL'))

    same = lambda p: {'refs/heads/main': head(p)}   # noqa: E731
    r = N.scan_kernel(cp, same)
    files = N.lib_files([x for x in git(cp, 'ls-tree', '-r', '--name-only', 'main').stdout.split('\n') if x], lambda f: open(os.path.join(cp, f), encoding='utf-8').read(),
                        open(os.path.join(cp, 'lakefile.lean'), encoding='utf-8').read())
    want('(1) the copy as it stands: the arm PASSES (files %d, hits %d, pair equal %s)' % (r['files'], len(r['hits']), r['equal']),
         r['equal'] and not r['hits'] and r['files'] > 0)
    target = files[-1]
    p = os.path.join(cp, target)
    orig = open(p, encoding='utf-8', newline='').read()
    open(p, 'w', encoding='utf-8', newline='').write(orig + '\ntheorem planted_b649 : 1 = 2 := by\n  sorry\n')
    git(cp, 'commit', '-q', '-am', 'planted sorry')
    r = N.scan_kernel(cp, same)
    n_lines = len((orig + '\ntheorem planted_b649 : 1 = 2 := by\n  sorry\n').split('\n'))
    want('(2) one sorry inserted in %s: the arm FAILS and names the file and line (%s)' % (target, r['hits']),
         r['hits'] == [(target, n_lines - 1, 'sorry')])
    open(p, 'w', encoding='utf-8', newline='').write(orig + '\n-- sorry in a comment\n/- sorry in a block -/\ndef planted_s := "sorry"\n')
    git(cp, 'commit', '-q', '-am', 'sorry in a comment and a string')
    r = N.scan_kernel(cp, same)
    want('(3) the word in a comment, a block and a string: the arm PASSES (hits %d)' % len(r['hits']), r['equal'] and not r['hits'])
    git(cp, 'checkout', '-q', '-b', 'sorry-quarantine-planted')
    open(p, 'w', encoding='utf-8', newline='').write(orig + '\ntheorem planted_q : 1 = 2 := by\n  sorry\n')
    git(cp, 'commit', '-q', '-am', 'quarantined sorry')
    git(cp, 'checkout', '-q', 'main')
    r = N.scan_kernel(cp, same)
    want('(4) the sorry on a branch sorry-quarantine-*, main clean: the arm PASSES (hits %d)' % len(r['hits']), r['equal'] and not r['hits'])
    stale = {'refs/heads/main': git(cp, 'rev-parse', 'HEAD~1').stdout.strip()}
    r = N.scan_kernel(cp, lambda _p: stale)
    want('(5) the remote reading an older main than the clone: the arm FAILS on the unequal pair (equal %s)' % r['equal'], not r['equal'])
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
