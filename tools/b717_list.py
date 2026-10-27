# -*- coding: utf-8 -*-
"""b717_list.py -- THE CERTIFIED ZERO LIST OF Q1 = x^2 + xy + 10y^2 (DISCRIMINANT -39), (R327)(4)(i): "the certified zero list of the principal
form's Epstein zeta, base and tiers [0, 100] and [100, 200], band by band in the foreground in b709's form, each band closed by its count, its
controls printed before its figures; the counts certified and the off-line points located, said so wherever the list is named"; the stop rule
(4)(v) "where the act's budget calls for it, the list stops at the end of tier [0, 100]". Priced at b716 (data/b716_price.txt :7-:61).

### UNTRACKED WRITE: data/b717_list_units* -- data/b717_list_units_band_<lo>_<hi>.jsonl, one file per band (b709's SEG form), and
### data/b717_list_units_control_<lo>_<hi>.jsonl and data/b717_list_units_base.jsonl, appended as each unit lands, resumable; declared by
### prefix for the root route's exclusion list.

### CARRIED FROM tools/b713_list.py (the -15 form, read through the Read tool :1-:200, :200-:399, :399-:457) by the Write tool, the form a
### parameter: C_FORM 4 -> 10, DQ 15 -> 39, the act's names b713 -> b717. THE ROUTE UNCHANGED: tools/b709_pairs.py IMPORTED UNEDITED -- its band
### route (the on-line scan, the count by b667's half path in twelve pieces per edge in the foreground, the on-line zeros by the certified sign
### of Lambda_Q halved to 1e-8, the off-line zeros by its Newton candidates, each band COMPLETE where N = on + 2 off) and its chain; b667's
### engine carried to sqrt(DQ) by b713's substitution at import (M_of, t4_bound, zq, tail_sum, logg_q, b671's _bessel); b709's right edge
### carried to Re s = SIGMA_R = 2 as b713 carried it (at Q1 of -39 the tail Z_Q1(2) - 2 is printed by the controls). At Q1 the expansion's
### lead is b667's: Q1(+-1, 0) = 1 its two least values, the cross term b = 1.
### THE CONTROLS BEFORE ANY -39 BAND (`controls`), changed from b713's where -39 asks it: (C-a) the carried engine at DQ = 23 equal to b667's,
### ball for ball, at three points (b713's (C-a)); (C-b) at DQ = 15, Z_Q1 of -15 against b713's genus identity zeta L(chi_-15) + L(chi_-3)
### L(chi_5) at three points, the balls overlapping (b713's (C-b), the substitution shown at a second discriminant); (C-e) at DQ = 39, Z_Q1
### against its own Dirichlet series SUM r_Q1(n) n^(-s) over n <= X = 100000 by direct enumeration, at three points with Re s = 2.4 (b667's
### t4_bound refuses |sigma - 1/2| > 2, so b713's Re s = 3 moved inside it), the
### series' ball widened by the explicit tail bound sigma [2 X^(1-sigma)/(sigma-1) + 10 X^(1/2-sigma)/(sigma-1/2) + X^(-sigma)/sigma] from
### #{Q1 <= t} <= 2t + 10 sqrt(t) + 1 (the count itself printed at X against that bound) -- -39's identity of registration (i) carries the
### quartic pair's Hecke L-function L_K(s, psi), which flint's Dirichlet L does not reach, so b713's (C-b) cannot be read at -39 and the
### series stands in its place in the half-plane where it converges; (C-f) at DQ = 39 the functional equation Lambda(s) = Lambda(1 - s),
### Lambda(s) = (sqrt(39)/(2 pi))^s Gamma(s) Z_Q1(s), at three points inside the strip, the balls overlapping; NEG, wanted to FAIL: Z_Q1 of -39
### against the series of Q0 = (1, 1, 6) widened alike, and against Z_Q1 of -15. Then (C-c), `control15`: -15's band [15.0, 30.0] counted
### fresh at DQ = 15 into this act's control file and read against b713's N 14 (data/b713_list.txt :19) -- the price's "-15's band counts".
### Routes: `carried` ; `controls [dry]` ; `control15` ; `base` ; `next [tier2]` ; `band <lo> <hi>` ; `status` ; `bank [dry]` ->
### data/b717_list.txt, data/b717_list.json, data/b717_list_hashes.txt. Free memory read before every band call and the call refused beneath
### the 2560 MB hold. Nothing here proves RH or GRH; the list certifies the count of zeros of Z_Q1 in each band it closes, locates the on-line
### zeros by certified sign changes and the off-line points by Newton (point values, the band's count certified), and states nothing beyond.
"""
import hashlib
import inspect
import io
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b709_pairs as P9            # noqa: E402  ### b709's band route and chain, imported unedited (it imports b667 as CERT, b671 as N)
from flint import acb, arb, ctx, dirichlet_char   # noqa: E402

