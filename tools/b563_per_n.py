# -*- coding: utf-8 -*-
"""b563_per_n.py -- COMPONENT 2: THE PER-n RE-SCORE OF b562's SYMMETRIC DRIFT, UNDER (R173)(2).
### FROM relay data/b562_drift.txt ALONE -- its text parsed, its sha256 printed; no transform computed, no zero read.
### For each n = 1..12: the least-squares line D = a + b δ through the three symmetric points, its intercept a (the δ -> 0
### extrapolation); Z(n, 0) := Λ_N(n) + T2(n) + a (b562's H13b third clause's value, its words carried); λ_n from table (i)'s
### BALPOS column where banked, else Λ_N + T2 (NOT CLASSICAL); the floor T2(n) + eps Σ|t| + the quadrature floor (the row's
### own columns; b562's bank carries one of each per n). H15d HOLDS unless two or more n miss.
### Printed beside it, NOT SCORED: the member's own sum Λ_N + D and its extrapolation; (D - T2) / (n² δ) at each δ.
### This file deletes nothing.
"""
import hashlib, io, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
SRC = os.path.join(D, 'b562_drift.txt')
DELTAS = (0.1, 0.03, 0.01)
NUM = r'[-+]?\d+\.\d+(?:e[-+]?\d+)?'


def parse(t):
    lines = t.split(NL)
    i1 = [k for k, l in enumerate(lines) if l.startswith('### (i) ')][0]
    ii = [k for k, l in enumerate(lines) if l.startswith('### (ii) ')][0]
    sym = [k for k, l in enumerate(lines) if l.strip() == '### SYMMETRIC'][0]
    tab1 = {}
    for l in lines[i1:ii]:
        m = re.match(r'^\s+(\d+)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s+(%s|\(not banked\))' % ((NUM,) * 5), l)
        if m:
            n = int(m.group(1))
            tab1[n] = dict(lam_N=float(m.group(2)), T2=float(m.group(3)), T1=float(m.group(4)), lamT2=float(m.group(5)),
                           balpos=None if m.group(6).startswith('(') else float(m.group(6)))
    tab2 = {}
    for l in lines[sym + 1:]:
        m = re.match(r'^\s+(\d+)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s*$' % ((NUM,) * 5), l)
        if not m:
            if tab2:
                break
            continue
        tab2[int(m.group(1))] = dict(D=[float(m.group(k)) for k in (2, 3, 4)], quad=float(m.group(5)), eps=float(m.group(6)))
    return tab1, tab2


def lsq(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    return my - b * mx, b


def main():
    t = io.open(SRC, encoding='utf-8').read().replace(chr(13), '')
    tab1, tab2 = parse(t)
    L = ['=' * 118, 'b563 -- COMPONENT 2: THE PER-n RE-SCORE OF b562`S SYMMETRIC DRIFT (R173)(2). ### FROM b562`S BANK ALONE; A '
         'RE-READING OF A MEASUREMENT, NOT A THEOREM.', '=' * 118,
         '### the source: relay data/b562_drift.txt, sha256 %s ; parsed rows: table (i) %d, symmetric table (ii) %d'
         % (hashlib.sha256(open(SRC, 'rb').read()).hexdigest(), len(tab1), len(tab2)),
         '### the extrapolation: the least-squares line D = a + b δ through δ = 0.1, 0.03, 0.01; Z(n, 0) = Λ_N(n) + T2(n) + a;',
         '### the floor(n) = T2(n) + eps Σ|t| + the quadrature floor (the row`s own columns, one of each per n in b562`s bank).', '',
         '      n        a (δ→0)        slope b        Z(n,0)               λ_n                  Z(n,0) - λ_n    floor        ratio  within  source']
    rows, misses = [], []
    for n in range(1, 13):
        r1, r2 = tab1[n], tab2[n]
        a, b = lsq(list(DELTAS), r2['D'])
        z0 = r1['lam_N'] + r1['T2'] + a
        classical = r1['balpos'] is not None
        lam = r1['balpos'] if classical else r1['lamT2']
        fl = r1['T2'] + r2['eps'] + r2['quad']
        diff = z0 - lam
        ok = abs(diff) <= fl
        if not ok:
            misses.append(n)
        own = r1['lam_N'] + a
        rat_n2 = [(r2['D'][k] - r1['T2']) / (n * n * DELTAS[k]) for k in range(3)]
        rows.append(dict(n=n, a=a, b=b, z0=z0, lam=lam, classical=classical, diff=diff, floor=fl, ratio=abs(diff) / fl, ok=ok,
                         own0=own, own_diff=own - lam, own_ratio=abs(own - lam) / fl, dmt2_n2d=rat_n2))
        L.append('     %2d  %+.6e  %+.6e  %.15f  %.15f  %+.4e  %.4e  %.3f  %-6s  %s'
                 % (n, a, b, z0, lam, diff, fl, abs(diff) / fl, 'yes' if ok else 'NO', 'BALPOS' if classical else 'NOT CLASSICAL (Λ_N + T2)'))
    h15d = len(misses) < 2
    L += ['', '### ### **H15d (the δ → 0 extrapolation within floor at every n in 1..12; refuted by two or more misses): %s** -- misses %s'
          % ('HOLDS' if h15d else 'REFUTED', misses or 'NONE'),
          '### classical comparisons: n = %s ; the rest against the bank`s own Λ_N + T2' % [r['n'] for r in rows if r['classical']], '',
          '### PRINTED BESIDE IT, NOT SCORED (the face`s READING (3)):',
          '###   (a) the member`s own sum over the bank, Λ_N(n) + D(n, δ), extrapolated: Λ_N(n) + a, against λ_n (no tail added: the',
          '###       member`s transform beyond the bank`s last ordinate is small, the jump`s is not);',
          '###   (b) (D(n, δ) - T2(n)) / (n² δ) at δ = 0.1, 0.03, 0.01 -- the drift with the jump`s tail taken off, per n² δ.',
          '      n    Λ_N + a - λ_n     ratio to floor     (D - T2)/(n² δ) at 0.1        0.03          0.01']
    for r in rows:
        L.append('     %2d   %+.4e        %.3f            %+.6f     %+.6f     %+.6f' % (r['n'], r['own_diff'], r['own_ratio'], *r['dmt2_n2d']))
    ratios = [round(r['ratio'], 2) for r in rows if r['classical']]
    L += ['', '### the literal ratio |Z(n,0) - λ_n| / floor at the classical n: %s' % ratios,
          '### the member`s-own ratio at the classical n: %s' % [round(r['own_ratio'], 2) for r in rows if r['classical']],
          '=' * 118]
    io.open(os.path.join(D, 'b563_per_n.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(rows=rows, h15d=h15d, misses=misses, source_sha=hashlib.sha256(open(SRC, 'rb').read()).hexdigest()),
              io.open(os.path.join(D, 'b563_per_n.json'), 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    print(NL.join(L))


if __name__ == '__main__':
    main()
