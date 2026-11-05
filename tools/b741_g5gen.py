# -*- coding: utf-8 -*-
"""scratch: the (c7) certificate. Mirrors the Lean definitions of Sums.lean / GammaVal.lean in exact Fractions, checks every side
condition the kernel will decide, and writes Centre.lean (G5). args: out_path"""
import math
import sys
from fractions import Fraction as F

GRID = 10 ** 26


def qadd(p, q): return (p[0] + q[0], p[1] + q[1])
def qsub(p, q): return (p[0] - q[0], p[1] - q[1])
def qmul(p, q): return (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])
def qscale(s, p): return (s * p[0], s * p[1])
def qn(p): return abs(p[0]) + abs(p[1])


def qpow(p, n):
    r = (F(1), F(0))
    for _ in range(n):
        r = qmul(r, p)
    return r


def qexpS(p, N):
    s = (F(0), F(0))
    for n in range(N):
        s = qadd(s, qscale(F(1, math.factorial(n)), qpow(p, n)))
    return s


def sReIm(r, wr, wi, n):
    a, b = F(0), F(0)
    for k in range(n):
        t = (-r) ** k / math.factorial(k)
        D = (wr + k) ** 2 + wi ** 2
        a += t * ((wr + k) / D)
        b -= t * (wi / D)
    return (a, b)


def rnd(x): return F(round(x * GRID), GRID)
def rc(p): return (rnd(p[0]), rnd(p[1]))
def up(x): return F(math.ceil(x * GRID), GRID)


def lq(x):
    x = F(x)
    if x.denominator == 1:
        return '(%d : ℚ)' % x.numerator
    return '(%d / %d : ℚ)' % (x.numerator, x.denominator)


def lp(p): return '(%s, %s)' % (lq(p[0]), lq(p[1]))


# lam bounds (GammaVal.lean carries the same literals)
P_LO, P_HI = F(314159265358979323846, 10 ** 20), F(314159265358979323847, 10 ** 20)
s0 = math.isqrt(23 * 10 ** 48)
S_LO, S_HI = F(s0, 10 ** 24), F(s0 + 1, 10 ** 24)
assert S_LO ** 2 < 23 < S_HI ** 2
LAM_LO = F(math.floor(2 * P_LO / S_HI * 10 ** 22), 10 ** 22)
LAM_HI = F(math.ceil(2 * P_HI / S_LO * 10 ** 22), 10 ** 22)
assert LAM_LO * S_HI <= 2 * P_LO and LAM_HI * S_LO >= 2 * P_HI
L2 = F(287209, 414355)

WA = (F(95326, 100000), F(16290216, 1000000))
WB = (1 - WA[0], -WA[1])
SHELLS = [(1, 2, 5), (4, 2, 3), (6, 4, 3), (8, 4, 2), (9, 2, 2), (12, 4, 2), (16, 2, 1), (18, 4, 1)]  # Q, count, j
XS = {32: None, 36: None, 48: None}
TAIL = F(1, 10 ** 30) + (F(5, 10 ** 14) + F(1, 10 ** 16))
DELTA = F(6, 10 ** 13)
EPS_IG = F(1, 10 ** 19)


def nterms(X, wr, tol=F(1, 10 ** 26)):
    n = 1
    while not (2 * X <= n + 1 and 2 * X ** n / (math.factorial(n) * (wr + n)) <= tol):
        n += 1
    return n


out = []
emit = out.append
facts = {}


