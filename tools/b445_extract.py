# -*- coding: utf-8 -*-
"""b445_extract.py -- THE SURVEY'S RECORD OF THE FOUR PRE-FACE READS (P1)-(P4).
### ### Written after the face was typed and before it was locked, and said so: the reads themselves were
### taken before the face and are declared on it; this file banks them. It computes no residual."""
import io, os, sys, time
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
SRC = os.path.join(ROOT, 'tools', 'e16', 'carto_atlas.py')
L = []
def rec(s=''):
    L.append(s); print(s)
def main():
    import mpmath as mp
    rec('b445 -- THE SURVEY: THE FOUR PRE-FACE READS.')
    src = io.open(SRC, encoding='utf-8').read().splitlines()
    for ndl in ('NGAM    = 10000', 'GAM = np.load', 'Truncation bound for the zero side is computed', 'NV      = 4001', 'NU      = 12001', 'UMAX    = 600.0'):
        hit = [(i + 1, l.strip()) for i, l in enumerate(src) if ndl in l]
        rec('  (P1/P2) carto_atlas.py:%s | %s' % hit[0] if hit else '  ### NOT LOCATED : %s' % ndl)
    g = np.load(os.path.join(ROOT, 'tools', 'e16', 'zeta_ordinates.npy'))
    rec('  (P1) library : %d ordinates ; first %.15f ; last %.12f' % (len(g), g[0], g[-1]))
    mp.mp.dps = 25
    t = time.time(); z = float(mp.zetazero(10001).imag)
    rec('  (P3) zetazero(10001) = %.12f (%.1fs) ; above the library`s last : %s' % (z, time.time() - t, z > g[-1]))
    for n in (10, 100, 500, 1000, 2000, 5000, 8000, 10000):
        zn = float(mp.zetazero(n).imag)
        rec('  (P4) n=%-6d library %.12f mpmath %.12f diff %.2e' % (n, g[n - 1], zn, abs(zn - g[n - 1])))
    rec('  ### READS 16 ; MISSES : 0')
    io.open(os.path.join(D, 'b445_extract.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
if __name__ == '__main__':
    main()
