# -*- coding: utf-8 -*-
"""b707_onset.py -- THE SIGN-ONSET RADIUS AT Q0, (R317)(3), AS data/b705_registrations.txt (iii) REGISTERED IT (:15-:54, committed alone at
relay d139cfcf before any number, unchanged): "for each support radius a on a ladder fixed at b707 before any value is computed (from a = log 2
upward through the ladder's radii 2 log w, w = 32 ... 192), the Weil form at Q0 ... restricted to the windows h of support radius a/2 in a
finite-dimensional family named at b707 ...; its least eigenvalue on that family. THE SIGN-ONSET RADIUS a*: the least a of the ladder at which
the restricted form has a negative eigenvalue".

### UNTRACKED WRITE: data/b707_onset_units.jsonl

### THE LADDER (fixed here before any value): a = log 2 (the window of width sqrt 2: h supported in [-log 2 / 2, log 2 / 2], k in
### [-log 2, log 2], the source's range), then a = 2 log w at w = 32, 48, 64, 96, 128, 192 (b694's ladder from 32, tools/b694_witness_terms.py
### :51; the ruling's "a = 32" names the width 32). THE FAMILY NAMED HERE: at one frequency gamma_0, the span of b694's two windows -- C, the
### centred window cos(gamma_0 u) phi_a(u), and N, b518's notched window (gamma_0^2 + D^2)[cos(gamma_0 u) phi_a(u)] (tools/b694_witness_terms.py
### Window :106, imported unedited) -- a two-dimensional family F_a(gamma_0) = span{C, N}; two frequencies, each a family of its own: the band
### zero's ordinate 29.5517... (data/b703_q0_band.txt :18, b705's window) and rho_0's 16.2902... (tools/b694_witness.py G0, b694's and b696's
### window). The form on the family is the symmetric matrix G = [[S(C*C), S(C*N)], [S(C*N), S(N*N)]], S = P - PR + A the Weil form in balls
### (tools/b696_witness_balls.py: the prime sum and the archimedean integral over [0, 4000] with its DLMF tail ball, b705's contour, no zero
### tail: the identity is not read), the cross term by polarisation from the window C + N (the class Combo below: q_j = p_j + p_j'' + 2 i
### gamma_0 p_j' on b694's pieces, h^ = (1 + gamma_0^2 - z^2) g^; b696's archimedean tail bound for the family N applies to it, since
### |alpha + gamma_0^2 - r^2| <= r^2 for r >= R = 4000 > gamma_0 and alpha >= 0). THE L2 GRAM M = [[k_C(0), k_CN(0)], [k_CN(0), k_N(0)]] (the
### convolution at 0 is INT h^2), so the least eigenvalue is read in the L2 metric: det(G - lambda M) = 0. THE READING per (frequency, a), in
### balls: NEGATIVE DIRECTION BEYOND ITS BOUND where S(C*C) < 0, S(N*N) < 0 or det G < 0 (Sylvester: the form is not positive semidefinite on
### the family), with a witness h = v_1 C + v_2 N whose S(h*h) is read negative beyond its bound; POSITIVE DEFINITE BEYOND ITS BOUND where
### S(C*C) > 0 and det G > 0; UNDECIDED otherwise. a* per frequency: the least rung read NEGATIVE DIRECTION.
### THE FALSIFIER (the registration's): a positive form at every a computed -- no negative direction at any rung of the ladder, in either family.
### THE HYPOTHESIS: a* exists on the ladder, at or below a = 2 log 192 and above a = log 4.
### THE CONTROLS, run and printed BEFORE any Q0 figure: (C1) the zeta form, the same families at the same radii, read POSITIVE DEFINITE at every
### rung (b694's N4 gate carried: a Q0 term is refused until C1 reads so at every rung of both frequencies); beside the first rung, the source's
### proven range, cited by page (Connes-Consani, arXiv:2006.13771, relay data/b705_source_cc_2006_13771.txt: the support (1/2, 2) page 2
### :94-:97, Weil's inequality at the archimedean place :104-:107, Theorem 1 page 3 :120-:125) -- its conditions on g^ (vanishing at i/2 and at
### 0) are not met by this family, so the control at a = log 2 is READ, not taken as proven; (C2) the form's own machinery on the registered
### windows: b705's notched window of width 32 at the band zero returns data/b705_window.txt :11's S (NONNEGATIVE BEYOND ITS BOUND), b696's
### notched window of width 32 at rho_0 returns data/b696_witness_balls.txt :14's S (NEGATIVE BEYOND ITS BOUND), each within the two balls;
### the Combo window's transform equal to C's plus N's at three points; the bilinearity of S in k read on a second combination 2C + N against
### the prediction from C, N and C + N (the polarisation's own check).
### THE RUNG STRUCTURE printed before any term: Lambda_Q(n) and Lambda(n) at n = 2 ... 7 as computed (b325's inversion, lambda_q :291;
### Lambda_Q(2) = Lambda_Q(3) = 0 as the registration reads by hand), and at each rung the terms that enter (log n <= a) at Q0 and at zeta.
### Routes (each its own foreground call; one unit per (route, freq, kind, rung, obj), appended to the units file, resumable):
###   rungs                     the rung structure            c2                 the controls on the registered windows
###   zeta <freq> [rung ...]    C1 at zeta                    q0 <freq> [rung ...]   the Q0 terms (refused until C1 and C2 are read)
###   bank                      data/b707_onset_controls.txt, data/b707_onset.txt, data/b707_onset.json.gz beside data/b707_onset_hashes.txt
### Written by the Write tool at b707; it writes only the banks it names and its units file. Every value a ball (python-flint) at 128 bits.
"""
import gzip
import hashlib
import io
import json
import math
import os
import re
import sys
import time

