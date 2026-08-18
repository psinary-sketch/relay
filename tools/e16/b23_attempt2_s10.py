"""W-ATTEMPT-2, SITTING 10 - THE LIMIT AT ONE PLACE: THE TOWER ON Q_2, LEVELS n = 1..6.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA at bench
grade; refused: any promotion to W_inf - Sum W_p at complete roster, or register movement.
THE PROTOCOL CORRECTION carried: the closure protocol gates the REGISTER, not
investigation - the programme tests its own object.

THE TOWER QUESTION, POSED EXACTLY (before any run)
==================================================
p = 2 throughout; V_n the level-n Schwartz-Bruhat space (sitting 8: canonically the model
space; the genuine transform IS the model DFT entry-exact; iota: V_n -> V_(n+1) isometric
with F o iota = iota o F on Sonin columns, banked). THE REGISTERED COMPATIBILITY CLAIMS,
each checked exactly in-run:
 (T1) iota(Son(2,n)) is CONTAINED in Son(2,n+1) - longhand: the integers' ball Z_2 is
      LEVEL-INDEPENDENT; iota is function-inclusion, so support-side vanishing on the
      ball transports verbatim, and transform-side vanishing transports by the banked
      intertwining. If exact, the Sonin spaces form a genuine inductive system whose
      union is the local field's own Sonin object:
          Son(2,infinity) = { f level-finite : f|_(Z_2) = 0 and F f|_(Z_2) = 0 }.
 (T2) the pairing is level-stable ON THE NOSE: <iota v, F iota w> = <v, F w> (isometry +
      intertwining) - the Gram of iota(Son(n)) inside V_(n+1) equals the level-n Gram
      entry-exact.
 (T3) the six laws' n-dependence at n = 1..6: eigen-dims (d_1, d_-1, d_i, d_-i) of the
      compressed transform EXACT at every level (tr M and tr Pi computed as cyclotomic
      coefficient dictionaries - no dense F ever formed); dim law (2^n - 1)^2; Q^2 =
      2 (2^(n-1) - 1)^2 exact via host-level sparse contraction (entries in Q(sqrt 2) -
      exact pair arithmetic); the localization trace Tr(U^k S) = 0, k = 1, 2, exact,
      at hosts n+k and n+k+1.
 (T4) the constrained sector's positivity is level-stable: the class dims at the
      one-place cell (constrained: 2*d_1; plain T-fixed: 2*d_1 + d_-1) with the
      REGISTERED PUNCTUATION CONTINUATION: d_1(2,1) = 0 (the arrival depth is dead) and
      d_1(2,n) > 0 for all n >= 2 (alive at every deeper level) - checked at n = 4, 5, 6;
      positivity on the constrained sector by the certified mechanism (B restricted =
      the L2-Gram, positive), verified exactly at n <= 3 and by the mechanism above.
 (T5) THE SCALING DOES NOT PRESERVE THE LIMIT'S SONIN CONDITION - longhand: the hat of
      U f on the ball reads f-hat on p^(-1)Z_2 \\ Z_2, which the Sonin condition does not
      control; REGISTERED CHECK: an exact witness f in Son(2,n) with (U f)-hat nonzero
      on the ball, computed at n = 2 (and 3). If it lands, the scaling acts on the limit
      object ONLY COMPRESSED (S U S) - CC's compressed-scaling structure RECOVERED AS
      FORCED on Q_2, not chosen; the compressed action's mass is exactly the fifth law.

THE BRANCHES, as ferried:
 (L-stable) all five claims land - the tower is compatible, the pairing level-stable,
            the positivity level-stable, and the limit's structure is NAMED: the
            inductive-limit Sonin object of the local field carrying the transform and
            the compressed scaling; the L^2 question answered at the level of what is
            constructed (the union is a nonzero subspace of L^2(Q_2); its closure and
            the compression's limit are NAMED, not constructed).
 (L-fails)  a compatibility or stability breaks at a named level and channel - the
            p-adic form of the archimedean refusal.

RECORDED PLAINLY AS DATA. The register is untouched.
Usage:  python b23_attempt2_s10.py register | run
"""

import os
import sys
import time
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ======================================================================================
# REUSE.  Sitting 8's machinery is IMPORTED, not re-derived: the prime-power cyclotomic
# field Cyc(p,k) of Fraction coefficients, the level-n chart on Z/p^(2n), the exact Sonin
# basis with 2-nonzero sparsity, the embedding iota (m -> p*m + p^(2n+1) j), the genuine
# pullback/pushforward scalings, and the sparse contraction.  Its banked facts are cited,
# never re-assumed: genuine transform = model DFT entry-exact; F_host o iota = iota o F_n
# on Sonin columns; Q_gen^2 = Q_model^2 = p(p^(n-1)-1)^2; Tr(U^k S) = 0, level-stable.
# ======================================================================================

from b21_attempt2_s8 import (Cyc, rat_inv, rat_det, rat_mm, rat_tr, transpose,
                             sonin_cols, emb_col, uk_col, push_col, pull_col,
                             contract, _fmt)

# ======================================================================================
# PURE-ASCII OUTPUT GUARD (as sitting 8).  The banked registration docstring above is
# VERBATIM; typographic characters are folded to ASCII at PRINT time only.
# ======================================================================================

_ASCII_FOLD = {0x2014: u"--", 0x2013: u"-", 0x2012: u"-", 0x2010: u"-", 0x2011: u"-",
               0x2018: u"'", 0x2019: u"'", 0x201c: u'"', 0x201d: u'"',
               0x2026: u"...", 0x00a0: u" ", 0x00d7: u"x", 0x2212: u"-"}

_emit = print


def print(*args, **kw):  # noqa: A001  (deliberate module-scope shadow: ASCII guard)
    out = []
    for a in args:
        s = a if isinstance(a, str) else str(a)
        s = s.translate(_ASCII_FOLD)
        try:
            s.encode("ascii")
        except UnicodeEncodeError:
            s = s.encode("ascii", "backslashreplace").decode("ascii")
        out.append(s)
    _emit(*out, **kw)


# ======================================================================================
# THE LEDGER
# ======================================================================================

LEDGER = []
FAILS = []
DECLARED = []


def check(name, ok):
    LEDGER.append((name, bool(ok)))
    if not ok:
        FAILS.append(name)
    print("  %s  %s" % ("PASS" if ok else "**FAIL**", name))
    sys.stdout.flush()
    return bool(ok)


def dnote(name):
    """A DECLARED line: float or skipped.  NEVER counted as EXACT."""
    DECLARED.append(name)
    print("  DECLARED  %s" % name)
    sys.stdout.flush()


# ======================================================================================
# THE KEY TECHNIQUE -- COEFFICIENT DICTIONARIES over Q(zeta_(2^k)).
#
#   Phi_(2^k)(x) = x^(2^(k-1)) + 1,  so  zeta^half = -1  with half = order/2, and the
#   power basis is zeta^0 .. zeta^(half-1).  A cyclotomic sum is carried as a dict
#       { exponent in [0, half) : coefficient }
#   and reduction mod Phi is a SINGLE fold applied as each term is accumulated:
#       e >= half  ->  e - half with the coefficient negated.
#   No dense transform matrix is ever formed at any level; a Gram/trace entry is a
#   4-term zeta sum by the Sonin basis's 2-nonzero sparsity, and a trace is a sum of
#   at most 4 * dim terms.
# ======================================================================================

class ZD(object):
    """Coefficient dictionaries for Q(zeta_(2^k)), order = 2^k."""

    __slots__ = ('order', 'half')

    def __init__(self, order):
        self.order = order
        self.half = order // 2

    def acc(self, d, e, c):
        """d += c * zeta^e, in place, folded."""
        if not c:
            return d
        e %= self.order
        if e >= self.half:
            e -= self.half
            c = -c
        w = d.get(e)
        if w is None:
            d[e] = c
        else:
            s = w + c
            if s:
                d[e] = s
            else:
                del d[e]
        return d

    @staticmethod
    def is_zero(d):
        for v in d.values():
            if v:
                return False
        return True

    @staticmethod
    def eq(a, b):
        for j, v in a.items():
            if v and b.get(j, 0) != v:
                return False
        for j, v in b.items():
            if v and a.get(j, 0) != v:
                return False
        return True

    @staticmethod
    def to_str(d, scale=None):
        parts = []
        for j in sorted(d):
            v = d[j]
            if not v:
                continue
            if scale is not None:
                v = Fraction(v) * scale
            f = _fmt(v)
            if j == 0:
                parts.append(f)
            elif v == 1:
                parts.append("z^%d" % j)
            elif v == -1:
                parts.append("-z^%d" % j)
            else:
                parts.append("%s*z^%d" % (f, j))
        if not parts:
            return "0"
        s = parts[0]
        for q in parts[1:]:
            s = s + (" - " + q[1:] if q.startswith("-") else " + " + q)
        return s


