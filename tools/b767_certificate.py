# -*- coding: utf-8 -*-
"""b767_certificate.py -- (R377)(4)(a): THE COMBINATION'S THREE FORMS, THEIR SUMS OF |r| AND THE DIGITS THEIR BUDGETS NEED; no Lean, no
dispatch.

Carried from tools/b766_certificate.py by import, unedited (committed at b766, 7bde5827): its window reader and digest (window), its
scaling (scaled), its exact K(n) (kn_scaled), its exact closed forms (Comb, lin, rho_comb, band_comb, lam_comb), its factor table and
Lambda_Q's loop (lambda_q_exact), its pieces (BETA_D). Nothing is computed at a zero, no bank of zeros is opened, the window's frequency
is not read (the coefficients are read from the bank), and no coefficient and no K(n) is printed.

THE THREE FORMS of S = P - PR + A at the window M 16, d 3 of data/b765_window.json, each S = r_0 + r_gamma gamma + r_pi log pi + SUM r_x x:
  (p)  THE PRIMES, b766's: x = log p, the closed forms' log m factored and PR's Lambda_Q(n) in its primes (data/b766_certificate.txt :16)
  (i)  THE INTEGERS, before factoring: x = log m for each integer m at which the closed forms are evaluated (log(c + 1) and log c of G_l
       and F_l, log 2 and log 23 of the archimedean constant) unfactored; PR's cQ(n) in its primes, as b766's L7 compiled them (ferry :13)
  (ii) BY PARTS, order 1: x = delta_k = log(k + 1) - log k, k >= 1, the coefficient of delta_k the tail SUM_(m > k) a_m of form (i)'s a_m
       (log m = SUM_(k < m) delta_k); order l + 1 from order l: SUM_k c_k D_k = (SUM_k c_k) D_1 + SUM_j (SUM_(k > j) c_k) (D_(j+1) - D_j),
       D the order-l differences, each order's first terms kept as constants of their own; continued while the sum of |r| falls
For each: the constants N (gamma and log pi among them), the sum of the |r| over them, the largest numerator's digits, THE BUDGET by
b766's rule (each constant an equal share of |S| / 2: digits floor(log10(2 N |r| / |S|)) + 1) with gamma's, log pi's and the others'
range, and the one width for all (floor(log10(2 SUM |r| / |S|)) + 1).
ITS CONTROLS: the prime form's S against b765's -6.62468014575 to 10 digits; its primes 1900 and its one width 21 digits, b766's
(data/b766_certificate.txt :16, :18); the integer form factored equal to the prime form, each prime exactly; each order of (ii) inverted
(c_k = T_(k-1) - T_k, the first terms read back) equal to the order before it exactly; each form's value by balls against S to 10 digits;
PLANTED: one coefficient T_k of (ii)'s order 1, at the middle k, moved by 1, its inversion read as the two differences it makes, at
m = k and m = k + 1, and at no other m.
THE BUDGET IN THE LEAN ((R377)(4)(a)), over the prime form: for each set of shares in LEAN_SHARES (digits for gamma, for log pi and for
every log p), the three sums |r| 10^-digits by group (gamma, log pi, the primes) and their total against |S| / 2; the certificate's equal
shares beside them, their total read against b766's 1.315 (data/b766_certificate.txt :18) as a further control. No r is printed.

  python -X utf8 -u tools/b767_certificate.py dry       computed and printed; nothing written
  python -X utf8 -u tools/b767_certificate.py write     data/b767_certificate.txt and data/b767_certificate.json (figures, no coefficient)
Each route refuses where this file differs from its blob at the relay's HEAD (committed before its run, N2). Written by the Write tool.
"""
import hashlib
import importlib.util
import json
import math
import os
import subprocess
import sys
import time
from decimal import Decimal

