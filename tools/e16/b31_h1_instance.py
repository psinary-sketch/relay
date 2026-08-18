"""W-ATTEMPT-2 ADJACENT — THE h = 1 INSTANCE: THE SAME CONSTRUCTION OVER Q ITSELF.

RELAY-ONLY. THE CORRECTED STOP IN FORCE: measured properties of constructed objects are
DATA at bench grade; refused: any promotion to W_inf - Sum W_p at complete roster, or
register movement. THIS IS THE INSTANCE NEAREST RH PROPER AND THE SCOPE GUARD RIDES
EVERY LINE: finite place sets, finite cutoffs, a model — nothing about the Hypothesis.

THE INSTANCE, REGISTERED: over Q (h = 1, Cl trivial, C[Cl] = C, tau = epsilon — the two
scalarizations coincide), the class-resolved diagonal section DEGENERATES to the plain
tensor of local Sonin squares: places {inf, 2, 3}, cutoffs to n = 2 (factors (2,1),
(2,2), (3,1), (3,2); cells {2:1}, {2:1,3:1}, {2:2,3:1}, {2:2,3:2} — the last
cutoff-capped, declared). Every prime of Q is principal: each label is [0] = 1, the
coupling is the SCALAR 1, and the norm-N coefficient of zeta is a_N = 1 (the count of
norm-N ideals of Q — exactly one, (N)). The antipode is TRIVIAL.

REGISTERED LONGHAND, before any number:
 (i)   the per-factor certificates (F K = K M, M^2 = Pi, radical zero, twist
       G-dagger = G Pi) are UNCHANGED — they never involved the class layer;
 (ii)  H^2 = C, dim 1, antipode-invariant dim 1 (was dim 3 / invariant 2 at h = 3);
 (iii) the constrained class at h = 1: antipode-fixed is EVERYTHING, so the class =
       T-fixed = the lam-product = +1 sectors — THE SAME SECTOR SET as h = 3's class —
       and B|_class = ||v||^2 * (scalar 1): POSITIVE, by the same sector-forcing, with
       C|_fix replaced by the positive scalar a_N = 1;
 (iv)  THE FLIP CHANNEL HAS NO HOME AT h = 1: the T-fixed negatives of h = 3 lived in
       the antipode-ANTI-invariant channel (lam-product = -1, nu = -1); with the
       antipode trivial that channel is EMPTY — at h = 1 there are NO T-fixed negative
       directions at all (the full pairing's lam-product = -1 negatives remain, off the
       fixed space). REGISTERED READING: the arrival-edge negativity-in-the-flipped-
       channel is a CLASS-RESOLUTION phenomenon; what the resolution supplied is the
       CHANNEL (the home of T-fixed negativity) and the tau/epsilon LEDGER SEPARATION
       (B5's selection principle: tau class-separating — vacuous at h = 1), NOT the
       positivity, which rides the same sector-forcing at both h.

BRANCHES, as ferried:
 (H1-same)     positivity holds by the same mechanism with C|_fix a positive scalar —
               the class resolution was STRUCTURE, not the source of the sign; the
               scalar is the norm-N coefficient count (= 1), positive by construction.
 (H1-collapse) something the resolution supplied is LOST — named exactly (the B5
               selection principle's content at h = 1).
 (H1-third)    filed openly.
LONGHAND EXPECTATION: (H1-same) for the sign, WITH the two named losses of (iv) recorded
as what the resolution actually supplied (channel + ledger separation) — i.e. the honest
verdict is expected to be (H1-same)-for-positivity AND the (iv) reading banked beside it.

MEASURED (exact where the cell allows, per the b18/b20 machinery): per factor — the four
certificates re-asserted; per cell — dim; H^2 = C data line; the T-fixed (= class) dims
by sector arithmetic (expected: {2:1}: 0 — the death survives h = 1, it was never a
class phenomenon; {2:1,3:1}: 1 via (i,-i); {2:2,3:1}: 9; {2:2,3:2}: 208 = sum over
lam-product = +1 of d*d for (2,2)x(3,2)); T-fixed negative count (expected 0 at every
cell — assert); full-pairing negative dims (lam-product = -1 sectors, scalar class);
DIRECT EXACT positivity of B|_class at {2:1,3:1} (dim 1) and {2:2,3:1} (dim 9): build
the exact eigenbases, restrict the Gram (NO class tensor now), certify positive-definite
by the rational-SPD factorization route (b20's precedent); the coupling scalar verified:
the number of ideals of Q of norm 6 (and of norm 36) enumerated = 1 = the coupling.

RECORDED PLAINLY AS DATA. The register is untouched; nothing circulates.
Usage:  python b31_h1_instance.py register | run
"""

import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import b18_attempt2_s5 as b18            # noqa: E402  (sitting 5's certified machinery)
import b20_attempt2_s7 as b20            # noqa: E402  (sitting 7's sector/eigen machinery)

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
# EXACT LEDGER.  Every entry is an EXACT arithmetic statement; no float ever enters.
# ======================================================================================

LEDGER = []
NOTES = []


def check(name, ok):
    LEDGER.append((name, bool(ok)))
    print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    sys.stdout.flush()
    assert ok, "EXACT LINE FAILED: " + name


def note(name):
    """A recorded exact observation that is NOT asserted (a registered fallback branch)."""
    NOTES.append(name)
    print("  NOTE  %s" % name)
    sys.stdout.flush()


CZ = b18.CZERO
CO = b18.CONE
I144 = b18.zetapow(36)
FLD = b20.FLD81

# The banked eigen-dims, cited at the head and RE-DERIVED in-run (never trusted).
BANKED_DIMS = {(2, 1): [0, 0, 1, 0],
               (2, 2): [2, 2, 3, 2],
               (3, 1): [1, 1, 1, 1],
               (3, 2): [16, 16, 16, 16]}

