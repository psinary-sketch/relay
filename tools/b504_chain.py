# -*- coding: utf-8 -*-
"""b504_chain.py -- THE CHAIN ON ONE TRANSFORM: ALL 119 CELLS, THE BOUND, AND THE EPSTEIN CONTROL.

### `python tools/b504_chain.py kernels | fixture | cells I J | report`
### ### **(R114): ONE INSTRUMENT, ONE TRANSFORM.** Z, A and P all by the exact transform of the piecewise-
### linear `(v, w)` -- `b326_closure.hhat_exact` and `mellin_exact`, imported, unedited. ### **THE GRID
### FOLLOWS THE BANK**: nv the smallest value, not below 8193, putting the image `2 pi (nv-1)/L` above
### `T + 200`; ceiling 16385. ### The bound is b501`s rule, under the exact transform. ### The Epstein
### control runs b325`s kernel (the control of record) and b326`s derived kernel beside it, on the same
### `hhat_exact(u)`. ### Each cell is appended to `b504_cells.jsonl` as it finishes.
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
import b321_window as WI        # noqa: E402
import b325_epstein as EP       # noqa: E402
import b326_closure as BC       # noqa: E402
import b326_windows as BW       # noqa: E402
import b501_bound as BB         # noqa: E402  ### the richardson rule, imported
import b503_zero as BZ          # noqa: E402  ### extrema, fits, the 119 cells` a-values

NL = chr(10)
CELLS = os.path.join(D, 'b504_cells.jsonl')
KFILE = os.path.join(D, 'b504_kernels.npz')
GAM = np.asarray(AT.GAM, dtype=np.float64)
TOP = float(GAM[-1])
FLOOR_NV, CEIL_NV = 8193, 16385
U_BASE = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)
U_HALF = np.linspace(-AT.UMAX, AT.UMAX, 2 * AT.NU - 1)
U_WIDE = np.linspace(-2 * AT.UMAX, 2 * AT.UMAX, 2 * AT.NU - 1)
LIB = json.loads(io.open(os.path.join(D, 'b326_epstein_zeros.json'), encoding='utf-8').read())
GQ = np.array([z['gamma_a'] for z in LIB['zeros']], dtype=np.float64)
TOPQ = float(GQ.max())

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def kernels():
    """### the three kernels on the three u-grids, once, banked; the zeta base kernel is the atlas`s own."""
    if os.path.exists(KFILE):
        z = np.load(KFILE)
        return {k: z[k] for k in z.files}
    t0 = time.time()
    K = {}
    for name, U in (('base', U_BASE), ('half', U_HALF), ('wide', U_WIDE)):
        AT._KERN = None
        K['z_' + name] = np.array(AT.kernel(U))
        AT._KERN = None
        K['q325_' + name] = np.array(EP.kernel_q(U))
        K['qd_' + name] = np.array(BW.kernel_q_derived(U))
        assert len(K['z_' + name]) == len(U)
    np.savez(KFILE, **K)
    print('  kernels computed in %.0f s' % (time.time() - t0))
    return K


def choose_nv(L):
    nv = max(FLOOR_NV, int(math.floor((TOP + 200.0) * L / (2 * math.pi))) + 2)
    while 2 * math.pi * (nv - 1) / L <= TOP + 200.0:
        nv += 1
    return nv


def arch(H, U, K):
    return float(np.trapezoid(H * K, U) / (2.0 * math.pi))


def epstein_zero(v, w):
    on = 2.0 * float(np.sum(BC.hhat_exact(v, w, GQ)))
    off = 0.0
    for o in LIB['offline']:
        b, g = o['rho_a']
        for rho in (complex(b, g), complex(b, -g), complex(1 - b, g), complex(1 - b, -g)):
            off += BC.ftilde(v, w, rho)[0].real
    return on + off, on, off


def pole(v, w):
    return float(np.real(BC.mellin_exact(v, w, np.array([0.5 + 0j]))[0] + BC.mellin_exact(v, w, np.array([-0.5 + 0j]))[0]))


