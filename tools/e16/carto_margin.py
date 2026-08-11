# -*- coding: utf-8 -*-
"""W-ORD-CARTOGRAPHY act 2 -- the margin sheet + E4's window comparison.

Instrument: carto_atlas (validated at act 1R, E2 residual 7.1e-7 vs TOL 1e-3).
COMMITTED GRID CONSTANTS UNCHANGED: NV=4001 NU=12001 UMAX=600 TOL=1e-3 NGAM=10000.
DISCLAIMED REGISTER: a computation maps and cannot prove. No sign claim is made.

M(a) := ARCH(a) - |PRIME(a)|   -- the margin, a determined quantity.
"""
import math, json, os, io
import numpy as np
import carto_atlas as C

BANK = r"D:\relay\data\carto_margin.jsonl"


def li_effective_support(n, span=8.0, npt=20001):
    """The Li-relevant multiplicative test function for index n, measured.

    lambda_n = sum_rho [1 - (1-1/rho)^n].  In the explicit-formula pairing the
    corresponding additive-side kernel is  k_n(v) = Re[1 - (1 - 1/rho)^n] read
    through rho = 1/2 + i u; we measure the ENVELOPE of its v-profile, i.e. the
    inverse Fourier transform of  u -> 1 - Re[(1 - 1/(1/2+iu))^n],
    and report the width containing 99% of its mass.  Support truncation bounds
    v directly; this measures whether the Li family is bounded in v at all.
    """
    u = np.linspace(-400.0, 400.0, 40001)
    rho = 0.5 + 1j * u
    z = 1.0 - 1.0 / rho
    ker = 1.0 - np.real(z ** n)
    v = np.linspace(-span, span, npt)
    prof = np.array([np.trapezoid(ker * np.cos(vv * u), u) for vv in v[::40]])
    vv = v[::40]
    m = np.abs(prof)
    tot = np.trapezoid(m, vv)
    if tot <= 0:
        return float('nan')
    c = np.cumsum(m) * (vv[1] - vv[0])
    lo = vv[np.searchsorted(c, 0.005 * tot)]
    hi = vv[np.searchsorted(c, 0.995 * tot)]
    return float(hi - lo)


if __name__ == "__main__":
    print("instrument: carto_atlas, validated (act 1R). Constants UNCHANGED.")
    print("\n--- THE MARGIN SHEET: M(a) = ARCH(a) - |PRIME(a)| ---")
    print("%-6s %13s %13s %13s %13s %s" % ("a", "arch", "|prime|", "M(a)", "zero", "primes"))
    rows = []
    grid = [1.30, 1.50, 1.70, 1.90, 2.00, 2.01, 2.10, 2.40, 2.80,
            2.99, 3.00, 3.01, 3.20, 3.50, 3.80, 3.99, 4.00]
    for a in grid:
        r = C.channels(a)
        M = r["arch"] - abs(r["prime"])
        r["margin"] = M
        rows.append(r)
        with open(BANK, "a", encoding="utf-8") as f:
            f.write(json.dumps(r) + "\n"); f.flush(); os.fsync(f.fileno())
        print("%-6.2f %13.6f %13.6f %13.6f %13.6f %s"
              % (a, r["arch"], abs(r["prime"]), M, r["zero"],
                 ",".join(map(str, r["prime_terms"])) or "-"))

    sgn = [(r["a"], r["margin"] > 0) for r in rows]
    cross = [ (sgn[i][0], sgn[i+1][0]) for i in range(len(sgn)-1) if sgn[i][1] != sgn[i+1][1] ]
    print("\n  M(a) > 0 anywhere : %s" % any(s for _, s in sgn))
    print("  M(a) < 0 anywhere : %s" % any(not s for _, s in sgn))
    print("  sign changes      : %s" % (cross or "NONE in the measured range"))
    print("  max residual      : %.2e" % max(abs(r["residual"]) for r in rows))

    print("\n--- THE ONE-PRIME BAND a in (2,3): only n=2 contributes ---")
    for r in rows:
        if 2.0 < r["a"] < 3.0:
            print("  a=%.2f  primes=%s  |prime|=%.6f  M=%.6f"
                  % (r["a"], r["prime_terms"], abs(r["prime"]), r["margin"]))

    print("\n--- E4: WINDOW COMPARISON (measured) ---")
    for n in (1, 2, 3, 5):
        w = li_effective_support(n)
        print("  Li index n=%d : 99%%-mass v-width = %.3f" % (n, w))
    print("  support window a=2.0 : v-width = %.3f  (by construction, = 2 log a)" % (2 * math.log(2.0)))
    print("  support window a=4.0 : v-width = %.3f" % (2 * math.log(4.0)))
    print("\nbanked: %s" % BANK)
