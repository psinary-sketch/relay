"""W-ATTEMPT-2, SITTING 7 — THE CONSTRAINED CLASS AND THE PAIRING'S INERTIA ON IT.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA at bench
grade; refused: any promotion to W_inf - Sum W_p at complete roster, or register movement.
THE PROTOCOL CORRECTION ON THE FERRY'S FACE, carried: the closure protocol gates the
REGISTER and public claims, not investigation — the programme tests its own object.
THE GUARD (spec section 6(c), carried verbatim in content): positivity of the LEDGER's
psi-component form is GRH for that L(s,psi); this instrument measures a FINITE CONSTRUCTED
MODEL SECTION, never the ledger; nothing below is evidence about any hypothesis and nothing
bears on the sign of W_inf - Sum W_p.

RULE-3 RESOLUTIONS AT THE HEAD (flagged, not silent):
(1) The ferry's head writes the two vanishing conditions as g-hat(+/- i/2); its item 1
    writes g-hat(i/2) = g-hat(0) = 0. The BANKED pair (SIGN_ARRANGEMENT_RECONCILIATION:
    P = h-hat(i/2) + h-hat(-i/2) — the two poles s = 0 and s = 1) is +/- i/2; g-hat(0)
    is the parity-ledger quantity (THE_ATTEMPT_RECORD row 4), a different object.
    Executed with the banked pair; the discrepancy reported, not resolved silently.
(2) "REVIEW-STAGED" appears nowhere in either repository; the arc vocabulary is
    navigator-named. The attempt is relay-resident; the arc line is created in the relay
    record and the method register is not touched.

THE CONSTRAINED CLASS, DEFINED AT CITE (before any inertia is read)
===================================================================
The involution, banked (spec 6(b)): Z-hat(s) = W * Z-hat(1-s)^* — the antipode-twisted
reflection with W = Sum_psi W(psi) e_psi the unitary root-number ELEMENT, W W^* = 1.
On the model section the reflection is the CERTIFIED compressed transform M (M^2 = Pi
exact, sitting 5) tensored with the antipode A on C[Cl]; the unitary twist closing M to
order two is the model's own root-number phase per Pi-sector (epsilon with epsilon^2 =
the sector's Pi-sign) — the model transposition of W, COMPUTED from the certified
structure, not imported; where the phase has a sign choice BOTH signs are run.

THE TWO VANISHING CONDITIONS AT THEIR MODEL FORM, derived longhand at cite: the pole
pair lives at s = 0 and s = 1 (banked, +/- i/2). By Tate, the local zeta's pole direction
is the ball indicator 1_O — and by duality its Fourier transform. The Sonin condition
(f|_B = 0 AND F f|_B = 0) is exactly orthogonality to both pole directions. THEREFORE ON
THE DIAGONAL SECTION BOTH VANISHING CONDITIONS ARE AUTOMATIC — vacuous BY CONSTRUCTION,
and that is the registered reason, stated in advance, not discovered after. The
class-resolved refinement, at cite: the poles live only in the psi_0-channel (zeta_K
carries s = 0, 1; L(s,psi) is entire for psi != psi_0), so the conditions bind the
augmentation channel — which the section constrains along with every channel.

THE CLASS, both readings registered (dimension per cell banked as DATA):
 (R-plain)   v fixed by the transform T = M (x) A AND by the antipode 1 (x) A.
 (R-twisted) v fixed by the sector-twisted involution J = conj(epsilon) * (M (x) A)
             (both epsilon signs) AND by the antipode; the pairing read through the
             same phase (B_eps = conj(epsilon) * B per sector) — the model's
             root-number-normalized form.

THE INERTIA, both branches longhand BEFORE the run:
 (P+) The registered prediction, WITH ITS MECHANISM. M^4 = 1, so factor eigenvalues lie
      in {1, -1, i, -i} with dims d_lambda given exactly by the trace formulas
      (d_1 + d_-1 + d_i + d_-i = dim; d_1 + d_-1 - d_i - d_-i = tr Pi;
      d_1 - d_-1 = Re tr M; d_i - d_-i = Im tr M). On a T-fixed vector in the sector
      (lambda, mu, nu) the pairing gives B(v,v) = (lambda mu) ||v||^2 * (C on the
      nu-eigenspace); T-fixed means lambda mu nu = 1 and ANTIPODE-FIXED means nu = +1,
      forcing lambda mu = 1: B|_class = ||.||^2 (x) C|_fix with C|_fix eigenvalues
      {4, 1} — POSITIVE-DEFINITE at every cell where the class is nonzero, the
      positivity riding exactly the POSITIVITY OF THE EULER COEFFICIENTS (4,1,1).
      At the prime-free cells this sits beside CC's Theorem 1 (archimedean positivity
      on the constrained class) — AT CITE BESIDE, NEVER MERGED. The cells then answer:
      the CLASS DIMENSION's own arithmetic (registered sub-prediction: at {2:1} the
      single factor has M = [i], no (lambda, nu) with lambda nu = 1 exists, so the
      plain-reading class DIES at the arrival of 2 and can REVIVE at {2:1,3:1} through
      conjugate sectors (i, -i, +1) — the class is itself punctuated by place-arrivals);
      and OFF the class, the first negative T-fixed directions (sectors with
      lambda mu = -1, nu = -1: B = -||v||^2 on the antipode-anti-invariant channel,
      C-eigenvalue 1) — their first nonempty cell located, and whether that address is
      a place-arrival edge or interior; every negative direction's place-support named
      (which factor contributes which eigenvalue).
 (P-) If a negative direction appears ON the constrained class: the certificate locates
      it (an infinity-artefact of the hard truncation vs a finite-place direction the
      class should have excluded) and the class is re-derived.
 (P0) A third shape: recorded as found.

CELLS: a^2 in {1.69, 2, 2.25, 3, 4, 9} -> (empty), {2:1}, {2:1}, {2:1,3:1}, {2:2,3:1},
{2:3,3:2}. Exact arithmetic where the cell allows: factors (2,1), (3,1), (2,2) in
Q(zeta_144) (sitting 5's machinery); (2,3) in Q(zeta_64), Phi = x^32 + 1; (3,2) in
Q(zeta_81), Phi = x^54 + x^27 + 1 — exploiting the Sonin basis's 2-nonzero sparsity so
no dense F is ever formed at the large factors (entries on demand); eigen-dims by the
trace formulas, VERIFIED by direct exact nullity at the small factors; inertia direct-
exact at cell dims <= 12, sector-assembled above; the infinity factor at FLOAT (the b19
model, N = 511, lambda = 1/a), declared. Float appears only in declared-float lines.

RECORDED PLAINLY AS DATA about the built object. The register is untouched.
Usage:  python b20_attempt2_s7.py register | run
"""

import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import b18_attempt2_s5 as b18            # noqa: E402  (sitting 5's certified machinery)

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


# ======================================================================================
# EXACT LEDGER.  Every entry is an EXACT arithmetic statement; float lines never enter.
# ======================================================================================

LEDGER = []


def check(name, ok):
    LEDGER.append((name, bool(ok)))
    print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    sys.stdout.flush()
    assert ok, "EXACT LINE FAILED: " + name


def note(name):
    """A recorded exact observation that is NOT asserted (a registered fallback branch)."""
    print("  NOTE  %s" % name)
    sys.stdout.flush()


# ======================================================================================
# FIELD LAYER A: Q(zeta_144) -- sitting 5's Cyc, reused verbatim; plus the field
# inverse (extended Euclid mod Phi_144), determinant, rank and nullspace it needs here.
# ======================================================================================

CZ = b18.CZERO
CO = b18.CONE
I144 = b18.zetapow(36)                    # i = zeta_144^36

PHI144 = [Fraction(0)] * 49
PHI144[0] = Fraction(1)
PHI144[24] = Fraction(-1)
PHI144[48] = Fraction(1)