# The registration's own class-dim arithmetic, per cell -- FLAGGED CHECKABLE.
REGISTERED_CLASS_DIMS = {"{2:1}": 0, "{2:1,3:1}": 1, "{2:2,3:1}": 9, "{2:2,3:2}": 208}

# The h = 1 cells (cutoffs capped at n = 2; the last cell is cutoff-capped, declared).
H1_CELLS = [("{2:1}", [(2, 1)], 2),
            ("{2:1,3:1}", [(2, 1), (3, 1)], 6),
            ("{2:2,3:1}", [(2, 2), (3, 1)], 12),
            ("{2:2,3:2}", [(2, 2), (3, 2)], 36)]


# ======================================================================================
# Q(zeta_81) HELPERS.  b20's Fld carries +, -, rational scaling only (the sparsity rule
# forbids a dense F at the large factor); conjugation and a SPARSE product are added
# HERE (b20 is not modified) -- both used only where the cell allows.
# ======================================================================================

def f81_conj(a):
    """Complex conjugation in Q(zeta_81): zeta^k -> zeta^(81-k), reduced mod Phi_81."""
    out = [Fraction(0)] * FLD.deg
    for k in range(FLD.deg):
        v = a[k]
        if v:
            m = FLD.mono((-k) % FLD.N)
            for j in range(FLD.deg):
                if m[j]:
                    out[j] += v * m[j]
    return tuple(out)


def f81_mul(a, b):
    """Sparse exact product in Q(zeta_81) (zeros skipped; no dense operator is formed)."""
    acc = [Fraction(0)] * (2 * FLD.deg - 1)
    for i in range(FLD.deg):
        ai = a[i]
        if ai:
            for j in range(FLD.deg):
                bj = b[j]
                if bj:
                    acc[i + j] += ai * bj
    return tuple(FLD.red(acc))


def f81_geometric_sums_ok():
    """sum_(r=0..80) zeta_81^(r t) = 81 * delta(t == 0), exactly, for every t in [0,81)."""
    N = FLD.N
    for t in range(N):
        e = [0] * N
        for r in range(N):
            e[(r * t) % N] += 1
        red = list(FLD.red(e))
        tgt = [0] * FLD.deg
        tgt[0] = N if t == 0 else 0
        if red != tgt:
            return False
    return True


def pi_column_action(G, Pi, smul):
    """(G Pi)[:, cp] for Pi an exact signed permutation -- a signed column permutation."""
    d = len(Pi)
    out = [[None] * d for _ in range(d)]
    for cp in range(d):
        nz = [(r, Pi[r][cp]) for r in range(d) if Pi[r][cp] != 0]
        if len(nz) != 1:
            return None
        r, s = nz[0]
        for i in range(d):
            out[i][cp] = smul(G[i][r], s)
    return out


# ======================================================================================
# PER-FACTOR CERTIFICATION -- THE FOUR CERTIFICATES, RE-ASSERTED (registration item (i))
# ======================================================================================

def certify_small(p, n):
    """(2,1), (3,1), (2,2) in Q(zeta_144): all four certificates FULL and entry-exact."""
    f = b20.small_factor(p, n)
    tag = f['tag']
    d = f['d']
    check("A1 %s  F K = K M entry-exact, FULL (b18 C2 / b20 P1a re-asserted at h = 1)"
          % tag, f['ok_fk'])
    check("A2 %s  P K = K Pi entry-exact, FULL; Pi the signed permutation "
          "(a,j) -> -(q-a, q-2-j) (b18 C3a re-asserted)" % tag, f['ok_pk'])
    is_sp, detPi = b18.perm_sign_and_det(f['Pi'])
    check("A3 %s  Pi is a signed permutation, det Pi = %+d in {+1,-1}" % (tag, detPi),
          is_sp and detPi in (1, -1))
    PiC = [[b18.cint(int(f['Pi'][i][j])) for j in range(d)] for i in range(d)]
    MM = b18.mm_cyc_cyc(f['M'], f['M'])
    check("A4 %s  M^2 - Pi = 0 entry-exact, FULL (F^2 = parity, compressed; b18 C3d)"
          % tag, b18.cyc_mat_is_zero(b18.cyc_sub_mat(MM, PiC)))
    detKtK = b18.rat_det(f['KtK'])
    check("A5 %s  det(K^T K) = %s is a NONZERO integer => K injective, radical ZERO "
          "(G_loc = (K^T K) M with M invertible by A4)" % (tag, b18._fmt(detKtK)),
          detKtK != 0 and detKtK.denominator == 1)
    G = f['G']
    KtKM = b18.mm_scal_cyc(f['KtK'], f['M'])
    check("A6 %s  G_loc - (K^T K) M = 0 entry-exact (b18 C4b)" % tag,
          b18.cyc_mat_is_zero(b18.cyc_sub_mat(G, KtKM)))
    Gc = [[G[i][j].conj() for j in range(d)] for i in range(d)]
    GPi = b18.mm_cyc_scal(G, f['Pi'])
    check("A7 %s  conj(G_loc) - G_loc * Pi = 0 entry-exact, FULL "
          "(G_loc^dagger = G_loc Pi; b18 C5b)" % tag,
          b18.cyc_mat_is_zero(b18.cyc_sub_mat(Gc, GPi)))
    A, B, extra = b20.gauss_parts_144(f['trM'])
    check("A8 %s  tr M is a GAUSSIAN INTEGER: tr M = %s + (%s)*i, no other coefficient "
          "nonzero" % (tag, A, B),
          extra == [] and A.denominator == 1 and B.denominator == 1)
    dims = b20.eigen_dims(f['d'], f['trPi'], A, B)
    check("A9 %s  the four trace equations give nonnegative integers summing to dim: "
          "(d_1,d_-1,d_i,d_-i) = (%s,%s,%s,%s), sum = %s = %d"
          % (tag, dims[0], dims[1], dims[2], dims[3], sum(dims), f['d']),
          b20.ok_dims(dims, f['d']))
    f['A'] = A
    f['B'] = B
    f['dims'] = [int(v) for v in dims]
    f['detKtK'] = detKtK
    check("A10 %s re-derived eigen-dims %s == the BANKED eigen-dims %s"
          % (tag, f['dims'], BANKED_DIMS[(p, n)]), f['dims'] == BANKED_DIMS[(p, n)])
    return f


