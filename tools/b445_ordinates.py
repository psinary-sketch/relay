# -*- coding: utf-8 -*-
"""b445_ordinates.py -- ARM (b)'S EXTENSION OF THE ZERO LIBRARY'S REACH. ### **UNDER (R57).**
### `mpmath.zetazero(n)` for n = 10001 ... 15000 at 25 digits, in parallel; banked as
### `data/b445_ordinates_10001_15000.npy`. `tools/e16/zeta_ordinates.npy` is NOT edited.
### These are mpmath's ordinates and are claimed to be nothing more."""
import io
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b445_ordinates_10001_15000.npy')
RUN = os.path.join(D, 'b445_ordinates_run.txt')
LO, HI = 10001, 15000


def one(n):
    import mpmath as mp
    mp.mp.dps = 25
    return n, float(mp.zetazero(n).imag)


def main():
    t0 = time.time()
    with Pool(10) as p:
        res = dict(p.imap_unordered(one, range(LO, HI + 1), chunksize=20))
    arr = np.array([res[n] for n in range(LO, HI + 1)])
    lib = np.load(os.path.join(ROOT, 'tools', 'e16', 'zeta_ordinates.npy'))
    inc = bool(np.all(np.diff(arr) > 0))
    above = bool(arr[0] > lib[-1])
    np.save(OUT, arr)
    lines = ['b445_ordinates.py -- n = %d ... %d at 25 digits' % (LO, HI),
             '  count %d ; first %.12f ; last %.12f' % (len(arr), arr[0], arr[-1]),
             '  control: first above the library`s last (%.12f) : %s' % (lib[-1], above),
             '  control: strictly increasing : %s' % inc,
             '  CONTROL : %s' % ('PASS' if (above and inc and len(arr) == HI - LO + 1) else 'FAIL'),
             '  wall seconds : %.0f' % (time.time() - t0)]
    io.open(RUN, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
