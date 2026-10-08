# -*- coding: utf-8 -*-
"""test_act_root_order_b641.py -- THE TEST OF W-ORD-ROOT-ORDER in tools/act_root.py, (R251)(3), written at b641.

### The act root is the last step of an act, after the last declared seal re-run; no bank the root names is written after it. Every case runs
### in a fresh temporary directory standing in for relay (its data/ and its roots file), the repositories and the cited tags emptied, so no
### remote is read and nothing in relay is written.
###   (1) a root computed and written over one bank reads AGREE at verify;
###   (2) THE PLANTED WRITE: the same bank written again after the root with its bytes unchanged reads DISAGREE, "written after the root";
###   (3) the bank written after the root with one byte changed reads DISAGREE, "changed";
###   (4) a root banked in the form before b641 (no `at`) over an unchanged bank written after it reads AGREE -- b640's root is not recomputed
###       and the rule reads forward only;
###   (5) compute refuses a root that leaves out the act's own seal bank when that bank exists, and computes one that names it.
### Usage: python tools/test_act_root_order_b641.py
"""
import json
import os
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import act_root as AR   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def _stage():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'data'))
    save = (AR.D, AR.ROOTS, AR.ROOT, AR.repositories, AR.registry_tags)
    AR.ROOT, AR.D, AR.ROOTS = d, os.path.join(d, 'data'), os.path.join(d, 'data', 'act_roots.txt')
    AR.repositories = lambda rev='HEAD': []
    AR.registry_tags = lambda kernels, rev='HEAD': []
    return d, save


def _unstage(save):
    AR.D, AR.ROOTS, AR.ROOT, AR.repositories, AR.registry_tags = save


def _bank(d, name, body):
    p = os.path.join(d, 'data', name)
    open(p, 'wb').write(body)
    return p


def _quiet(fn, *a, **k):
    import io as _io
    so = sys.stdout
    sys.stdout = _io.StringIO()
    try:
        return fn(*a, **k)
    finally:
        sys.stdout = so


def verdicts(v):
    return [(x[0], x[1]) for x in v]


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-118s %s' % (label, 'PASS' if cond else '### FAIL'))

    d, save = _stage()
    try:
        p = _bank(d, 't901_x.txt', b'the bank\n')
        old = time.time() - 60
        os.utime(p, (old, old))
        _quiet(AR.compute, 't901', ['data/t901_x.txt'], write=True)
        j = json.load(open(os.path.join(d, 'data', 't901_act_root.json')))
        v1 = AR.verify(remote=lambda q: {})
        want('(1) a root over one bank, written, reads AGREE (read %s; the root`s time banked %s)' % (verdicts(v1), j.get('at')),
             verdicts(v1) == [('t901', 'AGREE')] and isinstance(j.get('at_epoch'), float))
        open(p, 'wb').write(b'the bank\n')
        later = j['at_epoch'] + 30
        os.utime(p, (later, later))
        v2 = AR.verify(remote=lambda q: {})
        want('(2) THE PLANTED WRITE: the bank written again after the root, bytes unchanged, reads DISAGREE (read %s)' % (
             [(a, v, w) for a, v, w in v2]), verdicts(v2) == [('t901', 'DISAGREE')] and any('written after the root' in w for w in v2[0][2]))
        open(p, 'wb').write(b'the bank!\n')
        v3 = AR.verify(remote=lambda q: {})
        want('(3) the bank written after the root with a byte changed reads DISAGREE, changed (read %s)' % ([(a, v, w) for a, v, w in v3]),
             verdicts(v3) == [('t901', 'DISAGREE')] and any('changed' in w for w in v3[0][2]))
    finally:
        _unstage(save)
    d, save = _stage()
    try:
        p = _bank(d, 't902_x.txt', b'an old bank\n')
        h = AR.sha256_file(p)
        r = AR.root_of(['data/t902_x.txt ' + h], AR.EMPTY)
        json.dump(dict(act='t902', root=r, previous=AR.EMPTY, items=['data/t902_x.txt ' + h], reads=dict(heads={}, tags={}, banks={})),
                  open(os.path.join(d, 'data', 't902_act_root.json'), 'w'))
        open(AR.ROOTS, 'w').write('t902 %s %s\n' % (r, AR.EMPTY))
        later = time.time() + 30
        os.utime(p, (later, later))
        v4 = AR.verify(remote=lambda q: {})
        want('(4) a root in the form before b641 (no time banked), its bank unchanged but written later, reads AGREE (read %s)' % verdicts(v4),
             verdicts(v4) == [('t902', 'AGREE')])
    finally:
        _unstage(save)
    d, save = _stage()
    try:
        _bank(d, 't903_x.txt', b'x\n')
        _bank(d, 't903_seal_hashes.json', b'{}\n')
        try:
            _quiet(AR.compute, 't903', ['data/t903_x.txt'], write=True)
            refused = False
        except SystemExit as e:
            refused = 'W-ORD-ROOT-ORDER' in str(e)
        wrote_none = not os.path.exists(os.path.join(d, 'data', 't903_act_root.json'))
        _quiet(AR.compute, 't903', ['data/t903_x.txt', 'data/t903_seal_hashes.json'], write=True)
        named = os.path.exists(os.path.join(d, 'data', 't903_act_root.json'))
        want('(5) compute refuses a root leaving out the act`s seal bank (refused %s, nothing written %s) and computes one naming it (%s)' % (
             refused, wrote_none, named), refused and wrote_none and named)
    finally:
        _unstage(save)
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
