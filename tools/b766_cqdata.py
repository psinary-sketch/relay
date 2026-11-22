# -*- coding: utf-8 -*-
"""tools/b766_cqdata.py -- (R376)(4)(d) L7: THE VALUES OF cQ TO 1023 AND THE REPRESENTATIONS OF Q0 ENTER THE KERNEL AS DATA. Written by
the Write tool and committed before its first run in any form; its form carried from tools/b766_kdata.py.

From tools/b766_certificate.py's lambda_q_exact (imported as committed: the loop of tools/b694_witness_terms.py :291-:317 in exact
arithmetic, no bank of zeros imported) and a count of Q0(m, n) = m^2 + m n + 6 n^2 over the box |m| <= 38, |n| <= 13, this tool writes
SIDEExplicitFormula/Window/CQData.lean in SIDE-explicit-formula:
  LTree, a binary tree read by the bits of an index from the lowest, and its reader LTree.get;
  primeList, the 172 primes below 1024;
  repTree: at each k from 0 to 1023 the pairs (m, n) of the box with Q0(m, n) = k, in order, none at 0;
  cqTree: at each n from 0 to 1023 the pairs (p, z), z an integer not 0, with cQ(n) = SUM z log p, none where cQ(n) is 0.
The Lean (CQValues.lean, by hand) proves r_Q(k) the length of the list at k and cQ(n) the combination at n, each by the kernel's evaluation
of a check and an induction; the file is data and its truth is the Lean's. No value of cQ is printed; the file names no frequency (no
decimal literal, no barred word: tools/b766_controls.py's Lean text check).

THE CONTROL: the representations against the brute count over the box and a wider box (|m| <= 60, |n| <= 20), each list in the box, in
order and without repetition, their total the box's count of 1 <= Q0 <= 1023; the n at which cQ is not 0 equal to the n of
data/b766_certificate.json's K; each z an integer, each p a prime dividing its n; THE LEAN'S CHECKS MODELLED over the text as read back
(repOK at each k, the box's count, prodOK at each n, cqOK at each n with its proper divisors); the trees and the primes read back from the
text equal to those composed; a planted digit in each tree read as one difference at its index and as a failure of the modelled check; no
decimal literal and no barred word.

  python -X utf8 -u tools/b766_cqdata.py dry      compose in memory, the control over the composed text, nothing written
  python -X utf8 -u tools/b766_cqdata.py write    write the file, read it back from the disk, the control; data/b766_cqdata.txt
  python -X utf8 -u tools/b766_cqdata.py control  the control over the file on the disk, printed
"""
import hashlib
import io
import json
import os
import re
import sys
import time

