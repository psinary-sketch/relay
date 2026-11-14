# -*- coding: utf-8 -*-
"""b755, (R365)(4)(h) and (5)(ii): THE ZERO LIST FROM THE PRIMES -- (4)(h)'s generator, written by the seat from the statements alone
(data/b753_author_words_preseal.txt :42, (h); (R365)(4)(h) and (5)(ii), data/b755_ferry.txt :17, :23) and committed before its run ((S3)).
No value of any Epstein zeta function is computed here: only sums over primes.

THE FUNCTION, from the closed forms (candidate (a), data/b755_cand_a.txt; (e), data/b753_author_words_preseal.txt :26), each an identity on
Re s > 1 and a numerical reading to its left ("the sums not converging absolutely to the left of Re s = 1", (R365)(5)(ii)):
  CLASS NUMBER 3 (-23, -59): f(s) = 1 + 2 exp(-3 T_P(s)), T_P the sum of (-log(1 - p^-s) + log(1 - p^-3s)/3) over the primes p <= P that
      split and are not represented by the principal form; THE TAIL (5)(ii): (1/3) E1((s - 1) log P) + (1/6) E1((2s - 1) log P).
  CLASS NUMBER 2 (-15): f(s) = 1 + exp(-U_P(s)), U_P = 2S the sum of w_p log((1 + p^-s)/(1 - p^-s)) over the primes p <= P outside the
      principal class, w_p = 2 at a split prime and 1 at a ramified one (exp(-U) = L(s, chi)/zeta_K(s) on Re s > 1, the seat's reading of
      e^(-2S) = -1 of (e)); THE TAIL the seat's, by the same density count as (5)(ii)'s (a quarter of the primes, weight 2, leading term 2p^-s):
      E1((s - 1) log P).
THE ROUTE (5)(ii): the modulus |f| on sigma = 0.80..1.30 by 0.01 and t = 2..H by 0.01 at P = 10^4, no tail; each local minimum under 0.3
  (eight neighbours, the edges included) refined by Newton's method at the larger P with the tail, the step capped at 0.05; a root kept where
  |f| < 1e-9; roots within 1e-6 of each other one root.
THE MATCH (5)(ii)'s prediction, worded there: the zeros with real part at least 0.85 and height 2..H against the roots with real part at least
  0.85, one to one, each pair within 0.01; a zero or root with real part 0.83..0.85 may serve as a partner and needs none (nearest pairs first).

MODES
  banked             (4)(h): Newton from each zero of the banked lists with real part >= 0.80 (-23: data/b725_interference.txt, P = 3 x 10^5;
                     -15: data/b713_list.txt, P = 2 x 10^6), the distance to the root; groups Re >= 0.90 and [0.80, 0.90); bank data/b755_cand_h.txt
  plant              the same with the tail dropped (both fields) and with the split prime 2 given a ramified prime's weight at -15 (no ramified
                     prime lies outside the principal class at class number 3, data/b753_registrations.txt :18-:19); bank data/b755_cand_h_plant.txt
  scan <D> <H>       the route at a banked field (-23 or -15) and the match against its list: the route's own control and its timing;
                     bank data/b755_cand_h_scan_<|D|>.txt
  list -59 <H> <commit>   the route at -59: REFUSED unless <commit> is an ancestor of HEAD whose data/b755_registrations.txt holds the rule
                     H-ZEROS-FROM-PRIMES; bank data/b755_roots_59.txt and .json (the list of roots, committed before any value at -59 is read)
  verdict -59 200    the rule's test, added after the list of roots was committed (relay e21b5c8c) and committed with tools/b755_list.py
                     before the certified list at -59 exists: the band rows of data/b755_list_59.txt (b717's form, the -15 list's reader
                     above), their off-line count equal to data/b755_list_59.json's, every band COMPLETE and reaching 200, against the roots
                     of data/b755_roots_59.json by match() -- refused unless match()'s text equals its text at relay 1b84e4b1, the reading
                     data/b755_registrations.txt (2) fixes; bank data/b755_zeros_from_primes_59.txt and .json
"""
import json
import math
import os
import re
import subprocess
import sys
import time

