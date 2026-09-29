# -*- coding: utf-8 -*-
"""b562_drift.py -- THE DRIFT ON THE BENCH, (R172)(2), READING (3) of b562's face. A MEASUREMENT, NOT A THEOREM.

### At xi, over the chain bank's 10,000 ordinates (tools/e16/zeta_ordinates.npy) taken as zeros rho = 1/2 + i gamma with
### their conjugates. A family member is f . e^{u/2} P_n(u), f built from Mathlib's Real.smoothTransition st:
###   ONE-SIDED  f(u) = st(-u/d) on [-d, 0]      (1 left of it, 0 right of it; f(0) = 0)
###   SYMMETRIC  f(u) = st(1/2 - u/d) on [-d/2, d/2]   (f(u) + f(-u) = 1; f(0) = 1/2)
### the left edge at -infinity. The ZERO SIDE Z(n, d) = Lambda_N(n) + D(n, d), with
###   Lambda_N(n) = sum over the bank of 2 Re liTerm(n, rho),  liTerm = 1 - (1 - 1/rho)^n
###   D(n, d)     = sum over the bank of 2 Re int (f - 1_{u<0}) P_n(u) e^{rho u} du   (Gauss-Legendre on each transition piece)
### P_n(u) = sum_{j<n} C(n, j+1) u^j / j!; the moments int (f - 1_{u<0}) u^j e^{rho u} du for j < 12 are combined by those
### coefficients. Every number printed is this instrument's; the chunks are timed and each runs under 600 s.
### usage: python tools/b562_drift.py [--nodes M]   (writes data/b562_drift.txt and data/b562_drift.json)
"""
import io, json, math, os, sys, time
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
NMAX = 12
DELTAS = (0.1, 0.03, 0.01)
EPS = np.finfo(np.float64).eps
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
L = []


def rec(s=''):
    L.append(s)
    print(s)


def expneg(x):
    x = np.asarray(x, dtype=np.float64)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = np.exp(-1.0 / x[m])
    return out


def st(t):
    """### Mathlib's Real.smoothTransition: expNegInvGlue t / (expNegInvGlue t + expNegInvGlue (1 - t))."""
    a, b = expneg(t), expneg(1.0 - np.asarray(t, dtype=np.float64))
    return a / (a + b)


def pieces(family, d):
    """### the transition pieces [lo, hi] and the weight w(u) = f(u) - 1_{u<0} on each."""
    if family == 'one-sided':
        return [(-d, 0.0, lambda u: st(-u / d) - 1.0)]
    return [(-d / 2, 0.0, lambda u: st(0.5 - u / d) - 1.0), (0.0, d / 2, lambda u: st(0.5 - u / d))]


def coeffs():
    """### c[n][j] = C(n, j+1)/j!, n = 1..NMAX, j < n."""
    c = np.zeros((NMAX + 1, NMAX))
    for n in range(1, NMAX + 1):
        for j in range(n):
            c[n, j] = math.comb(n, j + 1) / math.factorial(j)
    return c


def moments(rho, family, d, M, chunk=1000):
    """### the moments int (f - 1_{u<0}) u^j e^{rho u} du, j < NMAX, for every rho: an array len(rho) x NMAX."""
    x, wq = np.polynomial.legendre.leggauss(M)
    out = np.zeros((len(rho), NMAX), dtype=np.complex128)
    for lo, hi, wfun in pieces(family, d):
        u = 0.5 * (hi - lo) * x + 0.5 * (hi + lo)
        wt = 0.5 * (hi - lo) * wq * wfun(u)
        W = np.stack([wt * u ** j for j in range(NMAX)], axis=1)          # M x NMAX
        for k in range(0, len(rho), chunk):
            E = np.exp(np.outer(rho[k:k + chunk], u))                       # chunk x M
            out[k:k + chunk] += E @ W
    return out


