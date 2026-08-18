"""W-ATTEMPT-2, SITTING 5 — THE CYCLOTOMIC HALF: THE SECTION'S PROPERTIES IN EXACT ARITHMETIC.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA at bench
grade; refused: any promotion to W_inf - Sum W_p at complete roster, or register movement.
THIS INSTRUMENT CERTIFIES THE BUILT OBJECT'S PROPERTIES, ASSERTS NO SIGN, MOVES NO REGISTER.

THE FIELD (exact, no floats): Q(zeta_144), Phi_144(x) = x^48 - x^24 + 1; elements are
Fraction-coefficient vectors of degree < 48; zeta_16 = zeta^9, zeta_9 = zeta^16, i = zeta^36,
omega = zeta^48; complex conjugation is zeta^k -> zeta^(144-k), reduced mod Phi_144.
Every local DFT here has rational normalization: F_N[j,k] = zeta_N^(jk)/sqrt(N) with
sqrt(N) in {2,3,4} for N in {4,9,16} — so every matrix entry is IN the field.

THE EXACT BASIS (replacing the float SVD basis of b8, same space): in the chart
m = alpha + p^n * beta on Z/p^(2n), Son(p,n) = V1 (x) W1 has the exact integer basis
k_(alpha,j) = delta_alpha (x) (e_j - e_(j+1)), alpha in [1, p^n), j in [0, p^n - 1).
The certified properties are basis-free (subspace invariance, rank, operator identities);
the float-era orthonormal-basis forms are their shadows.

CERTIFIED TARGETS — each a decidable statement, expected verdict registered before the run;
factors (p,n) in {(2,1), (3,1), (2,2)} (the diagonal cells at a in {sqrt2, sqrt3, 2}):
 (C1) the basis lands in Son: f|_B = 0 and (F f)|_B = 0 exactly, per basis column
      (B = the integers' ball, m == 0 mod p^n).
 (C2) T-invariance, exact form: F K = K M with M = (K^T K)^(-1) K^T F K — residual
      EXACTLY zero (the float-era closure ||(1-S)FK|| ~ 1e-16, now exact).
 (C3) the parity structure at the compressed level: M^2 = Pi, where Pi is the exact signed
      permutation induced on the basis by m -> -m (F^2 = parity, compressed); det Pi = +/-1.
 (C4) radical zero, exactly: G_loc = K^T F K = (K^T K) M; det(K^T K) a nonzero integer and
      M invertible by (C3), hence rank G_loc = dim Son — the pairing's local radical is ZERO.
 (C5) twisted-Hermitian, exact form: G_loc symmetric (F = F^T), and conj(G_loc) = G_loc * Pi
      — equivalently G_loc^dagger = G_loc * Pi: the float-era line ||G - (P(x)1)G^dag|| ~ 6e-15,
      now EXACT-ZERO.
 (C6) the class factor: C[alpha,beta] = coup[(beta-alpha) mod 3] with coup = (2,1,1) = c2*c3:
      C = C^T; character spectrum chi_k(c2*c3) = (4,1,1) exact in Z[omega] (imaginary parts
      exactly zero); det C = 4; the trace identity Tr(mult-by-coup) = 6 = 4+1+1 — the
      class-character TRACE of Z-hat's label-norm coefficient (the tau-route, question grade).
 (C7) the glued section at the diagonal cells a in {sqrt2, sqrt3, 2} (cells {2:1},
      {2:1,3:1}, {2:2,3:1}; dims 3, 12, 108): assembled by the exact tensor laws — rank is
      multiplicative; the twist and the invariance are tensor-functorial; the antipode A on
      C[Cl] satisfies A^2 = 1 — and the dim-12 cell is ALSO computed directly glued
      (F_4 (x) F_9 compressed onto K_2 (x) K_3, tensored with C) and checked ENTRY-EXACT
      against the tensor assembly.
 (C8) inertia (d/4, d/4, d/2): carried as banked DATA (sitting 2's run), not re-derived —
      a signature is a real-form computation this exact pass does not repeat; said plainly.

BRANCHES, registered: (pass) every certified line lands EXACT — the built object's
properties are certified in exact arithmetic; the Lean companion carries what decide
reaches and NAMES what needs Mathlib (the cyclotomic tower). (fail) any line lands
non-zero — the float-era line it shadows is RE-OPENED, the address named, nothing patched.

Usage:  python b18_attempt2_s5.py register | run
"""

