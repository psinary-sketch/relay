# -*- coding: utf-8 -*-
"""b333_derive.py -- THE ARCHIMEDEAN TERM DERIVED: THE CHAIN, THE THIRD ROUTE, THE RE-RANK.

### ### **THREE PHASES, ONE RUN FILE, NORMALIZATIONS FIRST.**
###   (1) THE CONVENTIONS (N1)-(N4) and THE CHAIN (L1)-(L5): every link a quotation found in the extract
###       file, or an elementary identity named and CHECKED NUMERICALLY with mpmath (the Gamma factor's
###       logarithmic derivative against `h_+`, for zeta and for the Epstein factor of b326). The verdict
###       word printed: DERIVES-ON-IMPORT / RESISTS / MISMATCH.
###   (2) THE THIRD ROUTE: the source's (150) evaluated on the real side with `mpmath.quad`, sharing no
###       code with the atlas, with b320's (38) route, or with the digamma route; the bump re-implemented
###       from its definition; `A_3 = -W_R`. Beside it, as a REPORT and not a bar, the source's (152)
###       evaluated the same way (`A_152`), so that the source's own equality `W_inf = -W_R` is checked
###       by this seat's numbers. The bar (registration (E)): `|A_3 - A_digamma(b320)| <= 2e-4` and
###       `|A_3 - W_38(b320)| <= 2e-4` at every cell, the banked values READ FROM b320's TABLE.
###       Two working precisions. ### **A DISAGREEMENT IS REPORTED FIRST.**
###   (3) THE RE-RANK: b332's sealed ORDER and rule, imported; K5's grades updated as the registration
###       says; both seats' expectations scored in words.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D = os.path.join(ROOT, 'data')
EXTRACT = os.path.join(D, 'b333_extract_notes.txt')
B320 = os.path.join(D, 'b320_the_lawful_function.txt')
OUTJ = os.path.join(D, 'b333_derive.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CELLS = [1.3, 1.35, 1.41, 1.5, 1.7, 1.9, 1.99, 2.0, 2.01, 2.1, 2.4, 2.8, 3.0]
BAR = 2e-4
CONVERGE = BAR / 10.0

# ### (link, kind, the quotations that carry it -- each must be IN THE EXTRACT FILE -- and the identity if any)
CHAIN = [
    ('N1', 'convention', ['`f-hat(t) = INT f(rho) rho^{-it} d*rho = INT w(v) e^{-itv} dv`', 'fpxqxs´1dx. (147)'],
     "f(x) = x^{-1/2} w(log x) under (147): f~(1/2 + i tau) = INT w(v) e^{i tau v} dv = f-hat(tau) for even w; the atlas's hhat."),
    ('N2', 'convention', ['w /= np.trapezoid(w, v)'], 'f(1) = w(0); f^# = f for even w.'),
    ('N3', 'convention', ['INT w e^{c v} dv = -(1/c^2) SUM_j beta_j (e^{c v_{j+1}} - e^{c v_j})'], 'dx = x dv is absorbed by x^{s-1} into e^{(s-1/2)v}.'),
    ('N4', 'identity', [], 'Fourier inversion at zero: w(0) = (1/2 pi) INT f-hat(tau) dtau.'),
    ('L1', 'import', ['WRpfq :“p log 4π`γqfp1q`', 'WRpfq“p logπqfp1q´ 1', '˜fpwqdw. (151)'], '(150) -> (151): the source\'s own step.'),
    ('L2', 'import+identity', ['namely the equality for the local term ( WR“´W8)', 'h`pτq“´ logπ` ℜpλp1{4`iτ{2qq, λ pzq“ Γ1pzq{Γpzq. (153)'],
     '(151) -> (152)-(153): W_inf = -W_R; (log pi) f(1) moved inside by N4; Re(Gamma\'/Gamma)(w/2) at w = 1/2 + i tau is Re lambda(1/4 + i tau/2).'),
    ('L3', 'identification', ['Re psi(1/4 + i u/2) - log pi, cached.', 'A = float(np.trapezoid(hhat(v, w, U) * kernel(U), U) / (2.0 * math.pi))', 'h`pτq ˜fpwqdτ'],
     "the atlas's kernel IS h_+, hhat IS f~(1/2 + iu), the atlas's A IS (152): A(f) = W_inf(f) = -W_R(f)."),
    ('L4', 'sign chain', ['sum_gamma hhat(gamma)  =  hhat(i/2) + hhat(-i/2)  -  PRIME  +  ARCH   [sign fixed BY the E2 calibration]', 'Wvpfq, (148)', '`SUM_v W_v(f) = - Z`.**', 'IT DOES NOT SCALE `A`. ### IT DOES NOT SET `A`. ### IT CHOOSES WHERE `A` GOES.'],
     '(148): SUM_rho f~ = pole - W_R - SUM_p W_p = pole + W_inf - PRIME, the atlas\'s orientation.'),
    ('L5', 'identity', ['Epstein archimedean kernel was ### **HALF** ### the derived', '`2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt23)`'],
     'h_+ = 2 Re (d/ds) log(pi^{-s/2} Gamma(s/2)) at s = 1/2 + i tau; the same rule on (sqrt23/2pi)^s Gamma(s) gives b326\'s kernel.'),
]


def read_b320_table():
    txt = io.open(B320, encoding='utf-8', errors='replace').read()
    rows = {}
    for m in re.finditer(r'^\s+(\d+(?:\.\d+)?)\s+(YES|no)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(\d\.\d+e-\d+)\s*$', txt, re.M):
        rows[float(m.group(1))] = (m.group(2) == 'YES', float(m.group(3)), float(m.group(4)))
    return rows


def identities(rec):
    from mpmath import mp, mpf, mpc, pi, log, loggamma, digamma, diff, re as mre, sqrt
    mp.dps = 30
    ok = True
    rec('  (L5) THE FACTOR-OF-TWO HAZARD, CHECKED FROM ONE IDENTITY (mpmath, dps 30):')
    for tau in (mpf('0.5'), mpf(3), mpf(17)):
        s = mpc(mpf(1) / 2, tau)
        ld = diff(lambda z: -z / 2 * log(pi) + loggamma(z / 2), s)
        hplus = -log(pi) + mre(digamma(mpc(mpf(1) / 4, tau / 2)))
        d1 = abs(2 * mre(ld) - hplus)
        ldq = diff(lambda z: z * log(sqrt(23) / (2 * pi)) + loggamma(z), s)
        kq = 2 * mre(digamma(mpc(mpf(1) / 2, tau))) - 2 * log(2 * pi / sqrt(23))
        d2 = abs(2 * mre(ldq) - kq)
        rec('      tau = %-5s  |2 Re (log Gamma_R)\'(1/2 + i tau) - h_+(tau)| = %.3e ;  Epstein: |2 Re (log Lambda_Q-factor)\' - kernel_b326| = %.3e' % (tau, d1, d2))
        ok = ok and d1 < mpf('1e-20') and d2 < mpf('1e-20')
    rec('      the zeta identity and the Epstein identity hold to the working precision : %s' % ok)
    rec('      ### the hazard: the 1/2 of Gamma(s/2) against the 2 of h_+; b325 carried the 1/2 without the 2.')
    return ok


def third_route(dps, rec, quiet=False):
    from mpmath import mp, mpf, mpc, pi, log, exp, sqrt, quad, digamma, euler, re as mre, cos, inf
    mp.dps = dps
    c0 = quad(lambda t: exp(-1 / (1 - t * t)), [-1, 1])
    out = {}
    for a in CELLS:
        a_ = mpf(a)
        L = log(a_)
        norm = L * c0

        def w(v):
            t = v / L
            if abs(t) >= 1:
                return mpf(0)
            return exp(-1 / (1 - t * t)) / norm

        def f(x):
            return w(log(x)) / sqrt(x)

        f1 = w(mpf(0))
        # ### (150): W_R = (log 4pi + gamma) f(1) + INT_1^inf (f + f^# - 2 f(1)/x) dx/(x - 1/x), f^# = f
        body = quad(lambda x: (2 * f(x) - 2 * f1 / x) / (x - 1 / x), [1, 1 + (a_ - 1) / 8, 1 + (a_ - 1) / 2, a_])
        tail = -f1 * log((a_ + 1) / (a_ - 1))          # INT_a^inf -2 f(1)/x dx/(x - 1/x) exactly
        WR = (log(4 * pi) + euler) * f1 + body + tail
        A3 = -WR
        # ### (152), evaluated the same way: A_152 = (1/2pi) INT f-hat(tau) [Re psi(1/4 + i tau/2) - log pi] dtau
        def fhat(tau):
            return quad(lambda v: w(v) * cos(tau * v), [-L, 0, L])

        def integrand(tau):
            return fhat(tau) * (mre(digamma(mpc(mpf(1) / 4, tau / 2))) - log(pi))

        T = 60 / L
        A152 = 2 * quad(integrand, [0, 2 / L, 8 / L, 20 / L, T]) / (2 * pi)
        out[a] = dict(A3=float(A3), WR=float(WR), A152=float(A152), f1=float(f1), body=float(body), tail=float(tail))
        if not quiet:
            rec('      a = %-5g  W_R(150) = %+.9f   A_3 = -W_R = %+.9f   A_152 = %+.9f   f(1) = %.9f' % (a, WR, A3, A152, f1))
    return out


def rerank(rec):
    import b332_statement as S
    cons = []
    for key, name, unfold, grades, reason in S.CONSTITUENTS:
        gs = list(grades)
        if key == 'K5':
            gs = [g for g in gs if g[0] != 'DEFINED-ONLY']
            gs.append(('DERIVES-ON-IMPORTS', 'b333', 'the source\'s (150)-(153) read link by link; superseding b315\'s DEFINED-ONLY'))
            gs.append(('MEASURED-ON-FAMILIES', 'b333', 'the third route at the thirteen arc cells'))
        cons.append((key, name, unfold, gs, reason))
    ranking = []
    for key, name, _u, gs, reason in cons:
        soft = min(gs, key=lambda g: S.ORDER.index(g[0]))
        ranking.append((S.ORDER.index(soft[0]), key, name, soft[0], reason))
    ranking.sort(key=lambda r: (r[0], r[1]))
    top = ranking[0][0]
    softest = [r[1] for r in ranking if r[0] == top]
    rec('  THE RE-RANK under b332\'s sealed rule, K5 updated (DEFINED-ONLY superseded by DERIVES-ON-IMPORTS; MEASURED-ON-FAMILIES added):')
    for i, (_o, k, n, g, _r) in enumerate(ranking, 1):
        rec('      %d. %s %-44s %s' % (i, k, n[:44], g))
    rec('  THE NEW SOFTEST : %s' % softest)
    seat = 'MET' if sorted(softest) == ['K5', 'K6'] else 'NOT MET'
    rec("  THE NAVIGATOR'S EXPECTATION FOR THE NEW SOFTEST : NOT STATED IN THE ORDER -- recorded as such, not scored.")
    rec("  THIS SEAT'S EXPECTATION (K5 and K6 tied at MEASURED-AT-COVERED-CELLS) : %s" % seat)
    return ranking, softest, seat, cons


OUT = []


def main():
    def rec(s=''):
        OUT.append(s)
        print(s)

    rec('=' * 100)
    rec('b333 -- THE ARCHIMEDEAN TERM DERIVED. ### THE CHAIN, THE THIRD ROUTE, THE RE-RANK.')
    rec('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    rec('  PHASE 1 -- NORMALIZATIONS BEFORE COUNTS, THEN THE CHAIN. Every quotation checked to be in the extract file.')
    missing = []
    for link, kind, quotes, identity in CHAIN:
        found = [q in extract for q in quotes]
        if not all(found):
            missing.append((link, [q for q, ok in zip(quotes, found) if not ok]))
        rec('  (%s) %-16s quotations %d/%d in the extract file ; %s' % (link, kind, sum(found), len(found), identity[:110]))
    ident_ok = identities(rec)
    if missing:
        verdict = 'RESISTS'
        rec('  ### VERDICT : RESISTS at %s -- a link\'s quotation is not in the extract file.' % missing)
    elif not ident_ok:
        verdict = 'RESISTS'
        rec('  ### VERDICT : RESISTS at (L5) -- the elementary identity does not hold numerically.')
    else:
        verdict = 'DERIVES-ON-IMPORT'
        rec('  ### VERDICT (chain) : DERIVES-ON-IMPORT -- the imports: (150), (151), (152)-(153), W_inf = -W_R; the identities: N4 and L5.')
    rec('')
    rec('  PHASE 2 -- THE THIRD ROUTE: (150) on the real side, mpmath.quad, the bump from its definition, no corpus code.')
    banked = read_b320_table()
    rec('  banked b320 table rows read : %d' % len(banked))
    r30 = third_route(30, rec)
    r50 = third_route(50, rec, quiet=True)
    rec('')
    rec('  THE BAR (sealed): |A_3 - A_digamma(b320)| <= %.0e and |A_3 - W_38(b320)| <= %.0e at every cell ; convergence |A_3(30) - A_3(50)| <= %.0e' % (BAR, BAR, CONVERGE))
    rec('  %-6s %13s %13s %13s %11s %11s %11s %11s' % ('a', 'A_3 (150)', 'A_dig(b320)', 'W_38(b320)', 'd_dig', 'd_38', 'd_conv', '|A_152-A_dig|'))
    worst = dict(dig=0.0, w38=0.0, conv=0.0, a152=0.0)
    fails = []
    for a in CELLS:
        cov, w38, adig = banked[a]
        A3 = r30[a]['A3']
        dd, d38, dc, d152 = abs(A3 - adig), abs(A3 - w38), abs(A3 - r50[a]['A3']), abs(r30[a]['A152'] - adig)
        worst = dict(dig=max(worst['dig'], dd), w38=max(worst['w38'], d38), conv=max(worst['conv'], dc), a152=max(worst['a152'], d152))
        flag = 'PASS' if (dd <= BAR and d38 <= BAR and dc <= CONVERGE) else '### FAIL ###'
        if flag != 'PASS':
            fails.append(a)
        rec('  %-6g %13.9f %13.9f %13.9f %11.3e %11.3e %11.3e %11.3e  %s' % (a, A3, adig, w38, dd, d38, dc, d152, flag))
    rec('  worst over the thirteen cells : d_dig %.3e ; d_38 %.3e ; d_conv %.3e ; |A_152 - A_dig| %.3e' % (worst['dig'], worst['w38'], worst['conv'], worst['a152']))
    route_ok = not fails
    if not route_ok:
        rec('  ### ### **THE THIRD ROUTE DISAGREES WITH THE RECORD AT %s -- REPORTED FIRST, AT FULL PROMINENCE.**' % fails)
        if worst['a152'] <= BAR:
            rec('  ### ### **THE SOURCE\'S (152) EVALUATED HERE AGREES WITH THE RECORD; THE SOURCE\'S (150) AS TRANSCRIBED DOES NOT:')
            rec('  ### ### **THE DIFFERING CONSTITUENT IS THE PRINCIPAL-VALUE FORM (150) AGAINST THE DIGAMMA FORM (152).**')
            verdict = 'MISMATCH at (L1): the principal-value form (150), as this seat transcribed it, is not minus the digamma form (152)'
        else:
            rec('  ### ### **BOTH FORMS EVALUATED HERE DISAGREE WITH THE RECORD: THE DIFFERING CONSTITUENT IS THE CORPUS\'S A ITSELF.**')
            verdict = 'MISMATCH at (L3): the corpus\'s A against the source\'s (152) as evaluated here'
    else:
        rec('  ### THE THIRD ROUTE AGREES WITH BOTH BANKED ROUTES INSIDE THE BAR AT EVERY CELL.')
    rec('')
    rec('  ### VERDICT : %s' % verdict)
    rec('')
    rec('  PHASE 3 -- THE RE-RANK.')
    ranking, softest, seat, cons = rerank(rec)
    payload = dict(verdict=verdict, chain=[list(c[:2]) + [c[3]] for c in CHAIN], identities=bool(ident_ok), bar=BAR, converge=CONVERGE,
                   cells={str(a): dict(A3=r30[a]['A3'], A3_dps50=r50[a]['A3'], A152=r30[a]['A152'], WR=r30[a]['WR'], f1=r30[a]['f1'],
                                       A_dig_b320=banked[a][2], W38_b320=banked[a][1], covered=banked[a][0]) for a in CELLS},
                   worst=worst, fails=fails, route_ok=route_ok, ranking=[list(r) for r in ranking], softest=softest, seat_expectation=seat,
                   navigator_expectation='NOT STATED IN THE ORDER', k5_grades=[list(g) for g in [c for c in cons if c[0] == 'K5'][0][3]])
    open(OUTJ + '.tmp', 'wb').write((json.dumps(payload, indent=1, ensure_ascii=False) + '\n').encode('utf-8'))
    os.replace(OUTJ + '.tmp', OUTJ)
    rec('=' * 100)
    return 0 if (verdict == 'DERIVES-ON-IMPORT' and route_ok) else 1


if __name__ == '__main__':
    code = main()
    base = 'b333_derive_run'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(OUT) + '\n')
    sys.exit(code)
