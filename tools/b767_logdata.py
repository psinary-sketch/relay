# -*- coding: utf-8 -*-
"""b767 (R377)(4)(c) L10a: THE TABLE OF THE LOGARITHMS OF THE PRIMES, GENERATED FOR THE KERNEL (data/b767_plan.txt :67-:74).

For each prime p up to 16,390 (the prime form's 1,900, data/b767_certificate.txt :16) an entry: p, the numerators L and H over
D = 2^100, the series' length K and the factors of p - 1. Each entry is computed exactly as the kernel's check reads it
(SIDEExplicitFormula/Window/LogBounds.lean, LPTree.chk): log p = log (p - 1) - log (1 - 1/p), log (p - 1) the sum of its factors'
ends, and -log (1 - 1/p) within S +- E, S the series' first K terms and E = (1/p)^(K+1) / (1 - 1/p) (Mathlib's remainder bound,
Real.abs_log_sub_add_sum_range_le); L the floor and H the ceiling of the two ends over D. K is the least with E <= 2^-112.

The table is written as a search tree keyed by p: three entries at its top and four subtrees, each checked by the kernel in its own
declaration (475 entries or fewer, within KT_CAP 4,100, tools/b766_kdata.py :65). Beside it, for L10b and L10c, the four rational
ends the hand file reads (Euler's constant at 500 by Mathlib's two sequences; log pi by 22/7 and pi's six-digit bounds).

Commands:
  control   the controls alone, nothing written
  write     the controls, then the kernel's data file and the bank data/b767_logdata.txt
Nothing is computed at a zero; no window coefficient, no K(n) and no combination r is read or printed."""
import sys, os, math, hashlib
from fractions import Fraction as F

KPATH = 'D:/SIDE-explicit-formula'
OUT = 'SIDEExplicitFormula/Window/LogData.lean'
BANK = 'data/b767_logdata.txt'
NMAX = 16390
WANT_PRIMES = 1900
D = 2 ** 100
EBOUND = F(1, 2 ** 112)
W = F(2, 10 ** 22)
KT_CAP = 4100
NL = '\n'


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def factor(n):
    out, q = [], 2
    while q * q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            out.append((q, e))
        q += 1
    if n > 1:
        out.append((n, 1))
    return out


def ser_s(p, K):
    s = F(0)
    for k in range(K):
        s += F(1, p) ** (k + 1) / (k + 1)
    return s


def ser_e(p, K):
    return F(1, p) ** (K + 1) / (1 - F(1, p))


def choose_k(p):
    K = 1
    while ser_e(p, K) > EBOUND:
        K += 1
    return K


def fac_lo(tab, fac):
    return sum((F(e) * F(tab[q][0], D) for q, e in fac), F(0))


def fac_hi(tab, fac):
    return sum((F(e) * F(tab[q][1], D) for q, e in fac), F(0))


def fac_prod(fac):
    r = 1
    for q, e in fac:
        r *= q ** e
    return r


def build():
    ps = primes_upto(NMAX)
    tab = {}
    for p in ps:
        fac = factor(p - 1)
        K = choose_k(p)
        s, e = ser_s(p, K), ser_e(p, K)
        L = math.floor((fac_lo(tab, fac) + s - e) * D)
        H = math.ceil((fac_hi(tab, fac) + s + e) * D)
        tab[p] = (L, H, K, fac)
    return ps, tab


def chk(tab, p, ent):
    """the kernel's LPTree.chk, read in Python: each conjunct in its order; the first that fails is named."""
    L, H, K, fac = ent
    if not 2 <= p:
        return 'p below 2'
    if fac_prod(fac) != p - 1:
        return 'the factors` product not p - 1'
    for q, _ in fac:
        if q not in tab:
            return 'a factor not a key'
        if not q < p:
            return 'a factor not below p'
    s, e = ser_s(p, K), ser_e(p, K)
    if not F(L, D) <= fac_lo(tab, fac) + s - e:
        return 'the lower end above'
    if not fac_hi(tab, fac) + s + e <= F(H, D):
        return 'the upper end below'
    if not F(H, D) - F(L, D) <= W:
        return 'the width above 2/10^22'
    return None


def tree_parts(n):
    """the three top indices and the four subtrees' index ranges of the balanced tree over [0, n)."""
    m0 = n // 2
    m1 = m0 // 2
    m2 = (m0 + 1 + n) // 2
    return (m0, m1, m2), ((0, m1), (m1 + 1, m0), (m0 + 1, m2), (m2 + 1, n))


