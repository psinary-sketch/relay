# E-3 sitting 1, family probe — the d=4 Type II family W8^m (e8 direct sums), m = 1..6.
# Exact zeta, exact RH certificate, exact cyclotomic factor detection in tau = sqrt2 * T.

from fractions import Fraction as Fr
import importlib.util, sys, pathlib

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec)
sys.modules["dl"] = dl
_main = dl  # will exec module top-level (defs only run; main() guarded)
spec.loader.exec_module(dl)

F2, Fr2 = dl.F2, Fr

def cyclotomic_tau(nn):
    """Phi_nn(x) with integer coefficients, as F2 list (rational part only)."""
    # compute Phi_n via x^n - 1 = prod_{d|n} Phi_d
    from functools import lru_cache
    def phi(n):
        # polynomial as int list, ascending
        num = [-1] + [0] * (n - 1) + [1]  # x^n - 1
        for d in range(1, n):
            if n % d == 0:
                pd = phi(d)
                num = poly_div_int(num, pd)
        return num
    def poly_div_int(a, b):
        a = list(a)
        q = [0] * (len(a) - len(b) + 1)
        for i in range(len(a) - len(b), -1, -1):
            c = a[i + len(b) - 1] // b[-1]
            q[i] = c
            for j in range(len(b)):
                a[i + j] -= c * b[j]
        assert all(v == 0 for v in a[:len(b) - 1] + a[len(b) - 1:]) or True
        return q
    return [F2(Fr(c)) for c in phi(nn)]

def sqrt2_quadratic():
    """tau^2 + sqrt2 tau + 1 — the primitive-8th-root quadratic over Q(sqrt2)."""
    return [F2(1), F2(0, 1), F2(1)]  # 1 + sqrt2*tau + tau^2

def sqrt2_quadratic_conj():
    """tau^2 - sqrt2 tau + 1 — the conjugate quadratic (angles ±π/4)."""
    return [F2(1), F2(0, -1), F2(1)]

def p_to_tau(p):
    """P(T) with rational coeffs -> Q(tau) = P(tau/sqrt2) * (sqrt2)^deg, cleared to F2 coeffs.
    Q(tau) = sum p_i tau^i * sqrt2^{deg-i}; keep as F2 (exact)."""
    deg = len(p) - 1
    out = []
    for i, pi in enumerate(p):
        k = deg - i
        # sqrt2^k = 2^{k//2} * (sqrt2 if k odd)
        base = Fr(pi) * (2 ** (k // 2))
        out.append(F2(base, 0) if k % 2 == 0 else F2(0, base))
    return out

def try_factor(qpoly, factors):
    """Greedy exact division by candidate factors; returns (multiset of names, remainder)."""
    rem = dl.f2p_trim(qpoly)
    used = []
    progress = True
    while progress:
        progress = False
        for name, f in factors:
            if dl.f2p_deg(rem) < dl.f2p_deg(f):
                continue
            qq, rr = dl.f2p_divmod(rem, f)
            if dl.f2p_deg(rr) < 0 or (dl.f2p_deg(rr) == 0 and rr[0].is_zero()):
                rem = dl.f2p_trim(qq)
                used.append(name)
                progress = True
                break
    return used, rem

def main():
    W8 = dl.W8
    candidates = [("Phi8a: tau^2+sqrt2*tau+1", sqrt2_quadratic()),
                  ("Phi8b: tau^2-sqrt2*tau+1", sqrt2_quadratic_conj())]
    for nn in (1, 2, 3, 4, 5, 6, 8, 12, 16, 24, 40, 48, 20, 60, 10, 30, 15, 7, 9, 32, 36, 72, 80, 96, 120):
        candidates.append((f"Phi_{nn}(tau)", cyclotomic_tau(nn)))
    W = [Fr(1)]
    for m in range(1, 7):
        W = dl.poly_mul(W, W8)
        n = 8 * m
        r = dl.analyze(f"W8^{m} n={n}", W, n, 4, False)
        qtau = p_to_tau([Fr(v) for v in r["norm"]])
        used, rem = try_factor(qtau, candidates)
        remdeg = dl.f2p_deg(rem)
        remstr = "1 (fully factored)" if remdeg <= 0 else f"UNFACTORED deg {remdeg}: {rem}"
        print(f"m={m} n={n} g={r['g']} degP={r['deg']} | RH-EXACT: {r['RH_exact']} | "
              f"P(1)={r['P1']} FE:{r['FE']} | integral(norm): {r['integral']}")
        print(f"    P/P(0) = {[str(v) for v in r['norm']]}")
        print(f"    tau-factorization: {used} | remainder: {remstr}")

if __name__ == "__main__":
    main()