from flint import acb, acb_poly, arb, ctx, fmpq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b694_witness_terms as W    # noqa: E402  ### the window, the prime channels, the bracket: imported unedited
import b696_witness_balls as WB   # noqa: E402  ### the archimedean integral and its tail ball: imported unedited
import b694_witness as WZ         # noqa: E402  ### rho_0's ordinate, G0

ACT = 'b707'
PREC = WB.PREC
ctx.prec = PREC
UNITS = os.path.join(D, '%s_onset_units.jsonl' % ACT)
BAND_RE = '0.79799715717868013876'      # ### data/b703_q0_band.txt :18
BAND_IM = '29.55176109862911459913'     # ### data/b703_q0_band.txt :18 ; b705's gamma_0
RHO0_IM = WZ.G0                         # ### tools/b694_witness.py G0 ; b694's and b696's gamma_0
FREQS = (('band', BAND_IM), ('rho0', RHO0_IM))
SQRT2 = '1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727'
RUNGS = (('log2', SQRT2), ('32', '32'), ('48', '48'), ('64', '64'), ('96', '96'), ('128', '128'), ('192', '192'))
RUNG_W = dict(RUNGS)
KINDS = ('C', 'N', 'CN')
R_INT = WB.R_HEIGHTS[0]                 # ### 4000, b705's contour
bs, bl, fmt = WB.bs, WB.bl, WB.fmt
B705_LINE, B696_LINE = 11, 14           # ### data/b705_window.txt :11 (N, 32, the band zero) ; data/b696_witness_balls.txt :14 (N, 32, rho_0)
CC = 'data/b705_source_cc_2006_13771.txt'
CC_CITES = 'the support (1/2, 2) page 2 :94-:97 ; Weil`s inequality at the archimedean place :104-:107 ; Theorem 1 page 3 :120-:125'


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put_txt(name, L):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u.get('freq', ''), u.get('kind', ''), u.get('rung', ''), u.get('obj', ''))] = u
    return U


def put_unit(u):
    u['at'] = utc()
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


# ================================================================================ THE WINDOWS: C, N AND THEIR SUM AT ONE FREQUENCY
class Combo(W.Window):
    """alpha C + N at one gamma_0: h = alpha cos(g0 u) phi + (g0^2 + D^2)[cos(g0 u) phi]; on b694's pieces q_j = alpha p_j + p_j'' + 2 i g0 p_j'
    (b694's N pieces plus alpha times its C pieces), h^ = (alpha + g0^2 - z^2) g^, g^ = (phi^(z - g0) + phi^(z + g0)) / 2. Its family name is
    'N' so that b696's archimedean tail bound (arch_tail :90, p = 8) applies: |alpha + g0^2 - r^2| <= r^2 for r >= R > g0 and alpha >= 0."""

    def __init__(self, a, g0, alpha=1):
        W.Window.__init__(self, a, 'N', g0=g0)
        assert alpha >= 0
        self.alpha = alpha
        self.q = [self.p[j] * acb(alpha) + self.q[j] for j in range(6)]
        self.qc = [acb_poly([c.conjugate() for c in qj.coeffs()]) for qj in self.q]

    def hhat(self, z):
        z = acb(z)
        g0 = acb(self.g0)
        gh = (self.phihat(z - g0) + self.phihat(z + g0)) / 2
        return (acb(self.alpha) + g0 * g0 - z * z) * gh


def window(kind, rung, g0):
    w = RUNG_W[rung]
    if kind == 'C':
        return W.Window(w, 'C', g0=g0)
    if kind == 'N':
        return W.Window(w, 'N', g0=g0)
    if kind == 'CN':
        return Combo(w, g0, 1)
    if kind == 'C2N':
        return Combo(w, g0, 2)
    raise KeyError(kind)


def nmax_of(Wd):
    """the last n whose term can be nonzero: n <= e^(2L) where the width is an integer (b696's reading, the boundary term exact by b694's
    rational path and zero), n < e^(2L) otherwise (the boundary term zero by the support; the float path is not sent to the boundary)."""
    e2L = math.exp(2 * float(Wd.L.mid()))
    if Wd.a.isdigit():
        return int(math.floor(e2L + 1e-9))
    return int(math.floor(e2L - 1e-9))


