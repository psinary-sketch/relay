# -*- coding: utf-8 -*-
"""b728_onset_table.py -- (R338)(3): THE SIX BANKED ONSETS' TABLE, DERIVED BEFORE ANY REGISTRATION, POST HOC WHATEVER IT READS.

### THE READING, FIXED HERE AND COMMITTED BEFORE ANY FIGURE OF THIS TOOL:
###   the onset point: the banked grid point of each zero's family, the first read NEGATIVE (data/b709_grid.txt :441, :4501; data/b723_support.txt
###     :15, :21; data/b725_onset_mass.txt :14); off52 has no onset: the point is a_- = 2 log 192, read POSITIVE, and its row is a one-sided bound;
###   the windows: b709's C, N and C + N at that point (G9._window, imported unedited);
###   per window, as b707's terms build it (terms709): P = khat(i/2) + khat(-i/2), the archimedean A, the prime sum PR, S = P - PR + A;
###     and M = the sum over the on-line rows of the certified list, at +t and at -t, of khat(t).real (b725's mass, imported unedited), the
###     on-line rows being those whose name begins "on": b725's the_list() and data/b725_registrations.txt :36 read "does not begin off", which
###     also takes the 69 ref rows, the reflections 1 - beta of the off-line rows (tools/b709_pairs.py :852); this tool's first run, whose (C2)
###     read S - M - O = -0.5000 at every C window and no table row, found them; the mass below is over the 547 on rows of (R338)(3)'s words;
###   THE PRIMARY READING, the form on the template family at its own least direction: v = (v_1, v_2) the witness of b707's reading at the point;
###     M* = v_1^2 M_CC + 2 v_1 v_2 M_CN + v_2^2 M_NN, A* = the same in P + A, M_CN and (P + A)_CN by the polarisation of b707's gram;
###   BESIDE IT, NOT THE TEST: the C window alone, M_C and (P + A)_C, the window b725 read;
###   THE PAIR: (beta - 1/2) a* and log(M*/A*), the second UNDEFINED where M*/A* > 0 is not certified;
###   THE AGREEMENT OF (R338)(3): | (beta - 1/2) a* / log(M*/A*) - 1 | <= 0.10 at each of the five computed onsets, and off52's lower bound
###     (beta - 1/2) a_- not above 1.10 log(M/A) at its own point. Nothing is fitted; the C row decides nothing.
### THE CONTROLS, PRINTED BEFORE THE TABLE, A TABLE ROW REFUSED UNTIL BOTH READ AS WANTED:
###   (C1) the banked lambda_min at each of the five onset points recomputed, within 1e-8 relative, the reading NEGATIVE;
###   (C2) the identity at the C window, S = M + O + (the list's tail): O the off-line rows' four images each, |S - M - O| <= 1e-3 |M|.
### Routes: table [--bank] ; banks data/b728_onset_table.txt.
###         reread [--bank]: off18, the one zero where b725's falsifier fired, a*_pred by b725's predict with the list as b725 read it and with the on rows alone, so that its
###         REFUTED is read on the corrected sum; banks data/b728_onset_b725_reread.txt. Written by the Write tool at b728; it writes those two and nothing else.
### Every value a ball at 128 bits. Nothing here proves RH or GRH.
"""
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b725_onset_mass as OM      # noqa: E402  ### the list, b725's mass: imported unedited
from flint import acb, arb, fmpq  # noqa: E402

S, O7, G9 = OM.S, OM.O7, OM.G9
bs, bl, fmt = OM.bs, OM.bl, OM.fmt
BANK = os.path.join(D, 'b728_onset_table.txt')
# ### (label, list beta, list gamma, lo rung, hi rung, the point, the banked a*, the banked lambda_min, its bank)
ZEROS = (('rho0', '0.9532604748', '16.29021', 'log2', '32', 'mid929_937', '6.838396011', '-0.003719132066', 'data/b709_grid.txt :409'),
         ('band', '0.7979971572', '29.551761', '128', '192', 'rung32381', '10.38532711', '-3.530086238e-5', 'data/b709_grid.txt :3629'),
         ('off12', '0.9515046580', '107.399291', '64', '96', 'mid5179_5189', '8.553331773', '-4.953079012e-5', 'data/b723_support.txt :15'),
         ('off18', '0.9105105144', '155.5508257', '128', '192', 'mid26959_26981', '10.20248033', '-0.0002229856298', 'data/b725_onset_mass.txt :14'),
         ('off27', '0.9107626196', '218.700845', '128', '192', 'mid19267_19273', '9.866304749', '-0.0001322565600', 'data/b723_support.txt :21'),
         ('off52', '0.9109585427', '355.531957', '128', '192', 'a-', None, None, 'data/b725_onset_mass.txt :17 ; data/b725_onset_mass_rule.txt'))


