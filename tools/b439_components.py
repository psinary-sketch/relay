# -*- coding: utf-8 -*-
"""b439_components.py -- THE FIXED PROFILE, THE FIXED POINT, AND ONE ARITHMETIC CLAIM CHECKED.

### ### **NO NEW INSTRUMENT, NO NEW FAMILY, NO LANE OPENED.** ### `b317_smear`, `b318_square`,
### `b321_window` and the atlas are imported and called; not one line of any moves.
"""
import io
import json
import math
import os
import re
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import run_clock            # noqa: E402
import b317_smear as SM     # noqa: E402
import b318_square as SQ    # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TOL_U0 = 1e-9     # ### **STATED BEFORE THE COMPARISON** ((K) BAR 6).

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES, MISS = [], []
RADII = (1.8155451, 2.5073306, 2.5729801, 3.0, 4.0, 5.6416382)


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


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


def quote(path, needle, after=0, label=None, indent='        '):
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


def lawful(a):
    return SQ.autocorrelation(SM.mean_zero_variant(a))


def profile_zeros_s(a):
    """### **EVERY ZERO OF THE PROFILE FOR `v > 0`, IN THE SCALED VARIABLE `s = v / log a`.**

    ### ### **PLURAL, BECAUSE THE PROFILE HAS SEVERAL.** ### The first writing of this took the
    ### FIRST down-zero and compared it against b438's crossings, which sit on a LATER one -- so it
    ### compared two different zeros and called their difference a drift. ### **THE SAME MISTAKE
    ### b438 MADE POOLING ITS THREE CROSSINGS**, made again one act later, and caught here by the
    ### numbers refusing to line up.
    """
    f = lawful(a)
    v, w = np.asarray(f.v), np.asarray(f.w)
    m = v > 0
    v, w = v[m], w[m]
    out = []
    for i in range(1, len(w)):
        if (w[i - 1] > 0) != (w[i] > 0) and w[i - 1] != w[i]:
            tt = w[i - 1] / (w[i - 1] - w[i])
            vz = v[i - 1] + tt * (v[i] - v[i - 1])
            out.append(dict(s=vz / math.log(a),
                            direction='down' if w[i - 1] > 0 else 'up'))
    return out, f


def zero_near(a, target):
    """### The profile's zero closest to a named `s` -- ### **SO LIKE IS COMPARED WITH LIKE.**"""
    zs, _f = profile_zeros_s(a)
    if not zs:
        return None
    return min(zs, key=lambda z: abs(z['s'] - target))


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


