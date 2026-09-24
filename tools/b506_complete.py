# -*- coding: utf-8 -*-
"""b506_complete.py -- b505`S TOOL, THE FIXTURE RESTATED UNDER (R116)(2). THE EPSTEIN BANK FOR Q0 = x^2 + xy + 6y^2 COUNTED BELOW 150 BY THE ARGUMENT PRINCIPLE.

### `python tools/b506_complete.py fixture | run | price J0 J1`

### THE EVALUATOR. Chowla-Selberg for `Z(s) = SUM' Q0(m, n)^{-s}`, a = b = 1, Delta = 23:
###   Z(s) = 2 zeta(2s) + 2^{2s} sqrt(pi) Gamma(s - 1/2)/Gamma(s) zeta(2s - 1) 23^{1/2 - s}
###        + 2^{s + 5/2} pi^s / (Gamma(s) 23^{s/2 - 1/4}) SUM_n n^{s - 1/2} sigma_{1 - 2s}(n) (-1)^n K_{s - 1/2}(pi n sqrt 23).
### ### Route A (the corpus's `epstein_census.Lam / gamma_Q`, dps 119, K 240) is the reference; the fixture
### compares the two at the banked zeros and off the strip before any count is read.

### THE CONTOUR. The whole strip and beyond sigma = 1: sigma in [1 - SIG_MAX, SIG_MAX], t in [0, 150], cut into
### three columns -- L [1 - SIG_MAX, 0.48], M [0.48, 0.52], R [0.52, SIG_MAX] -- and unit strips in t. ### The
### counted function is `F(s) = (s - 1) Z(s)`, entire in the rectangle, real and nonzero on the real segment.
### ### The ferry's left edge at sigma = 1/2 passes THROUGH the on-line zeros; the M column carries them instead.
"""
import io
import json
import math
import multiprocessing as mpr
import os
import sys
import time

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
BANK = os.path.join(D, 'b506_edges.jsonl')
LOG = os.path.join(D, 'b506_c2_log.txt')
OUT = os.path.join(D, 'b506_c2_results.json')
LIB = json.loads(io.open(os.path.join(D, 'b326_epstein_zeros.json'), encoding='utf-8').read())

DPS = 40
NBES = 12                 # ### e^{-pi sqrt 23 * 12} ~ 1e-79
SIG_MAX = 1.5             # ### the printed zero-free bound: SUM_{k>=2} r(k) k^{-1.5} <= 1.5498 < r(1) = 2
COLS = (('L', None, 0.48), ('M', 0.48, 0.52), ('R', 0.52, None))
T_TOP = 150
STEP0 = 0.05              # ### initial sample spacing on every edge
DARG = 0.4                # ### bisect while an adjacent pair differs by more than this in arg
PROCS = 10
RES = 2 * mp.pi / mp.sqrt(23)
WRITE_LOG = len(sys.argv) > 1 and sys.argv[1] == 'run'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def log(msg):
    line = '[%s] %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg)
    print(line, flush=True)
    if not WRITE_LOG:
        return
    with open(LOG, 'ab') as f:
        f.write((line + NL).encode('utf-8'))


def zcs(s):
    s = mp.mpc(s)
    sq = mp.sqrt(23)
    t1 = 2 * mp.zeta(2 * s)
    t2 = mp.power(2, 2 * s) * mp.sqrt(mp.pi) * mp.gamma(s - 0.5) / mp.gamma(s) * mp.zeta(2 * s - 1) * mp.power(23, 0.5 - s)
    pre = mp.power(2, s + 2.5) * mp.power(mp.pi, s) / (mp.gamma(s) * mp.power(23, s / 2 - 0.25))
    tot = mp.mpc(0)
    for n in range(1, NBES + 1):
        sig = sum(mp.power(d, 1 - 2 * s) for d in range(1, n + 1) if n % d == 0)
        tot += mp.power(n, s - 0.5) * sig * (-1) ** n * mp.besselk(s - 0.5, mp.pi * n * sq)
    return t1 + t2 + pre * tot


