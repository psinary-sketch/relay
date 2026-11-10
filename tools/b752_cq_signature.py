# -*- coding: utf-8 -*-
"""tools/b752_cq_signature.py -- (R362)(4): THE OPENING CONTROL, THE CLASS-GROUP SIGNATURE OF I-109'S NEGATIVE n. Committed before its run.

cQ(n), n <= 3000, recomputed by the route of relay tools/b750_cq_sign.py (that module imported: its recursion, its lattice counts, its
Kronecker symbol and its 60-digit evaluation, unchanged), and compared with data/b750_cq_sign.txt :39 as the control (exactly zero 2498,
nonnegative 399, negative 102, the smallest negative n = 48). Each prime p <= 3000 typed in Q(sqrt -23):
  R  ramified (p = 23);
  I  inert ((-23/p) = -1);
  P  split, its ideals principal (p represented by Q0 = x^2 + xy + 6y^2);
  N  split, its ideals outside the principal class (p represented by Q1 = 2x^2 + xy + 3y^2 and not by Q0).
The types are read two ways, as (R362)(4) orders -- the character (-23/p), and the enumeration of both forms -- with every mismatch printed,
and a third way for the split primes, independent of both forms: the Hilbert class field of Q(sqrt -23) is the splitting field of
x^3 - x - 1, so a split p is P exactly when x^3 - x - 1 has a root mod p (this criterion is the seat's addition, printed as such).
For every n with cQ(n) != 0 (exactly: some log-coefficient nonzero): its factorisation by type and its sign. The table of sign against
"n has a prime factor of type N", four cells; the statement "every n <= 3000 with cQ(n) < 0 has a prime factor of type N" printed TRUE or with
its counterexamples; the reverse printed beside it, n = 4, 6, 8, 12 named; finer regularities (the exponents of 2 and 3, the count of type-N
factors) printed as observations with their exceptions counted. The reading sentence says what was computed and no more. No INSTRUMENTS row.

  python -X utf8 -u tools/b752_cq_signature.py [--bank]      data/b752_cq_signature.txt, written once, LF
Reads nothing external; no network; no lean or lake process. Written at b752 by the Write tool; no identifier of the author in any string here.
"""
import io
import os
import re
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
BANK = os.path.join(RELAY, 'data', 'b752_cq_signature.txt')
CONTROL = os.path.join(RELAY, 'data', 'b750_cq_sign.txt')
NL = '\n'
sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b750_cq_sign as CS   # noqa: E402   ### b750's route, imported whole: N = 3000, its recursion and its evaluation


def control_line():
    """data/b750_cq_sign.txt :39, read by its line: (negative, smallest negative n, exactly zero, nonnegative)."""
    ls = io.open(CONTROL, encoding='utf-8').read().replace('\r', '').split(NL)
    l = ls[38] if len(ls) > 38 else ''
    m = re.search(r'NEGATIVE (\d+) ; THE SMALLEST NEGATIVE n = (\d+).*EXACTLY ZERO (\d+)\).*NONNEGATIVE (\d+)', l)
    return (tuple(int(x) for x in m.groups()) if m else None), l[:200]


def cubic_root_mod(p):
    return any((x * x * x - x - 1) % p == 0 for x in range(p))


def fstr(n, typ):
    return ' . '.join('%d^%d[%s]' % (p, e, typ[p]) if e > 1 else '%d[%s]' % (p, typ[p]) for p, e in sorted(CS.FAC[n].items()))


