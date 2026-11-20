# -*- coding: utf-8 -*-
"""b763 -- (R373)(8), W-ORD-IMP2-TAU, built as a tool of this act with its bank, on no kernel branch (data/b763_misses.txt (5)).

THE ORDER (PLACE-papers OPEN_TRAILS :3367-:3380, read by path, line and digest; its line :3377 asks the principal value at rho = 1):
compute CC's own archimedean term, eq. (53) with (39), at the banked diagonal a^2 cells and compare it with -A. THE TRANSCRIPTION READ
here is the relay's own of the same two displays, data/b232_sign_of_A.txt :95-:96 (b232's read of arXiv 2006.13771):

    W_inf(f) = - integral of f(rho^-1) tau(rho) d*rho,   tau(rho) = rho^(1/2)/2 * ( 1/(1+rho) + 1/|1-rho| ),   d*rho = d rho / rho.

WHAT THIS TOOL COMPUTES. In u = log rho (d*rho = du, f(rho^-1) = F(-u) with F(u) = f(e^u)) the truncated integral
T(eps) = - integral over |rho - 1| > eps, for eps = 10^-1 to 10^-8, at planted test functions, by mpmath's quadrature at 30 digits, each
interval split geometrically toward the excision. tau carries an EVEN pole at rho = 1: tau(rho) |1 - rho| -> 1/2 from both sides, so the
two sides of the excision add and do not cancel, and T(eps) moves by -F(0) ln 10 a decade wherever F(0) = f(1) is not 0. Every test
function the order names is an autocorrelation, Q^W(g) = W_inf(g * g*) (data/b232_sign_of_A.txt :94), and f(1) = ||g||^2 > 0 there for
g not 0; so at each diagonal cell the transcribed principal value has no finite value, and its comparison with -A is not made by this
tool. The constant of the finite part at rho = 1 is CC's, stated in their text; no other regularization is put in its place here.

THE PLANTED FUNCTIONS: TRI, the autocorrelation of the indicator of [0, 1/2] in u, F(u) = max(0, 1/2 - |u|), F(0) = 1/2; TRI2 = 2 TRI;
OFF, F(u) = max(0, 1/2 - |u - 1|), F(0) = 0, its support away from u = 0; and ODD, TRI against the kernel with 1/(1 - rho) in place of
1/|1 - rho|, whose odd pole has a principal value (the control that the instrument sees a convergent principal value beside a pole).
Nothing here is computed at a zero of any function; no zero enters W_inf.

usage:
  python -X utf8 -u tools/b763_imp2tau.py controls   the planted controls, printed; nothing written
  python -X utf8 -u tools/b763_imp2tau.py bank       the controls and the readings; data/b763_imp2tau.txt and .json written
"""
import hashlib
import io
import json
import os
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
import b763_worklist as K   # noqa: E402

mp.mp.dps = 30
NL = '\n'
ACT = 'b763'
BANK, BANKJ = os.path.join(D, 'b763_imp2tau.txt'), os.path.join(D, 'b763_imp2tau.json')
SRC = ('data/b232_sign_of_A.txt', 94, 96)
ORDER_LINES = (3367, 3375, 3377)   # ### the order's head, its transcription and its ask, in PLACE-papers OPEN_TRAILS.md at K.PRE_PP
EPS = [mp.mpf(10) ** -k for k in range(1, 9)]
LN10 = mp.log(10)


def tau(rho, odd=False):
    return mp.sqrt(rho) / 2 * (1 / (1 + rho) + (1 / (1 - rho) if odd else 1 / abs(1 - rho)))


TRI = (lambda u: max(mp.mpf(0), mp.mpf(1) / 2 - abs(u)), (-0.5, 0.5), (0,), mp.mpf(1) / 2)
TRI2 = (lambda u: 2 * max(mp.mpf(0), mp.mpf(1) / 2 - abs(u)), (-0.5, 0.5), (0,), mp.mpf(1))
OFF = (lambda u: max(mp.mpf(0), mp.mpf(1) / 2 - abs(u - 1)), (0.5, 1.5), (1,), mp.mpf(0))


def trunc(fn, eps, odd=False):
    """T(eps) = - the integral of F(-u) tau(e^u) du over u < log(1 - eps) and u > log(1 + eps), F's support split at its kinks and
    geometrically toward the excision."""
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


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

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
    return L, ok, dict(TRI=(vt, dt), TRI2=(v2, d2), OFF=(vo, None), ODD=(vd, dd))


def _digest_pp(n):
    b = subprocess.run(['git', '-C', K.PP, 'show', '%s:OPEN_TRAILS.md' % K.PRE_PP], capture_output=True).stdout
    ln = b.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    return hashlib.sha256(ln[n - 1].encode('utf-8')).hexdigest()[:16] if len(ln) >= n else None