def tree_find(ps, lo, hi, q):
    """the search tree's descent, as LPTree.find takes it, over the balanced tree on ps[lo:hi]."""
    while lo < hi:
        m = (lo + hi) // 2
        if q == ps[m]:
            return m
        if q < ps[m]:
            hi = m
        else:
            lo = m + 1
    return None


def entry_text(ps, tab, i):
    p = ps[i]
    L, H, K, fac = tab[p]
    fl = ', '.join('(%d, %d)' % (q, e) for q, e in fac)
    return '⟨%d, %d, %d, %d, [%s]⟩' % (p, L, H, K, fl)


def emit(ps, tab, lo, hi, ind):
    if lo >= hi:
        return ' ' * ind + 'LPTree.leaf'
    m = (lo + hi) // 2
    head = ' ' * ind + '(LPTree.node ' + entry_text(ps, tab, m)
    return head + NL + emit(ps, tab, lo, m, ind + 2) + NL + emit(ps, tab, m + 1, hi, ind + 2) + ')'


def harmonic(n):
    h = F(0)
    for k in range(1, n + 1):
        h += F(1, k)
    return h


def floor_at(x, n):
    return F(math.floor(x * 10 ** n), 10 ** n)


def ceil_at(x, n):
    return F(math.ceil(x * 10 ** n), 10 ** n)


def lo_of(tab, p):
    return F(tab[p][0], D)


def hi_of(tab, p):
    return F(tab[p][1], D)


def constants(tab):
    """L10b and L10c's ends, each read exactly as the hand file's kernel checks read them."""
    h500 = harmonic(500)
    g_lo = floor_at(h500 - fac_hi(tab, [(3, 1), (167, 1)]), 9)
    g_hi = ceil_at(h500 - fac_lo(tab, [(2, 2), (5, 3)]), 9)
    a = F(392699, 125000)
    b = F(3141593, 1000000)
    x = lo_of(tab, 2) + lo_of(tab, 11) - hi_of(tab, 7) + (1 - F(22) / (7 * a))
    y = hi_of(tab, 2) + hi_of(tab, 11) - lo_of(tab, 7) + (7 * b / 22 - 1)
    p_lo = floor_at(x, 9) - F(1, 10 ** 9)
    p_hi = ceil_at(y, 9) + F(1, 10 ** 9)
    return dict(h500=h500, g_lo=g_lo, g_hi=g_hi, p_lo=p_lo, p_hi=p_hi, p_x=x, p_y=y)


def qtext(q):
    return '%d / %d' % (q.numerator, q.denominator)


def lean_text(ps, tab):
    n = len(ps)
    (m0, m1, m2), blocks = tree_parts(n)
    names = ['lpTA', 'lpTB', 'lpTC', 'lpTD']
    out = ['import SIDEExplicitFormula.Window.LogBounds', '',
           '/-!',
           '# L10a\'s table: the logarithms of the primes up to 16,390, enclosed',
           '',
           'Generated by relay tools/b767_logdata.py. Each entry `⟨p, L, H, K, fac⟩` holds a prime `p`, the numerators `L` and `H`',
           'of its ends over `2 ^ 100`, the series\' length `K` and the factors of `p - 1`. The table is a search tree keyed by `p`:',
           'three entries at its top and four subtrees, each checked by the kernel in its own declaration (`lp_ok_A` to `lp_ok_D`).',
           '-/', '',
           'namespace SIDEExplicitFormula.Window', '']
    for nm, i in (('lpE0', m0), ('lpE1', m1), ('lpE2', m2)):
        out += ['/-- A top entry of the table. -/', 'def %s : LPEntry := %s' % (nm, entry_text(ps, tab, i)), '']
    for nm, (lo, hi) in zip(names, blocks):
        out += ['/-- A subtree of the table: entries %d to %d of %d. -/' % (lo, hi - 1, n), 'def %s : LPTree :=' % nm,
                emit(ps, tab, lo, hi, 2), '']
    out += ['/-- The table. -/',
            'def lpTree : LPTree := LPTree.node lpE0 (LPTree.node lpE1 lpTA lpTB) (LPTree.node lpE2 lpTC lpTD)', '']
    rows = []
    for k in range(0, n, 20):
        rows.append('  ' + ', '.join(str(p) for p in ps[k:k + 20]))
    out += ['/-- The table\'s keys, the primes up to 16,390. -/', 'def lpPrimes : List ℕ := [', (',' + NL).join(rows), ']', '']
    for nm in ('lpE0', 'lpE1', 'lpE2'):
        out += ['theorem lp_ok_%s : lpTree.chk %s = true := by decide +kernel' % (nm[2:].lower(), nm), '']
    for nm in names:
        out += ['theorem lp_ok_%s : %s.all lpTree.chk = true := by decide +kernel' % (nm[3:], nm), '']
    out += ['/-- The check at every entry of the table. -/',
            'theorem lp_all : lpTree.all lpTree.chk = true := by',
            '  show (LPTree.node lpE0 (LPTree.node lpE1 lpTA lpTB) (LPTree.node lpE2 lpTC lpTD)).all lpTree.chk = true',
            '  simp only [LPTree.all, lp_ok_e0, lp_ok_e1, lp_ok_e2, lp_ok_A, lp_ok_B, lp_ok_C, lp_ok_D, Bool.and_self]', '',
            '/-- Each listed prime is a key of the table. -/',
            'theorem lp_keys : ∀ p ∈ lpPrimes, (lpTree.find p).isSome = true := by decide +kernel', '',
            'theorem lp_count : lpPrimes.length = %d := by decide +kernel' % n, '',
            'end SIDEExplicitFormula.Window', '']
    return NL.join(out), blocks


