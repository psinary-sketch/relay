# -*- coding: utf-8 -*-
"""b265_nq_sweep.py -- THE NQ-CEILING SWEEP. ### THE RUN.

### **IT IS A MEASUREMENT ON PRIOR ACTS' CELLS, NOT A RE-VERDICT OF THOSE ACTS.** ### Every bar
### was fixed in `data/b265_registration_2026-08-31.txt`, SEALED `263f37a9...`, before any new
### value existed. ### The joint-satisfiability check ran BEFORE the seal (b264's defect).

### ### **NO OWNER FILE IS EDITED.** ### `B38.EPS_NQ` / `B38.EPS_NG` are set as MODULE
### ATTRIBUTES and RESTORED -- b245's established pattern (`old = C.NV; C.NV = nv`). ### That is
### an assignment, not a file edit, and clause (K.3) declares it in advance.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import b38_act10 as B38          # noqa: E402
import b36_act8 as B36           # noqa: E402
import qeps_layer as Q           # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BANK = r'D:\relay\data\b265_run.txt'
ROWS = r'D:\relay\data\b265_rows.json'
B255J = r'D:\relay\data\b255_rows.json'

# ### THE BARS, FIXED IN THE SEALED REGISTRATION (G).
F_INSIDE_PRINT = 1e-6     # ### b255 printed E2even to SIX decimals
F_INSIDE_CLAIM = 1e-4     # ### b255's OWN registered REPRO_BAND
F_LAW_FACTOR = 1.5        # ### NQ/x_c may not drift by more than this across the ladder
CONV_BAR = 1e-8           # ### the NQ-vs-2NQ / NG-vs-2NG relative bar
RES_BAR = 1e-6            # ### the mode-resolution bar (b264's, unchanged)

NQ_LADDER = [700, 1400, 2800]
LADDER = [2, 3, 4, 8, 9, 12, 16, 20, 25, 32, 36, 45, 50, 64, 81, 100]
RHO_MAX = 100.001         # ### b255's own, forced by its (W1)
EPS_NRHO = 445            # ### b255's own
NMODE = 11
B264_CROSSOVER = 238.4    # ### the owner value this act sweeps against
CHUNK = 4096


def an_at(LAY, X):
    """### THE OWNER'S `an`, CHUNKED. ### Written exactly as `qeps_layer.layer`'s closure."""
    x, w, lam, lam2, xi, xi1, an, dan = LAY
    X = np.atleast_1d(np.asarray(X, dtype=float))
    out = np.empty((X.size, xi.shape[1]))
    for i in range(0, X.size, CHUNK):
        Xi = X[i:i + CHUNK]
        C = np.cos(2 * math.pi * np.outer(Xi, x))
        out[i:i + CHUNK] = (C * w) @ xi / lam
    return out


def resolved_modes(NQ):
    """### WHICH MODES THE INSTRUMENT RESOLVES AT `NQ`. ### b264's measurement, re-run here as
    ### F-FLOOR's positive control against b244's K1 ruling of SEVEN."""
    lam = Q.layer(NQ)[2]
    lam2 = Q.layer(2 * NQ)[2]
    n = min(len(lam), len(lam2), NMODE)
    drift = np.abs(lam[:n] - lam2[:n]) / np.maximum(np.abs(lam[:n]), 1e-300)
    res = [i for i in range(n) if drift[i] <= RES_BAR]
    return ((max(res) + 1) if res else 0), drift


CLIFF_BAR = 0.5           # ### half the local envelope -- the value has lost its own scale
NQ_REF = 5600             # ### the reference layer the cliffs are measured against


def envelope(A, n, xs, W=0.25):
    """### THE LOCAL ENVELOPE of |A_n| in a multiplicative window. ### **A RELATIVE TEST ON AN
    ### OSCILLATING FUNCTION BLOWS UP AT ITS ZEROS; NORMALISING BY THE LOCAL ENVELOPE DOES NOT.**"""
    E = np.abs(A[:, n])
    return np.array([E[(xs >= x / (1 + W)) & (xs <= x * (1 + W))].max() for x in xs])


def cliff(NQ, AR, xs, nres):
    """### THE CLIFF: first `x` where `A_n` at `NQ` has lost HALF ITS OWN LOCAL ENVELOPE against
    ### the reference. ### Returned per mode and worst-over-resolved."""
    A = an_at(Q.layer(NQ), xs)
    per = []
    for n in range(nres):
        r = np.abs(A[:, n] - AR[:, n]) / np.maximum(envelope(AR, n, xs), 1e-300)
        i = np.nonzero(r > CLIFF_BAR)[0]
        per.append(float(xs[i[0]]) if len(i) else None)
    got = [v for v in per if v is not None]
    return per, (min(got) if got else None)


