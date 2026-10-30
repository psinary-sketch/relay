# -*- coding: utf-8 -*-
"""b725_c2.py -- (R335)(3)(iv), (4)(iv): THE C2 THEOREM BY THE CERTIFICATE ROUTE, ITS CONTROLS BEFORE ANY LEAN.

### routes:
###   e0        the statement as data/b722_c2_statement.txt writes it, its header graded by relay tools/e0_rule.py (imported unedited) --
###             printed before any proof term is written ((R335)(3)(iv), the registration's CONTROL BEFORE ANY PROOF)
###   mirror    route (B) in Python in the arithmetic SIDEExplicitFormula/C2Walk.lean's definitions use -- the sweep over the box
###             [-s, s]^2 (s the least with s*s > 2N), the Omega function by trial division, the Omega recursion with exact division --
###             against the statement's own bL (tools/b722_c2.py mirror, imported unedited: F by its recursion, the box [-n, n]^2 checked)
###             at every n <= n0 at each of the eighteen fields; any inexact division or unequal value printed and the route refused
###   bank      both, written to data/b725_c2.txt (the Lean grades appended by hand after the dispatch's read)
### Nothing here runs Lean or dispatches. Written by the Write tool.
"""
import io
import os
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
import e0_rule as E0      # noqa: E402  ### the shared E0 rule, imported unedited
import b722_c2 as C2      # noqa: E402  ### b722's statement text, mirror and header reader, imported unedited

D = os.path.join(os.path.dirname(T), 'data')
BANK = os.path.join(D, 'b725_c2.txt')
L_SCALE = 360360


def e0_lines():
    t = io.open(os.path.join(D, C2.STMT), encoding='utf-8').read().replace(chr(13), '')
    same = t == C2.lean_text()
    head = C2.header_of(t)
    g, why, read = E0.grade(head, 'theorem')
    return ['## (1) THE E0 GRADE AT THE STATEMENT, BEFORE ANY PROOF (relay tools/e0_rule.py, imported unedited; its self-test %s)'
            % ('PASS' if E0.self_test() else '### FAIL'),
            '  the statement: data/%s, equal to tools/b722_c2.py`s text: %s' % (C2.STMT, same),
            '  THE HEADER GRADED: theorem c2_value_law %s' % head,
            '  THE GRADE: %s -- %s' % (g, why),
            '  SCOPE (beside the statement, not a binder): the list `walk` names the eighteen imaginary quadratic fields of class number 2; that '
            'no other exists is Baker (1971) and Stark (1975), cited and not compiled.'], g


def omega(n):
    """Omega(n), the prime factors with multiplicity, by trial division -- C2Walk.lean's omegaAux with fuel n + 1."""
    k, p = 0, 2
    while n >= 2:
        if p * p > n:
            return k + 1
        if n % p == 0:
            k, n = k + 1, n // p
        else:
            p += 1
    return k