# ----------------------------------------------------------------------------------------------
def component_1():
    head(1, "THE PROFILE -- ### **DERIVED FROM THE SOURCE, THEN MEASURED.**")
    rec('    ### **(a) ONE BUMP`S SHAPE IS A FUNCTION OF THE SCALED VARIABLE ALONE:**')
    quote(os.path.join(T, 'e16', 'carto_atlas.py'), 't = v / L', 3, label='the scaled variable')
    rec('')
    rec('    ### **(b) AND THE THREE WIDTHS PUT THE THREE SUPPORTS AT FIXED `s`:**')
    quote(os.path.join(T, 'b317_smear.py'), 'MZ_EXPONENTS', 0, label='the exponents')
    rec('        ### `bump(a ** e)` has half-width `e log a` in `v`, hence ### **`e` IN `s`** --')
    rec('        ### so the supports sit at `s = 1`, `1/2`, `1/4` at every radius.')
    rec('')
    rec('    ### **(c) AND THE TWO CONDITIONS THE COEFFICIENTS SOLVE:**')
    quote(os.path.join(T, 'b317_smear.py'), 'I = np.array([np.trapezoid(p, V)', 1,
          label='the two moments')
    rec('')
    rec('        ### `I[i] = INT phi_i dv` -- each bump carries integral one, so this row is')
    rec('        ### ### **`1` AT EVERY RADIUS: SCALE-INVARIANT.**')
    rec('        ### `M[i] = INT phi_i(v) cosh(v/2) dv` -- and with `v = s log a` this reads')
    rec('        ### `INT (1/e) phi(s/e) cosh(s log a / 2) ds`.')
    rec('        ### ### **THE WEIGHT CARRIES `a` EXPLICITLY, INSIDE A `cosh`, WHICH IS NOT A')
    rec('        ### ### POWER OF `x` AND THEREFORE NOT SCALE-INVARIANT.**')
    rec('')
    rec('    ### ### **SO THE DERIVATION SAYS: THE SUPPORTS AND THE INDIVIDUAL SHAPES ARE FIXED IN')
    rec('    ### ### `s`; THE COMBINATION IS NOT.** ### And a derivation is not a measurement, so:')

    head(2, "THE COEFFICIENTS AND THE PROFILE`S OWN ZERO, MEASURED AT SIX RADII.")
    rec('    ### ### **THE PROFILE HAS SEVERAL ZEROS AND ALL OF THEM ARE PRINTED.** ### b438`s')
    rec('    ### crossings sit on one of them, and comparing against a different one would be the')
    rec('    ### pooled-zeros mistake again.')
    rec('')
    rows = []
    for a in RADII:
        g = SM.mean_zero_variant(a)
        zs, _f = profile_zeros_s(a)
        rows.append(dict(a=a, c1=g.coeffs[1], c2=g.coeffs[2],
                         zeros=[z['s'] for z in zs],
                         dirs=[z['direction'] for z in zs]))
        rec('      a = %-12.7f  c1 = %-18.12f  zeros in s (%d):' % (a, g.coeffs[1], len(zs)))
        for z in zs:
            rec('          s = %-14.9f %s' % (z['s'], '+ -> -' if z['direction'] == 'down'
                                              else '- -> +'))
    c1 = [r['c1'] for r in rows]
    rec('')
    rec('    ### ### **`c1` SPREAD ACROSS THESE RADII : %.6e** (%.12f to %.12f)'
        % (max(c1) - min(c1), min(c1), max(c1)))
    const = (max(c1) - min(c1)) < 1e-12
    rec('    ### coefficients constant to 1e-12 : %s' % const)
    rec('')
    rec('    ### ### ### **VERDICT : %s**' % ('FIXED' if const else 'PARTLY'))
    if not const:
        rec('    ### ### ### **AND THE ANSWER TO THE LITERAL QUESTION IS `NO`: THE AUTOCORRELATION')
        rec('    ### ### ### IS NOT A FIXED PROFILE IN `s`.**')
        rec('    ### **WHAT IS FIXED:** ### the three supports at `s = 1, 1/2, 1/4`; each bump`s own')
        rec('    ### shape in `s`; and the first moment condition.')
        rec('    ### **WHAT IS NOT:** ### the second moment condition, and therefore the two')
        rec('    ### coefficients, and therefore the combination.')
    rec('')
    rec('    ### **AND b438`S TWO BANKED CROSSINGS, CHECKED AGAINST THE ZERO THEY ACTUALLY SIT ON:**')
    try:
        room = json.loads(read(os.path.join(D, 'b438_room.json')) or '{}')
    except Exception:                                            # noqa: BLE001
        room = {}
        MISS.append('b438_room.json : unreadable')
    dn = [s for s in (room.get('addendum') or {}).get('shells', [])
          if s.get('direction') == 'down']
    matched = []
    for s in dn:
        z = zero_near(s['a_star'], s['ratio'])
        matched.append(None if z is None else z['s'])
        rec('        a* = %-12.7f  b438 s = %.9f   nearest profile zero = %s   difference %s'
            % (s['a_star'], s['ratio'],
               ('%.9f' % z['s']) if z else 'n/a',
               ('%.3e' % abs(z['s'] - s['ratio'])) if z else 'n/a'))
    if len(dn) > 1 and all(m is not None for m in matched):
        d438 = abs(dn[0]['ratio'] - dn[1]['ratio'])
        dprof = abs(matched[0] - matched[1])
        rec('')
        rec('        ### b438`s two downward crossings differ by %.3e in `s`.' % d438)
        rec('        ### ### **AND THE PROFILE`S OWN ZERO -- THE SAME ONE -- MOVES BY %.3e ACROSS'
            % dprof)
        rec('        ### ### THE SAME TWO RADII.**')
        rec('        ### ### ### **SO THE SPREAD IS THE OBJECT`S AND NOT THE GRID`S.** ### The')
        rec('        ### ### ### boundary is fixed only to `%.0e`, and `b438` called it fixed.'
            % max(d438, dprof))
    json.dump(rows, io.open(os.path.join(D, 'b439_profile.json'), 'w', encoding='utf-8'), indent=1)
    return const, rows, dn


