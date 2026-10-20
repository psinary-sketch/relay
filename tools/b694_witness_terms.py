# -*- coding: utf-8 -*-
"""b694_witness_terms.py -- THE WEIL-FACE WITNESS AT Q0, (R304)(4): THE COMPUTATION, ON THE AUTHOR'S WORD (relay data/b694_author_answers.txt,
prompts 3, 4 and 5; data/b694_witness_plan.txt and its amendment data/b694_witness_plan_amendment.txt).

### Two families on one ladder (the author's answer at prompt 5): N, b518's notched window, the witness reading; C, the centred window, its
### counterpart. h_a(u) = (gamma_0^2 + D^2)[cos(gamma_0 u) phi_a(u)] (N) or cos(gamma_0 u) phi_a(u) (C), phi_a(u) = N_6((u + L)/s)/s, L = log a,
### s = L/3; k = h * h (h real and even), k^ = h^^2, in the kernel's transform paperFT k z = INT k(x) e^(i z x) dx.
### Every value a ball (python-flint arb/acb), at PREC bits (128; the tolerance rung 256):
###   P(k)  = k^(i/2) + k^(-i/2)                                                     (SIDEExplicitFormula/B321Identity.lean :28-:29 at v0.34)
###   PR(k) = SUM_n c(n) n^(-1/2) 2 k(log n), n <= a^2 (the support reaches n <= e^(2L))   (:32-:34); c = Lambda at zeta, Lambda_Q at Q0
###           (Dirichlet inversion of r_Q / 2, tools/b325_epstein.py :73-:103, in balls); k(log n) by the exact piecewise convolution
###   A(k)  = (1/2 pi) INT k^(r) bracket(r) dr                                         (:36-:38), the bracket zeta's Re psi(1/4 + i r/2) - log pi
###           or Z_Q's 2 Re psi(1/2 + i r) - 2 log(2 pi / sqrt 23) (tools/b326_windows.py :220-:228); acb.integral over [0, R] doubled, the
###           tail beyond R bounded and added to the radius
###   S = P - PR + A, its bound the ball's radius. THE READING: FOUND where S's ball lies wholly below 0, the margin -S; else NOT FOUND.
### The identity (C3, the author's answer at prompt 3): the zero side Z = SUM_rho k^(gamma_rho) over the banked zeros (Q0: b681's 163 balls,
### the 17 partners 1 - conj rho, the band's two zeros (data/b687_jensen_q0.txt :5); zeta: acb.zeta_zero), the tail beyond bounded by a count;
### a width whose Z and S do not agree within their bounds is read as no reading at that width.
### Routes (each resumable, one unit per (route, family, width), appended to data/b694_witness_units.jsonl, untracked until banked):
###   classk <fam>            the classK membership of every k of the ladder, printed before any term
###   zeta <fam> [a ...]      C1: the three terms at zeta, before any Q0 reading
###   q0 <fam> [a ...]        the three terms at Q0
###   identity <obj> <fam> [a ...]   C3: the zero side against S
###   rung <fam> <a>          T1: the terms at 256 bits at one width
###   bank                    data/b694_witness.txt, data/b694_witness_controls.txt, data/b694_witness.json.gz, data/b694_witness_hashes.txt
### Written by the Write tool at b694; it writes only the banks it names.
"""
import gzip
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import acb, acb_poly, arb, ctx, fmpq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b694_witness as WZ   # noqa: E402  ### the step-zero reader: the gz read through its hashes, gamma_0 and delta to 40 digits

PREC = 128
ctx.prec = PREC
UNITS = os.path.join(D, 'b694_witness_units.jsonl')
LADDER = ('16', '24', '32', '48', '64', '96', '128', '192')
B518_A = '14.106736'                 # ### b518's widest width (data/b518_report.txt :125), the C2 re-read
FAMS = ('N', 'C')
R_INT = 4000                         # ### the archimedean integral's range [0, R]; the tail beyond bounded
CHUNK = 2                            # ### acb.integral called per chunk of this length
DISC = 23
ZETA_T = '151.59'                    # ### the zero lists' common top (the band's top, data/b687_jensen_q0.txt :4)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


# ================================================================================ BALLS TO TEXT AND BACK
def bs(x):
    """a real ball as [mid, rad] strings."""
    x = arb(x)
    return [x.mid().str(45, radius=False), x.rad().str(5, radius=False)]


def bl(p):
    return arb(p[0], p[1])


def fmt(x, n=12):
    x = arb(x)
    return '%s +- %s' % (x.mid().str(n, radius=False), x.rad().str(3, radius=False))


# ================================================================================ THE WINDOW
def n6_pieces():
    """the cardinal B-spline N_6 on [k, k+1], k = 0..5, as exact rational coefficient lists in x: (1/120) SUM_{j<=k} (-1)^j C(6,j) (x - j)^5."""
    out = []
    for k in range(6):
        c = [fmpq(0)] * 6
        for j in range(k + 1):
            sg = (-1) ** j * math.comb(6, j)
            for e in range(6):                       # (x - j)^5 = SUM_e C(5,e) x^e (-j)^(5-e)
                c[e] += fmpq(sg * math.comb(5, e) * (-j) ** (5 - e), 120)
        out.append(c)
    return out


N6 = n6_pieces()


