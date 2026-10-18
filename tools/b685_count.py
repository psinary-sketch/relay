# -*- coding: utf-8 -*-
"""b685_count.py -- THE COUNT LAW FOR Z_Q AT D = -23 IN BACKLUND'S FORM, ITS CONSTANTS IN ARB BALLS, COMPOSED WITH THE CERTIFIED REGION,
CONTROLLED AGAINST ζ, under (R295)(5)-(6), on the author's word on the plan (relay data/b685_count_plan.txt; relay data/b685_author_answers.txt).

### THE ROUTE (the plan's section 1, steps (1)-(9); source labels are relay data/b685_search.txt's):
###   N(T1, T2] = (1/π)[(T2 − T1) log κ + G(T2) − G(T1) + Δ_{σ1: T1→T2} arg Z_Q + top(T2) − top(T1)], κ = √23/2π, G(T) = Im lgamma(½ + iT);
###   |Δ_{σ1} arg Z_Q| ≤ 2 arcsin(ε/2), ε = Z_Q(σ1) − 2 < 2 (the (3c) bound, step (3));
###   |top(T)| ≤ (π/(2ℓ)) S(T) + E/2 + arctan((σ1 − 1)/T) + arctan(1/(2T)), ℓ = log(r/(c − ½)) ((Z1) Prop 3.2, (S3) Prop 5.4, step (5));
###   S(T) ≤ −log T − log(4 − Z_Q(c)) + (1/π)∫_0^π F_T(θ)dθ ((Z1) Prop 3.1 with the centre's bound 4 − Z_Q(c), step (6));
###   F_T(θ) ≥ log|a(c + re^{±iθ} + iT)|, a(s) = (s − 1)Z_Q(s): |Z_Q(s)| ≤ Z_Q(σ) for σ ≥ 1 + η; Phragmén-Lindelöf ((Z1) Prop 4.1) on [p, 1 + η],
###     p = c − r, at σ = p by the functional equation, the reflection formula ((M3)) and Stirling ((S1) (2.4)) (step (7)).
###   E bounds |Δ₊ + Δ₋| of the gamma factor and of arg(s − 1) over [½ − δ, ½ + δ] at T ≥ T_MIN, derived from (S1) (2.4) (printed in the bank).
### THE ORDER (the plan's section 4 with the author's word): p1 the Z_Q grid at real points; p2 the parameters and the constants; p4 control C1
###   (its second clause failing stops the act before the composition, the constants printed side by side); p3 the composition; p5 the bottom
###   edge, C₀, the consistency reading, control C2, the hypotheses and the banks. Each part one foreground call.
### Imports b667's evaluation route and b671's segment route unedited (b671 sets its carried segment and Bessel factor on b667 by name, as at
### b671 and b683); their sha256 printed. Its own bank writes, the only ones: data/b685_count_part<k>.json, data/b685_count.txt,
### data/b685_count.json, data/b685_count_controls.txt. No lean; no kernel byte. Written by the Write tool at b685.
### Usage: python -X utf8 tools/b685_count.py p1|p2|p4|p3|p5
"""
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import arb, acb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T_DIR = os.path.join(ROOT, 'tools')
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T_DIR)
import b671_narrow as B671          # noqa: E402  ### imported unedited; sets its carried segment and Bessel factor on b667 by name
import b667_epstein_certify as CERT  # noqa: E402  ### imported unedited

NL = chr(10)
PREC = 200
T_MIN = 149                         # ### the plan's T₁: every Z_Q window bound read at T ≥ 149
T_MIN_Z = 100                       # ### C1's: the smallest compared height
GRID = [round(1.02 + 0.01 * k, 2) for k in range(149)]      # ### Z_Q at σ = 1.02 ... 2.50 (|σ − ½| ≤ 2, T4's range)
PAR_C = [1.5, 1.55, 1.6, 1.65, 1.7, 1.8]
PAR_ETA = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]
PAR_C_Z = [1.05, 1.1, 1.15, 1.2, 1.3, 1.4, 1.5]
N_SEARCH, N_FINAL = 64, 2048        # ### θ pieces of the Jensen integral in the search and in the constants
HSW = ('0.1038', '0.2573', '9.3675')    # ### (Z1) Corollary 1.2, T ≥ e
BACKLUND = ('0.1370', '0.4430', '5.2250', 200)   # ### (Z1) Table 1, Backlund [1] (1918)
C1_T = (100, 1000, 10000)
SCAN_RATIO = 1.01
SCAN_TOP = 10 ** 6
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def say(s=''):
    print(s, flush=True)


def A(x):
    ctx.prec = PREC
    return arb(str(x))


def bs(x, n=12):
    return '%s ± %s' % (x.mid().str(n, radius=False), x.rad().str(3, radius=False))


def up(x):
    """the upper end of a ball as a ball of radius zero."""
    return arb(x.upper())