def main():
    M = int(sys.argv[sys.argv.index('--nodes') + 1]) if '--nodes' in sys.argv else 2048
    gam = np.load(os.path.join(ROOT, 'tools', 'e16', 'zeta_ordinates.npy'))[:10000]
    N, Tmax = len(gam), float(gam[-1])
    rho = 0.5 + 1j * gam
    c = coeffs()
    rec('=' * 110)
    rec('b562 -- THE DRIFT ON THE BENCH (R172)(2). ### A MEASUREMENT AT xi, NOT A THEOREM; NOTHING ABOUT ZETA`S ZEROS IS CLAIMED.')
    rec('=' * 110)
    rec('### the bank: tools/e16/zeta_ordinates.npy, N = %d ordinates, the last T = %.6f ; the zeros taken as 1/2 + i gamma' % (N, Tmax))
    rec('### the families (as this instrument computes them):')
    rec('###   one-sided  f(u) = st(-u/d) on [-d, 0], 1 left, 0 right ; st = Mathlib`s Real.smoothTransition')
    rec('###   symmetric  f(u) = st(1/2 - u/d) on [-d/2, d/2] ; f(u) + f(-u) = 1, f(0) = %.3f' % float(st(np.array([0.5]))[0]))
    rec('### the member f e^{u/2} P_n(u), its transform at gamma_rho = int f P_n e^{rho u} du ; the left edge at -infinity')
    cost = N * M * (1 + 2) * len(DELTAS) * 2
    rec('### COMPUTE COST, PRINTED BEFORE THE RUN: %d zeros x %d Gauss-Legendre nodes x 3 transition pieces (1 one-sided + 2 symmetric)'
        ' x %d deltas x 2 (the node-doubling check at d = 0.1) = %.3e complex exponentials, in chunks of 1000 zeros' % (N, M, len(DELTAS), cost))
    t0 = time.time()
    # ### the paired Li sum over the bank, and the tails
    lam_N = np.array([np.sum(2 * np.real(1 - (1 - 1 / rho) ** n)) for n in range(0, NMAX + 1)])
    A = (math.log(Tmax / (2 * math.pi)) + 1) / (2 * math.pi * Tmax)
    tail_n2 = np.array([n * n * A for n in range(NMAX + 1)])
    tail_face = np.array([n * A for n in range(NMAX + 1)])
    bal = {1: 0.02309570896612103, 2: 0.09234573529135263, 3: 0.20763892059268, 4: 0.36879047952, 5: 0.57554271443,
           6: 0.827566012282, 7: 1.12446011757, 8: 1.46575567715, 10: 2.27933936319}
    rec('')
    rec('### (i) THE PAIRED LI SUM OVER THE BANK AGAINST BALPOS`S λ_n (BALPOS :291-:295 the literature column n <= 5; :303-:311 the margin n = 6..8, 10):')
    rec('###     the tail beyond T at on-line zeros: 2 Re liTerm ~ n^2/gamma^2, so T2(n) = n^2 (log(T/2pi) + 1)/(2 pi T) ; the face`s')
    rec('###     formula T1(n) = n (log(T/2pi) + 1)/(2 pi T) printed beside it (see the desk: the face wrote n where the order is n^2)')
    rec('    %3s %22s %14s %14s %22s %22s %12s' % ('n', 'Lambda_N(n)', 'T2(n)', 'T1(n)', 'Lambda_N + T2', 'BALPOS λ_n', 'resid (T2)'))
    for n in range(1, NMAX + 1):
        b = bal.get(n)
        rec('    %3d %22.15f %14.6e %14.6e %22.15f %22s %12s' % (n, lam_N[n], tail_n2[n], tail_face[n], lam_N[n] + tail_n2[n],
                                                           '%.15f' % b if b else '(not banked)', '%.3e' % (lam_N[n] + tail_n2[n] - b) if b else ''))
    res = {}
    for fam in ('one-sided', 'symmetric'):
        for d in DELTAS:
            ts = time.time()
            m = moments(rho, fam, d, M)
            Dn = np.array([0.0] + [float(np.sum(2 * np.real(m[:, :n] @ c[n, :n]))) for n in range(1, NMAX + 1)])
            mag = np.array([0.0] + [float(np.sum(np.abs(2 * np.real(m[:, :n] @ c[n, :n])))) for n in range(1, NMAX + 1)])
            res[(fam, d)] = dict(D=Dn.tolist(), mag=mag.tolist(), secs=time.time() - ts)
    # ### the node-doubling check at d = 0.1 (the most oscillatory transition)
    chk = {}
    for fam in ('one-sided', 'symmetric'):
        m2 = moments(rho, fam, 0.1, 2 * M)
        chk[fam] = [0.0] + [float(np.sum(2 * np.real(m2[:, :n] @ c[n, :n]))) for n in range(1, NMAX + 1)]
    secs = time.time() - t0
    rec('')
    rec('### (ii) THE DRIFT D(n, d) = Z(n, d) - Lambda_N(n), both families, n = 1..12 (quadrature floor: |D at %d nodes - D at %d| at d = 0.1):' % (M, 2 * M))
    for fam in ('one-sided', 'symmetric'):
        rec('  ### %s' % fam.upper())
        rec('    %3s ' % 'n' + ' '.join('%20s' % ('d = %g' % d) for d in DELTAS) + ' %14s %14s' % ('quad floor', 'eps sum|t|'))
        for n in range(1, NMAX + 1):
            qf = abs(res[(fam, 0.1)]['D'][n] - chk[fam][n])
            rec('    %3d ' % n + ' '.join('%20.12f' % res[(fam, d)]['D'][n] for d in DELTAS) + ' %14.3e %14.3e'
                % (qf, EPS * max(res[(fam, d)]['mag'][n] for d in DELTAS)))
    rec('')
    rec('### (iii) H13a -- THE ONE-SIDED SLOPE IN n (least squares of D(n, d) on n = 1..12, with intercept, and through the origin):')
    h13a = {}
    ns = np.arange(1, NMAX + 1, dtype=float)
    for d in DELTAS:
        y = np.array(res[('one-sided', d)]['D'][1:])
        s1, a1 = np.polyfit(ns, y, 1)
        s0 = float(np.dot(ns, y) / np.dot(ns, ns))
        resid = float(np.max(np.abs(y - (s1 * ns + a1))))
        pred = -0.5 * math.log(1 / d)
        rel = abs(s1 - pred) / abs(pred)
        ok = rel <= 0.10 and (s1 < 0) == (pred < 0)
        h13a[d] = dict(slope=float(s1), intercept=float(a1), slope0=s0, maxresid=resid, pred=pred, rel=float(rel), sign=bool(s1 < 0), holds=bool(ok))
        rec('    d = %-5g slope %+.6f (intercept %+.6f, max residual %.3e) ; through 0 %+.6f ; -(1/2) log(1/d) = %+.6f ; off by %.1f%% ; sign %s ; clause %s'
            % (d, s1, a1, resid, s0, pred, 100 * rel, 'agrees' if (s1 < 0) == (pred < 0) else 'OPPOSITE', 'HOLDS' if ok else 'REFUTED'))
    h13a_all = bool(all(v['holds'] for v in h13a.values()))
    rec('    ### ### **H13a (within 10%% at each d, the same sign): %s**' % ('HOLDS' if h13a_all else 'REFUTED'))
    rec('')
    rec('### (iv) H13b -- THE SYMMETRIC FAMILY:')
    mx = {d: float(np.max(np.abs(res[('symmetric', d)]['D'][1:]))) for d in DELTAS}
    sl = {d: float(np.polyfit(ns, np.array(res[('symmetric', d)]['D'][1:]), 1)[0]) for d in DELTAS}
    shrink = bool(mx[0.1] > mx[0.03] > mx[0.01])
    rec('    (b1) bounded in n, the bound shrinking: max_n |D| = %s ; shrinking across d = 0.1, 0.03, 0.01: %s'
        % (', '.join('%.3e (d=%g)' % (mx[d], d) for d in DELTAS), shrink))
    rec('    (b2) drift in n: the least-squares slope of D in n = %s' % ', '.join('%+.3e (d=%g)' % (sl[d], d) for d in DELTAS))
    rec('    (b3) the value against λ_n within floor, floor(n) = T2(n) + eps sum|terms| + quadrature floor; λ_n from BALPOS where banked, else'
        ' Lambda_N + T2 (then the test is |D| <= floor):')
    within = {}
    for d in DELTAS:
        row = []
        for n in range(1, NMAX + 1):
            lam = bal.get(n, lam_N[n] + tail_n2[n])
            z = lam_N[n] + tail_n2[n] + res[('symmetric', d)]['D'][n]
            qf = abs(res[('symmetric', 0.1)]['D'][n] - chk['symmetric'][n])
            fl = tail_n2[n] + EPS * res[('symmetric', d)]['mag'][n] + qf
            row.append(dict(n=n, z=float(z), lam=float(lam), diff=float(z - lam), floor=float(fl), ok=bool(abs(z - lam) <= fl)))
        within[d] = row
        rec('      d = %-5g within floor at n = %s ; beyond floor at n = %s' % (d, [r['n'] for r in row if r['ok']], [r['n'] for r in row if not r['ok']]))
        rec('        |Z - λ_n| / floor : ' + ' '.join('%d:%.2f' % (r['n'], abs(r['diff']) / r['floor']) for r in row))
    b3 = {d: bool(all(r['ok'] for r in within[d])) for d in DELTAS}
    rec('    ### ### **H13b: (b1) bounded and shrinking %s ; (b3) within floor at every n: %s**' % (shrink, ', '.join('%s (d=%g)' % (b3[d], d) for d in DELTAS)))
    rec('')
    rec('### (v) THE SEAT`S (S3): |D_symmetric| < |D_one-sided| at every n and d: %s'
        % all(abs(res[('symmetric', d)]['D'][n]) < abs(res[('one-sided', d)]['D'][n]) for d in DELTAS for n in range(1, NMAX + 1)))
    rec('### the run: %.1f s in all ; per family and d: %s' % (secs, ', '.join('%s d=%g %.1f s' % (f, d, res[(f, d)]['secs']) for (f, d) in res)))
    rec('=' * 110)
    io.open(os.path.join(D, 'b562_drift.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(N=N, T=Tmax, nodes=M, lam_N=lam_N.tolist(), tail_n2=tail_n2.tolist(), tail_face=tail_face.tolist(),
                   D={'%s|%g' % k: v for k, v in res.items()}, check=chk, h13a={str(k): v for k, v in h13a.items()}, h13a_holds=h13a_all,
                   sym_max={str(k): v for k, v in mx.items()}, sym_slope={str(k): v for k, v in sl.items()}, shrink=shrink,
                   within={str(d): within[d] for d in DELTAS}, b3={str(k): v for k, v in b3.items()}, secs=secs),
              io.open(os.path.join(D, 'b562_drift.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print('  written: b562_drift.txt, b562_drift.json')


if __name__ == '__main__':
    main()
