# -*- coding: utf-8 -*-
"""tools/b742_s6gen.py -- (R352)(3)(b) as amended by the author's word, data/b742_s6_plan.txt (4) G4: THE 20 NODE VALUES. Carried from
tools/b741_g5gen.py: its exact-Fraction mirror of Sums.lean / GammaVal.lean and its half() unchanged but for the tail, which is NodeBase.lean's
lamM_sub_shellSum_fine (1e-30 + 1.2e-14 + 1e-16) in place of lamM_sub_shellSum. The nodes: c = 1/2 + 16.290216 i, rho = 49/100, M = 20,
z_j = c + rho w^j rounded to 1/10^18, symmetric under s -> 1 - conj s (z_(10-j) = 1 - conj z_j, asserted). Per node: lamM (qc z_j) in a disc
(the half), then lamF (qc z_j) = lamM z_j + conj (lamM z_(10-j)) - 1/(z_j (1 - z_j)) in a disc. Writes Nodes0..Nodes3.lean (five nodes each)
NodesF.lean and (G5) FrontierData.lean into the clone's OffZero directory, and prints each file's md5. args: out_dir"""
import hashlib
import json
import math
import os
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

SHELLS = [(1, 2, 5), (4, 2, 3), (6, 4, 3), (8, 4, 2), (9, 2, 2), (12, 4, 2), (16, 2, 1), (18, 4, 1)]  # Q, count, j
XS = {32: None, 36: None, 48: None}
TAIL = F(1, 10 ** 30) + (F(12, 10 ** 15) + F(1, 10 ** 16))
EPS_IG = F(1, 10 ** 19)


def nterms(X, wr, tol=F(1, 10 ** 26)):
    n = 1
    while not (2 * X <= n + 1 and 2 * X ** n / (math.factorial(n) * (wr + n)) <= tol):
        n += 1
    return n


out = []


def emit(s):
    out.append(s)
facts = {}


def half(tag, w):
    wr, wi = w
    ws = tag
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
    emit('theorem L_%s : inD (lamM (qc %s)) %s (%s + (1 / 10 ^ 30 + (12 / 10 ^ 15 + 1 / 10 ^ 16))) :=' % (ws, ws, lp(cSS), lq(rSS)))
    emit('  inD_near S_%s (by' % ws)
    emit('    rw [show ((1 / 10 ^ 30 + (12 / 10 ^ 15 + 1 / 10 ^ 16) : ℚ) : ℝ) = 1 / 10 ^ 30 + (12 / 10 ^ 15 + 1 / 10 ^ 16) by norm_num]')
    emit('    exact lamM_sub_shellSum_fine %s_re_le)\n' % ws)
    return cSS, rSS + TAIL



HEAD = """/-
SIDE-explicit-formula -- SIDEExplicitFormula/Schema/ZQ/OffZero/%s.lean
THIS PROGRAMME'S WORK (act b742, ruling (R352)(3)(b) as amended by the author's word, relay data/b742_s6_plan.txt (4) G4) -- NOT VENDORED.
SPIRAL_MAP section 7 rule 9 applies here in full: `theorem`, never `lemma`.
GENERATED by tools/b742_s6gen.py (committed before this file); every side condition a `ℚ` inequality or equality decided by the kernel.

%s
-/
import %s

namespace SIDEExplicitFormula
namespace Schema
namespace ZQ
namespace OffZero
"""
FOOT = """
end OffZero
end ZQ
end Schema
end SIDEExplicitFormula
"""
# A file that opens `noncomputable section` inside the namespace closes it before the namespaces (dispatch 5, NodesF.lean :284).
FOOT_NC = '\nend\n' + FOOT
NS ='SIDEExplicitFormula.Schema.ZQ.OffZero.'
CY = F(16290216, 1000000)
RHO = F(49, 100)
M = 20
DEN = 10 ** 18


def node_offsets():
    """rho w^j rounded to 1/DEN, built from j = 0..5 by the symmetries of the 20th roots (so z_(10-j) = 1 - conj z_j exactly)."""
    base = {}
    for j in range(6):
        t = 2 * math.pi * j / M
        c = F(0) if j == 5 else F(round(float(RHO) * math.cos(t) * DEN), DEN)
        s = F(0) if j == 0 else F(round(float(RHO) * math.sin(t) * DEN), DEN)
        base[j] = (c, s)
    off = {}
    for j in range(6):
        c, s = base[j]
        off[j] = (c, s)
        off[10 - j] = (-c, s)
        off[10 + j] = (-c, -s)
        off[(20 - j) % 20] = (c, -s)
    assert sorted(off) == list(range(20))
    return off