def certify_big_32():
    """(3,2) in Q(zeta_81): the four certificates at the cell's allowed grade."""
    bf = b20.BigFactor(3, 2, FLD)
    tag = bf.tag
    d = bf.d
    q = bf.q

    check("A2 %s  P K = K Pi verified FULLY (all %d rows; no F is involved)" % (tag, bf.N),
          bf.verify_PK_eq_KPi())
    is_sp, detPi = b18.perm_sign_and_det(bf.Pi)
    check("A3 %s  Pi is a signed permutation, det Pi = %+d in {+1,-1}" % (tag, detPi),
          is_sp and detPi in (1, -1))
    bad, ncols = bf.spot_check_FK_eq_KM()
    check("A1 %s  F K = K M SPOT-CHECKED entry-exact on %d deterministic columns "
          "(alpha in {1,2,q-2,q-1} x j in {0,1}), all %d rows each: %d mismatches "
          "(b20 P1a precedent)" % (tag, ncols, bf.N, bad), bad == 0)

    # K^T K, built directly from the two-nonzero column structure
    KtK = [[Fraction(0)] * d for _ in range(d)]
    for c in range(d):
        r1, r2 = bf.rows[c]
        for cp in range(d):
            s1, s2 = bf.rows[cp]
            v = ((1 if r1 == s1 else 0) - (1 if r1 == s2 else 0)
                 - (1 if r2 == s1 else 0) + (1 if r2 == s2 else 0))
            KtK[c][cp] = Fraction(v)
    I8 = [[1 if i == j else 0 for j in range(q - 1)] for i in range(q - 1)]
    KtKpred = b18.kron_scal(I8, b20.tri(q - 1))
    check("A5a %s K^T K == I_%d (x) tridiag(-1,2,-1)_%d entry-exact (the path Laplacian)"
          % (tag, q - 1, q - 1),
          all(KtK[i][j] == KtKpred[i][j] for i in range(d) for j in range(d)))
    detKtK = b18.rat_det(KtK)
    detT = b18.rat_det(b20.tri(q - 1))
    check("A5 %s  det(K^T K) = %s is a NONZERO integer (= det(T_%d)^%d = %s^%d) => "
          "K injective, radical ZERO" % (tag, b18._fmt(detKtK), q - 1, q - 1,
                                         b18._fmt(detT), q - 1),
          detKtK != 0 and detKtK.denominator == 1 and detKtK == detT ** (q - 1))

    # G = K^T F K, entries on demand (no dense F is ever formed)
    G = [[bf.Gent(c, cp) for cp in range(d)] for c in range(d)]
    check("A6a %s G_loc = G_loc^T entry-exact, FULL (F = F^T)" % tag,
          all(G[i][j] == G[j][i] for i in range(d) for j in range(d)))
    Gc = [[f81_conj(G[i][j]) for j in range(d)] for i in range(d)]
    GPi = pi_column_action(G, bf.Pi, FLD.smul)
    check("A7 %s  conj(G_loc) - G_loc * Pi = 0 entry-exact, FULL (%dx%d over %s)"
          % (tag, d, d, FLD.name),
          GPi is not None and all(Gc[i][j] == GPi[i][j]
                                  for i in range(d) for j in range(d)))

    # M^2 = Pi : derived exactly, plus a direct spot verification
    check("A4a %s F^2 = P over %s: sum_(r) zeta_81^(rt) = 81*delta(t) exactly for all "
          "t in [0,81), so (F^2)[m,m'] = delta(m + m' == 0) = P entry-exact"
          % (tag, FLD.name), f81_geometric_sums_ok())
    Mcols = [bf.Mcol(c) for c in range(d)]
    spot = bf.spot_columns()
    badm = 0
    for c in spot:
        v = Mcols[c]
        acc = [[Fraction(0)] * FLD.deg for _ in range(d)]
        for r in range(d):
            vr = v[r]
            if FLD.is_zero(vr):
                continue
            Mr = Mcols[r]
            for i in range(d):
                pr = f81_mul(Mr[i], vr)
                ai = acc[i]
                for k in range(FLD.deg):
                    if pr[k]:
                        ai[k] += pr[k]
        for i in range(d):
            tgt = [Fraction(0)] * FLD.deg
            tgt[0] = bf.Pi[i][c]
            if acc[i] != tgt:
                badm += 1
    check("A4 %s  M^2 - Pi = 0 entry-exact, SPOT on %d deterministic columns (all %d rows "
          "each): %d mismatches; and DERIVED FULLY: F^2 = P (A4a) with F K = K M (A1) and "
          "P K = K Pi (A2) give K M^2 = K Pi, and K is injective (A5) => M^2 = Pi"
          % (tag, len(spot), d, badm), badm == 0)

    tm = bf.trM()
    A, B, extra = FLD.parts(tm)
    check("A8 %s  tr M is a RATIONAL INTEGER in %s (%s contains no i, so d_i = d_-i is "
          "forced): tr M = %s, no other coefficient nonzero"
          % (tag, FLD.name, FLD.name, A),
          extra == [] and A.denominator == 1 and B == 0)
    dims = b20.eigen_dims(d, bf.trPi, A, B)
    check("A9 %s  the four trace equations give nonnegative integers summing to dim: "
          "(d_1,d_-1,d_i,d_-i) = (%s,%s,%s,%s), sum = %s = %d"
          % (tag, dims[0], dims[1], dims[2], dims[3], sum(dims), d),
          b20.ok_dims(dims, d))
    out = dict(p=3, n=2, N=bf.N, q=q, d=d, tag=tag, trPi=bf.trPi, A=A, B=B,
               dims=[int(v) for v in dims], KtK=KtK, detKtK=detKtK, big=bf)
    check("A10 %s re-derived eigen-dims %s == the BANKED eigen-dims %s"
          % (tag, out['dims'], BANKED_DIMS[(3, 2)]),
          out['dims'] == BANKED_DIMS[(3, 2)])
    return out