from flint import arb, ctx, fmpq, fmpz_poly

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ACT = 'b767'
SELF = 'tools/b767_certificate.py'
CARRIED = 'tools/b766_certificate.py'
CJSON, CTXT = 'data/b767_certificate.json', 'data/b767_certificate.txt'
YTOP = 1024
PREC = 512
SREF, DIGITS = '-6.62468014575', 10
B766_PRIMES, B766_UNIFORM = 1900, 21
MAX_ORDER = 16
B766_EQUAL = '1.315'   # ### data/b766_certificate.txt :18, SUM |r| 10^-digits at the equal shares
LEAN_SHARES = (('one width for all, 21 digits (b766`s)', (21, 21, 21)),
               ('gamma 3, log pi 3, each log p 22 digits', (3, 3, 22)),
               ('gamma 4, log pi 4, each log p 21 digits', (4, 4, 21)),
               ('gamma 6, log pi 6, each log p 24 digits', (6, 6, 24)))

_spec = importlib.util.spec_from_file_location('b766_certificate', os.path.join(ROOT, *CARRIED.split('/')))
B6 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B6)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)


def committed():
    out = []
    for rel in (SELF, CARRIED):
        here = open(os.path.join(ROOT, *rel.split('/')), 'rb').read().replace(b'\r', b'')
        r = _git('show', 'HEAD:' + rel)
        if r.returncode != 0 or r.stdout.replace(b'\r', b'') != here:
            sys.exit('### %s DIFFERS FROM ITS BLOB AT THE RELAY`S HEAD, OR IS NOT COMMITTED -- NOTHING RUN' % rel)
        out.append(hashlib.sha256(here).hexdigest())
    return _git('rev-parse', '--short=8', 'HEAD').stdout.decode().strip(), out[0], out[1]


def numer_digits(x):
    return len(str(abs(int(x.p)))) if x != 0 else 0


def budget(cons, aS):
    """b766's rule over [(name, r)]: (N, [(name, digits)], the sum of |r| times the half-widths, the one width)."""
    cons = [(n, x) for n, x in cons if x != 0]
    N = len(cons)
    ln10 = arb(10).log()
    out, tot = [], arb(0)
    for n, x in cons:
        v = ((arb(abs(x)) * (2 * N)) / aS).log() / ln10
        dgt = int(math.floor(float(v.mid()))) + 1
        out.append((n, dgt))
        tot += arb(abs(x)) * arb(10) ** (-dgt)
    sabs = sum((abs(x) for _n, x in cons), fmpq(0))
    uv = ((arb(sabs) * 2) / aS).log() / ln10
    return dict(N=N, digits=out, total=tot, below=bool(tot < aS / 2), uniform=int(math.floor(float(uv.mid()))) + 1, sabs=sabs,
                nd=max([numer_digits(x) for _n, x in cons] or [0]))


def agree(v):
    R = Decimal(SREF)
    tol = Decimal(10) ** (R.adjusted() - DIGITS + 1) / 2
    mid = Decimal(v.mid().str(40, radius=False))
    return abs(mid - R) < tol, mid


