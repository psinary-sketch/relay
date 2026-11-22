# -*- coding: utf-8 -*-
"""tools/b766_kdata.py -- (R376)(4)(d) L6 (c): THE VALUES K(n) OF THE CERTIFICATE ENTER THE KERNEL AS DATA. Written by the Write tool and
committed before its first run in any form; its form carried from tools/b766_window_data.py.

From the window's coefficients as integers a_j over 10^17 (tools/b766_certificate.py window() and scaled(), the integers
SIDEExplicitFormula/Window/Coeffs.lean holds), this tool writes SIDEExplicitFormula/Window/KData.lean in SIDE-explicit-formula:
  IntTree, a binary tree of integers read by the bits of an index from the lowest, and its reader IntTree.get;
  THE F TABLE fTree: F(T) = SUM_j a_j D(j - T) for T from 0 to 16383, D(x) = SUM_l w_l max(x + l, 0)^7, computed by its local
    recurrence F(T) = 4 F(T+1) - 6 F(T+2) + 4 F(T+3) - F(T+4) + SUM_{i<7} a_{T-3+i} E(i - 3), F = 0 from 16384, E the fourth difference
    of D (1, 120, 1191, 2416, 1191, 120, 1 on -3 .. 3, the spline's constants and no window's), as 64 subtrees of 256 leaves;
  THE COEFFICIENT TREE aTree: a_m for m from 0 to 16383, 0 off 16 .. 16380, as 64 subtrees;
  THE TABLE OF Kt: the 197 pairs (n, Kt n), Kt n = SUM_j SUM_m a_j a_m kapTilde n (j - n m) = SUM_m a_m SUM_k w_k F(n (m + k)), at each n
    of data/b766_certificate.json's K, in groups of at most KT_CAP strided terms, ktTable their concatenation.
The Lean (KFast.lean, by hand) checks the F tree against its recurrence, the coefficient tree against Coeffs.lean's list and the table of
Kt against the strided sums, each by the kernel's evaluation; the file is data and its truth is the Lean's. No coefficient, no value of
F and no K(n) is printed; the window's frequency is read nowhere and the file names none (no decimal literal, no barred word:
tools/b766_controls.py's Lean text check).

THE CONTROL: Kt(n) / (80640 n^4 10^34) against the certificate's K(n), 197 of 197 (the certificate's own route); F against its
definition, the full sum over j, at twelve T; Kt by the direct double sum with kapTilde at three n; the spline's constants; the two trees
and the table read back from the text equal to those composed, and Coeffs.lean's integers, read from the disk, equal to the tree's; the
head's three digests; the definitions named in order; THE LEAN'S CHECKS MODELLED over the text as read back (the recurrence at each T of
the sixteen chunks, the coefficient walk, the halving sums at the 197 n); a planted digit in each tree and in the table read as one
difference at its index and as a failure of the modelled check; no decimal literal and no barred word.

  python -X utf8 -u tools/b766_kdata.py dry      compose in memory, the control over the composed text, nothing written
  python -X utf8 -u tools/b766_kdata.py write    write the file, read it back from the disk, the control; data/b766_kdata.txt
  python -X utf8 -u tools/b766_kdata.py control  the control over the file on the disk, printed
"""
import hashlib
import io
import json
import os
import re
import sys
import time
from fractions import Fraction

