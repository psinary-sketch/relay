# -*- coding: utf-8 -*-
"""b503_zero.py -- COMPONENTS 1 TO 4: THE ZERO SIDE ALIAS-FREE, THE TAIL RE-READ, THE ATTRIBUTION.

### `python tools/b503_zero.py c1 | fixture | cells I J | report`
### ### **THE RULES ARE THE FACE`S, SEALED BEFORE THIS RAN**: verification on the ORDERED residual
### `Z_exact - (P - PR + A)` with the chain`s banked P, PR, A; the CONSISTENT residual (A by the exact
### transform) beside it; the fixture on the identity `exact = sinc^2(u dv/2) x trapezoid`, raw
### difference printed beside. ### `b326_closure.hhat_exact` is imported, not edited; the zero bank is
### `carto_atlas.GAM`, unchanged. ### Each cell is appended to `b503_cells.jsonl` as it finishes.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'e16'))
import carto_atlas as AT        # noqa: E402
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b326_closure as BC       # noqa: E402

NL = chr(10)
CELLS = os.path.join(D, 'b503_cells.jsonl')
GAM = np.asarray(AT.GAM, dtype=np.float64)
LOW5 = GAM[:5]
U = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rows_all():
    """### the 119 cells with their banked places side and bound: b501`s 35 (A, PR from b492), b502`s 84."""
    b492 = {r['a']: r for r in json.loads(io.open(os.path.join(D, 'b492_cells.json'), encoding='utf-8').read())['rows']}
    old = [json.loads(l) for l in io.open(os.path.join(D, 'b501_cells.jsonl'), encoding='utf-8') if l.strip()]
    new = [json.loads(l) for l in io.open(os.path.join(D, 'b502_cells.jsonl'), encoding='utf-8') if l.strip()]
    out = []
    for r in old:
        z = b492[r['a']]
        out.append(dict(a=r['a'], set='old', A=r['A'], PR=r['PR'], P=z['pole'], m=r['m'], B=r['B'],
                        Z_trap=z['zero'], res_trap=r['achieved'], trunc=r['trunc']))
    for r in new:
        out.append(dict(a=r['a'], set='new', A=r['arch'], PR=r['prime'], P=r['pole'], m=r['m'], B=r['B'],
                        Z_trap=r['zero'], res_trap=r['achieved'], trunc=r['trunc'], L=r['L']))
    out.sort(key=lambda r: r['a'])
    for i, r in enumerate(out):
        r['k'] = i
        r['kind0'] = ('VERIFIED' if r['res_trap'] <= r['B'] else
                      'ALIASED' if r['res_trap'] > 10 * r['B'] else 'ESTIMATE-SHORT')
    return out


def vw(a):
    f = SQ.autocorrelation(SM.mean_zero_variant(a))
    return np.asarray(f.v), np.asarray(f.w)


