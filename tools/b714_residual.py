# -*- coding: utf-8 -*-
"""b714_residual.py -- (R324)(8), THE RESIDUAL, AN OBSERVATION: for the ten computed pairs, the onset minus the prediction under the -15
tool's evaluation (the first-order form with C per pair, data/b714_law.txt), against the navigator's figures 45.1, 44.9, 58.7, 70.3, 65.2,
64.3, 64.8, 137.3 at -15 and 59.4, 60.7 at Q0, each EQUAL or DIFFERS to one decimal; beside each, log n*, the mean spacing of prime powers
near n* and the step of the onset search, each from its bank or tool. No registration; no onset computed.

### the onsets and predictions: data/b713_onsets.json rows (the -15 pairs 1-8, n_star and n_pred) and c1 (Q0 pairs 11 and 15 at T0` 415 and
### 445, n_star and n_pred). The mean spacing: the prime powers p^k (k >= 1) counted by a sieve over [n* - W, n* + W], W = 50000, the
### spacing 2W / count. The step: tools/b709_pairs.py onset709 :153-:159 (`n += 1`), the route both -15 and Q0 ran.
### Routes: `bank [dry]` -> data/b714_residual.txt. Written by the Write tool at b714; it writes that bank alone. Run as `python -I -X utf8`.
"""
import ctypes
import hashlib
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
ACT = 'b714'
OUT = os.path.join(D, 'b714_residual.txt')
W = 50000
NAV = [('-15', 1, 45.1), ('-15', 2, 44.9), ('-15', 3, 58.7), ('-15', 4, 70.3), ('-15', 5, 65.2), ('-15', 6, 64.3), ('-15', 7, 64.8),
       ('-15', 8, 137.3), ('Q0', 11, 59.4), ('Q0', 15, 60.7)]          # ### the ferry (R324)(8), data/b714_ferry.txt :21
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def free_mb():
    class M(ctypes.Structure):
        _fields_ = [('l', ctypes.c_ulong), ('load', ctypes.c_ulong), ('tot', ctypes.c_ulonglong), ('avail', ctypes.c_ulonglong),
                    ('tp', ctypes.c_ulonglong), ('ap', ctypes.c_ulonglong), ('tv', ctypes.c_ulonglong), ('av', ctypes.c_ulonglong),
                    ('ae', ctypes.c_ulonglong)]
    m = M()
    m.l = ctypes.sizeof(M)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.avail // (1 << 20), m.tot // (1 << 20)


def mid(s):
    if isinstance(s, (int, float)):
        return float(s)
    return float(s.strip().strip('[]').split('+/-')[0])


def small_primes(m):
    s = bytearray([1]) * (m + 1)
    s[0:2] = b'\x00\x00'
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(m + 1) if s[i]]


