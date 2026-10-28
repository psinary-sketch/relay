# -*- coding: utf-8 -*-
"""b722_c2.py -- THE C2 STATEMENT FOR LEAN, (R332)(5): WRITTEN, GRADED AT E0, THEN PRICED PER FIELD. Written whole at b722 by the Write tool.

  statement [dry]  writes data/b722_c2_statement.txt: the Lean text alone -- its definitions and the theorem's statement, no proof term, not
                   compiled, no Lean file anywhere; vanilla Lean 4 (Int, Nat, List; no Mathlib, no Rat).
  price [dry]      reads that file back, cuts the theorem's header (the text after its name), grades it by relay tools/e0_rule.py grade
                   (imported unedited), prints the completeness of the list as a SCOPE sentence beside the grade; then MIRRORS the file's
                   definitions in Python (the statement as written, read true or false at each of the eighteen, exact integers); then prices
                   each field: (A) decide on the definitions as written, in the kernel without sharing -- the lattice points the box of rQ
                   enumerates for every n <= n0 and the ordered factorizations F walks; (B) beside it the certificate route -- one sweep of
                   the lattice points with Q <= n0 and the Omega recursion over divisor pairs, each field's work against the bound the seat
                   prints (BOUND), the two general lemmas the route needs named and not proved. -> data/b722_c2_price.txt
NOTHING RUNS LEAN AND NOTHING IS DISPATCHED: the prices are counts computed in Python, not timings.
"""
import io
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import e0_rule as E0    # noqa: E402  ### the shared E0 rule, imported unedited

ACT = 'b722'
STMT = '%s_c2_statement.txt' % ACT
PRICE = '%s_c2_price.txt' % ACT
L_SCALE = 360360        # ### lcm(1, ..., 15)
K_MAX = 15              # ### n < 2^16 has Omega(n) <= 15
BOUND = 10 ** 6         # ### the seat's bound per field for the certificate route: lattice points plus divisor pairs
# ### the walk (data/b721_registrations.txt :31-:48; -20, -35, -40 from data/b719_coeffs.txt :16 and data/b720_coeffs.txt :57), each computed
# ### at b722 (data/b722_walk.txt) or banked: (D, n0, value numerator, value denominator)
WALK = [(-15, 24, -2, 1), (-20, 36, -2, 1), (-24, 36, -1, 2), (-35, 135, -2, 1), (-40, 100, -1, 2), (-51, 225, -2, 1), (-52, 196, -2, 1),
        (-88, 484, -1, 2), (-91, 875, -2, 1), (-115, 1225, -2, 1), (-123, 1089, -2, 1), (-148, 1444, -2, 1), (-187, 3773, -2, 1),
        (-232, 3364, -1, 2), (-235, 4225, -2, 1), (-267, 4761, -2, 1), (-403, 17303, -2, 1), (-427, 14161, -2, 1)]
SCOPE = ('SCOPE (beside the statement, not a binder): the list `walk` names the eighteen imaginary quadratic fields of class number 2 by '
         'their discriminants; that no other exists is Baker (1971) and Stark (1975), cited and not compiled. The theorem quantifies over the '
         'list; it says nothing of a field off it.')


