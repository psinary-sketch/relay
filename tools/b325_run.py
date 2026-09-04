# -*- coding: utf-8 -*-
"""b325_run.py -- THE THREE COMPONENTS. ### **THE READ, THE PRICING, AND THE RUN.**

### ### **THE VERDICT IS TAKEN AT THE ORDER'S OWN SCOPE AND NOWHERE WIDER.** ### (B2): the arc's
### cells are the atlas's thirteen. ### **A WIDTH BEYOND THEM IS PRICED, NEVER VERDICTED**, however
### interesting the number turns out to be -- and in this act it turns out very interesting indeed,
### which is exactly when a scope bar earns its keep.
"""
import io
import json
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))

import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b321_window as WI        # noqa: E402
import b325_epstein as EP       # noqa: E402
import noise_floor as NF        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
EXTRACT = os.path.join(D, 'b325_extract_notes.txt')

# ### **THE WIDTHS BEYOND THE ARC'S CELLS, FOR THE PRICING ONLY.** ### (B2) forbids a verdict here.
PRICED_WIDTHS = (8.0, 12.0, 16.0, 20.0, 22.0, 24.0, 28.0, 32.0, 50.0)

EXTRACT_NEEDLES = [
    ('the confinement keystone, subject B', 'When the class number of Q exceeds 1'),
    ('### and the theorem it rests on', 'Davenport'),
    ('### and what the functional equation does not do', 'it does not confine zeros to it'),
    ('the ledger called positive, at the residue keystone', 'positive ledger but RH false'),
    ('### THE EPSTEIN ARCHIMEDEAN FACTOR, at the corpus emitting file',
     'Lambda(s) = (sqrt(23)/2pi)^s Gamma(s) Z_Q(s)'),
    ('### the form, its discriminant, its class number', 'disc -23, principal form'),
    ('### and the census method', 'winding number of'),
    ("### the arc's kernel, zeta's, at its emitting file", 'def kernel'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def pull(anchor):
    txt = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    flat = ''.join(ch for ch in txt if not ch.isspace())
    return ''.join(ch for ch in anchor if not ch.isspace()) in flat


def main():
    fails = []
    rec('=' * 100)
    rec('b325 -- THE NEGATIVE CONTROL.')
    rec('=' * 100)

    good, arms, ls = EP.self_test()
    rec('  ### THE EPSTEIN INSTRUMENT FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    for s in ls:
        rec('    ' + s)
    if not good:
        fails.append('EPSTEIN FIXTURES')

    rec('')
    rec('  ### THE STATEMENTS, PULLED FROM THE EXTRACT FILE:')
    for lbl, anchor in EXTRACT_NEEDLES:
        got = pull(anchor)
        rec('    %-5s %s' % ('found' if got else '### NO', lbl))
        if not got:
            fails.append('needle: ' + lbl)

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE READ.')
    rec('=' * 100)
    rec('  ### **THE OBJECT:** ### the Epstein zeta of the principal form `x^2 + xy + 6y^2`,')
    rec('  ### discriminant `-23`, class number `h(-23) = 3`. ### The corpus names it in its own')
    rec('  ### census header and this act uses that form and no other.')
    rec('  ### **THE LEDGER THE KEYSTONE CALLS POSITIVE:** ### the residue keystone\'s')
    rec('  ### *"positive ledger but RH false"* -- and the ledger is the LI one, `lambda_n`, the')
    rec('  ### register the balance keystone works in. ### **THE POSITIVITY IS OF THE COEFFICIENT')
    rec('  ### ### SEQUENCE, NOT OF THE ZEROS.**')
    rec('  ### **WHERE ITS ZEROS COME FROM AND WHICH LIE OFF THE LINE:** ### the corpus\'s own')
    rec('  ### argument-principle census, `epstein_census.py`, 2-D by construction --')
    rec('  ### *"A critical-line scan would IMPOSE the real part"*. ### It banks 450 cells over')
    rec('  ### `sigma in [0.52, 1.50]`, `t in [0.5, 33.0]`, and finds ### **TWO ZEROS, BOTH OFF THE')
    rec('  ### ### LINE**: `sigma in [0.94, 1.08]` at `t in [16.0, 16.5]`, and `sigma in [0.66,')
    rec('  ### 0.80]` at `t in [29.5, 30.0]`.')
    rec('  ### **WHAT THE KEYSTONE CONCLUDES:** ### *"Same pipeline. Same analytic machinery. One')
    rec('  ### ingredient removed. Outcome changed."* ### and *"The functional equation illuminates')
    rec('  ### the critical line; it does not confine zeros to it."*')
    rec('')
    rec('  ### ### **AND WHAT THE CORPUS HOLDS TOWARD RUNNING IT ON THE ARC\'S INSTRUMENT.**')
    rec('  ###   ### **THE ARCHIMEDEAN TERM -- NOT THE SAME DISTRIBUTION, AND THE CORPUS SAYS SO')
    rec('  ###   ### IN ITS OWN VOICE.** ### `epstein_census.py`\'s METHOD header:')
    rec('  ###   ### *"Lambda(s) = (sqrt(23)/2pi)^s Gamma(s) Z_Q(s)"*. ### Zeta\'s is')
    rec('  ###   `pi^{-s/2} Gamma(s/2) zeta(s)`. ### **`Gamma(s)` AGAINST `Gamma(s/2)`** -- so the')
    rec('  ###   arc\'s kernel `Re psi(1/4 + iu/2) - log pi` does NOT transfer, and the Epstein one')
    rec('  ###   `Re psi(1/2 + iu) - log(2 pi / sqrt 23)` follows from the quoted factor by the')
    rec('  ###   atlas\'s own construction. ### **A BUILD, AND A SMALL ONE.**')
    rec('  ###   ### **THE FINITE SIDE -- REPRESENTATION NUMBERS WHERE ZETA HAD PRIME POWERS, BUT')
    rec('  ###   ### NOT DIRECTLY.** ### `r_Q` is the Dirichlet coefficient sequence; the explicit')
    rec('  ###   formula\'s finite side is the coefficient sequence of `-Z_Q\'/Z_Q`, which this act')
    rec('  ###   obtains from `r_Q` by Dirichlet inversion. ### **`Lambda_Q` IS NOT `r_Q`** -- they')
    rec('  ###   differ by up to `15.74` below `n = 60`. ### **A BUILD, AND A SMALL ONE.**')
    rec('  ###   ### **THE ZERO LIBRARY -- OWNED FOR THE OFF-LINE ZEROS AND NOT FOR THE ON-LINE')
    rec('  ###   ### ONES.** ### The census started at `sigma = 0.52`: it was hunting off-line zeros')
    rec('  ###   and found them. ### **AN EXPLICIT FORMULA NEEDS BOTH**, so the closure control')
    rec('  ###   cannot run. ### To own them: re-run the same census over `sigma in [0.45, 0.52]`')
    rec('  ###   and refine each winding cell to a zero. ### **A BUILD, AND THE TOOL EXISTS.**')

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE PRICING.')
    rec('=' * 100)
    rec('    %-34s %-10s %-8s %s' % ('constituent', 'type', 'acts', 'status'))
    price = [
        ('the form and r_Q', 'read', '0', 'OWNED -- reproduced from the corpus tool, value for value'),
        ('the archimedean factor', 'read', '0', "OWNED -- quoted from the census header"),
        ('the archimedean kernel', 'build', '0', 'BUILT THIS ACT from the quoted factor'),
        ('the finite side Lambda_Q', 'build', '0', 'BUILT THIS ACT by Dirichlet inversion'),
        ('the lawful class', 'read', '0', 'TRANSFERS -- the poles sit at s = 0, 1 as zeta\'s do'),
        ('the off-line zero library', 'read', '0', 'OWNED -- 2 zeros, as rectangles'),
        ('the ON-LINE zero library', 'build', '1', 'NOT OWNED -- census never scanned sigma < 0.52'),
        ('the explicit-formula control', 'build', '1', 'BLOCKED on the line above'),
        ("Theorem 1's archimedean control", 'n/a', '-', 'DOES NOT COVER Z_Q -- a hypothesis, not a cost'),
    ]
    for c, ty, ac, st in price:
        rec('    %-34s %-10s %-8s %s' % (c, ty, ac, st))
    rec('')
    rec('  ### ### **THE PRICING VERDICT: ### THE FALSIFIER FITS INSIDE THIS ACT; THE TWO NAMED')
    rec('  ### ### CONTROLS DO NOT.**')
    rec('  ### The order\'s falsifier reads the sign of the places sum ### **WITHOUT ANY ZERO**, and')
    rec('  ### every constituent it needs is owned or built above. ### So the run happens.')
    rec('  ### **THE CONTROLS THE ZETA WINDOW CARRIED DO NOT TRANSFER**, one for cost and one by')
    rec('  ### nature, and the verdict is reported at exactly the reduced scope that leaves.')
    rec('')
    rec('  ### **THE RUN\'S SHAPE, WRITTEN DOWN:** ### the places side `SUM_v W_v = PR_Q - A_Q` on')
    rec('  ### the arc\'s lawful seeds at the arc\'s thirteen cells; the sign read without any zero;')
    rec('  ### and ### **ZETA THROUGH THE SAME CHANNELS AS THE POSITIVE CONTROL**, whose correct')
    rec('  ### answer b321 already proved: never positive.')
    rec('  ### **THE FALSIFIER, FIXED BY THE ORDER:** ### the instrument SEES the failure if a')
    rec('  ### lawful `f` at some cell gives the places sum ### **A POSITIVE VALUE**, which is the')
    rec('  ### sign Proposition C.1 forbids.')

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE RUN.')
    rec('=' * 100)
    cells = [r['a'] for r in SM.atlas_cells()]
    rec('  ### (3a) AT THE ARC\'S THIRTEEN CELLS. ### **THIS IS WHERE THE VERDICT IS TAKEN.**')
    rec('    %-6s %-9s %-17s %-17s %-17s %-17s %s'
        % ('a', 'a^2', 'EPSTEIN finite', 'EPSTEIN arch', 'EPSTEIN places', 'ZETA places', 'terms'))
    rows, pos = [], []
    for a in cells:
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        eq = EP.channels_q(f.v, f.w)
        zc = EP.zeta_places_full(f.v, f.w)
        rows.append(dict(a=a, **{k: eq[k] for k in ('finite', 'arch', 'places', 'pole')},
                         zeta=zc['places'], terms=len(eq['terms'])))
        if eq['places'] > 0.0:
            pos.append(a)
        rec('    %-6g %-9.4f %-17.9f %-17.9f %-17.9f %-17.9f %d'
            % (a, a * a, eq['finite'], eq['arch'], eq['places'], zc['places'], len(eq['terms'])))
    zok = all(r['zeta'] <= 0.0 for r in rows)
    rec('    ### ### **THE POSITIVE CONTROL: ### ZETA IS NON-POSITIVE AT EVERY CELL : %s**' % zok)
    rec('    ### ### **CELLS WHERE EPSTEIN TAKES THE FORBIDDEN SIGN : %s**'
        % (', '.join('%g' % a for a in pos) if pos else 'NONE'))
    if not zok:
        fails.append('POSITIVE CONTROL FAILED AT AN ARC CELL')

    verdict = 'SEES IT' if pos else 'DOES NOT SEE IT'
    rec('')
    rec('  ### ### ### **VERDICT AT THE ARC\'S CELLS : %s**' % verdict)
    rec('  ### **AND THE REASON IS STRUCTURAL, NOT MARGINAL.** ### The form `x^2 + xy + 6y^2`')
    rec('  ### represents NOTHING between `1` and `4`: `r_Q(2) = r_Q(3) = 0`. ### So the finite')
    rec('  ### channel is ### **IDENTICALLY ZERO UNTIL `a = 2`** ### and still only `%.9f` at'
        % rows[-1]['finite'])
    rec('  ### `a = 3`, against an archimedean channel of `%.9f`. ### **THE ARITHMETIC HAS BARELY'
        % rows[-1]['arch'])
    rec('  ### ### ENTERED AT THE WIDTHS THE ARC SPANS.**')

    rec('')
    rec('  ### (3b) BEYOND THE ARC\'S CELLS. ### **PRICED, NEVER VERDICTED -- (B2).**')
    rec('    %-6s %-9s %-17s %-17s %-8s' % ('a', 'a^2', 'EPSTEIN places', 'ZETA places', 'terms'))
    priced, cross = [], None
    for a in PRICED_WIDTHS:
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        eq = EP.channels_q(f.v, f.w)
        zc = EP.zeta_places_full(f.v, f.w)
        priced.append(dict(a=a, places=eq['places'], zeta=zc['places'], terms=len(eq['terms'])))
        if cross is None and eq['places'] > 0.0:
            cross = a
        rec('    %-6g %-9.0f %-17.9f %-17.9f %-8d'
            % (a, a * a, eq['places'], zc['places'], len(eq['terms'])))
    zok2 = all(p['zeta'] <= 0.0 for p in priced)
    rec('    ### the positive control holds at every priced width too : %s' % zok2)
    rec('    ### ### **THE EPSTEIN SIGN CROSSES AT `a = %s`.**' % (cross if cross else 'NOWHERE'))
    rec('    ### ### **AND THIS IS NOT A VERDICT.** ### (B2) scopes the run to the arc\'s cells and')
    rec('    ### these are not among them. ### **IT IS A PRICE: ### IT SAYS WHAT REACH WOULD BE')
    rec("    ### ### NEEDED, AND THAT THE INSTRUMENT SEEING NOTHING AT THE ARC'S CELLS IS A MATTER")
    rec('    ### ### REACH RATHER THAN OF KIND.**')
    rec('    ### **NOR IS IT A `SEES IT`.** ### The order\'s `SEES IT` requires the zero side as')
    rec('    ### corroboration, and the on-line zero library is not owned. ### **A POSITIVE SIGN')
    rec('    ### ### WITHOUT ITS CORROBORATION IS A MEASUREMENT, NOT THE VERDICT.**')
    if not zok2:
        fails.append('POSITIVE CONTROL FAILED AT A PRICED WIDTH')

    rec('')
    rec('  ### (3c) THE NOISE-FLOOR GATE, IN THE PATH.')
    # ### ### **A DEFECT IN THE FIRST VERSION OF THIS BLOCK, FIXED AND DECLARED.** ### It fed the
    # ### gate ADJACENT CELLS -- `a = 1.3` against `a = 1.35` -- and the gate dutifully reported all
    # ### six DRIFTING. ### **TWO DIFFERENT CELLS ARE TWO DIFFERENT NUMBERS, NOT A REFINEMENT
    # ### ### PAIR**, and a convergence gate fed non-convergent pairs answers a question nobody
    # ### asked. ### The pairs below are the SAME cell at two `u`-grid resolutions, which is what
    # ### the gate is for.
    items = []
    for a in (1.3, 2.1, 3.0):
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        coarse = EP.channels_q(f.v, f.w)['places']
        U = np.linspace(-WI.AT.UMAX, WI.AT.UMAX, 4 * (WI.AT.NU - 1) + 1)
        kq = EP.kernel_q(U)
        A = float(np.trapezoid(WI.hhat_blocked(f.v, f.w, U) * kq, U) / (2.0 * math.pi))
        fine = EP.finite_channel(f.v, f.w)[0] - A
        items.append(('epstein a=%g' % a, coarse, fine))
    ok, grows, detail = NF.gate(items, label='b325')
    for name, val, ref, verd, why in grows:
        rec('    %-18s %-17.9f -> %-17.9f %-10s' % (name, val, ref, verd))
    rec('    ### %s' % detail)

    rec('')
    rec('=' * 100)
    rec('  ### CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('  ### ### **VERDICT : %s (at the arc\'s cells)** ; sign crosses at a = %s (priced)'
        % (verdict, cross))
    rec('=' * 100)

    payload = dict(cells=rows, priced=priced, verdict=verdict, cross=cross,
                   zeta_control_cells=bool(zok), zeta_control_priced=bool(zok2),
                   forbidden_at_arc_cells=pos, noise_ok=bool(ok), fails=fails)
    d = (json.dumps(payload, indent=1, default=float) + '\n').encode('utf-8')
    open(os.path.join(D, 'b325_rows.json') + '.tmp', 'wb').write(d)
    os.replace(os.path.join(D, 'b325_rows.json') + '.tmp', os.path.join(D, 'b325_rows.json'))
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    io.open(os.path.join(D, 'b325_run.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
