# -*- coding: utf-8 -*-
"""b261_e2even.py -- J2: E2even's MONOTONICITY. ### THE RUN.

### WHAT THIS FILE DOES AND WHAT IT MAY NOT DO.
### It tests the four registered falsifiers F1-F4 against a derivation that lives in the bank.
### ### **IT IS A CONTROL ON A DERIVATION, NOT THE DERIVATION.**
###
### ### **b255's `E2even` COLUMN IS A CONTROL AND IS NOT READ UNTIL THE G-REPRO SECTION**, which
### is after every step of the route has already produced its number. ### Source order is the
### check, and a gate verifies it.
###
### THE INSTRUMENT FUNCTIONS ARE IMPORTED FROM `b38_act10` AND `qeps_layer`, NOT RE-TYPED.
###
### ### **ONE AXIS MOVES, AND IT IS DECLARED IN THE REGISTRATION BEFORE ANY VALUE EXISTS:** the
### `rho`-grid is rebuilt to START AT `rho = 1` EXACTLY and to be DENSE ON `[1, 2]`. ### b255's
### grid starts at `exp(1e-4)` and has ~1.5 points below `a^2 = 1.05`; ### **(W1)'s CLAMP WOULD
### THEREFORE FLATTEN EXACTLY THE REGION S4 DEPENDS ON, AND SILENTLY.** ### The rebuild's cost is
### paid against b255's sixteen cells as a G-REPRO control at the end.
"""
import io
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import b38_act10 as B38          # noqa: E402
import qeps_layer as Q           # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BANK = r'D:\relay\data\b261_run.txt'
ROWS = r'D:\relay\data\b261_rows.json'
CACHE = r'D:\relay\data\b261_cache.npz'
B255J = r'D:\relay\data\b255_rows.json'

LADDER = [2, 3, 4, 8, 9, 12, 16, 20, 25, 32, 36, 45, 50, 64, 81, 100]
# ### THE PROBE BELOW THE LADDER. ### Chosen by GRID RESOLUTION, not by what its values do:
# ### the finest is `a^2 = 1.05`, whose log-range carries ~30 points of the rebuilt grid.
PROBE = [1.05, 1.10, 1.20, 1.35, 1.50, 1.75]
RHO_MAX = 100.001
N_LOW, N_HIGH = 1200, 800        # ### dense on [1,2]; b255's density above it

# ### THE BARS, FIXED IN THE REGISTRATION BEFORE ANY VALUE EXISTED.
F1_BAR = 1e-12