def cell(a, K, nv_force=None):
    g = SM.mean_zero_variant(a)
    L = 2.0 * abs(float(g.v[-1]))
    nv = nv_force or choose_nv(L)
    image = 2 * math.pi * (nv - 1) / L
    if nv > CEIL_NV:
        return dict(a=a, nv=nv, image=image, ceiling=True)
    lv = []
    for n in (nv, 2 * nv - 1, 4 * nv - 3):
        f = SQ.autocorrelation(g, n)
        v, w = np.asarray(f.v), np.asarray(f.w)
        H = BC.hhat_exact(v, w, U_BASE)
        PR = WI.prime_sum(v, w, 'corpus')[0]
        FQ = EP.finite_channel(v, w)[0]
        Az, A325, Ad = arch(H, U_BASE, K['z_base']), arch(H, U_BASE, K['q325_base']), arch(H, U_BASE, K['qd_base'])
        lv.append(dict(nv=n, v=v, w=w, H=H, PR=PR, FQ=FQ, Az=Az, A325=A325, Ad=Ad,
                       m=Az - PR, m325=A325 - FQ, md=Ad - FQ))
    b = lv[0]
    v, w = b['v'], b['w']
    Hh, Hw = BC.hhat_exact(v, w, U_HALF), BC.hhat_exact(v, w, U_WIDE)
    hz = BC.hhat_exact(v, w, GAM)
    Z = 2.0 * float(np.sum(hz))
    ZQ, ZQon, ZQoff = epstein_zero(v, w)
    P = pole(v, w)
    out = dict(a=a, nv=nv, image=image, ceiling=False, L=float(v[-1]), P=P,
               A=b['Az'], PR=b['PR'], Z=Z, m=b['m'], low5=[2.0 * float(x) for x in hz[:5]],
               rem=Z - 2.0 * float(np.sum(hz[:5])), FQ=b['FQ'], ZQ=ZQ, ZQ_on=ZQon, ZQ_off=ZQoff)
    for key, kz in (('z', 'z'), ('q325', 'q325'), ('qd', 'qd')):
        mk = {'z': 'm', 'q325': 'm325', 'qd': 'md'}[key]
        Ak = {'z': 'Az', 'q325': 'A325', 'qd': 'Ad'}[key]
        Ev, kind, order = BB.richardson(*[l[mk] for l in lv])
        A0 = b[Ak]
        Eu = abs(arch(Hh, U_HALF, K[kz + '_half']) - A0) + abs(arch(Hw, U_WIDE, K[kz + '_wide']) - A0)
        out['B_' + key] = Ev + Eu
        out['kindR_' + key] = kind
    out['A325'], out['Ad'] = b['A325'], b['Ad']
    out['m325'], out['md'] = b['m325'], b['md']
    out['r'] = Z - (P - b['PR'] + b['Az'])
    out['r325'] = ZQ - (P - b['FQ'] + b['A325'])
    out['rd'] = ZQ - (P - b['FQ'] + b['Ad'])
    return out


def fixture():
    K = kernels()
    b503 = {round(r['a'], 6): r for r in (json.loads(l) for l in io.open(os.path.join(D, 'b503_cells.jsonl'), encoding='utf-8') if l.strip())}
    L = ['=' * 104, 'COMPONENT 1 -- THE FIXTURE: b503`S CONSISTENT RESIDUAL REPRODUCED AT THREE VERIFIED CELLS.', '=' * 104]
    ok = True
    rows = []
    for a in (4.061553, 5.196152, 10.392193):
        key = min(b503, key=lambda k: abs(k - a))
        c = cell(b503[key]['a'], K, nv_force=None)
        d = abs(c['r'] - b503[key]['res_consistent'])
        ok = ok and d <= 1e-12 and c['nv'] == 8193
        rows.append(dict(a=b503[key]['a'], nv=c['nv'], r=c['r'], r_b503=b503[key]['res_consistent'], diff=d))
        L.append('    a=%-10.6f nv %d  r %+.15e  b503 %+.15e  |diff| %.2e' % (b503[key]['a'], c['nv'], c['r'], b503[key]['res_consistent'], d))
    L += ['    ### ### **REPRODUCED TO 1e-12 AT ALL THREE : %s**' % ok, '=' * 104]
    io.open(os.path.join(D, 'b504_fixture.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(rows=rows, passes=ok), io.open(os.path.join(D, 'b504_fixture.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))
    return 0 if ok else 2


