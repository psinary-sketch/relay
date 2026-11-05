# -*- coding: utf-8 -*-
"""b742 -- W-ORD-ZQ-OFFLINE-ZERO, S6 on the interpolation route on Lambda_Q, the plan's figures ((R352)(3)(a) as amended by the author's word,
relay data/b742_author_answers.txt :10). Read-only on every repository; writes data/b742_s6_price.txt and nothing else.

  F(z) = lamM z + lamM (1 - z) - 1/(z (1 - z)) = lam^(-z) Gamma(z) Z_Q0(z)   (OffZero/Centre.lean :247's object; Z_Q0 by b667's zq_point,
  tools/b667_epstein_certify.py imported unedited, arb balls).  c = 1/2 + 16.290216 i, the sample circle |w - c| = rho, the far circle |w - c| = R.

  (1) the box's farthest frontier point from c, and the interpolant's error bound there: truncation B_R (r/R)^M / (1 - r/R) and aliasing
      B_R (rho/R)^M / (1 - (rho/R)^M) * sum_{k<M} (r/R)^k, B_R a closed-form bound of |F| on the strip Re w in [1/2 - R, 1/2 + R] (not a sample);
  (2) the amplification A = sum_{k<M} (r/rho)^k of each sample's certification error, and the per-sample delta it forces against the margin;
  (3) the frontier's Re z > 1 length;
  (4) the margins in one line;
  each float a float of a computation; B_R and the remainders are closed forms evaluated in arb; the samples are samples.
Usage: python -X utf8 -u tools/b742_s6_price.py   (prints and banks)"""
import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx   # noqa: E402
import b667_epstein_certify as CERT   # noqa: E402

ctx.prec = 200
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'b742_s6_price.txt')
L = []


def say(s=''):
    print(s, flush=True)
    L.append(s)


T0 = time.time()
FREE0 = CERT.free_mb()
LAM = 2 * arb.pi() / arb(23).sqrt()
X0, X1, Y0, Y1 = Fr('0.85326'), Fr('1.05326'), Fr('16.190216'), Fr('16.390216')   # box A, data/b737_offlinezero_plan.txt :30
C_RE, C_IM = Fr(1, 2), Fr('16.290216')
C = acb(arb(1) / 2, arb('16.290216'))
RHO = Fr(49, 100)
M_LAM = 1e-12          # m_Lambda, the author's word
CENTRE = 6e-13         # Centre.lean :247 lamM_centre_encl


def r_of(K):
    r = [0] * (K + 1)
    B = int(math.isqrt(4 * K)) + 2
    for m in range(-B, B + 1):
        for n in range(-B, B + 1):
            q = m * m + m * n + 6 * n * n
            if q <= K:
                r[q] += 1
    return r


KMAX = 200
RK = r_of(KMAX)


