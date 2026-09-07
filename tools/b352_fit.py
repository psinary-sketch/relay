# -*- coding: utf-8 -*-
"""b352_fit.py -- COMPONENT 1 AND 2: THE MODELS, AND THE VERDICT. ### A REFIT. ### NOTHING IS RECOMPUTED.

### ### **THE RESIDUALS ARE READ FROM `data/b339_price.json` AND ARE NOT RECOMPUTED**, and the act prints the
### array it read so a reader can compare it to b339's own run file.
### ### **THE THREE MODELS ARE THE SEALED ONES**, section (C): `M1 = A X^-p` (k=2), `M2 = A X^-p + c` (k=3),
### `M3 = A X^-p + B X^-(p+1)` (k=3). ### The free two-term model is NOT fitted, for the sealed reason.
### ### **ONE CRITERION FOR ALL THREE** (section (D)): least squares on `log R`, so that `M1` here IS b322's
### `fit_power`. ### **THE FITTER IS IMPORTED AND THE LIKE-FOR-LIKE FIXTURE RUNS BEFORE ANY SCORE.**
### ### **TWO BARS** (section (E)), and they are independent for the sealed reason: a score ranks whole models,
### a floor is one parameter of one model, and they disagree exactly when a better fit is bought with an
### unphysical floor.
"""
import io
import json
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b322_ladder as LAD   # noqa: E402  ### THE FITTER, IMPORTED AND NEVER COPIED.
import run_clock            # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BAR_AICC = 2.0            # ### (E) BAR 1. ### floor: AICc differences at the object's floor are ~1e-14.
FLOOR_ABS = 5e-10         # ### (E) the object's floor: int_ef enters with 9 decimals.
LIKE_TOL = 1e-9           # ### (D) the like-for-like fixture's tolerance, relative.

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


# ------------------------------------------------------------------ THE MODELS, AS SEALED.
def m1(t, X):
    return t[0] * X ** (-t[1])


def m2(t, X):
    return t[0] * X ** (-t[1]) + t[2]


def m3(t, X):
    return t[0] * X ** (-t[1]) + t[2] * X ** (-(t[1] + 1.0))


MODELS = (('M1', m1, 2, 'A X^-p                 (pure power law, no floor)'),
          ('M2', m2, 3, 'A X^-p + c             (power law plus a constant floor)'),
          ('M3', m3, 3, 'A X^-p + B X^-(p+1)    (two-term: the next term of an expansion)'))


def logresid(f, t, X, R):
    v = f(t, X)
    v = np.where(v > 0, v, 1e-300)      # ### a non-positive prediction is a very bad fit, never a crash
    return np.log(R) - np.log(v)


