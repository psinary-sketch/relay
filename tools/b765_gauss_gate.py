# -*- coding: utf-8 -*-
"""b765_gauss_gate.py -- THE GATE OF (R375)(5)(b), BEFORE ANY DISPATCH OF GAUSS'S INTEGRAL FOR THE ARCHIMEDEAN TERM: a control and no
registration.

### THE NAVIGATOR'S READING ((R375)(5)(b)): for k in classK,
###   archTermQ k = 2 k(0) (log(sqrt 23 / (2 pi)) - gamma) + 2 INT_0^inf (e^-t k(0) - e^(-t/2) k(t)) / (1 - e^-t) dt.
### THE GATE: at the kernel's window at the widths of data/b709_grid.txt :426 and :439 (b709's N window, tools/b709_grid.py _window and
### terms709, imported unedited), the form S = P - PR + A computed with this right side in place of the kernel's integral equals the banked
### S_NN to 6 digits (half a unit of the sixth significant digit). Where it fails, no Lean of (5)(b) is sent and the difference is printed.
### THE RIGHT SIDE: k vanishes beyond 2L (L = log of the width); on [0, 2L] k is analytic between its knots t = m s (s = L/3, m = 0 .. 6),
### and the integrand is analytic at t = 0 (its singularity there removable), so the integral is taken by Gauss-Legendre on each of the six
### pieces at n nodes (nodes by Newton's method in arb, held as points; k by b694's exact piecewise convolution Window.kval), at n = 40 and
### n = 80, their difference printed as the quadrature's reading; beyond 2L the integral is k(0) (-log(1 - e^(-2L))), in closed form.
### P and PR are b709's own (terms709), its bracket integral A printed beside the right side's. Nothing computed at a zero; no bank of
### zeros opened; data/b709_grid.txt read at :426 and :439 alone.
### Routes: gate <rung983 | mid1021_1024> (one unit to data/b765_gauss_gate_units.jsonl, UNTRACKED, appended); bank (data/b765_gauss_gate.txt).
### Each route refuses where this file differs from its blob at the relay's HEAD: committed before its run ((R375)(5)(b), N2).
### Written by the Write tool at b765; it writes only the files it names.
"""
import hashlib
import io
import json
import math
import os
import re
import subprocess
import sys
import time

from flint import arb, ctx, fmpq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b696_witness_balls as WB   # noqa: E402  ### the precision b709 ran at: imported unedited
import b709_grid as G             # noqa: E402  ### the grid's points, its window and its terms: imported unedited

SELF = 'tools/b765_gauss_gate.py'
UNITS = os.path.join(D, 'b765_gauss_gate_units.jsonl')   # ### UNTRACKED WRITE: one unit a route, appended
BANK = 'data/b765_gauss_gate.txt'
GRID = 'data/b709_grid.txt'
GRID_ROWS = {'rung983': (426, 379), 'mid1021_1024': (439, 392)}
PREC = WB.PREC
NODES = (40, 80)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def bs(x):
    x = arb(x)
    return [x.mid().str(45, radius=False), x.rad().str(5, radius=False)]


def bl(p):
    return arb(p[0], p[1])


def fmt(x, n=12):
    x = arb(x)
    return '%s +- %s' % (x.mid().str(n, radius=False), x.rad().str(3, radius=False))