def F(s):
    s = mp.mpc(s)
    if abs(s - 1) < mp.mpf(10) ** (-30):
        return mp.mpc(RES)
    # ### ### **b506`S REPAIR, AFTER ITS FIRST RUN CRASHED:** at s = 1/2 and s = 0 exactly the Chowla-Selberg terms
    # ### carry cancelling poles (zeta(2s) against Gamma(s - 1/2); 1/Gamma(s); at s = -1/2, Gamma(-1) against zeta(-2) = 0),
    # ### removable in Z but raised by mpmath
    # ### term by term. ### The bottom edge`s M segment has its midpoint AT 1/2. ### F is continuous there; it is
    # ### read 1e-20 to the right, far below the 0.4 rad arg step.
    for x in (0, mp.mpf(1) / 2, -mp.mpf(1) / 2):
        if abs(s - x) < mp.mpf(10) ** (-25):
            s = s + mp.mpf(10) ** (-20)
    return (s - 1) * zcs(s)


def edge(p0, p1):
    """### net arg change of F along the segment p0 -> p1, adaptive; returns (darg, minmod, nevals)."""
    mp.mp.dps = DPS
    p0, p1 = mp.mpc(p0), mp.mpc(p1)
    n = max(2, int(math.ceil(float(abs(p1 - p0)) / STEP0)))
    pts = [p0 + (p1 - p0) * k / n for k in range(n + 1)]
    vals = [F(p) for p in pts]
    ne = len(vals)
    tot, mm = mp.mpf(0), min(abs(v) for v in vals)
    stack = [(pts[k], pts[k + 1], vals[k], vals[k + 1], 0) for k in range(n)][::-1]
    while stack:
        a, b, fa, fb, dep = stack.pop()
        d = mp.arg(fb / fa)
        if abs(d) > DARG and dep < 30:
            m = (a + b) / 2
            fm = F(m)
            ne += 1
            mm = min(mm, abs(fm))
            stack.append((m, b, fm, fb, dep + 1))
            stack.append((a, m, fa, fm, dep + 1))
            continue
        tot += d
    return float(tot), float(mm), ne


def sig_lines():
    return [1 - SIG_MAX, 0.48, 0.52, SIG_MAX]


def edge_tasks():
    s = sig_lines()
    tasks = []
    for j in range(T_TOP + 1):                     # ### horizontal edges at t = j, left to right, per column
        for c in range(3):
            tasks.append(('H', j, c, (s[c], j), (s[c + 1], j)))
    for j in range(T_TOP):                         # ### vertical edges on sigma line i, upward, t in [j, j+1]
        for i in range(4):
            tasks.append(('V', j, i, (s[i], j), (s[i], j + 1)))
    return tasks


def key(t):
    return '%s:%d:%d' % (t[0], t[1], t[2])


def run_edge(t):
    t0 = time.time()
    darg, mm, ne = edge(complex(*t[3]), complex(*t[4]))
    return dict(key=key(t), darg=darg, minmod=mm, nevals=ne, sec=time.time() - t0)


def load():
    out = {}
    if os.path.exists(BANK):
        for l in io.open(BANK, encoding='utf-8'):
            try:
                r = json.loads(l)
                out[r['key']] = r
            except Exception:                                          # noqa: BLE001
                pass
    return out


def run_pool(tasks):
    done = load()
    todo = [t for t in tasks if key(t) not in done]
    log('edges %d, banked %d, to run %d' % (len(tasks), len(tasks) - len(todo), len(todo)))
    if not todo:
        return
    k, t0 = 0, time.time()
    with mpr.Pool(PROCS) as pool:
        for r in pool.imap_unordered(run_edge, todo, chunksize=1):
            with open(BANK, 'ab') as f:
                f.write((json.dumps(r) + NL).encode('utf-8'))
                f.flush()
                os.fsync(f.fileno())
            k += 1
            if k % 50 == 0 or k == len(todo):
                log('  edges %d / %d  %.0f s' % (k, len(todo), time.time() - t0))


def box_wind(E, j, c):
    """### counterclockwise: bottom (left to right) + right side up - top - left side up."""
    return (E['H:%d:%d' % (j, c)]['darg'] + E['V:%d:%d' % (j, c + 1)]['darg']
            - E['H:%d:%d' % (j + 1, c)]['darg'] - E['V:%d:%d' % (j, c)]['darg']) / (2 * math.pi)


