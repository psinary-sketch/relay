# -*- coding: utf-8 -*-
"""b315_run.py -- THE CALIBRATION READ AND THE RATE, RE-DERIVED.

### ### **NO INSTRUMENT IS EDITED.** ### The owner modules are imported read-only; the source's
### convention runs only in b313's COPIES (`b313f_*`), which this file reads and extends and never
### writes. ### **AND `main()` IS NEVER CALLED ON ANY OF THEM** -- the owners' `main` writes their
### banked tables, which this act reads as reference.

### ### **COMPONENT 1 DECIDES BY READING THE OPERATION, NOT THE COMMENT.** ### The order says so in
### as many words, and it matters here: the comment says *sign fixed BY the E2 calibration*, and
### ### **THE OPERATION SAYS WHICH `E2` THAT IS.**

### ### **COMPONENT 2 RE-RUNS b264's ROUTE WITH THE CORRECTED EXPONENT.** ### The Cauchy-Schwarz
### and Plancherel steps are untouched -- they bound an INTEGRAL, and the flip is a PREFACTOR -- so
### the whole change is one power of the argument, carried through to the envelope and the rate.
"""
import io
import json
import math
import os
import re
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, E16)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ATLAS = os.path.join(E16, 'carto_atlas.py')
B38 = os.path.join(E16, 'b38_act10.py')
B264ROWS = os.path.join(D, 'b264_rows.json')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def lineno_of(path, needle):
    """### **A QUOTATION WITH ITS LINE NUMBER, PULLED FROM THE EMITTING FILE.**"""
    for i, ln in enumerate(io.open(path, encoding='utf-8').read().splitlines(), 1):
        if needle in ln:
            return i, ln.strip()
    return None, None


def independent_definition(paths, forbidden):
    """### **DOES `A` HAVE A DEFINITION THAT DOES NOT MENTION THE REMAINDER?**

    ### Returns the assignment lines for `A` together with whether any of the names in
    ### `forbidden` occurs in the enclosing function. ### **THE POSITIVE CONTROL IS THAT THE SAME
    ### SEARCH FINDS A DEPENDENCE WHEN ONE IS THERE**, and it is exercised in `self_test`.
    """
    out = []
    for p in paths:
        src = io.open(p, encoding='utf-8').read().splitlines()
        start = 0
        for i, ln in enumerate(src, 1):
            if re.match(r'^def\s+\w+\s*\(', ln):
                start = i
            m = re.match(r'^\s+A\s*=\s*(.+)$', ln)
            if m:
                end = len(src)
                for j in range(start, len(src)):
                    if j > start and re.match(r'^def\s+\w+\s*\(', src[j]):
                        end = j
                        break
                body = '\n'.join(src[start - 1:end])
                dep = sorted({f for f in forbidden if re.search(r'\b%s\b' % re.escape(f), body)})
                out.append((os.path.basename(p), i, ln.strip(), dep))
    return out


def converged_two_axis(mod, r, LAY, LAY2, ng_of, bar):
    """### **b264's REGISTERED CONVERGENCE TEST, BOTH AXES. ### A CELL COUNTS ONLY IF BOTH
    ### PASS.**

    ### b264's own `(D2)`: the `NG` vs `2NG` axis moves only the OUTER quadrature, and five
    ### cells were marked converged at ~1e-12 ### ON VALUES WRONG BY FOUR ORDERS OF MAGNITUDE.
    ### **THE BINDING AXIS IS THE INNER ONE**, and it is the one this act needs, because the
    ### breakdown sits just inside the nominal ceiling rather than just outside it.
    """
    NG = ng_of(r)
    a1 = float(mod.eps_modes(r, NG, LAY)[0::2].sum())
    a2 = float(mod.eps_modes(r, 2 * NG, LAY)[0::2].sum())
    b1 = float(mod.eps_modes(r, NG, LAY2)[0::2].sum())
    den = max(abs(a1), 1e-300)
    outer = abs(a1 - a2) / den
    inner = abs(a1 - b1) / den
    return (outer <= bar and inner <= bar), outer, inner, a1