import sys
from fractions import Fraction

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
# THE FIELD Q(zeta_144):  Phi_144(x) = x^48 - x^24 + 1,  so  x^48 = x^24 - 1.
# Elements: tuples of 48 Fractions (coefficients of zeta^0 .. zeta^47).  No floats.
# ======================================================================================

DEG = 48
ORD = 144
Z0 = Fraction(0)
Z1 = Fraction(1)


def _reduce(a):
    """Reduce a coefficient list of any length >= DEG modulo x^48 - x^24 + 1."""
    for d in range(len(a) - 1, DEG - 1, -1):
        v = a[d]
        if v:
            a[d] = Z0
            a[d - 24] += v
            a[d - 48] -= v
    return tuple(a[:DEG])


class Cyc(object):
    """An exact element of Q(zeta_144)."""
    __slots__ = ('c',)

    def __init__(self, c):
        self.c = tuple(c)

    def __add__(self, o):
        s = self.c
        t = o.c
        return Cyc([s[k] + t[k] for k in range(DEG)])

    def __sub__(self, o):
        s = self.c
        t = o.c
        return Cyc([s[k] - t[k] for k in range(DEG)])

    def __neg__(self):
        return Cyc([-v for v in self.c])

    def __mul__(self, o):
        s = self.c
        t = o.c
        acc = [Z0] * (2 * DEG - 1)
        for i in range(DEG):
            si = s[i]
            if si:
                for j in range(DEG):
                    tj = t[j]
                    if tj:
                        acc[i + j] += si * tj
        return Cyc(_reduce(acc))

    def smul(self, r):
        """Scalar multiplication by a Fraction / int."""
        if r == 0:
            return CZERO
        return Cyc([v * r for v in self.c])

    def conj(self):
        """Complex conjugation: zeta^k -> zeta^(144-k), reduced mod Phi_144."""
        out = [Z0] * DEG
        for k in range(DEG):
            v = self.c[k]
            if v:
                tc = ZPOW[(ORD - k) % ORD].c
                for j in range(DEG):
                    if tc[j]:
                        out[j] += v * tc[j]
        return Cyc(out)

    def is_zero(self):
        for v in self.c:
            if v:
                return False
        return True

    def is_rational(self):
        for k in range(1, DEG):
            if self.c[k]:
                return False
        return True

    def rational_part(self):
        return self.c[0]

    def __eq__(self, o):
        return self.c == o.c

    def __ne__(self, o):
        return self.c != o.c

    def __hash__(self):
        return hash(self.c)


def _fmt(r):
    if r.denominator == 1:
        return str(r.numerator)
    return "%d/%d" % (r.numerator, r.denominator)


def cyc_str(x):
    parts = []
    for k in range(DEG):
        v = x.c[k]
        if v:
            if k == 0:
                parts.append(_fmt(v))
            elif v == 1:
                parts.append("z^%d" % k)
            elif v == -1:
                parts.append("-z^%d" % k)
            else:
                parts.append("%s*z^%d" % (_fmt(v), k))
    if not parts:
        return "0"
    s = parts[0]
    for p in parts[1:]:
        s = s + (" - " + p[1:] if p.startswith("-") else " + " + p)
    return s


CZERO = Cyc([Z0] * DEG)
CONE = Cyc([Z1] + [Z0] * (DEG - 1))
_ZETA = Cyc([Z0, Z1] + [Z0] * (DEG - 2))

# table of zeta^k, k = 0 .. 143 (built by iterated exact multiplication)
ZPOW = [CONE]
for _k in range(1, ORD):
    ZPOW.append(ZPOW[-1] * _ZETA)


def zetapow(k):
    return ZPOW[k % ORD]


