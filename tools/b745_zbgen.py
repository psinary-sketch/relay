# -*- coding: utf-8 -*-
"""tools/b745_zbgen.py -- (R355)(4)(b) W-ORD-ZETA-BOX Z4: the certificate generator. Mirrors the Lean definitions of OffZero/Sums.lean and
OffZero/GammaVal.lean in exact Fractions (carried from tools/b741_g5gen.py), checks every side condition the kernel will decide, and writes
SIDEExplicitFormula/Schema/ZetaBox/Signs.lean: per point t (t = 16 first, SPZ2; then t = 12, SPZ3) the shell incGamma1 (1/4 + it/2) at the
rational rho = 3.14159265358979323846 (pi_gt_d20's literal) through the anchor X = 16 rho (j = 4), moved to pi by the Lipschitz carry, and the
sign of zLam t from it with Z2's 11/10^7 and the exact pole part. An mpmath control is printed first (the shell's value against the disc).

args: out_path t [t ...]     (the points, in the order written; each of 12, 16)
"""
import math
import sys
from fractions import Fraction as F

import mpmath

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


P_LO, P_HI = F(314159265358979323846, 10 ** 20), F(314159265358979323847, 10 ** 20)   # pi_gt_d20, pi_lt_d20
L2 = F(287209, 414355)
EPS_IG = F(1, 10 ** 19)
TAIL = F(11, 10 ** 7)      # Z2, Tail.lean zM_sub_le
J = 4
RHO = P_LO
X = 2 ** J * RHO
D = P_HI - P_LO


def nterms(Xv, wr, tol=F(1, 10 ** 26)):
    n = 1
    while not (2 * Xv <= n + 1 and 2 * Xv ** n / (math.factorial(n) * (wr + n)) <= tol):
        n += 1
    return n