def _git(*a):
    r = subprocess.run(('git', '-C', ROOT) + a, capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').strip()


def self_commit():
    rc1, blob = _git('rev-parse', 'HEAD:' + SELF)
    rc2, work = _git('hash-object', SELF)
    rc3, st = _git('status', '--porcelain', '--', SELF)
    if rc1 or rc2 or rc3 or blob != work or st:
        sys.exit('### %s DIFFERS FROM ITS BLOB AT THE RELAY`S HEAD, OR HEAD HOLDS NONE -- NOTHING RUN (committed before its run, N2)' % SELF)
    return _git('log', '-1', '--format=%H', '--', SELF)[1][:8]


def self_sha():
    return hashlib.sha256(open(os.path.join(ROOT, SELF), 'rb').read()).hexdigest()[:16]


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[u['key']] = u
    return U


def put_unit(u, commit):
    u['at'] = utc()
    u['tool'] = dict(commit=commit, sha256=self_sha())
    line = (json.dumps(u, ensure_ascii=False) + NL).encode('utf-8')
    with open(UNITS, 'ab') as fh:
        fh.write(line)


def grid_row(point):
    """data/b709_grid.txt at the point's row, read by its line and no other; its needle and its S_NN."""
    line, idx = GRID_ROWS[point]
    row = None
    with io.open(os.path.join(ROOT, GRID), encoding='utf-8') as fh:
        for i, l in enumerate(fh, 1):
            if i == line:
                row = l.rstrip(chr(13) + NL)
                break
    needle = '  rho0 | %4d | %s ' % (idx, point)
    m = re.search(r'\| S_NN (\S+) \+- (\S+) \|', row or '')
    if row is None or not row.startswith(needle) or m is None:
        sys.exit('### %s :%d DOES NOT OPEN WITH %r OR HOLDS NO S_NN -- NOTHING COMPUTED' % (GRID, line, needle))
    return m.group(1), m.group(2)


def gl_rule(n):
    """Gauss-Legendre on [-1, 1]: the nodes by Newton's method from the float guesses; the weights 2 / ((1 - x^2) P_n'(x)^2). Computed at twice
    the working precision and held as points, nodes and weights alike: the three-term recurrence widens a ball by about 2^n, so a weight
    computed as a ball at the working precision carries a radius that is the recurrence's and not the rule's (b765's first run at :426:
    4.5e-10 on the weights at n = 80 and 128 bits, the right side's radius 7.7e-7 over the gate's tolerance 5e-7, every node value of k and
    of the integrand within 1e-26; data/b765_events.txt (40))."""
    prec0 = ctx.prec
    ctx.prec = 2 * prec0
    out = []
    try:
        for i in range(1, n + 1):
            x = arb(math.cos(math.pi * (i - 0.25) / (n + 0.5)))
            for _ in range(16):
                p0, p1 = arb(1), x
                for k in range(2, n + 1):
                    p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
                dp = n * (x * p1 - p0) / (x * x - 1)
                x = arb((x - p1 / dp).mid())
            p0, p1 = arb(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            out.append((arb(x.mid()), arb((2 / ((1 - x * x) * dp * dp)).mid())))
    finally:
        ctx.prec = prec0
    return out


def gauss_integral(Wd, k0, n):
    """INT_0^(2L) (e^-t k(0) - e^(-t/2) k(t)) / (1 - e^-t) dt by Gauss-Legendre at n nodes on each piece [m s, (m+1) s], m = 0 .. 5."""
    rule = gl_rule(n)
    s = Wd.s
    tot = arb(0)
    for m in range(6):
        a, b = m * s, (m + 1) * s
        c, h = (a + b) / 2, (b - a) / 2
        for x, w in rule:
            t = c + h * x
            kv = Wd.kval(t)
            tot += h * w * ((-t).exp() * k0 - (-t / 2).exp() * kv) / (1 - (-t).exp())
    return tot


def gate(point=None, *a):
    if point not in GRID_ROWS:
        sys.exit('usage: gate <%s>' % ' | '.join(GRID_ROWS))
    commit = self_commit()
    ctx.prec = PREC
    t0 = time.time()
    bmid, brad = grid_row(point)
    banked = arb(bmid, brad)
    pts = {p['name']: p for p in G.grid('rho0')}
    pt = pts[point]
    if pt['i'] != GRID_ROWS[point][1]:
        sys.exit('### THE GRID`S POINT %s HAS INDEX %d, THE BANK`S ROW %d -- NOTHING COMPUTED' % (point, pt['i'], GRID_ROWS[point][1]))
    r = G.terms709('rho0', pt, 'N', 'q0')
    P, PR, A_br, k0 = bl(r['P']), bl(r['PR']), bl(r['A']), bl(r['k0'])
    Wd = G._window('rho0', pt, 'N')
    L = Wd.L
    tail = -k0 * (1 - (-2 * L).exp()).log()
    ints = {n: gauss_integral(Wd, k0, n) for n in NODES}
    quad = fmt(ints[NODES[1]] - ints[NODES[0]], 3)
    J = ints[NODES[1]] + tail
    A_g = 2 * k0 * ((arb(23).sqrt() / (2 * arb.pi())).log() - arb.const_euler()) + 2 * J
    S_g = P - PR + A_g
    e6 = int(math.floor(math.log10(abs(float(bmid))))) - 5
    tol = arb(fmpq(1, 2)) * arb(10) ** e6
    diff = S_g - banked
    passes = bool(abs(diff) < tol)
    u = dict(key='gate/' + point, route='gate', point=point, line=GRID_ROWS[point][0], index=pt['i'], banked=[bmid, brad], P=r['P'], PR=r['PR'],
             A_bracket=r['A'], k0=r['k0'], A_gauss=bs(A_g), S_gauss=bs(S_g), J=bs(J), tail=bs(tail), quad_diff=quad, nodes=list(NODES),
             A_diff=fmt(A_g - A_br, 4), diff=fmt(diff, 4), tol='0.5e%d' % e6, passes=passes, prec=PREC, seconds=int(time.time() - t0))
    put_unit(u, commit)
    print('  THE GATE at %s (%s :%d, index %d): S by the right side %s ; banked S_NN %s +- %s ; difference %s ; to 6 digits (%s) %s ; '
          'A by the right side %s ; A by the kernel`s bracket integral %s ; their difference %s ; k(0) %s ; the quadrature at %d and %d nodes a '
          'piece differs by %s ; the tail beyond 2L %s ; %s ; %d s' % (
              point, GRID, u['line'], pt['i'], fmt(S_g), bmid, brad, u['diff'], u['tol'], passes, fmt(A_g), fmt(A_br), u['A_diff'], fmt(k0),
              NODES[0], NODES[1], quad, fmt(tail), 'PASSES' if passes else 'FAILS', u['seconds']), flush=True)


def put_txt(path, L):
    data = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(ROOT, path)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)


def bank(*a):
    commit = self_commit()
    U = units()
    missing = [p for p in GRID_ROWS if 'gate/' + p not in U]
    if missing:
        sys.exit('### UNITS MISSING %s -- NOTHING BANKED' % missing)
    ctx.prec = PREC
    L = ['b765 -- THE GATE OF (R375)(5)(b): GAUSS`S INTEGRAL FOR THE ARCHIMEDEAN TERM AT THE KERNEL`S WINDOW, A CONTROL AND NO REGISTRATION (%s)'
         % utc(), '',
         '### the tool %s, sha256 %s, committed at relay %s before its run; b709`s N window and terms (tools/b709_grid.py, imported unedited) at'
         % (SELF, self_sha(), commit),
         '### %d bits; the right side by Gauss-Legendre on the six pieces of k in [0, 2L] at %d and %d nodes a piece, the tail beyond 2L in closed'
         % (PREC, NODES[0], NODES[1]),
         '### form; data/b709_grid.txt read at :426 and :439 alone; nothing computed at a zero; no bank of zeros opened.', '',
         '## THE GATE, CELL BY CELL']
    allu = []
    for l in io.open(UNITS, encoding='utf-8'):
        if l.strip():
            allu.append(json.loads(l))
    ok = True
    for p in GRID_ROWS:
        u = U['gate/' + p]
        ok = ok and u['passes']
        for e in [x for x in allu if x['key'] == 'gate/' + p][:-1]:
            L.append('  %s, AN EARLIER RUN (tool %s, %s): S by the right side %s ; difference %s ; to 6 digits %s ; the quadrature`s two readings '
                     'differ by %s ; %s, not the reading entered' % (p, e['tool']['commit'], e['at'], fmt(bl(e['S_gauss'])), e['diff'],
                                                                      e['passes'], e['quad_diff'], 'PASSES' if e['passes'] else 'FAILS'))
        L.append('  %s (%s :%d, index %d): S by the right side %s ; banked S_NN %s +- %s ; difference %s ; to 6 digits %s ; A by the right side %s ; '
                 'A by the kernel`s bracket integral %s ; difference %s ; the quadrature`s two readings differ by %s ; %s' % (
                     p, GRID, u['line'], u['index'], fmt(bl(u['S_gauss'])), u['banked'][0], u['banked'][1], u['diff'], u['passes'],
                     fmt(bl(u['A_gauss'])), fmt(bl(u['A_bracket'])), u['A_diff'], u['quad_diff'], 'PASSES' if u['passes'] else 'FAILS'))
    L += ['', '## THE READING', '  THE GATE %s: %s' % ('PASSES' if ok else 'FAILS',
                                                        'the Lean of (5)(b) may be sent, its statement first' if ok else
                                                        'no Lean of (5)(b) is sent; [S4] with the difference printed above')]
    put_txt(BANK, L)
    print(NL.join(L), flush=True)


ROUTES = {'gate': gate, 'bank': bank}

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ROUTES:
        sys.exit('usage: b765_gauss_gate.py <%s> [args]' % ' | '.join(ROUTES))
    ROUTES[sys.argv[1]](*sys.argv[2:])