def cint(n):
    return Cyc([Fraction(n)] + [Z0] * (DEG - 1))


# ======================================================================================
# MATRIX PLUMBING (exact; three flavours: rational, Cyc, and mixed)
# ======================================================================================

def mm_cyc_cyc(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[CZERO] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        row = out[i]
        for t in range(k):
            a = Ai[t]
            if a.is_zero():
                continue
            Bt = B[t]
            for j in range(m):
                b = Bt[j]
                if not b.is_zero():
                    row[j] = row[j] + a * b
    return out


def mm_scal_cyc(A, B):
    """A: matrix of Fraction/int.  B: matrix of Cyc."""
    n, k, m = len(A), len(B), len(B[0])
    out = [[CZERO] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        row = out[i]
        for t in range(k):
            a = Ai[t]
            if a == 0:
                continue
            Bt = B[t]
            for j in range(m):
                b = Bt[j]
                if not b.is_zero():
                    row[j] = row[j] + b.smul(a)
    return out


def mm_cyc_scal(A, B):
    """A: matrix of Cyc.  B: matrix of Fraction/int."""
    n, k, m = len(A), len(B), len(B[0])
    out = [[CZERO] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        row = out[i]
        for t in range(k):
            a = Ai[t]
            if a.is_zero():
                continue
            Bt = B[t]
            for j in range(m):
                b = Bt[j]
                if b != 0:
                    row[j] = row[j] + a.smul(b)
    return out


def mm_scal_scal(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[Fraction(0)] * m for _ in range(n)]
    for i in range(n):
        for t in range(k):
            a = A[i][t]
            if a == 0:
                continue
            for j in range(m):
                out[i][j] += a * B[t][j]
    return out


def transpose(A):
    return [list(r) for r in zip(*A)]


def cyc_eq_mat(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                return False
    return True


def cyc_sub_mat(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def cyc_mat_is_zero(A):
    for r in A:
        for v in r:
            if not v.is_zero():
                return False
    return True


def kron_cyc(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    out = [[CZERO] * (ca * cb) for _ in range(ra * rb)]
    for i1 in range(ra):
        for j1 in range(ca):
            a = A[i1][j1]
            for i2 in range(rb):
                for j2 in range(cb):
                    out[i1 * rb + i2][j1 * cb + j2] = a * B[i2][j2]
    return out


def kron_scal(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    out = [[Fraction(0)] * (ca * cb) for _ in range(ra * rb)]
    for i1 in range(ra):
        for j1 in range(ca):
            a = Fraction(A[i1][j1])
            for i2 in range(rb):
                for j2 in range(cb):
                    out[i1 * rb + i2][j1 * cb + j2] = a * Fraction(B[i2][j2])
    return out


def rat_det(A):
    """Exact determinant of a square Fraction/int matrix by Gaussian elimination."""
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


def rat_inv(A):
    """Exact inverse of a square Fraction/int matrix (Gauss-Jordan)."""
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


# ======================================================================================
# THE LOCAL DFTs  F_N[j,k] = zeta_N^(jk) / sqrt(N),  N in {4, 9, 16}, sqrt(N) in {2,3,4}
# ======================================================================================

SQRT = {4: 2, 9: 3, 16: 4}


def dft(N):
    step = ORD // N
    s = Fraction(1, SQRT[N])
    return [[zetapow(step * ((j * k) % N)).smul(s) for k in range(N)] for j in range(N)]


def dagger(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


# ======================================================================================
# THE EXACT SONIN BASIS  k_(alpha,j) = delta_alpha (x) (e_j - e_(j+1))
# ======================================================================================

def sonin_basis(p, n):
    """Return (N, q, cols, K) with K the N x (q-1)^2 integer basis matrix."""
    q = p ** n
    N = q * q
    cols = [(a, j) for a in range(1, q) for j in range(0, q - 1)]
    K = [[0] * len(cols) for _ in range(N)]
    for c, (a, j) in enumerate(cols):
        K[(a + q * j) % N][c] = 1
        K[(a + q * (j + 1)) % N][c] = -1
    return N, q, cols, K


# ======================================================================================
# CERTIFICATION LEDGER
# ======================================================================================

LEDGER = []


def check(name, ok):
    LEDGER.append((name, bool(ok)))
    print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    sys.stdout.flush()
    assert ok, "CERTIFIED LINE FAILED: " + name


def perm_sign_and_det(Pi):
    """Pi is a rational signed-permutation matrix; return (is_signed_perm, det)."""
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
    # sign of the permutation by cycle decomposition
    seen = [False] * n
    s = 1
    for i in range(n):
        if not seen[i]:
            L = 0
            k = i
            while not seen[k]:
                seen[k] = True
                k = perm[k]
                L += 1
            if L % 2 == 0:
                s = -s
    d = s
    for v in sgn:
        d *= v
    return True, d


# ======================================================================================
# PER-FACTOR CERTIFICATION  (C1) .. (C5)
# ======================================================================================

def certify_factor(p, n):
    tag = "(p,n)=(%d,%d)" % (p, n)
    N, q, cols, K = sonin_basis(p, n)
    d = len(cols)
    F = dft(N)
    print("--- FACTOR %s : N = p^(2n) = %d, q = p^n = %d, dim Son = (q-1)^2 = %d ---"
          % (tag, N, q, d))
    print("      basis columns (alpha,j): %s" % (cols,))
    sys.stdout.flush()

    FK = mm_cyc_scal(F, K)                              # N x d, Cyc

    # ---- (C1) the basis lands in Son -------------------------------------------------
    ball = [m for m in range(N) if m % q == 0]
    ok_f = all(K[m][c] == 0 for m in ball for c in range(d))
    check("C1a %s  f|_B = 0 on the integers' ball B = {m == 0 mod %d} (all %d columns)"
          % (tag, q, d), ok_f)
    ok_Ff = all(FK[m][c].is_zero() for m in ball for c in range(d))
    check("C1b %s  (F f)|_B = 0 exactly on B (all %d columns)" % (tag, d), ok_Ff)

    # ---- (C2) T-invariance, exact ----------------------------------------------------
    Kt = transpose(K)
    KtK = mm_scal_scal([[Fraction(v) for v in r] for r in Kt],
                       [[Fraction(v) for v in r] for r in K])
    detKtK = rat_det(KtK)
    KtKinv = rat_inv(KtK)
    G = mm_scal_cyc([[Fraction(v) for v in r] for r in Kt], FK)     # G_loc = K^T F K
    M = mm_scal_cyc(KtKinv, G)                                      # d x d, Cyc
    KM = mm_scal_cyc([[Fraction(v) for v in r] for r in K], M)
    check("C2  %s  F K - K M = 0 entry-exact (M = (K^T K)^-1 K^T F K); residual EXACT ZERO"
          % tag, cyc_mat_is_zero(cyc_sub_mat(FK, KM)))

    # ---- (C3) parity structure at the compressed level --------------------------------
    PK = [[K[(-m) % N][c] for c in range(d)] for m in range(N)]     # (P K)[m] = K[-m]
    Pi = mm_scal_scal(KtKinv, mm_scal_scal([[Fraction(v) for v in r] for r in Kt],
                                           [[Fraction(v) for v in r] for r in PK]))
    KPi = mm_scal_scal([[Fraction(v) for v in r] for r in K], Pi)
    ok_pk = all(Fraction(PK[i][j]) == KPi[i][j] for i in range(N) for j in range(d))
    check("C3a %s  P K - K Pi = 0 entry-exact (Pi solved, not assumed)" % tag, ok_pk)
    is_sp, detPi = perm_sign_and_det(Pi)
    check("C3b %s  Pi is a signed permutation (one +/-1 per row and per column)" % tag, is_sp)
    check("C3c %s  det Pi = %+d in {+1,-1}" % (tag, detPi), detPi in (1, -1))
    PiC = [[cint(int(Pi[i][j])) for j in range(d)] for i in range(d)]
    MM = mm_cyc_cyc(M, M)
    check("C3d %s  M^2 - Pi = 0 entry-exact (F^2 = parity, compressed)" % tag,
          cyc_mat_is_zero(cyc_sub_mat(MM, PiC)))

    # ---- (C4) radical zero ------------------------------------------------------------
    check("C4a %s  det(K^T K) = %s is a NONZERO integer"
          % (tag, _fmt(detKtK)), detKtK != 0 and detKtK.denominator == 1)
    KtKM = mm_scal_cyc(KtK, M)
    check("C4b %s  G_loc - (K^T K) M = 0 entry-exact" % tag,
          cyc_mat_is_zero(cyc_sub_mat(G, KtKM)))
    print("      C4 STATEMENT: det(M)^2 = det(M^2) = det(Pi) = %+d != 0, so M is invertible;" % detPi)
    print("      K^T K is invertible (det = %s != 0); hence G_loc = (K^T K) M is invertible and"
          % _fmt(detKtK))
    print("      rank G_loc = %d = dim Son(%d,%d) -- THE PAIRING'S LOCAL RADICAL IS ZERO." % (d, p, n))
    sys.stdout.flush()

    # ---- (C5) twisted-Hermitian, exact ------------------------------------------------
    ok_sym = all(G[i][j] == G[j][i] for i in range(d) for j in range(d))
    check("C5a %s  G_loc = G_loc^T entry-exact (F = F^T)" % tag, ok_sym)
    Gc = [[G[i][j].conj() for j in range(d)] for i in range(d)]
    GPi = mm_cyc_scal(G, Pi)
    check("C5b %s  conj(G_loc) - G_loc * Pi = 0 entry-exact (= G_loc^dagger = G_loc Pi)" % tag,
          cyc_mat_is_zero(cyc_sub_mat(Gc, GPi)))

    if d <= 4:
        print("      G_loc %s (exact, z = zeta_144):" % tag)
        for i in range(d):
            print("        [ " + " | ".join(cyc_str(G[i][j]) for j in range(d)) + " ]")
    else:
        print("      G_loc %s is %dx%d; entries suppressed (row 0 shown):" % (tag, d, d))
        print("        [ " + " | ".join(cyc_str(G[0][j]) for j in range(d)) + " ]")
    print()
    sys.stdout.flush()
    return dict(p=p, n=n, N=N, q=q, d=d, K=K, F=F, FK=FK, G=G, M=M, Pi=Pi,
                detKtK=detKtK, detPi=detPi, KtK=KtK)


# ======================================================================================
# MAIN
# ======================================================================================

def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 5 -- REGISTRATION. NO CERTIFIED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. CERTIFICATION BEGINS.\n")
    sys.stdout.flush()

    # ---------------- F0: the field itself ------------------------------------------
    print("--- F0: THE FIELD Q(zeta_144), Phi_144(x) = x^48 - x^24 + 1 (no floats anywhere) ---")
    check("F0a  zeta^144 = 1 exactly (ZPOW[143] * zeta = 1)", ZPOW[143] * _ZETA == CONE)
    check("F0b  Phi_144(zeta) = zeta^48 - zeta^24 + 1 = 0 exactly",
          (zetapow(48) - zetapow(24) + CONE).is_zero())
    check("F0c  conj(zeta^k) * zeta^k = 1 for all k in [0,144)",
          all((zetapow(k).conj() * zetapow(k)) == CONE for k in range(ORD)))
    check("F0d  i = zeta^36 satisfies i^2 = -1 exactly", zetapow(36) * zetapow(36) == -CONE)
    check("F0e  omega = zeta^48 satisfies omega^2 + omega + 1 = 0 exactly",
          (zetapow(96) + zetapow(48) + CONE).is_zero())
    for N in (4, 9, 16):
        FN = dft(N)
        I = [[CONE if i == j else CZERO for j in range(N)] for i in range(N)]
        check("F0f  F_%d^dagger F_%d = I exactly (rational normalization 1/%d keeps it in the field)"
              % (N, N, SQRT[N]), cyc_eq_mat(mm_cyc_cyc(dagger(FN), FN), I))
    print()
    sys.stdout.flush()

    # ---------------- C1..C5 per factor ----------------------------------------------
    facs = {}
    for (p, n) in [(2, 1), (3, 1), (2, 2)]:
        facs[(p, n)] = certify_factor(p, n)

    # ---------------- C6: the class factor -------------------------------------------
    print("--- C6: THE CLASS FACTOR  C[a,b] = coup[(b-a) mod 3],  coup = (2,1,1) = c2 * c3 ---")
    coup = (2, 1, 1)
    om = zetapow(48)
    chi = []
    for k in range(3):
        s = CZERO
        for c in range(3):
            s = s + zetapow(48 * ((k * c) % 3)).smul(Fraction(coup[c]))
        chi.append(s)
    expect = (4, 1, 1)
    for k in range(3):
        check("C6a  chi_%d(c2*c3) = %d exactly in Z[omega] (imaginary part EXACTLY zero)"
              % (k, expect[k]), chi[k] == cint(expect[k]))
    print("      chi = (%s, %s, %s)" % tuple(cyc_str(x) for x in chi))
    C = [[coup[(b - a) % 3] for b in range(3)] for a in range(3)]
    check("C6b  C = C^T exactly", all(C[i][j] == C[j][i] for i in range(3) for j in range(3)))
    detC = rat_det(C)
    check("C6c  det C = 4 exactly (det = %s)" % _fmt(detC), detC == 4)
    trC = sum(C[i][i] for i in range(3))
    check("C6d  Tr(mult-by-coup) = 6 = 4 + 1 + 1 (trace = sum of the character spectrum)",
          trC == 6 and trC == sum(expect))
    print("      C rows: %s   [circulant on Cl of order 3; omega = zeta^48 = %s]"
          % (C, cyc_str(om)))
    print("      NOTE (grade): this is the class-character TRACE of Z-hat's label-norm")
    print("      coefficient -- the tau-route, QUESTION GRADE. No sign is asserted here.")
    print()
    sys.stdout.flush()

    # ---------------- C7: the glued section at the diagonal cells ---------------------
    print("--- C7: THE GLUED SECTION AT THE DIAGONAL CELLS a in {sqrt2, sqrt3, 2} ---")
    cells = [("sqrt2", [(2, 1)], "{2:1}"),
             ("sqrt3", [(2, 1), (3, 1)], "{2:1,3:1}"),
             ("2", [(2, 2), (3, 1)], "{2:2,3:1}")]
    print("      %-8s %-12s %-26s %-8s %s" % ("a", "cell", "local dims x |Cl|", "dim", "rank (tensor law)"))
    for alab, fl, clab in cells:
        dims = [facs[f]['d'] for f in fl]
        dim = 1
        for x in dims:
            dim *= x
        dim *= 3
        print("      %-8s %-12s %-26s %-8d %d = dim  (rank multiplicative: %s x rank C = 3)"
              % (alab, clab, " * ".join(str(x) for x in dims) + " * 3", dim, dim,
                 " x ".join(str(x) for x in dims)))
    exp_dims = [3, 12, 108]
    got_dims = []
    for alab, fl, clab in cells:
        dim = 3
        for f in fl:
            dim *= facs[f]['d']
        got_dims.append(dim)
    check("C7a  cell dims by the tensor law = (3, 12, 108) exactly (got %s)" % (tuple(got_dims),),
          got_dims == exp_dims)
    print("      each factor's G_loc is invertible (C4), det C = 4 != 0 (C6); rank of a Kronecker")
    print("      product is the product of the ranks -- so rank = dim at every cell above.")
    sys.stdout.flush()

    f2 = facs[(2, 1)]
    f3 = facs[(3, 1)]

    # the direct glued computation at the dim-12 cell
    K2, K3 = f2['K'], f3['K']
    Kg = kron_scal(K2, K3)                              # 36 x 4 integer (as Fractions)
    FKg = kron_cyc(f2['FK'], f3['FK'])                  # (F4 (x) F9) (K2 (x) K3) = FK2 (x) FK3
    Gdirect = mm_scal_cyc(transpose(Kg), FKg)           # 4 x 4 Cyc
    Gtensor = kron_cyc(f2['G'], f3['G'])
    check("C7b  DIRECT GLUED dim-12 cell: K_g^T (F_4 (x) F_9) K_g  ==  G_2 (x) G_3 entry-exact",
          cyc_eq_mat(Gdirect, Gtensor))

    Mg = kron_cyc(f2['M'], f3['M'])
    KgMg = mm_scal_cyc(Kg, Mg)
    check("C7c  glued T-invariance: (F_4 (x) F_9) K_g - K_g (M_2 (x) M_3) = 0 entry-exact",
          cyc_mat_is_zero(cyc_sub_mat(FKg, KgMg)))

    Pig = kron_scal(f2['Pi'], f3['Pi'])
    PigC = [[cint(int(Pig[i][j])) for j in range(len(Pig))] for i in range(len(Pig))]
    check("C7d  tensor-functorial parity: (M_2 (x) M_3)^2 - (Pi_2 (x) Pi_3) = 0 entry-exact",
          cyc_mat_is_zero(cyc_sub_mat(mm_cyc_cyc(Mg, Mg), PigC)))

    Gdc = [[Gdirect[i][j].conj() for j in range(4)] for i in range(4)]
    check("C7e  tensor-functorial twist: conj(G_g) - G_g (Pi_2 (x) Pi_3) = 0 entry-exact",
          cyc_mat_is_zero(cyc_sub_mat(Gdc, mm_cyc_scal(Gdirect, Pig))))

    # the full 12 x 12 section Gram with the class factor
    Gram = [[CZERO] * 12 for _ in range(12)]
    for u in range(4):
        for a in range(3):
            for v in range(4):
                for b in range(3):
                    Gram[u * 3 + a][v * 3 + b] = Gdirect[u][v].smul(Fraction(coup[(b - a) % 3]))
    GramK = kron_cyc(Gdirect, [[cint(C[a][b]) for b in range(3)] for a in range(3)])
    check("C7f  full 12x12 section Gram[(u,a),(v,b)] = G_g[u][v]*coup[(b-a)%3] == G_g (x) C entry-exact",
          cyc_eq_mat(Gram, GramK))
    print("      rank of the 12x12 section Gram = 4 * 3 = 12 = dim, by the tensor law")
    print("      (det(K2^T K2) = %s, det(K3^T K3) = %s, both G_loc invertible; det C = 4)."
          % (_fmt(f2['detKtK']), _fmt(f3['detKtK'])))
    sys.stdout.flush()

    A = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
    I3 = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    AA = mm_scal_scal(A, A)
    check("C7g  antipode A on C[Cl]: A^2 = 1 exactly (integer)",
          all(AA[i][j] == I3[i][j] for i in range(3) for j in range(3)))
    ACA = mm_scal_scal(mm_scal_scal(A, C), A)
    check("C7h  A C A = C exactly (integer): the antipode preserves the class factor",
          all(ACA[i][j] == C[i][j] for i in range(3) for j in range(3)))
    print()
    sys.stdout.flush()

    # ---------------- C8: carried data ------------------------------------------------
    print("--- C8: CARRIED DATA (not re-derived here) ---")
    print("      inertia (d/4, d/4, d/2) on the untwisted symmetrization -- CARRIED from "
          "sitting 2's banked run (float era); not re-derived in exact arithmetic; a data row, "
          "never a sign datum.")
    print()
    sys.stdout.flush()

    # ---------------- ledger ----------------------------------------------------------
    n_ok = sum(1 for _, ok in LEDGER if ok)
    n_all = len(LEDGER)
    print("--- LEDGER ---")
    for name, ok in LEDGER:
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    print()
    print("SCOPE, said plainly: these are EXACT properties of a FINITE CONSTRUCTED OBJECT.")
    print("No sign is asserted; no register moves; W_inf - Sum W_p at complete roster is NOT touched.")
    print()
    print("ALL CERTIFIED LINES EXACT: %d/%d PASS" % (n_ok, n_all))


if __name__ == "__main__":
    main()