OFF = node_offsets()
Z = dict((j, (F(1, 2) + OFF[j][0], CY + OFF[j][1])) for j in range(M))
for j in range(M):
    k = (10 - j) % M
    assert (1 - Z[j][0], -Z[j][1]) == (Z[k][0], -Z[k][1]), j
    assert 0 < Z[j][0] <= 1
L = {}
files = {}
for part in range(4):
    out[:] = []
    js = list(range(5 * part, 5 * part + 5))
    for j in js:
        tag = 'n%d' % j
        emit('def %s : ℚ × ℚ := %s\n' % (tag, lp(Z[j])))
        emit('theorem %s_re_pos : 0 < (qc %s).re := by\n  rw [qc_re]\n  norm_num [%s]\n' % (tag, tag, tag))
        emit('theorem %s_re_le : (qc %s).re ≤ 1 := by\n  rw [qc_re]\n  norm_num [%s]\n' % (tag, tag, tag))
        L[j] = half(tag, Z[j])
    doc = ('G4, THE NODE VALUES, PART %d: lamM at the rational nodes n%d-n%d (data/b742_s6_plan.txt (2)), each by b741`s Centre shape (Centre.lean)\n'
           'with the tail of NodeBase.lean. Enclosures of lamM at rational points; no zero is located by this file.') % (part, js[0], js[-1])
    files['Nodes%d' % part] = HEAD % ('Nodes%d' % part, doc, NS + 'NodeBase') + '\n'.join(out) + FOOT
out[:] = []
FV = {}
for j in range(M):
    k = (10 - j) % M
    a = Z[j]
    ac = (1 - a[0], -a[1])
    P = qmul(a, ac)
    den = P[0] ** 2 + P[1] ** 2
    T = (P[0] / den, -P[1] / den)
    assert qmul(T, qmul(a, ac)) == (1, 0)
    cA_, rA_ = L[j]
    cB_, rB_ = L[k]
    cB_c = (cB_[0], -cB_[1])
    cF = qsub(qadd(cA_, cB_c), T)
    cR = rc(cF)
    tot = qn(qsub(cF, cR)) + rA_ + rB_
    rR = up(tot)
    FV[j] = (cR, rR)
    emit('def t%d : ℚ × ℚ := %s\n' % (j, lp(T)))
    emit('theorem F_n%d : inD (lamF (qc n%d)) %s %s := by' % (j, j, lp(cR), lq(rR)))
    emit('  have e1 : (1 : ℂ) - qc n%d = conj (qc n%d) := by' % (j, k))
    emit('    apply Complex.ext <;> simp [qc_re, qc_im, n%d, n%d] <;> norm_num' % (j, k))
    emit('  have e0 : (1 : ℂ) - qc n%d = qc ((1 : ℚ) - n%d.1, -n%d.2) := by' % (j, j, j))
    emit('    apply Complex.ext <;> simp [qc_re, qc_im]')
    emit('  have hm : qc t%d * (qc n%d * (1 - qc n%d)) = 1 := by' % (j, j, j))
    emit('    rw [e0, ← qc_mul, ← qc_mul, show qmul t%d (qmul n%d ((1 : ℚ) - n%d.1, -n%d.2)) = (1, 0) by decide +kernel, qc_one]' % (j, j, j, j))
    emit('  have e2 : 1 / (qc n%d * (1 - qc n%d)) = qc t%d := (eq_div_of_mul_eq (right_ne_zero_of_mul_eq_one hm) hm).symm' % (j, j, j))
    emit('  rw [lamF_eq_split, e2, e1, lamM_conj]')
    emit('  exact inD_recentre (inD_sub\' (inD_add\' L_n%d (inD_conj L_n%d)) (inD_self t%d)) (by decide +kernel)\n' % (j, k, j))