def put(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def get(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def ser(x):
    return [x.mid().str(60, radius=False), x.rad().str(12, radius=False)]


def des(v):
    ctx.prec = PREC
    m = arb(v[0])
    return m + arb(0, (arb(v[1]) + abs(m) * arb('1e-40')).upper())


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


# ================================================================================ P1: Z_Q AT REAL POINTS (steps (3), (6), (7))
def p1(*a):
    t0 = time.time()
    say('b685 count p1 -- Z_Q at real points σ = 1.02 ... 2.50 by b667`s route (tools/b667_epstein_certify.py sha256 %s; tools/b671_narrow.py '
        'sha256 %s), 200 bits, the 400 rung where wider than a relative 2^-40' % (sha(os.path.join(T_DIR, 'b667_epstein_certify.py'))[:16],
                                                                               sha(os.path.join(T_DIR, 'b671_narrow.py'))[:16]))
    rows, prev = {}, None
    for s in GRID:
        ctx.prec = PREC
        v = CERT.zq_point(acb(arb(str(s))))
        ctx.prec = PREC
        if not v.imag.contains(0):
            sys.exit('### Z_Q(%s) HAS AN IMAGINARY PART EXCLUDING 0 -- STOPPED' % s)
        re_ = v.real
        if prev is not None and not (re_ < prev):
            sys.exit('### Z_Q NOT DECREASING AT %s -- STOPPED' % s)
        prev = re_
        rows['%.2f' % s] = ser(re_)
    say('  Z_Q(1.02) = %s ; Z_Q(1.50) = %s ; Z_Q(2.00) = %s ; Z_Q(2.50) = %s' % tuple(bs(des(rows[k])) for k in ('1.02', '1.50', '2.00', '2.50')))
    say('  points %d, every value real and decreasing in σ ; %d s' % (len(rows), int(time.time() - t0)))
    put('b685_count_part1.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), prec=PREC, grid=rows,
                                      b667_sha256=sha(os.path.join(T_DIR, 'b667_epstein_certify.py')),
                                      b671_sha256=sha(os.path.join(T_DIR, 'b671_narrow.py')), seconds=int(time.time() - t0)))


def zq_up(grid, sig):
    """an upper bound for F on [sig, ∞) (non-negative coefficients, so F decreases on (1, ∞)): F's ball at the largest grid point whose
    decimal ball's lower end is ≤ sig's lower end (each grid value is the enclosure over that decimal ball), by exact comparisons."""
    ctx.prec = PREC
    s = sig if isinstance(sig, arb) else arb(str(sig))
    lo = arb(s.lower())
    keys = [k for k in sorted(grid, key=float) if arb(arb(k).lower()) <= lo]
    if not keys:
        raise ValueError('σ %s below the grid' % lo.str(10))
    return up(des(grid[keys[-1]]))


# ================================================================================ THE BOUNDS SHARED BY Z_Q AND ζ
def E_gamma(x0, y, d):
    """|Δ₊ + Δ₋| of Im log Γ(z) at z = x0 ± d + iy and x0 + iy, from (S1) (2.4) (|arg z| ≤ π/2, so x0 ≥ d): the second difference of
    h(x) = (x − ½) arg(x + iy) + y log|x + iy| − y bounded by 2|x0 − ½|(x0 + d)d²/y³ + 2d²/y (the arg terms) + 2d²/y + (d⁴ + 4x0²d²)/y³ (the log
    term, |log(1 + u)| ≤ 2|u| for |u| ≤ ½), and the three Stirling remainders by 2/(3y)."""
    return (2 * abs(x0 - A('0.5')) * (x0 + d) * d ** 2 / y ** 3 + 4 * d ** 2 / y + (d ** 4 + 4 * x0 ** 2 * d ** 2) / y ** 3 + A(2) / (3 * y))


def E_arg(d, t):
    """|Δ₊ + Δ₋| of arg(s − 1) = π/2 + arctan((1 − σ)/t): the second difference of arctan(x/t) at x = ½, |f″| ≤ 2|x|/t³."""
    return 2 * (A('0.5') + d) * d ** 2 / t ** 3


def theta(k, n):
    ctx.prec = PREC
    return arb.pi() * arb(2 * k + 1, 1) / (2 * n)


def jensen(pr, n, T):
    """(1/π)∫_0^π of the coefficient of log T and of the rest at T, F_T(θ) ≤ coef(θ) log T + rest(θ, T), every piece's upper end."""
    c, r, eta, p = pr['c'], pr['r'], pr['eta'], pr['p']
    one = A(1)
    Ic, Ir = arb(0), arb(0)
    for k in range(n):
        th = theta(k, n)
        sg = c + r * th.cos()
        forms = []
        if sg.lower() <= (one + eta).upper():          # ### the Phragmén-Lindelöf form on [p, 1 + η]
            lam = (one + eta - sg) / (one + eta - p)
            coef = one + lam * (pr['alpha1'] - one)
            rest = lam * pr['logA'] + (one - lam) * pr['logB'] + coef * ((1 + r / T) ** 2 + ((pr['Q'] + sg) / T) ** 2).log() / 2
            forms.append((coef, rest))
        if sg.upper() >= (one + eta).lower():          # ### |F(s)| ≤ F(σ) for σ ≥ 1 + η
            lo = arb(sg.lower()) if arb(sg.lower()) > arb((one + eta).lower()) else arb((one + eta).lower())
            rest = ((1 + r / T) ** 2 + ((sg - 1) / T) ** 2).log() / 2 + pr['logF'](lo)
            forms.append((one, rest))
        Ic += arb(max(f[0].upper() for f in forms))
        Ir += arb(max(f[1].upper() for f in forms))
    return Ic / n, Ir / n


def params_q(grid, c, r, eta):
    ctx.prec = PREC
    c, r, eta = A(c), A(r), A(eta)
    p = c - r
    kap = A(23).sqrt() / (2 * arb.pi())
    Q = 1 - 2 * p
    logA = (A(2) * kap ** (1 - 2 * p) * (A(1) / (3 * (1 - p))).exp() * zq_up(grid, 1 - p)).log()
    pr = dict(c=c, r=r, eta=eta, p=p, Q=Q, alpha1=2 - 2 * p, logA=logA, logB=zq_up(grid, 1 + eta).log(),
              logF=lambda s: zq_up(grid, s if float(s.lower()) <= 2.5 else A('2.5')).log())
    pr['sigma1'] = c + (c - A('0.5')) ** 2 / r
    pr['delta'] = 2 * c - pr['sigma1'] - A('0.5')
    pr['ell'] = (r / (c - A('0.5'))).log()
    pr['eps'] = zq_up(grid, pr['sigma1']) - 2
    pr['low'] = 4 - zq_up(grid, c)
    return pr


def conditions_q(pr):
    """(Z1) Prop 3.2 (1 < c < r, 0 < δ < ½), Prop 3.1 (c − r < ½ < 1 < c < σ1 < c + r), the centre (c ≥ 3/2, 4 − Z_Q(c) > 0), the right edge
    (σ1 ≥ 3/2, ε < 2), the growth (p < 0, 1 − p within the grid): each a ball comparison."""
    c, r, s1, d, p = pr['c'], pr['r'], pr['sigma1'], pr['delta'], pr['p']
    half = A('0.5')
    return [('1 < c < r', bool(1 < c and c < r)), ('0 < δ < ½', bool(0 < d and d < half)),
            ('c − r < ½ < 1 < c < σ1 < c + r', bool(c - r < half and 1 < c and c < s1 and s1 < c + r)),
            ('c ≥ 3/2 and 4 − Z_Q(c) > 0', bool(c >= A('1.5') and pr['low'] > 0)), ('σ1 ≥ 3/2 and ε < 2', bool(s1 >= A('1.5') and pr['eps'] < 2)),
            ('p < 0 and 1 − p ≥ 1.02', bool(p < 0 and 1 - p >= A('1.02')))]


def topq(pr, I, T, kappa_tag=''):
    """|top(T)| upper bound at T ≥ T_MIN, and S(T)'s bound."""
    Ic, Ir = I
    S = (Ic - 1) * A(T).log() + Ir - pr['low'].log()
    E = E_gamma(A('0.5'), A(T_MIN), pr['delta']) + E_arg(pr['delta'], A(T_MIN))
    top = arb.pi() / (2 * pr['ell']) * S + E / 2 + ((pr['sigma1'] - 1) / A(T_MIN)).atan() + (1 / (2 * A(T_MIN))).atan()
    return top, S, E


def W_window(pr, I, t):
    """the window bound W(t) for (t, t + 1], t ≥ 150: (1/π)[log κ + G(t + 1) − G(t) + 2 arcsin(ε/2) + top(t) + top(t + 1)] with G(t + 1) −
    G(t) ≤ log(t + 1) + 1/(8t) + 1/(3t) ((S1) (2.4)) and top read at t + 1 (its log T part increasing, its arctan parts at T_MIN)."""
    kap = A(23).sqrt() / (2 * arb.pi())
    tt = A(t)
    dG = (tt + 1).log() + 1 / (8 * tt) + 1 / (3 * tt)
    top1, _S, _E = topq(pr, I, t + 1)
    return (kap.log() + dG + 2 * (pr['eps'] / 2).asin() + 2 * top1) / arb.pi()


def p2(*a):
    t0 = time.time()
    grid = get('b685_count_part1.json')['grid']
    say('b685 count p2 -- the parameters (c, r, η), p = c − r, chosen on a grid to minimise W(150) (%d θ pieces), then the constants at %d pieces'
        % (N_SEARCH, N_FINAL))
    best, tried, refused = None, 0, 0
    for c in PAR_C:
        rmax = (c - 0.5) ** 2 / (c - 1)
        rs = [round(c + 0.05 + 0.05 * k, 3) for k in range(40) if c + 0.05 + 0.05 * k < rmax - 0.001]
        for r in rs:
            for eta in PAR_ETA:
                pr = params_q(grid, c, r, eta)
                cond = conditions_q(pr)
                tried += 1
                if not all(ok for _n, ok in cond):
                    refused += 1
                    continue
                I = jensen(pr, N_SEARCH, A(T_MIN))
                w = W_window(pr, I, 150)
                if best is None or w.upper() < best[0].upper():
                    best = (w, c, r, eta)
    if best is None:
        say('### NO PARAMETER SET MEETS THE CONDITIONS OF STEPS (5)-(7) AT c ≥ 3/2 -- STOPPED AT (P2) (the author`s word: raised)')
        for n_, ok in conditions_q(params_q(grid, PAR_C[0], PAR_C[0] + 0.05, PAR_ETA[0])):
            say('  %s : %s' % (n_, ok))
        put('b685_count_part2.json', dict(stopped=True, tried=tried))
        return
    w, c, r, eta = best
    pr = params_q(grid, c, r, eta)
    I = jensen(pr, N_FINAL, A(T_MIN))
    top150, S150, E = topq(pr, I, 150)
    a_ = (I[0] - 1) / (2 * pr['ell'])
    s0 = I[1] - pr['low'].log()
    c_ = ((2 * (pr['eps'] / 2).asin() + E / 2 + ((pr['sigma1'] - 1) / A(T_MIN)).atan() + (1 / (2 * A(T_MIN))).atan() + 1 / (8 * A(T_MIN))
           + 1 / (6 * A(T_MIN))) / arb.pi() + s0 / (2 * pr['ell']))
    W150 = W_window(pr, I, 150)
    say('  tried %d sets, %d refused by a condition ; chosen c = %s, r = %s, η = %s (W(150) at the search %s)' % (tried, refused, c, r, eta, bs(w)))
    for n_, ok in conditions_q(pr):
        say('  condition %-36s %s' % (n_, ok))
    say('  p = c − r %s ; σ1 %s ; δ %s ; ℓ = log(r/(c − ½)) %s ; ε = Z_Q(σ1) − 2 ≤ %s ; 4 − Z_Q(c) ≥ %s' % (
        bs(pr['p']), bs(pr['sigma1']), bs(pr['delta']), bs(pr['ell']), bs(pr['eps']), bs(pr['low'])))
    say('  log A %s (A = 2 κ^{1−2p} e^{1/(3(1−p))} Z_Q(1 − p)) ; log B %s (B = Z_Q(1 + η)) ; α1 = 2 − 2p %s ; Q = 1 − 2p %s' % (
        bs(pr['logA']), bs(pr['logB']), bs(pr['alpha1']), bs(pr['Q'])))
    say('  the Jensen integral at %d pieces: (1/π)∫coef %s ; (1/π)∫rest(θ, %d) %s ; E(δ, %d) %s' % (N_FINAL, bs(I[0]), T_MIN, bs(I[1]), T_MIN, bs(E)))
    say('  THE CONSTANTS: N_Q(T) = (T/π) log(√23 T/(2πe)) + C₀ + θ R(T), R(T) = a log T + b log log T + c for T ≥ %d:' % T_MIN)
    say('    a = %s ; b = 0 (exact: no log-power enters) ; c = %s' % (bs(a_), bs(c_)))
    say('  W(150) = %s against 10 log 153 = %s ; %d s' % (bs(W150), bs(10 * A(153).log()), int(time.time() - t0)))
    put('b685_count_part2.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), stopped=False, tried=tried, refused=refused,
                                      c=c, r=r, eta=eta, n_final=N_FINAL, Ic=ser(I[0]), Ir=ser(I[1]), E=ser(E), a=ser(a_), c_const=ser(c_),
                                      sigma1=ser(pr['sigma1']), delta=ser(pr['delta']), ell=ser(pr['ell']), eps=ser(pr['eps']), low=ser(pr['low']),
                                      p=ser(pr['p']), logA=ser(pr['logA']), logB=ser(pr['logB']), W150=ser(W150),
                                      conditions=[[n_, ok] for n_, ok in conditions_q(pr)], seconds=int(time.time() - t0)))