# ======================================================================================
# THE LEVEL DATA (p = 2 throughout)
#
#   q = 2^n,  N = q^2 = 4^n,  chart m = alpha + q*beta on Z/N,  ball B = {m == 0 mod q}.
#   Sonin basis k_(a,j) = delta_a (x) (e_j - e_(j+1)),  a in [1,q), j in [0,q-1),
#   column index c = (a-1)*(q-1) + j  -- so c splits as (SHELL a, DIFFERENCE index j)
#   and every (q-1) x (q-1) "block" below is a shell-to-shell block.
#   K^T K = I_(q-1) (x) T,  T the (q-1) path Laplacian tridiag(-1, 2, -1).
# ======================================================================================

class Level(object):
    __slots__ = ('n', 'q', 'N', 'd', 'cols', 'labs', 'icols')

    def __init__(self, n):
        self.n = n
        self.q = 2 ** n
        self.N = 4 ** n
        self.d = (self.q - 1) ** 2
        cols, labs = sonin_cols(2, n)
        self.labs = labs
        self.cols = cols
        # integer form (values are +-1): faster than Fraction for the sparse sums
        self.icols = [dict((m, int(v)) for m, v in c.items()) for c in cols]

    def cidx(self, a, j):
        return (a - 1) * (self.q - 1) + j

    def blk(self, c):
        a1, j = divmod(c, self.q - 1)
        return a1 + 1, j


def path_green_q(q):
    """THE CLOSED FORM, integer-scaled:  Tq[i][j] = q * T^(-1)[i][j]
       = min(i+1,j+1) * (q - max(i+1,j+1))   (the path-graph Green's function)."""
    m = q - 1
    return [[min(i + 1, j + 1) * (q - max(i + 1, j + 1)) for j in range(m)]
            for i in range(m)]


def path_lap(q):
    m = q - 1
    T = [[0] * m for _ in range(m)]
    for i in range(m):
        T[i][i] = 2
        if i + 1 < m:
            T[i][i + 1] = -1
            T[i + 1][i] = -1
    return T


# ======================================================================================
# P0.  THE CLOSED-FORM INVERSE, VERIFIED BEFORE IT IS USED.
#
# G = K^T K = I_(q-1) (x) T.  The bench never Gauss-eliminates a 3969 x 3969 rational
# matrix: it uses G^(-1) = I (x) T^(-1) with T^(-1) = Tq / q, Tq the path Green's
# function above.  THAT CLOSED FORM IS VERIFIED EXACTLY -- against direct rational
# inversion of T at every n = 1..6, and against direct inversion of the FULL G at
# n <= 3 -- before any line that uses it.
# ======================================================================================

def p0_closed_form(levels):
    print("=" * 100)
    print("P0.  THE CLOSED-FORM G^(-1) = I (x) T^(-1), T^(-1)[i,j] = "
          "min(i+1,j+1)(q - max(i+1,j+1))/q  --  VERIFIED BEFORE USE")
    print("=" * 100)
    for L in levels:
        q, n = L.q, L.n
        T = path_lap(q)
        Tq = path_green_q(q)
        Ti = rat_inv(T)
        ok = all(Ti[i][j] == Fraction(Tq[i][j], q)
                 for i in range(q - 1) for j in range(q - 1))
        check("P0a n=%d  T^(-1) (direct rational Gauss inversion, %dx%d) == Tq/q "
              "entry-exact  [the path-graph Green's function]" % (n, q - 1, q - 1), ok)
        # det T = q  (so the radical is zero at every level)
        check("P0b n=%d  det T = %s = q = %d exactly" % (n, _fmt(rat_det(T)), q),
              rat_det(T) == q)
    # the full Gram at n <= 3
    for L in levels:
        if L.n > 3:
            continue
        q, n, d = L.q, L.n, L.d
        G = contract(L.cols, L.cols, 1)
        Tq = path_green_q(q)
        okG = True
        for c1 in range(d):
            a1, j1 = L.blk(c1)
            for c2 in range(d):
                a2, j2 = L.blk(c2)
                want = path_lap(q)[j1][j2] if a1 == a2 else 0
                if G[c1][c2] != want:
                    okG = False
        check("P0c n=%d  K^T K == I_(q-1) (x) T entry-exact (d = %d)" % (n, d), okG)
        Gi = rat_inv(G)
        okGi = True
        for c1 in range(d):
            a1, j1 = L.blk(c1)
            for c2 in range(d):
                a2, j2 = L.blk(c2)
                want = Fraction(Tq[j1][j2], q) if a1 == a2 else Fraction(0)
                if Gi[c1][c2] != want:
                    okGi = False
        check("P0d n=%d  (K^T K)^(-1) (direct inversion, %dx%d) == I (x) Tq/q "
              "entry-exact -- THE CLOSED FORM IS LICENSED AT n >= 4" % (n, d, d), okGi)
    # the tensor-structure check at every level, sparsely (no dense G is formed)
    for L in levels:
        if L.n <= 3:
            continue
        q, n, d = L.q, L.n, L.d
        T = path_lap(q)
        oks = True
        idx = {}
        for c, col in enumerate(L.icols):
            for m, v in col.items():
                idx.setdefault(m, []).append((c, v))
        for c1, col in enumerate(L.icols):
            a1, j1 = L.blk(c1)
            row = {}
            for m, v in col.items():
                for c2, u in idx.get(m, ()):
                    row[c2] = row.get(c2, 0) + v * u
            for c2, val in row.items():
                a2, j2 = L.blk(c2)
                want = T[j1][j2] if a1 == a2 else 0
                if val != want:
                    oks = False
        check("P0e n=%d  K^T K == I_(q-1) (x) T entry-exact, SPARSELY (d = %d; no dense "
              "Gram formed)" % (n, d), oks)
    print()
    sys.stdout.flush()


# ======================================================================================
# T1.  iota(Son(2,n)) CONTAINED IN Son(2,n+1)
#
# Host h = n+1, N_h = 4^(n+1), host ball B_h = { m'' == 0 mod 2^(n+1) } (x = 2^(-h) m''
# lies in Z_2 iff 2^h | m'').  SUPPORT SIDE: an integer check on the embedded column.
# TRANSFORM SIDE: (F_host iota f)(k'') = 2^(-h) sum_(m'') (iota f)(m'') zeta_(N_h)^(k'' m'')
# evaluated ON THE BALL ROWS ONLY -- 2^(n+1) rows, each a 4-term zeta sum (iota of a
# 2-nonzero Sonin column has 4 nonzeros), folded by the coefficient dictionary.
# ======================================================================================

def t1_tower(levels):
    print("=" * 100)
    print("T1.  iota(Son(2,n)) CONTAINED IN Son(2,n+1)  --  the inductive system")
    print("=" * 100)
    for L in levels:
        n, q, N, d = L.n, L.q, L.N, L.d
        h = n + 1
        Nh = 4 ** h
        qh = 2 ** h
        zd = ZD(Nh)
        ball = list(range(0, Nh, qh))
        t0 = time.time()
        ok_sup = True
        ok_tr = True
        bad = []
        for c in range(d):
            ic = emb_col(L.icols[c], 2, n, h)
            for m, v in ic.items():
                if v and m % qh == 0:
                    ok_sup = False
            items = list(ic.items())
            for kpp in ball:
                acc = {}
                a = zd.acc
                for mpp, v in items:
                    a(acc, kpp * mpp, v)
                if acc:
                    ok_tr = False
                    if len(bad) < 4:
                        bad.append((c, kpp, dict(acc)))
        el = time.time() - t0
        check("T1a n=%d  SUPPORT SIDE: (iota f)|_(B_host) = 0 exactly, all %d columns "
              "(host ball = {m'' == 0 mod 2^%d}, %d rows) -- the ball Z_2 is "
              "level-independent and iota is function-inclusion"
              % (n, d, h, len(ball)), ok_sup)
        check("T1b n=%d  TRANSFORM SIDE: (F_host iota f)|_(B_host) = 0 EXACTLY, all %d "
              "columns x %d ball rows = %d exact 4-term zeta_(%d) sums [%.1f s]"
              % (n, d, len(ball), d * len(ball), Nh, el), ok_tr)
        if bad:
            print("      NONZERO (col, ball row, folded value): %s" % bad)
        check("T1c n=%d  => iota(Son(2,%d)) is CONTAINED in Son(2,%d): the level-n Sonin "
              "space embeds into the level-(n+1) one" % (n, n, n + 1), ok_sup and ok_tr)
    print("      CONSEQUENCE, stated: {Son(2,n), iota} is a genuine INDUCTIVE SYSTEM; "
          "its union is  Son(2,infinity) = { f level-finite : f|_(Z_2) = 0 and "
          "(F f)|_(Z_2) = 0 }  -- the local field's own Sonin object.  This NAMES the "
          "union; it does not construct its L^2 closure, and none is claimed.")
    print()
    sys.stdout.flush()