def terms707(Wd, obj):
    """b696's terms (tools/b696_witness_balls.py terms :179) composed from its imported parts with nmax_of above, and k(0) = INT h^2 beside."""
    t0 = time.time()
    nmax = nmax_of(Wd)
    P = (Wd.khat(acb(0, 0.5)) + Wd.khat(acb(0, -0.5))).real
    lam = W.lambda_q(nmax)[0] if obj == 'q0' else W.lambda_z(nmax)
    PR, nterms, _absum = W.prime_sum(Wd, lam, nmax) if nmax >= 2 else (arb(0), 0, 0.0)
    Ai = WB.a_int(Wd, obj, 0, R_INT)
    tl = WB.arch_tail(Wd, obj, R_INT)
    A = Ai + WB.unit_ball(tl)
    S = P - PR + A
    k0 = Wd.kval(arb(0), fmpq(0))
    return dict(P=bs(P), PR=bs(PR), Aint=bs(Ai), tail=bs(tl), A=bs(A), S=bs(S), k0=bs(k0), nmax=nmax, prime_terms=nterms, R=R_INT,
                L=bs(Wd.L), a_radius=bs(2 * Wd.L), seconds=int(time.time() - t0))


# ================================================================================ THE FORM ON THE FAMILY, IN BALLS
def gram(uC, uN, uCN):
    """G and M from the three windows' units: S_CN = (S_{C+N} - S_C - S_N) / 2, M_CN likewise from k(0)."""
    Scc, Snn, Scn = bl(uC['S']), bl(uN['S']), (bl(uCN['S']) - bl(uC['S']) - bl(uN['S'])) / 2
    Mcc, Mnn, Mcn = bl(uC['k0']), bl(uN['k0']), (bl(uCN['k0']) - bl(uC['k0']) - bl(uN['k0'])) / 2
    return (Scc, Snn, Scn), (Mcc, Mnn, Mcn)


def reading(G, M):
    """the sign of the form on span{C, N}, certified in balls, and the two eigenvalues in the L2 metric."""
    Scc, Snn, Scn = G
    Mcc, Mnn, Mcn = M
    det = Scc * Snn - Scn * Scn
    a_ = Mcc * Mnn - Mcn * Mcn
    b_ = Scc * Mnn + Snn * Mcc - 2 * Scn * Mcn
    disc = b_ * b_ - 4 * a_ * det
    sq = disc.sqrt() if disc >= 0 or disc.contains(0) else arb.nan()
    lmin, lmax = (b_ - sq) / (2 * a_), (b_ + sq) / (2 * a_)
    if Scc < 0 or Snn < 0 or det < 0:
        rd = 'NEGATIVE DIRECTION BEYOND ITS BOUND'
    elif Scc > 0 and det > 0:
        rd = 'POSITIVE DEFINITE BEYOND ITS BOUND'
    else:
        rd = 'UNDECIDED'
    # ### the witness direction for the least eigenvalue, from the midpoints, as rationals; its form value in balls
    lm = float(lmin.mid()) if not lmin.is_nan() else 0.0
    v1, v2 = -(float(Scn.mid()) - lm * float(Mcn.mid())), float(Scc.mid()) - lm * float(Mcc.mid())
    if abs(v1) + abs(v2) == 0:
        v1, v2 = 1.0, 0.0
    sc = max(abs(v1), abs(v2))
    v1, v2 = v1 / sc, v2 / sc
    r1, r2 = fmpq(int(round(v1 * 2 ** 40)), 2 ** 40), fmpq(int(round(v2 * 2 ** 40)), 2 ** 40)
    wv = arb(r1) * arb(r1) * Scc + 2 * arb(r1) * arb(r2) * Scn + arb(r2) * arb(r2) * Snn
    wn = arb(r1) * arb(r1) * Mcc + 2 * arb(r1) * arb(r2) * Mcn + arb(r2) * arb(r2) * Mnn
    return dict(reading=rd, det=bs(det), lmin=bs(lmin), lmax=bs(lmax), witness=[str(r1), str(r2)], witness_S=bs(wv), witness_norm=bs(wn),
                witness_reading=WB.reading(wv))


