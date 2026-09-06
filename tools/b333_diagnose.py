# -*- coding: utf-8 -*-
"""b333_diagnose.py -- THE MISMATCH DIAGNOSED: WHICH FUNCTION EACH BANKED NUMBER BELONGS TO.

### ### **WHAT `b333_derive.py` PRINTED, AND WHY IT IS NOT A MISMATCH IN THE RECORD.** ### The derivation
### tool evaluated the source's (150) on the ATLAS'S BUMP and compared the result against the two columns
### of b320's table, as the sealed registration (E) ordered. ### Both columns of b320's table were computed
### for b320's OWN test function -- `autocorrelation(mean_zero_variant(a))`, the source's `g conv g#` on the
### mean-zero variant -- and not for the bump: `tools/b320_corroborate.py::main` builds
### `f = SQ.autocorrelation(SM.mean_zero_variant(a))` for each cell before either route runs. ### The sealed
### bar therefore paired one function's value with another function's comparators, which no route can
### satisfy. ### **THAT IS A DEFECT ON THE SEALED FACE OF THIS ACT'S REGISTRATION, AND IT IS DECLARED AS
### SUCH IN THE BANK; THE SEALED BAR IS NOT REWRITTEN HERE.**

### ### **WHAT THIS FILE DOES INSTEAD: THE SAME COMPARISONS, LIKE FOR LIKE, AS A NEW TOOL.**
###   (A) THE BUMP: the third route's `A_3` (read from `b333_derive.json`, never recomputed) against the
###       corpus's OWN banked archimedean channel for the bump -- `arch` in `data/carto_atlas.jsonl`, the
###       atlas's route -- at the thirteen cells; and against b320's two routes APPLIED TO THE BUMP here
###       (`b320_corroborate.digamma_side` and `b320_weil.weil`, imported, on `b317_smear.corpus_bump(a)`).
###   (B) b320's FUNCTION: the source's (150) evaluated on `autocorrelation(mean_zero_variant(a))` by a
###       route sharing no code with b320's two -- (150) rewritten in `v = log x`:
###         `W_R = (log 4 pi + gamma) w(0) + INT_0^{L'} (w(v) e^{v/2} - w(0)) / sinh v dv - w(0) log((e^{L'}+1)/(e^{L'}-1))`
###       (for even `f`, `f + f# = 2 f`; the last term is the tail `-w(0) INT_{L'}^inf dv / sinh v` beyond
###       the support); `A = -W_R` -- against b320's banked table, the function the table was made for.
###   (C) THE SAME (150)-in-`v` ROUTE ON THE BUMP, as a cross-check of the derivation tool's mpmath route
###       and of the atlas's discretized bump against the continuous one.
###   (D) THE (152) EVALUATION OF THE DERIVATION TOOL: its `A_152` sat 3e-4 from `A_3` at a = 1.3, above
###       the bar; (152) is re-formed here on a resolved grid to `u = 1500` so the difference is attributed.
### The 2e-4 of the sealed bar is USED AS THE READING BAR for (A) and (B) and is named as such; a reading
### is not the sealed bar. Nothing here is a grade.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b333_diagnose_run.txt')
OUTJ = os.path.join(D, 'b333_diagnose.json')
READING_BAR = 2e-4

import carto_atlas as CA          # noqa: E402
import b317_smear as SM           # noqa: E402
import b318_square as SQ          # noqa: E402
import b320_weil as WE            # noqa: E402
import b320_corroborate as CO     # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []
CELLS = ['1.3', '1.35', '1.41', '1.5', '1.7', '1.9', '1.99', '2.0', '2.01', '2.1', '2.4', '2.8', '3.0']
EULER = 0.57721566490153286060651209
LOG4PI = math.log(4.0 * math.pi)


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def w150_in_v(v, w, refine=1):
    """(150) in `v = log x` on a gridded even test function; numpy trapezoid on the grid, optionally refined."""
    v = np.asarray(v, dtype=np.float64)
    w = np.asarray(w, dtype=np.float64)
    if refine > 1:
        vv = np.linspace(v[0], v[-1], (v.size - 1) * refine + 1)
        w = np.interp(vv, v, w)
        v = vv
    w0 = float(np.interp(0.0, v, w))
    m = v > 0.0
    vp = v[m]
    wp = w[m]
    g = (wp * np.exp(vp / 2.0) - w0) / np.sinh(vp)
    # the node at v = 0 carries the limit w'(0) + w(0)/2 = w(0)/2 for an even w
    vp = np.concatenate(([0.0], vp))
    g = np.concatenate(([0.5 * w0], g))
    Lp = float(v[-1])
    tail = -w0 * math.log((math.exp(Lp) + 1.0) / (math.exp(Lp) - 1.0))
    return (LOG4PI + EULER) * w0 + float(np.trapezoid(g, vp)) + tail


def a152_resolved(v, w, umax=1500.0, du=0.05):
    """(152) on a gridded function: `(1/2pi) INT fhat(u) [Re psi(1/4 + iu/2) - log pi] du`, resolved grid."""
    U = np.arange(-umax, umax + du / 2.0, du)
    K = CO.kernel(U)
    return float(np.trapezoid(CO.fhat_blocked(np.asarray(v), np.asarray(w), U) * K, U) / (2.0 * math.pi))


def main():
    t0 = time.time()
    R = json.load(io.open(os.path.join(D, 'b333_derive.json'), encoding='utf-8'))
    arch = {}
    for ln in io.open(os.path.join(D, 'carto_atlas.jsonl'), encoding='utf-8'):
        if ln.strip():
            r = json.loads(ln)
            if r.get('a') is not None:
                arch[str(r['a'])] = float(r['arch'])
    rec('=' * 100)
    rec('b333 -- THE MISMATCH DIAGNOSED. ### WHICH FUNCTION EACH BANKED NUMBER BELONGS TO.')
    rec('=' * 100)
    rec("  b320's table was made for : autocorrelation(mean_zero_variant(a))  [tools/b320_corroborate.py::main]")
    rec("  the third route was run on : the atlas's bump                     [registration (E), sealed]")
    rec("  the corpus's banked route for the bump : `arch` in data/carto_atlas.jsonl (the atlas's channels)")
    rec('  READING BAR (not the sealed bar) : %.0e' % READING_BAR)
    out = dict(reading_bar=READING_BAR, cells={})

    rec('')
    rec('  (A) THE BUMP: A_3 (150, mpmath, from b333_derive.json) against the atlas\'s banked arch, and against b320\'s two routes applied to the bump here')
    rec('  %-6s %13s %13s %11s %13s %11s %13s %11s' % ('a', 'A_3', 'atlas arch', '|d|', 'dig on bump', '|d|', '(38) on bump', '|d|'))
    worstA = dict(atlas=0.0, dig=0.0, w38=0.0)
    U = np.arange(-CO.UMAX, CO.UMAX + CO.DU / 2.0, CO.DU)
    K = CO.kernel(U)
    for a in CELLS:
        A3 = R['cells'][a]['A3']
        key = a if a in arch else str(float(a))
        at = arch[key]
        fb = SM.corpus_bump(float(a))
        dg = CO.digamma_side(fb, U=U, ker=K)
        w38 = WE.weil(fb)[0]
        d1, d2, d3 = abs(A3 - at), abs(A3 - dg), abs(A3 - w38)
        worstA = dict(atlas=max(worstA['atlas'], d1), dig=max(worstA['dig'], d2), w38=max(worstA['w38'], d3))
        out['cells'][a] = dict(A3=A3, atlas_arch=at, dig_on_bump=dg, w38_on_bump=w38)
        rec('  %-6s %+13.9f %+13.9f %11.3e %+13.9f %11.3e %+13.9f %11.3e' % (a, A3, at, d1, dg, d2, w38, d3))
    okA = all(x <= READING_BAR for x in worstA.values())
    rec('  worst : against the atlas %.3e ; against the digamma route on the bump %.3e ; against the (38) route on the bump %.3e  -> inside the reading bar at every cell : %s'
        % (worstA['atlas'], worstA['dig'], worstA['w38'], okA))
    out['A_worst'] = worstA
    out['A_ok'] = okA

    rec('')
    rec("  (B) b320's FUNCTION: (150) in v on autocorrelation(mean_zero_variant(a)), no b320 route code, against b320's banked table")
    rec('  %-6s %13s %13s %11s %13s %11s %11s' % ('a', 'A by (150)', 'A_dig(b320)', '|d|', 'W_38(b320)', '|d|', 'refine x4'))
    worstB = dict(dig=0.0, w38=0.0, refine=0.0)
    for a in CELLS:
        f = SQ.autocorrelation(SM.mean_zero_variant(float(a)))
        A = -w150_in_v(f.v, f.w)
        A4 = -w150_in_v(f.v, f.w, refine=4)
        dg, w38 = R['cells'][a]['A_dig_b320'], R['cells'][a]['W38_b320']
        d1, d2, d3 = abs(A - dg), abs(A - w38), abs(A - A4)
        worstB = dict(dig=max(worstB['dig'], d1), w38=max(worstB['w38'], d2), refine=max(worstB['refine'], d3))
        out['cells'][a].update(A150_on_b320_f=A, A150_on_b320_f_refined=A4, A_dig_b320=dg, W38_b320=w38)
        rec('  %-6s %+13.9f %+13.9f %11.3e %+13.9f %11.3e %11.3e' % (a, A, dg, d1, w38, d2, d3))
    okB = worstB['dig'] <= READING_BAR and worstB['w38'] <= READING_BAR
    rec('  worst : against the digamma column %.3e ; against the (38) column %.3e ; grid refinement moves it by %.3e  -> inside the reading bar at every cell : %s'
        % (worstB['dig'], worstB['w38'], worstB['refine'], okB))
    out['B_worst'] = worstB
    out['B_ok'] = okB

    rec('')
    rec('  (C) THE SAME (150)-in-v ROUTE ON THE BUMP (the atlas\'s 4001-node discretization), against A_3 (continuous bump, mpmath)')
    worstC = 0.0
    for a in CELLS:
        v, w = CA.bump(float(a))
        A = -w150_in_v(v, w)
        d = abs(A - R['cells'][a]['A3'])
        worstC = max(worstC, d)
        out['cells'][a]['A150_in_v_on_bump'] = A
        rec('  a = %-5s (150)-in-v %+13.9f  A_3 %+13.9f  |d| %.3e' % (a, A, R['cells'][a]['A3'], d))
    rec('  worst %.3e' % worstC)
    out['C_worst'] = worstC

    rec('')
    rec('  (D) THE DERIVATION TOOL\'S (152) EVALUATION, re-formed on a resolved grid to u = 1500 (du 0.05) for the bump')
    worstD = dict(deriv=0.0, resolved=0.0)
    for a in ['1.3', '2.0', '3.0']:
        v, w = CA.bump(float(a))
        A = a152_resolved(v, w)
        A3, A152 = R['cells'][a]['A3'], R['cells'][a]['A152']
        d1, d2 = abs(A152 - A3), abs(A - A3)
        worstD = dict(deriv=max(worstD['deriv'], d1), resolved=max(worstD['resolved'], d2))
        out['cells'][a]['A152_resolved'] = A
        rec('  a = %-5s A_152 (derive tool, quad to 60/L) %+13.9f  |d from A_3| %.3e ; (152) resolved %+13.9f  |d from A_3| %.3e' % (a, A152, d1, A, d2))
    rec('  worst : the derivation tool\'s (152) %.3e ; the resolved (152) %.3e' % (worstD['deriv'], worstD['resolved']))
    out['D_worst'] = worstD

    rec('')
    rec('  (E) THE ATLAS\'S CHANNELS RE-RUN LIVE at two cells, against the banked row (same code; a reproducibility reading only)')
    for a in ['1.3', '3.0']:
        r = CA.channels(float(a))
        key = a if a in arch else str(float(a))
        rec('  a = %-5s live arch %+13.9f  banked %+13.9f  |d| %.3e' % (a, r['arch'], arch[key], abs(r['arch'] - arch[key])))
        out['cells'][a]['atlas_live'] = float(r['arch'])

    rec('')
    rec('  ### THE FINDING, STATED ONCE:')
    rec('  ###   the third route\'s value for the bump IS the corpus\'s value for the bump (A);')
    rec('  ###   the source\'s (150), on b320\'s own function, IS b320\'s table (B);')
    rec('  ###   the "MISMATCH" the derivation tool printed is the sealed bar pairing the bump with a table made for another function.')
    rec('  ###   THE CORPUS\'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED. THE SEALED BAR, AS WRITTEN, IS NOT MET AND IS NOT REWRITTEN.')
    rec('  wall %.1f s' % (time.time() - t0))
    rec('=' * 100)
    out['finding'] = ('the third route agrees with the corpus\'s own bump route and with b320\'s routes applied to the bump; '
                      '(150) on b320\'s function agrees with b320\'s table; the sealed bar paired the bump with a table made for another function')
    open(OUTJ + '.tmp', 'wb').write((json.dumps(out, indent=1) + chr(10)).encode('utf-8'))
    os.replace(OUTJ + '.tmp', OUTJ)
    return 0 if (okA and okB) else 1


if __name__ == '__main__':
    code = main()
    k, name = 1, OUT
    while os.path.exists(name):
        k += 1
        name = os.path.join(D, 'b333_diagnose_run%d.txt' % k)
    io.open(name, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    sys.exit(code)
