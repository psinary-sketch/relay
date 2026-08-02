# E-16 — THE HANKEL BRIDGE instrument.
#
# H_t(z) = int_0^inf e^{t u^2} Phi(u) cos(zu) du   (Polymath normalization;
#   Phi(u) = sum_n (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u});
#   H_0(z) = xi(1/2 + iz/2)/8, zeros x_j = 2 gamma_j under RH-frame).
# Taylor: H_t(z) = sum_k c_k z^{2k}, c_k = (-1)^k M_k/(2k)!, M_k = int u^{2k} e^{tu^2} Phi du.
# In w = z^2: f(w) = sum (c_k/c_0) w^k = prod_j (1 - w/w_j); power sums of RECIPROCAL zeros
# beta_j = 1/w_j:  log f = -sum_k s_k w^k / k,  s_k = sum_j beta_j^k  (k >= 1).
# Reality layer:   A1_d = [s_{i+j+1}]_{0..d-1}  PSD  <=  all w_j real (Hermite/Hamburger).
# Positivity layer: A2_d = [s_{i+j+2}]          PSD additionally  <=  all w_j real POSITIVE
#   (Stieltjes) -- the toy wall's interval clause at zeta.
# Flip depth d(t): first d with a negative leading principal minor (diagonal-scaled;
# congruence preserves signs). Double-sourced: two working precisions; t=0 cross-checked
# against explicit zero-sums via mpmath.zetazero.

import mpmath as mp

def phi(u):
    s = mp.mpf(0)
    n = 1
    while True:
        a = mp.pi * n * n * mp.e**(4 * u)
        term = (2 * mp.pi**2 * n**4 * mp.e**(9 * u) - 3 * mp.pi * n * n * mp.e**(5 * u)) * mp.e**(-a)
        s += term
        if abs(term) < mp.mpf(10) ** (-mp.mp.dps - 25) and n > 3:
            break
        n += 1
        if n > 200:
            break
    return s

def moments(t, kmax):
    out = []
    for k in range(kmax + 1):
        f = lambda u: u ** (2 * k) * mp.e**(t * u * u) * phi(u)
        out.append(mp.quad(f, [0, mp.mpf(1)/2, 1, mp.mpf(3)/2, 2, 3, 4, 6]))
    return out

def power_sums(t, kmax):
    M = moments(t, kmax)
    a = [(-1) ** k * M[k] / (mp.factorial(2 * k) * M[0]) for k in range(kmax + 1)]
    L = [mp.mpf(0)] * (kmax + 1)
    for k in range(1, kmax + 1):
        acc = k * a[k]
        for i in range(1, k):
            acc -= i * L[i] * a[k - i]
        L[k] = acc / k
    s = [None] + [-k * L[k] for k in range(1, kmax + 1)]
    return s

def minors_scaled(s, shift, dmax):
    """Leading principal minors of [s_{i+j+shift}] after symmetric diagonal scaling by
    rho^(i): congruence, sign-preserving. rho from the dominant-zero ratio."""
    rho = s[6] / s[7] if s[7] != 0 else mp.mpf(800)
    dets = []
    for d in range(1, dmax + 1):
        A = mp.matrix(d, d)
        for i in range(d):
            for j in range(d):
                A[i, j] = s[i + j + shift] * rho ** (i + j + shift)
        dets.append(mp.det(A))
    return dets, rho

def run(t, kmax, dmax, dps_list):
    results = {}
    for dps in dps_list:
        mp.mp.dps = dps
        s = power_sums(mp.mpf(str(t)), kmax)
        m1, rho = minors_scaled(s, 1, dmax)
        m2, _ = minors_scaled(s, 2, dmax)
        results[dps] = (s, m1, m2)
    (s_a, m1_a, m2_a), (s_b, m1_b, m2_b) = results[dps_list[0]], results[dps_list[1]]
    # resolved depth: signs agree and relative agreement of the minor values
    def verdict(ma, mb):
        out = []
        for d in range(len(ma)):
            same_sign = (ma[d] > 0) == (mb[d] > 0)
            rel = abs(ma[d] - mb[d]) / (abs(mb[d]) + mp.mpf(10) ** (-mp.mp.dps))
            ok = same_sign and rel < mp.mpf(10) ** (-8)
            out.append((d + 1, '+' if mb[d] > 0 else '-', ok))
        return out
    v1 = verdict(m1_a, m1_b)
    v2 = verdict(m2_a, m2_b)
    def summarize(v):
        resolved = 0
        flip = None
        for d, sign, ok in v:
            if not ok:
                break
            resolved = d
            if sign == '-' and flip is None:
                flip = d
        return resolved, flip, ''.join(sign for _, sign, ok in v if ok)
    r1, f1, seq1 = summarize(v1)
    r2, f2, seq2 = summarize(v2)
    agree = max(abs(s_a[k] - s_b[k]) / abs(s_b[k]) for k in range(1, min(9, kmax + 1)))
    print(f"t = {t}:  s-agreement(2 dps, k<=8): {mp.nstr(agree, 3)}")
    print(f"  s_1..s_4 = {[mp.nstr(s_b[k], 12) for k in range(1, 5)]}")
    print(f"  REALITY layer  [s_(i+j+1)]: signs {seq1} | resolved depth {r1} | "
          f"FLIP at d = {f1 if f1 else '-- (none within resolution)'}")
    print(f"  POSITIVITY layer [s_(i+j+2)]: signs {seq2} | resolved depth {r2} | "
          f"FLIP at d = {f2 if f2 else '-- (none within resolution)'}")
    return f1, r1

def zero_sum_check(kmax=6, J=300):
    mp.mp.dps = 30
    sums = {}
    zs = [mp.zetazero(j).imag for j in range(1, J + 1)]
    for k in range(2, kmax + 1):
        sums[k] = sum((2 * g) ** (-2 * k) for g in zs)
    return sums

def main():
    print("=== t = 0 cross-check: integral route vs explicit zero-sums (J=300) ===")
    zsums = zero_sum_check()
    mp.mp.dps = 120
    s0 = power_sums(mp.mpf(0), 12)
    for k in range(2, 7):
        rel = abs(s0[k] - zsums[k]) / zsums[k]
        print(f"  k={k}: integral {mp.nstr(s0[k], 12)} vs zero-sum {mp.nstr(zsums[k], 12)} "
              f"| rel diff {mp.nstr(rel, 3)}")
    print()
    flips = {}
    for t in (0, -0.1, -0.3, -5, -15, -30, -50):
        f, r = run(t, kmax=26, dmax=12, dps_list=(150, 220))
        flips[t] = (f, r)
        print()
    print("=== FLIP-DEPTH SUMMARY d(t) ===")
    for t, (f, r) in flips.items():
        print(f"  t = {t}: flip depth = {f if f else f'none within resolved depth {r}'}")

if __name__ == "__main__":
    main()
