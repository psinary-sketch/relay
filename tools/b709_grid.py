# -*- coding: utf-8 -*-
"""b709_grid.py -- THE FINE GRID OF THE SIGN-ONSET RADIUS AT Q0, (R319)(3), AS data/b708_registrations.txt (i) REGISTERED IT (:10-:58,
committed alone at relay 6045dd8c before any number, unchanged): "for each family (the band zero's, rho_0's), the interval between the greatest
positive coarse radius and the least negative one subdivided at the rungs log p^k that fall in it and at the midpoints between consecutive rungs;
the least eigenvalue computed at each point; the onset the least grid point with a negative eigenvalue; the hypothesis read (the onset within one
subdivision step past a rung) and the falsifier read (the onset at a midpoint with no rung within one step below it), printed HELD or REFUTED per
family; the controls printed before the figures (the coarse endpoints reproducing b707's eigenvalues; the zeta form positive at every new point,
its lambda_min printed beside its certified tail bound from tools/b696_witness_balls.py); the rung named where the hypothesis holds, with the
coefficient of Z_Q that enters at it".

### UNTRACKED WRITE: data/b709_grid_units.jsonl (one unit per (route, family, kind, point, obj), appended, resumable; b707's form).

### THE FORM, b707's unchanged (tools/b707_onset.py, IMPORTED unedited: Combo, gram, reading, _gz_unit, the constants; tools/b694_witness_terms.py
### Window; tools/b696_witness_balls.py a_int, arch_tail): the family F_a(gamma_0) = span{C, N} at one frequency, the Weil form S = P - PR + A in
### balls at 128 bits as the 2 x 2 matrix G with the L2 Gram M, the least eigenvalue in the L2 metric, the reading POSITIVE DEFINITE / NEGATIVE
### DIRECTION / UNDECIDED beyond its bound. THE GRID POINTS: every point carries an integer N with a = (1/2) log N, L = a/2 = (1/4) log N -- a rung
### log p^k has N = p^(2k); the midpoint of log m1 and log m2 has N = m1 m2; a coarse endpoint 2 log w has N = w^4 and is given to the window as
### b707 gave it, the integer width w (so the controls reproduce b707's windows exactly). A non-endpoint's window has the width N^(1/4) as a
### 60-digit decimal, its L the log of that decimal in a ball (the window computed is the window of that width; a = 2L is printed as computed).
### THE PRIME SUM at such a width: tools/b694_witness_terms.py exact_ratio (:335) knows only integer widths, and the window's float path refuses
### an x = log n that meets a knot sum (kval :176-:177) -- at a rung log p^k with k >= 2 the lower powers p^j do meet one -- so the prime sum here
### (prime_sum709) is b694's prime_sum (:346-:358) with the exact ratio read from N: log n = (m/3) L exactly iff n^12 = N^m, m = 1..6, and
### those n go through the window's rational path as b694's integer widths do. nmax = isqrt(N) (n <= e^(2L) = sqrt N; the boundary term, where
### N is a square, exact by the rational path and zero by the support).
### THE CONTROLS, run and printed BEFORE any grid figure: (C1) the coarse endpoints a_+ and a_- of each family, both forms, recomputed through this
### tool's own path and read against b707's banked units (data/b707_onset.json.gz through data/b707_onset_hashes.txt): S per window and
### lambda_min within the balls, the readings equal; (C2) the zeta form at every grid point POSITIVE DEFINITE BEYOND ITS BOUND, its lambda_min
### printed beside the certified archimedean tail balls of its three windows (arch_tail :90; the zero tail is not read, b705's contour) -- a Q0
### figure at a point is refused until the zeta form at that point is read so; (C3) the rung structure printed before any figure: at each rung
### the prime power p^k, Lambda_Q(p^k) and Lambda(p^k) as computed (b325's inversion, lambda_q :291), the terms that enter.
### THE READING per family: the onset the least grid point (by a) read NEGATIVE DIRECTION BEYOND ITS BOUND; its kind (a rung, or the midpoint
### above a rung); the rung named with the coefficient of Z_Q entering at it; the hypothesis and the falsifier as registered, each printed
### HELD / REFUTED / NOT FIRED with the registration's own vacuity read beside (data/b708_registrations.txt :39-:45): on this grid every
### midpoint stands half a step above a rung, so the falsifier as worded cannot fire and the hypothesis holds of every point by construction --
### VACUOUS is printed in the same sentence as the verdict; the discriminating reading is the onset's kind and its rung.
### Routes (each its own foreground call, resumable by the units file):
###   rungs                        the grid per family, counted against the registration (197 / 2026 rungs; 395 / 4053 points), the rung structure
###   controls                     C1 at the four coarse endpoints, both forms (24 window terms), against b707's units; the per-window seconds
###   zeta <fam> <i> <j>           C2 at the grid points i..j of the family (the index in the grid's order), the zeta form
###   q0 <fam> <i> <j>             the Q0 form at the points i..j (refused at a point until its zeta reading is POSITIVE DEFINITE)
###   status [fam]                 what is banked, what remains, the seconds so far
###   bank [partial]               data/b709_grid.txt, data/b709_grid.json.gz beside data/b709_grid_hashes.txt (data/b680_rules.txt row (1))
### Written by the Write tool at b709; it writes only the banks it names and its units file. Every value a ball (python-flint) at 128 bits.
"""
import gzip
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import acb, arb, ctx, fmpq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b694_witness_terms as W    # noqa: E402  ### the window, the prime channels, the bracket: imported unedited
import b696_witness_balls as WB   # noqa: E402  ### the archimedean integral and its tail ball: imported unedited
import b707_onset as O7           # noqa: E402  ### b707's form: Combo, gram, reading, _gz_unit, the frequencies: imported unedited

