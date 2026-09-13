# -*- coding: utf-8 -*-
"""b446_components.py -- THE FLOOR HAS A DOMAIN. ### **UNDER (R58) AND (R59), AFTER THE LOCK.**

### Usage: `python b446_components.py run` -- the second doubling at the five cells, each result banked in
### `data/b446_doubling.json` as soon as it is computed, so a run can resume; `python b446_components.py
### report` -- Components 1, 3 and 4, by the rules the face fixed, into `data/b446_components.txt`.
### ### No chain file is edited: `nv` is passed; `NU` is set on the imported atlas module with its kernel
### cache cleared and restored -- b445's arm (a) code path, carried.
"""
import io
import json
import math
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
DBL = os.path.join(D, 'b446_doubling.json')
OUT = os.path.join(D, 'b446_components.txt')
FLOOR = 1.49e-08
NV0, NU0 = 8193, 12001
NV2, NU2 = 4 * NV0 - 3, 4 * NU0 - 3      # 32769, 48001
FIVE = ['3.158312', '3.461088', '3.605551', '4.061553', '4.123106']
OUTLIER = '4.123106'
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def load(p):
    try:
        return json.load(io.open(p, encoding='utf-8'))
    except Exception:
        return {}


def save(d):
    io.open(DBL + '.tmp', 'w', encoding='utf-8').write(json.dumps(d, indent=1))
    os.replace(DBL + '.tmp', DBL)


def run():
    import carto_atlas as AT
    import b317_smear as SM
    import b318_square as SQ
    import b321_window as WI
    assert SQ.AUTOCORR_NV == NV0 and AT.NU == NU0 and len(AT.GAM) == 10000, 'the chain is not at its banked constants'
    assert (NV2, NU2) == (32769, 48001)
    arms = load(os.path.join(D, 'b445_arms.json'))
    d = load(DBL)
    AT.NU = NU2
    AT._KERN = None
    try:
        for k in FIVE:
            if k in d:
                continue
            a = arms['a'][k]['a']
            t = time.time()
            g = SM.mean_zero_variant(a)
            f = SQ.autocorrelation(g, nv=NV2)
            ch = WI.channels(f.v, f.w)
            d[k] = dict(a=a, e=ch['residual'], zero=ch['zero'], arch=ch['arch'], prime=ch['prime'], pole=ch['pole'],
                        nv=NV2, nu=NU2, ngam=int(len(AT.GAM)), seconds=round(time.time() - t, 1))
            save(d)
            print('aa  a=%-10s e=%+.4e  %.0fs' % (k, ch['residual'], time.time() - t), flush=True)
    finally:
        AT.NU = NU0
        AT._KERN = None