def half(tag, w):
    wr, wi = w
    ws = 'w%s' % tag
    # 2^w
    N = 24
    p = qscale(L2 / 16, w)
    assert qn(p) <= 1 and qn(w) <= 10 ** 10
    E = qexpS(p, N)
    R = qn(p) ** N * (F(N + 1) / (math.factorial(N) * N))
    C16 = qpow(E, 16)
    R16 = (qn(E) + R) ** 16 - qn(E) ** 16
    D = 2 * qn(w) / 10 ** 10
    c2 = rc(C16)
    tot = qn(qsub(qmul(C16, (F(1), F(0))), c2)) + qn(C16) * D + 1 * R16 + R16 * D
    r2 = up(tot)
    assert tot <= r2
    emit('theorem two_%s : inD ((2 : ℂ) ^ qc %s) %s %s :=' % (ws, ws, lp(c2), lq(r2)))
    emit('  two_cpow_encl %s %d (by norm_num) (by decide +kernel) (by decide +kernel) (by decide +kernel)\n' % (ws, N))
    # G at X
    gx = {}
    for m in XS:
        X = LAM_LO * m
        n = nterms(X, wr)
        S = sReIm(X, wr, wi, n)
        cX = rc(S)
        tot = qn(qsub(S, cX)) + 2 * X ** n / (math.factorial(n) * (wr + n)) + EPS_IG
        rX = up(tot)
        assert X >= 41 and 2 * X <= n + 1 and tot <= rX
        gx[m] = (X, cX, rX)
        emit('theorem G%d_%s : inD (Gfac (qc %s) (%s : ℚ)) %s %s :=' % (m, ws, ws, lq(X), lp(cX), lq(rX)))
        emit('  GX_encl %s (by decide +kernel) (by decide +kernel) (by decide +kernel) %d (by decide +kernel) (by decide +kernel)\n' % (ws, n))
        facts['n_X%d_%s' % (m, tag)] = n
    # shells
    parts = []
    for Q, cnt, j in SHELLS:
        rho = LAM_LO * Q
        m = 2 ** j * Q
        X, cX, rX = gx[m]
        assert X == 2 ** j * rho
        n = nterms(rho, wr)
        S = sReIm(rho, wr, wi, n)
        rL = 2 * rho ** n / (math.factorial(n) * (wr + n))
        cP = qpow(c2, j)
        rP = (qn(c2) + r2) ** j - qn(c2) ** j
        cM = qmul(cP, cX)
        rM = qn(cP) * rX + qn(cX) * rP + rP * rX
        cS = qsub(cM, S)
        rS = rM + rL
        cI = rc(cS)
        tot = qn(qsub(cS, cI)) + rS
        rI = up(tot)
        assert tot <= rI and rho > 0 and F(13, 10) <= rho
        emit('theorem I%d_%s : inD (incGamma1 (qc %s) (%s : ℚ)) %s %s := by' % (Q, ws, ws, lq(rho), lp(cI), lq(rI)))
        emit('  rw [incGamma1_split (%s_re_pos) (ρ := %s) (X := %s) (by decide +kernel) %d (by decide +kernel)]' % (ws, lq(rho), lq(X), j))
        emit('  exact inD_recentre (inD_sub\' (inD_mul\' (inD_pow two_%s %d) G%d_%s) (lowInt_encl %s (by decide +kernel) (by decide +kernel) %d'
             % (ws, j, m, ws, ws, n))
        emit('    (by decide +kernel))) (by decide +kernel)\n')
        d = Q * (LAM_HI - LAM_LO)
        assert rho - d <= Q * LAM_LO and Q * LAM_HI <= rho + d
        rT = up(rI + d * F(10, 3))
        emit('theorem T%d_%s : inD (incGamma1 (qc %s) (lam * %d)) %s %s :=' % (Q, ws, ws, Q, lp(cI), lq(rT)))
        emit('  inD_transfer %s_re_le (q := %d) (Q := %d) (ρ := %s) (d := %s) (by norm_num) (by decide +kernel) (by decide +kernel)'
             % (ws, Q, Q, lq(rho), lq(d)))
        emit('    (by decide +kernel) (by decide +kernel) I%d_%s (by decide +kernel)\n' % (Q, ws))
        parts.append((Q, cnt, cI, rT))
        facts['n_rho%d_%s' % (Q, tag)] = n
    # shellSum
    c, r = None, None
    term = None
    for Q, cnt, cI, rT in parts:
        cc, rr = qscale(F(cnt), cI), cnt * rT
        t = 'inD_nat_mul\' %d T%d_%s' % (cnt, Q, ws)
        if c is None:
            c, r, term = cc, rr, t
        else:
            c, r, term = qadd(c, cc), r + rr, 'inD_add\' (%s) (%s)' % (term, t)
    cSS = rc(c)
    tot = qn(qsub(c, cSS)) + r
    rSS = up(tot)
    emit('theorem S_%s : inD (shellSum (qc %s)) %s %s := by' % (ws, ws, lp(cSS), lq(rSS)))
    emit('  have e : shellSum (qc %s) = %s := by' % (ws, ' + '.join('((%d : ℕ) : ℂ) * incGamma1 (qc %s) (lam * %d)' % (cnt, ws, Q)
                                                                       for Q, cnt, j in SHELLS)))
    emit('    unfold shellSum')
    emit('    push_cast <;> ring')
    emit('  rw [e]')
    emit('  exact inD_recentre (%s) (by decide +kernel)\n' % term)
    emit('theorem L_%s : inD (lamM (qc %s)) %s (%s + (1 / 10 ^ 30 + (5 / 10 ^ 14 + 1 / 10 ^ 16))) :=' % (ws, ws, lp(cSS), lq(rSS)))
    emit('  inD_near S_%s (by' % ws)
    emit('    rw [show ((1 / 10 ^ 30 + (5 / 10 ^ 14 + 1 / 10 ^ 16) : ℚ) : ℝ) = 1 / 10 ^ 30 + (5 / 10 ^ 14 + 1 / 10 ^ 16) by norm_num]')
    emit('    exact lamM_sub_shellSum %s_re_le)\n' % ws)
    return cSS, rSS + TAIL