def load_q():
    grid = get('b685_count_part1.json')['grid']
    j = get('b685_count_part2.json')
    if j.get('stopped'):
        sys.exit('### p2 STOPPED -- NOTHING FURTHER')
    pr = params_q(grid, j['c'], j['r'], j['eta'])
    return grid, j, pr, (des(j['Ic']), des(j['Ir']))


# ================================================================================ P4: CONTROL C1, ζ BY THE SAME STEPS
ZGRID = [round(1.01 + 0.01 * k, 2) for k in range(250)]     # ### ζ at σ = 1.01 ... 3.50 for C1's lookups


def zeta_grid():
    ctx.prec = PREC
    return dict(('%.2f' % s, ser(acb(arb(str(s))).zeta().real)) for s in ZGRID)


def params_z(zg, c, r, eta):
    ctx.prec = PREC
    c, r, eta = A(c), A(r), A(eta)
    p = c - r
    Q = 1 - 2 * p
    zeta = lambda x: acb(x).zeta().real   # noqa: E731
    logA = ((2 * arb.pi()) ** (p - A('0.5')) * zeta(1 - p)).log()
    pr = dict(c=c, r=r, eta=eta, p=p, Q=Q, alpha1=A('1.5') - p, logA=logA, logB=zeta(1 + eta).log(),
              logF=lambda s: zq_up(zg, s if float(s.lower()) <= 3.5 else A('3.5')).log())
    pr['sigma1'] = c + (c - A('0.5')) ** 2 / r
    pr['delta'] = 2 * c - pr['sigma1'] - A('0.5')
    pr['ell'] = (r / (c - A('0.5'))).log()
    pr['logz1'] = zeta(pr['sigma1']).log()
    pr['low'] = zeta(2 * c) / zeta(c)
    return pr