# ================================================================================ THE RUNG STRUCTURE, PRINTED BEFORE ANY TERM
def rungs(*a):
    U = units()
    if ('rungs', '', '', '', '') in U:
        print('  the rung structure banked')
        u = U[('rungs', '', '', '', '')]
    else:
        t0 = time.time()
        nm = nmax_of(W.Window('192', 'C'))
        lq, rq = W.lambda_q(nm)
        lz = W.lambda_z(nm)
        small = [(n, fmt(lq[n], 12), fmt(lz[n], 12), rq[n]) for n in range(2, 8)]
        rows = []
        prev = 0
        for name, w in RUNGS:
            Wd = W.Window(w, 'C')
            nmx = nmax_of(Wd)
            q_in = [n for n in range(2, nmx + 1) if not lq[n].is_zero()]
            z_in = [n for n in range(2, nmx + 1) if not lz[n].is_zero()]
            new_q = [n for n in q_in if n > prev]
            new_z = [n for n in z_in if n > prev]
            rows.append(dict(rung=name, w=w, a=bs(2 * Wd.L), nmax=nmx, q0_terms=len(q_in), zeta_terms=len(z_in), q0_first=q_in[:6], zeta_first=z_in[:6],
                             q0_new=len(new_q), zeta_new=len(new_z), q0_new_first=new_q[:6], zeta_new_first=new_z[:6]))
            prev = nmx
        u = dict(route='rungs', small=[dict(n=n, lambda_q=s1, lambda_z=s2, r_q=r) for n, s1, s2, r in small], rows=rows, nmax_top=nm, seconds=int(time.time() - t0))
        put_unit(u)
    print('  Lambda_Q(n), Lambda(n), r_Q(n) at n = 2..7 (lambda_q :291 computed, not read by hand):')
    for s in u['small']:
        print('    n %d | Lambda_Q %s | Lambda %s | r_Q %d' % (s['n'], s['lambda_q'], s['lambda_z'], s['r_q']))
    for r in u['rows']:
        print('  rung %-5s w %-6s a = 2L %s | n <= %d | Q0 terms %d (first %s ; new at this rung %d, first %s) | zeta terms %d (first %s ; new %d, first %s)' % (
            r['rung'], r['w'][:6], fmt(bl(r['a']), 10), r['nmax'], r['q0_terms'], r['q0_first'], r['q0_new'], r['q0_new_first'], r['zeta_terms'], r['zeta_first'],
            r['zeta_new'], r['zeta_new_first']))


# ================================================================================ THE CONTROLS ON THE REGISTERED WINDOWS (C2)
def _txt_S(name, line):
    L = io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '').split(NL)
    m = re.search(r'\| S (-?[0-9.]+(?:e-?\d+)?) \+- ([0-9.]+e-?\d+)', L[line - 1])
    return arb(m.group(1), m.group(2)), L[line - 1].strip()[:160]


def _gz_unit(gz_name, hashes_name, pick):
    """a unit of a banked gz read through its hashes bank (b705's form): the gz's sha256 and its JSON's must equal the bank's rows."""
    H = io.open(os.path.join(D, hashes_name), encoding='utf-8').read().replace(chr(13), '').split(NL)
    want_gz = want_js = None
    for l in H:
        m = re.search(r'\b([0-9a-f]{64})\b', l)
        if not m:
            continue
        if '.json.gz' in l:
            want_gz = m.group(1)
        elif '.json (inside' in l:
            want_js = m.group(1)
    gzb = open(os.path.join(D, gz_name), 'rb').read()
    raw = gzip.decompress(gzb)
    have_gz, have_js = hashlib.sha256(gzb).hexdigest(), hashlib.sha256(raw).hexdigest()
    if have_gz != want_gz or have_js != want_js:
        sys.exit('### data/%s %s / its JSON %s DO NOT EQUAL data/%s %s / %s -- NOT READ' % (gz_name, have_gz[:16], have_js[:16], hashes_name,
                                                                                            (want_gz or '-')[:16], (want_js or '-')[:16]))
    j = json.loads(raw.decode('utf-8'))
    hits = [x for x in j.get('units') or [] if pick(x)]
    return hits[0] if len(hits) == 1 else None


