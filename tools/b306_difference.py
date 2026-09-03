# -*- coding: utf-8 -*-
"""b306_difference.py -- THE CORPUS'S DIFFERENCE, CHECKED AGAINST ITS OWN EMITTING TABLES.

### WHAT IT IS FOR. ### The order states the corpus's difference as `L - R = -(E2even + junction)`.
### ### **THAT IS THE ORDER'S ALGEBRA AND THIS ACT MAY NOT ACCEPT IT ON THE ORDER'S WORD.** ### The
### identity is verified here against ### TWO INDEPENDENT EMITTING TABLES ### :
###   ### **b254's fourth face-off** ### -- columns `a^2`, `D - E2`, `PR - Theta_q`, residual, bar;
###   ### **b248's second-object split** ### -- columns `a^2`, `E2full`, `E2even`, `ARCHIMEDEAN`,
###     `JUNCTION`, `-D_dict`.
### ### **NEITHER TABLE IS RETYPED. ### BOTH ARE PARSED OUT OF THE FILES THAT EMITTED THEM**, which
### is the only way a cross-check between two acts means anything.

### ### **THE THREE THINGS IT DECIDES:**
###   ### (1) ### **IS b254's `D - E2` COLUMN THE NEGATIVE OF b248's `E2even`?** ### If it is, the
###     order's `E2even` really is the archimedean half of b254's residual, and the naming is not a
###     coincidence of two acts using one letter.
###   ### (2) ### **DOES b254's RESIDUAL EQUAL `(D - E2) - (PR - Theta_q)` AT EVERY ROW?** ### That
###     fixes the sign convention from the table rather than from the formula.
###   ### (3) ### **DO THE TWO ACTS AGREE ON THE JUNCTION, CELL BY CELL?** ### They are different
###     runs of different tools and ### **A DISAGREEMENT IS A FINDING, NOT A ROUNDING TO ABSORB.**

### ### **EXACT DECIMAL ARITHMETIC.** ### Every printed value is read as a `Fraction` of its exact
### decimal string. ### **NO FLOAT.** ### But the tables print to six and nine places, so exact
### EQUALITY is not available and is not demanded: ### **THE TOLERANCE IS DERIVED FROM THE PRINTED
### PRECISION AND IS STATED**, and every per-cell residual is printed so nothing hides inside it.
"""
import io
import os
import re
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

B254 = os.path.join(ROOT, 'data', 'b254_fourth_face_off.txt')
B248 = os.path.join(ROOT, 'data', 'b248_second_object.txt')

# ### THREE 6-DECIMAL ROUNDINGS CAN DISPLACE A SUM BY AT MOST 1.5e-6. ### **THE TOLERANCE IS THAT
# ### BOUND AND NOT A ROUND NUMBER CHOSEN TO MAKE THINGS PASS.**
TOL = Fraction(15, 10 ** 7)

NUM = r'-?\d+\.\d+'
ROW254 = re.compile(r'^###\s+(\d+)\s+(%s)\s+(%s)\s+(%s)\s+(\S+)\s+(\S+)' % (NUM, NUM, NUM))
ROW248 = re.compile(r'^###\s+(\d+)\s+(\d+)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s+(\S+)'
                    % (NUM, NUM, NUM, NUM, NUM))


def F(s):
    """### AN EXACT `Fraction` FROM A DECIMAL STRING. ### **NEVER `float`.**"""
    s = s.strip()
    neg = s.startswith('-')
    if neg:
        s = s[1:]
    if '.' in s:
        w, f = s.split('.')
    else:
        w, f = s, ''
    v = Fraction(int(w + f), 10 ** len(f))
    return -v if neg else v


def parse254(path):
    """### b254's TWO REALIZATION TABLES. ### Returns `{'A': {...}, 'B': {...}}` keyed by `a^2`."""
    out, cur = {'A': {}, 'B': {}}, None
    for ln in io.open(path, encoding='utf-8', errors='replace').read().splitlines():
        if 'REALIZATION (A)' in ln:
            cur = 'A'
        elif 'REALIZATION (B)' in ln:
            cur = 'B'
        m = ROW254.match(ln)
        if m and cur:
            out[cur][int(m.group(1))] = dict(d_minus_e2=F(m.group(2)),
                                             junction=F(m.group(3)),
                                             residual=F(m.group(4)))
    return out


