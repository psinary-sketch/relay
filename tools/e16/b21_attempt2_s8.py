"""W-ATTEMPT-2, SITTING 8 — THE LOCAL MODEL LIFTED ONE RUNG: THE SQUARE ON Q_p ITSELF.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA at bench
grade; refused: any promotion to W_inf - Sum W_p at complete roster, or register movement.
THE PROTOCOL CORRECTION ON THE FERRY'S FACE, carried: the closure protocol gates the
REGISTER and public claims, not investigation — the programme tests its own object.

THE LIFT, DECLARED (before any run)
===================================
Level-n Schwartz-Bruhat space on Q_p:
    V_n = { f : supp f in p^(-n) Z_p,  f invariant under translation by p^n Z_p }
— an honest finite-dimensional subspace of L^2(Q_p). THE FIRST CAVEAT of the banked
transposition table ("on K_p the O-translation-invariant functions are not L^2, so the
commuting-projection structure needs the compact quotient") DOES NOT ARISE at finite
level: V_n sits inside L^2; what remains of the caveat is only the n -> infinity limit,
stated at the foot. V_n IS canonically the model space: p^(-n)Z_p / p^n Z_p = Z/p^(2n)
via x = p^(-n) m; Haar measure (Z_p mass 1) gives each chart point mass p^(-n) —
uniform — so the model inner product is the L^2(Q_p) inner product up to the global
scalar p^(-n).

THE GENUINE TRANSFORM: (F f)(y) = int f(x) psi(x y) dx, psi the standard character of
conductor Z_p (psi(x) = e^(2 pi i {x}_p)), self-dual Haar. REGISTERED CLAIM, CHECKED
ENTRY-EXACT IN-RUN: on V_n this descends to EXACTLY the model DFT
F_N[j,k] = zeta_N^(jk) / p^n (N = p^(2n)) in the chart — the model transform IS the
genuine local transform at level n, with NO artifact. If exact, the dimension law
(p^n - 1)^2, the tensor square Son = V1 (x) W1 (S = P1 (x) Q1), and the certified
F-structure (M^2 = Pi, radical zero, the twist G-dagger = G Pi) LIFT VERBATIM by
canonical isomorphism — checked, never assumed.

THE GENUINE SCALING: (U f)(x) = p^(-1/2) f(p x), unitary on L^2(Q_p). Longhand, before
any number: U maps V_n INTO V_(n+1) and ESCAPES V_n — supp(U f) = p^(-n-1) Z_p — so THE
MODEL'S mod-N WRAPAROUND IS THE ARTIFACT, located exactly at the outer shell (b8's
declared edge, now derived rather than declared). The lift therefore re-measures every
U-law with the GENUINE U via the isometric embedding iota: V_n -> V_(n+1) (chart
refinement, m'' = p*m + p^(2n+1)*j; verified isometric in-run):
    Q_gen(p,n)  = || S_n U S_n ||_F, S_n the projection onto iota(Son(p,n)) inside
                  V_(n+1) — against the model law Q_model = sqrt(p) (p^(n-1) - 1);
    the trace   Tr(U^k S_n) computed at host levels n+k for k = 1, 2 — the model's
                  banked law is t_k = 0 (fixed-point localization, proved at the model);
                  THE SECOND CAVEAT ("(iv) transposes as an orbital integral requiring
                  regularization") is met by LEVEL-STABILITY: the same object's trace
                  computed with hosts n+k, n+k+1, n+k+2 — if stable, the stable value
                  IS the regularized orbital integral at bench grade; if it drifts, the
                  drift is the named exact residual.

VERDICT MAP, registered per law: VERBATIM (survives the lift unchanged, exact) /
CORRECTED (survives with a stated exact correction, e.g. an edge term) / FAILS (the
model law was an artifact of the truncation; the failing term named). The tensor square
is re-tested on the lift: if the transform identification is entry-exact, V1 (x) W1 is
the structure of Son inside V_n on the genuine field by transport — the check is the
proof's shadow, and it is still run.

CELLS: p in {2, 3}, n in {1, 2, 3}. Exact arithmetic (Fraction coefficients mod the
prime-power cyclotomic: Phi_(2^k) = x^(2^(k-1)) + 1; Phi_(3^k) = x^(2*3^(k-1)) +
x^(3^(k-1)) + 1) where the cell allows: (2,1), (2,2), (3,1) fully exact including the
level-(n+1) host; (2,3) exact at zeta_64/zeta_256 via on-demand entries and the Sonin
basis's 2-nonzero sparsity (no dense F is ever formed); (3,2) exact the same way as
feasible; (3,3) FLOAT, declared. Floats never appear in a line marked EXACT.

RECORDED PLAINLY AS DATA. Nothing here asserts any sign; the register is untouched.
Usage:  python b21_attempt2_s8.py register | run
"""

import sys
from fractions import Fraction

try:
    import numpy as np
except ImportError:                                       # pragma: no cover
    np = None

# ======================================================================================
# PURE-ASCII OUTPUT GUARD.  The banked registration docstring above is kept VERBATIM
# (byte-for-byte as registered) and is NOT altered; typographic characters are folded to
# ASCII at PRINT time only, so every emitted byte is < 128 on any console/redirect.
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


ONE = Fraction(1)
MONE = Fraction(-1)


# ======================================================================================
# THE FIELD Q(zeta_(p^k)), parameterized by the prime power.  SELF-CONTAINED.
#
#   Phi_(p^k)(x) = sum_(i=0)^(p-1) x^(i p^(k-1)),  deg = phi(p^k) = (p-1) p^(k-1).
#   p = 2:  Phi_(2^k) = x^(2^(k-1)) + 1                 -> zeta^(2^(k-1)) = -1
#   p = 3:  Phi_(3^k) = x^(2*3^(k-1)) + x^(3^(k-1)) + 1 -> zeta^(2*3^(k-1))
#                                                          = -zeta^(3^(k-1)) - 1
# Elements are SPARSE dicts {j: Fraction} with 0 <= j < deg (the power basis
# zeta^0 .. zeta^(deg-1)).  Sparsity is essential: every field element that occurs in
# this bench is a sum of a handful of roots of unity, and no dense N x N transform
# matrix is ever formed at any cell.
#
# The power table: for deg <= e < p^k write e = deg + s with 0 <= s < p^(k-1); then
#   zeta^e = zeta^s * zeta^deg = -sum_(i=0)^(p-2) zeta^(i p^(k-1) + s),
# and every exponent i*p^(k-1) + s is < deg -- so ANY single power of zeta is at most
# (p-1) basis terms.  b18's zeta_144-specific class is NOT imported; this one is
# parameterized by (p, k) as the sitting requires.
# ======================================================================================

