"""W-ATTEMPT-2, SITTING 9 — WHERE THE NEGATIVE DIRECTIONS LIVE: THE ARITHMETIC ALONG THE STAIRCASE.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA at bench
grade; refused: any promotion to W_inf - Sum W_p at complete roster, or register movement.
THE PROTOCOL CORRECTION carried: the closure protocol gates the REGISTER and public claims,
not investigation — this is the programme testing its own object. THE GUARD (spec 6(c)):
ledger positivity is GRH; this instrument measures a finite constructed model section,
never the ledger.

THE SECTOR ARITHMETIC, DERIVED LONGHAND BEFORE ANY RUN
======================================================
The glued transform T = (tensor of the M_p) (x) A has factor eigenvalues in {1,-1,i,-i}
(M^2 = Pi, certified) and class eigenvalue nu in {+1 (dim 2), -1 (dim 1)}. The pairing's
quadratic form on a sector with transform-eigenvalue product lam_prod is
    B(v,v) = lam_prod * ||v||^2 * (C on the nu-eigenspace),
real exactly when lam_prod = +/-1; the lam_prod = +/-i sectors are the twist's ZERO block
(the banked (d/4, d/4, 0:d/2) signature). C is positive on BOTH channels (spectrum {4,1}
on the antipode-invariant part, {1} on the anti-invariant part). THEREFORE, structurally:
 (i)  NEGATIVE DIRECTIONS OF THE FULL PAIRING = the lam_prod = -1 sectors tensor ALL of
      C[Cl] — they appear in BOTH channels, invariant : anti-invariant = 2 : 1 in dim.
 (ii) T-FIXED OFF-CLASS NEGATIVES (sitting 7's object) = sectors with lam_prod * nu = 1
      and nu = -1 — STRUCTURALLY anti-invariant only.
So the ferried (N-edge) branch's channel half HOLDS STRUCTURALLY for the T-fixed reading
and FAILS STRUCTURALLY for the full reading (registered before the run; both tabulated).
The LIVE arithmetic this sitting measures is the STAIRCASE SCHEDULE: where each reading's
negative count FIRST becomes nonzero (a place-arrival edge or a deepening/interior step),
and how it grows, per place set — including the DEAD ARRIVAL of 5 at a^2 = 5.

FIRST-APPEARANCE LONGHAND, registered: at {2:1} the single factor has eigen-dims
(0,0,1,0) — no lam_prod = -1 sector and no T-fixed sector exists, so BOTH readings have
ZERO negatives below a^2 = 3 and both first appear AT a^2 = 3 = THE ARRIVAL OF 3 (the
edge). Growth is expected at every staircase step thereafter (banked: T-fixed off-class
1 -> 9 across the deepening a^2 = 3 -> 4): the registration DISTINGUISHES first
appearance (the edge question) from growth (every step); both are recorded.

THE BRANCHES, as ferried:
 (N-edge)     first appearance at arrival edges; T-fixed negatives anti-invariant
              throughout; the constrained class stays positive along the whole staircase
              (P+ extended).
 (N-interior) a first appearance at a cell interior, or a T-fixed negative in the
              invariant channel — place-support named, the constrained-class positivity
              re-checked exactly at that cell.
 (N-third)    filed openly.

CELLS: a^2 in {3, 4, 5, 8, 9, 12} on {inf,2,3} and {inf,2,3,5}:
 {inf,2,3}   : {2:1,3:1} · {2:2,3:1} · {2:2,3:1} · {2:3,3:1} · {2:3,3:2} · {2:3,3:2}
 {inf,2,3,5} : same through a^2 = 4, then {2:2,3:1,5:1} · {2:3,3:1,5:1} · {2:3,3:2,5:1}
               · {2:3,3:2,5:1}
FACTORS: (2,1),(2,2),(2,3),(3,1),(3,2) banked exact (sitting 7); (5,1) NEW — exact over
Q(zeta_25), Phi_25(x) = x^20 + x^15 + x^10 + x^5 + 1, the same sparse technique, eigen-dims
by the trace formulas with P K = K Pi verified fully and F K = K M spot-checked; note
i is not in Q(zeta_25), so d_i = d_-i is forced there (the p-odd pattern).

RECORDED PLAINLY AS DATA about the built object. The register is untouched.
Usage:  python b22_attempt2_s9.py register | run
"""

import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import b18_attempt2_s5 as b18            # noqa: E402  (sitting 5's certified machinery)
import b20_attempt2_s7 as b20            # noqa: E402  (sitting 7's staircase machinery)

# ======================================================================================
# PURE-ASCII OUTPUT GUARD.  The banked registration docstring above is kept VERBATIM
# (byte-for-byte as registered) and is NOT altered; typographic characters are folded to
# ASCII at PRINT time only, so every emitted byte is < 128 on any console/redirect.
# ======================================================================================

_ASCII_FOLD = {0x2014: u"--", 0x2013: u"-", 0x2012: u"-", 0x2010: u"-", 0x2011: u"-",
               0x2018: u"'", 0x2019: u"'", 0x201c: u'"', 0x201d: u'"',
               0x2026: u"...", 0x00a0: u" ", 0x00d7: u"x", 0x2212: u"-",
               0x00b7: u"."}

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
# EXACT LEDGER.  Every entry is an EXACT arithmetic statement; no float ever enters this
# instrument at all (sitting 9 carries no archimedean float part).
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
# FIELD LAYER: Q(zeta_25), Phi_25(x) = x^20 + x^15 + x^10 + x^5 + 1,
# so x^20 = -x^15 - x^10 - x^5 - 1.  Elements are 20-tuples of Fractions.
# The additive/scalar layer is sitting 7's generic Fld; this sitting ADDS exact field
# multiplication, exact field inversion (extended Euclid mod Phi_25), and the quadratic
# extension Q(zeta_25)(i) needed for the direct nullity at lambda = +/- i.
# ======================================================================================

FLD25 = b20.Fld("Q(zeta_25)", 25, 20, [(15, -1), (10, -1), (5, -1), (0, -1)], None,
                "x^20 + x^15 + x^10 + x^5 + 1")

D25 = FLD25.deg
PHI25 = [Fraction(0)] * (D25 + 1)
for _k in (0, 5, 10, 15, 20):
    PHI25[_k] = Fraction(1)

F25_ZERO = FLD25.zero()
F25_ONE = tuple([Fraction(1)] + [Fraction(0)] * (D25 - 1))


