# -*- coding: utf-8 -*-
"""b764 -- (R374)(9)(b), W-ORD-IMP2-TAU: THE FINITE PART OF THE ARCHIMEDEAN TERM, scored against the registration H-TAU-FINITE-PART
(data/b764_registration.txt, [G1] with the author's word of 2026-11-20 in place, committed alone at relay 6fd013e9 before this tool).

Carried from tools/b763_imp2tau.py (b763, 171 lines) by the Write tool and committed before its run (N2). Kept from b763 unchanged: the
transcription (data/b232_sign_of_A.txt :94-:96), tau, the truncated integral T(eps) and its six planted controls. ADDED, as (9)(b) orders:

  THE LIMIT F. With f(rho) = k(log rho) and f(1) = k(0) ([G1] THE OBJECT), T(eps) - f(1) ln eps has a limit F as eps goes to 0. It is
  read by two routes sharing no step but tau:
    route 1, the subtraction at rho = 1: in u = log rho, tau(e^u) = (sech(u/2) + |csch(u/2)|)/4, and
        F = - integral over all u of (k(-u) - k(0) [|u| < 1]) tau(e^u) du - k(0) G0,
        G0 = lim (integral over delta < |u| < 1 of tau(e^u) du + ln delta) = 2 arctan(tanh(1/4)) + ln tanh(1/4) + ln 4 (closed form, read
        against its own quadrature, control (8));
    route 2, b763's own: T(eps) by quadrature over |rho - 1| > eps, its geometric splitting unchanged, read at eps = 10^-7 and 10^-8,
        T(10^-8) - f(1) ln 10^-8 beside route 1, and the decade's step beside -f(1) ln 10.
  The limit is REACHED at a function where the two routes agree within REACH and the step within STEP; otherwise the cell is named BEYOND
  REACH and not estimated ([G1]).

  THE CELLS ([G1] THE TEST SET): the banked diagonal a^2 cells the order names (PLACE-papers OPEN_TRAILS :3377, "at the banked diagonal a^2
  cells"; data/b232_sign_of_A.txt :31), the cells at which a bank prints A: a^2 = 2, 3, 4, 8, 9, 12 (data/b36_, b37_, b38_ and
  b40_2026-08-18.txt) and 16, 25, 36 (b40's alone). At each, as tools/e16/b40_act12.py family() builds it: w the atlas's bump on
  [-log a, log a] normalized to total 1 (tools/e16/carto_atlas.py bump), here from its definition; k = w * w, its autocorrelation, so that
  k(0) = f(1) = ||w||^2; A read from data/b40_2026-08-18.txt, the bank that prints it at all nine, its ball half its last printed digit, and
  b36's, b37's and b38's rows read equal beside it at the six.

  THE SCORE ([G1]): at each cell A against F - (log 2 pi + gamma) f(1), HELD where every cell agrees within the sum of the two balls (the
  bank's and F's: the two routes' difference); the reading (A - F) / f(1) printed at each cell, held or not. THE CONTROLS print before any
  cell, [G1]'s among them (the Gaussian k(u) = exp(-u^2), A by the digamma integral and F by the limit, each against the navigator's figures
  as [G1] prints them); no cell is computed where a control is not as wanted, nor where [G1] is not committed.

Nothing here is computed at a zero of any function; no zero enters A, T or F; no bank of zeros is opened. The A column alone is read from
the banks named.

usage:
  python -X utf8 -u tools/b764_imp2tau.py controls   the planted controls, printed; nothing written
  python -X utf8 -u tools/b764_imp2tau.py bank       the controls, then the cells and the score; data/b764_imp2tau.txt and .json written
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

import mpmath as mp

T_ = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T_)
D = os.path.join(RELAY, 'data')
if T_ not in sys.path:
    sys.path.insert(0, T_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b764_worklist as K   # noqa: E402

mp.mp.dps = 30
NL = '\n'
ACT = 'b764'
BANK, BANKJ = os.path.join(D, 'b764_imp2tau.txt'), os.path.join(D, 'b764_imp2tau.json')
REG = 'data/b764_registration.txt'
SRC = ('data/b232_sign_of_A.txt', 94, 96)
ORDER_LINES = (3367, 3375, 3377)   # ### the order's head, its transcription and its ask, in PLACE-papers OPEN_TRAILS.md at K.PRE_PP
EPS = [mp.mpf(10) ** -k for k in range(1, 9)]
LN10 = mp.log(10)
# ### INSTRUMENT CONSTANTS, COMMITTED HERE BEFORE ANY CELL IS COMPUTED
DPS_CELL = 20                       # ### the working digits at a cell
REACH = mp.mpf('1e-7')              # ### the two routes' agreement for the limit to read as reached
STEP = mp.mpf('1e-6')               # ### the last decade's step against -f(1) ln 10
CELL_EPS = (mp.mpf('1e-7'), mp.mpf('1e-8'))
A2S = (2, 3, 4, 8, 9, 12, 16, 25, 36)
A_BANK = 'data/b40_2026-08-18.txt'
A_BESIDE = ('data/b36_2026-08-18.txt', 'data/b37_2026-08-18.txt', 'data/b38_2026-08-18.txt')
NAV = dict(A='-2.5251491414', F='-0.1100564101')   # ### [G1] THE CONTROLS: the navigator's figures at k(u) = exp(-u^2), as printed


def tau(rho, odd=False):
    return mp.sqrt(rho) / 2 * (1 / (1 + rho) + (1 / (1 - rho) if odd else 1 / abs(1 - rho)))


def tau_u(u):
    """tau(e^u) = (sech(u/2) + |csch(u/2)|)/4, even in u."""
    return (mp.sech(u / 2) + 1 / abs(mp.sinh(u / 2))) / 4


def g0_closed():
    t = mp.tanh(mp.mpf(1) / 4)
    return 2 * mp.atan(t) + mp.log(t) + mp.log(4)


TRI = (lambda u: max(mp.mpf(0), mp.mpf(1) / 2 - abs(u)), (-0.5, 0.5), (0,), mp.mpf(1) / 2)
TRI2 = (lambda u: 2 * max(mp.mpf(0), mp.mpf(1) / 2 - abs(u)), (-0.5, 0.5), (0,), mp.mpf(1))
OFF = (lambda u: max(mp.mpf(0), mp.mpf(1) / 2 - abs(u - 1)), (0.5, 1.5), (1,), mp.mpf(0))
GAUSS = (lambda u: mp.exp(-u * u), (-12, 12), (), mp.mpf(1))


def trunc(fn, eps, odd=False):
    """b763's, unchanged: T(eps) = - the integral of F(-u) tau(e^u) du over u < log(1 - eps) and u > log(1 + eps), F's support split at its
    kinks and geometrically toward the excision."""
    F, (s0, s1), kinks, _f1 = fn
    a, b = mp.log(1 - eps), mp.log(1 + eps)
    g = lambda u: F(-u) * tau(mp.e ** u, odd)
    lo, hi = -mp.mpf(s1), -mp.mpf(s0)   # ### the support of u -> F(-u)
    pts = set([lo, hi] + [-mp.mpf(k) for k in kinks])
    for k in range(1, 10):
        pts.add(-mp.mpf(10) ** -k)
        pts.add(mp.mpf(10) ** -k)
    left = sorted(p for p in pts if lo <= p < a) + ([a] if a > lo else [])
    right = ([b] if b < hi else []) + sorted(p for p in pts if b < p <= hi)
    s = mp.mpf(0)
    for seg in (left, right):
        for x, y in zip(seg, seg[1:]):
            if y > x:
                s += mp.quad(g, [x, y])
    return -s


def series(fn, odd=False):
    vals = [trunc(fn, e, odd) for e in EPS]
    return vals, [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]


def route1(fn, even=True):
    """F = - integral of (F(-u) - f(1) [|u| < 1]) tau(e^u) du - f(1) G0; for an even function the half-line doubled."""
    F, (s0, s1), kinks, f1 = fn
    lo, hi = -mp.mpf(s1), -mp.mpf(s0)
    h = lambda u: (F(-u) - (f1 if abs(u) < 1 else 0)) * tau_u(u)
    a, b = min(lo, mp.mpf(-1)), max(hi, mp.mpf(1))
    pts = sorted(set([a, b, mp.mpf(-1), mp.mpf(0), mp.mpf(1), lo, hi] + [-mp.mpf(k) for k in kinks]))
    if even:
        pts = [p for p in pts if p >= 0]
    s = mp.mpf(0)
    for x, y in zip(pts, pts[1:]):
        if y > x:
            s += mp.quad(h, [x, y])
    return -(2 * s if even else s) - f1 * g0_closed()


def arch_digamma_gauss():
    """A at k(u) = exp(-u^2) by the digamma integral: (1/2 pi) integral of k-hat(r) (Re psi(1/4 + i r/2) - log pi) dr, k-hat = sqrt(pi) e^(-r^2/4)."""
    g = lambda r: mp.sqrt(mp.pi) * mp.exp(-r * r / 4) * (mp.re(mp.digamma(mp.mpc(mp.mpf(1) / 4, r / 2))) - mp.log(mp.pi))
    return 2 * mp.quad(g, [0, 2, 5, 10, 20, mp.inf]) / (2 * mp.pi)


# ================================================================================ the cells
def cell_fn(a2):
    """(k, support, kinks, k(0)) at the cell a^2: w the bump on [-L, L], L = log a, total 1; k = w * w on [-2L, 2L]."""
    L = mp.log(mp.mpf(a2)) / 2
    c0 = mp.quad(lambda t: mp.exp(-1 / (1 - t * t)), [-1, 0, 1])

    def w(v):
        t = v / L
        return mp.exp(-1 / (1 - t * t)) / (L * c0) if abs(t) < 1 else mp.mpf(0)

    cache = {}

    def k(u):
        u = abs(u)
        key = mp.nstr(u, DPS_CELL + 2)
        if key not in cache:
            cache[key] = mp.mpf(0) if u >= 2 * L else mp.quad(lambda v: w(v) * w(v - u), [u - L, (u - L + L) / 2, L])
        return cache[key]

    k0 = mp.quad(lambda v: w(v) ** 2, [-L, 0, L])
    return (k, (-2 * L, 2 * L), (), k0), w, L


def read_bank_A():
    """{a^2: (A as printed, line)} from data/b40_2026-08-18.txt, the A field alone; {path: {a^2: A}} from b36, b37 and b38 beside it."""
    out = {}
    for i, l in enumerate(io.open(os.path.join(RELAY, A_BANK), encoding='utf-8').read().split(NL), 1):
        m = re.match(r'^a\^2=(\d+)\s+A=\s*(-?\d+\.\d+)\s', l)
        if m:
            out.setdefault(int(m.group(1)), []).append((m.group(2), i))
    beside = {}
    for p in A_BESIDE:
        d = {}
        for l in io.open(os.path.join(RELAY, p), encoding='utf-8').read().split(NL):
            m = re.match(r'^(\d+)\s+(-?\d+\.\d{6})\s', l)
            if m:
                d.setdefault(int(m.group(1)), set()).add(m.group(2))
        beside[p] = d
    return out, beside


def registration():
    """(the commit that added [G1], its sha256, its committed-alone flag, the line of THE SENTENCES)."""
    log = subprocess.run(['git', '-C', RELAY, 'log', '--format=%H', '--', REG], capture_output=True, text=True).stdout.split()
    files = subprocess.run(['git', '-C', RELAY, 'show', '--name-only', '--format=', log[-1]], capture_output=True, text=True).stdout.split() if log else []
    b = open(os.path.join(RELAY, REG), 'rb').read() if os.path.exists(os.path.join(RELAY, REG)) else b''
    head = subprocess.run(['git', '-C', RELAY, 'show', 'HEAD:' + REG], capture_output=True).stdout
    sent = [l for l in b.decode('utf-8').split(NL) if l.startswith('THE SENTENCES. HELD: "')]
    return dict(commit=log[-1] if log else None, alone=files == [REG], sha=hashlib.sha256(b).hexdigest(), at_head=head == b and bool(b),
                sentences=sent[0] if len(sent) == 1 else '')


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    # ### b763's six, unchanged
    lim = [mp.nstr(tau(1 + s * mp.mpf(10) ** -12) * mp.mpf(10) ** -12, 12) for s in (-1, 1)]
    c('tau(rho) |1 - rho| at rho = 1 - 10^-12 and 1 + 10^-12, the pole even with residue 1/2 each side', lim,
      all(abs(mp.mpf(x) - mp.mpf(1) / 2) < mp.mpf(10) ** -11 for x in lim))
    w = [abs(tau(r) - (r ** mp.mpf(1.5) / (r ** 2 - 1) if r > 1 else mp.sqrt(r) / (1 - r ** 2))) for r in (mp.mpf('0.3'), mp.mpf('0.9'), mp.mpf('1.7'), mp.mpf(5))]
    c('tau against its own two branches, rho^(3/2)/(rho^2 - 1) above 1 and rho^(1/2)/(1 - rho^2) below, at four points', mp.nstr(max(w), 3), max(w) < mp.mpf(10) ** -25)
    vo, _do = series(OFF)
    c('OFF (f(1) = 0, support away from rho = 1): T(eps) one value from 10^-1 to 10^-8', mp.nstr(max(vo) - min(vo), 3), max(vo) - min(vo) < mp.mpf(10) ** -20)
    vt, dt = series(TRI)
    c('TRI (f(1) = 1/2): the last decade`s step against -f(1) ln 10 = %s' % mp.nstr(-TRI[3] * LN10, 12), mp.nstr(dt[-1], 12), abs(dt[-1] + TRI[3] * LN10) < mp.mpf(10) ** -6)
    v2, d2 = series(TRI2)
    c('TRI2 (f(1) = 1): its last step twice TRI`s', mp.nstr(d2[-1] / dt[-1], 12), abs(d2[-1] / dt[-1] - 2) < mp.mpf(10) ** -6)
    vd, dd = series(TRI, odd=True)
    c('ODD (TRI against 1/(1 - rho)): the principal value converges, its last step', mp.nstr(dd[-1], 3), abs(dd[-1]) < mp.mpf(10) ** -6)
    # ### added at b764: the limit F
    wu = [abs(tau_u(u) - tau(mp.e ** u)) for u in (mp.mpf('-1.3'), mp.mpf('-0.01'), mp.mpf('0.2'), mp.mpf(3))]
    c('tau(e^u) as (sech(u/2) + |csch(u/2)|)/4 against tau at four points', mp.nstr(max(wu), 3), max(wu) < mp.mpf(10) ** -25)
    gq = 2 * mp.quad(lambda u: tau_u(u) - 1 / (2 * u), [0, mp.mpf('0.1'), 1])
    c('G0 in closed form against its quadrature 2 * integral over (0, 1) of (tau(e^u) - 1/(2u)) du', '%s ; %s' % (mp.nstr(g0_closed(), 15), mp.nstr(gq, 15)),
      abs(g0_closed() - gq) < mp.mpf(10) ** -20)
    ft = route1(TRI)
    f8 = vt[-1] - TRI[3] * mp.log(EPS[-1])
    b763_t8 = mp.mpf('-8.4250784511297') - TRI[3] * mp.log(EPS[-1])
    c('TRI: route 1`s F against route 2`s T(10^-8) - f(1) ln 10^-8, and against b763`s banked T(10^-8) (data/b763_imp2tau.txt :15)',
      '%s ; %s ; %s' % (mp.nstr(ft, 13), mp.nstr(f8, 13), mp.nstr(b763_t8, 13)), abs(ft - f8) < REACH and abs(ft - b763_t8) < REACH)
    fo = route1(OFF, even=False)
    c('OFF: route 1`s F (f(1) = 0) equals T at every eps, and b763`s banked -0.18102992952218 (:19)', '%s ; %s' % (mp.nstr(fo, 15), mp.nstr(vo[-1], 15)),
      abs(fo - vo[-1]) < mp.mpf(10) ** -20 and abs(fo - mp.mpf('-0.18102992952218')) < mp.mpf(10) ** -13)
    f2 = route1(TRI2)
    c('TRI2: route 1`s F twice TRI`s (F is linear in f)', mp.nstr(f2 / ft, 15), abs(f2 - 2 * ft) < mp.mpf(10) ** -20)
    # ### [G1]'s control: the Gaussian
    ag = arch_digamma_gauss()
    fg = route1(GAUSS)
    fg8 = trunc(GAUSS, EPS[-1]) - GAUSS[3] * mp.log(EPS[-1])
    rhs = fg - (mp.log(2 * mp.pi) + mp.euler) * GAUSS[3]
    c('[G1]`s control at k(u) = exp(-u^2): A by the digamma integral against the navigator`s %s to the digits printed' % NAV['A'], mp.nstr(ag, 13),
      abs(ag - mp.mpf(NAV['A'])) < mp.mpf('5e-11'))
    c('[G1]`s control: F by route 1 against the navigator`s %s to the digits printed, and route 2 at 10^-8 within REACH' % NAV['F'],
      '%s ; %s' % (mp.nstr(fg, 13), mp.nstr(fg8, 13)), abs(fg - mp.mpf(NAV['F'])) < mp.mpf('5e-11') and abs(fg - fg8) < REACH)
    c('[G1]`s control: F - (log 2 pi + gamma) f(1) against A by the digamma integral, the two agreeing, each %s to the digits printed' % NAV['A'],
      '%s ; %s ; differ %s' % (mp.nstr(rhs, 13), mp.nstr(ag, 13), mp.nstr(abs(rhs - ag), 3)),
      abs(rhs - ag) < mp.mpf(10) ** -20 and abs(rhs - mp.mpf(NAV['A'])) < mp.mpf('5e-11'))
    # ### the cells' instruments, before any cell
    out, beside = read_bank_A()
    once = sorted(a for a in A2S if len(out.get(a, [])) == 1)
    eq6 = all(all(beside[p].get(a) == {out[a][0][0]} for p in A_BESIDE) for a in (2, 3, 4, 8, 9, 12))
    plant = dict((p, dict(beside[p])) for p in A_BESIDE)
    plant[A_BESIDE[0]][2] = {'-1.990529'}
    eq6p = all(all(plant[p].get(a) == {out[a][0][0]} for p in A_BESIDE) for a in (2, 3, 4, 8, 9, 12))
    c('the A reader: b40`s nine cells each read once (%s) ; b36`s, b37`s and b38`s rows equal to it at the six ; a planted last digit at a^2 = 2 read different'
      % ', '.join('%d %s :%d' % (a, out[a][0][0], out[a][0][1]) for a in once), (len(once), eq6, eq6p), len(once) == 9 and eq6 and not eq6p)
    with mp.workdps(DPS_CELL):
        fn, wf, Lc = cell_fn(2)
        tot_w = mp.quad(wf, [-Lc, 0, Lc])
        tot_k = 2 * mp.quad(fn[0], [0, Lc, 2 * Lc])
        c('the cell`s function at a^2 = 2: the bump`s total 1, its autocorrelation`s total 1 (the square of the first), k(0) = ||w||^2 = %s' % mp.nstr(fn[3], 12),
          '%s ; %s' % (mp.nstr(tot_w, 15), mp.nstr(tot_k, 15)), abs(tot_w - 1) < mp.mpf(10) ** -15 and abs(tot_k - 1) < mp.mpf(10) ** -12)
    R = registration()
    c('[G1] committed alone before this run (%s), its bytes at HEAD, sha256 %s' % (str(R['commit'])[:8], R['sha'][:16]), (R['alone'], R['at_head']),
      bool(R['commit']) and R['alone'] and R['at_head'] and bool(R['sentences']))
    return L, ok, dict(TRI=(vt, dt), TRI2=(v2, d2), OFF=(vo, None), ODD=(vd, dd), GAUSS=dict(A=ag, F=fg, F8=fg8, rhs=rhs), R=R, bank=out)


def cell(a2, A_txt):
    t0 = time.time()
    with mp.workdps(DPS_CELL):
        fn, _w, L = cell_fn(a2)
        k0 = fn[3]
        f1r = route1(fn)
        t7 = trunc(fn, CELL_EPS[0])
        t8 = trunc(fn, CELL_EPS[1])
        f2r = t8 - k0 * mp.log(CELL_EPS[1])
        step = t8 - t7
        reached = abs(f1r - f2r) < REACH and abs(step + k0 * LN10) < STEP
        C = mp.log(2 * mp.pi) + mp.euler
        A = mp.mpf(A_txt)
        dec = len(A_txt.split('.')[1])
        ball_A = mp.mpf(5) * mp.mpf(10) ** -(dec + 1)
        ball_F = abs(f1r - f2r)
        rhs = f1r - C * k0
        diff = A - rhs
        return dict(a2=a2, L=mp.nstr(L, 12), f1=mp.nstr(k0, 15), F1=mp.nstr(f1r, 15), F2=mp.nstr(f2r, 15), step=mp.nstr(step, 12),
                    step_want=mp.nstr(-k0 * LN10, 12), reached=bool(reached), A=A_txt, rhs=mp.nstr(rhs, 15), diff=float(diff), ball=float(ball_A + ball_F),
                    within=bool(abs(diff) <= ball_A + ball_F), reading=mp.nstr((A - f1r) / k0, 10), secs=round(time.time() - t0, 1))


def _digest_pp(n):
    b = subprocess.run(['git', '-C', K.PP, 'show', '%s:OPEN_TRAILS.md' % K.PRE_PP], capture_output=True).stdout
    ln = b.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    return hashlib.sha256(ln[n - 1].encode('utf-8')).hexdigest()[:16] if len(ln) >= n else None


def score(rows, R):
    C = mp.log(2 * mp.pi) + mp.euler
    beyond = [r['a2'] for r in rows if not r['reached']]
    if beyond:
        why = 'the two routes or the decade`s step not within REACH %s and STEP %s' % (mp.nstr(REACH, 2), mp.nstr(STEP, 2))
        sent = re.search(r'NOT SCORABLE: "(.*?)"\.', R['full']).group(1).replace('<the cells>', ', '.join('a^2 = %d' % a for a in beyond)).replace('<why>', why)
        return 'NOT SCORABLE', sent, None
    bad = [r for r in rows if not r['within']]
    if not bad:
        md = max(abs(r['diff']) for r in rows)
        d = min(min(len(r['A'].split('.')[1]) for r in rows), int(mp.floor(-mp.log10(2 * md))) if md > 0 else 99)
        held = R['sentences'][len('THE SENTENCES. HELD: "'):]
        held = held[:held.index('". REFUTED: "')]
        return 'HELD', held.replace('<n>', str(len(rows)), 1).replace('<d>', str(d), 1), d
    vals = [mp.mpf(r['reading']) for r in rows]
    const = max(vals) - min(vals) < mp.mpf('1e-5')
    how = 'the constant differs and the integral agrees' if const else 'the integral differs'
    ref = re.search(r'REFUTED: "(.*?)"\. NOT SCORABLE', R['full']).group(1)
    ref = ref.replace('<the cells>', ', '.join('a^2 = %d' % r['a2'] for r in bad)).replace('<the values>', ', '.join(
        '%s at a^2 = %d' % (r['reading'], r['a2']) for r in rows)).replace('<the constant differs and the integral agrees, or the integral differs>', how)
    _ = C
    return 'REFUTED', ref, None


def bank():
    t0 = time.time()
    L, ok, X = controls()
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    print(NL.join(L))
    print('### CONTROLS %d OF %d (%.0f s)' % (sum(ok), len(ok), time.time() - t0))
    R = X['R']
    R['full'] = open(os.path.join(RELAY, REG), encoding='utf-8').read()
    rows = []
    if all(ok):
        for a2 in A2S:
            r = cell(a2, X['bank'][a2][0][0])
            rows.append(r)
            print('  a^2 = %-3d f(1) %s ; F route 1 %s ; route 2 %s ; reached %s ; A %s ; F - (log 2pi + gamma) f(1) %s ; differ %.2e (ball %.2e) ; '
                  '(A - F)/f(1) %s ; %.0f s' % (a2, r['f1'], r['F1'], r['F2'], r['reached'], r['A'], r['rhs'], r['diff'], r['ball'], r['reading'], r['secs']))
        verdict, sentence, d = score(rows, R)
    else:
        verdict, sentence, d = 'NOT SCORABLE', re.search(r'NOT SCORABLE: "(.*?)"\.', R['full']).group(1).replace(
            '<the cells>', 'every cell').replace('<why>', 'a control of the tool not as wanted, so no cell was computed'), None
    dg = dict((n, _digest_pp(n)) for n in ORDER_LINES)
    C = mp.log(2 * mp.pi) + mp.euler
    out = ['b764 -- (R374)(9)(b), W-ORD-IMP2-TAU: THE FINITE PART F OF THE TRANSCRIBED ARCHIMEDEAN INTEGRAL AT rho = 1, SCORED AGAINST THE '
           'REGISTRATION H-TAU-FINITE-PART (%s, tools/b764_imp2tau.py bank)' % stamp, '',
           '### the registration: relay %s, committed alone at %s before this tool (sha256 %s), its HELD sentence with the author`s word of 2026-11-20 in place'
           % (REG, str(R['commit'])[:8], R['sha'][:16]),
           '### the order: PLACE-papers OPEN_TRAILS.md at %s, :%d (sha256 %s), its transcription :%d (sha256 %s), its ask :%d (sha256 %s), read by path, '
           'line and digest; the transcription computed here is the relay`s %s :%d-:%d' % (
               K.PRE_PP[:8], ORDER_LINES[0], dg[ORDER_LINES[0]], ORDER_LINES[1], dg[ORDER_LINES[1]], ORDER_LINES[2], dg[ORDER_LINES[2]], *SRC),
           '### T(eps) = - the integral over |rho - 1| > eps of f(rho^-1) tau(rho) d*rho, f(rho) = k(log rho), in u = log rho; F = lim T(eps) - f(1) ln eps by '
           'route 1 (the subtraction at rho = 1, G0 in closed form) and route 2 (b763`s truncation at 10^-7 and 10^-8); mpmath %s, controls at %d digits, '
           'cells at %d; REACH %s, STEP %s' % (mp.__version__, mp.mp.dps, DPS_CELL, mp.nstr(REACH, 2), mp.nstr(STEP, 2)),
           '### A at each cell from %s, the A field alone, its ball half its last printed digit; %s beside it at the six; the constant log 2 pi + gamma = %s'
           % (A_BANK, ', '.join(A_BESIDE), mp.nstr(C, 15)),
           '', '## THE CONTROLS, BEFORE ANY CELL'] + L
    out += ['', '## b763`S READINGS, T(eps) AND ITS STEP A DECADE, AT THE PLANTED FUNCTIONS']
    for k in ('TRI', 'TRI2', 'OFF', 'ODD'):
        v, dd = X[k]
        out.append('  %s: %s' % (k, ' ; '.join('eps 1e-%d %s' % (i + 1, mp.nstr(x, 14)) for i, x in enumerate(v))))
        if dd:
            out.append('  %s, the step a decade: %s' % (k, ' ; '.join(mp.nstr(x, 12) for x in dd)))
    G = X['GAUSS']
    out += ['  GAUSS, k(u) = exp(-u^2): A by the digamma integral %s ; F by route 1 %s ; by route 2 at 10^-8 %s ; F - (log 2 pi + gamma) f(1) %s' % (
        mp.nstr(G['A'], 15), mp.nstr(G['F'], 15), mp.nstr(G['F8'], 15), mp.nstr(G['rhs'], 15))]
    out += ['', '## THE CELLS: a^2 | f(1) = k(0) | F by route 1 | by route 2 | the step 10^-7 -> 10^-8 against -f(1) ln 10 | reached | A (the bank) | '
                'F - (log 2 pi + gamma) f(1) | A less it | the ball | (A - F) / f(1)']
    for r in rows:
        out.append('  %d | %s | %s | %s | %s against %s | %s | %s | %s | %+.3e | %.3e | %s' % (
            r['a2'], r['f1'], r['F1'], r['F2'], r['step'], r['step_want'], 'REACHED' if r['reached'] else 'BEYOND REACH', r['A'], r['rhs'], r['diff'], r['ball'], r['reading']))
    if not rows:
        out.append('  none computed: a control not as wanted')
    out += ['', '## THE SCORE OF H-TAU-FINITE-PART', '  %s' % verdict, '  THE SENTENCE: %s' % sentence,
            '  THE READING AT EACH CELL, HELD OR NOT ([G1]): (A - F) / f(1) against -(log 2 pi + gamma) = %s' % mp.nstr(-C, 10)]
    foot = '### ### **H-TAU-FINITE-PART: %s ; CELLS %d%s ; CONTROLS %d OF %d ; %.0f s.**' % (
        verdict, len(rows), (' TO %d DIGITS' % d) if d is not None else '', sum(ok), len(ok), time.time() - t0)
    out.append(foot)
    with io.open(BANK, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(NL.join(out) + NL)
    J = dict(act=ACT, at=stamp, registration=dict(path=REG, commit=R['commit'], sha256=R['sha']), order_lines=dict((str(n), dg[n]) for n in ORDER_LINES),
             source=list(SRC), controls=[sum(ok), len(ok)], cells=rows, verdict=verdict, sentence=sentence, digits=d, a_bank=A_BANK,
             constants=dict(DPS_CELL=DPS_CELL, REACH=str(REACH), STEP=str(STEP), CELL_EPS=[str(e) for e in CELL_EPS]), foot=foot)
    with io.open(BANKJ, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(J, indent=1, ensure_ascii=False) + NL)
    print(NL.join(out[-6:]))
    print('written data/b764_imp2tau.txt and data/b764_imp2tau.json')
    return all(ok)


if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else ''
    if m == 'controls':
        t0_ = time.time()
        L_, ok_, _X = controls()
        print(NL.join(L_))
        print('### CONTROLS %d OF %d (%.0f s)' % (sum(ok_), len(ok_), time.time() - t0_))
        sys.exit(0 if all(ok_) else 1)
    if m == 'bank':
        sys.exit(0 if bank() else 1)
    sys.exit(__doc__)
