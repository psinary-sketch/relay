# -*- coding: utf-8 -*-
"""b696_witness_balls.py -- (R306)(3): THE WEIL-FACE WITNESS AT Q0 WITH ITS TWO TAIL BOUNDS AS CERTIFIED BALLS, ON THE AUTHOR'S WORD AT
PROMPT 3 ("run as written"; relay data/b696_author_answers.txt), THE PLAN relay data/b696_tails_plan.txt.

### b694's window, prime sum and integral IMPORTED from tools/b694_witness_terms.py unedited (Window :106, lambda_q :291, lambda_z :320,
### prime_sum :346, the bracket :362, q0_zeros :437, zero_side :454); its two float tails (tail_bound :266, zero_tail :462) are NOT called:
###   (a) the archimedean tail beyond R as a ball, the plan's (2): DLMF (5.11.2) with its remainder bound at n = 1 (relay
###       data/b696_source_dlmf_5_11.txt :105-:107, :393-:399), |sinc w| <= 1/|w| on the line; the closed form in arb, no float, no factor;
###   (b) the zeros above T0 as a ball on P3's count law, the plan's (3): b685's a and c as balls (data/b685_count.txt :21, :23), HSW
###       Corollary 1.2 at zeta (data/b685_search.txt :65-:66); 4000 unit intervals in arb and the rest by the integral of the majorant.
### Every value a ball (python-flint arb/acb) at 128 bits; T1's rung at 256.
### Routes (resumable, one unit per cell appended to the untracked data/b696_witness_balls_units.jsonl), in the plan's parts:
###   tails                   (p1) the two bounds printed once with their lines, then every tail ball at both heights
###   zeta <fam>              (p2) C1: the terms at zeta with (a)'s ball, before any Q0 term
###   q0 <fam> | c2           (p3) the terms at Q0 (refused until C1 reads nonnegative at every width of both families); C2
###   identity <obj> <fam> | identity_c2   (p4) C3: the zero side against S with (b)'s ball
###   t1                      (p5) T1 at a = 32: S with R = 8000 and the integral over [4000, 8000]; S at 256 bits
###   bank                    (p6) data/b696_witness_balls.txt, _controls.txt, .json.gz beside _hashes.txt
### Written by the Write tool at b696; it writes only the banks it names and its units file.
"""
import gzip
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import acb, arb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b694_witness_terms as W   # noqa: E402  ### imported unedited; its float tails are not called

PREC = 128
ctx.prec = PREC
UNITS = os.path.join(D, 'b696_witness_balls_units.jsonl')
LADDER, B518_A, B518_G0, FAMS = W.LADDER, W.B518_A, W.B518_G0, W.FAMS
R_HEIGHTS = (4000, 8000)               # ### (a)'s two heights: b694's R_INT and its double
T0_HEIGHTS = ('151.59', '303.18')      # ### (b)'s two heights: the zero lists' top (tools/b694_witness_terms.py :57) and its double
J_SUM = 4000                           # ### (b)'s unit intervals summed in arb before the integral of the majorant
B694_GZ = os.path.join(D, 'b694_witness.json.gz')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def bs(x):
    x = arb(x)
    return [x.mid().str(45, radius=False), x.rad().str(5, radius=False)]


def bl(p):
    return arb(p[0], p[1])


def fmt(x, n=12):
    x = arb(x)
    return '%s +- %s' % (x.mid().str(n, radius=False), x.rad().str(3, radius=False))


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['fam'], u['a'], u['obj'], u['prec'], str(u.get('h', '')))] = u
    return U


def put_unit(u):
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


def unit_ball(r):
    """the ball [-r, r] for a nonnegative ball r: [-1, 1] times r."""
    return arb(0, 1) * arb(r)


# ================================================================================ (a) THE ARCHIMEDEAN TAIL AS A BALL
def arch_tail(Wd, obj, R):
    """(1/2pi) INT_{|r| > R} |k^(r)| |bracket(r)| dr <= (1/pi) (2/(theta s))^12 R^(1-p) [alpha (ln R/(p-1) + 1/(p-1)^2) + beta/(p-1)]: the plan's
    (2), every constant a ball. p = 8 (N) or 12 (C); theta = 1 - g0/R; alpha 2, beta_Q at Q0; alpha 1, beta_Z at zeta."""
    R = arb(R)
    s, g0 = Wd.s, Wd.g0
    assert R > 2 * g0
    theta = 1 - g0 / R
    p = 8 if Wd.fam == 'N' else 12
    Kc = (2 / (theta * s)) ** 12
    r2 = arb(2).sqrt()
    if obj == 'q0':
        alpha = arb(2)
        beta = 2 * abs((2 * arb.pi() / arb(23).sqrt()).log()) + 1 / R + (arb(1) / 4 + r2 / 3) / (R * R)
    else:
        alpha = arb(1)
        beta = (arb.pi() / 2).log() + 1 / R + (arb(1) / 8 + 2 * r2 / 3) / (R * R)
    q = arb(p - 1)
    return Kc * R ** (1 - p) * (alpha * (R.log() / q + 1 / (q * q)) + beta / q) / arb.pi()


