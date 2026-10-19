# -*- coding: utf-8 -*-
"""b687_readings.py -- THE FOUR READINGS OF THE b685 DERIVATION, EACH A REFUTATION TEST AT A NAMED STEP, AND THE CONTROLS, under (R297)(3)-(4)
on the author's word on the plan (relay data/b687_plan.txt; relay data/b687_author_answers.txt; data/b687_rules.txt row (1)).

### THE OBJECT: tools/b685_count.py's derivation, IMPORTED UNEDITED (its sha256 printed) -- params_q/params_z, conditions_q/conditions_z,
### jensen, E_gamma, E_arg, zq_up, zeta_grid, topq, W_window, load_q -- with b685's banks data/b685_count_part1/2/4.json read and never written;
### no constant of b685 changed. Where a step's bound is read at a height other than its own T_MIN, the copy of its few lines taking that
### height as an argument is printed beside its source lines (Rz :321-:329 -> rz_at; topq :205-:211 -> topq_at; jensen's piece :157-:173 ->
### env_piece); every copy reproduces its source exactly at the source's own T_MIN (checked and printed at R1/R5/R6).
### Zeros: ζ by acb.zeta_zero(n) (python-flint), each confirmed by a sign change of the completed function at its ball's ends (tools/b671_narrow.py
### lam_z_at, sign_at, imported unedited -- b681's C1 form); Z_Q by b681's 163 balls through their hashes bank, with the 17 partners, and the
### band (150, 151.5] counted by b667's argument principle (b671's carried square_count). Every count, bound and computed value a ball.
### Parts (each one foreground call under the 590 s guard): R1 reading (i); R2 reading (ii) and C1 for ζ; R3 the band; R4 reading (iii) and C1
### for Z_Q; R5 reading (iv) and C2 for ζ; R6 reading (iv) and C2 for Z_Q; R7 the hypotheses, the banks and (data/b687_rules.txt row (1))
### the composition where H2, H3 and H4 hold. Its bank writes, the only ones: data/b687_readings_part<k>.json, data/b687_matched.txt,
### data/b687_jensen_zeta.txt, data/b687_jensen_q0.txt, data/b687_steps.txt, data/b687_controls.txt, data/b687_composition.txt,
### data/b687_readings.json. No lean; no kernel byte. Written by the Write tool at b687. Usage: python -X utf8 tools/b687_readings.py R1..R7
"""
import gzip
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import arb, acb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T_DIR, D = os.path.join(ROOT, 'tools'), os.path.join(ROOT, 'data')
sys.path.insert(0, T_DIR)
import b685_count as BC              # noqa: E402  ### the derivation under test, imported unedited (it imports b671 and b667 unedited)
B671, CERT = BC.B671, BC.CERT