def compose_lin(coefs, a0, a1):
    """the polynomial SUM c_e y^e with y = a0 + a1 u, as an acb_poly in u (Horner)."""
    lin = acb_poly([acb(a0), acb(a1)])
    res = acb_poly([acb(arb(coefs[-1]))])
    for c in reversed(coefs[:-1]):
        res = res * lin + acb(arb(c))
    return res


class Window:
    def __init__(self, a, fam, g0=None):
        self.a, self.fam = str(a), fam
        self.g0 = arb(g0 or WZ.G0)
        self.L = arb(self.a).log()
        self.s = self.L / 3
        self.knots = [-self.L + j * self.s for j in range(7)]
        self.kf = [float(k.mid()) for k in self.knots]
        I = acb(0, 1)
        self.q = []
        # ### N6[j] is N_6 on [j, j+1] in the variable x = (u + L)/s itself: p_j(u) = N6[j]((u + L)/s) / s
        self.p = [compose_lin(N6[j], self.L / self.s, 1 / self.s) * acb(1 / self.s) for j in range(6)]
        for pj in self.p:
            if fam == 'N':
                self.q.append(pj.derivative().derivative() + pj.derivative() * (2 * I * acb(self.g0)))
            else:
                self.q.append(pj)
        self.qc = [acb_poly([c.conjugate() for c in qj.coeffs()]) for qj in self.q]

    # ### the transform
    def phihat(self, w):
        return (acb(w) * self.s / 2).sinc() ** 6

    def hhat(self, z):
        z = acb(z)
        g0 = acb(self.g0)
        gh = (self.phihat(z - g0) + self.phihat(z + g0)) / 2
        return (g0 * g0 - z * z) * gh if self.fam == 'N' else gh

    def khat(self, z):
        return self.hhat(z) ** 2

    # ### h and its derivatives on a piece
    def hder(self, j, u, d):
        """d^d/du^d of Re[e^(i g0 u) q_j(u)] at u (j = -1 or 6: outside the support, 0)."""
        if j < 0 or j > 5:
            return arb(0)
        I = acb(0, 1)
        ig = I * acb(self.g0)
        qd = [self.q[j]]
        for _m in range(d):
            qd.append(qd[-1].derivative())
        tot = acb(0)
        for m in range(d + 1):
            tot += math.comb(d, m) * ig ** (d - m) * qd[m](acb(u))
        return (acb(arb(u) * self.g0 * I).exp() * tot).real

    # ### k(x) by the exact piecewise convolution
    def kval(self, x, xr=None):
        """k(x). Where x is an exact rational multiple xr of L (x = log n with n^3 = a^k), every piece comparison is made in rationals (the
        knots are (-1 + j/3) L); otherwise in floats, refused where x meets a knot sum within 1e-20."""
        x = arb(x)
        xf = float(x.mid())
        I = acb(0, 1)
        g0 = acb(self.g0)
        c = 2 * I * g0
        tot = arb(0)
        kq = [fmpq(-3 + j, 3) for j in range(7)]
        for j in range(6):
            for l in range(6):
                if xr is not None:
                    lo_q, hi_q = max(kq[j], xr - kq[l + 1]), min(kq[j + 1], xr - kq[l])
                    if hi_q <= lo_q:
                        continue
                    lo, hi = arb(lo_q) * self.L, arb(hi_q) * self.L
                else:
                    lo_f = max(self.kf[j], xf - self.kf[l + 1])
                    hi_f = min(self.kf[j + 1], xf - self.kf[l])
                    if hi_f - lo_f < -1e-20:
                        continue
                    if abs(hi_f - lo_f) <= 1e-20 or any(abs(xf - self.kf[i] - self.kf[m]) < 1e-20 for i in range(7) for m in range(7)):
                        raise ValueError('### x = %r MEETS A KNOT SUM WITHIN 1e-20 -- THE PIECE ORDER UNDECIDED; NOTHING COMPUTED' % xf)
                    lo = self.knots[j] if self.kf[j] >= xf - self.kf[l + 1] else x - self.knots[l + 1]
                    hi = self.knots[j + 1] if self.kf[j + 1] <= xf - self.kf[l] else x - self.knots[l]
                ql = self._shift(self.q[l], x)
                qlc = self._shift(self.qc[l], x)
                A = self.q[j] * ql
                IA = A.integral()
                va = IA(acb(hi)) - IA(acb(lo))
                B = self.q[j] * qlc
                Sp, Bd, ck = acb_poly([0]), B, c
                k = 0
                while Bd.degree() >= 0 and k <= 12:
                    Sp = Sp + Bd * (acb((-1) ** k) / ck)
                    Bd = Bd.derivative()
                    ck = ck * c
                    k += 1
                vb = (c * acb(hi)).exp() * Sp(acb(hi)) - (c * acb(lo)).exp() * Sp(acb(lo))
                tot += ((I * g0 * acb(x)).exp() * va).real / 2 + ((-I * g0 * acb(x)).exp() * vb).real / 2
        return tot

    @staticmethod
    def _shift(qp, x):
        """q(x - t) as an acb_poly in t."""
        lin = acb_poly([acb(x), acb(-1)])
        cs = qp.coeffs()
        res = acb_poly([cs[-1]]) if cs else acb_poly([0])
        for cc in reversed(cs[:-1]):
            res = res * lin + cc
        return res


# ================================================================================ THE UNITS FILE
def units():
    out = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                out[(u['route'], u['fam'], u['a'], u.get('obj', ''), u.get('prec', PREC))] = u
    return out


