# E-23 — THE OSCILLATION'S SHAPE.  The string diagonal's oscillation o_k (about the
# density mean identified in E-20 face 4) tested for spacing-driven (pair-correlation-class)
# structure: Pearson correlation against the local normalized gap deviations of the actual
# zeros, at lags -1, 0, +1; the smooth-density control's oscillation (+/-0.0015) is the null
# baseline.  Truncation honesty: 14 points (k = 3..16); |r| and n reported, nothing more.
# Data: the recorded instrument outputs (continuum_audit dps-400 depth-16; constant_control).

import mpmath as mp

ZETA_RATIOS = {  # k: alpha_k / beta_k from the dps-400 depth-16 run
    3: 1.1249, 4: 1.1267, 5: 1.1642, 6: 1.2235, 7: 1.0024, 8: 1.0293,
    9: 1.3127, 10: 1.1154, 11: 1.1232, 12: 1.0573, 13: 1.0635, 14: 1.2411,
    15: 1.1183, 16: 1.0516,
}
CONTROL_MEAN = 1.1157
CONTROL_OSC = 0.0015

def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = mp.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = mp.sqrt(sum((y - my) ** 2 for y in ys))
    return num / (dx * dy)

def main():
    mp.mp.dps = 25
    zs = [mp.zetazero(j).imag for j in range(1, 20)]
    # normalized gaps: s_j = (gamma_{j+1} - gamma_j) * log(gamma_j / 2pi) / (2 pi)
    sgap = {}
    for j in range(1, 19):
        g = zs[j] - zs[j - 1]
        sgap[j] = float(g * mp.log(zs[j - 1] / (2 * mp.pi)) / (2 * mp.pi))
    ks = sorted(ZETA_RATIOS)
    o = [ZETA_RATIOS[k] - CONTROL_MEAN for k in ks]
    print(f"oscillation o_k (k=3..16): rms = {float(mp.sqrt(sum(x*x for x in o)/len(o))):.4f} "
          f"| control null rms ~ {CONTROL_OSC}")
    print(f"signal-to-null ratio: {float(mp.sqrt(sum(x*x for x in o)/len(o)))/CONTROL_OSC:.0f}x")
    for name, lag in (("gap AFTER zero k   (s_k)", 0), ("gap BEFORE zero k (s_{k-1})", -1),
                      ("gap two-before    (s_{k-2})", -2), ("mean adjacent", None)):
        if lag is None:
            xs = [(sgap[k - 1] + sgap[k]) / 2 - 1 for k in ks]
        else:
            xs = [sgap[k + lag] - 1 for k in ks]
        r = pearson(xs, o)
        print(f"corr(o_k, {name}) = {float(r):+.3f}   (n = {len(ks)})")

if __name__ == "__main__":
    main()