def lean_text():
    rows = ',\n   '.join('(%d, %d, %d, %d)' % w for w in WALK)
    return '''-- b722 -- THE C2 STATEMENT, (R332)(5): the Lean text alone. Statement and definitions; no proof term; not compiled; vanilla Lean 4
-- (Int, Nat, List; no Mathlib, no Rat). No Lean file in any kernel holds it.

namespace C2Walk

/-- the walk: (D, n0, v, q) -- at the discriminant D the least n with b(n) < 0 is n0 and b(n0) = v / q.
    The eighteen imaginary quadratic fields of class number 2 (completeness: Baker 1971, Stark 1975; cited, not compiled). -/
def walk : List (Int × Nat × Int × Nat) :=
  [%s]

/-- the principal form of discriminant D < 0, D ≡ 0 or 1 mod 4: x² + D·y²/(-4) or x² + xy + (1 - D)/4 · y² -/
def pform (D x y : Int) : Int :=
  if D %% 4 = 0 then x * x + (-D / 4) * y * y else x * x + x * y + ((1 - D) / 4) * y * y

/-- r_Q(n): the number of (x, y) with Q(x, y) = n, by finite enumeration over the box [-n, n]² (every representation lies in it,
    since Q(x, y) ≥ (x² + y²)/2 for the principal form of D < -4) -/
def rQ (D : Int) (n : Nat) : Nat :=
  ((List.range (2 * n + 1)).flatMap fun i => (List.range (2 * n + 1)).map fun j => ((i : Int) - n, (j : Int) - n)).countP
    fun p => decide (pform D p.1 p.2 = (n : Int))

/-- a(n) = r_Q(n) / 2 (two units) -/
def aQ (D : Int) (n : Nat) : Int := (rQ D n : Int) / 2

/-- F D k n: the sum over the ordered factorizations n = d₁ ⋯ d_k, every dᵢ ≥ 2, of a(d₁) ⋯ a(d_k) -/
def F (D : Int) : Nat → Nat → Int
  | 0, n => if n = 1 then 1 else 0
  | k + 1, n => ((List.range (n + 1)).filter fun d => decide (2 ≤ d ∧ n %% d = 0)).foldl (fun s d => s + aQ D d * F D k (n / d)) 0

/-- L · b(n), L = %d = lcm(1, …, 15): b(n), the coefficient of n^-s in log(Z_Q / 2), is SUM over k ≥ 1 of (-1)^(k+1) F_k(n) / k,
    and k ≤ 15 for n < 2^16 -/
def bL (D : Int) (n : Nat) : Int :=
  (List.range %d).foldl (fun s i => s + (if i %% 2 = 0 then 1 else -1) * (%d / ((i : Int) + 1)) * F D (i + 1) n) 0

/-- THE C2 VALUE LAW AT THE LEAST NEGATIVE INDEX, at each field of the list: b(n0) = v / q, and b(n) ≥ 0 for 2 ≤ n < n0. -/
theorem c2_value_law (D : Int) (n0 : Nat) (v : Int) (q : Nat) (hD : (D, n0, v, q) ∈ walk) : ((q : Int) * bL D n0 = v * %d) ∧ ∀ n, 2 ≤ n → n < n0 → 0 ≤ bL D n

end C2Walk
''' % (rows, L_SCALE, K_MAX, L_SCALE, L_SCALE)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _put(name, text):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)


def statement(*a):
    t = lean_text()
    print(t)
    if 'dry' in a:
        return
    _put(STMT, t)
    print('written data/%s' % STMT)