ACT = 'b709'
PREC = WB.PREC
ctx.prec = PREC
UNITS = os.path.join(D, '%s_grid_units.jsonl' % ACT)
FREQS = dict(O7.FREQS)                   # ### band: the band zero's ordinate (data/b703_q0_band.txt :18) ; rho0: tools/b694_witness.py G0
KINDS = O7.KINDS                         # ### ('C', 'N', 'CN')
R_INT = O7.R_INT                         # ### 4000, b705's contour
bs, bl, fmt = WB.bs, WB.bl, WB.fmt
REG = 'data/b708_registrations.txt'
# ### THE INTERVAL PER FAMILY (data/b708_registrations.txt :15-:20): the coarse endpoints as b707's integer widths, a = 2 log w
INTERVAL = dict(band=('128', '192'), rho0=(O7.SQRT2, '32'))
ENDPOINT_RUNG = dict(band=('128', '192'), rho0=('log2', '32'))   # ### b707's rung names for the endpoints (data/b707_onset.txt rows)
REG_COUNTS = dict(rho0=dict(rungs=197, points=395), band=dict(rungs=2026, points=4053))   # ### :24-:27, DERIVED there, re-counted here
WIDTH_DIGITS = 60


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put_txt(name, L):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


UNITS_BAND = os.path.join(D, '%s_grid_units_band.jsonl' % ACT)   # ### UNTRACKED WRITE: the band zero's zeta terms, their own file so that the
#                                                                 # ### families' and forms' parts may run as separate foreground processes at once
UNITS_Q0 = dict(rho0=os.path.join(D, '%s_grid_units_rho0_q0.jsonl' % ACT), band=os.path.join(D, '%s_grid_units_band_q0.jsonl' % ACT))   # ### UNTRACKED WRITES


SEG = ''   # ### a segment name given to zeta/q0 as the fourth argument: that call's terms go to data/b709_grid_units_seg_<name>.jsonl (UNTRACKED WRITE),
#          # ### so that several segments of one family run as separate foreground processes at once, none appending to another's file


def _units_file(u):
    if u.get('route') != 'terms':
        return UNITS
    if SEG:
        return os.path.join(D, '%s_grid_units_seg_%s.jsonl' % (ACT, SEG))
    if u.get('obj') == 'q0':
        return UNITS_Q0[u['fam']]
    return UNITS_BAND if u.get('fam') == 'band' else UNITS


def units():
    U = {}
    segs = sorted(os.path.join(D, f) for f in os.listdir(D) if f.startswith('%s_grid_units_seg_' % ACT) and f.endswith('.jsonl'))
    for path in (UNITS, UNITS_BAND, UNITS_Q0['rho0'], UNITS_Q0['band']) + tuple(segs):
        if os.path.exists(path):
            for l in io.open(path, encoding='utf-8'):
                if l.strip():
                    u = json.loads(l)
                    U[(u['route'], u.get('fam', ''), u.get('kind', ''), u.get('point', ''), u.get('obj', ''))] = u
    return U