CERT, N = P9.CERT, P9.N
ACT = 'b717'
C_FORM = 10                         # ### Q1 = (1, 1, 10)
DQ = 4 * C_FORM - 1                 # ### 39
PFX = '%s_list_units_band_' % ACT
PFX_CTL = '%s_list_units_control_' % ACT
BASE_FILE = '%s_list_units_base.jsonl' % ACT
T0 = '0.5'                          # ### the base rectangle [-1, 2] x [-T0, T0] (the pole at s = 1 inside), the chain's base. b713's T0 = 1.0
#   ### read N 2 at -39 (the half path 0 + the two poles, 14:55Z, its unit kept in the base file under key '1.0'): the first zero of Lambda_Q1
#   ### stands ON the line at t ~ 0.896 (Lambda real on the line, -0.0627 at t = 0.85, +0.0051 at t = 0.90; the scratch probe beside the act),
#   ### so the base moves to T0 = 0.5, where the chain's N = 0 holds, and tier one starts there; the band [0.5, 15] carries the zero at 0.896.
TIER1 = ['0.5', '15', '30', '45', '60', '75', '90', '100']
TIER2 = ['115', '130', '145', '160', '175', '190', '200']
COUNT_BUDGET = 300
MODE = ['q1']                       # ### 'q1' or 'control': which units the route reads and writes

CARRY = (('CERT', 'M_of'), ('CERT', 't4_bound'), ('CERT', 'zq'), ('CERT', 'tail_sum'), ('CERT', 'logg_q'), ('N', '_bessel'))
SUBS = (('math.sqrt(23)', 'math.sqrt(DQ)'), ('arb(23).sqrt()', 'arb(DQ).sqrt()'))
ORIG = {}
CARRIED = []


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def carry_engine(dq):
    """the six functions compiled from their own source with sqrt(23) -> sqrt(DQ), DQ = dq set in both modules; returns the rows printed."""
    mods = dict(CERT=CERT, N=N)
    rows = []
    for mn, fn in CARRY:
        m = mods[mn]
        f = ORIG.setdefault((mn, fn), getattr(m, fn))
        src = inspect.getsource(f)
        new, k = src, 0
        for a, b in SUBS:
            k += new.count(a)
            new = new.replace(a, b)
        code = [l for l in new.split(NL) if '23' in l and not l.strip().startswith(('"""', '#')) and 'K_ν(π√23' not in l and '√23' not in l]
        m.DQ = dq
        exec(compile(new, '<b717 carried %s.%s>' % (mn, fn), 'exec'), m.__dict__)
        rows.append((mn, fn, k, code))
    CERT._bessel = N._bessel           # ### b671's carried factor, as b671 sets it (b671 :145), now the substituted one
    CARRIED[:] = rows
    return rows


def restore_engine():
    for (mn, fn), f in ORIG.items():
        setattr(dict(CERT=CERT, N=N)[mn], fn, f)
    CERT._bessel = ORIG[('N', '_bessel')]


carry_engine(DQ)


