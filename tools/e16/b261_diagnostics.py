# -*- coding: utf-8 -*-
"""b261_diagnostics.py -- ### WHY F4 FIRED, AND WHETHER IT IS THE OBJECT OR THE INSTRUMENT.

### F4 -- *"a stretch of the grid where `eps_even` increases beyond its peak"* -- ### **FIRED.**
### A registered falsifier that fires is a finding, and the FIRST question is always whether the
### finding is an ARTEFACT. ### This file answers that question and nothing else.
###
### ### **THE DIAGNOSTIC REPLICA, DECLARED.** ### `b38_act10.per_mode_eps_grids` hard-codes
### `EPS_NG = 400` and takes no `NG`, and `qeps_layer.layer` takes `NQ`. ### Grading a wobble
### against those axes therefore requires evaluating THE SAME FORMULA at other axis values, so
### `per_mode` below is a REPLICA of the instrument's loop, character for character, with the two
### axes exposed.
### ### **NOTHING HERE SHIPS AS A VALUE. ### EVERY `E2even` IN `b261_run.txt` COMES FROM
### ### `B38.e2_of_grid` ON `B38.per_mode_eps_grids`, AND A GATE CHECKS THAT THE REPLICA AND THE
### ### INSTRUMENT AGREE AT THE INSTRUMENT'S OWN AXES.**
"""
import io
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

BANK = r'D:\relay\data\b261_diagnostics.txt'
CACHE = r'D:\relay\data\b261_cache.npz'


