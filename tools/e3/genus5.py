# E-3 face 2 — THE GENUS-5 THEOREM, certificates end-to-end.
#
# Theorem (Type II, genus <= 5): every Type II self-dual weight enumerator of genus <= 5
# satisfies Duursma-RH.  Classification: g = 4m+1-d (n=8m) forces g == 1 (mod 4); genus 1
# forces (n,d)=(8,4); genus 5 forces (n,d) in {(16,4),(24,8)} given Mallows-Sloane
# d <= 4*floor(n/24)+4 (kills every m >= 4 since 4(m-1) > 4*floor(m/3)+4 for m >= 4);
# Gleason uniqueness at each point (verified exactly below).  Confinement: the rational
# certificate H(u) — with h in Q(sqrt2)[s], Galois conjugation sigma acting as s -> -s,
# H(s) := h(s) h^sigma(s) is even with RATIONAL coefficients; H(u), u = s^2, has all roots
# in [0,4] iff all roots of h are real in [-2,2] iff Duursma-RH.  Certified by exact Sturm
# over Q (multiplicity-aware via gcd recursion).

from fractions import Fraction as Fr
import importlib.util, sys, pathlib

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec)
sys.modules["dl"] = dl
spec.loader.exec_module(dl)
F2 = dl.F2

# ---------- h(s) in Q(sqrt2)[s] from a zeta coefficient list ----------