import mpmath
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = {-23: (6, 3), -15: (4, 2), -59: (15, 3)}  # D: (c of x^2 + xy + c y^2, class number)
P_SCAN = 10 ** 4
P_NEWTON = {-23: 3 * 10 ** 5, -15: 2 * 10 ** 6, -59: 3 * 10 ** 5}
SIG = [round(0.80 + 0.01 * j, 2) for j in range(51)]
NAV = {-23: {'hi': (7, 0.00106), 'lo': (17, 0.00256), 'P': '3 x 10^5'}, -15: {'hi': (5, 0.00021), 'lo': (8, 0.00136), 'P': '2 x 10^6'}}
NAV_WORDS = 'the navigator\'s workspace, in no bank ((R365)(4)(h), data/b755_ferry.txt :17)'
RULE_HEAD = re.compile(r'^## \(\d+\) THE RULE \(H-ZEROS-FROM-PRIMES\)', re.M)
BAND_ROW = re.compile(r"^  band \[([0-9.]+), ([0-9.]+)\] \| N (\d+) \| on-line (\d+) \| off-line (\d+)\s*(\[.*\])?\s*\| (\S+)")
MATCH_AT = '1b84e4b1'   # ### the commit data/b755_registrations.txt (2) names for match()'s reading of "one to one"