def cells(i, j):
    fx = json.loads(io.open(os.path.join(D, 'b504_fixture.json'), encoding='utf-8').read())
    if not fx['passes']:
        print('### THE FIXTURE DID NOT PASS -- NO CELL IS RUN.')
        return 2
    K = kernels()
    A = [r['a'] for r in BZ.rows_all()]
    done = set()
    if os.path.exists(CELLS):
        done = {json.loads(l)['k'] for l in io.open(CELLS, encoding='utf-8') if l.strip()}
    for k in range(i, min(j, len(A))):
        if k in done:
            continue
        t0 = time.time()
        c = cell(A[k], K)
        c['k'] = k
        c['seconds'] = round(time.time() - t0, 1)
        if c['ceiling']:
            c['verified'] = False
            c['kind'] = 'IMAGE-ABOVE-CEILING'
        else:
            c['verified'] = abs(c['r']) <= c['B_z']
            c['kind'] = 'VERIFIED' if c['verified'] else ('ESTIMATE-SHORT' if abs(c['r']) <= 10 * c['B_z'] else 'OTHER')
            for q in ('325', 'd'):
                c['verified_q' + q] = abs(c['r' + q]) <= c['B_q' + q]
        with io.open(CELLS, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(c) + NL)
        if c['ceiling']:
            print('  %3d a=%-10.6f nv %d CEILING' % (k, c['a'], c['nv']), flush=True)
            continue
        print('  %3d a=%-10.6f nv %-5d img %-8.0f m %+.6e |r| %.2e B %.2e %-14s | Q325 m %+.4f |r| %.1e %s | Qd m %+.4f |r| %.1e %s  %.0fs'
              % (k, c['a'], c['nv'], c['image'], c['m'], abs(c['r']), c['B_z'], c['kind'], c['m325'], abs(c['r325']),
                 'V' if c['verified_q325'] else '-', c['md'], abs(c['rd']), 'V' if c['verified_qd'] else '-', c['seconds']), flush=True)