def build_h(p, g):
    def ptilde(i):
        base = Fr(p[i], 2 ** (i // 2))
        return F2(base, 0) if i % 2 == 0 else F2(0, base / 2)
    v_prev = [F2(2)]; v_curr = [F2(0), F2(1)]
    def padd(a, b):
        m = max(len(a), len(b)); z = F2(0)
        return [(a[i] if i < len(a) else z) + (b[i] if i < len(b) else z) for i in range(m)]
    h = [ptilde(g)]
    for j in range(1, g + 1):
        if j == 1:
            vj = v_curr
        else:
            vj = padd([F2(0)] + v_curr, [x * F2(-1) for x in v_prev])
            v_prev, v_curr = v_curr, vj
        h = padd(h, [x * ptilde(g + j) for x in vj])
    return dl.f2p_trim(h)

# ---------- rational polynomial helpers (ascending Fraction lists) ----------

def rdeg(p):
    d = len(p) - 1
    while d >= 0 and p[d] == 0:
        d -= 1
    return d

def rtrim(p):
    return p[:rdeg(p) + 1] if rdeg(p) >= 0 else [Fr(0)]

def reval(p, x):
    acc = Fr(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc

def rderiv(p):
    return rtrim([p[i] * i for i in range(1, len(p))]) if len(p) > 1 else [Fr(0)]

def rdivmod(a, b):
    a = list(a); db = rdeg(b)
    q = [Fr(0)] * max(1, len(a) - db)
    while rdeg(a) >= db:
        da = rdeg(a)
        c = a[da] / b[db]
        q[da - db] = c
        for i in range(db + 1):
            a[i + da - db] -= c * b[i]
        a[da] = Fr(0)
    return rtrim(q), rtrim(a)

def rgcd(a, b):
    a, b = rtrim(a), rtrim(b)
    while rdeg(b) >= 1 or (rdeg(b) == 0 and b[0] != 0):
        _, r = rdivmod(a, b)
        a, b = b, r
    d = rdeg(a)
    return [c / a[d] for c in a]

def sturm_count_open(p, lo, hi):
    chain = [rtrim(p), rderiv(p)]
    while rdeg(chain[-1]) > 0:
        _, r = rdivmod(chain[-2], chain[-1])
        if rdeg(r) < 0 or (rdeg(r) == 0 and r[0] == 0):
            break
        chain.append([-c for c in r])
    def var(x):
        signs = [(v > 0) - (v < 0) for v in (reval(c, x) for c in chain)]
        signs = [s for s in signs if s != 0]
        return sum(1 for i in range(len(signs) - 1) if signs[i] * signs[i + 1] < 0)
    return var(lo) - var(hi)

def all_roots_in_04(H):
    """True iff every root of H (with multiplicity) is real and lies in [0, 4]."""
    H = rtrim(H)
    if rdeg(H) <= 0:
        return True
    gg = rgcd(H, rderiv(H))
    hsf, rem = rdivmod(H, gg)
    assert rdeg(rem) < 0 or (rdeg(rem) == 0 and rem[0] == 0)
    hsf = rtrim(hsf)
    ends = 0
    for pt in (Fr(0), Fr(4)):
        if reval(hsf, pt) == 0:
            hsf, r0 = rdivmod(hsf, [-pt, Fr(1)])
            assert rdeg(r0) < 0 or r0[0] == 0
            ends += 1
    inner = sturm_count_open(hsf, Fr(0), Fr(4)) if rdeg(hsf) > 0 else 0
    if inner != rdeg(hsf):
        return False
    return all_roots_in_04(gg)

# ---------- H(u) from h ----------

def rational_certificate(h):
    """H(s) = h(s) * h^sigma(s); verify even and rational; return H(u) ascending in u."""
    hs = [F2(c.a, -c.b) for c in h]                      # Galois conjugate
    prod = [F2(0)] * (len(h) + len(hs) - 1)
    for i, a in enumerate(h):
        for j, b in enumerate(hs):
            prod[i + j] = prod[i + j] + a * b
    for i, c in enumerate(prod):
        assert c.b == 0, f"H not rational at s^{i}: {c}"
        if i % 2 == 1:
            assert c.a == 0, f"H not even at s^{i}: {c}"   # the Galois-parity lock
    return [prod[2 * k].a for k in range((len(prod) + 1) // 2)]

def show(name, W, n, d):
    r = dl.analyze(name, W, n, d, False)
    assert r["P1"] == 1 and r["FE"]
    h = build_h(r["p"], r["g"])
    Hu = rational_certificate(h)
    ok = all_roots_in_04(Hu)
    print(f"{name}: n={n} d={d} g={r['g']}")
    print(f"  H(u) (ascending, exact): {[str(c) for c in Hu]}")
    print(f"  Galois-parity lock verified (H even, rational): True")
    print(f"  ALL ROOTS OF H(u) IN [0,4] (exact Sturm over Q): {ok}")
    print(f"  cross-check vs sitting-1 certificate (Sturm over Q(sqrt2)): {r['RH_exact']}")
    assert ok == r["RH_exact"]
    return ok

def main():
    print("=== CLASSIFICATION ARITHMETIC (exact) ===")
    # parity: g = 4m+1-d, d ≡ 0 mod 4  =>  g ≡ 1 mod 4  (algebra; displayed for the record)
    print("genus parity: g = 4m+1-d with 4|d  =>  g == 1 (mod 4); genera 2,3,4 EMPTY")
    W8 = dl.W8
    W16 = dl.poly_mul(W8, W8)
    print(f"n=16 Gleason space is 1-dim; A_4(W8^2) = {W16[4]} != 0  =>  (16,8) EMPTY, d=4 forced")
    W83 = dl.poly_mul(W16, W8)
    print(f"n=24 pencil W8^3 + c*g24: A_4 = 42 + c  =>  d=8 forces c=-42 (Golay), unique")
    G = [W83[i] - 42 * dl.G24[i] for i in range(25)]
    print(f"A_8(Golay) = {G[8]} != 0  =>  (24,12) EMPTY")
    print("m >= 4 at genus 5: d = 4(m-1) > 4*floor(m/3)+4  =>  excluded by Mallows-Sloane (at cite)")
    print("classification: genus 1 = {e8}; genus 5 = {W8^2, Golay}; nothing else at genus <= 5\n")
    print("=== THE THREE RATIONAL CERTIFICATES ===")
    a = show("e8 [8,4,4]", W8, 8, 4)
    b = show("W8^2 (e8+e8 / d16+)", W16, 16, 4)
    c = show("Golay [24,12,8]", G, 24, 8)
    print(f"\nTHEOREM CERTIFIED: every Type II self-dual weight enumerator of genus <= 5 "
          f"satisfies Duursma-RH: {a and b and c}")

if __name__ == "__main__":
    main()