def rect_wind(s0, s1, t0, t1):
    tot, mm = 0.0, float('inf')
    for p0, p1 in (((s0, t0), (s1, t0)), ((s1, t0), (s1, t1)), ((s1, t1), (s0, t1)), ((s0, t1), (s0, t0))):
        d, m, _n = edge(complex(*p0), complex(*p1))
        tot += d
        mm = min(mm, m)
    return tot / (2 * math.pi), mm


def locate(s0, s1, t0, t1, want, depth=0):
    """### subdivide until each box holds one zero and is small, then Newton from its centre."""
    if want == 0:
        return []
    if want == 1 and max(s1 - s0, t1 - t0) < 0.05:
        mp.mp.dps = DPS
        c = mp.mpc((s0 + s1) / 2, (t0 + t1) / 2)
        try:
            r = mp.findroot(zcs, c)
        except Exception:                                              # noqa: BLE001
            return [dict(box=[s0, s1, t0, t1], rho=None)]
        inside = s0 - 1e-9 <= float(r.real) <= s1 + 1e-9 and t0 - 1e-9 <= float(r.imag) <= t1 + 1e-9
        return [dict(box=[s0, s1, t0, t1], rho=[float(r.real), float(r.imag)], inside=inside,
                     absz=float(abs(zcs(r))))]
    if depth > 14:
        return [dict(box=[s0, s1, t0, t1], rho=None, want=want)]
    if (s1 - s0) >= (t1 - t0):
        m = (s0 + s1) / 2
        parts = [(s0, m, t0, t1), (m, s1, t0, t1)]
    else:
        m = (t0 + t1) / 2
        parts = [(s0, s1, t0, m), (s0, s1, m, t1)]
    out = []
    w0 = int(round(rect_wind(*parts[0])[0]))
    out += locate(*parts[0], w0, depth + 1)
    out += locate(*parts[1], want - w0, depth + 1)
    return out


def locate_task(b):
    return b, locate(*b['rect'], b['want'])


def route_a(rho):
    """### route A`s |Z| at a located zero, and the distance it implies, |Z_A| / |Z`| -- the object`s units."""
    import b326_zeros as BZ
    BZ.bind(119, 240)
    s = mp.mpc(*rho)
    g = (mp.sqrt(23) / (2 * mp.pi)) ** s * mp.gamma(s)
    za = abs(BZ.CE.Lam(s) / g)
    mp.mp.dps = DPS
    d = abs(mp.diff(zcs, s))
    return float(za), float(za / d)


def _fx_one(z):
    """### one banked zero: Newton by the evaluator from it; route A and the evaluator at the banked ordinate."""
    import b326_zeros as BZ
    BZ.bind(119, 240)
    s = mp.mpc(z)
    g = (mp.sqrt(23) / (2 * mp.pi)) ** s * mp.gamma(s)
    a = BZ.CE.Lam(s) / g
    mp.mp.dps = DPS
    b = zcs(s)
    r = mp.findroot(zcs, s)
    return dict(s=[z.real, z.imag], newton=[float(r.real), float(r.imag)], dist=float(abs(r - s)),
                absz_newton=float(abs(zcs(r))), route_a=float(abs(a)), cs=float(abs(b)), ab=float(abs(a - b)))


def fixture():
    """### ### **(R116)(2): THE BAR IN THE OBJECT`S OWN UNITS.** ### Every banked zero within 1e-9 of the zero Newton
    ### locates from it; route A against the evaluator to 1e-8 (absolute: at a zero both values are near 0, so a relative
    ### figure there measures nothing) at EVERY banked ordinate. ### Both printed as counts passing out of 148."""
    offl = [complex(*o['rho_a']) for o in LIB['offline']]
    on = [complex(0.5, z['gamma_a']) for z in LIB['zeros']]
    with mpr.Pool(PROCS) as pool:
        rows = pool.map(_fx_one, offl + on)
    n_d = sum(1 for r in rows if r['dist'] < 1e-9)
    n_a = sum(1 for r in rows if r['ab'] < 1e-8)
    log('fixture (R116)(2): within 1e-9 of their Newton zeros %d of %d, largest distance %.2e ; route A against the'
        ' evaluator to 1e-8 %d of %d, largest |A - CS| %.2e ; largest |Z| after Newton %.2e'
        % (n_d, len(rows), max(r['dist'] for r in rows), n_a, len(rows), max(r['ab'] for r in rows),
           max(r['absz_newton'] for r in rows)))
    return rows, n_d, n_a