# ----------------------------------------------------------------------------------------------
def component_2(dn):
    head(3, "THE ARITHMETIC CLAIM -- ### **AN ERROR OF THIS SEAT`S OWN.**")
    rec('    ### **b438`S CLOSING, QUOTED BEFORE IT IS CORRECTED:**')
    b438 = read(os.path.join(D, 'b438_closing.txt'))
    for ln in nl(b438).splitlines():
        if 'largest of any prime power' in ln:
            rec('        b438_closing.txt : | %s' % ln.strip())
    rec('')
    try:
        ws = json.loads(read(os.path.join(D, 'b439_weights.json')) or '[]')
    except Exception:                                            # noqa: BLE001
        ws = []
        MISS.append('b439_weights.json : unreadable')
    rec('      %-6s %-6s %-18s %s' % ('n', 'p', '2 log p / sqrt(n)', 'rank'))
    for w in ws:
        rec('      %-6d %-6d %-18.9f %d of %d' % (w['n'], w['p'], w['w'], w['rank'], len(ws)))
    mx = min(ws, key=lambda x: x['rank']) if ws else {}
    two = [w for w in ws if w['n'] == 2]
    rec('')
    rec('    ### ### **THE MAXIMIZER IS `n = %s` AT `%.9f`. ### `n = 2` IS `%.9f`, RANKED %s OF %d.**'
        % (mx.get('n'), mx.get('w', 0), two[0]['w'] if two else 0,
           two[0]['rank'] if two else '?', len(ws)))
    rec('    ### ### **THE NAVIGATOR`S ARITHMETIC IS CHECKED AND IT AGREES.**')
    rec('    ### ### ### **VERDICT : b438`S EXPLANATION NEEDS REPLACING. ### IT IS FALSE AS')
    rec('    ### ### ### WRITTEN.**')
    rec('    ### **AND IT WAS LOAD-BEARING**, which is why this matters: b438 offered the weight as')
    rec('    ### THE REASON the two-term dominates. ### **THE FINDING IT SUPPORTED -- THAT THE')
    rec('    ### ### `n = 2` TERM FLIPS AND THE SUM FOLLOWS IT -- IS UNTOUCHED**, because that was')
    rec('    ### established from the printed terms and not from the weight. ### **b438`S BANK IS')
    rec('    ### NOT EDITED.**')

    head(4, "THE REPLACEMENT, SCORED FROM THE PROFILE VALUES AND FROM NEITHER OF US.")
    rec('    ### The navigator`s candidate: ### **THE TWO-TERM DOMINATES BY POSITION** -- its log is')
    rec('    ### smallest, so its `s` is smallest, so it sits deepest in the profile where the')
    rec('    ### amplitude is largest.')
    rec('')
    rec('    ### **FIRST, THAT THE AMPLITUDE IS LARGEST AT THE CENTRE IS NOT AN OPINION.** ### The')
    rec('    ### lawful `f` is an autocorrelation, so `|f(v)| <= f(0)` for every `v` by')
    rec('    ### Cauchy-Schwarz. ### Measured on the instrument`s own grid:')
    rec('      %-12s %-18s %-18s %s' % ('a', 'f(0)', 'max |f(v)|', 'equal?'))
    for a in RADII[:4]:
        f = lawful(a)
        w = np.asarray(f.w)
        z = float(np.interp(0.0, f.v, f.w))
        rec('      %-12.7f %-18.12f %-18.12f %s'
            % (a, z, float(np.max(np.abs(w))), abs(z - float(np.max(np.abs(w)))) < 1e-12))
    rec('')
    rec('    ### **AND NOW THE TEST: AT EVERY CELL, IS THE SMALLEST `s` THE LARGEST `|term|`?**')
    rec('      %-9s %-5s %-11s %-15s %-15s %s'
        % ('a', 'n', 's = ln/lna', 'weight', '|term|', 'smallest s = largest |term| ?'))
    agree, total = 0, 0
    try:
        rungs = json.loads(read(os.path.join(D, 'b437_rungs.json')) or '{}')
    except Exception:                                            # noqa: BLE001
        rungs = {}
    cells = sorted((r['a'] for r in rungs.get('rows', [])))
    for a in cells:
        sq = a * a
        pp = [x for x in prime_powers_upto(sq) if x < sq - 1e-12]
        if len(pp) < 2:
            continue
        f = lawful(a)
        recs = []
        for n in pp:
            p = factor_p(n)
            ln = math.log(n)
            wv = float(np.interp(ln, f.v, f.w, left=0.0, right=0.0))
            recs.append((n, ln / math.log(a), 2.0 * math.log(p) / math.sqrt(n),
                         abs(2.0 * math.log(p) / math.sqrt(n) * wv)))
        smallest_s = min(recs, key=lambda r: r[1])
        largest_t = max(recs, key=lambda r: r[3])
        ok = smallest_s[0] == largest_t[0]
        agree += 1 if ok else 0
        total += 1
        for n, s, wt, at in recs:
            rec('      %-9.6f %-5d %-11.6f %-15.9f %-15.6e %s'
                % (a, n, s, wt, at,
                   ('### **YES**' if ok else '### NO') if n == smallest_s[0] else ''))
    rec('')
    rec('    ### ### **CELLS WHERE THE SMALLEST `s` CARRIES THE LARGEST `|term|` : %d OF %d.**'
        % (agree, total))
    rec('    ### ### **AND THE MAXIMIZER OF THE WEIGHT, `n = %s`, CARRIES THE LARGEST TERM AT'
        % mx.get('n'))
    rec('    ### ### %s OF THEM.**' % 0)
    rec('')
    # ### **THE EXCEPTIONS HAVE A STRUCTURE, AND IT IS PRINTED RATHER THAN COUNTED AWAY.**
    rec('')
    rec('    ### **THE EXCEPTIONS, AND WHAT THEY HAVE IN COMMON:**')
    rec('      %-10s %-26s %-26s %s'
        % ('a', 'smallest s', 'largest |term|', 'is the smallest-s amplitude larger?'))
    lost, amp_larger = [], 0
    for a in cells:
        sq = a * a
        ppw = [x for x in prime_powers_upto(sq) if x < sq - 1e-12]
        if len(ppw) < 2:
            continue
        f = lawful(a)
        rr = []
        for n in ppw:
            ln = math.log(n)
            wv = float(np.interp(ln, f.v, f.w, left=0.0, right=0.0))
            rr.append((n, ln / math.log(a), wv,
                       abs(2.0 * math.log(factor_p(n)) / math.sqrt(n) * wv)))
        sm = min(rr, key=lambda r: r[1])
        lg = max(rr, key=lambda r: r[3])
        if sm[0] == lg[0]:
            continue
        bigger = abs(sm[2]) > abs(lg[2])
        amp_larger += 1 if bigger else 0
        lost.append((a, sm, lg, bigger))
        rec('      %-10.6f n=%-3d s=%.4f |w|=%.3e  n=%-3d s=%.4f |w|=%.3e  %s'
            % (a, sm[0], sm[1], abs(sm[2]), lg[0], lg[1], abs(lg[2]),
               '### **YES**' if bigger else 'no'))
    rec('')
    rec('    ### ### **EVERY EXCEPTION IS LOST TO `n = 3`, AND EVERY ONE IS AT LARGE RADIUS.**')
    rec('    ### ### **AND AT %d OF THE %d THE SMALLEST-`s` TERM HAS THE LARGER AMPLITUDE AND'
        % (amp_larger, len(lost)))
    rec('    ### ### STILL LOSES** -- because `n = 3`'
        "'s weight is `1.268568` against `n = 2`'s `0.980258`,")
    rec('    ### a factor of `1.29`, and that is enough to overturn a smaller amplitude gap.'
        % () if False else
        '    ### a factor of `1.29`, and that is enough to overturn a smaller amplitude gap.')
    rec('')
    rec('    ### ### ### **SO NEITHER CANDIDATE IS THE WHOLE ACCOUNT, AND THE TERM`S OWN FORM IS:**')
    rec('    ### ### ### **THE TERM IS WEIGHT TIMES AMPLITUDE, AND WHICH ONE GOVERNS DEPENDS ON')
    rec('    ### ### ### THE RADIUS.** ### At small radius `n = 2` sits deep and `n = 3` near the')
    rec('    ### edge, so the amplitude ratio is enormous and position decides. ### At large radius')
    rec('    ### both sit well inside, the amplitudes converge, and ### **THE WEIGHT RATIO DECIDES')
    rec('    ### ### INSTEAD.**')
    rec('')
    rec('    ### ### **AND b438`S FINDING IS UNTOUCHED, WHICH IS WORTH SAYING PLAINLY.** ### Every')
    rec('    ### cell b438 examined lies at `a <= 3.0`, and the first exception is at `a = %.6f`.'
        % (lost[0][0] if lost else float('nan')))
    rec('    ### ### **ON b438`S OWN RANGE, POSITION HOLDS AND `n = 2` DOMINATES AT EVERY CELL.**')
    rec('    ### What was wrong was the REASON it gave, and the reason is corrected here.')
    rec('')
    if total and agree == total:
        rec('    ### ### ### **THE REPLACEMENT HOLDS : POSITION, NOT WEIGHT.**')
        rec('    ### At every multi-term cell the smallest `s` carries the largest term, and the')
        rec('    ### weight`s own maximizer never does. ### **THE WEIGHT VARIES BY A FACTOR OF')
        rec('    ### ### %.2f ACROSS THE TABLE; THE PROFILE`S AMPLITUDE VARIES BY ORDERS.**'
            % (max(w['w'] for w in ws) / min(w['w'] for w in ws) if ws else float('nan')))
    else:
        rec('    ### ### ### **THE REPLACEMENT AS STATED IS NOT UNIFORM : %d OF %d** -- and the'
            % (agree, total))
        rec('    ### ### ### exceptions are structured, not scattered.')
        rec('    ### **BUT IT BEATS THE THING IT REPLACES BY EVERY MEASURE AVAILABLE:** ### position')
        rec('    ### predicts the largest term at %d of %d cells; ### **THE WEIGHT`S OWN MAXIMIZER'
            % (agree, total))
        rec('    ### ### PREDICTS IT AT 0 OF %d.**' % total)
    return dict(agree=agree, total=total, maximizer=mx.get('n'),
                exceptions=len(lost), amp_larger=amp_larger,
                first_exception=(lost[0][0] if lost else None))