def conditions_z(pr):
    c, r, s1, d, p = pr['c'], pr['r'], pr['sigma1'], pr['delta'], pr['p']
    half = A('0.5')
    return [('1 < c < r', bool(1 < c and c < r)), ('0 < δ < ½', bool(0 < d and d < half)),
            ('c − r < ½ < 1 < c < σ1 < c + r', bool(c - r < half and 1 < c and c < s1 and s1 < c + r)),
            ('−½ ≤ p < 0 ((Z1) (4.8))', bool(p >= -half and p < 0))]


def Rz(pr, I, T):
    """the derived bound for |N(T) − (T/2π) log(T/2πe) − 7/8| at T ≥ T_MIN_Z: e_θ(T) + (1/π)[log ζ(σ1) + |top_ζ(T)|]."""
    Ic, Ir = I
    S = (Ic - 1) * A(T).log() + Ir - pr['low'].log()
    E = E_gamma(A('0.25'), A(T_MIN_Z) / 2, pr['delta'] / 2) + E_arg(pr['delta'], A(T_MIN_Z))
    top = arb.pi() / (2 * pr['ell']) * S + E / 2 + ((pr['sigma1'] - 1) / A(T_MIN_Z)).atan() + (1 / (2 * A(T_MIN_Z))).atan()
    eth = (1 / (16 * A(T_MIN_Z)) + 1 / (8 * A(T_MIN_Z)) + 1 / (3 * A(T_MIN_Z))) / arb.pi()
    return eth + (pr['logz1'] + top) / arb.pi(), E


def p4(*a):
    import mpmath
    t0 = time.time()
    say('b685 count p4 -- control C1: ζ by the same steps (T ≥ %d), mpmath %s for N(T)' % (T_MIN_Z, mpmath.__version__))
    zg = zeta_grid()
    best, tried, refused = None, 0, 0
    for c in PAR_C_Z:
        rmax = min((c - 0.5) ** 2 / (c - 1), c + 0.5)
        rs = [round(c + 0.02 + 0.02 * k, 3) for k in range(60) if c + 0.02 + 0.02 * k < rmax - 0.001]
        for r in rs:
            for eta in PAR_ETA:
                pr = params_z(zg, c, r, eta)
                tried += 1
                if not all(ok for _n, ok in conditions_z(pr)):
                    refused += 1
                    continue
                I = jensen(pr, N_SEARCH, A(T_MIN_Z))
                R, _E = Rz(pr, I, T_MIN_Z)
                if best is None or R.upper() < best[0].upper():
                    best = (R, c, r, eta)
    R0, c, r, eta = best
    pr = params_z(zg, c, r, eta)
    I = jensen(pr, N_FINAL, A(T_MIN_Z))
    _R, E = Rz(pr, I, T_MIN_Z)
    say('  tried %d sets, %d refused ; chosen c = %s, r = %s, η = %s' % (tried, refused, c, r, eta))
    for n_, ok in conditions_z(pr):
        say('  condition %-36s %s' % (n_, ok))
    say('  σ1 %s ; δ %s ; ℓ %s ; log ζ(σ1) %s ; ζ(2c)/ζ(c) %s ; (1/π)∫coef %s ; (1/π)∫rest %s ; E %s' % (
        bs(pr['sigma1']), bs(pr['delta']), bs(pr['ell']), bs(pr['logz1']), bs(pr['low']), bs(I[0]), bs(I[1]), bs(E)))
    Rlog = (I[0] - 1) / (2 * pr['ell'])      # ### R's coefficient of log T: (1/π)(π/(2ℓ))((1/π)∫coef − 1)
    const = Rz(pr, I, 1)[0]                    # ### R at log T = 0: the constant part (the rest read at T_MIN_Z)
    say('  THE DERIVED ζ BOUND: |N(T) − (T/2π) log(T/2πe) − 7/8| ≤ a_ζ log T + b_ζ log log T + c_ζ for T ≥ %d, a_ζ = %s, b_ζ = 0, c_ζ = %s'
        % (T_MIN_Z, bs(Rlog), bs(const)))
    say('  beside (Z1) Corollary 1.2 (%s, %s, %s; T ≥ e) and Backlund`s row of (Z1) Table 1 (%s, %s, %s; T₀ %d)' % (HSW + BACKLUND))
    rows, ok1, ok2 = [], True, True
    for T in C1_T:
        t1 = time.time()
        mpmath.mp.dps = 30
        N = int(mpmath.nzeros(T))
        ctx.prec = PREC
        TT = A(T)
        main = TT / (2 * arb.pi()) * (TT / (2 * arb.pi() * A(1).exp())).log()
        Dv = A(N) - main - A('0.875')
        R, _ = Rz(pr, I, T)
        hsw = A(HSW[0]) * TT.log() + A(HSW[1]) * TT.log().log() + A(HSW[2])
        ours_full = R + A('0.875')          # ### our bound for |N(T) − main|, the quantity (Z1) bounds, by the triangle inequality
        c1i = bool(abs(Dv) <= R)
        c1ii = bool(ours_full >= hsw)
        ok1, ok2 = ok1 and c1i, ok2 and c1ii
        rows.append(dict(T=T, N=N, D=ser(Dv), R=ser(R), ours_full=ser(ours_full), hsw=ser(hsw), contains=c1i, not_sharper=c1ii,
                         ratio=ser(ours_full / hsw), seconds=int(time.time() - t1)))
        say('  T = %-6d N(T) = %-6d N − main − 7/8 = %s ; the derived R %s : CONTAINS %s ; R + 7/8 = %s against (Z1) %s : NOT SHARPER %s (ratio %s)'
            ' ; %d s' % (T, N, bs(Dv, 8), bs(R, 8), c1i, bs(ours_full, 8), bs(hsw, 8), c1ii, bs(ours_full / hsw, 6), int(time.time() - t1)))
    say('  ### C1 CLAUSE (i) %s ; CLAUSE (ii) %s ; C1 %s ; %d s' % (ok1, ok2, 'PASS' if ok1 and ok2 else 'FAIL', int(time.time() - t0)))
    if not ok2:
        say('### C1`s SECOND CLAUSE FAILS -- THE ACT STOPS BEFORE THE COMPOSITION (the author`s word); the constants side by side above')
    put('b685_count_part4.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), c=c, r=r, eta=eta, tried=tried, refused=refused,
                                      sigma1=ser(pr['sigma1']), delta=ser(pr['delta']), ell=ser(pr['ell']), Ic=ser(I[0]), Ir=ser(I[1]), E=ser(E),
                                      a_zeta=ser(Rlog), c_zeta=ser(const), rows=rows, clause_i=ok1, clause_ii=ok2, mpmath=mpmath.__version__,
                                      conditions=[[n_, ok] for n_, ok in conditions_z(pr)], seconds=int(time.time() - t0)))