doc = ('G4, THE NODE VALUES: lamF at the twenty rational nodes, from the four parts and the symmetry s -> 1 - conj s (z_(10-j) = 1 - conj z_j\n'
       'exactly): lamF z_j = lamM z_j + conj (lamM z_(10-j)) - 1/(z_j (1 - z_j)) (Frame.lean lamF_eq_split, Strip.lean lamM_conj). Enclosures of\n'
       'lamF at rational points; no zero is located by this file.')
pre = 'open ComplexConjugate\n\nnoncomputable section\n'
files['NodesF'] = (HEAD % ('NodesF', doc, '\nimport '.join(NS + 'Nodes%d' % p for p in range(4)))).replace(
    'namespace OffZero\n', 'namespace OffZero\n\n' + pre, 1) + '\n'.join(out) + FOOT_NC

# ---------------------------------------------------------------- G5: THE FRONTIER DATA (FrontierData.lean)
from decimal import Decimal, getcontext
getcontext().prec = 80
CIQ = (F(1, 2), CY)
s5 = Decimal(5).sqrt()
S5LO = F(int(s5 * 10 ** 30), 10 ** 30)
S5HI = S5LO + F(1, 10 ** 30)
assert S5LO ** 2 <= 5 <= S5HI ** 2
XLO = (10 + 2 * S5LO) / 16
cdec = (Decimal(XLO.numerator) / Decimal(XLO.denominator)).sqrt()
CLO = F(int(cdec * 10 ** 30), 10 ** 30)
CHI = CLO + F(2, 10 ** 30)
assert CLO ** 2 <= XLO and (10 + 2 * S5HI) / 16 <= CHI ** 2
W1 = (rnd((CLO + CHI) / 2), rnd(((S5LO - 1) / 4 + (S5HI - 1) / 4) / 2))
R1 = up(max(CHI - W1[0], W1[0] - CLO) + max((S5HI - 1) / 4 - W1[1], W1[1] - (S5LO - 1) / 4))
WT = [((F(1), F(0)), F(0)), (W1, R1)]
for m in range(2, 20):
    c0, r0 = WT[-1]
    cm = qmul(c0, W1)
    rm = qn(c0) * R1 + qn(W1) * r0 + r0 * R1
    cr = rc(cm)
    WT.append((cr, up(qn(qsub(cm, cr)) + rm)))
RHOQ = F(49, 100)
DEL_NODE = []
for j in range(M):
    w, rw_ = WT[j]
    d = qsub(qadd(CIQ, qscale(RHOQ, w)), Z[j])
    assert qn(qsub(Z[j], CIQ)) <= F(7, 10)
    DEL_NODE.append(FV[j][1] + 120 * 3 * (RHOQ * rw_ + qn(d)) / (3 - F(7, 10)) ** 2)
DELQ = F(math.ceil(max(DEL_NODE) * 10 ** 16), 10 ** 16)
VT = [FV[j][0] for j in range(M)]


def wexp(j, k): return (20 - (j * k) % 20) % 20


def sk(k): return 1 / (20 * RHOQ ** k)


CT, ET = [], []
for k in range(M):
    s = (F(0), F(0))
    rs = F(0)
    for j in range(M):
        w, rw_ = WT[wexp(j, k)]
        s = qadd(s, qmul(w, VT[j]))
        rs += qn(w) * 0 + qn(VT[j]) * rw_ + rw_ * 0
    cen = qscale(sk(k), s)
    rad = sk(k) * rs
    ck = rc(cen)
    CT.append(ck)
    ET.append(up(qn(qsub(cen, ck)) + rad))
RR = F(5623, 10000)
ECQ = F(math.ceil(sum(ET[k] * RR ** k for k in range(M)) * 10 ** 24) + 1, 10 ** 24)
LPQ = F(math.ceil(sum(qn(CT[k]) * k * RR ** (k - 1) for k in range(1, M)) * 10 ** 13) + 1, 10 ** 13)


def polyQ(u):
    s = (F(0), F(0))
    for k in range(M):
        s = qadd(s, qmul(CT[k], qpow(u, k)))
    return s


X0, X1, Y0, Y1 = F(85326, 100000), F(105326, 100000), F(16190216, 1000000), F(16390216, 1000000)
H = F(1, 100)
EDGES = (('bottom', lambda i: (X0 + H / 2 + i * H, Y0)), ('top', lambda i: (X0 + H / 2 + i * H, Y1)),
         ('left', lambda i: (X0, Y0 + H / 2 + i * H)), ('right', lambda i: (X1, Y0 + H / 2 + i * H)))