def put_unit(u):
    u['at'] = utc()
    with open(_units_file(u), 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


# ================================================================================ THE GRID PER FAMILY
def _prime_powers(lo, hi):
    """(p, k, p^k) with lo < p^k <= hi, by a sieve to hi."""
    sieve = bytearray([1]) * (hi + 1)
    out = []
    for p in range(2, hi + 1):
        if sieve[p]:
            for m in range(p * p, hi + 1, p):
                sieve[m] = 0
            q, k = p, 1
            while q <= hi:
                if q > lo:
                    out.append((p, k, q))
                q *= p
                k += 1
    return sorted(out, key=lambda x: x[2])


def grid(fam):
    """the points of the family in the order of a: each dict(name, kind, N, p, k, m (the prime power or the two it lies between), width).
    The endpoints a_+ (index 0) and a_- (the last index) are the controls' points (b707's integer widths); the rungs log p^k with
    e^(a_+) < p^k <= e^(a_-) and the midpoints between consecutive rungs. Where a_- is itself a rung (rho_0: 1024 = 2^10) the last rung and the
    endpoint coincide and the point is entered once, as the endpoint (b707's window), its rung structure beside it."""
    wlo, whi = INTERVAL[fam]
    lo = int(round(float(arb(wlo) ** 2)))   # ### e^(a_+) = w^2 (128^2 = 16384 ; (sqrt 2)^2 = 2), the interval open there
    hi = int(whi) ** 2
    rungs = _prime_powers(lo, hi)
    pts = [dict(name='a+', kind='end', N=int(wlo) ** 4 if wlo.isdigit() else None, width=wlo, rung=ENDPOINT_RUNG[fam][0], m=lo)]
    prev = None
    for p, k, q in rungs:
        if prev is not None:
            pts.append(dict(name='mid%d_%d' % (prev, q), kind='mid', N=prev * q, m=(prev, q)))
        if q == hi:
            pts.append(dict(name='a-', kind='end', N=int(whi) ** 4, width=whi, rung=ENDPOINT_RUNG[fam][1], m=hi, p=p, k=k, is_rung=True))
        else:
            pts.append(dict(name='rung%d' % q, kind='rung', N=q * q, p=p, k=k, m=q))
        prev = q
    if pts[-1]['kind'] != 'end':
        pts.append(dict(name='a-', kind='end', N=int(whi) ** 4, width=whi, rung=ENDPOINT_RUNG[fam][1], m=hi))
    for i, pt in enumerate(pts):
        pt['i'] = i
        if 'width' not in pt:
            pt['width'] = arb(pt['N']).root(4).str(WIDTH_DIGITS, radius=False)
    return pts


def _window(fam, pt, kind):
    g0 = FREQS[fam]
    w = pt['width']
    if kind == 'C':
        return W.Window(w, 'C', g0=g0)
    if kind == 'N':
        return W.Window(w, 'N', g0=g0)
    if kind == 'CN':
        return O7.Combo(w, g0, 1)
    raise KeyError(kind)


def exact_ratio709(N, n):
    """m/3 where n^12 = N^m exactly (m = 1..6): log n = (m/3) L with L = (1/4) log N; else None."""
    n12 = n ** 12
    for m in range(1, 7):
        if n12 == N ** m:
            return fmpq(m, 3)
    return None


def prime_sum709(Wd, N, lam, nmax):
    """b694's prime_sum (:346-:358) with the exact ratio read from N."""
    tot = arb(0)
    terms, absum = 0, 0.0
    for n in range(2, nmax + 1):
        if lam[n].is_zero():
            continue
        xr = exact_ratio709(N, n)
        kv = Wd.kval(arb(xr) * Wd.L if xr is not None else arb(n).log(), xr)
        t = lam[n] / arb(n).sqrt() * 2 * kv
        tot += t
        terms += 1
        absum += abs(float(t.mid()))
    return tot, terms, absum


_LAM = {}


def _lam(obj, fam):
    """Lambda_Q or Lambda to the family's top n, computed once per process (the values do not depend on the cut)."""
    key = (obj, fam)
    if key not in _LAM:
        top = int(INTERVAL[fam][1]) ** 2
        _LAM[key] = W.lambda_q(top)[0] if obj == 'q0' else W.lambda_z(top)
    return _LAM[key]


def terms709(fam, pt, kind, obj):
    """b707's terms707 (tools/b707_onset.py :155-:168) with the prime sum above and nmax = isqrt(N); k(0) = INT h^2 beside; the tail ball."""
    t0 = time.time()
    Wd = _window(fam, pt, kind)
    N = pt['N']
    if N is None:
        # ### rho_0's a_+ = log 2: b707's window of width sqrt 2 (the decimal SQRT2), N = (sqrt 2)^4 = 4; b707's nmax there 1 (nmax_of: the float
        # ### path is not sent to the boundary n = 2, where the term is zero by the support) -- kept so the control reproduces b707's unit exactly
        N, nmax = 4, 1
    else:
        nmax = math.isqrt(N)
    P = (Wd.khat(acb(0, 0.5)) + Wd.khat(acb(0, -0.5))).real
    lam = _lam(obj, fam)
    PR, nterms, _absum = prime_sum709(Wd, N, lam, nmax) if nmax >= 2 else (arb(0), 0, 0.0)
    Ai = WB.a_int(Wd, obj, 0, R_INT)
    tl = WB.arch_tail(Wd, obj, R_INT)
    A = Ai + WB.unit_ball(tl)
    S = P - PR + A
    k0 = Wd.kval(arb(0), fmpq(0))
    return dict(P=bs(P), PR=bs(PR), Aint=bs(Ai), tail=bs(tl), A=bs(A), S=bs(S), k0=bs(k0), nmax=nmax, prime_terms=nterms, R=R_INT,
                L=bs(Wd.L), a_radius=bs(2 * Wd.L), N=N, width=pt['width'][:24], seconds=int(time.time() - t0))


def _terms(U, fam, pt, kind, obj, route='terms'):
    k = (route, fam, kind, pt['name'], obj)
    if k in U:
        return U[k], False
    u = terms709(fam, pt, kind, obj)
    u.update(route=route, fam=fam, kind=kind, point=pt['name'], obj=obj, i=pt['i'], pkind=pt['kind'], g0=FREQS[fam], prec=PREC)
    put_unit(u)
    U[k] = u
    return u, True


def _form(U, fam, pt, obj, route='terms'):
    us = [U[(route, fam, kd, pt['name'], obj)] for kd in KINDS]
    G, M = O7.gram(*us)
    return us, G, M, O7.reading(G, M)


# ================================================================================ THE RUNG STRUCTURE
def rungs(*a):
    U = units()
    for fam in ('rho0', 'band'):
        pts = grid(fam)
        rg = [p for p in pts if p['kind'] == 'rung' or p.get('is_rung')]
        mids = [p for p in pts if p['kind'] == 'mid']
        want = REG_COUNTS[fam]
        key = ('rungs', fam, '', '', '')
        dup = 1 if any(p.get('is_rung') for p in pts) else 0   # ### rho_0: the last rung log 1024 = 2 log 32 is the endpoint a_-, one point at one a
        if key not in U or 'dup' not in U[key]:
            lq = _lam('q0', fam)
            lz = _lam('zeta', fam)
            rows = [dict(name=p['name'], p=p['p'], k=p['k'], pk=p['m'] if p['kind'] == 'rung' else int(INTERVAL[fam][1]) ** 2, i=p['i'],
                         lambda_q=fmt(lq[p['m'] if p['kind'] == 'rung' else int(INTERVAL[fam][1]) ** 2], 14),
                         lambda_z=fmt(lz[p['m'] if p['kind'] == 'rung' else int(INTERVAL[fam][1]) ** 2], 14)) for p in rg]
            u = dict(route='rungs', fam=fam, rungs=len(rg), mids=len(mids), points=len(pts), dup=dup, reg_rungs=want['rungs'], reg_points=want['points'],
                     counts_equal=(len(rg) == want['rungs'] and len(pts) + dup == want['points']), rows=rows, first=[p['name'] for p in pts[:4]], last=[p['name'] for p in pts[-4:]])
            put_unit(u)
            U[key] = u
        u = U[key]
        print('  %s: rungs %d (the registration %d) ; midpoints %d ; points %d%s (the registration %d) ; COUNTS EQUAL %s ; first %s ; last %s' % (
            fam, u['rungs'], u['reg_rungs'], u['mids'], u['points'], (' + 1 (the last rung log %d is the endpoint a_- itself, one point at one a, entered once)' % int(INTERVAL[fam][1]) ** 2) if u['dup'] else '',
            u['reg_points'], u['counts_equal'], u['first'], u['last']))
        nz = [r for r in u['rows'] if not r['lambda_q'].startswith('0 ') and not r['lambda_q'].startswith('[0 ')]
        print('  %s: rungs at which Lambda_Q(p^k) is non-zero (a Q0 term enters): %d of %d ; the first six rungs:' % (fam, len(nz), len(u['rows'])))
        for r in u['rows'][:6]:
            print('    %-14s p^k = %d^%d = %d | Lambda_Q %s | Lambda %s' % (r['name'], r['p'], r['k'], r['pk'], r['lambda_q'], r['lambda_z']))
    print('### THE GRID COUNTED AGAINST THE REGISTRATION: %s' % ' ; '.join('%s %s' % (f, U[('rungs', f, '', '', '')]['counts_equal']) for f in ('rho0', 'band')))


# ================================================================================ C1: THE COARSE ENDPOINTS AGAINST b707'S UNITS
def _b707_unit(fam, kind, rung, obj):
    return O7._gz_unit('b707_onset.json.gz', 'b707_onset_hashes.txt',
                       lambda x: x.get('route') == 'terms' and x.get('freq') == fam and x.get('kind') == kind and x.get('rung') == rung and x.get('obj') == obj)


def controls(*a):
    """`controls [fam a+|a-]`: the named endpoint's six windows (both forms) computed and read against b707's units, under a 500 s budget per call
    (resume by calling again); with no argument every endpoint is read and, where all 24 windows stand, the C1 verdict unit is written."""
    U = units()
    out = []
    t_all = time.time()
    sel = [(a[0], a[1])] if len(a) >= 2 else [(f, e) for f in ('rho0', 'band') for e in ('a+', 'a-')]
    for fam, which in sel:
        pts = grid(fam)
        for pt in ((pts[0],) if which == 'a+' else (pts[-1],)):
            for obj in ('zeta', 'q0'):
                secs = []
                for kind in KINDS:
                    if time.time() - t_all > 500 and ('c1', fam, kind, pt['name'], obj) not in U:
                        print('### THE CALL`S BUDGET REACHED BEFORE %s %s %s %s -- CALL AGAIN TO RESUME' % (fam, pt['name'], obj, kind))
                        return
                    u, fresh = _terms(U, fam, pt, kind, obj, route='c1')
                    secs.append(u['seconds'])
                    b7 = _b707_unit(fam, kind, pt['rung'], obj)
                    ok = b7 is not None and (bl(u['S']) - bl(b7['S'])).contains(0) and (bl(u['k0']) - bl(b7['k0'])).contains(0) and u['nmax'] == b7['nmax']
                    out.append(dict(fam=fam, point=pt['name'], rung=pt['rung'], obj=obj, kind=kind, S=fmt(bl(u['S']), 12), S_b707=fmt(bl(b7['S']), 12) if b7 else '### NO UNIT',
                                    nmax=u['nmax'], nmax_b707=b7['nmax'] if b7 else None, seconds=u['seconds'], fresh=fresh, ok=bool(ok)))
                    print('  C1 %s %-3s %-4s %-5s | S %s | b707 %s | nmax %d / %s | %d s | %s' % (
                        fam, pt['name'], obj, kind, out[-1]['S'], out[-1]['S_b707'], u['nmax'], out[-1]['nmax_b707'], u['seconds'], 'AS WANTED' if ok else '### NOT AS WANTED'), flush=True)
                us, G, M, r = _form(U, fam, pt, obj, route='c1')
                b7rows = O7._gz_unit('b707_onset.json.gz', 'b707_onset_hashes.txt', lambda x: False)   # ### no unit; the rows are read below
                J7 = _b707_rows()
                r7 = [x for x in J7 if x['obj'] == obj and x['freq'] == fam and x['rung'] == pt['rung']]
                r7 = r7[0] if r7 else None
                ok = r7 is not None and (bl(r['lmin']) - bl(r7['lmin'])).contains(0) and r['reading'] == r7['reading']
                out.append(dict(fam=fam, point=pt['name'], rung=pt['rung'], obj=obj, kind='FORM', lmin=fmt(bl(r['lmin']), 10), lmin_b707=fmt(bl(r7['lmin']), 10) if r7 else '### NO ROW',
                                reading=r['reading'], reading_b707=r7['reading'] if r7 else None, seconds=sum(secs), ok=bool(ok)))
                print('  C1 %s %-3s %-4s FORM  | lambda_min %s | b707 %s | %s / %s | %s' % (
                    fam, pt['name'], obj, out[-1]['lmin'], out[-1]['lmin_b707'], r['reading'], out[-1]['reading_b707'], 'AS WANTED' if ok else '### NOT AS WANTED'), flush=True)
    allok = all(x['ok'] for x in out)
    fresh_secs = [x['seconds'] for x in out if x.get('fresh')]
    if len(sel) == 4:
        put_unit(dict(route='c1verdict', rows=out, ok=allok, window_seconds=[x['seconds'] for x in out if x['kind'] != 'FORM']))
    print('### C1 %s %s ; windows computed this call %d ; seconds per window %s' % ('AS WANTED' if allok else 'NOT AS WANTED', allok if len(sel) == 4 else '(this endpoint alone; the verdict unit at the full call)', len(fresh_secs), fresh_secs))


def _b707_rows():
    H = io.open(os.path.join(D, 'b707_onset_hashes.txt'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    import re
    want_gz = want_js = None
    for l in H:
        m = re.search(r'\b([0-9a-f]{64})\b', l)
        if m and '.json.gz' in l:
            want_gz = m.group(1)
        elif m and '.json (inside' in l:
            want_js = m.group(1)
    gzb = open(os.path.join(D, 'b707_onset.json.gz'), 'rb').read()
    raw = gzip.decompress(gzb)
    if hashlib.sha256(gzb).hexdigest() != want_gz or hashlib.sha256(raw).hexdigest() != want_js:
        sys.exit('### data/b707_onset.json.gz DOES NOT EQUAL ITS HASHES BANK -- NOT READ')
    return json.loads(raw.decode('utf-8')).get('rows') or []


def _c1_ok(U):
    v = [u for k, u in U.items() if k[0] == 'c1verdict']
    return bool(v) and bool(v[-1].get('ok'))


# ================================================================================ C2 AND THE Q0 FORM ON THE GRID
def _run(obj, fam, i, j):
    U = units()
    if not _c1_ok(U):
        sys.exit('### C1 NOT READ AS WANTED -- NO GRID FIGURE COMPUTED (the control before the figure)')
    pts = grid(fam)
    i, j = int(i), int(j)
    t_all = time.time()
    done = skipped = 0
    seen_nonpos = False
    for pt in pts[i:j + 1]:
        if pt['kind'] == 'end':
            continue   # ### the endpoints are the controls' points (C1), not grid figures
        if obj == 'q0':
            zk = [('terms', fam, kd, pt['name'], 'zeta') for kd in KINDS]
            if any(k not in U for k in zk):
                sys.exit('### THE ZETA FORM AT %s %s IS NOT BANKED -- NO Q0 FIGURE AT THIS POINT (the control before the figure)' % (fam, pt['name']))
            _us, _G, _M, rz = _form(U, fam, pt, 'zeta')
            if rz['reading'] != 'POSITIVE DEFINITE BEYOND ITS BOUND':
                sys.exit('### THE ZETA FORM AT %s %s READS %s -- NO Q0 FIGURE AT THIS POINT' % (fam, pt['name'], rz['reading']))
        fresh = False
        for kind in KINDS:
            u, f_ = _terms(U, fam, pt, kind, obj)
            fresh = fresh or f_
        us, G, M, r = _form(U, fam, pt, obj)
        if not fresh:
            skipped += 1
            continue
        done += 1
        tails = [fmt(bl(u['tail']), 3) for u in us]
        nonpos = r['reading'] != 'POSITIVE DEFINITE BEYOND ITS BOUND'
        first_nonpos = nonpos and not seen_nonpos
        seen_nonpos = seen_nonpos or nonpos
        if done % 20 == 1 or first_nonpos or r['reading'] == 'UNDECIDED':   # ### every row is banked; the print is a sample, the call's first non-positive reading and every UNDECIDED one
            print('  %s %-4s %3d %-16s a %s | S_CC %s | S_NN %s | S_CN %s | lambda_min %s | %s | tails %s | %d s' % (
                fam, obj, pt['i'], pt['name'], fmt(bl(us[0]['a_radius']), 10), fmt(G[0], 8), fmt(G[1], 8), fmt(G[2], 8), fmt(bl(r['lmin']), 10), r['reading'],
                ' '.join(tails), sum(u['seconds'] for u in us)), flush=True)
        if time.time() - t_all > 540:
            print('### THE CALL`S BUDGET REACHED AT POINT %d -- RESUME FROM %d (this call: %d points computed, %d banked before)' % (pt['i'], pt['i'] + 1, done, skipped))
            return
    print('### THE RANGE %d..%d DONE (this call: %d points computed, %d banked before)' % (i, j, done, skipped))


def zeta(fam, i, j, *a):
    global SEG
    SEG = a[0] if a else ''
    _run('zeta', fam, i, j)


def q0(fam, i, j, *a):
    global SEG
    SEG = a[0] if a else ''
    _run('q0', fam, i, j)


def status(*a):
    U = units()
    for fam in (a or ('rho0', 'band')):
        pts = grid(fam)
        inner = [p for p in pts if p['kind'] != 'end']
        for obj in ('zeta', 'q0'):
            done = [p for p in inner if all(('terms', fam, kd, p['name'], obj) in U for kd in KINDS)]
            secs = sum(U[('terms', fam, kd, p['name'], obj)]['seconds'] for p in done for kd in KINDS)
            print('  %s %-4s: points %d ; banked %d ; remaining %d ; seconds so far %d ; mean per point %s' % (
                fam, obj, len(inner), len(done), len(inner) - len(done), secs, ('%.1f' % (secs / len(done))) if done else '-'))


# ================================================================================ THE BANK
def bank(*a):
    partial = 'partial' in a
    U = units()
    if not _c1_ok(U):
        sys.exit('### C1 NOT READ AS WANTED -- NOTHING WRITTEN')
    c1v = [u for k, u in U.items() if k[0] == 'c1verdict'][-1]
    L = ['%s -- (R319)(3): THE SIGN-ONSET RADIUS AT Q0 ON THE FINE GRID, AS data/b708_registrations.txt (i) REGISTERED IT (:10-:58) (%s)' % (ACT, utc()), '',
         '### THE FORM: b707`s (tools/b707_onset.py, imported unedited): the Weil form S = P - PR + A of the Epstein zeta of x^2 + xy + 6y^2 (Q0) on the',
         '### family F_a(gamma_0) = span{C, N} of support radius a/2, in balls at %d bits, the 2 x 2 matrix G with the L2 Gram M, the least eigenvalue' % PREC,
         '### in the L2 metric. THE GRID per family (data/b708_registrations.txt :21-:33): the rungs log p^k in (a_+, a_-] and the midpoints between',
         '### consecutive rungs; the coarse endpoints the controls` points. Each point`s window: the width N^(1/4) (a = (1/2) log N), the prime sum`s',
         '### exact ratios read from N (the tool`s head). Rows are grid points: family | index | point | a (as computed) | S_CC | S_NN | S_CN | det G |',
         '### lambda_min, lambda_max | the reading | the witness direction and its S | the zeta form`s lambda_min at the same point beside the',
         '### certified archimedean tail balls of its three windows (C2).', '',
         '### (C1) THE COARSE ENDPOINTS, both forms, through this tool`s own path against b707`s units (data/b707_onset.json.gz through its hashes):']
    for x in c1v['rows']:
        if x['kind'] == 'FORM':
            L.append('  %-4s %-3s %-4s FORM | lambda_min %s | b707 %s | %s / %s | %s' % (x['fam'], x['point'], x['obj'], x['lmin'], x['lmin_b707'], x['reading'], x['reading_b707'], 'AS WANTED' if x['ok'] else '### NOT AS WANTED'))
        else:
            L.append('  %-4s %-3s %-4s %-3s  | S %s | b707 %s | nmax %s / %s | %s' % (x['fam'], x['point'], x['obj'], x['kind'], x['S'], x['S_b707'], x['nmax'], x['nmax_b707'], 'AS WANTED' if x['ok'] else '### NOT AS WANTED'))
    L += ['  C1 AS WANTED %s' % c1v['ok'], '']
    J = dict(at=utc(), prec=PREC, freqs=FREQS, interval=INTERVAL, c1=c1v, families={}, partial=partial)
    verdict = {}
    for fam in ('rho0', 'band'):
        pts = grid(fam)
        rg = U.get(('rungs', fam, '', '', ''))
        if rg is None:
            sys.exit('### THE RUNG STRUCTURE OF %s IS NOT BANKED -- NOTHING WRITTEN' % fam)
        inner = [p for p in pts if p['kind'] != 'end']
        rows, missing, zeta_bad = [], [], []
        for pt in inner:
            have_z = all(('terms', fam, kd, pt['name'], 'zeta') in U for kd in KINDS)
            have_q = all(('terms', fam, kd, pt['name'], 'q0') in U for kd in KINDS)
            if not (have_z and have_q):
                missing.append(pt['name'])
                continue
            usz, Gz, Mz, rz = _form(U, fam, pt, 'zeta')
            us, G, M, r = _form(U, fam, pt, 'q0')
            if rz['reading'] != 'POSITIVE DEFINITE BEYOND ITS BOUND':
                zeta_bad.append(pt['name'])
            rows.append(dict(i=pt['i'], name=pt['name'], kind=pt['kind'], N=pt['N'], p=pt.get('p'), k=pt.get('k'), m=pt['m'], a=us[0]['a_radius'],
                             S_CC=bs(G[0]), S_NN=bs(G[1]), S_CN=bs(G[2]), M_CC=bs(M[0]), M_NN=bs(M[1]), M_CN=bs(M[2]), zeta_lmin=rz['lmin'], zeta_reading=rz['reading'],
                             zeta_tails=[u['tail'] for u in usz], **r))
        if missing and not partial:
            sys.exit('### %s: %d POINTS NOT BANKED (first %s) -- NOTHING WRITTEN (bank partial to write what stands)' % (fam, len(missing), missing[:4]))
        neg = [x for x in rows if x['reading'] == 'NEGATIVE DIRECTION BEYOND ITS BOUND']
        und = [x for x in rows if x['reading'] == 'UNDECIDED']
        onset = neg[0] if neg else None
        # ### the registration's hypothesis and falsifier (:37-:38) with its own vacuity (:39-:45): every midpoint is half a step above a rung
        if onset is None:
            hyp, fal = 'NOT SCORABLE (no negative reading among the %d points banked)' % len(rows), 'NOT FIRED (no onset among the points banked)'
        else:
            hyp = 'HELD -- VACUOUS AS WORDED: every grid point lies within one step past a rung by construction (data/b708_registrations.txt :39-:45)'
            fal = 'NOT FIRED -- VACUOUS AS WORDED: no midpoint of this grid lacks a rung one half-step below it (:39-:45)'
        if onset is not None:
            lq = _lam('q0', fam)
            if onset['kind'] == 'rung' or onset['name'] == 'a-':
                pk = onset['m'] if onset['kind'] == 'rung' else int(INTERVAL[fam][1]) ** 2
                rung_named = 'THE ONSET IS A RUNG: log %d (= %d^%d), Lambda_Q(%d) = %s entering there (zero where Z_Q`s prime side has no term at it)' % (
                    pk, onset['p'] or 0, onset['k'] or 0, pk, fmt(lq[pk], 12))
            else:
                m1, m2 = onset['m']
                below = [x for x in rows if x['name'] == 'rung%d' % m1]
                rung_named = 'THE ONSET IS A MIDPOINT between log %d and log %d: the rung one half-step below it log %d, Lambda_Q(%d) = %s, read %s there' % (
                    m1, m2, m1, m1, fmt(lq[m1], 12), below[0]['reading'] if below else '(not banked)')
        else:
            rung_named = 'no onset among the points banked'
        if onset is not None:
            # ### the discriminating reading beyond the registration's words: the nearest rungs below and above the onset at which a Q0 term
            # ### enters (Lambda_Q(p^k) != 0), by index on the grid, with their Lambda_Q -- the onset read against the term structure
            lq = _lam('q0', fam)
            rr = [p for p in pts if (p['kind'] == 'rung' or p.get('is_rung'))]
            def _pk(p):
                return p['m'] if p['kind'] == 'rung' else int(INTERVAL[fam][1]) ** 2
            below = [p for p in rr if p['i'] <= onset['i'] and not lq[_pk(p)].is_zero()]
            above = [p for p in rr if p['i'] > onset['i'] and not lq[_pk(p)].is_zero()]
            b_ = below[-1] if below else None
            a_ = above[0] if above else None
            rung_named += ' ; THE NEAREST RUNG AT WHICH A Q0 TERM ENTERS: below or at the onset %s ; above it %s' % (
                ('log %d (index %d, %d points below the onset, Lambda_Q %s)' % (_pk(b_), b_['i'], onset['i'] - b_['i'], fmt(lq[_pk(b_)], 10))) if b_ else 'NONE',
                ('log %d (index %d, %d points above, Lambda_Q %s)' % (_pk(a_), a_['i'], a_['i'] - onset['i'], fmt(lq[_pk(a_)], 10))) if a_ else 'NONE')
        verdict[fam] = dict(points=len(inner), banked=len(rows), missing=len(missing), onset=onset['name'] if onset else None, onset_a=onset['a'] if onset else None,
                            onset_kind=onset['kind'] if onset else None, onset_lmin=onset['lmin'] if onset else None, negative=len(neg), undecided=len(und),
                            undecided_at=[x['name'] for x in und][:12], zeta_positive_everywhere=not zeta_bad, zeta_bad=zeta_bad[:12], hypothesis=hyp, falsifier=fal, rung_named=rung_named)
        J['families'][fam] = dict(verdict=verdict[fam], rows=rows, missing=missing, rung_structure=rg)
        L += ['### THE FAMILY %s (gamma_0 = %s): the interval (%s, %s], rungs %d, points %d (the registration`s %d / %d, equal %s); points banked %d, missing %d%s' % (
            fam, FREQS[fam][:24], '2 log %s' % INTERVAL[fam][0][:8] if INTERVAL[fam][0].isdigit() else 'log 2', '2 log %s' % INTERVAL[fam][1], rg['rungs'], rg['points'],
            rg['reg_rungs'], rg['reg_points'], rg['counts_equal'], len(rows), len(missing), (' (PARTIAL: the first missing %s)' % missing[:3]) if missing else ''), '']
        for x in rows:
            L.append('  %-4s | %4d | %-16s | a %s | S_CC %s | S_NN %s | S_CN %s | det %s | lambda %s, %s | %s | v %s S %s %s | zeta lambda_min %s %s tails %s' % (
                fam, x['i'], x['name'], fmt(bl(x['a']), 10), fmt(bl(x['S_CC']), 10), fmt(bl(x['S_NN']), 12), fmt(bl(x['S_CN']), 10), fmt(bl(x['det']), 6),
                fmt(bl(x['lmin']), 10), fmt(bl(x['lmax']), 6), x['reading'], x['witness'], fmt(bl(x['witness_S']), 6), x['witness_reading'],
                fmt(bl(x['zeta_lmin']), 10), 'POS' if x['zeta_reading'] == 'POSITIVE DEFINITE BEYOND ITS BOUND' else '### ' + x['zeta_reading'], ' '.join(fmt(bl(t), 3) for t in x['zeta_tails'])))
        v = verdict[fam]
        L += ['', '  THE ONSET (%s): %s%s ; negative readings %d ; undecided %d %s' % (fam, v['onset'] or 'NONE AMONG THE POINTS BANKED',
                                                                                   (' at a = %s, lambda_min %s, %s' % (fmt(bl(v['onset_a']), 10), fmt(bl(v['onset_lmin']), 8), v['onset_kind'])) if v['onset'] else '',
                                                                                   v['negative'], v['undecided'], v['undecided_at'] or ''),
              '  %s' % v['rung_named'],
              '  THE HYPOTHESIS (the onset within one subdivision step past a rung): %s' % v['hypothesis'],
              '  THE FALSIFIER (the onset at a midpoint with no rung within one step below it): %s' % v['falsifier'],
              '  (C2) THE ZETA FORM POSITIVE DEFINITE BEYOND ITS BOUND AT EVERY POINT BANKED: %s%s' % (v['zeta_positive_everywhere'], (' -- NOT AT %s' % v['zeta_bad']) if v['zeta_bad'] else ''), '']
    L += ['### ### **THE ONSET AT rho_0`S FAMILY: %s (%s) ; AT THE BAND ZERO`S FAMILY: %s (%s) ; THE HYPOTHESIS %s / %s ; THE FALSIFIER %s / %s ; C1 AS WANTED %s ; C2 ZETA POSITIVE AT EVERY POINT %s / %s ; POINTS BANKED %d / %d OF %d / %d%s.**' % (
        verdict['rho0']['onset'] or 'NONE', verdict['rho0']['onset_kind'] or '-', verdict['band']['onset'] or 'NONE', verdict['band']['onset_kind'] or '-',
        verdict['rho0']['hypothesis'].split(' ')[0], verdict['band']['hypothesis'].split(' ')[0], verdict['rho0']['falsifier'].split(' ')[0] + ' ' + verdict['rho0']['falsifier'].split(' ')[1],
        verdict['band']['falsifier'].split(' ')[0] + ' ' + verdict['band']['falsifier'].split(' ')[1], c1v['ok'], verdict['rho0']['zeta_positive_everywhere'], verdict['band']['zeta_positive_everywhere'],
        verdict['rho0']['banked'], verdict['band']['banked'], verdict['rho0']['points'], verdict['band']['points'], ' ; PARTIAL' if partial else '')]
    put_txt('%s_grid.txt' % ACT, L)
    gz = os.path.join(D, '%s_grid.json.gz' % ACT)
    raw = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(gz + '.tmp', 'wb') as fh:
        fh.write(gzip.compress(raw, 9, mtime=0))
    os.replace(gz + '.tmp', gz)
    gzb = open(gz, 'rb').read()
    put_txt('%s_grid_hashes.txt' % ACT, ['%s -- THE GRID`S BINARY BANK, ITS HASHES (data/b680_rules.txt row (1)) (%s)' % (ACT, utc()), '',
                                         '### rows: path ; sha256 ; bytes, LF (the json inside the gz and the gz itself)',
                                         'data/%s_grid.json.gz ; %s ; %d' % (ACT, hashlib.sha256(gzb).hexdigest(), len(gzb)),
                                         'data/%s_grid.json (inside the gz) ; %s ; %d' % (ACT, hashlib.sha256(raw).hexdigest(), len(raw))])
    print(NL.join(L[-12:]))


ROUTES = dict(rungs=rungs, controls=controls, zeta=zeta, q0=q0, status=status, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b709_grid.py rungs | controls | zeta <fam> <i> <j> | q0 <fam> <i> <j> | status [fam] | bank [partial]')
        sys.exit(2)
    fn(*sys.argv[2:])