def compute():
    js, cm, WL, dig = B6.window()
    t0 = time.time()
    ctx.prec = PREC
    M = int(js['M'])
    jmax = YTOP * M - 4
    C, S = B6.scaled(cm, M, jmax)
    S2M = fmpq(M * S * S)
    dmax = jmax - M
    mmax = jmax + 6
    spf = B6.factor_table(mmax)
    intH = fmpq(sum(C), M * S)
    pc = (fmpz_poly(C) * fmpz_poly(list(reversed(C)))).coeffs()

    def cauto(x):
        idx = jmax + x
        return int(pc[idx]) if 0 <= x <= dmax and idx < len(pc) else 0
    k0 = (B6.BETA_D[0] * cauto(0) + 2 * sum((B6.BETA_D[d] * cauto(d) for d in (1, 2, 3)), fmpq(0))) / S2M
    rho = B6.rho_comb(C, M, jmax, mmax)
    band = B6.band_comb(C, M, jmax, mmax)
    lam = B6.lam_comb(cauto, dmax, mmax)
    one = B6.Comb(mmax)
    one.one = fmpq(1)
    J = B6.lin(mmax, (fmpq(11, 6) * k0, one), (fmpq(1) / S2M, band), (fmpq(-1) / S2M, lam))
    arch = B6.Comb(mmax)
    arch.L[23], arch.L[2], arch.logpi, arch.gamma = fmpq(1, 2), fmpq(-1), fmpq(-1), fmpq(-1)
    A = B6.lin(mmax, (2 * k0, arch), (fmpq(2), J))
    P = B6.lin(mmax, (2 * intH / S, rho))
    nmax = YTOP - 1
    lq, _rq = B6.lambda_q_exact(nmax, spf)
    PRp, nk = {}, 0
    for n in range(2, nmax + 1):
        if not lq[n]:
            continue
        Kn = B6.kn_scaled(C, M, jmax, n) / S2M
        nk += 1
        if Kn != 0:
            for p, x in lq[n].items():
                PRp[p] = PRp.get(p, fmpq(0)) + 2 * x * Kn
    Sc = B6.lin(mmax, (fmpq(1), P), (fmpq(1), A))
    rp = {}
    for m, x in enumerate(Sc.L):
        if m >= 2 and x != 0:
            for p, a in B6.factor(m, spf).items():
                rp[p] = rp.get(p, fmpq(0)) + a * x
    for p, x in PRp.items():
        rp[p] = rp.get(p, fmpq(0)) - x
    rp = dict((p, x) for p, x in rp.items() if x != 0)
    a = list(Sc.L)
    for p, x in PRp.items():
        a[p] -= x
    ai = dict((m, a[m]) for m in range(2, len(a)) if a[m] != 0)
    fac = {}
    for m, x in ai.items():
        for p, e in B6.factor(m, spf).items():
            fac[p] = fac.get(p, fmpq(0)) + e * x
    fac = dict((p, x) for p, x in fac.items() if x != 0)
    t_ex = time.time()
    return dict(js=js, dig=dig, WL=WL, M=M, d=int(js['d']), r0=Sc.one, rg=Sc.gamma, rpi=Sc.logpi, rp=rp, ai=ai, fac=fac, nk=nk,
                lq_n=sum(1 for n in range(2, nmax + 1) if lq[n]), secs=dict(exact=int(t_ex - t0)))


def by_parts(ai):
    """the orders of (ii): [(bounds, coeffs)], bounds the first terms' coefficients [order-1 first, ...], coeffs {k: c_k} on the order's
    differences at k = 1 .. top; and the inversions' checks [True ...] per order (order 1 against ai, order l + 1 against order l)."""
    top = max(ai)
    T, run = {}, fmpq(0)
    for k in range(top - 1, 0, -1):
        run += ai.get(k + 1, fmpq(0))
        T[k] = run
    orders, checks = [([], T)], []
    back = {}
    for m in range(2, top + 1):
        x = T.get(m - 1, fmpq(0)) - T.get(m, fmpq(0))
        if x != 0:
            back[m] = x
    checks.append(back == ai)
    for _l in range(2, MAX_ORDER + 1):
        bounds, c = orders[-1]
        kt = max(c) if c else 0
        b = sum(c.values(), fmpq(0))
        E, run = {}, fmpq(0)
        for j in range(kt - 1, 0, -1):
            run += c.get(j + 1, fmpq(0))
            E[j] = run
        back = {}
        for k in range(2, kt + 1):
            x = E.get(k - 1, fmpq(0)) - E.get(k, fmpq(0))
            if x != 0:
                back[k] = x
        c1 = b - sum(back.values(), fmpq(0))
        if c1 != 0:
            back[1] = c1
        checks.append(back == dict((k, x) for k, x in c.items() if x != 0))
        orders.append((bounds + [b], E))
    return orders, checks


def values(top, order_n):
    """the order-l differences as balls: D[l][k] for k = 1 .. top - l, l = 1 .. order_n (D[1][k] = log(k + 1) - log k)."""
    lg = [arb(0)] + [arb(m).log() for m in range(1, top + 1)]
    D = {1: [None] + [lg[k + 1] - lg[k] for k in range(1, top)]}
    for l in range(2, order_n + 1):
        prev = D[l - 1]
        D[l] = [None] + [prev[k + 1] - prev[k] for k in range(1, len(prev) - 1)]
    return D


