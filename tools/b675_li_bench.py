# -*- coding: utf-8 -*-
"""b675_li_bench.py -- THE LI INDEX AT Q0, THE BENCH OF (R285)(7) ON THE AUTHOR'S WORD ON THE PLAN (relay data/b675_li_plan.txt, the
navigator's answers on the plan, the control and the constant, data/b675_author_answers.txt). Written whole by the Write tool at b675.

### OBSERVATION ALONE: the v0.32 bound does not apply to Q0 (data/b675_hypotheses.txt); n* is "the v0.32 bound's onset, were HStrip to
### hold", consumed by no hypothesis; H3 and H4 read along V4's subsequence (the window's NEG count, least NEG n, longest runs).
### Every power zⁿ is exp(n·log z) in Arb balls at 256 bits, never repeated multiplication (plan section 2 (iii)). U_n is the plan's
### inequality on the strip (-1/2, 3/2) under T-COUNT (section 2 (iv)), an ASSUMPTION carried on the face.
### Routes, one foreground call each, each printing its seconds (plan section 6):
###   part1 -- the constants and their primed set, n* and n*', U_n's grid to n* + 300   -> data/b675_li_constants.json
###   part2 -- the bench P_n, n = 1 .. n* + 200, with U_n                                -> data/b675_li_bench.txt (.json)
###   part3 -- C2 as written and C2', n = 1 .. n* + 200                                  -> data/b675_li_controls.json (C2, C2')
###   part4 -- U_n's grid from n* + 300 to n*' + 300                                    -> data/b675_li_constants.json
###   part5 -- H6, n = 1 .. ceil((n*' + 200)/2)                                          -> data/b675_li_controls.json (H6, first half)
###   part6 -- H6, the rest to n*' + 200; the controls bank written                     -> data/b675_li_controls.txt (.json)
### This tool writes only the banks named above. Every python child none; no lean.
"""
import gzip
import hashlib
import io
import json
import os
import sys
import time

from flint import acb, arb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b675_worklist as K   # noqa: E402

