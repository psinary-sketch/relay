# -*- coding: utf-8 -*-
"""b326_zeros.py -- THE EPSTEIN ZEROS ON THE LINE, BY THE CORPUS'S OWN CENSUS RUN AT Re s = 1/2,
### WITH AN INDEPENDENT SECOND ROUTE AGREEING ON EVERY ZERO FOUND.

### ### **ROUTE A IS THE CORPUS'S OWN EVALUATOR** -- `epstein_census.Lam`, the incomplete-gamma
### form of `Lambda(s)`, IMPORTED and never edited, with its module constants REBOUND for the
### height (`KTERMS`, `RQ`, `AK`, and the working precision). ### `Lambda(1/2 + i t)` is REAL on the
### line (functional equation + real coefficients), so on-line zeros are sign changes of
### `H(t) := Lambda(1/2 + i t) e^{pi t / 2}` and are refined by a bracketing root-finder.
### ### **THE CENSUS'S OWN ARGUMENT PRINCIPLE, RUN AT THE REAL PART ONE HALF:** ### boxes
### `[1/2 - delta, 1/2 + delta] x [t_i, t_i + Delta]` wound by `epstein_census.winding`; a box whose
### winding exceeds its sign-change count holds a zero OFF the line within `delta` and is reported.
### ### **ROUTE B SHARES NO CODE OF THIS ACT'S WITH ROUTE A:** ### its own representation counts by
### a different enumeration, `Z_Q(s)` formed directly from REGULARIZED incomplete gammas with the
### pole terms divided through by `gamma_Q(s)`, its own Hardy-type real function, and
### `mpmath.findroot` from the route-A bracket. ### Agreement bar `1e-8`.

### ### ### **THE PRECISION, AND WHAT THE REGISTRATION GOT WRONG ABOUT IT -- DECLARED HERE, WHERE
### ### ### THE GATE FIRES.** ### The registration set `dps = 60` from the size of the cancelling
### incomplete-gamma terms (`e^{(pi/2 - 1) t}`). ### That is not the largest cancellation in the
### census's sum: ### **THE POLE TERM `-1/s - 1/(1-s) = -1/(1/4 + t^2)` IS `e^{pi t / 2} / t^2`
### ### TIMES LARGER THAN `Lambda(1/2 + i t)` ITSELF**, so the sum cancels by that factor and the
### working precision must carry `0.68 t - 2 log10 t` digits before any are left. ### The
### registered precision-convergence gate (`dps 60` against `dps 75`, three heights, `1e-15`) is
### RUN FIRST AT THE REGISTERED VALUES, and its verdict is recorded; the working precision is then
### the one at which the SAME gate passes. ### **THE GATE WAS REGISTERED SO THAT IT COULD FIRE;
### ### IT FIRES.**
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
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import epstein_census as CE     # noqa: E402  ### the corpus's own census, IMPORTED never edited

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
BANK = os.path.join(D, 'b326_epstein_zeros_bank.jsonl')
OUT = os.path.join(D, 'b326_epstein_zeros.json')

# ### ==============================================================================================
# ### THE REGISTERED CONSTANTS (section (3) of the sealed registration), and the working ones.
# ### ==============================================================================================
T_CAP = 150.0          # ### the registered cap; the library is reported complete to what it reaches
T_CAP = float(os.environ.get('B326_T', T_CAP))   # ### a SMOKE override only; the run uses the cap
K_REG = 240            # ### a_K = 314.4 at the cap
DPS_REG = 60           # ### REGISTERED -- and expected to fail its own gate (see the docstring)
DPS_STEP = 15          # ### the gate compares dps against dps + 15
GATE_REL = 1e-15       # ### the registered agreement for the precision gate
DELTA = 0.02           # ### the box half-width about Re s = 1/2
BOX_STEP = 0.5         # ### the census's own T_STEP
NSIDE = 10             # ### samples per side of a box: vertical spacing 0.05
SCAN_STEP = 0.1        # ### the sign-change scan on the line
T_LO = 0.5             # ### the census's own lower edge (the pole at s = 1 sits below)
ROUTE_TOL = 1e-8       # ### the registered route agreement
FE_TOL = 1e-12         # ### the census's own functional-equation self-test bar
PROCS = 10

OFFLINE_RECTS = [((0.94, 1.08), (16.0, 16.5)), ((0.66, 0.80), (29.5, 30.0))]   # ### banked, b325 read
SQ23 = None


def bind(dps, K):
    """### REBIND the census's constants for the height. ### The file is not edited."""
    global SQ23
    mp.mp.dps = dps
    CE.DPS = dps
    CE.KTERMS = K
    CE.RQ = CE.rep_counts(K)
    CE.SQ23 = mp.sqrt(23)
    CE.AK = [None] + [2 * mp.pi * k / CE.SQ23 for k in range(1, K + 1)]
    SQ23 = CE.SQ23


