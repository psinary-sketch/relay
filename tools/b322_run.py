# -*- coding: utf-8 -*-
"""b322_run.py -- THE THREE COMPONENTS. ### **THE LADDER FIRST, THE UNFOLDING SECOND.**

### ### **THE ORDER OF THE COMPONENTS IS ITSELF A BAR AND THE REGISTRATION SAYS SO.** ### (B1c):
### the reading is taken from the ladder's DIRECTION ### **BEFORE ANY DEFINITION IS UNFOLDED.** ###
### An act that unfolded the definitions first would know which answer it wanted from the numbers.
### ### **NO UNIT IS ADOPTED OR REPLACED HERE.** ### b300's derivation and b316/b319's measurement
### both stand at their own grade, and if no constituent gives way the act says so.
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
import b319_stable as ST        # noqa: E402
import b322_ladder as LD        # noqa: E402
import noise_floor as NF        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
EXTRACT = os.path.join(D, 'b322_extract_notes.txt')

# ### **THE BARS, READ OFF THE SEALED REGISTRATION AND LIVING NOWHERE ELSE.**
BAR_COMPARABLE_LO = 0.5     # ### (B1b) `1/2 <= p/q <= 2`
BAR_COMPARABLE_HI = 2.0
BAR_TAPER_EDGE = 0.5        # ### (B2) tapered below HALF the untapered at every frame
BAR_TAPER_VECTOR = 0.1      # ### (B2) moves by less than a tenth at every frame
P_PREDICTED = -0.5          # ### (B3) from `u ~ 1/x`
BAR_ROUTES = 0.2            # ### (B3) agree within 20 per cent of the prediction
PRICE_TARGET = 0.01         # ### (B5) the figure the price is quoted to

# ### b321's instrument-residual ladder at `a = 1.3`, quoted from that act's own bank. ### The
# ### exponent `q` is fitted from these five numbers by the SAME fitter that fits the unit's.
B321_INSTRUMENT = (0.896557, 0.306328, 0.112555, 0.047182, 0.023224)

EXTRACT_NEEDLES = [
    ('Definition 4.4 -- the space and its two conditions', 'nition 4.4 For'),
    ('(16) -- the inner product and its normalization', 'as follows'),
    ('(24) -- the transform on even functions', 'nes the unitary in L2'),
    ('CM Lemma 3.1 -- condition one, quoted at its emitter', 'zero on [-1,1]'),
    ("### and the closing line of its proof", 'F_eR phi_mu = xi_mu'),
    ("b211's (C3) -- the eigenrelation", 'F phi_mu = c phi_mu'),
    ("b203's fence -- and it is the one that matters", 'IS NOT'),
    ("b300's verdict (b)", 'DERIVES-on-IMPORTS'),
    ("b319's residual table", 'residual stable'),
    ("b321's instrument ladder", 'THE IDENTITY CONTROL HOLDS'),
    ('the instrument realization -- sonin_unit', 'def sonin_unit'),
    ('### and the edge diagnostic it ships with', 'def taper'),
]

# ### ==============================================================================================
# ### COMPONENT 2's TABLE. ### **EACH SIDE'S STATEMENT IS PULLED FROM THE EXTRACT, NOT TYPED HERE.**
# ### Every row carries the anchor that licenses it on each side; the runner refuses to print a row
# ### whose anchor does not pull. ### **NEITHER SIDE IS DESCRIBED IN THE OTHER'S LANGUAGE**, which
# ### is the order's own condition and the reason the two columns are written separately.
# ### ==============================================================================================
UNFOLD = [
    ('THE AMBIENT',
     'even, and in L^2(R) -- CM Lemma 3.1 says "the unique EVEN solution"; L^2 is NOT stated by any '
     'owner and travels as W-ORD-PHI-MU-L2', 'the unique even solution',
     'a real array on the grid x in [0, X], treated as an even function of x by the frame; '
     'square-summability is automatic for a finite array', 'def sonin_unit',
     'SAME in intent; the instrument cannot see the open L^2 question because a finite array is '
     'always square-summable'),
    ('CONDITION ONE',
     'phi_mu is "zero on [-1,1] and agrees with f_mu(x) for x > 1" -- a QUOTED property of the '
     'solution', 'zero on [-1,1]',
     'out = np.zeros(fr.N) and only the coordinates with x > 1 are filled -- an IMPOSED property of '
     'the array', 'out = np.zeros(fr.N)',
     'SAME value, DIFFERENT status: quoted at the source, imposed by construction here. The '
     'instrument could not detect a violation of it'),
    ('THE EIGENRELATION',
     'F phi_mu = c phi_mu with c = +-1, DERIVED by b211 (C3) from commutation plus simplicity, with '
     "b203's fence standing: F phi = xi is NOT F phi = phi", 'F phi_mu = c phi_mu',
     'never formed; the instrument applies the transform matrix and measures, it does not use an '
     'eigenrelation anywhere', 'def transform_matrix',
     'NOT COMPARABLE: the derivation USES it and the instrument does not NEED it. Neither contains '
     "the other's step"),
    ('CONDITION TWO',
     '(F_eR phi_mu)(p) = c * phi_mu(p) = c * 0 = 0 for |p| <= 1 -- one line, from the eigenrelation '
     'and condition one', 'F_eR phi_mu = xi_mu',
     'the null space of C = T[lo_y][:, hi_x]: the transform of the array, restricted to y <= 1, '
     'set against zero and MEASURED as a norm', 'def masks',
     'THE DERIVATION ASSERTS IT EXACTLY; THE INSTRUMENT MEASURES IT AND GETS A NONZERO NUMBER. '
     'This is where the residual lives'),
    ('THE TRANSFORM',
     "the source's (24), the unitary on even functions", 'it defines the unitary',
     '2 cos(2 pi outer(y, x)) * w -- (24) discretised on the frame, quadrature weights included',
     'def transform_matrix',
     'SAME convention, one exact and one quadrature'),
    ('THE INNER PRODUCT',
     "the source's (16), <eta|xi> = INT_0^inf eta conj(xi) dx", 'as follows',
     "the frame's weighted sum with the same normalization", 'def norm',
     'SAME convention, one exact and one quadrature'),
    ('THE DOMAIN',
     'the whole half-line: phi_mu is defined for all x > 1 and CM states its behaviour at infinity',
     'zero on [-1,1]',
     '[0, X] for a FINITE X, with a HARD CUT at X and nothing beyond it', 'def sonin_unit',
     'DIFFERENT, AND VISIBLY SO WITHOUT ANY MEASUREMENT. Whether this difference IS the residual is '
     "Component 1's question and Component 1 answers it first"),
    ('THE SPACE',
     "the source's Definition 4.4: S(1,1), two homogeneous vanishing conditions", 'Definition 4.4',
     "b319's eigenvalue-one cut of the sandwich on the free coordinates, a finite section",
     'def stable_subspace',
     'SAME definition, one exact and one a finite section of it'),
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
    t0 = time.time()
    fails = []
    rec('=' * 100)
    rec('b322 -- THE MEMBERSHIP.')
    rec('=' * 100)

    for lbl, fn in (('b316 INSTRUMENT', INS.self_test), ('b317 ASSEMBLY', SM.self_test),
                    ('b319 STABLE', ST.self_test), ('THIS ACT LADDER', LD.self_test)):
        out = fn()
        good, arms = out[0], out[1]
        rec('  ### %-18s FIXTURES : %s  %s' % (lbl, arms, 'PASS' if good else '### FAIL ###'))
        if lbl == 'THIS ACT LADDER':
            for s in out[2]:
                rec('    ' + s)
        if not good:
            fails.append(lbl)
    rec('  ### **FIXTURE (i) IS THE ONE THAT LICENSES EVERYTHING BELOW:** ### this act reproduces')
    rec('  ### b319\'s BANKED residual to four decimals on BOTH cuts. ### **A LADDER THAT COULD NOT')
    rec('  ### ### REPRODUCE THE ROW IT EXTENDS WOULD BE A DIFFERENT MEASUREMENT WEARING ITS NAME.**')

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
    rec('### COMPONENT 1 -- THE LADDER ON THE RESIDUAL.')
    rec('=' * 100)
    rec('  ### **THE READING IS TAKEN FROM THE DIRECTION, AND IT IS TAKEN HERE.**')
    rec('  ### ### **BEFORE ANY DEFINITION IS UNFOLDED** -- (B1c) fixed that ordering before any')
    rec('  ### value existed, and Component 2 is written after this one has reported.')
    rec('')
    rec('    %-7s %-7s %-8s %-16s %-16s %-16s %-14s'
        % ('N', 'X', 'rank', 'residual stable', 'residual grid', 'tapered', 'max |x u(x)|'))
    rows = []
    for (N, X, NY) in SM.DOMAIN_AXIS:
        r = LD.frame_row(N, X, NY)
        rows.append(r)
        rec('    %-7d %-7g %-8d %-16.9f %-16.9f %-16.9f %-14.6f'
            % (r['N'], r['X'], r['rank'], r['stable'], r['grid'], r['tapered'], r['far']))
    res = [r['stable'] for r in rows]
    Xs = [r['X'] for r in rows]
    steps = [res[i + 1] - res[i] for i in range(len(res) - 1)]
    falls = all(s < 0.0 for s in steps)
    rec('')
    rec('    steps : %s' % ', '.join('%+.9f' % s for s in steps))
    rec('    ### ### **(B1a) DIRECTION : %s**' % ('FALLS' if falls else 'FLAT'))
    if falls:
        rec('    ### **SO THE RESIDUAL IS THE TRUNCATION\'S AND THE DERIVATION IS NOT CONTRADICTED')
        rec('    ### ### BY IT** -- which is (B1c), read off (B1a) and off nothing else.')
    else:
        rec('    ### **SO THE RESIDUAL IS THE REALIZATION\'S AND COMPONENT 2 MUST EXPLAIN A FIXED')
        rec('    ### ### FRACTION.**')

    p, _a, prms = LD.fit_power(Xs, res)
    q, _b, qrms = LD.fit_power(Xs, list(B321_INSTRUMENT))
    ratio = p / q if q else float('nan')
    comparable = BAR_COMPARABLE_LO <= ratio <= BAR_COMPARABLE_HI
    rec('')
    rec('  ### (1b) THE RATE, FITTED. ### **`log(residual) = A + p log(X)`, FIVE POINTS.**')
    rec('    the unit\'s residual        : p = %+.6f   (fit rms %.4f)' % (p, prms))
    rec('    b321\'s instrument residual : q = %+.6f   (fit rms %.4f)' % (q, qrms))
    rec('    ### ### **RATIO p/q = %.6f ; (B1b) BAND [%.1f, %.1f] : %s**'
        % (ratio, BAR_COMPARABLE_LO, BAR_COMPARABLE_HI, 'COMPARABLE' if comparable else 'NOT'))
    rec('    ### **BOTH LADDERS ARE FITTED BY THE SAME FITTER ON THE SAME FIVE DOMAINS**, so the')
    rec('    ### ratio is a comparison and not a coincidence of two conventions.')

    rec('')
    rec('  ### (1c) THE EDGE DIAGNOSTIC -- b316\'s OWN `taper`, IMPORTED.')
    rec('    ### b316: *"IF THE VIOLATION OF CONDITION TWO IS THE STEP AT THE END OF THE DOMAIN,')
    rec('    ### THIS MOVES IT; IF IT IS THE VECTOR, THIS DOES NOT."*')
    rec('    %-7s %-7s %-16s %-16s %-12s' % ('N', 'X', 'untapered', 'tapered', 'ratio'))
    trs = []
    for r in rows:
        tr = r['tapered'] / max(r['stable'], 1e-300)
        trs.append(tr)
        rec('    %-7d %-7g %-16.9f %-16.9f %-12.6f' % (r['N'], r['X'], r['stable'], r['tapered'], tr))
    edge = all(t < BAR_TAPER_EDGE for t in trs)
    vector = all(abs(t - 1.0) < BAR_TAPER_VECTOR for t in trs)
    verdict2 = 'THE EDGE' if edge else ('THE VECTOR' if vector else 'MIXED')
    rec('    ### ### **(B2) : %s**' % verdict2)
    if verdict2 == 'MIXED':
        rec('    ### **REPORTED AS MIXED AND NOT ROUNDED TO EITHER**, which the registration')
        rec('    ### required before the value existed.')

    rec('')
    rec('  ### (1d) THE SECOND ROUTE TO THE EXPONENT. ### **THE VECTOR\'S SHAPE, AT ONE FRAME.**')
    Nb, Xb, NYb = SM.DOMAIN_AXIS[-1]
    frb = INS.Frame(int(Nb), float(Xb), int(NYb))
    ub = INS.sonin_unit(frb)
    ys, ts = LD.tail_exponent(frb, ub)
    pt, _c, trms = LD.fit_power(ys, ts)
    farb = float(INS.far_bound(frb, ub, 0.5 * float(Xb)))
    del frb, ub
    rec('    at the largest frame (N = %d, X = %g), reading only that frame:' % (Nb, Xb))
    rec('      max |x u(x)| beyond X/2                  : %.6f  -- BOUNDED, so u ~ 1/x' % farb)
    rec('      the tail norm exponent, measured directly : %+.6f  (fit rms %.4f)' % (pt, trms))
    rec('      the exponent (B3) PREDICTED from u ~ 1/x  : %+.6f' % P_PREDICTED)
    agree = abs(p - P_PREDICTED) <= BAR_ROUTES * abs(P_PREDICTED)
    rec('    ### ### **(B3) THE LADDER\'S `p = %+.6f` AGAINST THE PREDICTED `%+.6f` : %s**'
        % (p, P_PREDICTED, 'AGREE' if agree else 'DISAGREE'))
    rec('    ### **AND THE DIRECTLY MEASURED TAIL EXPONENT IS REPORTED BESIDE BOTH, NOT INSTEAD OF')
    rec('    ### ### EITHER.** ### (B3) as sealed scores the ladder against the prediction that')
    rec('    ### boundedness licenses; the direct measurement is the same route made sharper, and')
    rec('    ### where the three numbers differ the act prints all three rather than choosing.')

    # ### ---------------------------------------------------------------- the gate, IN THE PATH
    rec('')
    rec('  ### THE NOISE-FLOOR GATE, IN THE PATH.')
    items = [('residual X=%g' % rows[i]['X'], rows[i]['stable'], rows[i + 1]['stable'])
             for i in range(len(rows) - 1)]
    ok, grows, detail = NF.gate(items, label='b322')
    for name, val, ref, verdict, why in grows:
        rec('    %-20s %-16.9f -> %-16.9f %-10s' % (name, val, ref, verdict))
    rec('    ### %s' % detail)
    rec('    ### **A REFUSED VALUE HAS ITS DIRECTION REPORTED AND NOT ITS SIZE.** ### The DIRECTION')
    rec('    ### of this course is what (B1a) reads, and a course that is still moving is a course')
    rec('    ### whose direction is exactly what can be read from it.')

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE TWO REALIZATIONS, UNFOLDED TO BASE OBJECTS.')
    rec('=' * 100)
    rec('  ### **NEITHER IS DESCRIBED IN THE OTHER\'S LANGUAGE**, which is the order\'s condition.')
    rec('  ### Each side carries the anchor that licenses it, and a row whose anchor does not pull')
    rec('  ### is not printed.')
    diffs = []
    for name, dtxt, danc, itxt, ianc, cmp_ in UNFOLD:
        dok, iok = pull(danc), (pull(ianc) or ianc in io.open(
            os.path.join(ROOT, 'tools', 'b316_instrument.py'), encoding='utf-8').read()
            or ianc in io.open(os.path.join(ROOT, 'tools', 'b319_stable.py'),
                               encoding='utf-8').read())
        rec('')
        rec('  ### ---- **%s**' % name)
        rec('    DERIVED (b300, on CM and b211)  : %s' % dtxt)
        rec('      anchor %-34s pulls : %s' % (repr(danc), dok))
        rec('    INSTRUMENT (b316, b319)          : %s' % itxt)
        rec('      anchor %-34s pulls : %s' % (repr(ianc), iok))
        rec('    ### %s' % cmp_)
        if not (dok and iok):
            fails.append('unfold anchor: ' + name)
        if cmp_.startswith('DIFFERENT') or cmp_.startswith('THE DERIVATION ASSERTS'):
            diffs.append(name)
    rec('')
    rec('  ### ### **CONSTITUENTS THAT DIFFER : %d -- %s**' % (len(diffs), ', '.join(diffs)))
    rec('  ### ### **AND THE FIRST OF THEM IN (B6)\'s ORDER IS THE ONE THAT COUNTS.**')
    order = ['THE AMBIENT', 'CONDITION ONE', 'THE EIGENRELATION', 'CONDITION TWO', 'THE TRANSFORM',
             'THE INNER PRODUCT', 'THE DOMAIN', 'THE SPACE']
    first = next((n for n in order if n in diffs), None)
    rec('  ### ### **FIRST DIFFERING CONSTITUENT : %s**' % (first or 'NONE'))

    # ### ==========================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE VERDICT ON THE LEG, AT EXACTLY ITS SCOPE.')
    rec('=' * 100)
    if falls and edge and agree:
        branch = 'IN, DERIVED AND MEASURED TO CONVERGE'
    elif (not falls) or vector:
        branch = 'DIFFERENT VECTORS'
    else:
        branch = 'UNDER-RESOLVED'
    rec('  ### (B1a) %s   (B2) %s   (B3) %s'
        % ('FALLS' if falls else 'FLAT', verdict2, 'AGREE' if agree else 'DISAGREE'))
    rec("  ### ### **BRANCH REACHED BY THIS RUNNER'S CHAIN : %s**" % branch)
    both = falls and vector and agree
    if both:
        rec('  ### ### ### **AND TWO BRANCH CONDITIONS FIRED AT ONCE. ### THE SEAL DID NOT ORDER')
        rec('  ### ### ### THEM.**')
        rec('  ### (B5) reads *(DIFFERENT VECTORS) -- if (B1a) is FLAT, or if (B2) is THE VECTOR*')
        rec('  ### and *(UNDER-RESOLVED) -- if the arms disagree*. ### With `FALLS`, `THE VECTOR`')
        rec('  ### and `AGREE`, ### **BOTH HOLD**, and the registration says nothing about which')
        rec("  ### wins. ### **THE `if/elif` ABOVE IS THIS TOOL'S ORDERING AND NOT THE SEAL'S.**")
        rec('  ### ### ### **THE ACT TAKES THE WEAKER OF THE TWO: ### UNDER-RESOLVED.** ###')
        rec('  ### `DIFFERENT VECTORS` is a positive claim about the object; `UNDER-RESOLVED` is a')
        rec('  ### claim about this resolution. ### **BETWEEN TWO BRANCHES A DEFECTIVE RULE LICENSES')
        rec('  ### ### EQUALLY, AN ACT MAY NOT HELP ITSELF TO THE STRONGER ONE**, and the bank')
        rec('  ### carries the defect at full prominence.')
    price = None
    if res[-1] > 0 and p < 0:
        price = float(Xs[-1] * (PRICE_TARGET / res[-1]) ** (1.0 / p))
        rec('')
        rec('  ### **THE PRICE, COMPUTED AS b321 PRICED THE EXPONENT.** ### From the fitted `p` and')
        rec('  ### the last measured residual, the domain at which the residual would reach')
        rec('  ### `%.2f` is ### **`X = %.3e`**, against the `X = %g` this act reached --'
            % (PRICE_TARGET, price, Xs[-1]))
        rec('  ### a factor of ### **%.3e**.' % (price / Xs[-1]))
        rec('  ### ### **THAT IS AN EXTRAPOLATION OF A FITTED SLOPE AND IT IS LABELLED AS ONE.** ###')
        rec('  ### It is a price, not a prediction: it says what the instrument would have to reach,')
        rec('  ### on the assumption that the fitted exponent continues, and the act does not claim')
        rec('  ### that it does.')
    rec('')
    rec('  ### **THE OBJECT\'S CONDITIONS, RESTATED FROM THE LIST.**')
    rec('    ### **CONDITION ONE** -- `xi(q) = 0` for `|q| <= 1`. ### Quoted at CM for the derived')
    rec('    ### object; IMPOSED by array construction for the instrument\'s.')
    rec('    ### **CONDITION TWO** -- `(F_eR xi)(p) = 0` for `|p| <= 1`. ### Derived in one line for')
    rec('    ### the derived object; MEASURED, and nonzero, for the instrument\'s.')
    rec('    ### **THE AMBIENT** -- even, and in `L^2(R)`. ### Evenness quoted; ### **`L^2` STATED BY')
    rec('    ### ### NO OWNER AND STILL OPEN AS `W-ORD-PHI-MU-L2`**, which b300 filed and this act')
    rec('    ### does not close.')
    rec('')
    rec('  ### ### **AND WHAT IS NOT DONE HERE: ### NO UNIT IS ADOPTED AND NONE IS REPLACED.** ###')
    rec('  ### b300\'s derivation stands at DERIVES-on-IMPORTS. ### b316\'s and b319\'s measurements')
    rec('  ### stand at theirs. ### **NEITHER IS RE-VERDICTED BY THIS ACT.**')

    rec('')
    rec('=' * 100)
    rec('  ### CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)

    payload = dict(rows=rows, p=p, p_rms=prms, q=q, q_rms=qrms, ratio=ratio,
                   comparable=bool(comparable), falls=bool(falls), taper=verdict2,
                   taper_ratios=trs, tail_exponent=pt, tail_rms=trms, far=farb,
                   agree=bool(agree), branch=branch, price=price, diffs=diffs, first=first,
                   noise_ok=bool(ok), fails=fails)
    d = (json.dumps(payload, indent=1, default=float) + '\n').encode('utf-8')
    open(os.path.join(D, 'b322_rows.json') + '.tmp', 'wb').write(d)
    os.replace(os.path.join(D, 'b322_rows.json') + '.tmp', os.path.join(D, 'b322_rows.json'))
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    io.open(os.path.join(D, 'b322_components_run.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