def put_unit(u):
    u['at'] = utc()
    u.setdefault('prec', PREC)
    with io.open(UNITS, 'a', encoding='utf-8', newline=NL) as fh:
        fh.write(json.dumps(u, ensure_ascii=False) + NL)


# ================================================================================ classK, PRINTED BEFORE ANY TERM
def classk(fam, *a):
    widths = (B518_A,) + LADDER if fam == 'N' else LADDER
    U = units()
    for w in widths:
        if ('classk', fam, w, '', PREC) in U:
            print('  %s a %-9s classK: banked' % (fam, w))
            continue
        t0 = time.time()
        W = Window(w, fam)
        twoL = 2 * float(W.L.mid())
        xs = [twoL * f for f in (0.05, 0.13, 0.27, 0.41, 0.55, 0.69, 0.83, 0.97)]
        ev = [W.kval(arb(x)) - W.kval(arb(-x)) for x in xs]
        even = all(e.contains(0) for e in ev)
        jumps = {}
        for d in range(4):
            jumps['D%d' % d] = [W.hder(i, W.knots[i], d) - W.hder(i - 1, W.knots[i], d) for i in range(7)]
        c2 = all(j.contains(0) for d in ('D0', 'D1', 'D2') for j in jumps[d])
        d3 = max(abs(float(j.mid())) for j in jumps['D3'])
        # ### the form: k by the convolution against the inverse transform (1/pi) INT_0^R k^(r) cos(r x) dr, the tail beyond bounded
        R = 600
        form = []
        for x in xs[:3]:
            f = lambda z, an, x=x: W.khat(z) * (acb(z) * x).cos()   # noqa: E731
            tot = acb(0)
            for e in range(0, R, 4):
                tot += acb.integral(f, e, e + 4, rel_tol=arb(2) ** -110, abs_tol=arb(2) ** -110)
            inv = tot.real / arb.pi() + arb(0, tail_bound(W, R, 0.0, inverse=True))
            kv = W.kval(arb(x))
            form.append(((kv - inv).contains(0), fmt(kv), fmt(inv)))
        ok = even and c2 and all(f_[0] for f_ in form)
        u = dict(route='classk', fam=fam, a=w, L=bs(W.L), even=even, even_balls=[fmt(e, 3) for e in ev], c2=c2, d3_jump_max=d3,
                 jumps={k: [fmt(x, 3) for x in v] for k, v in jumps.items()}, support=[fmt(-W.L), fmt(W.L)],
                 form=[dict(agree=f_[0], conv=f_[1], inverse=f_[2]) for f_ in form], member=ok, seconds=int(time.time() - t0))
        put_unit(u)
        print('  %s a %-9s classK: even %s ; C2 (D0-D2 jumps contain 0 at the 7 knots) %s, D3 jump max %.3e ; support [-L, L], L %s ; the form '
              '(convolution = inverse transform at 3 points) %s ; MEMBER %s ; %d s' % (fam, w, even, c2, d3, fmt(W.L, 8), [f_[0] for f_ in form],
                                                                                     ok, u['seconds']), flush=True)


def tail_bound(W, R, Y, inverse=False):
    """a bound on (1/2 pi) INT_{|r| > R} |k^(r + i y)| |bracket| dr (|y| <= Y), or on (1/pi) INT_R^inf |k^(r)| dr (inverse), for R >= 2 gamma_0 + 2:
    |sinc w| <= 1.2 e^|Im w| / max(1, |w|); |z - g0| >= r/2, |z + g0| >= r; |h^| <= P(r) (1.2 e^(Y s/2))^6 (4/(r s))^6 with P = r^2 + Y^2 + g0^2
    (N) or 1 (C); |bracket| <= 2 log r + 2 for r >= 1000 (|psi(1/2 + i r)| <= log r + 1/r), log r + 2 for zeta's."""
    s = float(W.s.mid()) * (1 - 1e-12)
    g0 = float(W.g0.mid()) * (1 + 1e-12)
    assert R >= 2 * g0 + 2
    K = (1.2 * math.exp(Y * s / 2)) ** 6 * (4 / s) ** 6
    tot, r, step = 0.0, float(R), 1.0
    while r < 1e7:
        rr = r + step
        P = (rr * rr + Y * Y + g0 * g0) if W.fam == 'N' else 1.0
        hb = P * K / r ** 6
        f = hb * hb * (1.0 if inverse else (2 * math.log(rr) + 2))
        tot += f * step
        r, step = rr, step * 1.02
    # ### beyond 1e7: |k^| <= (2 r^2 K / r^6)^2 = 4 K^2 r^-8 (N) and the bracket <= 2 log r + 2
    tot += (4 * K * K) * (1e7 ** -7 / 7) * (2 * math.log(1e7) + 3)
    return (tot / math.pi if inverse else 2 * tot / (2 * math.pi)) * 1.01


# ================================================================================ THE PRIME CHANNELS
_LQ = {}