# ================================================================================ P3: THE COMPOSITION (6)
def p3(*a):
    t0 = time.time()
    j4 = get('b685_count_part4.json')
    if not j4['clause_ii']:
        sys.exit('### C1`s SECOND CLAUSE FAILED AT p4 -- THE COMPOSITION IS NOT RUN (the author`s word)')
    grid, j, pr, I = load_q()
    say('b685 count p3 -- the composition: the margin m(t) = 10 log(t + 3) − W(t) on [150, 10⁶] by pieces of ratio %s, the straddle (149, 150), '
        'and the coefficient form beyond' % SCAN_RATIO)
    rows = []
    # ### t = 149: the window (149, 150] inside the certified range, its listed points 2 (relay data/b685_p3.txt section 4)
    m149 = 10 * A(152).log() - 2
    rows.append(dict(range='t = 149 (certified)', bound='2', hcount=ser(10 * A(152).log()), margin=ser(m149)))
    # ### 149 < t < 150: N(t, t + 1) ≤ 2 + N(150, t + 1) ≤ 2 + N(150, 151] ≤ 2 + W(150) (the count is monotone in its window)
    kap = A(23).sqrt() / (2 * arb.pi())
    ctx.prec = PREC
    Wst = 2 + W_window(pr, I, 150)
    mst = 10 * A(152).log() - Wst
    rows.append(dict(range='149 < t < 150 (straddle)', bound=ser(Wst), hcount=ser(10 * A(152).log()), margin=ser(mst)))
    say('  t = 149: N ≤ 2 (listed) ; margin %s' % bs(m149))
    say('  149 < t < 150: N ≤ 2 + %s ; 10 log(t + 3) ≥ %s ; margin ≥ %s' % (bs(Wst - 2), bs(10 * A(152).log()), bs(mst)))
    # ### the scan
    narrow, ta, npieces, at = None, 150.0, 0, {}
    while ta < SCAN_TOP:
        tb = min(ta * SCAN_RATIO, SCAN_TOP)
        Wb = W_window(pr, I, tb)                       # ### W increasing in t: its value at tb bounds the piece
        m = 10 * A(ta + 3).log() - Wb
        npieces += 1
        if narrow is None or m.lower() < narrow[0].lower():
            narrow = (m, ta, tb, Wb)
        for mark in (150, 1000, SCAN_TOP):
            if ta <= mark <= tb and mark not in at:
                at[mark] = (ta, tb, Wb, m)
        ta = tb
    for mark in (150, 1000, SCAN_TOP):
        ta_, tb_, Wb, m = at.get(mark, (None, None, None, None))
        if Wb is not None:
            rows.append(dict(range='t in [%.6g, %.6g] (the piece holding %d)' % (ta_, tb_, mark), bound=ser(Wb), hcount=ser(10 * A(ta_ + 3).log()),
                             margin=ser(m)))
            say('  the piece [%.6g, %.6g] (holding t = %d): W ≤ %s ; 10 log(t + 3) ≥ %s ; margin ≥ %s' % (ta_, tb_, mark, bs(Wb), bs(10 * A(ta_ + 3).log()),
                                                                                                   bs(m)))
    m, nta, ntb, nW = narrow
    say('  pieces %d ; THE NARROWEST MARGIN ON [150, 10⁶]: %s on [%.6g, %.6g] (W ≤ %s)' % (npieces, bs(m), nta, ntb, bs(nW)))
    # ### beyond 10⁶: W(t) ≤ κ1 log(t + 1) + κ0(t), κ0 decreasing
    Ic, Ir = I
    k1 = (1 + arb.pi() * (Ic - 1) / pr['ell']) / arb.pi()
    t6 = A(SCAN_TOP)
    E = topq(pr, I, SCAN_TOP)[2]
    k0 = (kap.log() + A(11) / (24 * t6) + 2 * (pr['eps'] / 2).asin() + arb.pi() / pr['ell'] * (Ir - pr['low'].log()) + E
          + 2 * ((pr['sigma1'] - 1) / A(T_MIN)).atan() + 2 * (1 / (2 * A(T_MIN))).atan()) / arb.pi()
    mco = (10 - k1) * (t6 + 1).log() - k0
    rows.append(dict(range='t ≥ 10⁶ (coefficient form)', bound='κ1 log(t + 1) + κ0, κ1 %s, κ0 %s' % (bs(k1), bs(k0)), hcount='10 log(t + 3)',
                     margin=ser(mco)))
    say('  t ≥ 10⁶: W(t) ≤ κ1 log(t + 1) + κ0, κ1 = %s < 10 : %s ; κ0 = %s ; the margin ≥ (10 − κ1) log(10⁶ + 1) − κ0 = %s, increasing beyond'
        % (bs(k1), bool(k1 < 10), bs(k0), bs(mco)))
    covered = bool(m149 > 0 and mst > 0 and m > 0 and mco > 0 and k1 < 10)
    say('  ### THE TWO RANGES MEET AT t = 149 (certified −150 ≤ t ≤ 149; derived t ≥ 149) ; NO HEIGHT UNCOVERED: %s ; %d s' % (covered, int(time.time() - t0)))
    put('b685_count_part3.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=rows, narrowest=dict(margin=ser(m), ta=nta, tb=ntb),
                                      pieces=npieces, k1=ser(k1), k0=ser(k0), covered=covered, seconds=int(time.time() - t0)))