# ================================================================================ (b) THE ZERO-SIDE TAIL AS A BALL, ON P3
A_P3 = arb('0.432571915432', '4.33e-41')     # ### data/b685_count.txt :21
C_P3 = arb('1.26244217716', '1.26e-40')      # ### data/b685_count.txt :23 (b = 0, :22)
HSW = (arb('0.1038'), arb('0.2573'), arb('9.3675'))   # ### data/b685_search.txt :65


def count_unit(obj, u):
    """an upper bound on the zeros with ordinate in (u, u + 1] (u >= 149 at Q0): M'(u + 1) + 2 R(u + 1)."""
    x = u + 1
    if obj == 'q0':
        return (arb(23).sqrt() * x / (2 * arb.pi())).log() / arb.pi() + 2 * (A_P3 * x.log() + C_P3)
    return (x / (2 * arb.pi())).log() / (2 * arb.pi()) + 2 * (HSW[0] * x.log() + HSW[1] * x.log().log() + HSW[2])


def zero_tail(Wd, obj, T0):
    """the zeros above T0: SUM over [T0 + j, T0 + j + 1], j < J_SUM, of the count times 2 |k^| at the left end, in arb; the rest by the
    integral from U = T0 + J_SUM - 1 of 2 G u^-q (A1 ln u + B1), in closed form. |k^(gamma - i delta)| <= [(gamma^2 + Y^2 + g0^2)^[N]
    e^(3 Y s) (2/(theta' s gamma))^6]^2, |delta| <= Y (1 at Q0, 1/2 at zeta), theta' = 1 - g0/T0: the plan's (3)."""
    T0 = arb(T0)
    s, g0 = Wd.s, Wd.g0
    Y = arb(1) if obj == 'q0' else arb(1) / 2
    th = 1 - g0 / T0
    E = (3 * Y * s).exp()
    N_ = Wd.fam == 'N'

    def F(u):
        h = E * (2 / (th * s * u)) ** 6
        if N_:
            h = (u * u + Y * Y + g0 * g0) * h
        return h * h
    tot = arb(0)
    for j in range(J_SUM):
        u = T0 + j
        tot += count_unit(obj, u) * 2 * F(u)
    rem = zero_integral(Wd, obj, T0 + (J_SUM - 1), T0)
    return tot + rem, tot, rem


def zero_integral(Wd, obj, U, T0):
    """the integral from U of the decreasing majorant 2 G u^-q (A1 ln u + B1) of the zero side's terms above T0, in closed form (the plan's
    (3)); from U = T0 + J_SUM - 1 it is (b)'s remainder, and from U = T0 the bound's own prediction of its scaling with the height."""
    T0, U = arb(T0), arb(U)
    s, g0 = Wd.s, Wd.g0
    Y = arb(1) if obj == 'q0' else arb(1) / 2
    th = 1 - g0 / T0
    E = (3 * Y * s).exp()
    N_ = Wd.fam == 'N'
    if obj == 'q0':
        A1 = 1 / arb.pi() + 2 * A_P3
        B1 = (arb(23).sqrt() / (2 * arb.pi())).log() / arb.pi() + 2 * C_P3 + A1 / U
    else:
        A1 = 1 / (2 * arb.pi()) + 2 * HSW[0] + 2 * HSW[1]
        B1 = -(2 * arb.pi()).log() / (2 * arb.pi()) + 2 * HSW[2] + A1 / U
    kap = (1 + (Y * Y + g0 * g0) / (U * U)) if N_ else arb(1)
    G = (kap * E * (2 / (th * s)) ** 6) ** 2
    q = arb(8 if N_ else 12)
    return 2 * G * U ** (1 - q) * (A1 * (U.log() / (q - 1) + 1 / ((q - 1) * (q - 1))) + B1 / (q - 1))