def prime_powers_in(lo, hi):
    """the count of p^k (k >= 1) in [lo, hi]: primes by a segmented sieve, higher powers by enumeration."""
    ps = small_primes(int(hi ** 0.5) + 1)
    seg = bytearray([1]) * (hi - lo + 1)
    for p in ps:
        st = max(p * p, ((lo + p - 1) // p) * p)
        for j in range(st, hi + 1, p):
            seg[j - lo] = 0
    primes = sum(seg)
    powers = 0
    for p in ps:
        q = p * p
        while q <= hi:
            if q >= lo:
                powers += 1
            q *= p
    return primes, powers


def controls():
    """the sieve against known counts: pi(10^6) = 78498, so the primes in [2, 10^6]; the prime powers p^k, k >= 2, up to 100 (4, 8, 9, 16,
    25, 27, 32, 49, 64, 81) = 10; a NEG: a window of even numbers only cannot be read as primes (the count in [10^6, 10^6] is 0)."""
    p6, _ = prime_powers_in(2, 10 ** 6)
    _, k100 = prime_powers_in(2, 100)
    z, _ = prime_powers_in(10 ** 6, 10 ** 6)
    return [('(R1) POS primes in [2, 10^6] = 78498', p6 == 78498, p6), ('(R2) POS higher prime powers in [2, 100] = 10', k100 == 10, k100),
            ('(R3) NEG the even 10^6 is not prime (count 0)', z == 0, z)]


def bank(*a):
    t0 = time.time()
    fm, tm = free_mb()
    O = json.load(open(os.path.join(D, 'b713_onsets.json'), encoding='utf-8'))
    src = {('-15', r['k']): (r['n_star'], float(r['n_pred'])) for r in O['rows'] if r.get('n_star')}
    src.update({('Q0', u['idx']): (u['n_star'], mid(u['n_pred'])) for u in O['c1']})
    L = ['%s -- (R324)(8): THE RESIDUAL, AN OBSERVATION: THE ONSET MINUS THE PREDICTION UNDER THE -15 TOOL`S EVALUATION (%s)' % (ACT, utc()), '',
         '### free memory %d MB of %d MB before the run. The form: the first-order form with C per pair (data/b714_law.txt, THE READING TWO FORMS).' % (fm, tm),
         '### the onsets and predictions from data/b713_onsets.json (rows :6-:78, the -15 pairs; c1 :81-:115, Q0 at T0` 415 and 445); the',
         '### navigator`s figures from the ferry (data/b714_ferry.txt :21). The step of the onset search: tools/b709_pairs.py :159 (`n += 1`) in',
         '### onset709 :148-:160, the route b713`s -15 onsets and its Q0 (C1) both ran (b713_onsets.txt :4, :7). The spacing: the prime powers',
         '### p^k (k >= 1) over [n* - %d, n* + %d] by a sieve, the mean spacing 2W / count, printed beside log n*. NO ONSET COMPUTED.' % (W, W), '',
         '## I. THE SIEVE`S CONTROLS, BEFORE THE FIGURES']
    cs = controls()
    L += ['  %s : read %d -- %s' % (n, v, 'AS WANTED' if ok else 'NOT AS WANTED') for n, ok, v in cs]
    allok = all(ok for _n, ok, _v in cs)
    L += ['', '## II. THE TEN PAIRS: field | pair | n* (onset) | n*_pred | n* - n*_pred | the navigator`s | EQUAL/DIFFERS | log n* | primes + higher',
          '##     powers in the window | the mean prime-power spacing | the onset step']
    eq = 0
    res = []
    for f, k, nav in NAV:
        n, p = src[(f, k)]
        d = n - p
        same = ('%.1f' % d) == ('%.1f' % nav)
        eq += same
        pr, pw = prime_powers_in(n - W, n + W)
        sp = 2.0 * W / (pr + pw)
        res.append(d)
        L.append('  %-3s | %2d | %9d | %14.4f | %7.4f | %6.1f | %-6s | %.4f | %d + %d | %.4f | 1' % (
            f, k, n, p, d, nav, 'EQUAL' if same else 'DIFFERS', math.log(n), pr, pw, sp))
    L += ['', '## III. FOR THE NAVIGATOR, read, nothing computed for it',
          '  The route`s rate is log(R/s) with s = (1 + 3R)/4 (tools/b709_pairs.py :179-:180), which data/b710_registrations.txt :19-:20 reads as',
          '  r/4 + O(r^2); the first-order form keeps r/4 alone. Expanded one order further, log(R/s) = r/4 - 3r^2/32 + O(r^3), a rate smaller',
          '  by the factor (1 - 3r/8), which lengthens the onset; that term is the candidate this observation points to. It is not computed',
          '  here ((R324)(8): no new computation of onsets, no registration); it is a registration for b715 to write before any figure of it.']
    pos = sum(d > 0 for d in res)
    L += ['', '### ### **TEN PAIRS ; EQUAL %d OF 10 TO ONE DECIMAL ; THE RESIDUAL %.1f TO %.1f IN n, POSITIVE AT %d OF 10 (the onset after the prediction) ;'
          ' THE ONSET STEP 1 ; SIEVE CONTROLS %d OF %d ; NO ONSET COMPUTED ; %d s.**' % (
              eq, min(res), max(res), pos, sum(ok for _n, ok, _v in cs), len(cs), int(time.time() - t0))]
    out = NL.join(L) + NL
    print(out)
    if 'dry' in a or not allok:
        if not allok:
            print('### A CONTROL NOT AS WANTED -- NOTHING WRITTEN')
        return
    data = out.encode('utf-8')
    with open(OUT + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(OUT + '.tmp', OUT)
    print('  %s  data/b714_residual.txt' % hashlib.sha256(data).hexdigest())


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'bank':
        print('usage: b714_residual.py bank [dry]')
        sys.exit(2)
    bank(*sys.argv[2:])