_ON = []


def online():
    """the ordinates of the rows named on*, read once: the certified on-line zeros, beta = 1/2 exactly."""
    if not _ON:
        import b709_pairs as P9
        import b711_list as L11
        rows = P9.extended_rows(L11.units(), L11.top())[0]
        bad = [n for n, sg, tt in rows if n.startswith('on') and sg.mid().str(5, radius=False) not in ('0.5', '0.50000')]
        if bad:
            sys.exit('### A ROW NAMED on NOT AT beta 1/2: %s -- REFUSED' % bad[:3])
        _ON.extend(tt for n, sg, tt in rows if n.startswith('on'))
    return _ON


def row_of(lab, b, g):
    off = OM.the_list()['off']
    hit = [n for n, (sg, tt) in off.items() if abs(float(sg.mid()) - float(b)) < 5e-5 and abs(float(tt.mid()) - float(g)) < 5e-3]
    if len(hit) != 1 or (lab.startswith('off') and hit[0] != lab):
        sys.exit('### THE BANKED ZERO %s NOT MATCHED ONCE IN THE LIST (%s) -- REFUSED' % (lab, hit))
    return off[hit[0]]


def point(lab, g0, lo, hi, name):
    S.register(lab, g0, lo, hi)
    pts = [p for p in G9.grid(lab) if p['name'] == name]
    if len(pts) != 1:
        sys.exit('### THE POINT %s NOT ON %s`S GRID -- REFUSED' % (name, lab))
    return pts[0]


def off_sum(Wd):
    """the off-line rows' four images: z = +-t +- i (beta - 1/2)."""
    O = arb(0)
    half = arb('0.5')
    for _n, (sg, tt) in OM.the_list()['off'].items():
        d = sg - half
        for x in (tt, -tt):
            for y in (d, -d):
                O += Wd.khat(acb(x, y)).real
    return O


def quad(v, cc, nn, cn):
    return v[0] * v[0] * cc + 2 * v[0] * v[1] * cn + v[1] * v[1] * nn


def rowread(lab, b, g, lo, hi, name):
    t0 = time.time()
    sg, tt = row_of(lab, b, g)
    g0 = tt.mid().str(25, radius=False)
    pt = point(lab, g0, lo, hi, name)
    on = online()
    us, Ms, Os = {}, {}, {}
    for kd in ('C', 'N', 'CN'):
        us[kd] = G9.terms709(lab, pt, kd, 'q0')
        Wd = G9._window(lab, pt, kd)
        Ms[kd] = OM.mass(Wd, on)
        if kd == 'C':
            Os[kd] = off_sum(Wd)
    G, Mg = O7.gram(us['C'], us['N'], us['CN'])
    rd = O7.reading(G, Mg)
    v = [arb(eval_q(x)) for x in rd['witness']]
    PA = dict((kd, bl(us[kd]['P']) + bl(us[kd]['A'])) for kd in us)
    PRs = dict((kd, bl(us[kd]['PR'])) for kd in us)
    pol = lambda d: (d['C'], d['N'], (d['CN'] - d['C'] - d['N']) / 2)
    Mstar, Astar, PRstar = quad(v, *pol(Ms)), quad(v, *pol(PA)), quad(v, *pol(PRs))
    a = bl(us['C']['a_radius'])
    return dict(lab=lab, beta=sg, gamma=tt, g0=g0, name=name, a=a, reading=rd, lmin=bl(rd['lmin']), Mstar=Mstar, Astar=Astar, PRstar=PRstar, Ms=Ms, PA=PA, PRs=PRs,
                S_C=bl(us['C']['S']), O_C=Os['C'], lhs=(sg - arb('0.5')) * a, secs=time.time() - t0)


def eval_q(s):
    if '/' in s:
        p, q = s.split('/')
        return fmpq(int(p), int(q))
    return fmpq(int(s))


def logratio(m, a_):
    q = m / a_
    return q.log() if q > 0 else None