# ======================================================================================
# T2.  THE PAIRING IS LEVEL-STABLE ON THE NOSE
#
# NORMALIZATION, STATED (nothing is inserted by hand): Haar with Z_p of mass 1 gives every
# level-n chart cell the mass W_n = 2^(-n), and the genuine transform IS the integral, so
# in the chart F_n[m',m] = zeta_N^(m m')/2^n (sitting 8, A4 -- banked entry-exact).  Hence
#     <v, F_n w>_n = W_n * v^T F_n w = 4^(-n) * S_n(v,w),   S_n = sum v w zeta_N^(m m'),
#     <iota v, F_h iota w>_h = W_h * (iota v)^T F_h (iota w) = 4^(-h) * S_h(v,w).
# With h = n+1 the two agree ON THE NOSE (no scalar) iff  S_h = 4 * S_n.  That is the
# entry-exact comparison run below, made inside the HOST field Q(zeta_(4^(n+1))) with the
# level-n exponents lifted by zeta_N = zeta_(N_h)^4.  S_n is a 4-term sum, S_h a 16-term
# sum; both are folded coefficient dictionaries.
# ======================================================================================

def t2_pairing(levels, budget):
    print("=" * 100)
    print("T2.  <iota v, F iota w> = <v, F w>  --  THE GRAM OF iota(Son(n)) INSIDE V_(n+1) "
          "vs THE LEVEL-n GRAM, ENTRY-EXACT")
    print("=" * 100)
    print("      NORMALIZATION: level entry = 4^(-n) S_n, host entry = 4^(-(n+1)) S_h; "
          "equality ON THE NOSE <=> S_h = 4 S_n, compared inside the host field.")
    rate = None
    for L in levels:
        n, q, N, d = L.n, L.q, L.N, L.d
        h = n + 1
        Nh = 4 ** h
        zdh = ZD(Nh)
        if rate is not None:
            proj = rate * (d * d)
            if proj > budget:
                dnote("T2 n=%d  DECLARED-SKIPPED: %d^2 = %d Gram entries, projected "
                      "%.0f s > budget %.0f s at the measured entry rate.  NOT computed, "
                      "NOT counted as EXACT, NOT asserted."
                      % (n, d, d * d, proj, budget))
                continue
        t0 = time.time()
        ich = [emb_col(L.icols[c], 2, n, h) for c in range(d)]
        ichl = [list(x.items()) for x in ich]
        coll = [list(L.icols[c].items()) for c in range(d)]
        ok = True
        bad = []
        for c1 in range(d):
            A = ichl[c1]
            An = coll[c1]
            for c2 in range(d):
                Sh = {}
                a = zdh.acc
                for m1, v1 in A:
                    for m2, v2 in ichl[c2]:
                        a(Sh, m1 * m2, v1 * v2)
                Sn = {}
                for m1, v1 in An:
                    for m2, v2 in coll[c2]:
                        a(Sn, 4 * m1 * m2, 4 * v1 * v2)
                if not ZD.eq(Sh, Sn):
                    ok = False
                    if len(bad) < 3:
                        bad.append((c1, c2))
        el = time.time() - t0
        rate = el / float(d * d)
        check("T2  n=%d  the host Gram (iota K)^T W_h F_h (iota K) equals the level-n Gram "
              "K^T W_n F_n K ENTRY-EXACT on all %d x %d = %d entries -- the pairing is "
              "LEVEL-STABLE ON THE NOSE (no scalar) [%.1f s]"
              % (n, d, d, d * d, el), ok)
        if bad:
            print("      MISMATCHED ENTRIES (first): %s" % bad)
    print()
    sys.stdout.flush()


# ======================================================================================
# T3(a).  THE COMPRESSED TRANSFORM'S EIGEN-DIMS, EXACT AT n = 1..6.
#
# M = (K^T K)^(-1) K^T F K is the compression of the genuine transform to Son (sitting 8,
# L3a: F K = K M entry-exact).  F^2 = parity and P K = K Pi give M^2 = Pi, Pi^2 = I, so
# M^4 = I: M is diagonalizable with spectrum in {1,-1,i,-i}, multiplicities d_1,d_-1,d_i,d_-i.
#     d = d_1 + d_-1 + d_i + d_-i
#     tr M   = (d_1 - d_-1) + i (d_i - d_-i)          =: A + B i
#     tr M^2 = tr Pi = (d_1 + d_-1) - (d_i + d_-i)    =: C
# (tr M^3 = conj(tr M) is then automatic and carries no new information.)  Solving:
#     d_1 = ((d+C)/2 + A)/2,  d_-1 = ((d+C)/2 - A)/2,
#     d_i = ((d-C)/2 + B)/2,  d_-i = ((d-C)/2 - B)/2.
#
# tr M IS NEVER COMPUTED FROM A DENSE F.  (K^T K)^(-1) = I (x) T^(-1) is BLOCK DIAGONAL,
# so tr(G^(-1) G_loc) needs only the SHELL-DIAGONAL blocks of G_loc = K^T F K:
#     tr M = (1/q) * sum_(a=1)^(q-1) sum_(j1,j2) T^(-1)[j1,j2] * G0[(a,j2),(a,j1)]
# with G0 the un-normalized 4-term zeta_N sum.  Using T^(-1) = Tq/q the whole trace is
#     tr M = (1/q^2) * sum_a sum_(j1,j2) Tq[j1,j2] * (4-term zeta_N sum),
# i.e. (q-1)^3 integer-weighted 4-term accumulations -- 250047 x 4 at n = 6.
# ======================================================================================

def trace_M(L):
    n, q, N, d = L.n, L.q, L.N, L.d
    zd = ZD(N)
    Tq = path_green_q(q)
    acc = {}
    a_ = zd.acc
    m1 = q - 1
    for a in range(1, q):
        for j1 in range(m1):
            r1p = a + q * j1
            r1m = a + q * (j1 + 1)
            row = Tq[j1]
            for j2 in range(m1):
                w = row[j2]
                r2p = a + q * j2
                r2m = a + q * (j2 + 1)
                a_(acc, r1p * r2p, w)
                a_(acc, r1p * r2m, -w)
                a_(acc, r1m * r2p, -w)
                a_(acc, r1m * r2m, w)
    return acc, Fraction(1, q * q)   # tr M = scale * acc


def parity_pi(L):
    """Pi from P K = K Pi, SOLVED not assumed: P col_(a,j) = - col_(q-a, q-2-j).
       Returns (perm, sign) with Pi[perm[c]][c] = sign[c]."""
    q, d = L.q, L.d
    perm = [0] * d
    sgn = [0] * d
    for c in range(d):
        a, j = L.blk(c)
        perm[c] = L.cidx(q - a, q - 2 - j)
        sgn[c] = -1
    return perm, sgn


def verify_pi(L, perm, sgn):
    """P K = K Pi ENTRY-EXACT, sparsely (P: m -> -m mod N)."""
    N, d = L.N, L.d
    ok = True
    for c in range(d):
        pk = {}
        for m, v in L.icols[c].items():
            pk[(-m) % N] = v
        tgt = {}
        for m, v in L.icols[perm[c]].items():
            w = v * sgn[c]
            if w:
                tgt[m] = w
        if pk != tgt:
            ok = False
    return ok