def J(e, a):
    """int_1^oo t^e e^(-a t) dt for an integer e >= 0, closed form: e^(-a) sum_{j<=e} e!/(e-j)! a^(-j-1)."""
    s = arb(0)
    for j in range(e + 1):
        s += arb(math.factorial(e) // math.factorial(e - j)) / a ** (j + 1)
    return (-a).exp() * s


def strip_bound(s0, s1, imlo):
    """a closed-form bound of |F(w)| for Re w in [s0, s1], |Im w| >= imlo: |t^(w-1)| = t^(Re w - 1) <= t^e1 and |t^(-w)| <= t^e2 on t >= 1,
    e1 = max(0, ceil(s1 - 1)), e2 = max(0, ceil(-s0)); every lattice point off 0 with Q <= KMAX by its shell, the rest by
    N(X) <= (2 sqrt(4X/23) + 1)(2 sqrt(X) + 1) points with Q <= X and J's decrease in a; plus 1/|w (1 - w)| <= 1/imlo^2."""
    e1, e2 = max(0, math.ceil(s1 - 1)), max(0, math.ceil(-s0))
    tot = arb(0)
    for k in range(1, KMAX + 1):
        if RK[k]:
            a = LAM * k
            tot += RK[k] * (J(e1, a) + J(e2, a))
    tail = arb(0)
    for X in range(KMAX + 1, 4 * KMAX):
        nx = (2 * math.sqrt(4 * X / 23) + 1) * (2 * math.sqrt(X) + 1)
        a = LAM * X
        tail += arb(nx) * (J(e1, a) + J(e2, a))
    return tot + tail + 1 / arb(imlo) ** 2, e1, e2, tail


def F(z):
    return (LAM ** (-z)) * z.gamma() * CERT.zq_point(z)


def ff(x):
    return float(x.mid()) if hasattr(x, 'mid') else float(x)


say('b742 -- W-ORD-ZQ-OFFLINE-ZERO, S6, THE INTERPOLATION ROUTE ON LAMBDA_Q: THE PLAN`S FIGURES (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
say()
say('### tools/b742_s6_price.py; free memory at start %s MB (the hold 2560 MB); python-flint %s, prec 200; Z_Q0 by tools/b667_epstein_certify.py zq_point' % (FREE0, __import__('flint').__version__))
say('### imported unedited. B_R and the remainders are closed forms evaluated in arb (upper ends printed); the samples are samples, not bounds.')
say()

# ---------------- (1) the geometry
say('## (1) THE FRONTIER`S FARTHEST POINT FROM c = 1/2 + 16.290216 i')
pts = {'the right edge`s midpoint (1.05326, 16.290216)': (X1, C_IM), 'the corner (1.05326, 16.190216)': (X1, Y0), 'the corner (1.05326, 16.390216)': (X1, Y1),
       'the left edge`s midpoint (0.85326, 16.290216)': (X0, C_IM), 'the corner (0.85326, 16.190216)': (X0, Y0)}
for k_, (x, y) in pts.items():
    d2 = (x - C_RE) ** 2 + (y - C_IM) ** 2
    say('  %-48s |z - c|^2 = %s, |z - c| = %.6f' % (k_, d2, math.sqrt(d2)))
R2 = (X1 - C_RE) ** 2 + (Y0 - C_IM) ** 2
RMAX = math.sqrt(R2)
RMAXQ = Fr(5623, 10000)
assert RMAXQ ** 2 >= R2
say('  THE FARTHEST: the two right corners, r = sqrt(%s) = %.6f (the word`s "about 0.553 at the right edge" is the right edge`s midpoint; the' % (R2, RMAX))
say('  corners lie 0.009 farther); r is taken as the rational %s >= it; the sample radius rho = %s; r/rho = %.6f' % (RMAXQ, RHO, float(RMAXQ / RHO)))
say('  the sample circle`s real parts [%s, %s], inside 0 < Re w < 1, so b741`s Centre shape (0 < Re w <= 1 for w and 1 - w) applies at each node' % (C_RE - RHO, C_RE + RHO))
say('  the centre cA = (0.95326, 16.290216): |cA - c| = 0.45326 < rho, inside the sample disc; certified directly by Centre.lean :247 at 6e-13')
say()

# ---------------- the far-circle bounds and the remainders over a grid
say('## (1) THE INTERPOLANT`S ERROR AT r, TRUNCATION AND ALIASING, FROM THE FAR-CIRCLE SIZE B_R (closed form, the strip Re w in [1/2 - R, 1/2 + R])')
say('  M = nodes c + rho exp(2 pi i j / M); P(c + u) = sum_{k<M} c_k u^k, c_k = (1/M) sum_j F(node j) exp(-2 pi i j k / M) rho^(-k)')
say('  for |u| <= r: |F - P| <= B_R (r/R)^M / (1 - r/R)  [truncation]  +  B_R (rho/R)^M / (1 - (rho/R)^M) * sum_{k<M} (r/R)^k  [aliasing]')
say('  A = sum_{k<M} (r/rho)^k: samples within delta each move P by at most A delta on |u| <= r')
say('    R     e1 e2  B_R (bound)     M    truncation     aliasing       remainder      A')
r = arb(str(float(RMAXQ)))
rho = arb(str(float(RHO)))
grid = []
BR = {}
for R in (2, 3, 4, 6):
    Rb = arb(R)
    B, e1, e2, tail = strip_bound(0.5 - R, 0.5 + R, 16.290216 - R)
    BR[R] = (B, e1, e2, tail)
    for M in (16, 20, 24, 28):
        tr = B * (r / Rb) ** M / (1 - r / Rb)
        al = B * (rho / Rb) ** M / (1 - (rho / Rb) ** M) * sum(((r / Rb) ** k for k in range(M)), arb(0))
        A = sum(((r / rho) ** k for k in range(M)), arb(0))
        grid.append((R, M, B, tr, al, tr + al, A))
        say('    %-5d %-2d %-2d %.4e      %-4d %.3e      %.3e      %.3e      %.2f' % (R, e1, e2, ff(B.mid() + B.rad()), M, ff(tr), ff(al), ff(tr + al), ff(A)))
say('  the tail past Q = %d in B_R below %.1e at every R' % (KMAX, max(ff(v[3]) for v in BR.values())))
say()

# ---------------- samples at the chosen (M, R)
say('## (1)-(2) THE CHOSEN NODES AND THE SAMPLES (python-flint balls: samples, not bounds)')
free1 = CERT.free_mb()
say('  free memory before the samples %s MB' % free1)
NF = 160
front = []
for e in range(4):
    for j in range(NF // 4):
        u = Fr(j, NF // 4)
        x, y = ((X0 + (X1 - X0) * u, Y0), (X1, Y0 + (Y1 - Y0) * u), (X1 - (X1 - X0) * u, Y1), (X0, Y1 - (Y1 - Y0) * u))[e]
        front.append(acb(arb(str(float(x))), arb(str(float(y)))))
Fv = [F(z) for z in front]
minF = min(ff(abs(v)) for v in Fv)
say('  the frontier`s %d samples: min |F| %.4e' % (NF, minF))
rows = []
for (R, M) in ((3, 20), (3, 24), (4, 24), (2, 28)):
    om = [acb(0, 2 * arb.pi() * j / M).exp() for j in range(M)]
    nodes = [C + rho * w for w in om]
    Fn = [F(z) for z in nodes]
    coef = [sum((Fn[j] * om[j] ** (-k) for j in range(M)), acb(0)) / M / rho ** k for k in range(M)]
    errs, Pmin = 0.0, 1.0
    for z, fz in zip(front, Fv):
        u = z - C
        Pz = sum((coef[k] * u ** k for k in range(M)), acb(0))
        errs = max(errs, ff(abs(Pz - fz)))
        Pmin = min(Pmin, ff(abs(Pz)))
    LP = sum((k * abs(coef[k]) * r ** (k - 1) for k in range(1, M)), arb(0))
    g = [x for x in grid if x[0] == R and x[1] == M][0]
    B = BR[R][0]
    dF = B / (arb(R) - rho)
    rows.append((R, M, errs, Pmin, ff(LP), ff(g[5]), ff(g[6]), ff(dF)))
    say('  R %d, M %d: max |F - P| on the frontier`s samples %.3e (the bound %.3e) ; min |P| there %.4e ; L_P = sum k |c_k| r^(k-1) = %.4e ; |F`| on the node circle <= B_R/(R - rho) = %.3e'
        % (R, M, errs, ff(g[5]), Pmin, ff(LP), ff(dF)))
say()

say('## (2) THE PER-SAMPLE delta FORCED (the frontier`s check: |P~(z_i)| at N_c points, P~`s Lipschitz figure between them, spacing h = 0.8/N_c)')
say('  the frontier holds |F| >= m_Lambda if  min_i |P~(z_i)| - L_P h/2 - remainder - A (delta + eta F`) - coef >= m_Lambda; with min |P~(z_i)| read as min |P| above,')
say('  delta* = (min |P| - m_Lambda - remainder - L_P h/2) / A, the largest per-sample error the route allows (eta, coef: the node and coefficient roundings, set below 1e-16)')
say('    R  M   N_c   h          L_P h/2      delta*        A delta at b741`s shape as built (1.41e-13) ; with the mid shells by norm_shell_le (5.9e-14)')
D_BUILT, D_SHELL = 1.41e-13, 5.9e-14
for R, M, errs, Pmin, LP, rem, A, dF in rows:
    for Nc in (20, 40, 80):
        h = 0.8 / Nc
        ds = (Pmin - M_LAM - rem - LP * h / 2) / A
        say('    %d  %-3d %-5d %.4f     %.3e    %.3e     %.3e (%s) ; %.3e (%s)' % (
            R, M, Nc, h, LP * h / 2, ds, A * D_BUILT, 'FITS' if D_BUILT <= ds else 'DOES NOT FIT', A * D_SHELL, 'FITS' if D_SHELL <= ds else 'DOES NOT FIT'))
say('  b741`s per-point error as built: Centre.lean :124/:131 and :220/:227, the two halves` ball radii 3.186e-14 + 8.99e-15 plus 2 (1e-30 + 5e-14 + 1e-16)')
say('    (the mid shells 23 <= Q <= 31 by mid_numeric`s 5e-14 a half) = 1.41e-13; the mid shells by norm_shell_le (b741 plan :27, 1.77e-14 both halves) = 5.9e-14')
say()

say('## (3) THE FRONTIER`S Re z > 1 PART')
lr = 2 * (X1 - 1) + (Y1 - Y0)
say('  the bottom and top edges from x = 1 to 1.05326 and the whole right edge: %s = %.5f of the perimeter 0.8; there w = z has Re w > 1 and' % (lr, float(lr)))
say('  the compiled Series, GammaVal and Shells lemmas (0 < Re w <= 1) do not apply; on this part |F| is bounded below by P~ alone (the check')
say('  points and L_P), F - P bounded by the remainder from B_R, which rests on the strip bound above, not on the compiled lemmas')
say()

say('## (5) THE TWO RULED ROUTES ((R352)(3)(a)), PRICED: A LIPSCHITZ FIGURE ON THE FRONTIER BY CAUCHY`S ESTIMATE FROM THE NO-CANCELLATION SIZE')


def tri(z):
    """the triangle-inequality size of F at z: sum over shells of int_1^oo |t^(z-1)| e^(-a t) + |t^(-z)| e^(-a t) dt, plus 1/|z (1 - z)|."""
    s = z.real
    tot = arb(0)
    for k in range(1, 81):
        if RK[k]:
            a = LAM * k
            tot += RK[k] * ((a ** (-s)) * acb(a).gamma_upper(acb(s)).real + (a ** (s - 1)) * acb(a).gamma_upper(acb(1 - s)).real)
    return tot + 1 / abs(z * (1 - z))


TF = [ff(tri(z)) for z in front[::8]]
say('  the size T(z) on the frontier`s samples %.4e to %.4e, against min |F| %.4e: %.1f orders of cancellation' % (min(TF), max(TF), minF, math.log10(min(TF) / minF)))
LPTS = 265   # lines a frontier point, b741's Centre.lean measured per point (the Centre`s two halves)
for d in (0.05, 0.1, 0.2):
    TB = max(ff(tri(acb(arb(x), arb(y)))) for x in (0.85326 - d, 1.05326 + d) for y in (16.190216 - d, 16.390216 + d))
    Lc = TB / d
    h = 2 * (minF - CENTRE - M_LAM) / Lc
    say('  F (m_Lambda 1e-12): d %.2f ; the size at the widened box`s corners %.3e ; L = T/d %.3e ; h %.3e ; frontier points %.3e ; lines at %d a point %.3e' % (
        d, TB, Lc, h, 0.8 / h, LPTS, LPTS * 0.8 / h))
K = max(ff(abs(LAM ** z) * abs(z.rgamma())) for z in front)
minZ = min(ff(abs(CERT.zq_point(z))) for z in front[::4])
TB = max(ff(tri(acb(arb(x), arb(y)))) for x in (0.85326 - 0.1, 1.05326 + 0.1) for y in (16.190216 - 0.1, 16.390216 + 0.1))
Lz = K * TB / 0.1
hz = 2 * (minZ - 0.0126 - 0.1) / Lz
say('  zqFn (m = 1/10, centre 0.0126): K = sup |lam^z / Gamma(z)| on the frontier %.4e ; L %.3e ; min |zqFn| on the samples %.4f ; h %.3e ; frontier points %.3e' % (K, Lz, minZ, hz, 0.8 / hz))
say('  both against the plan`s figure: the three-times rule stops each before any Lean (their lines at %d a point, 4.7e13 and %.1e, exceed three times the' % (LPTS, LPTS * 0.8 / hz))
say('  plan`s high figure, 3 x 6,810 = 20,430 lines, by more than 10^9; the points alone by more than 10^6)')
say()

best = min(rows, key=lambda t: t[5] + t[6] * D_SHELL)
say('## (4) THE MARGINS, ONE LINE')
say('  centre %.0e ; m_Lambda %.0e ; frontier minimum %.3e (samples) ; interpolation error %.1e (samples, R %d, M %d ; bound %.1e)' % (CENTRE, M_LAM, minF, best[2], best[0], best[1], best[5]))
say()
say('### ### **r = %.6f AT THE RIGHT CORNERS ; FRONTIER MIN %.3e ; R %d, M %d: REMAINDER %.2e, A %.1f, L_P %.2e ; Re z > 1 LENGTH %.5f OF 0.8 ; FREE %s -> %s MB ; %.0f s.**' % (
    RMAX, minF, best[0], best[1], best[5], best[6], best[4], float(lr), FREE0, CERT.free_mb(), time.time() - T0))
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(L) + '\n')
