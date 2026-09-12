# -*- coding: utf-8 -*-
"""b438_extract.py -- THE SURVEY FOR THE ALTERNATION AND THE ROOM. ### **WRITTEN BEFORE THE FACE.**

### ### **IT READS, AND IT EVALUATES ONE FIXED FUNCTION.** ### The archimedean kernel `h+` is a
### property of the digamma and of nothing else -- it carries no family, no radius and no cell -- so
### locating its own zero is a read of a fixed object, not a measurement of this act's subject.
### ### **EVERY CELL VALUE BELONGS TO THE COMPONENTS, AFTER THE FACE IS LOCKED.**
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
OUT = os.path.join(D, 'b438_extract.txt')

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


def main():
    rec('=' * 100)
    rec('b438 -- WHAT ALTERNATES THE SIGN, AND WHERE THE ROOM CLOSES. ### THE SURVEY.')
    rec('=' * 100)

    head(1, "WHICH TEST FUNCTION THE LADDER USES -- ### **AIMED, NOT PLAIN.**")
    rec('    ### The order asks first whether the ladder rides the PLAIN bump`s autocorrelation or')
    rec('    ### an AIMED seed`s. ### **IT IS AIMED, AND THE INSTRUMENT`S OWN SOURCE SAYS SO:**')
    quote(os.path.join(T, 'b317_smear.py'), 'def mean_zero_variant(a):', 2,
          label='the aimed seed')
    rec('')
    rec('    ### and the coefficients are SOLVED, not chosen -- two moments are driven to zero:')
    quote(os.path.join(T, 'b317_smear.py'), 'c12 = np.linalg.solve(A2, b2)', 0,
          label='the solved coefficients')
    quote(os.path.join(T, 'b317_smear.py'), '`c_0` is fixed to one', 0, label='what is solved for')
    rec('')
    rec('    ### ### **SO THE SEED MUST TAKE NEGATIVE VALUES.** ### A non-negative function cannot')
    rec('    ### have a vanishing integral unless it is zero. ### **THE OSCILLATION IS BUILT IN BY')
    rec('    ### ### THE AIM**, and this act`s Component 1 asks what that oscillation does at the')
    rec('    ### log-primes.')
    rec('')
    rec('    ### and the chain the ladder actually runs, at its own line:')
    quote(os.path.join(T, 'b321_run.py'), 'g = SM.mean_zero_variant(a)', 2, label='the chain')
    rec('')
    rec('    ### ### **AND A SECOND FAMILY THE RECORD ALREADY HOLDS**, which Component 2 needs:')
    quote(os.path.join(T, 'b317_smear.py'), 'def corpus_bump(a):', 2, label='the second family')

    head(2, "THE WEIGHT IN THE PRIME SUM -- ### **AND WHAT IT SETTLES BEFORE ANY CELL IS READ.**")
    quote(os.path.join(T, 'b321_window.py'), "val = 2.0 * math.log(p) / math.sqrt(n)", 0,
          label="route `corpus`'s term")
    rec('')
    rec('    ### ### **`2 log p / sqrt(n)` IS STRICTLY POSITIVE FOR EVERY PRIME POWER `n = p^k`')
    rec('    ### ### WITH `p >= 2`.** ### So in this route the sign of a term IS the sign of the')
    rec('    ### test function at that prime power`s log, ### **BY THE FORM OF THE EXPRESSION AND')
    rec('    ### ### NOT AS AN EMPIRICAL FINDING.** ### Component 1 will still print every term --')
    rec('    ### a claim about the form is not a substitute for the values -- but the act must say')
    rec('    ### which kind of statement it is scoring.')
    rec('')
    rec('    ### and the OTHER route, which does not assume evenness:')
    quote(os.path.join(T, 'b321_window.py'), "val = math.log(p) * (fx + fs)", 0,
          label="route `s149`'s term")
    rec('    ### ### **THERE THE SIGN IS THE SIGN OF `f(x) + f^#(x)`**, which equals `2 w(log n)`')
    rec('    ### only because the lawful `f` is an autocorrelation and therefore EVEN. ### Both')
    rec('    ### routes are run in Component 1 so the evenness is exercised rather than assumed.')

    head(3, "THE TWO ROUTES FOR THE ARCHIMEDEAN CHANNEL.")
    rec('    ### **ROUTE ONE -- the transform side, against the corpus`s digamma kernel:**')
    quote(os.path.join(T, 'e16', 'carto_atlas.py'), 'A = float(np.trapezoid(hhat(v, w, U)', 0,
          label="the atlas's A")
    quote(os.path.join(T, 'e16', 'carto_atlas.py'), 'def kernel(U):', 2, label='the kernel')
    rec('')
    rec('    ### **ROUTE TWO -- b320`s, from the source`s (53), (38) and (39):**')
    quote(os.path.join(T, 'b320_weil.py'), 'def weil(f):', 7, label="b320's weil route")
    rec('')
    rec('    ### **AND b333`S `h+`, THE DISTRIBUTION ITSELF, AT ITS OWN LINE:**')
    quote(os.path.join(T, 'b333_derive.py'), 'hplus = -log(pi) + mre(digamma', 0, label='h+')

    head(4, "`h+` ALONE -- ### **A PROPERTY OF THE DIGAMMA, CARRYING NO FAMILY AND NO RADIUS.**")
    rec('    ### This is the one evaluation the survey makes, and it is of a FIXED function: `h+`')
    rec('    ### depends on `u` and on nothing else. ### **NO CELL, NO FAMILY, NO SUPPORT')
    rec('    ### PARAMETER ENTERS IT.**')
    try:
        from mpmath import mp, digamma, mpc, re as mre
        mp.dps = 20

        def hplus(u):
            return float(mre(digamma(mpc(0.25, u / 2.0)))) - math.log(math.pi)

        rec('')
        rec('      %-10s %s' % ('u', 'h+(u) = Re psi(1/4 + i u/2) - log pi'))
        for u in (0.0, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 20.0, 50.0):
            rec('      %-10.4f %+.9f' % (u, hplus(u)))
        lo, hi = 0.0, 50.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if hplus(mid) < 0:
                lo = mid
            else:
                hi = mid
        u0 = 0.5 * (lo + hi)
        rec('')
        rec('      ### ### **`h+` IS NEGATIVE AT `u = 0` (`%+.6f`) AND GROWS LIKE `log u`.**'
            % hplus(0.0))
        rec('      ### ### **IT HAS ONE SIGN CHANGE, AT `u0 = %.9f`** -- located by bisection to'
            % u0)
        rec('      ### `%.1e`, and `h+(u0) = %+.3e`.' % (hi - lo, hplus(u0)))
        json.dump(dict(u0=u0, h0=hplus(0.0)),
                  io.open(os.path.join(D, 'b438_hplus.json'), 'w', encoding='utf-8'), indent=1)
    except Exception as e:                                       # noqa: BLE001
        MISS.append('h+ : could not be evaluated (%s)' % str(e)[:60])
        rec('      ### **NOT EVALUATED** : %s' % str(e)[:70])
    rec('')
    rec('    ### ### **AND THIS IS WHAT MAKES COMPONENT 2 DECIDABLE RATHER THAN A MATTER OF')
    rec('    ### ### OPINION.** ### The archimedean channel is `A = (1/2pi) INT fhat(u) h+(u) du`,')
    rec('    ### and for the lawful `f = g conv g^#` the weight `fhat = |ghat|^2` is ### **NEVER')
    rec('    ### NEGATIVE.** ### So `A < 0` requires `h+ < 0` where that weight has its mass --')
    rec('    ### that is, the family`s transform sitting mostly BELOW `u0`.')
    rec('    ### ### **AND A NORMALIZATION CANNOT DO IT.** ### The scale is a POSITIVE number and')
    rec('    ### multiplying by a positive number moves no zero. ### Component 2 will say this')
    rec('    ### against printed values rather than on this reasoning alone.')

    head(5, "b437`S CELLS, AND WHAT THIS ACT MUST RE-OPEN.")
    READS[0] += 1
    try:
        rungs = json.loads(read(os.path.join(D, 'b437_rungs.json')) or '{}')
    except Exception:                                            # noqa: BLE001
        rungs = {}
        MISS.append('b437_rungs.json : unreadable')
    rows = rungs.get('rows', [])
    nega = [r for r in rows if r.get('arch') is not None and r['arch'] < 0]
    pos = [r for r in rows if r.get('arch') is not None and r['arch'] > 0]
    rec('    cells banked by b437            : %d' % len(rows))
    rec('    with a POSITIVE archimedean A   : %d' % len(pos))
    rec('    with a NEGATIVE archimedean A   : %d' % len(nega))
    if nega and pos:
        last_pos = max((r for r in pos), key=lambda r: r['a'])
        first_neg = min((r for r in nega), key=lambda r: r['a'])
        rec('')
        rec('    ### ### **THE BRACKET, FROM b437`S OWN TABLE:**')
        rec('        a = %.6f   A = %+.9f' % (last_pos['a'], last_pos['arch']))
        rec('        a = %.6f   A = %+.9f' % (first_neg['a'], first_neg['arch']))
        rec('    ### **THE ZERO LIES BETWEEN THEM**, and b437 reported only that it lies between')
        rec('    ### two GRID POINTS. ### Component 2 locates it.')
        json.dump(dict(lo=last_pos['a'], hi=first_neg['a'],
                       a_lo=last_pos['arch'], a_hi=first_neg['arch']),
                  io.open(os.path.join(D, 'b438_bracket.json'), 'w', encoding='utf-8'), indent=1)
    rec('')
    # ### **THE `if False else` SHAPE PRINTED A STRAY LINE IN b437 AND AGAIN HERE.** ### It is
    # ### an expression whose first branch is a rec() CALL, so the call runs before the ternary
    # ### chooses. ### **A FORMAT STRING WITH NO ARGUMENTS IS A LINE THAT PRINTS ITS OWN
    # ### PLACEHOLDER**, and the fix is to stop being clever: two plain statements.
    rec('    ### **AND THE CELLS PAST THE ROOM, WHICH COMPONENT 3 READS:** ### %d of them.'
        % len(nega))
    rec('    ### **AND (R49) AUTHORISES NO MORE**: its scope is the cells b437 banked, decomposed,')
    rec('    ### and the distribution evaluated against the same family. ### **NO NEW CELL.**')

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