NL = chr(10)
PREC = BC.PREC
A, bs, up, des, ser = BC.A, BC.bs, BC.up, BC.des, BC.ser
HZ = (100, 1000, 10000)               # ### ζ's sampled heights ((R297)(3)(ii), (iv))
HQ = (50, 100, 149)                   # ### Z_Q's ((R297)(3)(iii), (iv))
HM = ('e', 10, 100, 1000, 10000)      # ### the matched bank's heights: e, 10, 100 (matched range) and b685's 100, 1000, 10⁴ (miss (c)'s answer)
RHO = ('1.4', '1.6', '1.8')           # ### the inner radii of the navigator's answer on the vacuity
ZSET = (('derivation', 1.5, 1.98, 0.5), ('ruling', 1.7, 2.05, 0.5))   # ### the navigator's answer on the ζ disc: the derivation's first
NTH = 16                              # ### Z_Q's θ sampling in (iv): every 16th of the 2048 pieces (128 points)
BAND = ('150', '151.59')
B_H = '0.265'                         # ### R3's split (the plan's section 9 split, on R3's first run passing the guard at four of fifteen squares of
#                                     ### side ½, ~100-200 s each, no bank written): twelve squares of side 0.53, resumable, each banked as it lands
B_EDGES_RE = ('-0.55', '-0.02', '0.51', '1.04', '1.57')            # ### the band's square edges in σ: none on σ = ½; [−½, 3/2] covered
B_EDGES_IM = ('150', '150.53', '151.06', '151.59')                  # ### (150, 151.5] covered
B_LEAF = '1e-8'                       # ### a band zero's square quartered until its disc membership is decided at every radius, or to this
B_START_BY = 60                       # ### a call starts no new square after this many seconds (the 590 s guard; a square ~120-330 s; R3's third
#                                     ### call started its second square at 222 s and the guard stopped it, nothing banked for it); a square whose
#                                     ### attempt was banked unfinished is counted next as its four quarters, each banked as it lands
LOCATED = dict(
    HSW=('0.1038', '0.2573', '9.3675', 'e', False, '(Z1) HSW arXiv:2107.06506v1 Corollary 1.2, p. 2 (1.5): "|N(T) − T/2π log(T/2πe)| ≤ 0.1038 log T + 0.2573 log log T + 9.3675", T ≥ e'),
    HSW_BW=('0.1038', '0.2573', '9.4925', 'e', False, '(Z2) Bellotti-Wong arXiv:2412.15470v2 p. 2 footnote 1: "The value 9.3675 is now substituted with 9.4925"'),
    TR14=('0.111', '0.275', '2.450', 'e', True, '(Z3) Trudgian arXiv:1208.5846v2 Corollary 1, p. 2: "For T ≥ T0 ≥ e |N(T) − T/2π log T/2πe − 7/8| ≤ 0.111 log T + 0.275 log log T + 2.450 + 0.2/T0", T0 = e'),
    PT15=('0.110', '0.290', '2.290', 'e', True, '(PT) Platt-Trudgian arXiv:1402.3953v2 Corollary 1, p. 2: "If T ≥ e, then |S(T)| ≤ 0.110 log T + 0.290 log log T + 2.290", '
                                                '+ 0.2/T by (Z3) (2.5), p. 3'),
    BACKLUND=('0.1370', '0.4430', '5.2250', 200, False, '(Z1) Table 1, p. 1, Backlund [1] (1918): "0.1370 0.4430 5.2250 200"'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def say(s=''):
    print(s, flush=True)


def put(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, L):
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def get(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def TT(x):
    ctx.prec = PREC
    return arb(1).exp() if x == 'e' else A(x)


def sides(computed, bound):
    """a ball comparison computed ≤ bound: HOLDS (computed's upper end at or below bound's lower end), REFUTED (computed's lower end above
    bound's upper end), else UNDECIDED; the margin bound − computed as a ball."""
    m = bound - computed
    return ('HOLDS' if computed.upper() <= bound.lower() else 'REFUTED' if computed.lower() > bound.upper() else 'UNDECIDED'), m


def count_vs(n, bound):
    return 'HOLDS' if arb(n) <= arb(bound.lower()) else 'REFUTED' if arb(n) > arb(bound.upper()) else 'UNDECIDED'


def shas():
    return dict((f, sha(os.path.join(T_DIR, f))[:16]) for f in ('b685_count.py', 'b667_epstein_certify.py', 'b671_narrow.py'))


# ================================================================================ THE COPIES, EACH TAKING ITS HEIGHT AS AN ARGUMENT
def rz_at(pr, I, T, Tm):
    """tools/b685_count.py :321-:329 Rz with T_MIN_Z read as Tm: (R, E, top, S)."""
    Ic, Ir = I
    S = (Ic - 1) * TT(T).log() + Ir - pr['low'].log()
    E = BC.E_gamma(A('0.25'), TT(Tm) / 2, pr['delta'] / 2) + BC.E_arg(pr['delta'], TT(Tm))
    top = arb.pi() / (2 * pr['ell']) * S + E / 2 + ((pr['sigma1'] - 1) / TT(Tm)).atan() + (1 / (2 * TT(Tm))).atan()
    eth = (1 / (16 * TT(Tm)) + 1 / (8 * TT(Tm)) + 1 / (3 * TT(Tm))) / arb.pi()
    return eth + (pr['logz1'] + top) / arb.pi(), E, top, S


def topq_at(pr, I, T, Tm):
    """tools/b685_count.py :205-:211 topq with T_MIN read as Tm: (top, S, E)."""
    Ic, Ir = I
    S = (Ic - 1) * TT(T).log() + Ir - pr['low'].log()
    E = BC.E_gamma(A('0.5'), TT(Tm), pr['delta']) + BC.E_arg(pr['delta'], TT(Tm))
    top = arb.pi() / (2 * pr['ell']) * S + E / 2 + ((pr['sigma1'] - 1) / TT(Tm)).atan() + (1 / (2 * TT(Tm))).atan()
    return top, S, E


def env_piece(pr, k, n, T):
    """tools/b685_count.py :157-:173, jensen's loop body for piece k: (the coefficient's upper end, the rest's upper end, the piece's θ ball,
    which forms) -- F_T(θ) ≤ coef log T + rest on the piece."""
    c, r, eta, p = pr['c'], pr['r'], pr['eta'], pr['p']
    one = A(1)
    th = BC.theta(k, n)
    sg = c + r * th.cos()
    forms = []
    if sg.lower() <= (one + eta).upper():
        lam = (one + eta - sg) / (one + eta - p)
        coef = one + lam * (pr['alpha1'] - one)
        rest = lam * pr['logA'] + (one - lam) * pr['logB'] + coef * ((1 + r / T) ** 2 + ((pr['Q'] + sg) / T) ** 2).log() / 2
        forms.append(('PL', coef, rest))
    if sg.upper() >= (one + eta).lower():
        lo = arb(sg.lower()) if arb(sg.lower()) > arb((one + eta).lower()) else arb((one + eta).lower())
        rest = ((1 + r / T) ** 2 + ((sg - 1) / T) ** 2).log() / 2 + pr['logF'](lo)
        forms.append(('F(σ)', one, rest))
    return arb(max(f[1].upper() for f in forms)), arb(max(f[2].upper() for f in forms)), th, [f[0] for f in forms]


# ================================================================================ THE TWO INSTANCES
def inst_q():
    grid, j, pr, I = BC.load_q()
    return dict(kind='Z_Q', grid=grid, pr=pr, I=I, Tmin=BC.T_MIN, c=j['c'], r=j['r'], eta=j['eta'])


def inst_z(c, r, eta, Tmin=BC.T_MIN_Z, banked=True):
    zg = BC.zeta_grid()
    pr = BC.params_z(zg, c, r, eta)
    if banked:
        j4 = get('b685_count_part4.json')
        assert (j4['c'], j4['r'], j4['eta']) == (c, r, eta)
        I = (des(j4['Ic']), des(j4['Ir']))
    else:
        I = BC.jensen(pr, BC.N_FINAL, TT(Tmin))
    return dict(kind='ζ', grid=zg, pr=pr, I=I, Tmin=Tmin, c=c, r=r, eta=eta)


LAT_N = 60                            # ### the lattice sum's box max(|m|, |n|) ≤ LAT_N
LAT_LAMBDA = '0.95'                   # ### ≤ the least eigenvalue 3.5 − √6.5 = 0.9505 of Q0 = m² + mn + 6n² (data/b667_epstein_plan.txt :8)
_LAT = {}


def zq_lattice(s):
    """Z_Q(s) for σ > 2.5, outside b667's route (its T4 bound needs |σ − ½| ≤ 2): the lattice sum over max(|m|, |n|) ≤ N of Q(m, n)^{−s}, Q0 =
    m² + mn + 6n², plus the tail as a radius: the 8k points with max = k have Q ≥ λ k², so |tail| ≤ 8 λ^{−σ} Σ_{k > N} k^{1 − 2σ} ≤ 8 λ^{−σ}
    N^{2 − 2σ}/(2σ − 2). The seat's route, added at R6 (relay data/b687_defects.txt); checked against b667's where both apply (R6 prints it)."""
    ctx.prec = PREC
    if not _LAT:
        for m in range(-LAT_N, LAT_N + 1):
            for n in range(-LAT_N, LAT_N + 1):
                if m or n:
                    q = m * m + m * n + 6 * n * n
                    _LAT[q] = _LAT.get(q, 0) + 1
    sg = s.real.lower()
    if not sg > 2:
        raise ValueError('the lattice route is read for σ > 2 alone')
    v = acb(0)
    for q, cnt in _LAT.items():
        v += cnt * acb(q) ** (-s)
    lam, N = arb(LAT_LAMBDA), arb(LAT_N)
    sgl = arb(sg)
    tail = 8 * lam ** (-sgl) * N ** (2 - 2 * sgl) / (2 * sgl - 2)
    return v + acb(arb(0, tail.upper()), arb(0, tail.upper()))


def Zval(kind, s):
    ctx.prec = PREC
    if kind == 'Z_Q' and s.real.upper() > 2.5:
        v = zq_lattice(s)
    else:
        v = CERT.zq_point(s) if kind == 'Z_Q' else s.zeta()
    ctx.prec = PREC
    return v


def S_at(ins, T):
    """S(T) as the derivation states it: the banked Jensen integral where T ≥ its T_MIN, the integral at T itself below it (the rest
    decreasing in T, read at T)."""
    I = ins['I'] if T >= ins['Tmin'] else BC.jensen(ins['pr'], BC.N_FINAL, TT(T))
    Ic, Ir = I
    return (Ic - 1) * TT(T).log() + Ir - ins['pr']['low'].log(), I


# ================================================================================ R1: READING (i), THE ζ INSTANCE AT T ≥ e
def located(name, T, derivedR):
    """the located bound at T in its own form and the derived bound in the same form: (located, derived-in-form) or None out of range."""
    a_, b_, c_, T0, has78, _q = LOCATED[name]
    t = TT(T)
    if T0 != 'e' and (T == 'e' or float(T) < T0):
        return None
    ll = t.log().log() if T != 'e' else arb(0)
    L = A(a_) * t.log() + A(b_) * ll + A(c_)
    if name == 'TR14':
        L += A('0.2') / arb(1).exp()
    if name == 'PT15':
        L += A('0.2') / t
    return L, (derivedR if has78 else derivedR + A('0.875'))


def R1(*a):
    t0 = time.time()
    say('b687 R1 -- reading (i): the ζ instance by b685`s steps on T ≥ e ; routes sha256 %s' % shas())
    zg = BC.zeta_grid()
    e = TT('e')
    best, tried, refused = None, 0, 0
    for c in BC.PAR_C_Z:
        rmax = min((c - 0.5) ** 2 / (c - 1), c + 0.5)
        rs = [round(c + 0.02 + 0.02 * k, 3) for k in range(60) if c + 0.02 + 0.02 * k < rmax - 0.001]
        for r in rs:
            for eta in BC.PAR_ETA:
                pr = BC.params_z(zg, c, r, eta)
                tried += 1
                if not all(ok for _n, ok in BC.conditions_z(pr)):
                    refused += 1
                    continue
                I = BC.jensen(pr, BC.N_SEARCH, e)
                R = rz_at(pr, I, 'e', 'e')[0]
                if best is None or R.upper() < best[0].upper():
                    best = (R, c, r, eta)
    _R0, c, r, eta = best
    pr = BC.params_z(zg, c, r, eta)
    I = BC.jensen(pr, BC.N_FINAL, e)
    x0, d, y = A('0.25'), pr['delta'] / 2, e / 2
    cond = list(BC.conditions_z(pr)) + [('E_gamma at y = e/2: x0 ≥ d', bool(x0 >= d)), ('E_gamma at y = e/2: ((x0 + d)/y)² ≤ ½', bool(((x0 + d) / y) ** 2 <= A('0.5')))]
    a_e = (I[0] - 1) / (2 * pr['ell'])
    c_e = rz_at(pr, I, 1, 'e')[0]
    # ### the copy reproduces its source at the source's own T_MIN (the banked ζ instance at T = 100)
    zb = inst_z(1.5, 1.98, 0.5)
    chk = [(T, rz_at(zb['pr'], zb['I'], T, BC.T_MIN_Z)[0], BC.Rz(zb['pr'], zb['I'], T)[0]) for T in (100, 1000)]
    same = all(abs((x - y_).mid()) < arb('1e-50') and (x - y_).contains(0) for _T, x, y_ in chk)   # ### the midpoints equal; radii from the bank's balls
    a100, c100 = des(get('b685_count_part4.json')['a_zeta']), des(get('b685_count_part4.json')['c_zeta'])
    say('  tried %d sets, %d refused ; chosen c = %s, r = %s, η = %s' % (tried, refused, c, r, eta))
    for n_, ok in cond:
        say('  condition %-44s %s' % (n_, ok))
    say('  a_e = %s ; b_e = 0 ; c_e = %s   (T ≥ e)   beside a_ζ = %s, c_ζ = %s (T ≥ 100, b685)' % (bs(a_e), bs(c_e), bs(a100), bs(c100)))
    say('  the copy rz_at equals Rz at T_MIN 100 (T = 100, 1000): %s' % same)
    rows = []
    for T in HM:
        Re = rz_at(pr, I, T, 'e')[0]
        R100 = BC.Rz(zb['pr'], zb['I'], T)[0] if T != 'e' and float(T) >= 100 else None
        row = dict(T=str(T), Re=ser(Re), R100=ser(R100) if R100 is not None else None, bounds={})
        for nm in LOCATED:
            for tag, R in (('e', Re), ('100', R100)):
                if R is None:
                    continue
                v = located(nm, T, R)
                if v is None:
                    continue
                L, Rf = v
                row['bounds']['%s|%s' % (nm, tag)] = dict(located=ser(L), derived=ser(Rf), sharper=bool(Rf < L), not_sharper=bool(Rf >= L),
                                                        ratio=ser(Rf / L))
        rows.append(row)
        say('  T = %-5s R_e %s%s ; ' % (T, bs(Re, 8), (' ; R_100 %s' % bs(R100, 8)) if R100 is not None else '') + ' ; '.join(
            '%s %s/%s %s' % (k, bs(des(v['derived']), 6), bs(des(v['located']), 6), 'SHARPER' if v['sharper'] else 'NOT SHARPER' if v['not_sharper'] else 'UNDECIDED')
            for k, v in row['bounds'].items()))
    # ### the crossover heights (data/b687_rules.txt row (1)): the height beyond which each located bound stays below the derived one
    cross = {}
    for nm in LOCATED:
        for tag in ('e', '100'):
            def gap(u, nm=nm, tag=tag):
                T = math.exp(u)
                if tag == '100' and T < 100:
                    return None
                R = rz_at(pr, I, T, 'e')[0] if tag == 'e' else BC.Rz(zb['pr'], zb['I'], T)[0]
                v = located(nm, T, R)
                return None if v is None else float((v[1] - v[0]).mid())     # ### derived − located: > 0 where the located is the sharper
            lo_u = 1.0 if tag == 'e' else math.log(100)
            if LOCATED[nm][3] == 200:
                lo_u = max(lo_u, math.log(200))
            g0, gtop = gap(lo_u), gap(400.0)
            if g0 is None or gtop is None:
                continue
            if g0 > 0:
                cross['%s|%s' % (nm, tag)] = dict(T='from the range`s start', u=lo_u)
            elif gtop <= 0:
                cross['%s|%s' % (nm, tag)] = dict(T='beyond e^400', u=None)
            else:
                lo, hi = lo_u, 400.0
                for _ in range(80):
                    mid = (lo + hi) / 2
                    if gap(mid) > 0:
                        hi = mid
                    else:
                        lo = mid
                cross['%s|%s' % (nm, tag)] = dict(T='%.6g' % math.exp(hi), u=hi)
            say('  crossover %-14s the located bound below the derived beyond T = %s' % ('%s|%s' % (nm, tag), cross['%s|%s' % (nm, tag)]['T']))
    put('b687_readings_part1.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), shas=shas(), tried=tried, refused=refused, c=c, r=r, eta=eta,
                                         conditions=[[n_, ok] for n_, ok in cond], a_e=ser(a_e), c_e=ser(c_e), a100=ser(a100), c100=ser(c100),
                                         Ic=ser(I[0]), Ir=ser(I[1]), copy_equal=same, rows=rows, crossover=cross, seconds=int(time.time() - t0)))
    say('  %d s' % int(time.time() - t0))


# ================================================================================ R2: READING (ii), THE JENSEN DISC FOR ζ, AND C1
def zeta_zeros_near(T, R):
    """every ζ zero with |γ − T| ≤ R + 0.1 by acb.zeta_zero(n), the neighbours outside printed; each confirmed by the completed function's sign
    change across [mid − 1e-20, mid + 1e-20]: [(n, γ ball, the certified interval as a ball, signs)]."""
    ctx.prec = PREC
    import mpmath
    mpmath.mp.dps = 20
    n = max(1, int(mpmath.nzeros(T)))
    g_ = lambda k: acb.zeta_zero(k).imag   # noqa: E731
    while n > 1 and g_(n) > T - R - 0.1:
        n -= 1
    lo_n = n
    out, k = [], n + 1
    while True:
        gk = g_(k)
        if gk > T + R + 0.1:
            hi_n = k
            break
        if gk >= T - R - 0.1:
            m = gk.mid()
            a_, b_ = m - arb('1e-20'), m + arb('1e-20')
            sa, _ia, _la = B671.sign_at(B671.lam_z_at, arb(a_.mid()))
            sb, _ib, _lb = B671.sign_at(B671.lam_z_at, arb(b_.mid()))
            ctx.prec = PREC
            if not (sa and sb and sa == -sb):
                sys.exit('### ζ ZERO %d: NO CERTIFIED SIGN CHANGE ACROSS ITS BALL (%s, %s) -- STOPPED' % (k, sa, sb))
            out.append((k, gk, arb(m, arb('1e-20')), (sa, sb)))
        k += 1
    return out, (lo_n, float(g_(lo_n).mid())), (hi_n, float(g_(hi_n).mid()))


def disc_read(zeros, cre, T, rad_out, rads_in):
    """zeros: [(re ball, im ball)]: the inner counts at each inner radius and J = Σ log(r/|ρ − z₀|) over |ρ − z₀| < r; a zero whose comparison
    straddles a radius is UNDECIDED and stops the reading."""
    z0r, z0i = A(cre), TT(T)
    J, counts, inside = arb(0), dict((x, 0) for x in rads_in), []
    for re_, im_ in zeros:
        d2 = (re_ - z0r) ** 2 + (im_ - z0i) ** 2
        ro2 = A(rad_out) ** 2
        if not (d2 < ro2 or d2 > ro2):
            sys.exit('### A ZERO STRADDLES THE OUTER CIRCLE AT T = %s -- STOPPED (UNDECIDED)' % T)
        if d2 < ro2:
            J += (A(rad_out) / d2.sqrt()).log()
            inside.append([ser(re_), ser(im_), ser(d2.sqrt())])
        for x in rads_in:
            ri2 = A(x) ** 2
            if not (d2 < ri2 or d2 > ri2):
                sys.exit('### A ZERO STRADDLES THE INNER CIRCLE %s AT T = %s -- STOPPED (UNDECIDED)' % (x, T))
            if d2 < ri2:
                counts[x] += 1
    return J, counts, inside


def disc_rows(ins, zeros_at, heights, doubled=False):
    rows = []
    pr = ins['pr']
    c, r = ins['c'], ins['r']
    inner = '%.10g' % (c - 0.5)
    for T in heights:
        S, _I = S_at(ins, T)
        ell = pr['ell']
        zs = zeros_at(T)
        rin = (inner,) + tuple(x for x in RHO if float(x) < r and float(x) > c - 0.5)
        J, counts, inside = disc_read(zs, str(c), T, str(r), rin)
        bin_ = S / ell
        row = dict(T=T, S=ser(S), ell=ser(ell), J=ser(J), J_reading=sides(J, S)[0], J_margin=ser(S - J), inner=inner, n_inner=counts[inner],
                   inner_bound=ser(bin_), inner_reading=count_vs(counts[inner], bin_), inner_ratio=(ser(bin_ / counts[inner]) if counts[inner] else 'count 0'),
                   radii={}, inside=inside, zeros_listed=len(zs))
        for x in rin[1:]:
            b = S / (A(r) / A(x)).log()
            row['radii'][x] = dict(n=counts[x], bound=ser(b), reading=count_vs(counts[x], b), ratio=(ser(b / counts[x]) if counts[x] else 'count 0'))
        rows.append(row)
        say('  %s c %s r %s T %-6s : inner (radius %s) count %d against S/ℓ %s -> %s%s ; J %s against S %s -> %s ; radii %s' % (
            ins['kind'], c, r, T, inner, counts[inner], bs(bin_, 6), row['inner_reading'], ' (VACUOUS: every listed zero on σ = ½)' if ins['kind'] == 'ζ' else '',
            bs(J, 6), bs(S, 6), row['J_reading'], ' ; '.join('%s: %d ≤ %s %s' % (x, v['n'], bs(des(v['bound']), 5), v['reading']) for x, v in row['radii'].items())))
    return rows


def R2(*a):
    t0 = time.time()
    say('b687 R2 -- reading (ii): the Jensen disc for ζ at T = %s, the derivation`s parameters first ; C1 for ζ' % (HZ,))
    cache, out = {}, {}

    def zeros_at(Rmax):
        def f(T):
            if (T, Rmax) not in cache:
                z, lo, hi = zeta_zeros_near(T, Rmax)
                cache[(T, Rmax)] = (z, lo, hi)
                say('    ζ zeros listed near T = %s within %s: %d (n %d..%d ; the neighbours outside: γ_%d = %.6f, γ_%d = %.6f), each sign-checked' % (
                    T, Rmax + 0.1, len(z), z[0][0] if z else 0, z[-1][0] if z else 0, lo[0], lo[1], hi[0], hi[1]))
            return [(A('0.5'), iv) for _n, _g, iv, _s in cache[(T, Rmax)][0]]
        return f
    for tag, c, r, eta in ZSET:
        ins = inst_z(c, r, eta, banked=(tag == 'derivation'))
        cond = [[n_, ok] for n_, ok in BC.conditions_z(ins['pr'])]
        say('  the %s set c = %s, r = %s, η = %s ; conditions %s ; Ic %s Ir %s' % (tag, c, r, eta, cond, bs(ins['I'][0], 8), bs(ins['I'][1], 8)))
        rows = disc_rows(ins, zeros_at(2 * r), HZ)
        # ### C1: the planted disc -- the radius doubled, inner and outer (ℓ unchanged)
        ins2 = dict(ins, pr=BC.params_z(ins['grid'], c, 2 * r, eta), r=2 * r, c=c)
        ins2['pr']['ell'] = ins['pr']['ell']
        ins2['I'] = BC.jensen(ins2['pr'], BC.N_FINAL, TT(ins['Tmin']))
        cond2 = [[n_, ok] for n_, ok in BC.conditions_z(ins2['pr'])]
        c1 = []
        for T in HZ:
            S2, _ = S_at(ins2, T)
            inner2 = '%.10g' % (2 * (c - 0.5))
            _J, cnt2, _in = disc_read(zeros_at(2 * r)(T), str(c), T, str(2 * r), (inner2,))
            base = [x for x in rows if x['T'] == T][0]
            grow_b, grow_n = bool(S2 / ins['pr']['ell'] > des(base['inner_bound'])), cnt2[inner2] > base['n_inner']
            c1.append(dict(T=T, bound2=ser(S2 / ins['pr']['ell']), n2=cnt2[inner2], bound=base['inner_bound'], n=base['n_inner'], bound_grows=grow_b, count_grows=grow_n))
            say('    C1 %s T %-6s doubled: bound %s (was %s) GROWS %s ; inner count %d (was %d) GROWS %s' % (
                tag, T, bs(S2 / ins['pr']['ell'], 6), bs(des(base['inner_bound']), 6), grow_b, cnt2[inner2], base['n_inner'], grow_n))
        out[tag] = dict(c=c, r=r, eta=eta, conditions=cond, Ic=ser(ins['I'][0]), Ir=ser(ins['I'][1]), rows=rows, c1=c1, c1_conditions=cond2)
    zl = dict(('%s|%s' % k, dict(zeros=[[n, ser(g), ser(iv), list(s)] for n, g, iv, s in v[0]], lo=list(v[1]), hi=list(v[2]))) for k, v in cache.items())
    put('b687_readings_part2.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), shas=shas(), sets=out, zeros=zl, seconds=int(time.time() - t0)))
    say('  %d s' % int(time.time() - t0))


# ================================================================================ R3: THE BAND (150, 151.5] FOR Z_Q BY THE ARGUMENT PRINCIPLE
def _decided(x, y, h):
    """a square [x ± h] x [y ± h] decides every disc membership reading (iii) and C1 read at every Z_Q height: no radius straddled."""
    j2 = get('b685_count_part2.json')
    c, r = A(j2['c']), A(j2['r'])
    re_, im_ = x + arb(0, h.upper()), y + arb(0, h.upper())
    radii = [r, c - A('0.5'), 2 * (c - A('0.5'))] + [A(v) for v in RHO]
    for T in HQ:
        d2 = (re_ - c) ** 2 + (im_ - A(T)) ** 2
        for rho in radii:
            if not (d2 < rho ** 2 or d2 > rho ** 2):
                return False
    return True


def R3(*a):
    """resumable: the state in data/b687_readings_part3.json, each square banked as it lands; no new square started after B_START_BY s."""
    t0 = time.time()
    name = 'b687_readings_part3.json'
    stt = get(name) if os.path.exists(os.path.join(D, name)) else dict(squares={}, queue=[], zeros=[], complete=False)
    say('b687 R3 -- the band [%s, %s] x [%s, %s] by b667`s argument principle (b671`s carried square_count, %d segments a side), squares of side %s,'
        ' no edge on σ = ½ ; squares banked before this call %d of %d ; zero squares queued %d' % (
            BAND[0], BAND[1], B_EDGES_RE[0], B_EDGES_RE[-1], B671.SEGS_PER_SIDE, 2 * float(B_H), len(stt['squares']),
            (len(B_EDGES_RE) - 1) * (len(B_EDGES_IM) - 1), len(stt['queue'])))
    F = CERT.zq

    def save():
        stt.update(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), shas=shas(), band=list(BAND), leaf=B_LEAF,
                   count=sum(v['count'] for v in stt['squares'].values()))
        put(name, stt)
    for i in range(len(B_EDGES_RE) - 1):
        for j in range(len(B_EDGES_IM) - 1):
            key = '%d,%d' % (i, j)
            if key in stt['squares']:
                continue
            if time.time() - t0 > B_START_BY:
                say('  ### %d s: no new square started (the guard) -- resume with R3' % int(time.time() - t0))
                save()
                return
            ctx.prec = PREC
            cre = (A(B_EDGES_RE[i]) + A(B_EDGES_RE[i + 1])) / 2
            cim = (A(B_EDGES_IM[j]) + A(B_EDGES_IM[j + 1])) / 2
            t1 = time.time()
            att = stt.setdefault('attempts', {})
            if key in att or key in stt.setdefault('quarters', {}):
                # ### the square's attempt did not land in an earlier call: its four quarters, each banked as it lands
                qd = stt['quarters'].setdefault(key, {})
                q = A(B_H) / 2
                for dx in (-1, 1):
                    for dy in (-1, 1):
                        qk = '%+d%+d' % (dx, dy)
                        if qk in qd:
                            continue
                        if time.time() - t0 > B_START_BY:
                            say('  ### %d s: no new quarter started (the guard) -- resume with R3' % int(time.time() - t0))
                            save()
                            return
                        t2 = time.time()
                        m, cbq, stq = B671.square_count(F, cre + dx * q, cim + dy * q, q)
                        ctx.prec = PREC
                        if m is None:
                            save()
                            sys.exit('### QUARTER %s OF SQUARE %s UNRESOLVED %s -- STOPPED' % (qk, key, stq['unresolved']))
                        qd[qk] = dict(count=m, ball=ser(cbq), segments=stq['segments'], seconds=int(time.time() - t2))
                        if m:
                            stt['queue'].append([ser(cre + dx * q), ser(cim + dy * q), q.str(30, radius=False), m])
                        save()
                        say('  square %s quarter %s : count %d (%s ; segments %d ; %d s)' % (key, qk, m, bs(cbq, 6), stq['segments'], int(time.time() - t2)))
                n = sum(v['count'] for v in qd.values())
                cb, st = arb(n), dict(segments=sum(v['segments'] for v in qd.values()))
            else:
                att[key] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                save()
                n, cb, st = B671.square_count(F, cre, cim, B_H)
                ctx.prec = PREC
                if n is None:
                    save()
                    sys.exit('### SQUARE [%s, %s] x [%s, %s] UNRESOLVED %s -- STOPPED' % (B_EDGES_RE[i], B_EDGES_RE[i + 1], B_EDGES_IM[j], B_EDGES_IM[j + 1], st['unresolved']))
                if n:
                    stt['queue'].append([ser(cre), ser(cim), B_H, n])
            stt['squares'][key] = dict(re=[B_EDGES_RE[i], B_EDGES_RE[i + 1]], im=[B_EDGES_IM[j], B_EDGES_IM[j + 1]], count=n, ball=ser(cb),
                                       segments=st['segments'], seconds=int(time.time() - t1), by_quarters=key in stt.get('quarters', {}))
            save()
            say('  [%s, %s] x [%s, %s] : count %d (%s ; segments %d ; %d s) ; %d s' % (B_EDGES_RE[i], B_EDGES_RE[i + 1], B_EDGES_IM[j], B_EDGES_IM[j + 1], n,
                                                                                     bs(cb, 6), st['segments'], int(time.time() - t1), int(time.time() - t0)))
    # ### a square at count k > 0: quartered on the count (b671's (M-off) form) until every disc membership is decided, or to B_LEAF
    while stt['queue']:
        if time.time() - t0 > B_START_BY:
            say('  ### %d s: the quartering paused (the guard), %d squares queued -- resume with R3' % (int(time.time() - t0), len(stt['queue'])))
            save()
            return
        xs, ys, hs, k = stt['queue'][-1]
        x, y, hh = des(xs), des(ys), A(hs)
        if k == 1 and x - hh < A('0.5') and A('0.5') < x + hh:
            # ### b671's (M-on): the square at count 1 holds σ = ½; one certified sign change of Λ_Q(½ + it) across its t-range makes that zero the
            # ### square's one zero, on the line; bisected on the sign to half-width 1e-12. Not one sign change: the quartering below.
            ts = [y - hh + 2 * hh * arb(m_) / 64 for m_ in range(65)]
            sg = [B671.sign_at(B671.lam_q_at, arb(t_.mid()))[0] for t_ in ts]
            ctx.prec = PREC
            ch = [m_ for m_ in range(64) if sg[m_] and sg[m_ + 1] and sg[m_] == -sg[m_ + 1]]
            if None not in sg and len(ch) == 1:
                lo_, hi_, s_lo = ts[ch[0]].mid(), ts[ch[0] + 1].mid(), sg[ch[0]]
                while (hi_ - lo_) > arb('2e-12'):
                    md = (lo_ + hi_) / 2
                    s_md = B671.sign_at(B671.lam_q_at, arb(md.mid()))[0]
                    ctx.prec = PREC
                    if s_md is None:
                        break
                    if s_md == s_lo:
                        lo_ = md
                    else:
                        hi_ = md
                stt['queue'].pop()
                cy, ch_ = (lo_ + hi_) / 2, (hi_ - lo_) / 2
                stt['zeros'].append(dict(re=ser(A('0.5')), im=ser(cy), h=ser(arb(ch_.upper())), count=1, form='M-on: one sign change of Λ_Q on the line, '
                                         'the square`s count 1', square=[xs, ys, hs]))
                say('  a zero on the line by (M-on): ½ + i %s, half-width %s (the square`s count 1, one sign change in 64 steps) ; decided %s' % (
                    bs(cy, 14), arb(ch_.upper()).str(3), _decided(A('0.5'), cy, arb(ch_.upper()))))
                save()
                continue
            say('  the square at %s + i %s: sign changes on the line %d, unread signs %d -- quartered' % (bs(x, 6), bs(y, 8), len(ch), sg.count(None)))
        stt['queue'].pop()
        if k == 1 and (_decided(x, y, hh) or hh <= A(B_LEAF)):
            stt['zeros'].append(dict(re=ser(x), im=ser(y), h=ser(hh), count=k))
            say('  a zero: %s + i %s, half-width %s, its memberships decided %s' % (bs(x, 10), bs(y, 12), hh.str(4), _decided(x, y, hh)))
            save()
            continue
        q = hh / 2
        got, sub = 0, []
        for dx in (-1, 1):
            for dy in (-1, 1):
                xx, yy = x + dx * q, y + dy * q
                m, _cb2, _st2 = B671.square_count(F, xx, yy, q)
                ctx.prec = PREC
                if m is None:
                    save()
                    sys.exit('### A QUARTER AT %s %s h %s UNRESOLVED -- STOPPED' % (xx.str(12), yy.str(12), q.str(6)))
                if m:
                    sub.append([ser(xx), ser(yy), q.str(30, radius=False), m])
                    got += m
        if got != k:
            save()
            sys.exit('### THE QUARTERS COUNT %d, THE SQUARE %d -- STOPPED' % (got, k))
        stt['queue'] += sub
        save()
    stt['complete'] = True
    save()
    say('  THE BAND`S COUNT %d ; zeros located: %s ; COMPLETE ; %d s' % (stt['count'], [(bs(des(z['re']), 10), bs(des(z['im']), 12)) for z in stt['zeros']] or 'NONE',
                                                                     int(time.time() - t0)))


# ================================================================================ R4: READING (iii), THE JENSEN DISC FOR Z_Q, AND C1
def q_zeros():
    gz = os.path.join(D, 'b681_epstein_zeros_narrowed.json.gz')
    hs = io.open(os.path.join(D, 'b681_epstein_zeros_narrowed_hashes.txt'), encoding='utf-8').read()
    if sha(gz) not in hs or hashlib.sha256(gzip.open(gz).read()).hexdigest() not in hs:
        sys.exit('### b681`s BALLS DO NOT MATCH THEIR HASHES BANK -- STOPPED')
    j = json.load(gzip.open(gz))
    ctx.prec = PREC
    zs = []
    for r_ in j['rows']:
        h = arb(r_['h'])
        re_, im_ = arb(r_['re'], h), arb(r_['im'], h)
        zs.append((re_, im_, r_['kind']))
        if r_['kind'] == 'OFF':
            zs.append((1 - re_, im_, 'PARTNER'))
    b3 = get('b687_readings_part3.json')
    if not b3.get('complete'):
        sys.exit('### THE BAND (R3) IS NOT COMPLETE -- STOPPED')
    for z in b3['zeros']:
        zs.append((des(z['re']) + arb(0, des(z['h']).upper()), des(z['im']) + arb(0, des(z['h']).upper()), 'BAND'))
    return zs, j, b3


def R4(*a):
    t0 = time.time()
    zs, j, b3 = q_zeros()
    say('b687 R4 -- reading (iii): the Jensen disc for Z_Q at T = %s from b681`s %d balls (ON %d, OFF %d) with %d partners and the band`s %d zeros'
        ' (count %d, data/b687_readings_part3.json) ; C1 for Z_Q' % (HQ, len(j['rows']), sum(r['kind'] == 'ON' for r in j['rows']),
                                                                   sum(r['kind'] == 'OFF' for r in j['rows']), sum(1 for z in zs if z[2] == 'PARTNER'),
                                                                   len(b3['zeros']), b3['count']))
    ins = inst_q()
    za = lambda T: [(x, y) for x, y, _k in zs]   # noqa: E731
    rows = disc_rows(ins, za, HQ)
    for row in rows:
        say('    inside the outer disc at T %s: %s' % (row['T'], ['(%s, %s)' % (bs(des(x[0]), 8), bs(des(x[1]), 10)) for x in row['inside']]))
    ins2 = dict(ins, pr=BC.params_q(ins['grid'], ins['c'], 2 * ins['r'], ins['eta']), r=2 * ins['r'])
    ins2['pr']['ell'] = ins['pr']['ell']
    ins2['I'] = BC.jensen(ins2['pr'], BC.N_FINAL, TT(ins['Tmin']))
    cond2 = [[n_, ok] for n_, ok in BC.conditions_q(ins2['pr'])]
    c1 = []
    for T in HQ:
        S2, _ = S_at(ins2, T)
        inner2 = '%.10g' % (2 * (ins['c'] - 0.5))
        _J, cnt2, _in = disc_read(za(T), str(ins['c']), T, str(2 * ins['r']), (inner2,))
        base = [x for x in rows if x['T'] == T][0]
        gb, gn = bool(S2 / ins['pr']['ell'] > des(base['inner_bound'])), cnt2[inner2] > base['n_inner']
        c1.append(dict(T=T, bound2=ser(S2 / ins['pr']['ell']), n2=cnt2[inner2], bound=base['inner_bound'], n=base['n_inner'], bound_grows=gb, count_grows=gn))
        say('    C1 Z_Q T %-4s doubled: bound %s (was %s) GROWS %s ; inner count %d (was %d) GROWS %s' % (
            T, bs(S2 / ins['pr']['ell'], 6), bs(des(base['inner_bound']), 6), gb, cnt2[inner2], base['n_inner'], gn))
    put('b687_readings_part4.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), shas=shas(), c=ins['c'], r=ins['r'], eta=ins['eta'],
                                         rows=rows, c1=c1, c1_conditions=cond2, balls=len(zs), seconds=int(time.time() - t0)))
    say('  %d s' % int(time.time() - t0))


# ================================================================================ R5, R6: READING (iv), EVERY INTERMEDIATE INEQUALITY, AND C2
def steps(ins, heights, every):
    pr, kind = ins['pr'], ins['kind']
    c, r, eta, p = pr['c'], pr['r'], pr['eta'], pr['p']
    one, half = A(1), A('0.5')
    rows, c2 = [], []

    def row(step, T, bound, comp, where=''):
        v, m = sides(comp, bound)
        rows.append(dict(step=step, T=T, bound=ser(bound), computed=ser(comp), margin=ser(m), reading=v, where=where))
        return v, m
    for T in heights:
        t1 = time.time()
        Tm = T if T < ins['Tmin'] else ins['Tmin']
        Tb = TT(T)
        I = ins['I'] if T >= ins['Tmin'] else BC.jensen(pr, BC.N_FINAL, Tb)
        # ### (iv-1) the right edge
        v1 = Zval(kind, acb(pr['sigma1'].mid(), Tb))
        if not v1.real > 0:
            sys.exit('### Re Z(σ1 + iT) NOT POSITIVE AT T = %s -- STOPPED' % T)
        row('(iv-1) the right edge |arg Z(σ1 + iT)|', T, (pr['eps'] / 2).asin() if kind == 'Z_Q' else pr['logz1'], abs(v1.arg()))
        # ### (iv-2) the argument of Γ and of (s − 1), and Stirling's remainder
        if kind == 'Z_Q':
            x0, d, y = half, pr['delta'], Tb
        else:
            x0, d, y = A('0.25'), pr['delta'] / 2, Tb / 2
        G = lambda x: acb(x, y).lgamma().imag   # noqa: E731
        dpm = G(x0 + d) + G(x0 - d) - 2 * G(x0)
        Eg_stated = BC.E_gamma(x0, TT(Tm) if kind == 'Z_Q' else TT(Tm) / 2, d)
        row('(iv-2) the argument of Γ |Δ₊ + Δ₋|', T, Eg_stated, abs(dpm), 'E_gamma at the stated height %s' % Tm)
        planted = abs(G(x0 + d) - G(x0 - d))
        vp, mp = sides(planted, Eg_stated)
        c2.append(dict(T=T, planted=ser(planted), bound=ser(Eg_stated), reading=vp, fails=(vp == 'REFUTED')))
        da = acb(half + pr['delta'] - 1, Tb).arg() + acb(half - pr['delta'] - 1, Tb).arg() - 2 * acb(half - 1, Tb).arg()
        row('(iv-2) the argument of (s − 1) |Δ₊ + Δ₋|', T, BC.E_arg(pr['delta'], TT(Tm)), abs(da))
        if kind == 'Z_Q':
            Gt = acb(half, Tb).lgamma().imag
            row('(iv-2) Stirling: |Im log Γ(½ + iT) − (T log T − T)|', T, Tb / 2 * (1 + 1 / (4 * Tb ** 2)).log() + 1 / (6 * acb(half, Tb).abs_upper()),
                abs(Gt - (Tb * Tb.log() - Tb)))
        else:
            th = acb(A('0.25'), Tb / 2).lgamma().imag - Tb / 2 * arb.pi().log()
            eth = (1 / (16 * TT(Tm)) + 1 / (8 * TT(Tm)) + 1 / (3 * TT(Tm))) / arb.pi()
            row('(iv-2) Stirling: |θ(T)/π + 1 − (T/2π) log(T/2πe) − 7/8|', T, eth, abs(th / arb.pi() + 1 - Tb / (2 * arb.pi()) * (Tb / (2 * arb.pi() * one.exp())).log() - A('0.875')))
        # ### (iv-5) the centre
        z0 = acb(c, Tb)
        az0 = acb(c - 1, Tb).abs_lower() * Zval(kind, z0).abs_lower()
        lbound = Tb.log() + pr['low'].log()
        v5, m5 = sides(lbound, az0.log())
        rows.append(dict(step='(iv-5) the centre: log T + log L ≤ log|a(c + iT)|', T=T, bound=ser(az0.log()), computed=ser(lbound), margin=ser(m5), reading=v5, where=''))
        # ### (iv-3), (iv-4): the circle
        worst = {}
        for k in range(0, BC.N_FINAL, every):
            cf, rs, th_, forms = env_piece(pr, k, BC.N_FINAL, Tb)
            thm = arb(th_.mid())
            for sgn in (1, -1):
                s = acb(c + r * thm.cos(), Tb + sgn * r * thm.sin())
                Zs = Zval(kind, s)
                la_ball = (abs(s - 1) * abs(Zs)).log()
                if not la_ball.is_finite():
                    sys.exit('### log|a(s)| NOT FINITE AT θ %s, side %+d, T = %s -- STOPPED (UNDECIDED)' % (thm.str(6), sgn, T))
                env = cf * Tb.log() + rs
                for nm, b in (('(iv-4) the envelope: log|a(s)| ≤ coef(θ) log T + rest(θ, T) on the circle', env),):
                    v, m = sides(la_ball, b)
                    if nm not in worst or m.lower() < worst[nm][1].lower() or v != 'HOLDS':
                        worst[nm] = (v, m, b, la_ball, 'θ %s, side %+d' % (thm.str(6), sgn))
                sg = s.real
                if sg <= one + eta:
                    lam = (one + eta - sg) / (one + eta - p)
                    coef = one + lam * (pr['alpha1'] - one)
                    pl = lam * pr['logA'] + (one - lam) * pr['logB'] + coef * (pr['Q'] + s).abs_upper().log()
                    nm = '(iv-3) Phragmén-Lindelöf: log|a(s)| ≤ λ log A + (1 − λ) log B + coef log|Q + s| on [p, 1 + η]'
                    v, m = sides(la_ball, pl)
                    if nm not in worst or m.lower() < worst[nm][1].lower() or v != 'HOLDS':
                        worst[nm] = (v, m, pl, la_ball, 'θ %s, side %+d, σ %s' % (thm.str(6), sgn, sg.str(6)))
                else:
                    zb = BC.zq_up(ins['grid'], sg) if kind == 'Z_Q' else BC.zq_up(ins['grid'], sg if float(sg.lower()) <= 3.5 else A('3.5'))
                    nm = '(iv-4) |Z(s)| ≤ Z(σ) for σ ≥ 1 + η'
                    v, m = sides(abs(Zs), zb)
                    if nm not in worst or m.lower() < worst[nm][1].lower() or v != 'HOLDS':
                        worst[nm] = (v, m, zb, abs(Zs), 'θ %s, side %+d, σ %s' % (thm.str(6), sgn, sg.str(6)))
        for nm, (v, m, b, cmp_, where) in worst.items():
            rows.append(dict(step=nm, T=T, bound=ser(b), computed=ser(cmp_), margin=ser(m), reading=v, where='the narrowest of %d θ points x 2 sides: %s' % (
                BC.N_FINAL // every, where)))
        # ### (iv-3) its ends: σ = p by the functional equation, at τ = T + {−2, ..., 2}; and σ = 1 + η
        for tau in (-2, -1, 0, 1, 2):
            s = acb(p, Tb + tau)
            la = (s - 1).abs_upper().log() + Zval(kind, s).abs_upper().log()
            row('(iv-3) the end σ = p: log|a(s)| ≤ log A + α1 log|Q + s|', T, pr['logA'] + pr['alpha1'] * (pr['Q'] + s).abs_lower().log(), la, 'τ = T %+d' % tau)
            s = acb(one + eta, Tb + tau)
            la = (s - 1).abs_upper().log() + Zval(kind, s).abs_upper().log()
            row('(iv-3) the end σ = 1 + η: log|a(s)| ≤ log B + log|Q + s|', T, pr['logB'] + (pr['Q'] + s).abs_lower().log(), la, 'τ = T %+d' % tau)
        # ### (iv-6) the top edge
        st, cache = CERT._stats(), {}
        F = CERT.zq if kind == 'Z_Q' else CERT.zeta_f
        dtop = CERT.edge_arg(F, acb(pr['sigma1'].mid(), Tb), acb(half, Tb), 16, 24, st, cache)
        ctx.prec = PREC
        if dtop is None:
            sys.exit('### THE TOP EDGE AT T = %s UNRESOLVED %s -- STOPPED' % (T, st['unresolved']))
        if kind == 'Z_Q':
            top = topq_at(pr, I, T, Tm)[0]
        else:
            top = rz_at(pr, I, T, Tm)[2]
        row('(iv-6) the top edge: |Δ arg Z(σ + iT)|, σ1 -> ½, ≤ top(T)', T, top, abs(dtop), 'segments %d, unresolved %s' % (st['segments'], st['unresolved'] or 'NONE'))
        say('  %s T %-6s : %d rows ; C2 planted |Δ₊ − Δ₋| %s against E %s -> %s ; %d s' % (kind, T, sum(1 for x in rows if x['T'] == T), bs(planted, 6), bs(Eg_stated, 4),
                                                                                vp, int(time.time() - t1)))
    for x in rows:
        say('    %-9s T %-6s %-96s bound %s ; computed %s ; margin %s %s' % (x['reading'], x['T'], x['step'][:96], bs(des(x['bound']), 6), bs(des(x['computed']), 6),
                                                                       bs(des(x['margin']), 4), x['where'][:60]))
    return rows, c2


def R5(*a):
    t0 = time.time()
    ins = inst_z(1.5, 1.98, 0.5)
    say('b687 R5 -- reading (iv) for ζ at c = 1.5, r = 1.98, η = 0.5 (the derivation`s), T = %s, θ at all %d pieces ; C2 ; routes %s' % (HZ, BC.N_FINAL, shas()))
    rows, c2 = steps(ins, HZ, 1)
    put('b687_readings_part5.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), shas=shas(), rows=rows, c2=c2, seconds=int(time.time() - t0)))
    say('  %d s' % int(time.time() - t0))


def R6(*a):
    t0 = time.time()
    ins = inst_q()
    ok = all(abs((x - y).mid()) < arb('1e-50') and (x - y).contains(0) for x, y in
             ((topq_at(ins['pr'], ins['I'], T, BC.T_MIN)[0], BC.topq(ins['pr'], ins['I'], T)[0]) for T in (149, 1000)))
    say('b687 R6 -- reading (iv) for Z_Q at c = 1.7, r = 2.05, η = 0.2, T = %s, θ at every %dth piece ; C2 ; the copy topq_at equals topq at T_MIN 149: %s'
        % (HQ, NTH, ok))
    lat = []
    for sre, sim in (('2.4', '50'), ('2.45', '149'), ('2.5', '0')):
        ctx.prec = PREC
        s = acb(A(sre), A(sim))
        L_, B_ = zq_lattice(s), CERT.zq_point(s)
        ctx.prec = PREC
        lat.append(dict(s='%s + %si' % (sre, sim), lattice=[ser(L_.real), ser(L_.imag)], b667=[ser(B_.real), ser(B_.imag)], overlap=bool(L_.overlaps(B_))))
        say('  the lattice route against b667`s at %s + %si: lattice %s %s ; b667 %s %s ; OVERLAP %s' % (sre, sim, bs(L_.real, 10), bs(L_.imag, 10), bs(B_.real, 10),
                                                                                                   bs(B_.imag, 10), lat[-1]['overlap']))
    if not all(x['overlap'] for x in lat):
        sys.exit('### THE LATTICE ROUTE DISAGREES WITH b667`s -- STOPPED')
    rows, c2 = steps(ins, HQ, NTH)
    put('b687_readings_part6.json', dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), shas=shas(), copy_equal=ok, lattice_check=lat, lattice_n=LAT_N,
                                         rows=rows, c2=c2, seconds=int(time.time() - t0)))
    say('  %d s' % int(time.time() - t0))


# ================================================================================ R7: THE HYPOTHESES, THE BANKS AND THE COMPOSITION
def composition():
    """b685's (6) (data/b685_count_plan.txt :84-:90), run as tools/b685_count.py :394-:449 p3 runs it -- the lines copied with their gate on
    C1's second clause struck (data/b687_rules.txt row (1)) and their bank b687's: the window (149, 150), the scan on [150, 10⁶] by pieces of
    ratio 1.01 (W increasing, its value at a piece's end bounding the piece), the coefficient form beyond 10⁶."""
    grid, j, pr, I = BC.load_q()
    rows = []
    m149 = 10 * A(152).log() - 2
    rows.append(dict(range='t = 149 (certified)', bound='2', hcount=ser(10 * A(152).log()), margin=ser(m149)))
    kap = A(23).sqrt() / (2 * arb.pi())
    ctx.prec = PREC
    Wst = 2 + BC.W_window(pr, I, 150)
    mst = 10 * A(152).log() - Wst
    rows.append(dict(range='149 < t < 150 (straddle)', bound=ser(Wst), hcount=ser(10 * A(152).log()), margin=ser(mst)))
    narrow, ta, npieces, at = None, 150.0, 0, {}
    while ta < BC.SCAN_TOP:
        tb = min(ta * BC.SCAN_RATIO, BC.SCAN_TOP)
        Wb = BC.W_window(pr, I, tb)
        m = 10 * A(ta + 3).log() - Wb
        npieces += 1
        if narrow is None or m.lower() < narrow[0].lower():
            narrow = (m, ta, tb, Wb)
        for mark in (150, 1000, BC.SCAN_TOP):
            if ta <= mark <= tb and mark not in at:
                at[mark] = (ta, tb, Wb, m)
        ta = tb
    for mark in (150, 1000, BC.SCAN_TOP):
        ta_, tb_, Wb, m = at[mark]
        rows.append(dict(range='t in [%.6g, %.6g] (the piece holding %d)' % (ta_, tb_, mark), bound=ser(Wb), hcount=ser(10 * A(ta_ + 3).log()), margin=ser(m)))
    m, nta, ntb, nW = narrow
    Ic, Ir = I
    k1 = (1 + arb.pi() * (Ic - 1) / pr['ell']) / arb.pi()
    t6 = A(BC.SCAN_TOP)
    E = BC.topq(pr, I, BC.SCAN_TOP)[2]
    k0 = (kap.log() + A(11) / (24 * t6) + 2 * (pr['eps'] / 2).asin() + arb.pi() / pr['ell'] * (Ir - pr['low'].log()) + E
          + 2 * ((pr['sigma1'] - 1) / A(BC.T_MIN)).atan() + 2 * (1 / (2 * A(BC.T_MIN))).atan()) / arb.pi()
    mco = (10 - k1) * (t6 + 1).log() - k0
    rows.append(dict(range='t ≥ 10⁶ (coefficient form)', bound='κ1 log(t + 1) + κ0, κ1 %s, κ0 %s' % (bs(k1), bs(k0)), hcount='10 log(t + 3)', margin=ser(mco)))
    covered = bool(m149 > 0 and mst > 0 and m > 0 and mco > 0 and k1 < 10)
    return dict(rows=rows, narrowest=dict(margin=ser(m), ta=nta, tb=ntb, W=ser(nW)), pieces=npieces, k1=ser(k1), k0=ser(k0), covered=covered)


def R7(*a):
    t0 = time.time()
    P = dict((k, get('b687_readings_part%d.json' % k)) for k in range(1, 7))
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    p1, p2, p3, p4, p5, p6 = (P[k] for k in range(1, 7))
    V = lambda ok: 'HELD' if ok else 'REFUTED'   # noqa: E731
    # ### H2: the disc readings -- J(T) ≤ S(T) and the three radii, for ζ (both sets) and Z_Q; the literal inner count read beside
    disc = [(tag, row) for tag, st in p2['sets'].items() for row in st['rows']] + [('Z_Q', row) for row in p4['rows']]
    h2_rows = [(tag, row['T'], row['J_reading'], [v['reading'] for v in row['radii'].values()], row['inner_reading']) for tag, row in disc]
    h2 = all(j == 'HOLDS' and all(x == 'HOLDS' for x in rr) and inn == 'HOLDS' for _t, _T, j, rr, inn in h2_rows)
    h2_und = [x for x in h2_rows if 'UNDECIDED' in [x[2], x[4]] + x[3]]
    steps_rows = [('ζ', x) for x in p5['rows']] + [('Z_Q', x) for x in p6['rows']]
    h3 = all(x['reading'] == 'HOLDS' for _k, x in steps_rows)
    c1 = [(tag, x) for tag, st in p2['sets'].items() for x in st['c1']] + [('Z_Q', x) for x in p4['c1']]
    c2 = [('ζ', x) for x in p5['c2']] + [('Z_Q', x) for x in p6['c2']]
    h4 = all(x['bound_grows'] and x['count_grows'] for _t, x in c1) and all(x['fails'] for _k, x in c2)
    ex = p1['rows']
    sharper_every = dict((r['T'], all(v['sharper'] for k, v in r['bounds'].items() if k.endswith('|e'))) for r in ex)
    comp = composition() if (h2 and h3 and h4) else None
    h5 = (V(comp['covered']) if comp else 'NOT RUN')
    H = [('H1', 'HELD', 'the T ≥ e constants a_e = %s, b_e = 0, c_e = %s printed and compared at e, 10, 100 (and 1000, 10⁴) with HSW (9.3675; 9.4925), Trudgian 2014, '
          'Platt-Trudgian 2015 and Backlund (data/b687_matched.txt); sharper than every located bound at %s; the crossovers printed' % (
              bs(des(p1['a_e']), 6), bs(des(p1['c_e']), 6), ', '.join(T for T, v in sharper_every.items() if v) or 'no height')),
         ('H2', V(h2) if not h2_und else 'UNDECIDED', 'J(T) ≤ S(T) and n(ρ′) ≤ S(T)/log(r/ρ′) at ρ′ = 1.4, 1.6, 1.8 at every height, ζ at both sets and Z_Q: %d rows, %s ; '
          'the literal inner count at radius c − ½ beside it (VACUOUS for ζ)' % (len(h2_rows), 'every reading HOLDS' if h2 else 'NOT ALL HOLD')),
         ('H3', V(h3), '%d intermediate inequalities (ζ %d, Z_Q %d) at the sampled heights, each with its margin: %s' % (
             len(steps_rows), len(p5['rows']), len(p6['rows']), 'every one HOLDS' if h3 else '%d not holding' % sum(1 for _k, x in steps_rows if x['reading'] != 'HOLDS'))),
         ('H4', V(h4), 'C1: the doubled disc`s bound and count grow at every height (%d rows); C2: the planted Γ inequality fails at every height (%d rows)' % (len(c1), len(c2))),
         ('H5', h5, ('the composition (data/b687_composition.txt): narrowest margin %s on [%.6g, %.6g], κ1 %s, NO HEIGHT UNCOVERED %s' % (
             bs(des(comp['narrowest']['margin']), 6), comp['narrowest']['ta'], comp['narrowest']['tb'], bs(des(comp['k1']), 6), comp['covered'])) if comp else
          'H2, H3 and H4 not all held: the composition not run')]
    for h, v, why in H:
        say('  %s %s -- %s' % (h, v, why))
    n_ok = sum(1 for _k, x in steps_rows if x['reading'] == 'HOLDS')
    # ### the banks
    M = ['b687 -- READING (i): THE ζ INSTANCE AT MATCHED RANGE, T ≥ e, AGAINST THE LOCATED BOUNDS (%s)' % at, '',
         '### rows are heights with each bound`s value: the derived bound in each located bound`s own form (with 7/8 inside the modulus for Trudgian and',
         '### Platt-Trudgian, without it -- the derived R + 7/8 -- for HSW and Backlund), the located value, their ratio and the reading; every figure a ball.',
         '### The derivation: tools/b685_count.py`s steps imported unedited (sha256 %s), T_MIN_Z read as e by the copy rz_at (equal to Rz at b685`s T_MIN 100: %s).' % (
             p1['shas']['b685_count.py'], p1['copy_equal']), '',
         '== 1. THE CONSTANTS',
         '  T ≥ e : chosen c = %s, r = %s, η = %s of %d sets (%d refused) ; a_e = %s ; b_e = 0 ; c_e = %s' % (p1['c'], p1['r'], p1['eta'], p1['tried'], p1['refused'],
                                                                                                          bs(des(p1['a_e'])), bs(des(p1['c_e']))),
         '  T ≥ 100 (b685, data/b685_count_controls.txt :3) : a_ζ = %s ; b_ζ = 0 ; c_ζ = %s' % (bs(des(p1['a100'])), bs(des(p1['c100'])))]
    M += ['  condition %-46s %s' % (n_, ok) for n_, ok in p1['conditions']]
    M += ['', '== 2. THE LOCATED BOUNDS, AS QUOTED (relay data/b687_plan.txt section 1)'] + ['  %-9s %s' % (k, v[5]) for k, v in LOCATED.items()]
    M += ['  PT21 (arXiv:2004.09765v1, sha256 3362f66a...): NOT LOCATED AS NAMED -- no bound on N(T) or S(T) (data/b687_defects.txt (d))', '',
          '== 3. THE ROWS (derived | located | ratio | reading; |e the T ≥ e bound, |100 b685`s T ≥ 100 bound)']
    for r in ex:
        M.append('  T = %-5s R_e %s%s' % (r['T'], bs(des(r['Re']), 10), (' ; R_100 %s' % bs(des(r['R100']), 10)) if r['R100'] else ''))
        for k, v in r['bounds'].items():
            M.append('      %-13s derived %s | located %s | ratio %s | %s' % (k, bs(des(v['derived']), 8), bs(des(v['located']), 8), bs(des(v['ratio']), 6),
                                                                            'SHARPER' if v['sharper'] else 'NOT SHARPER' if v['not_sharper'] else 'UNDECIDED'))
        M.append('      SHARPER THAN EVERY LOCATED BOUND (the T ≥ e bound): %s' % sharper_every[r['T']])
    M += ['', '== 4. THE CROSSOVERS (data/b687_rules.txt row (1)): the height beyond which each located bound stays below the derived one']
    M += ['  %-13s T* = %s' % (k, v['T']) for k, v in p1['crossover'].items()]
    M += ['', '### ### **a_e = %s, b_e = 0, c_e = %s (T ≥ e) ; SHARPER THAN EVERY LOCATED BOUND AT e, 10, 100: %s ; THE NEAREST CROSSOVER %s (%s).**' % (
        bs(des(p1['a_e']), 6), bs(des(p1['c_e']), 6), all(sharper_every[x] for x in ('e', '10', '100')),
        min(((float(v['T']), k) for k, v in p1['crossover'].items() if v['T'][0].isdigit()), default=(0, '-'))[0],
        min(((float(v['T']), k) for k, v in p1['crossover'].items() if v['T'][0].isdigit()), default=(0, '-'))[1])]
    put_txt('b687_matched.txt', M)

    def disc_lines(rows, kind):
        L = []
        for row in rows:
            L.append('  T = %-6s | inner radius %s: certified count %d | the step`s bound S/ℓ %s | margin %s | ratio bound/count %s | %s%s' % (
                row['T'], row['inner'], row['n_inner'], bs(des(row['inner_bound']), 6), bs(des(row['inner_bound']) - row['n_inner'], 6),
                row['inner_ratio'] if isinstance(row['inner_ratio'], str) else bs(des(row['inner_ratio']), 4), row['inner_reading'],
                ' -- VACUOUS (every zero on σ = ½; the disc meets the line at one point)' if kind == 'ζ' else
                (' -- every zero in the outer disc on σ = ½ at this height (no off-line zero near it)' if all(abs(float(des(z[0]).mid()) - 0.5) < 1e-6 for z in row['inside']) else '')))
            L.append('             | the Jensen sum J(T) = Σ log(r/|ρ − z₀|) %s over %d zeros | the step`s bound S(T) %s | margin %s | ratio %s | %s' % (
                bs(des(row['J']), 8), len(row['inside']), bs(des(row['S']), 8), bs(des(row['J_margin']), 6), bs(des(row['S']) / des(row['J']), 4), row['J_reading']))
            for x, v in row['radii'].items():
                L.append('             | ρ′ = %s: count %d | bound S/log(r/ρ′) %s | ratio %s | %s' % (x, v['n'], bs(des(v['bound']), 6),
                                                                                           v['ratio'] if isinstance(v['ratio'], str) else bs(des(v['ratio']), 4), v['reading']))
        return L
    Zb = ['b687 -- READING (ii): THE JENSEN DISC OF THE DERIVATION FOR ζ (%s)' % at, '',
          '### rows are heights with the certified count, the step`s bound and the margin (and the ratio of bound to count, so a loose step reads as loose);',
          '### Jensen`s formula for a(s) = (s − 1)ζ(s) on the disc |s − (c + iT)| < r: J(T) = (1/2π)∫log|a| − log|a(z₀)| ≤ S(T) by steps (6)-(7), and n(ρ′)',
          '### log(r/ρ′) ≤ J(T). Zeros by acb.zeta_zero(n), each sign-checked by the completed function across [mid ± 1e-20] (b681`s C1 form).']
    for tag, st in p2['sets'].items():
        Zb += ['', '== %s SET: c = %s, r = %s, η = %s ; conditions %s ; (1/π)∫coef %s ; (1/π)∫rest %s%s' % (
            tag.upper(), st['c'], st['r'], st['eta'], st['conditions'], bs(des(st['Ic']), 8), bs(des(st['Ir']), 8),
            ' (THE BOUND UNDER TEST, b685`s banked integral)' if tag == 'derivation' else ' (the ruling`s figures, a second reading and not the test)')]
        Zb += disc_lines(st['rows'], 'ζ')
    Zb += ['', '== THE ZEROS READ (n | γ | the certified interval | signs at its ends)']
    for k, v in p2['zeros'].items():
        Zb.append('  near T|R = %s : %s ; outside neighbours %s, %s' % (k, ' ; '.join('%d %s' % (z[0], bs(des(z[1]), 14)) for z in v['zeros']), v['lo'], v['hi']))
    Zb += ['', '### ### **ζ: EVERY DISC READING %s (J(T) ≤ S(T) and the three radii at 100, 1000, 10⁴, both sets) ; THE INNER COUNT 0 AT EVERY HEIGHT -- VACUOUS.**' % (
        'HOLDS' if all(j == 'HOLDS' and all(x == 'HOLDS' for x in rr) for t, _T, j, rr, _i in h2_rows if t != 'Z_Q') else 'DOES NOT HOLD')]
    put_txt('b687_jensen_zeta.txt', Zb)
    Qb = ['b687 -- READING (iii): THE JENSEN DISC OF THE DERIVATION FOR Z_Q (%s)' % at, '',
          '### rows are heights with the certified count, the step`s bound and the margin (and the ratio); the zeros: b681`s 163 balls (h 1e-30) through',
          '### data/b681_epstein_zeros_narrowed_hashes.txt, the 17 partners 1 − conj ρ, and the band (150, 151.59] counted by b667`s argument principle',
          '### (data/b687_readings_part3.json: 12 squares, count %d, the zeros located on the line by (M-on): %s).' % (
              p3['count'], ', '.join('½ + i %s' % bs(des(z['im']), 12) for z in p3['zeros'])), '',
          '== c = %s, r = %s, η = %s (b685`s, data/b685_count.txt :8)' % (p4['c'], p4['r'], p4['eta'])]
    Qb += disc_lines(p4['rows'], 'Z_Q')
    Qb += ['', '== THE ZEROS IN THE OUTER DISC']
    Qb += ['  T = %s : %s' % (row['T'], ' ; '.join('%s + i %s (|ρ − z₀| %s)' % (bs(des(z[0]), 6), bs(des(z[1]), 12), bs(des(z[2]), 6)) for z in row['inside'])) for row in p4['rows']]
    Qb += ['', '### ### **Z_Q: EVERY DISC READING %s AT 50, 100, 149 (J(T) ≤ S(T), the three radii, the inner count).**' % (
        'HOLDS' if all(j == 'HOLDS' and all(x == 'HOLDS' for x in rr) and i == 'HOLDS' for t, _T, j, rr, i in h2_rows if t == 'Z_Q') else 'DOES NOT HOLD')]
    put_txt('b687_jensen_q0.txt', Qb)
    St = ['b687 -- READING (iv): EVERY INTERMEDIATE INEQUALITY OF STEPS (3), (5)-(7) AT THE SAMPLED HEIGHTS (%s)' % at, '',
          '### rows are steps with height, bound, computed value and margin, each a ball; ζ at c = 1.5, r = 1.98, η = 0.5 (the derivation`s), θ at all 2048',
          '### pieces; Z_Q at c = 1.7, r = 2.05, η = 0.2, θ at every 16th; a bound at a height below its T_MIN read at that height (the copies topq_at, rz_at).',
          '### Z_Q at σ > 2.5 by the lattice sum with its tail bound (zq_lattice; b667`s route covers |σ − ½| ≤ 2), checked against b667`s at three points',
          '### (data/b687_controls.txt).']
    for kind, x in steps_rows:
        St.append('  %-4s T %-6s %-104s | bound %s | computed %s | margin %s | %s%s' % (kind, x['T'], x['step'], bs(des(x['bound']), 8), bs(des(x['computed']), 8),
                                                                                  bs(des(x['margin']), 5), x['reading'], (' | ' + x['where']) if x['where'] else ''))
    St += ['', '### ### **%d OF %d INTERMEDIATE INEQUALITIES HOLD (ζ %d, Z_Q %d) ; NONE REFUTED%s.**' % (
        n_ok, len(steps_rows), len(p5['rows']), len(p6['rows']), '' if h3 else ' -- NOT SO: see the rows')]
    put_txt('b687_steps.txt', St)
    C = ['b687 -- THE CONTROLS OF (R297)(4) (%s): rows are controls with their expected and read values' % at, '']
    for tag, x in c1:
        C.append('  (C1) %-10s T = %-6s | expected: the doubled disc`s bound and inner count both grow | read: bound %s (was %s), count %d (was %d) -> %s' % (
            tag, x['T'], bs(des(x['bound2']), 6), bs(des(x['bound']), 6), x['n2'], x['n'], 'AS PLANTED' if x['bound_grows'] and x['count_grows'] else 'NOT AS PLANTED'))
    C.append('       the doubled circle lies outside the derivation`s conditions (the conditions at 2r: ζ %s ; Z_Q %s): its bound is the route`s value there' % (
        [st['c1_conditions'] for st in p2['sets'].values()], p4['c1_conditions']))
    for kind, x in c2:
        C.append('  (C2) %-4s T = %-6s | expected: |Δ₊ − Δ₋| of Im log Γ (Δ₋`s sign reversed) above E_gamma | read: %s against %s -> %s' % (
            kind, x['T'], bs(des(x['planted']), 6), bs(des(x['bound']), 6), 'FAILS AS PLANTED' if x['fails'] else 'NOT AS PLANTED'))
    for x in p6['lattice_check']:
        C.append('  (route) the lattice sum against b667`s at %s | expected: the balls overlap | read: lattice %s %s, b667 %s %s -> %s' % (
            x['s'], bs(des(x['lattice'][0]), 10), bs(des(x['lattice'][1]), 10), bs(des(x['b667'][0]), 10), bs(des(x['b667'][1]), 10), x['overlap']))
    C.append('  (copies) rz_at equals Rz at T_MIN 100: %s ; topq_at equals topq at T_MIN 149: %s' % (p1['copy_equal'], p6['copy_equal']))
    C += ['', '### ### **C1 %s ; C2 %s ; THE LATTICE ROUTE %s.**' % ('AS PLANTED' if all(x['bound_grows'] and x['count_grows'] for _t, x in c1) else 'NOT AS PLANTED',
                                                               'AS PLANTED' if all(x['fails'] for _k, x in c2) else 'NOT AS PLANTED',
                                                               'AGREES' if all(x['overlap'] for x in p6['lattice_check']) else 'DISAGREES')]
    put_txt('b687_controls.txt', C)
    if comp:
        Cm = ['b687 -- THE COMPOSITION OF b685`S (6), RUN ON H2, H3 AND H4 (data/b687_rules.txt row (1)) (%s)' % at, '',
              '### rows are T ranges -- the bound, HCount`s figure 10 log(|t| + 3), the margin; tools/b685_count.py :394-:449 p3`s lines with its gate on C1`s',
              '### second clause struck; W_window and topq imported unedited; b685`s constants from data/b685_count_part1/2.json, unchanged.', '']
        for r_ in comp['rows']:
            b = r_['bound'] if isinstance(r_['bound'], str) else bs(des(r_['bound']))
            hc = r_['hcount'] if isinstance(r_['hcount'], str) else bs(des(r_['hcount']))
            Cm.append('  %-46s | bound %s | HCount %s | margin %s' % (r_['range'], b, hc, bs(des(r_['margin']))))
        Cm += ['  the scan pieces %d ; THE NARROWEST MARGIN %s on [%.6g, %.6g] (W ≤ %s) ; negative t by the symmetry of data/b685_p3.txt section 3' % (
            comp['pieces'], bs(des(comp['narrowest']['margin'])), comp['narrowest']['ta'], comp['narrowest']['tb'], bs(des(comp['narrowest']['W']))),
               '  THE MEETING HEIGHT 149: the certified range −150 ≤ t ≤ 149 (data/b685_p3.txt section 4) and the derived t ≥ 149 ; NO HEIGHT UNCOVERED: %s' % comp['covered'],
               '', '### ### **HCOUNT`S INEQUALITY N(t, t + 1) ≤ 10 log(|t| + 3) AT EVERY t > 149: %s ; THE NARROWEST MARGIN %s.**' % (
                   comp['covered'], bs(des(comp['narrowest']['margin']), 6))]
        put_txt('b687_composition.txt', Cm)
    put('b687_readings.json', dict(at=at, hypotheses=[[h, v, w] for h, v, w in H], steps_hold=n_ok, steps=len(steps_rows), h2_rows=h2_rows, composition=comp,
                                   sharper_every=sharper_every, crossover=p1['crossover'], a_e=p1['a_e'], c_e=p1['c_e'], seconds=int(time.time() - t0)))
    say('### ### **H1 %s ; H2 %s ; H3 %s (%d of %d) ; H4 %s ; H5 %s ; %d s.**' % (H[0][1], H[1][1], H[2][1], n_ok, len(steps_rows), H[3][1], H[4][1], int(time.time() - t0)))


ROUTES = dict(R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b687_readings.py R1|R2|R3|R4|R5|R6|R7')
        sys.exit(2)
    fn(*sys.argv[2:])