# ================================================================================ THE MIRROR (the file's definitions, in Python)
def pform(Dd, x, y):
    return x * x + (-Dd // 4) * y * y if Dd % 4 == 0 else x * x + x * y + ((1 - Dd) // 4) * y * y


def a_table(Dd, N):
    """aQ for n <= N by one sweep of the box [-B, B]^2, B^2 <= 2N (the file's box [-n, n]^2 holds every representation: Q >= (x^2+y^2)/2)."""
    r = [0] * (N + 1)
    B = 1
    while B * B <= 2 * N:
        B += 1
    for x in range(-B, B + 1):
        for y in range(-B, B + 1):
            v = pform(Dd, x, y)
            if 1 <= v <= N:
                if abs(x) > v or abs(y) > v:
                    sys.exit('### A REPRESENTATION OUTSIDE THE FILE`S BOX [-n, n]^2 AT %d: (%d, %d) -> %d' % (Dd, x, y, v))
                r[v] += 1
    if any(x % 2 for x in r[1:]):
        sys.exit('### AN ODD r_Q(n) AT %d -- the two units' % Dd)
    pts = sum(1 for x in range(-B, B + 1) for y in range(-B, B + 1) if pform(Dd, x, y) <= N)
    return [x // 2 for x in r], pts


def divisors_ge2(N):
    dv = [[] for _ in range(N + 1)]
    for d in range(2, N + 1):
        for m in range(d, N + 1, d):
            dv[m].append(d)
    return dv


def mirror(Dd, n0):
    """the file's bL at every n <= n0, exactly: F(k, n) by its own recursion (shared here, the kernel shares nothing)."""
    a, pts = a_table(Dd, n0)
    dv = divisors_ge2(n0)
    F = [[1 if n == 1 else 0 for n in range(n0 + 1)]]
    for k in range(1, K_MAX + 1):
        prev = F[-1]
        F.append([sum(a[d] * prev[n // d] for d in dv[n]) if n >= 2 else 0 for n in range(n0 + 1)])
    bL = [sum((1 if i % 2 == 0 else -1) * (L_SCALE // (i + 1)) * F[i + 1][n] for i in range(K_MAX)) for n in range(n0 + 1)]
    return a, bL, pts, dv


def prices(n0, a, dv):
    """(A) decide as written, no sharing: the lattice points rQ's box enumerates and the factorizations F walks; (B) the certificate."""
    # ### (A): bL n calls F (i+1) n for i < 15; F (k+1) n scans range(n+1) and, per divisor d >= 2, evaluates aQ d (a box of (2d+1)^2 points)
    # ### and F k (n/d). cost[k][n] = (lattice points, divisor-scan steps, factorization terms) with no sharing.
    lp = [[0] * (n0 + 1) for _ in range(K_MAX + 1)]
    sc = [[0] * (n0 + 1) for _ in range(K_MAX + 1)]
    for k in range(1, K_MAX + 1):
        for n in range(1, n0 + 1):
            lp[k][n] = sum((2 * d + 1) ** 2 + lp[k - 1][n // d] for d in dv[n])
            sc[k][n] = (n + 1) + sum(sc[k - 1][n // d] for d in dv[n])
    A_lp = sum(sum(lp[k][n] for k in range(1, K_MAX + 1)) for n in range(2, n0 + 1))
    A_sc = sum(sum(sc[k][n] for k in range(1, K_MAX + 1)) for n in range(2, n0 + 1))
    H = [0] * (n0 + 1)
    H[1] = 1
    for n in range(2, n0 + 1):
        H[n] = sum(H[n // d] for d in dv[n])
    A_fact = sum(H[2:])
    A_fact_nz = None
    Hn = [0] * (n0 + 1)
    Hn[1] = 1
    for n in range(2, n0 + 1):
        Hn[n] = sum(Hn[n // d] for d in dv[n] if a[d])
    A_fact_nz = sum(Hn[2:])
    B_pairs = sum(len(dv[n]) for n in range(2, n0 + 1))
    return dict(A_lp=A_lp, A_scan=A_sc, A_fact=A_fact, A_fact_nonzero=A_fact_nz, B_pairs=B_pairs)


def header_of(t):
    m = re.search(r'theorem c2_value_law(.*?)\n\nend C2Walk', t, re.S)
    if not m:
        sys.exit('### THE THEOREM`S HEADER NOT FOUND IN data/%s' % STMT)
    return m.group(1).strip()


def sci(x):
    return '%.2e' % x


def price(*a):
    t0 = time.time()
    t = io.open(os.path.join(D, STMT), encoding='utf-8').read().replace(chr(13), '')
    if t != lean_text():
        sys.exit('### data/%s IS NOT THE TEXT THIS TOOL WRITES -- NOTHING READ' % STMT)
    head = header_of(t)
    st = E0.self_test()
    g, why, read = E0.grade(head, 'theorem')
    bs = E0.binders_of(head)
    L = ['%s -- (R332)(5): THE C2 STATEMENT GRADED AT E0, THEN PRICED PER FIELD (%s)' % (ACT, utc()), '',
         '### data/%s holds the Lean text alone (written by tools/%s_c2.py statement); read back here, equal to the text the tool writes.' % (STMT, ACT),
         '### NOTHING RUNS LEAN, NOTHING IS DISPATCHED: every price below is a count computed in Python, not a timing.', '',
         '## (1) THE E0 GRADE (relay tools/e0_rule.py, imported unedited; its self-test %s)' % ('PASS' if st else '### FAIL')]
    L += ['  ' + x for x in E0.RULE_TEXT[:6]]
    L += ['  THE HEADER GRADED: theorem c2_value_law ' + head]
    L += ['  binder %-10s %-6s : %-28s %s ; class %s ; outcome %s' % (b['kind'], b['name'], b['type'][:28], b['typing'], b['cls'], b['outcome']) for b in bs]
    L += ['  THE GRADE: %s -- %s' % (g, why), '  ' + SCOPE, '']
    L += ['## (2) THE STATEMENT AS WRITTEN, MIRRORED IN PYTHON (the file`s pform, rQ`s box, aQ, F, bL; exact integers): at each field b(n0)',
          '## = v/q and b(n) >= 0 for 2 <= n < n0, read from bL, and the least n with bL(n) < 0']
    rows, ok_all = [], True
    for Dd, n0, v, q in WALK:
        a_, bL, pts, dv = mirror(Dd, n0)
        neg = [n for n in range(2, n0 + 1) if bL[n] < 0]
        holds = q * bL[n0] == v * L_SCALE and all(bL[n] >= 0 for n in range(2, n0))
        ok_all &= holds
        pr = prices(n0, a_, dv)
        rows.append((Dd, n0, v, q, holds, neg[0] if neg else None, pts, pr))
        L.append('  D %-5d n0 %-6d value %s ; bL(n0) = %d = %s x L ; the least n with bL < 0: %s ; THE STATEMENT AT D: %s' % (
            Dd, n0, '%d/%d' % (v, q) if q > 1 else v, bL[n0], ('%d/%d' % (v, q)) if q > 1 else v, neg[0] if neg else 'NONE',
            'TRUE' if holds else '### FALSE'))
    L += ['  THE STATEMENT AS WRITTEN, IN PYTHON: TRUE AT %d OF 18' % sum(1 for r in rows if r[4]), '']
    L += ['## (3) THE PRICE PER FIELD, BEFORE ANY PROOF',
          '### (A) decide in vanilla Lean, axiom-free, no native_decide, on the definitions as written, the kernel sharing nothing: LP the lattice',
          '###     points rQ`s box [-d, d]^2 enumerates at every aQ d evaluated, SCAN the divisor-scan steps of F`s range filters, both summed over',
          '###     bL n for every n in 2..n0 (the bounded forall) and n0; FACT the ordered factorizations into factors >= 2 of every n <= n0 (all;',
          '###     those with every a(d) nonzero beside it).',
          '### (B) the certificate route: aQ at every n <= n0 by ONE sweep of the lattice points with Q <= n0 (LP*), and b by the Omega recursion',
          '###     Omega(n) b(n) = Omega(n) a(n) - SUM_{d | n, 1 < d < n} Omega(d) b(d) a(n/d) over the divisor pairs (PAIRS) -- tools/b718_classgroup.py',
          '###     log_coeffs`s route; its two general lemmas, (L1) the sweep`s table equals rQ and (L2) the Omega recursion equals the ordered-',
          '###     factorization sum (Omega a derivation of the Dirichlet ring), proved once and not per field, NAMED HERE AND NOT PROVED.',
          '### THE SEAT`S BOUND for (B): %s elementary operations (LP* + PAIRS) per field, a bound chosen, not measured.' % sci(BOUND)]
    L.append('  %-6s %-6s | %-9s %-9s %-9s %-9s | %-7s %-8s %-9s %s' % ('D', 'n0', 'A: LP', 'A: SCAN', 'A: FACT', 'FACT a!=0', 'B: LP*', 'B: PAIRS',
                                                                       'B: TOTAL', 'UNDER THE BOUND'))
    under = 0
    for Dd, n0, v, q, holds, nn, pts, pr in rows:
        tot = pts + pr['B_pairs']
        under += tot <= BOUND
        L.append('  %-6d %-6d | %-9s %-9s %-9s %-9s | %-7d %-8d %-9d %s' % (
            Dd, n0, sci(pr['A_lp']), sci(pr['A_scan']), sci(pr['A_fact']), sci(pr['A_fact_nonzero']), pts, pr['B_pairs'], tot,
            'YES' if tot <= BOUND else '### NO'))
    big = max(rows, key=lambda r: r[1])
    L += ['', '### THE READING: route (A) at -403 (n0 17303) enumerates %s lattice points and %s scan steps -- decide on the definitions as '
          'written is out of reach of the kernel at every field but the smallest; route (B) keeps each field at or under %s operations at %d of '
          '18 fields (the largest -403: %d), the lemmas (L1) and (L2) its price beside the counts. Where the compile lives is the author`s word '
          'at (13); no Lean file is written and nothing is dispatched.' % (
              sci(big[7]['A_lp']), sci(big[7]['A_scan']), sci(BOUND), under, big[6] + big[7]['B_pairs']),
          '', '### ### **THE C2 STATEMENT: E0 %s ; SCOPE BESIDE IT (Baker 1971, Stark 1975, cited) ; AS WRITTEN, TRUE IN PYTHON AT %d OF 18 ; '
          'PRICED: (A) decide as written OUT OF REACH, (B) THE CERTIFICATE ROUTE UNDER %s AT %d OF 18, TWO LEMMAS NAMED ; %d s.**' % (
              g, sum(1 for r in rows if r[4]), sci(BOUND), under, int(time.time() - t0))]
    print(NL.join(L))
    if 'dry' in a:
        return
    _put(PRICE, NL.join(L) + NL)
    print('written data/%s' % PRICE)


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = dict(statement=statement, price=price).get(route)
    if fn is None:
        sys.exit('usage: b722_c2.py statement [dry] | price [dry]')
    fn(*sys.argv[2:])