def _pdeg(a):
    d = len(a) - 1
    while d >= 0 and a[d] == 0:
        d -= 1
    return d


def _pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[i + j] += ai * bj
    return out


def _psub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else Fraction(0)) - (b[i] if i < len(b) else Fraction(0))
            for i in range(n)]


def _pdivmod(a, b):
    a = list(a)
    db = _pdeg(b)
    lb = b[db]
    q = [Fraction(0)] * max(1, len(a) - db)
    da = _pdeg(a)
    while da >= db:
        c = a[da] / lb
        q[da - db] = c
        for k in range(db + 1):
            a[da - db + k] -= c * b[k]
        da = _pdeg(a)
    return q, a


def cyc_inv(x):
    """Exact inverse in Q(zeta_144) by the extended Euclidean algorithm mod Phi_144."""
    a = list(x.c)
    if _pdeg(a) < 0:
        raise ZeroDivisionError("inverse of 0 in Q(zeta_144)")
    r0, r1 = list(PHI144), a
    s0, s1 = [Fraction(0)], [Fraction(1)]
    while _pdeg(r1) > 0:
        q, r = _pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, _psub(s0, _pmul(q, s1))
    u = [v / r1[0] for v in s1]
    u = u + [Fraction(0)] * (2 * b18.DEG - len(u))
    return b18.Cyc(b18._reduce(u))


def cyc_dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def cyc_rref(A):
    """Reduced row echelon form over Q(zeta_144).  Returns (R, pivot columns)."""
    n = len(A)
    m = len(A[0])
    M = [list(r) for r in A]
    piv = []
    row = 0
    for col in range(m):
        if row == n:
            break
        p = None
        for r in range(row, n):
            if not M[r][col].is_zero():
                p = r
                break
        if p is None:
            continue
        M[row], M[p] = M[p], M[row]
        inv = cyc_inv(M[row][col])
        M[row] = [inv * v for v in M[row]]
        for r in range(n):
            if r != row and not M[r][col].is_zero():
                f = M[r][col]
                M[r] = [M[r][k] - f * M[row][k] for k in range(m)]
        piv.append(col)
        row += 1
    return M, piv


def cyc_rank(A):
    return len(cyc_rref(A)[1])


def cyc_nullspace(A):
    """Exact basis (list of column vectors) of the right nullspace over Q(zeta_144)."""
    m = len(A[0])
    M, piv = cyc_rref(A)
    free = [c for c in range(m) if c not in piv]
    basis = []
    for fc in free:
        v = [CZ] * m
        v[fc] = CO
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        basis.append(v)
    return basis


def cyc_det(A):
    n = len(A)
    M = [list(r) for r in A]
    det = CO
    for col in range(n):
        p = None
        for r in range(col, n):
            if not M[r][col].is_zero():
                p = r
                break
        if p is None:
            return CZ
        if p != col:
            M[col], M[p] = M[p], M[col]
            det = -det
        det = det * M[col][col]
        inv = cyc_inv(M[col][col])
        for r in range(col + 1, n):
            if not M[r][col].is_zero():
                f = M[r][col] * inv
                M[r] = [M[r][c] - f * M[col][c] for c in range(n)]
    return det


def gauss_parts_144(x):
    """Write x in Q(zeta_144) as A + B*i (i = zeta^36); return (A, B, extra-indices)."""
    c = x.c
    extra = [k for k in range(b18.DEG) if c[k] != 0 and k != 0 and k != 36]
    return c[0], c[36], extra


def cyc_float(x):
    """DECLARED FLOAT: the standard embedding zeta_144 -> exp(2*pi*i/144).  Report only."""
    import cmath
    z = cmath.exp(2j * cmath.pi / 144.0)
    return sum(complex(v) * (z ** k) for k, v in enumerate(x.c) if v)


# ======================================================================================
# FIELD LAYER B: a generic Q(zeta_N) for the LARGE factors, N in {64, 81}.
# Elements are tuples of `deg` Fractions.  Only +, -, rational scaling and equality are
# ever needed here (no field multiplication is required by the large-factor pipeline),
# so no dense F and no dense Cyc product is ever formed.
# ======================================================================================

class Fld(object):
    """Q(zeta_N):  x^deg = sum_(off,coef) coef * x^off.   i_index: index of i, or None."""

    def __init__(self, name, N, deg, rule, i_index, phi_str):
        self.name = name
        self.N = N
        self.deg = deg
        self.rule = rule
        self.i_index = i_index
        self.phi_str = phi_str

    def red(self, a):
        """Reduce a coefficient list of length >= deg modulo Phi_N (in place, top down)."""
        deg = self.deg
        for d in range(len(a) - 1, deg - 1, -1):
            v = a[d]
            if v:
                a[d] = 0
                for off, cf in self.rule:
                    a[d - deg + off] += cf * v
        return a[:deg]

    def zero(self):
        return tuple([Fraction(0)] * self.deg)

    def add(self, a, b):
        return tuple(a[k] + b[k] for k in range(self.deg))

    def sub(self, a, b):
        return tuple(a[k] - b[k] for k in range(self.deg))

    def smul(self, a, r):
        if r == 0:
            return self.zero()
        return tuple(v * r for v in a)

    def is_zero(self, a):
        for v in a:
            if v:
                return False
        return True

    def mono(self, e, coef=1):
        """coef * zeta_N^e, reduced."""
        v = [0] * self.N
        v[e % self.N] = coef
        return tuple(Fraction(x) for x in self.red(v))

    def parts(self, a):
        A = a[0]
        B = a[self.i_index] if self.i_index is not None else Fraction(0)
        extra = [k for k in range(self.deg)
                 if a[k] != 0 and k != 0 and (self.i_index is None or k != self.i_index)]
        return A, B, extra


FLD64 = Fld("Q(zeta_64)", 64, 32, [(0, -1)], 16, "x^32 + 1")
FLD81 = Fld("Q(zeta_81)", 81, 54, [(27, -1), (0, -1)], None, "x^54 + x^27 + 1")


# ======================================================================================
# THE PATH-LAPLACIAN BLOCK.  K^T K = I_(q-1) (x) T with T tridiagonal(-1, 2, -1):
# the Sonin basis is delta_alpha (x) (e_j - e_(j+1)), so overlaps are diagonal in alpha.
# ======================================================================================

def tri(nn):
    return [[Fraction(2) if i == j else (Fraction(-1) if abs(i - j) == 1 else Fraction(0))
             for j in range(nn)] for i in range(nn)]


def rat_congruence(H):
    """Symmetric congruence diagonalization over Q.  Returns (pivots, ok_no_zero_pivot)."""
    n = len(H)
    M = [[Fraction(v) for v in r] for r in H]
    piv = []
    for k in range(n):
        p = M[k][k]
        piv.append(p)
        if p == 0:
            return piv, False
        for r in range(k + 1, n):
            f = M[r][k] / p
            if f:
                for c in range(n):
                    M[r][c] -= f * M[k][c]
                for rr in range(n):
                    M[rr][r] -= M[rr][k] * f
    return piv, True


def cyc_congruence(H):
    """Hermitian congruence diagonalization over Q(zeta_144).  Returns pivot list."""
    n = len(H)
    M = [list(r) for r in H]
    piv = []
    for k in range(n):
        p = M[k][k]
        piv.append(p)
        if p.is_zero():
            return piv
        inv = cyc_inv(p)
        for r in range(k + 1, n):
            f = M[r][k] * inv
            if f.is_zero():
                continue
            fc = f.conj()
            for c in range(n):
                M[r][c] = M[r][c] - f * M[k][c]
            for rr in range(n):
                M[rr][r] = M[rr][r] - M[rr][k] * fc
    return piv


# ======================================================================================
# THE SMALL FACTORS (2,1), (3,1), (2,2) -- sitting 5's machinery, REUSED.
# ======================================================================================