def point(T, emit):
    w = (F(1, 4), F(T, 2))
    wr, wi = w
    ws = 'zw%d' % T
    emit('/-- `w = 1/4 + %di`, the point `s/2` at `t = %d`. -/' % (T // 2, T))
    emit('def %s : ℚ × ℚ := ((1 / 4 : ℚ), (%d : ℚ) / 2)\n' % (ws, T))
    emit('theorem %s_re_pos : 0 < (qc %s).re := by\n  rw [qc_re]\n  norm_num [%s]\n' % (ws, ws, ws))
    emit('theorem %s_re_le : (qc %s).re ≤ 1 := by\n  rw [qc_re]\n  norm_num [%s]\n' % (ws, ws, ws))
    # 2^w
    N = 24
    p = qscale(L2 / 16, w)
    assert qn(p) <= 1 and qn(w) <= 10 ** 10
    E = qexpS(p, N)
    R = qn(p) ** N * (F(N + 1) / (math.factorial(N) * N))
    C16 = qpow(E, 16)
    R16 = (qn(E) + R) ** 16 - qn(E) ** 16
    Dd = 2 * qn(w) / 10 ** 10
    c2 = rc(C16)
    tot = qn(qsub(qmul(C16, (F(1), F(0))), c2)) + qn(C16) * Dd + 1 * R16 + R16 * Dd
    r2 = up(tot)
    assert tot <= r2
    emit('theorem two_%s : inD ((2 : ℂ) ^ qc %s) %s %s :=' % (ws, ws, lp(c2), lq(r2)))
    emit('  two_cpow_encl %s %d (by norm_num) (by decide +kernel) (by decide +kernel) (by decide +kernel)\n' % (ws, N))
    # Gamma(w)/X^w at the anchor
    nX = nterms(X, wr)
    S = sReIm(X, wr, wi, nX)
    cX = rc(S)
    tot = qn(qsub(S, cX)) + 2 * X ** nX / (math.factorial(nX) * (wr + nX)) + EPS_IG
    rX = up(tot)
    assert X >= 41 and 2 * X <= nX + 1 and tot <= rX and 0 < wr <= 1
    emit('theorem G_%s : inD (Gfac (qc %s) %s) %s %s :=' % (ws, ws, lq(X), lp(cX), lq(rX)))
    emit('  GX_encl %s (by decide +kernel) (by decide +kernel) (by decide +kernel) %d (by decide +kernel) (by decide +kernel)\n' % (ws, nX))
    # the shell at rho
    n = nterms(RHO, wr)
    SL = sReIm(RHO, wr, wi, n)
    rL = 2 * RHO ** n / (math.factorial(n) * (wr + n))
    cP = qpow(c2, J)
    rP = (qn(c2) + r2) ** J - qn(c2) ** J
    cM = qmul(cP, cX)
    rM = qn(cP) * rX + qn(cX) * rP + rP * rX
    cS = qsub(cM, SL)
    rS = rM + rL
    cI = rc(cS)
    tot = qn(qsub(cS, cI)) + rS
    rI = up(tot)
    assert tot <= rI and RHO > 0 and F(13, 10) <= RHO and X == 2 ** J * RHO and 2 * RHO <= n + 1
    emit('theorem I_%s : inD (incGamma1 (qc %s) %s) %s %s := by' % (ws, ws, lq(RHO), lp(cI), lq(rI)))
    emit('  rw [incGamma1_split (%s_re_pos) (ρ := %s) (X := %s) (by decide +kernel) %d (by decide +kernel)]' % (ws, lq(RHO), lq(X), J))
    emit('  exact inD_recentre (inD_sub\' (inD_mul\' (inD_pow two_%s %d) G_%s) (lowInt_encl %s (by decide +kernel) (by decide +kernel) %d'
         % (ws, J, ws, ws, n))
    emit('    (by decide +kernel))) (by decide +kernel)\n')
    # the carry to pi
    assert RHO - D <= P_LO and P_HI <= RHO + D
    rT = up(rI + D * F(10, 3))
    emit('theorem P_%s : inD (incGamma1 (qc %s) Real.pi) %s %s :=' % (ws, ws, lp(cI), lq(rT)))
    emit('  inD_transfer_pi %s_re_le (ρ := %s) (d := %s) (by decide +kernel) (by decide +kernel) (by decide +kernel) I_%s'
         % (ws, lq(RHO), lq(D), ws))
    emit('    (by decide +kernel)\n')
    # the control: mpmath's shell against the disc
    mpmath.mp.dps = 50
    wv = mpmath.mpc(mpmath.mpf(1) / 4, mpmath.mpf(T) / 2)
    val = mpmath.quad(lambda u: u ** (wv - 1) * mpmath.exp(-mpmath.pi * u), [1, 2, 4, 8, mpmath.inf])
    gap = abs(val - mpmath.mpc(mpmath.mpf(cI[0].numerator) / cI[0].denominator, mpmath.mpf(cI[1].numerator) / cI[1].denominator))
    ok = gap <= mpmath.mpf(rT.numerator) / rT.denominator
    print('  control t = %d: mpmath incGamma1 (1/4 + %di) pi = %s ; |value - centre| = %s against the radius %s : %s'
          % (T, T // 2, mpmath.nstr(val, 15), mpmath.nstr(gap, 3), mpmath.nstr(mpmath.mpf(rT.numerator) / rT.denominator, 3),
             'AS WANTED' if ok else 'NOT AS WANTED'))
    if not ok:
        sys.exit('### THE CONTROL FAILED -- NOTHING WRITTEN')
    # the sign
    K4 = 1 + 4 * T ** 2
    if T == 16:
        lhs = (2 * cI[0] - 2 * rT - TAIL) * K4
        assert lhs > 4, lhs
        print('  t = 16: (2 c - 2 r - 11/10^7)(1 + 4 t^2) = %.12f > 4, margin %.3e' % (float(lhs), float(lhs - 4)))
        emit('/-- **The sign at `t = 16`**: `0 < zLam 16`. -/')
        emit('theorem zLam_16_pos : 0 < zLam 16 := by')
        emit('  have h := zLam_pos_of (T := 16) P_%s (by decide +kernel)' % ws)
        emit('  rwa [show ((16 : ℚ) : ℝ) = 16 by norm_num] at h\n')
        emit('/-- **zeta_sign_16** (the plan\'s (a)). -/')
        emit('theorem zeta_sign_16 : 0 < (completedRiemannZeta (1 / 2 + 16 * Complex.I)).re := by')
        emit('  rw [(show (1 / 2 + 16 * Complex.I : ℂ) = lp 16 by unfold lp; norm_num), zeta_line, Complex.ofReal_re]')
        emit('  exact zLam_16_pos\n')
    elif T == 12:
        lhs = (2 * cI[0] + 2 * rT + TAIL) * K4
        assert lhs < 4, lhs
        print('  t = 12: (2 c + 2 r + 11/10^7)(1 + 4 t^2) = %.12f < 4, margin %.3e' % (float(lhs), float(4 - lhs)))
        emit('/-- **The sign at `t = 12`**: `zLam 12 < 0`. -/')
        emit('theorem zLam_12_neg : zLam 12 < 0 := by')
        emit('  have h := zLam_neg_of (T := 12) P_%s (by decide +kernel)' % ws)
        emit('  rwa [show ((12 : ℚ) : ℝ) = 12 by norm_num] at h\n')
        emit('/-- **zeta_sign_12** (the plan\'s (a)). -/')
        emit('theorem zeta_sign_12 : (completedRiemannZeta (1 / 2 + 12 * Complex.I)).re < 0 := by')
        emit('  rw [(show (1 / 2 + 12 * Complex.I : ℂ) = lp 12 by unfold lp; norm_num), zeta_line, Complex.ofReal_re]')
        emit('  exact zLam_12_neg\n')
    else:
        sys.exit('### t must be 12 or 16')
    return {'t': T, 'n_anchor': nX, 'n_rho': n, 'radius': float(rT), 'centre_re': float(cI[0])}


def main():
    out_path, pts = sys.argv[1], [int(a) for a in sys.argv[2:]]
    out = []
    emit = out.append
    emit('''/-
SIDE-explicit-formula -- SIDEExplicitFormula/Schema/ZetaBox/Signs.lean
THIS PROGRAMME'S WORK (act b745, ruling (R355)(4)(b), W-ORD-ZETA-BOX Z4; the plan relay data/b744_zetabox_plan.txt) -- NOT VENDORED.
SPIRAL_MAP section 7 rule 9 applies here in full: `theorem`, never `lemma`.
GENERATED by relay tools/b745_zbgen.py; every side condition a `ℚ` inequality or equality decided by the kernel (`decide +kernel`).

Z4, THE SIGNS (points %s). Per point: `2^w` from its exponential series; `Γ(w)/X^w` at the anchor `X = 16 ρ`, `ρ = 3.14159265358979323846`,
from the lower series and the upper piece's `e^(−X)/X`; the shell `incGamma1 w ρ = (2^w)^4 Γ(w)/X^w − lowInt w ρ`, moved to `π` by the
Lipschitz carry (`inD_transfer_pi`); the sign of `zLam t` with Z2's `11/10^7` and the exact pole part. A bound on one value at each point.
-/
import SIDEExplicitFormula.Schema.ZetaBox.Instr

namespace SIDEExplicitFormula
namespace Schema
namespace ZetaBox

open ZQ.OffZero

/-! ## Z4 -- the signs -/
''' % ', '.join('t = %d' % t for t in pts))
    facts = [point(t, emit) for t in pts]
    emit('end ZetaBox\nend Schema\nend SIDEExplicitFormula\n')
    text = '\n'.join(out)
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print('wrote %s: %d lines ; %s' % (out_path, text.count('\n'), facts))


if __name__ == '__main__':
    main()