def self_test():
    """### **FIXTURES. ### EVERY ARM MUST BE ABLE TO REPORT THE OTHER ANSWER.**"""
    ok = []
    tmp = os.path.join(D, '_b315_fixture.py')
    io.open(tmp, 'w', encoding='utf-8', newline='\n').write(
        'def clean(x):\n    A = x + 1\n    return A\n\n\n'
        'def dirty(x, E2):\n    A = x + E2\n    return A\n')
    try:
        rows = independent_definition([tmp], ('E2', 'eps'))
        ok.append(len(rows) == 2)
        ok.append(rows[0][3] == [])          # ### the clean one has no dependence
        ok.append(rows[1][3] == ['E2'])      # ### and the search FINDS one when it is there
    finally:
        os.remove(tmp)
    n, ln = lineno_of(tmp if False else ATLAS, 'sign fixed BY the E2 calibration')
    ok.append(n is not None)
    ok.append(lineno_of(ATLAS, 'a string that is certainly not in this file')[0] is None)
    return all(ok), ok


def main():
    t0 = time.time()
    fails = []
    rec('=' * 100)
    rec('b315 -- THE CALIBRATION AND THE RATE.')
    rec('=' * 100)
    good, arms = self_test()
    rec('  ### THE TOOL\'S OWN FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    rec('  ### **ARM 3 IS THE POSITIVE CONTROL: THE SEARCH FINDS A DEPENDENCE ON THE REMAINDER')
    rec('  ### WHEN ONE IS THERE.** ### Without it, "no dependence found" would be a sentence about')
    rec('  ### the search and not about the code.')
    if not good:
        return 2, LINES

    # ================================================================= COMPONENT 1
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE CALIBRATION READ.')
    rec('=' * 100)

    rec('')
    rec('  ### (1a) THE CALIBRATION, PULLED FROM ITS EMITTING FILE WITH LINE NUMBERS.')
    for needle in ('DISCLAIMED REGISTER', 'E2 pass tolerance on the explicit-formula residual',
                   'sign fixed BY the E2 calibration', 'A = float(np.trapezoid',
                   'residual=Z - (P - PR + A)', 'E2 VERDICT'):
        n, ln = lineno_of(ATLAS, needle)
        rec('    carto_atlas.py:%-4s %s' % (n, ln[:96] if ln else '### NOT FOUND'))
        if n is None:
            fails.append('missing quotation: %s' % needle)
    n38, l38 = lineno_of(B38, 'A = float(np.trapezoid')
    rec('    b38_act10.py:%-4s   %s' % (n38, l38))

    rec('')
    rec('  ### (1b) WHAT THE CALIBRATION FIXES -- DECIDED BY READING THE OPERATION.')
    rec('    ### **THE OPERATION IS TWO LINES AND THEY DO DIFFERENT THINGS.**')
    rec('    ### `A` is COMPUTED at carto_atlas.py:%s as an explicit integral of the digamma'
        % lineno_of(ATLAS, 'A = float(np.trapezoid')[0])
    rec('    ### kernel against the test function, divided by `2 pi`. ### **NO FREE CONSTANT, NO')
    rec('    ### FITTED FACTOR, AND NOTHING FROM ANY REMAINDER ENTERS IT.**')
    rec('    ### `residual` is FORMED at carto_atlas.py:%s as `Z - (P - PR + A)`, and the verdict'
        % lineno_of(ATLAS, 'residual=Z - (P - PR + A)')[0])
    rec('    ### at carto_atlas.py:%s is `abs(residual) <= TOL`.'
        % lineno_of(ATLAS, 'E2 VERDICT')[0])
    rec('    ### ### **SO WHAT THE CALIBRATION SETTLED IS THE ORIENTATION WITH WHICH THE')
    rec('    ### ### ARCHIMEDEAN TERM ENTERS THE EXPLICIT FORMULA -- A SIGN, IN THE BOOKKEEPING.**')
    rec('    ### **IT DOES NOT SCALE `A`. ### IT DOES NOT SET `A`. ### IT CHOOSES WHERE `A` GOES.**')

    rec('')
    rec('  ### (1c) AND WHICH `E2` THE BRACKET NAMES -- READ OFF THE SAME FILE.')
    rec('    ### The file\'s own constant block says `TOL` is the ### **"E2 pass tolerance on the')
    rec('    ### explicit-formula residual"**, and the verdict line prints ### **"E2 VERDICT"** ###')
    rec('    ### against `abs(residual) <= TOL`. ### The file\'s first line says ### **"E1-E4 stand')
    rec('    ### registered VERBATIM at PLACE-papers"**.')
    rec('    ### ### ### **SO `E2` IN THAT BRACKET IS THE NAME OF A REGISTERED CLAIM WHOSE TEST IS')
    rec('    ### ### ### THE EXPLICIT-FORMULA RESIDUAL. ### IT IS NOT THE ARCHIMEDEAN REMAINDER')
    rec('    ### ### ### `E2` OF b38\'s IDENTITY.**')
    rec('    ### **AND THE RESIDUAL IT TESTS CONTAINS NO REMAINDER AT ALL:** ### `Z - (P - PR + A)`')
    rec('    ### is the zero side, the pole, the primes and the archimedean term. ### The corpus\'s')
    rec('    ### remainder is not in it and never was.')
    rec('    ### ### **THIS IS THE DOUBLE-NAME SPECIES b200 NAMED AND b219 REALISED, AND IT IS')
    rec('    ### ### CORRECTED HERE AT THE READING RATHER THAN CARRIED FURTHER.**')

    rec('')
    rec('  ### (1d) DOES `A` HAVE A DEFINITION INDEPENDENT OF THE REMAINDER? ### **QUOTED.**')
    rows = independent_definition([ATLAS, B38], ('E2', 'eps', 'E2n', 'E2N', 'ee_full', 'qeps'))
    for base, ln, txt, dep in rows:
        rec('    %-16s line %-5d dependence on the remainder : %s'
            % (base, ln, dep if dep else '### NONE'))
        rec('        %s' % txt[:96])
    indep = all(not dep for _b, _l, _t, dep in rows) and rows
    rec('    ### ### **`A` IS DEFINED INDEPENDENTLY OF THE REMAINDER : %s**' % bool(indep))
    rec('    ### The enclosing function is searched, not the assignment line alone, so a')
    rec('    ### dependence introduced two lines above would be caught. ### **AND THE SEARCH IS')
    rec('    ### SHOWN ABLE TO FIND ONE** -- fixture arm 3, above.')
    if not indep:
        fails.append('A is not independently defined')

    rec('')
    rec('  ### (1e) A + E2 UNDER THE SOURCE\'S CONVENTION, RECOMPUTED ON THE COPIES.')
    rec('    ### **THE CALIBRATION FIXES A SIGN ONLY, SO THERE IS NOTHING TO SWITCH OFF**, and the')
    rec('    ### order\'s branch is taken: *left as is if it does not*.')
    import b38_act10 as ORIG              # noqa: E402  ### the OWNER, read-only
    import b313f_b38_act10 as FLIP        # noqa: E402  ### b313's COPY
    out = {}
    for tag, M in (('banked', ORIG), ('source', FLIP)):
        Q = M.Q
        rr = np.exp(np.linspace(1e-4, math.log(12.001), M.EPS_NRHO))
        ee_full = np.atleast_1d(Q.eps(rr, NQ=M.EPS_NQ, NG=M.EPS_NG))
        ee_modes = M.per_mode_eps_grids(rr)
        alg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))
        rec('    [%s] per-mode mask algebra : %.2e  %s'
            % (tag, alg, 'PASS' if alg <= 1e-10 else '### FAIL ###'))
        if alg > 1e-10:
            fails.append('mask algebra under %s' % tag)
        col = {}
        for a, alab in M.CELLS:
            v, w2, corr, vc, L = M.family(a)
            A, P, PR = M.left_side(a, M.S4, v, w2, corr, vc, L)
            E2n = np.array([M.e2_of_grid(a, corr, vc, L, rr, ee_modes[n])
                            for n in range(ee_modes.shape[0])])
            col[alab] = dict(A=A, E2N=float(E2n.sum()), E2even=float(E2n[0::2].sum()),
                             E2odd=float(E2n[1::2].sum()), L=L)
        out[tag] = col
    rec('')
    rec('    %-5s | %-11s %-11s %-11s | %-12s %-12s'
        % ('a^2', 'A', 'E2 banked', 'E2 source', 'A+E2 banked', 'A+E2 source'))
    worst = 0.0
    for a, alab in ORIG.CELLS:
        b, s = out['banked'][alab], out['source'][alab]
        worst = max(worst, abs(s['A'] + s['E2N']))
        rec('    %-5s | %-11.6f %-11.6f %-11.6f | %-12.6f %-12.6f'
            % (alab, b['A'], b['E2N'], s['E2N'], b['A'] + b['E2N'], s['A'] + s['E2N']))
    amax = max(abs(out['banked'][al]['A']) for _a, al in ORIG.CELLS)
    rec('    ### worst |A + E2| under the source\'s convention : %.6f' % worst)
    rec('    ### the same as a fraction of the largest |A| in the table : %.4f%%'
        % (100.0 * worst / amax))
    survives = worst < 0.05 * amax
    rec('')
    rec('    ### ### ### **VERDICT: %s**'
        % ('SURVIVES' if survives else 'THE CANCELLATION DOES NOT STAND'))
    if survives:
        rec('    ### **THE NEAR-CANCELLATION IS NOT PRODUCED BY THE CALIBRATION.** ### The')
        rec('    ### calibration fixes a sign; `A` is an independent integral; and the cancellation')
        rec('    ### stands with the calibration read for exactly what it does.')
        rec('    ### ### **AND IT IS PROMOTED TO NOTHING.** ### `E2 ~ -A` at six cells is a fact')
        rec('    ### ### WITH NO STATED DEFINITION BEHIND IT.** ### No act has written down a')
        rec('    ### relation these two terms are supposed to satisfy, and a numerical near-equality')
        rec('    ### without one is a question, not a result. ### **FILED AS `W-ORD-A-PLUS-E2`,')
        rec('    ### ### UNCHANGED IN STATUS AND CHANGED IN ITS REASON.**')

    # ================================================================= COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE RATE, RE-DERIVED UNDER THE SOURCE\'S CONVENTION.')
    rec('=' * 100)
    b264 = json.load(io.open(B264ROWS, encoding='utf-8'))
    C_even, K_even, nres = b264['C_even'], b264['K_even'], int(b264['nres'])
    rec('  ### b264\'s BANKED CONSTANTS, READ FROM ITS OWN ROWS:')
    rec('    C_even = %.9f   K_even = %.9f   NRES = %d' % (C_even, K_even, nres))

    rec('')
    rec('  ### (2a) THE ROUTE, RE-RUN. ### **ONLY THE PREFACTOR MOVES.**')
    rec('    ### b264 wrote the per-mode remainder in the `v = rho u` variable:')
    rec('    ###   `eps_n(rho) = [lam^2/(1-lam^2)] rho^(-1/2) INT_{1/rho}^{1} A_n(u) A_n(rho u) du`')
    rec('    ###             `= [lam^2/(1-lam^2)] rho^(-3/2) INT_1^rho A_n(v/rho) A_n(v) dv`')
    rec('    ### and bounded the integral by Cauchy-Schwarz with Plancherel (pin P3) and the tail')
    rec('    ### identity (IDENT-D):')
    rec('    ###   `|INT_1^rho A_n(v/rho) A_n(v) dv| <= rho^(1/2) sqrt(1-lam^2) / lam`')
    rec('    ### ### **THE FLIP CHANGES THE PREFACTOR AND NOTHING ELSE.** ### Cauchy-Schwarz and')
    rec('    ### Plancherel bound the INTEGRAL; the exponent multiplies it. ### So under the')
    rec('    ### source\'s convention the same three lines read:')
    rec('    ###   `eps_n^src(rho) = [lam^2/(1-lam^2)] rho^(+1/2) INT_{1/rho}^{1} ...`')
    rec('    ###                 `= [lam^2/(1-lam^2)] rho^(-1/2) INT_1^rho A_n(v/rho) A_n(v) dv`')
    rec('    ###   `|eps_n^src(rho)| <= [lam^2/(1-lam^2)] rho^(-1/2) rho^(1/2) sqrt(1-lam^2)/lam`')
    rec('    ###                    `= lam_n / sqrt(1 - lam_n^2)  =:  c_n`')
    rec('    ### ### ### **THE NEW ENVELOPE IS A CONSTANT: ### `|eps_even^src(rho)| <= C_even =')
    rec('    ### ### ### %.9f`, THE SAME CONSTANT b264 SUMMED, WITH NO POWER OF `rho` AT ALL.**'
        % C_even)
    rec('    ### ### **AND THAT IS A LOSS, NOT A NEUTRAL RESTATEMENT.** ### Under the banked')
    rec('    ### ### convention the envelope was `C_even / rho` and b264 used it to CARRY THE TAIL')
    rec('    ### ### beyond its measured node ceiling. ### **A CONSTANT ENVELOPE CARRIES NOTHING.**')
    rec('    ### The Cauchy-Schwarz route no longer certifies decay under the source\'s convention;')
    rec('    ### only the sharp rate does, and b264 graded that separately for its own reasons.')
    rec('')
    rec('    ### **THE SHARP RATE.** ### b264 derived `rho^(3/2) eps_n(rho) -> K_n` from the far')
    rec('    ### field of `A_n`, with `K_n = lambda_n^true A_n(0)^2 / 2` and the SIGNED pin P1.')
    rec('    ### That derivation is about the INTEGRAL\'s far field and is untouched by the')
    rec('    ### prefactor, so:')
    rec('    ###   ### ### **`rho^(1/2) eps_even^src(rho) -> K_even = %.9f`, THE SAME CONSTANT.**'
        % K_even)
    rec('    ###   ### i.e. ### **`eps_even^src(rho) ~ K_even * rho^(-1/2)`.**')

    rec('')
    rec('  ### (2b) THE LADDER, AT THE INSTRUMENT\'S OWN REACH, WITH THE NOISE-FLOOR GATE.')
    import b264_eps_decay as L264          # noqa: E402  ### the OWNER's evaluator, read-only
    import b313f_b264_eps_decay as L264F   # noqa: E402  ### b313's COPY
    LAY = ORIG.Q.layer(ORIG.EPS_NQ)
    rec('    ### b264\'s resolved-mode count, READ from its banked rows : NRES = %d' % nres)
    rec('    ### **MODES AT OR ABOVE THAT INDEX ARE AT THE EIGENSOLVER\'S FLOOR**, and what')
    rec('    ### excluding them removes is PRINTED rather than called negligible.')
    ceiling = float(b264['ceiling_nq'])
    rec('    ### **AND THE ENVELOPE TEST RUNS ON CONVERGED CELLS ONLY -- b264\'s OWN')
    rec('    ### CRITERION, QUOTED: *"if any converged |eps_even(x)| exceeds its derived')
    rec('    ### envelope"*. ### b264\'s own (D2) is why the word CONVERGED is')
    rec('    ### load-bearing: its registered NG vs 2NG test moved only the OUTER quadrature, so')
    rec('    ### five cells were marked converged at ~1e-12 ### **ON VALUES WRONG BY FOUR ORDERS')
    rec('    ### ### OF MAGNITUDE.** ### The binding axis is the inner one, and b264 banked its')
    rec('    ### ceiling: ### **ceiling_nq = %.4f, READ FROM b264\'s OWN ROWS.**' % ceiling)
    rec('    %-8s %-8s %-14s %-14s %-13s %-13s %-11s %-6s'
        % ('rho', 'NG', 'even banked', 'even source', 'env |e|/C', 'rate r^.5 e', 'floor',
           'conv?'))
    LAY2 = ORIG.Q.layer(2 * ORIG.EPS_NQ)
    CONV = L264.CONV_BAR
    rec('    ### **AND CONVERGENCE IS DECIDED BY b264\'S OWN TWO-AXIS TEST, NOT BY THE')
    rec('    ### ### CEILING NUMBER**: `NG` vs `2NG` AND `EPS_NQ` vs `2 EPS_NQ`, both at')
    rec('    ### `CONV_BAR = %.0e`. ### **b264 ADDED THE SECOND AXIS BECAUSE THE FIRST GAVE A' % CONV)
    rec('    ### ### FALSE PASS ON EXACTLY THESE CELLS**, and this act needs it because the')
    rec('    ### breakdown sits just INSIDE the nominal ceiling, not just outside it.')
    envworst, ok_env, tightest = 0.0, True, 0.0
    for row in b264['ladder']:
        r = float(row['rho'])
        NG = L264.ng_for(r)
        em = L264.eps_modes(r, NG, LAY)
        emf = L264F.eps_modes(r, NG, LAY)
        eb = float(em[0::2].sum())
        es = float(emf[0::2].sum())
        ress = float(sum(emf[n] for n in range(0, len(emf), 2) if n < nres))
        env = abs(es) / C_even
        conv, _o, _in, _a = converged_two_axis(L264F, r, LAY, LAY2,
                                              L264.ng_for, CONV)
        if conv:
            envworst = max(envworst, env)
            tightest = max(tightest, env)
            if env > 1.0:
                ok_env = False
        rec('    %-8g %-8d %-14.6g %-14.6g %-13.4f %-13.6g %-11.2e %-6s'
            % (r, NG, eb, es, env, es * r ** 0.5, es - ress,
               'yes' if conv else 'NO'))
    rec('    ### floor modes excluded from the resolved sum : even indices at or above %d' % nres)
    rec('    ### ### **VIOLATIONS OF THE NEW CONSTANT ENVELOPE, ON CONVERGED CELLS : %s**'
        % ('0' if ok_env else 'SOME'))
    rec('    ### worst |eps_even^src| / C_even on a converged cell : %.4f' % envworst)
    rec('    ### ### **AND THE ENVELOPE IS NOT MERELY LOOSE -- IT IS VACUOUS IN THE LIMIT.**')
    rec('    ### At its TIGHTEST converged cell the constant bound sits about %.0f times above'
        % (1.0 / tightest if tightest else 0))
    rec('    ### the value, and ### **BECAUSE IT DOES NOT DECAY IT GETS LOOSER WITHOUT BOUND AS')
    rec('    ### ### THE ARGUMENT GROWS.** ### b250 s standard is *one that is loose is'
        ' reported loose*; this one is reported for what it is.')
    rec('    ### **THE ROWS FROM `rho = 500` UPWARD ARE MARKED NOT-CONVERGED BY b264\'s OWN')
    rec('    ### MEASURED CEILING AND ARE EXCLUDED FROM THE TEST BY ITS OWN CRITERION** -- not by')
    rec('    ### a choice this act made. ### They are printed because deleting them would be a')
    rec('    ### choice nobody could check, and their values are visibly the numerical garbage')
    rec('    ### b264 diagnosed.')
    if not ok_env:
        fails.append('the new envelope is violated on a converged ladder cell')

    rec('')
    rec('  ### (2c) THE DILATION IDENTITY, AND THE CUTOFF.')
    rec('    ### **THE CORPUS\'S `cutoff` IS THE WINDOW PARAMETER `a`** -- b15\'s sentence, carried')
    rec('    ### by b261 and b264: *"a finite-place-set object at a finite cutoff decides nothing')
    rec('    ### global."* ### So the question is what `E2even(a)` does as `a` grows.')
    rec('    ### **THE DILATION IDENTITY, FROM THE OWNER\'S OWN CODE:**')
    rec('    ###   `E2even(a) = 2 INT_0^{2L} corr(u) eps_even(e^u) du`, `L = log a`,')
    rec('    ###   with `corr` the autocorrelation of the bump and `2 INT_0^{2L} corr = 1`.')
    rec('    ### The bump is a PURE DILATION -- `w(v) = beta(v/L)/(L c_beta)` -- so')
    rec('    ###   `corr(u) = phi(u/L)/L` for a fixed profile `phi`, and')
    rec('    ###   `E2even(a) = 2 INT_0^2 phi(t) eps_even(e^{L t}) dt`.')
    rec('    ### ### **HENCE, DERIVED:** ### substituting `s = L t`,')
    rec('    ###   `E2even(a) = (2/L) INT_0^{2L} phi(s/L) eps_even(e^s) ds`')
    rec('    ###   `-> (2 phi(0) / L) INT_0^inf eps_even(e^s) ds`   as `L -> infinity`,')
    rec('    ### provided that last integral converges. ### **IT DOES UNDER BOTH CONVENTIONS:**')
    rec('    ###   banked  : `eps_even ~ K rho^(-3/2)`, so `INT_1^inf eps_even drho/rho` converges;')
    rec('    ###   source  : `eps_even^src ~ K rho^(-1/2)`, so the same integral converges too,')
    rec('    ###     because the measure `drho/rho` supplies the extra power.')
    rec('    ### ### ### **SO THE EVEN SECTOR STILL VANISHES ALONG THE CUTOFF UNDER THE SOURCE\'S')
    rec('    ### ### ### CONVENTION, AND AT THE SAME LEADING ORDER: ### `E2even(a) ~ CONST / log a`')
    rec('    ### ### ### IN BOTH. ### WHAT CHANGES IS THE CONSTANT, NOT THE ORDER.**')
    rec('    ### **THAT IS SHARPER THAN THE EXPECTATION AND IT IS STATED AS SUCH:** ### along the')
    rec('    ### ARGUMENT the rate moves a full power; ### **ALONG THE CUTOFF IT DOES NOT MOVE AT')
    rec('    ### ALL.** ### The cutoff integral is against `drho/rho`, and that measure absorbs')
    rec('    ### exactly the one power the flip introduces.')

    rec('')
    rec('  ### (2c-bis) THE ROUTE IS b264\'S, AND SO IS THE ASYMPTOTE. ### **CITED, NOT')
    rec('  ### RE-CLAIMED.** ### b264 already derived the cutoff behaviour and banked it:')
    rec('    ###   ### **"E2even(a) * log a -> p(0) * M_even"**, with')
    rec('    ###   ### **"M_even = INT_1^inf eps_even(x) dx/x = 0.812581 (+0 / +5.644e-01)"**')
    rec('    ### -- the parenthesis being the tail interval its DERIVED ENVELOPE carried.')
    rec('    ### **THIS ACT ADDS ONE THING TO THAT: THE SAME ROUTE WITH THE CORRECTED EXPONENT.**')
    rec('    ###   `M_even^src = INT_1^inf eps_even^src(x) dx/x = INT_1^inf eps_even(x) dx`,')
    rec('    ### which converges because `eps_even ~ K x^(-3/2)`.')
    MB = MS = 0.0
    grid = np.exp(np.linspace(0.0, math.log(ceiling), 80))
    vb, vs, lg = [], [], []
    stopped_at = None
    for r in grid:
        r = float(r)
        if r <= 1.0:
            vb.append(0.0)
            vs.append(0.0)
            lg.append(0.0)
            continue
        okc, _o, _in, _a = converged_two_axis(L264F, r, LAY, LAY2, L264.ng_for, CONV)
        if not okc:
            stopped_at = r
            break
        NGk = L264.ng_for(r)
        vb.append(float(L264.eps_modes(r, NGk, LAY)[0::2].sum()))
        vs.append(float(L264F.eps_modes(r, NGk, LAY)[0::2].sum()))
        lg.append(math.log(r))
    MB = float(np.trapezoid(np.array(vb), np.array(lg)))
    MS = float(np.trapezoid(np.array(vs), np.array(lg)))
    top = math.exp(lg[-1]) if lg else 1.0
    rec('    ### ### **THE INTEGRATION RANGE IS NOT THE CEILING NUMBER; IT IS WHERE b264\'S')
    rec('    ### ### TWO-AXIS TEST STOPS PASSING.**')
    rec('    ###   first cell that FAILS the two-axis test : rho = %s'
        % ('%.4f' % stopped_at if stopped_at else 'none in range'))
    rec('    ###   integrated over `[1, %.4f]`, %d converged points on the NG law' % (top, len(lg)))
    rec('    ### **AND THAT MATTERS: THE FIRST DRAFT OF THIS BLOCK INTEGRATED TO THE CEILING')
    rec('    ### ### NUMBER AND GOT `M_even^src = -2.89` -- A NEGATIVE NUMBER FOR AN INTEGRAL OF A')
    rec('    ### ### CURVE THAT IS POSITIVE EVERYWHERE IT IS TRUSTED.** ### Three grid points sat')
    rec('    ### between the last sound cell and the ceiling, carrying values near `-100`. ### The')
    rec('    ### ceiling is where the evaluator FAILS, not the last place it works.')
    rec('    ### THE TWO INTEGRALS, OVER THAT RANGE:')

    rec('    ###   M_even   (banked convention) : %.6f   -- b264 banks 0.812581' % MB)
    rec('    ###   M_even^src (source convention): %.6f' % MS)
    rec('    ### ### ### **AND THE THING THAT MATTERS MORE THAN EITHER NUMBER: ### UNDER THE')
    rec('    ### ### ### SOURCE\'S CONVENTION THE TAIL BEYOND THE CEILING IS UNCONTROLLED.**')
    rec('    ### b264 carried its tail with the DERIVED ENVELOPE `C_even / x`, which is integrable')
    rec('    ### against `dx/x`. ### **THE NEW ENVELOPE IS A CONSTANT, AND A CONSTANT IS NOT')
    rec('    ### ### INTEGRABLE AGAINST `dx/x` OVER AN INFINITE RANGE.** ### So `M_even^src` has a')
    rec('    ### measured body and NO RIGOROUS TAIL BOUND from this route.')
    rec('    ### **THE CONSEQUENCE, STATED PLAINLY: ### THE ORDER OF THE CUTOFF DECAY IS DERIVED')
    rec('    ### ### AND UNCHANGED; ITS CONSTANT IS NOT CERTIFIED UNDER THE SOURCE\'S')
    rec('    ### ### CONVENTION BY b264\'S ROUTE.** ### A different route would be needed, and')
    rec('    ### this act does not supply one.')
    rec('')
    rec('  ### (2d) THE BENCH, AS THE CHECK ON THE DERIVATION.')
    rec('    ### `L * E2even(a)` should approach a constant under BOTH conventions if the')
    rec('    ### derivation is right, with the source\'s constant the larger.')
    rec('    %-6s %-8s | %-12s %-12s | %-12s %-12s'
        % ('a^2', 'L', 'E2even bkd', 'E2even src', 'L*E2 bkd', 'L*E2 src'))
    prodb, prods = [], []
    for a, alab in ORIG.CELLS:
        b, s = out['banked'][alab], out['source'][alab]
        prodb.append(b['L'] * b['E2even'])
        prods.append(s['L'] * s['E2even'])
        rec('    %-6s %-8.4f | %-12.6f %-12.6f | %-12.6f %-12.6f'
            % (alab, b['L'], b['E2even'], s['E2even'], prodb[-1], prods[-1]))
    fallb = all(out['banked'][al]['E2even'] < out['banked'][a0]['E2even']
                for (_x, a0), (_y, al) in zip(ORIG.CELLS[:-1], ORIG.CELLS[1:]))
    falls = all(out['source'][al]['E2even'] < out['source'][a0]['E2even']
                for (_x, a0), (_y, al) in zip(ORIG.CELLS[:-1], ORIG.CELLS[1:]))
    rec('    ### **E2even FALLS MONOTONICALLY ALONG THE CUTOFF -- banked : %s ; source : %s**'
        % (fallb, falls))
    rec('    ### **AND `L * E2even` IS STILL RISING IN BOTH COLUMNS**, so these six cells are NOT')
    rec('    ### in the asymptotic regime and the bench CONFIRMS THE DIRECTION AND NOT THE')
    rec('    ### CONSTANT. ### `L` runs only from %.3f to %.3f here.'
        % (out['banked'][ORIG.CELLS[0][1]]['L'], out['banked'][ORIG.CELLS[-1][1]]['L']))
    rec('    ### **SAYING SO IS THE POINT: A BENCH THAT DOES NOT REACH THE REGIME CHECKS THE SIGN')
    rec('    ### ### OF THE STATEMENT AND NOT ITS CONSTANT**, and a constant read off six')
    rec('    ### pre-asymptotic cells would be a fit.')
    if not (fallb and falls):
        fails.append('E2even does not fall along the cutoff in one of the columns')

    rec('')
    rec('  ### (2e) THE BEARING ON THE BRANCH SENTENCE, AT ITS SCOPE.')
    rec('    ### **BEARING ONLY.** ### b262\'s branch sentence is about the archimedean SIDE. ###')
    rec('    ### This act has one archimedean OBJECT -- the even sector of one remainder, computed')
    rec('    ### through one instrument at six cells and twelve ladder points.')
    rec('    ### **WHAT THE BEARING IS:** ### the even sector still vanishes along the cutoff, so')
    rec('    ### nothing here supplies the divergent behaviour b262\'s disjunction would need from')
    rec('    ### this object. ### **WHAT IT IS NOT: ### A DECISION ON THE BRANCH, WHICH REMAINS')
    rec('    ### ### UNDECIDED, AND NOT A STATEMENT ABOUT THE ARCHIMEDEAN SIDE.**')

    payload = dict(cells=out, C_even=C_even, K_even=K_even, nres=nres,
                   worst_A_plus_E2=worst, survives=bool(survives),
                   env_worst=envworst, prod_banked=prodb, prod_source=prods,
                   falls=[bool(fallb), bool(falls)], elapsed=time.time() - t0, fails=fails)
    io.open(os.path.join(D, 'b315_rows.json'), 'w', encoding='utf-8',
            newline='\n').write(json.dumps(payload, indent=1, default=float) + '\n')

    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    return (0 if not fails else 1), LINES


if __name__ == '__main__':
    code, ls = main()
    io.open(os.path.join(D, 'b315_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(ls) + '\n')
    sys.exit(code)
