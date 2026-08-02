# E-3 face 3 — the genus-9 dissection.
#
# (1) The length-32 rung (the armed doorway): extremal Type II n=32 (d=8, g=9) — exact zeta,
#     RH certificate, integrality, curve-factor, W-CHAIN-CURVE point-count conditions.
# (2) The genus-9 world = {n=24 pencil, c != -42 (d=4, g=9, ALL FAILING)} u {extremal-32}.
#     Dissection at the H-level, exact:
#       (a) sign-alternation of H(u) coefficients (necessary for all roots in (0,4));
#       (b) the HERMITE-HANKEL form: power sums s_k of h's roots (Newton identities, exact in
#           Q(sqrt2)); Hankel matrix [s_{i+j}]; leading principal minors' signs. Classical:
#           h real-rooted  <=>  Hankel PSD (signature counts distinct real roots).
#           The dissection measures WHERE the form breaks off the extremal stratum.
#       (c) zeta coefficient sign vector p_i.

from fractions import Fraction as Fr
import importlib.util, sys, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec)
sys.modules["dl"] = dl
spec.loader.exec_module(dl)
spec2 = importlib.util.spec_from_file_location(
    "gs", str(pathlib.Path(__file__).with_name("genus5.py")))
gs = importlib.util.module_from_spec(spec2)
sys.modules["gs"] = gs
spec2.loader.exec_module(gs)
F2 = dl.F2

def f2_from_fr(x): return F2(Fr(x), 0)

def newton_power_sums(h, kmax):
    """Power sums s_1..s_kmax of the roots of monic-normalized h, exact in Q(sqrt2).
    Coefficient form of Newton's identities: with h = x^d + A_1 x^{d-1} + ... + A_d,
    s_k = -k*A_k - sum_{i=1}^{k-1} A_i s_{k-i}   (A_i = 0 for i > d)."""
    d = dl.f2p_deg(h)
    inv = h[d].inv()
    A = [F2(0)] * (kmax + 1)
    for i in range(1, min(d, kmax) + 1):
        A[i] = h[d - i] * inv
    s = [F2(0)] * (kmax + 1)
    for k in range(1, kmax + 1):
        acc = A[k] * F2(Fr(-k))
        for i in range(1, k):
            acc = acc - A[i] * s[k - i]
        s[k] = acc
    return s

def hankel_minor_signs(h):
    """Leading principal minors of [s_{i+j}]_{0<=i,j<=g-1}, s_0 = deg h; exact signs."""
    g = dl.f2p_deg(h)
    s = newton_power_sums(h, 2 * g)
    s[0] = F2(Fr(g))
    M = [[s[i + j] for j in range(g)] for i in range(g)]
    signs = []
    for k in range(1, g + 1):
        # determinant of leading k x k via exact Gaussian elimination in Q(sqrt2)
        A = [row[:k] for row in M[:k]]
        det = F2(Fr(1)); sign_flip = 1; ok = True
        for col in range(k):
            piv = next((r for r in range(col, k) if not A[r][col].is_zero()), None)
            if piv is None:
                det = F2(0); break
            if piv != col:
                A[col], A[piv] = A[piv], A[col]; sign_flip = -sign_flip
            det = det * A[col][col]
            inv = A[col][col].inv()
            for r in range(col + 1, k):
                f = A[r][col] * inv
                A[r] = [A[r][j] - f * A[col][j] for j in range(k)]
        if det.is_zero():
            signs.append(0)
        else:
            signs.append(det.sign() * sign_flip)
    return signs

def alternation(Hu):
    """Strict sign alternation of H(u) coefficients: sign(c_i) = -sign(c_{i+1}), no zeros."""
    c = [x for x in Hu]
    d = len(c) - 1
    while d >= 0 and c[d] == 0: d -= 1
    c = c[:d + 1]
    if any(v == 0 for v in c):
        return False
    return all((c[i] > 0) != (c[i + 1] > 0) for i in range(len(c) - 1))

