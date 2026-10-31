# -*- coding: utf-8 -*-
"""b729_onset_fit.py -- (R339)(7): H-ONSET-C, FITTED ON FIVE AND TESTED ON TWO, SAID SO.

### THE READING, FIXED HERE AND COMMITTED BEFORE ANY FIGURE AT off44 OR off24:
###   THE FIT: from data/b728_onset_table.txt :30-:34 alone, the five computed onsets' pairs x = log(M_C / (P + A)_C), y = (beta - 1/2) a*, as banked;
###     y = alpha + kappa x by ordinary least squares on the five, each row's residual printed in y and in a (residual / (beta - 1/2)); off52 is a bound and enters no fit.
###     Beside the residuals: each row left out in turn, the four-point fit's a at that row, so the reader sees how far five points carry a sixth.
###   THE FORM AT ONE RADIUS: b707's C window at gamma_0 = the list's gamma (b725's window_at, imported unedited), M_C = b725's mass over the rows named on (b728's
###     correction, its online(), imported unedited), (P + A)_C = khat(i/2) + khat(-i/2) as terms709 builds P, plus b725's arch.
###     d(a) = (beta - 1/2) a_ball - alpha - kappa log(M_C / (P + A)_C), UNDEFINED where the log is not certified positive-argument.
###   a*_pred: read at the ladder's rungs (b707's seven, 32 to 192, and log 2 at the foot), and above the ladder at 256 and 384 where d < 0 at 192: the least rung with
###     d >= 0 whose left neighbour reads d < 0, then bisection on the midpoints to 1e-6 in a. d >= 0 at the foot, or an undefined left neighbour: printed, no a*_pred.
### THE CONTROLS, BEFORE THE POST HOC ROWS: (C1) M_C and (P + A)_C recomputed at each of the five onset radii against the table, within 1e-5 relative;
###   (C2) at off18's onset radius P + A read twice, the second through terms709's own P, within its ball (one window, two routes).
### Routes: fit [--bank]    the fit and its residuals; reads the bank alone, runs no form ; banks data/b729_onset_fit.txt
###         control [--bank] (C1), (C2), then the rule at the five, POST HOC ; appends to the same bank
###         predict [--bank] off44 and off24: M_C, (P + A)_C and d at the rungs, a*_pred ; banks data/b729_onset_pred.txt ; refused until the registration is committed
### Written by the Write tool at b729; it writes those two banks and nothing else. Every form value a ball at 128 bits. Nothing here proves RH or GRH.
"""
import math
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TABLE = os.path.join(D, 'b728_onset_table.txt')
FIT_BANK = os.path.join(D, 'b729_onset_fit.txt')
PRED_BANK = os.path.join(D, 'b729_onset_pred.txt')
REG = 'data/b729_registrations.txt'
NAMES = ('rho0', 'band', 'off12', 'off18', 'off27')
TOL_A = 1e-6
FALSIFIER = 0.05
ABOVE = (('256', '256'), ('384', '384'))
BRACKET = dict(off24=(9.704061, 10.514991), off44=(10.514991, None))       # ### data/b725_onset_mass.txt :20, :16: off24's coarse bracket, off44 positive to 2 log 192
ROW = re.compile(r'^  (\w+)\s+M_C ([\d.]+) \+- \S+ \| \(P \+ A\)_C ([\d.]+) \+- \S+ \| PR_C \S+ \+- \S+ \| \(beta-1/2\) a ([\d.]+) \+- \S+ \| log\(M_C/\(P\+A\)_C\) (-?[\d.]+) \+-')
BETA = re.compile(r'^  (\w+)\s+beta ([\d.]+) \+- \S+ gamma ([\d.]+) \+- \S+ (\S+) a ([\d.]+) \+-')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def banked():
    """the table's rows, by label: M, PA, y, x, beta, gamma, a; refused unless the five are read once each."""
    rows = {}
    with open(TABLE, encoding='utf-8') as fh:
        for l in fh:
            m = BETA.match(l)
            if m:
                rows.setdefault(m.group(1), {}).update(beta=float(m.group(2)), gamma=float(m.group(3)), point=m.group(4), a=float(m.group(5)))
            m = ROW.match(l)
            if m:
                rows.setdefault(m.group(1), {}).update(M=float(m.group(2)), PA=float(m.group(3)), y=float(m.group(4)), x=float(m.group(5)))
    miss = [n for n in NAMES if len(rows.get(n, {})) != 8]
    if miss:
        sys.exit('### THE TABLE`S ROWS NOT READ AT %s -- REFUSED' % miss)
    return rows


