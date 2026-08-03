# E-20 face 4 — THE CONSTANT: is the tracking ratio's ~1.12 a density-normalization
# artifact or arithmetic content?  CONTROL: a synthetic measure from the SMOOTH zero-counting
# function (gamma~_j solving the Riemann-von Mangoldt main term N(g) = j), same construction
# (beta~ = 1/(2 gamma~)^2, moments by summation + tail, Jacobi diagonal, tracking ratio).
# If the control reproduces ~1.12 within the band, the constant IDENTIFIES as the density
# normalization; if it differs, the measured constant carries arithmetic content.

import mpmath as mp

def smooth_zero(j):
    # N(g) = (g/2pi) log(g/(2 pi e)) + 7/8 = j
    f = lambda g: g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8 - j
    lo = mp.mpf(10)
    return mp.findroot(f, 14 + 6 * j)

def main():
    mp.mp.dps = 150
    J = 3000
    gam = [smooth_zero(j) for j in range(1, J + 1)]
    betas = [1 / (2 * g) ** 2 for g in gam]
    kmax = 25
    s = [None] * (kmax + 1)
    gJ = gam[-1]
    for k in range(1, kmax + 1):
        base = sum(b ** k for b in betas)
        tail = mp.quad(lambda g: mp.log(g / (2 * mp.pi)) / (2 * mp.pi) * (2 * g) ** (-2 * k),
                       [gJ, 10 * gJ, mp.inf])
        s[k] = base + tail
    mp.mp.dps = 220   # the precision law: arithmetic >= certification depth
    s = [None] + [mp.mpf(x) for x in s[1:]]
    depth = 10
    G = mp.matrix(depth + 1, depth + 1)
    for i in range(depth + 1):
        for j in range(depth + 1):
            G[i, j] = s[i + j + 1]
    R = mp.cholesky(G).T
    al = []
    for k in range(depth):
        t1 = R[k, k + 1] / R[k, k]
        t0 = R[k - 1, k] / R[k - 1, k - 1] if k >= 1 else mp.mpf(0)
        al.append(t1 - t0)
    print("=== CONTROL (smooth-density synthetic zeros): tracking ratio alpha_k / beta~_k ===")
    ratios = []
    for k in range(2, depth):
        r = al[k] / betas[k]
        ratios.append(r)
        print(f"  k={k+1}: ratio {mp.nstr(r, 5)}")
    mean = sum(ratios) / len(ratios)
    print(f"control mean (k=3..{depth}): {mp.nstr(mean, 5)}  | measured zeta mean ~ 1.12, band [1.00, 1.31]")

if __name__ == "__main__":
    main()