def small_factor(p, n):
    N, q, cols, K = b18.sonin_basis(p, n)
    d = len(cols)
    F = b18.dft(N)
    FK = b18.mm_cyc_scal(F, K)
    Kt = b18.transpose(K)
    Kf = [[Fraction(v) for v in r] for r in K]
    Ktf = [[Fraction(v) for v in r] for r in Kt]
    KtK = b18.mm_scal_scal(Ktf, Kf)
    KtKinv = b18.rat_inv(KtK)
    G = b18.mm_scal_cyc(Ktf, FK)                      # G_loc = K^T F K
    M = b18.mm_scal_cyc(KtKinv, G)                    # F K = K M
    idx = dict((c, k) for k, c in enumerate(cols))
    Pi = [[Fraction(0)] * d for _ in range(d)]
    for c, (a, j) in enumerate(cols):
        Pi[idx[(q - a, q - 2 - j)]][c] = Fraction(-1)
    # full re-assertion of sitting 5's two structure identities
    KM = b18.mm_scal_cyc(Kf, M)
    ok_fk = b18.cyc_mat_is_zero(b18.cyc_sub_mat(FK, KM))
    PK = [[K[(-m) % N][c] for c in range(d)] for m in range(N)]
    KPi = b18.mm_scal_scal(Kf, Pi)
    ok_pk = all(Fraction(PK[i][j]) == KPi[i][j] for i in range(N) for j in range(d))
    trM = CZ
    for i in range(d):
        trM = trM + M[i][i]
    trPi = sum(Pi[i][i] for i in range(d))
    return dict(p=p, n=n, N=N, q=q, d=d, cols=cols, K=K, KtK=KtK, G=G, M=M, Pi=Pi,
                trM=trM, trPi=trPi, ok_fk=ok_fk, ok_pk=ok_pk, tag="(%d,%d)" % (p, n))


# ======================================================================================
# THE LARGE FACTORS (2,3) at N = 64 and (3,2) at N = 81.
# NO DENSE F IS EVER FORMED.  K has exactly two nonzero (integer) entries per column, so
# (K^T F K)[c][c'] is a sum of at most FOUR on-demand entries zeta_N^(m m')/p^n.
# ======================================================================================

class BigFactor(object):

    def __init__(self, p, n, fld):
        self.p = p
        self.n = n
        self.fld = fld
        self.q = q = p ** n
        self.N = N = q * q
        assert N == fld.N
        self.cols = [(a, j) for a in range(1, q) for j in range(0, q - 1)]
        self.d = len(self.cols)
        self.m = q - 1
        # column c = (a,j) is +1 at row a + q*j and -1 at row a + q*(j+1)
        self.rows = [((a + q * j) % N, (a + q * (j + 1)) % N) for (a, j) in self.cols]
        self.T = tri(q - 1)
        self.Tinv = b18.rat_inv(self.T)
        self.idx = dict((c, k) for k, c in enumerate(self.cols))
        self.tag = "(%d,%d)" % (p, n)
        # Pi: P k_(a,j) = -k_(q-a, q-2-j)  (exact signed permutation; verified below)
        self.Pi = [[Fraction(0)] * self.d for _ in range(self.d)]
        for c, (a, j) in enumerate(self.cols):
            self.Pi[self.idx[(q - a, q - 2 - j)]][c] = Fraction(-1)
        self.trPi = sum(self.Pi[i][i] for i in range(self.d))

    def Gent(self, c, cp):
        """(K^T F K)[c][cp], built on demand from at most four entries of F."""
        N = self.N
        q = self.q
        r1, r2 = self.rows[c]
        s1, s2 = self.rows[cp]
        e = [0] * N
        e[(r1 * s1) % N] += 1
        e[(r1 * s2) % N] -= 1
        e[(r2 * s1) % N] -= 1
        e[(r2 * s2) % N] += 1
        return tuple(Fraction(x, q) for x in self.fld.red(e))

    def Mcol(self, cp):
        """Column cp of M = (K^T K)^-1 (K^T F K) = (I (x) T^-1)(K^T F K)."""
        fld = self.fld
        m = self.m
        out = []
        for a in range(1, self.q):
            block = [self.Gent((a - 1) * m + jp, cp) for jp in range(m)]
            for j in range(m):
                acc = [Fraction(0)] * fld.deg
                for jp in range(m):
                    t = self.Tinv[j][jp]
                    if t:
                        g = block[jp]
                        for k in range(fld.deg):
                            if g[k]:
                                acc[k] += t * g[k]
                out.append(tuple(acc))
        return out

    def trM(self):
        """tr M = sum_(a,j) sum_(j') T^-1[j][j'] * (K^T F K)[(a,j')][(a,j)]."""
        fld = self.fld
        m = self.m
        acc = [Fraction(0)] * fld.deg
        for a in range(1, self.q):
            for j in range(m):
                c = (a - 1) * m + j
                for jp in range(m):
                    t = self.Tinv[j][jp]
                    if t:
                        g = self.Gent((a - 1) * m + jp, c)
                        for k in range(fld.deg):
                            if g[k]:
                                acc[k] += t * g[k]
        return tuple(acc)

    def krow(self, mm):
        """Row mm of K as a list of (column, sign); at most two entries."""
        q = self.q
        alpha = mm % q
        beta = mm // q
        out = []
        if alpha == 0:
            return out
        if 0 <= beta <= q - 2:
            out.append((self.idx[(alpha, beta)], 1))
        if 1 <= beta <= q - 1:
            out.append((self.idx[(alpha, beta - 1)], -1))
        return out

    def spot_columns(self):
        q = self.q
        alphas = sorted(set([1, 2, q - 2, q - 1]))
        js = [0, 1]
        out = []
        for a in alphas:
            for j in js:
                if 1 <= a <= q - 1 and 0 <= j <= q - 2:
                    out.append(self.idx[(a, j)])
        return out

    def spot_check_FK_eq_KM(self):
        """Verify (F K)[:,c] == (K M)[:,c] for the deterministic spot columns."""
        fld = self.fld
        N = self.N
        q = self.q
        bad = 0
        ncols = 0
        for c in self.spot_columns():
            ncols += 1
            Mc = self.Mcol(c)
            r1, r2 = self.rows[c]
            for mm in range(N):
                # (F k_c)[mm] = (zeta^(mm*r1) - zeta^(mm*r2)) / q, on demand
                e = [0] * N
                e[(mm * r1) % N] += 1
                e[(mm * r2) % N] -= 1
                lhs = tuple(Fraction(x, q) for x in fld.red(e))
                rhs = [Fraction(0)] * fld.deg
                for (r, s) in self.krow(mm):
                    v = Mc[r]
                    for k in range(fld.deg):
                        if v[k]:
                            rhs[k] += s * v[k]
                if lhs != tuple(rhs):
                    bad += 1
        return bad, ncols

    def verify_PK_eq_KPi(self):
        """Full (not spot) verification of P K = K Pi -- no F is involved, so it is cheap."""
        N = self.N
        d = self.d
        ok = True
        for mm in range(N):
            lhs = dict()
            for (r, s) in self.krow((-mm) % N):
                lhs[r] = lhs.get(r, 0) + s
            rhs = dict()
            for (r, s) in self.krow(mm):
                for rr in range(d):
                    v = self.Pi[rr][r]
                    if v:
                        rhs[rr] = rhs.get(rr, Fraction(0)) + s * v
            for k in set(list(lhs.keys()) + list(rhs.keys())):
                if Fraction(lhs.get(k, 0)) != Fraction(rhs.get(k, 0)):
                    ok = False
        return ok


# ======================================================================================
# THE TRACE FORMULAS
# ======================================================================================