def ranks(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    for k, i in enumerate(o):
        r[i] = float(k + 1)
    return r


def spearman(xs, ys):
    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    return 1 - 6 * sum((p - q) ** 2 for p, q in zip(rx, ry)) / float(n * (n * n - 1))


def table(*a):
    do_bank = '--bank' in a
    S.WORKERS = 1
    S.guard('the table')
    L = []

    def out(s=''):
        print(s, flush=True)
        L.append(s)

    out('b728 -- (R338)(3): THE SIX BANKED ONSETS, M* AND A* AT EACH ONSET POINT, POST HOC, NOTHING FITTED (%s)' % OM.utc())
    out()
    out('### by tools/b728_onset_table.py; the reading fixed in its head and committed before any figure. The ruling says seven; the banks hold six zeros, five onsets and off52`s bound.')
    out('### The list: %d on-line ordinates (rows named on), %d off-line rows with beta > 1/2 and their reflections, top %s.' % (len(online()), len(OM.the_list()['off']), OM.the_list()['top']))
    R = []
    for z in ZEROS:
        print('  reading %s ...' % z[0], flush=True)
        R.append(rowread(z[0], z[1], z[2], z[3], z[4], z[5]))
    out()
    out('## THE CONTROLS, BEFORE THE TABLE')
    ok1 = ok2 = True
    for z, r in zip(ZEROS, R):
        if z[7] is None:
            out('  (C1) %-6s no onset banked: the reading at a- %s, wanted POSITIVE' % (r['lab'], r['reading']['reading']))
            ok1 = ok1 and r['reading']['reading'] == S.POS
            continue
        got, want = float(r['lmin'].mid()), float(z[7])
        hit = abs(got / want - 1) <= 1e-8 and r['reading']['reading'] == S.NEG
        ok1 = ok1 and hit
        out('  (C1) %-6s lambda_min %s against the banked %s (%s) ; %s ; %s' % (r['lab'], fmt(r['lmin'], 10), z[7], z[8], r['reading']['reading'], 'AS WANTED' if hit else 'NOT AS WANTED'))
    for r in R:
        res = r['S_C'] - r['Ms']['C'] - r['O_C']
        rel = abs(float(res.mid())) / abs(float(r['Ms']['C'].mid()))
        hit = rel <= 1e-3
        ok2 = ok2 and hit
        out('  (C2) %-6s S_C %s ; M_C %s ; O_C %s ; S - M - O %s ; relative %.3e ; %s' % (r['lab'], fmt(r['S_C'], 8), fmt(r['Ms']['C'], 8), fmt(r['O_C'], 8), fmt(res, 4), rel, 'AS WANTED' if hit else 'NOT AS WANTED'))
    out('  (C1) %s ; (C2) %s' % ('AS WANTED' if ok1 else 'NOT AS WANTED', 'AS WANTED' if ok2 else 'NOT AS WANTED'))
    if not (ok1 and ok2):
        out('### A CONTROL NOT AS WANTED -- NO TABLE ROW PRINTED')
        if do_bank:
            OM.put_txt(BANK, L)
        sys.exit(1)
    out()
    out('## THE TABLE, POST HOC: THE PRIMARY READING, THE FORM`S LEAST DIRECTION v AT THE ONSET POINT')
    agree = True
    for r in R:
        lg = logratio(r['Mstar'], r['Astar'])
        r['log'] = lg
        bound = r['lab'] == 'off52'
        ratio = None if lg is None else r['lhs'] / lg
        r['ratio'] = ratio
        out('  %-6s beta %s gamma %s %s a %s v %s | M* %s | A* %s | PR* %s | (beta-1/2) a %s %s log(M*/A*) %s | ratio %s' % (
            r['lab'], fmt(r['beta'], 10), fmt(r['gamma'], 9), r['name'], fmt(r['a'], 10), r['reading']['witness'], fmt(r['Mstar'], 8), fmt(r['Astar'], 8), fmt(r['PRstar'], 8), fmt(r['lhs'], 7),
            '>=(a BOUND)' if bound else '|', 'UNDEFINED' if lg is None else fmt(lg, 7), 'UNDEFINED' if ratio is None else fmt(ratio, 6)))
        if lg is None:
            agree = False
        elif bound:
            agree = agree and float(r['lhs'].mid()) <= 1.10 * float(lg.mid())
        else:
            agree = agree and abs(float(ratio.mid()) - 1) <= 0.10
    out()
    out('## BESIDE IT, DECIDING NOTHING: THE C WINDOW ALONE, b725`S')
    for r in R:
        lg = logratio(r['Ms']['C'], r['PA']['C'])
        r['logC'] = lg
        out('  %-6s M_C %s | (P + A)_C %s | PR_C %s | (beta-1/2) a %s | log(M_C/(P+A)_C) %s | ratio %s' % (
            r['lab'], fmt(r['Ms']['C'], 8), fmt(r['PA']['C'], 8), fmt(r['PRs']['C'], 8), fmt(r['lhs'], 7), 'UNDEFINED' if lg is None else fmt(lg, 7), 'UNDEFINED' if lg is None else fmt(r['lhs'] / lg, 6)))
    out()
    out('## WHAT MOVES WITH GAMMA (rank correlation over the five computed onsets, on midpoints; off52 printed apart; no law fitted)')
    five_ = [r for r in R if r['lab'] != 'off52']
    gs = [float(r['gamma'].mid()) for r in five_]
    cols = [('M*', lambda r: r['Mstar']), ('A*', lambda r: r['Astar']), ('PR*', lambda r: r['PRstar']), ('M_C', lambda r: r['Ms']['C']), ('(P+A)_C', lambda r: r['PA']['C']),
            ('a*', lambda r: r['a']), ('(beta-1/2)a*', lambda r: r['lhs'])]
    moves = []
    for nm, f in cols:
        vals = [float(f(r).mid()) for r in five_]
        rho_ = spearman(gs, vals)
        moves.append((abs(rho_), nm, rho_))
        out('  %-14s by gamma: %s ; Spearman %+.2f' % (nm, ' '.join('%.6g' % x for x in vals), rho_))
    lgs = [r['log'] for r in five_]
    if all(x is not None for x in lgs):
        vals = [float(x.mid()) for x in lgs]
        out('  %-14s by gamma: %s ; Spearman %+.2f' % ('log(M*/A*)', ' '.join('%.6g' % x for x in vals), spearman(gs, vals)))
    top_ = max(moves)
    out('  THE QUANTITY MOVING MOST WITH GAMMA BY RANK, FIVE POINTS: %s (Spearman %+.2f)' % (top_[1], top_[2]))
    out()
    verdict = 'THE PAIRS AGREE WITHIN 10%: H-ONSET-MASS-2 MAY BE REGISTERED' if agree else 'THE PAIRS DO NOT AGREE WITHIN 10%: NO HYPOTHESIS REGISTERED, THE TABLE AN OBSERVATION'
    out('### ### **THE TABLE AT SIX ZEROS, POST HOC: C1 AND C2 AS WANTED ; %s.**' % verdict)
    if do_bank:
        OM.put_txt(BANK, L)
        print('written data/b728_onset_table.txt')


def reread(*a):
    """off18: predict with the_list() as b725 read it (616 ordinates), then with the on rows alone (547), both on the registered grid."""
    do_bank = '--bank' in a
    S.WORKERS = 1
    S.guard('the reread')
    L = []

    def out(s=''):
        print(s, flush=True)
        L.append(s)

    out('b728 -- b725`S H-ONSET-MASS READ ON THE ON-LINE ROWS ALONE (%s)' % OM.utc())
    out()
    out('### b725`s the_list() and data/b725_registrations.txt :36 took 69 ref rows, reflections of off-line zeros, as on-line; b725`s banks are not edited. By b725`s predict, imported unedited,')
    out('### with the list as b725 read it, then with the rows named on. The falsifier as registered: |a*/a*_pred - 1| > 0.05.')
    out()
    as725 = list(OM.the_list()['on'])
    banked = dict(off18=('10.20248033', 'THE ONSET'))
    fired = []
    for lab in ('off18',):                      # ### the one zero whose falsifier fired (data/b725_onset_mass.txt :22); off44 and off24 carry no computed onset
        sg, tt = OM.the_list()['off'][lab]
        OM.the_list()['on'] = as725
        r0 = OM.predict(sg, tt)
        OM.the_list()['on'] = list(online())
        r1 = OM.predict(sg, tt)
        out('  %s: as b725 read (%d ordinates): %s a*_pred %s | on rows alone (%d): %s a*_pred %s | banked: %s %s' % (
            lab, len(as725), r0['kind'], r0.get('a_pred'), len(online()), r1['kind'], r1.get('a_pred'), banked[lab][1], banked[lab][0] or ''))
        if lab == 'off18' and r1.get('a_pred') is not None:
            q = float(banked[lab][0]) / r1['a_pred'] - 1
            out('    off18: a*/a*_pred - 1 on the on rows alone = %+.5f ; %s' % (q, 'BEYOND 0.05: THE FALSIFIER FIRES ON THE CORRECTED SUM' if abs(q) > 0.05 else 'WITHIN 0.05: b725`S FIRING DOES NOT STAND ON THE CORRECTED SUM'))
            if abs(q) > 0.05:
                fired.append(lab)
    out()
    out('### ### **b725`S H-ONSET-MASS ON THE ON-LINE ROWS ALONE: THE FALSIFIER %s.**' % ('FIRES AT %s, REFUTED STANDS' % fired if fired else 'DOES NOT FIRE, REFUTED DOES NOT STAND ON THE CORRECTED SUM'))
    if do_bank:
        OM.put_txt(os.path.join(D, 'b728_onset_b725_reread.txt'), L)
        print('written data/b728_onset_b725_reread.txt')


ROUTES = dict(table=table, reread=reread)
if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ROUTES:
        sys.exit('usage: b728_onset_table.py table|reread [--bank]')
    ROUTES[sys.argv[1]](*sys.argv[2:])
