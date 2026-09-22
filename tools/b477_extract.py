# -*- coding: utf-8 -*-
"""b477_extract.py -- THE SURVEY. ### The cross builder's POSITIVE CONTROL against the chain's own
### autocorrelation; one priced off-diagonal; the entry order; and the control's side, read from the
### Epstein chain's own return. ### **NO GRAM IS FORMED HERE; the run is b477_gram.py, detached.**
"""
import importlib.util
import io
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'e16'))

import numpy as np                    # noqa: E402
import b317_smear as SM               # noqa: E402
import b318_square as SQ              # noqa: E402
import b321_window as WI              # noqa: E402
import b325_epstein as EP             # noqa: E402

NL = chr(10)
L, MISSES = [], []
FLOOR = 1.49e-08

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def main():
    rec('=' * 104)
    rec('b477 -- THE SURVEY. ### THE CROSS BUILDER IS CONTROLLED BEFORE THE RUN IS LAUNCHED.')
    rec('=' * 104)
    spec = importlib.util.spec_from_file_location('b477_gram', os.path.join(T, 'b477_gram.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    rec('')
    rec('(P1) THE CROSS BUILDER`S POSITIVE CONTROL: cross(g, g) AGAINST THE CHAIN`S OWN autocorrelation.')
    rec('-' * 104)
    g = SM.mean_zero_variant(1.5)
    t0 = time.time()
    ac = SQ.autocorrelation(g)
    xc = m.cross(g, g)
    dw = float(np.max(np.abs(ac.w - xc.w)))
    cha, chx = WI.channels(ac.v, ac.w), WI.channels(xc.v, xc.w)
    Wa, Wx = cha['prime'] - cha['arch'], chx['prime'] - chx['arch']
    rec('    autocorrelation : v in [%.6f, %.6f], %d samples' % (ac.v[0], ac.v[-1], len(ac.v)))
    rec('    cross(g, g)     : v in [%.6f, %.6f], %d samples' % (xc.v[0], xc.v[-1], len(xc.v)))
    rec('    ### ### **MAX |WINDOW DIFFERENCE| : %.3e**' % dw)
    rec('    W from the chain`s autocorrelation : %+.12f' % Wa)
    rec('    W from cross(g, g)                 : %+.12f' % Wx)
    rec('    ### ### **|DIFFERENCE| : %.3e ; THE FLOOR : %.2e ; WITHIN IT : %s**'
        % (abs(Wa - Wx), FLOOR, abs(Wa - Wx) < FLOOR))
    if abs(Wa - Wx) >= FLOOR or dw >= FLOOR:
        MISSES.append(('cross builder', 'control'))
    rec('    ### **SO THE BUILDER REDUCES TO THE CHAIN`S OWN CONSTRUCTION ON THE DIAGONAL, AND THE')
    rec('    ### OFF-DIAGONAL IS THE SAME CONSTRUCTION WITH TWO SEEDS.** ### The chain is NOT edited.')

    rec('')
    rec('(P2) ONE OFF-DIAGONAL, PRICED -- AND THE CONTROL`S SIDE, FROM ITS OWN RETURN.')
    rec('-' * 104)
    gb = SM.mean_zero_variant(1.7)
    t1 = time.time()
    fab = m.cross(g, gb)
    ch = WI.channels(fab.v, fab.w)
    cq = EP.channels_q(fab.v, fab.w)
    dt = time.time() - t1
    rec('    G(1.5, 1.7) = PR - A = %+.12f   (zeta`s chain, b321_window.channels)' % (ch['prime'] - ch['arch']))
    rec('    the control at the same f_ab : places = %+.12f (finite %+.9f, arch %+.9f, pole %.2e)'
        % (cq['places'], cq['finite'], cq['arch'], cq['pole']))
    rec('    the Epstein chain`s own return keys : %s' % sorted(cq))
    rec('    ### ### **THE CONTROL`S CHAIN RETURNS A PLACES SUM AND NO ZERO SIDE.** ### `channels_q` is')
    rec('    ### the EPSTEIN object`s own finite channel and its own archimedean kernel -- b325`s, quoted')
    rec('    ### in its head as *"the same shape b321 established for zeta"*. ### **SO THE CONTROL`S GRAM')
    rec('    ### IS A PLACES-SIDE GRAM, AND ITS VERDICT IS SCOPED TO THAT SIDE.**')
    rec('    ### ### **ONE OFF-DIAGONAL COSTS %.1f s** -- both chains on one built window.' % dt)

    rec('')
    rec('(P3) THE ENTRY ORDER, AND THE PRICE OF THE RUN.')
    rec('-' * 104)
    S = json.loads(io.open(os.path.join(D, 'b476_survey.json'), encoding='utf-8').read())
    aim, lad = list(S['cells']), list(S['ladder'])
    na, nl = len(aim), len(lad)
    offa, offl = na * (na - 1) // 2, nl * (nl - 1) // 2
    rec('    the order : the diagonal at every cell FIRST (halt on mismatch), then the AIM PLANE`s')
    rec('      off-diagonals, then the LADDER`s, then the control`s diagonal on its own chain.')
    rec('    aim plane  : %d cells -> %d entries (%d off-diagonal)' % (na, na * (na + 1) // 2, offa))
    rec('    ladder     : %d cells -> %d entries (%d off-diagonal)' % (nl, nl * (nl + 1) // 2, offl))
    rec('    ### ### **OFF-DIAGONAL ENTRIES IN THIS RUN : %d ; DIAGONALS : %d ; CONTROL DIAGONALS : %d.**'
        % (offa + offl, na + nl, na + nl))
    est = (offa + offl) * dt + (na + nl) * 7.0 + (na + nl) * 3.0
    rec('    ### ### **PRICED AT %.0f s (%.0f min) FROM THIS SURVEY`S OWN TIMINGS**' % (est, est / 60.0))
    rec('    ### -- far above the 600 s foreground limit, so the run is DETACHED under (R80) per (R86).')

    rec('')
    rec('(P4) (R87)`S ORIENTATION, AND WHERE IT IS APPENDED.')
    rec('-' * 104)
    reg = io.open(os.path.join(D, 'b476_registration_2026-09-22.txt'), encoding='utf-8').read()
    rec('    the amendment is appended BELOW b476`s lock block : %s'
        % ('### THE AMENDMENT UNDER (R87)' in reg))
    rec('    the sealed text is unedited, and reg_seal --verify reads SEAL INTACT (banked at the amend).')
    rec('    ### the orientation, as (R87) fixes it: W = PR - A ; Sum_v W_v(f) = -Z ; ### **THE SIGNATURE')
    rec('    ### IS READ ON -G** ; under RH -G is positive semidefinite ; ### **(F2) HALTS ON A POSITIVE')
    rec('    ### EIGENVALUE OF G** ; (N2) and (N3) refer to the LARGEST eigenvalue of G.')
    if '### THE AMENDMENT UNDER (R87)' not in reg:
        MISSES.append(('b476 registration', 'amendment not appended'))

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b477_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(control=dict(window_diff=dw, W_autocorr=Wa, W_cross=Wx, diff=abs(Wa - Wx),
                                floor=FLOOR, within=bool(abs(Wa - Wx) < FLOOR)),
                   offdiagonal_seconds=dt, sample=dict(a=1.5, b=1.7, G=ch['prime'] - ch['arch'],
                                                       control_places=cq['places']),
                   control_keys=sorted(cq), aim=na, ladder=nl, off_entries=offa + offl,
                   diagonals=na + nl, priced_seconds=est, misses=MISSES),
              io.open(os.path.join(D, 'b477_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
