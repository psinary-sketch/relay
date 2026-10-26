# -*- coding: utf-8 -*-
"""b713_list.py -- THE CERTIFIED ZERO LIST OF Q1 = x^2 + xy + 4y^2 (DISCRIMINANT -15), (R323)(5)(i): "the certified zero list of Q1 at tier
two, in b709's band form, in the foreground"; the stop rule "tier one where the budget requires it". Priced at b712 (data/b712_price.txt :7-:39).

### UNTRACKED WRITE: data/b713_list_units* -- data/b713_list_units_band_<lo>_<hi>.jsonl, one file per band (b709's SEG form), and
### data/b713_list_units_control23_<lo>_<hi>.jsonl and data/b713_list_units_base.jsonl, appended as each unit lands, resumable; declared by
### prefix for the root route's exclusion list.

### THE ROUTE: tools/b709_pairs.py IMPORTED UNEDITED -- its band route (the on-line scan to one past the asked top and the top set clear of a zero
### on the line, the count by b667's half path in twelve pieces per edge in the foreground, the on-line zeros by the certified sign of Lambda_Q
### halved to 1e-8, the off-line zeros by its Newton candidates, each band COMPLETE where N = on + 2 off) and its chain (_bands, _chain).
### THE FORM A PARAMETER (data/b712_price.txt :8-:10): the engine's sqrt(23) of the (1,1,6) expansion made sqrt(DQ) for the form (1,1,c),
### DQ = 4c - 1, by SUBSTITUTION AT IMPORT -- the source of b667's M_of, t4_bound, zq, tail_sum, logg_q and b671's carried _bessel read by
### inspect, `math.sqrt(23)` and `arb(23).sqrt()` replaced by `math.sqrt(DQ)` and `arb(DQ).sqrt()`, each function compiled into its own module
### (CERT's, N's) and set by name there (every caller reads them by module attribute at call time); the substitution's count per function and
### every code line left naming 23 printed by `carried`. Nothing else of b667, b671 or b709 is changed. At Q1 the expansion's lead is the
### same: Q1(+-1, 0) = 1 its two least values (b709's `lead = 2`), and the cross term b = 1 gives b667's (-1)^m.
### Rebound here besides: `units` reads THIS ACT'S Q1 files only (b709's Q0 units never read), `put_unit` writes them through the membrane;
### T_BASE the base rectangle's top (`base`); the count's per-call budget 300 s (b711's).
### CONTROLS BEFORE ANY -15 BAND (`controls`): (C-a) the carried engine at DQ = 23 equal, ball for ball, to the original at three points;
### (C-b) at DQ = 15, Z_Q1 against registration (i)'s identity zeta(s)L(s,chi_-15) + L(s,chi_-3)L(s,chi_5) (flint's Dirichlet L) at three
### points, the balls overlapping; (C-c) at DQ = 23 the count of b711's first band reproduced (`control23`, its own units file).
### Routes: `carried` ; `controls` ; `control23` ; `base` ; `next [tier2]` ; `band <lo> <hi>` ; `status` ; `bank [dry]` -> data/b713_list.txt,
### data/b713_list.json, data/b713_list_hashes.txt. Free memory read before every band call and the call refused beneath the 2560 MB hold.
### Written by the Write tool at b713. Nothing here proves RH or GRH; the list certifies zeros of Z_Q1 in the bands it closes and states nothing
### beyond them.
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
ACT = 'b713'
C_FORM = 4                          # ### Q1 = (1, 1, 4)
DQ = 4 * C_FORM - 1                 # ### 15
PFX = '%s_list_units_band_' % ACT
PFX_CTL = '%s_list_units_control23_' % ACT
BASE_FILE = '%s_list_units_base.jsonl' % ACT
T0 = '1.0'                          # ### the base rectangle [-1/2, 3/2] x [-T0, T0] (the pole at s = 1 inside), the chain's base
TIER1 = ['1.0', '15', '30', '45', '60', '75', '90', '100']
TIER2 = ['115', '130', '145', '160', '175', '190', '200']
COUNT_BUDGET = 300
BASE_PARTS = 4                      # ### the base rectangle's pieces per edge
MODE = ['q1']                       # ### 'q1' or 'control23': which units the route reads and writes

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
        exec(compile(new, '<b713 carried %s.%s>' % (mn, fn), 'exec'), m.__dict__)
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
    import b713_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def units():
    """this act's Q1 units only (or the control's, in its mode); b709's and b711's Q0 units are never read; a later unit of a key wins."""
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

# ### THE RIGHT EDGE A PARAMETER: b709's half path closes on Re s = 3/2 by (3c), |Z - 2| <= Z(3/2) - 2 < 2 there; at Q1 the tail reads
# ### Z_Q1(3/2) - 2 = 2.1587 (the base's first count, data/b713_list_units_band_base.jsonl :38, "THE TAIL BOUND ... IS NOT BELOW 2"), so the
# ### edge is moved to Re s = SIGMA_R = 2 (Z_Q1(2) - 2 = 0.6846, data/b713_list_controls.txt (C-b); |sigma - 1/2| = 3/2 inside b667's T4
# ### bound): b709's _hp_task, half_path_pieces and _w_tail compiled from their own source with arb('1.5') -> arb(SIGMA_R), set by name in
# ### b709's module; the count then reads [-1, 2] x [t_lo, t_hi] (a zero with Re above 1.45 is outside the candidates' grid and leaves its
# ### band INCOMPLETE, not counted twice). Its control: (C-d), a Q0 band of b709's counted again at SIGMA_R = 2 (`control23 b709`).
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
        exec(compile(src.replace("arb('1.5')", 'arb(SIGMA_R)'), '<b713 carried %s.%s>' % (mn, fn), 'exec'), P9.__dict__)
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


def genus_rhs(s, prec):
    """registration (i): Z_Q1(s) = zeta(s) L(s, chi_-15) + L(s, chi_-3) L(s, chi_5) (data/b712_registrations.txt :21)."""
    ctx.prec = prec
    return s.zeta() * s.dirichlet_l(dirichlet_char(15, 14)) + s.dirichlet_l(dirichlet_char(3, 2)) * s.dirichlet_l(dirichlet_char(5, 4))


PTS = (('2.0', '0.0'), ('0.5', '12.0'), ('0.8', '40.0'))


def controls(*a):
    out = []
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
    carry_engine(DQ)
    out += ['  (C-a) DQ = 23, s = %s + %si: the carried Z_Q0 equal to b667`s, ball for ball: %s (%s)' % (r, i, e, v[:60]) for r, i, e, v in ca]
    # ### (C-b) DQ = 15: Z_Q1 against the genus identity of registration (i)
    cb = []
    for re_, im_ in PTS:
        s = acb(arb(re_), arb(im_))
        z = CERT.zq(s, CERT.PREC)
        g = genus_rhs(s, CERT.PREC)
        ctx.prec = CERT.PREC
        cb.append((re_, im_, bool(z.overlaps(g)), z.str(20, radius=True), g.str(20, radius=True), (z - g).str(5, radius=True)))
    out += ['  (C-b) DQ = 15, s = %s + %si: Z_Q1 %s ; the identity %s ; difference %s ; OVERLAP %s' % (r, i, z, g, d, o) for r, i, o, z, g, d in cb]
    # ### NEG controls, wanted to FAIL: Z_Q1 against the identity with its genus term's sign reversed; the carried engine at DQ = 15 against
    # ### b667's original (DQ = 23)
    neg = []
    for re_, im_ in PTS:
        s = acb(arb(re_), arb(im_))
        z = CERT.zq(s, CERT.PREC)
        ctx.prec = CERT.PREC
        g2 = s.zeta() * s.dirichlet_l(dirichlet_char(15, 14)) - s.dirichlet_l(dirichlet_char(3, 2)) * s.dirichlet_l(dirichlet_char(5, 4))
        restore_engine()
        z23 = CERT.zq(s, CERT.PREC)
        carry_engine(DQ)
        neg.append((re_, im_, bool(z.overlaps(g2)), bool(z.overlaps(z23))))
    out += ['  (NEG) s = %s + %si: Z_Q1 overlapping the sign-reversed identity %s ; Z_Q1 overlapping b667`s Z_Q0 %s (both wanted False)' % x for x in neg]
    ok = all(x[2] for x in ca) and all(x[2] for x in cb) and not any(x[2] or x[3] for x in neg)
    L = ['%s -- THE LIST`S CONTROLS (C-a) AND (C-b), BEFORE ANY -15 BAND (%s)' % (ACT, utc()), ''] + [
        '  carried %s.%s : substitutions %d ; code lines naming 23: %s' % (mn, fn, k, code or 'NONE') for mn, fn, k, code in CARRIED] + [''] + out + [
        '', '### ### **(C-a) %d OF %d EQUAL ; (C-b) %d OF %d OVERLAPPING ; NEG %d OF %d FAILING AS WANTED ; %s.**' % (
            sum(1 for x in ca if x[2]), len(ca), sum(1 for x in cb if x[2]), len(cb), sum(1 for x in neg if not (x[2] or x[3])), len(neg),
            'AS WANTED' if ok else '### NOT AS WANTED')]
    print(NL.join(L))
    if 'dry' not in a:
        _put('%s_list_controls.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
        _put('%s_list_controls.json' % ACT, (json.dumps(dict(at=utc(), ca=ca, cb=cb, neg=neg, ok=ok), indent=1) + NL).encode('utf-8'))


def _b709_n(key):
    """b709's N for the band, read from its bank (data/b709_pairs.txt :19 for 150_160)."""
    import re
    lo, hi = key.split('_')
    for l in io.open(os.path.join(D, 'b709_pairs.txt'), encoding='utf-8'):
        m = re.match(r'\s*band \[%s, %s\] \| N (\d+) \|' % (re.escape(repr(float(lo))), re.escape(repr(float(hi)))), l)
        if m:
            return int(m.group(1))
    return None