# ================================================================================ THE TERMS WITH (a)'S BALL
def a_int(Wd, obj, lo, hi):
    """(1/pi) INT_lo^hi k^(r) bracket(r) dr, acb.integral per chunk of W.CHUNK at the tolerances b694 used (tools/b694_witness_terms.py :374)."""
    f = lambda z, an: Wd.khat(z) * W.bracket(obj, z)   # noqa: E731
    tot = acb(0)
    for e in range(lo, hi, W.CHUNK):
        tot += acb.integral(f, e, e + W.CHUNK, rel_tol=arb(2) ** -110, abs_tol=arb(2) ** -110)
    return 2 * tot.real / (2 * arb.pi())


def terms(Wd, obj, R=R_HEIGHTS[0]):
    t0 = time.time()
    nmax = int(math.floor(math.exp(2 * float(Wd.L.mid())) + 1e-9))
    P = (Wd.khat(acb(0, 0.5)) + Wd.khat(acb(0, -0.5))).real
    lam = W.lambda_q(nmax)[0] if obj == 'q0' else W.lambda_z(nmax)
    PR, nterms, _absum = W.prime_sum(Wd, lam, nmax)
    Ai = a_int(Wd, obj, 0, R)
    tl = arch_tail(Wd, obj, R)
    A = Ai + unit_ball(tl)
    S = P - PR + A
    return dict(P=bs(P), PR=bs(PR), Aint=bs(Ai), tail=bs(tl), A=bs(A), S=bs(S), nmax=nmax, prime_terms=nterms, R=R, seconds=int(time.time() - t0))


def reading(S):
    S = bl(S) if isinstance(S, list) else S
    if S < 0:
        return 'NEGATIVE BEYOND ITS BOUND'
    if S > 0:
        return 'NONNEGATIVE BEYOND ITS BOUND'
    return 'UNDECIDED'


# ================================================================================ (p1) THE TWO BOUNDS PRINTED WITH THEIR LINES, THEN THE TAIL BALLS
def _lines(name, a, b):
    L = io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '').split(NL)
    return ['    %s :%d  %s' % (name, i, L[i - 1]) for i in range(a, b + 1)]