NL = chr(10)
PREC = 256
KMAX = 20000                     # ### the tail sums' last unit interval, the rest by the integral bound (plan section 2 (ii), (iv))
T0 = 150                         # ### the certified height
A0 = 10                          # ### T-COUNT: P3's A0Q (Schema/EpsteinQ0.lean :104)
GRID = 100                       # ### U_n's grid step (plan section 2 (iv))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx.prec = PREC


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put(name, data):
    p = os.path.join(D, name)
    b = (json.dumps(data, indent=1, ensure_ascii=False) + NL).encode('utf-8') if not isinstance(data, list) else (NL.join(data) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def get(name):
    p = os.path.join(D, name)
    return json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else {}


def s_(x, d=20):
    return x.str(d, radius=True)


# ================================================================================ THE OBJECT
def reps():
    """the certified points in the upper half-plane, each a representative of a conjugate pair (weight 2): 146 on-line, and for each off-line
    ρ both ρ and its reflection 1 - conj ρ. Rows: (name, σ ball, t ball). Both digests compared with b671's hashes bank first."""
    raw = open(os.path.join(D, K.ZEROS_GZ), 'rb').read()
    inner = gzip.decompress(raw)
    if hashlib.sha256(raw).hexdigest() != K.ZEROS_GZ_SHA or hashlib.sha256(inner).hexdigest() != K.ZEROS_JSON_SHA:
        sys.exit('### THE NARROWED LIST DIFFERS FROM b671`S HASHES BANK -- NOTHING READ')
    Z = json.loads(inner.decode('utf-8'))
    out = []
    for r in Z['rows']:
        t = arb(r['im'], r['h'])
        if r['kind'] == 'ON':
            if r['re'] != '0.5':
                sys.exit('### AN ON ROW WHOSE RE IS NOT "0.5" -- NOTHING READ')
            out.append(('on%d' % r['idx'], arb('0.5'), t))
        else:
            s = arb(r['re'], r['h'])
            out.append(('off%d' % r['idx'], s, t))
            out.append(('ref%d' % r['idx'], 1 - s, t))
    return out


def logz(sig, t):
    rho = acb(sig, t)
    return (1 - 1 / rho).log()


def terms(rows):
    """[(name, log z, σ, t)] for the rows."""
    return [(n, logz(s, t), s, t) for n, s, t in rows]


def P(T, n):
    """P_n over the rows' pairs: Σ 2(1 - Re exp(n log z)), a ball."""
    tot = arb(0)
    for _n, L, _s, _t in T:
        tot += 2 * (1 - (L * n).exp().real)
    return tot


# ================================================================================ U_n (plan section 2 (iv)) AND THE TAILS (section 2 (ii))
def _tailint():
    Kb = arb(KMAX)
    return (Kb.log() + 1) / Kb + 2 / (Kb * Kb)


def u_consts():
    """w_k = 2·A0·log(k + 4)/k′² and a_k = 1/k′², k = 149..KMAX, k′ = max(k, 150); A1 = Σ w_k + 2·A0·tailint."""
    W, A = [], []
    for k in range(T0 - 1, KMAX + 1):
        kp = arb(max(k, T0))
        W.append(2 * A0 * arb(k + 4).log() / (kp * kp))
        A.append(1 / (kp * kp))
    A1 = sum(W, arb(0)) + 2 * A0 * _tailint()
    return W, A, A1


def U(n, W, A, A1):
    """U_n = 1.5 n A1 + (n²/2)(Σ w_k exp(n a_k) + exp(n/KMAX²)·2·A0·tailint): an upper bound on the uncertified zeros' Σ Re(1 - zⁿ)."""
    B = arb(0)
    for w, a in zip(W, A):
        B += w * (a * n).exp()
    B += (arb(n) / (arb(KMAX) * arb(KMAX))).exp() * 2 * A0 * _tailint()
    return arb('1.5') * n * A1 + arb(n) * n / 2 * B


def grid_extend(C, upto):
    W, A, A1 = u_consts()
    g = dict((int(k), v) for k, v in (C.get('U_grid') or {}).items())
    start = (max(g) if g else 0) + GRID
    for n in range(start, upto + GRID, GRID):
        g[n] = arb(U(n, W, A, A1).upper()).str(30)
    C['U_grid'] = dict((str(k), g[k]) for k in sorted(g))
    return C


def Ulook(C, n, cache={}):
    """U at the grid point at or above n (U increases with n): an upper bound at n."""
    gp = ((n + GRID - 1) // GRID) * GRID
    if gp not in cache:
        v = (C.get('U_grid') or {}).get(str(gp))
        if v is None:
            sys.exit('### U_n`S GRID DOES NOT REACH n = %d -- STOPPED' % n)
        cache[gp] = arb(v.strip('[]').split(' +/-')[0])
    return cache[gp]


# ================================================================================ PART 1: THE CONSTANTS
def onset(Dm, R, c, Cc, s, cap=2000000):
    """the least n with Σ_D m - c·Rⁿ + C(n + 1)²sⁿ certified below 0, and the expression's ball there."""
    lR, ls = R.log(), s.log()
    for n in range(1, cap):
        e = Dm - c * (lR * n).exp() + Cc * (n + 1) ** 2 * (ls * n).exp()
        if e < 0:
            return n, e
    return None, None


def constants_for(T, dom, removed=()):
    """section 2 (ii)'s constants on the rows T less `removed`, D = the pair of `dom`: R, θ, r, s1, s, K_cert, K_tail, K, C, K′, n*."""
    rest = [x for x in T if x[0] not in removed and x[0] != dom]
    d = [x for x in T if x[0] == dom][0]
    z = (1 - 1 / acb(d[2], d[3]))
    R, th = abs(z), z.arg()
    r = (1 + R) / 2
    mods = [(x[0], abs(1 - 1 / acb(x[2], x[3]))) for x in rest]
    nxt = max(mods, key=lambda m: m[1].mid())
    unc = (1 + arb(2) / (T0 * T0)).sqrt()                         # ### every uncertified point's modulus bound (section 2 (i))
    below_r = all(bool(m[1] < r) for m in mods) and bool(unc < r)
    if not below_r:
        sys.exit('### A MODULUS IN [r, R) -- s1 IS NOT r; THE PLAN`S RULE DOES NOT REACH IT -- STOPPED')
    s1 = r
    s = (s1 + R) / 2
    Kc = 2 * sum((1 / (1 + x[3] * x[3] + (x[2] - arb('0.5')) ** 2) for x in rest), arb(0))
    Kpc = 2 * sum((1 / (x[2] * x[2] + x[3] * x[3]) for x in rest), arb(0))
    Kt, Kpt = arb(0), arb(0)
    for k in range(T0 - 1, KMAX + 1):
        kp = arb(max(k, T0))
        Kt += 2 * A0 * arb(k + 4).log() / (1 + kp * kp)
        Kpt += 2 * A0 * arb(k + 4).log() / (kp * kp)
    Kt += 2 * A0 * _tailint()
    Kpt += 2 * A0 * _tailint()
    Kk = Kc + Kt
    Cc = 2 * (2 + 2 * (1 + s) ** 2) * Kk
    n_, e = onset(arb(2), R, arb(1) / 4, Cc, s)
    return dict(dom=dom, removed=list(removed), R=s_(R, 25), theta=s_(th, 25), r=s_(r, 25), next_modulus=[nxt[0], s_(nxt[1], 25)],
                uncertified_modulus_bound=s_(unc, 15), every_rest_modulus_below_r=below_r, s1=s_(s1, 25), s=s_(s, 25),
                ln_R_over_s=s_((R / s).log(), 15), K_cert=s_(Kc, 20), K_tail=s_(Kt, 20), K=s_(Kk, 20), C=s_(Cc, 20),
                Kprime_cert=s_(Kpc, 20), Kprime_tail=s_(Kpt, 20), Kprime=s_(Kpc + Kpt, 20), n_star=n_, expr_at_n_star=s_(e, 15) if e is not None else None,
                rest_points=2 * len(rest))


SRC = {'R': 'Schema/LiConverseCfg.lean :169-:170 (r_max; data/b673_v4_control.txt :6, :23)', 'r': ':165-:166 (r = (1 + ‖1 - ρ′⁻¹‖)/2, ρ′ = reflect qE0)',
       's1': ':183-:191', 's': ':192 (s = (s1 + R)/2)', 'C': 'Schema/LiRemainder.lean :180-:181 (C = 2(2 + 2(1 + s)²)·K)',
       'K': 'K over the rest set {‖z‖ < s}, m/(1 + |γ|²), |γ|² = t² + (σ - 1/2)² (RestBound.lean :140, :145); tail under T-COUNT',
       'c': 'Schema/PowerSum.lean :222, consumed at Schema/LiConverseCfg.lean :241-:242 (c = Σm²/(4Σm) = 1/4)',
       'n_star': 'the composition line Schema/LiConverseCfg.lean :295, 2 - Rⁿ/4 + C(n + 1)²sⁿ < 0'}


def part1(*a):
    t0 = time.time()
    T = terms(reps())
    if len(T) != 180:
        sys.exit('### NOT 180 REPRESENTATIVES -- STOPPED')
    t1 = time.time()
    c0 = constants_for(T, 'ref0')
    t2 = time.time()
    c1 = constants_for(T, 'ref1', removed=('ref0',))
    t3 = time.time()
    C = dict(at=utc(), prec=PREC, kmax=KMAX, t_count='ASSUMED: P3 HCount Z 10 (Schema/EpsteinQ0.lean :104, :108)', sources=SRC,
             bench=c0, h6=c1, read_as='n* = the v0.32 bound`s onset, were HStrip to hold; consumed by no hypothesis')
    C = grid_extend(C, c0['n_star'] + 300)
    t4 = time.time()
    C['parts'] = dict(part1=dict(seconds=int(t4 - t0), phases=dict(read=round(t1 - t0, 1), constants=round(t2 - t1, 1),
                                                                     constants_h6=round(t3 - t2, 1), U_grid=round(t4 - t3, 1))))
    put('b675_li_constants.json', C)
    for k in ('R', 'theta', 'r', 'next_modulus', 'every_rest_modulus_below_r', 's', 'ln_R_over_s', 'K_cert', 'K_tail', 'K', 'C', 'Kprime', 'n_star', 'expr_at_n_star'):
        print('  %-28s %-60s | H6: %s' % (k, c0[k], c1[k]))
    print('  U grid to %d (%d points) ; seconds %s' % (max(int(x) for x in C['U_grid']), len(C['U_grid']), C['parts']['part1']))


# ================================================================================ PARTS 2-6: THE SUMS
def sign(b):
    return 'NEG' if b < 0 else ('NONNEG' if b >= 0 else 'UNDECIDED')


def runs(signs):
    """run-length: [[sign, first n, last n], ...]."""
    out = []
    for n, sg in signs:
        if out and out[-1][0] == sg and out[-1][2] == n - 1:
            out[-1][2] = n
        else:
            out.append([sg, n, n])
    return out


def window_stats(rows, lo, hi):
    w = [(n, sg) for n, sg in rows if lo <= n <= hi]
    neg = [n for n, sg in w if sg == 'NEG']
    rr = runs(w)
    longest = {}
    for sg, a, b in rr:
        if b - a + 1 > longest.get(sg, (0,))[0]:
            longest[sg] = (b - a + 1, a, b)
    return dict(window=[lo, hi], n=len(w), neg_count=len(neg), least_neg=neg[0] if neg else None,
                longest=dict((k, list(v)) for k, v in longest.items()), undecided=sum(1 for _n, sg in w if sg == 'UNDECIDED'))


def scan(T, lo, hi, C, with_u=True, th=None, keep=()):
    """P_n (+ U_n) for n in [lo, hi]: the signs, every 100th row, the rows in `keep` windows, and the largest n's radius."""
    signs, rows = [], []
    for n in range(lo, hi + 1):
        p = P(T, n)
        u = Ulook(C, n) if with_u else arb(0)
        q = p + u
        sg = sign(q)
        signs.append((n, sg))
        if n % 100 == 0 or any(a <= n <= b for a, b in keep):
            rows.append(dict(n=n, P=s_(p, 15), U=u.str(12), PU=s_(q, 15), sign=sg, rad=float(p.rad()),
                             cos2=(2 * (th * n).cos()).str(6) if th is not None else None))
    return signs, rows, float(P(T, hi).rad())


def _write_bench(B):
    L = ['b675 -- (R285)(7): THE LI INDEX AT Q0, THE BENCH -- OBSERVATION ALONE (%s)' % B['at'], '',
         '### rows are n with P_n as a ball, U_n, P_n + U_n and the sign (NEG below 0, NONNEG at or above, UNDECIDED containing 0), with',
         '### 2cos(nθ) = Re Σ_D wⁿ beside each row. P_n over the 360 certified points in Arb balls at %d bits, powers by exp(n·log z); U_n the plan`s' % PREC,
         '### inequality on (-1/2, 3/2) under T-COUNT (an ASSUMPTION: P3, HCount Z 10). The v0.32 bound does not apply to Q0 (relay',
         '### data/b675_hypotheses.txt); n* = %d is "the v0.32 bound`s onset, were HStrip to hold" (relay data/b675_li_constants.json), consumed' % B['n_star'],
         '### by no hypothesis. Rows: the window [n*, n* + 200] whole, every 100th n elsewhere; every sign change in the .json run-length line.', '']
    for r in B['rows']:
        L.append('  %7d  P %-40s U %-18s P+U %-40s %-9s  2cos(nθ) %s' % (r['n'], r['P'], r['U'], r['PU'], r['sign'], r['cos2']))
    W = B['window']
    L += ['', '### THE RADIUS OF P_n AT THE LARGEST n (%d): %.3e' % (B['hi'], B['rad_hi']),
          '### n_obs, THE LEAST n WITH P_n + U_n CERTIFIED BELOW 0: %s ; UNDECIDED n OVER [1, %d]: %d' % (B['n_obs'], B['hi'], B['undecided']),
          '### THE WINDOW [%d, %d] ALONG V4`S SUBSEQUENCE (the navigator`s answer on the plan): n %d ; NEG %d ; THE LEAST NEG %s ; THE LONGEST RUNS %s ; '
          'UNDECIDED %d' % (W['window'][0], W['window'][1], W['n'], W['neg_count'], W['least_neg'], W['longest'], W['undecided']),
          '', '### ### **n* (WERE HStrip TO HOLD) %d ; n_obs %s ; n_obs ≤ n* %s ; THE WINDOW: NEG %d OF %d, THE LEAST NEG %s ; T-COUNT ASSUMED.**' % (
              B['n_star'], B['n_obs'], B['n_obs'] is not None and B['n_obs'] <= B['n_star'], W['neg_count'], W['n'], W['least_neg'])]
    put('b675_li_bench.txt', L)


def part2(*a):
    t0 = time.time()
    C = get('b675_li_constants.json')
    ns = C['bench']['n_star']
    T = terms(reps())
    th = arb(C['bench']['theta'].strip('[]').split(' +/-')[0])
    signs, rows, rad = scan(T, 1, ns + 200, C, th=th, keep=[(ns, ns + 200)])
    neg = [n for n, sg in signs if sg == 'NEG']
    B = dict(at=utc(), n_star=ns, hi=ns + 200, n_obs=neg[0] if neg else None, rad_hi=rad, undecided=sum(1 for _n, sg in signs if sg == 'UNDECIDED'),
             window=window_stats(signs, ns, ns + 200), runs=runs(signs), rows=rows, seconds=int(time.time() - t0))
    put('b675_li_bench.json', B)
    _write_bench(B)
    C['parts']['part2'] = dict(seconds=B['seconds'])
    put('b675_li_constants.json', C)
    print('  n* %d ; n_obs %s ; window %s ; radius at %d %.3e ; %d s' % (ns, B['n_obs'], B['window'], ns + 200, rad, B['seconds']))


def part3(*a):
    """C2 as written (the dominant pair on the line at its ordinate) and C2′ (every off-line orbit on the line): P_n alone over [1, n* + 200];
    C2′ is the instrument control (P_n ≥ 0 by algebra), C2 an object reading with idx 1's predicted onset (the least n with R′ⁿ > 358)."""
    t0 = time.time()
    C = get('b675_li_constants.json')
    ns = C['bench']['n_star']
    R0 = reps()
    half = arb('0.5')
    c2 = [(n, half if n == 'ref0' else s, t) for n, s, t in R0]
    c2p = [(n, half if not n.startswith('on') else s, t) for n, s, t in R0]
    out = get('b675_li_controls.json')
    for key, rows_ in (('C2', c2), ('C2prime', c2p)):
        t1 = time.time()
        sg, rows, rad = scan(terms(rows_), 1, ns + 200, C, with_u=False)
        neg = [n for n, x in sg if x == 'NEG']
        out[key] = dict(at=utc(), range=[1, ns + 200], least_neg=neg[0] if neg else None, neg_count=len(neg),
                        undecided=sum(1 for _n, x in sg if x == 'UNDECIDED'), rad_hi=rad, runs=runs(sg), rows=rows, seconds=int(time.time() - t1))
    R1 = arb(C['h6']['R'].strip('[]').split(' +/-')[0])
    n1 = 1
    while not ((R1.log() * n1).exp() > 358):
        n1 += 1
    out['C2']['predicted_onset_idx1'] = dict(rule='the least n with R′ⁿ > 358 (idx 1`s reflected term against the at most 358 of the other points` '
                                                  'bounded part), R′ = %s (data/b673_v4_control.txt :7)' % C['h6']['R'], n=n1)
    put('b675_li_controls.json', out)
    C['parts']['part3'] = dict(seconds=int(time.time() - t0), C2=out['C2']['seconds'], C2prime=out['C2prime']['seconds'])
    put('b675_li_constants.json', C)
    for key in ('C2', 'C2prime'):
        x = out[key]
        print('  %-8s least NEG %s ; NEG %d ; UNDECIDED %d ; radius at %d %.3e ; %d s' % (key, x['least_neg'], x['neg_count'], x['undecided'],
                                                                                          ns + 200, x['rad_hi'], x['seconds']))
    print('  C2`s predicted onset from idx 1`s term: %d' % n1)


def part4(*a):
    t0 = time.time()
    C = get('b675_li_constants.json')
    C = grid_extend(C, C['h6']['n_star'] + 300)
    C['parts']['part4'] = dict(seconds=int(time.time() - t0))
    put('b675_li_constants.json', C)
    print('  U grid to %d (%d points) ; %d s' % (max(int(x) for x in C['U_grid']), len(C['U_grid']), C['parts']['part4']['seconds']))


def _h6(lo, hi, key):
    t0 = time.time()
    C = get('b675_li_constants.json')
    R0 = [x for x in reps() if x[0] != 'ref0']
    th = arb(C['h6']['theta'].strip('[]').split(' +/-')[0])
    ns = C['h6']['n_star']
    sg, rows, rad = scan(terms(R0), lo, hi, C, th=th, keep=[(ns, ns + 200)])
    out = get('b675_li_controls.json')
    out[key] = dict(at=utc(), range=[lo, hi], signs_runs=runs(sg), rows=rows, rad_hi=rad, seconds=int(time.time() - t0))
    put('b675_li_controls.json', out)
    C['parts'][key] = dict(seconds=out[key]['seconds'])
    put('b675_li_constants.json', C)
    return out, C


def part5(*a):
    C = get('b675_li_constants.json')
    hi = (C['h6']['n_star'] + 200 + 1) // 2
    out, C = _h6(1, hi, 'H6a')
    print('  H6 first half 1..%d ; %d s' % (hi, out['H6a']['seconds']))


def part6(*a):
    C = get('b675_li_constants.json')
    ns = C['h6']['n_star']
    lo = (ns + 200 + 1) // 2 + 1
    out, C = _h6(lo, ns + 200, 'H6b')
    sg = []
    for key in ('H6a', 'H6b'):
        for s, a_, b_ in out[key]['signs_runs']:
            sg += [(n, s) for n in range(a_, b_ + 1)]
    neg = [n for n, s in sg if s == 'NEG']
    B = get('b675_li_bench.json')
    out['H6'] = dict(n_star=ns, n_obs=neg[0] if neg else None, window=window_stats(sg, ns, ns + 200), runs=runs(sg),
                     undecided=sum(1 for _n, s in sg if s == 'UNDECIDED'),
                     order_onsets=dict(n_star=[C['bench']['n_star'], ns], n_obs=[B.get('n_obs'), neg[0] if neg else None]))
    put('b675_li_controls.json', out)
    _write_controls(out, C, B)
    print('  H6 n*′ %d ; n_obs′ %s ; window %s ; the orders %s ; %d s' % (ns, out['H6']['n_obs'], out['H6']['window'], out['H6']['order_onsets'],
                                                                         out['H6b']['seconds']))


def _write_controls(out, C, B):
    L = ['b675 -- (R285)(7): THE CONTROLS BESIDE THE BENCH -- C2′ (THE INSTRUMENT), C2 AS WRITTEN (AN OBJECT READING), H6 (%s)' % utc(), '',
         '### rows are n with the control`s P_n and sign (every 100th n and the windows); runs and every sign change in the .json.', '']
    for key, title in (('C2prime', 'C2′: every off-line orbit on the line at its ordinates -- P_n ≥ 0 at every n by algebra; H5 read here'),
                       ('C2', 'C2 as (R285)(7) writes it: the dominant pair on the line, sixteen off-line orbits left (an object reading)')):
        x = out[key]
        L += ['== %s' % title]
        L += ['  %7d  P %-40s %s' % (r['n'], r['P'], r['sign']) for r in x['rows']]
        L += ['  ### over [1, %d]: NEG %d ; THE LEAST NEG %s ; UNDECIDED %d ; radius at the largest n %.3e' % (
            x['range'][1], x['neg_count'], x['least_neg'], x['undecided'], x['rad_hi'])]
        if key == 'C2':
            L += ['  ### the onset predicted from idx 1`s term: %d (%s)' % (x['predicted_onset_idx1']['n'], x['predicted_onset_idx1']['rule'])]
        L += ['']
    h = out['H6']
    L += ['== H6: the dominant pair removed; D′ = idx 1`s reflection and its conjugate (constants: data/b675_li_constants.json "h6")']
    L += ['  %7d  P %-40s U %-18s P+U %-40s %-9s 2cos(nθ′) %s' % (r['n'], r['P'], r['U'], r['PU'], r['sign'], r['cos2'])
          for k in ('H6a', 'H6b') for r in out[k]['rows']]
    L += ['  ### n*′ %d ; n_obs′ %s ; UNDECIDED %d ; the window %s' % (h['n_star'], h['n_obs'], h['undecided'], h['window']),
          '  ### the ordering of the onsets: n* %s ; n_obs %s' % (
              '%d < %d' % tuple(h['order_onsets']['n_star']) if h['order_onsets']['n_star'][0] < h['order_onsets']['n_star'][1] else str(h['order_onsets']['n_star']),
              h['order_onsets']['n_obs']), '',
          '### ### **C2′: NEG %d, UNDECIDED %d (H5 %s) ; C2 AS WRITTEN: THE LEAST NEG %s, PREDICTED FROM idx 1 %d ; H6: n*′ %d, n_obs′ %s.**' % (
              out['C2prime']['neg_count'], out['C2prime']['undecided'], 'HELD' if out['C2prime']['neg_count'] == 0 and out['C2prime']['undecided'] == 0 else 'NOT HELD',
              out['C2']['least_neg'], out['C2']['predicted_onset_idx1']['n'], h['n_star'], h['n_obs'])]
    put('b675_li_controls.txt', L)


ROUTES = dict(part1=part1, part2=part2, part3=part3, part4=part4, part5=part5, part6=part6)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b675_li_bench.py %s' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
