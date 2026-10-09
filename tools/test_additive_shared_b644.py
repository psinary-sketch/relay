# -*- coding: utf-8 -*-
"""test_additive_shared_b644.py -- THE TEST OF THE ADDITIVE ARM, tools/additive_shared.py, (R254)(2), written at b644.

### Every case runs in a fresh temporary git clone standing in for relay (relay's `* text=auto eol=lf`), a shared file committed, then
### changed and committed again, and the arm's check read over that pair; nothing in relay is written.
###   (1) an entry appended at the end reads ADDITIVE;
###   (2) a dated line inserted beneath an entry in the middle reads ADDITIVE;
###   (3) a line of the older text changed reads NOT ADDITIVE ('replace');
###   (4) a line of the older text removed reads NOT ADDITIVE ('delete');
###   (5) the working file against HEAD: an uncommitted changed line reads NOT ADDITIVE, an uncommitted append ADDITIVE;
###   (6) a file named by two roots' items is a shared file; one named by one root is not.
### Usage: python tools/test_additive_shared_b644.py
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import additive_shared as A   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = b'alpha\tthe first\tsrc\nbeta\tthe second\tsrc\ngamma\tthe third\tsrc\n'


def git(d, *a):
    return subprocess.run(['git', '-C', d] + list(a), capture_output=True, text=True).stdout.strip()


def stage(second):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'data'))
    subprocess.run(['git', 'init', '-q', '-b', 'main', d], capture_output=True)
    git(d, 'config', 'user.email', 'test@example.invalid')
    git(d, 'config', 'user.name', 'test')
    open(os.path.join(d, '.gitattributes'), 'wb').write(b'* text=auto eol=lf\n')
    p = os.path.join(d, 'data', 'glossary.txt')
    for body in (BASE, second):
        open(p, 'wb').write(body)
        git(d, 'add', '-A')
        git(d, 'commit', '-q', '-m', 'step')
    return d


def verdict(d, worktree=False):
    save = A.ROOT
    A.ROOT = d
    try:
        return A.check(worktree=worktree, files=['data/glossary.txt'])
    finally:
        A.ROOT = save


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  (%d) %-118s %s' % (len(res), label, 'PASS' if cond else '### FAIL'))

    r = verdict(stage(BASE + b'delta\tthe fourth\tsrc\n'))
    want('an entry appended at the end reads ADDITIVE (read %s)' % r, r[0][2] == [])
    r = verdict(stage(BASE.replace(b'beta\tthe second\tsrc\n', b'beta\tthe second\tsrc\n# 2026-10-09: beta superseded by the entry below\n')))
    want('a dated line inserted beneath an entry in the middle reads ADDITIVE (read %s)' % r, r[0][2] == [])
    r = verdict(stage(BASE.replace(b'the second', b'the second, edited')))
    want('a line of the older text changed reads NOT ADDITIVE (read %s)' % r, [t for t, _l in r[0][2]] == ['replace'])
    r = verdict(stage(BASE.replace(b'beta\tthe second\tsrc\n', b'')))
    want('a line of the older text removed reads NOT ADDITIVE (read %s)' % r, [t for t, _l in r[0][2]] == ['delete'])
    d = stage(BASE)
    p = os.path.join(d, 'data', 'glossary.txt')
    open(p, 'wb').write(BASE.replace(b'the third', b'the third, edited'))
    w1 = verdict(d, worktree=True)[-1]
    open(p, 'wb').write(BASE + b'delta\tthe fourth\tsrc\n')
    w2 = verdict(d, worktree=True)[-1]
    want('the working file against HEAD: a changed line NOT ADDITIVE (%s), an append ADDITIVE (%s)' % (w1[2], w2[2]), w1[2] and not w2[2])
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'data'))
    for act, items in (('t1', ['data/x.txt aa', 'data/once.txt bb']), ('t2', ['data/x.txt aa', 'relay cc'])):
        json.dump(dict(items=items), open(os.path.join(d, 'data', '%s_act_root.json' % act), 'w'))
    save = A.ROOT
    A.ROOT = d
    try:
        sf = A.shared_files()
    finally:
        A.ROOT = save
    want('a file named by two roots is shared, one named once is not (read %s)' % sf,
         'data/x.txt' in sf and 'data/once.txt' not in sf and set(A.RULED) <= set(sf))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