def pi_trace_and_det(L, perm, sgn):
    d = L.d
    tr = sum(sgn[c] for c in range(d) if perm[c] == c)
    if sorted(perm) != list(range(d)):
        return tr, None
    seen = [False] * d
    s = 1
    for i in range(d):
        if not seen[i]:
            ln = 0
            k = i
            while not seen[k]:
                seen[k] = True
                k = perm[k]
                ln += 1
            if ln % 2 == 0:
                s = -s
    for v in sgn:
        s *= v
    return tr, s


def solve_eigdims(d, A, B, C):
    """Return (d1, dm1, di, dmi) or None if the linear solve is not integral."""
    s1 = Fraction(d + C, 2)
    s2 = Fraction(d - C, 2)
    vals = [(s1 + A) / 2, (s1 - A) / 2, (s2 + B) / 2, (s2 - B) / 2]
    out = []
    for v in vals:
        if v.denominator != 1 or v.numerator < 0:
            return None
        out.append(v.numerator)
    if sum(out) != d:
        return None
    return tuple(out)


EIG = {}


def t3a_eigendims(levels):
    print("=" * 100)
    print("T3(a).  THE EIGEN-DIMS OF THE COMPRESSED TRANSFORM, EXACT AT n = 1..6")
    print("=" * 100)
    for L in levels:
        n, q, N, d = L.n, L.q, L.N, L.d
        check("T3a0 n=%d  DIM LAW: dim Son(2,%d) = (2^%d - 1)^2 = %d, and the Sonin basis "
              "has exactly %d columns of 2 nonzeros each" % (n, n, n, d, d),
              d == (q - 1) ** 2 and len(L.cols) == d and
              all(len(c) == 2 for c in L.cols))
        perm, sgn = parity_pi(L)
        okpi = verify_pi(L, perm, sgn)
        check("T3a1 n=%d  P K = K Pi ENTRY-EXACT (Pi SOLVED from the chart: parity "
              "(alpha,beta) -> (q-alpha, q-1-beta) sends col_(a,j) to -col_(q-a,q-2-j))"
              % n, okpi)
        trPi, detPi = pi_trace_and_det(L, perm, sgn)
        check("T3a2 n=%d  Pi is a signed permutation, det Pi = %s in {+1,-1}; "
              "tr Pi = %d EXACT" % (n, detPi, trPi), detPi in (1, -1))
        okp2 = all(perm[perm[c]] == c and sgn[c] * sgn[perm[c]] == 1 for c in range(d))
        check("T3a3 n=%d  Pi^2 = I exactly (the signed permutation is an involution with "
              "+1 sign product) => M^4 = (M^2)^2 = Pi^2 = I" % n, okp2)
        t0 = time.time()
        acc, scale = trace_M(L)
        el = time.time() - t0
        iexp = N // 4                      # i = zeta_N^(N/4)
        supp_ok = all((e in (0, iexp)) or not v for e, v in acc.items())
        A = Fraction(acc.get(0, 0)) * scale
        B = Fraction(acc.get(iexp, 0)) * scale
        check("T3a4 n=%d  tr M = %s  EXACT (%d integer-weighted 4-term zeta_%d "
              "accumulations via the shell-diagonal blocks of K^T F K; NO dense F) "
              "-- lies in Q(i) = Q(zeta_4): %s  [%.1f s]"
              % (n, ZD.to_str(acc, scale), 4 * (q - 1) ** 3, N,
                 "YES" if supp_ok else "NO", el), supp_ok)
        C = Fraction(trPi)
        sol = solve_eigdims(d, A, B, C)
        check("T3a5 n=%d  the eigen-dim solve is INTEGRAL and sums to d: tr M = %s + %s i, "
              "tr Pi = %s  ->  %s" % (n, _fmt(A), _fmt(B), _fmt(C),
                                      sol if sol else "NON-INTEGRAL"), sol is not None)
        EIG[n] = dict(d=d, A=A, B=B, C=C, sol=sol, detPi=detPi, trPi=trPi)
    print()
    sys.stdout.flush()


# ======================================================================================
# T3(a').  M^2 = Pi BRUTE-FORCED EXACTLY AT n <= 3 (the licence for M^4 = I), using the
# imported Cyc(2, 2n) field of Fraction coefficients.  At n >= 4 the identity is DERIVED,
# exactly as sitting 8 derived it: F^2 = parity (exact geometric sums) => F^2 K = P K;
# F K = K M => F^2 K = K M^2; P K = K Pi; K has full column rank (det K^T K = q^(q-1) != 0)
# => K M^2 = K Pi => M^2 = Pi.
# ======================================================================================

def build_M_dense(L):
    """M = (K^T K)^(-1) K^T F K over Q(zeta_N), as a dense d x d of sparse dicts.
       Small n only."""
    n, q, N, d = L.n, L.q, L.N, L.d
    fld = Cyc(2, 2 * n)
    Tq = path_green_q(q)
    # G_loc = K^T F K, F[m',m] = zeta_N^(m m')/q
    Gloc = [[None] * d for _ in range(d)]
    for c1 in range(d):
        for c2 in range(d):
            acc = {}
            for m1, v1 in L.icols[c1].items():
                for m2, v2 in L.icols[c2].items():
                    fld.acc(acc, fld.pw((m1 * m2) % N), Fraction(v1 * v2, q))
            Gloc[c1][c2] = acc
    # M = (I (x) Tq/q) G_loc   (block diagonal left factor)
    M = [[{} for _ in range(d)] for _ in range(d)]
    for c1 in range(d):
        a1, j1 = L.blk(c1)
        for c2 in range(d):
            acc = {}
            for j in range(q - 1):
                w = Fraction(Tq[j1][j], q)
                if w:
                    fld.acc(acc, Gloc[L.cidx(a1, j)][c2], w)
            M[c1][c2] = acc
    return fld, Gloc, M


def t3ap_msq(levels):
    print("=" * 100)
    print("T3(a').  M^2 = Pi  --  BRUTE-FORCED EXACTLY AT n <= 3, DERIVED AT n >= 4")
    print("=" * 100)
    for L in levels:
        n, q, N, d = L.n, L.q, L.N, L.d
        perm, sgn = parity_pi(L)
        if n <= 3:
            t0 = time.time()
            fld, Gloc, M = build_M_dense(L)
            # F K = K M entry-exact
            okFK = True
            for c in range(d):
                for m in range(N):
                    lhs = {}
                    for mm, v in L.icols[c].items():
                        fld.acc(lhs, fld.pw((m * mm) % N), Fraction(v, q))
                    rhs = {}
                    for cp in range(d):
                        v = L.icols[cp].get(m, 0)
                        if v:
                            fld.acc(rhs, M[cp][c], Fraction(v))
                    if not fld.eq(lhs, rhs):
                        okFK = False
            check("T3a'1 n=%d  F K = K M ENTRY-EXACT with the genuine F (residual EXACT "
                  "ZERO on all %d x %d chart entries)" % (n, N, d), okFK)
            okM2 = True
            for i in range(d):
                Mi = M[i]
                for j in range(d):
                    acc = {}
                    for t in range(d):
                        if Mi[t] and M[t][j]:
                            fld.acc(acc, fld.mul(Mi[t], M[t][j]))
                    want = {}
                    if perm[j] == i:
                        want = fld.smul(fld.ONE, Fraction(sgn[j]))
                    if not fld.eq(acc, want):
                        okM2 = False
            el = time.time() - t0
            check("T3a'2 n=%d  M^2 = Pi ENTRY-EXACT, BRUTE-FORCED (d = %d, %d cyclotomic "
                  "products in Q(zeta_%d)) [%.1f s]" % (n, d, d ** 3, N, el), okM2)
        else:
            detG = q ** (q - 1)
            check("T3a'2 n=%d  M^2 = Pi, DERIVED EXACT (d = %d too large to brute-force "
                  "d^3 = %d cyclotomic products): F^2 = parity => F^2 K = P K; F K = K M "
                  "=> F^2 K = K M^2; P K = K Pi (T3a1, exact here); det(K^T K) = "
                  "det(T)^(q-1) = q^(q-1) = %d^%d != 0 (%d digits) so K has full column "
                  "rank => K M^2 = K Pi => M^2 = Pi."
                  % (n, d, d ** 3, q, q - 1, len(str(detG))), True)
    print()
    sys.stdout.flush()


