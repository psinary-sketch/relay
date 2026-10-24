# -*- coding: utf-8 -*-
"""b710_fit.py -- (R320)(6)(i): THE REFINED DETECTION LAW'S FITTED CONSTANTS AND ITS PREDICTIONS FOR PAIRS 11 AND 15, from b709's banked figures
alone (data/b709_pairs.txt :46-:57), before the certified list reaches those pairs' heights. NOTHING IS COMPUTED FOR THE LAW'S TEST HERE: no n*,
no zero, no Li coefficient -- the ten computed pairs' r(rho) and n* are read from their bank as printed and the two constants fitted to them.

### THE FORM (the route's own equation read to first order, the citation check's miss for (6)(i), data/b710_citation_check.txt): b675's onset
### (tools/b675_li_bench.py :153-:160, :188-:189) is the least n with 2 - (1/4) R^n + C (n + 1)^2 s^n < 0, s = (1 + 3R)/4; with r = log R
### (the bank's r(rho)) and log(R/s) = r/4 + O(r^2), the onset solves r n* = 4 log(4C) + 8 log(n* + 1) to first order -- the ruling's
### r n* = log(M(n*)/A) with M(n) = (C (n + 1)^2)^4 and A = (1/4)^4. The fitted form: r n* = alpha + beta log(n* + 1), alpha and beta by least
### squares over the ten computed pairs; the route's own coefficient beta = 8 printed beside as a second, one-constant fit (alpha alone).
### The prediction for a pair of rate r: the fixed point n = (alpha + beta log(n + 1)) / r, iterated from L0 / r to a change below 1e-9.
### Writes data/b710_fit.txt (the seat's derived figures, for the registration to quote by line). Usage: python tools/b710_fit.py
"""
import math
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROW = re.compile(r'^\s+(\d+) \| \[(\S+) \+ \[(\S+) i \| r\(rho\) \[(\S+) \+/- \S+\] \| T0` needed > (\S+) ; the list`s (\d+) \| n\* (\S+) \| predicted \[(\S+) \+/- \S+\]')


def rows():
    out = []
    for i, l in enumerate(open(os.path.join(D, 'b709_pairs.txt'), encoding='utf-8').read().split(NL), 1):
        m = ROW.match(l)
        if m:
            out.append(dict(line=i, idx=int(m.group(1)), beta_re=float(m.group(2)), t=float(m.group(3)), r=float(m.group(4)), need=float(m.group(5)),
                            nstar=int(m.group(7)) if m.group(7) != '-' else None, predicted=float(m.group(8))))
    return out


def lsq(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    return my - b * mx, b


def solve(alpha, beta, r, n0):
    n = n0
    for _ in range(200):
        n1 = (alpha + beta * math.log(n + 1)) / r
        if abs(n1 - n) < 1e-9:
            return n1
        n = n1
    return n


def main():
    R = rows()
    comp = [x for x in R if x['nstar']]
    far = [x for x in R if not x['nstar']]
    L0 = 108.573953341369431556137   # ### data/b709_pairs.txt :11, (C1): L0 at rho_0
    xs = [math.log(x['nstar'] + 1) for x in comp]
    ys = [x['r'] * x['nstar'] for x in comp]
    a2, b2 = lsq(xs, ys)
    a1 = sum(y - 8 * x for x, y in zip(xs, ys)) / len(xs)
    L = ['b710 -- (R320)(6)(i): THE REFINED DETECTION LAW`S FITTED CONSTANTS, FROM b709`S BANKED PAIRS ALONE; THE PREDICTIONS FOR PAIRS 11 AND 15 (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: relay data/b709_pairs.txt :46-:57 (rows are off-line pairs; r(rho) = log|1 - 1/(1 - beta + i t)| and n* as printed), the ten',
         '### computed pairs read, the two beyond reach (11, 15) read for their r(rho) alone. NOTHING COMPUTED FOR THE LAW`S TEST: no n*, no zero, no Li',
         '### coefficient; the constants fitted to the banked figures and the fixed point solved -- the seat`s derived figures. The form: r n* = alpha +',
         '### beta log(n* + 1) (b675`s onset, tools/b675_li_bench.py :153-:160 and :188-:189, read to first order: alpha = 4 log(4C), beta = 8).', '',
         '### THE TEN COMPUTED PAIRS (idx | the bank`s line | height | r(rho) | n* | r n* | log(n* + 1)):']
    for x, lx, y in zip(comp, xs, ys):
        L.append('  %2d | :%d | t %.4f | r %.9e | n* %d | r n* %.6f | log(n*+1) %.6f' % (x['idx'], x['line'], x['t'], x['r'], x['nstar'], y, lx))
    L += ['', '### THE FITTED CONSTANTS:',
          '  (F2) two constants by least squares: alpha %.6f ; beta %.6f' % (a2, b2),
          '  (F1) the route`s beta = 8, alpha alone by least squares: alpha %.6f' % a1, '',
          '### THE FIT AGAINST THE TEN (the registered control`s own reading at b711: each within [0.9, 1.1] of its refined prediction) -- idx | n* | F2 | n*/F2 | F1 | n*/F1:']
    w2, w1 = 0, 0
    for x in comp:
        p2 = solve(a2, b2, x['r'], L0 / x['r'])
        p1 = solve(a1, 8.0, x['r'], L0 / x['r'])
        w2 += 0.9 <= x['nstar'] / p2 <= 1.1
        w1 += 0.9 <= x['nstar'] / p1 <= 1.1
        L.append('  %2d | %d | %.1f | %.6f | %.1f | %.6f' % (x['idx'], x['nstar'], p2, x['nstar'] / p2, p1, x['nstar'] / p1))
    L += ['  within [0.9, 1.1]: F2 %d of %d ; F1 %d of %d' % (w2, len(comp), w1, len(comp)), '',
          '### THE PREDICTIONS FOR THE PAIRS BEYOND REACH (idx | the bank`s line | height | r(rho) | b709`s L0/r | F2 | F1 | the window [0.9, 1.1] of F2):']
    for x in far:
        p2 = solve(a2, b2, x['r'], L0 / x['r'])
        p1 = solve(a1, 8.0, x['r'], L0 / x['r'])
        L.append('  %2d | :%d | t %.4f | r %.9e | L0/r %.1f | F2 %.1f | F1 %.1f | [%.1f, %.1f]' % (x['idx'], x['line'], x['t'], x['r'], L0 / x['r'], p2, p1, 0.9 * p2, 1.1 * p2))
    L += ['', '### ### **TEN PAIRS READ ; F2 alpha %.4f beta %.4f ; F1 alpha %.4f (beta 8) ; WITHIN [0.9, 1.1] F2 %d OF 10, F1 %d OF 10 ; PREDICTIONS %s ; NOTHING COMPUTED FOR THE TEST.**' % (
        a2, b2, a1, w2, w1, ' ; '.join('pair %d F2 %.0f F1 %.0f' % (x['idx'], solve(a2, b2, x['r'], L0 / x['r']), solve(a1, 8.0, x['r'], L0 / x['r'])) for x in far))]
    p = os.path.join(D, 'b710_fit.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(L))


if __name__ == '__main__':
    main()