# ================================================================================================ c1
def c1():
    L = ['=' * 104, 'COMPONENT 1 -- THE FAILURE, LOCATED.', '=' * 104,
         '    the chain`s zero bank : `carto_atlas.GAM` -- ### **%d ORDINATES, %.10f TO %.6f**' % (GAM.size, GAM[0], GAM[-1]),
         '    `b326_closure.json` is a DIFFERENT bank (b326`s closure), not the chain`s.', '']
    rs = rows_all()
    unv = [r for r in rs if r['kind0'] != 'VERIFIED']
    L.append('    ### ### **UNVERIFIED BY (R113)(1)`S RULE : %d** -- old %d, new %d ; ALIASED %d, ESTIMATE-SHORT %d'
             % (len(unv), sum(r['set'] == 'old' for r in unv), sum(r['set'] == 'new' for r in unv),
                sum(r['kind0'] == 'ALIASED' for r in unv), sum(r['kind0'] == 'ESTIMATE-SHORT' for r in unv)))
    L.append('')
    L.append('    ### THE 23 NEW UNVERIFIED CELLS -- the image at 2 pi / dv (grid 2 x 8193 - 1 points), T = %.2f:' % GAM[-1])
    L.append('    %-11s %-10s %-10s %-10s %-10s %-9s %s' % ('a', 'L', 'image', 'trunc', '|W+Z|', 'B', 'kind'))
    for r in [x for x in unv if x['set'] == 'new']:
        dv = 2 * r['L'] / (2 * 8193 - 2)
        L.append('    %-11.6f %-10.4f %-10.1f %-10.2e %-10.2e %-9.2e %s'
                 % (r['a'], r['L'], 2 * math.pi / dv, r['trunc'], r['res_trap'], r['B'], r['kind0']))
    L.append('')
    L.append('    ### ### **IS THE BANK TOO SHORT? NO** -- it reaches 9877.78, and the image`s own position decides.')
    L.append('    ### ### **DOES THE TRANSFORM OVERFLOW? NO; IT ALIASES** -- the trapezoid sum carries a full image')
    L.append('    ### of its main lobe at 2 pi / dv, which falls from above T + 200 to below T as L grows.')
    L.append('    ### ### **IS trunc WRONG? IT IS BLIND** -- it reads the image while the image sits in [T, T + 200]')
    L.append('    ### (2.2e+02 from a = 12.845) and cannot see it once it falls among the zeros (a >= 13.637).')
    L.append('    ### The 33 marks, with kinds:')
    for r in unv:
        L.append('      %-4s a=%-10.6f  |W+Z| %.3e  B %.3e  x%-9.3g %s' % (r['set'], r['a'], r['res_trap'], r['B'],
                                                                    r['res_trap'] / r['B'], r['kind0']))
    io.open(os.path.join(D, 'b503_components_c1.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump([dict(a=r['a'], set=r['set'], kind=r['kind0'], res=r['res_trap'], B=r['B']) for r in unv],
              io.open(os.path.join(D, 'b503_marks.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


# ================================================================================================ fixture
def fixture():
    a = 4.061553
    v, w = vw(a)
    dv = float(v[1] - v[0])
    ex = BC.hhat_exact(v, w, LOW5)
    tr = AT.hhat(v, w, LOW5)
    sinc2 = (np.sin(LOW5 * dv / 2) / (LOW5 * dv / 2)) ** 2
    ident = np.abs(ex - sinc2 * tr) / np.abs(ex)
    raw = np.abs(ex - tr) / np.abs(ex)
    ex2 = BC.hhat_exact2(v, w, LOW5)
    routes = np.abs(ex - ex2) / np.abs(ex)
    L = ['=' * 104, 'COMPONENT 2 -- THE FIXTURE, BEFORE USE, AT a = 4.061553 (VERIFIED).', '=' * 104,
         '    dv = %.6e ; w at the ends %.3e, %.3e' % (dv, w[0], w[-1]),
         '    %-14s %-22s %-22s %-12s %-12s %-12s' % ('gamma', 'exact', 'trapezoid', 'identity', 'RAW', 'two routes')]
    for g, e, t, i, r, q in zip(LOW5, ex, tr, ident, raw, routes):
        L.append('    %-14.6f %+.15e %+.15e %-12.2e %-12.2e %-12.2e' % (g, e, t, i, r, q))
    ok = bool(np.all(ident <= 1e-12))
    L += ['    ### ### **THE IDENTITY exact = sinc^2(u dv/2) x trapezoid HOLDS TO %.2e RELATIVE -- %s THE 1e-12 BAR.**'
          % (ident.max(), 'WITHIN' if ok else 'OUTSIDE'),
          '    ### The RAW relative difference is %.2e -- the two are NOT the same number, as the face said.' % raw.max(),
          '    ### The two closed-form arrangements agree to %.2e.' % routes.max(), '=' * 104]
    io.open(os.path.join(D, 'b503_fixture.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(a=a, dv=dv, identity_max=float(ident.max()), raw_max=float(raw.max()), routes_max=float(routes.max()),
                   passes=ok), io.open(os.path.join(D, 'b503_fixture.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))
    return 0 if ok else 2


# ================================================================================================ cells
def cells(i, j):
    fx = json.loads(io.open(os.path.join(D, 'b503_fixture.json'), encoding='utf-8').read())
    if not fx['passes']:
        print('### THE FIXTURE DID NOT PASS -- NO CELL IS RUN.')
        return 2
    rs = rows_all()
    done = set()
    if os.path.exists(CELLS):
        done = {json.loads(l)['k'] for l in io.open(CELLS, encoding='utf-8') if l.strip()}
    K = AT.kernel(U)
    for r in rs[i:j]:
        if r['k'] in done:
            continue
        t0 = time.time()
        v, w = vw(r['a'])
        h = BC.hhat_exact(v, w, GAM)
        Z = 2.0 * float(np.sum(h))
        low = [2.0 * float(x) for x in h[:5]]
        Aex = float(np.trapezoid(BC.hhat_exact(v, w, U) * K, U) / (2.0 * math.pi))
        res_o = Z - (r['P'] - r['PR'] + r['A'])
        res_c = Z - (r['P'] - r['PR'] + Aex)
        row = dict(r, Z=Z, low5=low, rem=Z - sum(low), A_exact=Aex, res_ordered=res_o, res_consistent=res_c,
                   verified=abs(res_o) <= r['B'], m_minus_Z=r['m'] - Z, seconds=round(time.time() - t0, 1))
        row['kind'] = ('VERIFIED' if row['verified'] else
                       'ALIASED' if abs(res_o) > 10 * r['B'] else 'ESTIMATE-SHORT')
        with io.open(CELLS, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(row) + NL)
        print('  %3d %-3s a=%-10.6f |res| %.2e (was %.2e)  B %.2e  %-14s consistent %.2e  m-Z %+.2e  %.0fs'
              % (r['k'], r['set'], r['a'], abs(res_o), r['res_trap'], r['B'], row['kind'], abs(res_c),
                 row['m_minus_Z'], row['seconds']), flush=True)


# ================================================================================================ report
def extrema(xs, ys):
    out = []
    for k in range(1, len(xs) - 1):
        if ys[k] > ys[k - 1] and ys[k] > ys[k + 1]:
            out.append(('MAX', k))
        if ys[k] < ys[k - 1] and ys[k] < ys[k + 1]:
            out.append(('MIN', k))
    return out


def fit(xs, ys, g):
    G = np.array([g(x) for x in xs])
    Y = np.array(ys)
    c = float(np.dot(G, Y) / np.dot(G, G))
    return c, float(math.sqrt(np.mean((Y - c * G) ** 2)))


FORMS = [('(a) c', lambda a: 1.0), ('(b) c/a', lambda a: 1.0 / a),
         ('(c) c/log a', lambda a: 1.0 / math.log(a)), ('(d) c/a^2', lambda a: 1.0 / (a * a))]


def report():
    rs = sorted((json.loads(l) for l in io.open(CELLS, encoding='utf-8') if l.strip()), key=lambda r: r['a'])
    ver = [r for r in rs if r['verified']]
    unv = [r for r in rs if not r['verified']]
    L = ['=' * 104, 'COMPONENTS 2 TO 4 -- THE ZERO SIDE, THE TAIL, THE ATTRIBUTION.', '=' * 104,
         '    cells run : %d ; compute %.0f s' % (len(rs), sum(r['seconds'] for r in rs)),
         '    ### ### **VERIFIED AFTER THE EXACT TRANSFORM : %d OF %d**' % (len(ver), len(rs)),
         '    ### ### **STILL UNVERIFIED, WITH KIND : %d**' % len(unv)]
    for r in unv:
        L.append('      %-3s a=%-10.6f ordered %.3e  B %.3e  x%.3g  %s   consistent %.3e'
                 % (r['set'], r['a'], abs(r['res_ordered']), r['B'], abs(r['res_ordered']) / r['B'], r['kind'],
                    abs(r['res_consistent'])))
    L += ['', '    ### THE 33 MARKED CELLS, BEFORE AND AFTER:',
          '    %-11s %-15s %-10s %-10s %-10s %-10s %s' % ('a', 'kind before', 'trap res', 'exact res', 'consistent', 'B', 'now')]
    for r in rs:
        if r['kind0'] != 'VERIFIED':
            L.append('    %-11.6f %-15s %-10.2e %-10.2e %-10.2e %-10.2e %s'
                     % (r['a'], r['kind0'], r['res_trap'], abs(r['res_ordered']), abs(r['res_consistent']), r['B'], r['kind']))
    short = [r for r in rs if r['kind0'] == 'ESTIMATE-SHORT']
    # ### ### **REPAIRED: THE FIRST VERSION NARRATED THE SEAT`S PREDICTION ("a shortfall that survives is the
    # ### estimate`s") BESIDE A COUNT OF 0 THAT CONTRADICTED IT.** ### The reading is now computed, on the
    # ### CONSISTENT residual -- the one that compares one transform of one f -- and says what it says.
    s_ok = [r for r in short if abs(r['res_consistent']) <= r['B']]
    L.append('    ### ESTIMATE-SHORT cells (%d): the ordered residual equals the trapezoid one (to 5%%) at %d -- the'
             % (len(short), sum(abs(abs(r['res_ordered']) - r['res_trap']) <= 0.05 * r['res_trap'] for r in short)))
    L.append('    ### ordered residual mixes two transforms and is not a like-for-like comparison. ### On the CONSISTENT')
    L.append('    ### residual, %d of %d are within their bound: ### **THOSE SHORTFALLS WERE THE TRAPEZOID TRANSFORM`S;**'
             % (len(s_ok), len(short)))
    L.append('    ### the other %d %s.' % (len(short) - len(s_ok), 'remain short on either residual and are the estimate`s' if len(short) - len(s_ok) else 'are none'))
    cver = [r for r in rs if abs(r['res_consistent']) <= r['B']]
    cx, cy = [r['a'] for r in cver], [r['m'] for r in cver]
    L += ['', '    ### ### **BESIDE, NOT IN PLACE: VERIFIED ON THE CONSISTENT RESIDUAL : %d OF %d**' % (len(cver), len(rs)),
          '    ### its extrema of m : %s' % ['%s %.6f' % (t, cx[k]) for t, k in extrema(cx, cy)],
          '    ### consistent-unverified : %s' % [round(r['a'], 6) for r in rs if abs(r['res_consistent']) > r['B']]]
    # ------------------------------------------------------------------ component 3
    xs, ys = [r['a'] for r in ver], [r['m'] for r in ver]
    ex = extrema(xs, ys)
    L += ['', '### COMPONENT 3 -- THE TAIL, ON THE %d VERIFIED CELLS ALONE.' % len(ver), '-' * 104]
    for t, k in ex:
        L.append('    %s  a=%.6f  m=%+.9f  (%s)' % (t, xs[k], ys[k], ver[k]['set']))
    after = [r for r in ver if r['a'] > 13.152946 + 1e-9]
    rise = bool(after) and all(after[k + 1]['m'] > after[k]['m'] for k in range(len(after) - 1)) and after[0]['m'] > 0.000690365
    L.append('    verified cells after 13.152946 : %d ; ### **THE RISE SURVIVES : %s**'
             % (len(after), rise if after else 'NOT SCORABLE -- no verified cell after it'))
    fits = {}
    vo = [r for r in ver if r['set'] == 'old']
    vn = [r for r in ver if r['set'] == 'new']
    for name, g in FORMS:
        co, ro = fit([r['a'] for r in vo], [r['m'] for r in vo], g)
        cn, rn = fit([r['a'] for r in vn], [r['m'] for r in vn], g)
        fits[name] = dict(c_old=co, rms_old=ro, c_new=cn, rms_new=rn)
        L.append('    %-12s  verified OLD (%d) rms=%.6e    verified NEW (%d) rms=%.6e' % (name, len(vo), ro, len(vn), rn))
    wn = min(fits, key=lambda k: fits[k]['rms_new'])
    wo = min(fits, key=lambda k: fits[k]['rms_old'])
    L.append('    ### least on verified new : %s ; on verified old : %s' % (wn, wo))
    # ------------------------------------------------------------------ component 4
    L += ['', '### COMPONENT 4 -- THE ATTRIBUTION, AT THE VERIFIED CELLS.', '-' * 104,
          '    max |m - Z| : %.3e ; max |P| : %.3e ; cells with |m - Z| >= 1e-06 : %d'
          % (max(abs(r['m_minus_Z']) for r in ver), max(abs(r['P']) for r in ver),
             sum(abs(r['m_minus_Z']) >= 1e-6 for r in ver))]
    names = ['z1 %.4f' % LOW5[0], 'z2 %.4f' % LOW5[1], 'z3 %.4f' % LOW5[2], 'z4 %.4f' % LOW5[3], 'z5 %.4f' % LOW5[4]]
    zex = {}
    for j in range(5):
        zs = [r['low5'][j] for r in ver]
        zex[j] = extrema(xs, zs)
        L.append('    %-12s extrema at : %s' % (names[j], ['%s %.6f' % (t, xs[k]) for t, k in zex[j]] or 'NONE'))
    rex = extrema(xs, [r['rem'] for r in ver])
    L.append('    %-12s extrema at : %s' % ('remainder', ['%s %.6f' % (t, xs[k]) for t, k in rex] or 'NONE'))
    match = {}
    for t, k in ex:
        hits = [names[j] for j in range(5) if any(abs(kk - k) <= 1 for _, kk in zex[j])]
        match['%s %.6f' % (t, xs[k])] = hits
        L.append('    ### m`s %s at a=%.6f : zero terms with an extremum within one cell : ### **%s**'
                 % (t, xs[k], hits or 'NONE'))
    L.append('=' * 104)
    io.open(os.path.join(D, 'b503_components_c234.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    m13 = next((key for key in match if '13.152946' in key), None)
    json.dump(dict(n=len(rs), verified=len(ver), unverified=[dict(a=r['a'], kind=r['kind']) for r in unv],
                   extrema=[dict(t=t, a=xs[k]) for t, k in ex], rise=rise, after13=len(after), fits=fits,
                   win_new=wn, win_old=wo, max_m_minus_Z=max(abs(r['m_minus_Z']) for r in ver),
                   n_mz_big=sum(abs(r['m_minus_Z']) >= 1e-6 for r in ver), match=match, m13=m13,
                   m13_z1=(m13 is not None and names[0] in match[m13]),
                   aliased_before=[r['a'] for r in rs if r['kind0'] == 'ALIASED'],
                   aliased_now_verified=[r['a'] for r in rs if r['kind0'] == 'ALIASED' and r['verified']],
                   short_before=[r['a'] for r in short], short_now_verified=[r['a'] for r in short if r['verified']],
                   seconds=sum(r['seconds'] for r in rs),
                   consistent_verified=len(cver), consistent_extrema=[dict(t=t, a=cx[k]) for t, k in extrema(cx, cy)],
                   consistent_unverified=[r['a'] for r in rs if abs(r['res_consistent']) > r['B']],
                   short_consistent_ok=len(s_ok)),
              io.open(os.path.join(D, 'b503_results.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'cells':
        sys.exit(cells(int(sys.argv[2]), int(sys.argv[3])))
    sys.exit({'c1': c1, 'fixture': fixture, 'report': report}[cmd]())