def smooth_n(T):
    T = mp.mpf(T)
    return float((T * mp.log(mp.sqrt(23) / (2 * mp.pi)) + mp.im(mp.loggamma(mp.mpc(0.5, T)))) / mp.pi + 1)


def s_of_t(T):
    """### S(T) = arg Z(1/2 + iT) / pi by continuous variation from sigma = SIG_MAX, where |arg Z| < pi/2."""
    d, _m, _n = 0.0, 0, 0
    mp.mp.dps = DPS
    z0 = zcs(mp.mpc(SIG_MAX, T))
    d, _m, _n = edge_z(complex(SIG_MAX, T), complex(0.5, T))
    return (float(mp.arg(z0)) + d) / math.pi


def edge_z(p0, p1):
    global F
    keep = F
    F = zcs
    try:
        return edge(p0, p1)
    finally:
        F = keep


def run():
    t00 = time.time()
    log('b506 C2 -- start ; SIG_MAX %.2f ; columns %s ; dps %d ; Bessel terms %d' % (SIG_MAX, sig_lines(), DPS, NBES))
    rows, n_d, n_a = fixture()
    if not (n_d == len(rows) == n_a):
        log('### FIXTURE FAILED ; no count read')
        return 2
    log('REGISTERED GATE RE-EXAMINED : b326`s registered_gate_passed = False records its precision gate at the REGISTERED'
        ' dps 60 only; the library was built at dps 119, and under (R116)(2) its zeros pass at %d and %d of %d -- %s'
        % (n_d, n_a, len(rows), 'THE BANKED ZEROS STAND' if n_d == n_a == len(rows) else '### THE BANKED ZEROS DO NOT ALL STAND'))
    run_pool(edge_tasks())
    E = load()
    boxes = []
    for j in range(T_TOP):
        for c, (name, _a, _b) in enumerate(COLS):
            w = box_wind(E, j, c)
            boxes.append(dict(j=j, col=name, wind=w, n=int(round(w)), near=abs(w - round(w)) < 0.05))
    bad = [b for b in boxes if not b['near']]
    minmod = min(r['minmod'] for r in E.values())
    tot = sum(b['n'] for b in boxes)
    per = {name: sum(b['n'] for b in boxes if b['col'] == name) for name, _a, _b in COLS}
    whole = (sum(E['H:0:%d' % c]['darg'] for c in range(3)) + sum(E['V:%d:3' % j]['darg'] for j in range(T_TOP))
             - sum(E['H:%d:%d' % (T_TOP, c)]['darg'] for c in range(3))
             - sum(E['V:%d:0' % j]['darg'] for j in range(T_TOP))) / (2 * math.pi)
    log('boxes %d ; not near an integer %d ; smallest |F| on any edge %.2e' % (len(boxes), len(bad), minmod))
    log('COUNT : whole contour %.4f ; by columns L %d M %d R %d ; total %d' % (whole, per['L'], per['M'], per['R'], tot))
    sm = smooth_n(T_TOP)
    S = s_of_t(T_TOP)
    log('N(150) smooth term with the +1 : %.4f ; the ferry`s main term 178.596 ; S(150) by continuous variation %.4f ;'
        ' smooth + S = %.4f' % (sm, S, sm + S))
    on = [z['gamma_a'] for z in LIB['zeros']]
    sym = [j for j in range(T_TOP) if [b['n'] for b in boxes if b['j'] == j and b['col'] == 'L']
           != [b['n'] for b in boxes if b['j'] == j and b['col'] == 'R']]
    log('symmetry : strips whose L count differs from their R count %d' % len(sym))
    mism = []
    for b in boxes:
        if b['col'] == 'M':
            nb = sum(1 for g in on if b['j'] <= g < b['j'] + 1)
            b['bank'] = nb
            if nb != b['n']:
                mism.append(b)
    log('M column : banked on-line %d ; boxes whose count differs from the bank %d' % (len(on), len(mism)))
    todo = []
    for b in boxes:
        if b['col'] == 'R' and b['n'] > 0:
            todo.append(dict(col='R', j=b['j'], rect=(0.52, SIG_MAX, b['j'], b['j'] + 1), want=b['n']))
        if b['col'] == 'M' and b['n'] != b.get('bank'):
            todo.append(dict(col='M', j=b['j'], rect=(0.48, 0.52, b['j'], b['j'] + 1), want=b['n']))
    log('locating : %d boxes (R with a zero, M differing from the bank)' % len(todo))
    found = []
    with mpr.Pool(PROCS) as pool:
        for b, zs in pool.imap_unordered(locate_task, todo):
            for z in zs:
                z['col'], z['j'] = b['col'], b['j']
                found.append(z)
                log('  zero %s  col %s  |Z| %.1e  inside %s' % (z.get('rho'), b['col'], z.get('absz', float('nan')), z.get('inside')))
    for z in found:
        if z.get('rho'):
            z['route_a'], z['route_a_dist'] = route_a(z['rho'])
    found.sort(key=lambda z: (z['rho'] or [0, 0])[1])
    known = [tuple(o['rho_a']) for o in LIB['offline']]
    ctrl = [any(z.get('rho') and abs(z['rho'][0] - b) < 1e-8 and abs(z['rho'][1] - g) < 1e-8 for z in found) for b, g in known]
    offR = [z for z in found if z['col'] == 'R' and z.get('rho')]
    new_off = [z for z in offR if not any(abs(z['rho'][0] - b) < 1e-8 and abs(z['rho'][1] - g) < 1e-8 for b, g in known)]
    beyond1 = [z for z in offR if z['rho'][0] > 1]
    lacks_strip = tot - (len(on) + 2 * len(known))
    log('positive control : the banked pair recovered %s' % ctrl)
    log('off-line zeros in R : %d located, %d not in the bank, %d at sigma > 1' % (len(offR), len(new_off), len(beyond1)))
    log('the whole-strip count %d against the present bank`s %d (146 on-line + 2 x 2 off-line) : lacks %d'
        % (tot, len(on) + 2 * len(known), lacks_strip))
    res = dict(sig_max=SIG_MAX, dps=DPS, nbes=NBES, step0=STEP0, darg=DARG, fixture=rows, fixture_dist_pass=n_d, fixture_route_pass=n_a, boxes=boxes, not_near=len(bad), minmod=minmod, whole=whole, per=per, total=tot,
               smooth=sm, S=S, sym_mismatch=sym, main_ferry=178.5959741491629, m_mismatch=mism, found=found, control=ctrl,
               off_R=len(offR), new_off=len(new_off), beyond1=len(beyond1), lacks_strip=lacks_strip,
               bank_on=len(on), seconds=time.time() - t00, nevals=sum(r['nevals'] for r in E.values()))
    open(OUT + '.tmp', 'wb').write((json.dumps(res, indent=1) + NL).encode('utf-8'))
    os.replace(OUT + '.tmp', OUT)
    log('b506 C2 -- done in %.0f s ; results written' % res['seconds'])
    return 0


def price(j0, j1):
    """### every edge of strips j0..j1-1, timed on the pool, banked to a scratch file only."""
    global BANK
    BANK = os.path.join(os.environ.get('TEMP', '.'), 'b506_price_edges.jsonl')
    ts = [t for t in edge_tasks() if j0 <= t[1] < j1 or (t[0] == 'H' and t[1] == j1)]
    t0 = time.time()
    with mpr.Pool(PROCS) as pool:
        rs = list(pool.imap_unordered(run_edge, ts))
    wall = time.time() - t0
    print('strips %d..%d : %d edges, %d evaluations, %.0f s wall, %.0f s cpu'
          % (j0, j1, len(ts), sum(r['nevals'] for r in rs), wall, sum(r['sec'] for r in rs)))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'fixture':
        fixture()
    elif cmd == 'run':
        sys.exit(run())
    elif cmd == 'price':
        price(int(sys.argv[2]), int(sys.argv[3]))