def control23(*a):
    """(C-c): at DQ = 23 the count of b711's first band (data/b711_list.json `bands`[0]) run fresh into this act's control file and read
    against b711's N, the right edge at 3/2 (b709's own); one foreground call per budget, call again until it prints the reading.
    `control23 b709`: (C-d), the right edge at SIGMA_R -- b709's band [150, 160] (data/b709_pairs.json) counted at DQ = 23 with the edge at
    Re s = SIGMA_R, read against b709's N."""
    _free('THE CONTROL BAND')
    MODE[0] = 'control23'
    carry_engine(23)
    if a and a[0] == 'b709':
        b = dict(t_lo=150.0, t_hi=160.0, N=_b709_n('150_160'))
        P9.SIGMA_R = SIGMA_R
    else:
        b = json.load(io.open(os.path.join(D, 'b711_list.json'), encoding='utf-8'))['bands'][0]
        carry_edge('1.5')
    lo, hi = repr(b['t_lo']), repr(b['t_hi'])
    P9.SEG = '%s_%s' % (lo, hi)
    P9.count(lo, hi)
    u = units().get(('count', '%s_%s' % (lo, hi)))
    if u and u.get('count') is not None:
        print('### ### **%s band [%s, %s]: its N %s ; the carried engine at DQ = 23, the right edge Re s = %s, reads N %s ; %s.**' % (
            '(C-d) b709`s' if a and a[0] == 'b709' else '(C-c) b711`s', lo, hi, b['N'], P9.SIGMA_R, u['count'],
            'EQUAL' if u['count'] == b['N'] else '### UNEQUAL'))