def bank():
    t0 = time.time()
    L, ok, R = controls()
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    dg = dict((n, _digest_pp(n)) for n in ORDER_LINES)
    out = ['b763 -- (R373)(8), W-ORD-IMP2-TAU: CC`S ARCHIMEDEAN TERM AS THE RECORD TRANSCRIBES IT, ITS PRINCIPAL VALUE AT rho = 1 READ AT '
           'PLANTED AUTOCORRELATIONS (%s, tools/b763_imp2tau.py bank; data/b763_misses.txt (5))' % stamp, '',
           '### the order: PLACE-papers OPEN_TRAILS.md at %s, :%d (sha256 %s), its transcription :%d (sha256 %s), its ask :%d (sha256 %s), '
           'read by path, line and digest; the transcription computed here is the relay`s %s :%d-:%d' % (
               K.PRE_PP[:8], ORDER_LINES[0], dg[ORDER_LINES[0]], ORDER_LINES[1], dg[ORDER_LINES[1]], ORDER_LINES[2], dg[ORDER_LINES[2]], *SRC),
           '### T(eps) = - the integral over |rho - 1| > eps of f(rho^-1) tau(rho) d*rho, in u = log rho, mpmath %s at %d digits' % (mp.__version__, mp.mp.dps),
           '', '## THE CONTROLS'] + L + ['', '## THE READINGS, T(eps) AND ITS STEP A DECADE']
    for k in ('TRI', 'TRI2', 'OFF', 'ODD'):
        v, d = R[k]
        out.append('  %s: %s' % (k, ' ; '.join('eps 1e-%d %s' % (i + 1, mp.nstr(x, 14)) for i, x in enumerate(v))))
        if d:
            out.append('  %s, the step a decade: %s' % (k, ' ; '.join(mp.nstr(x, 12) for x in d)))
    st = R['TRI'][1][-1]
    out += ['', '## THE READING',
            '  The transcribed tau has an even pole at rho = 1, residue 1/2 from each side (control (1)); the two sides of the excision add, so '
            'T(eps) at an f with f(1) not 0 moves by -f(1) ln 10 a decade without end (TRI %s a decade at f(1) = 1/2, TRI2 twice it), while an f '
            'vanishing near rho = 1 and the odd kernel converge (OFF, ODD). The principal value the order asks has no finite value at any f with '
            'f(1) not 0.' % mp.nstr(st, 10),
            '  Each test function the order names is an autocorrelation, Q^W(g) = W_inf(g * g*) (%s :%d), with f(1) = ||g||^2 > 0 for g not 0: '
            'at every diagonal a^2 cell the transcribed integral diverges as f(1) log(1/eps), so its comparison with -A is NOT MADE by this tool.' % SRC[:2],
            '  The finite part at rho = 1 needs a constant that CC state in their text; that text is not on this host and (R373)(12) fetches '
            'nothing, so no regularization is put in its place. W-ORD-IMP2-TAU is carried by name with its price and this reading.']
    foot = '### ### **THE IMP2-TAU READING: THE TRANSCRIBED PRINCIPAL VALUE DIVERGES AT f(1) NOT 0, ITS STEP A DECADE -f(1) ln 10 (TRI %s) ; ' \
           'THE COMPARISON WITH -A NOT MADE ; CONTROLS %d OF %d ; %.0f s.**' % (mp.nstr(st, 10), sum(ok), len(ok), time.time() - t0)
    out.append(foot)
    with io.open(BANK, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(NL.join(out) + NL)
    J = dict(act=ACT, at=stamp, order_lines=dict((str(n), dg[n]) for n in ORDER_LINES), source=list(SRC), controls=[sum(ok), len(ok)],
             readings=dict((k, dict(T=[mp.nstr(x, 20) for x in R[k][0]], step=[mp.nstr(x, 20) for x in R[k][1]] if R[k][1] else None)) for k in R),
             outcome='DIVERGES AT f(1) NOT 0 ; THE COMPARISON WITH -A NOT MADE', foot=foot)
    with io.open(BANKJ, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(J, indent=1, ensure_ascii=False) + NL)
    print(NL.join(out))
    print('written data/b763_imp2tau.txt and data/b763_imp2tau.json')
    return all(ok)


if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else ''
    if m == 'controls':
        L_, ok_, _R = controls()
        print(NL.join(L_))
        print('### CONTROLS %d OF %d' % (sum(ok_), len(ok_)))
        sys.exit(0 if all(ok_) else 1)
    if m == 'bank':
        sys.exit(0 if bank() else 1)
    sys.exit(__doc__)