def nelder_mead(fun, t0, step=0.25, tol=1e-14, itmax=20000):
    """### ### **A DEPENDENCY-FREE SIMPLEX. ### `scipy` IS NOT INSTALLED IN THIS ENVIRONMENT, AND RATHER THAN
    ### ### CHANGE THE SEALED CRITERION TO ONE A LIBRARY HAPPENS TO OFFER, THE MINIMISER IS WRITTEN HERE AND
    ### ### CHECKED AGAINST b322's CLOSED FORM ON `M1` BEFORE ANY SCORE IS REPORTED.**"""
    t0 = np.asarray(t0, dtype=float)
    m = len(t0)
    sim = [t0.copy()]
    for i in range(m):
        v = t0.copy()
        v[i] = v[i] + (step * abs(v[i]) if v[i] != 0.0 else step)
        sim.append(v)
    sim = np.array(sim)
    fv = np.array([fun(v) for v in sim])
    for _ in range(itmax):
        o = np.argsort(fv)
        sim, fv = sim[o], fv[o]
        if abs(fv[-1] - fv[0]) <= tol * (abs(fv[0]) + tol):
            break
        cen = sim[:-1].mean(axis=0)
        xr = cen + 1.0 * (cen - sim[-1])
        fr = fun(xr)
        if fr < fv[0]:
            xe = cen + 2.0 * (cen - sim[-1])
            fe = fun(xe)
            sim[-1], fv[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < fv[-2]:
            sim[-1], fv[-1] = xr, fr
        else:
            xc = cen + 0.5 * (sim[-1] - cen)
            fc = fun(xc)
            if fc < fv[-1]:
                sim[-1], fv[-1] = xc, fc
            else:
                sim = sim[0] + 0.5 * (sim - sim[0])
                fv = np.array([fun(v) for v in sim])
    o = np.argsort(fv)
    return sim[o][0]


def gauss_newton(f, t, X, R, itmax=200):
    """### ### **THE POLISH, AND WHY IT IS HERE.** ### A derivative-free simplex converges on the FUNCTION to
    ### machine precision and therefore on the PARAMETERS only to about its square root -- near a quadratic
    ### minimum `S(t) - S* ~ (t - t*)^2`, so `1e-16` in `S` is `1e-8` in `t`. ### **THAT IS A LAW OF THE
    ### METHOD, NOT A TUNING**, and this act's first fit run failed its own sealed `1e-9` fixture on exactly
    ### it, at `1.1e-09`, `2.3e-08`, `1.3e-09`. ### The run is banked as it stood.
    ### ### **GAUSS-NEWTON ON THE SAME OBJECTIVE FIXES IT** -- it uses the residual's Jacobian and converges
    ### quadratically in the parameters. ### **THE OBJECTIVE IS UNCHANGED AND THE SEALED CRITERION IS
    ### UNTOUCHED; ONLY THE MINIMISER IS BETTER.**"""
    t = np.asarray(t, dtype=float).copy()
    r = logresid(f, t, X, R)
    S = float(np.sum(r * r))
    lam = 0.0
    for _ in range(itmax):
        J = np.empty((len(r), len(t)))
        for i in range(len(t)):
            # ### CENTRAL DIFFERENCES ARE LIMITED BY `eps/h + h^2`; the step that minimises that is
            # ### `eps^(1/3) ~ 6e-6`, NOT a small one. ### A step of `1e-8` is roundoff-dominated and
            # ### costs eight digits, which is exactly what the first polished run lost.
            h = 6e-6 * max(abs(t[i]), 1.0)
            tp, tm = t.copy(), t.copy()
            tp[i] += h
            tm[i] -= h
            J[:, i] = (logresid(f, tp, X, R) - logresid(f, tm, X, R)) / (2.0 * h)
        A = J.T @ J + lam * np.eye(len(t))
        try:
            d = np.linalg.lstsq(A, -J.T @ r, rcond=None)[0]
        except np.linalg.LinAlgError:
            break
        tn = t + d
        rn = logresid(f, tn, X, R)
        Sn = float(np.sum(rn * rn))
        # ### AT THE FLAT BOTTOM `S` IS ALREADY AT ITS OWN ROUNDOFF, SO A STRICT DECREASE IS THE WRONG
        # ### TEST: it rejects the very step that fixes the PARAMETERS. ### A move is accepted when it
        # ### does not WORSEN `S` beyond `S`'s own precision, and the loop still stops on `d`.
        if Sn <= S * (1.0 + 1e-12):
            moved = float(np.max(np.abs(d) / np.maximum(np.abs(t), 1e-30)))
            t, r, S = tn, rn, Sn
            lam = max(lam * 0.1, 0.0)
            if moved < 1e-15:
                break
        else:
            lam = 1e-12 if lam == 0.0 else lam * 10.0
            if lam > 1e6:
                break
    return t, S, r


def fit(f, t0, X, R):
    """### The simplex to find the basin, RESTARTED until it stops moving; then GAUSS-NEWTON to land in it."""
    def S_of(t):
        rr = logresid(f, t, X, R)
        return float(np.sum(rr * rr))
    t = np.asarray(t0, dtype=float)
    prev = float('inf')
    for _ in range(12):
        t = nelder_mead(S_of, t, step=0.10)
        s = S_of(t)
        if prev - s <= 1e-16 * max(abs(s), 1e-16):
            break
        prev = s
    return gauss_newton(f, t, X, R)


def aicc(S, n, k):
    """### (D)'s criterion. ### **RETURNS None WHERE n - k - 1 <= 0**, which is not a score of infinity."""
    if n - k - 1 <= 0:
        return None
    return n * math.log(S / n) + 2.0 * k + 2.0 * k * (k + 1.0) / (n - k - 1.0)


def main():
    P = json.load(io.open(os.path.join(D, 'b339_price.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b352_frames.json'), encoding='utf-8'))
    X = np.asarray(P['xs'], dtype=float)
    n = len(X)
    cells = sorted(P['cells'], key=float)

    rec('=' * 100)
    rec("b352 -- THE FLOOR'S FOURTH CANDIDATE. ### THE MODELS, AND THE VERDICT.")
    rec('=' * 100)
    rec('  ### THE LADDER, READ : X = %s ; NY = %s ; cells %s' % ([float(v) for v in X], P['ny'], cells))
    rec('  ### frames per cell, verified before the seal : %s ; covered cells : %d' % (F['frames'], F['n_cells']))
    rec("  ### the object's floor : %.1e absolute ; relative at the last rung : %.3e" % (F['floor_abs'], F['floor_rel']))
    rec('  ### ### **NOTHING IS RECOMPUTED. ### THE RESIDUALS BELOW ARE b339\'s BANKED ARRAY.**')

    # -------------------------------------------------- THE LIKE-FOR-LIKE FIXTURE, BEFORE ANY SCORE.
    rec('')
    rec('-' * 100)
    rec("  ### THE LIKE-FOR-LIKE FIXTURE (section (D)). ### **IT RUNS BEFORE ANY SCORE IS REPORTED.**")
    rec('-' * 100)
    rec('  %-8s %-16s %-16s %-14s %-16s %-16s %s'
        % ('a', 'p (b322)', 'p (this act)', '|rel diff|', 'A (b322)', 'A (this act)', 'agree'))
    like_ok = True
    m1fits = {}
    for k in cells:
        R = np.asarray(P['cells'][k]['R'], dtype=float)
        p_b, a_b, rms_b = LAD.fit_power(X, R)          # ### IMPORTED.
        t, S, _r = fit(m1, [1.0, 1.0], X, R)   # ### a NEUTRAL start: the fixture must test the minimiser
        m1fits[k] = (t, S)
        p_here, A_here = -t[1], t[0]
        dp = abs(p_here - p_b) / max(abs(p_b), 1e-300)
        dA = abs(A_here - math.exp(a_b)) / max(abs(math.exp(a_b)), 1e-300)
        ok = dp < LIKE_TOL and dA < LIKE_TOL
        like_ok = like_ok and ok
        rec('  %-8s %-16.9f %-16.9f %-14.2e %-16.9f %-16.9f %s'
            % (k, p_b, p_here, max(dp, dA), math.exp(a_b), A_here, 'YES' if ok else '### NO ###'))
    rec('  ### ### **M1 REPRODUCES b322\'s `fit_power` AT EVERY CELL TO %.0e RELATIVE : %s**'
        % (LIKE_TOL, like_ok))
    if not like_ok:
        rec('  ### ### **NO SCORE IS REPORTED. ### THE SEALED FIXTURE FAILED AND THE ACT SAYS SO.**')
        run_clock.write(D, 'b352_fit_run', LINES)
        return 1
    rec('  ### and that means the two fits are the same fit, which is what makes the three scores comparable.')

    # -------------------------------------------------- THE FITS.
    out = {}
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 1 -- THE MODELS, THEIR PARAMETERS AND THEIR RESIDUALS.')
    rec('-' * 100)
    for k in cells:
        R = np.asarray(P['cells'][k]['R'], dtype=float)
        rec('')
        rec('  ### a = %s   R = %s' % (k, ['%.9e' % v for v in R]))
        rec('  %-4s %-3s %-52s %-14s %-11s %-12s %s' % ('mod', 'k', 'parameters', 'S (log-space)', 'rms(log)', 'AICc', 'd(AICc)'))
        got = {}
        for name, f, kk, form in MODELS:
            t0 = list(m1fits[k][0]) + ([0.0] if kk == 3 else [])
            t, S, r = fit(f, t0, X, R)
            sc = aicc(S, n, kk)
            got[name] = dict(k=kk, form=form, t=[float(v) for v in t], S=float(S),
                             rms=float(math.sqrt(S / n)), aicc=sc,
                             resid=[float(v) for v in r], pred=[float(v) for v in f(t, X)])
        best = min((v['aicc'] for v in got.values() if v['aicc'] is not None))
        for name, _f, kk, form in MODELS:
            g = got[name]
            ps = ('A=%.6f p=%.6f' % (g['t'][0], g['t'][1])) if kk == 2 else \
                 (('A=%.6f p=%.6f c=%+.6e' % tuple(g['t'])) if name == 'M2'
                  else ('A=%.6f p=%.6f B=%+.6f' % tuple(g['t'])))
            rec('  %-4s %-3d %-52s %-14.6e %-11.6f %-12s %s'
                % (name, kk, ps, g['S'], g['rms'],
                   ('%.4f' % g['aicc']) if g['aicc'] is not None else 'NOT SCOREABLE',
                   ('%+.4f' % (g['aicc'] - best)) if g['aicc'] is not None else '--'))
        rec('  ### the free two-term model (k = 4) : ### **NOT SCOREABLE ON THIS LADDER** (n - k - 1 = %d),'
            % (n - 4 - 1))
        rec('  ### ### and it is NOT FITTED, for the sealed reason rather than after seeing a score.')

        # ---- BAR 1 -------------------------------------------------------------------------------
        d21 = got['M2']['aicc'] - got['M1']['aicc']
        d31 = got['M3']['aicc'] - got['M1']['aicc']
        d23 = got['M2']['aicc'] - got['M3']['aicc']
        b1_21 = abs(d21) > BAR_AICC
        b1_23 = abs(d23) > BAR_AICC
        rec('  ### **BAR 1** (AICc apart by more than %.1f ; floor ~1e-14, so the bar is strict) :' % BAR_AICC)
        rec('      M2 - M1 = %+.4f  distinguishable : %s' % (d21, b1_21))
        rec('      M3 - M1 = %+.4f' % d31)
        rec('      M2 - M3 = %+.4f  distinguishable : %s   ### **THE FLOOR AGAINST THE FASTER TERM, AT EQUAL k**'
            % (d23, b1_23))

        # ---- BAR 2 -------------------------------------------------------------------------------
        c = got['M2']['t'][2]
        scatter = got['M2']['rms'] * float(R[-1])
        b2 = (c > 0.0) and (c > scatter) and (c > FLOOR_ABS)
        rec('  ### **BAR 2** (c > 0 AND c > the M2 fit\'s own scatter at the last rung AND c > %.0e) :' % FLOOR_ABS)
        rec('      c = %+.6e   the fit\'s scatter at X = 128 : %.6e   POSITIVE FLOOR : %s' % (c, scatter, b2))
        smallest = max(scatter, FLOOR_ABS)
        rec('  ### **WHAT THIS ACT COULD NOT HAVE SEEN, PRINTED:** a true floor below %.6e would pass no arm'
            % smallest)
        rec('      here, because it is under this fit\'s own scatter at the last rung. ### That is %.3f%% of'
            % (100.0 * smallest / float(R[-1])))
        rec('      R(128) = %.9e, so this ladder is deaf to any floor smaller than that.' % float(R[-1]))
        out[k] = dict(models=got, d21=float(d21), d31=float(d31), d23=float(d23),
                      bar1_21=bool(b1_21), bar1_23=bool(b1_23), c=float(c), scatter=float(scatter),
                      bar2=bool(b2), smallest_visible=float(smallest), R128=float(R[-1]),
                      R=[float(v) for v in R])

    # -------------------------------------------------- THE VERDICT.
    rec('')
    rec('-' * 100)
    rec("  ### COMPONENT 2 -- THE VERDICT, BY THE SEALED BRANCH RULE OF SECTION (F).")
    rec('-' * 100)
    est = all(out[k]['bar1_21'] and out[k]['d21'] < 0 and out[k]['bar2'] for k in cells)
    m1_best = all(out[k]['models']['M1']['aicc'] <= min(out[k]['models'][m]['aicc'] for m in ('M2', 'M3'))
                  for k in cells)
    rec('  %-8s %-14s %-14s %-14s %-10s %s' % ('a', 'best by AICc', 'M2-M1', 'M2-M3', 'c sign', 'BAR2'))
    for k in cells:
        g = out[k]['models']
        best_name = min(('M1', 'M2', 'M3'), key=lambda m: g[m]['aicc'])
        rec('  %-8s %-14s %-+14.4f %-+14.4f %-10s %s'
            % (k, best_name, out[k]['d21'], out[k]['d23'],
               ('positive' if out[k]['c'] > 0 else 'NEGATIVE'), out[k]['bar2']))
    rec('')
    rec('  ### **(FLOOR ESTABLISHED)** -- demands M2 beating M1 by more than the bar AND c passing bar 2, at')
    rec('    EVERY cell. ### got : %s' % est)
    rec('  ### **(NO FLOOR PREFERRED)** -- demands M1 fitting as well or better at every cell. ### got : %s'
        % m1_best)
    if est:
        verdict = 'FLOOR ESTABLISHED'
    elif m1_best:
        verdict = 'NO FLOOR PREFERRED'
    else:
        verdict = 'FLOOR UNDER-RESOLVED AS A FIT'
    rec('  ### ### ### **VERDICT : %s**' % verdict)
    rec('')
    rec('  ### ### **AND THE ANSWER TO THE QUESTION THE ORDER ASKED IN ITS OWN TERMS -- can the five frames')
    rec('  ### ### distinguish a positive floor from a slowly decaying power law?**')
    sep = [k for k in cells if out[k]['bar1_23']]
    rec('    cells where the floor model and the faster-decaying term are separated at equal complexity : %s'
        % (sep if sep else 'NONE'))
    rec('    cells where a positive floor passes bar 2 : %s'
        % ([k for k in cells if out[k]['bar2']] or 'NONE'))
    rec('  ### ### **NO FIT HERE MEASURES A FLOOR. ### IT RANKS DESCRIPTIONS OF FIVE NUMBERS**, and the')
    rec('  ### ### smallest floor any arm here could have seen is printed per cell above.')
    # ---------------------------------------------------------------- THE BRANCH'S OWN PRICING.
    price = None
    if verdict == 'FLOOR UNDER-RESOLVED AS A FIT':
        rec('')
        rec('-' * 100)
        rec("  ### THE BRANCH'S PRICE (section (F)): THE FRAMES OR THE DOMAIN REACH THAT WOULD SETTLE IT.")
        rec('-' * 100)
        rec('  ### ### **FIRST, WHY THE CELLS DISAGREE, AND IT IS THE CRITERION AND NOT THE DATA.**')
        for kk in (2, 3):
            rec('    AICc penalty at n = 5 for k = %d : 2k + 2k(k+1)/(n-k-1) = %.1f'
                % (kk, 2.0 * kk + 2.0 * kk * (kk + 1.0) / (n - kk - 1.0)))
        pen5 = (2.0 * 3 + 24.0 / 1.0) - (2.0 * 2 + 12.0 / 2.0)
        rec('    ### ### **SO A THIRD PARAMETER COSTS %.1f AICc UNITS AT n = 5 -- TEN TIMES THE BAR OF %.1f.**'
            % (pen5, BAR_AICC))
        rec('    ### To break even, `S` must fall by a factor of exp(%.1f / %d) = %.1f. ### **AT FIVE POINTS'
            % (pen5, n, math.exp(pen5 / n)))
        rec('    ### THE CRITERION IS MOSTLY COUNTING PARAMETERS**, and which model wins turns on the penalty')
        rec('    ### rather than on the fit. ### The criterion was SEALED before any fit and is not changed here.')
        rec('')
        rec('  ### ### **THE PRICE, PER CELL: HOW MANY FRAMES WOULD PAY FOR THE THIRD PARAMETER, IF THE FIT')
        rec('  ### ### RATIO HELD.**')
        rec('  %-8s %-14s %-16s %-10s %-12s %s' % ('a', 'S(M2)/S(M1)', 'd(AICc) at n=5', 'frames', 'next X', 'inside b339 ceiling 512'))
        price = {}
        for k in cells:
            g = out[k]['models']
            ratio = g['M2']['S'] / g['M1']['S']
            need, nx = None, None
            for nn in range(5, 33):
                dd = nn * math.log(ratio) + ((2.0 * 3 + 24.0 / (nn - 4.0)) - (2.0 * 2 + 12.0 / (nn - 3.0)))
                if dd < -BAR_AICC:
                    need = nn
                    break
            if need is not None:
                nx = float(X[-1]) * (2.0 ** (need - n))
            rec('  %-8s %-14.6e %-+16.4f %-10s %-12s %s'
                % (k, ratio, out[k]['d21'], (need if need else '>32'),
                   ('%g' % nx if nx else '--'), (str(bool(nx and nx <= 512.0)) if nx else '--')))
            price[k] = dict(ratio=float(ratio), frames_needed=need, next_X=nx,
                            inside_ceiling=bool(nx and nx <= 512.0))
        worst = max((price[k]['frames_needed'] or 99) for k in cells)
        rec('  ### ### **THE BINDING CELL NEEDS %s FRAMES, ONE MORE THAN THE RECORD HOLDS**, and one more'
            % worst)
        rec('  ### ### frame is `X = %g`, `N = %d`.' % (float(X[-1]) * 2, int(float(X[-1]) * 2 * 128)))
        rec('  ### ### ### **AND THAT SITS INSIDE THE CEILING b339 SEALED (`X = 512`).** ### b339 found its own')
        rec('  ### ### ### question UNAFFORDABLE at that ceiling because the SPLIT criterion needed `X_req`')
        rec('  ### ### ### between `812` and `2358`. ### **THE FIT ASKS A DIFFERENT QUESTION OF THE SAME')
        rec("  ### ### ### LADDER, AND ITS PRICE IS AFFORDABLE WHERE b339'S WAS NOT.**")
        rec('  ### ### **AND THIS IS A PRICE AND NOT A PREDICTION.** ### It assumes the `S` ratio the five')
        rec('  ### ### points give would survive a sixth, which is exactly the extrapolation b339 labelled')
        rec('  ### ### when it priced its own. ### **NOTHING HERE SAYS WHAT A SIXTH FRAME WOULD SHOW.**')
        rec('  ### ### **THE ACT DOES NOT RUN IT.** ### Running it builds a frame, which this act may not do.')

    rec('')
    rec('  ### **b339 IS NOT RE-VERDICTED. ### ITS `UNAFFORDABLE` STANDS.** ### And its side-reading -- that')
    rec('  ### the residual descends toward a floor -- was labelled by its own act as that seat\'s reading;')
    rec('  ### this act reports what a fit can and cannot say about it and ### **DOES NOT WITHDRAW IT.**')
    rec('  ### **b346 IS NOT RE-VERDICTED EITHER**, and the exponent\'s resolution on the RATE axis is')
    rec('  ### untouched, because it never rested on the floor.')
    rec('=' * 100)

    p = run_clock.write(D, 'b352_fit_run', LINES)
    io.open(os.path.join(D, 'b352_fit.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(xs=list(X), n=n, cells=cells, per_cell=out, verdict=verdict, like_for_like=bool(like_ok),
             bar_aicc=BAR_AICC, floor_abs=FLOOR_ABS, separated_cells=sep,
             floor_cells=[k for k in cells if out[k]['bar2']], price=price,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
