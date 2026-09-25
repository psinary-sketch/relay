# -*- coding: utf-8 -*-
"""b523_caveats.py -- THE WITNESS'S THREE CAVEATS PRICED. ### `python tools/b523_caveats.py sigma | count | reread`

### (1) sigma_max: Z_Q0(s) = SUM r(n) n^{-s}, r(1) = 2; for Re s = sigma, |Z - 2| <= eta(sigma) = SUM_{n>=2} r(n) n^{-sigma};
###     eta < 2 forbids a zero. r(n) exact to N0 (b325`s own counter); above N0, r(n) <= 2 a(n), a(n) = SUM_{d|n} chi(d),
###     chi = (./23) -- the three reduced forms of disc -23 together represent n exactly 2 a(n) times (checked to N0) --
###     and SUM_{n>N0} a(n) n^{-sigma} = zeta(sigma) L(sigma, chi) - SUM_{n<=N0} a(n) n^{-sigma}.
### (2) the tail of b521 with the off-line allowance at s_max = sigma_max - 1/2 in place of 1/2 (b521`s closed form).
### (3) N(T) <= M0(T) + E(T) for T >= 150, by the argument principle on the box and Backlund`s count of sign changes
###     (Jensen), the growth off the line by Rademacher`s Phragmen-Lindelof between Re s = -eta and 1 + eta; the tail
###     re-priced by parts: SUM_{gamma>T} f = -f(T) N(T) + INT N (-f') <= 2 x [INT f dM0 + f(T)(M0(T) + E(T) - N_bank(T))
###     + e1 INT f / t], N(T) >= N_bank(T) (the bank`s count, complete below 150 by b506).
### (4) the u > 1200 shortfall against each negative cell`s margin.
"""
import io
import json
import math
import os
import sys

import mpmath as mp
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T_ = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T_)
import b325_epstein as EP   # noqa: E402
import b511_families as F   # noqa: E402
import b521_tail as B21     # noqa: E402

NL = chr(10)
N0 = 10 ** 6
TOP = 150.0
P = 7
C23 = math.sqrt(23.0) / (2.0 * math.pi)
STIRLING_PAD = 0.01          # ### |M_exact - M0| allowance, checked on a grid in `count`
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def chi(n):
    m = n % 23
    if m == 0:
        return 0
    return 1 if pow(m, 11, 23) == 1 else -1


def tables():
    r = np.array(EP.rep_counts(N0), dtype=float)
    a = np.zeros(N0 + 1)
    for d in range(1, N0 + 1):
        c = chi(d)
        if c:
            a[d::d] += c
    return r, a


def forms_total(K):
    """### the three reduced forms of disc -23 -- x^2+xy+6y^2, 2x^2+xy+3y^2, 2x^2-xy+3y^2 -- their summed counts to K."""
    t = np.zeros(K + 1)
    for (A, B, C) in ((1, 1, 6), (2, 1, 3), (2, -1, 3)):
        ym = int(2 * math.sqrt(A * K / 23.0)) + 2
        xm = int(math.sqrt(K)) + ym + 2
        for y in range(-ym, ym + 1):
            for x in range(-xm, xm + 1):
                k = A * x * x + B * x * y + C * y * y
                if 1 <= k <= K:
                    t[k] += 1
    return t


CHI = [chi(n) for n in range(23)]


def eta_bound(sig, r, a):
    n = np.arange(2, N0 + 1, dtype=float)
    head = float(np.sum(r[2:] * n ** (-sig)))
    part = float(np.sum(a[1:] * np.arange(1, N0 + 1, dtype=float) ** (-sig)))
    full = float(mp.zeta(sig) * mp.dirichlet(sig, CHI))
    return head + 2.0 * (full - part), head, full - part