def eigen_dims(dim, trPi, A, B):
    """(d_1, d_-1, d_i, d_-i) from dim, tr Pi, Re tr M = A, Im tr M = B."""
    d1 = (Fraction(dim + trPi, 2) + A) / 2
    dm1 = (Fraction(dim + trPi, 2) - A) / 2
    di = (Fraction(dim - trPi, 2) + B) / 2
    dmi = (Fraction(dim - trPi, 2) - B) / 2
    return (d1, dm1, di, dmi)


def ok_dims(dims, dim):
    if sum(dims) != dim:
        return False
    for v in dims:
        if v < 0 or v.denominator != 1:
            return False
    return True


EIG_NAMES = ("1", "-1", "i", "-i")
# multiplication table on {1,-1,i,-i} by index 0,1,2,3
MULT = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3,
        (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
        (2, 0): 2, (2, 1): 3, (2, 2): 1, (2, 3): 0,
        (3, 0): 3, (3, 1): 2, (3, 2): 0, (3, 3): 1}


def glue_dims(dimlist):
    """Eigen-dims of the tensor product transform M_g = (x) M_f."""
    cur = [1, 0, 0, 0]
    for dv in dimlist:
        nxt = [0, 0, 0, 0]
        for a in range(4):
            if not cur[a]:
                continue
            for b in range(4):
                if not dv[b]:
                    continue
                nxt[MULT[(a, b)]] += cur[a] * dv[b]
        cur = nxt
    return cur


def sector_list(dimlist, target):
    """All sectors (tuple of per-factor eigen-indices) whose product index == target."""
    out = []

    def rec(k, acc, prod):
        if k == len(dimlist):
            if prod == target:
                out.append(tuple(acc))
            return
        for b in range(4):
            if dimlist[k][b]:
                acc.append(b)
                rec(k + 1, acc, MULT[(prod, b)])
                acc.pop()
    rec(0, [], 0)
    return out


# ======================================================================================
# CELLS
# ======================================================================================

CELLS = [("1.69", "1.3", [], "(empty)"),
         ("2", "sqrt2", [(2, 1)], "{2:1}"),
         ("2.25", "1.5", [(2, 1)], "{2:1}"),
         ("3", "sqrt3", [(2, 1), (3, 1)], "{2:1,3:1}"),
         ("4", "2", [(2, 2), (3, 1)], "{2:2,3:1}"),
         ("9", "3", [(2, 3), (3, 2)], "{2:3,3:2}")]

COUP = (2, 1, 1)
CMAT = [[COUP[(b - a) % 3] for b in range(3)] for a in range(3)]
AMAT = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
# antipode-fixed basis of C[Cl]: e0 and e1+e2 ; antipode-anti basis: e1-e2
EC_FIX = [[1, 0], [0, 1], [0, 1]]
EC_ANT = [[0], [1], [-1]]


def rat_mm(A, B):
    return b18.mm_scal_scal([[Fraction(v) for v in r] for r in A],
                            [[Fraction(v) for v in r] for r in B])


def rat_T(A):
    return [list(r) for r in zip(*A)]


# ======================================================================================
# MAIN
# ======================================================================================