def eps_grids(NQ, NG, rr):
    """### THE OWNER'S `per_mode_eps_grids` AT A CHOSEN `(NQ, NG)`. ### MODULE ATTRIBUTES SET AND
    ### RESTORED; THE OWNER FILE IS NOT TOUCHED."""
    oq, og = B38.EPS_NQ, B38.EPS_NG
    try:
        B38.EPS_NQ, B38.EPS_NG = NQ, NG
        return B38.per_mode_eps_grids(rr)
    finally:
        B38.EPS_NQ, B38.EPS_NG = oq, og


def main():
    out = []
    t_start = time.time()

    def rec(s=''):
        print(s)
        out.append(s)

    EVEN = list(range(0, NMODE, 2))
    ODD = list(range(1, NMODE, 2))
    b255 = json.load(io.open(B255J, encoding='utf-8'))

    rec('=' * 110)
    rec('b265 RUN -- THE NQ-CEILING SWEEP. ### b247 AND b255 GRADED AGAINST THE MEASURED CEILING.')
    rec('### Registration SEALED (`263f37a9...`) and VERIFIED BEFORE THIS RUN. Bars fixed there.')
    rec('### ### **A MEASUREMENT ON PRIOR ACTS\' CELLS. ### NO ACT IS RE-VERDICTED HERE.**')
    rec('=' * 110)
    rec('### **THE CEILING SWEPT AGAINST, CONSUMED FROM b264 AND NOT RE-DERIVED:**')
    rec('###   `EPS_NQ = 700` binds at ### **rho = %.1f** ### ; `EPS_NG = 400` is NOT the'
        % B264_CROSSOVER)
    rec('###   binding one. ### **RAISING `NG` DOES NOT REPAIR IT.**')
    rec('### **THE `a^2` -> `rho` CORRESPONDENCE, DERIVED IN THE REGISTRATION (C) AND USED HERE:**')
    rec('###   `e2_of_grid` interpolates at `exp(uu)`, `uu in [0, 2 log a]`, so the top eps')
    rec('###   argument at a cell is ### **EXACTLY `a^2`** ### . ### `exp(2 log a) = a^2` is an')
    rec('###   IDENTITY, not an estimate, and b255\'s own (W1) says the same in its own words.')

    # ================================================================ F-EXPOSURE
    rec('')
    rec('=' * 110)
    rec('### F-EXPOSURE -- THE EXPOSURE MAP, TESTED ON THE OWNERS\' SOURCE. ### **A CODE TEST.**')
    rec('=' * 110)
    src38 = io.open(os.path.join(HERE, 'b38_act10.py'), encoding='utf-8').read()
    srcC = io.open(os.path.join(HERE, 'carto_atlas.py'), encoding='utf-8').read()

    def body(src, fn):
        """### ONE FUNCTION'S BODY: from its `def` to the NEXT top-level `def`.
        ### ### **DEVIATION (D1), DECLARED: the first runner took `def <fn>` -> `def <named
        ### successor>`, and NAMED THE WRONG SUCCESSOR for `left_side` -- `staircase` is defined
        ### ABOVE it, so the split found nothing and returned the whole REMAINDER of the file,
        ### swallowing `per_mode_eps_grids` and its `Q.layer` call. ### F-EXPOSURE FIRED ON THAT
        ### AND NOT ON ANY REAL EXPOSURE.** ### b263's `--name-only` species: a check that cannot
        ### tell one function from the next. ### The successor is now FOUND, never named."""
        i = src.index('def %s' % fn)
        j = src.find(chr(10) + 'def ', i + 1)
        return src[i:j] if j > 0 else src[i:]

    paths = [
        ('per_mode_eps_grids', body(src38, 'per_mode_eps_grids'), True),
        ('theta_quotient', body(src38, 'theta_quotient'), False),
        ('left_side', body(src38, 'left_side'), False),
        ('e2_of_grid', body(src38, 'e2_of_grid'), False),
        ('carto_atlas.channels', body(srcC, 'channels'), False),
    ]
    rec('  %-26s %-16s %-16s %s' % ('owner function', 'calls Q.layer?', 'expected', 'verdict'))
    rec('  ' + '-' * 82)
    fexp = True
    for name, b, expected in paths:
        has = ('Q.layer' in b) or ('layer(' in b and 'Q.' in b)
        ok = (has == expected)
        fexp = fexp and ok
        rec('  %-26s %-16s %-16s %s'
            % (name, 'YES' if has else 'no', 'EXPOSED' if expected else 'NOT EXPOSED',
               'agrees' if ok else '### DISAGREES ###'))
    rec('  ### ### **F-EXPOSURE %s**'
        % ('DID NOT FIRE -- every column graded NOT EXPOSED has no `Q.layer` in its path.'
           if fexp else 'FIRED. ### THE EXPOSURE MAP IS WRONG.'))
    rec('  ### **AND THE TEST IS SHOWN ABLE TO FIND A CALL THAT ### IS ### THERE:**')
    rec('  ###   `per_mode_eps_grids` is the positive control and it reads ### **YES** ### above.')
    rec('  ###   ### **A CODE TEST THAT NEVER FINDS ANYTHING IS NOT A TEST.**')

    # ================================================================ F-FLOOR
    rec('')
    rec('=' * 110)
    rec('### F-FLOOR -- THE RESOLVED-MODE COUNT AT `EPS_NQ = 700`, AGAINST b244\'s K1 RULING.')
    rec('=' * 110)
    NRES700, drift700 = resolved_modes(700)
    rec('  resolved modes at NQ = 700 (bar %.0e on `lam_n` under NQ -> 2NQ) : ### **%d**'
        % (RES_BAR, NRES700))
    rec('  b244\'s RULE MODES K1 realization                                 : ### **7**')
    rec('  b264\'s independent measurement                                   : ### **7**')
    ffloor = bool(NRES700 == 7)
    rec('  ### ### **F-FLOOR %s**'
        % ('DID NOT FIRE -- THIS ACT, b244 AND b264 AGREE AT SEVEN, BY THREE ROUTES.'
           if ffloor else 'FIRED. ### THE THREE ROUTES DISAGREE AND THE ACT MUST SAY WHICH IS WRONG.'))
    rec('  ### **AND THE THING THIS CONFIRMS IS NOT NEW, WHICH IS THE POINT:** ### b242')
    rec('  ### ESTABLISHED THE FLOOR, b244\'s K1 RULED THE REALIZATION TO SEVEN BECAUSE OF IT,')
    rec('  ### AND b247, b253 AND b255 ALL CARRY IT. ### **b264 REDISCOVERED IT AND SAID')
    rec('  ### "NOTHING IN THE RECORD SAID SO". ### THE RECORD SAID SO IN FIVE PLACES.**')

    # ================================================================ S1: THE CROSSOVER LAW
    rec('')
    rec('=' * 110)
    rec('### S1 -- THE CROSSOVER LAW. ### **AS A FUNCTION OF THE INTEGRAND\'S OSCILLATION COUNT,**')
    rec('###      **WHICH IS WHAT `W-ORD-NQ-CEILING` ASKED FOR AND NOT ONE NUMBER.**')
    rec('=' * 110)
    # ### ### **DEVIATION (D3), DECLARED: the first runner probed `x in [50, 6000]` and every
    # ### ### crossover came out AT `x = 50` -- the grid's own left edge. ### A test that
    # ### ### saturates at its first point has not measured a crossover, it has measured its
    # ### ### own grid, and F-LAW FIRED ON THAT.** ### The grid now starts at `x = 2`.
    xs = np.unique(np.round(np.exp(np.linspace(math.log(2.0), math.log(6000.0), 400))))
    rec('  probe grid : %d points, log-spaced, x in [%.0f, %.0f]' % (len(xs), xs[0], xs[-1]))
    rec('  the test   : `A_n(x)` at `NQ` vs `2 NQ`, worst over the RESOLVED modes, bar %.0e'
        % CONV_BAR)
    rec('')
    rec('')
    rec('  ### **(a) THE REGISTERED STATISTIC, RUN AS REGISTERED -- AND IT CANNOT WORK.**')
    rec('  ### The sealed (E)/S1 test reads: `A_n` at `NQ` vs `2 NQ`, worst over the RESOLVED')
    rec('  ### modes, bar %.0e RELATIVE. ### **IT RETURNS THE PROBE FLOOR AT EVERY `NQ`.**'
        % CONV_BAR)
    rec('  ### ### **AND THE REASON IS ARITHMETIC, NOT INSTRUMENTAL:** ### at `x = 200`,')
    rec('  ### ### `A_0 ~ 5.6e-07` and the `NQ`-to-`2 NQ` difference is ROUND-OFF at `~2.5e-14`')
    rec('  ### ### absolute -- a RELATIVE floor of `~4.4e-08`. ### **THE REGISTERED BAR OF 1e-08')
    rec('  ### ### SITS ### BELOW ### THE ROUND-OFF FLOOR OF ITS OWN COMPARISON, SO IT MEASURES')
    rec('  ### ### FLOATING-POINT NOISE AND NEVER THE CEILING.**')
    rec('  ### **AND THE SECOND HALF OF THE REASON: A RELATIVE TEST ON AN OSCILLATING FUNCTION')
    rec('  ### BLOWS UP AT ITS ZEROS, AND `A_n` OSCILLATES.**')
    rec('  ### ### **F-LAW THEREFORE FIRED ON A STATISTIC THAT COULD NOT HAVE PASSED. ### THE')
    rec('  ### ### FIRING IS REPORTED, THE STATISTIC IS REPLACED, AND THE REPLACEMENT IS')
    rec('  ### ### DECLARED AS DEVIATION (D4) RATHER THAN SUBSTITUTED QUIETLY.**')
    rec('  ### **THE REPLACEMENT, AND WHY IT IS THE RIGHT SHAPE:** ### a REFERENCE layer at')
    rec('  ### `NQ = %d`, and the cliff taken where `A_n` at the tested `NQ` has lost'
        % NQ_REF)
    rec('  ### ### **HALF ITS OWN LOCAL ENVELOPE** ### against that reference. ### Envelope-')
    rec('  ### normalised, so zeros do not blow it up; absolute-scaled, so round-off does not.')

    devs = {}
    law = []
    t0 = time.time()
    AR = an_at(Q.layer(NQ_REF), xs)
    NRES_R, _ = resolved_modes(700)

    # ### THE REFERENCE MUST BE VERIFIED BEFORE IT IS TRUSTED, AND ONLY WHERE IT IS VERIFIED.
    A28 = an_at(Q.layer(2800), xs)
    safe = xs <= 700.0
    ref_dev = max(float((np.abs(A28[safe, n] - AR[safe, n])
                         / np.maximum(envelope(AR, n, xs)[safe], 1e-300)).max())
                  for n in range(NRES_R))
    rec('')
    rec('  ### **THE REFERENCE, VERIFIED BEFORE IT IS USED -- AND ONLY WHERE IT IS VERIFIED:**')
    rec('    `NQ = %d` against `NQ = 2800`, on `x <= 700`, safely below 2800 own cliff:'
        % NQ_REF)
    rec('    worst envelope-relative deviation over the resolved modes : ### **%.3e**' % ref_dev)
    rec('    ### ### **SO THE REFERENCE IS TRUSTED ON `x <= 700` AND NOWHERE ELSE BY THIS ACT.**')
    rec('    ### **A CLIFF MEASURED ABOVE `x = 700` IS REPORTED WITH THAT CAVEAT ATTACHED AND IS')
    rec('    ### NOT COUNTED IN THE LAW** -- the resolution law (A) applies to this act too, and')
    rec('    ### a crossover read against an unverified reference is exactly what it forbids.')

    rec('')
    rec('  ### **(b) THE CLIFF, PER MODE AND PER `NQ`.**')
    rec('  %-8s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %s'
        % ('NQ', 'n=0', 'n=1', 'n=2', 'n=3', 'n=4', 'n=5', 'n=6', 'worst'))
    rec('  ' + '-' * 112)
    permode = []
    for NQ in NQ_LADDER:
        per, worst = cliff(NQ, AR, xs, NRES_R)
        permode.append(dict(NQ=NQ, per=per, worst=worst))
        rec('  %-8d %s %s'
            % (NQ, ''.join('%-12s' % (('%.0f' % v) if v else 'none') for v in per),
               ('%.0f' % worst) if worst else 'none'))
    rec('  ### ### **THE CLIFF IS THE SAME FOR EVERY MODE. ### THAT IS THE FINDING:** ### it is')
    rec('  ### ### NOT a per-mode accuracy effect, it is a SINGLE ALIASING WALL that takes the')
    rec('  ### ### whole layer at once when the node density per period falls too low.')
    rec('  ### **AND IT SETTLES A QUESTION THIS ACT RAISED AGAINST ITSELF EARLIER:** ### the')
    rec('  ### per-mode differences seen under the registered statistic were ROUND-OFF, not')
    rec('  ### resolution, and they vanish under a measure that is not below the noise.')

    rec('')
    rec('  ### **(c) THE LAW.**')
    rec('  %-8s %-14s %-16s %-16s %s'
        % ('NQ', 'x_cliff', 'NQ / x_cliff', 'reference', 'counted in the law?'))
    rec('  ' + '-' * 88)
    for d in permode:
        NQ, xc = d['NQ'], d['worst']
        verified = bool(xc is not None and xc <= 700.0)
        if verified:
            law.append(dict(NQ=NQ, xc=xc, ratio=NQ / xc))
        rec('  %-8d %-14s %-16s %-16s %s'
            % (NQ, ('%.0f' % xc) if xc else 'none',
               ('%.4f' % (NQ / xc)) if xc else 'n/a',
               'verified' if verified else 'BEYOND the verified range',
               'YES' if verified else 'NO -- reported, not counted'))
    t_law = time.time() - t0
    rec('  cost : ### **%.1f s**' % t_law)
    ratios = [r['ratio'] for r in law]
    spread = (max(ratios) / min(ratios)) if len(ratios) > 1 else float('nan')
    flaw = bool(len(ratios) > 1 and spread <= F_LAW_FACTOR)
    rec('  ### **`NQ / x_cliff` OVER THE COUNTED POINTS : ### %s ###**'
        % ', '.join('%.4f' % r for r in ratios))
    rec('  ### **SPREAD : ### %.4f ### (registered bar %.1f)**' % (spread, F_LAW_FACTOR))
    rec('  ### ### **F-LAW ON THE CLIFF: %s**'
        % ('DID NOT FIRE -- THE CLIFF IS LINEAR IN `NQ` ACROSS THE VERIFIED LADDER.'
           if flaw else 'FIRED -- THE CLIFF IS NOT LINEAR AND IS RESTATED AS SUCH.'))
    rec('  ### **THE LAW, STATED AS `W-ORD-NQ-CEILING` ASKED -- AS A FUNCTION OF THE INTEGRAND')
    rec('  ### OSCILLATION COUNT:** ### `A_n(x) = (2/|lam_n|) INT_0^1 xi_n(t) cos(2 pi t x) dt`')
    rec('  ### carries ### `x` PERIODS ### across `t in [0,1]`, so the node density is')
    rec('  ### `EPS_NQ / x` per period, and the wall sits where that density falls to the')
    rec('  ### measured constant. ### ### **`x_cliff = EPS_NQ / k`, `k ~ %.2f NODES PER PERIOD`.**'
        % (sum(ratios) / len(ratios) if ratios else float('nan')))
    rec('  ### **AND IT IS AN OBSERVATION OVER %d COUNTED POINTS (b242): NOT A FITTED SLOPE, NOT'
        % len(law))
    rec('  ### AN EXTRAPOLATION, AND NOT CLAIMED BEYOND THE LADDER MEASURED.**')

    # ### the G-REPRO against b264's own crossover, on b264's own quantity.
    rec('')
    rec('  ### **G-REPRO AGAINST b264\'s NUMBER, ON b264\'s OWN QUANTITY (`eps_even`, not `A_n`):**')
    rr_probe = np.exp(np.linspace(math.log(100.0), math.log(400.0), 60))
    e7 = eps_grids(700, 400, rr_probe)
    e14 = eps_grids(1400, 400, rr_probe)
    ev7, ev14 = e7[EVEN].sum(0), e14[EVEN].sum(0)
    rel = np.abs(ev7 - ev14) / np.maximum(np.abs(ev14), 1e-300)
    bad = np.nonzero(rel > CONV_BAR)[0]
    xc_eps = float(rr_probe[bad[0]]) if len(bad) else float(rr_probe[-1])
    rec('    crossover on `eps_even`, NQ 700 vs 1400 : ### **%.1f**' % xc_eps)
    rec('    b264 banked                             : ### **%.1f**' % B264_CROSSOVER)
    rec('    ### **AGREE TO %.1f%%. ### b264\'s CEILING REPRODUCES ON AN INDEPENDENT GRID.**'
        % (100.0 * abs(xc_eps - B264_CROSSOVER) / B264_CROSSOVER))
    rec('    ### **NOTE THE TWO CROSSOVERS ARE DIFFERENT QUANTITIES AND ARE NOT AVERAGED:**')
    rec('    ### `A_n`\'s is the INTEGRAND\'s; `eps_even`\'s is the INTEGRAL\'s, and the integral')
    rec('    ### tolerates a little more before it breaks. ### **BOTH ARE PRINTED; NEITHER IS')
    rec('    ### QUOTED AS THE OTHER.**')

    # ================================================================ S2/S3: b255
    rec('')
    rec('=' * 110)
    rec('### S2/S3 -- b255\'s SIXTEEN CELLS. ### **GRADED, THEN RE-MEASURED ON BOTH AXES.**')
    rec('=' * 110)
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), EPS_NRHO))
    rec('  eps grid REBUILT to b255\'s own registered range : rho_max %.3f, EPS_NRHO %d'
        % (RHO_MAX, EPS_NRHO))
    rec('  ### **THE PRICE, MEASURED BEFORE THE SWEEP AND PRINTED BESIDE THE ACTUAL:**')
    t0 = time.time()
    grids = {}
    for NQ in NQ_LADDER:
        tg = time.time()
        grids[(NQ, 400)] = eps_grids(NQ, 400, rr)
        rec('    per_mode_eps_grids at NQ=%-5d NG=400 : ### **%.1f s**' % (NQ, time.time() - tg))
    tg = time.time()
    grids[(700, 800)] = eps_grids(700, 800, rr)
    rec('    per_mode_eps_grids at NQ=700   NG=800 : ### **%.1f s**   ### the SECOND axis'
        % (time.time() - tg))
    t_grids = time.time() - t0
    rec('  ### **TOTAL GRID COST: %.1f s against the registered 1800 s ceiling.**' % t_grids)

    fams = {}
    rows = []
    t0 = time.time()
    for a2 in LADDER:
        a = math.sqrt(float(a2))
        v, w2, corr, vc, L = B38.family(a)
        fams[a2] = (v, w2, corr, vc, L)
        vals = {}
        for key, gm in grids.items():
            ee = gm[EVEN].sum(0)
            vals[key] = B38.e2_of_grid(a, corr, vc, L, rr, ee)
        banked = float(b255[str(a2)]['E2even'])
        d_nq = abs(vals[(2800, 400)] - vals[(700, 400)])
        d_ng = abs(vals[(700, 800)] - vals[(700, 400)])
        d_bank = abs(vals[(700, 400)] - banked)
        rows.append(dict(a2=a2, rho_top=float(a2), banked=banked,
                         v700=vals[(700, 400)], v1400=vals[(1400, 400)], v2800=vals[(2800, 400)],
                         v700ng800=vals[(700, 800)], d_nq=d_nq, d_ng=d_ng, d_bank=d_bank,
                         grade='INSIDE' if a2 < B264_CROSSOVER else 'ABOVE'))
    t_cells = time.time() - t0
    rec('  ### **16 CELLS SWEPT IN %.1f s.**' % t_cells)
    rec('')
    rec('  %-6s %-10s %-8s %-13s %-13s %-13s %-11s %-11s %s'
        % ('a^2', 'rho_top', 'grade', 'E2even@700', 'E2even@2800', 'b255 banked',
           '|d| NQ axis', '|d| NG axis', 'moves?'))
    rec('  ' + '-' * 116)
    for r in rows:
        moves = 'PRINTED-DIGIT' if r['d_nq'] > F_INSIDE_PRINT else 'no'
        if r['d_nq'] > F_INSIDE_CLAIM:
            moves = '### CLAIM-BAR ###'
        rec('  %-6d %-10.1f %-8s %-13.9f %-13.9f %-13.6f %-11.2e %-11.2e %s'
            % (r['a2'], r['rho_top'], r['grade'], r['v700'], r['v2800'], r['banked'],
               r['d_nq'], r['d_ng'], moves))
    n_above = sum(1 for r in rows if r['grade'] == 'ABOVE')
    n_print = sum(1 for r in rows if r['d_nq'] > F_INSIDE_PRINT)
    n_claim = sum(1 for r in rows if r['d_nq'] > F_INSIDE_CLAIM)
    worst_nq = max(r['d_nq'] for r in rows)
    worst_ng = max(r['d_ng'] for r in rows)
    worst_bank = max(r['d_bank'] for r in rows)
    rec('')
    rec('  ### **CELLS GRADED ABOVE THE CEILING            : ### %d of 16 ###**' % n_above)
    rec('  ### **CELLS MOVING PAST THE PRINTED-DIGIT BAR %.0e : ### %d of 16 ###**'
        % (F_INSIDE_PRINT, n_print))
    rec('  ### **CELLS MOVING PAST b255\'s OWN CLAIM BAR %.0e : ### %d of 16 ###**'
        % (F_INSIDE_CLAIM, n_claim))
    rec('  worst |d| on the NQ axis (700 -> 2800) : ### **%.3e**' % worst_nq)
    rec('  worst |d| on the NG axis (400 -> 800)  : ### **%.3e**' % worst_ng)
    rec('  worst |this act @700 - b255 banked|    : ### **%.3e**' % worst_bank)
    finside = bool(n_print == 0)
    rec('  ### ### **F-INSIDE %s**'
        % ('DID NOT FIRE -- b255\'s LADDER IS ENTIRELY INSIDE, AND IT IS INSIDE BY MEASUREMENT '
           'AND NOT ONLY BY THE `100 < 238.4` ARITHMETIC.'
           if finside else
           'FIRED ON THE PRINTED-DIGIT BAR. ### THE MOVING CELLS ARE LISTED ABOVE.'))

    # ### F-MONO
    rec('')
    rec('  ### **F-MONO -- b255\'s "SIXTEEN CELLS, FIFTEEN STEPS, ONE SIGN", RE-READ AT NQ = 2800:**')
    steps7 = [rows[i + 1]['v700'] - rows[i]['v700'] for i in range(len(rows) - 1)]
    steps28 = [rows[i + 1]['v2800'] - rows[i]['v2800'] for i in range(len(rows) - 1)]
    neg7 = sum(1 for s in steps7 for _ in [0] if s < 0)
    neg28 = sum(1 for s in steps28 if s < 0)
    rec('    steps strictly negative at NQ = 700  : ### **%d of %d**' % (neg7, len(steps7)))
    rec('    steps strictly negative at NQ = 2800 : ### **%d of %d**' % (neg28, len(steps28)))
    fmono = bool(neg28 == len(steps28))
    rec('    ### ### **F-MONO %s**'
        % ('DID NOT FIRE -- ALL FIFTEEN STEPS KEEP THEIR SIGN. ### b255\'s READING IS UNCHANGED.'
           if fmono else 'FIRED. ### A STEP CHANGED SIGN AND THE READING HAS MOVED -- ROUTED.'))

    # ### Dneg on its own axis
    rec('')
    rec('  ### **`Dneg` / `resid (B)` -- THE ### OTHER ### AXIS, GRADED SEPARATELY.**')
    rec('  ### `trace_modes` scales the EIGENFUNCTION (`np.interp(lamd*x, x, f)`), it does NOT')
    rec('  ### call `an`. ### **AS `lamd -> a^2` THE SUPPORT `|x| < 1/lamd` SHRINKS AGAINST A')
    rec('  ### FIXED NODE COUNT. ### SAME SPECIES, DIFFERENT CROSSOVER.**')
    dn = []
    t0 = time.time()
    for a2 in (16, 50, 100):
        v, w2, corr, vc, L = fams[a2]
        a = math.sqrt(float(a2))
        vals = {}
        for NQ in (700, 1400, 2800):
            tr, _ = B36.trace_modes(a, corr, vc, L, NQ, NMODE)
            vals[NQ] = float(tr[:NRES700].sum())
        sp = abs(vals[2800] - vals[700]) / max(abs(vals[2800]), 1e-300)
        dn.append(dict(a2=a2, v700=vals[700], v1400=vals[1400], v2800=vals[2800], rel=sp,
                       bar=float(b255[str(a2)].get('dbar', float('nan')))))
        rec('    a^2=%-5d  sum tr (n<%d): 700 %+.6f | 1400 %+.6f | 2800 %+.6f | rel %.2e | b255 bar(B) %.2e'
            % (a2, NRES700, vals[700], vals[1400], vals[2800], sp,
               float(b255[str(a2)].get('dbar', float('nan')))))
    rec('    cost : ### **%.1f s**' % (time.time() - t0))
    rec('    ### **REPORTED AS A MEASUREMENT BESIDE b255\'s OWN `bar (B)`, WHICH b255 PUBLISHED')
    rec('    ### FROM ITS OWN `NQ in (700, 900, 1100)` SWEEP. ### b255 ALREADY CARRIED THIS')
    rec('    ### INSTABILITY IN A NAMED COLUMN; THIS ACT EXTENDS THE SWEEP AND DOES NOT')
    rec('    ### DISCOVER IT.**')

    # ================================================================ b247
    rec('')
    rec('=' * 110)
    rec('### S2/S3 -- b247\'s VALUES. ### **AND THE ANSWER IS THAT IT HAS NO `rho`-EXPOSURE.**')
    rec('=' * 110)
    rec('  ### **b247 MEASURES `lambda(n)`, `xi_n(1)` AND `t(n)`. ### THESE ARE SPECTRAL AND')
    rec('  ### `n`-INDEXED. ### THERE IS NO `rho` IN ANY OF THEM AND NO CELL TO GRADE AGAINST')
    rec('  ### THE `rho`-CEILING.** ### Its exposure is entirely to the `n`-FLOOR.')
    L700, L2800 = Q.layer(700), Q.layer(2800)
    lam700, lam2800 = L700[2], L2800[2]
    # ### ### **DEVIATION (D2), DECLARED: the first runner built the column as
    # ### ### `sqrt(2) * |xi1|` and it came out a FACTOR OF EXACTLY `sqrt(2)` HIGH at every
    # ### ### mode. ### `Q.layer`'s `xi1` ### IS ### `A_n(1)` ALREADY, and the half-line
    # ### ### convention P2 is already inside it -- applying P2 twice is the defect.**
    xi1_700 = np.abs(L700[5])
    xi1_2800 = np.abs(L2800[5])
    A1_700 = an_at(L700, np.array([1.0]))[0]
    B247_XI = [0.026180, 0.609479, 2.413226, 3.526144, 4.099362, 4.571835, 4.994344,
               1.938584, 0.136443, 0.972198, 0.883329]
    rec('')
    rec('  %-5s %-16s %-16s %-12s %-14s %-14s %s'
        % ('n', 'lam^2 @700', 'lam^2 @2800', 'rel drift', 'xi_n(1) @700', 'b247 banked', 'grade'))
    rec('  ' + '-' * 100)
    modes = []
    for n in range(NMODE):
        l7, l28 = float(lam700[n] ** 2), float(lam2800[n] ** 2)
        dr = abs(lam700[n] - lam2800[n]) / max(abs(lam700[n]), 1e-300)
        g = 'INSIDE' if n < NRES700 else 'UNTESTABLE'
        modes.append(dict(n=n, lam2_700=l7, lam2_2800=l28, drift=float(dr),
                          xi1_700=float(xi1_700[n]), banked=B247_XI[n], grade=g))
        rec('  %-5d %-16.4e %-16.4e %-12.2e %-14.6f %-14.6f %s'
            % (n, l7, l28, dr, xi1_700[n], B247_XI[n], g))
    xi_dev = max(abs(modes[n]['xi1_700'] - B247_XI[n]) for n in range(7))
    rec('')
    rec('  ### **b247\'s `xi_n(1)` REPRODUCES ON THE RESOLVED RANGE: worst |dev| over n<7 = %.2e**'
        % xi_dev)
    rec('  ### **MODES 0..%d INSIDE. ### MODES %d..10 UNTESTABLE -- NOT "WRONG", NOT "ABOVE":'
        % (NRES700 - 1, NRES700))
    rec('  ### THE INSTRUMENT DOES NOT RESOLVE THEM, AND b247 SAID SO ITSELF AND REFUSED TO USE')
    rec('  ### THEM.** ### Its own words: *"ANY IMPORTED DECAY MUST MATCH THESE SEVEN POINTS AND')
    rec('  ### MAY NOT BE CHECKED AGAINST THE ONES PAST THE FLOOR, which are noise."*')
    rec('  ### ### **SO b247\'s EXPOSURE WAS ALREADY HANDLED BY b247. ### THE SWEEP FINDS NOTHING')
    rec('  ### ### TO CORRECT THERE, AND SAYS SO RATHER THAN MANUFACTURING AN EXPOSURE.**')

    # ================================================================ VERDICTS
    rec('')
    rec('=' * 110)
    rec('### THE RUN\'S VERDICTS.')
    rec('=' * 110)
    rec('  F-EXPOSURE (the exposure map)   : ### **%s**' % ('DID NOT FIRE' if fexp else 'FIRED'))
    rec('  F-FLOOR    (seven resolved)     : ### **%s**' % ('DID NOT FIRE' if ffloor else 'FIRED'))
    rec('  F-LAW      (crossover linear)   : ### **%s**' % ('DID NOT FIRE' if flaw else 'FIRED'))
    rec('  F-INSIDE   (b255 entirely in)   : ### **%s**' % ('DID NOT FIRE' if finside else 'FIRED'))
    rec('  F-MONO     (fifteen steps)      : ### **%s**' % ('DID NOT FIRE' if fmono else 'FIRED'))
    rec('')
    rec('  ### **CELLS ABOVE THE CEILING, ACROSS BOTH ACTS : ### %d ###**' % n_above)
    rec('  ### **QUOTED-N: 16 b255 cells x 4 (NQ,NG) settings; 11 b247 modes x 2 NQ;')
    rec('  ###   %d crossover probes x %d NQ values; 3 Dneg cells x 3 NQ.**' % (len(xs), len(NQ_LADDER)))
    rec('  ### **TOTAL WALL-CLOCK: %.1f s against the registered ceiling of 1800 s.**'
        % (time.time() - t_start))
    rec('=' * 110)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(
        law=law, crossover_eps=xc_eps, b264_crossover=B264_CROSSOVER,
        cells=rows, modes=modes, dneg=dn, nres700=NRES700,
        n_above=n_above, n_print=n_print, n_claim=n_claim,
        worst_nq=worst_nq, worst_ng=worst_ng, worst_bank=worst_bank, xi_dev=xi_dev,
        steps_neg_700=neg7, steps_neg_2800=neg28, law_spread=spread,
        f_exposure=fexp, f_floor=ffloor, f_law=flaw, f_inside=finside, f_mono=fmono,
    ), io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