# ================================================================================ THE BASE: [-1/2, 3/2] x [-T0, T0]
def base(*a):
    """N of the rectangle [-1/2, 3/2] x [-T0, T0]: Lambda_Q1(s) = Lambda_Q1(1 - s) and Lambda(conj s) = conj Lambda(s), so the argument change
    of Lambda around the rectangle is twice its change along the right half path 1/2 - iT0 -> 3/2 - iT0 -> 3/2 + iT0 -> 1/2 + iT0, and
    (zeros - poles) inside = (1/pi) times that change -- b709's `count` route itself, taken at [-T0, T0] (its half path in pieces, foreground,
    resumable); Lambda's poles inside are s = 0 (Gamma's) and s = 1 (Z's), so N = count + 2. The sign of Z_Q1 on [1/2, 3/2] at step 0.01
    (the real zeros; those on (-1/2, 1/2) are their mirrors 1 - sigma). The chain starts at T0 where N = 0. (The first form ran the four edges
    of the rectangle itself; its left edge at Re s = -1/2 passed the call's 600 s in one piece -- its banked pieces are not read.)"""
    _free('THE BASE')
    MODE[0] = 'q1'
    P9.SEG = 'base'
    U = units()
    if ('base', T0) in U:
        u = U[('base', T0)]
        print('  the base [-1/2, 3/2] x [-%s, %s]: N %s (banked) ; real sign changes %s' % (T0, T0, u['N'], u['real_changes']))
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
    print('  the base [-1/2, 3/2] x [-%s, %s]: the half path %s (ball %s) + Lambda`s 2 poles = N %s ; real sign changes on [1/2, 3/2] %s ; signs unread %s ; %d s' % (
        T0, T0, c['count'], c['ball'], n, ch or 'NONE', u['unread'] or 'NONE', u['seconds']))
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