def ols(pts):
    n = len(pts)
    mx, my = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    k = sum((p[0] - mx) * (p[1] - my) for p in pts) / sxx
    return my - k * mx, k


def fit(*a):
    rows = banked()
    pts = [(rows[n]['x'], rows[n]['y']) for n in NAMES]
    al, ka = ols(pts)
    L = ['b729 -- (R339)(7): H-ONSET-C`S FIT ON THE FIVE COMPUTED ONSETS, POST HOC (%s)' % utc(), '',
         '### by tools/b729_onset_fit.py `fit`; from data/b728_onset_table.txt :30-:34 alone; no form run; off52 a bound and in no fit. Fitted on five: every row below is POST HOC and tests nothing.', '',
         '## THE FIT: y = (beta - 1/2) a*, x = log(M_C/(P+A)_C), BY LEAST SQUARES ON THE FIVE',
         '  alpha %.9f' % al, '  kappa %.9f' % ka, '',
         '## THE RESIDUALS, POST HOC (y - fit; in a: the residual / (beta - 1/2), and as a share of a*); BESIDE EACH THE ROW LEFT OUT, THE FOUR-POINT FIT`S a AT IT']
    worst, worstloo = 0.0, 0.0
    ss = 0.0
    for n in NAMES:
        r = rows[n]
        res = r['y'] - al - ka * r['x']
        ss += res * res
        b = r['beta'] - 0.5
        a4, k4 = ols([(rows[m]['x'], rows[m]['y']) for m in NAMES if m != n])
        aloo = (a4 + k4 * r['x']) / b
        share, loo = res / b / r['a'], r['a'] / aloo - 1
        worst, worstloo = max(worst, abs(share)), max(worstloo, abs(loo))
        L.append('  %-6s x %+.7f y %.6f fit %.6f residual %+.6f ; in a %+.5f of a* %.5f, %+.2f%% ; left out: alpha %.4f kappa %.4f, a %.5f, a*/a - 1 %+.2f%%' % (
            n, r['x'], r['y'], al + ka * r['x'], res, res / b, r['a'], 100 * share, a4, k4, aloo, 100 * loo))
    L += ['  the residual sum of squares %.6f on 3 degrees of freedom ; the largest residual as a share of a* %.2f%% ; the largest left-out miss %.2f%%' % (ss, 100 * worst, 100 * worstloo),
          '  the falsifier`s tolerance is 5%; x clusters: rho0 and band near -2.3, the three others near -0.7, so kappa is carried by two clusters, not by five free points.', '',
          '### ### **H-ONSET-C`S FIT, POST HOC: alpha %.6f ; kappa %.6f ; FIVE RESIDUALS PRINTED ; FITTED ON FIVE, NOTHING TESTED.**' % (al, ka)]
    print(NL.join(L), flush=True)
    if '--bank' in a:
        with open(FIT_BANK + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(FIT_BANK + '.tmp', FIT_BANK)
        print('written data/b729_onset_fit.txt')
    return al, ka


# ================================================================================ THE FORM, IMPORTED LATE: `fit` RUNS NONE OF IT
def form():
    import b725_onset_mass as OM
    import b728_onset_table as TB
    return OM, TB


def read_at(OM, TB, g0, a):
    from flint import acb
    Wd = OM.window_at(g0, a)
    M = OM.mass(Wd, TB.online())
    P = (Wd.khat(acb(0, 0.5)) + Wd.khat(acb(0, -0.5))).real
    PA = P + OM.arch(Wd)
    return dict(a_ball=2 * Wd.L, M=M, PA=PA)


def d_of(OM, TB, beta, g0, a, al, ka):
    from flint import arb
    r = read_at(OM, TB, g0, a)
    r['a'] = a
    q = r['M'] / r['PA']
    if not (r['PA'] > 0) or not (q > 0):
        r['d'] = None
        return r
    r['x'] = q.log()
    r['d'] = (beta - arb('0.5')) * r['a_ball'] - arb(repr(al)) - arb(repr(ka)) * r['x']
    return r


def rungs(OM):
    S = OM.S
    return [(n, 2 * math.log(float(OM.O7.arb(S.WIDTH[n]).mid()))) for n in S.LADDER] + [(n, 2 * math.log(float(w))) for n, w in ABOVE]


def rule(OM, TB, beta, g0, al, ka, out):
    """the registered rule; returns (a*_pred or None, the note)."""
    fmt = OM.fmt
    prev, hit = None, None
    for n, a in rungs(OM):
        r = d_of(OM, TB, beta, g0, a, al, ka)
        v = None if r['d'] is None else float(r['d'].mid())
        out('    rung %-5s a %.6f M_C %s (P+A)_C %s %s d %s' % (n, a, fmt(r['M'], 8), fmt(r['PA'], 8), 'x UNDEFINED' if v is None else 'x ' + fmt(r['x'], 7), 'UNDEFINED' if v is None else fmt(r['d'], 7)))
        if v is not None and v >= 0:
            hit = (n, a)
            break
        prev = (n, a, v)
    if hit is None:
        return None, 'NO RUNG TO 384 CARRIES d >= 0: NO a*_pred'
    if prev is None:
        return None, 'd >= 0 AT THE LADDER`S FOOT: NO a*_pred'
    if prev[2] is None:
        return None, 'THE LEFT NEIGHBOUR OF %s UNDEFINED: NO a*_pred' % hit[0]
    lo, hi = prev[1], hit[1]
    while hi - lo > TOL_A:
        mid = (lo + hi) / 2
        r = d_of(OM, TB, beta, g0, mid, al, ka)
        if r['d'] is not None and float(r['d'].mid()) >= 0:
            hi = mid
        else:
            lo = mid
    return hi, 'bisected in (%s, %s]' % (prev[0], hit[0])


def control(*a):
    OM, TB = form()
    from flint import acb, arb
    OM.S.guard('the control')
    rows = banked()
    al, ka = fit()
    L = ['', '## THE CONTROLS, BEFORE THE POST HOC ROWS (%s)' % utc()]

    def out(s=''):
        print(s, flush=True)
        L.append(s)

    ok = True
    for lab, b, g, *_r in TB.ZEROS[:5]:
        sg, tt = TB.row_of(lab, b, g)
        g0 = tt.mid().str(25, radius=False)
        r = read_at(OM, TB, g0, rows[lab]['a'])
        dm, dp = float(r['M'].mid()) / rows[lab]['M'] - 1, float(r['PA'].mid()) / rows[lab]['PA'] - 1
        hit = abs(dm) <= 1e-5 and abs(dp) <= 1e-5
        ok = ok and hit
        out('  (C1) %-6s M_C %s against %.8g, %+.2e ; (P+A)_C %s against %.8g, %+.2e ; %s' % (lab, OM.fmt(r['M'], 8), rows[lab]['M'], dm, OM.fmt(r['PA'], 8), rows[lab]['PA'], dp, 'AS WANTED' if hit else 'NOT AS WANTED'))
    sg, tt = TB.row_of('off18', '0.9105105144', '155.5508257')
    g0 = tt.mid().str(25, radius=False)
    Wd = OM.window_at(g0, rows['off18']['a'])
    P1 = (Wd.khat(acb(0, 0.5)) + Wd.khat(acb(0, -0.5))).real + OM.arch(Wd)
    P2 = read_at(OM, TB, g0, rows['off18']['a'])['PA']
    hit = abs(float((P1 - P2).mid())) <= 1e-20
    ok = ok and hit
    out('  (C2) off18 (P+A)_C twice: %s ; %s ; difference %.2e ; %s' % (OM.fmt(P1, 8), OM.fmt(P2, 8), abs(float((P1 - P2).mid())), 'AS WANTED' if hit else 'NOT AS WANTED'))
    if not ok:
        out('### A CONTROL NOT AS WANTED -- NO POST HOC ROW')
    else:
        out('')
        out('## THE RULE AT THE FIVE, POST HOC, DECIDING NOTHING')
        for lab, b, g, *_r in TB.ZEROS[:5]:
            sg, tt = TB.row_of(lab, b, g)
            g0 = tt.mid().str(25, radius=False)
            out('  %s' % lab)
            ap, note = rule(OM, TB, sg, g0, al, ka, out)
            out('  %-6s a*_pred %s ; %s ; a* %.6f ; a*/a*_pred - 1 %s' % (lab, 'NONE' if ap is None else '%.6f' % ap, note, rows[lab]['a'], 'n/a' if ap is None else '%+.2f%%' % (100 * (rows[lab]['a'] / ap - 1))))
    out('')
    out('### ### **H-ONSET-C`S CONTROLS: %s.**' % ('C1 AND C2 AS WANTED' if ok else 'NOT AS WANTED'))
    if '--bank' in a:
        with open(FIT_BANK, 'ab') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        print('appended to data/b729_onset_fit.txt')


def registered():
    r = subprocess.run(['git', '-C', ROOT, 'log', '--format=%h', '-1', '--', REG], capture_output=True, text=True)
    return r.stdout.strip()


def predict(*a):
    h = registered()
    if not h:
        sys.exit('### THE REGISTRATION NOT COMMITTED -- NO FIGURE AT off44 OR off24 ((R339)(N2))')
    OM, TB = form()
    OM.S.guard('the predictions')
    al, ka = fit()
    L = ['b729 -- (R339)(7): H-ONSET-C`S PREDICTIONS, BY A COMMIT OF THEIR OWN BEFORE ANY ONSET (%s)' % utc(), '',
         '### by tools/b729_onset_fit.py `predict`; the registration %s at relay %s; alpha %.9f, kappa %.9f; no onset computed.' % (REG, h, al, ka), '']

    def out(s=''):
        print(s, flush=True)
        L.append(s)

    for lab in ('off44', 'off24'):
        sg, tt = OM.the_list()['off'][lab]
        g0 = tt.mid().str(25, radius=False)
        out('%s: beta %.10f ; gamma0 %s' % (lab, float(sg.mid()), g0))
        ap, note = rule(OM, TB, sg, g0, al, ka, out)
        if ap is None:
            out('  a*_pred NONE ; %s' % note)
        else:
            out('  a*_pred %.6f ; %s ; falsified where a* lies outside [%.6f, %.6f]' % (ap, note, 0.95 * ap, 1.05 * ap))
            lo, hi = BRACKET[lab]
            if hi is None:
                out('  the banked bound a* > %.6f: a_-/a*_pred - 1 = %+.4f ; %s' % (lo, lo / ap - 1, 'REFUTED BY THE BOUND' if lo / ap - 1 > FALSIFIER else 'within the tolerance: a bound, NOT SCORABLE until an onset'))
            else:
                ok_ = max(0.0, min(hi, 1.05 * ap) - max(lo, 0.95 * ap))
                out('  the banked bracket (%.6f, %.6f]: the share of it inside the window %.1f%%, outside %.1f%% ; a HELD here reads at that weight' % (lo, hi, 100 * ok_ / (hi - lo), 100 - 100 * ok_ / (hi - lo)))
        out('')
    out('### ### **H-ONSET-C`S PREDICTIONS BANKED ; ONSETS COMPUTED 0.**')
    if '--bank' in a:
        with open(PRED_BANK + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(PRED_BANK + '.tmp', PRED_BANK)
        print('written data/b729_onset_pred.txt')


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('fit', 'control', 'predict'):
        sys.exit('usage: fit|control|predict [--bank]')
    globals()[sys.argv[1]](*sys.argv[2:])