def forms(R):
    ctx.prec = PREC
    g, lp = arb.const_euler(), arb.pi().log()
    head = arb(R['r0']) + arb(R['rg']) * g + arb(R['rpi']) * lp
    Sp = head + sum((arb(x) * arb(p).log() for p, x in R['rp'].items()), arb(0))
    aS = abs(Sp)
    base = [('gamma', R['rg']), ('log pi', R['rpi'])]
    out = []
    out.append(('(p) the primes', Sp, budget(base + [('log %d' % p, x) for p, x in sorted(R['rp'].items())], aS), len(R['rp'])))
    Si = head + sum((arb(x) * arb(m).log() for m, x in R['ai'].items()), arb(0))
    out.append(('(i) the integers', Si, budget(base + [('log %d' % m, x) for m, x in sorted(R['ai'].items())], aS), len(R['ai'])))
    orders, checks = by_parts(R['ai'])
    top = max(R['ai'])
    D = values(top, len(orders))
    sums = []
    for l, (bounds, c) in enumerate(orders, 1):
        v = head + sum((arb(x) * D[l][k] for k, x in c.items() if x != 0), arb(0))
        for i_, bx in enumerate(bounds, 1):
            v += arb(bx) * D[i_][1]
        cons = base + [('first difference of order %d' % i_, bx) for i_, bx in enumerate(bounds, 1)] + \
            [('order %d at %d' % (l, k), x) for k, x in sorted(c.items())]
        B = budget(cons, aS)
        sums.append(B['sabs'])
        out.append(('(ii) by parts, order %d' % l, v, B, sum(1 for x in c.values() if x != 0)))
        if l >= 2 and sums[-1] >= sums[-2]:
            break
    return out, checks[:len(sums)], orders, Sp


def lean_budget(R, aS):
    """each set of LEAN_SHARES over the prime form: (name, shares, (gamma's, log pi's, the primes' |r| 10^-digits), total, below |S| / 2)."""
    sg, sp, sq = arb(abs(R['rg'])), arb(abs(R['rpi'])), arb(sum((abs(x) for x in R['rp'].values()), fmpq(0)))
    out = []
    for name, (dg, dp, dq) in LEAN_SHARES:
        parts = (sg * arb(10) ** (-dg), sp * arb(10) ** (-dp), sq * arb(10) ** (-dq))
        tot = parts[0] + parts[1] + parts[2]
        out.append((name, (dg, dp, dq), parts, tot, bool(tot < aS / 2)))
    return out