def _plan_lines(*needles):
    L = io.open(os.path.join(D, 'b696_tails_plan.txt'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    out = []
    for nd in needles:
        i = next(k for k, l in enumerate(L) if nd in l)
        j = i + 1
        while j < len(L) and L[j].startswith(' ' * 20) and not L[j].lstrip().startswith(('THE ', 'TWO ')):
            j += 1
        out += ['    data/b696_tails_plan.txt :%d  %s' % (k + 1, L[k]) for k in range(i, j)]
    return out


def tails(*a):
    """(p1): the DLMF remainder bound and the sinc bound printed once with their lines (the author's word at prompt 3), then every tail ball
    -- (a) at R 4000 and 8000, (b) at T0 151.59 and 303.18 -- for both families, every width, both objects; each unit banked."""
    pr = ['### THE DLMF EXPANSION AND ITS REMAINDER BOUND, AS BANKED (NIST DLMF section 5.11, fetched by tools/b696_tails_source.py):'] + \
        _lines('b696_source_dlmf_5_11.txt', 105, 107) + _lines('b696_source_dlmf_5_11.txt', 393, 399) + \
        ['### THE SINC BOUND AND THE TERM BOUNDS, AS THE PLAN DERIVES THEM:'] + _plan_lines('THE TRANSFORM (', 'THE TERM BOUND:')
    print(NL.join(pr), flush=True)
    U = units()
    if ('bounds', '', '', '', PREC, '') not in U:
        put_unit(dict(route='bounds', fam='', a='', obj='', prec=PREC, h='', printed=pr, at=utc()))
    for obj in ('zeta', 'q0'):
        for fam in FAMS:
            for w in ((B518_A,) + LADDER if (fam == 'N' and obj == 'q0') else LADDER):
                Wd = W.Window(w, fam)
                for R in R_HEIGHTS:
                    k = ('arch_tail', fam, w, obj, PREC, str(R))
                    if k not in U:
                        t = arch_tail(Wd, obj, R)
                        put_unit(dict(route='arch_tail', fam=fam, a=w, obj=obj, prec=PREC, h=str(R), ball=bs(t)))
                for T0 in T0_HEIGHTS:
                    k = ('zero_tail', fam, w, obj, PREC, T0)
                    if k not in U:
                        t, sm, rem = zero_tail(Wd, obj, T0)
                        put_unit(dict(route='zero_tail', fam=fam, a=w, obj=obj, prec=PREC, h=T0, ball=bs(t), summed=bs(sm), rest=bs(rem)))
                U = units()
                at = [bl(U[('arch_tail', fam, w, obj, PREC, str(R))]['ball']) for R in R_HEIGHTS]
                zt = [bl(U[('zero_tail', fam, w, obj, PREC, T0)]['ball']) for T0 in T0_HEIGHTS]
                print('  %-4s %s a %-9s (a) R 4000 %s ; 8000 %s ; ratio %.5e | (b) T0 151.59 %s ; 303.18 %s ; ratio %.5e' % (
                    obj, fam, w, fmt(at[0], 6), fmt(at[1], 6), float((at[1] / at[0]).mid()), fmt(zt[0], 6), fmt(zt[1], 6),
                    float((zt[1] / zt[0]).mid())), flush=True)
    print('### THE TAIL BALLS BANKED: %d units' % len([1 for k in units() if k[0] in ('arch_tail', 'zero_tail')]))


# ================================================================================ (p2), (p3): THE TERMS
def _run(route, obj, fam, widths, g0=None):
    U = units()
    for w in widths:
        key = (route, fam, w, obj, PREC, str(R_HEIGHTS[0]))
        if key in U:
            print('  %s %s a %-9s banked: S %s' % (route, fam, w, fmt(bl(U[key]['S']))))
            continue
        if obj == 'q0':
            zc = [x for x in U.values() if x['route'] == 'zeta' and x['prec'] == PREC]
            need = [(f_, w_) for f_ in FAMS for w_ in LADDER]
            done = set((x['fam'], x['a']) for x in zc)
            if any(n not in done for n in need) or any(reading(x['S']) != 'NONNEGATIVE BEYOND ITS BOUND' for x in zc):
                sys.exit('### C1 (ZETA) NOT READ NONNEGATIVE BEYOND ITS BALL RADIUS AT EVERY WIDTH OF BOTH FAMILIES -- NO Q0 TERM COMPUTED (N4)')
        Wd = W.Window(w, fam, g0=g0)
        u = terms(Wd, obj)
        u.update(route=route, fam=fam, a=w, obj=obj, prec=PREC, h=str(R_HEIGHTS[0]), g0=g0)
        put_unit(u)
        print('  %s %s a %-9s P %s | PR %s | A %s (tail ball %s) | S %s | %s | %d s' % (
            route, fam, w, fmt(bl(u['P']), 8), fmt(bl(u['PR']), 10), fmt(bl(u['A']), 10), fmt(bl(u['tail']), 4), fmt(bl(u['S'])), reading(u['S']),
            u['seconds']), flush=True)


def zeta(fam, *a):
    _run('zeta', 'zeta', fam, a or LADDER)


def q0(fam, *a):
    _run('q0', 'q0', fam, a or ((B518_A,) + LADDER if fam == 'N' else LADDER))


def c2(*a):
    _run('c2', 'q0', 'N', (B518_A,), g0=B518_G0)


# ================================================================================ (p4): C3, THE IDENTITY WITH (b)'S BALL
def _zeros(obj):
    if obj == 'q0':
        return W.q0_zeros()
    zs, n = [], 1
    while True:
        z = acb.zeta_zero(n)
        if z.imag > arb(W.ZETA_T):
            break
        zs.append((z.imag, arb(0), 1))
        n += 1
    return zs


def _identity(route, obj, fam, w, src, g0=None, zs=None):
    U = units()
    key = (route, fam, w, obj, PREC, T0_HEIGHTS[0])
    if key in U:
        print('  %s %s %s a %-9s banked: AGREE %s' % (route, obj, fam, w, U[key]['agree']))
        return
    st = U.get((src, fam, w, obj, PREC, str(R_HEIGHTS[0])))
    if not st:
        sys.exit('### THE TERMS AT %s %s %s a %s NOT BANKED -- THE IDENTITY NOT READ' % (src, obj, fam, w))
    zt = U.get(('zero_tail', fam, w, obj, PREC, T0_HEIGHTS[0])) if g0 is None else None
    t0 = time.time()
    Wd = W.Window(w, fam, g0=g0)
    zball = bl(zt['ball']) if zt else zero_tail(Wd, obj, T0_HEIGHTS[0])[0]
    Z = W.zero_side(Wd, zs)
    diff = Z - bl(st['S'])
    agree = (diff + unit_ball(zball)).contains(0)
    u = dict(route=route, fam=fam, a=w, obj=obj, prec=PREC, h=T0_HEIGHTS[0], Z=bs(Z), zero_tail=bs(zball), diff=bs(diff), agree=bool(agree),
             zeros=len(zs), g0=g0, seconds=int(time.time() - t0))
    put_unit(u)
    print('  %s %s %s a %-9s Z %s (%d zeros below %s) | Z - S %s | the zero-tail ball %s | AGREE %s | %d s' % (
        route, obj, fam, w, fmt(Z), len(zs), W.ZETA_T, fmt(diff, 4), fmt(zball, 4), agree, u['seconds']), flush=True)


def identity(obj, fam, *a):
    zs = _zeros(obj)
    for w in (a or ((B518_A,) + LADDER if (fam == 'N' and obj == 'q0') else LADDER)):
        _identity('identity', obj, fam, w, obj, zs=zs)


def identity_c2(*a):
    _identity('identity_c2', 'q0', 'N', B518_A, 'c2', g0=B518_G0, zs=_zeros('q0'))


# ================================================================================ (p5): T1 AT a = 32
def t1(*a):
    """T1 (ii): the integral over [4000, 8000] at a = 32 (N, Q0), read inside (a)'s ball at 4000; S at R = 8000 inside S at 4000. T1 (iii):
    the terms at 256 bits at a = 32 (R = 4000), the midpoints of S at 128 and 256 bits agreeing within the 256-bit ball."""
    global PREC
    U = units()
    lo = U.get(('q0', 'N', '32', 'q0', 128, '4000'))
    if not lo:
        sys.exit('### THE 128-BIT TERMS AT a = 32 NOT BANKED')
    if ('t1_ext', 'N', '32', 'q0', 128, '8000') not in U:
        t0 = time.time()
        Wd = W.Window('32', 'N')
        ext = a_int(Wd, 'q0', 4000, 8000)
        t8 = bl(U[('arch_tail', 'N', '32', 'q0', 128, '8000')]['ball'])
        S8 = bl(lo['P']) - bl(lo['PR']) + bl(lo['Aint']) + ext + unit_ball(t8)
        put_unit(dict(route='t1_ext', fam='N', a='32', obj='q0', prec=128, h='8000', ext=bs(ext), S8=bs(S8), seconds=int(time.time() - t0)))
        print('  T1 (ii) the integral over [4000, 8000] %s ; S at R = 8000 %s ; %d s' % (fmt(ext, 6), fmt(S8, 16), int(time.time() - t0)), flush=True)
    else:
        print('  T1 (ii) banked')
    if ('rung', 'N', '32', 'q0', 256, '4000') not in units():
        PREC = 256
        ctx.prec = 256
        Wd = W.Window('32', 'N')
        u = terms(Wd, 'q0')
        u.update(route='rung', fam='N', a='32', obj='q0', prec=256, h='4000')
        put_unit(u)
        print('  T1 (iii) S at 256 bits %s ; %d s' % (fmt(bl(u['S']), 24), u['seconds']), flush=True)
    else:
        print('  T1 (iii) banked')


# ================================================================================ (p6): THE BANKS
def _put(name, data):
    q = os.path.join(D, name)
    with open(q + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(q + '.tmp', q)


def _b694():
    j = json.loads(gzip.decompress(open(B694_GZ, 'rb').read()).decode('utf-8'))
    return dict(((u['route'], u.get('fam', ''), u.get('a', ''), u.get('obj', ''), u.get('prec', 128)), u) for u in j['units'] if 'route' in u)


def _pred_arch(p, h0, h1, g0):
    """(a)'s factor at leading order between two heights: (theta0/theta1)^12 (h1/h0)^(1-p) times the ratio of its log terms."""
    q = p - 1
    th = lambda h: 1 - g0 / h   # noqa: E731
    return (th(h0) / th(h1)) ** 12 * (h1 / h0) ** (1 - p) * (math.log(h1) / q + 1 / q / q) / (math.log(h0) / q + 1 / q / q)


def _pred_zero(fam, w, obj, g0=None):
    """(b)'s factor as its own majorant predicts it: the closed-form integral from T0 at the two heights (zero_integral from U = T0)."""
    Wd = W.Window(w, fam, g0=g0)
    i0, i1 = (zero_integral(Wd, obj, h, h) for h in T0_HEIGHTS)
    return float((i1 / i0).mid())


def bank(*a):
    U = units()
    ctx.prec = 128
    O = _b694()
    get = lambda r, f, w, o, h='4000', p=128: U.get((r, f, w, o, p, h))   # noqa: E731
    L = ['b696 -- THE WEIL-FACE WITNESS AT Q0 WITH ITS TAIL BOUNDS AS CERTIFIED BALLS, (R306)(3), ON THE AUTHOR`S WORD AT PROMPT 3 (%s)' % utc(), '',
         '### the plan relay data/b696_tails_plan.txt; the tool relay tools/b696_witness_balls.py, b694`s window, prime sum and integral imported',
         '### unedited (tools/b694_witness_terms.py). (a) THE ARCHIMEDEAN TAIL beyond R = 4000 as a ball from DLMF (5.11.2) and its remainder bound',
         '### at n = 1 (data/b696_source_dlmf_5_11.txt :105-:107, :393-:399), |sinc w| <= 1/|w| on the line, in closed form in arb: it enters the',
         '### SUM`S RADIUS. (b) THE ZERO TAIL above T0 = 151.59 as a ball on P3`s count law (data/b685_count.txt :21, :23, a and c as balls; P3',
         '### DERIVED, NOT COMPILED, data/b687_p3_status.txt) -- THE ONE PREMISE IT RESTS ON -- at zeta HSW Cor 1.2 (data/b685_search.txt :65): it',
         '### enters THE IDENTITY`S TOLERANCE, which gates a width`s reading. Terms in balls at 128 bits. Rows are widths: family | a | S | the old',
         '### radius (b694) | the new radius | the archimedean tail ball | the zero tail ball (on P3) | the identity | the reading at b694 -> now.', '']
    rows, found, changed = [], [], []
    for fam in FAMS:
        for w in ((B518_A,) + LADDER if fam == 'N' else LADDER):
            u, idn = get('q0', fam, w, 'q0'), get('identity', fam, w, 'q0', W_T0)
            o = O.get(('q0', fam, w, 'q0', 128))
            oi = O.get(('identity', fam, w, 'q0', 128))
            if not u:
                L.append('  %s %-9s ### NOT COMPUTED' % (fam, w))
                continue
            S = bl(u['S'])
            rd_ = reading(u['S']) if idn and idn['agree'] else 'NO READING (the identity not met)'
            ord_ = (reading(o['S']) if oi and oi['agree'] else 'NO READING') if o else '-'
            if fam == 'N' and rd_ == 'NEGATIVE BEYOND ITS BOUND' and w != B518_A:
                found.append((w, S))
            if ord_ != rd_:
                changed.append((fam, w, ord_, rd_))
            row = dict(fam=fam, a=w, S=u['S'], old_radius=(o['S'][1] if o else None), new_radius=S.rad().str(4, radius=False), arch_tail=u['tail'],
                       zero_tail=idn['zero_tail'] if idn else None, identity=dict(agree=bool(idn and idn['agree']), diff=idn and idn['diff']),
                       reading_b694=ord_, reading=rd_, P=u['P'], PR=u['PR'], A=u['A'])
            rows.append(row)
            L.append('  %s | %-9s | S %s | old radius %s | new radius %s | (a) %s | (b) %s on P3 | identity %s (Z - S %s) | %s -> %s' % (
                fam, w, fmt(S, 14), row['old_radius'], row['new_radius'], fmt(bl(u['tail']), 3), fmt(bl(idn['zero_tail']), 3) if idn else '-',
                'AGREE' if idn and idn['agree'] else '### NOT MET', fmt(bl(idn['diff']), 3) if idn else '-', ord_, rd_))
    b694_found = [w for w in ('32', '48', '64', '96', '128', '192')]
    now_found = [w for w, _S in found]
    lost = [w for w in b694_found if w not in now_found]
    narrow = min(found, key=lambda x: float((-x[1]).mid())) if found else None
    disc = not lost
    verdict = ('FOUND AT WIDTHS %s ; THE NARROWEST MARGIN AT a = %s, %s' % (', '.join(now_found), narrow[0], fmt(-narrow[1], 14))) if found else 'NOT FOUND'
    L += ['', '### THE READING: the notched family`s P - PR + A at Q0 with the archimedean tail as a ball lies wholly below 0 beyond its radius, the',
          '### identity met with the zero tail as a ball on P3, at the widths %s; the widths that changed against b694: %s. A sentence about the' % (
              ', '.join(now_found) or 'none', changed or 'NONE'),
          '### computation: nothing claimed of the kernel either way.',
          '', '### ### **THE WEIL-FACE WITNESS AT Q0 WITH BALL TAILS: %s ; EVERY b694 FOUND WIDTH FOUND %s ; THE ORDER %s.**' % (
              verdict, disc, 'DISCHARGED' if disc else 'CARRIED (THE WIDTHS %s CHANGED)' % lost)]
    _put('b696_witness_balls.txt', (NL.join(L) + NL).encode('utf-8'))
    # ### the controls: C1, C2, C3, the tail balls at two heights (N3), T1 re-worded, T2
    C = ['b696 -- THE WITNESS`S CONTROLS WITH THE BALL TAILS, (R306)(3)(d)-(e) AND THE PLAN`S (5)-(6) (%s)' % utc(), '',
         '### rows are controls: C1 zeta at matched widths with (a)`s ball, before any Q0 term; C2 b518`s family re-read; C3 the identity with (b)`s',
         '### ball; THE TAIL BALLS at two heights with the factor each bound predicts (N3); T1 re-worded; T2. Each value a ball.', '']
    c1 = []
    for fam in FAMS:
        for w in LADDER:
            z, idn = get('zeta', fam, w, 'zeta'), get('identity', fam, w, 'zeta', W_T0)
            oz = O.get(('zeta', fam, w, 'zeta', 128))
            r_ = reading(z['S'])
            c1.append(r_ == 'NONNEGATIVE BEYOND ITS BOUND')
            C.append('  C1 | %s | %-4s | S_zeta %s | old radius %s | new radius %s | %s | identity %s (Z - S %s ; the zero-tail ball %s, HSW)' % (
                fam, w, fmt(bl(z['S']), 14), oz['S'][1] if oz else '-', bl(z['S']).rad().str(3, radius=False), r_,
                'AGREE' if idn and idn['agree'] else '### NOT MET', fmt(bl(idn['diff']), 3) if idn else '-', fmt(bl(idn['zero_tail']), 3) if idn else '-'))
    c2u, ic2 = get('c2', 'N', B518_A, 'q0'), get('identity_c2', 'N', B518_A, 'q0', W_T0)
    C += ['', '  C2 | b518`s family at its own gamma_0 %s, a %s: S %s, wholly above 0 %s ; the identity on this window: Z - S %s (the zero-tail ball %s) '
          'AGREE %s' % (B518_G0, B518_A, fmt(bl(c2u['S']), 14), bl(c2u['S']) > 0, fmt(bl(ic2['diff']), 3), fmt(bl(ic2['zero_tail']), 3), ic2['agree'])]
    c3 = [x['agree'] for x in U.values() if x['route'] in ('identity', 'identity_c2')]
    C += ['', '  C3 | the identity at every cell with (b)`s ball: %d of %d AGREE (Q0 and zeta, both families, and C2`s window)' % (sum(c3), len(c3))]
    C += ['', '### THE TAIL BALLS AT TWO HEIGHTS (N3): rows are cells: object | family | a | (a) at R 4000 | at 8000 | ratio | predicted | (b) at T0 151.59 |',
          '### at 303.18 | ratio | predicted. (a)`s prediction is its leading term, (theta0/theta1)^12 (h1/h0)^(1-p) (ln h1/(p-1) + 1/(p-1)^2)/(ln h0/(p-1) +',
          '### 1/(p-1)^2), p = 8 (N) or 12 (C), theta = 1 - g0/h, read within 5%; (b)`s is its own majorant`s closed-form integral from T0 at each height',
          '### (the sum over unit intervals against the integral it is bounded by), read within 10%.']
    n3 = []
    for obj in ('zeta', 'q0'):
        for fam in FAMS:
            for w in ((B518_A,) + LADDER if (fam == 'N' and obj == 'q0') else LADDER):
                at = [bl(U[('arch_tail', fam, w, obj, 128, str(R))]['ball']) for R in R_HEIGHTS]
                zt = [bl(U[('zero_tail', fam, w, obj, 128, h)]['ball']) for h in T0_HEIGHTS]
                p = 8 if fam == 'N' else 12
                ra, rz = float((at[1] / at[0]).mid()), float((zt[1] / zt[0]).mid())
                pa, pz = _pred_arch(p, 4000.0, 8000.0, float(W.Window(w, fam).g0.mid())), _pred_zero(fam, w, obj)
                ok = at[1] < at[0] and zt[1] < zt[0] and abs(ra / pa - 1) < 0.05 and abs(rz / pz - 1) < 0.10
                n3.append(ok)
                C.append('  %-4s | %s | %-9s | (a) %s | %s | %.4e | %.4e | (b) %s | %s | %.4e | %.4e | %s' % (
                    obj, fam, w, fmt(at[0], 4), fmt(at[1], 4), ra, pa, fmt(zt[0], 4), fmt(zt[1], 4), rz, pz, 'SHRINKS AS PREDICTED' if ok else '### NOT AS PREDICTED'))
    lo, hi, ex = get('q0', 'N', '32', 'q0'), get('rung', 'N', '32', 'q0', '4000', 256), get('t1_ext', 'N', '32', 'q0', '8000')
    s1, s2, s8 = bl(lo['S']), bl(hi['S']), bl(ex['S8'])
    t4 = bl(lo['tail'])
    ext_in = unit_ball(t4).contains(bl(ex['ext']))
    ctx.prec = 256
    dmid = s2.mid() - s1.mid()
    within = abs(dmid) <= s2.rad()
    ctx.prec = 128
    C += ['', '  T1 | (i) every tail ball shrinks with its height by the factor its bound predicts: %d of %d cells (the rows above)' % (sum(n3), len(n3)),
          '     | (ii) at a = 32: the integral over [4000, 8000] %s lies inside (a)`s ball at 4000 %s: %s ; S at R = 8000 %s inside S at 4000 %s: %s' % (
              fmt(bl(ex['ext']), 4), fmt(t4, 4), ext_in, fmt(s8, 16), fmt(s1, 16), s1.contains(s8)),
          '     | (iii) at a = 32: S at 256 bits %s ; at 128 bits %s ; the midpoints differ by %s, within the 256-bit ball`s radius %s: %s ; 256 inside 128 %s' % (
              fmt(s2, 22), fmt(s1, 22), dmid.str(4, radius=False), s2.rad().str(4, radius=False), within, s1.contains(s2))]
    rad = s1.rad()
    p_hi = arb(3 * rad, rad)
    p_lo = arb(s1.mid() + rad / 3, rad)
    t2 = reading(p_hi) != reading(s1) and reading(p_lo) == reading(s1)
    C += ['', '  T2 | the planted shifts at a = 32, the new radius %s: S moved to 3 radii above 0 reads %s (the decision moved: %s) ; moved by a third of a '
          'radius reads %s (the decision unmoved: %s)' % (rad.str(4, radius=False), reading(p_hi), reading(p_hi) != reading(s1), reading(p_lo),
                                                          reading(p_lo) == reading(s1))]
    t1ok = all(n3) and ext_in and s1.contains(s8) and within
    C += ['', '### ### **C1 %d OF %d NONNEGATIVE BEYOND THE BALL RADIUS ; C2 POSITIVE %s ; C3 %d OF %d AGREE ; THE TAIL BALLS SHRINK AS PREDICTED %d OF %d ; '
          'T1 AS RE-WORDED %s ; T2 AS WANTED %s.**' % (sum(c1), len(c1), bl(c2u['S']) > 0, sum(c3), len(c3), sum(n3), len(n3), t1ok, t2)]
    _put('b696_witness_balls_controls.txt', (NL.join(C) + NL).encode('utf-8'))
    js = (json.dumps(dict(at=utc(), rows=rows, units=list(U.values()), verdict=verdict, discharged=disc, lost=lost, changed=changed), indent=1,
                     ensure_ascii=False) + NL).encode('utf-8')
    buf = io.BytesIO()
    with gzip.GzipFile(filename='', mode='wb', fileobj=buf, mtime=0) as gz:
        gz.write(js)
    gzb = buf.getvalue()
    _put('b696_witness_balls.json.gz', gzb)
    H = ['b696 -- THE WITNESS BALLS` BINARY BANK`S HASHES (rows are files; data/b680_rules.txt row (1)) (%s)' % utc(),
         'data/b696_witness_balls.json (inside the .gz) sha256 %s bytes %d' % (hashlib.sha256(js).hexdigest(), len(js)),
         'data/b696_witness_balls.json.gz sha256 %s bytes %d ; CR LF pairs in the .gz %d' % (hashlib.sha256(gzb).hexdigest(), len(gzb), gzb.count(b'\r\n')),
         'the units read: data/b696_witness_balls_units.jsonl (untracked) sha256 %s, %d units' % (hashlib.sha256(open(UNITS, 'rb').read()).hexdigest(), len(U))]
    _put('b696_witness_balls_hashes.txt', (NL.join(H) + NL).encode('utf-8'))
    print(L[-1])
    print(C[-1])


W_T0 = T0_HEIGHTS[0]
ROUTES = dict(tails=tails, zeta=zeta, q0=q0, c2=c2, identity=identity, identity_c2=identity_c2, t1=t1, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b696_witness_balls.py %s' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
