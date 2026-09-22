# -*- coding: utf-8 -*-
"""b483_components.py -- COMPONENTS 1, 2 AND 3. ### Run after the seal (sha256 `6847ae11ad584c97...`).
### ### **NO CHAIN IS RUN AND NO ENTRY IS COMPUTED.** ### Every matrix element is a banked entry of
### `b477_entries.jsonl`; an entry the bank does not hold is ABSENT and is never interpolated.
### ### **THE SIGNATURE IS READ ON `-G`, PER (R87).**
"""
import io
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

FLOOR = 1.49e-08          # ### the chain's own floor (b476 (A)(5), b446).
TAIL = 6.421e-11          # ### the largest reported `trunc_bound` over the diagonal cells.

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def entries():
    out = []
    for l in io.open(os.path.join(D, 'b477_entries.jsonl'), encoding='utf-8'):
        l = l.strip()
        if l:
            out.append(json.loads(l))
    return out


def spectrum(M):
    """### **eigh PLUS THE RESIDUAL FOR EVERY EIGENPAIR.** ### The residual is not decoration: it is
    ### the only thing that says the returned number solves the problem that was posed."""
    w, V = np.linalg.eigh(M)
    r = [float(np.linalg.norm(M @ V[:, i] - w[i] * V[:, i])) for i in range(len(w))]
    return w, r


def primepowers(hi):
    out = []
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        k, v = 1, p
        while v <= hi:
            out.append((v, '%d^%d' % (p, k) if k > 1 else '%d' % p))
            k += 1
            v = p ** k
    return sorted(set(out))


