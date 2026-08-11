# -*- coding: utf-8 -*-
"""W-ORD-SLOPE, stage 0: RECOVER the family-run instrument.

The generator that produced data/threshold_law_points.jsonl is not in the repo.
The B-definition is FROZEN at B = 2M, so the reconstruction must reproduce the
family's ten MEASURED first-negative indices exactly, or it is not the same
instrument and the run does not proceed on it.

Bombieri-Lagarias: lam_n = sum_rho [1 - (1 - 1/rho)^n] over a conjugate-closed multiset.
  on-line pair {1/2 +- i g}: contributes 2 - 2 cos(n*theta),  theta = pi - 2*atan(2g)
      (|1 - 1/rho| = 1 exactly on the critical line, so these oscillate at mean 2)
  off-line quadruple {1/2 +- d +- i g}: contributes 4 - 2Re(z_+^n) - 2Re(z_-^n)
      z_pm = 1 - 1/(1/2 +- d + i g); |z_-| > 1 is the growing channel.
Mean level of the base is 2M = B. That is why B := 2M.
"""
import json, math, sys
import numpy as np

def online_thetas(gammas):
    g = np.asarray(gammas, dtype=np.float64)
    return math.pi - 2.0 * np.arctan(2.0 * g)

def quad_channels(gamma, delta):
    out = []
    for s in (+1.0, -1.0):
        rho = complex(0.5 + s * delta, gamma)
        z = 1.0 - 1.0 / rho
        out.append((abs(z), math.atan2(z.imag, z.real)))
    return out            # [(r_+, phi_+), (r_-, phi_-)]

def scan(gammas, gamma, delta, nmax):
    """Return (first_negative_n, base_min_normalised) or (None, base_min)."""
    th = online_thetas(gammas)
    (rp, pp), (rm, pm) = quad_channels(gamma, delta)
    lrp, lrm = math.log(rp), math.log(rm)
    M = len(th)
    base_min = float('inf')
    TWO_PI = 2.0 * math.pi
    for n in range(1, nmax + 1):
        ang = np.fmod(n * th, TWO_PI)
        base = 2.0 * M - 2.0 * np.sum(np.cos(ang))
        if base < base_min:
            base_min = base
        quad = 4.0 - 2.0 * math.exp(n * lrp) * math.cos(math.fmod(n * pp, TWO_PI)) \
                   - 2.0 * math.exp(n * lrm) * math.cos(math.fmod(n * pm, TWO_PI))
        if base + quad < 0.0:
            return n, base_min / (2.0 * M)
    return None, base_min / (2.0 * M)

# ---- candidate base families -------------------------------------------------
def base_integers(M):        return [float(k) for k in range(1, M + 1)]
def base_half_integers(M):   return [k + 0.5 for k in range(1, M + 1)]
def base_zeta(M):
    from mpmath import mp, zetazero
    mp.dps = 15
    return [float(zetazero(k).imag) for k in range(1, M + 1)]
def base_zeta_asym(M):
    # Riemann-von Mangoldt approximation to the k-th ordinate (cheap, no mpmath)
    out = []
    for k in range(1, M + 1):
        t = 2.0 * math.pi * k / math.log(max(k, 2))
        for _ in range(60):
            t = 2.0 * math.pi * (k - 11.0 / 8.0) / max(math.log(t / (2.0 * math.pi)) - 1.0, 1e-9)
        out.append(t)
    return out

FAMILIES = {
    "integers k":        base_integers,
    "half-integers k+.5": base_half_integers,
    "zeta ordinates":    base_zeta,
    "zeta asymptotic":   base_zeta_asym,
}

if __name__ == "__main__":
    pts = [json.loads(l) for l in open(r"D:\relay\data\threshold_law_points.jsonl", encoding="utf-8")]
    which = sys.argv[1:] or list(FAMILIES)
    subset = [p for p in pts if p["M"] <= 150]          # cheap discriminating subset
    for name in which:
        fn = FAMILIES[name]
        print("\n=== base family: %s ===" % name)
        ok = 0
        for p in subset:
            g = fn(p["M"])
            n, bmin = scan(g, p["gamma"], p["delta"], int(p["n"] * 1.6) + 200)
            hit = (n == p["n"])
            ok += hit
            print("  id%-3d M=%-5d expect n=%-6d got %-8s  %s   base_min got %.5f expect %.5f"
                  % (p["id"], p["M"], p["n"], n, "MATCH" if hit else "no", bmin, p["base_min"]))
        print("  --> %d/%d exact" % (ok, len(subset)))