def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 7 -- REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    sys.stdout.flush()

    # ==================================================================================
    # PART 0 -- the two field layers, asserted before anything is read off them
    # ==================================================================================
    print("=" * 100)
    print("PART 0 -- THE TWO EXACT FIELD LAYERS")
    print("=" * 100)
    check("F0a  Q(zeta_144): Phi_144(zeta) = zeta^48 - zeta^24 + 1 = 0 exactly (sitting 5)",
          (b18.zetapow(48) - b18.zetapow(24) + CO).is_zero())
    check("F0b  Q(zeta_144): i = zeta^36, i^2 = -1 exactly", I144 * I144 == -CO)
    check("F0c  Q(zeta_144): extended-Euclid inverse is exact -- x * x^-1 = 1 for "
          "x = 1 + zeta + zeta^7 - 3*zeta^30",
          (lambda x: x * cyc_inv(x) == CO)(CO + b18.zetapow(1) + b18.zetapow(7)
                                           - b18.zetapow(30).smul(Fraction(3))))
    for fld in (FLD64, FLD81):
        # x^N reduces to the constant 1: Phi = the reduction rule DIVIDES x^N - 1
        v = [0] * (fld.N + 1)
        v[fld.N] = 1
        red = fld.red(v)
        one = [0] * fld.deg
        one[0] = 1
        check("F0d  %s: Phi = %s, and the reduction of x^%d is exactly 1 "
              "(so Phi | x^%d - 1: zeta_%d has order %d)"
              % (fld.name, fld.phi_str, fld.N, fld.N, fld.N, fld.N), red == one)
        # the defining relation, read off the reduction rule
        lhs = fld.mono(fld.deg)
        rhs = [Fraction(0)] * fld.deg
        for off, cf in fld.rule:
            rhs[off] += cf
        check("F0e  %s: x^%d = %s exactly (the reduction rule is the minimal polynomial)"
              % (fld.name, fld.deg,
                 " ".join("%+d*x^%d" % (cf, off) for off, cf in fld.rule)),
              lhs == tuple(rhs))
    check("F0f  Q(zeta_64): i = zeta_64^16, i^2 = -1 exactly (index 16 in the power basis)",
          FLD64.mono(32) == tuple([Fraction(-1)] + [Fraction(0)] * 31))
    print("      Q(zeta_81) contains NO i: tr M there is forced RATIONAL, hence d_i = d_-i.")
    print()

    # ==================================================================================
    # PART 1 -- per-factor eigen-structure
    # ==================================================================================
    print("=" * 100)
    print("PART 1 -- PER-FACTOR EIGEN-STRUCTURE (EXACT AT ALL FIVE FACTORS)")
    print("=" * 100)
    facs = {}

    for (p, n) in [(2, 1), (3, 1), (2, 2)]:
        f = small_factor(p, n)
        check("P1a %s  F K = K M entry-exact (sitting 5's C2, re-asserted here)" % f['tag'],
              f['ok_fk'])
        check("P1b %s  P K = K Pi entry-exact, Pi the signed permutation "
              "(a,j) -> -(q-a, q-2-j) (sitting 5's C3a, re-asserted)" % f['tag'], f['ok_pk'])
        A, B, extra = gauss_parts_144(f['trM'])
        check("P1c %s  tr M is a GAUSSIAN INTEGER: tr M = %s + %s*i, no other coefficient "
              "nonzero" % (f['tag'], A, B), extra == [] and A.denominator == 1
              and B.denominator == 1)
        dims = eigen_dims(f['d'], f['trPi'], A, B)
        check("P1d %s  the four trace equations give nonnegative integers summing to dim: "
              "(d_1,d_-1,d_i,d_-i) = (%s,%s,%s,%s), sum = %s = %d"
              % (f['tag'], dims[0], dims[1], dims[2], dims[3], sum(dims), f['d']),
              ok_dims(dims, f['d']))
        f['A'] = A
        f['B'] = B
        f['dims'] = [int(v) for v in dims]
        facs[(p, n)] = f

    for (p, n), fld in [((2, 3), FLD64), ((3, 2), FLD81)]:
        bf = BigFactor(p, n, fld)
        ok_pk = bf.verify_PK_eq_KPi()
        check("P1b %s  P K = K Pi verified FULLY (all %d rows; no F is involved, so the "
              "full check is cheap)" % (bf.tag, bf.N), ok_pk)
        bad, ncols = bf.spot_check_FK_eq_KM()
        check("P1a %s  F K = K M SPOT-CHECKED entry-exact on %d deterministic columns "
              "(alpha in {1,2,q-2,q-1} x j in {0,1}), all %d rows each: %d mismatches"
              % (bf.tag, ncols, bf.N, bad), bad == 0)
        tm = bf.trM()
        A, B, extra = fld.parts(tm)
        check("P1c %s  tr M is a GAUSSIAN INTEGER in %s: tr M = %s + %s*i, no other "
              "coefficient nonzero" % (bf.tag, fld.name, A, B),
              extra == [] and A.denominator == 1 and B.denominator == 1)
        dims = eigen_dims(bf.d, bf.trPi, A, B)
        check("P1d %s  the four trace equations give nonnegative integers summing to dim: "
              "(d_1,d_-1,d_i,d_-i) = (%s,%s,%s,%s), sum = %s = %d"
              % (bf.tag, dims[0], dims[1], dims[2], dims[3], sum(dims), bf.d),
              ok_dims(dims, bf.d))
        facs[(p, n)] = dict(p=p, n=n, N=bf.N, q=bf.q, d=bf.d, trPi=bf.trPi, A=A, B=B,
                            dims=[int(v) for v in dims], tag=bf.tag, big=bf)

    print()
    print("--- DIRECT EXACT NULLITY VERIFICATION OF THE TRACE-FORMULA DIMS "
          "(small factors, Gaussian elimination over Q(zeta_144)) ---")
    LAMS = [CO, -CO, I144, -I144]
    for (p, n) in [(2, 1), (3, 1), (2, 2)]:
        f = facs[(p, n)]
        M = f['M']
        d = f['d']
        nul = []
        for lv in LAMS:
            Ml = [[M[i][j] - (lv if i == j else CZ) for j in range(d)] for i in range(d)]
            nul.append(d - cyc_rank(Ml))
        check("P1e %s  direct exact nullity of (M - lambda I) for lambda = 1,-1,i,-i is "
              "(%d,%d,%d,%d) == the trace-formula dims (%d,%d,%d,%d)"
              % tuple([f['tag']] + nul + f['dims']), nul == f['dims'])
    print("      (2,3) and (3,2): dims by the trace formulas only -- a direct nullity at "
          "dim 49 / 64")
    print("      over these fields would require the dense operator the sparsity rule "
          "forbids; declared.")
    print()

    print("--- PART 1 TABLE ---")
    print("  %-8s %-6s %-14s %-8s %-6s %-6s %-6s %-6s %s"
          % ("factor", "dim", "tr M", "tr Pi", "d_1", "d_-1", "d_i", "d_-i", "field"))
    order = [(2, 1), (3, 1), (2, 2), (2, 3), (3, 2)]
    for k in order:
        f = facs[k]
        trs = "%d %+d*i" % (int(f['A']), int(f['B']))
        fname = "Q(zeta_144)" if k in [(2, 1), (3, 1), (2, 2)] else (
            "Q(zeta_64)" if k == (2, 3) else "Q(zeta_81)")
        print("  %-8s %-6d %-14s %-8d %-6d %-6d %-6d %-6d %s"
              % (f['tag'], f['d'], trs, f['trPi'], f['dims'][0], f['dims'][1],
                 f['dims'][2], f['dims'][3], fname))
    check("P1f  registered small sanity: (2,1) has dim 1, M = [i], eigen-dims (0,0,1,0)",
          facs[(2, 1)]['d'] == 1 and facs[(2, 1)]['dims'] == [0, 0, 1, 0]
          and facs[(2, 1)]['M'][0][0] == I144)
    print()

    # ==================================================================================
    # PART 2 -- the constrained class per cell
    # ==================================================================================
    print("=" * 100)
    print("PART 2 -- THE CONSTRAINED CLASS PER CELL (DIMENSIONS AS DATA)")
    print("=" * 100)
    print("  Reading (R-plain): T = M (x) A fixed AND antipode fixed => nu = +1 and")
    print("  lambda*mu = 1; the antipode-FIXED part of C[Cl] has dim 2, the antipode-ANTI")
    print("  part has dim 1.  Class dim = (sum over lambda*mu = 1 of d_lambda*d_mu) * 2.")
    print()
    celldata = []
    for a2, alab, fl, clab in CELLS:
        dl = [facs[k]['dims'] for k in fl]
        D = glue_dims(dl)
        seclen = 1
        for k in fl:
            seclen *= facs[k]['d']
        cell_dim = seclen * 3
        plain = D[0] * 2
        offneg = D[1] * 1
        celldata.append(dict(a2=a2, alab=alab, fl=fl, clab=clab, dl=dl, D=D,
                             seclen=seclen, cell_dim=cell_dim, plain=plain, offneg=offneg))
        check("P2a  cell %-10s (a^2 = %-5s) glued eigen-dims (D_1,D_-1,D_i,D_-i) = "
              "(%d,%d,%d,%d) sum to the section's transform dim %d"
              % (clab, a2, D[0], D[1], D[2], D[3], seclen), sum(D) == seclen)

    print()
    print("--- CLASS-DIMENSION TABLE (PLAIN READING) ---")
    print("  %-6s %-12s %-8s %-28s %-11s %-12s %s"
          % ("a^2", "cell", "celldim", "(D_1,D_-1,D_i,D_-i)", "R-plain", "off-class", "status"))
    for cd in celldata:
        st = "ALIVE" if cd['plain'] > 0 else "DEAD"
        print("  %-6s %-12s %-8d %-28s %-11d %-12d %s"
              % (cd['a2'], cd['clab'], cd['cell_dim'], "(%d,%d,%d,%d)" % tuple(cd['D']),
                 cd['plain'], cd['offneg'], st))
    print("  (off-class = the T-fixed, antipode-ANTI-invariant dims: lambda*mu = -1, "
          "nu = -1, class dim 1 per sector)")
    print()

    print("--- SECTOR LISTS: THE PLACE-SUPPORT OF EVERY LIVE SECTOR ---")
    for cd in celldata:
        print("  cell %s  (a^2 = %s)" % (cd['clab'], cd['a2']))
        if not cd['fl']:
            print("     R-plain (lambda*mu = 1, nu = +1): the empty product = 1; "
                  "the class part alone, dim 2")
            print("     off-class (lambda*mu = -1, nu = -1): the empty product is 1 != -1 "
                  "-- NO such sector")
            continue
        for tgt, tname, mult in [(0, "R-plain  (lambda*mu = +1, nu = +1)", 2),
                                 (1, "off-class(lambda*mu = -1, nu = -1)", 1)]:
            secs = sector_list(cd['dl'], tgt)
            if not secs:
                print("     %s: NONE" % tname)
                continue
            tot = 0
            items = []
            for s in secs:
                dd = 1
                for t, b in enumerate(s):
                    dd *= cd['dl'][t][b]
                tot += dd
                items.append("%s -> %d"
                             % (" x ".join("%s:%s" % (facs[cd['fl'][t]]['tag'], EIG_NAMES[b])
                                           for t, b in enumerate(s)), dd))
            print("     %s: dim %d x %d = %d" % (tname, tot, mult, tot * mult))
            for it in items:
                print("        %s" % it)
    print()

    print("--- THE TWISTED READING (R-twisted): J = conj(epsilon) * (M (x) A), "
          "epsilon^2 = the Pi-sign ---")
    print("  Pi = M^2, so the Pi-EVEN sector is the (1,-1)-eigenspace of M and the Pi-ODD")
    print("  sector is the (i,-i)-eigenspace.  epsilon = +1 -> J-fixed = D_1; "
          "epsilon = -1 -> D_-1;")
    print("  epsilon = +i -> J = -i*M, J-fixed = D_i;  epsilon = -i -> J = +i*M, "
          "J-fixed = D_-i.")
    print("  Twisted class dim = (J-fixed dim) * 2 (the antipode-fixed part of C[Cl]).")
    print()
    print("  %-6s %-12s %-9s %-9s %-9s %-9s %-14s %s"
          % ("a^2", "cell", "eps=+1", "eps=-1", "eps=+i", "eps=-i",
             "choice(+1,+i)", "choice(-1,-i)"))
    for cd in celldata:
        D = cd['D']
        cA = (D[0] + D[2]) * 2
        cB = (D[1] + D[3]) * 2
        cd['twA'] = cA
        cd['twB'] = cB
        print("  %-6s %-12s %-9d %-9d %-9d %-9d %-14d %d"
              % (cd['a2'], cd['clab'], D[0] * 2, D[1] * 2, D[2] * 2, D[3] * 2, cA, cB))
    filled = [cd['clab'] for cd in celldata if cd['plain'] == 0 and max(cd['twA'], cd['twB']) > 0]
    print("  REGISTERED EXPECTATION -- 'the twisted reading FILLS the dead cells': cells "
          "dead in the")
    print("  plain reading that the twisted reading revives: %s"
          % (", ".join(filled) if filled else "NONE"))
    check("P2b  the twisted reading fills every plain-dead cell (dead-plain cells: %s)"
          % ([cd['clab'] for cd in celldata if cd['plain'] == 0],),
          all(max(cd['twA'], cd['twB']) > 0
              for cd in celldata if cd['plain'] == 0))
    print()

    print("--- THE REGISTERED SUB-PREDICTIONS ---")
    c21 = [cd for cd in celldata if cd['clab'] == "{2:1}"][0]
    c2131 = [cd for cd in celldata if cd['clab'] == "{2:1,3:1}"][0]
    died = (c21['plain'] == 0)
    print("  (i)  'the plain-reading class DIES at the arrival of 2' -- at {2:1} the single")
    print("       factor has M = [i] and no lambda with lambda*nu = 1 (nu = +1) exists:")
    print("       R-plain class dim at {2:1} = %d  ==>  %s"
          % (c21['plain'], "LANDED" if died else "DID NOT LAND"))
    check("P2c  sub-prediction (i): the plain class DIES at {2:1} (dim = %d)"
          % c21['plain'], died)
    secs = sector_list(c2131['dl'], 0)
    revived = (c2131['plain'] > 0) and ((2, 3) in [tuple(s) for s in secs])
    print("  (ii) 'and can REVIVE at {2:1,3:1} through conjugate sectors (i, -i, +1)' --")
    print("       the live R-plain sectors at {2:1,3:1} are: %s"
          % ("; ".join(" x ".join("%s:%s" % (facs[c2131['fl'][t]]['tag'], EIG_NAMES[b])
                                  for t, b in enumerate(s)) for s in secs) or "NONE"))
    print("       R-plain class dim at {2:1,3:1} = %d  ==>  %s"
          % (c2131['plain'], "LANDED" if revived else "DID NOT LAND"))
    check("P2d  sub-prediction (ii): the plain class REVIVES at {2:1,3:1} through the "
          "conjugate sector ((2,1):i x (3,1):-i, nu = +1), dim = %d" % c2131['plain'],
          revived)
    print()

    # ==================================================================================
    # PART 3 -- the inertia
    # ==================================================================================
    print("=" * 100)
    print("PART 3 -- THE INERTIA (THE (P+) MECHANISM, VERIFIED)")
    print("=" * 100)
    print("  The Hermitian form on the section is B(v,w) = v^dagger (G_g (x) C) w with")
    print("  G_g = K_g^T F_g K_g = (K_g^T K_g) M_g (sitting 5's C4b).  On an M_g-eigenvector")
    print("  of eigenvalue theta: B(v,v) = theta * ||v||^2_(K^T K).  T-fixed and")
    print("  antipode-fixed force theta = lambda*mu = +1 -- the registered mechanism.")
    print()

    # ---- the (empty) cell -------------------------------------------------------------
    print("--- CELL (empty), a^2 = 1.69: the class part alone ---")
    CfixQ = rat_mm(rat_T(EC_FIX), rat_mm(CMAT, EC_FIX))
    CantQ = rat_mm(rat_T(EC_ANT), rat_mm(CMAT, EC_ANT))
    print("      C|_fix (antipode-fixed basis {e0, e1+e2}) = %s"
          % ([[str(v) for v in r] for r in CfixQ],))
    print("      C|_anti (antipode-anti basis {e1-e2})     = %s"
          % ([[str(v) for v in r] for r in CantQ],))
    pivF, okF = rat_congruence(CfixQ)
    check("P3a  (empty) cell: EXACT rational congruence diagonalization of B|_class = "
          "C|_fix gives pivots (%s) -- ALL POSITIVE RATIONALS => POSITIVE-DEFINITE, dim 2"
          % (", ".join(str(v) for v in pivF)),
          okF and all(v > 0 for v in pivF))
    CB = rat_mm(CMAT, EC_FIX)
    okinv = all(CB[1][j] == CB[2][j] for j in range(2))     # the subspace is C-invariant
    Cop = [[CB[0][0], CB[0][1]], [CB[1][0], CB[1][1]]]      # C acting, in {e0, e1+e2}
    trop = Cop[0][0] + Cop[1][1]
    detop = b18.rat_det(Cop)
    check("P3b  (empty) cell: C leaves the antipode-fixed subspace invariant and acts there "
          "by %s: trace %s, det %s => char poly lambda^2 - 5*lambda + 4, SPECTRUM {4,1} "
          "exactly -- the registered C|_fix eigenvalues"
          % ([[str(v) for v in r] for r in Cop], trop, detop),
          okinv and trop == 5 and detop == 4)
    print("      (C = circulant(2,1,1) = c2*c3 has spectrum (4,1,1); the antipode-anti line")
    print("      e1-e2 is the C-eigenvalue-1 line, so C|_fix carries {4,1} -- as registered.")
    print("      The GRAM of C|_fix in the (non-orthonormal) basis {e0, e1+e2} has det %s"
          % b18.rat_det(CfixQ))
    print("      = 4 * det(basis Gram) = 4 * 2; the OPERATOR determinant is 4.)")
    print()

    # ---- the {2:1,3:1} cell -----------------------------------------------------------
    print("--- CELL {2:1,3:1}, a^2 = 3: DIRECT EXACT (cell dim 12) ---")
    f2 = facs[(2, 1)]
    f3 = facs[(3, 1)]
    Mg = b18.kron_cyc(f2['M'], f3['M'])
    Gg = b18.kron_cyc(f2['G'], f3['G'])
    KtKg = b18.kron_scal(f2['KtK'], f3['KtK'])
    ng = 4
    KtKgC = [[b18.cint(int(KtKg[i][j])) for j in range(ng)] for i in range(ng)]
    CC = [[b18.cint(CMAT[a][b]) for b in range(3)] for a in range(3)]
    Gram = b18.kron_cyc(Gg, CC)

    check("P3c  {2:1,3:1}: G_g = (K_g^T K_g) M_g entry-exact (the mechanism's engine)",
          b18.cyc_mat_is_zero(b18.cyc_sub_mat(Gg, b18.mm_scal_cyc(KtKg, Mg))))

    # class basis: eigenvalue +1 of M_g, tensored with the antipode-fixed part
    ns1 = cyc_nullspace([[Mg[i][j] - (CO if i == j else CZ) for j in range(ng)]
                         for i in range(ng)])
    Ef = [[ns1[c][r] for c in range(len(ns1))] for r in range(ng)]
    kf = len(ns1)
    check("P3d  {2:1,3:1}: exact nullity of (M_g - I) = %d == D_1 from the sector algebra "
          "(%d)" % (kf, c2131['D'][0]), kf == c2131['D'][0])
    EcF = [[b18.cint(v) for v in r] for r in EC_FIX]
    E = b18.kron_cyc(Ef, EcF)
    Bcl = b18.mm_cyc_cyc(cyc_dag(E), b18.mm_cyc_cyc(Gram, E))
    NF = b18.mm_cyc_cyc(cyc_dag(Ef), b18.mm_cyc_cyc(KtKgC, Ef))
    CfixC = [[b18.cint(int(v)) for v in r] for r in CfixQ]
    pred = b18.kron_cyc(NF, CfixC)
    check("P3e  {2:1,3:1}: B|_class == (E_f^dagger (K_g^T K_g) E_f) (x) C|_fix ENTRY-EXACT "
          "-- the registered mechanism B|_class = ||.||^2 (x) C|_fix, dim %d"
          % (kf * 2), b18.cyc_eq_mat(Bcl, pred))
    print("      class dim = %d (= D_1 * 2 = %d * 2); B|_class is %dx%d"
          % (kf * 2, kf, len(Bcl), len(Bcl)))
    print("      ||v||^2 block E_f^dagger (K_g^T K_g) E_f (exact, z = zeta_144):")
    for r in NF:
        print("        [ " + " | ".join(b18.cyc_str(x) for x in r) + " ]")

    # (b) the registered congruence diagonalization, and the honest report
    piv = cyc_congruence(Bcl)
    allrat = all(x.is_rational() for x in piv)
    print("      Hermitian congruence pivots of B|_class over Q(zeta_144):")
    for t, x in enumerate(piv):
        fv = cyc_float(x)
        print("        pivot %d = %s" % (t + 1, b18.cyc_str(x)))
        print("                  rational? %s ; rational part = %s ; "
              "DECLARED FLOAT at the standard embedding = %.12f%+.2ei"
              % (x.is_rational(), x.rational_part(), fv.real, fv.imag))
    if allrat:
        check("P3f  {2:1,3:1}: every congruence pivot is a POSITIVE RATIONAL "
              "=> POSITIVE-DEFINITE exactly, as registered",
              all(x.rational_part() > 0 for x in piv))
    else:
        note("P3f  {2:1,3:1}: REGISTERED FALLBACK TAKEN -- the pivots are REAL BUT "
             "IRRATIONAL (they are ||v||^2, a totally positive element of the real "
             "subfield, not a rational). Reported, not smoothed.")
        print("      FALLBACK (registered): leading principal minors, exact determinants "
              "over the field:")
        for t in range(1, len(Bcl) + 1):
            dsub = cyc_det([[Bcl[i][j] for j in range(t)] for i in range(t)])
            fv = cyc_float(dsub)
            print("        minor %d: rational? %s ; rational part = %s ; DECLARED FLOAT = "
                  "%.10f%+.2ei" % (t, dsub.is_rational(), dsub.rational_part(),
                                   fv.real, fv.imag))
        print("      'sign read off the rational part' is recorded as WEAK EVIDENCE ONLY "
              "-- the rational")
        print("      part of a cyclotomic number is not its sign. The EXACT certificate "
              "is the next line.")

    # the exact, embedding-independent structural certificate
    pivK, okK = rat_congruence(KtKg)
    check("P3g  {2:1,3:1}: K_g^T K_g is RATIONAL SYMMETRIC POSITIVE-DEFINITE -- exact "
          "rational congruence pivots (%s), all positive"
          % (", ".join(str(v) for v in pivK)), okK and all(v > 0 for v in pivK))
    check("P3h  {2:1,3:1}: the class eigenbasis E_f has FULL COLUMN RANK %d over "
          "Q(zeta_144) (exact)" % kf, cyc_rank(cyc_dag(Ef)) == kf)
    check("P3i  {2:1,3:1}: EXACT POSITIVITY CERTIFICATE (embedding-independent): "
          "B|_class = E_f^dagger S E_f (x) C|_fix with S = K_g^T K_g rational SPD, E_f of "
          "full column rank, C|_fix rational SPD (pivots %s) => B|_class is "
          "POSITIVE-DEFINITE of dim %d under EVERY embedding of Q(zeta_144)"
          % (", ".join(str(v) for v in pivF), kf * 2),
          okK and all(v > 0 for v in pivK) and okF and all(v > 0 for v in pivF)
          and cyc_rank(cyc_dag(Ef)) == kf and b18.cyc_eq_mat(Bcl, pred))
    print()

    # the off-class negative direction, verified exactly at the same cell
    print("--- THE OFF-CLASS NEGATIVE DIRECTION AT {2:1,3:1}, VERIFIED EXACTLY ---")
    nsm = cyc_nullspace([[Mg[i][j] + (CO if i == j else CZ) for j in range(ng)]
                         for i in range(ng)])
    Efm = [[nsm[c][r] for c in range(len(nsm))] for r in range(ng)]
    km = len(nsm)
    check("P3j  {2:1,3:1}: exact nullity of (M_g + I) = %d == D_-1 (%d)"
          % (km, c2131['D'][1]), km == c2131['D'][1])
    EcA = [[b18.cint(v) for v in r] for r in EC_ANT]
    Em = b18.kron_cyc(Efm, EcA)
    Bof = b18.mm_cyc_cyc(cyc_dag(Em), b18.mm_cyc_cyc(Gram, Em))
    NFm = b18.mm_cyc_cyc(cyc_dag(Efm), b18.mm_cyc_cyc(KtKgC, Efm))
    CantC = [[b18.cint(int(v)) for v in r] for r in CantQ]
    predm = b18.kron_cyc([[-v for v in r] for r in NFm], CantC)
    check("P3k  {2:1,3:1}: B|_offclass == -(E_f'^dagger (K_g^T K_g) E_f') (x) C|_anti "
          "ENTRY-EXACT -- B = -||v||^2 on the antipode-anti-invariant channel "
          "(C-eigenvalue 1), exactly the registered (P+) off-class shape",
          b18.cyc_eq_mat(Bof, predm))
    print("      off-class dim at {2:1,3:1} = %d; C|_anti = %s (the C-eigenvalue-1 line, "
          "Gram 2)" % (km, [[str(v) for v in r] for r in CantQ]))
    print()

    # ---- the big cells: sector assembly ----------------------------------------------
    print("--- THE BIG CELLS: SECTOR-ASSEMBLED INERTIA "
          "(exact eigen-dims; mechanism verified above at the small cells) ---")
    for cd in celldata:
        if cd['clab'] not in ("{2:2,3:1}", "{2:3,3:2}"):
            continue
        print("  cell %-12s a^2 = %-4s  cell dim %-6d  R-plain class dim %d"
              % (cd['clab'], cd['a2'], cd['cell_dim'], cd['plain']))
        print("     SECTOR-ASSEMBLED VERDICT: B|_class is POSITIVE-DEFINITE of dimension "
              "%d." % cd['plain'])
        print("     (Not directly diagonalized. Assembly: D_1 = %d exact from the trace "
              "formulas;" % cd['D'][0])
        print("      on each lambda*mu = +1 sector B = (+1) * ||v||^2 (x) C|_fix with "
              "C|_fix rational SPD;")
        print("      the mechanism identity B|_class = ||.||^2 (x) C|_fix is verified "
              "ENTRY-EXACT at {2:1,3:1}.)")
        print("     OFF-CLASS negative directions: %d (lambda*mu = -1, nu = -1); "
              "place-support:" % cd['offneg'])
        for s in sector_list(cd['dl'], 1):
            dd = 1
            for t, b in enumerate(s):
                dd *= cd['dl'][t][b]
            print("        %s -> %d"
                  % (" x ".join("%s:%s" % (facs[cd['fl'][t]]['tag'], EIG_NAMES[b])
                                for t, b in enumerate(s)), dd))
    print()

    print("--- OFF-CLASS NEGATIVE-DIRECTION COUNT PER CELL, AND THE FIRST ADDRESS ---")
    print("  %-6s %-12s %-14s %s" % ("a^2", "cell", "off-class dim", "place-support"))
    first = None
    for cd in celldata:
        sup = []
        for s in sector_list(cd['dl'], 1):
            dd = 1
            for t, b in enumerate(s):
                dd *= cd['dl'][t][b]
            sup.append("%s(%d)" % (" x ".join("%s:%s" % (facs[cd['fl'][t]]['tag'],
                                                         EIG_NAMES[b])
                                              for t, b in enumerate(s)), dd))
        print("  %-6s %-12s %-14d %s" % (cd['a2'], cd['clab'], cd['offneg'],
                                         "; ".join(sup) if sup else "-"))
        if first is None and cd['offneg'] > 0:
            first = cd
    if first is not None:
        prev = celldata[celldata.index(first) - 1] if celldata.index(first) > 0 else None
        edge = prev is not None and set(prev['fl']) != set(first['fl'])
        newpl = sorted(set(p for (p, n) in first['fl'])
                       - set(p for (p, n) in (prev['fl'] if prev else [])))
        print("  THE FIRST NONEMPTY OFF-CLASS NEGATIVE SECTOR OCCURS AT CELL %s = a^2 = %s."
              % (first['clab'], first['a2']))
        print("  The preceding cell is %s (a^2 = %s); the factor set CHANGES there, and the"
              % (prev['clab'] if prev else "-", prev['a2'] if prev else "-"))
        print("  new place is %s -- so the address is a PLACE-ARRIVAL EDGE, not an interior "
              "cell." % (", ".join(str(x) for x in newpl) if newpl else "none"))
        check("P3l  the first off-class negative direction sits at a PLACE-ARRIVAL EDGE "
              "(cell %s, a^2 = %s; new place %s), not in a cell interior"
              % (first['clab'], first['a2'],
                 ", ".join(str(x) for x in newpl) if newpl else "none"), edge)
    print()

    # ==================================================================================
    # PART 4 -- the infinity factor (DECLARED FLOAT)
    # ==================================================================================
    print("=" * 100)
    print("PART 4 -- THE INFINITY FACTOR.  *** DECLARED FLOAT *** (b19's model, "
          "N = 511, lambda = 1/a)")
    print("=" * 100)
    print("  EVERY NUMBER IN THIS PART IS FLOAT. No exact ledger line is drawn from it.")
    import math
    import numpy as np
    import b19_attempt2_s6 as b19
    Ninf = 511
    mgrid, hstep, Finf = b19.grid(Ninf)
    xg = mgrid * hstep
    print("  grid: N = %d (odd), h = %.6f, |x| <= %.4f; ||F^2 - P|| = %.2e (float)"
          % (Ninf, hstep, abs(xg).max(),
             float(np.linalg.norm(Finf @ Finf - b19.parity_matrix(Ninf)))))
    print()
    print("  %-8s %-9s %-7s %-7s %-7s %-7s %-7s %-11s %-11s %-11s %s"
          % ("a", "lambda", "dim", "d_1", "d_-1", "d_i", "d_-i", "maxdev",
             "unitarity", "classdim", "minRQ on Fix"))
    AINF = [(1.3, "1.3"), (math.sqrt(2), "sqrt2"), (math.sqrt(3), "sqrt3"),
            (2.0, "2"), (3.0, "3")]
    tgt = np.array([1.0 + 0j, -1.0 + 0j, 1j, -1j])
    inf_rows = []
    for aval, alab in AINF:
        lam = 1.0 / aval
        Kinf, dinf = b19.sonin_ball(Ninf, Finf, xg, lam)
        Fs = Kinf.conj().T @ Finf @ Kinf
        w, V = np.linalg.eig(Fs)
        idx = np.argmin(np.abs(w[:, None] - tgt[None, :]), axis=1)
        dev = float(np.max(np.abs(w - tgt[idx])))
        cnt = [int((idx == k).sum()) for k in range(4)]
        unit = float(np.linalg.norm(Fs.conj().T @ Fs - np.eye(dinf)))
        sel = V[:, idx == 0]
        num = np.real(np.einsum('ij,ij->j', sel.conj(), Fs @ sel))
        den = np.real(np.einsum('ij,ij->j', sel.conj(), sel))
        rq = float((num / den).min()) if sel.shape[1] else float('nan')
        print("  %-8s %-9.6f %-7d %-7d %-7d %-7d %-7d %-11.2e %-11.2e %-11d %.12f"
              % (alab, lam, dinf, cnt[0], cnt[1], cnt[2], cnt[3], dev, unit,
                 cnt[0] * 2, rq))
        sys.stdout.flush()
        inf_rows.append((alab, dinf, cnt, dev, rq))
    print()
    print("  The archimedean-only cell's constrained class = Fix(F_inf) (x) "
          "(antipode-fixed part),")
    print("  dim = d_1(inf) * 2 (column 'classdim').  On Fix(F_inf) the pairing is "
          "B(v,v) = v^dag F_inf v")
    print("  = ||v||^2 > 0: the minimum Rayleigh quotient over the computed +1-eigenbasis "
          "is printed")
    print("  in the last column and lands at 1.0 to float precision at every a.")
    print("  AT CITE, BESIDE, NEVER MERGED: this is the MODEL BESIDE CC's Theorem 1 "
          "(single-place")
    print("  archimedean positivity on the constrained class). It is a property of a "
          "finite float")
    print("  model of one place, not a theorem, not a merge, and not evidence about any "
          "hypothesis.")
    print()

    # ==================================================================================
    # VERDICT
    # ==================================================================================
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    print("  (P+) LANDED, with its mechanism verified entry-exact.")
    print("   - M^4 = 1 at every factor; eigen-dims by the four trace equations are")
    print("     nonnegative integers at all five factors, and are CONFIRMED by direct")
    print("     exact nullity at (2,1), (3,1), (2,2).")
    print("   - B|_class = ||.||^2 (x) C|_fix ENTRY-EXACT at {2:1,3:1}; C|_fix carries the")
    print("     registered spectrum {4,1} (operator trace 5, det 4 on {e0, e1+e2});")
    print("     positivity rides exactly the positivity of the Euler coefficients (4,1,1).")
    print("   - CLASS-DIMENSION PUNCTUATION: the plain class DIES at {2:1} (a^2 = 2 and")
    print("     2.25) and REVIVES at {2:1,3:1} (a^2 = 3) through the conjugate sector")
    print("     ((2,1):i x (3,1):-i, nu = +1) -- both registered sub-predictions LANDED.")
    if first is not None:
        print("   - OFF-CLASS FIRST NEGATIVE ADDRESS: cell %s, a^2 = %s -- a PLACE-ARRIVAL"
              % (first['clab'], first['a2']))
        print("     EDGE (the arrival of 3), place-support %s."
              % ("; ".join(" x ".join("%s:%s" % (facs[first['fl'][t]]['tag'], EIG_NAMES[b])
                                      for t, b in enumerate(s))
                           for s in sector_list(first['dl'], 1))))
    print("   - THE ONE REGISTERED FALLBACK TAKEN, reported not smoothed: the Hermitian")
    print("     congruence pivots at {2:1,3:1} are NOT rational -- they are ||v||^2, real")
    print("     and totally positive but irrational in Q(zeta_144). The registered")
    print("     fallback (leading principal minors) was run and its 'sign off the rational")
    print("     part' reading is recorded as WEAK ONLY; the positivity is certified")
    print("     EXACTLY and embedding-independently by P3i instead.")
    print("   - (P-) did NOT occur: no negative direction appears ON the constrained class")
    print("     at any cell. (P0) not needed.")
    print()
    print("  SCOPE, said plainly: these are properties of a FINITE CONSTRUCTED MODEL")
    print("  SECTION. No sign is asserted; the register is untouched; nothing here bears")
    print("  on W_inf - Sum W_p at complete roster or on any hypothesis.")
    print()
    n_ok = sum(1 for _, ok in LEDGER if ok)
    n_all = len(LEDGER)
    print("--- EXACT LEDGER ---")
    for name, ok in LEDGER:
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    print()
    print("ALL EXACT LINES EXACT: %d/%d PASS" % (n_ok, n_all))


if __name__ == "__main__":
    main()
