# -*- coding: utf-8 -*-
"""b351_extract.py -- EXTRACT-TO-DISK. ### EVERY QUOTATION THIS ACT WILL USE, PULLED AT ITS EMITTING FILE AND LINE.

### ### **NOTHING IS TYPED FROM MEMORY.** ### Each entry names the file that EMITTED the sentence, and the puller
### fails loudly if the sentence is not there. ### The comparison goes through the sortie's shared normaliser, so
### the emitter and this reader cannot normalise differently.
### ### **THIS ACT IS A READ.** ### The extract file IS the act's evidence: every claim about a coordinate's range
### or its limit must point at a line here.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import quote_norm    # noqa: E402
import run_clock     # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


# ### (label, coordinate this bears on, emitting file, the sentence, EXACTLY as that file wraps it)
READS = [
    # ---- THE ORDER'S OWN CEILING -------------------------------------------------------------------
    ('the ceiling -- one act, reads and a pricing only', 'ORDER', d('b350_ferry_2026-09-07.txt'),
     'and a pricing only; NO partition constructed, NO class proved'),
    ('the ceiling -- UNAFFORDABLE is a full verdict', 'ORDER', d('b350_ferry_2026-09-07.txt'),
     'banked; UNAFFORDABLE is a full and welcome verdict. Ask: do'),
    ('the question -- the four coordinates', 'ORDER', d('b350_ferry_2026-09-07.txt'),
     "the aim plane's own coordinates"),
    ('the question -- bound it, or prove a class silent', 'ORDER', d('b350_ferry_2026-09-07.txt'),
     'whether the record can bound it, and where a class would have'),

    # ---- THE ABSCISSA ------------------------------------------------------------------------------
    ('ABSCISSA -- the bound is not a choice', 'beta', d('b326_the_reach.txt'),
     "height `2.5` at the working precision. ### **THE ABSCISSA `1.50` IS NOT A CHOICE:** ###"),
    ('ABSCISSA -- the summed bound that closes the half-plane', 'beta', d('b326_the_reach.txt'),
     '`SUM_{k>=2} r_Q(k) k^{-3/2} = 1.38 < 2`, so `|Z_Q(s) - 2| < 2` and `Z_Q` cannot vanish at'),
    ('ABSCISSA -- and the mirror half-plane by the functional equation', 'beta', d('b326_the_reach.txt'),
     '`Re s >= 1.5` (nor, by the functional equation, at `Re s <= -0.5`); and every box within `0.02` of'),
    ('ABSCISSA -- the charted top is the first off-line zero', 'beta', t('b334_aimmap.py'),
     'BETAS = (0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 0.9532604747946607)'),

    # ---- THE HEIGHT --------------------------------------------------------------------------------
    ('HEIGHT -- the census box grid, and its top', 'gamma', d('b326_the_reach.txt'),
     "### census's own `winding`, over `sigma in [0.52, 1.50]`, `t in [0.5, 150]`, in sixty boxes of"),
    ('HEIGHT -- the count closes at the top, and by what', 'gamma', d('b326_the_reach.txt'),
     '### `146` on the line plus'),
    ('HEIGHT -- the main term that says the count grows', 'gamma', d('b326_the_reach.txt'),
     '### ### DEFECT.** ### The Riemann-von Mangoldt main term `(T/pi) log(T sqrt23 / 2 pi e)` at'),
    ('HEIGHT -- above where a census stops, nothing is claimed', 'gamma', d('b326_the_reach.txt'),
     '### ### NEVER LOOKED**, so the deficit is off-line zeros nobody has banked -- and the'),
    ('HEIGHT -- the aim map prints its own height ceiling', 'gamma', d('b334_chart_run.txt'),
     "zero-side tail bound, largest over the seeds : 3.604e-03 ; zeta's ordinates to 9877.782657"),
    ('HEIGHT -- the largest height ever charted', 'gamma', d('b334_chart_run.txt'),
     'the largest gamma charted 61.687904'),

    # ---- THE PHASE WINDOW --------------------------------------------------------------------------
    ('PHASE -- the identity that makes the window algebraic', 'phi', t('b328_family.py'),
     '###   ### (B2) for an even seed `G(-c) = G(c)`, so the sum is `4 |G|^2 cos(2 phi)`;'),
    ('PHASE -- the window as b334 carries it, and it is a window', 'phi', d('b349_extend_run.txt'),
     "the sealed phase WINDOW : 45 < |phase| < 135 degrees (b328's refinement, a window and NOT a threshold)"),
    ('PHASE -- the degenerate class, and what measuring it cannot do', 'phi', d('b349_the_room_relative.txt'),
     '### ### NEVER DEGENERATES -- IT MEANS THESE THREE DID NOT.**'),
    ('PHASE -- three seeds checked, none degenerate', 'phi', d('b349_the_room_relative.txt'),
     '### ### DEGENERATE.** ### The window is'),

    # ---- THE WIDTH ---------------------------------------------------------------------------------
    ('WIDTH -- the square not reached, by measurement', 'a', d('b334_the_aim_map.txt'),
     "### `X = 32` against `f`'s support `a^2 = 1600` and `6561`; the eps evaluator measured at five radii:"),
    ('WIDTH -- the evaluator changes sign and grows past its radius', 'a', d('b334_the_aim_map.txt'),
     '### `eps(100) = +9.968008e-02`, `eps(1600) = -7.369351e+03`, `eps(6561) = -9.726459e+03` -- a sign change'),
    ('WIDTH -- and so the remainder is outside the reach', 'a', d('b334_the_aim_map.txt'),
     '### and a growth past `rho = 100`, so the remainder at these widths is outside'),
    ('WIDTH -- for the Epstein function there is no instrument at all', 'a', d('b334_leg_covered_run.txt'),
     'the square for Z_Q : NOT AN INSTRUMENT THE RECORD HAS'),
    ('WIDTH -- the charted widths, reaching and covered', 'a', t('b334_aimmap.py'),
     'REACHING = (40.0, 81.0)'),

    # ---- THE STANDING RULES THIS ACT RUNS UNDER ----------------------------------------------------
    ("b322 -- a price is not a prediction", 'RULE', d('b322_the_membership.txt'),
     '### it does. ### **A PRICE IS NOT A PREDICTION.**'),
    ('b350 -- pricing is not measuring', 'RULE', d('b350_the_two_held_axes.txt'),
     '### **PRICING IS NOT MEASURING, AND NOTHING PRICED HERE'),
    ('b339 -- UNAFFORDABLE is a verdict the record already carries', 'RULE', d('b339_checks_run.txt'),
     'G-VERDICT (F4: UNAFFORDABLE everywhere the act speaks'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b351 -- EXTRACT-TO-DISK. ### EVERY QUOTATION AT ITS EMITTING FILE AND LINE.')
    rec('=' * 100)
    bad = 0
    for label, coord, path, anchor in READS:
        try:
            hit = needle_pull.pull(path, anchor)
        except LookupError:
            bad += 1
            rec('  ### ### **UNPULLABLE** : %s' % label)
            rec('      file   : %s' % os.path.relpath(path, ROOT))
            rec('      anchor : %r' % anchor)
            continue
        line = hit[0] if isinstance(hit, (list, tuple)) else hit
        n = line if isinstance(line, int) else None
        txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
        if n is None:
            for i, ln in enumerate(txt, 1):
                if quote_norm.contains(ln, anchor):
                    n = i
                    break
        rec('')
        rec('  [%-5s] %s' % (coord, label))
        rec('      %s : line %s' % (os.path.relpath(path, ROOT).replace(os.sep, '/'), n))
        rec('      | %s' % txt[n - 1].rstrip())
        if n < len(txt) and txt[n].strip():
            rec('      | %s' % txt[n].rstrip())
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### UNPULLABLE : %d' % (len(READS), bad))
    rec('  ### ### **AN EXTRACT IS A QUOTATION AT A LINE. ### IT IS NOT A READING OF THE ARGUMENT AROUND IT,**')
    rec('  ### and every use this act makes of these lines is the act\'s own and defensible at the act.')
    rec('=' * 100)
    p = run_clock.write(D, 'b351_extract_notes', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
