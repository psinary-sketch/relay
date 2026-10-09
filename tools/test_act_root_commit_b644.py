# -*- coding: utf-8 -*-
"""test_act_root_commit_b644.py -- THE TEST OF W-ORD-CHAIN-AT-COMMIT in tools/act_root.py, (R254)(2), written at b644.

### verify reads every bank a root names at the commit that root recorded, not from the working tree. Every case runs in a fresh temporary
### git clone standing in for relay (its own data/, its roots file, relay's `* text=auto eol=lf` attribute), the repositories and the cited
### tags emptied, so no remote is read and nothing in relay is written.
###   (1) THE PLANTED LATER EDIT: a root over a committed bank, the bank then edited and committed -- AGREE at the recorded commit,
###       DISAGREE ("changed") at the working tree; the root banks its `commit`;
###   (2) a bank hashed before its first commit is read at the first later commit carrying it -- AGREE, counted at a later commit, and a
###       later edit after that commit still reads AGREE;
###   (3) a bank re-written between the root and its first commit reads DISAGREE at commit;
###   (4) a bank written with CR LF and hashed so, committed as LF: AGREE in its CRLF form on an act up to b643, DISAGREE on an act after it
###       (the author's answer at b644);
###   (5) compute --write refuses a bank holding CR LF, nothing written.
### Usage: python tools/test_act_root_commit_b644.py
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import act_root as AR   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def git(d, *a):
    r = subprocess.run(['git', '-C', d] + list(a), capture_output=True, text=True)
    return r.stdout.strip()


def _stage():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'data'))
    subprocess.run(['git', 'init', '-q', '-b', 'main', d], capture_output=True)
    git(d, 'config', 'user.email', 'test@example.invalid')
    git(d, 'config', 'user.name', 'test')
    git(d, 'config', 'core.autocrlf', 'true')
    open(os.path.join(d, '.gitattributes'), 'wb').write(b'* text=auto eol=lf\n')
    _commit(d, '.gitattributes', 'attributes')
    save = (AR.D, AR.ROOTS, AR.ROOT, AR.repositories, AR.registry_tags)
    AR.ROOT, AR.D, AR.ROOTS = d, os.path.join(d, 'data'), os.path.join(d, 'data', 'act_roots.txt')
    AR.repositories = lambda rev='HEAD': []
    AR.registry_tags = lambda kernels, rev='HEAD': []
    return d, save


def _unstage(save):
    AR.D, AR.ROOTS, AR.ROOT, AR.repositories, AR.registry_tags = save


def _commit(d, path, msg):
    git(d, 'add', path)
    git(d, 'commit', '-q', '-m', msg)
    return git(d, 'rev-parse', 'HEAD')


def _bank(d, name, body):
    open(os.path.join(d, 'data', name), 'wb').write(body)
    return 'data/' + name


def _quiet(fn, *a, **k):
    import io as _io
    so = sys.stdout
    sys.stdout = _io.StringIO()
    try:
        return fn(*a, **k)
    finally:
        sys.stdout = so


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  (%d) %-120s %s' % (len(res), label, 'PASS' if cond else '### FAIL'))

    d, save = _stage()
    try:
        b = _bank(d, 't901_x.txt', b'the bank\n')
        c0 = _commit(d, b, 'bank')
        _quiet(AR.compute, 't901', [b], write=True)
        j = json.load(open(os.path.join(d, 'data', 't901_act_root.json')))
        _bank(d, 't901_x.txt', b'the bank, edited later\n')
        _commit(d, b, 'planted later edit')
        vc = AR.verify(remote=lambda q: {}, worktree=False)
        ra = dict(AR.READS_AT.get('t901') or {})
        vw = AR.verify(remote=lambda q: {}, worktree=True)
        want('THE PLANTED LATER EDIT: AGREE at the recorded commit %s (read %s), DISAGREE at the working tree (read %s); the root banks commit %s' % (
             c0[:8], [(a, v) for a, v, _w in vc], [(a, v, w) for a, v, w in vw], (j.get('commit') or {}).get('relay', '')[:8]),
             [(a, v) for a, v, _w in vc] == [('t901', 'AGREE')] and ra.get('blob') == 1 and ra.get('commit') == c0 and
             [(a, v) for a, v, _w in vw] == [('t901', 'DISAGREE')] and any('changed' in w for w in vw[0][2]) and
             (j.get('commit') or {}).get('relay') == c0)
    finally:
        _unstage(save)
    d, save = _stage()
    try:
        b = _bank(d, 't902_x.txt', b'hashed before its commit\n')
        _quiet(AR.compute, 't902', [b], write=True)
        _commit(d, b, 'the act commit')
        v1 = AR.verify(remote=lambda q: {}, worktree=False)
        ra = dict(AR.READS_AT.get('t902') or {})
        _bank(d, 't902_x.txt', b'edited after its first commit\n')
        _commit(d, b, 'a later edit')
        v2 = AR.verify(remote=lambda q: {}, worktree=False)
        want('a bank hashed before its first commit reads AGREE at the first later commit carrying it (read %s, %s), and after a later edit (%s)' % (
             [(a, v) for a, v, _w in v1], ra, [(a, v) for a, v, _w in v2]),
             [(a, v) for a, v, _w in v1] == [('t902', 'AGREE')] and ra.get('later') == 1 and [(a, v) for a, v, _w in v2] == [('t902', 'AGREE')])
    finally:
        _unstage(save)
    d, save = _stage()
    try:
        b = _bank(d, 't903_x.txt', b'as hashed\n')
        _quiet(AR.compute, 't903', [b], write=True)
        _bank(d, 't903_x.txt', b're-written before its commit\n')
        _commit(d, b, 'the act commit')
        v3 = AR.verify(remote=lambda q: {}, worktree=False)
        want('a bank re-written between the root and its first commit reads DISAGREE at commit (read %s)' % ([(a, v, w) for a, v, w in v3]),
             [(a, v) for a, v, _w in v3] == [('t903', 'DISAGREE')] and any('changed' in w for w in v3[0][2]))
    finally:
        _unstage(save)
    oks = []
    for act, expect in (('t600', 'AGREE'), ('t904', 'DISAGREE')):
        d, save = _stage()
        try:
            name = '%s_x.txt' % act
            body = b'line one\r\nline two\r\n'
            _bank(d, name, body)
            h = AR.sha256_file(os.path.join(d, 'data', name))
            c = git(d, 'rev-parse', 'HEAD')
            r = AR.root_of(['data/%s %s' % (name, h)], AR.EMPTY)
            json.dump(dict(act=act, root=r, previous=AR.EMPTY, items=['data/%s %s' % (name, h)], reads=dict(heads={'relay': c}, tags={}, banks={})),
                      open(os.path.join(d, 'data', '%s_act_root.json' % act), 'w'))
            open(AR.ROOTS, 'w').write('%s %s %s\n' % (act, r, AR.EMPTY))
            _commit(d, 'data/' + name, 'the act commit, normalised to LF')
            blob = subprocess.run(['git', '-C', d, 'show', 'HEAD:data/' + name], capture_output=True).stdout
            v = AR.verify(remote=lambda q: {}, worktree=False)
            ra = dict(AR.READS_AT.get(act) or {})
            oks.append((act, blob == b'line one\nline two\n', [(a, x) for a, x, _w in v], ra.get('crlf'), expect))
        finally:
            _unstage(save)
    want('a CRLF bank committed as LF: AGREE in its CRLF form on an act up to b643, DISAGREE after it (read %s)' % oks,
         all(lf and vv == [(a, e)] and n == 1 for a, lf, vv, n, e in oks))
    d, save = _stage()
    try:
        b = _bank(d, 't905_x.txt', b'a\r\nb\r\n')
        try:
            _quiet(AR.compute, 't905', [b], write=True)
            refused = False
        except SystemExit as e:
            refused = 'CR LF' in str(e)
        wrote_none = not os.path.exists(os.path.join(d, 'data', 't905_act_root.json')) and not os.path.exists(AR.ROOTS)
        want('compute --write refuses a bank holding CR LF (refused %s), nothing written (%s)' % (refused, wrote_none), refused and wrote_none)
    finally:
        _unstage(save)
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
