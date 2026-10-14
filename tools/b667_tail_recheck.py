# -*- coding: utf-8 -*-
"""b667_tail_recheck.py -- THE (3d) CHECK'S NOT DECIDED POINT RE-READ, under the navigator's note on the b667 progress report (no new clause).

### At (σ, t) = (1.5, 40.0) the (3d) check read the terms M + 1 ... 2M, summed directly at 800 bits, as NOT DECIDED: their ball's floor
### (about 6e-73) above T4's bound (2.7199e-83). The note: where one point at a precision placing the floor beneath the bound costs under the
### foreground limit, it is re-run at that precision after the squares complete and before Component 4, its reading printed beneath the NOT
### DECIDED line; where it does not, NOT DECIDED stands and is declared on the face.
### This tool takes the same point, the same ball (radius 1e-6) for M and T4's bound (tools/b667_epstein_certify.py's own M_of, t4_bound and
### tail_sum, imported, unedited), and sums the tail directly at 1200, 1600, 2400 and 3200 bits in turn, stopping at the first whose floor
### lies beneath the bound or when the next step would pass the 600 s foreground limit; each step's ball, bound, reading and seconds printed.
### It inserts its lines beneath the NOT DECIDED line of data/b667_epstein_counts.txt (this act's bank, before the seal) and banks them as
### data/b667_tail_recheck.txt. Usage: `python -X utf8 tools/b667_tail_recheck.py`. Written by the Write tool at b667.
"""
import io
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, acb, ctx       # noqa: E402
import b667_epstein_certify as C      # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
LIMIT = 600
PRECS = (1200, 1600, 2400, 3200)
SG, TT, R = '1.5', '40.0', '1e-6'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main():
    t_all = time.time()
    ctx.prec = C.PREC
    bl = acb(arb(SG, R), arb(TT, R))
    Mb = C.M_of(C._tmax(bl), C.PREC)
    tb = C.t4_bound(bl, Mb)
    L = ['  ### RE-READ (the navigator`s note, %s): the terms M + 1 ... 2M at (σ, t) = (%s, %s), M %d, summed directly; T4`s bound at the ball %s' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), SG, TT, Mb, tb.str(5, radius=False))]
    state, last = 'NOT DECIDED', 0.0
    for p in PRECS:
        if time.time() - t_all + 2 * last > LIMIT:
            L.append('  ###   %d bits not run: the next step would pass the %d s foreground limit' % (p, LIMIT))
            break
        t0 = time.time()
        ctx.prec = p
        pt = acb(arb(SG), arb(TT))
        tl = abs(C.tail_sum(pt, p, Mb + 1, 2 * Mb))
        last = time.time() - t0
        ctx.prec = C.PREC
        state = 'BELOW' if tl.upper() <= tb else ('ABOVE' if tl.lower() > tb else 'NOT DECIDED')
        L.append('  ###   at %d bits: the tail %s against the bound %s : %s (%.1f s)' % (p, tl.str(5, radius=True), tb.str(5, radius=False), state, last))
        if state != 'NOT DECIDED':
            break
    L.append('  ###   THE RE-READ: %s%s' % (state, '' if state != 'NOT DECIDED' else ' -- it stands, declared on the face'))
    p = os.path.join(D, 'b667_epstein_counts.txt')
    t = io.open(p, encoding='utf-8').read()
    if 'RE-READ (the navigator' in t:
        sys.exit('### THE RE-READ IS ALREADY BENEATH THE LINE -- NOTHING WRITTEN')
    ls = t.split(NL)
    i = next((k for k, l in enumerate(ls) if l.startswith('  (σ, t) = (%s, %s) :' % (SG, TT)) and l.rstrip().endswith('NOT DECIDED')), None)
    if i is None:
        sys.exit('### THE NOT DECIDED LINE IS NOT IN THE COUNTS BANK -- NOTHING WRITTEN')
    ls[i + 1:i + 1] = L
    b = NL.join(ls).encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    q = os.path.join(D, 'b667_tail_recheck.txt')
    head = 'b667 -- THE (3d) CHECK`S NOT DECIDED POINT RE-READ (the navigator`s note); its lines, as inserted beneath the line in data/b667_epstein_counts.txt'
    open(q + '.tmp', 'wb').write((NL.join([head, ''] + L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    main()