T_ = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T_)
D_ = os.path.join(RELAY, 'data')
for p_ in (T_, os.path.join(T_, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b766_certificate as C     # noqa: E402  (window(), scaled(): the bank read and checked; no bank of zeros imported)
import commit as CT              # noqa: E402  (KERNELS)

NL = '\n'
ACT = 'b766'
EF = 'SIDE-explicit-formula'
REL = 'SIDEExplicitFormula/Window/KData.lean'
COEFFS_REL = 'SIDEExplicitFormula/Window/Coeffs.lean'
OUT = os.path.join(CT.KERNELS[EF], REL)
COEFFS = os.path.join(CT.KERNELS[EF], COEFFS_REL)
BANK = os.path.join(D_, 'b766_kdata.txt')
CERT = os.path.join(D_, 'b766_certificate.json')
J0, J1 = 16, 16380
TOP = 16384                # ### 2^14: both trees' indices 0 .. 16383
SUBS = 64                  # ### subtrees per tree, by the index's lowest six bits
SUBH = 8                   # ### each subtree 256 leaves, the index's next eight bits
CHUNK_T = 1024             # ### the Lean's recurrence chunks: 16 of 1024 from T = 16
NCHUNK = 16
KT_CAP = 4100              # ### at most this many strided terms in one group of the table of Kt
W = (1, -4, 6, -4, 1)
EVV = (1, 120, 1191, 2416, 1191, 120, 1)
DEN = 80640                # ### 16 * 5040: K(n) = Kt(n) / (80640 n^4 10^34)
PLANT_F = 5000             # ### the planted digit's T in the F tree
PLANT_A = 8016             # ### the planted digit's m in the coefficient tree
PLANT_K = 100              # ### the planted digit's index in the table of Kt
SAMPLE_T = (16, 17, 32, 1000, 8191, 16000, 16380, 16381, 16382, 16383, 16384, 16385)
DECIMAL = re.compile(r'\d\.\d')
BARRED = re.compile(r'(?i)frequen|ordinate|riemannZeta')
TOKEN = re.compile(r'\.node|\.leaf|\(|\)|-?\d+|[A-Za-z_][A-Za-z0-9_]*')


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def P7(x):
    return x ** 7 if x > 0 else 0


def kD(x):
    return sum(W[l] * P7(x + l) for l in range(5))


def kE(x):
    return kD(x) - 4 * kD(x - 1) + 6 * kD(x - 2) - 4 * kD(x - 3) + kD(x - 4)


def kapTilde(n, e):
    return sum(W[k] * W[l] * P7(e + l - k * n) for k in range(5) for l in range(5))


def mtop(n):
    return min(J1, (TOP - 1) // n)


def bitrev(q, h):
    return int(format(q, '0%db' % h)[::-1], 2)


def bank():
    """(a over 0 .. TOP + 7, the window's digests, the certificate's sha256 and K, Coeffs.lean's sha256 and integers, the reader's lines)."""
    js, cm, L, dig = C.window()
    Cs, S = C.scaled(cm, js['M'], J1)
    if S != 10 ** 17:
        sys.exit('### THE SCALE IS NOT 10^17 (Coeffs.lean`s coeffScale) -- NOTHING DONE')
    a = [0] * (TOP + 8)
    for j in range(J0, J1 + 1):
        a[j] = Cs[j]
    raw = io.open(CERT, 'rb').read()
    cert = json.loads(raw.decode('utf-8'))
    K = dict((int(n), Fraction(v)) for n, v in cert['K'].items())
    craw = io.open(COEFFS, 'rb').read()
    ctext = craw.decode('utf-8')
    chunks = re.findall(r'^def (coeffChunk\d+) : List ℤ := \[\n(.*?)\n\]$', ctext, re.M | re.S)
    lst = re.search(r'^def coeffList : List ℤ :=\n((?:  .*\n)+)', ctext, re.M)
    order = re.findall(r'coeffChunk\d+', lst.group(1)) if lst else []
    body = dict(chunks)
    clist = []
    for nm in order:
        clist += [int(x) for x in re.findall(r'-?\d+', body.get(nm, ''))]
    return a, dig, hashlib.sha256(raw).hexdigest(), K, hashlib.sha256(craw).hexdigest(), clist, L


def ftable(a):
    F = [0] * (TOP + 4)
    for T in range(TOP - 1, -1, -1):
        loc = sum(a[j] * EVV[j - T + 3] for j in range(max(0, T - 3), T + 4))
        F[T] = 4 * F[T + 1] - 6 * F[T + 2] + 4 * F[T + 3] - F[T + 4] + loc
    return F[:TOP]


def kt_fast(a, F, n):
    ff = lambda T: F[T] if T < TOP else 0   # noqa: E731
    return sum(a[m] * sum(W[k] * ff(n * (m + k)) for k in range(5)) for m in range(J0, mtop(n) + 1))


def kt_direct(a, n):
    tot = 0
    for m in range(J0, J1 + 1):
        if a[m]:
            for j in range(max(J0, n * m - 3), min(J1, n * m + 4 * n - 1) + 1):
                tot += a[j] * a[m] * kapTilde(n, j - n * m)
    return tot


def groups(ns):
    out, cur, tot = [], [], 0
    for n in ns:
        t = mtop(n) - J0 + 1
        if cur and tot + t > KT_CAP:
            out.append(cur)
            cur, tot = [], 0
        cur.append(n)
        tot += t
    if cur:
        out.append(cur)
    return out


def render(vals, ind, leaf):
    if len(vals) == 1:
        return leaf(vals[0])
    a_, b_ = render(vals[0::2], ind + 1, leaf), render(vals[1::2], ind + 1, leaf)
    if len(vals) <= 8:
        return '.node (%s) (%s)' % (a_, b_)
    pad = NL + '  ' * (ind + 1)
    return '.node' + pad + '(' + a_ + ')' + pad + '(' + b_ + ')'


def int_leaf(v):
    return '.leaf %d' % v if v >= 0 else '.leaf (%d)' % v


def tree_defs(vals, prefix, what):
    """the 64 subtree definitions and the top tree's, for the values at indices 0 .. TOP - 1."""
    out, names = [], []
    for r in range(SUBS):
        nm = '%sSub%02d' % (prefix, r)
        names.append(nm)
        out += ['/-- %s at the indices congruent to %d mod %d. -/' % (what, r, SUBS), 'def %s : IntTree :=' % nm,
                '  ' + render(vals[r::SUBS], 1, int_leaf), '']
    out += ['/-- %s at the indices 0 to %d, the subtrees by the index`s lowest six bits. -/' % (what, TOP - 1),
            'def %sTree : IntTree :=' % prefix, '  ' + render(names, 1, lambda s: s), '']
    return out, names


def compose(F, a, kt, gs, dig, csha, coeff_sha):
    out = ['import Mathlib.Data.Real.Basic', '',
           '/-!',
           '# The values `K(n)` of the certificate, as data',
           '',
           'THE F TREE `fTree`: `F(T) = ∑_j a_j D(j - T)` at `T` from 0 to %d, `a_j` the integer numerators of Coeffs.lean and' % (TOP - 1),
           '`D(x) = ∑_l w_l max(x + l, 0)^7`. THE COEFFICIENT TREE `aTree`: `a_m` at `m` from 0 to %d, 0 off %d to %d. THE TABLE' % (TOP - 1, J0, J1),
           'OF `Kt`: the %d pairs `(n, Kt n)`, `Kt n = ∑_j ∑_m a_j a_m kapTilde n (j - n m)`, at each `n` of the certificate, so' % len(kt),
           'that the certificate`s `K(n)` is `Kt n / (80640 n^4 10^34)`, in %d groups. Written by relay tools/b766_kdata.py under' % len(gs),
           '(R376)(4)(d); edited by no hand. The file is data: KFast.lean checks each tree and the table by the kernel`s evaluation.',
           '',
           'The window bank`s sha256, less its final line end: %s' % dig['text_sha'],
           'The certificate bank`s sha256, the file whole: %s' % csha,
           'Coeffs.lean`s sha256, the file whole: %s' % coeff_sha,
           '-/', '',
           'namespace SIDEExplicitFormula',
           'namespace Window', '',
           '/-- A binary tree of integers, read by the bits of an index from the lowest. -/',
           'inductive IntTree where',
           '  | leaf : ℤ → IntTree',
           '  | node : IntTree → IntTree → IntTree', '',
           '/-- The value at index `i`: at a node the even indices go left and the odd right, the index halved. -/',
           'def IntTree.get : IntTree → ℕ → ℤ',
           '  | .leaf v, _ => v',
           '  | .node l r, i => if i % 2 = 0 then IntTree.get l (i / 2) else IntTree.get r (i / 2)', '']
    fd, fn = tree_defs(F, 'f', '`F(T)`')
    ad, an = tree_defs(a[:TOP], 'a', 'The coefficients `a_m`')
    out += fd + ad
    for g, ns in enumerate(gs):
        out.append('/-- The pairs `(n, Kt n)` of group %d, %d `n`. -/' % (g, len(ns)))
        out.append('def ktTab%d : List (ℕ × ℤ) := [' % g)
        for i, n in enumerate(ns):
            out.append('  (%d, %d)%s' % (n, kt[n], ',' if i < len(ns) - 1 else ''))
        out += [']', '']
    out += ['/-- The pairs `(n, Kt n)` at the %d `n` of the certificate. -/' % len(kt),
            'def ktTable : List (ℕ × ℤ) :=', '  ' + ' ++ '.join('ktTab%d' % g for g in range(len(gs))), '',
            'end Window', 'end SIDEExplicitFormula', '']
    return NL.join(out), fn, an


def parse_trees(text, prefix):
    """the subtrees and the top tree of a prefix, parsed from the text; (defs in order, the top tree or None)."""
    blocks = re.findall(r'^def (%sSub\d+|%sTree) : IntTree :=\n(.*?)\n\n' % (prefix, prefix), text, re.M | re.S)
    defs, order = {}, []

    def parse(tok, pos):
        t = tok[pos]
        if t == '(':
            v, pos = parse(tok, pos + 1)
            if tok[pos] != ')':
                raise ValueError('paren')
            return v, pos + 1
        if t == '.node':
            x, pos = parse(tok, pos + 1)
            y, pos = parse(tok, pos)
            return ('N', x, y), pos
        if t == '.leaf':
            x, pos = parse(tok, pos + 1)
            if x[0] != 'I':
                raise ValueError('leaf')
            return ('L', x[1]), pos
        if re.match(r'-?\d+$', t):
            return ('I', int(t)), pos + 1
        return defs[t], pos + 1
    for nm, body in blocks:
        tok = TOKEN.findall(body)
        v, pos = parse(tok, 0)
        if pos != len(tok):
            raise ValueError('trailing')
        defs[nm] = v
        order.append(nm)
    return defs, order


def tget(t, i):
    while t[0] == 'N':
        t = t[1] if i % 2 == 0 else t[2]
        i //= 2
    return t[1]


def read_back(text):
    fdefs, forder = parse_trees(text, 'f')
    adefs, aorder = parse_trees(text, 'a')
    ft, at = fdefs.get('fTree'), adefs.get('aTree')
    Fr = [tget(ft, T) for T in range(TOP)] if ft else []
    Ar = [tget(at, m) for m in range(TOP)] if at else []
    gbl = re.findall(r'^def (ktTab\d+) : List \(ℕ × ℤ\) := \[\n(.*?)\n\]$', text, re.M | re.S)
    kts = [(nm, [(int(n), int(v)) for n, v in re.findall(r'\((\d+), (-?\d+)\)', body)]) for nm, body in gbl]
    tl = re.search(r'^def ktTable : List \(ℕ × ℤ\) :=\n  (.*)$', text, re.M)
    torder = re.findall(r'ktTab\d+', tl.group(1)) if tl else []
    heads = (re.search(r'less its final line end: ([0-9a-f]{64})$', text, re.M),
             re.search(r'certificate bank`s sha256, the file whole: ([0-9a-f]{64})$', text, re.M),
             re.search(r'Coeffs\.lean`s sha256, the file whole: ([0-9a-f]{64})$', text, re.M))
    return dict(F=Fr, A=Ar, ft=ft, at=at, forder=forder, aorder=aorder, kts=kts, torder=torder,
                heads=tuple(h.group(1) if h else None for h in heads))


def model(rb, clist):
    """the Lean's three checks over the text as read back: (recurrence failures by T, the walk's verdict, Kt failures by n)."""
    ft, at = rb['ft'], rb['at']

    def Ff(T):
        return tget(ft, T) if T < TOP else 0

    def aG(m):
        return tget(at, m) if J0 <= m <= J1 else 0

    def locA(T):
        b = T - 3 if T >= 3 else 0
        return sum(aG(b + i) * EVV[i] for i in range(7))
    rec_bad = [T for T in range(J0, J0 + CHUNK_T * NCHUNK)
               if Ff(T) != 4 * Ff(T + 1) - 6 * Ff(T + 2) + 4 * Ff(T + 3) - Ff(T + 4) + locA(T)]
    walk = len(clist) == J1 - J0 + 1 and all(tget(at, J0 + i) == x for i, x in enumerate(clist))

    def gk(n, m):
        return Ff(n * m) - 4 * Ff(n * (m + 1)) + 6 * Ff(n * (m + 2)) - 4 * Ff(n * (m + 3)) + Ff(n * (m + 4))

    def sumDC(f, lo, ln, d):
        if d == 0 or ln <= 1:
            return 0 if ln == 0 else f(lo)
        h = ln // 2
        return sumDC(f, lo, h, d - 1) + sumDC(f, lo + h, ln - h, d - 1)
    kt_bad = []
    for _nm, rows in rb['kts']:
        for n, v in rows:
            if not (n > 0 and sumDC(lambda m: aG(m) * gk(n, m), J0, mtop(n) + 1 - J0, 14) == v):
                kt_bad.append(n)
    return rec_bad, walk, kt_bad


def plant_tree(text, prefix, idx):
    """the text with the leaf at index idx of a tree moved in its last digit; the leaf found by its subtree and the bit-reversed order."""
    r, q = idx % SUBS, idx // SUBS
    k = bitrev(q, SUBH)
    m = re.search(r'^def %sSub%02d : IntTree :=\n(.*?)\n\n' % (prefix, r), text, re.M | re.S)
    s = m.start(1)
    pos = [(s + mm.start(), s + mm.end()) for mm in re.finditer(r'-?\d+', m.group(1))]
    a_, b = pos[k]
    d = text[b - 1]
    return text[:b - 1] + str((int(d) + 1) % 10) + text[b:]


def plant_kt(text, index):
    rows = [mm for mm in re.finditer(r'\((\d+), (-?\d+)\)', text)]
    b = rows[index].end(2)
    d = text[b - 1]
    return text[:b - 1] + str((int(d) + 1) % 10) + text[b:]


def control(text, F, a, kt, gs, K, dig, csha, coeff_sha, clist):
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))
    ns = sorted(K)
    dk = [n for n in ns if Fraction(kt.get(n, 0), DEN * n ** 4 * 10 ** 34) != K[n]]
    c('Kt(n) / (80640 n^4 10^34) against the certificate`s K(n), its own route (no value printed)', 'n %d ; differences %d' % (len(ns), len(dk)),
      len(ns) == 197 and not dk and sorted(kt) == ns)
    fd = [T for T in SAMPLE_T if sum(a[j] * kD(j - T) for j in range(J0, J1 + 1)) != (F[T] if T < TOP else 0)]
    c('F against its definition, the full sum over j, at twelve T', 'differences %d %s' % (len(fd), fd), not fd)
    tri = (ns[0], ns[len(ns) // 2], ns[-1])
    dd = [i for i, n in enumerate(tri) if kt_direct(a, n) != kt[n]]
    c('Kt by the direct double sum with kapTilde at the first, middle and last n', 'differences %d' % len(dd), not dd)
    c('E on -3 .. 3, the spline`s constants (KFast.lean`s evv)', [kE(x) for x in range(-3, 4)], tuple(kE(x) for x in range(-3, 4)) == EVV)
    rb = read_back(text)
    c('the F tree read back from the text, its value at each T against the composed', '%d of %d' % (
        sum(1 for x, y in zip(rb['F'], F) if x == y), TOP), rb['F'] == F)
    c('the coefficient tree read back, at each m against the composed', '%d of %d' % (sum(1 for x, y in zip(rb['A'], a) if x == y), TOP),
      rb['A'] == a[:TOP])
    c('Coeffs.lean`s integers read from the disk against the coefficient tree at 16 .. 16380', 'read %d ; differences %d' % (
        len(clist), sum(1 for i, x in enumerate(clist) if J0 + i < TOP and a[J0 + i] != x)),
      len(clist) == J1 - J0 + 1 and all(a[J0 + i] == x for i, x in enumerate(clist)))
    want_kts = [('ktTab%d' % g, [(n, kt[n]) for n in ns_]) for g, ns_ in enumerate(gs)]
    c('the table of Kt read back, its groups in order and each pair against the composed', '%d groups, %d pairs ; the line names %d' % (
        len(rb['kts']), sum(len(r) for _n, r in rb['kts']), len(rb['torder'])),
      rb['kts'] == want_kts and rb['torder'] == [nm for nm, _r in want_kts])
    c('the head`s three digests (the window bank less its final line end ; the certificate bank whole ; Coeffs.lean whole)',
      tuple((h or '')[:16] for h in rb['heads']), rb['heads'] == (dig['text_sha'], csha, coeff_sha))
    c('the subtrees defined in order before their top tree, in each tree',
      '%d and %d' % (len(rb['forder']), len(rb['aorder'])),
      rb['forder'] == ['fSub%02d' % r for r in range(SUBS)] + ['fTree'] and rb['aorder'] == ['aSub%02d' % r for r in range(SUBS)] + ['aTree'])
    rec_bad, walk, kt_bad = model(rb, clist)
    c('THE LEAN`S CHECKS MODELLED over the text: the recurrence at T from 16 to %d, the walk over Coeffs.lean`s list, the halving sums at each n' % (
        J0 + CHUNK_T * NCHUNK - 1), 'recurrence failures %d ; walk %s ; Kt failures %d' % (len(rec_bad), walk, len(kt_bad)),
      not rec_bad and walk and not kt_bad)
    pf = plant_tree(text, 'f', PLANT_F)
    rbf = read_back(pf)
    pfd = [T for T, (x, y) in enumerate(zip(rbf['F'], F)) if x != y]
    prb = model(rbf, clist)
    c('PLANTED: one leaf of the F tree moved in its last digit, read as one difference at its T, and the modelled recurrence failing',
      '%s ; recurrence failures %d' % (pfd, len(prb[0])), pfd == [PLANT_F] and len(prb[0]) > 0)
    pa = plant_tree(text, 'a', PLANT_A)
    rba = read_back(pa)
    pad = [m for m, (x, y) in enumerate(zip(rba['A'], a)) if x != y]
    c('PLANTED: one leaf of the coefficient tree moved, read as one difference at its m, and the modelled walk failing',
      '%s ; walk %s' % (pad, model(rba, clist)[1]), pad == [PLANT_A] and not model(rba, clist)[1])
    pk = plant_kt(text, PLANT_K)
    rbk = read_back(pk)
    flat = [p for _n, r in rbk['kts'] for p in r]
    pkd = [i for i, n in enumerate(ns) if i < len(flat) and flat[i][1] != kt[n]]
    pkm = model(rbk, clist)[2]
    c('PLANTED: one Kt of the table moved in its last digit, read as one difference at its index, and the modelled sum failing at its n',
      '%s ; Kt failures %s' % (pkd, len(pkm)), pkd == [PLANT_K] and pkm == [ns[PLANT_K]])
    nd, nb = len(DECIMAL.findall(text)), len(BARRED.findall(text))
    c('no decimal literal and no barred word in the text (tools/b766_controls.py`s Lean text check)', 'decimal %d ; barred %d' % (nd, nb), nd == 0 and nb == 0)
    return L, ok


def main(cmd):
    a, dig, csha, K, coeff_sha, clist, RL = bank()
    F = ftable(a)
    ns = sorted(K)
    kt = dict((n, kt_fast(a, F, n)) for n in ns)
    gs = groups(ns)
    text, fn, an = compose(F, a, kt, gs, dig, csha, coeff_sha)
    gterms = [sum(mtop(n) - J0 + 1 for n in g) for g in gs]
    H = ['%s -- (R376)(4)(d) L6 (c): THE VALUES K(n) OF THE CERTIFICATE ENTER THE KERNEL AS DATA, SIDE-explicit-formula %s (%s, %s)' % (
        ACT, REL, cmd, _now()), ''] + RL + [
        '', '## THE FILE COMPOSED',
        '  F(T) at %d T, 0 to %d, the largest %d digits ; the coefficients at %d m, the largest %d digits ; each tree %d subtrees of %d leaves' % (
            len(F), TOP - 1, max(len(str(abs(x))) for x in F), TOP, max(len(str(abs(x))) for x in a), SUBS, TOP // SUBS),
        '  Kt at %d n, %d to %d, the largest %d digits ; the strided terms %d in %d groups (KT_CAP %d), the groups` terms %s and their n %s' % (
            len(kt), min(kt), max(kt), max(len(str(abs(v))) for v in kt.values()), sum(gterms), len(gs), KT_CAP, gterms,
            [len(g) for g in gs]),
        '  lines %d ; bytes %d ; sha256 %s' % (len(text.split(NL)) - 1, len(text.encode('utf-8')), hashlib.sha256(text.encode('utf-8')).hexdigest()[:16])]
    if cmd == 'dry':
        L, ok = control(text, F, a, kt, gs, K, dig, csha, coeff_sha, clist)
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
    L, ok = control(disk, F, a, kt, gs, K, dig, csha, coeff_sha, clist)
    eq = disk == text
    out = H + ['', '## THE FILE ON THE DISK, READ BACK',
               '  %s: bytes %d ; sha256 %s ; carriage returns %d ; equal to the composed text: %s' % (
                   REL, len(disk.encode('utf-8')), hashlib.sha256(disk.encode('utf-8')).hexdigest()[:16], disk.count('\r'), eq),
               '', '## THE CONTROL OVER THE FILE AS WRITTEN'] + L + [
        '', '### ### **THE DATA FILE %s ; THE CONTROL %d OF %d %s ; NO COEFFICIENT, NO F AND NO K(n) PRINTED.**' % (
            'WRITTEN AND READ BACK' if cmd == 'write' else 'READ', sum(ok), len(ok), 'AS WANTED' if all(ok) and eq else 'NOT AS WANTED')]
    print(NL.join(out))
    if cmd == 'write':
        with io.open(BANK, 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(out) + NL)
        print('written data/%s' % os.path.basename(BANK))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '')
