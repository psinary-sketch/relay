# -*- coding: utf-8 -*-
"""b766_certificate.py -- (R376)(4)(a): THE CERTIFICATE, BANKED AS DATA BEFORE ANY DISPATCH; no Lean.

Carried from tools/b765_window.py (committed at b765): its exact polynomial pieces copied unedited (padd, pmul, pscale, plin, pint,
cardinal; BETA, MU, BETA_D), its scaling of the coefficients (scaled) and its exact K(n) (kn_scaled) copied unedited; its closed forms in
G_l and F_l (tools/b765_window.py :278-:371 and :399-:441) written exactly in place of its balls: G_0(c) = log(c + 1) - log c and
G_l = 1/l - c G_(l-1), so G_l(c) = a_l (log(c + 1) - log c) + b_l with a_l = (-c)^l and b_l rational; F_l(c) = (log(c + 1) - G_(l+1)(c))
/ (l + 1), F_l(0) = -1/(l + 1)^2. Lambda_Q's loop copied exact from tools/b694_witness_terms.py :291-:317 and not imported (that module
imports the step-zero reader of a bank of zeros). Nothing is computed at a zero, no bank of zeros is opened, the window's frequency is not
read (the coefficients are read from the bank), and no coefficient and no K(n) is printed.

THE CERTIFICATE ((R376)(4)(a)) at the window M 16, d 3 of data/b765_window.json, as exact rationals: K(n) = n^(-1/2) k(log n) for each n
from 2 to 1023 at which cQ(n) is not 0; k(0); the integral of H; the sum of the |c_j|; and the arithmetic side S = P - PR + A as one
combination S = r_0 + r_gamma gamma + r_pi log pi + SUM_p r_p log p, each r an exact rational, with the number of primes in it, the length
in digits of its largest numerator, and THE BUDGET: for each constant the digits its rational enclosure needs (a half-width 10^-digits),
each constant given an equal share, so that SUM |r| times the half-widths stays below |S| / 2.
ITS CONTROLS, the values b765's (data/b765_window.txt :19): the combination with its constants as balls equals S, -6.62468014575, to 10
digits; 2 SUM cQ(n) K(n) equals PR, 657.637691719, to 10 digits; k(0) equals 128.956888485 to 10 digits; the bank as composed read back,
each K(n) equal to the computed, and one K(n) with its numerator moved by 1 read as that one difference.

  python -X utf8 -u tools/b766_certificate.py check     the json's digest against data/b765_window.txt :26, both forms printed
  python -X utf8 -u tools/b766_certificate.py dry       the certificate computed and its controls printed; nothing written
  python -X utf8 -u tools/b766_certificate.py write     data/b766_certificate.json and data/b766_certificate.txt
Each route refuses where this file differs from its blob at the relay's HEAD (committed before its run, N2). Written by the Write tool.
"""
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
from decimal import Decimal
from operator import mul

from flint import arb, ctx, fmpq, fmpz_poly

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b766'
SELF = 'tools/b766_certificate.py'
WJSON, WTXT, WTXT_LINE = 'data/b765_window.json', 'data/b765_window.txt', 26
CJSON, CTXT = 'data/b766_certificate.json', 'data/b766_certificate.txt'
DISC = 23
YTOP = 1024
PREC = 512
REF = (('S', '-6.62468014575'), ('PR', '657.637691719'), ('k0', '128.956888485'))   # ### data/b765_window.txt :19
DIGITS = 10


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)


def committed():
    here = open(os.path.abspath(__file__), 'rb').read().replace(b'\r', b'')
    r = _git('show', 'HEAD:' + SELF)
    if r.returncode != 0 or r.stdout.replace(b'\r', b'') != here:
        sys.exit('### %s DIFFERS FROM ITS BLOB AT THE RELAY`S HEAD, OR IS NOT COMMITTED -- NOTHING RUN' % SELF)
    return _git('rev-parse', '--short=8', 'HEAD').stdout.decode().strip(), hashlib.sha256(here).hexdigest()


# ================================================================================ CARRIED FROM tools/b765_window.py :149-:208, UNEDITED
def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else fmpq(0)) + (b[i] if i < len(b) else fmpq(0)) for i in range(n)]


