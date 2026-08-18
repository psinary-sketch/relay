"""B11(1) — THE CORRECTION FACTOR DISCRIMINATED: the n-trend of the quotient trace's
per-lag ratio, in EXACT RATIONAL arithmetic (no floats, no dense matrices).

Relay-only. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.
POSITIVITY GUARD: nothing here bears on h2.

THE QUANTITY, EXACT
===================
On the model, T_quot(k) = p^{-k/2} * R(k) where R(k) is RATIONAL:
    R(k) = Sum_{orbit classes j} #{(a,b) in class_j^2 : p^k a == b mod p^{2n}} / |class_j|
(the 0/1 pushforward matrix traced against the normalized class indicators). Computed with
Fractions -- the exact rationals ARE the bank; denominators are DATA, checked against the
p+1 and p^n+1 patterns BEFORE any trend is read (registered order of operations).
The per-lag ratio r_k(n) = T(k+1)/T(k) = p^{-1/2} * R(k+1)/R(k).

REGISTERED VERDICT MAP (both branches longhand, before any number)
==================================================================
F1  GENUINE: at fixed k, r_k(n) -> sqrt(p)/(p+1) as n grows (equivalently
    R(k+1)/R(k) -> p/(p+1)): the (1+p^{-1})^{-1} is a local Euler-type factor and the
    quotient trace carries local zeta structure natively -- column (i) entering the
    trace; MODEL GRADE, OURS, NO PROMOTION.
F2  TRUNCATION: r_k(n) -> p^{-1/2} (R-ratio -> 1): the factor dies with the cutoff,
    leaving the pure Weil weight q^{-1/2}.
F3  third shape, filed openly.
The k >= n truncation edge is respected (only k <= n-2 ratios read for trend).

CELLS: p in {2,3,5,7}; n up to the grid limit (N = p^{2n} <= ~2*10^5, sparse union-find
and orbit-wise pair counts -- no matrices).

Usage:  python b11_factor.py register | run
"""
import sys
from fractions import Fraction


def orbits(p, n):
    N = p ** (2 * n)
    pn = p ** n
    parent = list(range(N))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for m in range(N):
        if m % pn != 0:
            m2 = (p * m) % N
            if m2 % pn != 0:
                ra, rb = find(m), find(m2)
                if ra != rb: parent[ra] = rb
    cls = {}
    for m in range(N):
        if m % pn != 0:
            cls.setdefault(find(m), []).append(m)
    return N, list(cls.values())


def R_exact(p, n, kmax):
    N, classes = orbits(p, n)
    out = []
    for k in range(1, kmax + 1):
        pk = pow(p, k, N)
        tot = Fraction(0)
        for mem in classes:
            s = set(mem)
            cnt = sum(1 for a in mem if (pk * a) % N in s and True)
            # count ordered pairs (a,b) with p^k a == b: b determined by a; count a with image in class
            tot += Fraction(cnt, len(mem))
        out.append(tot)
    return N, len(classes), out


def registration():
    print("=" * 100)
    print("B11(1) — REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("  the two reference ratios per p (R-ratio form):")
    for p in (2, 3, 5, 7):
        print("    p=%d   F1: p/(p+1) = %d/%d     F2: 1" % (p, p, p + 1))
    print("=" * 100)
    sys.stdout.flush()


def run():
    CELLS = {2: [2, 3, 4, 5, 6, 7], 3: [2, 3, 4, 5], 5: [2, 3], 7: [2]}
    print("  %-3s %-3s %-9s %-9s %-46s" % ("p", "n", "N", "dimVinv", "R(k) exact, k=1..min(2n-1, 6)"))
    bank = {}
    for p, ns in CELLS.items():
        for n in ns:
            N = p ** (2 * n)
            if N > 250000:
                continue
            kmax = min(2 * n - 1, 6)
            N, d, Rs = R_exact(p, n, kmax)
            bank[(p, n)] = Rs
            print("  %-3d %-3d %-9d %-9d %s" % (p, n, N, d, "  ".join(str(r) for r in Rs)))
            sys.stdout.flush()
    print("\n  DENOMINATOR CHECK (registered to run before the trend is read):")
    for (p, n), Rs in sorted(bank.items()):
        dens = [r.denominator for r in Rs if r != 0]
        pats = []
        for dd in dens:
            tag = []
            if dd == 1: tag.append("1")
            if dd == p + 1: tag.append("p+1")
            for j in range(1, 2 * n):
                if dd == p ** j + 1: tag.append("p^%d+1" % j)
                if dd == (p ** j - 1): tag.append("p^%d-1" % j)
                if (p ** j - 1) % dd == 0 and dd > 1: tag.append("| p^%d-1" % j); break
            pats.append("%d[%s]" % (dd, ",".join(tag) if tag else "?"))
        print("    (p=%d,n=%d): %s" % (p, n, "  ".join(pats)))
    print("\n  THE n-TREND AT FIXED k (R(k+1)/R(k), read only k <= n-2):")
    for p in (2, 3, 5, 7):
        print("    p=%d  target F1 = %s = %.6f   F2 = 1" % (p, Fraction(p, p + 1), p / (p + 1)))
        for k in (1, 2, 3):
            row = []
            for n in sorted(nn for (pp, nn) in bank if pp == p):
                Rs = bank[(p, n)]
                if k + 1 <= len(Rs) and k <= n - 2 and Rs[k - 1] != 0:
                    rat = Rs[k] / Rs[k - 1]
                    row.append("n=%d: %s = %.6f" % (n, rat, float(rat)))
            if row:
                print("      k=%d:  %s" % (k, "   ".join(row)))
        sys.stdout.flush()


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