def report():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    arms = load(os.path.join(D, 'b445_arms.json'))
    dbl = load(DBL)
    rungs = load(os.path.join(D, 'b437_rungs.json'))
    rec('=' * 100)
    rec('b446 -- THE FLOOR HAS A DOMAIN. ### THE COMPONENTS, RUN AFTER THE LOCK, UNDER (R58) AND (R59).')
    rec('=' * 100)

    # ---------------------------------------------------------------- COMPONENT 1, THE HISTORY
    rec('')
    rec('  ### ### **COMPONENT 1 -- WHERE THE FLOOR CAME FROM. QUOTED BY LINE FROM THE SOURCES.**')

    def q(rel, needle):
        ls = io.open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read().splitlines()
        h = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
        rec('      %s:%d | %s' % ((rel,) + h[0]) if h else '      ### MISS %s %r' % (rel, needle))
        return bool(h)
    ok_hist = all([
        q('tools/noise_floor.py', 'DEFAULT_FLOOR = math.sqrt(MACHINE_EPS)'),
        q('tools/noise_floor.py', "b264's bank names `~1.5e-8 ~ sqrt(machine"),
        q('data/b264_run.txt', 'lam_n(NQ=700)    lam_n(NQ=1400)'),
        q('data/b264_run.txt', 'they sit at `~1.5e-8 ~ sqrt(machine epsilon)`'),
        q('tools/noise_floor.py', 'ANY ACT READING A COMPUTED SPECTRAL OR MODAL QUANTITY'),
        q('tools/noise_floor.py', 'IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM.'),
        q('data/b437_closing.txt', 'THE FLOOR, PRICED PAST THREE RADII FOR THE FIRST TIME.'),
    ])
    rec('    ### ORIGIN : b264, eigenvalues lam_n of a quadrature discretization at NQ = 700 and 1400, four modes')
    rec('    ###          stopping between 1.52e-08 and 2.18e-08 -- identified there with sqrt(machine epsilon).')
    rec('    ### DEFINED: b272, noise_floor.py, DEFAULT_FLOOR = sqrt(2.220446049250313e-16) = 1.4901161193847656e-08.')
    rec('    ### METHOD : not a measurement at this object; the float64 rounding level, the same at every radius.')
    rec('    ### DOMAIN : stated OF KIND by the emitting act -- computed spectral or modal quantities; OF RADIUS, none.')
    rec('    ### b437   : RAN the gate at 5.196152, 5.385165, 5.567764 and called that pricing; it set no floor and')
    rec('    ###          stated no domain.')
    rec('    history quoted from sources : %s' % ok_hist)

    # ---------------------------------------------------------------- COMPONENT 3, THE DOUBLING
    rec('')
    rec('  ### ### **COMPONENT 3 -- THE SECOND DOUBLING (nv 32769, NU 48001), AT THE FIVE CELLS.**')
    rec('    %-10s %-12s %-12s %-12s %-8s %-8s %-10s %s' % ('a', 'e0 8193', 'e1 16385', 'e2 32769', 'rate', 'order p',
                                                            'limit E', '|e2| vs the quoted bar'))
    orders, limits, c3 = {}, {}, {}
    for k in FIVE:
        e0, e1 = arms['base'][k]['e'], arms['a'][k]['e']
        if k not in dbl:
            rec('    %-10s %+.3e   %+.3e   NOT RUN' % (k, e0, e1))
            c3[k] = dict(run=False)
            continue
        e2 = dbl[k]['e']
        rate = math.log2(abs(e1) / abs(e2)) if e2 != 0 else float('inf')
        p = math.log2(abs(e0 - e1) / abs(e1 - e2)) if e1 != e2 else float('inf')
        E = e2 - (e1 - e2) / (2 ** p - 1) if math.isfinite(p) and p != 0 else float('nan')
        orders[k], limits[k] = p, E
        below = abs(e2) <= FLOOR
        c3[k] = dict(run=True, e0=e0, e1=e1, e2=e2, rate=rate, p=p, E=E, below=below)
        rec('    %-10s %+.3e   %+.3e   %+.3e   %-8.2f %-8.2f %+.2e  %s' % (k, e0, e1, e2, rate, p, E,
            'BELOW 1.49e-08 (the bar quoted outside its kind)' if below else 'above 1.49e-08 (the bar quoted outside its kind)'))
    nbelow = sum(1 for v in c3.values() if v.get('below'))
    rec('    cells run %d of 5 ; |e2| below the quoted bar at %d of 5' % (sum(1 for v in c3.values() if v['run']), nbelow))
    others = sorted(orders[k] for k in FIVE if k != OUTLIER and k in orders)
    refuses = None
    if OUTLIER in orders and len(others) == 4:
        m = (others[1] + others[2]) / 2
        refuses = not (m - 0.5 <= orders[OUTLIER] <= m + 0.5)
        rec('    THE OUTLIER RULE: median of the other four orders m = %.2f ; %s order %.2f ; window [%.2f, %.2f] -> %s'
            % (m, OUTLIER, orders[OUTLIER], m - 0.5, m + 0.5, 'REFUSES' if refuses else 'CONVERGES AT THE OTHERS` RATE'))
        if refuses:
            rec('    ### WHAT WOULD EXPLAIN IT, PRICED AND NOT RUN: the integrand`s non-smooth points falling against the grid')
            rec('    ### differently at this radius from one level to the next, so the error does not shrink monotonely. NOT')
            rec('    ### the rung alone: 4.123106 is sqrt(17), where b437`s ladder turns from rung 10 to 11, but 3.605551 is')
            rec('    ### sqrt(13), also at a prime power, and converged at order 1.04. The test: a third doubling at this cell')
            rec('    ### (nv 65537, about two minutes at the second doubling`s 48 s) and a read of where the kinks fall modulo')
            rec('    ### the grid spacing at each level. NOT RUN -- (R58) opened the lane for the second doubling only.')
    if orders:
        fin = [k for k in FIVE if k in orders and k != OUTLIER]
        rec('    ### THE ORDERS ARE NOT THE TRAPEZOID RULE`S ASYMPTOTIC 2: the other four measure %s. The limits E rest on'
            % ', '.join('%.2f' % orders[k] for k in fin))
        rec('    ### those orders and are PRE-ASYMPTOTIC ESTIMATES; E is printed, and not read as a residual of the object.')

    # ---------------------------------------------------------------- COMPONENT 1, THE PER-CELL FLOOR
    rec('')
    rec('  ### ### **COMPONENT 1 -- THE CHAIN`S OWN DISCRETIZATION ERROR AT nv = 8193, PER CELL. NO FUNCTION FITTED.**')
    ps = [orders[k] for k in FIVE if k in orders]
    span = (max(ps) - min(ps)) if len(ps) >= 3 else None
    pstar = sorted(ps)[len(ps) // 2] if (span is not None and span <= 1.0) else None
    rec('    measured orders %s ; span %s ; p* %s' % (['%.2f' % x for x in ps], ('%.2f' % span) if span is not None else '-',
                                                    ('%.2f' % pstar) if pstar is not None else 'NOT TAKEN (span > 1.0 or fewer than three)'))
    c1 = []
    rec('    %-10s %-12s %-12s %-14s %s' % ('a', 'e0 8193', 'e1 16385', 'error at 8193', 'how'))
    for k in sorted(arms['base'], key=float):
        e0, e1 = arms['base'][k]['e'], arms['a'][k]['e']
        if k in limits and math.isfinite(limits[k]):
            err, how = e0 - limits[k], 'THREE LEVELS, measured order %.2f' % orders[k]
        elif pstar is not None:
            err, how = (e0 - e1) / (1 - 2 ** (-pstar)), 'TWO LEVELS -- AN ESTIMATE AT THE ASSUMED ORDER p* %.2f' % pstar
        else:
            err, how = e0 - e1, 'TWO LEVELS -- e0 - e1 ALONE (no p* taken)'
        c1.append(dict(a=k, e0=e0, e1=e1, err=err, how=how))
        rec('    %-10s %+.3e   %+.3e   %+.3e     %s' % (k, e0, e1, err, how))
    unmeasured = []
    for r in rungs.get('rows', []):
        if r.get('resid') is None:
            continue
        k = '%.6f' % r['a']
        if k not in arms['base']:
            unmeasured.append((k, r['resid']))
    for k, e in unmeasured:
        rec('    %-10s %+.3e   NOT MEASURED -- below the quoted bar at base; no arm ran here' % (k, e))
    rec('    cells printed : %d measured, %d NOT MEASURED' % (len(c1), len(unmeasured)))

    # ---------------------------------------------------------------- COMPONENT 4
    rec('')
    rec('  ### ### **COMPONENT 4 -- THE MINT.**')
    import ast
    src = io.open(os.path.join(T, 'noise_floor.py'), encoding='utf-8').read()
    names = [t.id for n in ast.parse(src).body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)]
    kind_bound = any(re.search(r'KIND|DOMAIN|SCOPE', x) for x in names)
    param_bound = any(re.search(r'PARAM|NQ', x) for x in names) or 'NQ=700' in src
    readable = kind_bound and param_bound
    rec('    names bound in noise_floor.py : %s' % names)
    rec('    kind bound in code : %s ; parameters bound in code : %s -> READABLE BY A GATE : %s' % (kind_bound, param_bound, readable))
    rec('    ### ### **A FLOOR CARRIES THE DOMAIN OF KIND AND THE PARAMETERS OVER WHICH IT WAS MEASURED; A FLOOR QUOTED')
    rec('    ### ### OUTSIDE THAT DOMAIN IS A BAR WHOSE STRICTNESS IS UNKNOWN.**')
    rec('    ### %s' % ('FILED AS JUDGEMENT, NOT MECHANIZED: registration_gate.py is not edited, and the rule is not listed beside'
                       ' the mechanized ones.' if not readable else 'READABLE -- the face fixed judgement only if unreadable; see the checks.'))
    # ---------------------------------------------------------------- COMPONENT 2, READ FROM ITS OWN BANK
    cj = load(os.path.join(D, 'b446_floor_census.json'))
    rec('')
    rec('  ### ### **COMPONENT 2 -- THE CENSUS, AS b446_census.py BANKED IT (data/b446_floor_census.txt).**')
    kd = cj.get('kind', {})
    res = cj.get('residue', {})
    rec('    controls : %s' % ('PASS' if cj.get('controls', {}).get('ok') else '### FAIL'))
    rec('    comparisons %d ; IN %d ; OUT %d (share %.3f) ; floor-arm decisions by M2 %d ; drift-arm refusals %d ; passed both %d'
        % (kd.get('all', 0), kd.get('all', 0) - kd.get('out', 0), kd.get('out', 0),
           (kd.get('out', 0) / kd['all']) if kd.get('all') else 0, cj.get('m2', 0),
           cj.get('m1_verdicts', {}).get('DRIFTING', 0), cj.get('m1_verdicts', {}).get('RESOLVED', 0)))
    rec('    residue, not governing: JSON gate records AT_FLOOR %s, all on an exact zero : %s'
        % (res.get('json_verdicts', {}).get('AT_FLOOR'), res.get('at_floor_zero_only')))

    # ---------------------------------------------------------------- ADDITION (a)
    rec('')
    rec('  ### ### **ADDITION (a) -- THE FLOOR ARM`S OWN RECORD.**')
    m0 = cj.get('m0', {})
    rec('    the figures the ruling quoted, as what they count: lines carrying RESOLVED %s, DRIFTING %s, AT_FLOOR %s, over %s'
        % (m0.get('RESOLVED'), m0.get('DRIFTING'), m0.get('AT_FLOOR'), cj.get('m0_stems')))
    rec('    file stems (%s of them act stems) -- WORD-LINES, PROSE INCLUDED; both AT_FLOOR lines are definitions.' % cj.get('m0_act_stems'))
    q('tools/noise_floor.py', 'IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM.')
    rec('    ### ### **WHAT THE FLOOR ARM DECIDED IN THE BANKED RECORD: %s AT_FLOOR VERDICTS IN THE TEXT MATCHERS` REACH, AND %s'
        % (cj.get('m1_verdicts', {}).get('AT_FLOOR', 0), res.get('json_verdicts', {}).get('AT_FLOOR', 0)))
    rec('    ### ### STRUCTURED AT_FLOOR RECORDS IN ONE JSON BANK -- EVERY ONE ON A VALUE OF EXACTLY ZERO, WHICH ANY POSITIVE')
    rec('    ### ### FLOOR REFUSES. THE FLOOR`S SIZE, 1.49e-08, DECIDED NONE. "ABOVE THE FLOOR" IN A CLOSING REPORTS THE ARM')
    rec('    ### ### THAT DID NOT GOVERN.** ### Nothing re-verdicted; the count is the product.')

    # ---------------------------------------------------------------- THE EXPECTATIONS
    rec('')
    rec('  ### ### **THE EXPECTATIONS, SCORED ON THE DOMAIN OF KIND.**')
    n1 = 'REFUTED -- b272`s contract states a domain of kind: computed spectral or modal quantities'
    share = (kd.get('out', 0) / kd['all']) if kd.get('all') else 0
    n2 = ('HELD -- %d of %d comparisons OUT of kind, share %.3f (with b264`s mode rows read IN: %.3f)'
          % (kd.get('out', 0), kd.get('all', 0), share, (kd.get('out', 0) - res.get('b264_rows_out', 0)) / kd['all'])
          if share > 0.5 else 'REFUTED -- OUT share %.3f' % share)
    n3a = ('HELD' if nbelow == 4 else 'REFUTED') + ' -- %d of 5 below the quoted bar (outside its kind)' % nbelow
    n3b = ('NOT SCORABLE -- the outlier did not run' if refuses is None else
           ('HELD -- ' if refuses else 'REFUTED -- ') + 'the outlier`s order %.2f against the window of the other four'
           % orders.get(OUTLIER, float('nan')))
    rec('    (N1)    neither emitting act stated a domain            ### %s' % n1)
    rec('            radius reading: no radius domain was stated -- VACUOUS, the floor was measured at no radius')
    rec('    (N2)    more than half the comparisons lie outside     ### %s' % n2)
    rec('            radius reading: all lie outside -- VACUOUS, the radius domain is empty')
    rec('    (N3)(a) four of five fall below the floor               ### %s' % n3a)
    rec('    (N3)(b) the outlier still refuses                       ### %s' % n3b)
    rec('    ### the seat`s own from the face: (N1) REFUTED -- %s; (N2) HELD -- %s; (N3) no expectation.'
        % ('HELD' if n1.startswith('REFUTED') else 'REFUTED', 'HELD' if n2.startswith('HELD') else 'REFUTED'))
    expect = dict(n1=n1, n2=n2, n3a=n3a, n3b=n3b)

    rec('')
    rec('    ### NO CLAIM ABOUT RH, h2 OR ANY ZERO. NOTHING RE-VERDICTED.')
    rec('    ### ### **THE INSTRUMENT LANE OPENED BY (R58) CLOSES AT THIS ACT`S END.** No instrument built; no chain file edited.')
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    d = load(DBL)
    d['report'] = dict(orders=orders, limits=limits, c3=c3, below=nbelow, outlier_refuses=refuses, pstar=pstar, span=span,
                       c1=c1, unmeasured=unmeasured, readable=readable, history_ok=ok_hist, expect=expect)
    io.open(DBL + '.tmp', 'w', encoding='utf-8').write(json.dumps(d, indent=1))
    os.replace(DBL + '.tmp', DBL)


if __name__ == '__main__':
    if sys.argv[1] == 'run':
        run()
    else:
        report()