def controls(ps, tab, consts):
    rows = []

    def row(name, ok, detail):
        rows.append((name, ok, detail))

    row('(1) the keys: the primes up to 16,390, 1,900 of them, the largest 16,381', len(ps) == WANT_PRIMES and ps[-1] == 16381,
        '%d, the largest %d' % (len(ps), ps[-1]))
    fails = [(p, chk(tab, p, tab[p])) for p in ps if chk(tab, p, tab[p])]
    row('(2) the kernel`s check, read in Python, at each entry', not fails, 'fails %d%s' % (len(fails), (' ' + repr(fails[:3])) if fails else ''))
    try:
        import flint
        flint.ctx.prec = 400
        bad = []
        for p in ps:
            lg = flint.arb(p).log()
            lo = flint.arb(flint.fmpq(tab[p][0], D))
            hi = flint.arb(flint.fmpq(tab[p][1], D))
            if not ((lg - lo) > 0 and (hi - lg) > 0):
                bad.append(p)
        row('(3) each interval holds log p, read by arb at 400 bits apart from the chain', not bad, 'outside %d' % len(bad))
        g = flint.arb.const_euler()
        lpi = flint.arb.pi().log()
        okg = (g - flint.arb(flint.fmpq(consts['g_lo'].numerator, consts['g_lo'].denominator))) > 0 and \
              (flint.arb(flint.fmpq(consts['g_hi'].numerator, consts['g_hi'].denominator)) - g) > 0
        okp = (lpi - flint.arb(flint.fmpq(consts['p_lo'].numerator, consts['p_lo'].denominator))) > 0 and \
              (flint.arb(flint.fmpq(consts['p_hi'].numerator, consts['p_hi'].denominator)) - lpi) > 0
        row('(4) Euler`s constant and log pi within their ends, read by arb', bool(okg and okp), 'gamma %s, log pi %s' % (okg, okp))
    except ImportError:
        row('(3) arb', False, 'python-flint not importable')
        row('(4) arb', False, 'python-flint not importable')
    widths = [F(tab[p][1] - tab[p][0], D) for p in ps]
    wmax = max(widths)
    row('(5) the widest interval within 2/10^22', wmax <= W, 'the widest %.3e' % float(wmax))
    (m0, m1, m2), blocks = tree_parts(len(ps))
    sizes = [hi - lo for lo, hi in blocks]
    row('(6) four subtrees and three top entries cover the keys once, each block within KT_CAP 4,100',
        sum(sizes) + 3 == len(ps) and max(sizes) <= KT_CAP, 'blocks %s' % sizes)
    miss = [p for p in ps if tree_find(ps, 0, len(ps), p) != ps.index(p)]
    row('(7) the tree`s descent finds each key at its own entry', not miss, 'missed %d' % len(miss))
    p0 = ps[100]
    L, H, K, fac = tab[p0]
    plants = [
        ('L one above', (L + 1, H, K, fac), 'the lower end above'),
        ('H one below', (L, H - 1, K, fac), 'the upper end below'),
        ('a factor dropped', (L, H, K, fac[1:]), 'the factors` product not p - 1'),
        ('a factor not a key', (L, H, K, [(1, 1)] + fac), 'a factor not a key'),
        ('the width planted wide', (L - 10 ** 9, H, K, fac), 'the width above 2/10^22'),
    ]
    got = [(nm, chk(tab, p0, ent), want) for nm, ent, want in plants]
    row('(8) five planted entries, each refused by the conjunct planted', all(g == w for _, g, w in got),
        '; '.join('%s: %s' % (nm, g) for nm, g, _ in got))
    gw = consts['g_hi'] - consts['g_lo']
    pw = consts['p_hi'] - consts['p_lo']
    row('(9) the two constants` widths within 2/10^3', gw <= F(2, 1000) and pw <= F(2, 1000),
        'gamma %.6e, log pi %.6e' % (float(gw), float(pw)))
    row('(10) the log pi ends strict against the kernel`s two sums', consts['p_lo'] < consts['p_x'] and consts['p_y'] < consts['p_hi'],
        'below by %.1e, above by %.1e' % (float(consts['p_x'] - consts['p_lo']), float(consts['p_hi'] - consts['p_y'])))
    return rows


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd not in ('control', 'write'):
        print('usage: b767_logdata.py control | write')
        return 2
    ps, tab = build()
    consts = constants(tab)
    rows = controls(ps, tab, consts)
    good = sum(1 for _, ok, _ in rows if ok)
    for nm, ok, det in rows:
        print('  %-100s %s ; %s' % (nm, 'AS WANTED' if ok else 'NOT AS WANTED', det))
    print('### CONTROLS %d OF %d AS WANTED' % (good, len(rows)))
    kmax = max(tab[p][2] for p in ps)
    ksum = sum(tab[p][2] for p in ps)
    print('  the series` lengths: the most %d (at 2), the sum %d' % (kmax, ksum))
    print('  gamma between %s and %s ; log pi between %s and %s' % (qtext(consts['g_lo']), qtext(consts['g_hi']), qtext(consts['p_lo']),
                                                                    qtext(consts['p_hi'])))
    if good != len(rows):
        print('### NOTHING WRITTEN: a control not as wanted')
        return 1
    if cmd == 'control':
        return 0
    text, blocks = lean_text(ps, tab)
    data = text.encode('utf-8')
    path = os.path.join(KPATH, OUT)
    with open(path, 'wb') as f:
        f.write(data)
    sha = hashlib.sha256(data).hexdigest()
    nlines = text.count(NL)
    bank = ['b767 -- (R377)(4)(c) L10a: THE TABLE OF THE LOGARITHMS OF THE PRIMES, GENERATED FOR THE KERNEL (tools/b767_logdata.py write)',
            '', '## THE CONTROLS']
    for nm, ok, det in rows:
        bank.append('  %s: %s ; %s' % (nm, 'AS WANTED' if ok else 'NOT AS WANTED', det))
    bank += ['  CONTROLS %d OF %d AS WANTED' % (good, len(rows)), '', '## THE TABLE',
             '  keys %d (the primes up to 16,390) ; scale 2^100 ; the remainder bound 2^-112 ; the series` lengths the most %d, the sum %d'
             % (len(ps), kmax, ksum),
             '  blocks %s and three top entries ; the widest interval %.3e against 2/10^22' %
             ([hi - lo for lo, hi in blocks], float(max(F(tab[p][1] - tab[p][0], D) for p in ps))),
             '  the kernel`s file %s: %d lines, %d bytes, sha256 %s' % (OUT, nlines, len(data), sha),
             '', '## L10b AND L10c`S ENDS (the hand file SIDEExplicitFormula/Window/LogConst.lean reads them)',
             '  gLo %s ; gHi %s (Euler`s constant by Mathlib`s two sequences at 500, log 501 and log 500 from the table)' %
             (qtext(consts['g_lo']), qtext(consts['g_hi'])),
             '  pLo %s ; pHi %s (log pi by 22/7, pi`s six-digit bounds and log y between 1 - 1/y and y - 1)' %
             (qtext(consts['p_lo']), qtext(consts['p_hi'])),
             '', 'Nothing computed at a zero; no window coefficient, no K(n) and no combination r read or printed.', '']
    btext = NL.join(bank)
    with open(BANK, 'w', encoding='utf-8', newline='\n') as f:
        f.write(btext)
    print('  WRITTEN: %s (%d lines, %d bytes, sha256 %s) ; %s' % (OUT, nlines, len(data), sha[:16], BANK))
    return 0


if __name__ == '__main__':
    sys.exit(main())