def dissect(name, W, n, d):
    r = dl.analyze(name, W, n, d, False)
    h = gs.build_h(r["p"], r["g"])
    Hu = gs.rational_certificate(h)
    alt = alternation(Hu)
    signs = hankel_minor_signs(h)
    first_fail = next((i + 1 for i, sg in enumerate(signs) if sg < 0), None)
    psd = all(sg >= 0 for sg in signs)
    print(f"{name}: n={n} d={d} g={r['g']} | RH-EXACT={r['RH_exact']} | "
          f"H-alternation={alt} | Hankel minors={signs} | PSD={psd}"
          f"{'' if first_fail is None else f' | first negative minor at k={first_fail}'}")
    print(f"    p_i signs: {''.join('+' if v > 0 else ('0' if v == 0 else '-') for v in r['p'])}")
    return r, Hu, signs

def main():
    print("=== sanity: Hermite-Hankel on known members ===")
    W24, d24 = dl.extremal_type2_enumerator(24)
    dissect("Golay (extremal, g=5)", W24, 24, 8)
    W8 = dl.W8
    W83 = dl.poly_mul(dl.poly_mul(W8, W8), W8)
    print("\n=== THE LENGTH-32 RUNG (the armed doorway) ===")
    W32, d32 = dl.extremal_type2_enumerator(32)
    assert d32 == 8
    print(f"extremal n=32 weight enumerator head: A_8 = {W32[8]}")
    r32 = dl.analyze("extremal n=32", W32, 32, 8, False)
    print(f"n=32 d=8 g={r32['g']} | RH-EXACT={r32['RH_exact']} | P(1)={r32['P1']} FE={r32['FE']}"
          f" | integral={r32['integral']} | curve-factor divides={r32['curve_factor']}")
    # W-CHAIN-CURVE point-count necessary conditions (would-be N_m from the zeta as if a curve)
    # N_m = q^m + 1 - sum alpha_i^m with alpha = 1/(sqrt2 T-roots scaled): use power sums of
    # reciprocal roots of P: alpha_i with prod(1 - alpha_i T) = P(T)/P(0).
    norm = r32["norm"]
    g2 = r32["deg"]
    # power sums of alpha via Newton on reversed poly (monic in alpha): prod(x - alpha_i)
    rev = list(reversed([Fr(v) for v in norm]))  # monic in alpha: x^g2 + A_1 x^{g2-1} + ...
    A = [Fr(0)] * 11
    for i in range(1, min(g2, 10) + 1):
        A[i] = rev[g2 - i]
    s = [Fr(0)] * 11
    for k in range(1, 11):
        acc = -Fr(k) * A[k]
        for i in range(1, k):
            acc -= A[i] * s[k - i]
        s[k] = acc
    Ns = [Fr(2) ** m + 1 - s[m] for m in range(1, 6)]
    print(f"    would-be point counts N_1..N_5 = {[str(v) for v in Ns]} | "
          f"all nonneg integers: {all(v.denominator == 1 and v >= 0 for v in Ns)}")
    dissect("extremal n=32 (g=9)", W32, 32, 8)
    print("\n=== THE FAILING INTERIOR (n=24 pencil, d=4, g=9) ===")
    for c in (Fr(0), Fr(-10), Fr(-21), Fr(-30), Fr(-41), Fr(-419, 10)):
        Wc = [W83[i] + c * dl.G24[i] for i in range(25)]
        dissect(f"pencil c={c}", Wc, 24, 4)
    print("\n=== the channel boundary (Hankel-PSD flip along the pencil) ===")
    def psd_at(c):
        Wc = [W83[i] + c * dl.G24[i] for i in range(25)]
        r = dl.analyze(f"pencil c={c}", Wc, 24, 4, False)
        h = gs.build_h(r["p"], r["g"])
        return all(sg >= 0 for sg in hankel_minor_signs(h))
    hi, lo = Fr(-30), Fr(-41)        # PSD at hi, indefinite at lo (moving negative)
    while hi - lo > Fr(1, 8):
        mid = (hi + lo) / 2
        if psd_at(mid): hi = mid
        else: lo = mid
    print(f"reality-escape channel opens between c = {hi} (PSD, real-rooted) and c = {lo} "
          f"(indefinite, complex roots); bracket width {hi - lo}")
    print("\n=== beyond the Golay point (the pencil's other side) ===")
    for c in (Fr(-43), Fr(-50)):
        Wc = [W83[i] + c * dl.G24[i] for i in range(25)]
        dissect(f"pencil c={c} (beyond)", Wc, 24, 4)

if __name__ == "__main__":
    main()