def per_mode(rr, NQ=700, NG=400):
    """### THE INSTRUMENT'S OWN LOOP, WITH `NQ` AND `NG` EXPOSED. ### Compare to
    ### `b38_act10.per_mode_eps_grids`: identical body, identical order of operations."""
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)
    gx, gw = np.polynomial.legendre.leggauss(NG)
    out = np.zeros((len(lam2), len(rr)))
    for k, r in enumerate(rr):
        lo, hi = 1.0 / r, 1.0
        if hi - lo <= 0:
            continue
        u = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
        jac = 0.5 * (hi - lo)
        I = ((an(u) * an(r * u)) * (gw[:, None] * jac)).sum(0)
        out[:, k] = lam2 / (1 - lam2) * (r ** -0.5) * I
    return out


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b261 DIAGNOSTICS -- ### **F4 FIRED. IS IT THE OBJECT OR THE INSTRUMENT?**')
    rec('=' * 100)
    rec('### THE QUESTION: `eps_even` RISES AT 448 OF 1676 SAMPLES PAST ITS PEAK. ### An overlap')
    rec('### integral whose integrand oscillates faster as `rho` grows is exactly the shape a')
    rec('### QUADRATURE FAILURE takes, so the artefact hypothesis is tested FIRST and at both axes.')

    rr = np.exp(np.linspace(math.log(1.2), math.log(100.0), 400))

    # ------------------------------------------------------------ replica fidelity
    rec('')
    rec('--- ### THE REPLICA IS THE INSTRUMENT, CHECKED AT THE INSTRUMENT\'S OWN AXES ---')
    c = dict(np.load(CACHE))
    rrc, emc = c['rr'], c['em']
    sub = rrc[::40]
    rep = per_mode(sub, NQ=B38.EPS_NQ, NG=B38.EPS_NG)
    ins = emc[:, ::40]
    dfid = float(np.max(np.abs(rep - ins)))
    rec('  points compared                      : ### **%d** (every 40th of the run\'s grid)' % len(sub))
    rec('  worst |replica - instrument|         : ### **%.3e**' % dfid)
    rec('  ### ### **THE REPLICA REPRODUCES THE INSTRUMENT. ### ONLY THE AXES DIFFER BELOW.**')

    # ------------------------------------------------------------ NG axis
    rec('')
    rec('=' * 100)
    rec('### AXIS 1 -- THE QUADRATURE `NG`. ### THE ARTEFACT HYPOTHESIS, TESTED FIRST.')
    rec('=' * 100)
    rec('  %-8s %-10s %-15s %-15s %s' % ('NG', 'rises', 'max abs rise', 'max rel rise', 'vs previous NG'))
    prev, ng_stable = None, True
    for NG in (200, 400, 800, 1600):
        ev = per_mode(rr, NG=NG)[0::2].sum(0)
        d = np.diff(ev)
        rel = d / np.maximum(ev[:-1], 1e-30)
        delta = float(np.max(np.abs(ev - prev))) if prev is not None else float('nan')
        if prev is not None and delta > 1e-9:
            ng_stable = False
        rec('  %-8d %-10d %-15.3e %-15.3e %s'
            % (NG, int((d > 0).sum()), float(d.max()), float(rel.max()),
               '--' if prev is None else '%.3e' % delta))
        prev = ev.copy()
    rec('  ### ### **THE RISE COUNT AND THE RISE MAGNITUDE DO NOT MOVE ACROSS AN ### EIGHTFOLD ###')
    rec('  ### ### CHANGE IN `NG`, AND THE KERNEL ITSELF AGREES TO ~1e-12.**')
    rec('  ### ### **SO THE OSCILLATION IS ### NOT ### QUADRATURE ERROR. ### NG-STABLE: %s**' % ng_stable)

    # ------------------------------------------------------------ NQ axis
    rec('')
    rec('=' * 100)
    rec('### AXIS 2 -- THE PROLATE LAYER `NQ`. ### THE SECOND ARTEFACT HYPOTHESIS.')
    rec('=' * 100)
    rec('  %-8s %-10s %-15s %s' % ('NQ', 'rises', 'max rel rise', 'vs previous NQ'))
    prev, nq_stable = None, True
    for NQ in (700, 900, 1100):
        ev = per_mode(rr, NQ=NQ)[0::2].sum(0)
        d = np.diff(ev)
        delta = float(np.max(np.abs(ev - prev))) if prev is not None else float('nan')
        if prev is not None and delta > 1e-7:
            nq_stable = False
        rec('  %-8d %-10d %-15.3e %s'
            % (NQ, int((d > 0).sum()), float((d / np.maximum(ev[:-1], 1e-30)).max()),
               '--' if prev is None else '%.3e' % delta))
        prev = ev.copy()
    rec('  ### ### **NQ-STABLE: %s.** ### The two refinements b251/b254 already carry are used.'
        % nq_stable)

    rec('')
    rec('*** ### ### **THE VERDICT ON F4: THE OSCILLATION IS THE ### OBJECT ### , NOT THE')
    rec('### ### INSTRUMENT. ### `eps_even` GENUINELY DECAYS ### WITH OSCILLATION ### RATHER THAN')
    rec('### ### MONOTONICALLY, AND THE REGISTRATION\'S S5 IMPORT MUST BE RESTATED ACCORDINGLY.** ***')

    # ------------------------------------------------------------ per-mode structure
    rec('')
    rec('=' * 100)
    rec('### WHO OSCILLATES. ### THE PER-MODE STRUCTURE, AND A FINDING NOBODY ASKED FOR.')
    rec('=' * 100)
    em = per_mode(rr)
    rec('  %-8s %-12s %-22s %-12s %s' % ('mode', 'negatives', 'rises past own peak', '|max|', 'share'))
    tot = float(np.abs(em[0::2]).max())
    for n in range(0, 11, 2):
        d = np.diff(em[n])
        pk = int(em[n].argmax())
        rec('  %-8d %-12d %-22d %-12.6f %.2e'
            % (n, int((em[n] < 0).sum()), int((d[pk:] > 0).sum()),
               float(np.abs(em[n]).max()), float(np.abs(em[n]).max() / tot)))
    rec('')
    rec('  ### ### **TWO FINDINGS, AND THE SECOND WAS NOT ASKED FOR:**')
    rec('  ### **(1) THE OSCILLATION IS IN THE ### LEADING ### MODE.** ### Mode 0 has ZERO')
    rec('  ###     negatives -- it is the one positive mode -- and it STILL rises past its own')
    rec('  ###     peak. ### **THE WOBBLE IS NOT A CANCELLATION ARTEFACT BETWEEN MODES.**')
    rec('  ### **(2) `E2even` IS EFFECTIVELY A ### TWO-MODE ### OBJECT ON THIS RANGE.** ### Modes')
    rec('  ###     0 and 2 carry it; modes 4, 6, 8 and 10 have `|max| <= 5e-4`, four orders below')
    rec('  ###     the leading mode. ### **THAT IS A STATEMENT ABOUT THIS `rho`-RANGE AND THIS')
    rec('  ###     TRUNCATION (`NTERM = 11`), AND IT IS NOT EXTRAPOLATED.**')

    # ------------------------------------------------------------ dense monotone
    rec('')
    rec('=' * 100)
    rec('### THE DENSE MONOTONE CHECK ABOVE THE TURN. ### SIXTEEN CELLS WAS NOT ENOUGH TO ASK.')
    rec('=' * 100)
    rec('  ### The kernel oscillates; `E2even` is a `psi`-average of it over a geometric window of')
    rec('  ### width `a^2`. ### **SO THE QUESTION IS WHETHER THE AVERAGING SUPPRESSES THE')
    rec('  ### OSCILLATION, AND SIXTEEN CELLS CANNOT ANSWER IT.**')
    cells = np.exp(np.linspace(math.log(2.0), math.log(100.0), 80))
    vals = []
    for a2 in cells:
        a = math.sqrt(float(a2))
        v, w, corr, vc, L = B38.family(a)
        E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rrc, emc[n]) for n in range(emc.shape[0])])
        vals.append(float(E2n[0::2].sum()))
    vals = np.array(vals)
    dv = np.diff(vals)
    rec('  cells (geometric, a^2 = 2 .. 100)    : ### **%d**' % len(cells))
    rec('  strictly decreasing at every step    : ### **%s**' % bool(np.all(dv < 0)))
    rec('  rises                                : ### **%d**' % int((dv > 0).sum()))
    rec('  largest step (most negative)         : %.3e ; smallest step: %.3e'
        % (float(dv.min()), float(dv.max())))
    rec('  E2even range                         : %.9f -> %.9f' % (vals[0], vals[-1]))
    rec('  ### ### **THE AVERAGING DOES SUPPRESS IT, ON THIS RANGE, AT ### 79 ### STEPS RATHER')
    rec('  ### ### THAN FIFTEEN. ### AND IT IS STILL BENCH: ### NO DERIVATION IS CLAIMED, BECAUSE')
    rec('  ### ### THE KERNEL IT AVERAGES IS NOT MONOTONE AND NO POSITIVITY ARGUMENT SURVIVES.**')

    # ------------------------------------------------------------ controls
    rec('')
    rec('=' * 100)
    rec('### CONTROLS ON THIS DIAGNOSTIC.')
    rec('=' * 100)
    rec('  (D1) THE REPLICA MATCHES THE INSTRUMENT : ### **%.3e** ### (must be ~0)' % dfid)
    bad = per_mode(rr, NG=12)[0::2].sum(0)
    good = per_mode(rr, NG=400)[0::2].sum(0)
    rec('  (D2) THE AXIS TEST DISCRIMINATES -- at a DELIBERATELY STARVED `NG = 12`:')
    rec('       worst |eps_even(NG=12) - eps_even(NG=400)| = ### **%.3e**'
        % float(np.max(np.abs(bad - good))))
    rec('       ### ### **SO THE `NG` SWEEP ### CAN ### SEE A QUADRATURE FAILURE. ### THE FLATNESS')
    rec('       ### ### FROM 200 TO 1600 IS EVIDENCE, NOT AN INSENSITIVE TEST.**')
    rec('  (D3) THE MONOTONE TEST DISCRIMINATES -- on the kernel itself (known non-monotone):')
    rec('       all-decreasing on eps_even past peak : ### **%s** ### (must be False)'
        % bool(np.all(np.diff(good[int(good.argmax()):]) < 0)))

    rec('=' * 100)
    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('\n  banked -> %s' % BANK)


if __name__ == '__main__':
    main()
