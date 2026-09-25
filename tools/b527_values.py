# -*- coding: utf-8 -*-
"""b527_values.py -- COMPONENT 3: THE CONCRETE PLATEAU`S VALUES, TWO WAYS. ### `python tools/b527_values.py`

### `phi_chain(u, a)` is THE CHAIN`S FORMULA, the one b528 imports: `smoothTransition((L - |u|) / (F L))`, F = 1/4, L = log a,
### in double precision. ### `phi_kernel_mp(u, a)` is THE KERNEL`S DEFINITION AS WRITTEN -- the product
### `smoothTransition((L - u) / (F L)) * smoothTransition((L + u) / (F L))`, `smoothTransition x = e(x) / (e(x) + e(1 - x))`,
### `e(x) = exp(-1/x)` for x > 0 and 0 else -- in mpmath at 50 digits, outside Lean. ### Twenty points across the ramp
### u in [(1 - F) L, L] at a = 34 (and their mirror images), the largest absolute difference against 1e-14.
"""
import io
import json
import math
import os
import sys

import mpmath as mp
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
F = 0.25
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def smooth_transition(x):
    x = np.asarray(x, dtype=float)
    a = np.where(x > 0, np.exp(-1.0 / np.where(x > 0, x, 1.0)), 0.0)
    b = np.where(1 - x > 0, np.exp(-1.0 / np.where(1 - x > 0, 1 - x, 1.0)), 0.0)
    return a / (a + b)


def phi_chain(u, a):
    L = math.log(a)
    return smooth_transition((L - np.abs(np.asarray(u, dtype=float))) / (F * L))


def phi_kernel_mp(u, a):
    mp.mp.dps = 50
    L = mp.log(mp.mpf(a))
    u = mp.mpf(u)
    FL = mp.mpf(F) * L

    def e(x):
        return mp.exp(-1 / x) if x > 0 else mp.mpf(0)

    def st(x):
        return e(x) / (e(x) + e(1 - x))
    return st((L - u) / FL) * st((L + u) / FL)


def main(a=34.0):
    L = math.log(a)
    us = [(1 - F) * L + F * L * (k + 0.5) / 20.0 for k in range(20)]
    rows = []
    for u in us + [-x for x in us]:
        c = float(phi_chain(u, a))
        k = phi_kernel_mp(u, a)
        rows.append(dict(u=u, chain=c, kernel=float(k), kernel_str=mp.nstr(k, 20), diff=abs(c - float(k))))
    extra = dict(flat=float(phi_chain(0.5 * (1 - F) * L, a)), outside=float(phi_chain(1.01 * L, a)),
                 flat_mp=float(phi_kernel_mp(0.5 * (1 - F) * L, a)), outside_mp=float(phi_kernel_mp(1.01 * L, a)))
    res = dict(a=a, L=L, F=F, rows=rows, max_diff=max(r['diff'] for r in rows), agree=max(r['diff'] for r in rows) <= 1e-14, checks=extra)
    io.open(os.path.join(D, 'b527_values.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('  a = %.0f, L = %.6f ; ramp u in [%.6f, %.6f]' % (a, L, (1 - F) * L, L))
    for r in rows[:20]:
        print('    u=%9.6f  chain %.17f  kernel(mp) %s  |diff| %.1e' % (r['u'], r['chain'], r['kernel_str'], r['diff']))
    print('  ### mirror points agree too ; max |diff| over 40 points %.2e -- within 1e-14 : %s ; flat %s, outside %s'
          % (res['max_diff'], res['agree'], extra['flat'], extra['outside']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