def planted(R):
    orders, _c = by_parts(R['ai'])
    T = dict(orders[0][1])
    k0 = sorted(T)[len(T) // 2]
    T[k0] = T[k0] + 1
    top = max(R['ai'])
    back = {}
    for m in range(2, top + 1):
        x = T.get(m - 1, fmpq(0)) - T.get(m, fmpq(0))
        if x != 0:
            back[m] = x
    diff = sorted(m for m in set(back) | set(R['ai']) if back.get(m, fmpq(0)) != R['ai'].get(m, fmpq(0)))
    return k0, diff


def run(write):
    commit, sha, sha6 = committed()
    R = compute()
    t1 = time.time()
    F, checks, orders, Sp = forms(R)
    R['secs']['forms'] = int(time.time() - t1)
    k0, diff = planted(R)
    okS, mid = agree(Sp)
    pform = F[0][2]
    ctl = [('the prime form`s S against b765`s %s to %d digits' % (SREF, DIGITS), '%.12g' % float(mid), okS),
           ('the prime form`s primes and its one width against b766`s %d and %d digits (data/b766_certificate.txt :16, :18)' % (B766_PRIMES, B766_UNIFORM),
            'primes %d, one width %d' % (len(R['rp']), pform['uniform']), len(R['rp']) == B766_PRIMES and pform['uniform'] == B766_UNIFORM),
           ('the integer form factored against the prime form, each prime exactly', 'primes %d against %d, equal %s' % (
               len(R['fac']), len(R['rp']), R['fac'] == R['rp']), R['fac'] == R['rp']),
           ('each order of (ii) inverted against the order before it, exactly', '%s' % checks, all(checks) and len(checks) == len(F) - 2)]
    for name, v, _B, _n in F:
        ok, m_ = agree(v)
        ctl.append(('%s: its value by balls against S to %d digits' % (name, DIGITS), '%.12g (radius %.3g)' % (float(m_), float(v.rad())), ok))
    ctl.append(('PLANTED: one coefficient T_k of (ii)`s order 1, at the middle k, moved by 1, its inversion read at m = k and m = k + 1 alone',
                'differences at %s (k %d, so m %d and %d)' % (diff, k0, k0, k0 + 1), diff == [k0, k0 + 1]))
    LB = lean_budget(R, abs(Sp))
    eqt = '%.4g' % float(pform['total'].mid())
    ctl.append(('the equal shares` sum over the prime form against b766`s %s (data/b766_certificate.txt :18)' % B766_EQUAL, eqt, eqt == B766_EQUAL))
    allok = all(c[2] for c in ctl)
    fl = []
    best = min(F[2:], key=lambda t: t[2]['sabs']) if len(F) > 2 else None
    for name, v, B, n in F:
        dg = dict(B['digits'])
        rest = [d for nm, d in B['digits'] if nm not in ('gamma', 'log pi')]
        fl.append(dict(form=name, constants=B['N'], terms=n, sum_abs_r='%.6g' % float(arb(B['sabs']).mid()),
                       sum_abs_r_log10='%.3f' % float((arb(B['sabs']).log() / arb(10).log()).mid()), largest_numerator_digits=B['nd'],
                       uniform_digits=B['uniform'], gamma_digits=dg.get('gamma'), logpi_digits=dg.get('log pi'),
                       others_digits=[min(rest) if rest else None, max(rest) if rest else None],
                       equal_share_total='%.4g' % float(B['total'].mid()), below_half=B['below']))
    L = ['%s -- THE COMBINATION`S THREE FORMS AT THE WINDOW M %d, d %d: THE SUMS OF |r| AND THE BUDGETS, (R377)(4)(a); no Lean, no dispatch (%s)' % (
        ACT, R['M'], R['d'], utc()), '',
         '### the tool %s, sha256 %s, committed at relay %s before its run, importing %s unedited (sha256 %s); every r an exact' % (
             SELF, sha[:16], commit, CARRIED, sha6[:16]),
         '### rational (python-flint fmpq), the values read by balls at %d bits; nothing computed at a zero, no bank of zeros opened, the' % PREC,
         '### window`s frequency not read, no coefficient and no K(n) printed', ''] + R['WL'] + ['',
         '## THE COMBINATION, EXACT: cQ(n) not 0 at %d n of 2 to 1023 ; K(n) computed at %d n ; the integer form`s logarithms %d ; '
         'seconds %s' % (R['lq_n'], R['nk'], len(R['ai']), ' ; '.join('%s %d' % kv for kv in R['secs'].items())), '',
         '## THE FORMS (each: the constants N with gamma and log pi among them ; the sum of the |r| ; the largest numerator ; THE BUDGET by '
         'b766`s rule, gamma`s, log pi`s and the others` digits ; the one width for all)']
    for f in fl:
        L.append('  %-28s N %5d ; SUM |r| %s (10^%s) ; numerator %d digits ; gamma %s, log pi %s, the others %s-%s digits ; the equal shares` '
                 'sum %s < |S| / 2: %s ; ONE WIDTH %d DIGITS' % (
                     f['form'], f['constants'], f['sum_abs_r'], f['sum_abs_r_log10'], f['largest_numerator_digits'], f['gamma_digits'],
                     f['logpi_digits'], f['others_digits'][0], f['others_digits'][1], f['equal_share_total'], f['below_half'], f['uniform_digits']))
    stop = len(F) - 2
    L += ['  (ii) stopped at order %d: %s' % (stop, 'its sum of |r| not below order %d`s, so order %d is the least' % (stop - 1, stop - 1)
                                              if stop >= 2 and float(arb(F[-1][2]['sabs']).mid()) >= float(arb(F[-2][2]['sabs']).mid())
                                              else 'the cap of %d orders reached' % MAX_ORDER),
          '  the least sum of |r| among (ii)`s orders: %s, SUM |r| %s, one width %d digits' % (
              best[0], '%.6g' % float(arb(best[2]['sabs']).mid()), best[2]['uniform']) if best else '  (ii): none', '',
          '## THE BUDGET IN THE LEAN, over the prime form: |r| 10^-digits summed by group, the total against |S| / 2 %.6g' % float((abs(Sp) / 2).mid()),
          '  %-44s gamma %d, log pi %d, the log p %d-%d digits (data/b766_certificate.txt :18) ; total %s ; below: %s' % (
              'the certificate`s equal shares', pform['digits'][0][1] if pform['digits'][0][0] == 'gamma' else -1,
              dict(pform['digits']).get('log pi', -1), min(d for n, d in pform['digits'] if n not in ('gamma', 'log pi')),
              max(d for n, d in pform['digits'] if n not in ('gamma', 'log pi')), eqt, pform['below'])]
    L += ['  %-44s gamma %d, log pi %d, each log p %d digits ; gamma %.3g, log pi %.3g, the primes %.3g ; total %.4g ; below: %s' % (
        name, sh[0], sh[1], sh[2], float(pt[0].mid()), float(pt[1].mid()), float(pt[2].mid()), float(tot.mid()), bl) for name, sh, pt, tot, bl in LB]
    L += ['', '## THE CONTROLS']
    L += ['  %s: %s -- %s' % (n, g, 'AS WANTED' if ok else '### NOT AS WANTED') for n, g, ok in ctl]
    L += ['', '### ### **THE THREE FORMS %s: %d OF %d CONTROLS AS WANTED ; THE PRIMES` ONE WIDTH %d DIGITS, THE INTEGERS` %d, BY PARTS AT ITS LEAST %d '
              '(ORDER %s).**' % ('READ' if allok else 'WITH A CONTROL FAILED', sum(1 for c in ctl if c[2]), len(ctl), fl[0]['uniform_digits'],
                                 fl[1]['uniform_digits'], best[2]['uniform'] if best else -1, best[0].rsplit(' ', 1)[-1] if best else '-')]
    print(NL.join(L[5:]))
    if write:
        js = dict(act=ACT, ruling='(R377)(4)(a)', at=utc(), tool=dict(path=SELF, commit=commit, sha256=sha[:16], carried=CARRIED, carried_sha256=sha6[:16]),
                  window=dict(bank=B6.WJSON, sha256_less_final_line_end=R['dig']['text_sha'], coef_sha=R['dig']['coef_sha'], M=R['M'], d=R['d']),
                  forms=fl, by_parts_stop=stop, least=best[0] if best else None, equal_shares_total=eqt, half_S='%.6g' % float((abs(Sp) / 2).mid()),
                  lean_budget=[dict(shares=name, gamma_digits=sh[0], logpi_digits=sh[1], logp_digits=sh[2], gamma='%.3g' % float(pt[0].mid()),
                                    logpi='%.3g' % float(pt[1].mid()), primes='%.3g' % float(pt[2].mid()), total='%.4g' % float(tot.mid()),
                                    below_half=bl) for name, sh, pt, tot, bl in LB],
                  controls=[dict(name=n, got=g, as_wanted=ok) for n, g, ok in ctl],
                  rule='each constant an equal share: digits floor(log10(2 N |r| / |S|)) + 1; one width floor(log10(2 SUM |r| / |S|)) + 1')
        for rel, s in ((CJSON, json.dumps(js, ensure_ascii=False, indent=1) + NL), (CTXT, NL.join(L) + NL)):
            p = os.path.join(ROOT, *rel.split('/'))
            with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
                f.write(s)
            os.replace(p + '.tmp', p)
        print('written', CJSON, 'and', CTXT)
    return 0 if allok else 1


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('dry', 'write'):
        sys.exit(__doc__)
    sys.exit(run(sys.argv[1] == 'write'))