def c2(*a):
    U = units()
    out = []
    # ### (1) b705's notched window of width 32 at the band zero, through this tool's terms
    k = ('c2', 'band', 'N', '32', 'q0')
    if k not in U:
        u = terms707(W.Window('32', 'N', g0=BAND_IM), 'q0')
        u.update(route='c2', freq='band', kind='N', rung='32', obj='q0', cite='data/b705_window.txt :%d' % B705_LINE)
        put_unit(u)
        U = units()
    u = U[k]
    want, line = _txt_S('b705_window.txt', B705_LINE)
    g5 = _gz_unit('b705_window.json.gz', 'b705_window_hashes.txt', lambda x: x.get('route') == 'q0' and x.get('fam') == 'N' and str(x.get('a')) == '32')
    ok1 = g5 is not None and (bl(u['S']) - bl(g5['S'])).contains(0) and ('S %s' % fmt(bl(u['S']), 14)) in line and WB.reading(u['S']) == 'NONNEGATIVE BEYOND ITS BOUND'
    out.append(('b705`s notched window of width 32 at the band zero (data/b705_window.txt :%d; the ball from data/b705_window.json.gz through its hashes)' % B705_LINE,
                fmt(bl(u['S']), 14), fmt(bl(g5['S']), 14) if g5 else '### NO UNIT', WB.reading(u['S']), ok1))
    # ### (2) b696's notched window of width 32 at rho_0
    k = ('c2', 'rho0', 'N', '32', 'q0')
    if k not in U:
        u = terms707(W.Window('32', 'N', g0=RHO0_IM), 'q0')
        u.update(route='c2', freq='rho0', kind='N', rung='32', obj='q0', cite='data/b696_witness_balls.txt :%d' % B696_LINE)
        put_unit(u)
        U = units()
    u = U[k]
    want2, line2 = _txt_S('b696_witness_balls.txt', B696_LINE)
    g6 = _gz_unit('b696_witness_balls.json.gz', 'b696_witness_balls_hashes.txt',
                  lambda x: x.get('route') == 'q0' and x.get('fam') == 'N' and str(x.get('a')) == '32' and x.get('obj') == 'q0' and x.get('prec') == 128 and str(x.get('h')) == '4000')
    ok2 = g6 is not None and (bl(u['S']) - bl(g6['S'])).contains(0) and ('S %s' % fmt(bl(u['S']), 14)) in line2 and WB.reading(u['S']) == 'NEGATIVE BEYOND ITS BOUND'
    out.append(('b696`s notched window of width 32 at rho_0 (data/b696_witness_balls.txt :%d; the ball from data/b696_witness_balls.json.gz through its hashes)' % B696_LINE,
                fmt(bl(u['S']), 14), fmt(bl(g6['S']), 14) if g6 else '### NO UNIT', WB.reading(u['S']), ok2))
    # ### (3) the Combo window's transform against C's plus N's at three points
    Cw, Nw, CNw = window('C', '32', BAND_IM), window('N', '32', BAND_IM), window('CN', '32', BAND_IM)
    pts = [acb(0, 0.5), acb(arb('7.25')), acb(arb('31.5'), arb('0.3'))]
    dif = [CNw.hhat(z) - (Cw.hhat(z) + Nw.hhat(z)) for z in pts]
    ok3 = all(d.contains(0) for d in dif)
    out.append(('the Combo window`s transform (1 + g0^2 - z^2) g^ against C`s plus N`s at three points (band, 32)', ' ; '.join(fmt(d.real, 3) + ' + i ' + fmt(d.imag, 3) for d in dif), '0 at each', 'CONTAINS 0 %s' % ok3, ok3))
    # ### (4) the bilinearity of S: 2C + N against the prediction 2 S_C + 2 S_{C+N} - S_N from C, N and C + N (band, 32, zeta: no Q0 figure before C1)
    for kind in ('C', 'N', 'CN', 'C2N'):
        k = ('c2', 'band', kind, '32', 'zeta')
        if k not in U:
            u = terms707(window(kind, '32', BAND_IM), 'zeta')
            u.update(route='c2', freq='band', kind=kind, rung='32', obj='zeta')
            put_unit(u)
            U = units()
    sC, sN, sCN, s2 = (bl(U[('c2', 'band', kd, '32', 'zeta')]['S']) for kd in ('C', 'N', 'CN', 'C2N'))
    pred = 2 * sC + 2 * sCN - sN
    ok4 = (s2 - pred).contains(0)
    out.append(('the bilinearity of S in k (band, 32, zeta): S(2C+N) computed against 2 S(C) + 2 S(C+N) - S(N)', fmt(s2, 14), fmt(pred, 14), 'CONTAINS 0 %s' % ok4, ok4))
    kC, kN, kCN, k2 = (bl(U[('c2', 'band', kd, '32', 'zeta')]['k0']) for kd in ('C', 'N', 'CN', 'C2N'))
    predk = 2 * kC + 2 * kCN - kN
    ok5 = (k2 - predk).contains(0)
    out.append(('the bilinearity of k(0) = INT h^2 (band, 32): k_{2C+N}(0) against 2 k_C(0) + 2 k_{C+N}(0) - k_N(0)', fmt(k2, 14), fmt(predk, 14), 'CONTAINS 0 %s' % ok5, ok5))
    put_unit(dict(route='c2verdict', rows=[dict(case=c_, have=h_, want=w_, reading=r_, ok=bool(o_)) for c_, h_, w_, r_, o_ in out], ok=all(o_ for *_x, o_ in out)))
    for c_, h_, w_, r_, o_ in out:
        print('  C2 | %s | have %s | want %s | %s | %s' % (c_, h_, w_, r_, 'AS WANTED' if o_ else '### NOT AS WANTED'))
    print('### C2 AS WANTED %s' % all(o_ for *_x, o_ in out))


def _c2_ok(U):
    v = [u for k, u in U.items() if k[0] == 'c2verdict']
    return bool(v) and bool(v[-1].get('ok'))


# ================================================================================ C1 AND THE Q0 TERMS
def _zeta_ok(U):
    bad, miss = [], []
    for fq, g0 in FREQS:
        for name, _w in RUNGS:
            us = [U.get(('terms', fq, kd, name, 'zeta')) for kd in KINDS]
            if any(u is None for u in us):
                miss.append((fq, name))
                continue
            G, M = gram(*us)
            if reading(G, M)['reading'] != 'POSITIVE DEFINITE BEYOND ITS BOUND':
                bad.append((fq, name))
    if miss:
        return False, 'C1 (ZETA) NOT BANKED AT EVERY RUNG OF BOTH FREQUENCIES: missing %s' % miss
    if bad:
        return False, 'C1 (ZETA) NOT POSITIVE DEFINITE BEYOND ITS BOUND AT %s' % bad
    return True, 'C1 (ZETA) POSITIVE DEFINITE AT EVERY RUNG OF BOTH FREQUENCIES'