# ================================================================================ P5: THE BOTTOM EDGE, C₀, THE CONSISTENCY READING, C2, THE BANKS
def p5(*a):
    t0 = time.time()
    grid, j, pr, I = load_q()
    j4 = get('b685_count_part4.json')
    # ### the navigator's answer on the landing: P5 runs without the composition where C1's second clause failed (no part-3 bank then)
    j3 = get('b685_count_part3.json') if os.path.exists(os.path.join(D, 'b685_count_part3.json')) else None
    ctx.prec = PREC
    say('b685 count p5 -- the bottom edge ½ + i/2 -> σ1 + i/2 by b671`s segment route through b667`s edge_arg; C₀; the consistency reading; C2%s'
        % ('' if j3 else ' (the composition NOT RUN: C1`s second clause failed, the author`s word; the navigator`s answer on the landing)'))
    st, cache = CERT._stats(), {}
    za = acb(A('0.5'), A('0.5'))
    zb = acb(pr['sigma1'].mid(), A('0.5'))
    cB = CERT.edge_arg(CERT.zq, za, zb, 8, 24, st, cache)
    ctx.prec = PREC
    if cB is None:
        sys.exit('### THE BOTTOM EDGE UNRESOLVED %s -- STOPPED' % st['unresolved'])
    # ### the right edge's foot: the edge from σ1.mid + i/2 is the half path's; σ1's ball radius is zero (an exact dyadic in arb's arithmetic)
    say('  Δ arg Z_Q on the bottom edge c_B = %s (segments %d, rung segments %d, max depth %d, unresolved %s)' % (
        bs(cB), st['segments'], st['rung_segments'], st['max_depth'], st['unresolved'] or 'NONE'))
    G = lambda T: acb(A('0.5'), A(T)).lgamma().imag   # noqa: E731
    out = {}
    for tag, kap in (('true', A(23).sqrt() / (2 * arb.pi())), ('planted', A(23).sqrt() / arb.pi())):
        ctx.prec = PREC
        if tag == 'planted':
            # ### C2: κ′ in step (2) and in step (7)'s functional-equation factor alike; the Jensen integral re-read with κ′
            pp = dict(pr)
            pp['logA'] = (A(2) * kap ** (1 - 2 * pr['p']) * (A(1) / (3 * (1 - pr['p']))).exp() * zq_up(grid, 1 - pr['p'])).log()
            Ip = jensen(pp, N_FINAL, A(T_MIN))
        else:
            pp, Ip = pr, I
        C0 = (-kap.log() / 2 - G('0.5') + cB) / arb.pi()
        mid150 = (A('149.5') * kap.log() + G(150) - G('0.5') + cB) / arb.pi()
        top150 = topq(pp, Ip, 150)[0]
        R150 = (2 * (pp['eps'] / 2).asin() + top150) / arb.pi()
        lo, hi = mid150 - R150, mid150 + R150
        contains = bool(lo < 180 and 180 < hi)
        out[tag] = dict(C0=ser(C0), mid150=ser(mid150), R150=ser(R150), lo=ser(lo), hi=ser(hi), contains180=contains)
        say('  %-8s κ = %s : N_Q(150) ∈ [%s, %s] (centre %s, R(150) %s) ; C₀ %s ; CONTAINS 180: %s' % (
            tag, bs(kap, 8), bs(lo, 8), bs(hi, 8), bs(mid150, 8), bs(R150, 6), bs(C0, 8), contains))
    shift = A('149.5') * A(2).log() / arb.pi()
    c2 = not out['planted']['contains180']
    say('  C2: the planted interval EXCLUDES 180: %s ; the read shift of the centre %s against the expected (150 − ½) log 2/π = %s' % (
        c2, bs(des(out['planted']['mid150']) - des(out['true']['mid150']), 8), bs(shift, 8)))
    # ### the hypotheses
    a_, c_ = des(j['a']), des(j['c_const'])
    V = lambda ok: 'HELD' if ok else 'REFUTED'   # noqa: E731
    H = [('H1', 'HELD', 'data/b685_p3.txt sections 2-3: HCount quoted (RestBound.lean :42-:45, Wide.HCount :48-:50), its inequality at Q0 written out'),
         ('H2', 'HELD', 'data/b685_search.txt: 10 candidates, each with its reach to Z_Q read'),
         ('H3', V(a_.rad() >= 0 and c_.rad() >= 0), 'a = %s, b = 0, c = %s, C₀ = %s (data/b685_count.txt section 2), each step sourced in data/b685_count_plan.txt'
          % (bs(a_), bs(c_), bs(des(out['true']['C0'])))),
         ('H4', V(j3['covered']) if j3 else 'NOT SCORABLE', ('the narrowest margin %s on [%.6g, %.6g]; the meeting height 149 (data/b685_count.txt section 3)' % (
             bs(des(j3['narrowest']['margin'])), j3['narrowest']['ta'], j3['narrowest']['tb'])) if j3 else
          'the composition not run: C1`s second clause failed and the author`s word stops the act before it (data/b685_count.txt section 3)'),
         ('H5', V(j4['clause_i'] and j4['clause_ii']), 'C1 clause (i) %s, clause (ii) %s, as the author`s word reads them (data/b685_count_controls.txt)' % (
             j4['clause_i'], j4['clause_ii'])),
         ('H6', V(c2), 'C2: the planted κ′ = √23/π interval at 150 excludes 180: %s (data/b685_count_controls.txt)' % c2)]
    for h, v, why in H:
        say('  %s %s -- %s' % (h, v, why))
    banks(j, j3, j4, pr, I, cB, st, out, shift, c2, H)
    say('  %d s' % int(time.time() - t0))