def _membrane(p):
    import act_membrane as MEM
    import b717_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def units():
    """this act's Q1 units only (or the control's, in its mode); no earlier act's units are read; a later unit of a key wins."""
    U = {}
    pf = PFX if MODE[0] == 'q1' else PFX_CTL
    names = sorted(f for f in os.listdir(D) if f.startswith(pf) and f.endswith('.jsonl'))
    if MODE[0] == 'q1' and os.path.exists(os.path.join(D, BASE_FILE)):
        names = [BASE_FILE] + names
    for f in names:
        for l in io.open(os.path.join(D, f), encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['key'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    pf = PFX if MODE[0] == 'q1' else PFX_CTL
    path = os.path.join(D, '%s%s.jsonl' % (pf, P9.SEG or 'misc'))
    _membrane(path)
    with open(path, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


P9.units, P9.put_unit = units, put_unit
P9.T_BASE = T0

# ### THE RIGHT EDGE A PARAMETER, as b713 carried it: b709's _hp_task, half_path_pieces and _w_tail compiled from their own source with
# ### arb('1.5') -> arb(SIGMA_R), set by name in b709's module; each count reads [-1, 2] x [t_lo, t_hi]. b713's (C-d) read b709's band
# ### [150, 160] at this edge EQUAL (data/b713_list.txt :12).
SIGMA_R = '2.0'
EDGE = (('P9', '_hp_task'), ('P9', 'half_path_pieces'), ('P9', '_w_tail'))
ORIG_EDGE = {}


def carry_edge(sig):
    rows = []
    for mn, fn in EDGE:
        f = ORIG_EDGE.setdefault(fn, getattr(P9, fn))
        src = inspect.getsource(f)
        k = src.count("arb('1.5')")
        P9.SIGMA_R = sig
        exec(compile(src.replace("arb('1.5')", 'arb(SIGMA_R)'), '<b717 carried %s.%s>' % (mn, fn), 'exec'), P9.__dict__)
        rows.append((mn, fn, k))
    return rows


EDGE_ROWS = carry_edge(SIGMA_R)
_P9_PIECES = P9.half_path_pieces


def half_path_pieces(U, key, t_lo, t_hi, parts=12, budget=COUNT_BUDGET):
    # ### the pieces keyed by the right edge too ('<key>@<SIGMA_R>'), so no piece banked for another edge is read
    return _P9_PIECES(U, '%s@%s' % (key, P9.SIGMA_R), t_lo, t_hi, parts, budget)


P9.half_path_pieces = half_path_pieces


def _free(what):
    f = CERT.free_mb()
    ok = f is not None and f >= CERT.HOLD_MB
    print('### FREE MEMORY BEFORE %s: %s MB against the hold %d MB : %s' % (what, f, CERT.HOLD_MB, 'ABOVE' if ok else '### BENEATH OR UNREAD -- NOTHING RUN'), flush=True)
    if not ok:
        sys.exit(6)
    return f


# ================================================================================ THE CARRIED ENGINE AND ITS CONTROLS
def carried(*a):
    for mn, fn, k, code in CARRIED:
        print('  %s.%s : substitutions %d ; code lines still naming 23: %s' % (mn, fn, k, code or 'NONE'))
    for mn, fn, k in EDGE_ROWS:
        print('  %s.%s : the right edge arb(\'1.5\') -> arb(SIGMA_R) substitutions %d' % (mn, fn, k))
    print('### DQ %d ; THE FORM (1, 1, %d) ; THE RIGHT EDGE Re s = %s' % (DQ, C_FORM, SIGMA_R))


def genus15(s, prec):
    """b713's registration (i) at -15: Z_Q1(s) = zeta(s) L(s, chi_-15) + L(s, chi_-3) L(s, chi_5) (data/b712_registrations.txt :21)."""
    ctx.prec = prec
    return s.zeta() * s.dirichlet_l(dirichlet_char(15, 14)) + s.dirichlet_l(dirichlet_char(3, 2)) * s.dirichlet_l(dirichlet_char(5, 4))


def r_counts(c, X):
    """r_Q(n) for n <= X, Q = x^2 + xy + c y^2, by direct enumeration (y from 0 with its sign counted, x over all integers)."""
    r = [0] * (X + 1)
    ymax = int(math.isqrt(4 * X // (4 * c - 1))) + 2
    for y in range(-ymax, ymax + 1):
        # ### Q = (x + y/2)^2 + (4c - 1) y^2 / 4 <= X
        rest = X - (4 * c - 1) * y * y / 4.0
        if rest < 0:
            continue
        w = math.isqrt(int(rest)) + 2
        for x in range(-w - abs(y), w + abs(y) + 1):
            q = x * x + x * y + c * y * y
            if 0 < q <= X:
                r[q] += 1
    return r


def series(r, s, sigma, X, prec):
    """SUM_{n <= X} r(n) n^(-s) as a ball, widened by the explicit tail bound of the docstring."""
    ctx.prec = prec
    tot = acb(0)
    for n in range(1, X + 1):
        if r[n]:
            tot += r[n] * acb(n) ** (-s)
    tail = sigma * (2.0 * X ** (1 - sigma) / (sigma - 1) + 10.0 * X ** (0.5 - sigma) / (sigma - 0.5) + X ** (-sigma) / sigma)
    tb = arb(0, 2 * tail)
    return tot + acb(tb, tb), tail


PTS = (('2.0', '0.0'), ('0.5', '12.0'), ('0.8', '40.0'))
PTS_E = (('2.4', '0.0'), ('2.4', '10.0'), ('2.4', '40.0'))   # ### Re s = 2.4: b667's T4 bound holds for |sigma - 1/2| <= 2 (its own refusal at 3)
PTS_F = (('0.3', '12.0'), ('0.8', '40.0'), ('0.65', '95.0'))
X_SERIES = 100000


def _lam(s, prec):
    ctx.prec = prec
    return (arb(DQ).sqrt() / (2 * arb.pi())) ** s * s.gamma() * CERT.zq(s, prec)


def controls(*a):
    out = []
    t0 = time.time()
    # ### (C-a) DQ = 23: the carried engine against the original, ball for ball
    carry_engine(23)
    ca = []
    for re_, im_ in PTS:
        s = acb(arb(re_), arb(im_))
        v1 = CERT.zq(s, CERT.PREC).str(30, radius=True)
        restore_engine()
        v0 = CERT.zq(s, CERT.PREC).str(30, radius=True)
        carry_engine(23)
        ca.append((re_, im_, v0 == v1, v1))
    out += ['  (C-a) DQ = 23, s = %s + %si: the carried Z_Q0 equal to b667`s, ball for ball: %s (%s)' % (r, i, e, v[:60]) for r, i, e, v in ca]
    # ### (C-b) DQ = 15: Z_Q1 of -15 against b713's genus identity
    carry_engine(15)
    cb, z15 = [], {}
    for re_, im_ in PTS:
        s = acb(arb(re_), arb(im_))
        z = CERT.zq(s, CERT.PREC)
        z15[(re_, im_)] = z
        g = genus15(s, CERT.PREC)
        ctx.prec = CERT.PREC
        cb.append((re_, im_, bool(z.overlaps(g)), z.str(20, radius=True), g.str(20, radius=True)))
    out += ['  (C-b) DQ = 15, s = %s + %si: Z_Q1 of -15 %s ; b713`s identity %s ; OVERLAP %s' % (r, i, z, g, o) for r, i, o, z, g in cb]
    carry_engine(DQ)
    # ### (C-e) DQ = 39: Z_Q1 against its Dirichlet series, Re s = 3
    r39 = r_counts(C_FORM, X_SERIES)
    r0 = r_counts(6, X_SERIES)
    cnt = sum(r39)
    bound = 2 * X_SERIES + 10 * math.sqrt(X_SERIES) + 1
    out.append('  (C-e) the count #{0 < Q1 <= %d} = %d against the bound 2t + 10 sqrt(t) + 1 = %.1f : %s ; the main term 2 pi t / sqrt(39) = %.1f' % (
        X_SERIES, cnt, bound, 'WITHIN' if cnt + 1 <= bound else '### OVER', 2 * math.pi * X_SERIES / math.sqrt(DQ)))
    ce, neg = [], []
    for re_, im_ in PTS_E:
        s = acb(arb(re_), arb(im_))
        z = CERT.zq(s, CERT.PREC)
        ser, tail = series(r39, s, float(re_), X_SERIES, CERT.PREC)
        ser0, _ = series(r0, s, float(re_), X_SERIES, CERT.PREC)
        ctx.prec = CERT.PREC
        ce.append((re_, im_, bool(z.overlaps(ser)), z.str(20, radius=True), ser.str(20, radius=True), '%.2e' % tail))
        neg.append((re_, im_, 'Q0`s series', bool(z.overlaps(ser0))))
    out += ['  (C-e) DQ = 39, s = %s + %si: Z_Q1 %s ; the series to X with its tail %s ; tail bound %s ; OVERLAP %s' % (r, i, z, sr, t, o) for r, i, o, z, sr, t in ce]
    # ### (C-f) DQ = 39: the functional equation inside the strip
    cf = []
    for re_, im_ in PTS_F:
        s = acb(arb(re_), arb(im_))
        l1, l2 = _lam(s, CERT.PREC), _lam(1 - s, CERT.PREC)
        ctx.prec = CERT.PREC
        cf.append((re_, im_, bool(l1.overlaps(l2)), l1.str(15, radius=True), l2.str(15, radius=True)))
    out += ['  (C-f) DQ = 39, s = %s + %si: Lambda(s) %s ; Lambda(1 - s) %s ; OVERLAP %s' % (r, i, l1, l2, o) for r, i, o, l1, l2 in cf]
    # ### NEG: Z_Q1 of -39 against -15's Z_Q1 at the same points
    for re_, im_ in PTS:
        s = acb(arb(re_), arb(im_))
        z = CERT.zq(s, CERT.PREC)
        ctx.prec = CERT.PREC
        neg.append((re_, im_, 'Z_Q1 of -15', bool(z.overlaps(z15[(re_, im_)]))))
    out += ['  (NEG) DQ = 39, s = %s + %si: Z_Q1 overlapping %s : %s (wanted False)' % x for x in neg]
    tail2 = CERT.zq(acb(arb(SIGMA_R)), CERT.PREC).real - 2
    out.append('  THE RIGHT EDGE: Z_Q1(%s) - 2 = %s (b709`s half path closes on the edge where it is below 2)' % (SIGMA_R, tail2.str(10, radius=True)))
    ok = (all(x[2] for x in ca) and all(x[2] for x in cb) and all(x[2] for x in ce) and all(x[2] for x in cf) and not any(x[3] for x in neg)
          and cnt + 1 <= bound and tail2 < 2)
    L = ['%s -- THE LIST`S CONTROLS (C-a), (C-b), (C-e), (C-f) AND NEG, BEFORE ANY -39 BAND (%s ; %d s)' % (ACT, utc(), int(time.time() - t0)), ''] + [
        '  carried %s.%s : substitutions %d ; code lines naming 23: %s' % (mn, fn, k, code or 'NONE') for mn, fn, k, code in CARRIED] + [''] + out + [
        '', '### ### **(C-a) %d OF %d EQUAL ; (C-b) %d OF %d OVERLAPPING ; (C-e) %d OF %d OVERLAPPING ; (C-f) %d OF %d OVERLAPPING ; NEG %d OF %d FAILING AS WANTED ; %s.**' % (
            sum(1 for x in ca if x[2]), len(ca), sum(1 for x in cb if x[2]), len(cb), sum(1 for x in ce if x[2]), len(ce),
            sum(1 for x in cf if x[2]), len(cf), sum(1 for x in neg if not x[3]), len(neg), 'AS WANTED' if ok else '### NOT AS WANTED')]
    print(NL.join(L))
    if 'dry' not in a:
        _put('%s_list_controls.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
        _put('%s_list_controls.json' % ACT, (json.dumps(dict(at=utc(), ca=ca, cb=cb, ce=ce, cf=cf, neg=neg, count=cnt, ok=ok), indent=1) + NL).encode('utf-8'))


def control15(*a):
    """(C-c): -15's band [15.0, 30.0] counted fresh at DQ = 15 (the right edge SIGMA_R, b713's) into this act's control file, read against
    b713's N 14 (data/b713_list.txt :19); one foreground call per budget, call again until it prints the reading."""
    _free('THE CONTROL BAND')
    MODE[0] = 'control'
    carry_engine(15)
    lo, hi = '15.0', '30.0'
    P9.SEG = '%s_%s' % (lo, hi)
    P9.count(lo, hi)
    u = units().get(('count', '%s_%s' % (lo, hi)))
    if u and u.get('count') is not None:
        print('### ### **(C-c) -15`s band [%s, %s]: b713`s N 14 ; the carried engine at DQ = 15, the right edge Re s = %s, reads N %s ; %s.**' % (
            lo, hi, P9.SIGMA_R, u['count'], 'EQUAL' if u['count'] == 14 else '### UNEQUAL'))
    carry_engine(DQ)
    MODE[0] = 'q1'


# ================================================================================ THE BASE: [-1, 2] x [-T0, T0]
def base(*a):
    """N of the rectangle [-1, 2] x [-T0, T0] by b709's `count` route at [-T0, T0] (Lambda's symmetry; its half path in pieces, foreground,
    resumable); Lambda's poles inside are s = 0 (Gamma's) and s = 1 (Z's), so N = count + 2. The sign of Z_Q1 on [1/2, 3/2] at step 0.01
    (the real zeros). The chain starts at T0 where N = 0 (b713's base, its form unchanged)."""
    _free('THE BASE')
    MODE[0] = 'q1'
    P9.SEG = 'base'
    U = units()
    if ('base', T0) in U:
        u = U[('base', T0)]
        print('  the base [-1, %s] x [-%s, %s]: N %s (banked) ; real sign changes %s' % (SIGMA_R, T0, T0, u['N'], u['real_changes']))
        return u
    t0 = time.time()
    lo = '-' + T0
    P9.count(lo, T0)
    U = units()
    c = U.get(('count', '%s_%s' % (lo, T0)))
    if not c or c.get('count') is None:
        print('  the base: the half path at [%s, %s] not yet assembled -- call again' % (lo, T0))
        return None
    n = c['count'] + 2
    st = dict(segments=c['segments'], max_depth=c['max_depth'])
    nb = arb(n)
    sg, ch = [], []
    x = 0.5
    while x <= 1.5 + 1e-9:
        if abs(x - 1.0) > 0.005:
            v = CERT.zq(acb(arb(repr(round(x, 4)))), CERT.PREC).real
            s_ = 1 if v > 0 else (-1 if v < 0 else 0)
            if sg and s_ and sg[-1][1] and s_ != sg[-1][1] and not (sg[-1][0] < 1.0 < x):
                ch.append([sg[-1][0], round(x, 4)])
            sg.append((round(x, 4), s_))
        x += 0.01
    u = dict(route='base', key=T0, N=n, half_path=c['count'], half_ball=c['ball'], ball=nb.str(12, radius=True), real_changes=ch, unread=[p for p, s_ in sg if s_ == 0],
             segments=st['segments'], max_depth=st['max_depth'], seconds=int(time.time() - t0))
    put_unit(u)
    print('  the base [-1, %s] x [-%s, %s]: the half path %s (ball %s) + Lambda`s 2 poles = N %s ; real sign changes on [1/2, 3/2] %s ; signs unread %s ; %d s' % (
        SIGMA_R, T0, T0, c['count'], c['ball'], n, ch or 'NONE', u['unread'] or 'NONE', u['seconds']))
    return u


# ================================================================================ THE BANDS
def top():
    U = units()
    b = U.get(('base', T0))
    if not b or b.get('N') != 0:
        return None
    return P9._complete_to(P9._bands(U), U)


def nxt(*a):
    MODE[0] = 'q1'
    t = top()
    if t is None:
        print('### THE BASE IS NOT BANKED AT N = 0 -- run `base` first')
        return
    grid = [float(g) for g in TIER1 + (TIER2 if 'tier2' in a else [])]
    above = [g for g in grid if g > t + 1.0]
    if not above:
        print('  the list is complete to %s, the tier`s top: no band to run' % t)
        return
    _free('THE BAND [%s, %s]' % (t, above[0]))
    print('  the chain`s top %s ; the band [%s, %s]' % (t, t, above[0]), flush=True)
    P9.band(str(t), str(above[0]) if above[0] != int(above[0]) else str(int(above[0])))


def band(lo, hi, *a):
    MODE[0] = 'q1'
    _free('THE BAND [%s, %s]' % (lo, hi))
    P9.band(lo, hi)


def _rows():
    U = units()
    bands = P9._bands(U)
    t = top()
    chain, _t = P9._chain(U) if t is not None else ([], None)
    on_z, off_z = [], []
    for b, t_from in chain:
        on = U[('online', b['key'])]
        on_z += [z for z in on['zeros'] if float(z['t']) > t_from + 1e-9]
        off = U.get(('offline', b['key']))
        off_z += [z for z in (off['zeros'] if off else []) if float(z['im']) > t_from + 1e-9]
    return U, bands, t, chain, on_z, off_z


def status(*a):
    U, bands, t, chain, on_z, off_z = _rows()
    for b in bands:
        print('  band [%s, %s]: N %s ; on-line %s ; off-line %s ; %s' % (b['t_lo'], b['t_hi'], b['N'], b['on'], b['off'], 'COMPLETE' if b['complete'] else 'INCOMPLETE'))
    print('### THE LIST COMPLETE TO %s ; on-line zeros %d ; off-line pairs %d %s' % (t, len(on_z), len(off_z), [(z['re'][:10], z['im'][:12]) for z in off_z]))


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


def bank(*a):
    U, bands, t, chain, on_z, off_z = _rows()
    bands = [b for b in bands if b['t_lo'] >= float(T0) - 1e-9]
    bu = U.get(('base', T0)) or {}
    over1 = [z for z in off_z if float(z['re']) > 1.0]
    MODE[0] = 'control'
    cc = units().get(('count', '15.0_30.0'))
    MODE[0] = 'q1'
    ctl = json.load(io.open(os.path.join(D, '%s_list_controls.json' % ACT), encoding='utf-8')) if os.path.exists(os.path.join(D, '%s_list_controls.json' % ACT)) else {}
    qs = [v.get('seconds', 0) for (r_, k_), v in U.items() if r_ == 'hppiece' and '@' in k_] or [0]
    ctl_lines = ['### THE CONTROLS, PRINTED BEFORE THE FIGURES: data/b717_list_controls.txt ((C-a) the engine carried to sqrt(23) equal to b667`s,',
                 '### (C-b) Z_Q1 of -15 against b713`s genus identity, (C-e) Z_Q1 of -39 against its Dirichlet series at Re s = 2.4 with its tail, (C-f) the',
                 '### functional equation of Lambda_Q1 at -39 inside the strip, NEG failing): %s ;' % ('AS WANTED' if ctl.get('ok') else '### NOT AS WANTED OR NOT RUN'),
                 '### (C-c) -15`s band [15.0, 30.0] counted at DQ = 15, the right edge %s: N %s, b713`s 14 (data/b713_list.txt :19), %s.' % (
                     SIGMA_R, (cc or {}).get('count'), 'EQUAL' if (cc or {}).get('count') == 14 else '### NOT EQUAL OR NOT RUN'),
                 '### THE RIGHT EDGE: b709`s three functions carried to Re s = %s by substitution as b713 carried them (`carried`), each count over' % SIGMA_R,
                 '### [-1, %s] x [t_lo, t_hi]; the -39 bands` pieces ran %d to %d s.' % (SIGMA_R, min(qs), max(qs)), '']
    L = ['%s -- COMPONENT 2, (R327)(4)(i): THE CERTIFIED ZERO LIST OF Q1 = x^2 + xy + 10y^2 (DISCRIMINANT -39) IN b709`S FOREGROUND BAND FORM (%s)' % (ACT, utc()), '',
         '### rows are bands, each by tools/b709_pairs.py`s band route imported unedited over b667`s engine carried to sqrt(%d) by substitution' % DQ,
         '### (tools/b717_list.py `carried`): N(band) by the half path, THE COUNT CERTIFIED; the on-line zeros by the certified sign of Lambda_Q1',
         '### halved to %s; THE OFF-LINE POINTS LOCATED by Newton candidates (point values, the band`s count certified, RECT_CERTIFY %s);' % (P9.W_ON, P9.RECT_CERTIFY),
         '### COMPLETE where N = on + 2 off. THE BASE: [-1, %s] x [-%s, %s] by b709`s count at [-%s, %s] (Lambda`s symmetry), the half path %s + Lambda`s' % (
             SIGMA_R, T0, T0, T0, T0, bu.get('half_path')),
         '### two poles (s = 0, s = 1) = N %s ; the sign of Z_Q1 on [1/2, 3/2] changes %s (unread at 1/2, where zeta(2s) and Gamma(s - 1/2) meet).' % (
             bu.get('N'), bu.get('real_changes') or 'nowhere'),
         '### THE MAIN TERM BESIDE IT (not a bound): N(T) ~ (T/pi) log(T sqrt(39)/(2 pi e)) + 1 at T = %s reads %.1f ; the list holds %d.' % (
             t, (t / math.pi) * math.log(t * math.sqrt(DQ) / (2 * math.pi * math.e)) + 1 if t else 0, len(on_z) + 2 * len(off_z)), ''] + ctl_lines
    for b in bands:
        offz = U.get(('offline', b['key']))
        L.append('  band [%s, %s] | N %s | on-line %s | off-line %s %s | %s' % (
            b['t_lo'], b['t_hi'], b['N'], b['on'], b['off'], [(z['re'][:12], z['im'][:12]) for z in (offz['zeros'] if offz else [])] or '',
            'COMPLETE' if b['complete'] else '### INCOMPLETE'))
    L += ['', '### THE OFF-LINE PAIRS (rho and 1 - conj(rho) in the strip; the list`s order by height; each LOCATED by Newton, its band`s count certified):']
    L += ['  pair %d : rho = %s + %s i%s' % (k + 1, z['re'][:20], z['im'][:20], ' ; Re rho > 1' if float(z['re']) > 1.0 else '') for k, z in enumerate(off_z)]
    L += ['', '### THE LEAST HEIGHT OF A ZERO WITH Re rho > 1: %s' % (over1[0]['im'][:16] if over1 else 'none in the list to %s' % t),
          '', '### ### **THE LIST COMPLETE TO %s, THE COUNTS CERTIFIED AND THE OFF-LINE POINTS LOCATED ; BANDS %d (COMPLETE %d) ; ON-LINE ZEROS %d ; OFF-LINE PAIRS %d.**' % (
              t, len(bands), sum(1 for b in bands if b['complete']), len(on_z), len(off_z))]
    j = dict(at=utc(), DQ=DQ, form=[1, 1, C_FORM], base=bu, top=t, bands=bands, chained=[dict(b, t_from=f) for b, f in chain], online=on_z, offline=off_z,
             re_over_1=over1, units=dict(('%s|%s' % k, v) for k, v in U.items() if k[0] in ('count', 'online', 'offline', 'base')))
    print(NL.join(L))
    if 'dry' in a:
        return
    h1 = _put('%s_list.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    h2 = _put('%s_list.json' % ACT, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    H = ['%s -- THE LIST`S BANKS, THEIR sha256 (%s)' % (ACT, utc()), '', '  %s  data/%s_list.txt' % (h1, ACT), '  %s  data/%s_list.json' % (h2, ACT)]
    for f in sorted(f for f in os.listdir(D) if (f.startswith(PFX) or f.startswith(PFX_CTL) or f == BASE_FILE) and f.endswith('.jsonl')):
        H.append('  %s  data/%s (untracked, its units)' % (hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest(), f))
    H += ['', '### ### **BANKS 2 HASHED, THE UNITS FILES BESIDE.**']
    _put('%s_list_hashes.txt' % ACT, (NL.join(H) + NL).encode('utf-8'))
    print(H[-1])


ROUTES = dict(carried=carried, controls=controls, control15=control15, base=base, next=nxt, band=band, status=status, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b717_list.py carried | controls [dry] | control15 | base | next [tier2] | band <lo> <hi> | status | bank [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