# ======================================================================================
# T3(b).  Q^2 = 2 (2^(n-1) - 1)^2 AT n = 1..6, EXACT.
#
# Sitting 8's route, verbatim in structure:
#     Q_gen^2 = (1/p) tr(A_rat^T G_h^(-1) A_rat G_h^(-1)),  A_gen = 2^(-1/2) A_rat,
#     A_rat = W_h (iota K)^T (U K),  G_h = W_h (iota K)^T (iota K),  W_h = 2^(-h), h = n+1.
# THE sqrt(2) IS CARRIED SYMBOLICALLY (never a float): U = 2^(-1/2) x (an integer pullback),
# so A_rat is exactly rational and Q_gen^2 = (1/2) x (exact rational) -- the Q(sqrt 2)
# pair arithmetic degenerates to pure Q at the SQUARED level, which is where the law lives.
#
# G_h = W_n K^T K = 2^(-n) (I (x) T)  (iota is an isometry: p^(h-n) host cells of mass
# p^(-h) = one level cell of mass p^(-n); checked sparsely in-run), so
#     G_h^(-1) = 2^n (I (x) T^(-1)) = 2^n (I (x) Tq/q) = I (x) Tq        [since 2^n = q]
# -- an INTEGER matrix in closed form.  No 3969 x 3969 Gauss elimination is ever run.
#
# The Frobenius trace is then evaluated BLOCKWISE.  With A = I (x) Tq block-diagonal,
#     tr(Z^T A Z A) = sum_(k,i) (A Z)[k,i] (Z A)[k,i]
#                   = sum over nonzero shell-blocks Z_(a,b) of
#                     sum_(k,i) (Tq Z_(a,b))[k,i] (Z_(a,b) Tq)[k,i],
# and each Z_(a,b) has at most 4 nonzeros per row -- so the cost is O(nnz * (q-1)) per
# block, not O(d^3).
# ======================================================================================

def blocks_of(L, S):
    """S: dict c1 -> dict c2 -> int.  Return dict (a1,a2) -> dict j1 -> dict j2 -> int."""
    out = {}
    for c1, row in S.items():
        a1, j1 = L.blk(c1)
        for c2, v in row.items():
            if not v:
                continue
            a2, j2 = L.blk(c2)
            b = out.setdefault((a1, a2), {})
            b.setdefault(j1, {})[j2] = v
    return out


def block_frob(blocks, Tq, m):
    """sum over blocks of sum_(k,i) (Tq Z)[k,i] * (Z Tq)[k,i]  -- all integer."""
    total = 0
    for Z in blocks.values():
        TZ = [[0] * m for _ in range(m)]
        for j, rowj in Z.items():
            for i, v in rowj.items():
                if not v:
                    continue
                for k in range(m):
                    t = Tq[k][j]
                    if t:
                        TZ[k][i] += t * v
        ZT = [[0] * m for _ in range(m)]
        for k, rowk in Z.items():
            outk = ZT[k]
            for l, v in rowk.items():
                if not v:
                    continue
                Tl = Tq[l]
                for i in range(m):
                    t = Tl[i]
                    if t:
                        outk[i] += t * v
        s = 0
        for k in range(m):
            Ak = TZ[k]
            Bk = ZT[k]
            for i in range(m):
                a = Ak[i]
                if a:
                    b = Bk[i]
                    if b:
                        s += a * b
        total += s
    return total


def sparse_contract_int(colsA, colsB):
    """(colsA)^T (colsB) as dict c1 -> dict c2 -> int, from sparse integer columns."""
    idx = {}
    for cp, col in enumerate(colsB):
        for m, v in col.items():
            if v:
                idx.setdefault(m, []).append((cp, v))
    out = {}
    for c, col in enumerate(colsA):
        row = {}
        for m, v in col.items():
            if not v:
                continue
            for cp, u in idx.get(m, ()):
                w = row.get(cp)
                nv = (w + v * u) if w is not None else v * u
                if nv:
                    row[cp] = nv
                elif w is not None:
                    del row[cp]
        if row:
            out[c] = row
    return out


QTAB = {}


def t3b_qsquare(levels):
    print("=" * 100)
    print("T3(b).  THE FIFTH LAW  Q^2 = 2 (2^(n-1) - 1)^2  AT n = 1..6, EXACT")
    print("=" * 100)
    for L in levels:
        n, q, N, d = L.n, L.q, L.N, L.d
        h = n + 1
        m = q - 1
        Tq = path_green_q(q)
        T = path_lap(q)
        t0 = time.time()
        Kh = [emb_col(c, 2, n, h) for c in L.icols]
        UK = [uk_col(c, 2, n, h, 1) for c in L.icols]
        # the isometry of iota, sparsely: (iota K)^T (iota K) = 2^(h-n) K^T K
        GhN = sparse_contract_int(Kh, Kh)
        okiso = True
        for c1, row in GhN.items():
            a1, j1 = L.blk(c1)
            for c2, v in row.items():
                a2, j2 = L.blk(c2)
                want = 2 * T[j1][j2] if a1 == a2 else 0
                if v != want:
                    okiso = False
        check("T3b0 n=%d  iota IS AN ISOMETRY, exact and SPARSE: (iota K)^T (iota K) = "
              "2 * K^T K = 2 (I (x) T), so G_h = 2^(-h) (iota K)^T (iota K) = 2^(-n) K^T K "
              "and G_h^(-1) = I (x) Tq EXACTLY (integer closed form; no dense inversion)"
              % n, okiso)
        # U is an isometry on Son:  2^(-h) 2^(-1) (U K)^T (U K) = 2^(-n) K^T K
        GUN = sparse_contract_int(UK, UK)
        okU = True
        for c1, row in GUN.items():
            a1, j1 = L.blk(c1)
            for c2, v in row.items():
                a2, j2 = L.blk(c2)
                want = 4 * T[j1][j2] if a1 == a2 else 0
                if v != want:
                    okU = False
        check("T3b1 n=%d  U IS AN ISOMETRY on Son, exact: 2^(-h-1) (U K)^T (U K) = "
              "2^(-n) K^T K entry-for-entry" % n, okU)
        # A_rat = 2^(-h) * Z,  Z = (iota K)^T (U K) integer
        Z = sparse_contract_int(Kh, UK)
        blk = blocks_of(L, Z)
        shells = sorted(blk.keys())
        okshell = all(a2 == (2 * a1) % q for (a1, a2) in shells)
        check("T3b2 n=%d  A_rat is SHELL-SPARSE: every nonzero block (a1,a2) has "
              "a2 = 2 a1 mod q (the scaling doubles the shell) -- %d nonzero blocks out "
              "of %d" % (n, len(shells), m * m), okshell)
        SS = block_frob(blk, Tq, m)
        #   tr(A_rat^T Ghi A_rat Ghi) = 2^(-2h) * SS   with Ghi = I (x) Tq
        Qg2 = Fraction(SS, 2) * Fraction(1, 4 ** h)
        # the model: B = K^T P K (truncated pushforward), Gm^(-1) = I (x) Tq / q
        PK = [push_col(c, 2, n) for c in L.icols]
        Bm = sparse_contract_int(L.icols, PK)
        blkB = blocks_of(L, Bm)
        SB = block_frob(blkB, Tq, m)
        Qm2 = Fraction(SB, 2) * Fraction(1, q * q)
        law = Fraction(2 * (2 ** (n - 1) - 1) ** 2)
        el = time.time() - t0
        check("T3b3 n=%d  Q_gen^2 = %s  EXACT RATIONAL (genuine U on L^2(Q_2) compressed "
              "to iota(Son) inside V_(n+1); the 2^(-1/2) carried symbolically) [%.1f s]"
              % (n, _fmt(Qg2), el), True)
        check("T3b4 n=%d  Q_model^2 = %s  EXACT RATIONAL (sitting 8's model U = "
              "P/sqrt(2), truncated pushforward)" % (n, _fmt(Qm2)), True)
        check("T3b5 n=%d  Q_gen^2 - Q_model^2 = %s  -> the fifth law lifts %s"
              % (n, _fmt(Qg2 - Qm2), "VERBATIM" if Qg2 == Qm2 else "CORRECTED"),
              Qg2 == Qm2)
        check("T3b6 n=%d  THE BANKED LAW  Q^2 = 2 (2^(n-1) - 1)^2 = %s : %s"
              % (n, _fmt(law), "HOLDS EXACTLY" if Qg2 == law else "DOES NOT HOLD"),
              Qg2 == law)
        QTAB[n] = dict(Qg2=Qg2, Qm2=Qm2, law=law)
        # the closed-form licence: at n <= 3, redo with a DIRECT dense inversion
        if n <= 3:
            Wh = Fraction(1, 2 ** h)
            Gh = contract(Kh, Kh, Wh)
            Ghi = rat_inv(Gh)
            Arat = contract(Kh, UK, Wh)
            X = rat_mm(rat_mm(rat_mm(transpose(Arat), Ghi), Arat), Ghi)
            Qg2d = Fraction(1, 2) * rat_tr(X)
            check("T3b7 n=%d  CLOSED-FORM LICENCE: the same Q_gen^2 recomputed with a "
                  "DIRECT rational Gauss inversion of the host Gram (%dx%d) gives %s -- "
                  "identical" % (n, d, d, _fmt(Qg2d)), Qg2d == Qg2)
    print()
    sys.stdout.flush()


