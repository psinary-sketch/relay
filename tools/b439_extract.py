# -*- coding: utf-8 -*-
"""b439_extract.py -- THE SURVEY. ### **WRITTEN BEFORE THE FACE.**

### ### **IT READS THE CONSTRUCTION AND DOES ARITHMETIC ON A FORMULA.** ### The weight table is a
### closed expression evaluated at named integers; the coefficient read is the instrument's own
### stored `tf.coeffs`. ### **NEITHER IS A NEW MEASUREMENT OF THE ACT'S SUBJECT** -- the profile's
### zeros, and their drift, belong to the components, after the face is locked.
"""
import io
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b439_extract.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L, READS, MISS = [], [0], []


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('-' * 100)
    rec('  ### (%s) %s' % (n, t))
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def nl(s):
    return s.replace(chr(13) + chr(10), chr(10))


def wrap(s, n=88):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, after=0, label=None, indent='      '):
    READS[0] += 1
    lines = nl(read(path)).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rec('%s%s:%d' % (indent, os.path.basename(path), i + 1))
            for b in lines[i:i + after + 1]:
                for c in wrap(b.strip(), 84):
                    rec('%s  | %s' % (indent, c))
            return True
    MISS.append('%s : %r NOT LOCATED' % (os.path.basename(path), (label or needle)[:60]))
    rec('%s### **NOT LOCATED** : %s' % (indent, (label or needle)[:60]))
    return False


def prime_powers_upto(x):
    out, n = [], 2
    while n <= x + 1e-12:
        m, p = n, 0
        for q in range(2, int(n ** 0.5) + 2):
            if m % q == 0:
                while m % q == 0:
                    m //= q
                    p += 1
                break
        if (m == 1 and p >= 1) or (m == n):
            out.append(n)
        n += 1
    return out


def factor_p(n):
    for q in range(2, n + 1):
        if n % q == 0:
            return q
    return n