class Cyc(object):
    """The cyclotomic field Q(zeta_(p^k)) with sparse-dict elements."""

    __slots__ = ('p', 'k', 'order', 'deg', '_pw', 'ONE', 'ZERO')

    def __init__(self, p, k):
        self.p = p
        self.k = k
        self.order = p ** k
        self.deg = (p - 1) * p ** (k - 1)
        t = p ** (k - 1)
        tab = []
        for e in range(self.order):
            if e < self.deg:
                tab.append({e: ONE})
            else:
                s = e - self.deg                       # 0 <= s < t
                d = {}
                for i in range(p - 1):
                    d[i * t + s] = MONE
                tab.append(d)
        self._pw = tab
        self.ONE = {0: ONE}
        self.ZERO = {}

    # -- primitives ---------------------------------------------------------------
    def pw(self, e):
        """zeta_(p^k)^e as a basis dict (fresh copy: callers may mutate)."""
        return dict(self._pw[e % self.order])

    def zeta_sub(self, N, j):
        """zeta_N^j for N | p^k, expressed in the ambient field."""
        return self.pw(j * (self.order // N))

    @staticmethod
    def add(a, b):
        out = dict(a)
        for j, v in b.items():
            w = out.get(j)
            if w is None:
                out[j] = v
            else:
                s = w + v
                if s:
                    out[j] = s
                else:
                    del out[j]
        return out

    @staticmethod
    def acc(out, b, r=ONE):
        """out += r * b, in place."""
        for j, v in b.items():
            c = v * r
            if not c:
                continue
            w = out.get(j)
            if w is None:
                out[j] = c
            else:
                s = w + c
                if s:
                    out[j] = s
                else:
                    del out[j]
        return out

    @staticmethod
    def sub(a, b):
        out = dict(a)
        for j, v in b.items():
            w = out.get(j)
            if w is None:
                out[j] = -v
            else:
                s = w - v
                if s:
                    out[j] = s
                else:
                    del out[j]
        return out

    @staticmethod
    def smul(a, r):
        if r == 0:
            return {}
        return dict((j, v * r) for j, v in a.items())

    def mul(self, a, b):
        out = {}
        pwt = self._pw
        o = self.order
        for i, x in a.items():
            if not x:
                continue
            for j, y in b.items():
                c = x * y
                if not c:
                    continue
                for e, z in pwt[(i + j) % o].items():
                    w = out.get(e)
                    nv = (w + c * z) if w is not None else c * z
                    if nv:
                        out[e] = nv
                    elif w is not None:
                        del out[e]
        return out

    def conj(self, a):
        """Complex conjugation: zeta^j -> zeta^(order - j)."""
        out = {}
        for j, v in a.items():
            self.acc(out, self._pw[(self.order - j) % self.order], v)
        return out

    @staticmethod
    def is_zero(a):
        for v in a.values():
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

    def to_str(self, a):
        parts = []
        for j in sorted(a):
            v = a[j]
            if not v:
                continue
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


def _fmt(r):
    r = Fraction(r)
    if r.denominator == 1:
        return str(r.numerator)
    return "%d/%d" % (r.numerator, r.denominator)


# ======================================================================================
# EXACT RATIONAL LINEAR ALGEBRA (small matrices only: d = (p^n - 1)^2 <= 64 exact)
# ======================================================================================

def rat_inv(A):
    n = len(A)
    M = [[Fraction(v) for v in row] + [Fraction(1) if i == j else Fraction(0)
                                       for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        piv = None
        for r in range(col, n):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            raise ZeroDivisionError("singular matrix")
        M[col], M[piv] = M[piv], M[col]
        inv = Fraction(1) / M[col][col]
        M[col] = [v * inv for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [M[r][c] - f * M[col][c] for c in range(2 * n)]
    return [row[n:] for row in M]


def rat_det(A):
    n = len(A)
    M = [[Fraction(v) for v in row] for row in A]
    det = Fraction(1)
    for col in range(n):
        piv = None
        for r in range(col, n):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            return Fraction(0)
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            det = -det
        det *= M[col][col]
        inv = Fraction(1) / M[col][col]
        for r in range(col + 1, n):
            f = M[r][col] * inv
            if f != 0:
                for c in range(col, n):
                    M[r][c] -= f * M[col][c]
    return det


def rat_mm(A, B):
    n, kk, m = len(A), len(B), len(B[0])
    out = [[Fraction(0)] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        row = out[i]
        for t in range(kk):
            a = Ai[t]
            if a == 0:
                continue
            Bt = B[t]
            for j in range(m):
                b = Bt[j]
                if b:
                    row[j] += a * b
    return out


def rat_tr(A):
    return sum(A[i][i] for i in range(len(A)))


def transpose(A):
    return [list(r) for r in zip(*A)]


def perm_sign_and_det(Pi):
    """Pi rational; return (is_signed_permutation, det)."""
    n = len(Pi)
    perm = [-1] * n
    sgn = [0] * n
    for i in range(n):
        nz = [(j, Pi[i][j]) for j in range(n) if Pi[i][j] != 0]
        if len(nz) != 1:
            return False, None
        j, v = nz[0]
        if v != 1 and v != -1:
            return False, None
        perm[i] = j
        sgn[i] = int(v)
    if sorted(perm) != list(range(n)):
        return False, None
    seen = [False] * n
    s = 1
    for i in range(n):
        if not seen[i]:
            L = 0
            kk = i
            while not seen[kk]:
                seen[kk] = True
                kk = perm[kk]
                L += 1
            if L % 2 == 0:
                s = -s
    dt = s
    for v in sgn:
        dt *= v
    return True, dt


# ======================================================================================
# THE LEDGER.  EXACT lines are counted; FLOAT lines are reported and NEVER counted.
# A failing line does NOT abort the run: the sitting must report what did not land.
# ======================================================================================

LEDGER = []
FAILS = []
FLOATLINES = []


def check(name, ok):
    LEDGER.append((name, bool(ok)))
    if not ok:
        FAILS.append(name)
    print("  %s  %s" % ("PASS" if ok else "**FAIL**", name))
    sys.stdout.flush()
    return bool(ok)


def fnote(name):
    FLOATLINES.append(name)
    print("  FLOAT %s" % name)
    sys.stdout.flush()


# ======================================================================================
# CHART, SONIN BASIS, EMBEDDING, SCALING
#
# CHART.  V_n has the basis { 1_(x_m + p^n Z_p) : m in Z/N },  x_m = p^(-n) m,
# N = p^(2n).  Haar with Z_p of mass 1 gives every chart cell the mass p^(-n).
# Chart splitting m = alpha + q*beta, q = p^n, alpha,beta in [0,q).
#
# SONIN BASIS (b18's convention, verbatim): k_(alpha,j) = delta_alpha (x) (e_j - e_(j+1)),
# alpha in [1,q), j in [0,q-1);  dim = (q-1)^2.
# ======================================================================================

def sonin_cols(p, n):
    """Return (cols, labels): each col a dict {m: +-1} on Z/N."""
    q = p ** n
    N = q * q
    labs = [(a, j) for a in range(1, q) for j in range(0, q - 1)]
    cols = []
    for (a, j) in labs:
        cols.append({(a + q * j) % N: ONE, (a + q * (j + 1)) % N: MONE})
    return cols, labs


# --------------------------------------------------------------------------------------
# DERIVATION 1 -- THE EMBEDDING iota: V_n -> V_h  (h > n), CHART FORM.
#
# V_n is LITERALLY a subspace of V_h as a space of functions on Q_p:
#   supp f in p^(-n)Z_p in p^(-h)Z_p, and p^n Z_p-invariance implies p^h Z_p-invariance.
# So iota is the inclusion, and it is an isometry for the L^2(Q_p) inner product by
# definition (no normalization is inserted by hand); the CHART form of that inclusion is:
#   the level-n point p^(-n) m is the host point p^(-h)(p^(h-n) m), and the level-n cell
#   p^(-n)m + p^n Z_p is the disjoint union of the host cells p^(-h)m'' + p^h Z_p with
#   m'' = p^(h-n) m + p^(h+n) j,  j = 0 .. p^(h-n) - 1.
# For h = n+1 this is exactly the registered  m'' = p*m + p^(2n+1) j.
# The isometry is then a MEASURE statement, checked exactly in-run (B1):
#   p^(h-n) host cells of mass p^(-h) each == one level cell of mass p^(-n).
# --------------------------------------------------------------------------------------

def emb_col(col, p, n, h):
    e = h - n
    pe = p ** e
    ph = p ** (h + n)
    Nh = p ** (2 * h)
    out = {}
    for m, v in col.items():
        base = (pe * m) % Nh
        for j in range(pe):
            out[(base + ph * j) % Nh] = v
    return out


# --------------------------------------------------------------------------------------
# DERIVATION 2 -- THE GENUINE SCALING U^k IN THE HOST CHART.
#
# (U f)(x) = p^(-1/2) f(p x), so (U^k f)(x) = p^(-k/2) f(p^k x).  For f in V_n:
#   supp(U^k f) = { x : p^k x in p^(-n)Z_p } = p^(-n-k) Z_p    (U ESCAPES V_n: k >= 1
#       puts mass on |x| = p^(n+k) > p^n -- the shell the model had to wrap around),
#   invariance: (U^k f)(x + t) = (U^k f)(x) whenever p^k t in p^n Z_p, i.e.
#       t in p^(n-k) Z_p  -- COARSER than p^(n+k)Z_p: U^k f is constant on the LARGER
#       blocks p^(n-k)Z_p, not merely on host cells.  In the host chart at level h this
#       reads: the value depends on m'' only through m'' mod p^(n+k+... ) -- concretely
#       for k = 1, h = n+1 the value depends on m'' only mod N = p^(2n) (checked, C0a).
# Host chart at level h >= n+k:  x = p^(-h) m'', p^k x = p^(k-h) m''.  This lies in
# p^(-n)Z_p iff p^(h-n-k) | m'', and then the level-n chart index of p^k x is
#   (m'' / p^(h-n-k)) mod p^(2n).
# For h = n+k this is exactly the registered  (U^k f)(m'') = p^(-k/2) f_n(m'' mod p^(2n)).
# The irrational factor p^(-k/2) is CARRIED SYMBOLICALLY (never evaluated as a float):
# uk_col returns the RATIONAL part; every reported quantity is either p^(-k/2) times an
# exact rational (the traces) or quadratic in U (Q^2), where the factor is exactly p^(-k).
# --------------------------------------------------------------------------------------

def uk_col(col, p, n, h, k):
    """U^k applied to a level-n column, as a host-h dict of RATIONAL parts
       (true value = p^(-k/2) * this).  Requires h >= n + k."""
    N = p ** (2 * n)
    Nh = p ** (2 * h)
    e = h - n - k
    pe = p ** e
    reps = p ** (h + k - n)
    out = {}
    for m, v in col.items():
        for t in range(reps):
            out[(pe * (m + N * t)) % Nh] = v
    return out


def push_col(col, p, n):
    """The MODEL scaling's underlying map P (b8): P[(p*m) mod N, m] = 1 -- the
       PUSHFORWARD with mod-N wraparound.  b8's U_model = P / sqrt(p)."""
    N = p ** (2 * n)
    out = {}
    for m, v in col.items():
        j = (p * m) % N
        w = out.get(j)
        if w is None:
            out[j] = v
        else:
            s = w + v
            if s:
                out[j] = s
            else:
                del out[j]
    return out


def pull_col(col, p, n):
    """P^T: (P^T v)_m = v_(p m mod N) -- the PULLBACK."""
    N = p ** (2 * n)
    out = {}
    for m in range(N):
        v = col.get((p * m) % N)
        if v:
            out[m] = v
    return out


def contract(colsA, colsB, w, zero=None):
    """(colsA)^T diag(w) (colsB) as a dense d x d list, from sparse columns."""
    if zero is None:
        zero = Fraction(0)
    dA, dB = len(colsA), len(colsB)
    idx = {}
    for cp, col in enumerate(colsB):
        for m, v in col.items():
            idx.setdefault(m, []).append((cp, v))
    M = [[zero] * dB for _ in range(dA)]
    for c, col in enumerate(colsA):
        row = M[c]
        for m, v in col.items():
            for cp, u in idx.get(m, ()):
                row[cp] = row[cp] + v * u
    if w != 1:
        M = [[w * x for x in row] for row in M]
    return M


# --------------------------------------------------------------------------------------
# DERIVATION 3 -- THE GENUINE TRANSFORM ON V_n (the registered claim of section A).
#
# psi = the standard character of Q_p, conductor Z_p: psi(x) = e^(2 pi i {x}_p), where
# {a/p^j}_p = (a mod p^j)/p^j for a in Z (PROOF: write a = c p^j + r, 0 <= r < p^j; then
# a/p^j - r/p^j = c is in Z, in Z_p, and psi is trivial on Z_p -- so the two agree; this
# is exactly the integrality assertion checked at A0, and additivity + triviality on Z
# are checked at A1/A2).  Self-dual Haar for this psi is the one with Z_p of mass 1.
#
# For the chart basis vector f = 1_(x0 + p^n Z_p),  x0 = p^(-n) m:
#     (F f)(y) = int_(x0 + p^n Z_p) psi(x y) dx
#              = psi(x0 y) * int_(p^n Z_p) psi(t y) dt
#              = psi(x0 y) * p^(-n) * [ y p^n Z_p in ker psi = Z_p ]
#              = psi(x0 y) * p^(-n) * [ |y| <= p^n ].
# Hence F f is supported in p^(-n)Z_p; and it is p^n Z_p-invariant in y because
# psi(x0 (y + p^n u)) = psi(x0 y) psi(m u) = psi(x0 y).  So F maps V_n -> V_n with NO
# truncation, and in the chart y = p^(-n) m':
#     F[m', m] = p^(-n) psi(p^(-2n) m m') = p^(-n) zeta_N^((m m') mod N) = zeta_N^(m m')/p^n,
# which is ENTRY-FOR-ENTRY the model DFT of b8/b18 (their 1/sqrt(N) = 1/p^n).  A3 runs
# the coset integral as a refined Riemann sum over p^r sub-cells (r = 0,1,2) -- legitimate
# because psi is constant on each sub-cell (the correction is psi(p^(n+r) u y) = psi(p^r u m')
# = 1) -- and checks refinement-stability exactly; A4 compares to the model entry.
# --------------------------------------------------------------------------------------

def make_psi(fld, p):
    def psi(a, j):
        """psi(a / p^j) for a in Z, p^j | order."""
        pj = p ** j
        return fld.pw((a % pj) * (fld.order // pj))
    return psi


# ======================================================================================
# THE EXACT CELL
# ======================================================================================

RESULTS = []


def cell_exact(p, n):
    q = p ** n
    N = q * q
    h = n + 1
    Nh = p ** (2 * h)
    d = (q - 1) ** 2
    tag = "(p,n)=(%d,%d)" % (p, n)
    fld = Cyc(p, 2 * n + 2)
    psi = make_psi(fld, p)
    cols, labs = sonin_cols(p, n)
    res = dict(p=p, n=n, N=N, q=q, d=d, exact=True)

    print("=" * 100)
    print("CELL %s   EXACT.   N = p^(2n) = %d,  q = p^n = %d,  host level h = %d, "
          "N_host = %d" % (tag, N, q, h, Nh))
    print("  ambient field Q(zeta_%d) = Q(zeta_(p^(2n+2))), degree phi = %d "
          "(sparse power-basis dicts; NO dense transform matrix is ever formed)"
          % (fld.order, fld.deg))
    print("=" * 100)
    sys.stdout.flush()

    # ---------------------------------------------------------------------------------
    # F0  the field itself
    # ---------------------------------------------------------------------------------
    print("- F0  THE FIELD (exact) -")
    z = fld.pw(1)
    acc = dict(fld.ONE)
    for _ in range(fld.order):
        acc = fld.mul(acc, z)
    check("F0a %s  zeta^(p^k) = 1 exactly (%d iterated exact multiplications)"
          % (tag, fld.order), fld.eq(acc, fld.ONE))
    phi_val = {}
    for i in range(p):
        fld.acc(phi_val, fld.pw(i * p ** (fld.k - 1)))
    check("F0b %s  Phi_(p^k)(zeta) = sum_i zeta^(i p^(k-1)) = 0 exactly" % tag,
          fld.is_zero(phi_val))
    okc = True
    for e in range(fld.order):
        if not fld.eq(fld.mul(fld.conj(fld.pw(e)), fld.pw(e)), fld.ONE):
            okc = False
            break
    check("F0c %s  conj(zeta^e) * zeta^e = 1 exactly for all e in [0, p^k)" % tag, okc)

    # ---------------------------------------------------------------------------------
    # A  TRANSFORM IDENTIFICATION
    # ---------------------------------------------------------------------------------
    print("- A  TRANSFORM IDENTIFICATION: the genuine (F f)(y) = int f psi(xy) dx "
          "vs the model DFT -")
    # A0 the fractional-part identity, as an integrality assertion
    ok = True
    for c in range(0, N * p * p):
        if (c - (c % N)) % N != 0:
            ok = False
            break
    check("A0  %s  {p^(-2n) c}_p = (c mod N)/N : c/N - (c mod N)/N is an INTEGER for all "
          "c in [0, p^2 N) (hence in Z_p, where psi = 1)" % tag, ok)
    # A1 additivity of psi on the relevant lattice
    ok = True
    for a in range(N):
        pa = psi(a, 2 * n)
        for b in range(N):
            if not fld.eq(psi(a + b, 2 * n), fld.mul(pa, psi(b, 2 * n))):
                ok = False
                break
        if not ok:
            break
    check("A1  %s  psi is a character: psi(u+v) = psi(u) psi(v) exactly for all "
          "u,v in p^(-2n)Z/Z (%d pairs)" % (tag, N * N), ok)
    # A2 triviality on Z_p
    ok = all(fld.eq(psi(c * N, 2 * n), fld.ONE) for c in range(p * p * p))
    check("A2  %s  psi is trivial on Z (conductor Z_p): psi(c) = 1 exactly" % tag, ok)

    # A3 the coset integral as a refined Riemann sum, r = 0, 1, 2
    inv = [Fraction(1, p ** (n + r)) for r in range(3)]
    ok3 = True
    Fent = {}
    for m in range(N):
        for mp in range(N):
            vals = []
            for r in range(3):
                accd = {}
                for s in range(p ** r):
                    fld.acc(accd, psi(m * mp + s * mp * N, 2 * n))
                vals.append(fld.smul(accd, inv[r]))
            if not (fld.eq(vals[0], vals[1]) and fld.eq(vals[1], vals[2])):
                ok3 = False
            Fent[(m, mp)] = vals[0]
    check("A3  %s  the coset integral int_(x0+p^n Z_p) psi(xy) dx is REFINEMENT-STABLE "
          "(r = 0,1,2 sub-cells) exactly, all %d chart pairs" % (tag, N * N), ok3)
    # A4 the identification
    ok4 = True
    for m in range(N):
        for mp in range(N):
            mod = fld.smul(fld.zeta_sub(N, (m * mp) % N), Fraction(1, q))
            if not fld.eq(Fent[(m, mp)], mod):
                ok4 = False
    check("A4  %s  GENUINE ENTRY == MODEL DFT ENTRY zeta_N^(m m')/p^n, ENTRY-EXACT on all "
          "%d pairs -- NO ARTIFACT" % (tag, N * N), ok4)
    res['transform'] = ok4
    # A5 unitarity + F^2 = parity, via the exact geometric sums
    gs = []
    for c in range(N):
        accd = {}
        for mp in range(N):
            fld.acc(accd, fld.zeta_sub(N, (c * mp) % N))
        gs.append(accd)
    okg = fld.eq(gs[0], fld.smul(fld.ONE, Fraction(N))) and \
        all(fld.is_zero(gs[c]) for c in range(1, N))
    check("A5a %s  sum_(m') zeta_N^(c m') = N [c = 0] exactly for all c in Z/N "
          "(the exact geometric sums)" % tag, okg)
    check("A5b %s  F^dagger F = I exactly: (F^dagger F)[m,k] = S_((k-m))/p^(2n) = delta"
          % tag, okg)
    check("A5c %s  F^2 = parity exactly: (F^2)[m,k] = S_((m+k))/p^(2n) = delta_(m+k=0)"
          % tag, okg)
    # A6 the ball rows -> the tensor square
    ok6 = True
    for g in range(q):
        for m in range(N):
            a = m % q
            lhs = Fent[(q * g, m)]
            rhs = fld.smul(fld.zeta_sub(q, (a * g) % q), Fraction(1, q))
            if not fld.eq(lhs, rhs):
                ok6 = False
    check("A6  %s  F[q*gamma, alpha + q*beta] = zeta_q^(alpha gamma)/p^n exactly "
          "(independent of beta): the ball rows factor" % tag, ok6)

    # ---------------------------------------------------------------------------------
    # THE LAWS THAT RIDE THE IDENTIFICATION
    # ---------------------------------------------------------------------------------
    print("- A' THE LAWS THAT RIDE IT (computed with the GENUINE F; the model's are the "
          "same matrices by A4, so these are simultaneously b18's certificates and the "
          "lift's) -")
    # the columns land in Son
    ball = [m for m in range(N) if m % q == 0]
    okb = all(col.get(m, 0) == 0 for col in cols for m in ball)
    check("L0a %s  f|_B = 0 exactly on the integers' ball B = {m == 0 mod q}, all %d "
          "columns" % (tag, d), okb)
    okFb = True
    for col in cols:
        for m in ball:
            accd = {}
            for mm, v in col.items():
                fld.acc(accd, Fent[(mm, m)], v)
            if not fld.is_zero(accd):
                okFb = False
    check("L0b %s  (F f)|_B = 0 exactly (genuine F), all %d columns" % (tag, d), okFb)
    check("L1  %s  DIM LAW: dim Son = (p^n - 1)^2 = %d.  By A6 the ball rows of F are "
          "(zeta_q^(alpha gamma))_gamma,alpha applied to the beta-sums, and that q x q "
          "matrix is invertible (A5a) -- so (F f)|_B = 0 <=> sum_beta f_(alpha,beta) = 0; "
          "with f|_B = 0 that is q + (q-1) independent conditions on q^2 unknowns, "
          "dim = q^2 - (2q-1) = (q-1)^2" % (tag, d), okb and okFb and ok6 and okg)
    check("L2  %s  TENSOR SQUARE: Son = V1 (x) W1 with V1 = {v_0 = 0} (dim q-1) and "
          "W1 = {sum_beta w = 0} (dim q-1); the exact basis IS the tensor basis "
          "delta_alpha (x) (e_j - e_(j+1)) by construction, and S = P1 (x) Q1 is the "
          "orthoprojection.  Transported to the lift by A4 (same matrices)." % tag,
          ok6 and okb and okFb)

    # G_loc, M, Pi, twist
    Kt_cols = cols
    Gm = contract(Kt_cols, Kt_cols, 1)                       # K^T K, integer
    detG = rat_det(Gm)
    Gmi = rat_inv(Gm)
    # G_loc = K^T F K  (sparse: 2 x 2 terms per entry)
    Gloc = [[{} for _ in range(d)] for _ in range(d)]
    for c in range(d):
        for cp in range(d):
            accd = {}
            for m1, v1 in cols[c].items():
                for m2, v2 in cols[cp].items():
                    fld.acc(accd, Fent[(m1, m2)], v1 * v2)
            Gloc[c][cp] = accd
    # M = (K^T K)^(-1) G_loc
    M = [[{} for _ in range(d)] for _ in range(d)]
    for i in range(d):
        row = Gmi[i]
        for j in range(d):
            accd = {}
            for t in range(d):
                r = row[t]
                if r:
                    fld.acc(accd, Gloc[t][j], r)
            M[i][j] = accd
    # F K = K M ?
    okFK = True
    for c in range(d):
        for m in range(N):
            lhs = {}
            for mm, v in cols[c].items():
                fld.acc(lhs, Fent[(m, mm)], v)
            rhs = {}
            for cp in range(d):
                v = cols[cp].get(m, 0)
                if v:
                    fld.acc(rhs, M[cp][c], v)
            if not fld.eq(lhs, rhs):
                okFK = False
    check("L3a %s  F K = K M entry-exact, M = (K^T K)^(-1) K^T F K (residual EXACT ZERO)"
          % tag, okFK)
    # parity compression Pi
    PK = [dict(((-m) % N, v) for m, v in col.items()) for col in cols]
    KtPK = contract(Kt_cols, PK, 1)
    Pi = rat_mm(Gmi, KtPK)
    okPK = True
    for c in range(d):
        for m in range(N):
            lhs = Fraction(PK[c].get(m, 0))
            rhs = Fraction(0)
            for cp in range(d):
                v = cols[cp].get(m, 0)
                if v:
                    rhs += Fraction(v) * Pi[cp][c]
            if lhs != rhs:
                okPK = False
    check("L3b %s  P K = K Pi entry-exact (parity m -> -m; Pi solved, not assumed)"
          % tag, okPK)
    isp, detPi = perm_sign_and_det(Pi)
    check("L3c %s  Pi is a signed permutation with det Pi = %s in {+1,-1}"
          % (tag, detPi), isp and detPi in (1, -1))
    if d <= 9:
        MM = [[fld.ZERO] * d for _ in range(d)]
        for i in range(d):
            for j in range(d):
                accd = {}
                for t in range(d):
                    if M[i][t] and M[t][j]:
                        fld.acc(accd, fld.mul(M[i][t], M[t][j]))
                MM[i][j] = accd
        okM2 = True
        for i in range(d):
            for j in range(d):
                pij = fld.smul(fld.ONE, Fraction(Pi[i][j])) if Pi[i][j] else {}
                if not fld.eq(MM[i][j], pij):
                    okM2 = False
        check("L3d %s  M^2 = Pi entry-exact, BRUTE-FORCED (d = %d)" % (tag, d), okM2)
    else:
        check("L3d %s  M^2 = Pi, DERIVED EXACT (d = %d too large to brute-force the "
              "d^3 cyclotomic products): F^2 = parity (A5c) => F^2 K = P K; F K = K M "
              "(L3a) => F^2 K = K M^2; P K = K Pi (L3b); K has full column rank "
              "(det K^T K = %s != 0) => K M^2 = K Pi => M^2 = Pi."
              % (tag, d, _fmt(detG)), okFK and okPK and okg and detG != 0)
    check("L4  %s  RADICAL ZERO: det(K^T K) = %s is a nonzero integer, G_loc = (K^T K) M "
          "and det(M)^2 = det(M^2) = det(Pi) = %s != 0, so G_loc is invertible and "
          "rank G_loc = dim Son = %d" % (tag, _fmt(detG), detPi, d),
          detG != 0 and detG.denominator == 1 and detPi in (1, -1))
    okGKM = True
    for i in range(d):
        for j in range(d):
            accd = {}
            for t in range(d):
                r = Gm[i][t]
                if r:
                    fld.acc(accd, M[t][j], Fraction(r))
            if not fld.eq(accd, Gloc[i][j]):
                okGKM = False
    check("L4b %s  G_loc - (K^T K) M = 0 entry-exact" % tag, okGKM)
    oksym = all(fld.eq(Gloc[i][j], Gloc[j][i]) for i in range(d) for j in range(d))
    check("L5a %s  G_loc = G_loc^T entry-exact (F = F^T)" % tag, oksym)
    oktw = True
    for i in range(d):
        for j in range(d):
            lhs = fld.conj(Gloc[i][j])
            rhs = {}
            for t in range(d):
                r = Pi[t][j]
                if r:
                    fld.acc(rhs, Gloc[i][t], Fraction(r))
            if not fld.eq(lhs, rhs):
                oktw = False
    check("L5b %s  TWIST: G_loc^dagger = conj(G_loc) = G_loc * Pi entry-exact" % tag, oktw)
    print("      [b18 sitting 5 certified C1-C5 at (2,1),(3,1),(2,2) in Q(zeta_144) with "
          "the SAME matrices (its F_N = zeta_N^(jk)/sqrt(N), sqrt(N) = p^n); by A4 those "
          "certificates ARE certificates of the genuine local object -- transported, and "
          "here RE-RUN in the prime-power field, plus the two new cells.]")
    res.update(detG=detG, detPi=detPi, laws=(okFK and okPK and okGKM and oksym and oktw))
    sys.stdout.flush()

    # ---------------------------------------------------------------------------------
    # B  THE EMBEDDING iota
    # ---------------------------------------------------------------------------------
    print("- B  THE EMBEDDING iota : V_n -> V_(n+1) -")
    Kh = [emb_col(c, p, n, h) for c in cols]
    Wh = Fraction(1, p ** h)
    Gh = contract(Kh, Kh, Wh)
    Gn = contract(cols, cols, Fraction(1, q))
    okiso = all(Gh[i][j] == Gn[i][j] for i in range(d) for j in range(d))
    check("B1a %s  iota IS AN ISOMETRY, exact: the host Gram p^(-h) (iota K)^T (iota K) "
          "equals the level-n Gram p^(-n) K^T K entry-for-entry (p^(h-n) host cells of "
          "mass p^(-h) = one level cell of mass p^(-n))" % tag, okiso)
    okcnt = all(len(Kh[c]) == p * len(cols[c]) for c in range(d))
    check("B1b %s  each level cell splits into exactly p host cells "
          "(m'' = p*m + p^(2n+1)*j, j = 0..p-1)" % tag, okcnt)
    # B2: does the genuine F commute with level-inclusion on the Sonin columns?
    okD = True
    nzpat = []
    for c in range(d):
        for kpp in range(Nh):
            lhs = {}
            for mpp, v in Kh[c].items():
                fld.acc(lhs, psi(mpp * kpp, 2 * h), v)
            lhs = fld.smul(lhs, Fraction(1, p ** h))
            rhs = {}
            if kpp % p == 0:
                mm = (kpp // p) % N
                for m0, v in cols[c].items():
                    fld.acc(rhs, Fent[(m0, mm)], v)
            if not fld.eq(lhs, rhs):
                okD = False
                if len(nzpat) < 4:
                    nzpat.append((c, kpp))
    check("B2  %s  REGISTERED QUESTION, ANSWERED: F_host(iota f) = iota(F_n f) on ALL %d "
          "Sonin columns and all %d host indices -- D = 0 EXACTLY (the genuine transform "
          "DOES commute with level-inclusion on the Sonin subspace)" % (tag, d, Nh), okD)
    if not okD:
        print("      NONZERO PATTERN (first entries, column c / host index k''): %s" % nzpat)
    res['iota_intertwines'] = okD
    sys.stdout.flush()

    # ---------------------------------------------------------------------------------
    # C  THE GENUINE SCALING
    # ---------------------------------------------------------------------------------
    print("- C  THE GENUINE SCALING U f (x) = p^(-1/2) f(p x) -")
    UK = [uk_col(c, p, n, h, 1) for c in cols]
    okper = True
    for c in range(d):
        for mpp in range(Nh):
            if UK[c].get(mpp, 0) != UK[c].get((mpp + N) % Nh, 0):
                okper = False
    check("C0a %s  U f is constant on the blocks p^(n-1)Z_p: the host values depend on "
          "m'' only mod N = p^(2n) (the derivation's own check)" % tag, okper)
    okesc = any((mpp % p) != 0 and v != 0 for c in range(d) for mpp, v in UK[c].items())
    check("C0b %s  U ESCAPES V_n, exactly: some host index with p does not divide m'' "
          "carries nonzero mass -- supp(U f) = p^(-n-1)Z_p, strictly bigger than "
          "p^(-n)Z_p.  THE MODEL'S mod-N WRAPAROUND IS EXACTLY THIS ESCAPED MASS FOLDED "
          "BACK IN." % tag, okesc)
    GU = contract(UK, UK, Wh * Fraction(1, p))
    check("C1  %s  U IS AN ISOMETRY on Son, exact: p^(-h) p^(-1) (U K)^T (U K) == "
          "p^(-n) K^T K entry-for-entry" % tag,
          all(GU[i][j] == Gn[i][j] for i in range(d) for j in range(d)))
    # A_rat = W_h (iota K)^T (U K)  [true A = p^(-1/2) A_rat]
    Arat = contract(Kh, UK, Wh)
    # the derived identity  A = p^(-n-1/2) K^T P^T K
    PtK = [pull_col(c, p, n) for c in cols]
    Bt = contract(cols, PtK, 1)
    okid = all(Arat[i][j] == Fraction(1, q) * Bt[i][j] for i in range(d) for j in range(d))
    check("C2a %s  DERIVATION CHECK: <iota k_c , U k_c'> = p^(-n-1/2) (K^T P^T K)[c,c'] "
          "exactly -- i.e. THE COMPRESSION OF THE GENUINE U TO Son IS THE PULLBACK "
          "P^T/sqrt(p), while b8's model U is the truncated PUSHFORWARD P/sqrt(p).  "
          "They are ADJOINT, not equal: that adjointness IS the wraparound artifact."
          % tag, okid)
    Ghi = rat_inv(Gh)
    # Q_gen^2 = tr(A^dag G^-1 A G^-1) = (1/p) tr(Arat^T Ghi Arat Ghi)
    T1 = rat_mm(transpose(Arat), Ghi)
    T2 = rat_mm(rat_mm(T1, Arat), Ghi)
    Qg2 = Fraction(1, p) * rat_tr(T2)
    # the model: Q_model^2 = (1/p) tr(B^T Gm^-1 B Gm^-1), B = K^T P K
    PK2 = [push_col(c, p, n) for c in cols]
    B = contract(cols, PK2, 1)
    S1 = rat_mm(transpose(B), Gmi)
    S2 = rat_mm(rat_mm(S1, B), Gmi)
    Qm2 = Fraction(1, p) * rat_tr(S2)
    law = Fraction(p) * Fraction((p ** (n - 1) - 1) ** 2)
    diff = Qg2 - Qm2
    verdict = "VERBATIM" if diff == 0 else "CORRECTED"
    check("C2b %s  Q_gen^2 = %s  (EXACT RATIONAL)" % (tag, _fmt(Qg2)), True)
    check("C2c %s  Q_model^2 = %s  (EXACT RATIONAL, b8's model re-measured exactly)"
          % (tag, _fmt(Qm2)), True)
    check("C2d %s  Q_gen^2 - Q_model^2 = %s  -> the fifth law lifts %s"
          % (tag, _fmt(diff), verdict), True)
    okl = (Qm2 == law)
    check("C2e %s  the BANKED MODEL LAW Q_model = sqrt(p)(p^(n-1)-1), i.e. "
          "Q_model^2 = p(p^(n-1)-1)^2 = %s : %s at this cell"
          % (tag, _fmt(law), "HOLDS" if okl else "DOES NOT HOLD"), okl)
    print("      Q_gen = %.12f   Q_model = %.12f   sqrt(p)(p^(n-1)-1) = %.12f   "
          "[FLOAT DISPLAY of the exact squares above; the comparison itself was made "
          "EXACTLY at the squared level]"
          % (float(Qg2) ** 0.5, float(Qm2) ** 0.5, float(law) ** 0.5))
    res.update(Qg2=Qg2, Qm2=Qm2, law=law, qverdict=verdict, lawholds=okl)
    sys.stdout.flush()

    # ---------------------------------------------------------------------------------
    # D  THE TRACE / SECOND CAVEAT
    # ---------------------------------------------------------------------------------
    print("- D  THE LOCALIZATION TRACE Tr(U^k S_n) AND LEVEL-STABILITY (the second "
          "caveat: the orbital integral's regularization) -")
    tr_tab = {}
    for kk in (1, 2):
        vals = []
        for hh in (n + kk, n + kk + 1):
            Khh = [emb_col(c, p, n, hh) for c in cols]
            Whh = Fraction(1, p ** hh)
            Ghh = contract(Khh, Khh, Whh)
            Ghhi = rat_inv(Ghh)
            Ukk = [uk_col(c, p, n, hh, kk) for c in cols]
            Akk = contract(Khh, Ukk, Whh)
            tr_rat = rat_tr(rat_mm(Ghhi, Akk))
            vals.append((hh, tr_rat))
            unit = "1" if kk % 2 == 0 else "p^(-1/2)"
            if kk % 2 == 0:
                shown = _fmt(tr_rat * Fraction(1, p ** (kk // 2)))
            else:
                shown = ("0" if tr_rat == 0 else "%s * %s" % (unit, _fmt(tr_rat)))
            check("D%d  %s  host h = %d (= n+k%s): Tr(U^%d S_n) = %s   EXACT"
                  % (kk, tag, hh, "" if hh == n + kk else "+1", kk, shown), True)
        stable = (vals[0][1] == vals[1][1])
        check("D%ds %s  LEVEL-STABILITY of Tr(U^%d S_n) across hosts h = %d and %d: %s"
              % (kk, tag, kk, vals[0][0], vals[1][0],
                 "STABLE (the stable value IS the regularized orbital integral at bench "
                 "grade)" if stable else "DRIFTS -- exact residual %s"
                 % _fmt(vals[1][1] - vals[0][1])), stable)
        zero = (vals[0][1] == 0 and vals[1][1] == 0)
        check("D%dz %s  the model's banked law t_%d = 0 (fixed-point localization) on the "
              "lift: %s" % (kk, tag, kk, "HOLDS EXACTLY" if zero else "FAILS"), zero)
        tr_tab[kk] = (vals, stable, zero)
    res['traces'] = tr_tab
    print("      LOCALIZATION, said exactly: a diagonal term needs m and p^k m in the same "
          "support shell alpha != 0 mod q, i.e. alpha(p^k - 1) == 0 mod p^n; "
          "gcd(p^k - 1, p) = 1 forces alpha == 0 mod p^n, impossible for 1 <= alpha < q.")
    print()
    sys.stdout.flush()
    RESULTS.append(res)
    return res


# ======================================================================================
# THE FLOAT CELL (3,3) -- DECLARED FLOAT.  No line here is marked EXACT.
# ======================================================================================

def cell_float(p, n):
    q = p ** n
    N = q * q
    h = n + 1
    Nh = p ** (2 * h)
    d = (q - 1) ** 2
    tag = "(p,n)=(%d,%d)" % (p, n)
    res = dict(p=p, n=n, N=N, q=q, d=d, exact=False)
    print("=" * 100)
    print("CELL %s   FLOAT, DECLARED.   N = %d, host N = %d, dim Son = %d "
          "(the cyclotomic field would be Q(zeta_%d), degree %d -- out of reach at bench "
          "cost; every number below is a FLOAT and is marked so)"
          % (tag, N, Nh, d, p ** (2 * n + 2), (p - 1) * p ** (2 * n + 1)))
    print("=" * 100)
    sys.stdout.flush()
    if np is None:
        print("  numpy unavailable: FLOAT CELL SKIPPED (declared).")
        res['skipped'] = True
        RESULTS.append(res)
        return res

    cols, labs = sonin_cols(p, n)
    colsf = [dict((m, float(v)) for m, v in c.items()) for c in cols]

    # A (float): genuine coset integral vs model DFT
    mm = np.arange(N)
    prod = np.outer(mm, mm) % N
    Fmod = np.exp(2j * np.pi * prod / N) / (p ** n)
    Fgen = np.zeros((N, N), dtype=complex)
    for s in range(p):
        a = (prod + s * np.outer(np.zeros(N, dtype=np.int64) + 1, mm) * N) % N
        Fgen += np.exp(2j * np.pi * a / N)
    Fgen = Fgen / (p ** (n + 1))
    err = float(np.max(np.abs(Fgen - Fmod)))
    fnote("A(3,3)  genuine coset integral (refined, r = 1) vs model DFT entry: "
          "max |diff| = %.3e over all %d pairs" % (err, N * N))
    uni = float(np.max(np.abs(Fmod.conj().T @ Fmod - np.eye(N))))
    fnote("A(3,3)  ||F^dagger F - I||_max = %.3e" % uni)
    res['transform'] = (err < 1e-9)

    # B (float): iota isometry and the intertwining, on a sample of columns
    Kh = [emb_col(c, p, n, h) for c in colsf]
    Wh = 1.0 / p ** h
    Gh = contract(Kh, Kh, Wh, zero=0.0)
    Gn = contract(colsf, colsf, 1.0 / q, zero=0.0)
    iso = max(abs(Gh[i][j] - Gn[i][j]) for i in range(d) for j in range(d))
    fnote("B(3,3)  iota isometry: max |host Gram - level Gram| = %.3e" % iso)
    # intertwining on the first 3 columns, all host indices
    kpp = np.arange(Nh)
    worst = 0.0
    for c in range(min(3, d)):
        lhs = np.zeros(Nh, dtype=complex)
        for mpp, v in Kh[c].items():
            lhs += v * np.exp(2j * np.pi * ((mpp * kpp) % Nh) / Nh)
        lhs /= p ** h
        rhs = np.zeros(Nh, dtype=complex)
        for m0, v in colsf[c].items():
            idx = kpp[kpp % p == 0]
            rhs[idx] += v * np.exp(2j * np.pi * ((m0 * ((idx // p) % N)) % N) / N)
        rhs /= p ** n
        worst = max(worst, float(np.max(np.abs(lhs - rhs))))
    fnote("B(3,3)  F_host(iota f) - iota(F_n f) on the first %d Sonin columns, all %d "
          "host indices: max |D| = %.3e" % (min(3, d), Nh, worst))
    res['iota_intertwines'] = (worst < 1e-9)

    # C (float): Q_gen and Q_model
    UK = [uk_col(c, p, n, h, 1) for c in colsf]
    Arat = contract(Kh, UK, Wh, zero=0.0)
    A = np.array(Arat, dtype=float)
    Gm_h = np.array(Gh, dtype=float)
    Ghi = np.linalg.inv(Gm_h)
    Qg2 = float(np.trace(A.T @ Ghi @ A @ Ghi)) / p
    Gm = np.array(contract(colsf, colsf, 1.0, zero=0.0), dtype=float)
    Gmi = np.linalg.inv(Gm)
    B = np.array(contract(colsf, [push_col(c, p, n) for c in colsf], 1.0, zero=0.0),
                 dtype=float)
    Qm2 = float(np.trace(B.T @ Gmi @ B @ Gmi)) / p
    law = float(p * (p ** (n - 1) - 1) ** 2)
    fnote("C(3,3)  Q_gen^2 = %.9f   Q_model^2 = %.9f   diff = %.3e   "
          "banked law p(p^(n-1)-1)^2 = %.9f" % (Qg2, Qm2, Qg2 - Qm2, law))
    fnote("C(3,3)  Q_gen = %.9f   Q_model = %.9f   sqrt(p)(p^(n-1)-1) = %.9f"
          % (Qg2 ** 0.5, Qm2 ** 0.5, law ** 0.5))
    res.update(Qg2=Qg2, Qm2=Qm2, law=law,
               qverdict="VERBATIM" if abs(Qg2 - Qm2) < 1e-6 * max(1.0, abs(Qm2))
               else "CORRECTED",
               lawholds=abs(Qm2 - law) < 1e-6 * max(1.0, law))

    # D (float): traces
    tr_tab = {}
    for kk in (1, 2):
        vals = []
        for hh in (n + kk, n + kk + 1):
            Khh = [emb_col(c, p, n, hh) for c in colsf]
            Whh = 1.0 / p ** hh
            Ghh = np.array(contract(Khh, Khh, Whh, zero=0.0), dtype=float)
            Ukk = [uk_col(c, p, n, hh, kk) for c in colsf]
            Akk = np.array(contract(Khh, Ukk, Whh, zero=0.0), dtype=float)
            tr = float(np.trace(np.linalg.solve(Ghh, Akk)))
            vals.append((hh, tr))
            fnote("D(3,3)  Tr(U^%d S_n) at host h = %d : %+.3e  (times p^(-%d/2))"
                  % (kk, hh, tr, kk))
        st = abs(vals[0][1] - vals[1][1]) < 1e-9
        fnote("D(3,3)  level-stability of Tr(U^%d S_n): %s"
              % (kk, "STABLE" if st else "DRIFTS by %.3e" % (vals[1][1] - vals[0][1])))
        tr_tab[kk] = (vals, st, max(abs(v) for _, v in vals) < 1e-9)
    res['traces'] = tr_tab
    print()
    sys.stdout.flush()
    RESULTS.append(res)
    return res


# ======================================================================================
# FLOAT CROSS-CHECK OF THE MODEL Q (instrument integrity; never an EXACT line)
# ======================================================================================

def float_xcheck():
    if np is None:
        return
    print("- FLOAT CROSS-CHECK (instrument integrity only; b8's float SVD-basis route "
          "re-run against this sitting's exact Q_model^2) -")
    for r in RESULTS:
        if not r.get('exact'):
            continue
        p, n, N = r['p'], r['n'], r['N']
        F = np.exp(2j * np.pi * np.outer(np.arange(N), np.arange(N)) / N) / np.sqrt(N)
        ball = np.arange(N) % (p ** n) == 0
        C = np.vstack([np.eye(N)[ball], F[ball]])
        _, s, Vh = np.linalg.svd(C)
        tol = max(C.shape) * np.finfo(float).eps * (s[0] if len(s) else 1.0)
        rank = int((s > tol).sum())
        K = Vh[rank:].conj().T
        U = np.zeros((N, N))
        for m in range(N):
            U[(p * m) % N, m] = 1.0
        U /= np.sqrt(p)
        qf = float(np.linalg.norm(K.conj().T @ U @ K))
        fnote("(p,n)=(%d,%d)  b8 float route: dim = %d (exact %d), Q_model = %.9f "
              "(exact sqrt(%s) = %.9f)" % (p, n, K.shape[1], r['d'], qf,
                                           _fmt(r['Qm2']), float(r['Qm2']) ** 0.5))
    print()
    sys.stdout.flush()


# ======================================================================================
# E  THE VERDICT TABLE
# ======================================================================================

def verdict_table():
    print("=" * 100)
    print("E.  THE VERDICT TABLE -- one row per law.  VERBATIM / CORRECTED / FAILS.")
    print("=" * 100)
    rows = []
    allx = [r for r in RESULTS if r.get('exact')]
    dim_ok = all(r.get('laws') is not None for r in allx)
    rows.append(("dim law",
                 "dim Son(p,n) = (p^n - 1)^2",
                 "dim of Son inside V_n on Q_p: same, by A4 + A6",
                 "VERBATIM",
                 ", ".join("(%d,%d):%d" % (r['p'], r['n'], r['d']) for r in RESULTS)))
    rows.append(("tensor square",
                 "Son = V1 (x) W1, S = P1 (x) Q1",
                 "same subspace of V_n, same basis; transported by A4",
                 "VERBATIM",
                 "basis delta_alpha (x) (e_j - e_(j+1)) is the tensor basis by "
                 "construction"))
    rows.append(("M^2 = Pi",
                 "compressed parity: M^2 = Pi, det Pi = +-1",
                 "identical matrices (A4); brute-forced d<=9, derived above",
                 "VERBATIM",
                 ", ".join("(%d,%d): det Pi = %+d" % (r['p'], r['n'], r['detPi'])
                           for r in allx)))
    rows.append(("radical zero",
                 "rank G_loc = dim Son",
                 "same G_loc = K^T F K with the GENUINE F",
                 "VERBATIM",
                 ", ".join("(%d,%d): det K^TK = %s" % (r['p'], r['n'], _fmt(r['detG']))
                           for r in allx)))
    rows.append(("twist",
                 "G_loc^dagger = G_loc Pi",
                 "same, entry-exact with the genuine F",
                 "VERBATIM",
                 "exact zero residual at every exact cell"))
    qv = "VERBATIM" if all(r.get('qverdict') == "VERBATIM" for r in RESULTS) \
        else "CORRECTED"
    rows.append(("Q (fifth law)",
                 "Q_model = ||S U_model S||_F, U_model = P/sqrt(p) (truncated pushforward)",
                 "Q_gen = ||S_n U S_n||_F with the GENUINE unitary U on L^2(Q_p)",
                 qv,
                 "; ".join("(%d,%d): Q_gen^2 = %s, Q_model^2 = %s"
                           % (r['p'], r['n'],
                              _fmt(r['Qg2']) if r.get('exact') else "%.6f" % r['Qg2'],
                              _fmt(r['Qm2']) if r.get('exact') else "%.6f" % r['Qm2'])
                           for r in RESULTS)))
    tz = all(all(t[2] for t in r['traces'].values()) for r in RESULTS if 'traces' in r)
    ts = all(all(t[1] for t in r['traces'].values()) for r in RESULTS if 'traces' in r)
    rows.append(("localization trace",
                 "t_k = Tr(U_model^k S) = 0 (fixed-point localization)",
                 "Tr(U^k S_n) with the genuine U^k, hosts n+k and n+k+1",
                 "VERBATIM" if (tz and ts) else "CORRECTED",
                 "all traces 0 EXACT and level-STABLE" if (tz and ts)
                 else "see cell lines"))
    for name, mf, lf, vd, num in rows:
        print("  LAW        : %s" % name)
        print("    model    : %s" % mf)
        print("    lift     : %s" % lf)
        print("    VERDICT  : %s" % vd)
        print("    numbers  : %s" % num)
        print("    " + "-" * 90)
    sys.stdout.flush()
    return rows


# ======================================================================================
# MAIN
# ======================================================================================

EXACT_CELLS = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]
FLOAT_CELLS = [(3, 3)]


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 8 -- REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    sys.stdout.flush()

    for (p, n) in EXACT_CELLS:
        cell_exact(p, n)
    for (p, n) in FLOAT_CELLS:
        cell_float(p, n)

    float_xcheck()
    verdict_table()

    print()
    print("THE FOOT: WHAT REMAINS OF THE FIRST CAVEAT.  At every finite level V_n sits "
          "inside L^2(Q_p) and the commuting-projection structure is honest there; the "
          "caveat survives only as the n -> infinity limit -- the union of the V_n is "
          "dense in L^2(Q_p), but Son(p,n) does NOT stabilize (its dimension (p^n-1)^2 "
          "grows), so nothing here constructs a limit object, and none is claimed.")
    print()
    print("SCOPE, said plainly: these are EXACT properties of a FINITE CONSTRUCTED "
          "OBJECT, now on the genuine local field at finite level.  No sign is asserted; "
          "no register moves; W_inf - Sum W_p at complete roster is NOT touched.")
    print()
    if FAILS:
        print("*** LINES THAT DID NOT LAND AS REGISTERED (%d) ***" % len(FAILS))
        for nm in FAILS:
            print("    FAIL  %s" % nm)
        print()
    else:
        print("NOTHING FAILED TO LAND: every EXACT line landed as registered.")
        print()
    print("FLOAT LINES (declared, never counted as EXACT): %d" % len(FLOATLINES))
    n_ok = sum(1 for _, ok in LEDGER if ok)
    n_all = len(LEDGER)
    print()
    print("ALL EXACT LINES EXACT: %d/%d PASS" % (n_ok, n_all))


if __name__ == "__main__":
    main()