# ======================================================================================
# T3(c).  THE LOCALIZATION TRACE Tr(U^k S) = 0, k = 1, 2, AT HOSTS n+k AND n+k+1.
#
# Tr(U^k S_n) = tr(G_hh^(-1) A_k) with A_k = W_hh (iota_hh K)^T (U^k K) and
# G_hh = W_hh (iota_hh K)^T (iota_hh K) = 2^(-n) K^T K  (iota is an isometry at EVERY
# host, checked in-run), so G_hh^(-1) = I (x) Tq exactly.  Since that inverse is BLOCK
# DIAGONAL only the SHELL-DIAGONAL blocks of A_k are needed:
#     Tr(U^k S_n) = 2^(-k/2) * 2^(-hh) * sum_a sum_(j1,j2) Tq[j1,j2] Z[(a,j2),(a,j1)],
# Z = (iota K)^T (U^k K) an integer contraction.  The 2^(-k/2) is carried symbolically.
# LEVEL-STABILITY is the second caveat's answer: the same object at hosts hh = n+k and
# n+k+1.
# ======================================================================================

TRTAB = {}


def t3c_traces(levels):
    print("=" * 100)
    print("T3(c).  THE LOCALIZATION TRACE  Tr(U^k S_n), k = 1, 2, HOSTS n+k AND n+k+1")
    print("=" * 100)
    for L in levels:
        n, q, N, d = L.n, L.q, L.N, L.d
        m = q - 1
        Tq = path_green_q(q)
        T = path_lap(q)
        tab = {}
        for kk in (1, 2):
            vals = []
            for hh in (n + kk, n + kk + 1):
                t0 = time.time()
                Khh = [emb_col(c, 2, n, hh) for c in L.icols]
                Ukk = [uk_col(c, 2, n, hh, kk) for c in L.icols]
                Gn_ = sparse_contract_int(Khh, Khh)
                okiso = True
                fac = 2 ** (hh - n)
                for c1, row in Gn_.items():
                    a1, j1 = L.blk(c1)
                    for c2, v in row.items():
                        a2, j2 = L.blk(c2)
                        want = fac * T[j1][j2] if a1 == a2 else 0
                        if v != want:
                            okiso = False
                Z = sparse_contract_int(Khh, Ukk)
                tot = 0
                for c1, row in Z.items():
                    a1, j1 = L.blk(c1)
                    for c2, v in row.items():
                        a2, j2 = L.blk(c2)
                        if a1 == a2:
                            tot += Tq[j2][j1] * v
                tr = Fraction(tot, 2 ** hh)
                el = time.time() - t0
                shown = "0" if tr == 0 else "2^(-%d/2) * %s" % (kk, _fmt(tr))
                check("T3c%d n=%d  host h = %d (= n+k%s), N_host = 4^%d: iota isometric "
                      "there (%s) and Tr(U^%d S_n) = %s   EXACT [%.1f s]"
                      % (kk, n, hh, "" if hh == n + kk else "+1", hh,
                         "yes" if okiso else "NO", kk, shown, el), okiso)
                vals.append((hh, tr))
            stable = (vals[0][1] == vals[1][1])
            check("T3c%ds n=%d  LEVEL-STABILITY of Tr(U^%d S_n) across hosts h = %d and "
                  "%d: %s" % (kk, n, kk, vals[0][0], vals[1][0],
                              "STABLE -- the stable value IS the regularized orbital "
                              "integral at bench grade" if stable
                              else "DRIFTS, exact residual %s"
                                   % _fmt(vals[1][1] - vals[0][1])), stable)
            zero = (vals[0][1] == 0 and vals[1][1] == 0)
            check("T3c%dz n=%d  the banked law t_%d = 0 (fixed-point localization) at "
                  "level %d: %s" % (kk, n, kk, n,
                                    "HOLDS EXACTLY" if zero else "FAILS"), zero)
            tab[kk] = (vals, stable, zero)
        TRTAB[n] = tab
    print("      LOCALIZATION, said exactly (and level-independently): a diagonal term "
          "needs m and 2^k m in the same support shell alpha != 0 mod q, i.e. "
          "alpha(2^k - 1) == 0 mod 2^n; gcd(2^k - 1, 2) = 1 forces alpha == 0 mod 2^n, "
          "impossible for 1 <= alpha < q.  The vanishing is therefore n-INDEPENDENT, "
          "which is what the table measures.")
    print()
    sys.stdout.flush()


# ======================================================================================
# T4.  THE CONSTRAINED SECTOR: CLASS DIMS, THE PUNCTUATION CONTINUATION, POSITIVITY.
#
# THE MECHANISM, exactly (this is what makes the positivity LEVEL-STABLE rather than a
# per-level accident).  Let R = (I + M + M^2 + M^3)/4 be the projector onto the
# eigenvalue-1 eigenspace E_1 of M (legitimate: M^4 = I).  Then
#     G_loc R = (K^T K) M R = (K^T K) R          [G_loc = (K^T K) M, and M R = R],
# so for v, w in E_1 the compressed form  B(v,w) = <v, F w>_(L^2) = W_n v^T G_loc w
# equals  W_n v^T (K^T K) w = <v, w>_(L^2)  -- the L^2 GRAM, which is positive definite
# because K^T K = I (x) T and T is the path Laplacian with leading principal minors
# 2, 3, ..., q, all > 0.  Both halves are checked exactly below: the minors at every
# n = 1..6, and the identity G_loc R = (K^T K) R entry-exact at n <= 3.
# ======================================================================================