T_ = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T_)
D_ = os.path.join(RELAY, 'data')
for p_ in (T_, os.path.join(T_, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b766_certificate as C     # noqa: E402  (factor_table, lambda_q_exact)
import commit as CT              # noqa: E402  (KERNELS)

NL = '\n'
ACT = 'b766'
EF = 'SIDE-explicit-formula'
REL = 'SIDEExplicitFormula/Window/CQData.lean'
OUT = os.path.join(CT.KERNELS[EF], REL)
BANK = os.path.join(D_, 'b766_cqdata.txt')
CERT = os.path.join(D_, 'b766_certificate.json')
TOP = 1024                 # ### 2^10: both trees' indices 0 .. 1023
NMAX = 1023
MB, NB = 38, 13            # ### the box: |m| <= 38, |n| <= 13 (the Lean's qBox)
FUEL = 10                  # ### ev's divisions
PLANT_CQ = 840             # ### the planted digit's n in cqTree
PLANT_REP = 600            # ### the planted digit's k in repTree
DECIMAL = re.compile(r'\d\.\d')
BARRED = re.compile(r'(?i)frequen|ordinate|riemannZeta')


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def q0(m, n):
    return m * m + m * n + 6 * n * n


def primes_below(x):
    return [p for p in range(2, x) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def data():
    spf = C.factor_table(NMAX)
    lam, r = C.lambda_q_exact(NMAX, spf)
    cq = [[] for _ in range(TOP)]
    bad = []
    for n in range(2, NMAX + 1):
        for p in sorted(lam[n]):
            x = lam[n][p]
            if int(x.q) != 1:
                bad.append(n)
            cq[n].append((p, int(x.p)))
    reps = [[] for _ in range(TOP)]
    for m in range(-MB, MB + 1):
        for n in range(-NB, NB + 1):
            k = q0(m, n)
            if 1 <= k <= NMAX:
                reps[k].append((m, n))
    for k in range(TOP):
        reps[k].sort()
    raw = io.open(CERT, 'rb').read()
    K = set(int(n) for n in json.loads(raw.decode('utf-8'))['K'])
    return cq, reps, r, bad, K, hashlib.sha256(raw).hexdigest()


def render(vals, ind, leaf):
    if len(vals) == 1:
        return leaf(vals[0])
    a_, b_ = render(vals[0::2], ind + 1, leaf), render(vals[1::2], ind + 1, leaf)
    pad = NL + '  ' * (ind + 1)
    return '.node' + pad + '(' + a_ + ')' + pad + '(' + b_ + ')'


def list_leaf(v):
    return '.leaf [' + ', '.join('(%d, %d)' % t for t in v) + ']'


def compose(cq, reps, csha):
    P = primes_below(TOP)
    out = ['import Mathlib.Data.Real.Basic', '',
           '/-!',
           '# The values of `cQ` to 1023 and the representations of `Q0`, as data',
           '',
           '`primeList`: the %d primes below 1024. `repTree`: at each `k` from 0 to 1023 the pairs `(m, n)` with' % len(P),
           '`|m| ≤ %d`, `|n| ≤ %d` and `m^2 + m n + 6 n^2 = k`, in order, none at 0. `cqTree`: at each `n` from 0 to 1023 the pairs' % (MB, NB),
           '`(p, z)`, `z` an integer not 0, with `cQ n = ∑ z log p`, none where `cQ n` is 0. Written by relay tools/b766_cqdata.py',
           'under (R376)(4)(d); edited by no hand. The file is data: CQValues.lean checks it by the kernel`s evaluation.',
           '',
           'The certificate bank`s sha256, the file whole: %s' % csha,
           '-/', '',
           'namespace SIDEExplicitFormula',
           'namespace Window', '',
           '/-- A binary tree, read by the bits of an index from the lowest. -/',
           'inductive LTree (α : Type) where',
           '  | leaf : α → LTree α',
           '  | node : LTree α → LTree α → LTree α', '',
           '/-- The value at index `i`: at a node the even indices go left and the odd right, the index halved. -/',
           'def LTree.get {α : Type} : LTree α → ℕ → α',
           '  | .leaf v, _ => v',
           '  | .node l r, i => if i % 2 = 0 then LTree.get l (i / 2) else LTree.get r (i / 2)', '',
           '/-- The primes below 1024. -/',
           'def primeList : List ℕ := [' + ', '.join(str(p) for p in P) + ']', '',
           '/-- The representations of each `k` below 1024 in the box. -/',
           'def repTree : LTree (List (ℤ × ℤ)) :=', '  ' + render(reps, 1, list_leaf), '',
           '/-- The coefficients of `cQ n` on the logarithms of primes, each `n` below 1024. -/',
           'def cqTree : LTree (List (ℕ × ℤ)) :=', '  ' + render(cq, 1, list_leaf), '',
           'end Window', 'end SIDEExplicitFormula', '']
    return NL.join(out), P


TOK = re.compile(r'\.node|\.leaf|\(|\)|\[|\]|,|-?\d+')


def parse_tree(text, name):
    m = re.search(r'^def %s : LTree \(List \((?:ℤ|ℕ) × ℤ\)\) :=\n(.*?)\n\n' % name, text, re.M | re.S)
    if not m:
        return None
    toks = TOK.findall(m.group(1))
    pos = [0]

    def nxt():
        t = toks[pos[0]]
        pos[0] += 1
        return t

    def tree():
        t = nxt()
        if t == '.node':
            assert nxt() == '('
            a_ = tree()
            assert nxt() == ')'
            assert nxt() == '('
            b_ = tree()
            assert nxt() == ')'
            return ('n', a_, b_)
        assert t == '.leaf'
        assert nxt() == '['
        v = []
        if toks[pos[0]] == ']':
            nxt()
            return ('l', v)
        while True:
            assert nxt() == '('
            x = int(nxt())
            assert nxt() == ','
            y = int(nxt())
            assert nxt() == ')'
            v.append((x, y))
            t = nxt()
            if t == ']':
                return ('l', v)
            assert t == ','
    try:
        t = tree()
    except (AssertionError, IndexError, ValueError):
        return None
    return t if pos[0] == len(toks) else None


def tget(t, i):
    while t[0] == 'n':
        t, i = (t[1] if i % 2 == 0 else t[2]), i // 2
    return t[1]


def read_back(text):
    rt, ct = parse_tree(text, 'repTree'), parse_tree(text, 'cqTree')
    pm = re.search(r'^def primeList : List ℕ := \[(.*?)\]$', text, re.M)
    P = [int(x) for x in re.findall(r'\d+', pm.group(1))] if pm else None
    reps = [tget(rt, i) for i in range(TOP)] if rt else None
    cq = [tget(ct, i) for i in range(TOP)] if ct else None
    return reps, cq, P


def ev(p, n):
    f, out = FUEL, 0
    while f > 0 and n > 0 and n % p == 0:
        out, n, f = out + 1, n // p, f - 1
    return out


def model(reps, cq, P):
    """the Lean's four checks, as CQValues.lean states them, over the read-back data: (repOK fails, count equal, prodOK fails, cqOK fails)."""
    def zl(lst, p):
        for q, v in lst:
            if q == p:
                return v
        return 0

    def zc(n, p):
        return zl(cq[n % TOP], p) if n % p == 0 else 0

    def rT(k):
        return len(reps[k % TOP])
    rep_bad = [k for k in range(1, NMAX + 1) if not (all(-MB <= m <= MB and -NB <= n <= NB and q0(m, n) == k for m, n in reps[k])
                                                     and len(set(reps[k])) == len(reps[k]))]
    cnt = sum(1 for m in range(-MB, MB + 1) for n in range(-NB, NB + 1) if 1 <= q0(m, n) <= NMAX)
    count_eq = cnt == sum(rT(k) for k in range(1, NMAX + 1))
    prod_bad = []
    for n in range(1, NMAX + 1):
        pr = 1
        for p in P:
            pr *= p ** ev(p, n)
        if pr != n:
            prod_bad.append(n)
    cq_bad = []
    for n in range(2, NMAX + 1):
        pd = [d for d in range(1, n) if n % d == 0]
        for p in P:
            if n % p == 0 and 2 * zc(n, p) != rT(n) * ev(p, n) - sum(zc(d, p) * rT(n // d) for d in pd):
                cq_bad.append(n)
                break
    return rep_bad, count_eq, cnt, prod_bad, cq_bad


def control(text, cq, reps, r, bad, K):
    L, ok = [], []

    def row(w, c):
        ok.append(bool(c))
        L.append('  %-150s %s' % (w, 'AS WANTED' if c else 'NOT AS WANTED'))
    rb, cb, P = read_back(text)
    row('the representations equal the tool`s r at each k from 1 to 1023 (the certificate`s loop)', all(len(reps[k]) == r[k] for k in range(1, NMAX + 1)))
    wide = [0] * TOP
    for m in range(-60, 61):
        for n in range(-20, 21):
            k = q0(m, n)
            if 1 <= k <= NMAX:
                wide[k] += 1
    row('the box holds every representation: the counts over |m| <= 60, |n| <= 20 equal the box`s at each k', all(wide[k] == len(reps[k]) for k in range(TOP)))
    nz = set(n for n in range(TOP) if cq[n])
    row('cQ not 0 at %d n, the n of the certificate`s K (%d), equal' % (len(nz), len(K)), nz == K)
    row('each coefficient an integer (%d not) and each p a prime dividing its n' % len(bad),
        not bad and all(n % p == 0 and p in set(primes_below(TOP)) for n in range(TOP) for p, _ in cq[n]))
    row('the trees and the primes read back from the text equal to those composed', rb == reps and cb == cq and P == primes_below(TOP))
    if rb is not None and cb is not None and P is not None:
        rep_bad, count_eq, cnt, prod_bad, cq_bad = model(rb, cb, P)
        row('THE LEAN`S CHECKS MODELLED: repOK at each k (%d fail) ; the box`s count %d equal to the lists` total ; prodOK at each n (%d fail) ; '
            'cqOK at each n (%d fail)' % (len(rep_bad), cnt, len(prod_bad), len(cq_bad)), not rep_bad and count_eq and not prod_bad and not cq_bad)
        # ### the planted digits: in cqTree at the first n from PLANT_CQ whose leaf is not empty and stands once in the text
        pc = next((n for n in range(PLANT_CQ, TOP) if cb[n] and text.count(list_leaf(cb[n])) == 1), None)
        lst = cb[pc] if pc is not None else []
        t2 = None
        if lst:
            old = list_leaf(lst)
            new = list_leaf([(lst[0][0], lst[0][1] + 1)] + lst[1:])
            t2 = text.replace(old, new)
        if t2 is not None:
            r2, c2, P2 = read_back(t2)
            diffs = [i for i in range(TOP) if c2[i] != cb[i]]
            m2 = model(r2, c2, P2)
            row('a planted digit in cqTree at n %d read as the one difference (%s) and as a failure of cqOK there (%s)' % (pc, diffs, m2[4][:3]),
                diffs == [pc] and pc in m2[4])
        else:
            row('a planted digit in cqTree from n %d: no leaf not empty and standing once in the text' % PLANT_CQ, False)
        lst = rb[PLANT_REP]
        t3 = None
        if lst:
            old = list_leaf(lst)
            new = list_leaf([(lst[0][0] + 1, lst[0][1])] + lst[1:])
            if text.count(old) == 1:
                t3 = text.replace(old, new)
        if t3 is not None:
            r3, c3, P3 = read_back(t3)
            diffs = [i for i in range(TOP) if r3[i] != rb[i]]
            m3 = model(r3, c3, P3)
            row('a planted digit in repTree at k %d read as the one difference (%s) and as a failure of repOK there (%s)' % (PLANT_REP, diffs, m3[0][:3]),
                diffs == [PLANT_REP] and PLANT_REP in m3[0])
        else:
            row('a planted digit in repTree at k %d: its leaf not found once in the text' % PLANT_REP, False)
    else:
        row('the text parsed', False)
    row('no decimal literal and no barred word in the text (%d, %d)' % (len(DECIMAL.findall(text)), len(BARRED.findall(text))),
        not DECIMAL.search(text) and not BARRED.search(text))
    return L, ok


def main(cmd):
    cq, reps, r, bad, K, csha = data()
    text, P = compose(cq, reps, csha)
    H = ['%s -- (R376)(4)(d) L7: THE VALUES OF cQ TO 1023 AND THE REPRESENTATIONS OF Q0 ENTER THE KERNEL AS DATA, SIDE-explicit-formula %s (%s, %s)' % (
        ACT, REL, cmd, _now()), '',
        '## THE FILE COMPOSED',
        '  primes %d ; representations %d over %d k, at most %d at one k ; cQ not 0 at %d n, pairs %d, at most %d primes at one n, the largest |z| %d bits' % (
            len(P), sum(len(x) for x in reps), sum(1 for x in reps if x), max(len(x) for x in reps), sum(1 for x in cq if x), sum(len(x) for x in cq),
            max(len(x) for x in cq), max(abs(z).bit_length() for x in cq for _p, z in x)),
        '  lines %d ; bytes %d ; sha256 %s' % (len(text.split(NL)) - 1, len(text.encode('utf-8')), hashlib.sha256(text.encode('utf-8')).hexdigest()[:16])]
    if cmd == 'dry':
        L, ok = control(text, cq, reps, r, bad, K)
        print(NL.join(H + ['', '## THE CONTROL OVER THE COMPOSED TEXT (nothing written)'] + L + [
            '', '### ### **THE CONTROL %d OF %d ; NOTHING WRITTEN.**' % (sum(ok), len(ok))]))
        return
    if cmd == 'write':
        if os.path.exists(OUT):
            sys.exit('### %s STANDS ALREADY -- nothing written (the file is written once; read it by `control`)' % REL)
        with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
    if cmd not in ('write', 'control'):
        sys.exit(__doc__)
    if not os.path.exists(OUT):
        sys.exit('### %s ABSENT -- nothing read' % REL)
    disk = io.open(OUT, encoding='utf-8', newline='').read()
    L, ok = control(disk, cq, reps, r, bad, K)
    eq = disk == text
    out = H + ['', '## THE FILE ON THE DISK, READ BACK',
               '  %s: bytes %d ; sha256 %s ; carriage returns %d ; equal to the composed text: %s' % (
                   REL, len(disk.encode('utf-8')), hashlib.sha256(disk.encode('utf-8')).hexdigest()[:16], disk.count('\r'), eq),
               '', '## THE CONTROL OVER THE FILE AS WRITTEN'] + L + [
        '', '### ### **THE DATA FILE %s ; THE CONTROL %d OF %d %s ; NO VALUE OF cQ PRINTED.**' % (
            'WRITTEN AND READ BACK' if cmd == 'write' else 'READ', sum(ok), len(ok), 'AS WANTED' if all(ok) and eq else 'NOT AS WANTED')]
    print(NL.join(out))
    if cmd == 'write':
        with io.open(BANK, 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(out) + NL)
        print('written data/%s' % os.path.basename(BANK))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '')