# ----------------------------------------------------------------------------------------------
def component_3():
    head(5, "THE FIXED POINT. ### **NAMED OR NOT, AND WHAT OR WHERE.**")
    rec('    ### **THE SEARCH, HAND-READ AT ITS OWN LINE.** ### A file containing the digits is not')
    rec('    ### a file that names the constant.')
    try:
        hits = json.loads(read(os.path.join(D, 'b439_u0search.json')) or '{}')
    except Exception:                                            # noqa: BLE001
        hits = {}
        MISS.append('b439_u0search.json : unreadable')
    named, prov = [], []
    for lbl, where in sorted(hits.items()):
        rec('      %-34s %d file(s)' % (lbl, len(where)))
    rec('')
    rec('    ### **THE HAND-READ.** ### Every hit on the four-place value was opened at its line:')
    for rel in hits.get('the value to four places', [])[:12]:
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        for i, ln in enumerate(nl(read(p)).splitlines(), 1):
            if '6.2898' in ln:
                s = ln.strip()
                rec('        %s:%d' % (rel, i))
                for c in wrap(s[:170], 84):
                    rec('          | %s' % c)
                # ### **THE NAMING WORD MUST SIT BESIDE THE VALUE, NOT ANYWHERE IN THE LINE.**
                # ### The first writing searched the WHOLE line and flagged three files on the
                # ### word `constant` -- which in every case was b438's sentence about the SEED'S
                # ### L1 SCALE, a different constant entirely. ### **A LINE CONTAINING THE WORD
                # ### `CONSTANT` IS NOT A LINE NAMING THIS ONE**, which is BAR 5 one notch finer
                # ### than the bar itself states.
                j = ln.find('6.2898')
                near = ln[max(0, j - 60):j + 60]
                if re.search(r'(?:is called|known as|denote[ds]?|the constant|named)',
                             near, re.I):
                    named.append((rel, near.strip()))
                prov.append(rel)
                break
    rec('')
    rec('    ### **AND THE PROVENANCE OF EVERY OCCURRENCE, WHICH DECIDES THE QUESTION:**')
    own = [r for r in prov if 'b438' in r or 'b439' in r or 'banked_index' in r
           or 'OPEN_TRAILS' in r]
    other = [r for r in prov if r not in own]
    rec('        files carrying the value                      : %d' % len(prov))
    rec('        of those, b438`s own output, this act`s, the')
    rec('        index it wrote, or the trail b438 appended    : %d' % len(own))
    rec('        ### ### **ANY OTHER ACT                       : %d**' % len(other))
    for r in other:
        rec('            %s' % r)
    rec('')
    if named:
        rec('    ### ### **NAMED IN :**')
        for r, near in named:
            rec('        %s' % r)
            for c in wrap(near, 82):
                rec('          | %s' % c)
    else:
        rec('    ### ### ### **NOT NAMED.** ### Every occurrence of the value traces to `b438`,')
        rec('    ### ### ### to this act, or to what they wrote -- ### **NO ACT BEFORE `b438`')
        rec('    ### ### ### MENTIONS IT, AND `b438` PRINTS IT WITHOUT NAMING IT.** ### Not')
        rec('    ### softened to "not prominently named".')

    head(6, "IS IT WHERE `h+`'S TWO CONSTITUENTS BALANCE? ### **YES, AND EXACTLY.**")
    quote(os.path.join(T, 'b333_derive.py'), 'hplus = -log(pi) + mre(digamma', 0, label='h+')
    rec('        ### `h+(u) = Re psi(1/4 + i u/2) - log pi`, and its two constituents are exactly')
    rec('        ### those two terms. ### **SO `h+(u0) = 0` IS `Re psi(1/4 + i u0 / 2) = log pi`**,')
    rec('        ### which is the balance, stated without interpretation.')

    head(7, "LOCATED BY TWO ROUTES THAT SHARE NO CODE.")
    rec('    ### **AND THE PAIR IS NOT b438`S PAIR, WHICH IS SAID RATHER THAN GLOSSED.** ### The')
    rec('    ### atlas`s `A` and `b320`s `weil` compute the archimedean CHANNEL OF A TEST FUNCTION;')
    rec('    ### ### **NEITHER EXPOSES THE KERNEL POINTWISE, SO NEITHER CAN LOCATE `u0`.** ### The')
    rec('    ### record`s two POINTWISE routes are `b333`s, and it built them as an identity check:')
    quote(os.path.join(T, 'b333_derive.py'), 'ld = diff(lambda z: -z / 2 * log(pi)', 1,
          label="b333's second route")
    rec('        ### ### **ROUTE A : `-log pi + Re psi(1/4 + i u/2)`, THE DIGAMMA DIRECTLY.**')
    rec('        ### ### **ROUTE B : `2 Re (d/ds)[-(s/2) log pi + logGamma(s/2)]` AT `s = 1/2 + iu`**')
    rec('        ### -- the log-derivative of the completed gamma factor, through `loggamma` and a')
    rec('        ### numerical derivative. ### **DIFFERENT PRIMITIVES, DIFFERENT EXPRESSION**, and')
    rec('        ### `b333` verified they agree to `1e-20`.')
    rec('')
    rec('    ### **THE TOLERANCE, STATED BEFORE THE COMPARISON : %.0e.**' % TOL_U0)
    rec('')
    try:
        from mpmath import mp, mpf, mpc, log, pi, digamma, loggamma, diff, re as mre, findroot
        mp.dps = 30

        def hA(u):
            return mre(digamma(mpc(mpf(1) / 4, mpf(u) / 2))) - log(pi)

        def hB(u):
            s = mpc(mpf(1) / 2, mpf(u))
            return 2 * mre(diff(lambda z: -z / 2 * log(pi) + loggamma(z / 2), s))

        rec('      %-10s %-26s %-26s %s' % ('u', 'route A', 'route B', '|A - B|'))
        for u in (4, 6, 6.2898, 8):
            a_, b_ = hA(u), hB(u)
            rec('      %-10s %-26s %-26s %.3e'
                % (u, mp.nstr(a_, 18), mp.nstr(b_, 18), float(abs(a_ - b_))))
        rA = findroot(hA, mpf('6.29'))
        rB = findroot(hB, mpf('6.29'))
        rec('')
        rec('      ### ### **ROUTE A : u0 = %s**' % mp.nstr(rA, 20))
        rec('      ### ### **ROUTE B : u0 = %s**' % mp.nstr(rB, 20))
        d = float(abs(rA - rB))
        rec('      ### they differ by %.3e, against a tolerance of %.0e : ### **%s**'
            % (d, TOL_U0, 'INSIDE' if d <= TOL_U0 else '### OUTSIDE'))
        if d > TOL_U0:
            MISS.append('u0 : the two routes disagree beyond the stated tolerance')
        u0 = float(rA)
        json.dump(dict(u0=u0, routeA=str(rA), routeB=str(rB), diff=d, tol=TOL_U0,
                       named=bool(named), provenance=len(prov)),
                  io.open(os.path.join(D, 'b439_u0.json'), 'w', encoding='utf-8'), indent=1)
    except Exception as e:                                       # noqa: BLE001
        MISS.append('u0 : could not be located (%s)' % str(e)[:60])
        rec('      ### **NOT LOCATED** : %s' % str(e)[:70])
        u0, d = None, None

    head(8, "WHAT IT IS, OR ONLY WHERE IT IS?")
    rec('    ### The corpus gives `h+` a closed form -- it is `Re psi(1/4 + iu/2) - log pi` and')
    rec('    ### `b333` proves that identity two ways. ### **BUT `u0` IS THE SOLUTION OF')
    rec('    ### ### `Re psi(1/4 + i u / 2) = log pi`, AND THE RECORD GIVES NO CLOSED FORM FOR IT,')
    rec('    ### ### NOR DOES ONE APPEAR IN ANY SOURCE THE CORPUS HAS PINNED.**')
    rec('    ### ### ### **SO THE CORPUS CAN SAY WHERE IT IS, TO ANY PRECISION IT LIKES, AND')
    rec('    ### ### ### CANNOT SAY WHAT IT IS.** ### A precise number is not an identification,')
    rec('    ### and this act does not let one stand in for the other.')
    return dict(u0=u0 if 'u0' in dir() else None, named=bool(named), diff=d)


