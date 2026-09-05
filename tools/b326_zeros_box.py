# -*- coding: utf-8 -*-
"""b326_zeros_box.py -- THE ONE BOX WHOSE WINDING EXCEEDED ITS SIGN-CHANGE COUNT, RESOLVED.

### ### **`t in [145.5, 146.0]`: winding `2.000`, sign changes `0`.** ### Two readings are possible
### and the registered procedure names only one of them (an off-line pair within `delta = 0.02`),
### so BOTH are tested: ### (a) the line is re-scanned at a step twenty times finer -- two on-line
### zeros closer than `0.1` give an even number of sign changes inside one scan step and are
### invisible to the coarse scan; ### (b) if (a) finds nothing, a two-dimensional root search from
### inside the box on both routes. ### Whatever is found is APPENDED to the library with a flag that
### says which reading it was, and the box's record is updated; the original library is kept beside
### it under a different name. ### **NOTHING IS OVERWRITTEN.**
"""
import io
import json
import os
import shutil
import sys

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import epstein_census as CE     # noqa: E402
import b326_zeros as BZ         # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
LIB = os.path.join(D, 'b326_epstein_zeros.json')
LIB_BEFORE = os.path.join(D, 'b326_epstein_zeros_before_box.json')
OUT = os.path.join(D, 'b326_zeros_box_run.txt')
FINE = 0.005


def main():
    lines = []

    def rec(s=''):
        lines.append(s)
        print(s, flush=True)

    lib = json.load(io.open(LIB, encoding='utf-8'))
    BZ.bind(lib['dps'], lib['K'])
    bad = [b for b in lib['boxes'] if int(round(b['wind'])) != b['sign_changes']]
    rec('=' * 100)
    rec('b326 -- THE MISMATCHED BOX, RESOLVED. ### boxes with winding != sign changes : %d' % len(bad))
    rec('=' * 100)
    if not bad:
        rec('  nothing to resolve.')
        io.open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 0
    if not os.path.exists(LIB_BEFORE):
        shutil.copyfile(LIB, LIB_BEFORE)
    added = []
    for b in bad:
        t_lo, t_hi = b['t_lo'], b['t_hi']
        rec('  box t in [%.1f, %.1f]  winding %.3f  sign changes %d' % (t_lo, t_hi, b['wind'], b['sign_changes']))
        # ### (a) the fine scan.
        pts = []
        t = t_lo
        while t <= t_hi + 1e-12:
            h, _ = BZ.H(t)
            pts.append((t, float(h)))
            t = round(t + FINE, 6)
        br = [(ta, tb) for (ta, ha), (tb, hb) in zip(pts, pts[1:]) if (ha < 0) != (hb < 0)]
        rec('    (a) fine scan at step %g : %d points, %d sign change(s) %s' % (FINE, len(pts), len(br), br))
        found = []
        for (ta, tb) in br:
            ga = float(mp.findroot(lambda x: BZ.H(x)[0], (mp.mpf(ta), mp.mpf(tb)), solver='anderson', tol=mp.mpf('1e-24')))
            gb = float(mp.findroot(lambda x: BZ.hardy_b(x)[0], (mp.mpf(ta), mp.mpf(tb)), solver='anderson', tol=mp.mpf('1e-24')))
            found.append(dict(bracket=[ta, tb], gamma_a=ga, gamma_b=gb, route_b='bracket',
                              agree=abs(ga - gb) <= BZ.ROUTE_TOL, reading='on-line pair inside one coarse step'))
            rec('      on-line zero  route A %.12f  route B %.12f  agree %s' % (ga, gb, abs(ga - gb) <= BZ.ROUTE_TOL))
        if len(found) < int(round(b['wind'])):
            # ### (b) the two-dimensional search.
            for s0 in (mp.mpc(0.51, (t_lo + t_hi) / 2), mp.mpc(0.515, t_lo + 0.15), mp.mpc(0.515, t_hi - 0.15)):
                try:
                    za = mp.findroot(lambda z: CE.Lam(z), s0, solver='secant', tol=mp.mpf('1e-24'))
                    zb = mp.findroot(lambda z: BZ.zq_b(z), za, solver='secant', tol=mp.mpf('1e-24'))
                except Exception as e:
                    rec('      2-D search from %s failed: %s' % (s0, e))
                    continue
                inside = (t_lo <= float(za.imag) <= t_hi) and abs(float(za.real) - 0.5) <= BZ.DELTA
                rec('      2-D search from %s : rho_A = %s  rho_B = %s  inside the box %s'
                    % (s0, za, zb, inside))
                if inside and abs(float(za.real) - 0.5) > 1e-9:
                    lib.setdefault('offline_near_line', []).append(
                        dict(rho_a=[float(za.real), float(za.imag)], rho_b=[float(zb.real), float(zb.imag)],
                             agree=abs(za - zb) <= BZ.ROUTE_TOL, reading='off-line within delta of the line'))
        added.extend(found)
        b['sign_changes'] = b['sign_changes'] + len(found)
        b['resolved_by'] = 'fine scan' if found else '2-D search'
    lib['zeros'] = sorted(lib['zeros'] + added, key=lambda z: z['gamma_a'])
    lib['box_mismatches'] = sum(1 for b in lib['boxes'] if int(round(b['wind'])) != b['sign_changes'])
    lib['box_resolution'] = dict(fine_step=FINE, added_on_line=len(added),
                                 added_off_line_near=len(lib.get('offline_near_line', [])))
    open(LIB + '.tmp', 'wb').write((json.dumps(lib, indent=1) + '\n').encode('utf-8'))
    os.replace(LIB + '.tmp', LIB)
    rec('  on-line zeros now %d ; box mismatches now %d ; the pre-resolution library kept as %s'
        % (len(lib['zeros']), lib['box_mismatches'], os.path.basename(LIB_BEFORE)))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return 0 if lib['box_mismatches'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