ns = []
for name, pt in EDGES:
    for i in range(20):
        p = polyQ(qsub(pt(i), CIQ))
        ns.append(p[0] ** 2 + p[1] ** 2)
MLO = F(17, 10 ** 12)
assert all(MLO ** 2 <= x for x in ns), min(ns)
A_ = sum((RR / RHOQ) ** k for k in range(M))
REM = F(120 * 3) * (RR ** 20 + RHOQ ** 20) / ((3 - RR) * (3 ** 20 - RHOQ ** 20))
MARGIN = MLO - LPQ * F(1, 200) - REM - DELQ * A_ - ECQ
assert MARGIN >= F(1, 10 ** 12), float(MARGIN)


def lst(xs): return '[' + ',\n    '.join(xs) + ']'


out[:] = []
emit('def s5lo : ℚ := %s\ndef s5hi : ℚ := %s\ndef clo : ℚ := %s\ndef chi : ℚ := %s\n' % (lq(S5LO), lq(S5HI), lq(CLO), lq(CHI)))
emit('theorem W_one : inD omg %s %s :=' % (lp(W1), lq(R1)))
emit('  omg_inD (lo := s5lo) (hi := s5hi) (clo := clo) (chi := chi) (by decide +kernel) (by decide +kernel) (by decide +kernel)')
emit('    (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel) (by decide +kernel)\n')
emit('def wtab : List (ℚ × ℚ) := %s\n' % lst([lp(c) for c, r in WT]))
emit('def wrad : List ℚ := %s\n' % lst([lq(r) for c, r in WT]))
emit('theorem W_0 : inD (omg ^ 0) (wtab.getD 0 0) (wrad.getD 0 0) := by\n  rw [pow_zero]\n  have h := inD_self (1, 0)\n  rw [qc_one] at h\n'
     '  exact inD_recentre h (by decide +kernel)\n')
emit('theorem W_1 : inD (omg ^ 1) (wtab.getD 1 0) (wrad.getD 1 0) := by\n  rw [pow_one]\n  exact inD_recentre W_one (by decide +kernel)\n')
for m in range(2, 20):
    emit('theorem W_%d : inD (omg ^ %d) (wtab.getD %d 0) (wrad.getD %d 0) := by\n  rw [show omg ^ %d = omg ^ %d * omg from pow_succ omg %d]\n'
         '  exact inD_recentre (inD_mul\' W_%d W_one) (by decide +kernel)\n' % (m, m, m, m, m, m - 1, m - 1, m - 1))
emit('theorem W_all : ∀ m < 20, inD (omg ^ m) (wtab.getD m 0) (wrad.getD m 0) := by\n  intro m hm\n  interval_cases m\n' +
     '\n'.join('  · exact W_%d' % m for m in range(20)) + '\n')
emit('def vtab : List (ℚ × ℚ) := %s\n' % lst([lp(v) for v in VT]))
emit('def DELq : ℚ := %s\n' % lq(DELQ))
for j in range(M):
    emit('theorem V_%d : ‖lamF (cI + ((49 / 100 : ℝ) : ℂ) * omg ^ %d) - qc (vtab.getD %d 0)‖ ≤ (DELq : ℝ) :=' % (j, j, j))
    emit('  node_value_le F_n%d (W_all %d (by norm_num)) (by decide +kernel) (by decide +kernel)\n' % (j, j))
emit('/-- **G5, the node values at the exact roots**: within `DELq` of the table, at every node. -/')
emit('theorem V_all : ∀ j < 20, ‖lamF (cI + ((49 / 100 : ℝ) : ℂ) * omg ^ j) - qc (vtab.getD j 0)‖ ≤ (DELq : ℝ) := by\n'
     '  intro j hj\n  interval_cases j\n' + '\n'.join('  · exact V_%d' % j for j in range(20)) + '\n')
