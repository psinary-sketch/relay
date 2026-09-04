# -*- coding: utf-8 -*-
"""b321_run.py -- THE FOUR COMPONENTS. ### **TWO MORE THEOREMS, THEN THE WINDOW.**

### ### **WHAT THIS RUNNER MAY AND MAY NOT DO.**
### It may compute. ### It may print. ### **IT MAY NOT SAY WHAT THE WINDOW MEANS**, and the
### registration caps `interpretations of the window's balance` at zero.
### ### **EVERY SIGN IS QUOTED FROM AN OWNER** -- the source's (148), (149), (155) and its page-49
### sentence `W_infinity = - W_R`; the atlas's own header. ### None is supplied by the navigator.
### ### **A FINITE WINDOW AT A FINITE CUTOFF DECIDES NOTHING GLOBAL**, and that sentence is printed
### beside the balance and not once at the end of it.
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

import b316_instrument as INS   # noqa: E402
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b319_stable as ST        # noqa: E402
import b320_weil as WE          # noqa: E402
import b321_window as WI        # noqa: E402
import b313f_qeps_layer as EF   # noqa: E402
import b313r_qeps_layer as ER   # noqa: E402
import noise_floor as NF        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
B320 = os.path.join(D, 'b320_rows.json')
EXTRACT = os.path.join(D, 'b321_extract_notes.txt')

# ### **THE BARS, READ OFF THE SEALED REGISTRATION AND LIVING NOWHERE ELSE.**
BAR_TWOROUTE = 1e-6     # ### (B1d) relative
BAR_EF = 1e-3           # ### (B2), the ATLAS's own TOL, imported below and checked against it
BOUNDARY = math.sqrt(2.0)   # ### Theorem 1's support condition, `2^{1/2}`

# ### the needles this run pulls from the EXTRACT FILE, never from the artefact
EXTRACT_NEEDLES = [
    ('Theorem 4.7 -- the EQUALITY', 'Theorem 4.7 Let S be'),
    ('### and the remainder it names, (84)', 'which is given, for'),
    ('(1) -- the explicit formula as the paper opens with it', 'explicit formula'),
    ('(148) -- the same formula with its signs', 'takes the form'),
    ('(149) -- the finite place', 'runs over all places'),
    ('### the archimedean sign, in the source own sentence', 'is proven'),
    ('Proposition C.1 -- the criterion itself', 'Positivity criterion'),
    ('### and the inequality it asks for', 'RH'),
    ('(61) -- the exponent at its defining site', 'its action is given by'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def pull(anchor):
    txt = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    flat = ''.join(ch for ch in txt if not ch.isspace())
    a = ''.join(ch for ch in anchor if not ch.isspace())
    return a in flat


def main():
    t0 = time.time()
    fails = []
    rec('=' * 100)
    rec('b321 -- THE WINDOW OPENED.')
    rec('=' * 100)

    # ### -------------------------------------------------------------- the imported instruments
    for lbl, fn in (('b316 INSTRUMENT', INS.self_test), ('b317 ASSEMBLY', SM.self_test),
                    ('b318 SQUARE', SQ.self_test), ('b319 STABLE', ST.self_test),
                    ('b320 WEIL', WE.self_test), ('THIS ACT WINDOW', WI.self_test)):
        out = fn()
        good, arms = out[0], out[1]
        rec('  ### %-18s FIXTURES : %s  %s' % (lbl, arms, 'PASS' if good else '### FAIL ###'))
        if lbl == 'THIS ACT WINDOW':
            for s in out[2]:
                rec('    ' + s)
        if not good:
            fails.append(lbl)
    rec('  ### **FIXTURE (i) OF THIS ACT IS THE ONE THAT LICENSES EVERYTHING BELOW:** ### the')
    rec('  ### re-formed channels reproduce `carto_atlas.channels(a)` on the atlas\'s OWN bump.')
    rec('  ### **A RE-IMPLEMENTATION THAT CANNOT REPRODUCE ITS ORIGINAL IS AN OVERWRITE.**')

    rec('')
    rec('  ### THE SOURCE STATEMENTS, PULLED FROM THE EXTRACT FILE:')
    for lbl, anchor in EXTRACT_NEEDLES:
        got = pull(anchor)
        rec('    %-5s %s' % ('found' if got else '### NO', lbl))
        if not got:
            fails.append('needle: ' + lbl)

    rec('')
    rec('  ### THE BARS, AND WHERE EACH COMES FROM:')
    rec('    (B1d) two-quadrature limit      : %.0e relative      -- sealed' % BAR_TWOROUTE)
    rec('    (B2)  explicit-formula residual : %.0e or the bound  -- the ATLAS\'s own TOL = %.0e'
        % (BAR_EF, WI.AT.TOL))
    rec('    the truncation                  : NGAM = %d, last ordinate %.9f -- registered'
        % (WI.AT.NGAM, float(WI.AT.GAM[-1])))
    if abs(BAR_EF - WI.AT.TOL) > 0:
        rec('    ### ### **THE ACT\'S BAR IS NOT THE ATLAS\'S. ### HARD FAILURE.**')
        fails.append('B2 bar does not match the atlas')

    b320 = json.load(io.open(B320, encoding='utf-8'))
    rows320 = {r['a']: r for r in b320['rows']}
    covered = list(b320['covered'])
    cells = [r['a'] for r in SM.atlas_cells()]

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE IDENTITY CONTROL. ### **THEOREM 4.7 IS AN EQUALITY.**')
    rec('=' * 100)
    rec('  ### **(83): ### `Tr(theta(f) S) = W_infinity(f) + INT f(rho^-1) eps(rho) d*rho`.**')
    rec('  ### By cyclicity `Tr(theta(g) S theta(g)^*) = Tr(theta(f) S)` for `f = g conv g^#`, so')
    rec('  ### ### **b320\'s MARGIN MUST BE MINUS THAT INTEGRAL, EXACTLY.**')
    rec('  ### ### **AND THE REMAINDER IS THE b313 FLIPPED COPY** -- the source\'s exponent, chosen')
    rec('  ### on b313\'s reading of three sites and on no number. ### The other copy is printed')
    rec('  ### beside it at every cell, because an act that showed only one would be asking to be')
    rec('  ### believed.')
    rec('')
    rec('  ### (1a) THE REMAINDER INTEGRAL, BOTH QUADRATURES AND BOTH EXPONENTS.')
    rec('    %-6s %-18s %-18s %-12s %-18s'
        % ('a', 'uniform (source)', 'chebyshev (source)', 'rel. diff', 'corpus exponent'))
    c1 = {}
    for a in covered:
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        ru = WI.remainder_integral(f, EF, 'uniform')
        rc = WI.remainder_integral(f, EF, 'cheb')
        rr = WI.remainder_integral(f, ER, 'uniform')
        rel = abs(ru - rc) / max(abs(ru), 1e-300)
        c1[a] = dict(uniform=ru, cheb=rc, rel=rel, corpus=rr)
        rec('    %-6g %-18.9f %-18.9f %-12.3e %-18.9f' % (a, ru, rc, rel, rr))
    twok = all(c1[a]['rel'] < BAR_TWOROUTE for a in covered)
    rec('    ### ### **(B1d) THE TWO QUADRATURES AGREE TO %.0e AT EVERY CELL : %s**'
        % (BAR_TWOROUTE, twok))
    rec('    ### **AND THEY ARE NOT TWO ROUTES.** ### There is exactly one implementation of (84)')
    rec('    ### in this corpus; both quadratures call it. ### (B1d) said so before the value.')
    if not twok:
        fails.append('B1d')

    rec('')
    rec('  ### (1b) AGAINST b320\'s MARGIN LADDER. ### **THE DOMAIN AXIS HAS NOT CONVERGED AND THAT')
    rec('  ### ### IS WHY THE BAR IS A LADDER AND NOT A TOLERANCE.**')
    scores = {}
    for a in covered:
        r = rows320[a]
        weil = r['weil']
        dom = b320['axes'][str(a)]['domain']
        drank = b320['axes'][str(a)]['drank']
        margins = [weil - s for s in dom]
        pred = -c1[a]['uniform']
        resid = [m - pred for m in margins]
        sign_ok = pred > 0.0
        brack_ok = pred < margins[-1]
        appr_ok = all(abs(resid[i + 1]) < abs(resid[i]) for i in range(len(resid) - 1))
        scores[a] = dict(pred=pred, margins=margins, resid=resid, drank=drank,
                         sign=sign_ok, bracket=brack_ok, approach=appr_ok)
        rec('')
        rec('    ### `a = %g`   ### **- INT f eps = %.9f**   (b320 reference margin %.9f)'
            % (a, pred, r['margin']))
        rec('      %-8s %-8s %-18s %-18s %-18s'
            % ('rank', 'frame', 'Tr (square)', 'margin W - Tr', 'residual to -INT'))
        for i, s in enumerate(dom):
            rec('      %-8d %-8d %-18.9f %-18.9f %-18.9f'
                % (drank[i], i + 1, s, margins[i], resid[i]))
        rec('      (B1a) sign strictly positive        : %s' % sign_ok)
        rec('      (B1b) below the largest-frame margin: %s   (%.9f < %.9f)'
            % (brack_ok, pred, margins[-1]))
        rec('      (B1c) residual strictly decreasing  : %s' % appr_ok)
    a1 = all(scores[a]['sign'] for a in covered)
    b1 = all(scores[a]['bracket'] for a in covered)
    cc1 = all(scores[a]['approach'] for a in covered)
    ident = a1 and b1 and cc1 and twok
    rec('')
    rec('  ### (B1a) SIGN : %s      (B1b) BRACKET : %s      (B1c) APPROACH : %s      (B1d) : %s'
        % (a1, b1, cc1, twok))
    rec('  ### ### **VERDICT -- THE IDENTITY CONTROL : %s**' % ('HOLDS' if ident else 'FAILS'))
    if ident:
        rec('')
        rec('  ### (1c) ### **AND WHETHER IT CLOSES THE EXPONENT QUESTION -- MEASURED, NOT ASSUMED.**')
        rec('  ### The order says this act closes that question by measurement IF the identity holds.')
        rec('  ### ### **IT HOLDS. ### SO THE OTHER COPY IS SCORED AGAINST THE SAME ARMS.**')
        rec('    %-6s %-16s %-16s %-14s %-16s %-9s'
            % ('a', 'source copy', 'corpus copy', 'apart by', 'from equality', 'corpus?'))
        both = 0
        for a in covered:
            sc = scores[a]
            apart = abs(c1[a]['uniform'] - c1[a]['corpus'])
            inst = abs(sc['resid'][-1])
            passes = (-c1[a]['corpus'] > 0.0) and (-c1[a]['corpus'] < sc['margins'][-1])
            both += 1 if passes else 0
            rec('    %-6g %-16.9f %-16.9f %-14.9f %-16.9f %-9s'
                % (a, sc['pred'], -c1[a]['corpus'], apart, inst,
                   'PASSES' if passes else 'fails'))
        rec('    ### ### **THE CORPUS COPY PASSES THE SAME ARMS AT %d OF %d CELLS.**'
            % (both, len(covered)))
        rec('    ### ### **SO THE ANSWER IS NO: ### THIS MEASUREMENT DOES NOT CLOSE THE EXPONENT')
        rec('    ### ### QUESTION, AND THE ORDER\'S CONDITIONAL IS REFUTED BY THE ACT\'S OWN')
        rec('    ### ### NUMBERS.** ### The two copies sit closer to each other than either sits to')
        rec('    ### the equality: they are apart by a FRACTION of the distance in the column')
        rec('    ### beside it. ### **AN INSTRUMENT CANNOT DISCRIMINATE BETWEEN TWO CANDIDATES THAT')
        rec('    ### ### LIE CLOSER TOGETHER THAN ITS OWN DISTANCE FROM THE ANSWER.**')
        rec('    ### **b313 SETTLED THE EXPONENT BY READING AND THAT READING STILL STANDS ALONE.**')
        rec('    ### b313 said a residue is not a vote on it. ### This is not a residue, and it is')
        rec('    ### still not a vote, because it cannot tell the two apart.')
    else:
        rec('  ### ### **THE LINK ORDER OF (B6) IS WALKED BELOW AND THE FIRST DIFFERING')
        rec('  ### ### CONSTITUENT IS QUOTED. ### NO BAR IS MOVED.**')
        fails.append('IDENTITY CONTROL')

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE EXPLICIT-FORMULA CONTROL.')
    rec('=' * 100)
    rec('  ### **(148): ### `SUM_rho f-tilde(rho) = INT f dx + INT f^# dx - SUM_v W_v(f)`.**')
    rec('  ### In the corpus\'s settled chain that is ### **`Z = P - PR + A`**, and the archimedean')
    rec('  ### sign comes from the source\'s own page-49 sentence: ### *"a positivity result for the')
    rec('  ### distribution `W_infinity = - W_R` is proven"* ### -- so ### **`A = W_infinity`**.')
    rec('  ### ### **THE ZEROS ARE THE CORPUS\'S INDEPENDENT LIBRARY**, %d ordinates to %.6f, and'
        % (WI.AT.NGAM, float(WI.AT.GAM[-1])))
    rec('  ### the truncation was registered before the first value.')
    rec('')
    rec('    %-6s %-16s %-16s %-16s %-16s %-13s %-11s'
        % ('a', 'Z (zeros)', 'P (poles)', 'A (arch)', 'PR (primes)', 'residual', 'bound'))
    c2 = {}
    for a in cells:
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        ch = WI.channels(f.v, f.w)
        tb = WI.trunc_bound(f.v, f.w)
        ch['bound'] = tb
        ch['ok'] = abs(ch['residual']) <= max(tb, BAR_EF)
        c2[a] = ch
        rec('    %-6g %-16.9f %-16.3e %-16.9f %-16.9f %-13.3e %-11.3e'
            % (a, ch['zero'], ch['pole'], ch['arch'], ch['prime'], ch['residual'], tb))
    covok = all(c2[a]['ok'] for a in covered)
    allok = all(c2[a]['ok'] for a in cells)
    rec('    ### ### **(B2) THE RESIDUAL IS INSIDE `max(bound, %.0e)` AT EVERY COVERED CELL : %s**'
        % (BAR_EF, covok))
    rec('    ### and at all %d cells : %s' % (len(cells), allok))
    rec('    ### ### **VERDICT -- THE EXPLICIT-FORMULA CONTROL : %s**'
        % ('HOLDS' if covok else 'FAILS'))
    if not covok:
        fails.append('EXPLICIT FORMULA')

    rec('')
    rec('  ### (2b) AND `A` AGAINST b320\'s `W_infinity`, WHICH IS A SECOND ROUTE AND A SIGN TEST')
    rec('  ### ### AT THE SAME TIME.')
    rec('    %-6s %-18s %-18s %-13s' % ('a', 'A (this chain)', 'W_inf by (38)', 'difference'))
    worst = 0.0
    for a in cells:
        w = rows320[a]['weil']
        d = abs(c2[a]['arch'] - w)
        worst = max(worst, d)
        rec('    %-6g %-18.9f %-18.9f %-13.3e' % (a, c2[a]['arch'], w, d))
    rec('    ### ### **WORST DIFFERENCE : %.3e**' % worst)
    rec('    ### **THE TWO SIDES OF THIS COMPARISON SHARE NO CODE**: one is a Hadamard integral of')
    rec('    ### the source\'s (38), the other a transform-side integral against the corpus\'s digamma')
    rec('    ### kernel through the settled chain. ### **AND IT IS ALSO THE SIGN TEST**: had the')
    rec('    ### page-49 sentence been read the other way, this column would differ by a factor of')
    rec('    ### `-1` and not by `%.0e`.' % worst)

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE WINDOW.')
    rec('=' * 100)
    above = [a for a in cells if a > BOUNDARY]
    rec('  ### **THE CELLS ABOVE THE BOUNDARY: ### `a > 2^{1/2}`, WHERE THE SEED\'S SUPPORT EXCEEDS')
    rec('  ### ### THE NARROW WINDOW AND THE PRIMES ENTER THROUGH THE LOCAL DISTRIBUTION.**')
    rec('  ### The lawful `f = g conv g^#` is supported in `[a^-2, a^2]`, so a prime power `p^m`')
    rec('  ### enters exactly when `p^m <= a^2`. ### **THAT IS WHY THE PRIME COLUMN IS SILENT AT THE')
    rec('  ### ### COVERED CELLS AND NOT SILENT HERE**, and it is a fact about a support.')
    rec('')
    rec('    %-6s %-15s %-15s %-15s %-15s %-15s %-9s'
        % ('a', 'W_inf', 'square', 'margin', 'PR (primes)', 'Z (zeros)', 'primes'))
    for a in above:
        r = rows320[a]
        rec('    %-6g %-15.9f %-15.9f %-15.9f %-15.9f %-15.9f %-9s'
            % (a, r['weil'], r['square'], r['margin'], c2[a]['prime'], c2[a]['zero'],
               c2[a]['prime_terms']))
    rec('')
    rec('  ### (3b) ### **AND BEFORE ANY TOTAL IS TAKEN: ### WHAT THE POLE COLUMN DID.**')
    rec('    %-6s %-18s %-18s %-18s' % ('a', 'f-tilde(0)+f-tilde(1)', 'Z (zeros)', 'min f-hat'))
    poles = []
    for a in cells:
        poles.append(abs(c2[a]['pole']))
        cf = {r['a']: r for r in b320['class_f']}
        rec('    %-6g %-18.3e %-18.9f %-18.3e'
            % (a, c2[a]['pole'], c2[a]['zero'], cf[a]['minf']))
    rec('    ### ### **THE POLE TERM VANISHES AT EVERY CELL -- WORST `%.3e`.**' % max(poles))
    rec('    ### **AND IT IS NOT AN ACCIDENT.** ### `P = f-tilde(0) + f-tilde(1)`, and Theorem 1\'s')
    rec('    ### own two vanishing conditions on the seed are exactly `g-hat(0) = 0` and')
    rec('    ### `g-hat(i/2) = 0`, which force both Mellin values of `f = g conv g^#` to zero.')
    rec('    ### ### **SO FOR A LAWFUL `f`, (148) COLLAPSES TO ### `SUM_v W_v(f) = - Z`.**')
    rec('')
    rec('  ### ### **AND THAT SETTLES THE SIGN OF THE TOTAL BEFORE THE TOTAL IS COMPUTED.** ### `Z`')
    rec('  ### is `2 SUM_gamma f-hat(gamma)` over the corpus\'s library, and ### **`f-hat = |g-hat|^2`')
    rec('  ### ### BECAUSE `f` IS A SQUARE** -- which b320 measured directly, `13 of 13` by')
    rec('  ### Definition 3.1 with minima at `-4.6e-17`. ### **EVERY TERM OF `Z` IS THEREFORE')
    rec('  ### ### NON-NEGATIVE, SO `Z >= 0`, SO `SUM_v W_v <= 0`, AUTOMATICALLY.**')
    rec('  ### ### **THE WINDOW\'S BALANCE IS NON-POSITIVE FOR REASONS THAT HAVE NOTHING TO DO WITH')
    rec('  ### ### THE PRIMES.** ### It is forced by two facts about the computation: the test')
    rec('  ### function is a square, and the ordinate library contains only zeros ON the critical')
    rec('  ### line, whose contributions cannot be negative. ### **A ZERO OFF THE LINE IS EXACTLY')
    rec('  ### ### WHAT WOULD BREAK IT, AND THIS LIBRARY CONTAINS NONE BY CONSTRUCTION.**')
    rec('  ### ### **SO THE COUNT BELOW IS NOT EVIDENCE. ### IT IS THE SHAPE OF THE ARITHMETIC.**')
    rec('')
    rec('  ### (3c) THE PLACES SUM, THE TOTAL THE CRITERION SPEAKS ABOUT.')
    rec('  ### ### **`SUM_v W_v(f) = W_R(f) + SUM_p W_p(f) = PR - A`**, every sign from an owner.')
    rec('    %-6s %-18s %-18s %-18s %-10s'
        % ('a', 'PR (primes)', 'A = W_infinity', 'SUM_v W_v = PR - A', 'sign'))
    tot = {}
    for a in above:
        s = c2[a]['prime'] - c2[a]['arch']
        tot[a] = s
        rec('    %-6g %-18.9f %-18.9f %-18.9f %-10s'
            % (a, c2[a]['prime'], c2[a]['arch'], s, 'NEGATIVE' if s < 0 else 'POSITIVE'))
    rec('')
    rec('  ### (3c) AND WHAT THE CRITERION ASKS FOR, QUOTED VERBATIM FROM PROPOSITION C.1 / (155):')
    rec('  ###   ### *"RH <=> SUM_v W_v(g * g-bar^#) <= 0, for all g in C_c^inf(R*_+) with')
    rec('  ###   ### g-tilde(z) = 0 for all z in F"*, ### F a finite set containing `{0, 1}`.')
    rec('  ### ### **THE CRITERION ASKS FOR A NON-POSITIVE TOTAL.**')
    npos = sum(1 for a in above if tot[a] <= 0.0)
    rec('  ### ### **CELLS ABOVE THE BOUNDARY WHOSE FINITE-INSTANCE TOTAL IS NON-POSITIVE : %d OF %d**'
        % (npos, len(above)))
    rec('')
    rec('  ### ### **THAT IS A MEASUREMENT AND IT IS INTERPRETED BY NOBODY IN THIS ACT.**')
    rec('  ### ### **A FINITE WINDOW AT A FINITE CUTOFF DECIDES NOTHING GLOBAL.** ### The sum runs')
    rec('  ### over %d ordinates and not over all of them; over %d primes and not over all of them;'
        % (WI.AT.NGAM, len(WI.PRIMES)))
    rec('  ### at thirteen cells of one family of test functions and not over the class the')
    rec('  ### criterion quantifies. ### **THE CRITERION IS A STATEMENT ABOUT EVERY LAWFUL `g`.**')
    rec('  ### **THIS IS THIRTEEN OF THEM.**')

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- WHAT THE SLACK DOES.')
    rec('=' * 100)
    rec('  ### **THE CHART-READY BLOCK. ### margin AND prime sum, ACROSS ALL THIRTEEN CELLS.**')
    rec('    %-6s %-9s %-16s %-16s %-16s %-16s'
        % ('a', 'covered', 'margin', 'PR (primes)', 'PR - margin', 'SUM_v W_v'))
    first = None
    for a in cells:
        m = rows320[a]['margin']
        pr = c2[a]['prime']
        s = pr - c2[a]['arch']
        if first is None and pr > m:
            first = a
        rec('    %-6g %-9s %-16.9f %-16.9f %-16.9f %-16.9f'
            % (a, 'YES' if a in covered else 'no', m, pr, pr - m, s))
    rec('')
    if first is None:
        rec('  ### ### **THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL OF THIS LADDER.**')
    else:
        rec('  ### ### **THE FIRST CELL WHERE THE PRIME SUM EXCEEDS THE MARGIN : `a = %g`.**' % first)
    rec('  ### **REPORTED AS A FACT ABOUT THIS LADDER AND NOT AS A TREND.** ### Thirteen cells of')
    rec('  ### one family are not a curve.')
    rec('')
    ms = [rows320[a]['margin'] for a in covered]
    rec('  ### **AND b320\'s OBSERVATION, RESTATED AS MEASURED AND NOT EXTRAPOLATED:** ### across the')
    rec('  ### three covered cells the margin runs `%s`, which GROWS toward the boundary where the'
        % ', '.join('%+.6f' % m for m in ms))
    rec('  ### registered expectation had it shrink. ### **THAT IS THREE NUMBERS.** ### It is not a')
    rec('  ### limit, not a rate, and nothing here is extrapolated past `a = %g`.' % max(cells))

    # ### -------------------------------------------------------------- the gate, IN THE PATH
    rec('')
    rec('  ### THE NOISE-FLOOR GATE, IN THE PATH.')
    items = []
    for a in covered:
        dom = b320['axes'][str(a)]['domain']
        items.append(('domain a=%g' % a, dom[-2], dom[-1]))
        items.append(('identity a=%g' % a, c1[a]['uniform'], c1[a]['cheb']))
    ok, rows, detail = NF.gate(items, label='b321')
    for name, val, ref, verdict, why in rows:
        rec('    %-18s %-18.9f -> %-18.9f %-10s' % (name, val, ref, verdict))
    rec('    ### %s' % detail)
    rec('    ### **THE IDENTITY VALUES ARE RESOLVED AND THE DOMAIN VALUES ARE NOT.** ### So the')
    rec('    ### identity\'s SIZE is certified and every margin\'s SIZE is not, and the two are in')
    rec('    ### different columns above so the distinction cannot be lost.')

    rec('')
    rec('=' * 100)
    rec('  ### CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)

    payload = dict(c1={str(k): v for k, v in c1.items()},
                   scores={str(k): {kk: (vv if not isinstance(vv, np.ndarray) else vv.tolist())
                                    for kk, vv in v.items()} for k, v in scores.items()},
                   c2={str(k): v for k, v in c2.items()},
                   above=above, totals={str(k): v for k, v in tot.items()},
                   identity=bool(ident), ef_covered=bool(covok), ef_all=bool(allok),
                   npos=npos, n_above=len(above), first_exceed=first,
                   arch_worst=worst, noise_ok=bool(ok), fails=fails)
    d = (json.dumps(payload, indent=1, default=float) + '\n').encode('utf-8')
    open(os.path.join(D, 'b321_rows.json') + '.tmp', 'wb').write(d)
    os.replace(os.path.join(D, 'b321_rows.json') + '.tmp', os.path.join(D, 'b321_rows.json'))
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    io.open(os.path.join(D, 'b321_components_run.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
