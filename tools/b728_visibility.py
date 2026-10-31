# -*- coding: utf-8 -*-
"""b728_visibility.py -- (R338)(6), W-ORD-VISIBILITY: |Z_Q1(rho)| AT THE 69 OFF-LINE ZEROS AGAINST beta - 1/2 AND AGAINST gamma, FROM data/b725_interference.txt :32-:100.

### No computation of Z_Q1: the rows are read from the bank. No law fitted, no registration. The rank correlation is Spearman's, on midpoints, ties averaged.
### WHAT "READS CLEAN" MEANS, FIXED HERE AND COMMITTED BEFORE ANY CORRELATION IS PRINTED, (R338)(6) NAMING NO BAR: a relation is MONOTONE CLEAN where
###   |Spearman| >= 0.80 AND the pairs of zeros whose |Z_Q1| balls are disjoint and whose order runs against the correlation's sign are at most 5% of the
###   pairs with disjoint balls. Both, on the whole 69. Short of either, it is printed NOT CLEAN, and no candidate law is written.
### beside it, deciding nothing: Spearman between beta - 1/2 and gamma, so that a reading against one is not taken for a reading against the other.
### Routes: read [--bank]; banks data/b728_visibility.txt. Written by the Write tool at b728; it writes that bank and nothing else.
"""
import io
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
SRC = os.path.join(D, 'b725_interference.txt')
BANK = os.path.join(D, 'b728_visibility.txt')
ROW = re.compile(r'^  (off\d+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+) \+- ([0-9.e+-]+)\s+(\d+)\s+EXCLUDES 0')
RHO_BAR, AGAINST_BAR = 0.80, 0.05


def rows():
    L = io.open(SRC, encoding='utf-8').read().split(NL)
    out = []
    for i, l in enumerate(L, 1):
        m = ROW.match(l)
        if m:
            out.append(dict(line=i, name=m.group(1), d=float(m.group(2)), g=float(m.group(3)), z=float(m.group(4)), r=float(m.group(5)), bits=int(m.group(6))))
    if len(out) != 69 or out[0]['line'] != 32 or out[-1]['line'] != 100:
        sys.exit('### THE TABLE NOT READ AS 69 ROWS AT :32-:100 (%d rows) -- REFUSED' % len(out))
    return out


def ranks(x):
    o = sorted(range(len(x)), key=lambda i: x[i])
    r = [0.0] * len(x)
    i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]:
            j += 1
        for k in range(i, j + 1):
            r[o[k]] = (i + j) / 2.0 + 1
        i = j + 1
    return r


def spearman(x, y):
    a, b = ranks(x), ranks(y)
    n = float(len(x))
    ma, mb = sum(a) / n, sum(b) / n
    c = sum((p - ma) * (q - mb) for p, q in zip(a, b))
    va = sum((p - ma) ** 2 for p in a)
    vb = sum((q - mb) ** 2 for q in b)
    return c / (va * vb) ** 0.5


def against(R, key, sign):
    """pairs with disjoint |Z_Q1| balls, and those whose order runs against the sign."""
    tot = bad = 0
    for i in range(len(R)):
        for j in range(i + 1, len(R)):
            p, q = R[i], R[j]
            if abs(p['z'] - q['z']) <= p['r'] + q['r'] or p[key] == q[key]:
                continue
            tot += 1
            if (p['z'] - q['z']) * (p[key] - q[key]) * sign < 0:
                bad += 1
    return tot, bad


def read(*a):
    R = rows()
    L = []

    def out(s=''):
        print(s, flush=True)
        L.append(s)

    out('b728 -- (R338)(6), W-ORD-VISIBILITY: |Z_Q1(rho)| AGAINST beta - 1/2 AND AGAINST gamma, FROM THE BANK, NO LAW FITTED, NO REGISTRATION (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    out()
    out('### by tools/b728_visibility.py, committed before any correlation; the rows data/b725_interference.txt :32-:100, read unedited; "monotone clean" as its head fixes it, (R338)(6) naming no bar.')
    out()
    out('## THE TABLE, IN THE BANK`S ORDER (decreasing beta - 1/2)')
    out('  name    beta - 1/2     gamma        |Z_Q1(rho)|             ball radius   bits  bank line')
    for r in R:
        out('  %-6s  %.10f  %11.6f  %.14f  %.4e  %4d  :%d' % (r['name'], r['d'], r['g'], r['z'], r['r'], r['bits'], r['line']))
    d, g, z = [r['d'] for r in R], [r['g'] for r in R], [r['z'] for r in R]
    out()
    out('## THE RANK CORRELATIONS, ON MIDPOINTS, THE 69 ROWS')
    verdicts = {}
    for key, nm, xs in (('d', 'beta - 1/2', d), ('g', 'gamma', g)):
        rho = spearman(xs, z)
        sign = 1 if rho >= 0 else -1
        tot, bad = against(R, key, sign)
        share = bad / float(tot) if tot else 1.0
        clean = abs(rho) >= RHO_BAR and share <= AGAINST_BAR
        verdicts[nm] = clean
        out('  |Z_Q1| against %-10s Spearman %+.4f ; pairs with disjoint balls %d ; against the sign %d, share %.4f ; %s' % (nm, rho, tot, bad, share, 'MONOTONE CLEAN' if clean else 'NOT CLEAN'))
    out('  beside it, deciding nothing: beta - 1/2 against gamma, Spearman %+.4f' % spearman(d, g))
    rs = sorted(r['r'] for r in R)
    out('  the ball radii: least %.3e ; median %.3e ; greatest %.3e' % (rs[0], rs[len(rs) // 2], rs[-1]))
    out()
    if any(verdicts.values()):
        hit = [k for k, v in verdicts.items() if v]
        out('## THE CANDIDATE, IN WORDS, FOR b729`S REGISTRATION, NOT REGISTERED HERE: |Z_Q1(rho)| at an off-line zero of Z_Q0 is monotone in %s.' % ' and in '.join(hit))
    else:
        out('## NO CANDIDATE LAW: neither relation reads monotone clean by the bar fixed in the tool.')
    out()
    out('### ### **W-ORD-VISIBILITY, THE TABLE AT 69 ZEROS: AGAINST beta - 1/2 %s ; AGAINST gamma %s ; NO LAW FITTED ; NOTHING REGISTERED.**' % tuple('MONOTONE CLEAN' if verdicts[k] else 'NOT CLEAN' for k in ('beta - 1/2', 'gamma')))
    if '--bank' in a:
        with open(BANK + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(BANK + '.tmp', BANK)
        print('written data/b728_visibility.txt')


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] != 'read':
        sys.exit('usage: b728_visibility.py read [--bank]')
    read(*sys.argv[2:])