emit('''def sk (k : ℕ) : ℚ := 1 / (20 * (49 / 100 : ℚ) ^ k)

def ccen (k : ℕ) : ℚ × ℚ := qscale (sk k) (∑ j ∈ Finset.range 20, qmul (wtab.getD (wexp j k) 0) (vtab.getD j 0))

def crad (k : ℕ) : ℚ := sk k * ∑ j ∈ Finset.range 20,
  (qn (wtab.getD (wexp j k) 0) * 0 + qn (vtab.getD j 0) * wrad.getD (wexp j k) 0 + wrad.getD (wexp j k) 0 * 0)

/-- The interpolant's coefficient of `u^k` from the table. -/
def coefA (k : ℕ) : ℂ :=
  (((49 / 100 : ℝ) : ℂ) ^ k)⁻¹ * (((20 : ℕ) : ℂ)⁻¹ * ∑ j ∈ Finset.range 20, ((omg ^ j)⁻¹) ^ k * qc (vtab.getD j 0))

theorem coef_inD (k : ℕ) : inD (coefA k) (ccen k) (crad k) := by
  have hs : (((sk k : ℚ) : ℝ) : ℂ) = (((49 / 100 : ℝ) : ℂ) ^ k)⁻¹ * ((20 : ℕ) : ℂ)⁻¹ := by
    unfold sk
    push_cast
    ring
  have hs0 : 0 ≤ sk k := by
    unfold sk
    positivity
  unfold coefA ccen crad
  rw [← mul_assoc, ← hs]
  refine inD_qscale (sk k) hs0 (inD_sum _ fun j _ => ?_)
  rw [omg_inv_pow (wexp_spec j k)]
  exact inD_mul' (W_all _ (wexp_lt j k)) (inD_self _)
''')
emit('def ctab : List (ℚ × ℚ) := %s\n' % lst([lp(c) for c in CT]))
emit('def etab : List ℚ := %s\n' % lst([lq(e) for e in ET]))
emit('theorem coef_near : ∀ k < 20, qn (qsub (ccen k) (ctab.getD k 0)) + crad k ≤ etab.getD k 0 := by\n  decide +kernel\n')
emit('''/-- **G5, the coefficients**: each within its `etab` entry of the table `ctab`. -/
theorem coef_le : ∀ k ∈ Finset.range 20, ‖coefA k - qc (ctab.getD k 0)‖ ≤ ((etab.getD k 0 : ℚ) : ℝ) := fun k hk =>
  inD_recentre (coef_inD k) (coef_near k (Finset.mem_range.1 hk))
''')
emit('def ECq : ℚ := %s\n' % lq(ECQ))
emit('''theorem ecoef_le : ∑ k ∈ Finset.range 20, ((etab.getD k 0 : ℚ) : ℝ) * (5623 / 10000 : ℝ) ^ k ≤ (ECq : ℝ) := by
  have h : (∑ k ∈ Finset.range 20, etab.getD k 0 * (5623 / 10000 : ℚ) ^ k) ≤ ECq := by decide +kernel
  have h' := (Rat.cast_le (K := ℝ)).mpr h
  push_cast at h'
  exact h'
''')
emit('def LPq : ℚ := %s\n' % lq(LPQ))
emit('''/-- **G5, L_P**, proved: `Σ_k ‖ĉ_k‖ k r^(k−1) ≤ LPq` (`norm_qc_le`, Sums.lean, and the table). -/
theorem lp_le : ∑ k ∈ Finset.range 20, ‖qc (ctab.getD k 0)‖ * ((k : ℝ) * (5623 / 10000 : ℝ) ^ (k - 1)) ≤ (LPq : ℝ) := by
  refine (Finset.sum_le_sum fun k _ => mul_le_mul_of_nonneg_right (norm_qc_le _) (by positivity)).trans ?_
  have h : (∑ k ∈ Finset.range 20, qn (ctab.getD k 0) * ((k : ℚ) * (5623 / 10000 : ℚ) ^ (k - 1))) ≤ LPq := by decide +kernel
  have h' := (Rat.cast_le (K := ℝ)).mpr h
  push_cast at h'
  exact h'
''')
emit('def MLO : ℚ := %s\n' % lq(MLO))
emit('def cIq : ℚ × ℚ := ((1 : ℚ) / 2, (16290216 : ℚ) / 1000000)\n')
PT = {'bottom': '((85326 : ℚ) / 100000 + 1 / 200 + ((i : ℕ) : ℚ) * (1 / 100), (16190216 : ℚ) / 1000000)',
      'top': '((85326 : ℚ) / 100000 + 1 / 200 + ((i : ℕ) : ℚ) * (1 / 100), (16390216 : ℚ) / 1000000)',
      'left': '((85326 : ℚ) / 100000, (16190216 : ℚ) / 1000000 + 1 / 200 + ((i : ℕ) : ℚ) * (1 / 100))',
      'right': '((105326 : ℚ) / 100000, (16190216 : ℚ) / 1000000 + 1 / 200 + ((i : ℕ) : ℚ) * (1 / 100))'}