def _ctl():
    """(C-c) and (C-d) as their units read them (the control file, its count units)."""
    MODE[0] = 'control23'
    Uc = units()
    MODE[0] = 'q1'
    cc = Uc.get(('count', '325.0_340.285786'))
    cd = Uc.get(('count', '150.0_160.0'))
    return cc, cd


def bank(*a):
    U, bands, t, chain, on_z, off_z = _rows()
    bands = [b for b in bands if b['t_lo'] >= float(T0) - 1e-9]
    bu = U.get(('base', T0)) or {}
    over1 = [z for z in off_z if float(z['re']) > 1.0]
    cc, cd = _ctl()
    MODE[0] = 'control23'
    cpieces = [v for (r_, k_), v in units().items() if r_ == 'hppiece' and k_.startswith('325.0_340.285786')]
    MODE[0] = 'q1'
    qs = [v.get('seconds', 0) for (r_, k_), v in U.items() if r_ == 'hppiece' and '@' in k_] or [0]
    ctl_lines = ['### THE CONTROLS: data/b713_list_controls.txt ((C-a) the engine carried to sqrt(23) equal to b667`s, (C-b) Z_Q1 against the genus',
                 '### identity, NEG failing); (C-c) b711`s band [325.0, 340.285786] counted at DQ = 23, the right edge 3/2: N %s, b711`s 26, %s ;' % (
                     (cc or {}).get('count'), 'EQUAL' if (cc or {}).get('count') == 26 else '### NOT EQUAL'),
                 '### (C-d) b709`s band [150.0, 160.0] counted at DQ = 23, the right edge %s: N %s, b709`s 15 (data/b709_pairs.txt :19), %s.' % (
                     SIGMA_R, (cd or {}).get('count'), 'EQUAL' if (cd or {}).get('count') == 15 else '### NOT EQUAL'),
                 '### THE RIGHT EDGE: b709`s Re s = 3/2 cannot close at Q1 (its tail Z_Q1(3/2) - 2 = 2.1587 is not below 2); the half path closes at',
                 '### Re s = %s (tail 0.6846), b709`s three functions carried by substitution (`carried`), each count over [-1, %s] x [t_lo, t_hi].' % (SIGMA_R, SIGMA_R),
                 '### THE PRICE READ AGAINST THE RUN: b712`s per-band seconds (data/b712_price.txt :20-:39) read b711`s count units alone, not its',
                 '### twelve-piece units (route hppiece): (C-c)`s one band at 325 ran %d pieces, %d s; the -15 bands` pieces ran %d to %d s.' % (
                     len(cpieces), sum(p.get('seconds', 0) for p in cpieces), min(qs), max(qs)), '']
    L = ['%s -- COMPONENT 2, (R323)(5)(i): THE CERTIFIED ZERO LIST OF Q1 = x^2 + xy + 4y^2 (DISCRIMINANT -15) IN b709`S FOREGROUND BAND FORM (%s)' % (ACT, utc()), '',
         '### rows are bands, each by tools/b709_pairs.py`s band route imported unedited over b667`s engine carried to sqrt(%d) by substitution' % DQ,
         '### (tools/b713_list.py `carried`; its controls data/b713_list_controls.txt and (C-c)): N(band) by the half path, the on-line zeros by the',
         '### certified sign of Lambda_Q1 halved to %s, the off-line zeros by Newton candidates (point values and the band`s count, RECT_CERTIFY %s),' % (P9.W_ON, P9.RECT_CERTIFY),
         '### COMPLETE where N = on + 2 off. THE BASE: [-1, %s] x [-%s, %s] by b709`s count at [-%s, %s] (Lambda`s symmetry), the half path %s + Lambda`s' % (
             SIGMA_R, T0, T0, T0, T0, bu.get('half_path')),
         '### two poles (s = 0, s = 1) = N %s ; the sign of Z_Q1 on [1/2, 3/2] changes %s (unread at 1/2, where zeta(2s) and Gamma(s - 1/2) meet).' % (
             bu.get('N'), bu.get('real_changes') or 'nowhere'),
         '### THE MAIN TERM BESIDE IT (not a bound): N(T) ~ (T/pi) log(T sqrt(15)/(2 pi e)) + 1 at T = %s reads %.1f ; the list holds %d.' % (
             t, (t / math.pi) * math.log(t * math.sqrt(DQ) / (2 * math.pi * math.e)) + 1, len(on_z) + 2 * len(off_z)), ''] + ctl_lines
    for b in bands:
        offz = U.get(('offline', b['key']))
        L.append('  band [%s, %s] | N %s | on-line %s | off-line %s %s | %s' % (
            b['t_lo'], b['t_hi'], b['N'], b['on'], b['off'], [(z['re'][:12], z['im'][:12]) for z in (offz['zeros'] if offz else [])] or '',
            'COMPLETE' if b['complete'] else '### INCOMPLETE'))
    L += ['', '### THE OFF-LINE PAIRS (rho and 1 - conj(rho) in the strip; the list`s order by height):']
    L += ['  pair %d : rho = %s + %s i%s' % (k + 1, z['re'][:20], z['im'][:20], ' ; Re rho > 1' if float(z['re']) > 1.0 else '') for k, z in enumerate(off_z)]
    L += ['', '### THE LEAST HEIGHT OF A ZERO WITH Re rho > 1: %s' % (over1[0]['im'][:16] if over1 else 'none in the list to %s' % t),
          '', '### ### **THE LIST COMPLETE TO %s ; BANDS %d (COMPLETE %d) ; ON-LINE ZEROS %d ; OFF-LINE PAIRS %d.**' % (
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


ROUTES = dict(carried=carried, controls=controls, control23=control23, base=base, next=nxt, band=band, status=status, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b713_list.py carried | controls [dry] | control23 | base | next [tier2] | band <lo> <hi> | status | bank [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