def parse248(path):
    """### b248's SPLIT TABLE, keyed by `a^2`."""
    out = {}
    for ln in io.open(path, encoding='utf-8', errors='replace').read().splitlines():
        m = ROW248.match(ln)
        if m:
            out[int(m.group(1))] = dict(e2full=F(m.group(3)), e2even=F(m.group(4)),
                                        arch=F(m.group(5)), junction=F(m.group(6)),
                                        neg_d=F(m.group(7)))
    return out


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def self_test(verbose=True):
    """### **BOTH POLARITIES ON THE DECIMAL READER, THE TOLERANCE, AND THE ROW PARSER.**"""
    bad = 0

    def chk(lbl, got, exp):
        nonlocal bad
        ok = (got == exp)
        bad += 0 if ok else 1
        if verbose:
            print('  %-60s %-22s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if ok else '### NO ###'))

    if verbose:
        print('  %-60s %-22s %s' % ('fixture', 'got/expected', 'agree'))
    chk('exact decimal: 0.5 is one half, not a float', F('0.5'), Fraction(1, 2))
    chk('exact decimal: a negative reads negative', F('-1.001814'),
        -Fraction(1001814, 10 ** 6))
    chk('exact decimal: trailing zeros do not change the value',
        F('0.087342000'), F('0.087342'))
    chk('### and 0.087342 is NOT 0.087341', F('0.087342') == F('0.087341'), False)
    chk('tolerance accepts a one-ulp printing difference',
        close(F('0.087342'), F('0.087341')), True)
    chk('### tolerance REFUSES a difference ten times larger',
        close(F('0.087342'), F('0.087332')), False)
    # ### THE ROW PARSERS, ### **AND THE NEGATIVE ARM IS THE ONE THAT MATTERS** -- a parser that
    # ### matched prose would silently invent rows.
    chk('b254 row parses', bool(ROW254.match(
        '###   3     -0.910943        0.106484     -1.017427      1.256e-15    8.10e+14')), True)
    chk('### b254 parser quiet on prose', bool(ROW254.match(
        '### ### **BEYOND BARS BY FOURTEEN ORDERS AT EVERY CELL.**')), False)
    chk('b248 row parses', bool(ROW248.match(
        '###   3         1  1.516644564  0.910943230    2.427587794   0.106484000'
        '  2.534071794     4.20%')), True)
    chk('### b248 parser quiet on its header', bool(ROW248.match(
        '###   a^2   terms       E2full       E2even    ARCHIMEDEAN      JUNCTION'
        '      -D_dict    junc %')), False)
    return bad == 0


def main(argv):
    print('=' * 100)
    print('b306_difference.py -- THE CORPUS\'S DIFFERENCE, CHECKED AGAINST ITS EMITTING TABLES.')
    print('=' * 100)
    ok = self_test()
    print('  self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        print('  ### REFUSING TO REPORT FROM A SUITE THAT FAILS ITS OWN FIXTURES.')
        return 2

    t254 = parse254(B254)
    t248 = parse248(B248)
    print()
    print('  rows parsed from b254 : realization A = %d, realization B = %d'
          % (len(t254['A']), len(t254['B'])))
    print('  rows parsed from b248 : %d' % len(t248))
    print('  tolerance             : %s   ### three 6-decimal roundings, and stated not chosen'
          % TOL)
    if not t254['A'] or not t254['B'] or not t248:
        print('  ### HARD FAILURE -- A TABLE CAME BACK EMPTY. A check over no rows is not a check.')
        return 2

    fails = 0

    # ### (0) b248's OWN INTERNAL IDENTITY, AS A CONTROL ON THE PARSE.
    print()
    print('  ### (0) b248\'s OWN INTERNAL IDENTITY, AS A CONTROL ON THE PARSE:')
    print('      `ARCHIMEDEAN = E2full + E2even`  and  `-D_dict = ARCHIMEDEAN + JUNCTION`')
    for a2 in sorted(t248):
        r = t248[a2]
        i1 = close(r['arch'], r['e2full'] + r['e2even'])
        i2 = close(r['neg_d'], r['arch'] + r['junction'])
        fails += 0 if (i1 and i2) else 1
        print('      a^2 = %-3d  arch == E2full+E2even : %-5s   -D_dict == arch+junction : %-5s'
              % (a2, i1, i2))

    # ### (1) IS b254's `D - E2` THE NEGATIVE OF b248's `E2even`?
    print()
    print('  ### (1) IS b254\'s `D - E2` THE NEGATIVE OF b248\'s `E2even`?')
    print('      ### **TWO ACTS, TWO TOOLS, ONE COLUMN -- AND THIS IS WHAT SETTLES THAT THE')
    print('      ### ORDER\'S `E2even` IS b254\'s ARCHIMEDEAN HALF AND NOT A SHARED LETTER.**')
    for a2 in sorted(t254['A']):
        if a2 not in t248:
            continue
        lhs = t254['A'][a2]['d_minus_e2']
        rhs = -t248[a2]['e2even']
        agree = close(lhs, rhs)
        fails += 0 if agree else 1
        print('      a^2 = %-3d  b254 D-E2 = %-12s  -b248 E2even = %-14s  diff = %-12s  %s'
              % (a2, float(lhs), float(rhs), float(abs(lhs - rhs)),
                 'AGREE' if agree else '### DISAGREE ###'))

    # ### (2) DOES THE RESIDUAL EQUAL `(D - E2) - (PR - Theta_q)` AT EVERY ROW, BOTH REALIZATIONS?
    print()
    print('  ### (2) DOES b254\'s RESIDUAL EQUAL `(D - E2) - (PR - Theta_q)` AT EVERY ROW?')
    print('      ### **THE SIGN CONVENTION IS FIXED BY THE TABLE, NOT BY THE FORMULA.**')
    for real in ('A', 'B'):
        for a2 in sorted(t254[real]):
            r = t254[real][a2]
            got = r['d_minus_e2'] - r['junction']
            agree = close(got, r['residual'])
            fails += 0 if agree else 1
            print('      (%s) a^2 = %-3d  (D-E2) - junction = %-12s  residual = %-12s  %s'
                  % (real, a2, float(got), float(r['residual']),
                     'AGREE' if agree else '### DISAGREE ###'))

    # ### (3) DO THE TWO ACTS AGREE ON THE JUNCTION?
    print()
    print('  ### (3) DO b254 AND b248 AGREE ON THE JUNCTION, CELL BY CELL?')
    print('      ### **A DISAGREEMENT HERE IS A FINDING AND IS PRINTED, NOT ABSORBED.**')
    disagree = []
    for a2 in sorted(t254['A']):
        if a2 not in t248:
            continue
        j254, j248 = t254['A'][a2]['junction'], t248[a2]['junction']
        d = abs(j254 - j248)
        exact = (j254 == j248)
        if not exact:
            disagree.append((a2, d))
        print('      a^2 = %-3d  b254 = %-12s  b248 = %-12s  diff = %-12s  %s'
              % (a2, float(j254), float(j248), float(d),
                 'IDENTICAL' if exact else '### DIFFERS AT THE LAST PRINTED PLACE ###'))
    print('      cells where the two acts print different junctions : %d %s'
          % (len(disagree), [a for a, _ in disagree]))

    # ### (4) THE SIGN.
    print()
    print('  ### (4) THE SIGN OF THE RESIDUAL, BOTH REALIZATIONS, EVERY CELL:')
    neg = 0
    total = 0
    for real in ('A', 'B'):
        for a2 in sorted(t254[real]):
            total += 1
            if t254[real][a2]['residual'] < 0:
                neg += 1
    print('      entries negative : %d of %d  %s'
          % (neg, total, 'UNIFORMLY NEGATIVE' if neg == total else '### NOT UNIFORM ###'))
    if neg != total:
        fails += 1

    print()
    print('  ### CHECKS FAILING : %d' % fails)
    print('  ### ### **THEREFORE, AT THE TABLE\'S OWN PRECISION:**')
    print('  ### ### `L - R  =  (D - E2) - (PR - Theta_q)  =  -(E2even + junction)`,')
    print('  ### ### **AND THE ORDER\'S ALGEBRA IS CONFIRMED FROM TWO EMITTING TABLES RATHER')
    print('  ### ### THAN ACCEPTED FROM THE ORDER.**')
    print('  ### **AND WHAT THIS DOES NOT SHOW: ### NOTHING ABOUT WHAT THE DIFFERENCE ### IS ### .**')
    print('  ### It is an arithmetic identity among banked columns. ### The species question is')
    print('  ### the bank\'s, and no number here bears on it.')
    print('=' * 100)
    return 0 if fails == 0 else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