def sigma():
    r, a = tables()
    K = 20000
    ft = forms_total(K)
    eq = bool(np.all(ft[1:] == 2 * a[1:K + 1]))
    dom = bool(np.all(r[1:] <= 2 * a[1:] + 1e-9))
    lo, hi = 1.05, 4.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if eta_bound(mid, r, a)[0] < 2.0:
            hi = mid
        else:
            lo = mid
    smax = math.ceil(hi * 1000) / 1000.0
    e, head, tail = eta_bound(smax, r, a)
    below = eta_bound(smax - 0.01, r, a)[0]
    offb = max(b for b, g in F.OFFQ)
    res = dict(N0=N0, sigma_max=smax, eta_at=e, head=head, tail_bound=2 * tail, eta_below=below, forms_equal_2a_to=K if eq else None,
               r_le_2a_to_N0=dom, bank_max_real_part=offb, control=offb < smax, r2=int(r[2]), r4=int(r[4]), r6=int(r[6]),
               zetaL=float(mp.zeta(smax) * mp.dirichlet(smax, CHI)))
    for s in (1.2, 1.5, 2.0, 2.5):
        res['eta_%.1f' % s] = eta_bound(s, r, a)[0]
    io.open(os.path.join(D, 'b523_sigma.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('  three forms sum to 2 a(n) for n <= %d : %s ; r(n) <= 2 a(n) for n <= %d : %s' % (K, eq, N0, dom))
    print('  ### sigma_max = %.3f : eta = %.6f (exact part %.6f + tail bound %.2e) ; at sigma_max - 0.01 eta = %.6f'
          % (smax, e, head, 2 * tail, below))
    print('  positive control: the bank`s largest real part %.4f < sigma_max : %s' % (offb, offb < smax))
    return 0


def smax():
    return json.loads(io.open(os.path.join(D, 'b523_sigma.json'), encoding='utf-8').read())['sigma_max']


# ### ### COMPONENT 3 -- THE COUNT.
def zabs(sig):
    """### SUM r(n) n^{-sig} <= 2 zeta(sig) L(sig, chi) (r <= 2a), sig > 1."""
    return float(2.0 * mp.zeta(sig) * mp.dirichlet(sig, CHI))


def gamma_ratio_sup(eta):
    """### sup_t |Gamma(1+eta+it) / Gamma(1-eta+it)| / |1-eta+it|^{2 eta}, on t in [0, 1e4] (step 0.05 to 50, then geometric);
    ### Stirling`s remainder (|mu(z)| <= 1/(6|z|), Re z > 0) bounds the drift beyond by 1/(3t) in the log."""
    ts = list(np.arange(0.0, 50.0, 0.05)) + list(np.geomspace(50.0, 1e4, 4000))
    best = 0.0
    for t in ts:
        v = float(mp.exp(mp.re(mp.loggamma(mp.mpc(1 + eta, t)) - mp.loggamma(mp.mpc(1 - eta, t)))) / abs(complex(1 - eta, t)) ** (2 * eta))
        best = max(best, v)
    return best * math.exp(1.0 / (3e4)) * 1.001


def e_params(eta, s1, g, sm_eta):
    """### E(T) = 1.5 + [log(max(A,B)/g0) + (2+2 eta) log(T+R+2+eta) - log(T-R)] / log(R/r) + STIRLING_PAD."""
    R, r_ = s1 + eta, s1 - 0.5
    B = zabs(1 + eta)
    A = (1 + eta) / (1 - eta) * C23 ** (1 + 2 * eta) * g * B
    g0 = 2.0 - sm_eta
    return dict(eta=eta, sigma1=s1, R=R, r=r_, A=A, B=B, G=g, g0=g0, lRr=math.log(R / r_), K=math.log(max(A, B) / g0),
                e1=(1 + 2 * eta) / math.log(R / r_))


def E_of(pp, T):
    return 1.5 + (pp['K'] + (2 + 2 * pp['eta']) * math.log(T + pp['R'] + 2 + pp['eta']) - math.log(T - pp['R'])) / pp['lRr'] + STIRLING_PAD


def M0(T):
    return (T / math.pi) * math.log(T * math.sqrt(23.0) / (2 * math.pi * math.e)) + 1.0


def M_exact(T):
    return float((mp.pi + T * mp.log(C23) + mp.im(mp.loggamma(mp.mpc(0.5, T)))) / mp.pi)


def n_bank(T):
    # ### b523`s defect: the first form summed numpy comparisons, returned numpy`s integer, and the control flags built
    # ### on it were numpy booleans json refused -- the count run died and left a zero-byte husk (b328`s trap). ### Cast.
    return int(np.sum(F.GQ <= T)) + 2 * int(sum(1 for b, g in F.OFFQ if float(g) <= T))


def count():
    sm = smax()
    r, a = tables()
    best = None
    for eta in (0.1, 0.2, 0.3, 0.4, 0.5):
        g = gamma_ratio_sup(eta)
        for k in range(0, 13):
            s1 = sm + 0.25 * k
            pp = e_params(eta, s1, g, eta_bound(s1, r, a)[0])
            e = E_of(pp, TOP)
            if best is None or e < best[0]:
                best = (e, pp)
    pp = best[1]
    stir = max(abs(M_exact(T) - M0(T)) for T in list(np.linspace(150, 2000, 300)) + list(np.geomspace(2000, 1e7, 200)))
    ctrl = []
    for T in (30.0, 60.0, 90.0, 120.0, 149.9):
        nb, me = n_bank(T), M_exact(T)
        ctrl.append(dict(T=T, n_bank=nb, M_exact=me, M0=M0(T), E=E_of(pp, T), inside=abs(nb - me) <= E_of(pp, T),
                         shifted_outside=abs(nb + math.ceil(E_of(pp, T)) + 1 - me) > E_of(pp, T)))
    res = dict(params=pp, E150=E_of(pp, TOP), E1e4=E_of(pp, 1e4), stirling_max_diff=stir, stirling_pad=STIRLING_PAD,
               stirling_ok=stir <= STIRLING_PAD, controls=ctrl, n_bank_150=n_bank(TOP), M0_150=M0(TOP))
    # ### b523`s defect, second form: numpy`s float comparisons made numpy booleans json refused; the text is now built with
    # ### a converter BEFORE the file is opened, so a failure cannot leave a zero-byte husk.
    txt = json.dumps(res, indent=1, default=lambda o: o.item()) + NL
    io.open(os.path.join(D, 'b523_count.json'), 'w', encoding='utf-8', newline=NL).write(txt)
    print('  parameters (least E(150) on the grid): eta %.1f sigma1 %.3f R %.3f r %.3f ; A %.4g B %.4g G %.6f g0 %.4f ; e1 %.4f'
          % (pp['eta'], pp['sigma1'], pp['R'], pp['r'], pp['A'], pp['B'], pp['G'], pp['g0'], pp['e1']))
    print('  ### E(150) = %.3f ; E(1e4) = %.3f ; |M_exact - M0| max %.2e (pad %.2f) ; N_bank(150) %d, M0(150) %.3f'
          % (res['E150'], res['E1e4'], stir, STIRLING_PAD, res['n_bank_150'], res['M0_150']))
    for c in ctrl:
        print('  control T=%-6.1f N_bank %-4d M_exact %.3f E %.2f : inside %s ; shifted count outside %s'
              % (c['T'], c['n_bank'], c['M_exact'], c['E'], c['inside'], c['shifted_outside']))
    return 0


def tails(a, sm, pp):
    W = B21.PWindow(a, 'q', P)
    s = sm - 0.5
    c1, c2, t2 = B21.consts(W, s)
    old = B21.new_tail(W)['total']
    t_sig = B21.tail_s(W, s)
    f_T = B21.allowance(W, TOP, s)
    extra = 2.0 * (f_T * (M0(TOP) + STIRLING_PAD + E_of(pp, TOP) - n_bank(TOP)) + pp['e1'] * c2 ** 2 * TOP ** (2 - 2 * P) / (2 * P - 2))
    return dict(old=old, sigma=t_sig, full=t_sig + extra, t2=t2, t2_below_T=t2 <= TOP)


def reread():
    sm = smax()
    cnt = json.loads(io.open(os.path.join(D, 'b523_count.json'), encoding='utf-8').read())
    pp = cnt['params']
    cells = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b522_cells.jsonl'), encoding='utf-8') if l.strip()), key=lambda c: c['a'])
    rows = []
    for c in cells:
        t = tails(c['a'], sm, pp)
        base = c['Eu'] + c['Ek'] + c['Eround']
        row = dict(a=c['a'], h2=c['h2'], r=c['r'], Bprime=base, shortfall=c['shortfall'], neg522=c['h2'] < -c['B'] and abs(c['r']) <= c['B'],
                   tail_old=t['old'], tail_sigma=t['sigma'], tail_full=t['full'], t2_below_T=t['t2_below_T'])
        for k, tk in (('sigma', t['sigma']), ('full', t['full'])):
            B = base + tk
            row['B_' + k] = B
            row['ver_' + k] = abs(c['r']) <= B
            row['neg_' + k] = row['ver_' + k] and c['h2'] < -B
            row['in_reach_' + k] = tk <= base
        row['margin_full'] = -c['h2'] - row['B_full']
        row['shortfall_over_margin'] = (c['shortfall'] / row['margin_full']) if row['margin_full'] > 0 else None
        row['survives'] = row['neg_full'] and row['margin_full'] > c['shortfall']
        rows.append(row)
        print('  a=%-3.0f h2 %+.4e ; tail old %.2e -> sigma %.2e -> full %.2e ; B_full %.2e ; neg %s/%s/%s ; shortfall/margin %s'
              % (c['a'], c['h2'], t['old'], t['sigma'], t['full'], row['B_full'], row['neg522'], row['neg_sigma'], row['neg_full'],
                 ('%.1e' % row['shortfall_over_margin']) if row['shortfall_over_margin'] is not None else '-'))
    res = dict(sigma_max=sm, s_max=sm - 0.5, rows=rows,
               neg522=[r['a'] for r in rows if r['neg522']], neg_sigma=[r['a'] for r in rows if r['neg_sigma']],
               neg_full=[r['a'] for r in rows if r['neg_full']], survivors=[r['a'] for r in rows if r['survives']])
    txt = json.dumps(res, indent=1, default=lambda o: o.item()) + NL
    io.open(os.path.join(D, 'b523_reread.json'), 'w', encoding='utf-8', newline=NL).write(txt)
    print('### NEGATIVE: b522 %d ; sigma-repriced %d ; full %d ; SURVIVING ALL THREE %d, narrowest %s'
          % (len(res['neg522']), len(res['neg_sigma']), len(res['neg_full']), len(res['survivors']), min(res['survivors']) if res['survivors'] else 'NONE'))
    return 0


if __name__ == '__main__':
    sys.exit({'sigma': sigma, 'count': count, 'reread': reread}[sys.argv[1]]())