def sweep(Dd, N):
    s = 0
    while not s * s > 2 * N:
        s += 1
    r = [0] * (N + 1)
    pts = 0
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = C2.pform(Dd, x, y)
            if v <= N:
                pts += 1
                if v >= 0:
                    r[v] += 1
    return [x // 2 for x in r], pts, s


def b_table(Dd, N, a):
    """L * b(n) for n <= N by the Omega recursion: Omega(n) bL(n) = Omega(n) L a(n) - SUM_{d | n, 1 < d < n} Omega(d) bL(d) a(n/d)."""
    B = []
    pairs = 0
    for n in range(N + 1):
        if n < 2:
            B.append(0)
            continue
        s = 0
        for d in range(2, n):
            if n % d == 0:
                pairs += 1
                s += omega(d) * B[d] * a[n // d]
        num = omega(n) * L_SCALE * a[n] - s
        if num % omega(n):
            return None, pairs, 'INEXACT DIVISION AT n = %d' % n
        B.append(num // omega(n))
    return B, pairs, ''


def w_cert(Dd, n0, v, q, a):
    """C2Walk.lean's cert as written: W(n) = Omega(n) L a(n) - SUM over d | n, 2 <= d, d * d <= n, of W(d) a(n/d) (+ W(n/d) a(d) where
    n/d != d); the certificate: Omega(n0) divides W(n0), q (W(n0) / Omega(n0)) = v L, and W(n) >= 0 for 2 <= n < n0."""
    W = [0] * (n0 + 1)
    for n in range(2, n0 + 1):
        s, d = 0, 2
        while d * d <= n:
            if n % d == 0:
                e = n // d
                s += W[d] * a[d] if e == d else W[d] * a[e] + W[e] * a[d]
            d += 1
        W[n] = omega(n) * L_SCALE * a[n] - s
    o = omega(n0)
    return W, W[n0] % o == 0 and q * (W[n0] // o) == v * L_SCALE and all(W[n] >= 0 for n in range(2, n0))


def mirror_lines():
    L, ok_all = ['', '## (2) ROUTE (B) MIRRORED IN PYTHON IN C2Walk.lean`s ARITHMETIC, AGAINST THE STATEMENT`S OWN bL AT EVERY n <= n0'], True
    n_ok = 0
    for Dd, n0, v, q in C2.WALK:
        aS, pts, s = sweep(Dd, n0)
        a, bL, _p, _dv = C2.mirror(Dd, n0)
        B, pairs, err = b_table(Dd, n0, aS)
        eq_a = aS[1:] == a[1:]
        eq_b = B is not None and B[2:] == bL[2:]
        cert = B is not None and q * B[n0] == v * L_SCALE and all(B[n] >= 0 for n in range(2, n0)) and B[n0] < 0
        W, wc = w_cert(Dd, n0, v, q, aS)
        eq_w = B is not None and all(W[n] == omega(n) * B[n] for n in range(2, n0 + 1))
        ok = eq_a and eq_b and cert and eq_w and wc and not err
        ok_all = ok_all and ok
        n_ok += ok
        L.append('  D %-5d n0 %-6d box s %-4d points %-6d pairs %-7d | a equal %s ; bL equal at 2..n0 %s ; the certificate (q bL(n0) = v L, '
                 'bL >= 0 below n0) %s ; W = Omega bL at 2..n0 %s ; the Lean cert (W form) %s%s'
                 % (Dd, n0, s, pts, pairs, eq_a, eq_b, cert, eq_w, wc, (' ; ' + err) if err else ''))
    L.append('  THE ROUTE AS THE LEAN DEFINITIONS COMPUTE IT: %s AT %d OF %d' % ('EQUAL TO THE STATEMENT AND THE CERTIFICATE TRUE' if ok_all
                                                                              else '### NOT EQUAL', n_ok, len(C2.WALK)))
    return L, ok_all


def e0(*a):
    print('\n'.join(e0_lines()[0]))


def mirror(*a):
    print('\n'.join(mirror_lines()[0]))


def bank(*a):
    t0 = time.time()
    e, g = e0_lines()
    m, ok = mirror_lines()
    L = ['b725 -- (R335)(3)(iv), (4)(iv): THE C2 THEOREM BY THE CERTIFICATE ROUTE -- THE E0 GRADE FIRST, THE ROUTE MIRRORED, THEN THE BRANCH (%s)'
         % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### Written by tools/b725_c2.py bank before any Lean file of (iv) is written; nothing here runs Lean or dispatches. The Lean tree, its',
         '### one dispatch and its grades are appended below by the Edit tool after the read.', ''] + e + m
    L += ['', '### ### **THE C2 STATEMENT: E0 %s ; ROUTE (B) IN THE LEAN DEFINITIONS` ARITHMETIC %s AT 18 OF 18 ; %d s.**'
          % (g, 'EQUAL TO THE STATEMENT, THE CERTIFICATE TRUE' if ok else 'NOT EQUAL', time.time() - t0)]
    io.open(BANK, 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
    print('\n'.join(L))
    print('written data/b725_c2.txt')


ROUTES = dict(e0=e0, mirror=mirror, bank=bank)

if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ROUTES:
        sys.exit('### routes: %s' % ' | '.join(ROUTES))
    ROUTES[r](*sys.argv[2:])