def report():
    rs = sorted((json.loads(l) for l in io.open(CELLS, encoding='utf-8') if l.strip()), key=lambda r: r['a'])
    fx = json.loads(io.open(os.path.join(D, 'b504_fixture.json'), encoding='utf-8').read())
    ver = [r for r in rs if r['verified']]
    unv = [r for r in rs if not r['verified']]
    maxnv = max(r['nv'] for r in rs)
    price = max((r['seconds'] for r in rs if r['nv'] == maxnv), default=0)
    L = ['=' * 104, 'COMPONENTS 1 TO 4 -- THE CHAIN ON ONE TRANSFORM.', '=' * 104,
         '    fixture at three verified cells, b503 reproduced to 1e-12 : %s' % fx['passes'],
         '    nv used : %d distinct, from %d to %d ; cells above 8193 : %d ; price at the largest nv : %.0f s a cell'
         % (len({r['nv'] for r in rs}), min(r['nv'] for r in rs), maxnv, sum(r['nv'] > 8193 for r in rs), price),
         '    cells at the ceiling : %d' % sum(r['ceiling'] for r in rs),
         '    compute : %.0f s' % sum(r['seconds'] for r in rs),
         '', '### COMPONENT 2.', '-' * 104,
         '    ### ### **VERIFIED ON THE CONSISTENT RESIDUAL : %d OF %d**' % (len(ver), len(rs)),
         '    ### every unverified cell, with its kind:']
    for r in unv:
        L.append('      a=%-10.6f nv %-5d  |r| %.3e  B %.3e  x%-7.3g %s' % (r['a'], r['nv'], abs(r.get('r', float('nan'))),
                                                                      r.get('B_z', float('nan')), abs(r.get('r', 0)) / r.get('B_z', 1), r['kind']))
    eight = [r for r in rs if r['a'] >= 13.63]
    L.append('    ### the eight cells from a = 13.637 : %s' % ['%.3f nv %d img %.0f %s' % (r['a'], r['nv'], r['image'], r['kind']) for r in eight])
    ext_named = {}
    for a0 in (4.061553, 5.196152, 13.152946):
        r = min(rs, key=lambda x: abs(x['a'] - a0))
        ext_named[str(a0)] = r['kind']
        L.append('    extremum a = %s : |r| %.3e B %.3e ### **%s**' % (a0, abs(r['r']), r['B_z'], r['kind']))
    xs, ys = [r['a'] for r in ver], [r['m'] for r in ver]
    ex = BZ.extrema(xs, ys)
    L += ['', '### COMPONENT 3 -- THE TAIL AND THE ATTRIBUTION, ON THE VERIFIED SET.', '-' * 104]
    for t, k in ex:
        L.append('    %s  a=%.6f  m=%+.9f' % (t, xs[k], ys[k]))
    # ### ### **REPAIRED: THE FIRST VERSION TESTED `a > 13.152946 + 1e-9`, AND THE CELL`S EXACT a IS
    # ### 13.152946437..., SO THE MINIMUM COUNTED AS THE FIRST CELL `AFTER` ITSELF** and the strict rise
    # ### failed against its own value. ### The minimum`s cell is now located, and `after` starts past it.
    c13 = min(ver, key=lambda r: abs(r['a'] - 13.152946))
    after = [r for r in ver if r['a'] > c13['a']]
    base13 = c13['m']
    rise = bool(after) and base13 is not None and all(after[k + 1]['m'] > after[k]['m'] for k in range(len(after) - 1)) and after[0]['m'] > base13
    L.append('    verified cells after 13.152946 : %d ; ### **THE RISE STANDS : %s**' % (len(after), rise))
    fits = {}
    for name, g in BZ.FORMS:
        c, rms = BZ.fit(xs, ys, g)
        fits[name] = dict(c=c, rms=rms)
        L.append('    %-12s rms %.6e over %d verified cells' % (name, rms, len(ver)))
    win = min(fits, key=lambda k: fits[k]['rms'])
    L.append('    ### least residual : %s' % win)
    zex = [BZ.extrema(xs, [r['low5'][j] for r in ver]) for j in range(5)]
    match = {}
    for t, k in ex:
        hits = ['z%d %.4f' % (j + 1, GAM[j]) for j in range(5) if any(abs(kk - k) <= 1 for _, kk in zex[j])]
        match['%s %.6f' % (t, xs[k])] = hits
        L.append('    m`s %s at a=%.6f : zero terms with an extremum within one cell : ### **%s**' % (t, xs[k], hits or 'NONE'))
    L += ['', '### COMPONENT 4 -- THE EPSTEIN CONTROL, ONE TRANSFORM, TWO KERNELS.', '-' * 104,
          '    Epstein bank : %d on-line zeros to %.3f + %d off-line ; the grid rule on its T is met at every cell.'
          % (GQ.size, TOPQ, len(LIB['offline']))]
    eps = {}
    for q, name in (('325', 'b325 kernel (CONTROL OF RECORD)'), ('d', 'b326 derived kernel (BESIDE)')):
        vq = [r for r in rs if not r['ceiling'] and r['verified_q' + q]]
        mm = [r['m' + q] for r in rs if not r['ceiling']]
        bad = [r for r in vq if not (r['m' + q] > 0 and r['m' + q] > r['B_q' + q])]
        mn = min((r for r in rs if not r['ceiling']), key=lambda r: r['m' + q])
        eps[q] = dict(verified=len(vq), n4_fail=len(bad), min_m=mn['m' + q], min_a=mn['a'],
                      max_abs_r=max(abs(r['r' + q]) for r in rs if not r['ceiling']),
                      min_abs_r=min(abs(r['r' + q]) for r in rs if not r['ceiling']))
        L.append('    %-34s verified %3d of %d ; |r| from %.2e to %.2e ; smallest margin %+.6f at a = %.6f ; among verified, margin not above floor at %d'
                 % (name, len(vq), len(rs), eps[q]['min_abs_r'], eps[q]['max_abs_r'], mn['m' + q], mn['a'], len(bad)))
        if not vq:
            L.append('      ### ### **NO CELL VERIFIES UNDER THIS KERNEL -- (N4) ON IT IS VACUOUS.**')
    L.append('=' * 104)
    io.open(os.path.join(D, 'b504_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        io.open(os.path.join(D, 'b504_fixture.txt'), encoding='utf-8').read() + NL.join(L) + NL)
    json.dump(dict(n=len(rs), verified=len(ver), unverified=[dict(a=r['a'], kind=r['kind']) for r in unv],
                   eight=[dict(a=r['a'], nv=r['nv'], image=r['image'], kind=r['kind']) for r in eight],
                   ext_named=ext_named, extrema=[dict(t=t, a=xs[k]) for t, k in ex], rise=rise, after13=len(after),
                   fits=fits, win=win, match=match, eps=eps, maxnv=maxnv, price=price,
                   seconds=sum(r['seconds'] for r in rs)),
              io.open(os.path.join(D, 'b504_results.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'cells':
        sys.exit(cells(int(sys.argv[2]), int(sys.argv[3])))
    if cmd == 'kernels':
        kernels()
        sys.exit(0)
    sys.exit({'fixture': fixture, 'report': report}[cmd]())
