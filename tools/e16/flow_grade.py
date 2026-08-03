# W-LEHMER UPGRADE: model grade -> flow grade (windowed).
# Integrate the dBN backward zero dynamics  dx_k/dt = sum_{j!=k} 2/(x_k - x_j)
# (Polymath15 normalization, x = 2*gamma; mirror zeros at -x included exactly;
# far-tail field beyond the window added as a density integral; double-sourced by
# running tail ON vs OFF) from t = 0 to t = -0.1 over the first 1500 zeros.
# Collision: gap < 1e-3 -> pair merged to a weight-2 point, time recorded.
# GRADE: FLOW-GRADE-WINDOWED (finite window; post-collision far-field approximated by
# the merged double point; beneath Polymath15's rigorous effective machinery, cited).

import numpy as np, os, sys
import mpmath as mp

CACHE = os.path.join(os.environ.get("TEMP", "."), "zeros1500.npy")

def zeros():
    if os.path.exists(CACHE):
        return np.load(CACHE)
    mp.mp.dps = 20
    zs = np.array([float(mp.zetazero(n).imag) for n in range(1, 1501)])
    np.save(CACHE, zs)
    return zs

def tail_field(x, X_edge):
    # paired far-tail: 2 * integral_X^inf rho(y) * 2x/(x^2 - y^2) dy, rho(y) = log(y/(4 pi))/(4 pi)
    y = np.linspace(X_edge, 2.0e6, 400000)
    rho = np.log(y / (4 * np.pi)) / (4 * np.pi)
    out = np.empty_like(x)
    for i, xi in enumerate(x):
        out[i] = 2.0 * np.trapezoid(rho * 2 * xi / (xi * xi - y * y), y)
    return out

def run(use_tail):
    g = zeros()
    x = 2.0 * g
    w = np.ones_like(x)
    alive = np.ones(len(x), dtype=bool)
    orig_idx = np.arange(len(x))
    X_edge = x[-1] + 2.0
    tail0 = tail_field(x, X_edge) if use_tail else np.zeros_like(x)
    t = 0.0
    collisions = []  # (orig pair index n, collision t)
    def field(xv, wv):
        d = xv[:, None] - xv[None, :]
        np.fill_diagonal(d, np.inf)
        F = (2.0 * wv[None, :] / d).sum(axis=1)
        F += (2.0 * wv[None, :] / (xv[:, None] + xv[None, :])).sum(axis=1)
        return F
    while t > -0.1:
        xv = x[alive]; wv = w[alive]
        gaps = np.diff(xv)
        dt = -min(2e-4, max(1e-7, gaps.min() ** 2 / 40.0))
        if t + dt < -0.1:
            dt = -0.1 - t
        tl = tail0[alive] if use_tail else 0.0
        k1 = field(xv, wv) + tl
        k2 = field(xv + 0.5 * dt * k1, wv) + tl
        k3 = field(xv + 0.5 * dt * k2, wv) + tl
        k4 = field(xv + dt * k3, wv) + tl
        xv = xv + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        x[alive] = xv
        t += dt
        # collision check
        idx_alive = np.where(alive)[0]
        gaps = np.diff(xv)
        hit = np.where(gaps < 1e-3)[0]
        for h in hit[::-1]:
            i1, i2 = idx_alive[h], idx_alive[h + 1]
            n_pair = orig_idx[i1] + 1  # 1-based index of the lower zero
            collisions.append((int(n_pair), t))
            x[i1] = (x[i1] * w[i1] + x[i2] * w[i2]) / (w[i1] + w[i2])
            w[i1] = w[i1] + w[i2]
            alive[i2] = False
            idx_alive = np.where(alive)[0]
            xv = x[alive]
    return collisions

def main():
    for use_tail in (True, False):
        cols = run(use_tail)
        cols.sort()
        label = "tail ON " if use_tail else "tail OFF"
        interior = [c for c in cols if 50 <= c[0] <= 1450]
        edge = [c for c in cols if c[0] < 50 or c[0] > 1450]
        print(f"[{label}] collisions by t=-0.1: {len(cols)} total; "
              f"{len(interior)} interior (50<=n<=1450), {len(edge)} edge-flagged")
        print(f"  interior collided pairs (n, t_collision): "
              f"{[(n, round(tc, 4)) for n, tc in interior[:20]]}")
        if interior:
            lo = min(interior)
            print(f"  LOWEST interior collided pair at flow grade: n={lo[0]}, "
                  f"t_c = {lo[1]:.4f}")
        print()

if __name__ == "__main__":
    main()