# ### ==============================================================================================
# ### ROUTE A -- the corpus's own evaluator, on the line.
# ### ==============================================================================================
def lam_a(s):
    return CE.Lam(s)


def H(t):
    """### `Lambda(1/2 + i t) e^{pi t / 2}`, real on the line; returns (real part, |imag|/|Lambda|)."""
    t = mp.mpf(t)
    v = CE.Lam(mp.mpc(mp.mpf('0.5'), t))
    sc = mp.exp(mp.pi * t / 2)
    return v.real * sc, (abs(v.imag) / abs(v)) if abs(v) > 0 else mp.mpf(0)


# ### ==============================================================================================
# ### ROUTE B -- this act's own evaluator: Z_Q directly, regularized, divided through by gamma_Q.
# ### ==============================================================================================
def rq_b(K):
    """### r_Q(k) by a DIFFERENT enumeration: for each y, solve the quadratic in x."""
    r = [0] * (K + 1)
    ymax = int(math.isqrt(4 * K // 23)) + 2
    for y in range(-ymax, ymax + 1):
        # x^2 + x y + (6 y^2 - k) = 0 has real x iff y^2 - 4(6y^2 - k) >= 0, i.e. k >= 23 y^2 / 4
        kmin = (23 * y * y + 3) // 4
        if kmin > K:
            continue
        # walk x over the real range for k <= K
        disc = y * y - 4 * (6 * y * y - K)
        span = int(math.isqrt(max(disc, 0))) + 2
        xlo = (-y - span) // 2 - 1
        xhi = (-y + span) // 2 + 1
        for x in range(xlo, xhi + 1):
            k = x * x + x * y + 6 * y * y
            if 1 <= k <= K:
                r[k] += 1
    return r


_RQB = None


def gamma_q(s):
    return (SQ23 / (2 * mp.pi)) ** s * mp.gamma(s)


def zq_b(s):
    """### `Z_Q(s)` by regularized incomplete gammas; the pole terms divided through by `gamma_Q`."""
    global _RQB
    if _RQB is None or len(_RQB) != CE.KTERMS + 1:
        _RQB = rq_b(CE.KTERMS)
    s = mp.mpc(s)
    one = 1 - s
    chi = gamma_q(one) / gamma_q(s)
    tot1 = mp.mpc(0)
    tot2 = mp.mpc(0)
    for k in range(1, CE.KTERMS + 1):
        rk = _RQB[k]
        if rk == 0:
            continue
        a = 2 * mp.pi * k / SQ23
        tot1 += rk * mp.power(k, -s) * mp.gammainc(s, a, regularized=True)
        tot2 += rk * mp.power(k, s - 1) * mp.gammainc(one, a, regularized=True)
    return tot1 + chi * tot2 - (1 / s + 1 / one) / gamma_q(s)


def hardy_b(t):
    """### `Z_Q(1/2 + i t) gamma_Q / |gamma_Q|` is real on the line; returns (real, |imag|/|.|)."""
    t = mp.mpf(t)
    s = mp.mpc(mp.mpf('0.5'), t)
    g = gamma_q(s)
    v = zq_b(s) * g / abs(g)
    return v.real, (abs(v.imag) / abs(v)) if abs(v) > 0 else mp.mpf(0)


# ### ==============================================================================================
# ### THE GATES RUN BEFORE THE LIBRARY IS BUILT.
# ### ==============================================================================================
def precision_gate(dps, heights, K):
    """### the registered gate: dps against dps + DPS_STEP at three heights, relative agreement."""
    out = []
    for t in heights:
        bind(dps, K)
        h1, _ = H(t)
        bind(dps + DPS_STEP, K)
        h2, _ = H(t)
        rel = float(abs(h1 - h2) / max(abs(h2), mp.mpf('1e-300')))
        out.append((t, rel))
    return out


def fe_selftest(dps, K, t):
    """### the census's own self-test, at the cap: Lambda(s) == Lambda(1 - s)."""
    bind(dps, K)
    s = mp.mpc(mp.mpf('0.6'), t)
    a, b = CE.Lam(s), CE.Lam(1 - s)
    return float(abs(a - b) / max(abs(a), mp.mpf('1e-300')))


def route_agreement(dps, K, pts):
    """### Lambda_A / gamma_Q against Z_B at points off the line: the two evaluators agree."""
    bind(dps, K)
    out = []
    for sig, t in pts:
        s = mp.mpc(sig, t)
        za = CE.Lam(s) / gamma_q(s)
        zb = zq_b(s)
        out.append(((sig, t), float(abs(za - zb) / max(abs(za), mp.mpf('1e-300')))))
    return out


# ### ==============================================================================================
# ### THE WORKERS.
# ### ==============================================================================================
_W = {}


def _init(dps, K):
    bind(dps, K)
    _W['dps'] = dps


def task_scan(args):
    t0, t1 = args
    rows = []
    t = t0
    while t <= t1 + 1e-12:
        h, im = H(t)
        rows.append((round(t, 6), float(h), float(im)))
        t += SCAN_STEP
    return ('scan', t0, rows)


def task_refine(args):
    t1, t2 = args
    fa = lambda x: H(x)[0]          # noqa: E731
    ga = mp.findroot(fa, (mp.mpf(t1), mp.mpf(t2)), solver='anderson', tol=mp.mpf('1e-24'))
    ga = float(ga)
    fb = lambda x: hardy_b(x)[0]    # noqa: E731
    try:
        gb = mp.findroot(fb, (mp.mpf(t1), mp.mpf(t2)), solver='anderson', tol=mp.mpf('1e-24'))
        gb = float(gb)
        how = 'bracket'
    except Exception:
        gb = float(mp.findroot(fb, mp.mpf(ga), solver='secant', tol=mp.mpf('1e-24')))
        how = 'secant'
    return ('zero', t1, dict(bracket=[t1, t2], gamma_a=ga, gamma_b=gb, route_b=how,
                             agree=abs(ga - gb) <= ROUTE_TOL))


def task_box(args):
    t_lo, t_hi = args
    w, mm = CE.winding(0.5 - DELTA, 0.5 + DELTA, t_lo, t_hi, NSIDE)
    return ('box', t_lo, dict(t_lo=t_lo, t_hi=t_hi, wind=float(w), minmod=float(mm)))


def task_offline(args):
    (slo, shi), (tlo, thi) = args
    s0 = mp.mpc((slo + shi) / 2, (tlo + thi) / 2)
    za = mp.findroot(lambda z: CE.Lam(z), s0, solver='secant', tol=mp.mpf('1e-24'))
    zb = mp.findroot(lambda z: zq_b(z), s0, solver='secant', tol=mp.mpf('1e-24'))
    inside = (slo <= float(za.real) <= shi) and (tlo <= float(za.imag) <= thi)
    return ('offline', tlo, dict(rect=[[slo, shi], [tlo, thi]],
                                 rho_a=[float(za.real), float(za.imag)],
                                 rho_b=[float(zb.real), float(zb.imag)],
                                 agree=abs(za - zb) <= ROUTE_TOL, inside=inside))


# ### ==============================================================================================
# ### THE BANK -- per task, resumable, the census's own idiom.
# ### ==============================================================================================
def load_bank():
    recs = []
    if os.path.exists(BANK):
        for ln in io.open(BANK, encoding='utf-8'):
            ln = ln.strip()
            if ln:
                recs.append(json.loads(ln))
    return recs


def bank(rec):
    with io.open(BANK, 'a', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec) + '\n')


def run_pool(kind, fn, jobs, done_keys, dps, K, log):
    todo = [j for j in jobs if (kind, round(j[0] if not isinstance(j[0], tuple) else j[1][0], 6))
            not in done_keys]
    log('  %-8s jobs %d  (already banked %d)' % (kind, len(todo), len(jobs) - len(todo)))
    if not todo:
        return
    t0 = time.time()
    ctx = mpr.get_context('spawn')
    with ctx.Pool(processes=PROCS, initializer=_init, initargs=(dps, K)) as pool:
        n = 0
        for res in pool.imap_unordered(fn, todo):
            k, key, payload = res
            bank(dict(kind=k, key=round(key, 6), payload=payload, dps=dps, K=K))
            n += 1
            if n % 10 == 0 or n == len(todo):
                log('    %s %d/%d  %.0fs' % (kind, n, len(todo), time.time() - t0))


def main():
    lines = []

    def log(s=''):
        print(s, flush=True)
        lines.append(s)

    log('=' * 100)
    log('b326 -- THE EPSTEIN ZEROS ON THE LINE. ### ROUTE A: THE CENSUS. ### ROUTE B: THIS ACT.')
    log('=' * 100)
    T = T_CAP
    K = K_REG
    heights = tuple(h for h in (50.0, 100.0, 150.0) if h <= T) or (T / 2, T)

    # ### (i) the fixtures that must pass before anything is built.
    log('  (i) representation counts, route B against the census, k = 1..4096 : %s'
        % (rq_b(4096) == CE.rep_counts(4096)))
    log('  (ii) THE REGISTERED PRECISION GATE, AT THE REGISTERED VALUES (dps %d vs %d):'
        % (DPS_REG, DPS_REG + DPS_STEP))
    g_reg = precision_gate(DPS_REG, heights, K)
    for t, rel in g_reg:
        log('      t = %5.1f   relative disagreement %.3e   %s'
            % (t, rel, 'PASS' if rel <= GATE_REL else '### FAIL -- THE GATE FIRES'))
    reg_ok = all(rel <= GATE_REL for _t, rel in g_reg)
    dps = DPS_REG
    if not reg_ok:
        need = int(0.6821 * T - 2 * math.log10(T) + 22)
        log('  ### ### **THE REGISTERED PRECISION FAILS ITS OWN GATE.** ### The cancellation is'
            ' against the pole term, e^{pi t/2}/t^2; the working precision is raised to dps = %d'
            ' and THE SAME GATE IS RUN AGAIN:' % need)
        g2 = precision_gate(need, heights, K)
        for t, rel in g2:
            log('      t = %5.1f   relative disagreement %.3e   %s'
                % (t, rel, 'PASS' if rel <= GATE_REL else '### FAIL'))
        if not all(rel <= GATE_REL for _t, rel in g2):
            log('  ### THE LIBRARY IS NOT BUILT. ### the gate fails at the raised precision too.')
            return 2
        dps = need
    log('  working precision : dps = %d ; K = %d (a_K = %.2f)' % (dps, K, 2 * math.pi * K / math.sqrt(23)))
    fe = fe_selftest(dps, K, T)
    log('  (iii) the census\'s own self-test at the cap, Lambda(s) == Lambda(1-s) at s = 0.6 + %gi :'
        ' rel err %.3e  %s' % (T, fe, 'PASS' if fe <= FE_TOL else '### FAIL'))
    if fe > FE_TOL:
        log('  ### THE LIBRARY IS NOT BUILT.')
        return 2
    ra = route_agreement(dps, K, [(0.5, T / 7), (0.7, T / 2), (0.5, 0.93 * T)])
    for (sig, t), rel in ra:
        log('  (iv) route A / gamma_Q against route B at s = %.1f + %gi : rel %.3e  %s'
            % (sig, t, rel, 'PASS' if rel <= 1e-12 else '### FAIL'))
    if not all(rel <= 1e-12 for _p, rel in ra):
        log('  ### THE LIBRARY IS NOT BUILT.')
        return 2
    bind(dps, K)
    w_hit, mm_hit = CE.winding(0.94, 1.08, 16.0, 16.5, 24)
    log('  (v) the census\'s own banked hit reproduced with the rebound constants : winding %.4f'
        ' (banked 1.000), minmod %.2e' % (float(w_hit), float(mm_hit)))
    ims = [float(H(t)[1]) for t in (7.3, 61.1, 133.7)]
    log('  (vi) Lambda real on the line, |Im|/|Lambda| at three heights : %s  %s'
        % (['%.1e' % x for x in ims], 'PASS' if max(ims) < 1e-20 else '### FAIL'))
    fr = float(mp.findroot(lambda x: mp.cos(x), (1.0, 2.0), solver='anderson'))
    log('  (vii) the bracketing root-finder on cos on (1, 2) : %.12f  %s'
        % (fr, 'PASS' if abs(fr - math.pi / 2) < 1e-10 else '### FAIL'))
    if not (abs(w_hit - 1) < 0.05 and max(ims) < 1e-20 and abs(fr - math.pi / 2) < 1e-10):
        log('  ### THE LIBRARY IS NOT BUILT.')
        return 2

    # ### (2) the scan, banked in chunks.
    recs = load_bank()
    done = set((r['kind'], r['key']) for r in recs if r.get('dps') == dps and r.get('K') == K)
    chunks = []
    t = T_LO
    while t < T - 1e-9:
        t1 = min(t + 5.0 - SCAN_STEP, T)
        chunks.append((round(t, 6), round(t1, 6)))
        t = round(t + 5.0, 6)
    run_pool('scan', task_scan, chunks, done, dps, K, log)

    recs = load_bank()
    scan = []
    for r in recs:
        if r['kind'] == 'scan' and r['dps'] == dps and r['K'] == K:
            scan.extend(r['payload'])
    scan.sort()
    brackets = []
    for (ta, ha, _ia), (tb, hb, _ib) in zip(scan, scan[1:]):
        if ha == 0.0 or (ha < 0) != (hb < 0):
            if tb - ta <= SCAN_STEP + 1e-9:
                brackets.append((ta, tb))
    log('  scan points %d, sign changes %d' % (len(scan), len(brackets)))
    done = set((r['kind'], r['key']) for r in load_bank() if r.get('dps') == dps and r.get('K') == K)
    run_pool('zero', task_refine, brackets, done, dps, K, log)

    # ### (3) the off-line zeros, both routes.
    done = set((r['kind'], r['key']) for r in load_bank() if r.get('dps') == dps and r.get('K') == K)
    todo = [rc for rc in OFFLINE_RECTS if ('offline', round(rc[1][0], 6)) not in done]
    for rc in todo:
        k, key, payload = task_offline(rc)
        bank(dict(kind=k, key=round(key, 6), payload=payload, dps=dps, K=K))

    # ### (4) the boxes, the census's own argument principle at Re s = 1/2.
    boxes = []
    t = T_LO
    while t < T - 1e-9:
        boxes.append((round(t, 6), round(min(t + BOX_STEP, T), 6)))
        t = round(t + BOX_STEP, 6)
    done = set((r['kind'], r['key']) for r in load_bank() if r.get('dps') == dps and r.get('K') == K)
    run_pool('box', task_box, boxes, done, dps, K, log)

    # ### (5) assemble.
    recs = [r for r in load_bank() if r.get('dps') == dps and r.get('K') == K]
    zeros = sorted([r['payload'] for r in recs if r['kind'] == 'zero'], key=lambda z: z['gamma_a'])
    boxes_out = sorted([r['payload'] for r in recs if r['kind'] == 'box'], key=lambda b: b['t_lo'])
    offl = [r['payload'] for r in recs if r['kind'] == 'offline']
    disagree = [z for z in zeros if not z['agree']]
    log('  on-line zeros located : %d ; route disagreements above %.0e : %d'
        % (len(zeros), ROUTE_TOL, len(disagree)))
    mism = []
    for b in boxes_out:
        n_in = sum(1 for z in zeros if b['t_lo'] <= z['gamma_a'] < b['t_hi'])
        w = int(round(b['wind']))
        b['sign_changes'] = n_in
        b['near_integer'] = abs(b['wind'] - w) < 0.1
        if w != n_in or not b['near_integer']:
            mism.append(b)
    log('  boxes %d ; boxes whose winding differs from their sign-change count or is not near an'
        ' integer : %d' % (len(boxes_out), len(mism)))
    for b in mism:
        log('    ### t in [%.1f, %.1f]  winding %.3f  sign changes %d' % (b['t_lo'], b['t_hi'], b['wind'], b['sign_changes']))
    nt = (T / math.pi) * math.log(T * math.sqrt(23) / (2 * math.pi * math.e))
    log('  Riemann-von Mangoldt main term at T = %g : %.2f ; located on the line : %d ; banked'
        ' off-line pairs inside the strip below T : %d' % (T, nt, len(zeros), len(offl)))
    for o in offl:
        log('    off-line zero: route A %s  route B %s  agree %s  inside its banked rectangle %s'
            % (o['rho_a'], o['rho_b'], o['agree'], o['inside']))
    lib = dict(T=T, K=K, dps=dps, dps_registered=DPS_REG, registered_gate_passed=reg_ok,
               delta=DELTA, box_step=BOX_STEP, nside=NSIDE, scan_step=SCAN_STEP,
               route_tol=ROUTE_TOL, fe_selftest_rel=fe,
               zeros=zeros, offline=offl, boxes=boxes_out, box_mismatches=len(mism),
               rvm_main_term=nt, log=lines)
    open(OUT + '.tmp', 'wb').write((json.dumps(lib, indent=1) + '\n').encode('utf-8'))
    os.replace(OUT + '.tmp', OUT)
    log('  library written : %s' % os.path.basename(OUT))
    log('=' * 100)
    return 0 if (not disagree and not mism and all(o['agree'] and o['inside'] for o in offl)) else 1


if __name__ == '__main__':
    mpr.freeze_support()
    sys.exit(main())
