# -*- coding: utf-8 -*-
"""W-ORD-CARTOGRAPHY act 1R — repaired instrument, validation-first.

E1-E4 stand registered VERBATIM at PLACE-papers 0de616d. This file changes
IMPLEMENTATION ONLY: hhat is now one matrix operation instead of a Python loop.

DISCLAIMED REGISTER: a computation maps and cannot prove. No sign claim is made.

INSTRUMENT CONSTANTS -- COMMITTED HERE, BEFORE ANY ANSWER IS SEEN
(per the undefined-requirement loom line: grid choices are instrument constants):
    NV      = 4001      v-grid points on [-log a, log a]
    NU      = 12001     u-grid points
    UMAX    = 600.0     u-range; hhat decays faster than any polynomial,
                        the psi-kernel grows like log u, so the tail is negligible
    TOL     = 1e-3      E2 pass tolerance on the explicit-formula residual
    NGAM    = 10000     banked verified ordinates
Truncation bound for the zero side is computed and printed, not assumed.

Explicit formula, even test function, standard normalisation:
    sum_gamma hhat(gamma)  =  hhat(i/2) + hhat(-i/2)  -  PRIME  +  ARCH   [sign fixed BY the E2 calibration]
"""
import math, os, sys, json, time
import numpy as np

NV, NU, UMAX, TOL, NGAM = 4001, 12001, 600.0, 1e-3, 10000
HERE = os.path.dirname(os.path.abspath(__file__))
GAM = np.load(os.path.join(HERE, "zeta_ordinates.npy"))[:NGAM]
BANK = r"D:\relay\data\carto_atlas.jsonl"

_KERN = None


def kernel(U):
    """Re psi(1/4 + i u/2) - log pi, cached."""
    global _KERN
    if _KERN is None:
        from mpmath import mp, digamma, mpc, re as mre
        mp.dps = 15
        _KERN = np.array([float(mre(digamma(mpc(0.25, uu / 2.0)))) for uu in U]) - math.log(math.pi)
    return _KERN


def bump(a):
    L = math.log(a)
    v = np.linspace(-L, L, NV)
    t = v / L
    w = np.zeros_like(t)
    m = np.abs(t) < 1.0
    w[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))
    w /= np.trapezoid(w, v)
    return v, w


def hhat(v, w, u):
    """ONE matrix operation: cos(u (x) v) @ (w dv).  Vectorised repair."""
    u = np.atleast_1d(np.asarray(u, dtype=np.float64))
    dv = np.gradient(v)
    return np.cos(np.outer(u, v)) @ (w * dv)


def channels(a):
    v, w = bump(a)
    Z = 2.0 * float(np.sum(hhat(v, w, GAM)))                 # zero side
    P = 2.0 * float(np.trapezoid(w * np.cosh(v / 2.0), v))   # pole
    U = np.linspace(-UMAX, UMAX, NU)
    A = float(np.trapezoid(hhat(v, w, U) * kernel(U), U) / (2.0 * math.pi))
    PR, terms = 0.0, []
    L = math.log(a)
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        k = 1
        while p ** k <= a + 1e-12:
            n = p ** k
            ln = math.log(n)
            if ln <= L:
                val = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, v, w))
                if val:
                    PR += val
                    terms.append(n)
            k += 1
    return dict(a=a, zero=Z, pole=P, arch=A, prime=PR,
                residual=Z - (P - PR + A), prime_terms=terms)


def trunc_bound(a):
    """|2 sum_{gamma > T} hhat(gamma)| bound: hhat decays like the bump's transform."""
    v, w = bump(a)
    T = float(GAM[-1])
    tail = hhat(v, w, np.linspace(T, T + 200.0, 401))
    return float(2.0 * np.max(np.abs(tail)) * 200.0)


def bank(rec):
    with open(BANK, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


if __name__ == "__main__":
    print("INSTRUMENT CONSTANTS COMMITTED: NV=%d NU=%d UMAX=%.0f TOL=%.0e NGAM=%d"
          % (NV, NU, UMAX, TOL, NGAM))
    print("ordinates: %d, last = %.4f" % (len(GAM), GAM[-1]))

    t0 = time.time()
    r = channels(1.35)
    dt = time.time() - t0
    tb = trunc_bound(1.35)
    print("\n--- TIMED DRY RUN + E2 VALIDATION ROW (a = 1.35, prime-silent) ---")
    print("  wall time            : %.2f s per a-value" % dt)
    print("  prime terms          : %s  (MUST be empty)" % (r["prime_terms"] or "none"))
    print("  zero side            : %+.8f" % r["zero"])
    print("  pole                 : %+.8f" % r["pole"])
    print("  arch                 : %+.8f" % r["arch"])
    print("  residual Z-(P-PR+A)  : %+.8f" % r["residual"])
    print("  10k truncation bound : %.2e" % tb)
    ok = abs(r["residual"]) <= TOL and not r["prime_terms"]
    print("\n  E2 VERDICT: %s (tol %.0e)" % ("PASS" if ok else "FAIL", TOL))
    if not ok:
        print("  -> FAIL stops the register at the instrument. The discrepancy above IS the report.")
        sys.exit(1)

    print("\n--- E1/E3 SWEEP (validated instrument) ---")
    print("%-6s %13s %13s %13s %13s %11s %s" % ("a", "zero", "pole", "arch", "prime", "resid", "primes"))
    for a in (1.30, 1.35, 1.41, 1.50, 1.70, 1.90, 1.99, 2.00, 2.01, 2.10, 2.40, 2.80, 3.00):
        rr = channels(a)
        bank(rr)
        tot = abs(rr["zero"]) + abs(rr["arch"]) + abs(rr["prime"])
        rr["prime_share"] = abs(rr["prime"]) / tot if tot else 0.0
        print("%-6.2f %13.6f %13.6f %13.6f %13.6f %11.2e %s"
              % (a, rr["zero"], rr["pole"], rr["arch"], rr["prime"], rr["residual"],
                 ",".join(map(str, rr["prime_terms"])) or "-"))
    print("\nbanked: %s" % BANK)