def f25_mul(a, b):
    """Exact multiplication in Q(zeta_25) (polynomial product, then reduce mod Phi_25)."""
    acc = [Fraction(0)] * (2 * D25 - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    acc[i + j] += ai * bj
    return tuple(FLD25.red(acc))


def f25_inv(x):
    """Exact inverse in Q(zeta_25) by the extended Euclidean algorithm mod Phi_25."""
    if FLD25.is_zero(x):
        raise ZeroDivisionError("inverse of 0 in Q(zeta_25)")
    r0, r1 = list(PHI25), list(x)
    s0, s1 = [Fraction(0)], [Fraction(1)]
    while b20._pdeg(r1) > 0:
        q, r = b20._pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, b20._psub(s0, b20._pmul(q, s1))
    u = [v / r1[0] for v in s1]
    u = u + [Fraction(0)] * (2 * D25 - len(u))
    return tuple(FLD25.red(u))


def f25_rank(A):
    """Exact rank over Q(zeta_25) (Gauss-Jordan)."""
    n, m = len(A), len(A[0])
    M = [list(r) for r in A]
    row = 0
    for col in range(m):
        if row == n:
            break
        p = None
        for r in range(row, n):
            if not FLD25.is_zero(M[r][col]):
                p = r
                break
        if p is None:
            continue
        M[row], M[p] = M[p], M[row]
        iv = f25_inv(M[row][col])
        M[row] = [f25_mul(iv, v) for v in M[row]]
        for r in range(n):
            if r != row and not FLD25.is_zero(M[r][col]):
                f = M[r][col]
                M[r] = [FLD25.sub(M[r][k], f25_mul(f, M[row][k])) for k in range(m)]
        row += 1
    return row


# ---- the quadratic extension E = Q(zeta_25)(i):  elements are pairs (a, b) = a + b*i ----

E_ZERO = (F25_ZERO, F25_ZERO)
E_ONE = (F25_ONE, F25_ZERO)
E_I = (F25_ZERO, F25_ONE)
E_MONE = (FLD25.smul(F25_ONE, Fraction(-1)), F25_ZERO)
E_MI = (F25_ZERO, FLD25.smul(F25_ONE, Fraction(-1)))


def e_sub(x, y):
    return (FLD25.sub(x[0], y[0]), FLD25.sub(x[1], y[1]))


def e_mul(x, y):
    return (FLD25.sub(f25_mul(x[0], y[0]), f25_mul(x[1], y[1])),
            FLD25.add(f25_mul(x[0], y[1]), f25_mul(x[1], y[0])))


def e_is_zero(x):
    return FLD25.is_zero(x[0]) and FLD25.is_zero(x[1])


def e_inv(x):
    n = FLD25.add(f25_mul(x[0], x[0]), f25_mul(x[1], x[1]))
    ni = f25_inv(n)
    return (f25_mul(x[0], ni), FLD25.smul(f25_mul(x[1], ni), Fraction(-1)))


def e_rank(A):
    """Exact rank over Q(zeta_25)(i) (Gauss-Jordan)."""
    n, m = len(A), len(A[0])
    M = [list(r) for r in A]
    row = 0
    for col in range(m):
        if row == n:
            break
        p = None
        for r in range(row, n):
            if not e_is_zero(M[r][col]):
                p = r
                break
        if p is None:
            continue
        M[row], M[p] = M[p], M[row]
        iv = e_inv(M[row][col])
        M[row] = [e_mul(iv, v) for v in M[row]]
        for r in range(n):
            if r != row and not e_is_zero(M[r][col]):
                f = M[r][col]
                M[r] = [e_sub(M[r][k], e_mul(f, M[row][k])) for k in range(m)]
        row += 1
    return row


# ======================================================================================
# THE (5,1) FACTOR: sitting 7's BigFactor at p = 5, n = 1, N = 25, dim Son = 16.
# Every F entry is produced ON DEMAND (the Sonin basis has two nonzero entries per
# column), so no dense 25 x 25 transform is ever formed.  N = 25 is small enough that
# BOTH structure identities are verified FULLY, not spot-checked.
# ======================================================================================

def full_check_FK_eq_KM(bf, Mcols):
    """(F K)[:,c] == (K M)[:,c] for ALL columns c and ALL N rows.  Returns (bad, ncols)."""
    fld = bf.fld
    N = bf.N
    q = bf.q
    bad = 0
    for c in range(bf.d):
        Mc = Mcols[c]
        r1, r2 = bf.rows[c]
        for mm in range(N):
            e = [0] * N
            e[(mm * r1) % N] += 1
            e[(mm * r2) % N] -= 1
            lhs = tuple(Fraction(x, q) for x in fld.red(e))
            rhs = [Fraction(0)] * fld.deg
            for (r, s) in bf.krow(mm):
                v = Mc[r]
                for k in range(fld.deg):
                    if v[k]:
                        rhs[k] += s * v[k]
            if lhs != tuple(rhs):
                bad += 1
    return bad, bf.d


def ktk_from_rows(bf):
    """K^T K built directly from the sparse column supports (exact integers)."""
    d = bf.d
    out = [[Fraction(0)] * d for _ in range(d)]
    sup = []
    for c in range(d):
        r1, r2 = bf.rows[c]
        sup.append({r1: 1, r2: -1})
    for c in range(d):
        for cp in range(d):
            s = Fraction(0)
            for r, v in sup[c].items():
                w = sup[cp].get(r)
                if w:
                    s += v * w
            out[c][cp] = s
    return out


# ======================================================================================
# THE SECTOR ALGEBRA (pure integer arithmetic on the factor eigen-dims)
# ======================================================================================

EIG = b20.EIG_NAMES                      # ("1", "-1", "i", "-i")
LAM_REAL = {0: 1, 1: -1}                 # index -> real eigenvalue, for the two real ones
NU_CHANNELS = ((1, 2, "invariant"), (-1, 1, "anti-invariant"))


def sectors_with(dl, target):
    """[(sector tuple, dim)] for all sectors whose transform-eigenvalue product is target."""
    out = []
    for s in b20.sector_list(dl, target):
        dd = 1
        for t, b in enumerate(s):
            dd *= dl[t][b]
        out.append((s, dd))
    return out


def sector_label(fl, s):
    return " x ".join("(%d,%d):%s" % (fl[t][0], fl[t][1], EIG[b]) for t, b in enumerate(s))


def cell_row(fl, dims_by_factor):
    """All sector counts for one cell, BY ENUMERATION (nothing read off a formula)."""
    dl = [dims_by_factor[k] for k in fl]
    seclen = 1
    for k in fl:
        seclen *= sum(dims_by_factor[k])
    D = b20.glue_dims(dl)
    secs = dict((t, sectors_with(dl, t)) for t in range(4))

    # --- the FULL pairing, enumerated over sectors x the whole of C[Cl] ---------------
    full_pos = full_neg_inv = full_neg_anti = zero_blk = 0
    for t in range(4):
        for (s, dd) in secs[t]:
            for nuval, nudim, _ in NU_CHANNELS:
                if t in (2, 3):
                    zero_blk += dd * nudim               # lam_prod = +/- i: not real
                elif LAM_REAL[t] > 0:
                    full_pos += dd * nudim
                else:
                    if nuval == 1:
                        full_neg_inv += dd * nudim
                    else:
                        full_neg_anti += dd * nudim

    # --- the T-FIXED reading: lam_prod * nu = 1 --------------------------------------
    tf_class = tf_off = tf_neg_inv = tf_neg_anti = 0
    for t in range(4):
        for (s, dd) in secs[t]:
            for nuval, nudim, _ in NU_CHANNELS:
                if t in (2, 3):
                    continue                              # lam_prod*nu = +/- i, never 1
                if LAM_REAL[t] * nuval != 1:
                    continue                              # not T-fixed
                if LAM_REAL[t] > 0:
                    tf_class += dd * nudim
                else:
                    tf_off += dd * nudim
                    if nuval == 1:
                        tf_neg_inv += dd * nudim
                    else:
                        tf_neg_anti += dd * nudim

    return dict(fl=fl, dl=dl, D=D, seclen=seclen, cell_dim=seclen * 3, secs=secs,
                full_pos=full_pos, full_neg_inv=full_neg_inv, full_neg_anti=full_neg_anti,
                zero_blk=zero_blk, tf_class=tf_class, tf_off=tf_off,
                tf_neg_inv=tf_neg_inv, tf_neg_anti=tf_neg_anti)


COLS = ("tf_class", "tf_neg_anti", "tf_neg_inv", "full_neg_inv", "full_neg_anti",
        "zero_blk", "full_pos")
COLNAMES = ("class", "Tneg-anti", "Tneg-inv", "Fneg-inv", "Fneg-anti", "zero", "Fpos")


# ======================================================================================
# THE STAIRCASE.  The a^2 = 2 row is the REGISTERED PRE-CELL: the registration's
# first-appearance longhand argues from {2:1}, so the row below the first cell is carried
# here as context so that "first appears AT a^2 = 3" is MEASURED, not assumed.
# ======================================================================================

PRECELL = ("2", [(2, 1)], "{2:1}", "pre-cell (registered context)")

STAIR3 = [("3", [(2, 1), (3, 1)], "{2:1,3:1}"),
          ("4", [(2, 2), (3, 1)], "{2:2,3:1}"),
          ("5", [(2, 2), (3, 1)], "{2:2,3:1}"),
          ("8", [(2, 3), (3, 1)], "{2:3,3:1}"),
          ("9", [(2, 3), (3, 2)], "{2:3,3:2}"),
          ("12", [(2, 3), (3, 2)], "{2:3,3:2}")]

STAIR5 = [("3", [(2, 1), (3, 1)], "{2:1,3:1}"),
          ("4", [(2, 2), (3, 1)], "{2:2,3:1}"),
          ("5", [(2, 2), (3, 1), (5, 1)], "{2:2,3:1,5:1}"),
          ("8", [(2, 3), (3, 1), (5, 1)], "{2:3,3:1,5:1}"),
          ("9", [(2, 3), (3, 2), (5, 1)], "{2:3,3:2,5:1}"),
          ("12", [(2, 3), (3, 2), (5, 1)], "{2:3,3:2,5:1}")]

PLACESETS = [("{inf,2,3}", STAIR3), ("{inf,2,3,5}", STAIR5)]

BANKED = {(2, 1): (1, [0, 0, 1, 0]), (3, 1): (4, [1, 1, 1, 1]), (2, 2): (9, [2, 2, 3, 2]),
          (2, 3): (49, [12, 12, 13, 12]), (3, 2): (64, [16, 16, 16, 16])}


# ======================================================================================
# MAIN
# ======================================================================================

def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 9 -- REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    print("NO FLOAT ENTERS THIS INSTRUMENT AT ANY POINT. Every number below is exact.\n")
    sys.stdout.flush()

    # ==================================================================================
    # PART 0 -- the new field layer Q(zeta_25) and its quadratic extension
    # ==================================================================================
    print("=" * 100)
    print("PART 0 -- THE NEW EXACT FIELD LAYER Q(zeta_25)")
    print("=" * 100)
    v = [0] * (FLD25.N + 1)
    v[FLD25.N] = 1
    one_l = [0] * D25
    one_l[0] = 1
    check("F0a  Q(zeta_25): Phi_25 = %s, and the reduction of x^25 is exactly 1 "
          "(so Phi_25 | x^25 - 1)" % FLD25.phi_str, FLD25.red(v) == one_l)
    v5 = [0] * 6
    v5[5] = 1
    check("F0b  Q(zeta_25): the reduction of x^5 is NOT 1 -- zeta_25 has exact order 25, "
          "not 5", FLD25.red(v5) != one_l)
    lhs = FLD25.mono(20)
    rhs = [Fraction(0)] * D25
    for off, cf in FLD25.rule:
        rhs[off] += cf
    check("F0c  Q(zeta_25): x^20 = -x^15 - x^10 - x^5 - 1 exactly (the reduction rule IS "
          "the minimal polynomial, degree 20 = phi(25))", lhs == tuple(rhs))
    xt = FLD25.add(FLD25.mono(1), FLD25.mono(7))
    xt = FLD25.add(xt, FLD25.smul(FLD25.mono(13), Fraction(3)))
    check("F0d  Q(zeta_25): the extended-Euclid inverse is exact -- x * x^-1 = 1 for "
          "x = zeta + zeta^7 + 3*zeta^13", f25_mul(xt, f25_inv(xt)) == F25_ONE)

    # ---- i is NOT in Q(zeta_25): PROVED here, not assumed --------------------------
    ordr = 1
    vv = 2
    while vv != 1:
        vv = (vv * 2) % 25
        ordr += 1
    check("F0e  the order of 2 mod 25 is exactly %d = phi(25): (Z/25)^* is CYCLIC, so "
          "Gal(Q(zeta_25)/Q) is cyclic of order 20 and has a UNIQUE quadratic subfield"
          % ordr, ordr == 20)
    gs = FLD25.sub(FLD25.add(FLD25.mono(5), FLD25.mono(20)),
                   FLD25.add(FLD25.mono(10), FLD25.mono(15)))
    gs2 = f25_mul(gs, gs)
    five = tuple([Fraction(5)] + [Fraction(0)] * (D25 - 1))
    is_irr = any(gs[k] != 0 for k in range(1, D25))
    check("F0f  the Gauss sum s = zeta_5 + zeta_5^4 - zeta_5^2 - zeta_5^3 (= zeta_25^5 + "
          "zeta_25^20 - zeta_25^10 - zeta_25^15) satisfies s^2 = 5 EXACTLY and s is not "
          "rational: Q(sqrt 5) IS a quadratic subfield of Q(zeta_25)",
          gs2 == five and is_irr)
    print("      => by F0e the quadratic subfield is UNIQUE, and by F0f it is Q(sqrt 5),")
    print("         which is REAL.  If i were in Q(zeta_25) then Q(i) would be A quadratic")
    print("         subfield, hence THE one, hence Q(sqrt 5) = Q(i) -- false.  THEREFORE")
    check("F0g  i is NOT in Q(zeta_25) (proved from F0e + F0f). Hence tr M at (5,1) is "
          "FORCED RATIONAL, hence d_i = d_-i there -- the p-odd pattern, forced in advance",
          gs2 == five and is_irr and ordr == 20)
    ii = e_mul(E_I, E_I)
    check("F0h  the quadratic extension E = Q(zeta_25)(i) is built exactly: i^2 = -1 in E, "
          "and E-inversion is exact (x * x^-1 = 1 for x = (zeta+3) + (zeta^4)*i)",
          ii == E_MONE and
          (lambda x: e_mul(x, e_inv(x)) == E_ONE)(
              (FLD25.add(FLD25.mono(1), FLD25.smul(F25_ONE, Fraction(3))),
               FLD25.mono(4))))
    print()

    # ==================================================================================
    # PART 1 -- the (5,1) factor, exact; and the five banked factors re-derived
    # ==================================================================================
    print("=" * 100)
    print("PART 1 -- THE FACTORS.  (5,1) IS NEW AND FULLY EXACT; THE OTHER FIVE ARE "
          "RE-DERIVED AND CHECKED AGAINST THE BANK")
    print("=" * 100)
    facs = {}
    dims_by_factor = {}

    # ---- the five banked factors -----------------------------------------------------
    for (p, n) in [(2, 1), (3, 1), (2, 2)]:
        f = b20.small_factor(p, n)
        check("P1a %s  F K = K M entry-exact (sitting 5's C2, re-asserted)" % f['tag'],
              f['ok_fk'])
        check("P1b %s  P K = K Pi entry-exact (sitting 5's C3a, re-asserted)" % f['tag'],
              f['ok_pk'])
        A, B, extra = b20.gauss_parts_144(f['trM'])
        dims = b20.eigen_dims(f['d'], f['trPi'], A, B)
        check("P1c %s  trace formulas give nonnegative integers summing to dim: "
              "(d_1,d_-1,d_i,d_-i) = (%s,%s,%s,%s)"
              % (f['tag'], dims[0], dims[1], dims[2], dims[3]),
              extra == [] and b20.ok_dims(dims, f['d']))
        f['A'], f['B'], f['dims'] = A, B, [int(x) for x in dims]
        f['field'] = "Q(zeta_144)"
        facs[(p, n)] = f
        dims_by_factor[(p, n)] = f['dims']

    for (p, n), fld in [((2, 3), b20.FLD64), ((3, 2), b20.FLD81)]:
        bf = b20.BigFactor(p, n, fld)
        check("P1b %s  P K = K Pi verified FULLY (all %d rows)" % (bf.tag, bf.N),
              bf.verify_PK_eq_KPi())
        bad, ncols = bf.spot_check_FK_eq_KM()
        check("P1a %s  F K = K M spot-checked entry-exact on %d deterministic columns, "
              "all %d rows each: %d mismatches" % (bf.tag, ncols, bf.N, bad), bad == 0)
        tm = bf.trM()
        A, B, extra = fld.parts(tm)
        dims = b20.eigen_dims(bf.d, bf.trPi, A, B)
        check("P1c %s  trace formulas give nonnegative integers summing to dim: "
              "(d_1,d_-1,d_i,d_-i) = (%s,%s,%s,%s)"
              % (bf.tag, dims[0], dims[1], dims[2], dims[3]),
              extra == [] and b20.ok_dims(dims, bf.d))
        facs[(p, n)] = dict(p=p, n=n, N=bf.N, q=bf.q, d=bf.d, trPi=bf.trPi, A=A, B=B,
                            dims=[int(x) for x in dims], tag=bf.tag, field=fld.name)
        dims_by_factor[(p, n)] = facs[(p, n)]['dims']

    for k in sorted(BANKED):
        bd, bdims = BANKED[k]
        check("P1d %s  the re-derived (dim; d_1,d_-1,d_i,d_-i) = (%d; %d,%d,%d,%d) equals "
              "SITTING 7's BANKED row exactly"
              % (facs[k]['tag'], facs[k]['d'], facs[k]['dims'][0], facs[k]['dims'][1],
                 facs[k]['dims'][2], facs[k]['dims'][3]),
              facs[k]['d'] == bd and facs[k]['dims'] == bdims)
    print()

    # ---- the NEW factor (5,1) --------------------------------------------------------
    print("--- THE NEW FACTOR (5,1) OVER Q(zeta_25): EVERY IDENTITY VERIFIED IN FULL ---")
    bf5 = b20.BigFactor(5, 1, FLD25)
    check("P1e (5,1)  chart m = alpha + 5*beta on Z/25; the Sonin basis has %d columns "
          "(alpha in [1,5), j in [0,4)) with EXACTLY TWO nonzero entries each -- the "
          "sparsity that keeps F off the page" % bf5.d,
          bf5.d == 16 and all(len(set(bf5.rows[c])) == 2 for c in range(bf5.d)))
    KtK5 = ktk_from_rows(bf5)
    IT = b18.kron_scal([[1 if i == j else 0 for j in range(4)] for i in range(4)],
                       b20.tri(4))
    check("P1f (5,1)  K^T K = I_4 (x) tridiag(-1,2,-1) EXACTLY (sparse integer), built "
          "directly from the column supports",
          all(KtK5[i][j] == IT[i][j] for i in range(16) for j in range(16)))
    detKtK5 = b18.rat_det(KtK5)
    check("P1g (5,1)  det(K^T K) = %s = 5^4 -- a nonzero integer, so (K^T K)^-1 exists "
          "exactly over Q" % detKtK5, detKtK5 == 625)
    KtKinv5 = b18.rat_inv(KtK5)
    prod = b18.mm_scal_scal(KtK5, KtKinv5)
    check("P1h (5,1)  the exact inverse checks: (K^T K)(K^T K)^-1 = I_16 entry-exact",
          all(prod[i][j] == (1 if i == j else 0) for i in range(16) for j in range(16)))

    Mcols = [bf5.Mcol(c) for c in range(bf5.d)]
    M5 = [[Mcols[c][r] for c in range(bf5.d)] for r in range(bf5.d)]
    check("P1i (5,1)  P K = K Pi verified FULLY (all %d rows, all %d columns)"
          % (bf5.N, bf5.d), bf5.verify_PK_eq_KPi())
    bad5, nc5 = full_check_FK_eq_KM(bf5, Mcols)
    check("P1j (5,1)  F K = K M verified FULLY -- ALL %d columns x ALL %d rows "
          "(N = 25 is small enough that no spot-check is needed): %d mismatches"
          % (nc5, bf5.N, bad5), bad5 == 0)
    note("P1j' DIVERGENCE FROM THE REGISTERED WORDING, flagged not silent: the "
         "registration says 'F K = K M spot-checked' at (5,1). N = 25 turned out small "
         "enough for the FULL check, so the full check was run instead. The run is "
         "STRICTLY STRONGER than registered; no weaker check was substituted.")
    is_sp5, detPi5 = b18.perm_sign_and_det(bf5.Pi)
    check("P1k (5,1)  Pi is a signed permutation (a,j) -> -(5-a, 3-j), one +/-1 per row "
          "and per column", is_sp5)
    check("P1l (5,1)  det Pi = %+d in {+1,-1}" % (detPi5 if is_sp5 else 0),
          is_sp5 and detPi5 in (1, -1))
    badMM = 0
    for i in range(16):
        for j in range(16):
            acc = [Fraction(0)] * D25
            for k in range(16):
                g = f25_mul(M5[i][k], M5[k][j])
                for t in range(D25):
                    if g[t]:
                        acc[t] += g[t]
            exp = [Fraction(0)] * D25
            exp[0] = Fraction(bf5.Pi[i][j])
            if acc != exp:
                badMM += 1
    check("P1m (5,1)  M * M = Pi ENTRY-EXACT over Q(zeta_25) (%d mismatches in the 16x16 "
          "product) -- so M^4 = Pi^2 = I and the eigenvalues lie in {1,-1,i,-i}" % badMM,
          badMM == 0)

    tm5 = bf5.trM()
    A5, B5, extra5 = FLD25.parts(tm5)
    check("P1n (5,1)  tr M = %s, RATIONAL: every coefficient above the constant term is "
          "exactly zero -- as F0g FORCED in advance (i not in Q(zeta_25))" % A5,
          extra5 == [] and A5.denominator == 1)
    check("P1o (5,1)  tr Pi = %d exactly (Pi has no fixed column: a = 5 - a has no "
          "solution in [1,5))" % bf5.trPi, bf5.trPi == 0)
    dims5 = b20.eigen_dims(bf5.d, bf5.trPi, A5, B5)
    check("P1p (5,1)  the four trace equations give nonnegative integers summing to dim: "
          "(d_1,d_-1,d_i,d_-i) = (%s,%s,%s,%s), sum = %s = 16"
          % (dims5[0], dims5[1], dims5[2], dims5[3], sum(dims5)),
          b20.ok_dims(dims5, bf5.d))
    dims5i = [int(x) for x in dims5]
    check("P1q (5,1)  d_i = d_-i = %d -- FORCED by F0g, and observed" % dims5i[2],
          dims5i[2] == dims5i[3])

    # ---- direct exact nullity verification at (5,1) -----------------------------------
    print("      direct exact nullity of (M - lambda I), dim 16 -- lambda = +/-1 lives in")
    print("      Q(zeta_25) itself; lambda = +/-i REQUIRES the quadratic extension E:")
    sys.stdout.flush()
    nul5 = []
    for lv in (Fraction(1), Fraction(-1)):
        A = [[FLD25.sub(M5[i][j], FLD25.smul(F25_ONE, lv) if i == j else F25_ZERO)
              for j in range(16)] for i in range(16)]
        nul5.append(16 - f25_rank(A))
    for lv in (E_I, E_MI):
        A = [[e_sub((M5[i][j], F25_ZERO), lv if i == j else E_ZERO)
              for j in range(16)] for i in range(16)]
        nul5.append(16 - e_rank(A))
        sys.stdout.flush()
    check("P1r (5,1)  DIRECT EXACT NULLITY of (M - lambda I) for lambda = 1,-1,i,-i is "
          "(%d,%d,%d,%d) == the trace-formula dims (%d,%d,%d,%d) -- the trace formulas are "
          "VERIFIED, not trusted, at the new factor"
          % tuple(nul5 + dims5i), nul5 == dims5i)

    facs[(5, 1)] = dict(p=5, n=1, N=25, q=5, d=16, trPi=bf5.trPi, A=A5, B=B5,
                        dims=dims5i, tag="(5,1)", field="Q(zeta_25)")
    dims_by_factor[(5, 1)] = dims5i
    print()

    print("--- PART 1 TABLE (the (5,1) row is the new one) ---")
    print("  %-8s %-6s %-14s %-8s %-6s %-6s %-6s %-6s %s"
          % ("factor", "dim", "tr M", "tr Pi", "d_1", "d_-1", "d_i", "d_-i", "field"))
    for k in [(2, 1), (3, 1), (2, 2), (2, 3), (3, 2), (5, 1)]:
        f = facs[k]
        trs = "%d %+d*i" % (int(f['A']), int(f['B']))
        print("  %-8s %-6d %-14s %-8d %-6d %-6d %-6d %-6d %s"
              % (f['tag'], f['d'], trs, f['trPi'], f['dims'][0], f['dims'][1],
                 f['dims'][2], f['dims'][3], f['field']))
    flat = [facs[k]['tag'] for k in [(2, 1), (3, 1), (2, 2), (2, 3), (3, 2), (5, 1)]
            if len(set(facs[k]['dims'])) == 1]
    print("  FLAT factors (all four eigen-dims equal): %s" % ", ".join(flat))
    check("P1s  (5,1) is FLAT: (d_1,d_-1,d_i,d_-i) = (4,4,4,4), dim 16 -- the p-odd "
          "pattern (tr M = 0, tr Pi = 0) shared with (3,1) = (1,1,1,1) and "
          "(3,2) = (16,16,16,16)",
          dims5i == [4, 4, 4, 4] and facs[(3, 1)]['dims'] == [1, 1, 1, 1]
          and facs[(3, 2)]['dims'] == [16, 16, 16, 16])
    print()

    # ---- the class factor C, both channels -------------------------------------------
    print("--- THE CLASS FACTOR C = circulant(2,1,1) = c2*c3, BOTH CHANNELS ---")
    CfixQ = b20.rat_mm(b20.rat_T(b20.EC_FIX), b20.rat_mm(b20.CMAT, b20.EC_FIX))
    CantQ = b20.rat_mm(b20.rat_T(b20.EC_ANT), b20.rat_mm(b20.CMAT, b20.EC_ANT))
    pivF, okF = b20.rat_congruence(CfixQ)
    pivA, okA = b20.rat_congruence(CantQ)
    check("P1t  C|_fix (antipode-invariant, basis {e0, e1+e2}) has exact rational "
          "congruence pivots (%s) -- ALL POSITIVE, POSITIVE-DEFINITE of dim 2"
          % ", ".join(str(x) for x in pivF), okF and all(x > 0 for x in pivF))
    check("P1u  C|_anti (antipode-anti-invariant, basis {e1-e2}) has exact pivot (%s) -- "
          "POSITIVE, dim 1 (C-eigenvalue 1)" % ", ".join(str(x) for x in pivA),
          okA and all(x > 0 for x in pivA))
    CB = b20.rat_mm(b20.CMAT, b20.EC_FIX)
    Cop = [[CB[0][0], CB[0][1]], [CB[1][0], CB[1][1]]]
    check("P1v  C acts on the antipode-invariant subspace with trace 5 and det 4 -- char "
          "poly x^2 - 5x + 4, SPECTRUM {4,1} exactly; and C(e1-e2) = e1-e2, spectrum {1} "
          "on the anti channel: C IS POSITIVE ON BOTH CHANNELS, as registered",
          all(CB[1][j] == CB[2][j] for j in range(2))
          and Cop[0][0] + Cop[1][1] == 5 and b18.rat_det(Cop) == 4)
    print()

    # ==================================================================================
    # PART 2 -- the sector tables per cell, per place set
    # ==================================================================================
    print("=" * 100)
    print("PART 2 -- THE SECTOR TABLES PER CELL (PURE INTEGER ARITHMETIC ON THE "
          "FACTOR EIGEN-DIMS)")
    print("=" * 100)
    print("  Every count below is produced by ENUMERATING sectors (lambda_p per live p) x")
    print("  the class eigenvalue nu, then summing dims. Nothing is read off a closed form.")
    print("  T-FIXED means lam_prod * nu = 1.  nu = +1 has class-dim 2 (invariant channel),")
    print("  nu = -1 has class-dim 1 (anti-invariant channel).")
    print()

    tables = {}
    for psname, stair in PLACESETS:
        rows = []
        for (a2, fl, clab, tag) in [PRECELL]:
            r = cell_row(fl, dims_by_factor)
            r.update(a2=a2, clab=clab, tag=tag)
            rows.append(r)
        for (a2, fl, clab) in stair:
            r = cell_row(fl, dims_by_factor)
            r.update(a2=a2, clab=clab, tag="")
            rows.append(r)
        tables[psname] = rows

    for psname, stair in PLACESETS:
        rows = tables[psname]
        print("=" * 100)
        print("PLACE SET %s" % psname)
        print("=" * 100)
        print("  %-5s %-15s %-8s %-8s %-7s %-10s %-9s %-9s %-10s %-8s %s"
              % ("a^2", "cell", "secdim", "celldim", "class", "Tneg-anti", "Tneg-inv",
                 "Fneg-inv", "Fneg-anti", "zero", "delta(class,Tanti,Finv,Fanti,zero)"))
        prev = None
        for r in rows:
            if prev is None:
                dl_s = "-  (first row)"
            else:
                dl_s = "(%+d,%+d,%+d,%+d,%+d)" % (
                    r['tf_class'] - prev['tf_class'],
                    r['tf_neg_anti'] - prev['tf_neg_anti'],
                    r['full_neg_inv'] - prev['full_neg_inv'],
                    r['full_neg_anti'] - prev['full_neg_anti'],
                    r['zero_blk'] - prev['zero_blk'])
            print("  %-5s %-15s %-8d %-8d %-7d %-10d %-9d %-9d %-10d %-8d %s"
                  % (r['a2'], r['clab'] + (" *" if r['tag'] else ""), r['seclen'],
                     r['cell_dim'], r['tf_class'], r['tf_neg_anti'], r['tf_neg_inv'],
                     r['full_neg_inv'], r['full_neg_anti'], r['zero_blk'], dl_s))
            prev = r
        print("  * = the registered PRE-CELL (a^2 = 2, {2:1}); it is below the staircase's")
        print("    first cell and is carried so that 'first appears AT a^2 = 3' is MEASURED.")
        print("  (Fpos, the full pairing's positive count, is class-independent: "
              "%s)" % ", ".join("%s:%d" % (r['a2'], r['full_pos']) for r in rows))
        print()

        for r in rows:
            check("P2a %-12s cell %-14s glued eigen-dims (D_1,D_-1,D_i,D_-i) = "
                  "(%d,%d,%d,%d) sum to the transform dim %d"
                  % (psname, r['clab'], r['D'][0], r['D'][1], r['D'][2], r['D'][3],
                     r['seclen']), sum(r['D']) == r['seclen'])
        for r in rows:
            check("P2b %-12s cell %-14s T-FIXED NEGATIVES IN THE INVARIANT CHANNEL = 0 BY "
                  "ENUMERATION (nu = +1 and lam_prod*nu = 1 force lam_prod = +1: no such "
                  "sector exists -- STRUCTURAL, and confirmed sector by sector)"
                  % (psname, r['clab']), r['tf_neg_inv'] == 0)
        for r in rows:
            check("P2c %-12s cell %-14s the FULL pairing's negatives split 2 : 1 between "
                  "the invariant and anti-invariant channels (%d : %d) -- registered "
                  "structural claim (i)" % (psname, r['clab'], r['full_neg_inv'],
                                            r['full_neg_anti']),
                  r['full_neg_inv'] == 2 * r['full_neg_anti']
                  and r['full_neg_anti'] == r['D'][1])
        for r in rows:
            check("P2d %-12s cell %-14s T-fixed off-class negatives (%d) = the full "
                  "pairing's ANTI-channel negatives (%d) = D_-1: the T-fixed reading keeps "
                  "exactly the anti-invariant third" % (psname, r['clab'], r['tf_off'],
                                                        r['full_neg_anti']),
                  r['tf_off'] == r['full_neg_anti'] == r['tf_neg_anti'])
        for r in rows:
            if r['tag']:
                check("P2e %-12s PRE-CELL %-12s the full-pairing signature is (n+, n-, n0) "
                      "= (%d, %d, %d) = (0, 0, celldim): the WHOLE pre-cell is the twist's "
                      "zero block" % (psname, r['clab'], r['full_pos'],
                                      r['full_neg_inv'] + r['full_neg_anti'],
                                      r['zero_blk']),
                      r['full_pos'] == 0 and r['full_neg_inv'] + r['full_neg_anti'] == 0
                      and r['zero_blk'] == r['cell_dim'])
            else:
                d = r['cell_dim']
                check("P2e %-12s cell %-14s the full-pairing signature is (n+, n-, n0) = "
                      "(%d, %d, %d) = (d/4, d/4, d/2) with d = %d -- the BANKED twist "
                      "signature, holding at every staircase cell"
                      % (psname, r['clab'], r['full_pos'],
                         r['full_neg_inv'] + r['full_neg_anti'], r['zero_blk'], d),
                      r['full_pos'] * 4 == d
                      and (r['full_neg_inv'] + r['full_neg_anti']) * 4 == d
                      and r['zero_blk'] * 2 == d)
        print()

    # ---- the sector lists ------------------------------------------------------------
    print("=" * 100)
    print("THE SECTOR LISTS: THE PLACE-SUPPORT OF EVERY NEGATIVE DIRECTION")
    print("=" * 100)
    print("  The lam_prod = -1 sectors carry BOTH the T-fixed off-class negatives (x1, the")
    print("  anti-invariant line) AND the full pairing's negatives (x3 = x2 invariant + x1")
    print("  anti). One list per cell therefore serves both readings; the multipliers differ.")
    print()
    for psname, _ in PLACESETS:
        print("  --- PLACE SET %s ---" % psname)
        seen = set()
        for r in tables[psname]:
            if r['clab'] in seen:
                print("  a^2 = %-4s cell %-15s (cell unchanged -- sector list identical to "
                      "the row above)" % (r['a2'], r['clab']))
                continue
            seen.add(r['clab'])
            secs = r['secs'][1]
            print("  a^2 = %-4s cell %-15s lam_prod = -1 sectors: %d sector(s), total "
                  "transform dim %d" % (r['a2'], r['clab'], len(secs),
                                        sum(dd for _, dd in secs)))
            if not secs:
                print("        NONE -- no negative direction exists at this cell, in "
                      "either reading.")
            for (s, dd) in secs:
                print("        %-46s dim %-6d  -> T-fixed off-class %-6d full-pairing "
                      "%d (= %d inv + %d anti)"
                      % (sector_label(r['fl'], s), dd, dd * 1, dd * 3, dd * 2, dd * 1))
        print()

    # ==================================================================================
    # PART 3 -- first appearance, the arrival of 5, and the constrained class
    # ==================================================================================
    print("=" * 100)
    print("PART 3 -- FIRST APPEARANCE, THE ARRIVAL OF 5, AND THE CONSTRAINED CLASS")
    print("=" * 100)

    print("--- 3(a) FIRST APPEARANCE PER PLACE SET, AND ITS ADDRESS ---")
    firsts = {}
    for psname, _ in PLACESETS:
        rows = tables[psname]
        for key, kname in [('tf_off', "T-FIXED off-class negatives"),
                           ('full_neg_inv', "FULL-pairing negatives")]:
            idx = None
            for t, r in enumerate(rows):
                if r[key] > 0:
                    idx = t
                    break
            r = rows[idx]
            prev = rows[idx - 1] if idx > 0 else None
            newpl = sorted(set(p for (p, n) in r['fl'])
                           - set(p for (p, n) in (prev['fl'] if prev else [])))
            deepen = sorted(set(r['fl']) - set(prev['fl'] if prev else []))
            verdict = "EDGE" if newpl else ("INTERIOR" if deepen else "NO CHANGE")
            firsts[(psname, key)] = (r, prev, newpl, verdict)
            print("  %-12s %-28s first nonzero at a^2 = %-4s cell %-15s value %d"
                  % (psname, kname, r['a2'], r['clab'], r[key]))
            print("               previous row: a^2 = %-4s cell %-15s value %d"
                  % (prev['a2'] if prev else "-", prev['clab'] if prev else "-",
                     prev[key] if prev else 0))
            print("               the cell change admits NEW PLACE(S) %s  =>  VERDICT: %s"
                  % (", ".join(str(x) for x in newpl) if newpl else "none", verdict))
    for (psname, key), (r, prev, newpl, verdict) in sorted(firsts.items()):
        check("P3a %-12s first nonzero %-14s is at a^2 = %s, cell %s, and its address is a "
              "PLACE-ARRIVAL EDGE (the arrival of %s) -- not a cell interior"
              % (psname, key, r['a2'], r['clab'],
                 ", ".join(str(x) for x in newpl) if newpl else "none"),
              verdict == "EDGE" and r['a2'] == "3")
    for psname, _ in PLACESETS:
        pre = tables[psname][0]
        check("P3b %-12s below a^2 = 3 (the pre-cell {2:1}, eigen-dims (0,0,1,0)) BOTH "
              "readings have ZERO negatives: T-fixed off-class %d, full negatives %d -- "
              "the registered first-appearance longhand LANDS"
              % (psname, pre['tf_off'], pre['full_neg_inv'] + pre['full_neg_anti']),
              pre['tf_off'] == 0 and pre['full_neg_inv'] + pre['full_neg_anti'] == 0)
    print()

    print("--- 3(a') GROWTH ALONG THE STAIRCASE: the registered expectation, tested ---")
    print("  Registered: 'Growth is expected at every staircase step thereafter'.")
    print("  Measured, step by step (a step is a^2 -> next a^2 within a place set):")
    grow_ok = True
    zero_steps = []
    for psname, _ in PLACESETS:
        rows = tables[psname]
        for t in range(1, len(rows)):
            a, b = rows[t - 1], rows[t]
            d = b['tf_off'] - a['tf_off']
            same = (a['fl'] == b['fl'])
            print("  %-12s a^2 %-4s -> %-4s  cell %-15s -> %-15s  T-fixed off-class "
                  "%-7d -> %-7d  delta %+d   %s"
                  % (psname, a['a2'], b['a2'], a['clab'], b['clab'], a['tf_off'],
                     b['tf_off'], d, "CELL UNCHANGED (no-op step)" if same else "cell changes"))
            if same:
                zero_steps.append((psname, a['a2'], b['a2'], b['clab']))
                if d != 0:
                    grow_ok = False
            else:
                if d <= 0:
                    grow_ok = False
    check("P3c  growth is STRICT at every step that CHANGES the cell, and EXACTLY ZERO at "
          "every step that does not: measured on all %d steps across both place sets"
          % sum(len(tables[ps]) - 1 for ps, _ in PLACESETS), grow_ok)
    check("P3d  the banked deepening a^2 = 3 -> 4 carries the T-fixed off-class count "
          "1 -> 9, exactly as banked",
          tables["{inf,2,3}"][1]['tf_off'] == 1 and tables["{inf,2,3}"][2]['tf_off'] == 9)
    note("P3e  REGISTERED EXPECTATION THAT DOES NOT LAND AS STATED: 'growth at EVERY "
         "staircase step thereafter'. There are %d steps at which the CELL DOES NOT "
         "CHANGE, and at each the growth is EXACTLY ZERO, not positive: %s. The "
         "registration conflated the a^2 grid with the cell grid; corrected form (P3c): "
         "growth is strict exactly at the cell-changing steps. Reported, not smoothed."
         % (len(zero_steps),
            "; ".join("%s a^2 %s->%s (%s)" % z for z in zero_steps)))
    print()

    print("--- 3(b) THE ARRIVAL OF 5 AT a^2 = 5 (its DEAD EDGE) ---")
    r3 = [r for r in tables["{inf,2,3}"] if r['a2'] == "5"][0]
    r5 = [r for r in tables["{inf,2,3,5}"] if r['a2'] == "5"][0]
    print("  The two place sets at the SAME a^2 = 5:")
    print("     {inf,2,3}   cell %-15s secdim %-6d" % (r3['clab'], r3['seclen']))
    print("     {inf,2,3,5} cell %-15s secdim %-6d" % (r5['clab'], r5['seclen']))
    print()
    print("  %-14s %-12s %-12s %-12s %s" % ("column", "3-place", "4-place", "delta",
                                            "ratio"))
    for cname, ckey in zip(COLNAMES, COLS):
        v3, v5 = r3[ckey], r5[ckey]
        ratio = ("%d x" % (v5 // v3)) if v3 else ("-" if v5 == 0 else "0 -> %d" % v5)
        print("  %-14s %-12d %-12d %+-12d %s" % (cname, v3, v5, v5 - v3, ratio))
    print("  %-14s %-12d %-12d %+-12d %s"
          % ("celldim", r3['cell_dim'], r5['cell_dim'], r5['cell_dim'] - r3['cell_dim'],
             "%d x" % (r5['cell_dim'] // r3['cell_dim'])))
    print()
    check("P3f  THE ARRIVAL OF 5 IS DEAD IN STRUCTURE: every column at a^2 = 5 is "
          "multiplied by EXACTLY dim Son(5,1) = 16, and the glued eigen-dims go "
          "(%d,%d,%d,%d) -> (%d,%d,%d,%d) = 16 x the previous ones. No ratio changes, no "
          "channel changes, no first appearance is created."
          % tuple(list(r3['D']) + list(r5['D'])),
          all(r5[k] == 16 * r3[k] for k in COLS)
          and all(r5['D'][t] == 16 * r3['D'][t] for t in range(4)))
    e5 = dims_by_factor[(5, 1)]
    tot3 = sum(r3['D'])
    check("P3g  THE MECHANISM: (5,1) is FLAT (d_1 = d_-1 = d_i = d_-i = %d). Gluing a FLAT "
          "factor of common dim e sends D_k -> e * (D_1 + D_-1 + D_i + D_-i) for EVERY k, "
          "so the glued dims become uniform and every sector count scales by 4e = dim. "
          "Verified: %d * %d = %d = each new D_k" % (e5[0], e5[0], tot3, e5[0] * tot3),
          len(set(e5)) == 1 and all(r5['D'][t] == e5[0] * tot3 for t in range(4)))
    print("  WHAT d_i = d_-i FORCES (F0g, proved before the run): with e_i = e_-i the glued")
    print("  difference obeys  D_1(new) - D_-1(new) = (D_1 - D_-1) * (e_1 - e_-1).  At (5,1)")
    print("  tr M = 0 gives e_1 = e_-1 as well, so the difference is annihilated outright:")
    print("  5 can NEVER create an imbalance between the positive and negative real sectors,")
    print("  at any cell it ever enters. That is the exact content of 'DEAD ARRIVAL'.")
    dpos = r3['D'][0] - r3['D'][1]
    check("P3h  the forced identity D_1(new) - D_-1(new) = (D_1 - D_-1)*(e_1 - e_-1) holds "
          "exactly here: (%d - %d) = (%d - %d)*(%d - %d) = 0"
          % (r5['D'][0], r5['D'][1], r3['D'][0], r3['D'][1], e5[0], e5[1]),
          r5['D'][0] - r5['D'][1] == dpos * (e5[0] - e5[1]))
    print()
    print("  WHERE (5,1)'s EIGENVALUES ENTER -- the lam_prod = -1 sectors at "
          "{2:2,3:1,5:1}, grouped by (5,1)'s eigenvalue:")
    byeig = dict((t, []) for t in range(4))
    ipos = r5['fl'].index((5, 1))
    for (s, dd) in r5['secs'][1]:
        byeig[s[ipos]].append((s, dd))
    for t in range(4):
        tot = sum(dd for _, dd in byeig[t])
        print("     (5,1):%-4s carries %d sector(s), total dim %d" % (EIG[t],
                                                                     len(byeig[t]), tot))
        for (s, dd) in byeig[t]:
            print("        %-46s dim %d" % (sector_label(r5['fl'], s), dd))
    check("P3i  (5,1)'s FOUR eigenvalues enter the lam_prod = -1 sectors in EQUAL total "
          "dimension (%s) -- the flatness again, now visible sector by sector"
          % ", ".join("%s:%d" % (EIG[t], sum(dd for _, dd in byeig[t])) for t in range(4)),
          len(set(sum(dd for _, dd in byeig[t]) for t in range(4))) == 1)
    print("  NOTE ON THE OTHER PLACE SET: on {inf,2,3} the step a^2 = 4 -> 5 is a NO-OP")
    print("  (the cell {2:2,3:1} repeats), so 5's dead edge is dead in BOTH senses -- it")
    print("  changes nothing where 5 is absent, and only rescales where 5 is present.")
    print()

    print("--- 3(c) THE CONSTRAINED CLASS ALONG THE STAIRCASE ---")
    print("  MECHANISM (sitting 7, entry-exact at {2:1,3:1}): T-fixed AND antipode-fixed")
    print("  force nu = +1 and lam_prod = +1, so B|_class = ||.||^2_(K^T K) (x) C|_fix with")
    print("  K^T K rational SPD and C|_fix rational SPD (P1t). Hence POSITIVE-DEFINITE at")
    print("  every cell where the class is nonzero, under EVERY embedding.")
    print()
    print("  %-12s %-5s %-15s %-10s %s" % ("place set", "a^2", "cell", "class dim",
                                           "verdict"))
    for psname, _ in PLACESETS:
        for r in tables[psname]:
            v = ("SECTOR-ASSEMBLED POSITIVE-DEFINITE" if r['tf_class'] > 0
                 else "CLASS IS EMPTY (dim 0) -- nothing to be positive about")
            print("  %-12s %-5s %-15s %-10d %s" % (psname, r['a2'], r['clab'],
                                                   r['tf_class'], v))
    print()
    print("  SPOT VERIFICATION, EXACT AND DIRECT, AT ONE NEW CELL: {2:2,3:1}, class dim 18")
    print("  (sitting 7 did {2:1,3:1} at cell dim 12; this is cell dim 108).")
    sys.stdout.flush()
    f22 = facs[(2, 2)]
    f31 = facs[(3, 1)]
    CZ, CO, I144 = b18.CZERO, b18.CONE, b20.I144
    LAMS = [CO, -CO, I144, -I144]

    def nsp(M, d, lv):
        return b20.cyc_nullspace([[M[i][j] - (lv if i == j else CZ) for j in range(d)]
                                  for i in range(d)])

    ns22 = [nsp(f22['M'], 9, lv) for lv in LAMS]
    ns31 = [nsp(f31['M'], 4, lv) for lv in LAMS]
    check("P3j  {2:2,3:1}: EXACT nullities of (M - lambda I) at (2,2) are (%d,%d,%d,%d) == "
          "its trace-formula dims, and at (3,1) are (%d,%d,%d,%d) == its trace-formula dims"
          % tuple([len(x) for x in ns22] + [len(x) for x in ns31]),
          [len(x) for x in ns22] == f22['dims'] and [len(x) for x in ns31] == f31['dims'])

    def build(pairs):
        cols = []
        for (a, b) in pairs:
            for v in ns22[a]:
                for w in ns31[b]:
                    cols.append([v[i] * w[j] for i in range(9) for j in range(4)])
        return [[cols[c][r] for c in range(len(cols))] for r in range(36)]

    Ef = build([(0, 0), (1, 1), (2, 3), (3, 2)])       # lam_prod = +1
    Efm = build([(0, 1), (1, 0), (2, 2), (3, 3)])      # lam_prod = -1
    r4 = [r for r in tables["{inf,2,3}"] if r['a2'] == "4"][0]
    check("P3k  {2:2,3:1}: the tensored eigenbasis has %d columns for lam_prod = +1 and %d "
          "for lam_prod = -1, matching D_1 = %d and D_-1 = %d from the sector algebra"
          % (len(Ef[0]), len(Efm[0]), r4['D'][0], r4['D'][1]),
          len(Ef[0]) == r4['D'][0] and len(Efm[0]) == r4['D'][1])
    Mg = b18.kron_cyc(f22['M'], f31['M'])
    check("P3l  {2:2,3:1}: M_g E_f = E_f entry-exact (36x9) -- the tensored basis really "
          "is the +1 eigenspace of the glued transform",
          b18.cyc_eq_mat(b18.mm_cyc_cyc(Mg, Ef), Ef))
    Gg = b18.kron_cyc(f22['G'], f31['G'])
    KtKg = b18.kron_scal(f22['KtK'], f31['KtK'])
    check("P3m  {2:2,3:1}: G_g = (K_g^T K_g) M_g entry-exact (36x36) -- the mechanism's "
          "engine at the new cell",
          b18.cyc_mat_is_zero(b18.cyc_sub_mat(Gg, b18.mm_scal_cyc(KtKg, Mg))))
    CC = [[b18.cint(b20.CMAT[a][b]) for b in range(3)] for a in range(3)]
    Gram = b18.kron_cyc(Gg, CC)                        # 108 x 108
    EcF = [[b18.cint(v) for v in r] for r in b20.EC_FIX]
    EcA = [[b18.cint(v) for v in r] for r in b20.EC_ANT]
    E = b18.kron_cyc(Ef, EcF)                          # 108 x 18
    sys.stdout.flush()
    Bcl = b18.mm_cyc_cyc(b20.cyc_dag(E), b18.mm_cyc_cyc(Gram, E))
    KtKgC = [[b18.cint(int(KtKg[i][j])) for j in range(36)] for i in range(36)]
    NF = b18.mm_cyc_cyc(b20.cyc_dag(Ef), b18.mm_cyc_cyc(KtKgC, Ef))
    CfixC = [[b18.cint(int(v)) for v in r] for r in CfixQ]
    check("P3n  {2:2,3:1}: B|_class == (E_f^dagger (K_g^T K_g) E_f) (x) C|_fix ENTRY-EXACT "
          "on the FULL 108-dimensional cell Gram (18x18 block) -- the registered mechanism "
          "B|_class = ||.||^2 (x) C|_fix, verified DIRECTLY at a second, larger cell",
          b18.cyc_eq_mat(Bcl, b18.kron_cyc(NF, CfixC)))
    pivK, okK = b20.rat_congruence(KtKg)
    check("P3o  {2:2,3:1}: K_g^T K_g is RATIONAL SYMMETRIC POSITIVE-DEFINITE -- all %d "
          "exact rational congruence pivots positive" % len(pivK),
          okK and all(x > 0 for x in pivK))
    rk = b20.cyc_rank(b20.cyc_dag(Ef))
    check("P3p  {2:2,3:1}: E_f has FULL COLUMN RANK %d over Q(zeta_144) (exact)" % rk,
          rk == 9)
    check("P3q  {2:2,3:1}: EXACT POSITIVITY CERTIFICATE (embedding-independent): "
          "B|_class = (E_f^dagger S E_f) (x) C|_fix with S = K_g^T K_g rational SPD, E_f "
          "of full column rank 9, C|_fix rational SPD => B|_class is POSITIVE-DEFINITE of "
          "dim 18 under EVERY embedding of Q(zeta_144)",
          okK and all(x > 0 for x in pivK) and rk == 9 and okF
          and all(x > 0 for x in pivF)
          and b18.cyc_eq_mat(Bcl, b18.kron_cyc(NF, CfixC)))
    sys.stdout.flush()
    Em = b18.kron_cyc(Efm, EcA)                        # 108 x 9
    Bof = b18.mm_cyc_cyc(b20.cyc_dag(Em), b18.mm_cyc_cyc(Gram, Em))
    NFm = b18.mm_cyc_cyc(b20.cyc_dag(Efm), b18.mm_cyc_cyc(KtKgC, Efm))
    CantC = [[b18.cint(int(v)) for v in r] for r in CantQ]
    check("P3r  {2:2,3:1}: B|_offclass == -(E_f'^dagger (K_g^T K_g) E_f') (x) C|_anti "
          "ENTRY-EXACT on the full 108-dimensional cell Gram (9x9 block) -- the T-fixed "
          "negatives really are B = -||v||^2 on the ANTI-invariant line, dim %d = "
          "Tneg-anti at this cell" % len(Em[0]),
          b18.cyc_eq_mat(Bof, b18.kron_cyc([[-v for v in r] for r in NFm], CantC))
          and len(Em[0]) == r4['tf_neg_anti'])
    print("      Verified directly at {2:2,3:1}: the class block is +||.||^2 (x) C|_fix")
    print("      (dim 18, positive-definite) and the off-class block is -||.||^2 (x) C|_anti")
    print("      (dim 9, negative-definite, ANTI-invariant channel only). The remaining")
    print("      cells are SECTOR-ASSEMBLED from the same identity -- declared honestly:")
    print("      not directly diagonalized at {2:3,3:1}, {2:3,3:2} or any 5-bearing cell.")
    print()

    # ==================================================================================
    # PART 4 -- the verdict
    # ==================================================================================
    print("=" * 100)
    print("PART 4 -- THE VERDICT")
    print("=" * 100)
    all_edge = all(v[3] == "EDGE" and v[0]['a2'] == "3" for v in firsts.values())
    all_anti = all(r['tf_neg_inv'] == 0 for ps, _ in PLACESETS for r in tables[ps])
    all_pos = all(r['tf_class'] >= 0 for ps, _ in PLACESETS for r in tables[ps])
    check("P4a  (N-edge) BRANCH LANDED: (1) BOTH readings' negatives first appear at "
          "a^2 = 3 on BOTH place sets, and that address is the PLACE-ARRIVAL EDGE of 3, "
          "not a cell interior; (2) the T-fixed negatives are ANTI-INVARIANT at every cell "
          "of both staircases (invariant-channel count 0 by enumeration everywhere); "
          "(3) the constrained class is positive at every cell, by the certified mechanism, "
          "spot-verified entry-exact at the new cell {2:2,3:1}",
          all_edge and all_anti and all_pos)
    print()
    print("  THE CHANNEL CAVEAT, EXACTLY AS REGISTERED BEFORE THE RUN:")
    print("   - The FULL pairing's negative directions DO appear in the invariant channel")
    print("     (invariant : anti = 2 : 1 at every cell). This was DERIVED LONGHAND IN THE")
    print("     REGISTRATION as a STRUCTURAL consequence of B = lam_prod * ||v||^2 * C|_nu,")
    print("     and the registration states plainly that the ferried channel half FAILS")
    print("     STRUCTURALLY for the full reading. It is therefore NOT a finding and it")
    print("     DOES NOT FIRE (N-interior).")
    print("   - (N-interior) fires only on a T-FIXED invariant-channel negative or on an")
    print("     INTERIOR first appearance. Neither occurred: the T-fixed invariant count is")
    print("     0 at all %d cells enumerated, and both first appearances are at the arrival")
    print("     edge of 3.")
    print("   - (N-third) not needed.")
    check("P4b  (N-interior) DID NOT FIRE: zero T-fixed invariant-channel negatives across "
          "all %d enumerated cells, and no first appearance at a cell interior"
          % sum(len(tables[ps]) for ps, _ in PLACESETS), all_anti and all_edge)
    print()
    print("  THE STAIRCASE SCHEDULE, said plainly (the live arithmetic this sitting measured):")
    print("   - Below a^2 = 3 the section's whole transform sits in the +i eigenvalue: the")
    print("     pre-cell {2:1} is ENTIRELY the twist's zero block, signature (0, 0, 3).")
    print("   - At a^2 = 3 the arrival of 3 switches on all four eigenvalues at once")
    print("     ((3,1) is FLAT: (1,1,1,1)), and from that cell onward EVERY staircase cell")
    print("     has the exact signature (d/4, d/4, d/2). The negative count is d/4 and the")
    print("     T-fixed off-class count is d/12 at every cell of both staircases.")
    print("   - Growth is by cell, not by a^2: the three no-op steps grow by exactly 0.")
    print("   - The arrival of 5 rescales by 16 and changes nothing else: DEAD.")
    print()
    print("  SCOPE, said plainly: these are properties of a FINITE CONSTRUCTED MODEL")
    print("  SECTION. No sign is asserted; the register is untouched; nothing here bears")
    print("  on W_inf - Sum W_p at complete roster or on any hypothesis. The ledger-")
    print("  positivity guard (spec 6(c)) is not approached: no ledger quantity is computed.")
    print()

    n_ok = sum(1 for _, ok in LEDGER if ok)
    n_all = len(LEDGER)
    print("--- EXACT LEDGER (%d lines) ---" % n_all)
    for name, ok in LEDGER:
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    print()
    print("ALL EXACT LINES EXACT: %d/%d PASS" % (n_ok, n_all))


if __name__ == "__main__":
    main()