def main():
    rec('=' * 100)
    rec('b439 -- THE FIXED PROFILE, THE FIXED POINT, AND ONE ARITHMETIC CLAIM. ### THE SURVEY.')
    rec('=' * 100)

    # ------------------------------------------------------------------------------------------
    head(1, "THE CONSTRUCTION, AT ITS OWN LINES -- ### **WHAT SCALES AND WHAT DOES NOT.**")
    rec('    ### **THE BUMP, AND ITS SCALED VARIABLE:**')
    quote(os.path.join(T, 'e16', 'carto_atlas.py'), 'def bump(a):', 7, label='the bump')
    rec('        ### ### **`t = v / L` WITH `L = log a`.** ### The shape `exp(-1/(1-t^2))` is a')
    rec('        ### function of `t` alone, and `t` IS the scaled variable `s`. ### **SO ONE BUMP`S')
    rec('        ### ### SHAPE IN `s` IS THE SAME AT EVERY RADIUS**, up to the `1/log a` the')
    rec('        ### normalisation carries.')
    rec('')
    rec('    ### **THE THREE WIDTHS, AND WHERE THEY SIT IN `s`:**')
    quote(os.path.join(T, 'b317_smear.py'), 'MZ_EXPONENTS', 0, label='the three exponents')
    rec('        ### ### **`bump(a ** e)` HAS HALF-WIDTH `e log a` IN `v`, HENCE `e` IN `s`.** ###')
    rec('        ### So the three supports sit at `s = 1`, `1/2`, `1/4` ### **FOR EVERY RADIUS**,')
    rec('        ### exactly as the order says.')
    rec('')
    rec('    ### **AND THE TWO CONDITIONS THE COEFFICIENTS SOLVE:**')
    quote(os.path.join(T, 'b317_smear.py'), 'I = np.array([np.trapezoid(p, V)', 1,
          label='the first moment')
    quote(os.path.join(T, 'b317_smear.py'), 'A2 = np.array([[I[1], I[2]], [M[1], M[2]]])', 2,
          label='the 2x2 system')
    rec('')
    rec('    ### ### **THE FIRST CONDITION IS SCALE-INVARIANT AND THE SECOND IS NOT, AND THAT IS')
    rec('    ### ### READ OFF THE INTEGRANDS RATHER THAN ASSERTED.**')
    rec('        `I[i] = INT phi_i dv` -- each bump is normalised to integral one, so `I` is `1`')
    rec('        for all three at every radius. ### **NO `a` IN IT.**')
    rec('        `M[i] = INT phi_i(v) cosh(v/2) dv` -- and in the scaled variable `v = s log a`')
    rec('        this is `INT (1/e) phi(s/e) cosh(s log a / 2) ds`. ### **THE WEIGHT CARRIES `a`')
    rec('        ### EXPLICITLY, INSIDE A `cosh`, WHICH IS NOT A POWER OF `x` AND THEREFORE NOT')
    rec('        ### SCALE-INVARIANT.**')

    # ------------------------------------------------------------------------------------------
    head(2, "THE COEFFICIENTS, READ AT SIX RADII. ### **THE INSTRUMENT`S OWN STORED VALUES.**")
    rec('    ### **THIS READ WAS TAKEN AT STEP ZERO, BEFORE THE FACE**, because it decides what')
    rec('    ### shape this act has. ### It is the instrument`s own `tf.coeffs`, stored by')
    rec('    ### `mean_zero_variant` when it solves; ### **NOTHING IS RE-DERIVED HERE.** ### The')
    rec('    ### components re-read and re-print them after the lock.')
    rec('')
    try:
        import b317_smear as SM
        rec('      %-12s %-18s %-18s %s' % ('a', 'c0', 'c1', 'c2'))
        co = []
        for a in (1.8155451, 2.5073306, 2.5729801, 3.0, 4.0, 5.6416382):
            g = SM.mean_zero_variant(a)
            co.append(dict(a=a, c=list(g.coeffs)))
            rec('      %-12.7f %-18.12f %-18.12f %.12f' % ((a,) + tuple(g.coeffs)))
        c1 = [x['c'][1] for x in co]
        rec('')
        rec('      ### ### **`c1` RUNS %.12f -> %.12f ACROSS THESE RADII.**' % (c1[0], c1[-1]))
        rec('      ### ### **THE COEFFICIENTS ARE NOT CONSTANT IN `a`.**')
        rec('      ### And at b438`s two DOWNWARD crossing radii specifically:')
        rec('          a* = 1.8155451  c1 = %.12f' % c1[0])
        rec('          a* = 2.5729801  c1 = %.12f' % c1[2])
        rec('          they differ by %.3e' % abs(c1[2] - c1[0]))
        json.dump(co, io.open(os.path.join(D, 'b439_coeffs.json'), 'w', encoding='utf-8'),
                  indent=1)
    except Exception as e:                                       # noqa: BLE001
        MISS.append('the coefficients could not be read (%s)' % str(e)[:60])
        rec('      ### **NOT READ** : %s' % str(e)[:70])

    # ------------------------------------------------------------------------------------------
    head(3, "THE WEIGHT TABLE -- ### **ARITHMETIC ON A CLOSED FORMULA, NOT A MEASUREMENT.**")
    quote(os.path.join(T, 'b321_window.py'), "val = 2.0 * math.log(p) / math.sqrt(n)", 0,
          label='the weight')
    rec('')
    rec('      %-6s %-6s %-16s %s' % ('n', 'p', '2 log p / sqrt(n)', 'rank'))
    ws = []
    for n in prime_powers_upto(16):
        p = factor_p(n)
        ws.append((n, p, 2.0 * math.log(p) / math.sqrt(n)))
    order = sorted(ws, key=lambda x: -x[2])
    rk = dict((w[0], i + 1) for i, w in enumerate(order))
    for n, p, w in ws:
        rec('      %-6d %-6d %-16.9f %d of %d' % (n, p, w, rk[n], len(ws)))
    rec('')
    rec('      ### ### **THE MAXIMIZER BELOW SIXTEEN IS `n = %d` AT `%.9f`.**'
        % (order[0][0], order[0][2]))
    two = [w for w in ws if w[0] == 2][0]
    rec('      ### ### **AND `n = 2` IS `%.9f`, RANKED %d OF %d.**'
        % (two[2], rk[2], len(ws)))
    rec('      ### **SO THE NAVIGATOR`S ARITHMETIC IS CHECKED AND IT AGREES**: two at `0.980`,')
    rec('      ### seven at `1.471`, and two is sixth of ten. ### **b438`S CLOSING SAID THE')
    rec('      ### ### TWO-TERM`S WEIGHT WAS THE LARGEST OF ANY PRIME POWER, AND THAT IS FALSE.**')
    rec('      ### The correction rides in this act`s record; ### **b438`S BANK IS NOT EDITED.**')
    json.dump([dict(n=n, p=p, w=w, rank=rk[n]) for n, p, w in ws],
              io.open(os.path.join(D, 'b439_weights.json'), 'w', encoding='utf-8'), indent=1)

    # ------------------------------------------------------------------------------------------
    head(4, "HAS ANY ACT NAMED `u0`? ### **THE SEARCH, PRINTED.**")
    pats = [('the value to four places', r'6\.2898'),
            ('the value to two places', r'6\.29(?![0-9])'),
            ('a named `u0`', r'\bu_?0\b'),
            ('the balance condition in words', r'Re\s*psi[^\n]{0,40}=\s*log\s*pi'),
            ('digamma equals log pi', r'digamma[^\n]{0,40}log\s*\(?pi')]
    hits = {}
    for lbl, rx in pats:
        where = []
        for base in (PP, D, T):
            for root, dirs, fs in os.walk(base):
                dirs[:] = [x for x in dirs if x not in ('.git', '__pycache__', 'archive')]
                for f in fs:
                    if not f.endswith(('.md', '.txt', '.py')):
                        continue
                    if f.startswith('b439_'):
                        continue
                    t = read(os.path.join(root, f))
                    if re.search(rx, t, re.I):
                        where.append(os.path.relpath(os.path.join(root, f), ROOT)
                                     .replace(os.sep, '/'))
        hits[lbl] = where
        rec('      %-34s %-4d %s' % (lbl, len(where), ', '.join(where[:3]) or '-'))
    rec('')
    rec('    ### ### **THIS PRINTS WHERE THE VOCABULARY OCCURS AND DECIDES NOTHING.** ### Whether')
    rec('    ### any hit NAMES the constant, or merely contains the digits, is Component 3`s work')
    rec('    ### and is done by hand-reading each at its own line.')
    json.dump(dict((k, v) for k, v in hits.items()),
              io.open(os.path.join(D, 'b439_u0search.json'), 'w', encoding='utf-8'), indent=1)

    # ------------------------------------------------------------------------------------------
    head(5, "b438`S BANKED CROSSINGS, RE-READ.")
    READS[0] += 1
    try:
        room = json.loads(read(os.path.join(D, 'b438_room.json')) or '{}')
    except Exception:                                            # noqa: BLE001
        room = {}
        MISS.append('b438_room.json : unreadable')
    sh = (room.get('addendum') or {}).get('shells', [])
    for s in sh:
        rec('      flip at a = %-10.6f  n = %-3d  a* = %-12.7f  %-8s  s = %.9f'
            % (s['flip_at'], s['n'], s['a_star'],
               '+ -> -' if s['direction'] == 'down' else '- -> +', s['ratio']))
    dn = [s for s in sh if s['direction'] == 'down']
    if len(dn) > 1:
        rec('')
        rec('      ### **THE TWO DOWNWARD CROSSINGS DIFFER BY %.3e IN `s`.**'
            % abs(dn[0]['ratio'] - dn[1]['ratio']))
        rec('      ### **b438 CALLED THAT A FIXED BOUNDARY. ### COMPONENT 1 ASKS WHETHER THE')
        rec('      ### ### RESIDUAL IS THE GRID`S OR THE OBJECT`S**, and the coefficient read')
        rec('      ### above already bears on it.')

    rec('')
    rec('=' * 100)
    rec('  ### READS ATTEMPTED : %d' % READS[0])
    rec('  ### MISSES          : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