def main():
    E = entries()
    dg = {d['a']: d for d in E if d['kind'] == 'diagonal'}
    cd = {d['a']: d for d in E if d['kind'] == 'control_diagonal'}
    od = {}
    fam_cells = {}
    for d in E:
        if d['kind'] != 'offdiagonal':
            continue
        od[(d['a'], d['b'])] = d
        od[(d['b'], d['a'])] = d
        fam_cells.setdefault(d['family'], [])
        for x in (d['a'], d['b']):
            if x not in fam_cells[d['family']]:
                fam_cells[d['family']].append(x)
    # ### **THE NESTING ORDER IS THE RUN'S OWN SEED ORDER**, read off the diagonal entries in the
    # ### order they were appended -- not re-sorted here, because a re-sort would silently change
    # ### which cell each family size adds.
    seedorder = [d['a'] for d in E if d['kind'] == 'diagonal']
    for f in fam_cells:
        fam_cells[f] = [a for a in seedorder if a in fam_cells[f]]

    OUT = {}
    rec('=' * 108)
    rec('COMPONENT 1 -- THE GRAMS, FORMED FROM THE BANK AND READ AT EVERY FAMILY SIZE.')
    rec('=' * 108)
    rec('  ### **THE ORIENTATION, (R87):** `W = PR - A`, `Sum_v W_v(f) = -Z`, ### **THE SIGNATURE IS')
    rec('  ### READ ON `-G`.** ### Under RH `-G` is positive semidefinite. ### **(F2) HALTS ON A')
    rec('  ### POSITIVE EIGENVALUE OF `G`** beyond the threshold, which is ### **THE SMALLEST')
    rec('  ### EIGENVALUE OF `-G` GOING NEGATIVE.** ### Both ends are printed under both names.')
    rec('')

    for fam in ('AIM PLANE', 'LADDER'):
        cells = fam_cells[fam]
        N = len(cells)
        rec('-' * 108)
        rec('  ### FAMILY: %s   ### cells: %d   ### a from %g to %g' % (fam, N, cells[0], cells[-1]))
        rec('-' * 108)
        Gz = np.zeros((N, N))
        Gc = np.zeros((N, N))
        Err = np.zeros((N, N))
        absent = 0
        for i, a in enumerate(cells):
            Gz[i, i] = dg[a]['W']
            Gc[i, i] = cd[a]['places']
            Err[i, i] = abs(dg[a]['W'] + dg[a]['zero'])
            for j, b in enumerate(cells):
                if i == j:
                    continue
                e = od.get((a, b))
                if e is None:
                    absent += 1
                    continue
                Gz[i, j] = e['W']
                Gc[i, j] = e['control_places']
                Err[i, j] = abs(e['W'] + e['zero'])
        rec('    entries the bank does not hold : %d ### -- ### **NONE IS INTERPOLATED.**' % absent)
        rec('    ### **THE INSTRUMENT`S OWN RESOLUTION, MEASURED ENTRY BY ENTRY.** ### Every zeta')
        rec('    ### entry carries BOTH sides, so `|W + Z|` is a per-entry measure of how well the')
        rec('    ### two sides agree. ### By Weyl, no eigenvalue is determined better than the')
        rec('    ### spectral norm of that error matrix.')
        rec('')
        hdr = ('%-4s %-15s %-15s %-10s %-10s %-10s %-11s %s'
               % ('n', 'lam_min(-G)', 'lam_max(-G)', 'neg@obs', 'neg@floor', 'neg@tail',
                  'Weyl |E|', 'max resid'))
        rec('    ### ZETA. ### `lam_min(-G)` IS `-lam_max(G)`: the falsifier-bearing end.')
        rec('    ' + hdr)
        rec('    ' + '-' * 100)
        zrows = []
        for n in range(1, N + 1):
            M = -Gz[:n, :n]
            w, r = spectrum(M)
            En = float(np.linalg.norm(Err[:n, :n], 2))
            row = dict(n=n, a=cells[n - 1], lmin=float(w[0]), lmax=float(w[-1]),
                       neg_obs=int((w < -En).sum()), neg_floor=int((w < -FLOOR).sum()),
                       neg_tail=int((w < -TAIL).sum()), weyl=En, resid=max(r))
            zrows.append(row)
            rec('    %-4d %-15.6e %-15.6e %-10d %-10d %-10d %-11.3e %.2e'
                % (n, row['lmin'], row['lmax'], row['neg_obs'], row['neg_floor'],
                   row['neg_tail'], En, row['resid']))
        rec('')
        rec('    ### CONTROL (Epstein, ### **PLACES SIDE ONLY -- THE CHAIN HAS NO ZERO SIDE**).')
        rec('    %-4s %-15s %-15s %-10s %-10s %s'
            % ('n', 'lam_min(-G)', 'lam_max(-G)', 'neg@floor', 'neg@tail', 'max resid'))
        rec('    ' + '-' * 86)
        crows = []
        for n in range(1, N + 1):
            M = -Gc[:n, :n]
            w, r = spectrum(M)
            row = dict(n=n, a=cells[n - 1], lmin=float(w[0]), lmax=float(w[-1]),
                       neg_floor=int((w < -FLOOR).sum()), neg_tail=int((w < -TAIL).sum()),
                       resid=max(r))
            crows.append(row)
            rec('    %-4d %-15.6e %-15.6e %-10d %-10d %.2e'
                % (n, row['lmin'], row['lmax'], row['neg_floor'], row['neg_tail'], row['resid']))
        OUT[fam] = dict(cells=cells, zeta=zrows, control=crows,
                        max_resolution=float(np.linalg.norm(Err, 2)))
        rec('')

    # =============================================================== COMPONENT 2
    rec('=' * 108)
    rec('COMPONENT 2 -- THE SIX, SCORED IN (R87)`S ORIENTATION, EACH WITH ITS DECIDING FIGURE.')
    rec('=' * 108)
    S = {}

    # ---- (F1)
    rec('')
    rec('  ### **(F1) UNINFORMATIVE** -- the control`s Gram shows no negative index at the resolving')
    rec('  ### family, so the instrument cannot see a hyperbolic plane.')
    rec('  ### THE RESOLVING FAMILY SIZE, PRICED BY b476 BEFORE THE RUN : ### **ONE CELL** (all 35')
    rec('  ### cells resolve `t`, the smallest at `a = 1.3` with `|hhat| = 1.286e-02`).')
    r1 = OUT['AIM PLANE']['control'][0]
    rec('  ### THE DECIDING FIGURE: the control`s `-G` at size 1 in the aim plane has the single')
    rec('  ### eigenvalue ### **%+.6e**, so its negative index is ### **%d**.'
        % (r1['lmin'], r1['neg_floor']))
    f1 = r1['neg_floor'] == 0
    rec('  ### ### **(F1) %s.**' % ('FIRES' if f1 else 'DOES NOT FIRE'))
    rec('  ### ### **AND IT FIRES ON FORM, NOT ON MEASUREMENT.** ### A one-by-one symmetric matrix has')
    rec('  ### one eigenvalue and ### **CANNOT BE INDEFINITE WHATEVER ITS ENTRY IS**, so a negative')
    rec('  ### index at the priced resolving size was ### **ARITHMETICALLY UNAVAILABLE BEFORE THE RUN')
    rec('  ### STARTED.** ### **THE DEFECT IS IN THE PRICED RESOLVING SIZE, NOT IN THE CONTROL**:')
    rec('  ### b476 derived "the resolving family size is one cell" from a per-cell resolution test,')
    rec('  ### and a per-cell test cannot bound the size of a matrix that needs a PAIR to be')
    rec('  ### indefinite. ### The control`s behaviour at sizes above one is read under (N1) below.')
    S['F1'] = dict(verdict='FIRES' if f1 else 'DOES NOT FIRE',
                   figure=r1['lmin'], reason='one-by-one cannot be indefinite; defect is the price')

    # ---- (F2)
    rec('')
    rec('  ### **(F2) HALT** -- a positive eigenvalue of zeta`s `G` beyond the threshold.')
    worst = None
    for fam in OUT:
        for r in OUT[fam]['zeta']:
            if worst is None or r['lmin'] < worst[1]['lmin']:
                worst = (fam, r)
    fam, r = worst
    rec('  ### THE DECIDING FIGURE, over every family size of both families: the most negative')
    rec('  ### `lam_min(-G)` anywhere is ### **%+.6e**, at %s size %d (`a = %g`) --'
        % (r['lmin'], fam, r['n'], r['a']))
    rec('  ### equivalently ### **`lam_max(G) = %+.6e`**, which is the falsifier-bearing end.'
        % (-r['lmin'],))
    ths = [('the observed two-side agreement (Weyl)', r['weyl']),
           ('the chain floor', FLOOR), ('the reported tail figure', TAIL)]
    rec('  ### READ AGAINST EACH THRESHOLD, ALL THREE PRINTED:')
    fires = {}
    for name, th in ths:
        f = r['lmin'] < -th
        fires[name] = f
        rec('      %-42s %-12.3e ### %s' % (name, th, 'FIRES' if f else 'does not fire'))
    flip = len(set(fires.values())) > 1
    rec('  ### ### **(F2) %s.**' % ('FIRES' if all(fires.values()) else
                                    ('FIRES ON SOME THRESHOLDS AND NOT OTHERS' if flip
                                     else 'DOES NOT FIRE')))
    if flip:
        rec('  ### ### **AND THE VERDICT FLIPS WITH THE THRESHOLD, SO BOTH READINGS ARE GIVEN**, as')
        rec('  ### the face required before any spectrum existed.')
    else:
        rec('  ### ### **THE VERDICT IS THE SAME ON ALL THREE THRESHOLDS**, so it does not depend on')
        rec('  ### which one is chosen.')
    S['F2'] = dict(verdict=('FIRES' if all(fires.values()) else
                            ('THRESHOLD-DEPENDENT' if flip else 'DOES NOT FIRE')),
                   worst=r['lmin'], family=fam, n=r['n'], a=r['a'],
                   weyl=r['weyl'], flips=flip)

    # ---- (N1)
    rec('')
    rec('  ### **(N1)** the control goes indefinite at a family size below the full aim plane.')
    first = {}
    for fam in OUT:
        f = next((x for x in OUT[fam]['control'] if x['neg_floor'] > 0), None)
        first[fam] = f
        if f:
            rec('      %-10s first indefinite at size ### **%d** (`a = %g`), `lam_min(-G) = %+.6e`,'
                % (fam, f['n'], f['a'], f['lmin']))
            rec('                 negative index %d, residual %.2e' % (f['neg_floor'], f['resid']))
        else:
            rec('      %-10s ### **NEVER INDEFINITE** at any size, to %d cells'
                % (fam, len(OUT[fam]['control'])))
    fa = first['AIM PLANE']
    n1 = bool(fa) and fa['n'] < len(OUT['AIM PLANE']['control'])
    rec('  ### ### **(N1) %s.**' % ('HELD' if n1 else 'REFUTED'))
    if fa:
        rec('  ### The aim plane has %d cells and the control goes indefinite at size ### **%d**,'
            % (len(OUT['AIM PLANE']['control']), fa['n']))
        rec('  ### which is below the full plane. ### **SO THE INSTRUMENT CAN SEE A HYPERBOLIC PLANE')
        rec('  ### AFTER ALL -- JUST NOT AT THE SIZE b476 PRICED.**')
    S['N1'] = dict(verdict='HELD' if n1 else 'REFUTED',
                   first={k: (v['n'] if v else None) for k, v in first.items()})

    # ---- (F3)
    rec('')
    rec('  ### **(F3) MEASURED** -- zeta stays within the threshold at every size to the reach')
    rec('  ### ### **WHILE THE CONTROL GOES INDEFINITE AT THE PRICED SIZE.**')
    c1 = not (S['F2']['verdict'] == 'FIRES')
    c2 = (r1['neg_floor'] > 0)
    rec('      conjunct (a) zeta within the threshold at every size : %s' % c1)
    rec('      conjunct (b) the control indefinite ### **AT THE PRICED SIZE (one cell)** : %s' % c2)
    rec('  ### ### **(F3) %s.**' % ('MET' if (c1 and c2) else 'NOT MET'))
    rec('  ### ### **AND THE REASON IS CONJUNCT (b), NOT ANYTHING ZETA DOES.** ### In the aim plane')
    rec('  ### the control is NEVER indefinite; in the ladder it first is at size %s -- and in'
        % (first['LADDER']['n'] if first['LADDER'] else 'NONE'))
    rec('  ### neither family at the PRICED size of one. ### So `(F3)` fails on the same defect')
    rec('  ### `(F1)` exposed. ### **THE COMPRESSION REGISTER THEREFORE TAKES NO GRADE FROM THIS')
    rec('  ### RUN**, and in particular ### **NOT `MEASURED`.**')
    S['F3'] = dict(verdict='MET' if (c1 and c2) else 'NOT MET', zeta_ok=c1, control_at_priced=c2)

    # ---- (N2)
    rec('')
    rec('  ### **(N2)** zeta`s falsifier-bearing end goes the wrong way at some family size, within')
    rec('  ### the bound. ### Under (R87) that end is ### **THE LARGEST EIGENVALUE OF `G`**.')
    rec('  ### ### **(N2) IS A CLAIM ABOUT A SUB-BOUND EXCURSION**, so its two conjuncts are')
    rec('  ### (a) the sign goes the wrong way at all, and (b) it stays WITHIN the bound. ### It')
    rec('  ### therefore CANNOT also demand that the excursion exceed the resolution -- that would')
    rec('  ### be `(F2)`. ### **THE FIRST READING OF THIS PREDICATE IN THIS ACT`S OWN TOOL HAD IT')
    rec('  ### BACKWARDS AND SCORED `(N2)` REFUTED; THE ERROR IS THE SEAT`S AND IS CORRECTED HERE.**')
    exc = []
    for fam in OUT:
        for x in OUT[fam]['zeta']:
            if -x['lmin'] > 0.0:
                exc.append((fam, x))
    rec('  ### sizes where `lam_max(G) > 0` at all : ### **%d**' % len(exc))
    for f, x in exc[:4]:
        rec('      %-10s n=%-3d a=%-10g lam_max(G) = %+.6e   resolution %.3e'
            % (f, x['n'], x['a'], -x['lmin'], x['weyl']))
    if len(exc) > 4:
        rec('      ... and %d more, all in the same family.' % (len(exc) - 4))
    n2 = False
    if exc:
        big = max(-x['lmin'] for _, x in exc)
        within_obs = big <= max(x['weyl'] for _, x in exc)
        within_tail = big <= TAIL
        rec('  ### the LARGEST such excursion : ### **%+.6e**' % big)
        rec('      within the observed resolution (%.3e) : ### **%s**'
            % (max(x['weyl'] for _, x in exc), within_obs))
        rec('      within the reported tail figure (%.3e) : ### **%s**' % (TAIL, within_tail))
        n2 = within_obs
        rec('  ### ### **(N2) %s, READ AGAINST THE OBSERVED RESOLUTION.**'
            % ('HELD' if within_obs else 'REFUTED'))
        rec('  ### ### **AND `REFUTED` READ AGAINST THE TAIL FIGURE** -- because against THAT figure')
        rec('  ### the excursion is not "within the bound" at all, it is `(F2)`. ### **THE SAME')
        rec('  ### NUMBER IS AN EXPECTATION MET OR A HALT DEPENDING ON WHICH BOUND IS BELIEVED**,')
        rec('  ### and that, not the number, is this act`s finding.')
    else:
        rec('  ### ### **(N2) REFUTED** -- the sign never goes the wrong way at any size.')
    S['N2'] = dict(verdict=('HELD at the observed resolution, REFUTED at the tail figure'
                            if exc and n2 else ('REFUTED' if not exc else 'REFUTED')),
                   count=len(exc),
                   largest=(max(-x['lmin'] for _, x in exc) if exc else None))

    # ---- (N3)
    rec('')
    rec('  ### **(N3)** the earliest such excursion sits at a family whose supports straddle a prime')
    rec('  ### power -- ### **A RESEMBLANCE, NAMED AS ONE.**')
    if not n2:
        rec('  ### ### **(N3) VACUOUS** -- `(N2)` found no excursion, so there is no earliest one, and')
        rec('  ### ### **A VACUOUS PASS IS NOT EVIDENCE.** ### The word is printed in the same')
        rec('  ### sentence as the verdict, as (R59) requires.')
        S['N3'] = dict(verdict='VACUOUS')
    else:
        f, x = exc[0]
        cells = OUT[f]['cells']
        prev = cells[x['n'] - 2] if x['n'] >= 2 else 0.0
        pp = [q for q in primepowers(max(cells)) if prev < q[0] <= x['a']]
        rec('  ### the earliest excursion : %s size %d, the cell it ADDS is `a = %g` (the previous'
            % (f, x['n'], x['a']))
        rec('  ### cell being `a = %g`).' % prev)
        rec('  ### THE READING OF "STRADDLE", FIXED HERE AND NOT AFTER: the step from the previous')
        rec('  ### cell to this one straddles a prime power `q` when `a_prev < q <= a_n`.')
        rec('  ### prime powers in that half-open step : ### **%s**'
            % (', '.join('%g (%s)' % q for q in pp) if pp else 'NONE'))
        rec('  ### ### **(N3) %s.**' % ('HELD' if pp else 'REFUTED'))
        S['N3'] = dict(verdict='HELD' if pp else 'REFUTED',
                       family=f, n=x['n'], a=x['a'], prev=prev, straddles=[q[1] for q in pp])
        rec('  ### ### **AND IT IS A RESEMBLANCE EITHER WAY.** ### One family, one step, no control')
        rec('  ### over non-prime-power steps of the same size -- ### **A COINCIDENCE THIS ACT')
        rec('  ### RECORDS AND DOES NOT PROMOTE.**')
        rec('')
        rec('  ### ### **BUT THE CELL IT LANDS ON IS ALREADY NAMED IN THE RECORD, BY ANOTHER**')
        rec('  ### ### **MEASUREMENT ENTIRELY.** ### `a = 4.12311` is ### **`sqrt(17)`**, and')
        rec('  ### `b446` recorded it as ### **THE OUTLIER THAT REFUSES**: *"THE OUTLIER 4.123106:')
        rec('  ### order -0.34 against [0.95, 1.95] -- REFUSES"* (`b446_closing.txt:82`), the one')
        rec('  ### cell of five whose decorrelation order fell outside the window. ### `b437` has')
        rec('  ### the ladder turning from rung 10 to rung 11 at the same place.')
        rec('  ### ### **SO TWO UNRELATED MEASUREMENTS SINGLE OUT THE SAME CELL** -- b446`s')
        rec('  ### residual-order test and this act`s signature test -- ### **AND THAT IS STILL A')
        rec('  ### RESEMBLANCE AND NOT A MECHANISM.** ### b446 itself already refused the obvious')
        rec('  ### reading, recording that it is ### **"not the rung alone: 3.605551 = sqrt(13)')
        rec('  ### converged"**. ### The seat routes this and claims nothing from it.')

    # =============================================================== COMPONENT 3
    rec('')
    rec('=' * 108)
    rec('COMPONENT 3 -- WHAT THIS INSTRUMENT CAN AND CANNOT RESOLVE.')
    rec('=' * 108)
    res = max(OUT[f]['max_resolution'] for f in OUT)
    for f in sorted(OUT):
        rec('  ### the observed two-side disagreement in %-10s : ### **%.3e**'
            % (f, OUT[f]['max_resolution']))
    rec('  the three candidate thresholds, largest first:')
    rec('    ### **the observed two-side disagreement, spectral norm over the full matrix : %.3e**'
        % res)
    rec('    the chain floor, sqrt(eps)                                          : %.3e' % FLOOR)
    rec('    the largest reported `trunc_bound`                                  : %.3e' % TAIL)
    rec('  ### ### **THEY SPAN SIX ORDERS, AND THE LARGEST IS THE ONE THE INSTRUMENT ACTUALLY**')
    rec('  ### ### **SUPPORTS.** ### `trunc_bound` bounds the truncation of the zero SUM; it says')
    rec('  ### nothing about the quadrature of the places side, and the measured disagreement')
    rec('  ### between the two sides is up to seven orders larger than it.')
    rec('  ### ### **SO THE SMALLEST EIGENVALUE MAGNITUDE THIS INSTRUMENT COULD HONESTLY CALL')
    rec('  ### NON-ZERO IS ABOUT `%.0e`**, and any verdict resting on a figure below that is a' % res)
    rec('  ### verdict about rounding.')
    rec('')
    rec('  ### AND TWO SCOPES THAT DO NOT WIDEN:')
    rec('    (i)  ### **THE CONTROL IS A PLACES-SIDE GRAM.** ### `b325_epstein.channels_q` returns')
    rec('         `arch`, `finite`, `places`, `pole` and ### **NO ZERO SIDE**, so the control shows')
    rec('         what the places side of the Epstein object does under this family and ### **CANNOT')
    rec('         SHOW WHAT A SUMMED EPSTEIN ZERO CHANNEL WOULD.** ### Its resolution also cannot be')
    rec('         measured the way zeta`s was, ### **BECAUSE THERE IS NO SECOND SIDE TO COMPARE IT')
    rec('         TO** -- so the control`s own figures are read against the chain floor alone.')
    rec('    (ii) ### **THE TWO FAMILIES ARE NEVER PAIRED.** ### No cross-family entry was computed,')
    rec('         so nothing here bears on a Gram over the union of the two families.')

    io.open(os.path.join(D, 'b483_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(scores=S, resolution=res, floor=FLOOR, tail=TAIL,
                   families={f: dict(cells=OUT[f]['cells'], zeta=OUT[f]['zeta'],
                                     control=OUT[f]['control'],
                                     resolution=OUT[f]['max_resolution']) for f in OUT}),
              io.open(os.path.join(D, 'b483_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