for name, _pt in EDGES:
    emit('theorem check_%s : ∀ i : ℕ, i < 20 → MLO ^ 2 ≤ normSqQ (polyQ ctab (qsub %s cIq)) := by\n  decide +kernel\n' % (name, PT[name]))
emit('''/-- **G5, the margin**: `MLO − LPq/200 − REM − DELq·A − ECq ≥ 1/10^12`, REM the aliasing lemma's bound at `B 120, R 3, M 20, ρ 49/100,
r 5623/10000`, A `Σ_{k<20} (r/ρ)^k`. -/
theorem margin : (1 : ℝ) / 10 ^ 12 ≤ (MLO : ℝ) - (LPq : ℝ) * (1 / 200)
    - 120 * 3 * ((5623 / 10000 : ℝ) ^ 20 + (49 / 100 : ℝ) ^ 20) / ((3 - 5623 / 10000) * (3 ^ 20 - (49 / 100 : ℝ) ^ 20))
    - (DELq : ℝ) * ∑ k ∈ Finset.range 20, ((5623 / 10000 : ℝ) / (49 / 100)) ^ k - (ECq : ℝ) := by
  norm_num [MLO, LPq, DELq, ECq, Finset.sum_range_succ]
''')
doc = ('G5, THE FRONTIER DATA: omega in a disc from rational bounds on the square root of 5 (Omega.lean omg_inD) and its twenty powers; the\n'
       'node values at the exact roots c + rho omega^j within DELq of the table (Omega.lean node_value_le, NodesF.lean); the interpolant`s\n'
       'coefficients within etab of the table ctab; the rounding sum ECq; L_P proved at LPq; P^ at 80 frontier check points, each with\n'
       '|P^|^2 >= MLO^2, by decide +kernel; the margin. No zero is located by this file.')
files['FrontierData'] = (HEAD % ('FrontierData', doc, NS + 'Omega\nimport ' + NS + 'NodesF')).replace(
    'namespace OffZero\n', 'namespace OffZero\n\nopen Complex\n\nnoncomputable section\n', 1) + '\n'.join(out) + FOOT_NC
print('G5: DELq %s (%.4e) ; ECq %.4e ; LPq %.6e ; MLO %.3e ; min |P^| %.4e ; A %.4f ; REM %.4e ; MARGIN %.4e against 1e-12' % (
    DELQ, float(DELQ), float(ECQ), float(LPQ), float(MLO), math.sqrt(float(min(ns))), float(A_), float(REM), float(MARGIN)))
odir = sys.argv[1]
for name, text in sorted(files.items()):
    p = os.path.join(odir, name + '.lean')
    io_ = open(p, 'w', encoding='utf-8', newline='\n')
    io_.write(text)
    io_.close()
    print('%-8s lines %5d md5 %s' % (name, text.count('\n') + 1, hashlib.md5(text.encode('utf-8')).hexdigest()))
print('LAM_LO', LAM_LO, 'LAM_HI', LAM_HI)
rs = [FV[j][1] for j in range(M)]
print('node F radii: max %.4e min %.4e' % (float(max(rs)), float(min(rs))))
for j in range(M):
    print('  n%-2d z = (%.18f, %.18f) F = (%.6e, %.6e) r = %.4e' % (j, float(Z[j][0]), float(Z[j][1]), float(FV[j][0][0]), float(FV[j][0][1]), float(FV[j][1])))
json_out = dict((j, dict(z=[str(Z[j][0]), str(Z[j][1])], c=[str(FV[j][0][0]), str(FV[j][0][1])], r=str(FV[j][1]))) for j in range(M))
jf = open(sys.argv[2], 'w', encoding='utf-8', newline='\n')
jf.write(json.dumps(json_out, indent=1))
jf.close()
print('terms', len(facts))