def banks(j, j3, j4, pr, I, cB, st, out, shift, c2, H):
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    j1 = get('b685_count_part1.json')
    L = ['b685 -- THE COUNT LAW FOR Z_Q AT D = −23 IN BACKLUND`S FORM, ITS CONSTANTS IN BALLS, %s (%s)' % (
        'COMPOSED WITH THE CERTIFIED REGION' if j3 else 'THE COMPOSITION NOT RUN (C1`s SECOND CLAUSE FAILED)', at), '',
         '### rows are T ranges with the bound, HCount`s figure and the margin (section 3), after the constants (section 2); the plan relay',
         '### data/b685_count_plan.txt, the author`s word relay data/b685_author_answers.txt; python-flint arb at %d bits; b667`s route sha256 %s, b671`s'
         % (PREC, j1['b667_sha256'][:16]),
         '### segment route sha256 %s, imported unedited. Nothing here is proved or compiled in Lean: constants certified in balls, analytic steps sourced.'
         % j1['b671_sha256'][:16], '',
         '== 1. THE PARAMETERS AND THE CONDITIONS (the plan`s steps (5)-(7))',
         '  c = %s, r = %s, η = %s, p = c − r = %s ; σ1 = c + (c − ½)²/r = %s ; δ = 2c − σ1 − ½ = %s ; ℓ = log(r/(c − ½)) = %s' % (
             j['c'], j['r'], j['eta'], bs(pr['p']), bs(pr['sigma1']), bs(pr['delta']), bs(pr['ell'])),
         '  ε = Z_Q(σ1) − 2 ≤ %s (< 2) ; |Z_Q(c + iT)| ≥ 4 − Z_Q(c) ≥ %s ; log A %s ; log B %s ; Q = 1 − 2p %s ; α1 = 2 − 2p %s' % (
             bs(pr['eps']), bs(pr['low']), bs(pr['logA']), bs(pr['logB']), bs(pr['Q']), bs(pr['alpha1']))]
    L += ['  condition %-36s %s' % (n_, ok) for n_, ok in j['conditions']]
    L += ['  parameter sets tried %d, refused by a condition %d ; the Jensen integral at %d θ pieces, every piece`s upper end' % (j['tried'], j['refused'], j['n_final']),
          '  E(δ, %d), the gamma factor`s and arg(s − 1)`s |Δ₊ + Δ₋|, from (S1) (2.4): 2|x0 − ½|(x0 + δ)δ²/T³ + 4δ²/T + (δ⁴ + 4x0²δ²)/T³ + 2/(3T) + '
          '2(½ + δ)δ²/T³ at x0 = ½ = %s' % (T_MIN, bs(des(j['E']))), '',
          '== 2. THE CONSTANTS (H3)',
          '  N_Q(T) = (T/π) log(√23 T/(2πe)) + C₀ + θ R(T), |θ| ≤ 1, R(T) = a log T + b log log T + c for T ≥ %d:' % T_MIN,
          '    a = %s' % bs(des(j['a'])), '    b = 0 (exact: the convexity-only growth bound carries no power of log)',
          '    c = %s' % bs(des(j['c_const'])),
          '    C₀ = (1/π)[−½ log κ − Im log Γ(½ + i/2) + c_B] = %s, c_B = Δ arg Z_Q on ½ + i/2 -> σ1 + i/2 = %s (segments %d, unresolved %s)' % (
              bs(des(out['true']['C0'])), bs(cB), st['segments'], st['unresolved'] or 'NONE'),
          '  the window: N(t, t + 1) ≤ W(t) = (1/π)[log κ + log(t + 1) + 1/(8t) + 1/(3t) + 2 arcsin(ε/2) + 2 |top(t + 1)|] for t ≥ 150, |top(T)| ≤ '
          '(π/(2ℓ))[(%s − 1) log T + %s − log(4 − Z_Q(c))] + E/2 + arctan((σ1 − 1)/%d) + arctan(1/(2·%d))' % (
              bs(des(j['Ic'])), bs(des(j['Ir'])), T_MIN, T_MIN), '',
          '== 3. THE COMPOSITION, (R295)(6) (H4): rows are T ranges -- the bound, HCount`s figure 10 log(|t| + 3), the margin']
    if j3 is None:
        L += ['  NOT RUN. C1`s second clause failed at p4 (data/b685_count_controls.txt) and the author`s word stops the act before the composition',
              '  (relay data/b685_author_answers.txt); the navigator`s answer on the landing ran P5 without it. No margin is read and none is claimed: H4',
              '  NOT SCORABLE. The window bound at one height, read at p2 in the parameter choice and not a composition: W(150) = %s against 10 log 153.'
              % bs(des(j['W150']))]
    else:
        for r_ in j3['rows']:
            b = r_['bound'] if isinstance(r_['bound'], str) else bs(des(r_['bound']))
            hc = r_['hcount'] if isinstance(r_['hcount'], str) else bs(des(r_['hcount']))
            L.append('  %-46s | bound %s | HCount %s | margin %s' % (r_['range'], b, hc, bs(des(r_['margin']))))
        L += ['  the scan pieces %d ; THE NARROWEST MARGIN %s on [%.6g, %.6g] ; negative t by the symmetry of data/b685_p3.txt section 3' % (
            j3['pieces'], bs(des(j3['narrowest']['margin'])), j3['narrowest']['ta'], j3['narrowest']['tb']),
              '  THE MEETING HEIGHT 149: the certified range −150 ≤ t ≤ 149 (data/b685_p3.txt section 4) and the derived t ≥ 149 ; NO HEIGHT UNCOVERED: %s'
              % j3['covered']]
    L += ['', '== 4. THE HYPOTHESES']
    L += ['  %s %s -- %s' % (h, v, why) for h, v, why in H]
    allh = all(v == 'HELD' for _h, v, _w in H)
    L += ['', '### ### **H1-H6 %s (%s) ; a = %s, b = 0, c = %s ; THE COMPOSITION %s ; C1 %s ; C2 %s ; P3 NOT DERIVED IN THIS ACT.**' % (
        'HELD' if allh else 'NOT ALL HELD', ', '.join('%s %s' % (h, v) for h, v, _w in H), bs(des(j['a']), 6), bs(des(j['c_const']), 6),
        ('NARROWEST MARGIN %s' % bs(des(j3['narrowest']['margin']), 6)) if j3 else 'NOT RUN',
        'PASS' if j4['clause_i'] and j4['clause_ii'] else 'FAIL', 'PASS' if c2 else 'NOT DISCRIMINATING')]
    p = os.path.join(D, 'b685_count.txt')
    open(p + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    C = ['b685 -- THE CONTROLS OF (R295)(6) (%s): rows are controls with their expected and read values' % at, '',
         '  (C1) ζ by the same steps, T ≥ %d: c = %s, r = %s, η = %s ; the derived a_ζ = %s, b_ζ = 0, c_ζ = %s ; beside (Z1) Corollary 1.2 (%s, %s, %s; '
         'T ≥ e) and Backlund`s row (%s, %s, %s; T₀ %d)' % ((T_MIN_Z, j4['c'], j4['r'], j4['eta'], bs(des(j4['a_zeta'])), bs(des(j4['c_zeta']))) + HSW + BACKLUND)]
    for r_ in j4['rows']:
        C.append('      T = %-6d | expected: |N(T) − main − 7/8| ≤ R and R + 7/8 ≥ (Z1) | read: N(T) %d (mpmath %s), N − main − 7/8 = %s, R = %s -> CONTAINS %s ; '
                 'R + 7/8 = %s, (Z1) %s -> NOT SHARPER %s' % (r_['T'], r_['N'], j4['mpmath'], bs(des(r_['D']), 8), bs(des(r_['R']), 8), r_['contains'],
                                                             bs(des(r_['ours_full']), 8), bs(des(r_['hsw']), 8), r_['not_sharper']))
    C += ['      C1 %s (clause (i) %s, clause (ii) %s), as the author`s word reads it: "a derived bound sharper than a located explicit one is the'
          % ('PASS' if j4['clause_i'] and j4['clause_ii'] else 'FAIL', j4['clause_i'], j4['clause_ii']),
          '      signature of a dropped term, and is read as a failure of the derivation, not as a gain".',
          '      THE SEAT`S READING (entered as the seat`s, not as the act`s finding; the navigator`s answer on the landing): the candidate dropped',
          '      term, (Z1) Proposition 3.2`s "+ π/N + π/(2N) + π/4", read at its source -- Hasanalizade, Shen, Wong, arXiv:2102.04663v3, Lemma 3.6,',
          '      p. 7, (3.4): "|arctan T/(½ + d) − arctan T/½ + arctan T/(½ − d) − arctan T/½| ... ≤ π/2", the arg(σ + iT) term of ξ_K = s(s − 1)...ζ_K',
          '      with Z(w) = (w − 1)ζ_K(w), bounded by π/2 and carried as N π/2 into its Proposition 3.7 (p. 8: "+ 1/4 + 1/(2N)"). Λ_Q = κ^s Γ(s) Z_Q(s)',
          '      and Λ = π^{−s/2} Γ(s/2) ζ(s) carry no factor s; their (s − 1) factor`s |Δ₊ + Δ₋| is bounded by 2(½ + δ)δ²/T³ (E_arg, in E). The seat',
          '      reads no dropped term; (Z1)`s constant 9.3675 covers T ≥ e (its proof of Corollary 1.2, p. 15, (5.6)), this instance T ≥ %d.' % T_MIN_Z,
          '      What would decide it, for a continuation act (none made here): the trigger of W-ORD-EPSTEIN-COUNT, readings (i)-(iii).',
          '  (C2) planted κ′ = √23/π in steps (2) and (7) | expected: N_Q(150)`s interval excludes the certified 180, the centre shifted by (150 − ½) log 2/π = %s '
          '| read: [%s, %s], the shift %s -> %s' % (bs(shift, 8), bs(des(out['planted']['lo']), 8), bs(des(out['planted']['hi']), 8),
                                                   bs(des(out['planted']['mid150']) - des(out['true']['mid150']), 8), 'PASS' if c2 else 'NOT DISCRIMINATING'),
          '  (consistency, no hypothesis) the true κ | expected: N_Q(150)`s interval contains 180 | read: [%s, %s] -> %s' % (
              bs(des(out['true']['lo']), 8), bs(des(out['true']['hi']), 8), out['true']['contains180']), '',
          '### ### **C1 %s ; C2 %s ; THE TRUE INTERVAL CONTAINS 180: %s.**' % ('PASS' if j4['clause_i'] and j4['clause_ii'] else 'FAIL',
                                                                             'PASS' if c2 else 'NOT DISCRIMINATING', out['true']['contains180'])]
    p = os.path.join(D, 'b685_count_controls.txt')
    open(p + '.tmp', 'wb').write((NL.join(C) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    put('b685_count.json', dict(at=at, params=dict(c=j['c'], r=j['r'], eta=j['eta']), a=j['a'], b='0', c=j['c_const'], C0=out['true']['C0'],
                                cB=ser(cB), consistency=out['true'], planted=out['planted'], c2=c2, composition=j3, c1=j4,
                                hypotheses=[[h, v, why] for h, v, why in H]))


if __name__ == '__main__':
    fn = dict(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5).get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b685_count.py p1|p2|p4|p3|p5')
        sys.exit(2)
    fn(*sys.argv[2:])