def main(argv):
    t0 = time.time()
    N = CS.N
    L = ['b752 -- (R362)(4): THE OPENING CONTROL, THE CLASS-GROUP SIGNATURE OF I-109`S NEGATIVE n, n <= %d (%s)' % (N, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### by relay tools/b752_cq_signature.py, committed before its run; cQ by relay tools/b750_cq_sign.py`s route, that module imported unchanged (the recursion of',
         '### SIDE-explicit-formula Schema/ZQ/LogDeriv.lean :63-:65 at v0.38, 14ca5725; rQ the lattice count of m^2 + m k + 6 k^2 = n, EpsteinZQ.lean :59).', '']
    rq0 = CS.form_counts(1, 1, 6, N)
    rq1 = CS.form_counts(2, 1, 3, N)
    cq = CS.recursion(rq0)
    vals = [None, None] + [CS.value(cq[n]) for n in range(2, N + 1)]
    zero = [n for n in range(2, N + 1) if not cq[n]]
    nz = [n for n in range(2, N + 1) if cq[n]]
    neg = [n for n in nz if vals[n] < 0]
    pos = [n for n in nz if vals[n] > 0]
    want, cl = control_line()
    got = (len(neg), neg[0] if neg else None, len(zero), len(pos))
    ctl = want is not None and want == got
    L += ['## THE CONTROL: data/b750_cq_sign.txt :39 against this recomputation',
          '  the bank`s line: %s ...' % cl,
          '  the bank: negative %s, the smallest negative n = %s, exactly zero %s, nonnegative %s' % (want or ('UNREAD',) * 4),
          '  recomputed: negative %d, the smallest negative n = %s, exactly zero %d, nonnegative (nonzero, positive) %d' % got,
          '  ### THE CONTROL %s' % ('AS WANTED' if ctl else 'NOT AS WANTED'), '']
    if not ctl:
        L += ['### ### **THE CONTROL NOT AS WANTED: NOTHING FURTHER READ.**']
        print(NL.join(L))
        return 3
    # ### the types, two ways and a third
    typ, mism, third_bad = {}, [], []
    for p in CS.PR:
        chi = CS.kronecker(CS.D, p)
        by_char = 'R' if chi == 0 else ('I' if chi == -1 else 'S')
        by_enum = 'B' if (rq0[p] and rq1[p]) else ('P' if rq0[p] else ('N' if rq1[p] else 'I'))
        if by_char == 'R':
            t = 'R'
            if p != 23:
                mism.append((p, 'character 0 at p != 23'))
        elif by_char == 'I':
            t = 'I'
            if by_enum != 'I':
                mism.append((p, 'inert by the character, represented by %s' % by_enum))
        else:
            if by_enum in ('P', 'N'):
                t = by_enum
            else:
                t = '?'
                mism.append((p, 'split by the character, the enumeration reads %s' % by_enum))
            if t in ('P', 'N') and cubic_root_mod(p) != (t == 'P'):
                third_bad.append(p)
        typ[p] = t
    cnt = dict((k, sum(1 for p in CS.PR if typ[p] == k)) for k in 'RIPN?')
    L += ['## THE PRIMES p <= %d TYPED IN Q(sqrt -23): %d primes' % (N, len(CS.PR)),
          '  R ramified %d (23) ; I inert %d ; P split principal (Q0) %d ; N split outside the principal class (Q1, not Q0) %d ; unresolved %d' % (cnt['R'], cnt['I'], cnt['P'], cnt['N'], cnt['?']),
          '  the first primes by type: R %s ; I %s ; P %s ; N %s' % tuple(', '.join(str(p) for p in CS.PR if typ[p] == k)[:160] for k in 'RIPN'),
          '  the two ways (the character (-23/p); the enumeration of Q0 and Q1): mismatches %d %s' % (len(mism), mism[:10] or ''),
          '  the third way, the seat`s (a split p is P exactly when x^3 - x - 1 has a root mod p): disagreements %d %s' % (len(third_bad), third_bad[:10] or ''),
          '  note: p = 23 is represented by Q0 (x = -1, y = 2: 1 - 2 + 24), its ideal (sqrt -23) principal; typed R by the character', '']
    hasN = dict((n, any(typ[p] == 'N' for p in CS.FAC[n])) for n in range(2, N + 1))
    omN = dict((n, sum(e for p, e in CS.FAC[n].items() if typ[p] == 'N')) for n in range(2, N + 1))
    L += ['## EVERY n <= %d WITH cQ(n) != 0 (%d): n = its factorisation by type ; its sign ; cQ(n) to 6 places' % (N, len(nz))]
    row = []
    for n in nz:
        row.append('%d = %s ; %s ; %.6f' % (n, fstr(n, typ), '-' if vals[n] < 0 else '+', float(vals[n])))
    for i in range(0, len(row), 4):
        L.append('  ' + '   |   '.join(row[i:i + 4]))
    L.append('')
    a = sum(1 for n in neg if hasN[n])
    b = sum(1 for n in neg if not hasN[n])
    c = sum(1 for n in pos if hasN[n])
    d = sum(1 for n in pos if not hasN[n])
    L += ['## THE TABLE: THE SIGN OF cQ(n) AGAINST "n HAS A PRIME FACTOR OF TYPE N", over the %d n with cQ(n) != 0' % len(nz),
          '                          has a type-N factor    has none',
          '  cQ(n) < 0               %6d                 %6d' % (a, b),
          '  cQ(n) > 0               %6d                 %6d' % (c, d), '']
    cex = [n for n in neg if not hasN[n]]
    L += ['## THE STATEMENT: every n <= %d with cQ(n) < 0 has a prime factor of type N -- %s' % (N, 'TRUE (%d of %d)' % (len(neg), len(neg)) if not cex else
                                                                                              'FALSE, counterexamples %d: %s' % (len(cex), ', '.join('%d = %s' % (n, fstr(n, typ)) for n in cex[:20])))]
    rev_nz = [n for n in nz if hasN[n] and vals[n] > 0]
    rev_all = [n for n in range(2, N + 1) if hasN[n] and not (cq[n] and vals[n] < 0)]
    L += ['## THE REVERSE, BESIDE IT: every n with a prime factor of type N has cQ(n) < 0 -- FALSE: among the n with cQ(n) != 0, %d with a type-N factor and cQ(n) > 0; '
          'among all n <= %d, %d with a type-N factor and cQ(n) >= 0 (exactly zero among them %d)' % (len(rev_nz), N, len(rev_all), sum(1 for n in rev_all if not cq[n])),
          '  named so the bank does not read the type as sufficient (data/b750_cq_sign.txt :35, the opening values): %s' % ' ; '.join(
              '%d = %s, cQ = %.6f, %s' % (n, fstr(n, typ), float(vals[n]), 'type-N factor' if hasN[n] else 'no type-N factor') for n in (4, 6, 8, 12)),
          '  the first twenty with a type-N factor and cQ(n) > 0: %s' % ', '.join(str(n) for n in rev_nz[:20]), '']
    # ### observations
    L += ['## OBSERVATIONS (printed with their exceptions counted; not claims)']
    by_om = {}
    for n in nz:
        k = omN[n]
        by_om.setdefault(k, [0, 0])[0 if vals[n] < 0 else 1] += 1
    L.append('  (o1) the count of type-N prime factors with multiplicity, Omega_N(n), against the sign (n with cQ != 0): %s' % ' ; '.join(
        'Omega_N = %d: negative %d, positive %d' % (k, v[0], v[1]) for k, v in sorted(by_om.items())))
    by_m3 = {}
    for n in nz:
        by_m3.setdefault(omN[n] % 3, [0, 0])[0 if vals[n] < 0 else 1] += 1
    L.append('  (o2) Omega_N(n) mod 3 against the sign: %s' % ' ; '.join('%d: negative %d, positive %d' % (k, v[0], v[1]) for k, v in sorted(by_m3.items())))
    oth = [n for n in nz if any(typ[p] == 'N' and p not in (2, 3) for p in CS.FAC[n])]
    L.append('  (o3) the type-N primes in the n with cQ != 0: 2 and 3 alone in %d of %d; another type-N prime in %d (%s)' % (
        len(nz) - len(oth), len(nz), len(oth), ', '.join('%d = %s ; %s' % (n, fstr(n, typ), '-' if vals[n] < 0 else '+') for n in oth[:12])))
    v23 = {}
    for n in nz:
        k = (CS.FAC[n].get(2, 0), CS.FAC[n].get(3, 0))
        v23.setdefault(k, [0, 0])[0 if vals[n] < 0 else 1] += 1
    L.append('  (o4) the exponents (v_2(n), v_3(n)) against the sign, every pair met: %s' % ' ; '.join(
        '(%d, %d): -%d +%d' % (k[0], k[1], v[0], v[1]) for k, v in sorted(v23.items())))
    mixed = [k for k, v in v23.items() if v[0] and v[1]]
    L.append('  (o5) the pairs (v_2, v_3) that carry both signs: %d of %d %s' % (len(mixed), len(v23), sorted(mixed)[:20]))
    L.append('')
    L += ['## THE READING: computed, for n <= %d, cQ(n) by b750`s route (the control reproduced), the type of each prime in Q(sqrt -23) two ways (and a third for the split '
          'primes), and the sign of every nonzero cQ(n) against its type-N factors; the statement and its reverse are printed as computed over this range and are not '
          'claimed beyond it; the observations are tables, not claims. No INSTRUMENTS row this act; the row carried to a sitting.' % N, '',
          '### ### **THE SIGNATURE, n <= %d: CONTROL AS WANTED (negative %d, smallest 48, exactly zero %d, nonnegative %d) ; PRIMES %d: R %d, I %d, P %d, N %d ; TYPE MISMATCHES %d, THIRD WAY %d ; '
          'THE TABLE (neg & N %d, neg & no N %d, pos & N %d, pos & no N %d) ; THE STATEMENT %s ; THE REVERSE FALSE (%d counterexamples among nonzero) ; %.1f s.**' % (
              N, len(neg), len(zero), len(pos), len(CS.PR), cnt['R'], cnt['I'], cnt['P'], cnt['N'], len(mism), len(third_bad), a, b, c, d,
              'TRUE' if not cex else 'FALSE (%d)' % len(cex), len(rev_nz), time.time() - t0)]
    text = NL.join(L) + NL
    print(text, end='')
    if '--bank' in argv:
        if os.path.exists(BANK):
            sys.exit('### %s EXISTS: THE BANK IS WRITTEN ONCE -- NOTHING WRITTEN' % BANK)
        io.open(BANK, 'w', encoding='utf-8', newline='\n').write(text)
        print('  banked: data/b752_cq_signature.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