def pmul(a, b):
    out = [fmpq(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x != 0:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def pscale(a, c):
    return [x * c for x in a]


def plin(c0, c1, k):
    """(c0 + c1 s)^k."""
    out = [fmpq(1)]
    for _ in range(k):
        out = pmul(out, [fmpq(c0), fmpq(c1)])
    return out


def pint(a, lo, hi):
    """INT_lo^hi a(y) dy, exact."""
    lo, hi = fmpq(lo), fmpq(hi)
    tot = fmpq(0)
    for l, x in enumerate(a):
        if x != 0:
            tot += x * (hi ** (l + 1) - lo ** (l + 1)) / (l + 1)
    return tot


def cardinal(m):
    """the cardinal B-spline N_m on [p, p + 1], p = 0 .. m - 1, in the local variable s = u - p: (1/(m-1)!) SUM_(i<=p) (-1)^i C(m, i) (s + p - i)^(m-1)."""
    out = []
    for p in range(m):
        acc = [fmpq(0)] * m
        for i in range(p + 1):
            acc = padd(acc, pscale(plin(p - i, 1, m - 1), fmpq((-1) ** i * math.comb(m, i), math.factorial(m - 1))))
        out.append(acc)
    return out


BETA = cardinal(4)      # ### B, the cubic B-spline on [0, 4]: BETA[q] on [q, q + 1]
BETA_D = {d: sum((pint(pmul(BETA[q], BETA[q + d]), 0, 1) for q in range(4) if 0 <= q + d <= 3), fmpq(0)) for d in range(-3, 4)}
MU = [[sum((BETA[q][a] / (a + l + 1) for a in range(4)), fmpq(0)) for l in range(4)] for q in range(4)]   # ### INT_0^1 beta_q(s) s^l ds


# ================================================================================ CARRIED FROM tools/b765_window.py :265-:271 AND :374-:395, UNEDITED
def scaled(cm, M, jmax):
    """the coefficients as integers C_j over one power of ten S: c_j = C_j / S."""
    E = max([0] + [-e for (m, e) in cm.values() if m != 0])
    C = [0] * (jmax + 1)
    for j, (m, e) in cm.items():
        C[j] = m * 10 ** (e + E)
    return C, 10 ** E


def kn_scaled(C, M, jmax, n):
    """M S^2 K(n) = SUM_e kappa_n(e) Gamma_n(e), exact. Gamma_n(e) = SUM_i C_i C_(n i + e), e = -3 .. 4n - 1; kappa_n(e) = (1/n) SUM_q
    V(q, m, g) over t = q + e = m n + g in [0, 4n), V(q, m, g) = INT_0^1 beta_q(s) beta_m((g + s)/n) ds = SUM_k A(q, m, k) g^k."""
    gam = []
    for e in range(-3, 4 * n):
        i0 = max(M, -((e - M) // n))
        i1 = min(jmax, (jmax - e) // n)
        gam.append(sum(map(mul, C[i0:i1 + 1], C[n * i0 + e:n * i1 + e + 1:n])) if i1 >= i0 else 0)
    gp = [[g ** k for g in range(n)] for k in range(4)]
    nq = fmpq(n)
    tot = fmpq(0)
    for q in range(4):
        for m in range(4):
            A = [sum((BETA[m][j] * math.comb(j, k) * MU[q][j - k] / nq ** j for j in range(k, 4)), fmpq(0)) for k in range(4)]
            base = m * n - q + 3
            sl = gam[base:base + n]
            for k in range(4):
                if A[k] != 0:
                    sk = sum(map(mul, gp[k], sl))
                    if sk:
                        tot += A[k] * sk
    return tot / n


# ================================================================================ THE WINDOW'S BANK, ITS DIGEST
def q_of(s):
    """an exact rational from its printed form 'p/q' or 'p'."""
    s = str(s).strip()
    if '/' in s:
        a, b = s.split('/')
        return fmpq(int(a), int(b))
    return fmpq(int(s))


def window():
    """data/b765_window.json read and checked: its sha256 less its final line end against :26, the file's whole printed beside; the
    coefficients as (m, e), each against its rational; their sha256 against the bank's coef_sha. Returns (js, cm, lines)."""
    raw = open(os.path.join(ROOT, WJSON), 'rb').read()
    body = raw[:-1] if raw.endswith(b'\n') else raw
    body = body[:-1] if body.endswith(b'\r') else body
    text_sha, file_sha = hashlib.sha256(body).hexdigest(), hashlib.sha256(raw).hexdigest()
    line = open(os.path.join(ROOT, WTXT), encoding='utf-8').read().replace('\r', '').split(NL)[WTXT_LINE - 1]
    m = re.search(r'b765_window\.json: written, (\d+) coefficients as rationals, sha256 ([0-9a-f]{16})$', line)
    if not m:
        sys.exit('### %s :%d DOES NOT READ AS THE JSON BANK`S LINE -- NOTHING DONE' % (WTXT, WTXT_LINE))
    js = json.loads(body.decode('utf-8'))
    cm, bad = {}, []
    for j, me, rat in js['coefficients']:
        mm, ee = me.split('e')
        mm, ee = int(mm), int(ee)
        if q_of(rat) != (fmpq(mm) * fmpq(10) ** ee if ee >= 0 else fmpq(mm, 10 ** -ee)):
            bad.append(j)
        cm[int(j)] = (mm, ee)
    csha = hashlib.sha256(json.dumps(sorted([j, mm, ee] for j, (mm, ee) in cm.items())).encode('utf-8')).hexdigest()[:16]
    ok = text_sha[:16] == m.group(2) and len(cm) == int(m.group(1)) and csha == js.get('coef_sha') and not bad
    L = ['## THE WINDOW`S BANK, %s' % WJSON,
         '  its sha256 less its final line end %s ; %s :%d gives %s -- %s' % (text_sha[:16], WTXT, WTXT_LINE, m.group(2),
                                                                          'EQUAL' if text_sha[:16] == m.group(2) else '### NOT EQUAL'),
         '  the file whole %s ; %d bytes' % (file_sha[:16], len(raw)),
         '  coefficients %d (the line gives %s) ; each (m, e) against its rational: %s ; their sha256 %s, the bank`s coef_sha %s -- %s' % (
             len(cm), m.group(1), 'EQUAL' if not bad else '### %d DIFFER' % len(bad), csha, js.get('coef_sha'),
             'EQUAL' if csha == js.get('coef_sha') else '### NOT EQUAL'),
         '  M %s, d %s ; no coefficient printed ; THE BANK %s' % (js.get('M'), js.get('d'), 'AS WANTED' if ok else '### NOT AS WANTED')]
    if not ok:
        print(NL.join(L))
        sys.exit('### THE WINDOW`S BANK NOT AS WANTED -- NOTHING COMPUTED')
    return js, cm, L, dict(text_sha=text_sha, file_sha=file_sha, coef_sha=csha)


# ================================================================================ THE CLOSED FORMS, EXACT
class Comb:
    """one combination: one + gamma * gamma + logpi * log pi + SUM_m L[m] log m (m >= 2), every coefficient an exact rational."""

    def __init__(self, mmax):
        self.one, self.gamma, self.logpi = fmpq(0), fmpq(0), fmpq(0)
        self.L = [fmpq(0)] * (mmax + 1)


def lin(mmax, *terms):
    """SUM c X over (c, X), X a Comb; a new Comb."""
    out = Comb(mmax)
    for c, X in terms:
        out.one += c * X.one
        out.gamma += c * X.gamma
        out.logpi += c * X.logpi
        for m, x in enumerate(X.L):
            if x != 0:
                out.L[m] += c * x
    return out


def g_coeffs(c, lmax):
    """G_l(c) = a_l (log(c + 1) - log c) + b_l, l = 0 .. lmax, c >= 1: [(a_l, b_l)], a_l = (-c)^l."""
    a, b = fmpq(1), fmpq(0)
    out = [(a, b)]
    for l in range(1, lmax + 1):
        a, b = -c * a, fmpq(1, l) - c * b
        out.append((a, b))
    return out


_F = {}


def f_coeffs(c):
    """F_l(c) = alpha log(c + 1) + beta log c + gamma_l, l = 0 .. 6: [(alpha, beta, gamma_l)]; F_l(0) = -1/(l + 1)^2."""
    if c not in _F:
        if c == 0:
            _F[c] = [(fmpq(0), fmpq(0), fmpq(-1, (l + 1) ** 2)) for l in range(7)]
        else:
            g = g_coeffs(c, 7)
            _F[c] = [((1 - g[l + 1][0]) / (l + 1), g[l + 1][0] / (l + 1), -g[l + 1][1] / (l + 1)) for l in range(7)]
    return _F[c]


def rho_comb(C, M, jmax, mmax):
    """SUM_j C_j rho(j), rho(j) = SUM_q SUM_l BETA[q][l] G_l(j + q) (b765 rho_sum), exact."""
    X = Comb(mmax)
    for j in range(M, jmax + 1):
        if not C[j]:
            continue
        for q in range(4):
            c = j + q
            g = g_coeffs(c, 3)
            for l in range(4):
                if BETA[q][l] != 0:
                    w = BETA[q][l] * C[j]
                    a, b = g[l]
                    X.L[c + 1] += w * a
                    X.L[c] -= w * a
                    X.one += w * b
    return X


def band_comb(C, M, jmax, mmax):
    """SUM_i SUM_(|d|<=3) C_i C_(i-d) Lg(i, d), Lg(i, d) = SUM_q SUM_l PI(d, q)[l] F_l(i + q) (b765 band_sum), exact."""
    PI = dict(((d, q), pmul(BETA[q], BETA[q + d])) for d in range(-3, 4) for q in range(4) if 0 <= q + d <= 3)
    X = Comb(mmax)
    for i in range(M, jmax + 1):
        if not C[i]:
            continue
        w = [[fmpq(0)] * 7 for _ in range(4)]
        for d in range(-3, 4):
            j = i - d
            if j < M or j > jmax or not C[j]:
                continue
            cc = C[i] * C[j]
            for q in range(4):
                pi = PI.get((d, q))
                if pi is not None:
                    for l in range(7):
                        if pi[l] != 0:
                            w[q][l] += pi[l] * cc
        for q in range(4):
            f = f_coeffs(i + q)
            for l in range(7):
                x = w[q][l]
                if x != 0:
                    al, be, ga = f[l]
                    X.L[i + q + 1] += x * al
                    X.L[i + q] += x * be
                    X.one += x * ga
    return X


def lam_comb(cauto, dmax, mmax):
    """SUM_(d=-3..dmax) lam(d) cauto(|d|) (b765 lam_table and its sum), exact, as SUM_e E(e) w(e): lam(d) = (1/6) SUM_i (-1)^i C(4, i)
    E(d - i), so w(e) = (1/6) SUM_i (-1)^i C(4, i) cauto(|e + i|) over e + i in [-3, dmax]; E(e) = SUM_q INT_0^1 beta_q(s) (s + c)^3
    log(s + c) ds over c = q + e >= 0."""
    X = Comb(mmax)
    for e in range(-7, dmax + 1):
        w = sum(((-1) ** i * math.comb(4, i) * cauto(abs(e + i)) for i in range(5) if -3 <= e + i <= dmax), 0)
        if w == 0:
            continue
        wq = fmpq(w, 6)
        for q in range(4):
            c = q + e
            if c < 0:
                continue
            f = f_coeffs(c)
            cq = fmpq(c)
            for l, x in enumerate(pmul(BETA[q], [cq ** 3, 3 * cq ** 2, 3 * cq, fmpq(1)])):
                if x != 0:
                    al, be, ga = f[l]
                    t = wq * x
                    X.L[c + 1] += t * al
                    if c >= 1:
                        X.L[c] += t * be
                    X.one += t * ga
    return X


def factor_table(mmax):
    spf = list(range(mmax + 1))
    for p in range(2, int(mmax ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, mmax + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factor(m, spf):
    out = {}
    while m > 1:
        p = spf[m]
        out[p] = out.get(p, 0) + 1
        m //= p
    return out


def lambda_q_exact(nmax, spf):
    """Lambda_Q(n) = b_n log n - SUM_{d|n, 1<d<n} Lambda_Q(d) b_{n/d}, b = r_Q / 2 (tools/b694_witness_terms.py :291-:317, its loop copied,
    exact): each Lambda_Q(n) a dict {p: rational coefficient of log p}, empty where it is 0. Returns (lam, r)."""
    r = [0] * (nmax + 1)
    ymax = int(2 * math.sqrt(nmax / float(DISC))) + 1
    for y in range(-ymax, ymax + 1):
        for x in range(-int(math.sqrt(nmax)) - abs(y) - 1, int(math.sqrt(nmax)) + abs(y) + 2):
            k = x * x + x * y + 6 * y * y
            if 1 <= k <= nmax:
                r[k] += 1
    b = [fmpq(r[k], 2) for k in range(nmax + 1)]
    divs = [[] for _ in range(nmax + 1)]
    for d in range(2, nmax // 2 + 1):
        for m in range(2 * d, nmax + 1, d):
            divs[m].append(d)
    lam = [dict() for _ in range(nmax + 1)]
    for n in range(2, nmax + 1):
        t = {}
        if b[n] != 0:
            for p, a in factor(n, spf).items():
                t[p] = t.get(p, fmpq(0)) + b[n] * a
        for d in divs[n]:
            e = n // d
            if b[e] != 0 and lam[d]:
                for p, x in lam[d].items():
                    t[p] = t.get(p, fmpq(0)) - x * b[e]
        lam[n] = dict((p, x) for p, x in t.items() if x != 0)
    return lam, r


# ================================================================================ THE CERTIFICATE
def ball(c, primes):
    """the combination's value as a ball at PREC bits: c = (r_0, r_gamma, r_pi, {p: r_p})."""
    r0, rg, rpi, rp = c
    v = arb(r0) + arb(rg) * arb.const_euler() + arb(rpi) * arb.pi().log()
    for p in primes:
        if rp.get(p, 0) != 0:
            v += arb(rp[p]) * arb(p).log()
    return v


def agree(v, ref):
    """the ball's midpoint against the decimal ref to DIGITS significant digits: |mid - ref| < 10^(adjusted(ref) - DIGITS + 1) / 2."""
    R = Decimal(ref)
    tol = Decimal(10) ** (R.adjusted() - DIGITS + 1) / 2
    mid = Decimal(v.mid().str(40, radius=False))
    return abs(mid - R) < tol, mid


def numer_digits(x):
    return len(str(abs(int(x.p))))


def compute():
    js, cm, L, dig = window()
    t0 = time.time()
    ctx.prec = PREC
    M = int(js['M'])
    jmax = YTOP * M - 4
    C, S = scaled(cm, M, jmax)
    S2M = fmpq(M * S * S)
    dmax = jmax - M
    mmax = jmax + 6
    spf = factor_table(mmax)
    intH = fmpq(sum(C), M * S)
    sum_abs = fmpq(sum(abs(x) for x in C), S)
    A_ = fmpz_poly(C)
    pc = (A_ * fmpz_poly(list(reversed(C)))).coeffs()

    def cauto(x):
        idx = jmax + x
        return int(pc[idx]) if 0 <= x <= dmax and idx < len(pc) else 0
    k0 = (BETA_D[0] * cauto(0) + 2 * sum((BETA_D[d] * cauto(d) for d in (1, 2, 3)), fmpq(0))) / S2M
    rho = rho_comb(C, M, jmax, mmax)
    t_rho = time.time()
    band = band_comb(C, M, jmax, mmax)
    t_band = time.time()
    lam = lam_comb(cauto, dmax, mmax)
    t_lam = time.time()
    one = Comb(mmax)
    one.one = fmpq(1)
    J = lin(mmax, (fmpq(11, 6) * k0, one), (fmpq(1) / S2M, band), (fmpq(-1) / S2M, lam))
    arch = Comb(mmax)   # ### log(sqrt 23 / (2 pi)) - gamma = (1/2) log 23 - log 2 - log pi - gamma
    arch.L[23], arch.L[2], arch.logpi, arch.gamma = fmpq(1, 2), fmpq(-1), fmpq(-1), fmpq(-1)
    A = lin(mmax, (2 * k0, arch), (fmpq(2), J))
    P = lin(mmax, (2 * intH / S, rho))
    nmax = YTOP - 1
    lq, rq = lambda_q_exact(nmax, spf)
    K, PRp = {}, {}
    for n in range(2, nmax + 1):
        if not lq[n]:
            continue
        K[n] = kn_scaled(C, M, jmax, n) / S2M
        if K[n] != 0:
            for p, x in lq[n].items():
                PRp[p] = PRp.get(p, fmpq(0)) + 2 * x * K[n]
    t_kn = time.time()
    Sc = lin(mmax, (fmpq(1), P), (fmpq(1), A))
    rp = {}
    for m, x in enumerate(Sc.L):
        if m >= 2 and x != 0:
            for p, a in factor(m, spf).items():
                rp[p] = rp.get(p, fmpq(0)) + a * x
    for p, x in PRp.items():
        rp[p] = rp.get(p, fmpq(0)) - x
    rp = dict((p, x) for p, x in rp.items() if x != 0)
    primes = sorted(rp)
    comb = (Sc.one, Sc.gamma, Sc.logpi, rp)
    Sv = ball(comb, primes)
    PRv = ball((fmpq(0), fmpq(0), fmpq(0), PRp), sorted(PRp))
    k0v = arb(k0)
    return dict(js=js, dig=dig, L=L, M=M, d=int(js['d']), S_int=S, K=K, k0=k0, intH=intH, sum_abs=sum_abs, comb=comb, primes=primes,
                Sv=Sv, PRv=PRv, k0v=k0v, nq=sum(1 for n in range(2, nmax + 1) if lq[n]), products=sum(1 for n in K if K[n] != 0),
                secs=dict(rho=int(t_rho - t0), band=int(t_band - t_rho), lam=int(t_lam - t_band), kn=int(t_kn - t_lam), all=int(time.time() - t0)))


def budget(R):
    """for each constant x (gamma, log pi, each log p) with coefficient r_x: digits d_x = floor(log10(2 N |r_x| / |S|)) + 1, N the
    number of constants, so that |r_x| 10^-d_x < |S| / (2 N) and SUM |r_x| 10^-d_x < |S| / 2; the sum checked by balls."""
    r0, rg, rpi, rp = R['comb']
    cons = [('gamma', rg), ('log pi', rpi)] + [('log %d' % p, rp[p]) for p in R['primes']]
    cons = [(n, x) for n, x in cons if x != 0]
    N = len(cons)
    aS = abs(R['Sv'])
    ln10 = arb(10).log()
    out, tot = [], arb(0)
    for n, x in cons:
        v = ((arb(abs(x)) * (2 * N)) / aS).log() / ln10
        dgt = int(math.floor(float(v.mid()))) + 1
        out.append((n, dgt))
        tot += arb(abs(x)) * arb(10) ** (-dgt)
    half = aS / 2
    uv = ((sum((arb(abs(x)) for _n, x in cons), arb(0)) * 2) / aS).log() / ln10
    uni = int(math.floor(float(uv.mid()))) + 1
    return dict(N=N, digits=out, total=tot, half=half, below=bool(tot < half), uniform=uni)


def compose(R, commit, sha):
    r0, rg, rpi, rp = R['comb']
    B = budget(R)
    nd = max([numer_digits(x) for x in [r0, rg, rpi] + list(rp.values())])
    js = dict(act=ACT, ruling='(R376)(4)(a)', at=utc(), tool=dict(path=SELF, commit=commit, sha256=sha[:16]),
              window=dict(bank=WJSON, sha256_less_final_line_end=R['dig']['text_sha'], sha256_file=R['dig']['file_sha'],
                          coef_sha=R['dig']['coef_sha'], M=R['M'], d=R['d'], ncoef=len(R['js']['coefficients'])),
              K=dict((str(n), str(R['K'][n])) for n in sorted(R['K'])), K_meaning='K(n) = n^(-1/2) k(log n), n from 2 to 1023 at which cQ(n) is not 0',
              k0=str(R['k0']), intH=str(R['intH']), sum_abs_c=str(R['sum_abs']),
              S=dict(form='S = r_0 + r_gamma gamma + r_pi log pi + SUM_p r_p log p', r_0=str(r0), r_gamma=str(rg), r_pi=str(rpi),
                     r_p=dict((str(p), str(rp[p])) for p in R['primes'])),
              primes=len(R['primes']), largest_numerator_digits=nd,
              budget=dict(constants=B['N'], digits=dict(B['digits']), uniform_digits=B['uniform'],
                          rule='each constant an equal share: digits floor(log10(2 N |r| / |S|)) + 1, the half-width 10^-digits'))
    return js, B, nd


def controls(R, js):
    out = []
    for name, ref in REF:
        v = dict(S=R['Sv'], PR=R['PRv'], k0=R['k0v'])[name]
        ok, mid = agree(v, ref)
        out.append(('%s against b765`s %s to %d digits' % (name, ref, DIGITS), '%.12g' % float(mid), ok))
    text = json.dumps(js, ensure_ascii=False, indent=1)
    back = json.loads(text)
    diff = [n for n in R['K'] if q_of(back['K'][str(n)]) != R['K'][n]]
    out.append(('the bank as composed read back: each K(n) against the computed', 'differences %d of %d' % (len(diff), len(R['K'])), not diff))
    n0 = sorted(R['K'])[len(R['K']) // 2]
    q = R['K'][n0]
    back['K'][str(n0)] = str(fmpq(int(q.p) + 1, int(q.q)))
    pd = [n for n in R['K'] if q_of(back['K'][str(n)]) != R['K'][n]]
    out.append(('PLANTED: one K(n), its numerator moved by 1, read as a difference', 'differences %s' % pd, pd == [n0]))
    return out, text


def lines(R, js, B, nd, ctl, commit, sha):
    r0, rg, rpi, rp = R['comb']
    dg = dict(B['digits'])
    pd = [d for n, d in B['digits'] if n.startswith('log ') and n != 'log pi']
    L = ['%s -- THE CERTIFICATE AT THE WINDOW M %d, d %d, BANKED AS DATA BEFORE ANY DISPATCH, (R376)(4)(a); no Lean (%s)' % (ACT, R['M'], R['d'], utc()), '',
         '### the tool %s, sha256 %s, committed at relay %s before its run; every r an exact rational (python-flint fmpq), the values read' % (SELF, sha[:16], commit),
         '### by balls at %d bits; nothing computed at a zero, no bank of zeros opened, the window`s frequency not read, no coefficient and no' % PREC,
         '### K(n) printed: each stands in %s by its n' % CJSON, ''] + R['L'] + ['',
         '## THE CERTIFICATE (%s)' % CJSON,
         '  K(n) = n^(-1/2) k(log n): %d values, n from 2 to 1023 at which cQ(n) is not 0 (cQ(n) not 0 at %d n ; b765`s rational products 269 at :19)' % (
             len(R['K']), R['nq']),
         '  k(0), the integral of H and the sum of the |c_j|: exact rationals in the bank (their numerators %d, %d and %d digits)' % (
             numer_digits(R['k0']), numer_digits(R['intH']), numer_digits(R['sum_abs'])),
         '  THE COMBINATION: S = r_0 + r_gamma gamma + r_pi log pi + SUM_p r_p log p, each r exact ; primes %d (the largest %d) ; the largest '
         'numerator %d digits' % (len(R['primes']), R['primes'][-1] if R['primes'] else 0, nd),
         '  its value by balls: S %s (radius %.3g)' % ('%.12g' % float(R['Sv'].mid()), float(R['Sv'].rad())),
         '  THE BUDGET: constants %d, each an equal share of |S| / 2: gamma %d digits, log pi %d digits, the log p from %d to %d digits ; SUM |r| '
         '10^-digits %.4g < |S| / 2 %.6g: %s ; one width for all, %d digits' % (
             B['N'], dg.get('gamma', 0), dg.get('log pi', 0), min(pd) if pd else 0, max(pd) if pd else 0, float(B['total'].mid()),
             float(B['half'].mid()), B['below'], B['uniform']),
         '  seconds: %s' % ' ; '.join('%s %d' % kv for kv in R['secs'].items()), '',
         '## THE CONTROLS ((R376)(4)(a)), the values b765`s']
    L += ['  %s: %s -- %s' % (n, g, 'AS WANTED' if ok else '### NOT AS WANTED') for n, g, ok in ctl]
    allok = all(ok for _n, _g, ok in ctl)
    L += ['', '### ### **THE CERTIFICATE %s: %d OF %d CONTROLS AS WANTED ; THE EXACT FORM %s.**' % (
        'BANKED, [E1]' if allok else 'WITH A CONTROL FAILED, [E2]', sum(1 for c in ctl if c[2]), len(ctl), 'WRITTEN')]
    return L, allok


def put(rel, s):
    p = os.path.join(ROOT, rel)
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    os.replace(p + '.tmp', p)


def main(argv):
    if not argv or argv[0] not in ('check', 'dry', 'write'):
        sys.exit(__doc__)
    commit, sha = committed()
    if argv[0] == 'check':
        _js, _cm, L, _d = window()
        print(NL.join(L))
        return 0
    R = compute()
    js, B, nd = compose(R, commit, sha)
    ctl, text = controls(R, js)
    js['controls'] = [dict(name=n, got=g, as_wanted=ok) for n, g, ok in ctl]
    L, allok = lines(R, js, B, nd, ctl, commit, sha)
    print(NL.join(L[5:]))
    if argv[0] == 'write':
        put(CJSON, json.dumps(js, ensure_ascii=False, indent=1) + NL)
        put(CTXT, NL.join(L) + NL)
        print('written', CJSON, 'and', CTXT)
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