def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def represented(c, n):
    rep = np.zeros(n + 1, dtype=bool)
    ymax = int(math.isqrt(4 * n // (4 * c - 1))) + 1
    for y in range(-ymax, ymax + 1):
        # x^2 + xy + c y^2 <= n  <=>  (2x + y)^2 <= 4n - (4c - 1) y^2
        rem = 4 * n - (4 * c - 1) * y * y
        if rem < 0:
            continue
        r = math.isqrt(rem)
        xs = np.arange((-r - y) // 2 - 1, (r - y) // 2 + 2, dtype=np.int64)
        v = xs * xs + xs * y + c * y * y
        v = v[(v >= 1) & (v <= n)]
        rep[v] = True
    return rep


def kron(D, p):
    p = int(p)
    if p == 2:
        return 0 if D % 2 == 0 else (1 if D % 8 in (1, 7) else -1)
    if D % p == 0:
        return 0
    return 1 if pow(D % p, (p - 1) // 2, p) == 1 else -1


def prime_set(D, P, weight_plant=False):
    """the primes <= P outside the principal class with their weights (class number 2) or their T term (class number 3)."""
    c, h = FIELDS[D]
    ps = sieve(P)
    rep = represented(c, P)
    sel, w = [], []
    for p in ps:
        k = kron(D, p)
        if k == 1 and not rep[p]:
            sel.append(p)
            w.append(2.0)
        elif k == 0 and not rep[p]:
            if h == 3:
                raise SystemExit('### a ramified prime outside the principal class at class number 3: %d -- REFUSED' % p)
            sel.append(p)
            w.append(1.0)
    sel = np.array(sel, dtype=np.float64)
    w = np.array(w)
    if weight_plant:
        w[np.nonzero(w == 2.0)[0][0]] = 1.0  # the least split prime outside the principal class given a ramified prime's weight
    return sel, np.log(sel), w


def tail(D, s, P, on):
    if not on:
        return 0j, 0j
    L = math.log(P)
    h = FIELDS[D][1]
    z1 = (s - 1) * L
    if h == 3:
        z2 = (2 * s - 1) * L
        v = complex(mpmath.e1(z1)) / 3 + complex(mpmath.e1(z2)) / 6
        dv = -complex(mpmath.exp(-z1)) / (3 * (s - 1)) - complex(mpmath.exp(-z2)) / (3 * (2 * s - 1))
    else:
        v = complex(mpmath.e1(z1))
        dv = -complex(mpmath.exp(-z1)) / (s - 1)
    return v, dv


def f_and_df(D, s, logp, w, P, tail_on):
    h = FIELDS[D][1]
    x = np.exp(-s * logp)
    tv, tdv = tail(D, s, P, tail_on)
    if h == 3:
        x3 = x ** 3
        T = np.sum(-np.log1p(-x) + np.log1p(-x3) / 3) + tv
        dT = np.sum(logp * (-x / (1 - x) + x3 / (1 - x3))) + tdv
        e = np.exp(-3 * T)
        return 1 + 2 * e, -6 * dT * e
    U = np.sum(w * (np.log1p(x) - np.log1p(-x))) + tv
    dU = np.sum(w * (-logp) * x * 2 / (1 - x * x)) + tdv
    e = np.exp(-U)
    return 1 + e, -dU * e


def newton(D, s0, logp, w, P, tail_on, cap=0.05, iters=100):
    s = complex(s0)
    fv = None
    for _ in range(iters):
        fv, dfv = f_and_df(D, s, logp, w, P, tail_on)
        if abs(fv) < 1e-13:
            break
        step = fv / dfv
        if abs(step) > cap:
            step = step * (cap / abs(step))
        s -= step
        if abs(step) < 1e-15:
            break
    fv, _ = f_and_df(D, s, logp, w, P, tail_on)
    return s, abs(fv)


def banked_list(D):
    zs = []
    if D == -23:
        for line in open(os.path.join(ROOT, 'data', 'b725_interference.txt'), encoding='utf-8'):
            m = re.match(r'^\s+off(\d+)\s+([0-9.]+)\s+([0-9.]+)\s', line)
            if m:
                zs.append(complex(0.5 + float(m.group(2)), float(m.group(3))))
        want, top = 69, 445.0
    else:
        for line in open(os.path.join(ROOT, 'data', 'b713_list.txt'), encoding='utf-8'):
            if line.startswith('  band ['):
                for b, g in re.findall(r"\('([0-9.]+)', '([0-9.]+)'\)", line):
                    zs.append(complex(float(b), float(g)))
        want, top = 37, 199.33082
    if len(zs) != want:
        raise SystemExit('### the banked list at %d read %d zeros, wanted %d -- REFUSED' % (D, len(zs), want))
    return sorted(zs, key=lambda z: z.imag), top


def write(path, text):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    os.replace(tmp, path)


def from_banked(D, tail_on=True, weight_plant=False):
    zs, top = banked_list(D)
    P = P_NEWTON[D]
    t0 = time.time()
    _, logp, w = prime_set(D, P, weight_plant)
    t_primes = time.time() - t0
    rows = []
    for z in zs:
        if z.real < 0.80:
            continue
        r, res = newton(D, z, logp, w, P, tail_on)
        rows.append({'zero': [z.real, z.imag], 'root': [r.real, r.imag], 'dist': abs(r - z), 'residual': res})
    out = {'D': D, 'P': P, 'primes': int(len(logp)), 'tail': tail_on, 'weight_plant': weight_plant, 'listed': len(zs), 'top': top,
           'rows': rows, 'seconds_primes': round(t_primes, 1), 'seconds': round(time.time() - t0, 1)}
    for g, lo, hi in (('hi', 0.90, 9.0), ('lo', 0.80, 0.90)):
        sub = [x for x in rows if lo <= x['zero'][0] < hi]
        good = [x for x in sub if x['dist'] <= 0.02 and x['residual'] < 1e-9]
        out[g] = {'n': len(sub), 'within': len(good), 'worst': max((x['dist'] for x in sub), default=None)}
    return out


def fmt_banked(o, nav=True):
    L = ['  D = %d: primes <= %d outside the principal class %d ; the banked list %d off-line zeros with beta > 1/2 (complete to height %s) ; tail %s%s ; %.1f s'
         % (o['D'], o['P'], o['primes'], o['listed'], o['top'], 'ON' if o['tail'] else 'DROPPED (THE PLANT)',
            ' ; THE WEIGHT PLANT: the split prime 2 at weight 1' if o['weight_plant'] else '', o['seconds'])]
    for g, name in (('hi', 'Re >= 0.90'), ('lo', 'Re in [0.80, 0.90)')):
        x = o[g]
        L.append('    %s: %d of %d within 0.02 with |f| < 1e-9, the worst distance %s%s' % (
            name, x['within'], x['n'], ('%.5f' % x['worst']) if x['worst'] is not None else '-',
            ('   | beside it %s: %d of %d, the worst %.5f' % (NAV_WORDS if g == 'hi' else 'the same', NAV[o['D']][g][0], NAV[o['D']][g][0],
                                                            NAV[o['D']][g][1])) if nav else ''))
    for x in o['rows']:
        L.append('      zero %.6f + %.6f i -> root %.6f + %.6f i ; distance %.5f ; |f| %.1e' % (
            x['zero'][0], x['zero'][1], x['root'][0], x['root'][1], x['dist'], x['residual']))
    return L


def scan(D, H, P_new):
    t0 = time.time()
    _, logp_s, w_s = prime_set(D, P_SCAN)
    nt = int(round((H - 2) / 0.01)) + 1
    ts = 2 + 0.01 * np.arange(nt)
    M = np.empty((len(SIG), nt))
    h = FIELDS[D][1]
    for j, sg in enumerate(SIG):
        a = np.exp(-sg * logp_s)
        for k0 in range(0, nt, 2000):
            tt = ts[k0:k0 + 2000]
            x = a[None, :] * np.exp(-1j * np.outer(tt, logp_s))
            if h == 3:
                T = np.sum(-np.log1p(-x) + np.log1p(-x ** 3) / 3, axis=1)
                M[j, k0:k0 + 2000] = np.abs(1 + 2 * np.exp(-3 * T))
            else:
                U = np.sum(w_s[None, :] * (np.log1p(x) - np.log1p(-x)), axis=1)
                M[j, k0:k0 + 2000] = np.abs(1 + np.exp(-U))
    t_scan = time.time() - t0
    pad = np.pad(M, 1, constant_values=np.inf)
    core = pad[1:-1, 1:-1]
    ismin = np.ones_like(M, dtype=bool)
    for dj in (-1, 0, 1):
        for dk in (-1, 0, 1):
            if dj or dk:
                ismin &= core <= pad[1 + dj:1 + dj + M.shape[0], 1 + dk:1 + dk + M.shape[1]]
    ismin &= M < 0.3
    seeds = [complex(SIG[j], ts[k]) for j, k in zip(*np.nonzero(ismin))]
    t1 = time.time()
    _, logp, w = prime_set(D, P_new)
    roots = []
    for s0 in seeds:
        r, res = newton(D, s0, logp, w, P_new, True)
        if res < 1e-9 and not any(abs(r - q) < 1e-6 for q in roots):
            roots.append(r)
    t_newton = time.time() - t1
    roots.sort(key=lambda z: z.imag)
    return {'D': D, 'H': H, 'P_scan': P_SCAN, 'P_newton': P_new, 'primes_scan': int(len(logp_s)), 'primes_newton': int(len(logp)),
            'grid': [len(SIG), nt], 'minima': len(seeds), 'roots': [[r.real, r.imag] for r in roots],
            'seconds_scan': round(t_scan, 1), 'seconds_newton': round(t_newton, 1)}


def match(zeros, roots, H):
    Z = [z for z in zeros if z.real >= 0.83 and 2 <= z.imag <= H]
    R = [r for r in roots if r.real >= 0.83 and 2 <= r.imag <= H]
    pairs = sorted(((abs(z - r), i, j) for i, z in enumerate(Z) for j, r in enumerate(R) if abs(z - r) <= 0.01))
    uz, ur, P = set(), set(), []
    for d, i, j in pairs:
        if i not in uz and j not in ur:
            uz.add(i)
            ur.add(j)
            P.append((Z[i], R[j], d))
    lone_z = [Z[i] for i in range(len(Z)) if i not in uz and Z[i].real >= 0.85]
    lone_r = [R[j] for j in range(len(R)) if j not in ur and R[j].real >= 0.85]
    return {'zeros_85': sum(1 for z in Z if z.real >= 0.85), 'roots_85': sum(1 for r in R if r.real >= 0.85), 'pairs': len(P),
            'worst': max((d for _, _, d in P), default=None), 'zero_without_partner': [[z.real, z.imag] for z in lone_z],
            'root_without_partner': [[r.real, r.imag] for r in lone_r], 'held': not lone_z and not lone_r}


def match_as_registered():
    """match()'s text now against its text at relay MATCH_AT, the commit the rule (2) names: True where equal (the verdict mode refuses
    otherwise)."""
    import inspect
    now = inspect.getsource(match)
    blob = subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/b755_zlist.py' % MATCH_AT], capture_output=True, text=True,
                          encoding='utf-8').stdout
    m = re.search(r'^def match\(.*?(?=^def )', blob, re.M | re.S)
    return bool(m) and m.group(0).rstrip() == now.rstrip()


def registered(commit):
    try:
        anc = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', commit, 'HEAD'], capture_output=True).returncode == 0
        blob = subprocess.run(['git', '-C', ROOT, 'show', '%s:data/b755_registrations.txt' % commit], capture_output=True, text=True,
                              encoding='utf-8').stdout
    except OSError:
        return False
    return anc and RULE_HEAD.search(blob) is not None


def main(argv):
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    if argv[:1] == ['banked'] or argv[:1] == ['plant']:
        plant = argv[0] == 'plant'
        L, J = [], {'mode': argv[0], 'runs': []}
        if plant:
            runs = [(-23, False, False), (-15, False, False), (-15, True, True)]
            base = [from_banked(-23), from_banked(-15)]
        else:
            runs = [(-23, True, False), (-15, True, False)]
            base = []
        for D, tail_on, wp in runs:
            o = from_banked(D, tail_on, wp)
            J['runs'].append(o)
            L += fmt_banked(o, nav=not plant)
        verdict = []
        if plant:
            b = {x['D']: x for x in base}
            for o in J['runs']:
                rise = all(o[g]['worst'] is not None and b[o['D']][g]['worst'] is not None and o[g]['worst'] > b[o['D']][g]['worst']
                           for g in ('hi', 'lo'))
                lost = sum(b[o['D']][g]['within'] - o[g]['within'] for g in ('hi', 'lo'))
                verdict.append('%d %s: the worst distances %s (unplanted %s / %s ; planted %s / %s), zeros lost from within 0.02: %d' % (
                    o['D'], 'weight plant' if o['weight_plant'] else 'tail dropped', 'RISE IN BOTH GROUPS' if rise else 'DO NOT RISE IN BOTH',
                    '%.5f' % b[o['D']]['hi']['worst'], '%.5f' % b[o['D']]['lo']['worst'], '%.5f' % o['hi']['worst'], '%.5f' % o['lo']['worst'], lost))
                o['broke'] = rise or lost > 0
            ok = all(o['broke'] for o in J['runs'])
        else:
            ok = all(o[g]['within'] == o[g]['n'] for o in J['runs'] for g in ('hi', 'lo'))
            for o in J['runs']:
                verdict.append('%d: Re >= 0.90 %d of %d, worst %.5f ; [0.80, 0.90) %d of %d, worst %.5f' % (
                    o['D'], o['hi']['within'], o['hi']['n'], o['hi']['worst'], o['lo']['within'], o['lo']['n'], o['lo']['worst']))
        name = 'b755_cand_h_plant' if plant else 'b755_cand_h'
        head = ('b755 -- (R365)(4)(h): THE ZERO LIST FROM THE PRIMES, NEWTON FROM EACH BANKED ZERO WITH%s THE TAIL%s (%s)\n\n'
                '### by tools/b755_zlist.py %s, written from the statements alone and committed before its run; no value of an Epstein zeta function\n'
                '### computed. The navigator\'s figures are printed beside, as %s; none is a banked figure.\n\n'
                % ('OUT' if plant else '', ' -- THE PLANTS' if plant else '', stamp, argv[0], NAV_WORDS))
        tail_line = '\n### ### **(4)(h) %s: %s ; %s.**\n' % ('THE PLANTS' if plant else 'FROM THE BANKED ZEROS', ' | '.join(verdict),
                                                             ('EACH PLANT BREAKS THE MATCH: AS WANTED' if ok else 'A PLANT DOES NOT BREAK THE MATCH: NOT AS WANTED')
                                                             if plant else ('EVERY ZERO FOUND WITHIN 0.02' if ok else 'NOT EVERY ZERO FOUND WITHIN 0.02'))
        text = head + '\n'.join(L) + '\n' + tail_line
        print(text)
        write(os.path.join(ROOT, 'data', name + '.txt'), text)
        write(os.path.join(ROOT, 'data', name + '.json'), json.dumps(J, indent=1, default=str) + '\n')
        return 0 if ok else 1
    if argv[:1] == ['scan'] and len(argv) == 3:
        D, H = int(argv[1]), float(argv[2])
        if D not in (-23, -15):
            raise SystemExit('### scan reads a field with a banked list only (-23, -15) -- REFUSED; -59 goes by "list"')
        o = scan(D, H, P_NEWTON[D])
        zs, _ = banked_list(D)
        m = match(zs, [complex(*r) for r in o['roots']], H)
        o['match'] = m
        L = ['  D = %d to height %.2f: the grid %d x %d at P = %d (%d primes), local minima under 0.3: %d ; Newton at P = %d (%d primes) with the tail:'
             ' roots %d ; scan %.1f s, Newton %.1f s' % (D, H, o['grid'][0], o['grid'][1], P_SCAN, o['primes_scan'], o['minima'], o['P_newton'],
                                                       o['primes_newton'], len(o['roots']), o['seconds_scan'], o['seconds_newton']),
             '  THE MATCH in (5)(ii)\'s words against the banked list: zeros with Re >= 0.85 %d ; roots with Re >= 0.85 %d ; pairs within 0.01 %d,'
             ' the worst %s ; a zero without its partner %s ; a root without its partner %s: %s' % (
                 m['zeros_85'], m['roots_85'], m['pairs'], ('%.5f' % m['worst']) if m['worst'] is not None else '-', m['zero_without_partner'] or 'none',
                 m['root_without_partner'] or 'none', 'ONE TO ONE' if m['held'] else 'NOT ONE TO ONE')]
        L += ['    root %.6f + %.6f i' % (r[0], r[1]) for r in o['roots'] if r[0] >= 0.83 and 2 <= r[1] <= H]
        text = ('b755 -- (R365)(4)(h)/(5)(ii): THE ROUTE AT %d, A FIELD WITH A BANKED LIST, AND THE MATCH IN (5)(ii)\'S WORDS (%s)\n\n'
                '### by tools/b755_zlist.py scan; the seat\'s control of the scan stage, which Newton from the banked zeros does not test, and the\n'
                '### route\'s timing for the price table ((R365)(8); data/b755_stepzero.txt :97). No value of an Epstein zeta function computed.\n\n'
                % (D, stamp)) + '\n'.join(L) + '\n\n### ### **THE ROUTE AT %d TO %.2f: ROOTS %d, THE MATCH %s ; %.1f s.**\n' % (
                    D, H, len(o['roots']), 'ONE TO ONE' if m['held'] else 'NOT ONE TO ONE', o['seconds_scan'] + o['seconds_newton'])
        print(text)
        write(os.path.join(ROOT, 'data', 'b755_cand_h_scan_%d.txt' % -D), text)
        write(os.path.join(ROOT, 'data', 'b755_cand_h_scan_%d.json' % -D), json.dumps(o, indent=1) + '\n')
        return 0
    if argv[:1] == ['list'] and len(argv) == 4 and argv[1] == '-59':
        H, commit = float(argv[2]), argv[3]
        if not registered(commit):
            raise SystemExit('### H-ZEROS-FROM-PRIMES not found committed at %s in an ancestor of HEAD -- REFUSED: the rule first' % commit)
        o = scan(-59, H, P_NEWTON[-59])
        o['registration'] = commit
        rs = [r for r in o['roots'] if r[0] >= 0.83 and 2 <= r[1] <= H]
        L = ['  D = -59, x^2 + xy + 15y^2, to height %.2f: the grid %d x %d at P = %d (%d primes), local minima under 0.3: %d ; Newton at P = %d'
             ' (%d primes) with the tail: roots %d, with Re >= 0.83 and height 2..H %d, with Re >= 0.85 %d ; scan %.1f s, Newton %.1f s' % (
                 H, o['grid'][0], o['grid'][1], P_SCAN, o['primes_scan'], o['minima'], o['P_newton'], o['primes_newton'], len(o['roots']), len(rs),
                 sum(1 for r in rs if r[0] >= 0.85), o['seconds_scan'], o['seconds_newton'])]
        L += ['    root %.6f + %.6f i' % (r[0], r[1]) for r in rs]
        text = ('b755 -- (R365)(5)(ii): THE LIST OF ROOTS AT -59 FROM THE PRIMES, BEFORE ANY VALUE OF THE EPSTEIN ZETA FUNCTION THERE IS READ (%s)\n\n'
                '### by tools/b755_zlist.py list, under the rule H-ZEROS-FROM-PRIMES committed at %s; no value of an Epstein zeta function computed.\n\n'
                % (stamp, commit)) + '\n'.join(L) + '\n\n### ### **THE LIST AT -59 TO %.2f: ROOTS WITH Re >= 0.85 %d, WITH Re IN [0.83, 0.85) %d.**\n' % (
                    H, sum(1 for r in rs if r[0] >= 0.85), sum(1 for r in rs if r[0] < 0.85))
        print(text)
        write(os.path.join(ROOT, 'data', 'b755_roots_59.txt'), text)
        write(os.path.join(ROOT, 'data', 'b755_roots_59.json'), json.dumps(o, indent=1) + '\n')
        return 0
    if argv == ['verdict', '-59', '200']:
        H, t0 = 200.0, time.time()
        same = match_as_registered()
        if not same:
            raise SystemExit('### match() differs from its text at relay %s, the reading the rule fixes -- REFUSED' % MATCH_AT)
        rj = json.load(open(os.path.join(ROOT, 'data', 'b755_roots_59.json'), encoding='utf-8'))
        roots = [complex(*r) for r in rj['roots']]
        bands, zs = [], []
        for line in open(os.path.join(ROOT, 'data', 'b755_list_59.txt'), encoding='utf-8'):
            if not line.startswith('  band ['):
                continue
            m = BAND_ROW.match(line)
            if not m:
                raise SystemExit('### a band row not read: %s -- REFUSED' % line.strip()[:100])
            got = re.findall(r"\('([0-9.]+)', '([0-9.]+)'\)", m.group(6) or '')
            if len(got) != int(m.group(5)):
                raise SystemExit('### band [%s, %s]: %s off-line read, %d listed -- REFUSED' % (m.group(1), m.group(2), m.group(5), len(got)))
            bands.append((float(m.group(1)), float(m.group(2)), m.group(7)))
            zs += [complex(float(b), float(g)) for b, g in got]
        lj = json.load(open(os.path.join(ROOT, 'data', 'b755_list_59.json'), encoding='utf-8'))
        if len(lj['offline']) != len(zs):
            raise SystemExit('### the band rows hold %d off-line zeros, the json %d -- REFUSED' % (len(zs), len(lj['offline'])))
        complete = bool(bands) and all(b[2] == 'COMPLETE' for b in bands) and max(b[1] for b in bands) >= H - 1e-9
        zs.sort(key=lambda z: z.imag)
        o = {'stamp': stamp, 'H': H, 'bands': len(bands), 'complete': complete, 'offline': len(zs), 'roots_listed': len(roots),
             'match_text_equal_at': [MATCH_AT, same], 'zeros': [[z.real, z.imag] for z in zs]}
        L = ['  the certified list data/b755_list_59.txt: bands %d, every band COMPLETE and reaching %.0f: %s ; off-line zeros with beta > 1/2 %d'
             ' (the json %d) ; the largest real part among them %s' % (len(bands), H, complete, len(zs), len(lj['offline']),
                                                                    ('%.6f' % max(z.real for z in zs)) if zs else '-'),
             '  the list of roots data/b755_roots_59.json (relay e21b5c8c): roots %d' % len(roots),
             '  match() equal to its text at relay %s, the reading data/b755_registrations.txt (2) fixes: %s' % (MATCH_AT, same)]
        if not complete:
            verdict = 'NO VERDICT: THE LIST IS NOT COMPLETE TO H'
            m = None
        else:
            m = match(zs, roots, H)
            o['match'] = m
            L.append('  THE MATCH in (5)(ii)\'s words: zeros with Re >= 0.85 and height 2..%.0f %d ; roots with Re >= 0.85 %d ; pairs within 0.01 %d,'
                     ' the worst %s ; a zero without its partner %s ; a root without its partner %s' % (
                         H, m['zeros_85'], m['roots_85'], m['pairs'], ('%.5f' % m['worst']) if m['worst'] is not None else '-',
                         m['zero_without_partner'] or 'none', m['root_without_partner'] or 'none'))
            verdict = 'HELD' if m['held'] else 'REFUTED'
        L += ['    zero %.6f + %.6f i' % (z.real, z.imag) for z in zs if z.real >= 0.83 and 2 <= z.imag <= H]
        L += ['    root %.6f + %.6f i' % (r.real, r.imag) for r in roots if r.real >= 0.83 and 2 <= r.imag <= H]
        o['verdict'] = verdict
        text = ('b755 -- (R365)(5)(ii): H-ZEROS-FROM-PRIMES AT -59, THE LIST OF ROOTS AGAINST THE CERTIFIED LIST (%s)\n\n'
                '### by tools/b755_zlist.py verdict, committed before the certified list at -59 existed; read against the rule of\n'
                '### data/b755_registrations.txt (2) and nothing written after it; no sentence says why.\n\n' % stamp) + '\n'.join(L) + (
            '\n\n### ### **H-ZEROS-FROM-PRIMES AT -59 TO HEIGHT %.0f: %s ; ZEROS WITH Re >= 0.85 %s AGAINST ROOTS %s ; %.1f s.**\n' % (
                H, verdict, m['zeros_85'] if m else '-', m['roots_85'] if m else '-', time.time() - t0))
        print(text)
        write(os.path.join(ROOT, 'data', 'b755_zeros_from_primes_59.txt'), text)
        write(os.path.join(ROOT, 'data', 'b755_zeros_from_primes_59.json'), json.dumps(o, indent=1) + '\n')
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