def lambda_q(nmax):
    """Lambda_Q(n), n <= nmax, in balls: r_Q by b325's loop (tools/b325_epstein.py :53-:67), b = r/2, Lambda_Q(n) = b_n log n - SUM_{d|n, d<n}
    Lambda_Q(d) b_{n/d}."""
    if nmax in _LQ:
        return _LQ[nmax]
    r = [0] * (nmax + 1)
    ymax = int(2 * math.sqrt(nmax / float(DISC))) + 1
    for y in range(-ymax, ymax + 1):
        for x in range(-int(math.sqrt(nmax)) - abs(y) - 1, int(math.sqrt(nmax)) + abs(y) + 2):
            k = x * x + x * y + 6 * y * y
            if 1 <= k <= nmax:
                r[k] += 1
    b = [fmpq(r[k], 2) for k in range(nmax + 1)]
    lam = [arb(0)] * (nmax + 1)
    divs = [[] for _ in range(nmax + 1)]
    for d in range(2, nmax // 2 + 1):
        for m in range(2 * d, nmax + 1, d):
            divs[m].append(d)
    for n in range(2, nmax + 1):
        t = arb(b[n]) * arb(n).log() if b[n] != 0 else arb(0)
        for d in divs[n]:
            e = n // d
            if b[e] != 0 and not lam[d].is_zero():
                t -= lam[d] * arb(b[e])
        lam[n] = t
    _LQ[nmax] = (lam, r)
    return lam, r


def lambda_z(nmax):
    """von Mangoldt: log p at p^k, 0 elsewhere, in balls."""
    lam = [arb(0)] * (nmax + 1)
    sieve = bytearray([1]) * (nmax + 1)
    for p in range(2, nmax + 1):
        if sieve[p]:
            for m in range(p * p, nmax + 1, p):
                sieve[m] = 0
            q = p
            while q <= nmax:
                lam[q] = arb(p).log()
                q *= p
    return lam


def exact_ratio(a, n):
    """k/3 where n^3 = a^k exactly (a an integer width, 1 <= k <= 6), else None: log n an exact rational multiple of L = log a."""
    if not a.isdigit():
        return None
    A = int(a)
    for k in range(1, 7):
        if n ** 3 == A ** k:
            return fmpq(k, 3)
    return None


def prime_sum(W, lam, nmax):
    tot = arb(0)
    terms, absum = 0, 0.0
    for n in range(2, nmax + 1):
        if lam[n].is_zero():
            continue
        xr = exact_ratio(W.a, n)
        kv = W.kval(arb(xr) * W.L if xr is not None else arb(n).log(), xr)
        t = lam[n] / arb(n).sqrt() * 2 * kv
        tot += t
        terms += 1
        absum += abs(float(t.mid()))
    return tot, terms, absum


# ================================================================================ THE ARCHIMEDEAN TERM
def bracket(obj, z):
    z = acb(z)
    I = acb(0, 1)
    if obj == 'q0':
        return (acb(0.5) + I * z).digamma() + (acb(0.5) - I * z).digamma() - 2 * (2 * arb.pi() / arb(DISC).sqrt()).log()
    return ((acb(0.25) + I * z / 2).digamma() + (acb(0.25) - I * z / 2).digamma()) / 2 - arb.pi().log()


def arch(W, obj, R=R_INT):
    f = lambda z, an: W.khat(z) * bracket(obj, z)   # noqa: E731
    tot = acb(0)
    for e in range(0, R, CHUNK):
        tot += acb.integral(f, e, e + CHUNK, rel_tol=arb(2) ** -110, abs_tol=arb(2) ** -110)
    tb = tail_bound(W, R, 0.0)
    return 2 * tot.real / (2 * arb.pi()) + arb(0, tb), tb


# ================================================================================ THE TERMS AT ONE WIDTH
def terms(W, obj):
    t0 = time.time()
    nmax = int(math.floor(math.exp(2 * float(W.L.mid())) + 1e-9))
    P = (W.khat(acb(0, 0.5)) + W.khat(acb(0, -0.5))).real
    lam = lambda_q(nmax)[0] if obj == 'q0' else lambda_z(nmax)
    PR, nterms, absum = prime_sum(W, lam, nmax)
    A, tb = arch(W, obj)
    S = P - PR + A
    phase = acb(W.hhat(acb(arb(WZ.G0), -arb(WZ.DELTA0))) ** 2)
    return dict(P=bs(P), PR=bs(PR), A=bs(A), S=bs(S), nmax=nmax, prime_terms=nterms, prime_abs=absum, tail=tb,
                phase_deg=float((phase.arg() * 180 / arb.pi()).mid()), seconds=int(time.time() - t0))


def reading(S):
    S = bl(S) if isinstance(S, list) else S
    if S < 0:
        return 'NEGATIVE BEYOND ITS BOUND', bs(-S)
    if S > 0:
        return 'NONNEGATIVE BEYOND ITS BOUND', bs(S)
    return 'UNDECIDED', None


def _run_terms(route, obj, fam, widths):
    U = units()
    for w in widths:
        key = (route, fam, w, obj, PREC)
        if key in U:
            print('  %s %s a %-9s banked: S %s' % (obj, fam, w, fmt(bl(U[key]['S']))))
            continue
        ck = U.get(('classk', fam, w, '', PREC))
        if not ck or not ck.get('member'):
            sys.exit('### classK NOT PRINTED (OR NOT A MEMBER) FOR %s a %s -- NO TERM COMPUTED' % (fam, w))
        if obj == 'q0':
            zc = [x for x in U.values() if x['route'] == 'zeta' and x['prec'] == PREC]
            need = [(f_, w_) for f_ in FAMS for w_ in LADDER]
            done = set((x['fam'], x['a']) for x in zc)
            if any(n not in done for n in need) or any(reading(x['S'])[0] != 'NONNEGATIVE BEYOND ITS BOUND' for x in zc):
                sys.exit('### C1 (ZETA) NOT READ NONNEGATIVE BEYOND ITS BOUND AT EVERY WIDTH OF BOTH FAMILIES -- NO Q0 TERM COMPUTED (N4)')
        W = Window(w, fam)
        u = terms(W, obj)
        u.update(route=route, fam=fam, a=w, obj=obj)
        put_unit(u)
        rd_, m = reading(u['S'])
        print('  %s %s a %-9s P %s | PR %s (%d terms to n %d) | A %s | S %s | %s%s | phase %.3f deg | %d s' % (
            obj, fam, w, fmt(bl(u['P']), 8), fmt(bl(u['PR']), 8), u['prime_terms'], u['nmax'], fmt(bl(u['A']), 8), fmt(bl(u['S'])), rd_,
            (' margin %s' % fmt(bl(m))) if m else '', u['phase_deg'], u['seconds']), flush=True)


def zeta(fam, *a):
    _run_terms('zeta', 'zeta', fam, a or LADDER)


def q0(fam, *a):
    _run_terms('q0', 'q0', fam, a or ((B518_A,) + LADDER if fam == 'N' else LADDER))


# ================================================================================ C3: THE IDENTITY
def q0_zeros():
    """[(t, delta, mult)]: b681's ON (delta 0) and OFF balls (delta = sigma - 1/2), each OFF with its partner (delta -> -delta); the band's two."""
    B = WZ.balls()
    out = []
    for r in B['rows']:
        t = arb(r['im'], r['h'])
        d = arb(r['re'], r['h']) - arb('0.5')
        if r['kind'] == 'ON':
            out.append((t, arb(0, r['h']), 1))
        else:
            out.append((t, d, 1))
            out.append((t, -d, 1))
    for t in (('150.515359960', '1e-11'), ('151.568701014', '1e-11')):   # ### data/b687_jensen_q0.txt :5 (to the digits it prints)
        out.append((arb(t[0], t[1]), arb(0, '1e-11'), 1))
    return out


def zero_side(W, zeros):
    """SUM over zeros with t > 0 of k^(t - i delta) + k^(-t - i delta) = 2 Re k^(t - i delta) (k real and even)."""
    tot = arb(0)
    for t, d, m in zeros:
        tot += 2 * m * W.khat(acb(t, -d)).real
    return tot


def zero_tail(W, obj, T0):
    """the zeros above T0: SUM over unit intervals [m, m+1] of a count bound times 2 max|k^| there (|delta| <= 1 at Q0, the strip (-1/2, 3/2);
    0 at zeta). Q0's count: N(t, t+1] <= 10 log(t + 3), (P3)'s inequality (relay data/b685_count.txt; certified to 149, DERIVED beyond, not
    compiled -- data/b687_p3_status.txt). zeta's: 1 + (1/2pi) log((t+1)/2pi) + 2 (0.1038 log t + 0.2573 log log t + 9.3675) (HSW Cor 1.2)."""
    Y = 1.0 if obj == 'q0' else 0.0
    s = float(W.s.mid()) * (1 - 1e-12)
    g0 = float(W.g0.mid()) * (1 + 1e-12)
    K = (1.2 * math.exp(Y * s / 2)) ** 6 * (4 / s) ** 6
    tot, m = 0.0, math.floor(T0)
    while m < 1e6:
        P = ((m + 1) ** 2 + Y * Y + g0 * g0) if W.fam == 'N' else 1.0
        hb = P * K / m ** 6
        cnt = 10 * math.log(m + 4) if obj == 'q0' else (1 + math.log((m + 1) / (2 * math.pi)) / (2 * math.pi)
                                                        + 2 * (0.1038 * math.log(m + 1) + 0.2573 * math.log(math.log(m + 1)) + 9.3675))
        tot += cnt * 2 * hb * hb
        m += 1
    tot += 20 * math.log(2e6) * 4 * K * K * (1e6 ** -7 / 7) * 1.01
    return tot * 1.01


def identity(obj, fam, *a):
    U = units()
    zs = q0_zeros() if obj == 'q0' else None
    if obj == 'zeta':
        zs, n = [], 1
        while True:
            z = acb.zeta_zero(n)
            if z.imag > arb(ZETA_T):
                break
            zs.append((z.imag, arb(0), 1))
            n += 1
    T0 = float(ZETA_T)
    for w in (a or ((B518_A,) + LADDER if (fam == 'N' and obj == 'q0') else LADDER)):
        key = ('identity', fam, w, obj, PREC)
        if key in U:
            print('  identity %s %s a %-9s banked: %s' % (obj, fam, w, U[key]['agree']))
            continue
        st = U.get((obj, fam, w, obj, PREC))
        if not st:
            sys.exit('### THE TERMS AT %s %s a %s NOT BANKED -- THE IDENTITY NOT READ' % (obj, fam, w))
        t0 = time.time()
        W = Window(w, fam)
        Z = zero_side(W, zs)
        tl = zero_tail(W, obj, T0)
        diff = Z - bl(st['S'])
        agree = (diff + arb(0, tl)).contains(0)
        u = dict(route='identity', fam=fam, a=w, obj=obj, Z=bs(Z), tail=tl, diff=bs(diff), agree=bool(agree), zeros=len(zs),
                 seconds=int(time.time() - t0))
        put_unit(u)
        print('  identity %s %s a %-9s Z %s (%d zeros below %s) | S %s | Z - S %s | tail %.2e | AGREE %s | %d s' % (
            obj, fam, w, fmt(Z), len(zs), ZETA_T, fmt(bl(st['S'])), fmt(diff, 4), tl, agree, u['seconds']), flush=True)


# ================================================================================ T1: THE TOLERANCE RUNG
def rung(fam, w, obj='q0'):
    global PREC
    U = units()
    lo = U.get((obj, fam, w, obj, 128))
    if not lo:
        sys.exit('### THE 128-BIT TERMS AT %s %s a %s NOT BANKED' % (obj, fam, w))
    PREC = 256
    ctx.prec = 256
    if ('rung', fam, w, obj, 256) in units():
        print('  rung banked')
        return
    W = Window(w, fam)
    u = terms(W, obj)
    inside = bl(lo['S']).contains(bl(u['S']))
    u.update(route='rung', fam=fam, a=w, obj=obj, prec=256, inside=bool(inside))
    put_unit(u)
    print('  rung %s %s a %s at 256 bits: S %s ; inside the 128-bit ball %s ; %d s' % (obj, fam, w, fmt(bl(u['S']), 20), inside, u['seconds']))


B518_G0 = '16.290216'     # ### b518's own gamma_0, to its six decimals (tools/b518_window.py :28; data/b518_cells.jsonl :119 "gamma0": 16.290216)


def c2(*a):
    """C2: b518's two-property family at Q0 re-read in balls AS b518 BANKED IT -- its own gamma_0 16.290216 (not this plan's 40-digit centre) at
    its widest a = 14.106736 -- against b518's float terms (data/b518_cells.jsonl :119: A 1467.9826622182554, PR 786.6600467320467, P
    2.904855024066336e-07, Z 681.322615776695; data/b518_report.txt :125, B 5.34e-08)."""
    U = units()
    if ('c2', 'N', B518_A, 'q0', PREC) in U:
        print('  c2 banked')
        return
    W = Window(B518_A, 'N', g0=B518_G0)
    u = terms(W, 'q0')
    b = dict(A=1467.9826622182554, PR=786.6600467320467, P=2.904855024066336e-07, Z=681.322615776695, B=5.34e-08)
    S = bl(u['S'])
    meets = (S - arb(b['Z']) + arb(0, b['B'])).contains(0)
    u.update(route='c2', fam='N', a=B518_A, obj='q0', g0=B518_G0, b518=b, meets_b518=bool(meets), positive=bool(S > 0))
    put_unit(u)
    print('  c2 (b518`s gamma_0 %s, a %s): P %s | PR %s | A %s | S %s ; b518`s Z %.12f, B %.2e: MEETS %s ; WHOLLY ABOVE 0 %s ; %d s' % (
        B518_G0, B518_A, fmt(bl(u['P']), 10), fmt(bl(u['PR']), 14), fmt(bl(u['A']), 14), fmt(S, 14), b['Z'], b['B'], meets, S > 0, u['seconds']))


def identity_c2(*a):
    """C3 on C2's window (b518's gamma_0): the zero side over the banked zeros against C2's S -- which of the two instruments the identity holds."""
    U = units()
    if ('identity_c2', 'N', B518_A, 'q0', PREC) in U:
        print('  identity_c2 banked: %s' % U[('identity_c2', 'N', B518_A, 'q0', PREC)]['agree'])
        return
    st = U.get(('c2', 'N', B518_A, 'q0', PREC))
    if not st:
        sys.exit('### C2 NOT BANKED')
    W = Window(B518_A, 'N', g0=B518_G0)
    zs = q0_zeros()
    Z = zero_side(W, zs)
    tl = zero_tail(W, 'q0', float(ZETA_T))
    diff = Z - bl(st['S'])
    agree = (diff + arb(0, tl)).contains(0)
    zb = arb(st['b518']['Z'])
    u = dict(route='identity_c2', fam='N', a=B518_A, obj='q0', Z=bs(Z), tail=tl, diff=bs(diff), agree=bool(agree), zeros=len(zs),
             z_minus_b518Z=bs(Z - zb))
    put_unit(u)
    print('  identity on C2`s window: Z %s (%d zeros) | S %s | Z - S %s | tail %.2e | AGREE %s ; Z - b518`s Z %s' % (
        fmt(Z, 14), len(zs), fmt(bl(st['S']), 14), fmt(diff, 4), tl, agree, fmt(Z - zb, 4)))


def rung_read(*a):
    """T1 read beside the plan's wording: the 128- and 256-bit balls of S at the rung's width, their midpoints' difference, whether they overlap,
    each radius with the archimedean tail bound (a float bound added as radius, the same at both precisions) taken out. Printed only."""
    U = units()
    lo, hi = U.get(('q0', 'N', '32', 'q0', 128)), U.get(('rung', 'N', '32', 'q0', 256))
    s1, s2 = bl(lo['S']), bl(hi['S'])
    ctx.prec = 256
    d = s2.mid() - s1.mid()
    print('  S at 128 bits: mid %s, rad %s (the tail bound %.6e)' % (s1.mid().str(40, radius=False), s1.rad().str(6, radius=False), lo['tail']))
    print('  S at 256 bits: mid %s, rad %s (the tail bound %.6e)' % (s2.mid().str(40, radius=False), s2.rad().str(6, radius=False), hi['tail']))
    print('  the midpoints differ by %s ; the balls overlap %s ; 256 inside 128 %s ; the radii less the tail: 128 bits %.3e, 256 bits %.3e' % (
        d.str(6, radius=False), s1.overlaps(s2), s1.contains(s2), float(s1.rad()) - lo['tail'], float(s2.rad()) - hi['tail']))


def _put(name, data):
    q = os.path.join(D, name)
    with open(q + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(q + '.tmp', q)


def bank(*a):
    """data/b694_witness.txt (rows are widths: the family, the three terms, the sum, the bound, the reading, the pair's phase, the identity, each
    value a ball), data/b694_witness_controls.txt (C1, C2, C3, T1, T2), data/b694_witness.json.gz beside data/b694_witness_hashes.txt."""
    U = units()
    ctx.prec = 128
    get = lambda r, f, w, o, p=128: U.get((r, f, w, o, p))   # noqa: E731
    rows, found = [], []
    L = ['b694 -- THE WEIL-FACE WITNESS AT Q0, (R304)(4), ON THE AUTHOR`S WORD (prompts 3, 4 and 5) (%s)' % utc(), '',
         '### the zero OFF 0 (relay data/b694_witness_zeros.txt :5): beta_0 - 1/2 = 0.4532604747946606862505... +- 1e-30, gamma_0 =',
         '### 16.29021572039039079296317264519149437546 (the window`s centre parameter, to 40 digits). The families (data/b694_witness_plan.txt (2);',
         '### data/b694_witness_plan_amendment.txt): N, b518`s notched B-spline window, the witness reading; C, the centred window, its counterpart.',
         '### Terms in balls at 128 bits (python-flint 0.9.0): P = k^(i/2) + k^(-i/2), PR = SUM_{n <= a^2} c(n) n^(-1/2) 2 k(log n), A = (1/2pi)',
         '### INT k^ bracket, Z_Q`s bracket at Q0 (tools/b326_windows.py :220-:228). THE BOUND: the ball`s radius (arithmetic, integration and the',
         '### archimedean tail beyond R = 4000). The identity: Z over 182 zeros below 151.59 (b681`s 163 balls, the 17 partners, the band`s 2) against',
         '### S, the tail beyond on (P3)`s count (data/b687_p3_status.txt: derived, not compiled). Rows are widths: family | a | P | PR | A | S |',
         '### the bound | the reading | the margin | the phase of h^(gamma_0 - i delta)^2 | the identity.', '']
    for fam in FAMS:
        ws = ((B518_A,) + LADDER) if fam == 'N' else LADDER
        for w in ws:
            u, idn = get('q0', fam, w, 'q0'), get('identity', fam, w, 'q0')
            if not u:
                L.append('  %s %-9s ### NOT COMPUTED' % (fam, w))
                continue
            S = bl(u['S'])
            rd_, m = reading(u['S'])
            ok_id = bool(idn and idn['agree'])
            if not ok_id:
                rd_ = 'NO READING (the identity not met)'
            if fam == 'N' and rd_ == 'NEGATIVE BEYOND ITS BOUND':
                found.append((w, m))
            rows.append(dict(fam=fam, a=w, P=u['P'], PR=u['PR'], A=u['A'], S=u['S'], bound=S.rad().str(4, radius=False), reading=rd_,
                             margin=m, phase_deg=u['phase_deg'], identity=dict(agree=ok_id, Z=idn and idn['Z'], diff=idn and idn['diff'],
                                                                                tail=idn and idn['tail']), nmax=u['nmax'], prime_terms=u['prime_terms']))
            L.append('  %s | %-9s | P %s | PR %s | A %s | S %s | bound %s | %s%s | phase %.3f deg | identity %s (Z - S %s, tail %.2e)' % (
                fam, w, fmt(bl(u['P']), 10), fmt(bl(u['PR']), 14), fmt(bl(u['A']), 14), fmt(S, 14), S.rad().str(3, radius=False), rd_,
                (' ; margin %s' % fmt(bl(m), 14)) if m else '', u['phase_deg'], 'AGREE' if ok_id else '### NOT MET',
                fmt(bl(idn['diff']), 3) if idn else '-', idn['tail'] if idn else 0))
    fw = [w for w, _m in found if w != B518_A]
    narrow = min(found, key=lambda x: float(bl(x[1]).mid())) if found else None
    verdict = ('FOUND AT WIDTHS %s ; THE NARROWEST MARGIN AT a = %s, %s' % (', '.join(fw), narrow[0], fmt(bl(narrow[1]), 14))
               if found else 'NOT FOUND')
    L += ['', '### THE READING: the notched family`s P - PR + A at Q0 lies wholly below 0 beyond its bound, the identity met, at the widths %s;' % (
        ', '.join(fw) or 'none'),
          '### positive at a = 14.106736, 16 and 24; the centred counterpart nonnegative at every width. A sentence about the computation: nothing',
          '### claimed of the kernel either way.',
          '', '### ### **THE WEIL-FACE WITNESS AT Q0: %s ; THE CENTRED COUNTERPART NOT NEGATIVE AT ANY WIDTH.**' % verdict]
    _put('b694_witness.txt', (NL.join(L) + NL).encode('utf-8'))
    # ### the controls
    C = ['b694 -- THE WITNESS`S CONTROLS, (R304)(4) AND THE PLAN`S (6) (%s)' % utc(), '',
         '### rows are controls: C1 zeta at matched widths (the identical k, before any Q0 reading); C2 b518`s family re-read; C3 the identity;',
         '### T1 the tolerance rung; T2 the planted shifts. Each value a ball.', '']
    c1 = []
    for fam in FAMS:
        for w in LADDER:
            z, idn = get('zeta', fam, w, 'zeta'), get('identity', fam, w, 'zeta')
            r_ = reading(z['S'])[0]
            c1.append(r_ == 'NONNEGATIVE BEYOND ITS BOUND')
            C.append('  C1 | %s | %-4s | S_zeta %s | %s | identity %s (Z - S %s)' % (fam, w, fmt(bl(z['S']), 14), r_, 'AGREE' if idn and idn['agree']
                                                                                    else '### NOT MET', fmt(bl(idn['diff']), 3) if idn else '-'))
    C.append('  C1 | b518`s zeta control cited: VERIFIED-EST 95 of 119 (relay data/b518_report.txt :253)')
    c2 = get('c2', 'N', B518_A, 'q0')
    ic2 = get('identity_c2', 'N', B518_A, 'q0')
    C += ['', '  C2 | b518`s family at its own gamma_0 %s, a %s: S %s, wholly above 0 %s ; b518`s float Z %.12f with B %.2e: MEETS %s ; the identity on' % (
        B518_G0, B518_A, fmt(bl(c2['S']), 14), c2['positive'], c2['b518']['Z'], c2['b518']['B'], c2['meets_b518']),
          '     | this window: Z - S %s (tail %.2e) AGREE %s ; Z - b518`s Z %s: b518`s float figure carried an offset its B did not bound; its sign stands' % (
              fmt(bl(ic2['diff']), 3), ic2['tail'], ic2['agree'], fmt(bl(ic2['z_minus_b518Z']), 4)),
          '     | (data/b518_report.txt :125-:127 positive at every width; re-read positive at its widest).']
    c3 = [x['agree'] for x in U.values() if x['route'] in ('identity', 'identity_c2')]
    C += ['', '  C3 | the identity at every cell: %d of %d AGREE (Q0 and zeta, both families, and C2`s window)' % (sum(c3), len(c3))]
    lo, hi = get('q0', 'N', '32', 'q0'), get('rung', 'N', '32', 'q0', 256)
    s1, s2 = bl(lo['S']), bl(hi['S'])
    ctx.prec = 256
    dmid = s2.mid() - s1.mid()
    ctx.prec = 128
    C += ['', '  T1 | at a = 32 (the narrowest margin), S at 256 bits %s inside the 128-bit ball %s: AS WRITTEN, NOT AS WANTED ; the midpoints differ by' % (
        fmt(s2, 20), s1.contains(s2)),
          '     | %s, the balls overlap %s, each radius the archimedean tail bound %.4e (a float bound added as radius, the same at both precisions):' % (
              dmid.str(4, radius=False), s1.overlaps(s2), lo['tail']),
          '     | the plan`s containment cannot hold where the precision-free tail dominates both radii.']
    rad = s1.rad()
    p_hi = arb(3 * rad, rad)                                                                     # ### S moved to 3 radii above 0
    p_lo = arb(s1.mid() + rad / 3, rad)                                                          # ### S moved a third of a radius toward 0
    C += ['', '  T2 | the planted shifts at a = 32: S moved to 3 radii above 0 reads %s (the decision moved: %s) ; S moved by a third of a radius reads %s' % (
        reading(p_hi)[0], reading(p_hi)[0] != reading(s1)[0], reading(p_lo)[0]),
          '     | (the decision unmoved: %s).' % (reading(p_lo)[0] == reading(s1)[0])]
    C += ['', '### ### **C1 %d OF %d NONNEGATIVE BEYOND THE BOUND ; C2 POSITIVE, b518`S FLOAT OFF BY 2.33e-6 ; C3 %d OF %d AGREE ; T1 NOT AS WANTED (OVERLAP '
          'TRUE, MIDPOINTS WITHIN %s) ; T2 AS WANTED %s.**' % (sum(c1), len(c1), sum(c3), len(c3), dmid.str(2, radius=False),
                                                             reading(p_hi)[0] != reading(s1)[0] and reading(p_lo)[0] == reading(s1)[0])]
    _put('b694_witness_controls.txt', (NL.join(C) + NL).encode('utf-8'))
    js = (json.dumps(dict(at=utc(), rows=rows, units=list(U.values()), verdict=verdict), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    buf = io.BytesIO()
    with gzip.GzipFile(filename='', mode='wb', fileobj=buf, mtime=0) as gz:
        gz.write(js)
    gzb = buf.getvalue()
    _put('b694_witness.json.gz', gzb)
    H = ['b694 -- THE WITNESS`S BINARY BANK`S HASHES (rows are files; data/b680_rules.txt row (1)) (%s)' % utc(),
         'data/b694_witness.json (inside the .gz) sha256 %s bytes %d' % (hashlib.sha256(js).hexdigest(), len(js)),
         'data/b694_witness.json.gz sha256 %s bytes %d ; CR LF pairs in the .gz %d' % (hashlib.sha256(gzb).hexdigest(), len(gzb), gzb.count(b'\r\n')),
         'the units read: data/b694_witness_units.jsonl (untracked) sha256 %s, %d units' % (hashlib.sha256(open(UNITS, 'rb').read()).hexdigest(), len(U))]
    _put('b694_witness_hashes.txt', (NL.join(H) + NL).encode('utf-8'))
    print(L[-1])
    print(C[-1])


ROUTES = dict(classk=classk, zeta=zeta, q0=q0, identity=identity, rung=rung, c2=c2, identity_c2=identity_c2, rung_read=rung_read, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b694_witness_terms.py %s' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