def _run(obj, freq, names):
    g0 = dict(FREQS)[freq]
    U = units()
    if obj == 'q0':
        ok, why = _zeta_ok(U)
        if not ok:
            sys.exit('### %s -- NO Q0 TERM COMPUTED (the control before the figure)' % why)
        print('  ' + why)
        if not _c2_ok(U):
            sys.exit('### C2 NOT READ AS WANTED -- NO Q0 TERM COMPUTED (the control before the figure)')
        print('  C2 AS WANTED')
    for name in names:
        for kind in KINDS:
            k = ('terms', freq, kind, name, obj)
            if k in U:
                u = U[k]
                print('  %s %s %-3s rung %-5s banked: S %s %s' % (obj, freq, kind, name, fmt(bl(u['S'])), WB.reading(u['S'])))
                continue
            u = terms707(window(kind, name, g0), obj)
            u.update(route='terms', freq=freq, kind=kind, rung=name, obj=obj, g0=g0, prec=PREC)
            put_unit(u)
            U = units()
            print('  %s %s %-3s rung %-5s a %s | P %s | PR %s (%d terms to n %d) | A %s (tail %s) | S %s | %s | k(0) %s | %d s' % (
                obj, freq, kind, name, fmt(bl(u['a_radius']), 8), fmt(bl(u['P']), 6), fmt(bl(u['PR']), 10), u['prime_terms'], u['nmax'], fmt(bl(u['A']), 10),
                fmt(bl(u['tail']), 3), fmt(bl(u['S']), 12), WB.reading(u['S']), fmt(bl(u['k0']), 6), u['seconds']), flush=True)
        us = [U[('terms', freq, kd, name, obj)] for kd in KINDS]
        G, M = gram(*us)
        r = reading(G, M)
        print('  %s %s rung %-5s FORM on span{C, N}: S_CC %s | S_NN %s | S_CN %s | det %s | lambda (L2) min %s max %s | %s | witness %s S %s %s' % (
            obj, freq, name, fmt(G[0], 8), fmt(G[1], 8), fmt(G[2], 8), fmt(bl(r['det']), 6), fmt(bl(r['lmin']), 8), fmt(bl(r['lmax']), 6), r['reading'],
            r['witness'], fmt(bl(r['witness_S']), 6), r['witness_reading']), flush=True)


def zeta(freq, *a):
    _run('zeta', freq, a or [n for n, _w in RUNGS])


def q0(freq, *a):
    _run('q0', freq, a or [n for n, _w in RUNGS])