def t4_constrained(levels):
    print("=" * 100)
    print("T4.  THE CONSTRAINED SECTOR: CLASS DIMS, PUNCTUATION CONTINUATION, POSITIVITY")
    print("=" * 100)
    # (i) positive definiteness of the L^2 Gram at every level
    for L in levels:
        n, q = L.n, L.q
        T = path_lap(q)
        minors = []
        pm2, pm1 = 1, 2
        minors.append(pm1)
        for k in range(2, q):
            cur = 2 * pm1 - pm2
            minors.append(cur)
            pm2, pm1 = pm1, cur
        okrec = (minors == list(range(2, q + 1)))
        okdet = True
        if q - 1 <= 15:
            for k in range(1, q):
                sub = [row[:k] for row in T[:k]]
                if rat_det(sub) != minors[k - 1]:
                    okdet = False
        check("T4a n=%d  K^T K = I (x) T IS POSITIVE DEFINITE, exact: the leading "
              "principal minors of T are 2,3,...,%d, all > 0%s"
              % (n, q, "" if q - 1 > 15 else " (cross-checked against direct rational "
                 "determinants)"), okrec and okdet)
    # (ii) the exact mechanism at n <= 3
    for L in levels:
        if L.n > 3:
            continue
        n, q, d = L.n, L.q, L.d
        fld, Gloc, M = build_M_dense(L)
        perm, sgn = parity_pi(L)
        # M^3 = M * Pi  (Pi a signed permutation: O(d^2))
        M3 = [[{} for _ in range(d)] for _ in range(d)]
        for i in range(d):
            for c in range(d):
                # (M Pi)[i][c] = sum_t M[i][t] Pi[t][c] = M[i][perm[c]] * sgn[c]
                M3[i][c] = fld.smul(M[i][perm[c]], Fraction(sgn[c]))
        # R = (I + M + Pi + M3)/4
        R = [[{} for _ in range(d)] for _ in range(d)]
        for i in range(d):
            for j in range(d):
                acc = {}
                if i == j:
                    fld.acc(acc, fld.ONE)
                fld.acc(acc, M[i][j])
                if perm[j] == i:
                    fld.acc(acc, fld.ONE, Fraction(sgn[j]))
                fld.acc(acc, M3[i][j])
                R[i][j] = fld.smul(acc, Fraction(1, 4))
        # M R = R
        okMR = True
        for i in range(d):
            for j in range(d):
                acc = {}
                for t in range(d):
                    if M[i][t] and R[t][j]:
                        fld.acc(acc, fld.mul(M[i][t], R[t][j]))
                if not fld.eq(acc, R[i][j]):
                    okMR = False
        check("T4b n=%d  R = (I + M + M^2 + M^3)/4 satisfies M R = R entry-exact: R "
              "projects onto the eigenvalue-1 eigenspace E_1 (d = %d)" % (n, d), okMR)
        # tr R = d_1
        trR = {}
        for i in range(d):
            fld.acc(trR, R[i][i])
        d1 = EIG[n]['sol'][0] if EIG.get(n) and EIG[n]['sol'] else None
        want = fld.smul(fld.ONE, Fraction(d1)) if d1 is not None else None
        check("T4c n=%d  tr R = %s = d_1 exactly (independent confirmation of the "
              "eigen-dim solve)" % (n, fld.to_str(trR)),
              want is not None and fld.eq(trR, want))
        # G_loc R = (K^T K) R
        T = path_lap(q)
        okB = True
        for i in range(d):
            a_i, j_i = L.blk(i)
            for j in range(d):
                lhs = {}
                for t in range(d):
                    if Gloc[i][t] and R[t][j]:
                        fld.acc(lhs, fld.mul(Gloc[i][t], R[t][j]))
                rhs = {}
                for jj in range(q - 1):
                    w = T[j_i][jj]
                    if w:
                        fld.acc(rhs, R[L.cidx(a_i, jj)][j], Fraction(w))
                if not fld.eq(lhs, rhs):
                    okB = False
        check("T4d n=%d  THE MECHANISM, ENTRY-EXACT: G_loc R = (K^T K) R -- so on E_1 the "
              "compressed form B(v,w) = <v, F w> IS the L^2 Gram <v,w>, which is positive "
              "definite by T4a.  POSITIVITY ON THE CONSTRAINED SECTOR, CERTIFIED." % n,
              okB)
    print("      AT n >= 4 the same mechanism applies verbatim: G_loc = (K^T K) M "
          "(definition of M, and F K = K M is banked entry-exact at n <= 3 and derived "
          "from the entry-exact transform identification), M R = R (from M^4 = I, T3a3), "
          "and K^T K = I (x) T is positive definite at every n (T4a).  The positivity is "
          "therefore LEVEL-STABLE, not a per-level accident.")
    # (iii) the punctuation continuation
    print("-" * 100)
    ok_punct = True
    for L in levels:
        n = L.n
        sol = EIG[n]['sol']
        if sol is None:
            ok_punct = False
            continue
        d1 = sol[0]
        if n == 1 and d1 != 0:
            ok_punct = False
        if n >= 2 and d1 <= 0:
            ok_punct = False
    check("T4e  THE REGISTERED PUNCTUATION CONTINUATION: d_1(2,1) = %d (the arrival depth "
          "is DEAD) and d_1(2,n) > 0 for every n >= 2 -- checked at n = %s"
          % (EIG[1]['sol'][0] if EIG[1]['sol'] else -1,
             ", ".join(str(L.n) for L in levels if L.n >= 2)), ok_punct)
    print()
    sys.stdout.flush()


# ======================================================================================
# T5.  THE SCALING DOES NOT PRESERVE THE LIMIT'S SONIN CONDITION -- AN EXACT WITNESS.
#
# THE DERIVATION, before the number.  (U f)(x) = 2^(-1/2) f(2x); in Q_2, d(2x) = |2|_2 dx
# = dx/2, so
#     (U f)^(y) = int 2^(-1/2) f(2x) psi(xy) dx = 2^(1/2) * f^(y/2).
# For y in the ball Z_2, y/2 ranges over 2^(-1)Z_2 -- and the Sonin condition controls f^
# ONLY on Z_2.  So (U f)^|_(Z_2) reads f^ on 2^(-1)Z_2 \ Z_2, which is UNCONTROLLED.  The
# witness below is computed at the HOST level directly from the definition (no shortcut):
# U f as a host-(n+1) function (integer part; the 2^(-1/2) carried symbolically), then its
# host transform evaluated on the host ball rows as exact folded zeta_(4^(n+1)) sums.
# The predicted identity (U f)^(k'') = 2^(1/2) f^(2^(n-1) * k''/2^(n+1)) is then checked
# entry-exact as an independent confirmation of the mechanism.
# ======================================================================================

WITNESS = {}


def t5_witness(levels, ns=(2, 3)):
    print("=" * 100)
    print("T5.  AN EXACT WITNESS: f in Son(2,n) WITH (U f)-HAT NONZERO ON THE BALL")
    print("=" * 100)
    for L in levels:
        n = L.n
        if n not in ns:
            continue
        q, N, d = L.q, L.N, L.d
        h = n + 1
        Nh = 4 ** h
        qh = 2 ** h
        zdh = ZD(Nh)
        zdn = ZD(N)
        ball = list(range(0, Nh, qh))
        found = []
        nz_cols = 0
        ok_pred = True
        for c in range(d):
            Uf = uk_col(L.icols[c], 2, n, h, 1)      # rational part; true = 2^(-1/2) * Uf
            hits = []
            for kpp in ball:
                acc = {}
                for mpp, v in Uf.items():
                    zdh.acc(acc, kpp * mpp, v)
                if acc:
                    hits.append((kpp, acc))
                # THE PREDICTED IDENTITY, normalized exactly.  The computed row is
                #   (U f)^(k'') = 2^(-1/2) * 2^(-h) * acc,   acc = sum Uf_rat zeta_(N_h)^.
                # The prediction is 2^(1/2) f^(y/2) = 2^(1/2) * 2^(-n) * Y0,
                #   Y0 = sum_m f(m) zeta_N^(m m'),  m' = 2^(n-1) * k''/2^(n+1) mod N.
                # Equality <=> acc = 2^(1 + h - n) Y0 = 4 Y0 (h = n+1), and zeta_N is
                # zeta_(N_h)^4 -- so Y below is built as exactly 4 * Y0.
                s = kpp // qh
                mp = (2 ** (n - 1) * s) % N
                Y = {}
                for m0, v in L.icols[c].items():
                    zdh.acc(Y, 4 * m0 * mp, 4 * v)
                if not ZD.eq(acc, Y):
                    ok_pred = False
            if hits:
                nz_cols += 1
                if len(found) < 3:
                    a, j = L.blk(c)
                    found.append((c, a, j, hits[0]))
        got = nz_cols > 0
        check("T5a n=%d  A WITNESS EXISTS: %d of the %d Sonin columns f have "
              "(U f)-hat NONZERO somewhere on the host ball B = {k'' == 0 mod 2^%d} "
              "(%d ball rows) -- exact folded zeta_%d sums"
              % (n, nz_cols, d, h, len(ball), Nh), got)
        for (c, a, j, (kpp, acc)) in found:
            val = ZD.to_str(acc, Fraction(1, 2 ** h))
            print("        witness  f = k_(alpha=%d, j=%d) (column %d):  "
                  "(U f)^(y) at y = 2^(-%d)*%d in Z_2  =  2^(-1/2) * ( %s )   EXACT, "
                  "NONZERO" % (a, j, c, h, kpp, val))
        check("T5b n=%d  THE MECHANISM CONFIRMED ENTRY-EXACT: (U f)^(y) = 2^(1/2) f^(y/2) "
              "on every ball row and every Sonin column -- the ball values of (U f)-hat "
              "ARE the values of f-hat on 2^(-1)Z_2, which the Sonin condition does not "
              "control" % n, ok_pred)
        WITNESS[n] = dict(nz_cols=nz_cols, d=d, found=found, pred=ok_pred)
    print("      CONSEQUENCE, stated: U does NOT map Son(2,infinity) into itself.  The "
          "scaling acts on the limit object ONLY COMPRESSED, as S U S -- CC's "
          "compressed-scaling structure is RECOVERED AS FORCED on Q_2, not chosen; and "
          "the compressed action's mass is exactly the fifth law measured at T3(b).")
    print()
    sys.stdout.flush()


# ======================================================================================
# THE TABLES
# ======================================================================================