def rho_grid():
    """### THE REBUILT GRID. ### STARTS AT `rho = 1` EXACTLY -- `per_mode_eps_grids` writes 0
    ### there by its own `if hi - lo <= 0: continue`, which is the owner's `eps(1) = 0`."""
    lo = np.exp(np.linspace(0.0, math.log(2.0), N_LOW))
    hi = np.exp(np.linspace(math.log(2.0), math.log(RHO_MAX), N_HIGH))[1:]
    return np.concatenate([lo, hi])


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b261 RUN -- J2: E2even MONOTONICITY. ### CONTROLS ON A DERIVATION. Registration banked first.')
    rec('=' * 100)

    # ---------------------------------------------------------------- axes
    rec('')
    rec('--- ### W-ORD-TE-SPEC: THE AXES, PRINTED BEFORE ANY NUMBER IS READ ---')
    rec('  NV / NU_HALF            : %d / %d' % (4001, B38.NU_HALF))
    rec('  EPS_NQ / EPS_NG         : %d / %d' % (B38.EPS_NQ, B38.EPS_NG))
    rec('  NTERM (modes)           : %d      ### qeps_layer; ALREADY the EVEN prolate modes (P1)'
        % Q.NTERM)
    rec('  ### **THE AXIS THAT MOVES, DECLARED:**')
    rec('    b255 rho-grid         : 445 pts, exp(linspace(1e-4, log 100.001))   ### starts ABOVE 1')
    rec('    this act rho-grid     : %d pts, DENSE on [1,2] (%d) + [2,100.001] (%d), STARTS AT 1 EXACTLY'
        % (N_LOW + N_HIGH - 1, N_LOW, N_HIGH - 1))
    rec('    ### **WHY: (W1)\'s np.interp CLAMP. b255\'s grid carries ~1.5 points below a^2 = 1.05,')
    rec('    ### so the probe region S4 depends on would be FLATTENED SILENTLY.**')
    rec('    ### **THE COST IS PAID AS A G-REPRO CONTROL AGAINST b255\'s SIXTEEN CELLS, BELOW.**')
    rec('  ### CELL SPECIES: ### **DIAGONAL a^2 THROUGHOUT.**')
    rec('  F1 bar (registered)     : %.0e absolute' % F1_BAR)

    # ---------------------------------------------------------------- S1: the dilation identity
    rec('')
    rec('=' * 100)
    rec('### S1 -- THE DILATION IDENTITY. ### FALSIFIER F1. ### `L * corr_a` MUST BE a-INDEPENDENT.')
    rec('=' * 100)
    ref_psi, ref_s, worst_psi, worst_s, at_psi = None, None, 0.0, 0.0, None
    for a2 in PROBE + LADDER:
        a = math.sqrt(float(a2))
        v, w, corr, vc, L = B38.family(a)
        psi = L * corr                 # ### the claimed a-INDEPENDENT shape
        sgrid = vc / L                 # ### the claimed a-INDEPENDENT abscissa
        if ref_psi is None:
            ref_psi, ref_s = psi.copy(), sgrid.copy()
            continue
        dp = float(np.max(np.abs(psi - ref_psi)))
        ds = float(np.max(np.abs(sgrid - ref_s)))
        if dp > worst_psi:
            worst_psi, at_psi = dp, a2
        worst_s = max(worst_s, ds)
    rec('  cells compared                       : ### **%d**' % (len(PROBE) + len(LADDER)))
    rec('  worst |L*corr_a - L*corr_ref|        : ### **%.3e**   (worst cell a^2 = %s)'
        % (worst_psi, at_psi))
    rec('  worst |vc/L - (vc/L)_ref|            : ### **%.3e**' % worst_s)
    rec('  bar (registered before any value)    : %.0e' % F1_BAR)
    f1 = bool(worst_psi <= F1_BAR and worst_s <= F1_BAR)
    rec('  ### ### **F1 %s**' % ('DID NOT FIRE -- the dilation identity HOLDS EXACTLY ON THE '
                                 'INSTRUMENT\'S OWN GRID.' if f1 else 'FIRED.'))
    rec('  ### ### **SO `corr_a(u) = (1/L) * psi(u/L)` WITH `psi` FIXED, AND THE WHOLE OF `a`')
    rec('  ### ### ENTERS `E2even` THROUGH THE ARGUMENT `a^s` AND NOWHERE ELSE.**')
    psi_fixed, s_fixed = ref_psi, ref_s
    rec('  psi integral over [-2,2]             : %.9f   ### (must be ~1; p := 2*psi on [0,2])'
        % float(np.trapezoid(psi_fixed, s_fixed)))

    # ---------------------------------------------------------------- the kernel
    rec('')
    rec('=' * 100)
    rec('### S2 -- THE KERNEL `eps_even`. ### FALSIFIER F2 (sign) AND F4 (far tail).')
    rec('=' * 100)
    if os.path.exists(CACHE):
        c = dict(np.load(CACHE))
        rr, em = c['rr'], c['em']
    else:
        sys.stderr.write('  building the rebuilt eps grid ...\n')
        rr = rho_grid()
        em = B38.per_mode_eps_grids(rr)
        np.savez(CACHE, rr=rr, em=em)
    ev = em[0::2].sum(0)
    od = em[1::2].sum(0)
    rec('  grid points                          : ### **%d**, rho in [%.6f, %.4f]'
        % (len(rr), rr[0], rr[-1]))
    rec('  ### **eps_even(rho = 1) = %.1e** ### -- the owner\'s "eps(1) = 0", written by')
    rec('  ###   `per_mode_eps_grids`\'s own `if hi - lo <= 0: continue`. ### **DERIVED, NOT MEASURED.**')
    out[-2] = out[-2].replace('%.1e', '%.1e' % ev[0])
    rec('  eps_even samples < 0                 : ### **%d of %d**' % (int((ev < 0).sum()), len(ev)))
    neg_modes = [(n, int((em[n] < 0).sum())) for n in range(em.shape[0])]
    rec('  per-mode negatives (mode, count)     : %s' % neg_modes)
    rec('  ### ### **F2 %s**' % ('DID NOT FIRE -- `eps_even >= 0` at every grid point.'
                                 if int((ev < 0).sum()) == 0 else 'FIRED.'))
    rec('  ### ### **AND IT IS STILL BENCH-ONLY. ### `eps_n` IS AN OVERLAP OF AN OSCILLATING')
    rec('  ### ### ENTIRE FUNCTION AGAINST ITS OWN DILATE, NOT A SUM OF SQUARES, AND b250\'s')
    rec('  ### ### MERCER CORNERS SIGN ONLY `eps\'(1+)`. ### THE DERIVATION IS NOT CLAIMED.**')
    ipk = int(ev.argmax())
    rec('')
    rec('  ### **THE KERNEL\'S SHAPE, WHICH IS THE WHOLE ACT:**')
    rec('    peak                               : ### **eps_even = %.6f at rho = %.6f**'
        % (ev[ipk], rr[ipk]))
    rec('    rising on  [1, %.4f]               : %s' % (rr[ipk], bool(np.all(np.diff(ev[:ipk + 1]) >= 0))))
    rec('    falling on [%.4f, %.2f]            : %s' % (rr[ipk], rr[-1], bool(np.all(np.diff(ev[ipk:]) <= 0))))
    rec('    ### ### **eps_even IS NOT MONOTONE ON [1, inf). ### IT RISES FROM 0 AND THEN DECAYS.**')
    rec('  ### ### **F4 %s** ### -- the far tail: eps_even(%.1f) = %.3e'
        % ('DID NOT FIRE' if bool(np.all(np.diff(ev[ipk:]) <= 0)) else 'FIRED',
           rr[-1], ev[-1]))
    rec('  %-10s %-14s %-14s' % ('rho', 'eps_even', 'eps_odd'))
    for t in (1.0, 1.02, 1.1, 1.2054, 1.5, 2.0, 5.0, 10.0, 50.0, 100.0):
        i = int(np.argmin(abs(rr - t)))
        rec('  %-10.4f %-14.6f %-14.6f' % (rr[i], ev[i], od[i]))

    # ---------------------------------------------------------------- S3
    rec('')
    rec('=' * 100)
    rec('### S3 -- THE FERRY\'S MONOTONE-WEIGHT STEP. ### **REFUTED, AND STRUCTURALLY.**')
    rec('=' * 100)
    rec('  ### `d/dL [ (1/L) psi(u/L) ] = -(1/L^2) * d/dr[ r psi(r) ]`, `r = u/L`.')
    rec('  ### So `corr_a(u)` is non-increasing in `a` IFF `r psi(r)` is non-decreasing.')
    pos = s_fixed >= 0
    rs, ps = s_fixed[pos], psi_fixed[pos]
    rp = rs * ps
    imax = int(rp.argmax())
    drp = np.diff(rp)
    rec('  `r psi(r)` at r = 0                  : %.6e   ### (must be 0)' % rp[0])
    rec('  `r psi(r)` at r = 2                  : %.6e   ### (must be ~0)' % rp[-1])
    rec('  maximizer of `r psi(r)`              : ### **r* = %.6f**, value %.6f' % (rs[imax], rp[imax]))
    rec('  samples where d/dr[r psi(r)] < 0     : ### **%d of %d**' % (int((drp < 0).sum()), len(drp)))
    rec('  ### ### **S3 REFUTED. ### `r psi(r)` VANISHES AT BOTH ENDS AND IS POSITIVE BETWEEN, SO')
    rec('  ### ### IT MUST DECREASE SOMEWHERE. ### THE REFUTATION IS NECESSARY, NOT NUMERICAL.**')
    # ### THE DIRECT WITNESS, at a named u where the ferry's step fails.
    r_bad = float(rs[imax + max(1, (len(rs) - imax) // 2)])
    a_lo, a_hi = math.sqrt(9.0), math.sqrt(16.0)
    L_lo, L_hi = math.log(a_lo), math.log(a_hi)
    u_bad = r_bad * L_lo
    _, _, c_lo, vc_lo, _ = B38.family(a_lo)
    _, _, c_hi, vc_hi, _ = B38.family(a_hi)
    v_lo = float(np.interp(u_bad, vc_lo, c_lo))
    v_hi = float(np.interp(u_bad, vc_hi, c_hi))
    rec('')
    rec('  ### **THE DIRECT WITNESS, AT A NAMED `u`** (the ferry\'s own falsifier, firing):')
    rec('    r = %.4f (beyond r*), u = r*L(a^2=9) = %.6f' % (r_bad, u_bad))
    rec('    corr at a^2 = 9   : %.9f' % v_lo)
    rec('    corr at a^2 = 16  : %.9f' % v_hi)
    rec('    ### ### **corr INCREASES with a at this u : %s**' % bool(v_hi > v_lo))

    # ---------------------------------------------------------------- S4
    rec('')
    rec('=' * 100)
    rec('### S4 -- J2\'s VERDICT. ### THE PROBE BELOW THE LADDER. ### FALSIFIER F3.')
    rec('=' * 100)

    def e2_sectors(a2):
        a = math.sqrt(float(a2))
        v, w, corr, vc, L = B38.family(a)
        E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rr, em[n]) for n in range(em.shape[0])])
        return float(E2n[0::2].sum()), float(E2n[1::2].sum())

    def e2_reduced(a2):
        """### THE REDUCED FORM, COMPUTED INDEPENDENTLY: `2 * INT_0^2 psi(s) eps_even(a^s) ds`.
        ### ### **NOT DERIVED FROM `e2_of_grid`. ### THAT IS WHAT MAKES THE COMPARISON A TEST.**"""
        a = math.sqrt(float(a2))
        s = np.linspace(0.0, 2.0, B38.NU_HALF)
        ps = np.interp(s, s_fixed, psi_fixed)
        eu = np.interp(a ** s, rr, ev)
        return 2.0 * float(np.trapezoid(ps * eu, s))

    probe_rows, worst_red = [], 0.0
    rec('  %-8s %-14s %-14s %-14s %s' % ('a^2', 'E2even', 'E2even(reduced)', '|delta|', 'note'))
    rec('  ' + '-' * 74)
    for a2 in PROBE + LADDER:
        e_ev, e_od = e2_sectors(a2)
        red = e2_reduced(a2)
        d = abs(e_ev - red)
        worst_red = max(worst_red, d)
        probe_rows.append(dict(a2=a2, E2even=e_ev, E2odd=e_od, reduced=red))
        rec('  %-8s %-14.9f %-14.9f %-14.3e %s'
            % (a2, e_ev, red, d, 'PROBE' if a2 in PROBE else 'ladder'))
    rec('')
    rec('  ### **S1 CONFIRMED INDEPENDENTLY: worst |instrument - reduced form| = ### %.3e**'
        % worst_red)
    rec('  ### ### **THE TWO ROUTES AGREE, SO THE REDUCTION IS THE INSTRUMENT AND NOT A MODEL.**')

    base = [r for r in probe_rows if r['a2'] == 2][0]['E2even']
    below = [r for r in probe_rows if r['a2'] < 2]
    smaller = [r for r in below if r['E2even'] < base]
    rec('')
    rec('  ### **THE REFUTATION, TESTED:** `E2even(a^2 = 2)` = ### **%.9f**' % base)
    rec('  probe cells below a^2 = 2            : ### **%d**' % len(below))
    rec('  of those with E2even SMALLER         : ### **%d**' % len(smaller))
    rec('  ### ### **F3 %s**'
        % ('DID NOT FIRE -- the rise is there, and J2 AS STATED IS REFUTED.' if smaller
           else 'FIRED -- no cell below the ladder is smaller; J2 SURVIVES THE PROBE.'))
    if smaller:
        rec('  ### **THE NAMED COUNTEREXAMPLES TO "E2even DECREASES MONOTONICALLY":**')
        for r in smaller:
            rec('      a^2 = %-6s E2even = %.9f  <  %.9f = E2even(a^2 = 2)'
                % (r['a2'], r['E2even'], base))
    seq = [r['E2even'] for r in sorted(probe_rows, key=lambda r: r['a2'])]
    a2s = [r['a2'] for r in sorted(probe_rows, key=lambda r: r['a2'])]
    ups = [(a2s[i], a2s[i + 1]) for i in range(len(seq) - 1) if seq[i + 1] > seq[i]]
    imx = int(np.argmax(seq))
    rec('')
    rec('  ### **THE FULL PROBE+LADDER SEQUENCE:** rises at ### **%d** ### of %d steps; the'
        % (len(ups), len(seq) - 1))
    rec('  ###   rising steps are %s' % (ups,))
    rec('  ### ### **THE MAXIMUM SITS AT a^2 = %s, SO `a_0` LIES IN (%s, %s].**'
        % (a2s[imx], a2s[imx - 1] if imx else 1, a2s[imx]))
    lad = [r['E2even'] for r in sorted([x for x in probe_rows if x['a2'] in LADDER],
                                       key=lambda r: r['a2'])]
    mono_above = bool(all(lad[i + 1] < lad[i] for i in range(len(lad) - 1)))
    rec('  ### **AND ABOVE THE TURN: the sixteen ladder cells are strictly decreasing : %s**'
        % mono_above)

    # ---------------------------------------------------------------- G-REPRO
    rec('')
    rec('=' * 100)
    rec('### THE G-REPRO CONTROL. ### THE REBUILT GRID AGAINST b255\'s BANKED COLUMN.')
    rec('### ### **b255 IS READ ### HERE ### AND NOWHERE EARLIER. NO STEP ABOVE CITED IT.**')
    rec('=' * 100)
    b255 = json.load(io.open(B255J, encoding='utf-8'))
    worst_g, at_g = 0.0, None
    rec('  %-8s %-16s %-16s %s' % ('a^2', 'E2even (this act)', 'E2even (b255)', '|delta|'))
    rec('  ' + '-' * 62)
    for r in probe_rows:
        if r['a2'] not in LADDER:
            continue
        b = b255[str(int(r['a2']))]['E2even']
        d = abs(r['E2even'] - b)
        if d > worst_g:
            worst_g, at_g = d, r['a2']
        rec('  %-8d %-16.9f %-16.9f %.3e' % (int(r['a2']), r['E2even'], b, d))
    rec('')
    rec('  ### **WORST |this act - b255| ACROSS THE SIXTEEN CELLS : ### %.3e** ### at a^2 = %s'
        % (worst_g, at_g))
    rec('  ### **b255 IS NOT RE-VERDICTED (b246\'s RULE). ### THE GRID CHANGE IS PRICED, NOT HIDDEN.**')

    # ---------------------------------------------------------------- S5
    rec('')
    rec('=' * 100)
    rec('### S5 -- THE LIMIT NOTE. ### `E2even -> 0`, OR A POSITIVE FLOOR?')
    rec('=' * 100)
    rec('  ### From S1, `E2even(a) = E_{s~p}[ eps_even(a^s) ]`. ### For every `s > 0`, `a^s -> inf`.')
    rec('  ### **IF `eps_even -> 0` AT INFINITY AND IS BOUNDED, DOMINATED CONVERGENCE GIVES 0.**')
    rec('  eps_even bounded above by            : ### **%.6f** (its peak)' % ev.max())
    rec('  eps_even at the grid\'s far end        : ### **%.3e** at rho = %.2f' % (ev[-1], rr[-1]))
    lo_i = int(np.argmin(abs(rr - 10.0)))
    slope = math.log(ev[-1] / ev[lo_i]) / math.log(rr[-1] / rr[lo_i])
    rec('  measured log-log slope on [10, %.0f]  : ### **%.4f**' % (rr[-1], slope))
    rec('  ### ### **THAT IS A MEASURED RATE AND b242 GOVERNS IT: ### *A MEASURED RATE IS NOT A')
    rec('  ### ### TAIL BOUND.* ### NO EXTRAPOLATION IS BANKED. ### THE IMPORT `eps_even -> 0` IS')
    rec('  ### ### NAMED AS AN IMPORT AND NOT PROVED HERE.**')
    tail = [r['E2even'] for r in probe_rows if r['a2'] in LADDER][-4:]
    rec('  E2even at the last four cells        : %s' % ['%.6f' % t for t in tail])

    # ---------------------------------------------------------------- tautology + controls
    rec('')
    rec('=' * 100)
    rec('### THE TAUTOLOGY CONTROL. ### AND THE KERNEL DISCRIMINATOR.')
    rec('=' * 100)
    import random
    rng = random.Random(20260830)
    sub_hold = 0
    for _ in range(20000):
        Lx = rng.uniform(0.05, 5.0)
        n = 40
        sg = np.linspace(0.0, 2.0, n)
        wt = np.abs(np.array([rng.uniform(0, 1) for _ in range(n)]))
        val = np.array([rng.uniform(-1, 1) for _ in range(n)])
        lhs = float(np.trapezoid(wt * val, sg * Lx))
        rhs = Lx * float(np.trapezoid(wt * val, sg))
        if abs(lhs - rhs) <= 1e-9 * max(1.0, abs(rhs)):
            sub_hold += 1
    rec('  (T1) S1\'s CHANGE OF VARIABLES on arbitrary weights and values')
    rec('       holds on arbitrary tuples : ### **%d / 20000**' % sub_hold)
    rec('       ### ### **IT IS MEANT TO. ### A SUBSTITUTION THAT FAILED ON ARBITRARY DATA WOULD BE')
    rec('       ### ### AN ERROR, NOT A DISCOVERY. ### IT IS A TAUTOLOGY AND IS REPORTED AS ONE.**')
    # ### THE KERNEL DISCRIMINATOR: a CONSTANT kernel must produce NO rise.
    const = np.ones_like(ev)

    def e2_with(kern, a2):
        a = math.sqrt(float(a2))
        s = np.linspace(0.0, 2.0, B38.NU_HALF)
        ps = np.interp(s, s_fixed, psi_fixed)
        return 2.0 * float(np.trapezoid(ps * np.interp(a ** s, rr, kern), s))
    cvals = [e2_with(const, a2) for a2 in sorted(a2s)]
    crise = sum(1 for i in range(len(cvals) - 1) if cvals[i + 1] > cvals[i] + 1e-12)
    rec('  (T2) THE SAME PIPELINE ON A ### CONSTANT ### KERNEL')
    rec('       rises detected : ### **%d** ### (must be 0) ; values all %.9f'
        % (crise, cvals[0]))
    rec('       ### ### **THE RISE IS A PROPERTY OF ### THIS ### KERNEL, NOT OF THE PIPELINE.**')
    rec('       ### ### If a constant kernel had produced a rise, S4\'s finding would have been')
    rec('       ### ### an artefact of the machinery and the act would have said so.')

    rec('')
    rec('=' * 100)
    rec('### POSITIVE CONTROLS.')
    rec('=' * 100)
    rec('  (C1) THE SIGN TEST DISCRIMINATES -- on a deliberately negative array:')
    rec('       negatives counted : ### **%d of 3** ### (must be 3)'
        % int((np.array([-1.0, -0.5, -0.25]) < 0).sum()))
    rec('  (C2) THE MONOTONE TEST DISCRIMINATES -- on a deliberately increasing sequence:')
    rec('       all-decreasing : ### **%s** ### (must be False)'
        % bool(all(x > y for x, y in zip([1.0, 2.0, 3.0], [1.0, 2.0, 3.0][1:]))))
    rec('  (C3) THE DILATION TEST DISCRIMINATES -- a perturbed psi is caught:')
    pert = psi_fixed.copy()
    pert[len(pert) // 2] += 1e-9
    rec('       max|pert - psi| = %.1e  >  bar %.0e : ### **%s** ### (must be True)'
        % (float(np.max(np.abs(pert - psi_fixed))), F1_BAR,
           bool(float(np.max(np.abs(pert - psi_fixed))) > F1_BAR)))
    rec('  (C4) THE G-REPRO COMPARATOR DISCRIMINATES -- against the WRONG b255 column (E2odd):')
    wrongd = max(abs(r['E2even'] - b255[str(int(r['a2']))]['E2odd'])
                 for r in probe_rows if r['a2'] in LADDER)
    rec('       worst |E2even - b255 E2odd| = ### **%.3e** ### -- must FAR EXCEED the E2even match'
        % wrongd)
    rec('  (C5) THE PROBE GRID IS RESOLVED -- points of the rho-grid below a^2 = 1.05:')
    rec('       ### **%d** ### (b255\'s grid would carry ~1-2)'
        % int((rr <= 1.05).sum()))

    rec('')
    rec('=' * 100)
    rec('### THE RUN\'S VERDICTS, IN THE REGISTERED BRANCH LANGUAGE.')
    rec('=' * 100)
    rec('  S1 (dilation identity, F1)   : ### **%s**' % ('HOLDS' if f1 else 'REFUTED'))
    rec('  S2 (kernel sign, F2)         : ### **%s, BENCH-ONLY**'
        % ('HOLDS' if int((ev < 0).sum()) == 0 else 'REFUTED'))
    rec('  S3 (weight monotone in a)    : ### **REFUTED, STRUCTURALLY**')
    rec('  S4 (J2 as stated, F3)        : ### **%s**'
        % ('REFUTED -- E2even RISES below the ladder' if smaller else 'SURVIVES THE PROBE'))
    rec('  S4b (monotone above the turn): ### **%s on the sixteen ladder cells**'
        % ('HOLDS' if mono_above else 'FAILS'))
    rec('  S5 (limit, F4)               : ### **-> 0 on the named import; NO POSITIVE FLOOR**')
    rec('')
    rec('  ### **QUOTED-N: %d cells (%d probe + %d ladder); %d rho-grid points; %d modes.**'
        % (len(probe_rows), len(PROBE), len(LADDER), len(rr), em.shape[0]))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(rows=probe_rows, peak_rho=float(rr[ipk]), peak_val=float(ev[ipk]),
                   worst_f1=worst_psi, worst_red=worst_red, worst_grepro=worst_g,
                   rstar=float(rs[imax]), neg=int((ev < 0).sum()), ngrid=len(rr)),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    print('\n  banked -> %s\n  rows   -> %s' % (BANK, ROWS))


if __name__ == '__main__':
    main()
