# -*- coding: utf-8 -*-
"""W-ORD-CARTOGRAPHY act 4 -- the TRUE quantity: the autocorrelation.

f_a = g_a * g~_a  (multiplicative correlation), so:
    supp(f_a) = [1/a^2, a^2]   -> prime p^k enters at a = sqrt(p^k)
    fhat_a(u) = |ghat_a(u)|^2  -> the zero side is sum |ghat(gamma)|^2 >= 0
This is the Weil-form-compatible element (f = g* conv g).

Constants unchanged: NV=4001 NU=12001 UMAX=600 TOL=1e-3 NGAM=10000.
DISCLAIMED REGISTER: a computation maps and cannot prove. No sign claim.
"""
import math, json, os
import numpy as np
import carto_atlas as C

BANK = r"D:\relay\data\carto_auto.jsonl"


def ghat(v, w, u):
    return C.hhat(v, w, u)          # real, even


def channels_auto(a):
    v, w = C.bump(a)
    dv = np.gradient(v)
    # zero side: sum over +-gamma of |ghat(gamma)|^2
    G = ghat(v, w, C.GAM)
    Z = 2.0 * float(np.sum(G ** 2))
    # pole: fhat(+-i/2) = [int w cosh(v/2)]^2 each
    c = float(np.trapezoid(w * np.cosh(v / 2.0), v))
    P = 2.0 * c * c
    # arch
    U = np.linspace(-C.UMAX, C.UMAX, C.NU)
    GU = ghat(v, w, U)
    A = float(np.trapezoid(GU ** 2 * C.kernel(U), U) / (2.0 * math.pi))
    # prime: additive-side correlation (w conv w) on [-2L, 2L]
    L = math.log(a)
    corr = np.convolve(w, w, mode="full") * float(dv[0])
    vc = np.linspace(-2 * L, 2 * L, corr.size)
    PR, terms = 0.0, []
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        k = 1
        while p ** k <= a * a + 1e-12:
            n = p ** k
            ln = math.log(n)
            if ln <= 2 * L:
                val = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, vc, corr))
                if val:
                    PR += val
                    terms.append(n)
            k += 1
    return dict(a=a, zero=Z, pole=P, arch=A, prime=PR,
                residual=Z - (P - PR + A), prime_terms=terms)


if __name__ == "__main__":
    print("THE TRUE QUANTITY: f_a = g_a * g~_a,  supp = [1/a^2, a^2]")
    print("thresholds: sqrt(2)=%.5f  sqrt(3)=%.5f  2=2  sqrt(5)=%.5f  3=3"
          % (math.sqrt(2), math.sqrt(3), math.sqrt(5)))
    print("\n--- FAR-END RE-VALIDATION ---")
    ok = True
    for a in (1.30, 3.50):
        r = channels_auto(a)
        good = abs(r["residual"]) <= C.TOL
        ok &= good
        print("  a=%.2f  residual = %+.3e   %s" % (a, r["residual"], "PASS" if good else "FAIL"))
    print("  BOTH-ENDS: %s" % ("PASS" if ok else "FAIL"))

    print("\n--- E8/E9: THE AUTOCORRELATION BUDGET ---")
    print("%-8s %12s %8s %11s %11s %11s %8s %s"
          % ("a", "zero=W", ">=0", "pole", "arch", "prime", "pr.shr", "primes"))
    grid = [1.30, 1.35, 1.40, 1.4142, 1.4200, 1.50, 1.60, 1.7000, 1.7321, 1.75,
            1.90, 2.00, 2.05, 2.20, 2.45, 2.65, 3.00, 3.20, 3.50]
    rows = []
    for a in grid:
        r = channels_auto(a)
        geo = abs(r["arch"]) + abs(r["prime"])
        r["prime_share"] = abs(r["prime"]) / geo if geo else 0.0
        rows.append(r)
        with open(BANK, "a", encoding="utf-8") as f:
            f.write(json.dumps(r) + "\n"); f.flush(); os.fsync(f.fileno())
        print("%-8.4f %12.6f %8s %11.6f %11.6f %11.6f %8.4f %s"
              % (a, r["zero"], "yes" if r["zero"] >= 0 else "NO",
                 r["pole"], r["arch"], r["prime"], r["prime_share"],
                 ",".join(map(str, r["prime_terms"])) or "-"))

    print("\n--- E10: THE CC BOUNDARY a = sqrt(2) +- eps ---")
    for a in (1.4100, 1.4130, 1.41421, 1.4150, 1.4180, 1.4250):
        r = channels_auto(a)
        geo = abs(r["arch"]) + abs(r["prime"])
        print("  a=%.5f  a^2=%.5f  prime=%.8f  share=%.6f  primes=%s"
              % (a, a * a, r["prime"], (abs(r["prime"]) / geo if geo else 0.0),
                 r["prime_terms"] or "-"))
    print("\nbanked: %s" % BANK)