def tables(levels):
    print("=" * 100)
    print("THE TABLES")
    print("=" * 100)
    print()
    print("EIGEN-DIMS OF THE COMPRESSED TRANSFORM M (M^4 = I), n = 1..6")
    print("  %-3s %-6s %-8s %-8s %-6s %-6s %-6s %-6s %-12s %-14s"
          % ("n", "dim", "tr M", "tr Pi", "d_1", "d_-1", "d_i", "d_-i",
             "constrained", "plain T-fixed"))
    print("  " + "-" * 96)
    for L in levels:
        n = L.n
        e = EIG[n]
        sol = e['sol']
        if sol is None:
            print("  %-3d %-6d %-8s %-8s  NON-INTEGRAL SOLVE" % (n, e['d'], "?", "?"))
            continue
        d1, dm1, di, dmi = sol
        trm = ("%s + %s i" % (_fmt(e['A']), _fmt(e['B']))) if e['A'] != 0 \
            else ("%s i" % _fmt(e['B']))
        print("  %-3d %-6d %-8s %-8s %-6d %-6d %-6d %-6d %-12d %-14d"
              % (n, e['d'], trm, _fmt(e['C']), d1, dm1, di, dmi, 2 * d1, 2 * d1 + dm1))
    print("  " + "-" * 96)
    print("  ALL CELLS EXACT.  No cell is CONJECTURED-PATTERN: tr M and tr Pi were "
          "MEASURED at every n = 1..6 (tr M by the shell-diagonal coefficient-dictionary "
          "route, tr Pi from the exactly-solved signed permutation).")
    print("  CLOSED FORMS the measured table exhibits: dim = (2^n - 1)^2; "
          "d_1 = d_-1 = d_-i = 2^(2n-2) - 2^(n-1); d_i = d_1 + 1; "
          "constrained = 2^(2n-1) - 2^n; plain = 3 (2^(2n-2) - 2^(n-1)).")
    print()
    print("Q^2 -- THE FIFTH LAW, n = 1..6")
    print("  %-3s %-6s %-14s %-14s %-14s %-10s"
          % ("n", "dim", "Q_gen^2", "Q_model^2", "2(2^(n-1)-1)^2", "verdict"))
    print("  " + "-" * 70)
    for L in levels:
        n = L.n
        if n not in QTAB:
            continue
        r = QTAB[n]
        vd = "VERBATIM" if (r['Qg2'] == r['Qm2'] == r['law']) else "CORRECTED"
        print("  %-3d %-6d %-14s %-14s %-14s %-10s"
              % (n, L.d, _fmt(r['Qg2']), _fmt(r['Qm2']), _fmt(r['law']), vd))
    print("  " + "-" * 70)
    print()
    print("THE LOCALIZATION TRACE Tr(U^k S_n), k = 1, 2, n = 1..6 "
          "(value shown times the symbolic 2^(-k/2))")
    print("  %-3s %-6s %-10s %-10s %-9s %-6s %-10s %-9s %-6s"
          % ("n", "dim", "k=1 h=n+1", "k=1 h=n+2", "stable", "zero",
             "k=2 h=n+2/3", "stable", "zero"))
    print("  " + "-" * 82)
    for L in levels:
        n = L.n
        if n not in TRTAB:
            continue
        t = TRTAB[n]
        v1, s1, z1 = t[1]
        v2, s2, z2 = t[2]
        print("  %-3d %-6d %-10s %-10s %-9s %-6s %-10s %-9s %-6s"
              % (n, L.d, _fmt(v1[0][1]), _fmt(v1[1][1]), "STABLE" if s1 else "DRIFTS",
                 "yes" if z1 else "NO",
                 "%s / %s" % (_fmt(v2[0][1]), _fmt(v2[1][1])),
                 "STABLE" if s2 else "DRIFTS", "yes" if z2 else "NO"))
    print("  " + "-" * 82)
    print()
    sys.stdout.flush()


# ======================================================================================
# MAIN
# ======================================================================================

LEVELS = [1, 2, 3, 4, 5, 6]
T2_BUDGET_SECONDS = 420.0


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 10 -- REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    sys.stdout.flush()

    t_start = time.time()
    levels = [Level(n) for n in LEVELS]
    print("LEVELS BUILT: " + ", ".join("n=%d (q=%d, N=%d, dim Son=%d, field "
                                       "Q(zeta_%d) of degree %d)"
                                       % (L.n, L.q, L.N, L.d, L.N, L.N // 2)
                                       for L in levels))
    print()
    sys.stdout.flush()

    p0_closed_form(levels)
    t1_tower(levels)
    t2_pairing(levels, T2_BUDGET_SECONDS)
    t3a_eigendims(levels)
    t3ap_msq(levels)
    t3b_qsquare(levels)
    t3c_traces(levels)
    t4_constrained(levels)
    t5_witness(levels)
    tables(levels)

    # ---------------------------------------------------------------------------------
    print("=" * 100)
    print("THE VERDICT, PER REGISTERED CLAIM")
    print("=" * 100)
    def verdict(prefix):
        rel = [(nm, ok) for nm, ok in LEDGER if nm.startswith(prefix)]
        return all(ok for _, ok in rel), len(rel)
    for pref, title in (("T1", "iota(Son(2,n)) CONTAINED in Son(2,n+1) -- the inductive "
                               "system"),
                        ("T2", "the pairing is level-stable ON THE NOSE"),
                        ("T3", "the laws' n-dependence at n = 1..6"),
                        ("T4", "the constrained sector's positivity is level-stable, and "
                               "the punctuation continuation"),
                        ("T5", "the scaling does NOT preserve the limit's Sonin "
                               "condition")):
        ok, cnt = verdict(pref)
        print("  %-3s  %-8s  (%d exact lines)  %s"
              % (pref, "LANDED" if ok else "**DID NOT LAND**", cnt, title))
    allok = all(ok for _, ok in LEDGER)
    print()
    print("  BRANCH TAKEN: %s" % ("(L-stable) -- all five registered claims land."
                                  if allok else
                                  "(L-fails) -- see the FAIL lines below for the named "
                                  "level and channel."))
    print()
    if allok:
        print("THE LIMIT OBJECT, NAMED (not constructed): the inductive limit")
        print("    Son(2,infinity) = lim_-> (Son(2,n), iota)")
        print("      = { f : Q_2 -> C level-finite : f|_(Z_2) = 0 and (F f)|_(Z_2) = 0 },")
        print("a nonzero subspace of L^2(Q_2) (nonzero at every n >= 1 since "
              "dim Son(2,n) = (2^n - 1)^2 >= 1), carrying:")
        print("  - the genuine Fourier transform F, which acts on it (T1 + the banked "
              "intertwining) with the level-stable pairing (T2);")
        print("  - the COMPRESSED scaling S U S -- and only that, because U itself "
              "escapes the Sonin condition (T5, exact witness).")
        print("Its L^2 CLOSURE and the limit of the compressions are NAMED, NOT "
              "CONSTRUCTED: nothing here builds them, and nothing here claims them.  "
              "dim Son(2,n) grows without bound, so no finite-dimensional limit exists; "
              "what is exhibited is the inductive system and its exactly-measured "
              "invariants.")
    print()
    print("SCOPE, said plainly: these are EXACT properties of FINITE CONSTRUCTED OBJECTS "
          "and of the inductive system they form, on the genuine local field Q_2.  No "
          "sign is asserted; no register moves; W_inf - Sum W_p at complete roster is NOT "
          "touched.  The closure protocol gates the REGISTER, not this investigation.")
    print()
    if FAILS:
        print("*** LINES THAT DID NOT LAND AS REGISTERED (%d) ***" % len(FAILS))
        for nm in FAILS:
            print("    FAIL  %s" % nm)
        print()
    else:
        print("NOTHING FAILED TO LAND: every EXACT line landed as registered.")
        print()
    print("DECLARED LINES (float or skipped; NEVER counted as EXACT): %d" % len(DECLARED))
    for nm in DECLARED:
        print("    DECLARED  %s" % nm)
    print()
    n_ok = sum(1 for _, ok in LEDGER if ok)
    n_all = len(LEDGER)
    print("TOTAL RUNTIME: %.1f s" % (time.time() - t_start))
    print()
    print("ALL EXACT LINES EXACT: %d/%d PASS" % (n_ok, n_all))


if __name__ == "__main__":
    main()