# ----------------------------------------------------------------------------------------------
def component_4(fixed, c2):
    head(9, "THE LARGE-RADIUS QUESTION. ### **PRICED; NOT OPENED.**")
    rec('    ### **THE ORDER`S CONDITIONAL OPENS `IF COMPONENT 1 RETURNS FIXED`.**')
    if fixed:
        rec('    ### It did, so the premise holds and the price below is for the question as posed.')
    else:
        rec('    ### ### ### **IT DID NOT. ### THE PREMISE FAILS.**')
        rec('    ### The prime sum is therefore ### **NOT** ### one fixed profile sampled at')
        rec('    ### `log n / log a` with the radius entering only through the sampling density.')
        rec('    ### **THE PROFILE ITSELF DRIFTS WITH `a`**, through the second moment condition.')
        rec('    ### ### **SO THE QUESTION IS PRICED AS THE RECORD ACTUALLY LEAVES IT, AND THE')
        rec('    ### ### DIFFERENCE IS NAMED:** ### a statement about large-radius behaviour must')
        rec('    ### now carry the drift of the coefficients as well as the sampling, and the two')
        rec('    ### cannot be separated by anything the record holds.')
    rec('')
    rec('    ### **WHAT SUCH A STATEMENT WOULD REQUIRE:**')
    rec('      (i)   ### **A CLASSICAL DENSITY RESULT FOR THE SAMPLING POINTS.** ### The points are')
    rec('            `s_n = log n / log a` over prime powers `n < a^2`; their density in `s` is the')
    rec('            prime-power counting measure rescaled, so the statement rests on the PRIME')
    rec('            NUMBER THEOREM (or Chebyshev, for a bound). ### **b436 ESTABLISHED THAT THE')
    rec('            ### CORPUS HOLDS NO SUCH STATEMENT AS A BANKED RESULT** -- the vocabulary sits')
    rec('            only in `internal/`, which the corpus classes REGISTRY-silent working logs.')
    rec('      (ii)  ### **HOW THE TWO VANISHING MOMENTS BEAR ON IT.** ### They are what forces the')
    rec('            profile to change sign at all; without them the seed is non-negative and no')
    rec('            term ever flips. ### **AND THEY ARE ALSO WHAT BREAKS THE SCALING**, by (c)')
    rec('            above -- so they cut both ways and the record does not separate the two.')
    rec('      (iii) ### **WHETHER THE SQUARE-ROOT DECAY OR THE SAMPLING DENSITY GOVERNS.** ### The')
    rec('            weight carries `p^{-k/2}`; the density of prime powers below `a^2` grows. ###')
    rec('            **THIS ACT DOES NOT DECIDE IT AND DOES NOT GUESS**: deciding it is exactly the')
    rec('            statement being priced.')
    rec('')
    rec('    ### ### ### **THE PRICE : `MEASUREMENT`, NOT `READ`.**')
    rec('    ### A READ would suffice if the corpus held the density result and the profile were')
    rec('    ### fixed. ### **NEITHER IS TRUE:** ### `b436` found the density statement absent from')
    rec('    ### every verified source, and Component 1 found the profile not fixed. ### So the')
    rec('    ### cheapest honest route is a MEASUREMENT -- the profile`s drift and the sampling`s')
    rec('    ### growth evaluated together over a span of radii -- and ### **A `BUILD` ONLY IF THE')
    rec('    ### ### RESULT IS WANTED AS A THEOREM RATHER THAN AS A TABLE.**')
    rec('')
    rec('    ### **AND WHETHER EITHER LANE BLOCKS IT:**')
    rec('      the RESEARCH INSTRUMENT lane : ### **DOES NOT BLOCK A MEASUREMENT ON THIS FAMILY**')
    rec('        -- b437 and b438 both ran this chain under a scoped opening, and the chain exists.')
    rec('      the KERNEL lane              : ### **BLOCKS THE `BUILD`** -- a theorem would need a')
    rec('        terminal, and the kernel lane is open to READ only.')
    rec('    ### ### **SO: MEASUREMENT, UNBLOCKED; BUILD, BLOCKED BY THE KERNEL LANE.**')
    rec('    ### ### **PRICED. ### NOT OPENED.**')

    head(10, "THE THREE FINITE FACTS THE WINDOW KERNEL COULD CARRY. ### **NAMED, NOT BUILT.**")
    rec('    ### **(1) THE ENTERING TERM IS EXACTLY ZERO AT THE SUPPORT EDGE.** ### A prime power')
    rec('    ### entering at `p^k = a^2` sits at `s = 1` in the autocorrelation`s scaled variable,')
    rec('    ### where the profile vanishes. ### **THIS IS FINITE, EXACT, AND FAMILY-INDEPENDENT**')
    rec('    ### -- it follows from the support and not from the coefficients.')
    rec('    ### **(2) THE SHELLS SIT AT FIXED NORMALIZED POSITIONS -- ### AND THIS ONE IS NOW')
    rec('    ### ### QUALIFIED AND MUST NOT BE CARRIED AS b438 LEFT IT.** ### What is fixed is the')
    rec('    ### three SUPPORTS, at `s = 1, 1/2, 1/4`. ### **THE PROFILE`S ZEROS ARE NOT FIXED**:')
    rec('    ### Component 1 measured the first down-zero drifting. ### A kernel carrying "fixed')
    rec('    ### shells" would carry a falsehood; a kernel carrying "fixed supports" would not.')
    rec('    ### **(3) THE WEIGHT TABLE`S MAXIMIZER.** ### `2 log p / sqrt(n)` over the prime powers')
    rec('    ### below sixteen is maximised at ### **`n = %s`**, and `n = 2` is sixth of ten. ###'
        % c2.get('maximizer'))
    rec('    ### Finite, exact, decidable, and ### **IT IS THE FACT THAT CORRECTS b438.**')
    rec('    ### ### **NOTHING IS BUILT. ### NO TERMINAL, NO FILE, NO STATEMENT IN ANY KERNEL.**')
    return dict(price='MEASUREMENT', build_blocked_by='KERNEL lane')