emit('''/-
SIDE-explicit-formula -- SIDEExplicitFormula/Schema/ZQ/OffZero/Centre.lean
THIS PROGRAMME'S WORK (act b741, ruling (R351)(3)(b), relay data/b741_c7_plan.txt (5) G5) -- NOT VENDORED.
SPIRAL_MAP section 7 rule 9 applies here in full: `theorem`, never `lemma`.
GENERATED by the seat's certificate script; every side condition a `ℚ` inequality or equality decided by the kernel (`decide +kernel`).

G5, (c7) AND SP3. Per half (`w = cA`, `w = 1 − cA`): `2^w` from its exponential series; `Γ(w)/X^w` at `X = 32ℓ, 36ℓ, 48ℓ` from the lower
series and the upper piece's `e^(−X)/X`; each evaluated shell at `ρ = ℓ Q` as `(2^w)^j Γ(w)/X^w − lowInt w ρ`, moved to `lam Q` by the
Lipschitz bound; the shells summed with their counts and `lamM` within G4's tail. Then `(c7)`:
`‖lamM cA + lamM (1 − cA) − 1/(cA (1 − cA))‖ ≤ 6/10^13`, and by (d8) `‖zqFn cA‖ ≤ 1/10`. A bound on one value of `zqFn` at one rational
point; this file does not locate a zero.
-/
import SIDEExplicitFormula.Schema.ZQ.OffZero.GammaVal

namespace SIDEExplicitFormula
namespace Schema
namespace ZQ
namespace OffZero
''')
for tag, w in (('A', WA), ('B', WB)):
    emit('def w%s : ℚ × ℚ := %s\n' % (tag, lp(w)))
    emit('theorem w%s_re_pos : 0 < (qc w%s).re := by\n  rw [qc_re]\n  norm_num [w%s]\n' % (tag, tag, tag))
    emit('theorem w%s_re_le : (qc w%s).re ≤ 1 := by\n  rw [qc_re]\n  norm_num [w%s]\n' % (tag, tag, tag))
cA_, rA_ = half('A', WA)
cB_, rB_ = half('B', WB)
P = qmul(WA, WB)
den = P[0] ** 2 + P[1] ** 2
TINV = (P[0] / den, -P[1] / den)
assert qmul(TINV, qmul(WA, WB)) == (1, 0)
tot = qn(qsub(qadd(cA_, cB_), TINV)) + rA_ + rB_
assert tot <= DELTA, float(tot)
emit('''def tInv : ℚ × ℚ := %s

theorem cA_eq : cA = qc wA := by
  apply Complex.ext <;> norm_num [cA, qc, wA]

theorem one_sub_cA_eq : 1 - cA = qc wB := by
  apply Complex.ext <;> norm_num [cA, qc, wB]

theorem inv_centre_eq : 1 / (cA * (1 - cA)) = qc tInv := by
  have hm : qc tInv * (qc wA * qc wB) = 1 := by
    rw [← qc_mul, ← qc_mul, show qmul tInv (qmul wA wB) = (1, 0) by decide +kernel, qc_one]
  rw [one_sub_cA_eq, cA_eq]
  exact (eq_div_of_mul_eq (right_ne_zero_of_mul_eq_one hm) hm).symm

/-- **(c7)** The one enclosure (d8) wants, at `δ = 6/10^13`. -/
theorem lamM_centre_encl : ‖lamM cA + lamM (1 - cA) - 1 / (cA * (1 - cA))‖ ≤ 6 / 10 ^ 13 := by
  rw [inv_centre_eq, one_sub_cA_eq, cA_eq]
  have h := inD_recentre (inD_add' L_wA L_wB) (c := tInv) (r := 6 / 10 ^ 13) (by decide +kernel)
  unfold inD at h
  rw [show ((6 / 10 ^ 13 : ℚ) : ℝ) = 6 / 10 ^ 13 by norm_num] at h
  exact h

/-- **SP3, (d8) at (c7)'s δ** `‖zqFn cA‖ ≤ 13103/10000 · 16012218800 · 6/10^13 = %s`. -/
theorem zqFn_centre_eps : ‖zqFn cA‖ ≤ %s :=
  (zqFn_centre_le lamM_centre_encl).trans (le_of_eq (by norm_num))

/-- **SP3** `‖zqFn cA‖ ≤ 1/10`. -/
theorem zqFn_centre_small : ‖zqFn cA‖ ≤ 1 / 10 :=
  zqFn_centre_eps.trans (by norm_num)

end OffZero
end ZQ
end Schema
end SIDEExplicitFormula
''' % (lp(TINV), str(F(13103, 10000) * 16012218800 * DELTA), lq(F(13103, 10000) * 16012218800 * DELTA).replace(' : ℚ', '')))
src = '\n'.join(out)
open(sys.argv[1], 'w', encoding='utf-8', newline='\n').write(src)
print('LAM_LO', LAM_LO, 'LAM_HI', LAM_HI, 'S_LO', S_LO, 'S_HI', S_HI)
print('centre A', [float(x) for x in cA_], float(rA_))
print('centre B', [float(x) for x in cB_], float(rB_))
print('tInv', [float(x) for x in TINV])
print('final tot', float(tot), 'delta', float(DELTA))
print('eps', F(13103, 10000) * 16012218800 * DELTA, float(F(13103, 10000) * 16012218800 * DELTA))
print('terms', facts)
print('lines', src.count('\n') + 1)