# ======================================================================================
# THE h = 1 CLASS LAYER: Cl trivial, C[Cl] = C, antipode trivial, coupling the scalar 1.
# ======================================================================================

def ideals_of_Z_of_norm(N, bound=None):
    """Enumerate the ideals of Z_Q = Z of norm N.  Every ideal is (n) for a unique n >= 0;
    the norm is the INDEX [Z : nZ], counted here, not assumed."""
    if bound is None:
        bound = N
    out = []
    for n in range(1, bound + 1):
        idx = len(set(k % n for k in range(0, n + 2 * N + 3)))   # [Z : nZ], counted
        if idx == N:
            out.append(n)
    return out


# ======================================================================================
# MAIN
# ======================================================================================

def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 ADJACENT -- THE h = 1 INSTANCE. REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    sys.stdout.flush()

    # ==================================================================================
    # PART 0 -- the exact field layers and the h = 1 class layer
    # ==================================================================================
    print("=" * 100)
    print("PART 0 -- THE EXACT FIELD LAYERS, AND THE h = 1 CLASS LAYER")
    print("=" * 100)
    check("F0a  Q(zeta_144): Phi_144(zeta) = zeta^48 - zeta^24 + 1 = 0 exactly (b18)",
          (b18.zetapow(48) - b18.zetapow(24) + CO).is_zero())
    check("F0b  Q(zeta_144): i = zeta^36, i^2 = -1 exactly", I144 * I144 == -CO)
    v = [0] * (FLD.N + 1)
    v[FLD.N] = 1
    one = [0] * FLD.deg
    one[0] = 1
    check("F0c  %s: Phi = %s, and the reduction of x^%d is exactly 1 (zeta_81 has order 81)"
          % (FLD.name, FLD.phi_str, FLD.N), list(FLD.red(v)) == one)
    xtest = FLD.mono(5)
    xtest = FLD.add(xtest, FLD.mono(40))
    check("F0d  %s: the added conjugation is an involution on a test element "
          "(conj(conj(x)) = x exactly)" % FLD.name, f81_conj(f81_conj(xtest)) == xtest)
    check("F0e  %s: the added sparse product is exact: zeta^40 * zeta^41 = zeta^81 = 1"
          % FLD.name, f81_mul(FLD.mono(40), FLD.mono(41)) == tuple(Fraction(x)
                                                                   for x in one))
    check("F0f  %s: x * conj(x) = 1 for x = zeta_81^k, all k in [0,81) (unit circle)"
          % FLD.name,
          all(f81_mul(FLD.mono(k), f81_conj(FLD.mono(k)))
              == tuple(Fraction(x) for x in one) for k in range(FLD.N)))
    print()

    print("--- THE h = 1 CLASS LAYER, EXACTLY (registration items (ii) and (iv)) ---")
    CL = [1]                                    # Cl(Q) = the trivial group
    CMAT1 = [[1]]                               # the coupling matrix: the SCALAR 1
    AMAT1 = [[1]]                               # the antipode: TRIVIAL
    check("H1a  Cl(Q) is trivial: |Cl| = 1, so C[Cl] = C has dim 1 "
          "(h = 3 banked: dim 3)", len(CL) == 1)
    check("H1b  the antipode A on C[Cl] is the identity 1x1 matrix and A^2 = 1 exactly",
          b18.mm_scal_scal(AMAT1, AMAT1) == [[Fraction(1)]])
    check("H1c  A C A = C exactly (vacuously: A = 1)",
          b20.rat_mm(b20.rat_T(AMAT1), b20.rat_mm(CMAT1, AMAT1)) == [[Fraction(1)]])
    fix_dim = 1
    anti_dim = 0
    check("H1d  H^2 = C DATA LINE: dim C[Cl] = 1; antipode-INVARIANT dim = %d; "
          "antipode-ANTI-invariant dim = %d (h = 3 banked: dim 3, invariant 2, anti 1)"
          % (fix_dim, anti_dim), fix_dim == 1 and anti_dim == 0)
    pivC, okC = b20.rat_congruence(CMAT1)
    check("H1e  C|_fix = the scalar [%s]: exact rational congruence pivot (%s) POSITIVE "
          "=> C|_fix is rational SPD of dim 1 (h = 3 banked spectrum {4,1})"
          % (CMAT1[0][0], ", ".join(str(x) for x in pivC)),
          okC and all(x > 0 for x in pivC))
    print("      REGISTERED READING (iv), stated before the cells: the h = 3 T-fixed")
    print("      NEGATIVES lived in the antipode-ANTI-invariant channel (lam-product = -1,")
    print("      nu = -1).  At h = 1 that channel has dimension %d -- IT HAS NO HOME."
          % anti_dim)
    print("      tau = epsilon at h = 1 (the two scalarizations coincide); B5's selection")
    print("      principle (tau class-separating) is VACUOUS here -- the LEDGER SEPARATION")
    print("      is the second thing the class resolution supplied, and it is absent.")
    print()

    # ==================================================================================
    # PART 1 -- the four factors, the four certificates each
    # ==================================================================================
    print("=" * 100)
    print("PART 1 -- THE FOUR FACTORS: THE FOUR CERTIFICATES RE-ASSERTED (item (i))")
    print("=" * 100)
    print("  The certificates never involved the class layer, so they are UNCHANGED at")
    print("  h = 1.  They are re-run here, not cited.")
    print()
    facs = {}
    for (p, n) in [(2, 1), (3, 1), (2, 2)]:
        print("--- FACTOR (%d,%d) in Q(zeta_144) ---" % (p, n))
        facs[(p, n)] = certify_small(p, n)
        print()
    print("--- FACTOR (3,2) in Q(zeta_81) (sparse: no dense F is ever formed) ---")
    facs[(3, 2)] = certify_big_32()
    print()

    print("--- DIRECT EXACT NULLITY VERIFICATION OF THE EIGEN-DIMS (small factors) ---")
    LAMS = [CO, -CO, I144, -I144]
    eigbasis = {}
    for (p, n) in [(2, 1), (3, 1), (2, 2)]:
        f = facs[(p, n)]
        M = f['M']
        d = f['d']
        nul = []
        bs = []
        for lv in LAMS:
            ns = b20.cyc_nullspace([[M[i][j] - (lv if i == j else CZ) for j in range(d)]
                                    for i in range(d)])
            bs.append([[ns[c][r] for c in range(len(ns))] for r in range(d)])
            nul.append(len(ns))
        eigbasis[(p, n)] = bs
        check("A11 %s direct exact nullity of (M - lambda I) for lambda = 1,-1,i,-i is "
              "(%d,%d,%d,%d) == the trace-formula dims (%d,%d,%d,%d) == BANKED"
              % tuple([f['tag']] + nul + f['dims']), nul == f['dims'])
    print("      (3,2): dims by the trace formulas only -- a direct nullity at dim 64 over")
    print("      Q(zeta_81) would require the dense operator the sparsity rule forbids; "
          "declared.")
    print()

    print("--- PART 1 TABLE ---")
    print("  %-8s %-6s %-14s %-8s %-6s %-6s %-6s %-6s %-14s %s"
          % ("factor", "dim", "tr M", "tr Pi", "d_1", "d_-1", "d_i", "d_-i",
             "det(K^T K)", "field"))
    for k in [(2, 1), (2, 2), (3, 1), (3, 2)]:
        f = facs[k]
        trs = "%d %+d*i" % (int(f['A']), int(f['B']))
        fname = "Q(zeta_81)" if k == (3, 2) else "Q(zeta_144)"
        print("  %-8s %-6d %-14s %-8d %-6d %-6d %-6d %-6d %-14s %s"
              % (f['tag'], f['d'], trs, int(f['trPi']), f['dims'][0], f['dims'][1],
                 f['dims'][2], f['dims'][3], b18._fmt(f['detKtK']), fname))
    print()

    # ==================================================================================
    # PART 2 -- the cells: dims, class dims, T-fixed negatives, full-pairing negatives
    # ==================================================================================
    print("=" * 100)
    print("PART 2 -- THE CELLS AT h = 1 (SECTOR ARITHMETIC: PURE INTEGERS)")
    print("=" * 100)
    print("  At h = 1 the class layer is the scalar 1, so T-fixed <=> lam-product = +1")
    print("  (nu is forced to +1: there is only the trivial character).  On a T-fixed")
    print("  vector B(v,v) = (lam-product) * ||v||^2 * a_N = +||v||^2 * 1.")
    print()
    celldata = []
    corrected = []
    for clab, fl, Nnorm in H1_CELLS:
        dl = [facs[k]['dims'] for k in fl]
        D = b20.glue_dims(dl)
        seclen = 1
        for k in fl:
            seclen *= facs[k]['d']
        cell_dim = seclen * 1                   # |Cl| = 1
        check("P2a  cell %-12s glued eigen-dims (D_1,D_-1,D_i,D_-i) = (%d,%d,%d,%d) "
              "sum to the section's transform dim %d"
              % (clab, D[0], D[1], D[2], D[3], seclen), sum(D) == seclen)
        # class dim by sector sums (the honest computation)
        secs_plus = b20.sector_list(dl, 0)
        cls = 0
        items = []
        for s in secs_plus:
            dd = 1
            for t, b in enumerate(s):
                dd *= dl[t][b]
            cls += dd
            items.append((s, dd))
        cls = cls * fix_dim
        check("P2b  cell %-12s class dim by sector sums = D_1 * (antipode-fixed dim) = "
              "%d * %d = %d" % (clab, D[0], fix_dim, cls), cls == D[0] * fix_dim)
        reg = REGISTERED_CLASS_DIMS[clab]
        if cls != reg:
            note("P2c  cell %s: REGISTRATION ARITHMETIC CORRECTED IN-RUN -- the "
                 "registration wrote %d; the computed class dim is %d. The registration's "
                 "(iii)/(iv) STRUCTURE is what was registered; this specific number was "
                 "flagged as checkable arithmetic. The COMPUTED value %d is used."
                 % (clab, reg, cls, cls))
            corrected.append((clab, reg, cls))
        else:
            check("P2c  cell %-12s class dim %d == the registration's arithmetic (%d)"
                  % (clab, cls, reg), cls == reg)
        # full-pairing negatives: lam-product = -1 sectors, scalar class (multiplier 1)
        secs_minus = b20.sector_list(dl, 1)
        fneg = 0
        nitems = []
        for s in secs_minus:
            dd = 1
            for t, b in enumerate(s):
                dd *= dl[t][b]
            fneg += dd
            nitems.append((s, dd))
        fneg = fneg * 1
        # T-fixed negatives, BY ENUMERATION over the T-fixed sector set
        tneg = 0
        for s, dd in items:
            sign = 0                            # lam-product index; 0 == +1
            for t, b in enumerate(s):
                sign = b20.MULT[(sign, b)]
            if sign != 0:                       # a T-fixed sector with negative B
                tneg += dd
        # the anti-invariant channel that housed h = 3's T-fixed negatives
        tneg_anti = D[1] * anti_dim
        celldata.append(dict(clab=clab, fl=fl, Nnorm=Nnorm, dl=dl, D=D, seclen=seclen,
                             cell_dim=cell_dim, cls=cls, items=items, fneg=fneg,
                             nitems=nitems, tneg=tneg, tneg_anti=tneg_anti))
        check("P2d  cell %-12s T-FIXED NEGATIVE COUNT = 0, by ENUMERATION: every T-fixed "
              "sector has lam-product = +1 (%d sectors, total dim %d) so B = +||v||^2 * 1 "
              "> 0; and the antipode-ANTI channel that housed h = 3's T-fixed negatives "
              "has dim D_-1 * %d = %d * %d = %d -- EMPTY (item (iv))"
              % (clab, len(items), cls, anti_dim, D[1], anti_dim, tneg_anti),
              tneg == 0 and tneg_anti == 0)

    print()
    print("--- THE {2:2,3:2} CLASS-DIM ARITHMETIC, LONGHAND (the flagged number) ---")
    cd36 = [c for c in celldata if c['clab'] == "{2:2,3:2}"][0]
    tot = 0
    for s, dd in cd36['items']:
        lab = " x ".join("%s:%s" % (facs[cd36['fl'][t]]['tag'], b20.EIG_NAMES[b])
                         for t, b in enumerate(s))
        parts = " * ".join(str(cd36['dl'][t][b]) for t, b in enumerate(s))
        print("      %-26s  %s = %d" % (lab, parts, dd))
        tot += dd
    print("      ---------------------------------------------------------------")
    print("      sum over lam-product = +1 of d_x * d_y = %d  (x |Cl| = 1)  = %d" % (tot, tot))
    print("      the registration wrote 208.  COMPUTED: %d." % tot)
    print()

    print("--- PER-CELL TABLE ---")
    print("  %-12s %-6s %-9s %-28s %-11s %-16s %s"
          % ("cell", "norm", "cell dim", "(D_1,D_-1,D_i,D_-i)", "class dim",
             "T-fixed negs", "full-pairing negs"))
    for cd in celldata:
        print("  %-12s %-6d %-9d %-28s %-11d %-16d %d"
              % (cd['clab'], cd['Nnorm'], cd['cell_dim'],
                 "(%d,%d,%d,%d)" % tuple(cd['D']), cd['cls'], cd['tneg'], cd['fneg']))
    print("  (cell dim = product of local Sonin dims x |Cl| = ... x 1; the class = the")
    print("   T-fixed space = the lam-product = +1 sectors; full-pairing negs = the")
    print("   lam-product = -1 sectors, OFF the fixed space.)")
    print()

    print("--- SECTOR LISTS: THE PLACE-SUPPORT OF EVERY LIVE AND EVERY NEGATIVE SECTOR ---")
    for cd in celldata:
        print("  cell %s (norm %d)" % (cd['clab'], cd['Nnorm']))
        for tname, its in [("class    (lam-product = +1)", cd['items']),
                           ("negative (lam-product = -1, OFF the fixed space)",
                            cd['nitems'])]:
            if not its:
                print("     %s: NONE" % tname)
                continue
            print("     %s: dim %d" % (tname, sum(dd for _, dd in its)))
            for s, dd in its:
                print("        %s -> %d"
                      % (" x ".join("%s:%s" % (facs[cd['fl'][t]]['tag'], b20.EIG_NAMES[b])
                                    for t, b in enumerate(s)), dd))
    print()

    c21 = [c for c in celldata if c['clab'] == "{2:1}"][0]
    check("P2e  the DEATH AT {2:1} SURVIVES h = 1: class dim = %d. The single factor (2,1) "
          "has M = [i] and eigen-dims (0,0,1,0); no lam-product = +1 sector exists. It was "
          "NEVER a class phenomenon -- it is the sector arithmetic of the place 2 alone."
          % c21['cls'], c21['cls'] == 0)
    c2131 = [c for c in celldata if c['clab'] == "{2:1,3:1}"][0]
    revived = ((2, 3) in [tuple(s) for s, _ in c2131['items']])
    check("P2f  the REVIVAL at {2:1,3:1} is through the conjugate sector "
          "((2,1):i x (3,1):-i), class dim = %d -- THE SAME SECTOR SET as h = 3's class"
          % c2131['cls'], revived and c2131['cls'] == 1)
    print()

    # ==================================================================================
    # PART 3 -- DIRECT EXACT POSITIVITY OF B|_class (NO CLASS TENSOR)
    # ==================================================================================
    print("=" * 100)
    print("PART 3 -- DIRECT EXACT POSITIVITY OF B|_class AT {2:1,3:1} AND {2:2,3:1}")
    print("=" * 100)
    print("  B(v,w) = v^dagger G_g w with G_g = K_g^T F_g K_g = (K_g^T K_g) M_g.  At h = 1")
    print("  there is NO class tensor: the coupling is the scalar a_N = 1.  On the class")
    print("  (M_g v = v) this collapses to B|_class = E^dagger (K_g^T K_g) E -- a rational")
    print("  SPD form pulled back through a full-column-rank E: POSITIVE-DEFINITE under")
    print("  EVERY embedding.  That is the b20 rational-SPD factorization route, with")
    print("  C|_fix replaced by the positive scalar 1.")
    print()

    posresults = []
    for clab, fl in [("{2:1,3:1}", [(2, 1), (3, 1)]), ("{2:2,3:1}", [(2, 2), (3, 1)])]:
        cd = [c for c in celldata if c['clab'] == clab][0]
        fa, fb = facs[fl[0]], facs[fl[1]]
        ng = fa['d'] * fb['d']
        print("--- CELL %s : section dim %d (= %d x %d x |Cl| 1) ---"
              % (clab, ng, fa['d'], fb['d']))
        Mg = b18.kron_cyc(fa['M'], fb['M'])
        Gg = b18.kron_cyc(fa['G'], fb['G'])
        KtKg = b18.kron_scal(fa['KtK'], fb['KtK'])
        check("P3a %-12s G_g = (K_g^T K_g) M_g entry-exact (the mechanism's engine)"
              % clab, b18.cyc_mat_is_zero(
                  b18.cyc_sub_mat(Gg, b18.mm_scal_cyc(KtKg, Mg))))

        # the exact eigenbasis of the class: tensor the per-factor exact eigenbases over
        # every lam-product = +1 sector pair
        cols = []
        used = []
        for x in range(4):
            for y in range(4):
                if b20.MULT[(x, y)] != 0:
                    continue
                Ea = eigbasis[fl[0]][x]
                Eb = eigbasis[fl[1]][y]
                ka = len(Ea[0]) if Ea and Ea[0] else 0
                kb = len(Eb[0]) if Eb and Eb[0] else 0
                if ka == 0 or kb == 0:
                    continue
                blk = b18.kron_cyc(Ea, Eb)
                for c in range(len(blk[0])):
                    cols.append([blk[r][c] for r in range(ng)])
                used.append((x, y, ka * kb))
        kf = len(cols)
        E = [[cols[c][r] for c in range(kf)] for r in range(ng)]
        print("      class eigenbasis assembled from the lam-product = +1 sector pairs:")
        for (x, y, dd) in used:
            print("        %s:%-3s x %s:%-3s -> %d columns"
                  % (fa['tag'], b20.EIG_NAMES[x], fb['tag'], b20.EIG_NAMES[y], dd))
        check("P3b %-12s the assembled exact eigenbasis has %d columns == the sector-"
              "arithmetic class dim (%d)" % (clab, kf, cd['cls']), kf == cd['cls'])
        MgE = b18.mm_cyc_cyc(Mg, E)
        check("P3c %-12s M_g E - E = 0 entry-exact: every assembled column really IS "
              "T-fixed (eigenvalue +1 of M_g)" % clab,
              b18.cyc_mat_is_zero(b18.cyc_sub_mat(MgE, E)))
        Ed = b20.cyc_dag(E)
        Bcl = b18.mm_cyc_cyc(Ed, b18.mm_cyc_cyc(Gg, E))
        S = b18.mm_scal_cyc(KtKg, E)
        pred = b18.mm_cyc_cyc(Ed, S)
        check("P3d %-12s B|_class == E^dagger (K_g^T K_g) E ENTRY-EXACT -- the registered "
              "mechanism B|_class = ||v||^2 * (scalar 1), NO class tensor, dim %d"
              % (clab, kf), b18.cyc_eq_mat(Bcl, pred))
        herm = all(Bcl[i][j] == Bcl[j][i].conj() for i in range(kf) for j in range(kf))
        check("P3e %-12s B|_class is HERMITIAN entry-exact (B = B^dagger)" % clab, herm)
        pivK, okK = b20.rat_congruence(KtKg)
        check("P3f %-12s K_g^T K_g is RATIONAL SYMMETRIC POSITIVE-DEFINITE -- exact "
              "rational congruence pivots all positive (%s)"
              % (clab, ", ".join(str(x) for x in pivK)),
              okK and all(x > 0 for x in pivK))
        rk = b20.cyc_rank(Ed)
        check("P3g %-12s the class eigenbasis E has FULL COLUMN RANK %d over Q(zeta_144) "
              "(exact rank of E^dagger)" % (clab, kf), rk == kf)
        okpos = (okK and all(x > 0 for x in pivK) and rk == kf
                 and b18.cyc_eq_mat(Bcl, pred) and okC and all(x > 0 for x in pivC))
        check("P3h %-12s EXACT POSITIVITY CERTIFICATE (embedding-independent): "
              "B|_class = E^dagger S E * a_N with S = K_g^T K_g rational SPD, E of full "
              "column rank %d, and a_N = 1 a POSITIVE SCALAR => B|_class is "
              "POSITIVE-DEFINITE of dim %d under EVERY embedding of Q(zeta_144). "
              "NO NEGATIVE DIRECTION ON THE CLASS." % (clab, kf, kf), okpos)
        # the b20 fallback ledger, reported not smoothed
        piv = b20.cyc_congruence(Bcl)
        allrat = all(x.is_rational() for x in piv)
        print("      Hermitian congruence pivots of B|_class over Q(zeta_144):")
        for t, x in enumerate(piv):
            print("        pivot %d = %s" % (t + 1, b18.cyc_str(x)))
            print("                  rational? %s ; rational part = %s"
                  % (x.is_rational(), x.rational_part()))
        if allrat:
            check("P3i %-12s every congruence pivot is a POSITIVE RATIONAL => "
                  "POSITIVE-DEFINITE exactly by the congruence route as well" % clab,
                  all(x.rational_part() > 0 for x in piv))
        else:
            note("P3i  %s: the b20 FALLBACK is in force -- the congruence pivots are "
                 "REAL BUT IRRATIONAL (they are ||v||^2, totally positive in the real "
                 "subfield, not rationals). Reported, not smoothed; the EXACT "
                 "embedding-independent certificate is P3h." % clab)
        posresults.append((clab, kf, okpos))
        print()

    print("--- THE OTHER TWO CELLS: SECTOR-ASSEMBLED, THE SAME MECHANISM ---")
    for cd in celldata:
        if cd['clab'] in ("{2:1,3:1}", "{2:2,3:1}"):
            continue
        print("  cell %-12s class dim %-4d -- %s"
              % (cd['clab'], cd['cls'],
                 "EMPTY (nothing to certify: the class died at the arrival of 2)"
                 if cd['cls'] == 0 else
                 "B|_class POSITIVE-DEFINITE of dimension %d by the same mechanism "
                 "(not directly diagonalized: the (3,2) factor's dense operator is "
                 "forbidden by the sparsity rule; the mechanism identity "
                 "B|_class = E^dagger (K^T K) E is verified ENTRY-EXACT at the two "
                 "cells above, and K^T K is rational SPD at (3,2) by A5a/A5)" % cd['cls']))
    print()

    # ==================================================================================
    # PART 4 -- the coupling scalar, enumerated
    # ==================================================================================
    print("=" * 100)
    print("PART 4 -- THE COUPLING SCALAR: THE IDEALS OF Q OF NORM 6 AND OF NORM 36")
    print("=" * 100)
    print("  ENUMERATION LOGIC, stated before the count: Z_Q = Z is a PID; every nonzero")
    print("  ideal is (n) for a unique integer n >= 1, and its norm is the INDEX [Z : nZ],")
    print("  which is counted below (not assumed) as the number of residues mod n.")
    print("  So the ideals of norm N are exactly the n in [1, N] whose counted index is N.")
    print()
    print("  %-6s %-40s %-8s %s" % ("norm N", "ideals (n) with [Z:nZ] = N", "count",
                                    "a_N (zeta coefficient)"))
    coupvals = {}
    for Nn in [2, 6, 12, 36]:
        gens = ideals_of_Z_of_norm(Nn)
        coupvals[Nn] = len(gens)
        print("  %-6d %-40s %-8d %d"
              % (Nn, ", ".join("(%d)" % g for g in gens), len(gens), len(gens)))
    check("P4a  the number of ideals of Q of norm 6, ENUMERATED, is 1 (the single ideal "
          "(6)) = the coupling scalar at cell {2:1,3:1}", coupvals[6] == 1)
    check("P4b  the number of ideals of Q of norm 36, ENUMERATED, is 1 (the single ideal "
          "(36)) = the coupling scalar at cell {2:2,3:2}", coupvals[36] == 1)
    check("P4c  a_N = 1 at every cell norm (2, 6, 12, 36) -- the coupling matrix is the "
          "1x1 POSITIVE matrix [1]; zeta_Q(s) = sum_(n>=1) n^-s has every coefficient 1",
          all(coupvals[Nn] == 1 for Nn in [2, 6, 12, 36]) and CMAT1 == [[1]])
    print("  CONTRAST, banked (h = 3): the coupling was circulant(2,1,1) = c2*c3 with")
    print("  spectrum (4,1,1) and C|_fix spectrum {4,1}.  At h = 1 it is the scalar 1.")
    print("  Positivity rode the POSITIVITY OF THE EULER COEFFICIENTS at h = 3; it rides")
    print("  the positivity of the single coefficient a_N = 1 here.  SAME MECHANISM.")
    print()
    check("P4d  tau = epsilon at h = 1: with |Cl| = 1 there is exactly ONE class character "
          "(the trivial one), so the class-separating scalarization tau and the plain "
          "epsilon coincide -- B5's selection principle is VACUOUS, a NAMED LOSS",
          len(CL) == 1)
    print()

    # ==================================================================================
    # VERDICT
    # ==================================================================================
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    allpos = all(ok for _, _, ok in posresults)
    check("V1   (H1-same) FOR THE SIGN: B|_class is POSITIVE-DEFINITE at every cell where "
          "the class is nonzero, certified EXACTLY and embedding-independently at "
          "{2:1,3:1} (dim %d) and {2:2,3:1} (dim %d), with C|_fix replaced by the positive "
          "scalar a_N = 1. The class resolution was STRUCTURE, not the source of the sign."
          % (posresults[0][1], posresults[1][1]), allpos)
    check("V2   THE (iv) READING, BANKED BESIDE IT: T-fixed negative directions at h = 1 "
          "= 0 at EVERY cell (enumerated), because the antipode-ANTI-invariant channel -- "
          "the home of h = 3's T-fixed negatives -- has dimension 0. The flip channel has "
          "NO HOME at h = 1.", all(cd['tneg'] == 0 and cd['tneg_anti'] == 0
                                   for cd in celldata))
    print("  THE TWO NAMED LOSSES (what the class resolution actually supplied):")
    print("   (1) THE CHANNEL: the antipode-anti-invariant part of C[Cl] (dim 1 at h = 3,")
    print("       dim 0 at h = 1) -- the home of T-fixed negativity. Without it the")
    print("       arrival-edge negativity-in-the-flipped-channel CANNOT OCCUR at h = 1.")
    print("       (The full pairing's lam-product = -1 negatives DO remain, off the fixed")
    print("       space: %s.)"
          % ("; ".join("%s -> %d" % (cd['clab'], cd['fneg']) for cd in celldata)))
    print("   (2) THE LEDGER SEPARATION: tau class-separating vs epsilon. At h = 1,")
    print("       tau = epsilon and B5's selection principle is vacuous.")
    print("  NEITHER loss touches the POSITIVITY, which rides the same sector-forcing at")
    print("  both h -- exactly as the longhand expectation registered.")
    print("  (H1-collapse) did NOT occur for the sign; its content is instead the two")
    print("  NAMED losses above, recorded as registered. (H1-third) not needed.")
    print()
    if corrected:
        print("  NOT LANDING AS REGISTERED -- REGISTRATION ARITHMETIC CORRECTED IN-RUN:")
        for clab, reg, got in corrected:
            print("    cell %s: registration wrote %d; COMPUTED %d. The (iii)/(iv) "
                  "STRUCTURE" % (clab, reg, got))
            print("    is what was registered and it stands; the flagged number is "
                  "replaced by the computed value.")
    else:
        print("  Every registered number landed as written; no in-run correction was "
              "needed.")
    print()
    print("  SCOPE, said plainly: these are EXACT properties of a FINITE CONSTRUCTED MODEL")
    print("  SECTION over Q at finite place sets and finite cutoffs. No sign is asserted")
    print("  about any ledger; the register is untouched; nothing here bears on")
    print("  W_inf - Sum W_p at complete roster, and NOTHING here is about the Hypothesis.")
    print()
    n_ok = sum(1 for _, ok in LEDGER if ok)
    n_all = len(LEDGER)
    print("--- EXACT LEDGER ---")
    for name, ok in LEDGER:
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    if NOTES:
        print()
        print("--- NOTES (recorded, not asserted) ---")
        for nm in NOTES:
            print("  NOTE  %s" % nm)
    print()
    print("ALL EXACT LINES EXACT: %d/%d PASS" % (n_ok, n_all))


if __name__ == "__main__":
    main()