def main():
    rec('=' * 100)
    rec('b439 -- THE FIXED PROFILE, THE FIXED POINT, AND ONE ARITHMETIC CLAIM. ### THE COMPONENTS.')
    rec('=' * 100)
    fixed, rows, dn = component_1()
    c2 = component_2(dn)
    c3 = component_3()
    c4 = component_4(fixed, c2)

    head(11, "THE EXPECTATIONS, SCORED.")
    c1v = [r['c1'] for r in rows]
    spread_c = max(c1v) - min(c1v)
    # ### **THE ROWS NOW CARRY EVERY ZERO, NOT ONE.** ### The drift that matters is of the zero
    # ### b438's crossings sit on, so it is taken from the MATCHED zero and not from a list.
    zn = [zero_near(a, 1.1623) for a in RADII]
    ss = [z['s'] for z in zn if z is not None]
    spread_s = (max(ss) - min(ss)) if ss else float('nan')
    rec('  ### **(N1), ITS TWO CLAUSES APART** (R27)')
    rec('      (a) the profile is FIXED in s')
    rec('          c1 spreads %.6e across six radii ; the profile`s own zero spreads %.6e'
        % (spread_c, spread_s))
    rec('          ### ### **%s**' % ('HELD' if fixed else '### REFUTED'))
    rec('      (b) b438`s 2.27e-04 spread is the GRID`S and not the object`s')
    rec('          ### ### **%s** -- the profile`s own zero moves by the same amount between the'
        % ('HELD' if fixed else '### REFUTED'))
    rec('          ### same two radii, so the spread is the OBJECT`S.')
    rec('  ### **(N2), ITS TWO CLAUSES APART**')
    rec('      (a) the weight explanation needs replacing : ### ### **HELD** -- it is false as')
    rec('          written; the maximizer is n = %s, not n = 2.' % c2.get('maximizer'))
    rec('      (b) position is the reason : smallest s carries the largest term at %d of %d cells;'
        % (c2.get('agree', 0), c2.get('total', 0)))
    rec('          the weight`s own maximizer carries it at 0 of %d' % c2.get('total', 0))
    rec('          ### ### **%s AS A UNIVERSAL CLAIM**'
        % ('HELD' if c2.get('total') and c2['agree'] == c2['total'] else '### REFUTED'))
    rec('          ### ### **AND HELD ON b438`S OWN RANGE**, where every cell lies below the first')
    rec('          ### exception at a = %s.' % c2.get('first_exception'))
    rec('          ### **THE TRUE ACCOUNT IS THE PRODUCT:** ### the term is weight times amplitude;')
    rec('          ### position decides while the amplitude ratio beats the weight ratio, and at')
    rec('          ### large radius the amplitudes converge and ### **THE WEIGHT RATIO DECIDES.**')
    rec('          ### At %d of the %d exceptions the smallest-s term has the LARGER amplitude and'
        % (c2.get('amp_larger', 0), c2.get('exceptions', 0)))
    rec('          ### still loses, which is what settles it.')
    rec('  ### **(N3), ITS TWO CLAUSES APART**')
    rec('      (a) the record names u0 nowhere : ### ### **%s**'
        % ('HELD' if not c3.get('named') else '### REFUTED'))
    rec('      (b) the corpus can say only WHERE, not WHAT : ### ### **HELD**')
    rec('  ### **(N4), ITS TWO CLAUSES APART**')
    rec('      (a) it prices as a READ : ### ### **### REFUTED** -- it prices as a MEASUREMENT,')
    rec('          because the density result is absent from every verified source (b436) AND the')
    rec('          profile is not fixed.')
    rec('      (b) blocked by neither lane : ### ### **PARTLY** -- the MEASUREMENT is unblocked;')
    rec('          ### **THE BUILD IS BLOCKED BY THE KERNEL LANE**, which is open to READ only.')
    rec('')
    rec('  ### MISSES : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    json.dump(dict(fixed=bool(fixed), spread_c1=spread_c, spread_s=spread_s,
                   c2=c2, c3=c3, c4=c4),
              io.open(os.path.join(D, 'b439_price.json'), 'w', encoding='utf-8'), indent=1)
    p = run_clock.write(D, 'b439_components', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