# ================================================================================ THE BANKS
def bank(*a):
    U = units()
    need = [('terms', fq, kd, nm, ob) for ob in ('zeta', 'q0') for fq, _g in FREQS for nm, _w in RUNGS for kd in KINDS]
    miss = [k for k in need if k not in U]
    if miss:
        sys.exit('### UNITS MISSING -- NOTHING WRITTEN: %s' % miss[:6])
    if not _c2_ok(U):
        sys.exit('### C2 NOT READ AS WANTED -- NOTHING WRITTEN')
    zok, zwhy = _zeta_ok(U)
    rg = U[('rungs', '', '', '', '')]
    c2v = [u for k, u in U.items() if k[0] == 'c2verdict'][-1]
    rows = {}
    for ob in ('zeta', 'q0'):
        for fq, g0 in FREQS:
            for nm, _w in RUNGS:
                us = [U[('terms', fq, kd, nm, ob)] for kd in KINDS]
                G, M = gram(*us)
                r = reading(G, M)
                rows[(ob, fq, nm)] = dict(obj=ob, freq=fq, rung=nm, a=us[0]['a_radius'], S_CC=bs(G[0]), S_NN=bs(G[1]), S_CN=bs(G[2]), M_CC=bs(M[0]), M_NN=bs(M[1]),
                                          M_CN=bs(M[2]), **r)
    onset = {}
    for fq, _g in FREQS:
        neg = [nm for nm, _w in RUNGS if rows[('q0', fq, nm)]['reading'] == 'NEGATIVE DIRECTION BEYOND ITS BOUND']
        und = [nm for nm, _w in RUNGS if rows[('q0', fq, nm)]['reading'] == 'UNDECIDED']
        onset[fq] = dict(negative_at=neg, undecided_at=und, a_star=neg[0] if neg else None, a_star_radius=rows[('q0', fq, neg[0])]['a'] if neg else None)
    any_neg = any(onset[fq]['a_star'] for fq, _g in FREQS)
    falsifier = not any_neg and not any(onset[fq]['undecided_at'] for fq, _g in FREQS)
    log4 = arb(4).log()
    top = 2 * arb(192).log()
    band = onset['band']
    # ### "at or below 2 log 192" is the ladder's own top rung, so a* on the ladder is at or below it by construction; "above log 4" by the ball
    hyp = 'REFUTED' if falsifier else ('UNDECIDED' if not band['a_star'] else ('HELD' if bl(band['a_star_radius']) > log4 else 'REFUTED'))
    # --- the controls bank
    C = ['%s -- (R317)(3): THE ONSET`S CONTROLS, RUN AND PRINTED BEFORE ANY Q0 FIGURE (%s)' % (ACT, utc()), '',
         '### the family F_a(gamma_0) = span{C, N} at gamma_0 = the band zero`s ordinate %s (data/b703_q0_band.txt :18) and at rho_0`s %s' % (BAND_IM, RHO0_IM[:24]),
         '### (tools/b694_witness.py G0); the window tools/b694_witness_terms.py Window :106 and the terms tools/b696_witness_balls.py a_int :170, arch_tail :90,',
         '### both imported unedited; the form in balls at %d bits. Rows are rungs: frequency | rung | a = 2L | S_CC | S_NN | S_CN | det G | lambda_min, lambda_max' % PREC,
         '### (the L2 metric) | the reading.', '',
         '### THE RUNG STRUCTURE (printed before any term): Lambda_Q(n), Lambda(n), r_Q(n) at n = 2..7 as computed:']
    C += ['    n %d | Lambda_Q %s | Lambda %s | r_Q %d' % (s['n'], s['lambda_q'], s['lambda_z'], s['r_q']) for s in rg['small']]
    C += ['    rung %-5s a = 2L %s | n <= %d | Q0 terms %d (first %s ; new at this rung %d) | zeta terms %d (first %s ; new %d)' % (
        r['rung'], fmt(bl(r['a']), 10), r['nmax'], r['q0_terms'], r['q0_first'], r['q0_new'], r['zeta_terms'], r['zeta_first'], r['zeta_new']) for r in rg['rows']]
    C += ['', '### (C1) THE ZETA FORM, both frequencies, every rung -- the instrument where no off-line zero stands (b694`s N4 gate carried: a Q0 term is',
          '### refused until every rung reads POSITIVE DEFINITE BEYOND ITS BOUND). At the first rung, a = log 2, the source`s proven range stands beside the',
          '### reading: Connes-Consani arXiv:2006.13771 (relay %s): %s -- its conditions on g^ (vanishing at i/2 and at 0) not met by this family,' % (CC, CC_CITES),
          '### so the row is READ, not taken as proven.']
    for fq, _g in FREQS:
        for nm, _w in RUNGS:
            r = rows[('zeta', fq, nm)]
            C.append('  %-4s | %-5s | a %s | S_CC %s | S_NN %s | S_CN %s | det %s | lambda %s, %s | %s%s' % (
                fq, nm, fmt(bl(r['a']), 8), fmt(bl(r['S_CC']), 10), fmt(bl(r['S_NN']), 10), fmt(bl(r['S_CN']), 10), fmt(bl(r['det']), 6), fmt(bl(r['lmin']), 8),
                fmt(bl(r['lmax']), 6), r['reading'], ' | the source`s range: %s' % CC_CITES if nm == 'log2' else ''))
    C += ['  ' + zwhy, '', '### (C2) THE FORM`S MACHINERY ON THE REGISTERED WINDOWS, AND ITS OWN BILINEARITY:']
    C += ['  %s | have %s | want %s | %s | %s' % (x['case'], x['have'], x['want'], x['reading'], 'AS WANTED' if x['ok'] else '### NOT AS WANTED') for x in c2v['rows']]
    C += ['', '### ### **C1 ZETA POSITIVE DEFINITE AT EVERY RUNG OF BOTH FREQUENCIES %s ; C2 AS WANTED %s (%d cases) ; THE RUNG STRUCTURE: Lambda_Q(2) = 0 %s, Lambda_Q(3) = 0 %s.**' % (
        zok, c2v['ok'], len(c2v['rows']), rg['small'][0]['lambda_q'].startswith('0 '), rg['small'][1]['lambda_q'].startswith('0 '))]
    put_txt('%s_onset_controls.txt' % ACT, C)
    # --- the reading bank
    L = ['%s -- (R317)(3): THE SIGN-ONSET RADIUS AT Q0, AS data/b705_registrations.txt (iii) REGISTERED IT (:15-:54) (%s)' % (ACT, utc()), '',
         '### THE FORM: the Epstein zeta of x^2 + xy + 6y^2 (Q0, discriminant -23); the Weil form S = P - PR + A on k = h * h (b321`s identity, the',
         '### terms of tools/b696_witness_balls.py with the archimedean tail beyond R = 4000 as a DLMF ball; no zero tail), restricted to the family',
         '### F_a(gamma_0) = span{C, N} of support radius a/2 (b694`s centred and notched windows at one frequency), read as the symmetric matrix',
         '### G = [[S(C*C), S(C*N)], [S(C*N), S(N*N)]] in balls with the L2 Gram M beside it; two frequencies, the band zero`s ordinate (b705`s window)',
         '### and rho_0`s (b694`s). THE LADDER: a = log 2, then 2 log w at w = 32, 48, 64, 96, 128, 192. The controls: data/b707_onset_controls.txt.',
         '### Rows are rungs: frequency | rung | a = 2L | S_CC | S_NN | S_CN | det G | lambda_min, lambda_max (the L2 metric) | the reading | the witness',
         '### direction (v_1 C + v_2 N) and its S beyond its bound.', '', '### THE READING, THE FORM AT Q0:']
    for fq, _g in FREQS:
        for nm, _w in RUNGS:
            r = rows[('q0', fq, nm)]
            L.append('  %-4s | %-5s | a %s | S_CC %s | S_NN %s | S_CN %s | det %s | lambda %s, %s | %s | v %s S %s %s' % (
                fq, nm, fmt(bl(r['a']), 8), fmt(bl(r['S_CC']), 10), fmt(bl(r['S_NN']), 12), fmt(bl(r['S_CN']), 10), fmt(bl(r['det']), 6), fmt(bl(r['lmin']), 8),
                fmt(bl(r['lmax']), 6), r['reading'], r['witness'], fmt(bl(r['witness_S']), 6), r['witness_reading']))
    L += ['', '### THE ONSET RADIUS per frequency (the least rung read NEGATIVE DIRECTION BEYOND ITS BOUND):']
    for fq, _g in FREQS:
        o = onset[fq]
        L.append('  %-4s | negative at %s ; undecided at %s ; a* = %s%s' % (fq, o['negative_at'] or 'NO RUNG', o['undecided_at'] or 'NO RUNG', o['a_star'] or 'NONE ON THE LADDER',
                                                                             (' (a = %s)' % fmt(bl(o['a_star_radius']), 10)) if o['a_star'] else ''))
    L += ['', '### THE FALSIFIER (a positive form at every a computed, both frequencies): %s' % ('FIRED' if falsifier else 'NOT FIRED'),
          '### THE REGISTRATION`S HYPOTHESIS (a* on the ladder, at or below 2 log 192 = %s and above log 4 = %s; read at the band zero`s family, rho_0`s beside): %s%s' % (
              fmt(top, 8), fmt(log4, 8), hyp, (' -- a* = %s' % band['a_star']) if band['a_star'] else ''),
          '### THE RUNGS NAMED BY THE RULING: log 2 (empty prime side at both), log 3, log 4, log 5, log 7 -- none of these but log 2 is a rung of the ladder; the',
          '### terms entering at each rung are printed in the controls bank (Lambda_Q(2) = Lambda_Q(3) = 0 as computed).',
          '### THE LADDER`S COARSENESS: at rho_0`s family a* is the first rung above log 2, so the onset lies in (log 2, 2 log 32] on this ladder; b696`s finer',
          '### ladder reads N at width 24 NONNEGATIVE and at 32 NEGATIVE (data/b696_witness_balls.txt :13-:14), placing it in (2 log 24, 2 log 32]. At the band',
          '### zero`s family a* is the ladder`s last rung, where N alone is negative (b705`s reading): the family adds no earlier negative direction.', '',
          '### ### **THE ONSET AT THE BAND ZERO`S FAMILY: a* = %s ; AT rho_0`S FAMILY: a* = %s ; THE FALSIFIER %s ; THE HYPOTHESIS %s ; C1 ZETA POSITIVE DEFINITE %s ; C2 AS WANTED %s.**' % (
              band['a_star'] or 'NONE', onset['rho0']['a_star'] or 'NONE', 'FIRED' if falsifier else 'NOT FIRED', hyp, zok, c2v['ok'])]
    put_txt('%s_onset.txt' % ACT, L)
    J = dict(at=utc(), zero=dict(re=BAND_RE, im=BAND_IM, cite='data/b703_q0_band.txt :18'), rho0_im=RHO0_IM, rungs=[dict(rung=n, w=w) for n, w in RUNGS], prec=PREC,
             onset=onset, falsifier_fired=falsifier, hypothesis=hyp, c1_zeta_ok=zok, c2=c2v, rung_structure=rg,
             rows=[rows[k] for k in sorted(rows)], units=[U[k] for k in need] + [U[k] for k in U if k[0] == 'c2'])
    gz = os.path.join(D, '%s_onset.json.gz' % ACT)
    raw = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(gz + '.tmp', 'wb') as fh:
        fh.write(gzip.compress(raw, 9, mtime=0))
    os.replace(gz + '.tmp', gz)
    gzb = open(gz, 'rb').read()
    put_txt('%s_onset_hashes.txt' % ACT, ['%s -- THE ONSET`S BINARY BANK, ITS HASHES (data/b680_rules.txt row (1)) (%s)' % (ACT, utc()), '',
                                           '### rows: path ; sha256 ; bytes, LF (the json inside the gz and the gz itself)',
                                           'data/%s_onset.json.gz ; %s ; %d' % (ACT, hashlib.sha256(gzb).hexdigest(), len(gzb)),
                                           'data/%s_onset.json (inside the gz) ; %s ; %d' % (ACT, hashlib.sha256(raw).hexdigest(), len(raw))])
    print(NL.join(C[-1:] + L[10:]))


ROUTES = dict(rungs=rungs, c2=c2, zeta=zeta, q0=q0, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b707_onset.py rungs | c2 | zeta <freq> [rung ...] | q0 <freq> [rung ...] | bank')
        sys.exit(2)
    fn(*sys.argv[2:])
