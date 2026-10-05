# -*- coding: utf-8 -*-
"""test_act_root.py -- THE TEST OF tools/act_root.py, W-ORD-ACT-ROOT, (R234)(3), written at b624.

###   (1) a fixed item list and the empty previous root hash to a fixed root (the form's vector, computed once and written here);
###   (2) the root does not depend on the items' order (they are sorted);
###   (3) a different previous root gives a different root (the chain);
###   (4) a one-byte change on a COPY of a bank changes the bank's line and so the root -- the copy made in a fresh temporary
###       directory, the bank itself never touched;
###   (5) the previous root of a chain's first act is the empty string's sha256;
###   (6) verify reads a chain whose second line names a previous root other than the first line's root as DISAGREE, on a
###       roots file and banks written to a fresh temporary directory, never relay's.
### Nothing in relay is written. Usage: python tools/test_act_root.py
"""
import hashlib
import json
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import act_root as AR   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EMPTY = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
ITEMS = ['relay 0123456789abcdef0123456789abcdef01234567', 'SIDE-x v0.1 89abcdef0123456789abcdef0123456789abcdef',
         'data/b000_x.txt ' + hashlib.sha256(b'x').hexdigest()]
WANT = 'af3a43edc36a0b38a1c9195bc98e3fda6008f0a3098dcb1df9782da94aee3664'


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    r1 = AR.root_of(ITEMS, EMPTY)
    want('(1) the fixed items and the empty previous root hash to the fixed root (read %s)' % r1[:16], r1 == WANT)
    want('(2) the root does not depend on the items` order', AR.root_of(list(reversed(ITEMS)), EMPTY) == r1)
    want('(3) a different previous root gives a different root', AR.root_of(ITEMS, r1) != r1)
    src = os.path.join(ROOT, 'tools', 'act_root.py')
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, 'bank_copy.txt')
    shutil.copy(src, cp)
    before = AR.sha256_file(src)
    a = AR.root_of(ITEMS + ['data/bank_copy.txt ' + AR.sha256_file(cp)], EMPTY)
    b_ = bytearray(open(cp, 'rb').read())
    b_[0] ^= 0x01
    open(cp, 'wb').write(bytes(b_))
    b = AR.root_of(ITEMS + ['data/bank_copy.txt ' + AR.sha256_file(cp)], EMPTY)
    want('(4) a one-byte change on a copy of a bank changes the root (copy %s; the source unmoved %s)' % (cp.replace(os.sep, '/'), AR.sha256_file(src) == before),
         a != b and AR.sha256_file(src) == before)
    want('(5) a chain`s first previous root is the empty string`s sha256', AR.EMPTY == EMPTY == hashlib.sha256(b'').hexdigest())
    d = tempfile.mkdtemp()
    save = (AR.D, AR.ROOTS, AR.ROOT)
    try:
        AR.D, AR.ROOTS, AR.ROOT = d, os.path.join(d, 'act_roots.txt'), d
        r_a = AR.root_of([], EMPTY)
        r_b = AR.root_of([], 'f' * 64)
        for act, r, p in (('t001', r_a, EMPTY), ('t002', r_b, 'f' * 64)):
            json.dump(dict(act=act, root=r, previous=p, items=[]), open(os.path.join(d, '%s_act_root.json' % act), 'w'))
        open(AR.ROOTS, 'w').write('t001 %s %s\nt002 %s %s\n' % (r_a, EMPTY, r_b, 'f' * 64))
        v = AR.verify(remote=lambda p: {})
    finally:
        AR.D, AR.ROOTS, AR.ROOT = save
    want('(6) verify reads a broken chain`s second act DISAGREE and its first AGREE (read %s)' % [(x[0], x[1]) for x in v],
         [(x[0], x[1]) for x in v] == [('t001', 'AGREE'), ('t002', 'DISAGREE')])
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
