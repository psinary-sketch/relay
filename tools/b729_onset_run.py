# -*- coding: utf-8 -*-
"""b729_onset_run.py -- (R339)(7): THE ONSETS OF H-ONSET-C, BY b707'S ROUTE AS tools/b725_onset_mass.py `run` COMPUTES IT, IMPORTED UNEDITED.

### THREE BINDINGS, AND ONLY THREE, EACH MADE HERE AT MODULE LEVEL SO THE SPAWNED WORKERS CARRY THEM (spawn re-imports this file):
###   (1) THE UNITS: data/b729_onset_units.jsonl, seeded once from b725's committed units, so that its coarse rungs and (C1) are read and not re-run, and b725's bank is not written.
###   (2) THE PREDICTION: `selected` returns data/b729_onset_pred.txt's a*_pred, not b725's, so that the route's printed deviation is this registration's.
###   (3) THE RUNG 256, above b707's ladder, the registration's :16 and :31: entered in O7.RUNG_W, S.WIDTH and S.LADDER.
### Routes: run <off24|off44> [--workers n] [--budget s]    one call of the route, resumable; call again until it prints THE ONSET or BEYOND REACH
###         state                                            the highest point read positive at each zero, against the window
###         score [--bank]                                   the registration's verdict; banks data/b729_onset_score.txt
### Written by the Write tool at b729. Every figure is the route's. Nothing here proves RH or GRH.
"""
import io
import math
import os
import re
import shutil
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b725_onset_mass as M       # noqa: E402  ### imported unedited; its module level binds S.UNITS to b725's file, rebound on the next lines
import b723_support as S          # noqa: E402
import b707_onset as O7           # noqa: E402

UNITS = os.path.join(D, 'b729_onset_units.jsonl')
SEED = os.path.join(D, 'b725_onset_mass_units.jsonl')
PRED = os.path.join(D, 'b729_onset_pred.txt')
SCORE = os.path.join(D, 'b729_onset_score.txt')
M.UNITS = UNITS
S.UNITS = UNITS
O7.RUNG_W['256'] = '256'
S.WIDTH['256'] = '256'
if '256' not in S.LADDER:
    S.LADDER.append('256')
FALSIFIER = 0.05


def predictions():
    """{name: a*_pred} from the predictions bank, each read under its zero's own heading."""
    name, out = None, {}
    for l in io.open(PRED, encoding='utf-8'):
        m = re.search(r'\b(off44|off24)\b', l)
        if m and 'a*_pred' not in l:
            name = m.group(1)
        m = re.match(r'\s+a\*_pred ([\d.]+) ; bisected', l)
        if m:
            out[name] = float(m.group(1))
    assert sorted(out) == ['off24', 'off44'], out
    return out


_selected = M.selected


def selected():
    P = predictions()
    return dict((k, (v[0], v[1], P[k])) for k, v in _selected().items() if k in P)


M.selected = selected


def seed():
    if not os.path.exists(UNITS):
        shutil.copyfile(SEED, UNITS)
        print('### the units seeded from data/b725_onset_mass_units.jsonl')


def state(*a):
    U = M.units()
    P = predictions()
    res = {}
    for z in ('off24', 'off44'):
        o = next((u for k, u in U.items() if k[0] == 'onset' and k[1] == z), None)
        rows = [u for k, u in U.items() if k[0] == 'fine' and k[1] == z and k[2] == 'C' and k[4] == 'q0']
        tops = [float(M.bl(u['a_radius']).mid()) for u in rows]
        res[z] = dict(onset=o, top=max(tops) if tops else None, n=len(rows), pred=P[z])
        print('  %s a*_pred %.6f ; window [%.6f, %.6f] ; fine points read %d ; highest a read %s ; onset %s' % (
            z, P[z], P[z] * (1 - FALSIFIER), P[z] * (1 + FALSIFIER), len(rows), ('%.6f' % max(tops)) if tops else 'none', ('%s' % o.get('point')) if o else 'none'))
    return res


def score(*argv):
    res = state()
    L = ['b729 -- (R339)(7): H-ONSET-C SCORED, BY THE REGISTRATION`S OWN VERDICT (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### by tools/b729_onset_run.py; b707`s route as tools/b725_onset_mass.py `run` computes it, imported unedited; the registration data/b729_registrations.txt at relay d1f94c17; the predictions at acf699c0.',
         '### SCOPE: fitted on five, tested on two; a HELD is two points, not a law.',
         '### off24`s WEIGHT: its whole banked bracket lay inside its 5% window (data/b729_onset_pred.txt), so its onset could not fire the falsifier; its 0.2% is a closeness, not a test passed.',
         '### off44`s STOP: the rule of the registration (A BOUND) fired at a read of a = 10.615236; the calls went on to tighten the bound and were stopped at point 1321 of 5295, the guard refusing and the trend putting the onset near point 3100, past the 06:20Z cap the seat had set; off44`s onset is NOT computed.', '']
    held, refuted, open_ = [], [], []
    for z in ('off24', 'off44'):
        r = res[z]
        o = r['onset']
        if o and o.get('a') is not None:
            a = float(M.bl(o['a']).mid())
            dev = a / r['pred'] - 1
            ok = abs(dev) <= FALSIFIER
            L.append('  %s the onset at %s, a = %.9f ; a*_pred %.6f ; a*/a*_pred - 1 = %+.5f ; %s' % (z, o['point'], a, r['pred'], dev, 'WITHIN 0.05' if ok else 'BEYOND 0.05'))
            (held if ok else refuted).append(z)
        elif r['top'] is not None and r['top'] / r['pred'] - 1 > FALSIFIER:
            L.append('  %s no onset computed; positive to a = %.6f, so a*/a*_pred - 1 > %+.5f ; REFUTED BY THE BOUND' % (z, r['top'], r['top'] / r['pred'] - 1))
            refuted.append(z)
        else:
            L.append('  %s no onset computed ; a bound, NOT SCORABLE, never a confirmation' % z)
            open_.append(z)
    if refuted:
        v = 'REFUTED'
    elif len(held) == 2:
        v = 'HELD at 2'
    elif held:
        v = 'CARRIED, HELD AT ONE'
    else:
        v = 'CARRIED'
    L += ['', '### ### **H-ONSET-C %s ; ONSETS COMPUTED %d ; WITHIN 0.05: %s ; BEYOND: %s ; OPEN: %s.**' % (v, len(held) + sum(1 for z in refuted if res[z]['onset']), held or 'none', refuted or 'none', open_ or 'none')]
    print(NL.join(L))
    if '--bank' in argv:
        with open(SCORE, 'w', encoding='utf-8', newline='') as fh:
            fh.write(NL.join(L) + NL)
        print('### banked', os.path.relpath(SCORE, ROOT))


if __name__ == '__main__':
    A = sys.argv[1:]
    if not A:
        sys.exit(__doc__)
    if A[0] == 'run':
        seed()
        M.run(*A[1:])
    elif A[0] == 'state':
        state()
    elif A[0] == 'score':
        score(*A[1:])
    else:
        sys.exit('### no route ' + A[0])
